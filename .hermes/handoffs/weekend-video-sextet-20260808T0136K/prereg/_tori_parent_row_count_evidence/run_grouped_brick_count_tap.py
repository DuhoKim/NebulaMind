#!/usr/bin/env python3
"""Submit one fail-closed grouped per-brick Cut-6 count query."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ASYNC_ENDPOINT = "https://datalab.noirlab.edu/tap/async"
UWS = "{http://www.ivoa.net/xml/UWS/v1.0}"
XLINK = "{http://www.w3.org/1999/xlink}href"
SERVICE_PRESSURE_HTTP = {429, 502, 503, 504}
RESULT_COLUMNS = ["brickid", "n_cut6_dered"]
MAX_RESULT_BYTES = 5_000_000
SUBMISSION_CLOSED = True
CLOSED_MESSAGE = "CLOSED: authorized Tier-3 grouped-count run reached 67/67 coverage; no further POST is permitted"


class HTTPStatusFailure(RuntimeError):
    def __init__(self, code: int, url: str, payload: bytes):
        self.code = code
        self.url = url
        self.payload = payload
        super().__init__(f"HTTP {code} for {url}: {payload[:1000]!r}")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def validate_grouped_count_query(query: str) -> None:
    normalized = " ".join(re.sub(r"--[^\n]*", " ", query).split())
    upper = normalized.upper()
    if not upper.startswith("SELECT ") or upper.count("SELECT ") != 1:
        raise ValueError("query must contain exactly one top-level SELECT")
    if ";" in normalized:
        raise ValueError("multiple statements forbidden")
    if re.search(r"\b(TOP|LIMIT|OFFSET|INTO|UPLOAD|CREATE|DROP|DELETE|UPDATE|INSERT|UNION|HAVING)\b", upper):
        raise ValueError("row/export/mutation construct forbidden")
    if re.search(r"\b(SIN|COS|TAN|ASIN|ACOS|ATAN|RADIANS|DEGREES|COSTHETA)\s*\(", upper):
        raise ValueError("trigonometric construct forbidden")
    if re.search(r"\b(AXIS|THETA|DIPOLE|CHIRALITY|HANDEDNESS|CLOCKWISE|COUNTERCLOCKWISE|CW|CCW|SPIN)\b", upper):
        raise ValueError("directional or signal construct forbidden")
    if re.search(r"\b[TP]\.((RA|DEC|OBJID|LS_ID|TYPE|SHAPE_E1|SHAPE_E2|SHAPE_R|MAG_R|DERED_MAG_R|Z_PHOT_MEDIAN))\s+AS\b", upper):
        raise ValueError("object or position projection forbidden")
    if " FROM " not in upper:
        raise ValueError("FROM clause missing")
    select_clause = normalized[7 : upper.index(" FROM ")]
    if not re.fullmatch(
        r"t\.brickid\s+AS\s+brickid\s*,\s*COUNT\s*\(\s*\*\s*\)\s+AS\s+n_cut6_dered",
        select_clause,
        re.IGNORECASE,
    ):
        raise ValueError("projection must be exactly brickid plus COUNT(*)")
    if len(re.findall(r"\bGROUP\s+BY\s+t\.brickid\b", normalized, re.IGNORECASE)) != 1:
        raise ValueError("group must be exactly GROUP BY t.brickid")
    if len(re.findall(r"\bORDER\s+BY\s+t\.brickid\b", normalized, re.IGNORECASE)) != 1:
        raise ValueError("order must be exactly ORDER BY t.brickid")
    group_tail = re.split(r"\bGROUP\s+BY\s+t\.brickid\b", normalized, flags=re.IGNORECASE)
    if len(group_tail) != 2 or not re.fullmatch(r"\s*ORDER\s+BY\s+t\.brickid\s*", group_tail[1], re.IGNORECASE):
        raise ValueError("group/order tail contains unauthorized terms")
    if "FROM ls_dr10.tractor_s AS t" not in normalized:
        raise ValueError("authorized tractor source missing")
    if "LEFT OUTER JOIN ls_dr10.photo_z AS p" not in normalized:
        raise ValueError("authorized photo-z join missing")


def parse_grouped_result(text: str, lo: int, hi: int) -> list[tuple[int, int]]:
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames != RESULT_COLUMNS:
        raise RuntimeError(f"result columns must be exactly {RESULT_COLUMNS}, got {reader.fieldnames}")
    parsed: list[tuple[int, int]] = []
    previous = lo - 1
    for row in reader:
        if None in row or any(value is None for value in row.values()):
            raise RuntimeError("malformed grouped CSV row")
        try:
            brickid = int(row["brickid"])
            count = int(row["n_cut6_dered"])
        except (TypeError, ValueError) as exc:
            raise RuntimeError("brickid and count must be integer") from exc
        if str(brickid) != row["brickid"].strip() or str(count) != row["n_cut6_dered"].strip():
            raise RuntimeError("brickid and count must use canonical integer encoding")
        if not lo <= brickid <= hi:
            raise RuntimeError(f"brickid {brickid} outside expected range {lo}..{hi}")
        if brickid <= previous:
            raise RuntimeError("brickid rows must be strictly increasing and unique")
        if count <= 0:
            raise RuntimeError("grouped counts must be positive; zero-count bricks must be omitted")
        parsed.append((brickid, count))
        previous = brickid
    if len(parsed) > hi - lo + 1:
        raise RuntimeError("more grouped rows than BRICKID keys")
    return parsed


def record_service_pressure(path: Path, code: int, url: str, attempt: int) -> None:
    event = {
        "detected_utc": utc_now(),
        "signal": f"HTTP_{code}",
        "url": url,
        "attempt": attempt,
        "request_stage": "submission" if url.rstrip("/") == ASYNC_ENDPOINT else "poll_or_retrieval",
    }
    history: list[dict] = []
    if path.exists():
        previous = json.loads(path.read_text())
        history = previous.get("events", [previous])
    atomic_json(path, {**event, "events": history + [event]})


def request(
    url: str,
    *,
    data: dict[str, str] | None = None,
    timeout: int = 120,
    pressure_path: Path | None = None,
    transient_attempts: int = 8,
    retry_seconds: float = 15.0,
) -> tuple[int, str, bytes, dict[str, str]]:
    if data is not None and SUBMISSION_CLOSED:
        raise RuntimeError(CLOSED_MESSAGE)
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    for attempt in range(1, transient_attempts + 1):
        req = urllib.request.Request(url, data=body, headers={"User-Agent": "Tori-grouped-brick-count/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                headers = {key.lower(): value for key, value in response.headers.items()}
                return response.status, response.geturl(), response.read(), headers
        except urllib.error.HTTPError as exc:
            payload = exc.read()
            if exc.code in SERVICE_PRESSURE_HTTP and pressure_path is not None:
                record_service_pressure(pressure_path, exc.code, url, attempt)
            if exc.code not in SERVICE_PRESSURE_HTTP or attempt == transient_attempts:
                raise HTTPStatusFailure(exc.code, url, payload) from exc
            time.sleep(retry_seconds)
    raise AssertionError("unreachable retry loop")


def request_phase(job_url: str, output_dir: Path) -> bytes:
    try:
        return request(job_url + "/phase", pressure_path=output_dir / "service_pressure.json")[2]
    except HTTPStatusFailure as exc:
        if exc.code == 404:
            atomic_json(
                output_dir / "remote_job_lost.json",
                {
                    "detected_utc": utc_now(),
                    "signal": "REMOTE_JOB_HTTP_404",
                    "job_url": job_url,
                    "payload_sha256": sha256_bytes(exc.payload),
                },
            )
        raise


def parse_job(xml_bytes: bytes) -> ET.Element:
    return ET.fromstring(xml_bytes)


def run(
    query_path: Path,
    output_dir: Path,
    lo: int,
    hi: int,
    *,
    poll_seconds: float = 15.0,
    max_wait_seconds: int = 5400,
    resume_job_url: str | None = None,
) -> dict:
    query_bytes = query_path.read_bytes()
    query = query_bytes.decode("utf-8")
    validate_grouped_count_query(query)
    if f"t.brickid BETWEEN {lo} AND {hi}" not in query:
        raise RuntimeError("query range does not match worker custody")
    output_dir.mkdir(parents=True, exist_ok=True)
    pressure_path = output_dir / "service_pressure.json"
    started = utc_now()
    if resume_job_url:
        job_url = resume_job_url.rstrip("/")
        submission = json.loads((output_dir / "submission.json").read_text())
        if submission["query_sha256"] != sha256_bytes(query_bytes) or submission["brickid_range"] != {"lo": lo, "hi": hi}:
            raise RuntimeError("resume submission custody mismatch")
    else:
        protected = [output_dir / name for name in ("submission.json", "receipt.json", "result.csv", "query.adql", "job.xml")]
        occupied = [str(path) for path in protected if path.exists()]
        if occupied:
            raise RuntimeError(f"refuse fresh submission into occupied directory: {occupied}")
        status, final_url, _, headers = request(
            ASYNC_ENDPOINT,
            data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "phase": "RUN", "QUERY": query},
            pressure_path=pressure_path,
        )
        if status not in {200, 201, 303}:
            raise RuntimeError(f"unexpected create status {status}")
        job_url = headers.get("location", final_url).rstrip("/")
        if "/tap/async/" not in job_url:
            raise RuntimeError(f"unexpected job URL {job_url}")
        submission = {
            "recorded_utc": started,
            "endpoint": ASYNC_ENDPOINT,
            "job_url": job_url,
            "query_path": str(query_path.resolve()),
            "query_sha256": sha256_bytes(query_bytes),
            "brickid_range": {"lo": lo, "hi": hi},
            "aggregate_schema": RESULT_COLUMNS,
            "trigonometric_terms": 0,
            "axis_terms": 0,
            "positions": 0,
            "object_rows": 0,
        }
        atomic_json(output_dir / "submission.json", submission)
        (output_dir / "query.adql").write_bytes(query_bytes)

    initial_phase = request_phase(job_url, output_dir).decode().strip()
    if initial_phase == "PENDING":
        request(job_url + "/phase", data={"PHASE": "RUN"}, pressure_path=pressure_path)
    observations: list[dict[str, str]] = []
    history_path = output_dir / "poll_history.json"
    deadline = time.monotonic() + max_wait_seconds
    while True:
        phase = request_phase(job_url, output_dir).decode().strip()
        observations.append({"timestamp_utc": utc_now(), "phase": phase})
        atomic_json(history_path, {"job_url": job_url, "observations": observations})
        if phase == "QUEUED" and not pressure_path.exists():
            atomic_json(pressure_path, {"detected_utc": utc_now(), "job_url": job_url, "signal": "UWS_QUEUED"})
        if phase in {"COMPLETED", "ERROR", "ABORTED"}:
            break
        if time.monotonic() >= deadline:
            atomic_json(
                output_dir / "worker_timeout.json",
                {"recorded_utc": utc_now(), "job_url": job_url, "observed_phase": phase, "max_wait_seconds": max_wait_seconds},
            )
            raise TimeoutError(f"job still {phase} after max wait; job_url={job_url}")
        time.sleep(poll_seconds)

    job_xml = request(job_url, pressure_path=pressure_path)[2]
    root = parse_job(job_xml)
    if phase != "COMPLETED":
        raise RuntimeError(f"job ended {phase}: {job_xml[:4000]!r}")
    result = root.find(f"{UWS}results/{UWS}result")
    if result is None or XLINK not in result.attrib:
        raise RuntimeError("completed job has no result URL")
    result_url = result.attrib[XLINK]
    result_bytes = request(result_url, timeout=300, pressure_path=pressure_path)[2]
    if len(result_bytes) > MAX_RESULT_BYTES:
        raise RuntimeError(f"grouped aggregate response unexpectedly large: {len(result_bytes)} bytes")
    text = result_bytes.decode("utf-8")
    rows = parse_grouped_result(text, lo, hi)
    (output_dir / "result.csv").write_bytes(result_bytes)
    (output_dir / "job.xml").write_bytes(job_xml)
    receipt = {
        "authorization_scope": "exact post-Cut-6 aggregate count per brick; no object rows or geometry",
        "started_utc": started,
        "completed_utc": utc_now(),
        "endpoint": ASYNC_ENDPOINT,
        "job_url": job_url,
        "result_url": result_url,
        "brickid_range": {"lo": lo, "hi": hi},
        "query_sha256": sha256_bytes(query_bytes),
        "result_sha256": sha256_bytes(result_bytes),
        "result_bytes": len(result_bytes),
        "aggregate_group_rows_returned": len(rows),
        "partition_population": sum(count for _, count in rows),
        "result_columns": RESULT_COLUMNS,
        "trigonometric_terms_in_query": 0,
        "axis_terms_in_query": 0,
        "object_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "handedness_spin_cw_ccw_computed": False,
        "sky_statistics_computed_server_side": False,
        "phases": observations,
    }
    atomic_json(output_dir / "receipt.json", receipt)
    return receipt


def main() -> None:
    if SUBMISSION_CLOSED:
        raise SystemExit(CLOSED_MESSAGE)
    parser = argparse.ArgumentParser()
    parser.add_argument("query_path", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--expected-lo", type=int, required=True)
    parser.add_argument("--expected-hi", type=int, required=True)
    parser.add_argument("--poll-seconds", type=float, default=15.0)
    parser.add_argument("--max-wait-seconds", type=int, default=5400)
    parser.add_argument("--resume-job-url")
    args = parser.parse_args()
    receipt = run(
        args.query_path,
        args.output_dir,
        args.expected_lo,
        args.expected_hi,
        poll_seconds=args.poll_seconds,
        max_wait_seconds=args.max_wait_seconds,
        resume_job_url=args.resume_job_url,
    )
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
