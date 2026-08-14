#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
RUN = ROOT / "footprint_variance_partitioned_20260813"
OUT = RUN / "FINAL_OUTCOME_20260814.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads((RUN / "manifest.json").read_text())
    status = json.loads((RUN / "status.json").read_text())
    guard = json.loads((RUN / "guard_lifecycle.json").read_text())
    reconciliation = json.loads((RUN / "FINAL_JOB_RECONCILIATION_20260814.json").read_text())
    attempt_history = PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"
    orchestrator_custody = RUN / "executed_code_custody/run_partitioned_footprint_variance.py.txt"
    worker_custody = RUN / "executed_code_custody/run_footprint_variance_partition.py.txt"

    assert len(manifest["entries"]) == 67
    assert manifest["coverage"] == {"lo": 1, "hi": 662174}
    assert status["stop_reason"] == "deadline_reached"
    assert status["completed_partitions"] == 0
    assert status["completed_keyspace_units"] == 0
    assert status["partial_running_totals"] is None
    assert guard["exception_state"] == "CLOSED"
    assert guard["ordinary_guard_unchanged"] is True
    assert guard["ordinary_guard_verified_rejects_query_after"] is True
    assert reconciliation["submission_records"] == 9
    assert reconciliation["unique_job_urls"] == 9
    assert reconciliation["archived_lost_attempts"] == 8
    assert reconciliation["deadline_abort_records"] == 1
    assert reconciliation["remote_phase_counts"] == {"200:ABORTED": 1, "404:None": 8}
    assert reconciliation["result_csv_count"] == 0
    assert reconciliation["receipt_json_count"] == 0
    assert sha(attempt_history) == manifest["attempt_history_sha256"]
    assert sha(orchestrator_custody) == manifest["orchestrator_sha256"]
    assert sha(worker_custody) == manifest["worker_sha256"]

    attempts_by_range: dict[str, list[dict[str, object]]] = {}
    for row in reconciliation["rows"]:
        if row["deadline_abort"]:
            lo, hi = 1, 10000
        else:
            r = row["archived_failure"]["brickid_range"]
            lo, hi = int(r["lo"]), int(r["hi"])
        key = f"{lo}-{hi}"
        attempts_by_range.setdefault(key, []).append(
            {
                "job_url": row["job_url"],
                "query_sha256": row["query_sha256"],
                "terminal_custody": "ABORTED" if row["deadline_abort"] else "LOST_404_AFTER_502",
                "remote_checked_phase": row["remote"],
            }
        )

    outcome = {
        "status": "UNRESOLVED",
        "threshold_verdict": "NONE",
        "threshold": "var(cos theta) >= 0.15",
        "population": "frozen dered Cut-6",
        "expected_population_count_from_count_certificate": manifest["expected_population_count"],
        "axis_galactic_degrees": {"l": 52, "b": 68.5},
        "manifest_partition_count": manifest["partition_count"],
        "manifest_coverage": manifest["coverage"],
        "completed_partitions": status["completed_partitions"],
        "completed_keyspace_units": status["completed_keyspace_units"],
        "aggregate_result_rows": reconciliation["result_csv_count"],
        "contributing_count_returned": None,
        "sum_cos_theta_returned": None,
        "sum_cos2_theta_returned": None,
        "mean_cos_theta": None,
        "var_pop_cos_theta": None,
        "stop_reason": status["stop_reason"],
        "deadline_utc": status["deadline_utc"],
        "closed_utc": guard["closed_utc"],
        "guard_state": guard["exception_state"],
        "ordinary_guard_sha256_before": guard["ordinary_guard_sha256_before"],
        "ordinary_guard_sha256_after": guard["ordinary_guard_sha256_after"],
        "ordinary_guard_unchanged": guard["ordinary_guard_unchanged"],
        "ordinary_guard_verified_rejects_query_after": guard["ordinary_guard_verified_rejects_query_after"],
        "submission_records": reconciliation["submission_records"],
        "unique_job_urls": reconciliation["unique_job_urls"],
        "lost_jobs_404_after_pressure": reconciliation["archived_lost_attempts"],
        "deadline_aborted_jobs": reconciliation["deadline_abort_records"],
        "attempts_by_range": attempts_by_range,
        "object_rows_exported": 0,
        "positions_exported": 0,
        "images_requested": 0,
        "chirality_computed": 0,
        "handedness_fields_joined_or_referenced": 0,
        "cw_ccw_fields_joined_or_referenced": 0,
        "dipole_amplitude_computed": 0,
        "sky_maps_or_angle_bins": 0,
        "publication_acceptance_commit_push": 0,
        "hashes": {
            "attempt_history": sha(attempt_history),
            "manifest": sha(RUN / "manifest.json"),
            "status": sha(RUN / "status.json"),
            "guard_lifecycle": sha(RUN / "guard_lifecycle.json"),
            "job_reconciliation": sha(RUN / "FINAL_JOB_RECONCILIATION_20260814.json"),
            "orchestrator_executed": sha(orchestrator_custody),
            "worker_executed": sha(worker_custody),
            "ordinary_guard": guard["ordinary_guard_sha256_after"],
        },
    }
    OUT.write_text(json.dumps(outcome, indent=2, sort_keys=True) + "\n")
    print(f"final_outcome={OUT} sha256={sha(OUT)} status=UNRESOLVED submissions=9 results=0 guard=CLOSED")


if __name__ == "__main__":
    main()
