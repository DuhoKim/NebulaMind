#!/usr/bin/env python3
"""Independently finalize the 2026-08-14 partitioned variance rerun after lifecycle closure."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
RUN = ROOT / "footprint_variance_partitioned_rerun_20260814"
MANIFEST_PATH = RUN / "manifest.json"
STATUS_PATH = RUN / "status.json"
LIFECYCLE_PATH = RUN / "guard_lifecycle.json"
OUTPUT = RUN / "FINAL_OUTCOME_20260814_RERUN.json"
ORCHESTRATOR_PATH = ROOT / "run_partitioned_footprint_variance_rerun.py"
EXPECTED_POPULATION_COUNT = 832393
THRESHOLD = Decimal("0.15")
FORBIDDEN_QUERY_TERMS = (
    "CHIRALITY",
    "HANDEDNESS",
    "CLOCKWISE",
    "COUNTERCLOCKWISE",
    "CW_CCW",
    "DIPOLE_AMPLITUDE",
    " SPIN ",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def load_orchestrator():
    spec = importlib.util.spec_from_file_location("variance_rerun_finalizer_source", ORCHESTRATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load rerun orchestrator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def classify_result(*, completed_partitions: int, partition_count: int, combined: dict | None) -> dict[str, str]:
    if completed_partitions == 0:
        if combined is not None:
            raise RuntimeError("zero completed partitions cannot have combined moments")
        return {"status": "UNRESOLVED", "threshold_verdict": "NONE"}
    if completed_partitions < partition_count:
        if combined is None:
            raise RuntimeError("partial completion is missing additive moments")
        return {"status": "PARTIAL", "threshold_verdict": "NONE"}
    if completed_partitions != partition_count or combined is None:
        raise RuntimeError("invalid partition completion state")
    if int(combined["n_cut6_dered"]) != EXPECTED_POPULATION_COUNT:
        raise RuntimeError("full coverage population count mismatch")
    variance = Decimal(combined["var_pop_cos_theta"])
    return {"status": "COMPLETE", "threshold_verdict": "PASS" if variance >= THRESHOLD else "FAIL"}


def remote_phase(job_url: str) -> dict:
    checked = now()
    request = urllib.request.Request(
        job_url.rstrip("/") + "/phase",
        headers={"User-Agent": "Tori-rerun-final-reconciliation/1.0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return {"checked_utc": checked, "http_status": response.status, "phase": response.read().decode().strip()}
    except urllib.error.HTTPError as exc:
        body = exc.read()
        return {
            "checked_utc": checked,
            "http_status": exc.code,
            "phase": None,
            "response_sha256": hashlib.sha256(body).hexdigest(),
        }
    except Exception as exc:
        return {"checked_utc": checked, "error": repr(exc), "phase": None}


def query_boundary_audit(manifest: dict) -> None:
    for entry in manifest["entries"]:
        path = Path(entry["query_path"])
        if sha(path) != entry["query_sha256"]:
            raise RuntimeError(f"query hash drift: {path}")
        query = path.read_text()
        upper = f" {query.upper()} "
        if query.upper().count("SELECT") != 1 or query.upper().count("COUNT(") != 1 or query.upper().count("SUM(") != 2:
            raise RuntimeError(f"aggregate query shape drift: {path}")
        if "AVG(" in upper or "GROUP BY" in upper or "SELECT *" in upper:
            raise RuntimeError(f"non-additive projection: {path}")
        if any(term in upper for term in FORBIDDEN_QUERY_TERMS):
            raise RuntimeError(f"forbidden signal term: {path}")


def submission_records(manifest: dict) -> list[dict]:
    rows = []
    by_run = {Path(entry["run_dir"]): entry for entry in manifest["entries"]}
    for run_dir, entry in by_run.items():
        paths = [run_dir / "submission.json", *run_dir.glob("failed_attempts/*/submission.json")]
        for path in paths:
            if not path.exists():
                continue
            submission = json.loads(path.read_text())
            if submission.get("query_sha256") != entry["query_sha256"]:
                raise RuntimeError(f"submission query hash mismatch: {path}")
            abort_path = path.parent / "deadline_abort.json"
            if path.parent == run_dir:
                abort_path = run_dir / "deadline_abort.json"
            rows.append(
                {
                    "brickid_range": {"lo": entry["lo"], "hi": entry["hi"]},
                    "submission_path": str(path.relative_to(RUN)),
                    "job_url": submission["job_url"],
                    "query_sha256": submission["query_sha256"],
                    "recorded_utc": submission.get("recorded_utc"),
                    "abort_record": json.loads(abort_path.read_text()) if abort_path.exists() else None,
                    "remote": remote_phase(submission["job_url"]),
                }
            )
    urls = [row["job_url"] for row in rows]
    if len(urls) != len(set(urls)):
        raise RuntimeError("duplicate job URL in final reconciliation")
    return rows


def decimal_strings(value: dict | None) -> dict | None:
    if value is None:
        return None
    return {key: str(item) if isinstance(item, Decimal) else item for key, item in value.items()}


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text())
    status = json.loads(STATUS_PATH.read_text())
    lifecycle = json.loads(LIFECYCLE_PATH.read_text())
    if lifecycle.get("exception_state") != "CLOSED":
        raise RuntimeError("refuse finalization while rerun lifecycle is not CLOSED")
    if lifecycle.get("ordinary_guard_unchanged") is not True:
        raise RuntimeError("ordinary guard hash changed")
    if lifecycle.get("ordinary_guard_verified_rejects_query_after") is not True:
        raise RuntimeError("ordinary guard rejection after close is unverified")
    query_boundary_audit(manifest)

    orchestrator = load_orchestrator()
    completed = orchestrator.landed(manifest)
    entries = [entry for entry, _ in completed]
    rows = [row for _, row in completed]
    combined = orchestrator.combine_rows(rows, require_expected_count=False) if rows else None
    classification = classify_result(
        completed_partitions=len(completed),
        partition_count=len(manifest["entries"]),
        combined=combined,
    )
    jobs = submission_records(manifest)
    receipts = list((RUN / "runs").glob("run_*/receipt.json"))
    results = list((RUN / "runs").glob("run_*/result.csv"))
    if len(receipts) != len(completed) or len(results) != len(completed):
        raise RuntimeError("landed artifact count mismatch")

    landed_partitions = []
    for entry, row in completed:
        run_dir = Path(entry["run_dir"])
        receipt = json.loads((run_dir / "receipt.json").read_text())
        landed_partitions.append(
            {
                "brickid_range": {"lo": entry["lo"], "hi": entry["hi"]},
                "query_sha256": entry["query_sha256"],
                "result_sha256": receipt["result_sha256"],
                "receipt_sha256": sha(run_dir / "receipt.json"),
                "job_url": receipt["job_url"],
                "n_cut6_dered": row["n_cut6_dered"],
                "sum_cos_theta": str(row["sum_cos_theta"]),
                "sum_cos2_theta": str(row["sum_cos2_theta"]),
            }
        )

    outcome = {
        "created_utc": now(),
        **classification,
        "stop_reason": status.get("stop_reason"),
        "threshold": "0.15",
        "population": "frozen dered Cut-6",
        "expected_population_count_from_count_certificate": EXPECTED_POPULATION_COUNT,
        "partition_count": len(manifest["entries"]),
        "completed_partitions": len(completed),
        "completed_keyspace_units": sum(entry["key_count"] for entry in entries),
        "full_keyspace_units": 662174,
        "coverage_is_full_footprint": len(completed) == len(manifest["entries"]),
        "combined_moments": decimal_strings(combined),
        "landed_partitions": landed_partitions,
        "submission_records": len(jobs),
        "unique_job_urls": len(jobs),
        "jobs": jobs,
        "result_csv_count": len(results),
        "receipt_json_count": len(receipts),
        "guard_state": lifecycle["exception_state"],
        "ordinary_guard_sha256_before": lifecycle["ordinary_guard_sha256_before"],
        "ordinary_guard_sha256_after": lifecycle["ordinary_guard_sha256_after"],
        "ordinary_guard_unchanged": lifecycle["ordinary_guard_unchanged"],
        "ordinary_guard_verified_rejects_query_after": lifecycle["ordinary_guard_verified_rejects_query_after"],
        "object_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "angle_bins": 0,
        "sky_maps": 0,
        "dipole_amplitudes": 0,
        "extra_directional_outputs": 0,
        "publication_acceptance_commit_push": 0,
        "hashes": {
            "manifest": sha(MANIFEST_PATH),
            "source_manifest": manifest["source_manifest_sha256"],
            "status": sha(STATUS_PATH),
            "guard_lifecycle": sha(LIFECYCLE_PATH),
            "global_attempt_history": sha(PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"),
            "partition_attempt_history": sha(PREREG / "TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md"),
            "orchestrator": sha(ORCHESTRATOR_PATH),
            "worker": sha(ROOT / "run_footprint_variance_partition_rerun.py"),
        },
    }
    OUTPUT.write_text(json.dumps(outcome, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(OUTPUT),
                "sha256": sha(OUTPUT),
                "status": outcome["status"],
                "threshold_verdict": outcome["threshold_verdict"],
                "completed_partitions": outcome["completed_partitions"],
                "jobs": outcome["unique_job_urls"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
