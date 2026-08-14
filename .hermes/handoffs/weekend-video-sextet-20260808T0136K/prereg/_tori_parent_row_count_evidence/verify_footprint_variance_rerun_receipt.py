#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
RUN = ROOT / "footprint_variance_partitioned_rerun_20260814"
OUTCOME_PATH = RUN / "FINAL_OUTCOME_20260814_RERUN.json"
RECEIPT = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
GLOBAL_HISTORY = PREREG / "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md"
PARTITION_HISTORY = PREREG / "TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    outcome = json.loads(OUTCOME_PATH.read_text())
    receipt = RECEIPT.read_text()
    assert sha(GLOBAL_HISTORY) == "ef995652531d35cf3dc68df542661f9c503b571be9d34e4423de0347c63bf20e"
    assert sha(PARTITION_HISTORY) == "f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289"
    assert outcome["guard_state"] == "CLOSED"
    assert outcome["ordinary_guard_unchanged"] is True
    assert outcome["ordinary_guard_verified_rejects_query_after"] is True
    assert outcome["object_rows_exported"] == 0
    assert outcome["positions_exported"] == 0
    assert outcome["images_requested"] == 0
    assert outcome["angle_bins"] == 0
    assert outcome["sky_maps"] == 0
    assert outcome["dipole_amplitudes"] == 0
    assert outcome["extra_directional_outputs"] == 0
    assert outcome["publication_acceptance_commit_push"] == 0

    required = (
        "same frozen dered Cut-6 population",
        "same 67 disjoint BRICKID partitions",
        "BRICKID keyspace is not sky area",
        "TORI_FOOTPRINT_VARIANCE_ATTEMPT_20260813.md",
        sha(GLOBAL_HISTORY),
        "TORI_FOOTPRINT_VARIANCE_PARTITIONED_ATTEMPT_20260814.md",
        sha(PARTITION_HISTORY),
        sha(OUTCOME_PATH),
        "exception state: **CLOSED**",
        "hashes identical: **YES**",
        "independently verified to reject the query after close: **YES**",
        "exception entry points are disabled refusal stubs",
        "object rows exported: **0**",
        "positions exported: **0**",
        "images requested: **0**",
        "angle bins: **0**",
        "sky maps: **0**",
        "dipole amplitudes: **0**",
        "extra directional outputs: **0**",
        "publication/acceptance/commit/push: **0**",
        "No chirality, handedness, spin, CW/CCW",
    )
    for literal in required:
        assert literal in receipt, literal
    for digest in outcome["hashes"].values():
        assert digest in receipt, digest
    for row in outcome["jobs"]:
        assert row["job_url"].rstrip("/").split("/")[-1] in receipt
        assert row["query_sha256"] in receipt
    for row in outcome["landed_partitions"]:
        assert row["result_sha256"] in receipt

    status = outcome["status"]
    verdict = outcome["threshold_verdict"]
    if status == "COMPLETE":
        assert verdict in {"PASS", "FAIL"}
        assert "FULL RESULT:" in receipt
        variance = outcome["combined_moments"]["var_pop_cos_theta"]
        assert variance in receipt
        if verdict == "FAIL":
            assert "real below-threshold result" in receipt
    else:
        assert verdict == "NONE"
        assert "**Threshold verdict:** **NONE**" in receipt
        assert "FULL RESULT:" not in receipt
        assert "Threshold verdict:** **PASS" not in receipt
        assert "Threshold verdict:** **FAIL" not in receipt
        assert "do not pass or fail 0.15" in receipt or "neither a pass nor a below-threshold failure" in receipt
    print(
        f"footprint_variance_rerun_receipt_verification=PASS status={status} "
        f"verdict={verdict} jobs={outcome['unique_job_urls']} landed={outcome['completed_partitions']}"
    )


if __name__ == "__main__":
    main()
