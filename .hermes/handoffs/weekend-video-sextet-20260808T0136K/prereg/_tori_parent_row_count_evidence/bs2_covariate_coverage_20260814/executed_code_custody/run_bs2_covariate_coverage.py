#!/usr/bin/env python3
"""Measure BS-2 catalogue-field coverage with one aggregate row per frozen range."""
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
SCOPE = ROOT / "bs2_covariate_coverage_20260814"
QUERIES = SCOPE / "queries"
RUNS = SCOPE / "runs"
MANIFEST_PATH = SCOPE / "manifest.json"
STATUS_PATH = SCOPE / "status.json"
FINAL_PATH = SCOPE / "FINAL_COVERAGE.json"
LOCK_PATH = SCOPE / "orchestrator.lock"
AUTHORIZATION_PATH = SCOPE / "LAUNCH_AUTHORIZATION.json"
WORKER_PATH = ROOT / "run_aggregate_tap.py"
SOURCE_MANIFEST_PATH = ROOT / "footprint_variance_partitioned_20260813" / "manifest.json"
SOURCE_MANIFEST_SHA256 = "076131fff15c0338cce689b4742cd64631f855e2a04398dc2d527b0962edda93"
WORKER_SHA256 = "228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51"
EXPECTED_POPULATION = 832393
MAX_CONCURRENT = 3
POLL_SECONDS = 10
MAX_WAIT_SECONDS = 5400
SUBMISSION_CLOSED = False
RESULT_COLUMNS = [
    "n_total",
    "n_extinction",
    "n_angular_size",
    "n_axis_ratio",
    "n_colour",
    "n_magnitude",
    "n_flag_fields",
    "n_photoz",
]
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


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def load_ordinary_worker():
    spec = importlib.util.spec_from_file_location("aggregate_worker", WORKER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load aggregate worker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_inputs() -> None:
    for path, expected in {
        SOURCE_MANIFEST_PATH: SOURCE_MANIFEST_SHA256,
        WORKER_PATH: WORKER_SHA256,
    }.items():
        if not path.exists() or sha256_path(path) != expected:
            raise RuntimeError(f"frozen input missing or changed: {path}")
    if not AUTHORIZATION_PATH.exists():
        raise RuntimeError("launch authorization receipt is missing")


def ranges() -> list[tuple[int, int]]:
    if sha256_path(SOURCE_MANIFEST_PATH) != SOURCE_MANIFEST_SHA256:
        raise RuntimeError("source range manifest changed")
    source = json.loads(SOURCE_MANIFEST_PATH.read_text())
    result = [(int(entry["lo"]), int(entry["hi"])) for entry in source["entries"]]
    if len(result) != 67 or result[0] != (1, 10000) or result[-1] != (660001, 662174):
        raise RuntimeError("source range manifest shape drift")
    cursor = 1
    for lo, hi in result:
        if lo != cursor or hi != min(lo + 9999, 662174):
            raise RuntimeError("source range manifest is not contiguous")
        cursor = hi + 1
    if cursor != 662175:
        raise RuntimeError("source range manifest is incomplete")
    return result


def render_query(lo: int, hi: int) -> str:
    if (lo, hi) not in ranges():
        raise ValueError("range outside frozen manifest")
    return f"""SELECT
  COUNT(*) AS n_total,
  SUM(CASE WHEN t.ebv IS NOT NULL THEN 1 ELSE 0 END) AS n_extinction,
  SUM(CASE WHEN t.shape_r IS NOT NULL AND t.shape_r > 0 THEN 1 ELSE 0 END) AS n_angular_size,
  SUM(CASE WHEN t.shape_e1 IS NOT NULL AND t.shape_e2 IS NOT NULL AND POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 1 THEN 1 ELSE 0 END) AS n_axis_ratio,
  SUM(CASE WHEN t.flux_g IS NOT NULL AND t.flux_g > 0 AND t.flux_r IS NOT NULL AND t.flux_r > 0 AND t.mw_transmission_g IS NOT NULL AND t.mw_transmission_g > 0 AND t.mw_transmission_r IS NOT NULL AND t.mw_transmission_r > 0 THEN 1 ELSE 0 END) AS n_colour,
  SUM(CASE WHEN t.flux_r IS NOT NULL AND t.flux_r > 0 AND t.mw_transmission_r IS NOT NULL AND t.mw_transmission_r > 0 THEN 1 ELSE 0 END) AS n_magnitude,
  SUM(CASE WHEN t.maskbits IS NOT NULL AND t.fitbits IS NOT NULL THEN 1 ELSE 0 END) AS n_flag_fields,
  SUM(CASE WHEN p.z_phot_median IS NOT NULL AND p.z_phot_median >= 0 AND p.z_phot_median < 0.15 THEN 1 ELSE 0 END) AS n_photoz
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
"""


def validate_query(query: str, lo: int, hi: int) -> None:
    load_ordinary_worker().validate_aggregate_only(query)
    if (lo, hi) not in ranges() or f"t.brickid BETWEEN {lo} AND {hi}" not in query:
        raise RuntimeError("query range mismatch")
    where_clause = query.split("\nWHERE ", 1)[1]
    for predicate in REQUIRED_PREDICATES:
        if where_clause.count(predicate) != 1:
            raise RuntimeError(f"frozen predicate missing or repeated: {predicate}")
    normalized = " ".join(query.upper().split())
    for alias in RESULT_COLUMNS:
        if normalized.count(f" AS {alias.upper()}") != 1:
            raise RuntimeError(f"coverage projection missing or repeated: {alias}")
    if "T.RA" in normalized or "T.DEC" in normalized:
        raise RuntimeError("position term reached query")
    if re.search(r"\b(SIN|COS|TAN|ASIN|ACOS|ATAN|RADIANS|DEGREES|COSTHETA)\s*\(", normalized):
        raise RuntimeError("sky-statistic or trigonometric term reached query")
    if re.search(r"\b(CHIRALITY|HANDEDNESS|CLOCKWISE|COUNTERCLOCKWISE|CW|CCW|SPIN|ARM_CONTRAST)\b", normalized):
        raise RuntimeError("morphology or signal term reached query")


def reduce_rows(rows: list[dict[str, str]]) -> dict:
    totals = {name: 0 for name in RESULT_COLUMNS}
    for row in rows:
        if list(row) != RESULT_COLUMNS:
            raise RuntimeError(f"result columns drift: {list(row)}")
        for name in RESULT_COLUMNS:
            totals[name] += int(row[name] or 0)
    population = totals["n_total"]
    if population <= 0:
        raise RuntimeError("aggregate population must be positive")
    coverage = {}
    for name in RESULT_COLUMNS[1:]:
        key = name.removeprefix("n_")
        coverage[key] = {
            "count": totals[name],
            "fraction": totals[name] / population,
        }
    return {
        "partition_count": len(rows),
        "aggregate_rows_returned": len(rows),
        "population": population,
        "coverage": coverage,
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_or_morphology_computed": False,
        "sky_statistic_computed": False,
    }


def build_manifest() -> dict:
    verify_inputs()
    entries = []
    QUERIES.mkdir(parents=True, exist_ok=True)
    for lo, hi in ranges():
        query = render_query(lo, hi)
        validate_query(query, lo, hi)
        query_path = QUERIES / f"query_{lo:06d}_{hi:06d}.adql"
        encoded = query.encode()
        if query_path.exists() and query_path.read_bytes() != encoded:
            raise RuntimeError(f"refuse overwrite of changed query: {query_path}")
        if not query_path.exists():
            query_path.write_bytes(encoded)
        entries.append(
            {
                "lo": lo,
                "hi": hi,
                "query_path": str(query_path),
                "query_sha256": hashlib.sha256(encoded).hexdigest(),
                "run_dir": str(RUNS / f"run_{lo:06d}_{hi:06d}"),
            }
        )
    manifest = {
        "created_utc": utc_now(),
        "scope": "BS-2 Cut-6 catalogue-field coverage; one aggregate row per range",
        "endpoint": "https://datalab.noirlab.edu/tap/async",
        "partition_count": len(entries),
        "coverage": {"lo": 1, "hi": 662174},
        "result_columns": RESULT_COLUMNS,
        "expected_population": EXPECTED_POPULATION,
        "max_concurrent": MAX_CONCURRENT,
        "source_manifest_sha256": SOURCE_MANIFEST_SHA256,
        "ordinary_guard_sha256": WORKER_SHA256,
        "authorization_sha256": sha256_path(AUTHORIZATION_PATH),
        "object_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "arm_contrast_queried": False,
        "entries": entries,
    }
    if MANIFEST_PATH.exists():
        existing = json.loads(MANIFEST_PATH.read_text())
        comparison = dict(manifest)
        existing.pop("created_utc", None)
        comparison.pop("created_utc", None)
        if existing != comparison:
            raise RuntimeError("refuse overwrite of changed manifest")
    else:
        atomic_json(MANIFEST_PATH, manifest)
    return json.loads(MANIFEST_PATH.read_text())


def load_completed(entry: dict) -> dict[str, str] | None:
    tap = Path(entry["run_dir"]) / "tap"
    receipt_path = tap / "receipt.json"
    result_path = tap / "result.csv"
    if not receipt_path.exists() or not result_path.exists():
        return None
    receipt = json.loads(receipt_path.read_text())
    if receipt.get("query_sha256") != entry["query_sha256"]:
        raise RuntimeError(f"query receipt hash mismatch: {tap}")
    if receipt.get("result_sha256") != sha256_path(result_path):
        raise RuntimeError(f"result receipt hash mismatch: {tap}")
    if receipt.get("result_columns") != RESULT_COLUMNS:
        raise RuntimeError(f"result columns drift: {tap}")
    if receipt.get("result_row_count") != 1:
        raise RuntimeError(f"partition did not return exactly one aggregate row: {tap}")
    for name, expected in {
        "sample_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": False,
        "sky_statistics_computed": False,
    }.items():
        if receipt.get(name) != expected:
            raise RuntimeError(f"boundary receipt mismatch {name}: {tap}")
    rows = list(csv.DictReader(result_path.read_text().splitlines()))
    if len(rows) != 1 or list(rows[0]) != RESULT_COLUMNS:
        raise RuntimeError(f"malformed aggregate result: {tap}")
    return rows[0]


def runner_command(entry: dict) -> list[str]:
    tap = Path(entry["run_dir"]) / "tap"
    command = [
        sys.executable,
        str(WORKER_PATH),
        entry["query_path"],
        str(tap),
        "--poll-seconds",
        str(POLL_SECONDS),
        "--max-wait-seconds",
        str(MAX_WAIT_SECONDS),
    ]
    submission = tap / "submission.json"
    if submission.exists():
        command += ["--resume-job-url", json.loads(submission.read_text())["job_url"]]
    return command


def main() -> None:
    if SUBMISSION_CLOSED:
        raise SystemExit("CLOSED: BS-2 aggregate coverage census completed; no further submissions permitted")
    SCOPE.mkdir(parents=True, exist_ok=True)
    lock = LOCK_PATH.open("a+")
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        raise SystemExit("another BS-2 coverage orchestrator holds the lock") from exc
    manifest = build_manifest()
    pending = [entry for entry in manifest["entries"] if load_completed(entry) is None]
    active: dict[str, dict] = {}
    state = {
        "started_utc": utc_now(),
        "updated_utc": utc_now(),
        "manifest_sha256": sha256_path(MANIFEST_PATH),
        "authorization_sha256": sha256_path(AUTHORIZATION_PATH),
        "completed": len(manifest["entries"]) - len(pending),
        "active": {},
        "stop_reason": None,
    }
    atomic_json(STATUS_PATH, state)
    while pending or active:
        for key, worker in list(active.items()):
            returncode = worker["process"].poll()
            if returncode is None:
                continue
            entry = worker["entry"]
            if returncode != 0 or load_completed(entry) is None:
                state["stop_reason"] = f"partition_failed_{key}"
                atomic_json(STATUS_PATH, state)
                for other in active.values():
                    if other["process"].poll() is None:
                        other["process"].terminate()
                raise RuntimeError(f"aggregate partition failed: {key}")
            del active[key]
            state["active"].pop(key, None)
            state["completed"] += 1
            state["updated_utc"] = utc_now()
            atomic_json(STATUS_PATH, state)
            print(json.dumps({"partition": key, "status": "completed"}), flush=True)
        while pending and len(active) < MAX_CONCURRENT:
            entry = pending.pop(0)
            key = f"{entry['lo']:06d}-{entry['hi']:06d}"
            tap = Path(entry["run_dir"]) / "tap"
            tap.mkdir(parents=True, exist_ok=True)
            stdout = (tap / "runner_stdout.log").open("a")
            stderr = (tap / "runner_stderr.log").open("a")
            process = subprocess.Popen(runner_command(entry), stdout=stdout, stderr=stderr, text=True)
            stdout.close()
            stderr.close()
            active[key] = {"entry": entry, "process": process}
            state["active"][key] = {"pid": process.pid, **entry}
            state["updated_utc"] = utc_now()
            atomic_json(STATUS_PATH, state)
        if pending or active:
            time.sleep(5)
    rows = [load_completed(entry) for entry in manifest["entries"]]
    if any(row is None for row in rows):
        raise RuntimeError("full manifest coverage not reached")
    final = {
        "recorded_utc": utc_now(),
        "manifest_sha256": sha256_path(MANIFEST_PATH),
        "authorization_sha256": sha256_path(AUTHORIZATION_PATH),
        "ordinary_guard_sha256": sha256_path(WORKER_PATH),
        **reduce_rows([row for row in rows if row is not None]),
    }
    final["population_matches_frozen_cut6"] = final["population"] == EXPECTED_POPULATION
    if not final["population_matches_frozen_cut6"]:
        raise RuntimeError("coverage population does not match frozen Cut-6 population")
    atomic_json(FINAL_PATH, final)
    state["updated_utc"] = utc_now()
    state["finished_utc"] = utc_now()
    state["stop_reason"] = "full_manifest_coverage"
    atomic_json(STATUS_PATH, state)
    print(json.dumps(final, sort_keys=True))


if __name__ == "__main__":
    main()
