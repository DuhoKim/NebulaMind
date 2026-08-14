#!/usr/bin/env python3
"""Slow GET-only scheduler monitor for one recorded footprint-moment canary job."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

EXPECTED_QUERY_SHA256 = "0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98"
EXPECTED_COLUMNS = ["n_cut6_dered", "sum_cos_theta", "sum_cos2_theta"]
EXPECTED_N_LOWER = 2583
EXPECTED_N_UPPER = 26464
PRESSURE_CODES = {429, 502, 503, 504}
UWS = "{http://www.ivoa.net/xml/UWS/v1.0}"
XLINK = "{http://www.w3.org/1999/xlink}href"


class RemoteHTTP(RuntimeError):
    def __init__(self, code: int, url: str, body: bytes):
        self.code = code
        self.url = url
        self.body = body
        super().__init__(f"HTTP {code} for {url}: {body[:1000]!r}")


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def classify_phase(phase: str) -> str:
    if phase in {"PENDING", "QUEUED"}:
        return "WAIT"
    if phase in {"EXECUTING", "COMPLETED"}:
        return "QUEUE_OPEN"
    if phase in {"ERROR", "ABORTED"}:
        return "TERMINAL_FAILURE"
    raise RuntimeError(f"unrecognized UWS phase: {phase}")


def get_bytes(url: str, *, opener: Callable = urllib.request.urlopen, timeout: int = 180) -> bytes:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != "datalab.noirlab.edu":
        raise RuntimeError("GET URL outside Data Lab HTTPS custody")
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Tori-footprint-scheduler-canary-monitor/1.0"},
        method="GET",
    )
    try:
        with opener(request, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        raise RemoteHTTP(exc.code, url, exc.read()) from exc


def validate_result(data: bytes) -> dict[str, object]:
    if len(data) > 100_000:
        raise RuntimeError("canary aggregate response unexpectedly large")
    rows = list(csv.DictReader(data.decode().splitlines()))
    if len(rows) != 1 or list(rows[0]) != EXPECTED_COLUMNS:
        raise RuntimeError("canary must return one exact aggregate row")
    row = rows[0]
    n = int(row["n_cut6_dered"])
    if not EXPECTED_N_LOWER <= n <= EXPECTED_N_UPPER:
        raise RuntimeError(
            f"canary count {n} outside prior-count custody bracket "
            f"{EXPECTED_N_LOWER}..{EXPECTED_N_UPPER}"
        )
    first = float(row["sum_cos_theta"])
    second = float(row["sum_cos2_theta"])
    if not math.isfinite(first) or not math.isfinite(second):
        raise RuntimeError("nonfinite canary moments")
    if abs(first) > n + 1e-7 or second < -1e-7 or second > n + 1e-7:
        raise RuntimeError("canary moment outside unit-vector bounds")
    return {
        "n_cut6_dered": n,
        "sum_cos_theta": row["sum_cos_theta"],
        "sum_cos2_theta": row["sum_cos2_theta"],
    }


def retrieve_completed(output_dir: Path, job_url: str, *, opener: Callable) -> dict[str, object]:
    job_xml = get_bytes(job_url, opener=opener)
    root = ET.fromstring(job_xml)
    result_element = root.find(f"{UWS}results/{UWS}result")
    if result_element is None or XLINK not in result_element.attrib:
        raise RuntimeError("completed canary has no result URL")
    result_url = result_element.attrib[XLINK]
    result_bytes = get_bytes(result_url, opener=opener, timeout=300)
    row = validate_result(result_bytes)
    output_dir.joinpath("job.xml").write_bytes(job_xml)
    output_dir.joinpath("result.csv").write_bytes(result_bytes)
    receipt = {
        "completed_utc": now(),
        "job_url": job_url,
        "result_url": result_url,
        "query_sha256": EXPECTED_QUERY_SHA256,
        "brickid_range": {"lo": 1, "hi": 10000},
        "result_sha256": digest(result_bytes),
        "job_xml_sha256": digest(job_xml),
        "result_row_count": 1,
        "result_columns": EXPECTED_COLUMNS,
        "expected_n_bracket_from_prior_counts": {"lower": EXPECTED_N_LOWER, "upper": EXPECTED_N_UPPER},
        **row,
        "partial_coverage_only": True,
        "full_footprint_variance_verdict": None,
        "full_manifest_auto_launches": 0,
        "object_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "extra_directional_outputs": 0,
    }
    atomic_json(output_dir / "canary_result_receipt.json", receipt)
    return receipt


def monitor(
    output_dir: Path,
    *,
    poll_seconds: float = 300,
    max_wait_seconds: int = 10800,
    opener: Callable = urllib.request.urlopen,
    sleeper: Callable[[float], None] = time.sleep,
) -> dict[str, object]:
    if poll_seconds < 300:
        raise ValueError("canary polling cadence must be at least 300 seconds")
    submission_path = output_dir / "submission.json"
    lifecycle_path = output_dir / "guard_lifecycle.json"
    submission = json.loads(submission_path.read_text())
    lifecycle = json.loads(lifecycle_path.read_text())
    if submission.get("query_sha256") != EXPECTED_QUERY_SHA256:
        raise RuntimeError("canary submission query hash mismatch")
    if lifecycle.get("exception_state") != "CLOSED":
        raise RuntimeError("GET-only monitor requires the submit exception already CLOSED")
    if not lifecycle.get("ordinary_guard_unchanged") or not lifecycle.get(
        "ordinary_guard_verified_rejects_query_after"
    ):
        raise RuntimeError("GET-only monitor requires complete guard restoration proof")
    job_url = str(submission["job_url"]).rstrip("/")
    if "/tap/async/" not in job_url:
        raise RuntimeError("invalid canary job URL")
    history_path = output_dir / "poll_history.json"
    history: list[dict[str, object]] = []
    if history_path.exists():
        existing = json.loads(history_path.read_text())
        history = list(existing.get("observations", []))
    started_monotonic = time.monotonic()
    atomic_json(
        output_dir / "monitor_started.json",
        {
            "started_utc": now(),
            "job_url": job_url,
            "poll_seconds": poll_seconds,
            "max_wait_seconds": max_wait_seconds,
            "get_only": True,
            "abort_on_timeout": False,
            "full_manifest_auto_launches": 0,
        },
    )
    while True:
        try:
            phase_bytes = get_bytes(job_url + "/phase", opener=opener)
        except RemoteHTTP as exc:
            event = {
                "timestamp_utc": now(),
                "kind": "HTTP",
                "http_status": exc.code,
                "url": exc.url,
                "body_sha256": digest(exc.body),
            }
            history.append(event)
            atomic_json(history_path, {"job_url": job_url, "observations": history, "partial": True})
            if exc.code == 404:
                outcome = {
                    "recorded_utc": now(),
                    "monitor_result": "REMOTE_JOB_LOST",
                    "observed_phase": None,
                    "job_url": job_url,
                    "http_status": 404,
                    "replacement_submissions": 0,
                    "abort_requests": 0,
                    "full_manifest_auto_launches": 0,
                }
                atomic_json(output_dir / "remote_job_lost.json", outcome)
                print(json.dumps(outcome, sort_keys=True))
                return outcome
            if exc.code not in PRESSURE_CODES:
                raise
        else:
            phase = phase_bytes.decode().strip().upper()
            classification = classify_phase(phase)
            history.append({"timestamp_utc": now(), "kind": "PHASE", "phase": phase})
            atomic_json(history_path, {"job_url": job_url, "observations": history, "partial": True})
            if classification == "QUEUE_OPEN":
                result_receipt = retrieve_completed(output_dir, job_url, opener=opener) if phase == "COMPLETED" else None
                outcome = {
                    "recorded_utc": now(),
                    "monitor_result": "QUEUE_OPEN",
                    "observed_phase": phase,
                    "job_url": job_url,
                    "poll_count": sum(1 for item in history if item.get("kind") == "PHASE"),
                    "result_landed": result_receipt is not None,
                    "remote_job_left_running": phase == "EXECUTING",
                    "abort_requests": 0,
                    "replacement_submissions": 0,
                    "full_manifest_auto_launches": 0,
                }
                atomic_json(output_dir / "queue_signal.json", outcome)
                atomic_json(history_path, {"job_url": job_url, "observations": history, "partial": False})
                print(json.dumps(outcome, sort_keys=True))
                return outcome
            if classification == "TERMINAL_FAILURE":
                outcome = {
                    "recorded_utc": now(),
                    "monitor_result": "TERMINAL_FAILURE",
                    "observed_phase": phase,
                    "job_url": job_url,
                    "abort_requests": 0,
                    "replacement_submissions": 0,
                    "full_manifest_auto_launches": 0,
                }
                atomic_json(output_dir / "terminal_failure.json", outcome)
                atomic_json(history_path, {"job_url": job_url, "observations": history, "partial": False})
                print(json.dumps(outcome, sort_keys=True))
                return outcome
        elapsed = time.monotonic() - started_monotonic
        if elapsed >= max_wait_seconds:
            last_phase = next(
                (str(item["phase"]) for item in reversed(history) if item.get("kind") == "PHASE"),
                None,
            )
            outcome = {
                "recorded_utc": now(),
                "monitor_result": "PARKED_AFTER_OBSERVATION_WINDOW",
                "observed_phase": last_phase,
                "job_url": job_url,
                "observation_window_seconds": max_wait_seconds,
                "remote_job_left_sitting": True,
                "abort_requests": 0,
                "replacement_submissions": 0,
                "full_manifest_auto_launches": 0,
            }
            atomic_json(output_dir / "parked_pending.json", outcome)
            print(json.dumps(outcome, sort_keys=True))
            return outcome
        sleeper(poll_seconds)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--poll-seconds", type=float, default=300)
    parser.add_argument("--max-wait-seconds", type=int, default=10800)
    args = parser.parse_args()
    monitor(args.output_dir, poll_seconds=args.poll_seconds, max_wait_seconds=args.max_wait_seconds)


if __name__ == "__main__":
    main()
