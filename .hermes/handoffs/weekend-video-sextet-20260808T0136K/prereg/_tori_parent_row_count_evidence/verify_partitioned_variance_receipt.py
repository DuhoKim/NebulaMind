#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
RUN = ROOT / "footprint_variance_partitioned_20260813"
RECEIPT = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
OUTCOME = RUN / "FINAL_OUTCOME_20260814.json"
ATTEMPT = PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    o = json.loads(OUTCOME.read_text())
    receipt = RECEIPT.read_text()
    assert o["status"] == "UNRESOLVED"
    assert o["threshold_verdict"] == "NONE"
    assert o["completed_partitions"] == 0
    assert o["completed_keyspace_units"] == 0
    assert o["aggregate_result_rows"] == 0
    assert o["mean_cos_theta"] is None
    assert o["var_pop_cos_theta"] is None
    assert o["guard_state"] == "CLOSED"
    assert o["ordinary_guard_unchanged"] is True
    assert o["ordinary_guard_verified_rejects_query_after"] is True
    assert o["submission_records"] == 9
    assert o["unique_job_urls"] == 9
    assert o["lost_jobs_404_after_pressure"] == 8
    assert o["deadline_aborted_jobs"] == 1
    assert sha(ATTEMPT) == "ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e"
    assert o["hashes"]["attempt_history"] == sha(ATTEMPT)

    required = (
        "UNRESOLVED — PARTITIONED RE-RUN REACHED THE 06:00 KST DEADLINE WITH ZERO LANDED PARTITIONS",
        "**Threshold verdict:** **NONE",
        "0 of 67 partitions / 0 of 662,174 BRICKID keyspace units",
        "not a below-threshold result and not a pass",
        "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md",
        sha(ATTEMPT),
        "832,393",
        "not** a returned contributing count",
        "mean(cos theta)`: **UNMEASURED",
        "var(cos theta)`: **UNMEASURED",
        "BRICKID keyspace is not sky area",
        "Nine unique partition UWS jobs",
        "LOST_404_AFTER_502",
        "deadline-aborted and rechecked `ABORTED`: **1**",
        "landed result CSVs: **0**",
        "partition receipts: **0**",
        "exception state: **CLOSED**",
        "hashes identical: **YES**",
        "active Python variance processes after close: **0**",
        "disabled refusal stub",
        "object rows exported: **0**",
        "positions exported: **0**",
        "chirality computed: **0**",
        "handedness fields joined or referenced: **0**",
        "spin or CW/CCW fields joined or referenced: **0**",
        "dipole amplitude computed: **0**",
        "publication/acceptance/commit/push: **0**",
        o["hashes"]["manifest"],
        o["hashes"]["status"],
        o["hashes"]["guard_lifecycle"],
        o["hashes"]["job_reconciliation"],
        sha(OUTCOME),
    )
    for literal in required:
        assert literal in receipt, literal
    for range_key, attempts in o["attempts_by_range"].items():
        for attempt in attempts:
            assert attempt["job_url"].split("/")[-1] in receipt
            assert attempt["query_sha256"] in receipt
    forbidden = (
        "**Threshold verdict:** **PASS",
        "**Threshold verdict:** **FAIL",
        "VARIANCE REQUIREMENT: PASS",
        "VARIANCE REQUIREMENT: FAIL",
        "measured variance",
        "aggregate moment rows returned: **1**",
    )
    for literal in forbidden:
        assert literal not in receipt, literal
    print(
        "partitioned_variance_receipt_verification=PASS "
        "status=UNRESOLVED submissions=9 lost=8 aborted=1 results=0 guard=CLOSED"
    )


if __name__ == "__main__":
    main()
