#!/usr/bin/env python3
"""Submit exactly one aggregate-only ADQL count job and retain no sample rows."""

from __future__ import annotations

import argparse
import csv
import hashlib
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


def record_service_pressure(path: Path, code: int, url: str, attempt: int) -> None:
    event = {
        "detected_utc": utc_now(),
        "signal": f"HTTP_{code}",
        "url": url,
        "attempt": attempt,
        "request_stage": "submission" if url.rstrip("/") == ASYNC_ENDPOINT else "poll_or_retrieval",
    }
    history = []
    if path.exists():
        existing = json.loads(path.read_text())
        history = existing.get("events", [existing])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({**event, "events": history + [event]}, indent=2, sort_keys=True) + "\n")


def request(
    url: str,
    *,
    data: dict[str, str] | None = None,
    timeout: int = 120,
    pressure_path: Path | None = None,
    transient_attempts: int = 8,
    retry_seconds: float = 15.0,
) -> tuple[int, str, bytes, dict[str, str]]:
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    for attempt in range(1, transient_attempts + 1):
        req = urllib.request.Request(url, data=body, headers={"User-Agent": "Tori-count-custody/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                headers = {k.lower(): v for k, v in response.headers.items()}
                return response.status, response.geturl(), response.read(), headers
        except urllib.error.HTTPError as exc:
            payload = exc.read()
            if exc.code in SERVICE_PRESSURE_HTTP and pressure_path is not None:
                record_service_pressure(pressure_path, exc.code, url, attempt)
            if exc.code not in SERVICE_PRESSURE_HTTP or attempt == transient_attempts:
                raise HTTPStatusFailure(exc.code, url, payload) from exc
            time.sleep(retry_seconds)
    raise AssertionError("unreachable HTTP retry loop")


def request_phase(
    job_url: str,
    output_dir: Path,
    *,
    transient_attempts: int = 8,
    retry_seconds: float = 15.0,
) -> tuple[int, str, bytes, dict[str, str]]:
    try:
        return request(
            job_url + "/phase",
            pressure_path=output_dir / "service_pressure.json",
            transient_attempts=transient_attempts,
            retry_seconds=retry_seconds,
        )
    except HTTPStatusFailure as exc:
        if exc.code == 404:
            (output_dir / "remote_job_lost.json").write_text(
                json.dumps(
                    {
                        "detected_utc": utc_now(),
                        "signal": "REMOTE_JOB_HTTP_404",
                        "job_url": job_url,
                        "url": exc.url,
                        "payload_sha256": sha256_bytes(exc.payload),
                    },
                    indent=2,
                    sort_keys=True,
                )
                + "\n"
            )
        raise


def validate_aggregate_only(query: str) -> None:
    normalized = " ".join(re.sub(r"--[^\n]*", " ", query).split())
    upper = normalized.upper()
    if not upper.startswith("SELECT "):
        raise ValueError("query must begin SELECT")
    if not any(token in f" {upper}" for token in (" COUNT(", " SUM(")) or " FROM " not in upper:
        raise ValueError("query must contain COUNT or SUM and FROM")
    if re.search(r"\b(TOP|LIMIT|OFFSET|INTO|UPLOAD|CREATE|DROP|DELETE|UPDATE|INSERT)\b", upper):
        raise ValueError("row/export/mutation construct forbidden")
    if re.search(r"\b(SIN|COS|TAN|ASIN|ACOS|ATAN|RADIANS|DEGREES|COSTHETA)\b", upper):
        raise ValueError("sky-statistic/trigonometric construct forbidden")
    select_clause = normalized[7 : upper.index(" FROM ")]
    expressions: list[str] = []
    start = 0
    depth = 0
    for index, char in enumerate(select_clause):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        elif char == "," and depth == 0:
            expressions.append(select_clause[start:index].strip())
            start = index + 1
    expressions.append(select_clause[start:].strip())
    if depth != 0 or not expressions:
        raise ValueError("malformed SELECT expression list")
    for expression in expressions:
        if not re.match(r"^(COUNT|SUM)\s*\(", expression, re.IGNORECASE):
            raise ValueError(f"non-aggregate projection forbidden: {expression[:80]}")
    if re.search(r"SELECT\s+\*", upper):
        raise ValueError("SELECT * forbidden")
    if " GROUP BY " in upper:
        raise ValueError("GROUP BY forbidden: only one aggregate row is authorized")


def parse_job(xml_bytes: bytes) -> ET.Element:
    return ET.fromstring(xml_bytes)


def child_text(root: ET.Element, name: str) -> str | None:
    node = root.find(UWS + name)
    return node.text if node is not None else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query_path", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--poll-seconds", type=float, default=10.0)
    parser.add_argument("--max-wait-seconds", type=int, default=7200)
    parser.add_argument("--resume-job-url")
    args = parser.parse_args()

    query_bytes = args.query_path.read_bytes()
    query = query_bytes.decode("utf-8")
    validate_aggregate_only(query)
    started = utc_now()
    pressure_path = args.output_dir / "service_pressure.json"
    if args.resume_job_url:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        job_url = args.resume_job_url.rstrip("/")
    else:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        protected = [
            args.output_dir / name
            for name in ("submission.json", "receipt.json", "result.csv", "query.adql", "job.xml")
        ]
        occupied = [str(path) for path in protected if path.exists()]
        if occupied:
            raise RuntimeError(f"refuse fresh submission into occupied output directory: {occupied}")
        try:
            status, final_url, _, headers = request(
                ASYNC_ENDPOINT,
                data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "phase": "RUN", "QUERY": query},
                pressure_path=pressure_path,
            )
        except HTTPStatusFailure:
            raise
        if status not in (200, 201, 303):
            raise RuntimeError(f"unexpected create status {status}")
        job_url = headers.get("location", final_url).rstrip("/")
    if "/tap/async/" not in job_url:
        raise RuntimeError(f"unexpected job URL {job_url}")
    submission = {
        "recorded_utc": started,
        "endpoint": ASYNC_ENDPOINT,
        "job_url": job_url,
        "query_path": str(args.query_path.resolve()),
        "query_sha256": sha256_bytes(query_bytes),
        "resumed": bool(args.resume_job_url),
    }
    (args.output_dir / "submission.json").write_text(json.dumps(submission, indent=2, sort_keys=True) + "\n")

    # Some servers accept phase=RUN at creation but leave the job PENDING.
    _, _, phase_bytes, _ = request_phase(job_url, args.output_dir)
    phase = phase_bytes.decode().strip()
    if phase == "PENDING":
        request(job_url + "/phase", data={"PHASE": "RUN"}, pressure_path=pressure_path)
    elif phase == "QUEUED":
        (args.output_dir / "service_pressure.json").write_text(
            json.dumps(
                {
                    "detected_utc": utc_now(),
                    "job_url": job_url,
                    "signal": "UWS_QUEUED",
                },
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )

    deadline = time.monotonic() + args.max_wait_seconds
    phases: list[dict[str, str]] = []
    while True:
        _, _, phase_bytes, _ = request_phase(job_url, args.output_dir)
        phase = phase_bytes.decode().strip()
        phases.append({"timestamp_utc": utc_now(), "phase": phase})
        if phase == "QUEUED":
            pressure_path = args.output_dir / "service_pressure.json"
            if not pressure_path.exists():
                pressure_path.write_text(
                    json.dumps(
                        {
                            "detected_utc": utc_now(),
                            "job_url": job_url,
                            "signal": "UWS_QUEUED",
                        },
                        indent=2,
                        sort_keys=True,
                    )
                    + "\n"
                )
        if phase in {"COMPLETED", "ERROR", "ABORTED"}:
            break
        if time.monotonic() >= deadline:
            raise TimeoutError(f"job still {phase} after max wait; job_url={job_url}")
        time.sleep(args.poll_seconds)

    _, _, job_xml, _ = request(job_url, pressure_path=pressure_path)
    root = parse_job(job_xml)
    if phase != "COMPLETED":
        raise RuntimeError(f"job ended {phase}: {job_xml[:4000]!r}")
    result = root.find(f"{UWS}results/{UWS}result")
    if result is None or XLINK not in result.attrib:
        raise RuntimeError("completed job has no result URL")
    result_url = result.attrib[XLINK]
    _, _, result_bytes, _ = request(result_url, timeout=300, pressure_path=pressure_path)
    if len(result_bytes) > 100_000:
        raise RuntimeError(f"aggregate response unexpectedly large: {len(result_bytes)} bytes")

    text = result_bytes.decode("utf-8")
    rows = list(csv.DictReader(text.splitlines()))
    if len(rows) != 1:
        raise RuntimeError(f"aggregate query must return exactly one row, got {len(rows)}")
    if any(key is None or not key for key in rows[0]):
        raise RuntimeError("malformed aggregate CSV")

    (args.output_dir / "query.adql").write_bytes(query_bytes)
    (args.output_dir / "result.csv").write_bytes(result_bytes)
    (args.output_dir / "job.xml").write_bytes(job_xml)
    receipt = {
        "authorization_scope": "server-side aggregate parent-row counts only",
        "started_utc": started,
        "completed_utc": utc_now(),
        "endpoint": ASYNC_ENDPOINT,
        "job_url": job_url,
        "result_url": result_url,
        "phases": phases,
        "query_sha256": sha256_bytes(query_bytes),
        "query_bytes": len(query_bytes),
        "result_sha256": sha256_bytes(result_bytes),
        "result_bytes": len(result_bytes),
        "result_row_count": len(rows),
        "result_columns": list(rows[0]),
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "sky_statistics_computed": False,
    }
    (args.output_dir / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"phase": phase, "job_url": job_url, "result": rows[0], "receipt": receipt}, sort_keys=True))


if __name__ == "__main__":
    main()
