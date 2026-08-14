#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
PACKET = PREREG / "TORI_BS1_CLOSURE_PACKET.md"
VARIANCE = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
OUTCOME = ROOT / "footprint_variance_partitioned_20260813/FINAL_OUTCOME_20260814.json"
EXPECTED = {
    "KUN_PREREG_DRAFT_GATE_20260812.md": "5d726380d64e34a1188a5bfb0b080962008bc80746e86fc5e39bde75a6264dff",
    "TORI_SURVEY_ROUTE_BINDING_20260812.md": "3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87",
    "TORI_PARENT_ROW_COUNT_20260812.md": "df9357085d4cfd35320ab34346a1fb3080dc1e5ba1e3d86e2dc6231dbbf534f3",
    "TORI_CUT6_INCLINATION_COUNT_20260812.md": "ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651",
    "TORI_FULL_KEYSPACE_SWEEP_20260813.md": "9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020",
    "YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md": "b4e2f5b5f92fc881ec2a0a35e84515fd05057c1051bff516cad7acae3609e18a",
    "YUI_INCLINATION_RETENTION_REMEASURE_20260812.md": "012cb5fd677e6a77427b592b362796f71fa837b7ccd93248559c48709e1e1073",
    "LANA_SPIRAL_FRACTION_SOURCED_20260812.md": "46e10c6a028d2a2047b6af1c2103b38337f93fc5ccc8466c3f61ff1045214bef",
    "GORU_ACCEPTED_YIELD_RECEIPT_20260812.md": "bbe3bbaaedb7efaacb9bf1f214094115464dac81c9339df18e3223ff3dac9172",
}
KUN_BULLETS = (
    "exact DR10/DR10.1 product paths or records",
    "exact frozen parent cuts",
    "actual queried surviving counts after each cut, not only plausible extrapolation",
    "actual footprint variance around Longo's axis, meeting `var(cos theta) >= 0.15`",
    "actual parent count multiplied by measured BS-3 lower-bound retention, yielding `N_accepted >= 100,000`",
    "licence statement permitting derived-catalogue publication",
    "query/code receipt with hash and rerunnable command or script",
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    assert PACKET.exists()
    assert VARIANCE.exists()
    assert OUTCOME.exists()
    for name, digest in EXPECTED.items():
        path = PREREG / name
        assert path.exists(), path
        assert sha(path) == digest, f"source drift: {name}"
    o = json.loads(OUTCOME.read_text())
    assert o["status"] == "UNRESOLVED"
    assert o["threshold_verdict"] == "NONE"
    assert o["completed_partitions"] == 0
    assert o["aggregate_result_rows"] == 0
    assert o["guard_state"] == "CLOSED"

    getcontext().prec = 50
    exact_yield = Decimal(832393) * Decimal("0.1823") * Decimal("0.8572")
    assert exact_yield == Decimal("130076.02307108")

    packet = PACKET.read_text()
    for bullet in KUN_BULLETS:
        assert bullet in packet, bullet
    for name, digest in EXPECTED.items():
        assert name in packet, name
        assert digest in packet, digest
    assert sha(VARIANCE) in packet
    assert sha(OUTCOME) in packet
    for digest in o["hashes"].values():
        assert digest in packet, digest

    required = (
        "Campaign five-item status:** **4 CLOSED / 1 UNRESOLVED",
        "VARIANCE REQUIREMENT: UNRESOLVED — THRESHOLD VERDICT NONE",
        "OVERALL KUN BS-1 STATUS: HOLD — NOT CLOSED",
        "0 landed partitions and 0 returned moments",
        "Nothing published, accepted, committed, or pushed",
        "1,015,881",
        "832,393",
        "81.700580%",
        "BRICKID keyspace is not sky area",
        "0 of 67",
        "0 of 662,174",
        "UNMEASURED",
        "Nine unique UWS jobs",
        "eight were lost after HTTP 502",
        "not a failing below-threshold result and not a pass",
        "130,076.02307108",
        "130,076 ≥ 100,000",
        "96.15%",
        "SUPERSEDED",
        "85.72%",
        "AUTHORITATIVE",
        "Derived-catalogue publication licence — OPEN",
        "execution permission CLOSED",
        "aggregate variance rows returned: **0**",
        "sample rows exported: **0**",
        "positions exported: **0**",
        "chirality computed: **0**",
        "handedness joined or referenced: **0**",
        "spin or CW/CCW fields joined or referenced: **0**",
        "publication/acceptance/commit/push: **0**",
    )
    for literal in required:
        assert literal in packet, literal
    forbidden = (
        "five campaign blockers: CLOSED",
        "Campaign five-item status:** **CLOSED",
        "VARIANCE REQUIREMENT: PASS",
        "VARIANCE REQUIREMENT: FAIL",
        "actual footprint variance — CLOSED",
        "BS-1 fully closed",
        "all seven closed",
        "aggregate variance rows returned: **1**",
    )
    for literal in forbidden:
        assert literal not in packet, literal
    for line in packet.splitlines():
        if "SHA-256" in line:
            assert "..." not in line and "…" not in line, line
    print(
        "bs1_closure_packet_verification=PASS overall=HOLD "
        "campaign=4_closed_1_unresolved kun_variance=UNRESOLVED licence=OPEN"
    )


if __name__ == "__main__":
    main()
