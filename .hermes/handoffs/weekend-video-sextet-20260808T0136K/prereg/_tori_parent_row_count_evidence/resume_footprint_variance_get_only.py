#!/usr/bin/env python3
"""GET-only continuation for the one already-submitted footprint-variance UWS job."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCOPE = ROOT / "footprint_variance_20260813"
OUTPUT_DIR = SCOPE / "run"
SUBMISSION = OUTPUT_DIR / "submission.json"
QUERY_SOURCE = SCOPE / "query.adql"
ALLOWED_JOB_URL = "https://datalab.noirlab.edu/tap/async/v0d4e15lm8hkz7zv"
EXPECTED_QUERY_SHA256 = "5d4c7812331419eff0ec7dca4e40f690203cb94cc71b6309d7b8694299249ff1"
EXPECTED_COLUMNS = ["n_cut6_dered", "mean_cos_theta", "var_pop_cos_theta"]
EXPECTED_POPULATION_COUNT = 832393
UWS = "{http://www.ivoa.net/xml/UWS/v1.0}"
XLINK = "{http://www.w3.org/1999/xlink}href"
TRANSIENT = {429, 502, 503, 504}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def get(url: str, *, timeout: int = 300, attempts: int = 8, retry_seconds: float = 15.0) -> bytes:
    if not (url == ALLOWED_JOB_URL or url.startswith(ALLOWED_JOB_URL + "/")):
        raise RuntimeError(f"GET-only continuation refuses URL outside recorded job: {url}")
    for attempt in range(1, attempts + 1):
        request = urllib.request.Request(url, headers={"User-Agent": "Tori-variance-get-only/1.0"}, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            payload = exc.read()
            if exc.code not in TRANSIENT or attempt == attempts:
                raise RuntimeError(f"GET HTTP {exc.code} for {url}: {payload[:1000]!r}") from exc
            time.sleep(retry_seconds)
    raise AssertionError("unreachable")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--poll-seconds", type=float, default=30.0)
    parser.add_argument("--max-wait-seconds", type=int, default=7200)
    args = parser.parse_args()

    submission = json.loads(SUBMISSION.read_text())
    if submission["job_url"] != ALLOWED_JOB_URL:
        raise RuntimeError("recorded job URL drift")
    if submission["submission_attempts"] != 1 or submission["submission_limit"] != 1:
        raise RuntimeError("one-submission custody drift")
    query_bytes = QUERY_SOURCE.read_bytes()
    if sha(query_bytes) != EXPECTED_QUERY_SHA256 or submission["query_sha256"] != EXPECTED_QUERY_SHA256:
        raise RuntimeError("query hash drift")

    deadline = time.monotonic() + args.max_wait_seconds
    phases: list[dict[str, str]] = []
    while True:
        phase = get(ALLOWED_JOB_URL + "/phase").decode().strip()
        phases.append({"timestamp_utc": utc_now(), "phase": phase})
        if phase in {"COMPLETED", "ERROR", "ABORTED"}:
            break
        if time.monotonic() >= deadline:
            atomic_json(OUTPUT_DIR / "get_only_poll.json", {"job_url": ALLOWED_JOB_URL, "phases": phases, "timed_out_utc": utc_now()})
            raise TimeoutError(f"recorded job still {phase}; no query was submitted")
        time.sleep(args.poll_seconds)

    job_xml = get(ALLOWED_JOB_URL)
    OUTPUT_DIR.joinpath("job.xml").write_bytes(job_xml)
    if phase != "COMPLETED":
        raise RuntimeError(f"recorded job ended {phase}: {job_xml[:4000]!r}")
    root = ET.fromstring(job_xml)
    result = root.find(f"{UWS}results/{UWS}result")
    if result is None or XLINK not in result.attrib:
        raise RuntimeError("completed recorded job has no result URL")
    result_url = result.attrib[XLINK]
    result_bytes = get(result_url)
    if len(result_bytes) > 100_000:
        raise RuntimeError("aggregate response unexpectedly large")
    rows = list(csv.DictReader(result_bytes.decode("utf-8").splitlines()))
    if len(rows) != 1 or list(rows[0]) != EXPECTED_COLUMNS:
        raise RuntimeError("expected one exact three-column aggregate row")
    n = int(rows[0]["n_cut6_dered"])
    mean = float(rows[0]["mean_cos_theta"])
    variance = float(rows[0]["var_pop_cos_theta"])
    if n != EXPECTED_POPULATION_COUNT:
        raise RuntimeError(f"Cut-6 population mismatch: {n} != {EXPECTED_POPULATION_COUNT}")
    if not (math.isfinite(mean) and -1 <= mean <= 1):
        raise RuntimeError(f"invalid mean: {mean}")
    if not (math.isfinite(variance) and 0 <= variance <= 1):
        raise RuntimeError(f"invalid population variance: {variance}")

    OUTPUT_DIR.joinpath("query.adql").write_bytes(query_bytes)
    OUTPUT_DIR.joinpath("result.csv").write_bytes(result_bytes)
    receipt = {
        "authorization_scope": "one server-side aggregate geometry check over the exact dered Cut-6 population",
        "started_utc": submission["recorded_utc"],
        "completed_utc": utc_now(),
        "endpoint": submission["endpoint"],
        "job_url": ALLOWED_JOB_URL,
        "result_url": result_url,
        "phases": phases,
        "query_sha256": EXPECTED_QUERY_SHA256,
        "result_sha256": sha(result_bytes),
        "job_xml_sha256": sha(job_xml),
        "result_row_count": 1,
        "result_columns": EXPECTED_COLUMNS,
        "population_count_expected": EXPECTED_POPULATION_COUNT,
        "population_count_returned": n,
        "mean_cos_theta": mean,
        "var_pop_cos_theta": variance,
        "threshold": 0.15,
        "threshold_met": variance >= 0.15,
        "submission_attempts": 1,
        "continuation_mode": "GET_ONLY_EXISTING_JOB",
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "handedness_joined_or_referenced": False,
        "directional_outputs_beyond_authorized_moments": 0,
    }
    atomic_json(OUTPUT_DIR / "receipt.json", receipt)
    atomic_json(OUTPUT_DIR / "get_only_poll.json", {"job_url": ALLOWED_JOB_URL, "phases": phases, "completed_utc": receipt["completed_utc"]})
    print(json.dumps({"phase": phase, "job_url": ALLOWED_JOB_URL, "result": rows[0]}, sort_keys=True))


if __name__ == "__main__":
    main()
