#!/usr/bin/env python3
"""Generate and execute disjoint aggregate-only DR10-South count partitions.

The script never projects object identifiers or coordinates. Each query returns
one row of aggregate counts. Existing submissions are resumed by exact TAP job
URL; they are never blindly resubmitted.
"""

from __future__ import annotations

import hashlib
import importlib.util
import csv
import fcntl
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
import urllib.parse
import urllib.request

ROOT = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K/prereg/"
    "_tori_parent_row_count_evidence"
)
TEMPLATE_PATH = ROOT / "09_partition_benchmark_brickid_001001_011000.adql"
RUNNER_PATH = ROOT / "run_aggregate_tap.py"
RENDERER_PATH = ROOT / "render_parent_count_receipt.py"
PARTITIONS = ROOT / "partitions"
MANIFEST_PATH = PARTITIONS / "manifest.json"
STATUS_PATH = PARTITIONS / "status.json"
START = 11001
STOP = 662174
WIDTH = 10000
MAX_CONCURRENT = 3
MAX_WAIT_SECONDS = 5400
POLL_SECONDS = 15
STOP_PARENT_LOWER_BOUND = 200000
DEADLINE_UTC = "2026-08-12T13:56:00Z"
LOCK_PATH = PARTITIONS / "orchestrator.lock"
LOG_PATH = PARTITIONS / "orchestrator.log"

def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_json(path: Path, obj: object) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def load_guard():
    spec = importlib.util.spec_from_file_location("aggregate_runner", RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load aggregate runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_aggregate_only


def build_manifest() -> dict:
    PARTITIONS.mkdir(parents=True, exist_ok=True)
    template = TEMPLATE_PATH.read_text()
    old = "WHERE t.brickid BETWEEN 1001 AND 11000\n"
    if template.count(old) != 1:
        raise RuntimeError("template range marker missing or non-unique")
    validate = load_guard()
    entries = []
    lo = START
    while lo <= STOP:
        hi = min(lo + WIDTH - 1, STOP)
        query = template.replace(old, f"WHERE t.brickid BETWEEN {lo} AND {hi}\n")
        validate(query)
        qpath = PARTITIONS / f"query_{lo:06d}_{hi:06d}.adql"
        qbytes = query.encode()
        if qpath.exists():
            if qpath.read_bytes() != qbytes:
                raise RuntimeError(f"refuse overwrite of nonidentical query: {qpath}")
        else:
            qpath.write_bytes(qbytes)
        entries.append(
            {
                "lo": lo,
                "hi": hi,
                "query_path": str(qpath),
                "query_sha256": sha256(qbytes),
                "run_dir": str(PARTITIONS / f"run_{lo:06d}_{hi:06d}"),
            }
        )
        lo = hi + 1

    manifest = {
        "created_utc": utc_now(),
        "endpoint": "https://datalab.noirlab.edu/tap/async",
        "scope": "aggregate counts only; no sample rows, positions, images, chirality, or sky statistics",
        "coverage": {"start_brickid": START, "stop_brickid": STOP, "width": WIDTH},
        "preceding_completed_coverage": [
            {"lo": 1, "hi": 1000, "run": "run08_partition_test_000001_001000"},
            {"lo": 1001, "hi": 11000, "run": "run09_partition_benchmark_001001_011000"},
        ],
        "partition_count": len(entries),
        "max_concurrent": MAX_CONCURRENT,
        "stop_rule": {
            "parent_column": "n_cut5_parent_dered",
            "lower_bound": STOP_PARENT_LOWER_BOUND,
            "deadline_utc": DEADLINE_UTC,
            "keyspace_exhaustion": STOP,
        },
        "entries": entries,
    }
    encoded = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    if MANIFEST_PATH.exists():
        old_manifest = json.loads(MANIFEST_PATH.read_text())
        old_manifest.pop("created_utc", None)
        check_manifest = dict(manifest)
        check_manifest.pop("created_utc", None)
        if old_manifest != check_manifest:
            raise RuntimeError("refuse overwrite of nonidentical partition manifest")
    else:
        MANIFEST_PATH.write_bytes(encoded)
    return json.loads(MANIFEST_PATH.read_text())


def validate_receipt(run_dir: Path, query_sha: str) -> bool:
    receipt_path = run_dir / "receipt.json"
    result_path = run_dir / "result.csv"
    if not receipt_path.exists() or not result_path.exists():
        return False
    receipt = json.loads(receipt_path.read_text())
    if receipt.get("query_sha256") != query_sha:
        raise RuntimeError(f"receipt query hash mismatch: {run_dir}")
    if receipt.get("result_row_count") != 1:
        raise RuntimeError(f"non-single-row result: {run_dir}")
    if receipt.get("sample_rows_exported") != 0 or receipt.get("positions_exported") != 0:
        raise RuntimeError(f"custody boundary violated: {run_dir}")
    if receipt.get("sky_statistics_computed") is not False:
        raise RuntimeError(f"sky-stat boundary violated: {run_dir}")
    if sha256(result_path.read_bytes()) != receipt.get("result_sha256"):
        raise RuntimeError(f"result hash mismatch: {run_dir}")
    return True


def completed_row(entry: dict) -> dict[str, int] | None:
    tap_dir = Path(entry["run_dir"]) / "tap"
    if not validate_receipt(tap_dir, entry["query_sha256"]):
        return None
    rows = list(csv.DictReader((tap_dir / "result.csv").read_text().splitlines()))
    if len(rows) != 1:
        raise RuntimeError(f"expected one row: {tap_dir}")
    return {key: int(value) for key, value in rows[0].items()}


def lower_bound(manifest: dict) -> dict[str, int]:
    fixed = [
        ROOT / "run12_partition_normalized_000001_001000" / "result.csv",
        ROOT / "run09_partition_benchmark_001001_011000" / "result.csv",
    ]
    raw = 0
    dered = 0
    covered_hi = 0
    for path, hi in zip(fixed, (1000, 11000)):
        rows = list(csv.DictReader(path.read_text().splitlines()))
        if len(rows) != 1:
            raise RuntimeError(f"expected one fixed aggregate row: {path}")
        raw += int(rows[0]["n_cut5_parent_raw"])
        dered += int(rows[0]["n_cut5_parent_dered"])
        covered_hi = hi
    cursor = 11001
    completed_partitions = 0
    for entry in manifest["entries"]:
        if entry["lo"] != cursor:
            raise RuntimeError("manifest is not contiguous")
        row = completed_row(entry)
        if row is None:
            break
        raw += row["n_cut5_parent_raw"]
        dered += row["n_cut5_parent_dered"]
        covered_hi = entry["hi"]
        completed_partitions += 1
        cursor = entry["hi"] + 1
    return {
        "covered_hi": covered_hi,
        "completed_manifest_partitions": completed_partitions,
        "n_cut5_parent_raw": raw,
        "n_cut5_parent_dered": dered,
    }


def runner_command(entry: dict) -> tuple[list[str], Path]:
    query_path = Path(entry["query_path"])
    run_dir = Path(entry["run_dir"])
    run_dir.mkdir(parents=True, exist_ok=True)
    tap_dir = run_dir / "tap"
    cmd = [
        sys.executable,
        str(RUNNER_PATH),
        str(query_path),
        str(tap_dir),
        "--poll-seconds",
        str(POLL_SECONDS),
        "--max-wait-seconds",
        str(MAX_WAIT_SECONDS),
    ]
    submission_path = tap_dir / "submission.json"
    if submission_path.exists():
        submission = json.loads(submission_path.read_text())
        if submission.get("query_sha256") != entry["query_sha256"]:
            raise RuntimeError(f"submission query hash mismatch: {run_dir}")
        cmd += ["--resume-job-url", submission["job_url"]]
    return cmd, tap_dir


def tap_request(url: str, data=None) -> str:
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    request = urllib.request.Request(
        url,
        data=body,
        headers={"User-Agent": "Tori-count-custody/1.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode().strip()


def stop_active_worker(worker: dict, reason: str) -> dict:
    entry = worker["entry"]
    tap_dir = worker["tap_dir"]
    submission_path = tap_dir / "submission.json"
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
    proc = worker["proc"]
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=15)
    receipt = {
        "recorded_utc": utc_now(),
        "stop_reason": reason,
        "brickid_range": {"lo": entry["lo"], "hi": entry["hi"]},
        "job_url": job_url,
        "phase_before": phase_before,
        "phase_after": phase_after,
        "abort_error": abort_error,
        "runner_exit_code": proc.returncode,
        "query_sha256": entry["query_sha256"],
        "result_rows_exported": 0,
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "sky_statistics_computed": False,
    }
    atomic_json(tap_dir / "intentional_stop_receipt.json", receipt)
    return {**entry, "status": "intentionally_stopped", **receipt}


def main() -> None:
    PARTITIONS.mkdir(parents=True, exist_ok=True)
    lock_handle = LOCK_PATH.open("a+")
    try:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise SystemExit("another partition orchestrator holds the lock") from exc
    manifest = build_manifest()
    state = {
        "started_utc": utc_now(),
        "updated_utc": utc_now(),
        "manifest_sha256": sha256(MANIFEST_PATH.read_bytes()),
        "configured_concurrency": MAX_CONCURRENT,
        "active_concurrency": MAX_CONCURRENT,
        "stop_parent_lower_bound": STOP_PARENT_LOWER_BOUND,
        "stop_parent_column": "n_cut5_parent_dered",
        "deadline_utc": DEADLINE_UTC,
        "execution_mode": "detached_tracked_background",
        "results": {},
        "active": {},
    }
    if STATUS_PATH.exists():
        state["previous_status_sha256"] = sha256(STATUS_PATH.read_bytes())
    for entry in manifest["entries"]:
        if completed_row(entry) is not None:
            key = f"{entry['lo']:06d}-{entry['hi']:06d}"
            state["results"][key] = {"status": "completed_existing", **entry}
    state["lower_bound"] = lower_bound(manifest)
    atomic_json(STATUS_PATH, state)

    def persist() -> None:
        state["updated_utc"] = utc_now()
        atomic_json(STATUS_PATH, state)

    def render_after(result: dict) -> None:
        key = f"{result['lo']:06d}-{result['hi']:06d}"
        state["results"][key] = result
        state["active"].pop(key, None)
        state["lower_bound"] = lower_bound(manifest)
        persist()
        render = subprocess.run(
            [sys.executable, str(RENDERER_PATH)],
            text=True,
            capture_output=True,
        )
        render_log = Path(result["run_dir"]) / "receipt_render.json"
        atomic_json(
            render_log,
            {
                "rendered_utc": utc_now(),
                "exit_code": render.returncode,
                "stdout": render.stdout,
                "stderr": render.stderr,
            },
        )
        if render.returncode != 0:
            raise RuntimeError(f"receipt renderer failed after {key}: {render.stderr}")

    entries = manifest["entries"]
    pending = [entry for entry in entries if completed_row(entry) is None]
    active: dict[str, dict] = {}
    target_concurrency = MAX_CONCURRENT
    stop_submitting = False
    hard_failure = False

    while pending or active:
        bound = lower_bound(manifest)
        state["lower_bound"] = bound
        if bound["n_cut5_parent_dered"] >= STOP_PARENT_LOWER_BOUND:
            stop_submitting = True
            state["stop_reason"] = "dered_cut5_contiguous_lower_bound_reached_200000"
        elif datetime.now(timezone.utc) >= parse_utc(DEADLINE_UTC):
            stop_submitting = True
            state["stop_reason"] = "four_hour_wall_clock_deadline_reached"

        while pending and not stop_submitting and not hard_failure and len(active) < target_concurrency:
            entry = pending.pop(0)
            key = f"{entry['lo']:06d}-{entry['hi']:06d}"
            cmd, tap_dir = runner_command(entry)
            tap_dir.mkdir(parents=True, exist_ok=True)
            stdout_handle = (tap_dir / "runner_stdout.log").open("a")
            stderr_handle = (tap_dir / "runner_stderr.log").open("a")
            proc = subprocess.Popen(cmd, stdout=stdout_handle, stderr=stderr_handle, text=True)
            stdout_handle.close()
            stderr_handle.close()
            active[key] = {"entry": entry, "proc": proc, "started_utc": utc_now(), "tap_dir": tap_dir}
            state["active"][key] = {"pid": proc.pid, "started_utc": active[key]["started_utc"], **entry}
            persist()

        for key, worker in list(active.items()):
            pressure_path = worker["tap_dir"] / "service_pressure.json"
            if pressure_path.exists() and target_concurrency != 1:
                target_concurrency = 1
                state["active_concurrency"] = 1
                state["service_backoff"] = {
                    "detected_utc": utc_now(),
                    "source": str(pressure_path),
                    "signal": json.loads(pressure_path.read_text()).get("signal", "unknown"),
                    "action": "reduced future submissions to serial; already-active jobs left unduplicated",
                }
                persist()

            returncode = worker["proc"].poll()
            if returncode is None:
                continue
            entry = worker["entry"]
            stderr_path = worker["tap_dir"] / "runner_stderr.log"
            stderr = stderr_path.read_text() if stderr_path.exists() else ""
            result = {
                **entry,
                "started_utc": worker["started_utc"],
                "finished_utc": utc_now(),
                "runner_exit_code": returncode,
            }
            if returncode == 0 and completed_row(entry) is not None:
                result["status"] = "completed"
            elif ("job still EXECUTING" in stderr or "job still QUEUED" in stderr):
                result["status"] = "resume_required"
                pending.insert(0, entry)
            elif pressure_path.exists() and not (worker["tap_dir"] / "submission.json").exists():
                result["status"] = "service_pressure_retry_serial"
                target_concurrency = 1
                state["active_concurrency"] = 1
                pending.insert(0, entry)
                time.sleep(60)
            else:
                result["status"] = "failed"
                result["stderr_sha256"] = sha256(stderr.encode())
                hard_failure = True
                stop_submitting = True
                state["stop_reason"] = f"partition_failure_{key}"
            render_after(result)
            print(json.dumps(result, sort_keys=True), flush=True)
            del active[key]

        bound = lower_bound(manifest)
        state["lower_bound"] = bound
        if bound["n_cut5_parent_dered"] >= STOP_PARENT_LOWER_BOUND:
            stop_submitting = True
            state["stop_reason"] = "dered_cut5_contiguous_lower_bound_reached_200000"
        elif datetime.now(timezone.utc) >= parse_utc(DEADLINE_UTC):
            stop_submitting = True
            state["stop_reason"] = "four_hour_wall_clock_deadline_reached"

        if stop_submitting and active:
            for key, worker in list(active.items()):
                entry = worker["entry"]
                row = completed_row(entry)
                if row is not None:
                    proc = worker["proc"]
                    if proc.poll() is None:
                        proc.terminate()
                        try:
                            proc.wait(timeout=15)
                        except subprocess.TimeoutExpired:
                            proc.kill()
                            proc.wait(timeout=15)
                    result = {
                        **entry,
                        "status": "completed",
                        "started_utc": worker["started_utc"],
                        "finished_utc": utc_now(),
                        "runner_exit_code": proc.returncode,
                    }
                else:
                    result = stop_active_worker(worker, state["stop_reason"])
                render_after(result)
                print(json.dumps(result, sort_keys=True), flush=True)
                del active[key]

        if stop_submitting and not active:
            break
        time.sleep(5)

    state["finished_utc"] = utc_now()
    state["lower_bound"] = lower_bound(manifest)
    persist()
    final_render = subprocess.run(
        [sys.executable, str(RENDERER_PATH)],
        text=True,
        capture_output=True,
    )
    atomic_json(
        PARTITIONS / "final_receipt_render.json",
        {
            "rendered_utc": utc_now(),
            "exit_code": final_render.returncode,
            "stdout": final_render.stdout,
            "stderr": final_render.stderr,
        },
    )
    if final_render.returncode != 0:
        raise SystemExit(f"final receipt renderer failed: {final_render.stderr}")
    if hard_failure:
        raise SystemExit(state["stop_reason"])
    print(json.dumps({"status": "stopped", "reason": state.get("stop_reason", "manifest_exhausted"), "lower_bound": state["lower_bound"]}, sort_keys=True))


if __name__ == "__main__":
    main()
