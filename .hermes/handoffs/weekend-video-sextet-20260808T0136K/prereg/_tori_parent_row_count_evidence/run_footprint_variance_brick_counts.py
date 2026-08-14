#!/usr/bin/env python3
"""Run exact post-Cut-6 counts grouped by brick over the frozen 67 ranges."""
from __future__ import annotations

import fcntl
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
SCOPE = ROOT / "footprint_variance_brick_counts_20260814"
QUERIES = SCOPE / "queries"
RUNS = SCOPE / "runs"
MANIFEST_PATH = SCOPE / "manifest.json"
STATUS_PATH = SCOPE / "status.json"
FINAL_OUTCOME_PATH = SCOPE / "FINAL_COUNTS_OUTCOME.json"
LOCK_PATH = SCOPE / "orchestrator.lock"
WORKER_PATH = ROOT / "run_grouped_brick_count_tap.py"
ORDINARY_GUARD_PATH = ROOT / "run_aggregate_tap.py"
SOURCE_MANIFEST_PATH = ROOT / "footprint_variance_partitioned_20260813" / "manifest.json"
STATIC_PRODUCT_PATH = SCOPE / "static" / "survey-bricks-dr10-south.fits.gz"
AUTHORIZATION_PATH = SCOPE / "LAUNCH_AUTHORIZATION.json"
START = 1
STOP = 662174
WIDTH = 10000
MAX_CONCURRENT = 3
POLL_SECONDS = 15
MAX_WAIT_SECONDS = 5400
QUEUE_STALL_SECONDS = 1800
SUBMISSION_CLOSED = True
CLOSED_MESSAGE = "CLOSED: authorized Tier-3 grouped-count run reached 67/67 coverage; no further orchestration is permitted"
DEADLINE_UTC = "2026-08-14T13:00:00Z"
DEADLINE_KST = "2026-08-14T22:00:00+09:00"
EXPECTED_POPULATION = 832393
SOURCE_MANIFEST_SHA256 = "076131fff15c0338cce689b4742cd64631f855e2a04398dc2d527b0962edda93"
ORDINARY_GUARD_SHA256 = "228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51"
STATIC_PRODUCT_SHA256 = "863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a"
RESULT_COLUMNS = ["brickid", "n_cut6_dered"]
CUT6 = "POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551"
REQUIRED_PREDICATES = [
    "t.brick_primary = 1",
    "t.maskbits = 0",
    "t.type <> 'PSF'",
    "t.flux_r > 0",
    "p.z_phot_median >= 0",
    "p.z_phot_median < 0.15",
    "t.dered_mag_r < 17.7",
    "t.shape_r > 1.5",
    CUT6,
]
AUDIT_HASHES = {
    PREREG / "GORU_VARIANCE_APPROACH_AUDIT.md": "3dba46c58bc2c01920c22af273f36cbbe1358e5c1375b9e8b23aa9c49acf0a15",
    PREREG / "KUN_VARIANCE_APPROACH_AUDIT.md": "e14c76a4bf45f8d3535ff50d5f761ddc9af3de4c4f538a660b5653cfc1a3dc17",
    PREREG / "LANA_VARIANCE_APPROACH_AUDIT.md": "04738a649b9d0533ce6070a5b8327839de7878250f092c517e950bba248b2c44",
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


def load_worker():
    spec = importlib.util.spec_from_file_location("grouped_worker", WORKER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load grouped-count worker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_frozen_inputs(*, require_static: bool) -> None:
    expected = {
        SOURCE_MANIFEST_PATH: SOURCE_MANIFEST_SHA256,
        ORDINARY_GUARD_PATH: ORDINARY_GUARD_SHA256,
        **AUDIT_HASHES,
    }
    if require_static:
        expected[STATIC_PRODUCT_PATH] = STATIC_PRODUCT_SHA256
    for path, digest in expected.items():
        if not path.exists() or sha256_path(path) != digest:
            raise RuntimeError(f"frozen input missing or changed: {path}")
    if not AUTHORIZATION_PATH.exists():
        raise RuntimeError("launch authorization missing")
    authorization = json.loads(AUTHORIZATION_PATH.read_text())
    if authorization["guard_contract"]["ordinary_guard_state"] != "ARMED_AND_BYTE_IDENTICAL":
        raise RuntimeError("ordinary guard not frozen armed")
    if authorization["guard_contract"]["exception_opened"] is not False:
        raise RuntimeError("guard exception must remain closed")


def ranges() -> list[tuple[int, int]]:
    verify_frozen_inputs(require_static=False)
    source = json.loads(SOURCE_MANIFEST_PATH.read_text())
    result = [(int(entry["lo"]), int(entry["hi"])) for entry in source["entries"]]
    if len(result) != 67 or result[0] != (START, 10000) or result[-1] != (660001, STOP):
        raise RuntimeError("source 67-range manifest shape drift")
    cursor = START
    for lo, hi in result:
        if lo != cursor or hi != min(lo + WIDTH - 1, STOP):
            raise RuntimeError("source ranges are not contiguous canonical 10,000-key partitions")
        cursor = hi + 1
    if cursor != STOP + 1:
        raise RuntimeError("source manifest does not exhaust frozen BRICKID keyspace")
    return result


def render_query(lo: int, hi: int) -> str:
    if (lo, hi) not in ranges():
        raise ValueError(f"range outside frozen manifest: {lo}..{hi}")
    return f"""SELECT
  t.brickid AS brickid,
  COUNT(*) AS n_cut6_dered
FROM ls_dr10.tractor_s AS t
LEFT OUTER JOIN ls_dr10.photo_z AS p
  ON t.ls_id = p.ls_id
 AND t.release = p.release
 AND t.brickid = p.brickid
 AND t.objid = p.objid
WHERE t.brickid BETWEEN {lo} AND {hi}
  AND t.brick_primary = 1
  AND t.maskbits = 0
  AND t.type <> 'PSF'
  AND t.flux_r > 0
  AND p.z_phot_median >= 0
  AND p.z_phot_median < 0.15
  AND t.dered_mag_r < 17.7
  AND t.shape_r > 1.5
  AND {CUT6}
GROUP BY t.brickid
ORDER BY t.brickid
"""


def validate_query(query: str, lo: int, hi: int) -> None:
    load_worker().validate_grouped_count_query(query)
    if (lo, hi) not in ranges():
        raise ValueError("range outside frozen manifest")
    if f"t.brickid BETWEEN {lo} AND {hi}" not in query:
        raise RuntimeError("query range mismatch")
    for predicate in REQUIRED_PREDICATES:
        if query.count(predicate) != 1:
            raise RuntimeError(f"frozen predicate missing or repeated: {predicate}")
    normalized = " ".join(query.split()).upper()
    if normalized.count("GROUP BY T.BRICKID") != 1 or normalized.count("ORDER BY T.BRICKID") != 1:
        raise RuntimeError("group/order clause drift")
    if re.search(r"\b(SIN|COS|TAN|ASIN|ACOS|ATAN|RADIANS|DEGREES|COSTHETA)\s*\(", normalized):
        raise RuntimeError("trigonometry reached server query")
    if re.search(r"\b(AXIS|THETA|DIPOLE|CHIRALITY|HANDEDNESS|CLOCKWISE|COUNTERCLOCKWISE|CW|CCW|SPIN)\b", normalized):
        raise RuntimeError("directional or signal term reached server query")
    if "T.RA" in normalized or "T.DEC" in normalized:
        raise RuntimeError("position term reached server query")


def build_manifest(*, dry_run: bool = False) -> dict:
    verify_frozen_inputs(require_static=False)
    entries = []
    for lo, hi in ranges():
        query = render_query(lo, hi)
        validate_query(query, lo, hi)
        encoded = query.encode()
        query_path = QUERIES / f"query_{lo:06d}_{hi:06d}.adql"
        run_dir = RUNS / f"run_{lo:06d}_{hi:06d}"
        entries.append(
            {
                "lo": lo,
                "hi": hi,
                "key_count": hi - lo + 1,
                "query_path": str(query_path),
                "query_sha256": sha256_bytes(encoded),
                "run_dir": str(run_dir),
            }
        )
        if not dry_run:
            QUERIES.mkdir(parents=True, exist_ok=True)
            if query_path.exists() and query_path.read_bytes() != encoded:
                raise RuntimeError(f"refuse overwrite of nonidentical query: {query_path}")
            if not query_path.exists():
                query_path.write_bytes(encoded)
    manifest = {
        "created_utc": utc_now(),
        "endpoint": "https://datalab.noirlab.edu/tap/async",
        "scope": "exact post-Cut-6 aggregate count per BRICKID; no server-side geometry",
        "coverage": {"lo": START, "hi": STOP},
        "partition_count": len(entries),
        "width": WIDTH,
        "columns": RESULT_COLUMNS,
        "max_concurrent": MAX_CONCURRENT,
        "service_pressure_backoff": "serial",
        "queue_stall_seconds": QUEUE_STALL_SECONDS,
        "ordinary_guard_state": "ARMED_AND_BYTE_IDENTICAL",
        "ordinary_guard_sha256": ORDINARY_GUARD_SHA256,
        "guard_exception_opened": False,
        "source_range_manifest_sha256": SOURCE_MANIFEST_SHA256,
        "static_product_sha256": STATIC_PRODUCT_SHA256,
        "expected_population": EXPECTED_POPULATION,
        "stop_rule": {
            "coverage": True,
            "service_pressure_judgement": True,
            "deadline_utc": DEADLINE_UTC,
            "deadline_kst": DEADLINE_KST,
            "first_of": True,
        },
        "authorization_sha256": sha256_path(AUTHORIZATION_PATH),
        "entries": entries,
    }
    if dry_run:
        return manifest
    encoded_manifest = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    if MANIFEST_PATH.exists():
        existing = json.loads(MANIFEST_PATH.read_text())
        comparison = dict(manifest)
        existing.pop("created_utc", None)
        comparison.pop("created_utc", None)
        if existing != comparison:
            raise RuntimeError("refuse overwrite of nonidentical grouped-count manifest")
    else:
        MANIFEST_PATH.write_bytes(encoded_manifest)
    return json.loads(MANIFEST_PATH.read_text())


def validate_completed(entry: dict) -> list[tuple[int, int]] | None:
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
    if receipt.get("result_columns") != RESULT_COLUMNS:
        raise RuntimeError(f"result columns drift: {tap}")
    if receipt.get("brickid_range") != {"lo": entry["lo"], "hi": entry["hi"]}:
        raise RuntimeError(f"result range drift: {tap}")
    for name, expected in {
        "trigonometric_terms_in_query": 0,
        "axis_terms_in_query": 0,
        "object_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "handedness_spin_cw_ccw_computed": False,
        "sky_statistics_computed_server_side": False,
    }.items():
        if receipt.get(name) != expected:
            raise RuntimeError(f"boundary violation {name}: {tap}")
    rows = load_worker().parse_grouped_result(result_path.read_text(), entry["lo"], entry["hi"])
    if receipt.get("aggregate_group_rows_returned") != len(rows):
        raise RuntimeError(f"group-row count mismatch: {tap}")
    if receipt.get("partition_population") != sum(count for _, count in rows):
        raise RuntimeError(f"partition population mismatch: {tap}")
    return rows


def coverage_summary(manifest: dict) -> dict:
    all_rows: list[tuple[int, int]] = []
    completed = 0
    for entry in manifest["entries"]:
        rows = validate_completed(entry)
        if rows is None:
            continue
        completed += 1
        all_rows.extend(rows)
    ids = [brickid for brickid, _ in all_rows]
    if len(ids) != len(set(ids)):
        raise RuntimeError("duplicate BRICKID across partition results")
    return {
        "completed_partitions": completed,
        "partition_count": len(manifest["entries"]),
        "aggregate_group_rows": len(all_rows),
        "population": sum(count for _, count in all_rows),
        "full_coverage": completed == len(manifest["entries"]),
    }


def runner_command(entry: dict) -> list[str]:
    tap = Path(entry["run_dir"]) / "tap"
    command = [
        sys.executable,
        str(WORKER_PATH),
        entry["query_path"],
        str(tap),
        "--expected-lo",
        str(entry["lo"]),
        "--expected-hi",
        str(entry["hi"]),
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


def tap_request(url: str, data: dict[str, str] | None = None) -> str:
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    request = urllib.request.Request(url, data=body, headers={"User-Agent": "Tori-grouped-brick-orchestrator/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode().strip()


def latest_phase(tap: Path) -> str | None:
    history_path = tap / "poll_history.json"
    if not history_path.exists():
        return None
    history = json.loads(history_path.read_text())
    observations = history.get("observations", [])
    return observations[-1]["phase"] if observations else None


def archive_lost_attempt(tap: Path, entry: dict) -> Path:
    if (tap / "receipt.json").exists() or (tap / "result.csv").exists():
        raise RuntimeError("refuse archive of landed grouped result")
    timestamp = utc_now().replace(":", "").replace("-", "")
    archive = tap / "failed_attempts" / f"attempt_{timestamp}"
    archive.mkdir(parents=True)
    atomic_json(
        archive / "failure_record.json",
        {
            "recorded_utc": utc_now(),
            "cause": "remote UWS job URL returned HTTP 404 before any grouped result landed",
            "recovery": "fresh serial submission for the same unlanded manifest partition",
            "brickid_range": {"lo": entry["lo"], "hi": entry["hi"]},
            "query_sha256": entry["query_sha256"],
            "object_rows": 0,
            "positions": 0,
        },
    )
    for name in (
        "submission.json",
        "query.adql",
        "poll_history.json",
        "runner_stdout.log",
        "runner_stderr.log",
        "service_pressure.json",
        "remote_job_lost.json",
        "worker_timeout.json",
        "job.xml",
    ):
        path = tap / name
        if path.exists():
            shutil.move(str(path), archive / name)
    return archive


def stop_worker(worker: dict, reason: str) -> dict:
    entry = worker["entry"]
    tap = worker["tap"]
    process = worker["process"]
    job_url = None
    phase_before = "NO_SUBMISSION"
    phase_after = "NO_SUBMISSION"
    abort_error = None
    submission_path = tap / "submission.json"
    if submission_path.exists():
        job_url = json.loads(submission_path.read_text())["job_url"]
        try:
            phase_before = tap_request(job_url + "/phase")
            if phase_before not in {"COMPLETED", "ERROR", "ABORTED"}:
                tap_request(job_url + "/phase", {"PHASE": "ABORT"})
            phase_after = tap_request(job_url + "/phase")
        except Exception as exc:
            abort_error = repr(exc)
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
        "aggregate_group_rows_landed": 0,
        "object_rows": 0,
        "positions": 0,
    }
    atomic_json(tap / "intentional_stop_receipt.json", receipt)
    return receipt


def main() -> None:
    if SUBMISSION_CLOSED:
        raise SystemExit(CLOSED_MESSAGE)
    verify_frozen_inputs(require_static=True)
    SCOPE.mkdir(parents=True, exist_ok=True)
    lock = LOCK_PATH.open("a+")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise SystemExit("another grouped-count orchestrator holds the lock") from exc
    manifest = build_manifest()
    previous_status = json.loads(STATUS_PATH.read_text()) if STATUS_PATH.exists() else None
    summary = coverage_summary(manifest)
    state = {
        "started_utc": utc_now(),
        "updated_utc": utc_now(),
        "manifest_sha256": sha256_path(MANIFEST_PATH),
        "authorization_sha256": sha256_path(AUTHORIZATION_PATH),
        "ordinary_guard_sha256": sha256_path(ORDINARY_GUARD_PATH),
        "ordinary_guard_state": "ARMED_AND_BYTE_IDENTICAL",
        "guard_exception_opened": False,
        "configured_concurrency": MAX_CONCURRENT,
        "active_concurrency": MAX_CONCURRENT,
        "deadline_utc": DEADLINE_UTC,
        "deadline_kst": DEADLINE_KST,
        "queue_stall_seconds": QUEUE_STALL_SECONDS,
        "results": {},
        "active": {},
        "coverage": summary,
    }
    if previous_status is not None:
        state["previous_status_sha256"] = sha256_path(STATUS_PATH)
    for entry in manifest["entries"]:
        if validate_completed(entry) is not None:
            key = f"{entry['lo']:06d}-{entry['hi']:06d}"
            state["results"][key] = {"status": "completed_existing", **entry}
    atomic_json(STATUS_PATH, state)

    pending = [entry for entry in manifest["entries"] if validate_completed(entry) is None]
    active: dict[str, dict] = {}
    target_concurrency = MAX_CONCURRENT
    stop_reason: str | None = None
    last_scheduler_progress = time.monotonic()

    def persist() -> None:
        state["updated_utc"] = utc_now()
        state["active_concurrency"] = target_concurrency
        state["coverage"] = coverage_summary(manifest)
        atomic_json(STATUS_PATH, state)

    while pending or active:
        for key, worker in list(active.items()):
            tap = worker["tap"]
            if (tap / "service_pressure.json").exists() and target_concurrency != 1:
                target_concurrency = 1
                state["service_backoff"] = {
                    "detected_utc": utc_now(),
                    "source": str(tap / "service_pressure.json"),
                    "action": "future submissions reduced to serial; active jobs preserved",
                }
                persist()
            phase = latest_phase(tap)
            if phase == "EXECUTING":
                last_scheduler_progress = time.monotonic()
            returncode = worker["process"].poll()
            if returncode is None:
                continue
            entry = worker["entry"]
            result = {
                **entry,
                "started_utc": worker["started_utc"],
                "finished_utc": utc_now(),
                "runner_exit_code": returncode,
            }
            rows = validate_completed(entry)
            stderr_path = tap / "runner_stderr.log"
            stderr = stderr_path.read_text() if stderr_path.exists() else ""
            if returncode == 0 and rows is not None:
                result["status"] = "completed"
                result["aggregate_group_rows"] = len(rows)
                result["partition_population"] = sum(count for _, count in rows)
                last_scheduler_progress = time.monotonic()
            elif (tap / "remote_job_lost.json").exists():
                archive = archive_lost_attempt(tap, entry)
                target_concurrency = 1
                result["status"] = "remote_job_lost_resubmit_serial"
                result["failed_attempt_archive"] = str(archive)
                pending.insert(0, entry)
            elif phase in {"ERROR", "ABORTED"}:
                result["status"] = f"terminal_{phase.lower()}"
                result["stderr_sha256"] = sha256_bytes(stderr.encode())
                stop_reason = f"partition_terminal_{phase.lower()}_{key}"
            elif (tap / "service_pressure.json").exists() and not (tap / "worker_timeout.json").exists():
                target_concurrency = 1
                result["status"] = "service_pressure_resume_serial"
                pending.insert(0, entry)
            else:
                result["status"] = "failed"
                result["stderr_sha256"] = sha256_bytes(stderr.encode())
                stop_reason = f"partition_failure_{key}"
            del active[key]
            state["active"].pop(key, None)
            state["results"][key] = result
            persist()
            print(json.dumps(result, sort_keys=True), flush=True)

        if datetime.now(timezone.utc) >= parse_utc(DEADLINE_UTC):
            stop_reason = "deadline_2026_08_14_2200_kst_reached"

        phases = [latest_phase(worker["tap"]) for worker in active.values()]
        if active and phases and all(phase in {"PENDING", "QUEUED"} for phase in phases):
            if time.monotonic() - last_scheduler_progress >= QUEUE_STALL_SECONDS:
                stop_reason = "queue_stalled_1800_seconds"

        if stop_reason is not None and active:
            for key, worker in list(active.items()):
                entry = worker["entry"]
                rows = validate_completed(entry)
                if rows is not None:
                    result = {**entry, "status": "completed_before_stop", "finished_utc": utc_now()}
                else:
                    result = {**entry, "status": "intentionally_stopped", **stop_worker(worker, stop_reason)}
                del active[key]
                state["active"].pop(key, None)
                state["results"][key] = result
                persist()

        while pending and stop_reason is None and len(active) < target_concurrency:
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

        if not pending and not active and stop_reason is None:
            stop_reason = "full_manifest_coverage"
        if stop_reason is not None and not active:
            break
        time.sleep(5)

    final_summary = coverage_summary(manifest)
    if final_summary["full_coverage"] and final_summary["population"] != EXPECTED_POPULATION:
        stop_reason = "full_coverage_population_mismatch"
    state["stop_reason"] = stop_reason
    state["finished_utc"] = utc_now()
    state["coverage"] = final_summary
    persist()
    outcome = {
        "recorded_utc": utc_now(),
        "stop_reason": stop_reason,
        "coverage": final_summary,
        "expected_population": EXPECTED_POPULATION,
        "population_matches_frozen_total": final_summary["population"] == EXPECTED_POPULATION,
        "manifest_sha256": sha256_path(MANIFEST_PATH),
        "ordinary_guard_sha256": sha256_path(ORDINARY_GUARD_PATH),
        "ordinary_guard_state": "ARMED_AND_BYTE_IDENTICAL",
        "guard_exception_opened": False,
        "static_product_sha256": sha256_path(STATIC_PRODUCT_PATH),
        "trigonometric_terms_in_queries": 0,
        "axis_terms_in_queries": 0,
        "object_rows": 0,
        "positions": 0,
    }
    atomic_json(FINAL_OUTCOME_PATH, outcome)
    print(json.dumps(outcome, sort_keys=True))


if __name__ == "__main__":
    main()
