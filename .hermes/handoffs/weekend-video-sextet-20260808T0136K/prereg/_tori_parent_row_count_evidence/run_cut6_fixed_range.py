#!/usr/bin/env python3
"""Run a fixed-range aggregate-only Cut 6 pass over BRICKID 1..121000.

This is a sibling count pass. It never changes or resumes the stopped Cut-5
sweep and never submits a range beyond BRICKID 121000.
"""
from __future__ import annotations

import csv
import fcntl
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNNER_PATH = ROOT / "run_aggregate_tap.py"
RENDERER_PATH = ROOT / "render_cut6_receipt.py"
SCOPE = ROOT / "cut6_fixed_000001_121000"
QUERIES = SCOPE / "queries"
RUNS = SCOPE / "runs"
MANIFEST_PATH = SCOPE / "manifest.json"
STATUS_PATH = SCOPE / "status.json"
LOCK_PATH = SCOPE / "orchestrator.lock"
RANGES = [
    (1, 1000),
    (1001, 11000),
    *[(lo, lo + 9999) for lo in range(11001, 111002, 10000)],
]
COLUMNS = [
    "n_cut5_parent_raw",
    "n_cut5_parent_dered",
    "n_cut6_inclination_raw",
    "n_cut6_inclination_dered",
]
THRESHOLD = "0.1836734693877551"
MAX_CONCURRENT = 3
POLL_SECONDS = 15
MAX_WAIT_SECONDS = 5400


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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
    return re.findall(r"\bAS\s+([A-Za-z_][A-Za-z0-9_]*)\b", select, flags=re.IGNORECASE)


def cut_predicate(magnitude: str, *, cut6: bool) -> str:
    lines = [
        "1 = 1",
        "t.brick_primary = 1",
        "t.maskbits = 0",
        "t.type <> 'PSF'",
        "t.flux_r > 0",
        "p.z_phot_median >= 0",
        "p.z_phot_median < 0.15",
        f"t.{magnitude} < 17.7",
        "t.shape_r > 1.5",
    ]
    if cut6:
        lines.append(
            f"POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < {THRESHOLD}"
        )
    return "\n         AND ".join(lines)


def aggregate_expression(alias: str, magnitude: str, *, cut6: bool) -> str:
    predicate = cut_predicate(magnitude, cut6=cut6).replace(
        "\n         AND ", "\n         AND ", 1
    )
    return (
        "  SUM(CASE\n"
        f"        WHEN {predicate}\n"
        "        THEN 1 ELSE 0\n"
        f"      END) AS {alias}"
    )


def render_query(lo: int, hi: int) -> str:
    if (lo, hi) not in RANGES:
        raise ValueError(f"range outside frozen Cut 6 manifest: {lo}..{hi}")
    expressions = [
        aggregate_expression("n_cut5_parent_raw", "mag_r", cut6=False),
        aggregate_expression("n_cut5_parent_dered", "dered_mag_r", cut6=False),
        aggregate_expression("n_cut6_inclination_raw", "mag_r", cut6=True),
        aggregate_expression("n_cut6_inclination_dered", "dered_mag_r", cut6=True),
    ]
    return (
        "SELECT\n"
        + ",\n\n".join(expressions)
        + "\n\nFROM ls_dr10.tractor_s AS t\n"
        + "LEFT OUTER JOIN ls_dr10.photo_z AS p\n"
        + "  ON t.ls_id = p.ls_id\n"
        + " AND t.release = p.release\n"
        + " AND t.brickid = p.brickid\n"
        + " AND t.objid = p.objid\n"
        + f"WHERE t.brickid BETWEEN {lo} AND {hi}\n"
    )


def source_cut5_result_path(lo: int, hi: int) -> Path:
    if (lo, hi) == (1, 1000):
        return ROOT / "run12_partition_normalized_000001_001000" / "result.csv"
    if (lo, hi) == (1001, 11000):
        return ROOT / "run09_partition_benchmark_001001_011000" / "result.csv"
    return ROOT / "partitions" / f"run_{lo:06d}_{hi:06d}" / "tap" / "result.csv"


def build_manifest(*, dry_run: bool = False) -> dict:
    validate = load_guard()
    entries = []
    for lo, hi in RANGES:
        query = render_query(lo, hi)
        validate(query)
        if projected_aliases(query) != COLUMNS:
            raise RuntimeError("Cut 6 query projection drift")
        query_bytes = query.encode()
        query_path = QUERIES / f"query_{lo:06d}_{hi:06d}.adql"
        run_dir = RUNS / f"run_{lo:06d}_{hi:06d}"
        source_path = source_cut5_result_path(lo, hi)
        if not source_path.exists():
            raise RuntimeError(f"missing source Cut 5 aggregate: {source_path}")
        entries.append(
            {
                "lo": lo,
                "hi": hi,
                "query_path": str(query_path),
                "query_sha256": sha256_bytes(query_bytes),
                "run_dir": str(run_dir),
                "source_cut5_result_path": str(source_path),
                "source_cut5_result_sha256": sha256_bytes(source_path.read_bytes()),
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
        "scope": "server-side aggregate Cut 5/Cut 6 counts only; no rows, positions, images, chirality, or sky statistics",
        "coverage": {
            "start_brickid": 1,
            "stop_brickid": 121000,
            "keyspace_total": 662174,
            "keyspace_fraction": 121000 / 662174,
            "keyspace_not_sky_area": True,
        },
        "partition_count": len(entries),
        "columns": COLUMNS,
        "threshold_expression": "POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551",
        "no_coverage_extension": True,
        "max_concurrent": MAX_CONCURRENT,
        "entries": entries,
    }
    if not dry_run:
        SCOPE.mkdir(parents=True, exist_ok=True)
        encoded = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
        if MANIFEST_PATH.exists():
            existing = json.loads(MANIFEST_PATH.read_text())
            existing.pop("created_utc", None)
            comparison = dict(manifest)
            comparison.pop("created_utc", None)
            if existing != comparison:
                raise RuntimeError("refuse overwrite of nonidentical Cut 6 manifest")
        else:
            MANIFEST_PATH.write_bytes(encoded)
        return json.loads(MANIFEST_PATH.read_text())
    return manifest


def read_one_row(path: Path) -> dict[str, int]:
    rows = list(csv.DictReader(path.read_text().splitlines()))
    if len(rows) != 1:
        raise RuntimeError(f"expected exactly one aggregate row: {path}")
    return {key: int(value) for key, value in rows[0].items()}


def validate_completed(entry: dict) -> dict[str, int] | None:
    tap = Path(entry["run_dir"]) / "tap"
    receipt_path = tap / "receipt.json"
    result_path = tap / "result.csv"
    if not receipt_path.exists() or not result_path.exists():
        return None
    receipt = json.loads(receipt_path.read_text())
    if receipt.get("query_sha256") != entry["query_sha256"]:
        raise RuntimeError(f"Cut 6 receipt/query hash mismatch: {tap}")
    if receipt.get("result_sha256") != sha256_bytes(result_path.read_bytes()):
        raise RuntimeError(f"Cut 6 result hash mismatch: {tap}")
    if receipt.get("result_row_count") != 1 or receipt.get("result_columns") != COLUMNS:
        raise RuntimeError(f"Cut 6 result shape mismatch: {tap}")
    for name, expected in {
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "sky_statistics_computed": False,
    }.items():
        if receipt.get(name) != expected:
            raise RuntimeError(f"Cut 6 custody violation {name}: {tap}")
    row = read_one_row(result_path)
    if list(row) != COLUMNS:
        raise RuntimeError(f"unexpected Cut 6 columns: {tap}")
    source = read_one_row(Path(entry["source_cut5_result_path"]))
    if row["n_cut5_parent_raw"] != source["n_cut5_parent_raw"]:
        raise RuntimeError(f"raw Cut 5 comparison mismatch: {tap}")
    if row["n_cut5_parent_dered"] != source["n_cut5_parent_dered"]:
        raise RuntimeError(f"dered Cut 5 comparison mismatch: {tap}")
    if not 0 <= row["n_cut6_inclination_raw"] <= row["n_cut5_parent_raw"]:
        raise RuntimeError(f"raw Cut 6 monotonicity failure: {tap}")
    if not 0 <= row["n_cut6_inclination_dered"] <= row["n_cut5_parent_dered"]:
        raise RuntimeError(f"dered Cut 6 monotonicity failure: {tap}")
    return row


def totals(manifest: dict) -> dict[str, int]:
    sums = {column: 0 for column in COLUMNS}
    completed = 0
    covered_hi = 0
    for entry in manifest["entries"]:
        row = validate_completed(entry)
        if row is None:
            break
        for column in COLUMNS:
            sums[column] += row[column]
        completed += 1
        covered_hi = entry["hi"]
    return {"completed_partitions": completed, "covered_hi": covered_hi, **sums}


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
    submission = tap / "submission.json"
    if submission.exists():
        value = json.loads(submission.read_text())
        if value.get("query_sha256") != entry["query_sha256"]:
            raise RuntimeError(f"Cut 6 submission/query hash mismatch: {tap}")
        command += ["--resume-job-url", value["job_url"]]
    return command


def render_receipt() -> None:
    result = subprocess.run(
        [sys.executable, str(RENDERER_PATH)], text=True, capture_output=True
    )
    atomic_json(
        SCOPE / "last_receipt_render.json",
        {
            "rendered_utc": utc_now(),
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        },
    )
    if result.returncode != 0:
        raise RuntimeError(f"Cut 6 receipt renderer failed: {result.stderr}")


def main() -> None:
    SCOPE.mkdir(parents=True, exist_ok=True)
    lock = LOCK_PATH.open("a+")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise SystemExit("another Cut 6 orchestrator holds the lock") from exc
    manifest = build_manifest()
    state = {
        "started_utc": utc_now(),
        "updated_utc": utc_now(),
        "manifest_sha256": sha256_bytes(MANIFEST_PATH.read_bytes()),
        "configured_concurrency": MAX_CONCURRENT,
        "active_concurrency": MAX_CONCURRENT,
        "coverage_frozen": manifest["coverage"],
        "results": {},
        "active": {},
        "totals": totals(manifest),
    }
    if STATUS_PATH.exists():
        state["previous_status_sha256"] = sha256_bytes(STATUS_PATH.read_bytes())
    for entry in manifest["entries"]:
        if validate_completed(entry) is not None:
            key = f"{entry['lo']:06d}-{entry['hi']:06d}"
            state["results"][key] = {"status": "completed_existing", **entry}
    atomic_json(STATUS_PATH, state)
    render_receipt()

    pending = [entry for entry in manifest["entries"] if validate_completed(entry) is None]
    active: dict[str, dict] = {}
    target_concurrency = MAX_CONCURRENT
    hard_failure = False

    def persist() -> None:
        state["updated_utc"] = utc_now()
        state["totals"] = totals(manifest)
        atomic_json(STATUS_PATH, state)

    while pending or active:
        while pending and not hard_failure and len(active) < target_concurrency:
            entry = pending.pop(0)
            key = f"{entry['lo']:06d}-{entry['hi']:06d}"
            tap = Path(entry["run_dir"]) / "tap"
            tap.mkdir(parents=True, exist_ok=True)
            stdout_handle = (tap / "runner_stdout.log").open("a")
            stderr_handle = (tap / "runner_stderr.log").open("a")
            process = subprocess.Popen(
                runner_command(entry), stdout=stdout_handle, stderr=stderr_handle, text=True
            )
            stdout_handle.close()
            stderr_handle.close()
            active[key] = {
                "entry": entry,
                "tap": tap,
                "process": process,
                "started_utc": utc_now(),
            }
            state["active"][key] = {
                "pid": process.pid,
                "started_utc": active[key]["started_utc"],
                **entry,
            }
            persist()

        for key, worker in list(active.items()):
            pressure = worker["tap"] / "service_pressure.json"
            if pressure.exists() and target_concurrency != 1:
                target_concurrency = 1
                state["active_concurrency"] = 1
                state["service_backoff"] = {
                    "detected_utc": utc_now(),
                    "signal": json.loads(pressure.read_text()).get("signal", "unknown"),
                    "source": str(pressure),
                    "action": "future Cut 6 submissions reduced to serial; active jobs preserved",
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
            elif "job still EXECUTING" in stderr or "job still QUEUED" in stderr:
                result["status"] = "resume_required"
                pending.insert(0, entry)
            elif pressure.exists() and not (worker["tap"] / "submission.json").exists():
                result["status"] = "service_pressure_retry_serial"
                target_concurrency = 1
                state["active_concurrency"] = 1
                pending.insert(0, entry)
                time.sleep(60)
            else:
                result["status"] = "failed"
                result["stderr_sha256"] = sha256_bytes(stderr.encode())
                hard_failure = True
                state["stop_reason"] = f"cut6_partition_failure_{key}"
            state["results"][key] = result
            state["active"].pop(key, None)
            del active[key]
            persist()
            render_receipt()
            print(json.dumps(result, sort_keys=True), flush=True)

        if hard_failure and not active:
            break
        time.sleep(5)

    state["finished_utc"] = utc_now()
    state["totals"] = totals(manifest)
    if not hard_failure and state["totals"]["completed_partitions"] == len(RANGES):
        state["stop_reason"] = "fixed_range_1_121000_complete"
    persist()
    render_receipt()
    if hard_failure:
        raise SystemExit(state["stop_reason"])
    if state["totals"]["completed_partitions"] != len(RANGES):
        raise SystemExit("Cut 6 fixed range incomplete")
    print(json.dumps({"status": "complete", "totals": state["totals"]}, sort_keys=True))


if __name__ == "__main__":
    main()
