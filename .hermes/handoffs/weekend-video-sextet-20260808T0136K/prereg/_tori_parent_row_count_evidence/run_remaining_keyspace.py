#!/usr/bin/env python3
"""Run the remaining DR10-South BRICKID keyspace as one-pass aggregate blocks.

The certified BRICKID 1..121000 artifacts are immutable inputs. This sibling
pass submits only BRICKID 121001..662174 and returns the existing 21 aggregate
columns plus raw/dered Cut 6 in the same one-row response.
"""
from __future__ import annotations

import csv
import fcntl
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
PARTITIONS = ROOT / "partitions"
SCOPE = PARTITIONS / "remaining_121001_662174"
QUERIES = SCOPE / "queries"
RUNS = SCOPE / "runs"
MANIFEST_PATH = SCOPE / "manifest.json"
STATUS_PATH = SCOPE / "status.json"
LOCK_PATH = SCOPE / "orchestrator.lock"
LOG_PATH = SCOPE / "orchestrator.log"
RUNNER_PATH = ROOT / "run_aggregate_tap.py"
RENDERER_PATH = ROOT / "render_remaining_receipt.py"
RECEIPT_PATH = PREREG / "TORI_FULL_KEYSPACE_SWEEP_20260813.md"
BASE_QUERY_PATH = PARTITIONS / "query_111001_121000.adql"
FROZEN_PARENT_RECONSTRUCTION = PARTITIONS / "FINAL_THRESHOLD_INDEPENDENT_RECONSTRUCTION_20260812.json"
FROZEN_CUT6_RECONSTRUCTION = ROOT / "cut6_fixed_000001_121000" / "FINAL_CUT6_INDEPENDENT_RECONSTRUCTION_20260812.json"
FROZEN_PARENT_RECEIPT = PREREG / "TORI_PARENT_ROW_COUNT_20260812.md"
FROZEN_CUT6_RECEIPT = PREREG / "TORI_CUT6_INCLINATION_COUNT_20260812.md"
START = 121001
STOP = 662174
WIDTH = 10000
MAX_CONCURRENT = 3
POLL_SECONDS = 15
MAX_WAIT_SECONDS = 5400
DEADLINE_UTC = "2026-08-12T21:00:00Z"
DEADLINE_KST = "2026-08-13T06:00:00+09:00"
CUT6 = "POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551"
BASE_QUERY_SHA256 = "2744592ec072ab3e9908f320425432bc549cca8effb1daca94624ff3e8c5cf5b"
FROZEN_PARENT_RECEIPT_SHA256 = "df9357085d4cfd35320ab34346a1fb3080dc1e5ba1e3d86e2dc6231dbbf534f3"
FROZEN_CUT6_RECEIPT_SHA256 = "ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651"
FROZEN_PARENT_RECONSTRUCTION_SHA256 = "31e1c4a461e3f3d6ebbbe3d3b21fc9fdb7b9f2b98e61c980540331e9258f24ab"
FROZEN_CUT6_RECONSTRUCTION_SHA256 = "74541ec868f99ef95456d7e3ed89c3101bd9ae99b71ed63b90aa33b919ce487a"
BASE_COLUMNS = [
    "n_join_rows",
    "n_cut1_primary_mask",
    "n_cut2_extended_flux",
    "n_photoz_joined_cut2",
    "n_cut3_photoz",
    "n_cut4_raw_mag",
    "n_cut4_dered_mag",
    "n_cut5_parent_raw",
    "n_cut5_parent_dered",
    "n_raw_allband_nobs",
    "n_dered_allband_nobs",
    "n_raw_allband_ngood",
    "n_dered_allband_ngood",
    "n_raw_allband_ivar",
    "n_dered_allband_ivar",
    "n_raw_shape_valid",
    "n_dered_shape_valid",
    "n_raw_native_covariates",
    "n_dered_native_covariates",
    "n_raw_all_countable_availability",
    "n_dered_all_countable_availability",
]
COLUMNS = BASE_COLUMNS + ["n_cut6_inclination_raw", "n_cut6_inclination_dered"]
BASE_TOTALS = {
    "n_join_rows": 765205959,
    "n_cut1_primary_mask": 674896997,
    "n_cut2_extended_flux": 338508894,
    "n_photoz_joined_cut2": 338508894,
    "n_cut3_photoz": 2618678,
    "n_cut4_raw_mag": 208996,
    "n_cut4_dered_mag": 238922,
    "n_cut5_parent_raw": 185345,
    "n_cut5_parent_dered": 208407,
    "n_raw_allband_nobs": 185345,
    "n_dered_allband_nobs": 208407,
    "n_raw_allband_ngood": 185344,
    "n_dered_allband_ngood": 208406,
    "n_raw_allband_ivar": 185345,
    "n_dered_allband_ivar": 208407,
    "n_raw_shape_valid": 177606,
    "n_dered_shape_valid": 199035,
    "n_raw_native_covariates": 185345,
    "n_dered_native_covariates": 208406,
    "n_raw_all_countable_availability": 177606,
    "n_dered_all_countable_availability": 199034,
    "n_cut6_inclination_raw": 154420,
    "n_cut6_inclination_dered": 171737,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def load_guard():
    spec = importlib.util.spec_from_file_location("aggregate_runner", RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load aggregate runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_aggregate_only


def projected_aliases(query: str) -> list[str]:
    normalized = " ".join(query.split())
    select = normalized[7 : normalized.upper().index(" FROM ")]
    return re.findall(r"\bAS\s+([A-Za-z_][A-Za-z0-9_]*)\b", select, re.IGNORECASE)


def ranges() -> list[tuple[int, int]]:
    result = []
    lo = START
    while lo <= STOP:
        hi = min(lo + WIDTH - 1, STOP)
        result.append((lo, hi))
        lo = hi + 1
    return result


def cut6_expression(alias: str, magnitude: str) -> str:
    return f"""  SUM(CASE
        WHEN t.brick_primary = 1
         AND t.maskbits = 0
         AND t.type <> 'PSF'
         AND t.flux_r > 0
         AND p.z_phot_median >= 0
         AND p.z_phot_median < 0.15
         AND t.{magnitude} < 17.7
         AND t.shape_r > 1.5
         AND {CUT6}
        THEN 1 ELSE 0
      END) AS {alias}"""


def render_query(lo: int, hi: int) -> str:
    if (lo, hi) not in ranges():
        raise ValueError(f"range outside remaining-keyspace manifest: {lo}..{hi}")
    if sha256_path(BASE_QUERY_PATH) != BASE_QUERY_SHA256:
        raise RuntimeError("frozen base full-chain query hash drift")
    base = BASE_QUERY_PATH.read_text()
    from_index = base.upper().index("\nFROM ")
    select = base[:from_index].rstrip()
    from_clause = base[from_index:]
    old_range = "WHERE t.brickid BETWEEN 111001 AND 121000\n"
    if from_clause.count(old_range) != 1:
        raise RuntimeError("frozen base query range marker missing or non-unique")
    from_clause = from_clause.replace(old_range, f"WHERE t.brickid BETWEEN {lo} AND {hi}\n")
    return (
        select
        + ",\n\n"
        + cut6_expression("n_cut6_inclination_raw", "mag_r")
        + ",\n\n"
        + cut6_expression("n_cut6_inclination_dered", "dered_mag_r")
        + from_clause
    )


def validate_query(query: str, lo: int, hi: int) -> None:
    load_guard()(query)
    if (lo, hi) not in ranges() or lo <= 121000 or hi > STOP:
        raise ValueError("query range outside authorization")
    if projected_aliases(query) != COLUMNS:
        raise RuntimeError("remaining-keyspace projection drift")
    if query.count(CUT6) != 2:
        raise RuntimeError("Cut 6 predicate must appear exactly once per branch")
    if f"WHERE t.brickid BETWEEN {lo} AND {hi}\n" not in query:
        raise RuntimeError("query range mismatch")


def verify_frozen_inputs() -> None:
    expected = {
        BASE_QUERY_PATH: BASE_QUERY_SHA256,
        FROZEN_PARENT_RECEIPT: FROZEN_PARENT_RECEIPT_SHA256,
        FROZEN_CUT6_RECEIPT: FROZEN_CUT6_RECEIPT_SHA256,
        FROZEN_PARENT_RECONSTRUCTION: FROZEN_PARENT_RECONSTRUCTION_SHA256,
        FROZEN_CUT6_RECONSTRUCTION: FROZEN_CUT6_RECONSTRUCTION_SHA256,
    }
    for path, digest in expected.items():
        if not path.exists() or sha256_path(path) != digest:
            raise RuntimeError(f"frozen input missing or changed: {path}")
    parent = json.loads(FROZEN_PARENT_RECONSTRUCTION.read_text())
    cut6 = json.loads(FROZEN_CUT6_RECONSTRUCTION.read_text())
    for column in BASE_COLUMNS:
        if parent["totals"][column] != BASE_TOTALS[column]:
            raise RuntimeError(f"frozen parent total drift: {column}")
    for column in ("n_cut5_parent_raw", "n_cut5_parent_dered", "n_cut6_inclination_raw", "n_cut6_inclination_dered"):
        if cut6["totals"][column] != BASE_TOTALS[column]:
            raise RuntimeError(f"frozen Cut 6 total drift: {column}")


def build_manifest(*, dry_run: bool = False) -> dict:
    verify_frozen_inputs()
    entries = []
    for lo, hi in ranges():
        query = render_query(lo, hi)
        validate_query(query, lo, hi)
        query_bytes = query.encode()
        query_path = QUERIES / f"query_{lo:06d}_{hi:06d}.adql"
        run_dir = RUNS / f"run_{lo:06d}_{hi:06d}"
        entries.append(
            {
                "lo": lo,
                "hi": hi,
                "key_count": hi - lo + 1,
                "query_path": str(query_path),
                "query_sha256": sha256_bytes(query_bytes),
                "run_dir": str(run_dir),
            }
        )
        if not dry_run:
            QUERIES.mkdir(parents=True, exist_ok=True)
            if query_path.exists() and query_path.read_bytes() != query_bytes:
                raise RuntimeError(f"refuse overwrite of nonidentical query: {query_path}")
            if not query_path.exists():
                query_path.write_bytes(query_bytes)
    manifest = {
        "created_utc": utc_now(),
        "endpoint": "https://datalab.noirlab.edu/tap/async",
        "scope": "server-side full-chain and Cut 6 aggregate counts only",
        "frozen_preceding_coverage": {"lo": 1, "hi": 121000},
        "coverage": {"lo": START, "hi": STOP},
        "remaining_key_count": STOP - START + 1,
        "partition_count": len(entries),
        "width": WIDTH,
        "columns": COLUMNS,
        "max_concurrent": MAX_CONCURRENT,
        "server_pressure_backoff": "serial",
        "no_requery_at_or_below": 121000,
        "stop_rule": {
            "deadline_utc": DEADLINE_UTC,
            "deadline_kst": DEADLINE_KST,
            "keyspace_exhaustion": STOP,
            "first_of": True,
        },
        "frozen_inputs": {
            str(BASE_QUERY_PATH): BASE_QUERY_SHA256,
            str(FROZEN_PARENT_RECEIPT): FROZEN_PARENT_RECEIPT_SHA256,
            str(FROZEN_CUT6_RECEIPT): FROZEN_CUT6_RECEIPT_SHA256,
            str(FROZEN_PARENT_RECONSTRUCTION): FROZEN_PARENT_RECONSTRUCTION_SHA256,
            str(FROZEN_CUT6_RECONSTRUCTION): FROZEN_CUT6_RECONSTRUCTION_SHA256,
        },
        "entries": entries,
    }
    if dry_run:
        return manifest
    SCOPE.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    if MANIFEST_PATH.exists():
        existing = json.loads(MANIFEST_PATH.read_text())
        existing.pop("created_utc", None)
        comparison = dict(manifest)
        comparison.pop("created_utc", None)
        if existing != comparison:
            raise RuntimeError("refuse overwrite of nonidentical remaining-keyspace manifest")
    else:
        MANIFEST_PATH.write_bytes(encoded)
    return json.loads(MANIFEST_PATH.read_text())


def one_row(path: Path) -> dict[str, int]:
    rows = list(csv.DictReader(path.read_text().splitlines()))
    if len(rows) != 1 or list(rows[0]) != COLUMNS:
        raise RuntimeError(f"expected one exact aggregate row: {path}")
    joined = int(rows[0]["n_join_rows"])
    values = {"n_join_rows": joined}
    for column in COLUMNS[1:]:
        value = rows[0][column]
        if value == "":
            if joined != 0:
                raise RuntimeError(f"blank aggregate {column} with nonzero joined population: {path}")
            values[column] = 0
        else:
            values[column] = int(value)
    return values


def validate_completed(entry: dict) -> dict[str, int] | None:
    tap = Path(entry["run_dir"]) / "tap"
    receipt_path = tap / "receipt.json"
    result_path = tap / "result.csv"
    if not receipt_path.exists() or not result_path.exists():
        return None
    receipt = json.loads(receipt_path.read_text())
    if receipt.get("query_sha256") != entry["query_sha256"]:
        raise RuntimeError(f"receipt/query hash mismatch: {tap}")
    if receipt.get("result_sha256") != sha256_path(result_path):
        raise RuntimeError(f"receipt/result hash mismatch: {tap}")
    if receipt.get("result_row_count") != 1 or receipt.get("result_columns") != COLUMNS:
        raise RuntimeError(f"result shape mismatch: {tap}")
    for name, expected in {
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "sky_statistics_computed": False,
    }.items():
        if receipt.get(name) != expected:
            raise RuntimeError(f"custody violation {name}: {tap}")
    row = one_row(result_path)
    if not 0 <= row["n_cut6_inclination_raw"] <= row["n_cut5_parent_raw"]:
        raise RuntimeError(f"raw Cut 6 monotonicity failure: {tap}")
    if not 0 <= row["n_cut6_inclination_dered"] <= row["n_cut5_parent_dered"]:
        raise RuntimeError(f"dered Cut 6 monotonicity failure: {tap}")
    return row


def landed_entries(manifest: dict) -> list[tuple[dict, dict[str, int]]]:
    result = []
    for entry in manifest["entries"]:
        row = validate_completed(entry)
        if row is not None:
            result.append((entry, row))
    return result


def totals(manifest: dict) -> dict:
    landed = landed_entries(manifest)
    all_totals = dict(BASE_TOTALS)
    for _, row in landed:
        for column in COLUMNS:
            all_totals[column] += row[column]
    contiguous_totals = dict(BASE_TOTALS)
    cursor = START
    contiguous_hi = 121000
    contiguous_partitions = 0
    for entry, row in landed:
        if entry["lo"] != cursor:
            break
        for column in COLUMNS:
            contiguous_totals[column] += row[column]
        contiguous_hi = entry["hi"]
        contiguous_partitions += 1
        cursor = entry["hi"] + 1
    landed_new_keys = sum(entry["key_count"] for entry, _ in landed)
    return {
        "landed_new_partitions": len(landed),
        "landed_new_keys": landed_new_keys,
        "landed_total_keys": 121000 + landed_new_keys,
        "contiguous_new_partitions": contiguous_partitions,
        "contiguous_covered_hi": contiguous_hi,
        "all_landed_totals": all_totals,
        "contiguous_totals": contiguous_totals,
    }


def runner_command(entry: dict) -> list[str]:
    tap = Path(entry["run_dir"]) / "tap"
    command = [
        sys.executable,
        str(RUNNER_PATH),
        entry["query_path"],
        str(tap),
        "--poll-seconds",
        str(POLL_SECONDS),
        "--max-wait-seconds",
        str(MAX_WAIT_SECONDS),
    ]
    submission_path = tap / "submission.json"
    if submission_path.exists():
        submission = json.loads(submission_path.read_text())
        if submission.get("query_sha256") != entry["query_sha256"]:
            raise RuntimeError(f"submission/query hash mismatch: {tap}")
        command += ["--resume-job-url", submission["job_url"]]
    return command


def detect_prior_service_pressure(manifest: dict) -> dict | None:
    events = []
    for entry in manifest["entries"]:
        tap = Path(entry["run_dir"]) / "tap"
        pressure_paths = [tap / "service_pressure.json", *sorted(tap.glob("failed_attempts/*/service_pressure.json"))]
        stderr_paths = [tap / "runner_stderr.log", *sorted(tap.glob("failed_attempts/*/runner_stderr.log"))]
        for pressure_path in pressure_paths:
            if not pressure_path.exists():
                continue
            pressure = json.loads(pressure_path.read_text())
            signal = pressure.get("signal", "unknown")
            if signal in {"HTTP_429", "HTTP_502", "HTTP_503", "HTTP_504", "UWS_QUEUED"}:
                events.append(
                    {
                        "signal": signal,
                        "detected_utc": pressure.get("detected_utc", utc_now()),
                        "source": str(pressure_path),
                    }
                )
        for stderr_path in stderr_paths:
            if not stderr_path.exists():
                continue
            stderr = stderr_path.read_text()
            matches = re.findall(r"HTTP (429|502|503|504)", stderr)
            for code in matches:
                events.append(
                    {
                        "signal": f"HTTP_{code}",
                        "detected_utc": utc_now(),
                        "source": str(stderr_path),
                    }
                )
    if not events:
        return None
    event = events[0]
    return {
        **event,
        "initial_concurrency": 1,
        "action": "resume unchanged manifest serially; preserve landed receipts and existing job URLs",
    }


def archive_lost_attempt(tap: Path, entry: dict, stderr: str) -> Path:
    submission_path = tap / "submission.json"
    if not submission_path.exists():
        raise RuntimeError(f"lost remote job has no submission custody: {tap}")
    if (tap / "receipt.json").exists() or (tap / "result.csv").exists():
        raise RuntimeError(f"refuse archive of landed result: {tap}")
    submission = json.loads(submission_path.read_text())
    if submission.get("query_sha256") != entry["query_sha256"]:
        raise RuntimeError(f"lost-attempt submission/query hash mismatch: {tap}")
    timestamp = utc_now().replace(":", "").replace("-", "")
    archive = tap / "failed_attempts" / f"attempt_{timestamp}"
    suffix = 1
    while archive.exists():
        archive = tap / "failed_attempts" / f"attempt_{timestamp}_{suffix}"
        suffix += 1
    archive.mkdir(parents=True)
    failure_record = {
        "recorded_utc": utc_now(),
        "cause": "remote UWS job URL returned HTTP 404 after an HTTP service-pressure event",
        "recovery": "fresh submission authorized for this unlanded manifest partition only",
        "brickid_range": {"lo": entry["lo"], "hi": entry["hi"]},
        "job_url": submission["job_url"],
        "query_sha256": entry["query_sha256"],
        "stderr_sha256": sha256_bytes(stderr.encode()),
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "sky_statistics_computed": False,
    }
    atomic_json(archive / "failure_record.json", failure_record)
    for name in (
        "submission.json",
        "runner_stdout.log",
        "runner_stderr.log",
        "service_pressure.json",
        "remote_job_lost.json",
    ):
        path = tap / name
        if path.exists():
            shutil.move(str(path), archive / name)
    return archive


def classify_worker_failure(tap: Path, stderr: str) -> str:
    if (tap / "remote_job_lost.json").exists():
        return "remote_job_lost"
    if "job still EXECUTING" in stderr or "job still QUEUED" in stderr:
        return "resume_required"
    if re.search(r"HTTP (429|502|503|504)", stderr):
        return "service_pressure"
    if (tap / "service_pressure.json").exists() and not (tap / "submission.json").exists():
        return "service_pressure_retry"
    return "hard_failure"


def recovery_history(previous_status: dict | None, manifest: dict) -> list[dict]:
    history_path = SCOPE / "failure_recovery_history.json"
    history = json.loads(history_path.read_text()) if history_path.exists() else []
    if previous_status and str(previous_status.get("stop_reason", "")).startswith("partition_failure_"):
        detected = previous_status.get("finished_utc", utc_now())
        if not any(event.get("detected_utc") == detected for event in history):
            history.append(
                {
                    "detected_utc": detected,
                    "stop_reason": previous_status["stop_reason"],
                    "cause": "HTTP 502 Bad Gateway from nginx while polling three existing UWS /phase URLs",
                    "runner_defect": "HTTP 502 was omitted from pressure handling; children exited and the generic hard-failure branch stopped the orchestrator",
                    "landed_partitions_preserved": previous_status.get("totals", {}).get("landed_new_partitions", 0),
                    "recovery_action": "resume same manifest serially; remotely lost job URLs require fresh submissions for unlanded ranges only",
                }
            )
            atomic_json(history_path, history)
    return history


def tap_request(url: str, data: dict[str, str] | None = None) -> str:
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    request = urllib.request.Request(url, data=body, headers={"User-Agent": "Tori-count-custody/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode().strip()


def stop_worker(worker: dict, reason: str) -> dict:
    entry = worker["entry"]
    tap = worker["tap"]
    submission_path = tap / "submission.json"
    job_url = None
    phase_before = "NO_SUBMISSION"
    phase_after = "NO_SUBMISSION"
    abort_error = None
    if submission_path.exists():
        submission = json.loads(submission_path.read_text())
        job_url = submission["job_url"]
        try:
            phase_before = tap_request(job_url + "/phase")
            if phase_before not in {"COMPLETED", "ERROR", "ABORTED"}:
                tap_request(job_url + "/phase", {"PHASE": "ABORT"})
            phase_after = tap_request(job_url + "/phase")
        except Exception as exc:
            abort_error = repr(exc)
    process = worker["process"]
    if process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=15)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=15)
    receipt = {
        "recorded_utc": utc_now(),
        "stop_reason": reason,
        "brickid_range": {"lo": entry["lo"], "hi": entry["hi"]},
        "job_url": job_url,
        "phase_before": phase_before,
        "phase_after": phase_after,
        "abort_error": abort_error,
        "runner_exit_code": process.returncode,
        "query_sha256": entry["query_sha256"],
        "result_rows_exported": 0,
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "sky_statistics_computed": False,
    }
    atomic_json(tap / "intentional_stop_receipt.json", receipt)
    return {**entry, "status": "intentionally_stopped", **receipt}


def render_receipt() -> None:
    result = subprocess.run([sys.executable, str(RENDERER_PATH)], text=True, capture_output=True)
    atomic_json(
        SCOPE / "last_receipt_render.json",
        {"rendered_utc": utc_now(), "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr},
    )
    if result.returncode != 0:
        raise RuntimeError(f"remaining-keyspace receipt renderer failed: {result.stderr}")


def main() -> None:
    SCOPE.mkdir(parents=True, exist_ok=True)
    lock = LOCK_PATH.open("a+")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise SystemExit("another remaining-keyspace orchestrator holds the lock") from exc
    manifest = build_manifest()
    previous_status = json.loads(STATUS_PATH.read_text()) if STATUS_PATH.exists() else None
    prior_pressure = detect_prior_service_pressure(manifest)
    history = recovery_history(previous_status, manifest)
    initial_concurrency = 1 if prior_pressure else MAX_CONCURRENT
    state = {
        "started_utc": utc_now(),
        "updated_utc": utc_now(),
        "manifest_sha256": sha256_path(MANIFEST_PATH),
        "configured_concurrency": MAX_CONCURRENT,
        "active_concurrency": initial_concurrency,
        "deadline_utc": DEADLINE_UTC,
        "deadline_kst": DEADLINE_KST,
        "execution_mode": "detached_background",
        "frozen_preceding_coverage": {"lo": 1, "hi": 121000},
        "results": {},
        "active": {},
        "totals": totals(manifest),
        "recovery_history": history,
    }
    if previous_status is not None:
        state["previous_status_sha256"] = sha256_path(STATUS_PATH)
    if prior_pressure:
        state["service_backoff"] = prior_pressure
    for entry, _ in landed_entries(manifest):
        key = f"{entry['lo']:06d}-{entry['hi']:06d}"
        state["results"][key] = {"status": "completed_existing", **entry}
    atomic_json(STATUS_PATH, state)
    render_receipt()

    pending = [entry for entry in manifest["entries"] if validate_completed(entry) is None]
    active: dict[str, dict] = {}
    target_concurrency = initial_concurrency
    hard_failure = False
    stop_submitting = False

    def persist() -> None:
        state["updated_utc"] = utc_now()
        state["totals"] = totals(manifest)
        atomic_json(STATUS_PATH, state)

    def record_result(key: str, result: dict) -> None:
        state["results"][key] = result
        state["active"].pop(key, None)
        persist()
        render_receipt()
        print(json.dumps(result, sort_keys=True), flush=True)

    while pending or active:
        for key, worker in list(active.items()):
            pressure_path = worker["tap"] / "service_pressure.json"
            if pressure_path.exists() and target_concurrency != 1:
                target_concurrency = 1
                state["active_concurrency"] = 1
                state["service_backoff"] = {
                    "detected_utc": utc_now(),
                    "source": str(pressure_path),
                    "signal": json.loads(pressure_path.read_text()).get("signal", "unknown"),
                    "action": "future submissions reduced to serial; active jobs preserved and never duplicated",
                }
                persist()
            returncode = worker["process"].poll()
            if returncode is None:
                continue
            entry = worker["entry"]
            stderr_path = worker["tap"] / "runner_stderr.log"
            stderr = stderr_path.read_text() if stderr_path.exists() else ""
            result = {
                **entry,
                "started_utc": worker["started_utc"],
                "finished_utc": utc_now(),
                "runner_exit_code": returncode,
            }
            if returncode == 0 and validate_completed(entry) is not None:
                result["status"] = "completed"
            elif classify_worker_failure(worker["tap"], stderr) == "remote_job_lost":
                archive = archive_lost_attempt(worker["tap"], entry, stderr)
                target_concurrency = 1
                state["active_concurrency"] = 1
                result["status"] = "remote_job_lost_resubmit_serial"
                result["failed_attempt_archive"] = str(archive)
                state.setdefault("recovery_actions", []).append(
                    {
                        "recorded_utc": utc_now(),
                        "range": {"lo": entry["lo"], "hi": entry["hi"]},
                        "action": "archived lost UWS job and authorized one fresh serial submission",
                        "archive": str(archive),
                    }
                )
                pending.insert(0, entry)
            elif classify_worker_failure(worker["tap"], stderr) == "resume_required":
                result["status"] = "resume_required"
                pending.insert(0, entry)
            elif classify_worker_failure(worker["tap"], stderr) == "service_pressure":
                if not pressure_path.exists():
                    match = re.search(r"HTTP (429|502|503|504)", stderr)
                    if match is None:
                        raise RuntimeError("service-pressure classification lost its HTTP status")
                    code = match.group(1)
                    atomic_json(
                        pressure_path,
                        {"detected_utc": utc_now(), "signal": f"HTTP_{code}", "stderr_sha256": sha256_bytes(stderr.encode())},
                    )
                target_concurrency = 1
                state["active_concurrency"] = 1
                state["service_backoff"] = {
                    "detected_utc": utc_now(),
                    "source": str(pressure_path),
                    "signal": json.loads(pressure_path.read_text()).get("signal", "HTTP_SERVICE_PRESSURE"),
                    "action": "future submissions reduced to serial; resume existing job URL when present",
                }
                result["status"] = "service_pressure_resume_serial"
                pending.insert(0, entry)
            elif classify_worker_failure(worker["tap"], stderr) == "service_pressure_retry":
                target_concurrency = 1
                state["active_concurrency"] = 1
                result["status"] = "service_pressure_retry_serial"
                pending.insert(0, entry)
            else:
                result["status"] = "failed"
                result["stderr_sha256"] = sha256_bytes(stderr.encode())
                hard_failure = True
                stop_submitting = True
                state["stop_reason"] = f"partition_failure_{key}"
            del active[key]
            record_result(key, result)

        if datetime.now(timezone.utc) >= parse_utc(DEADLINE_UTC):
            stop_submitting = True
            state["stop_reason"] = "deadline_2026_08_13_0600_kst_reached"
            persist()

        if hard_failure:
            stop_submitting = True

        if stop_submitting and active:
            for key, worker in list(active.items()):
                entry = worker["entry"]
                row = validate_completed(entry)
                if row is not None:
                    process = worker["process"]
                    if process.poll() is None:
                        process.terminate()
                        try:
                            process.wait(timeout=15)
                        except subprocess.TimeoutExpired:
                            process.kill()
                            process.wait(timeout=15)
                    result = {
                        **entry,
                        "status": "completed",
                        "started_utc": worker["started_utc"],
                        "finished_utc": utc_now(),
                        "runner_exit_code": process.returncode,
                    }
                else:
                    result = stop_worker(worker, state["stop_reason"])
                del active[key]
                record_result(key, result)

        while pending and not stop_submitting and len(active) < target_concurrency:
            entry = pending.pop(0)
            key = f"{entry['lo']:06d}-{entry['hi']:06d}"
            tap = Path(entry["run_dir"]) / "tap"
            tap.mkdir(parents=True, exist_ok=True)
            stdout_handle = (tap / "runner_stdout.log").open("a")
            stderr_handle = (tap / "runner_stderr.log").open("a")
            process = subprocess.Popen(runner_command(entry), stdout=stdout_handle, stderr=stderr_handle, text=True)
            stdout_handle.close()
            stderr_handle.close()
            active[key] = {"entry": entry, "tap": tap, "process": process, "started_utc": utc_now()}
            state["active"][key] = {"pid": process.pid, "started_utc": active[key]["started_utc"], **entry}
            persist()

        if not pending and not active and not stop_submitting:
            state["stop_reason"] = "remaining_keyspace_exhausted"
            stop_submitting = True
            persist()
        if stop_submitting and not active:
            break
        time.sleep(5)

    state["finished_utc"] = utc_now()
    state["totals"] = totals(manifest)
    persist()
    render_receipt()
    if hard_failure:
        raise SystemExit(state["stop_reason"])
    print(json.dumps({"status": "stopped", "reason": state.get("stop_reason"), "totals": state["totals"]}, sort_keys=True))


if __name__ == "__main__":
    main()
