#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
CANARY = ROOT / "footprint_variance_canary_20260814"
RECEIPT = PREREG / "TORI_FOOTPRINT_VARIANCE_CANARY_RECEIPT_20260814.md"
VARIANCE = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
SUBMITTER = ROOT / "run_footprint_variance_canary.py"
MONITOR = ROOT / "monitor_footprint_variance_canary.py"
COUNT_LOWER = ROOT / "cut6_fixed_000001_121000/runs/run_000001_001000/tap/result.csv"
COUNT_SUPERSET = ROOT / "cut6_fixed_000001_121000/runs/run_001001_011000/tap/result.csv"
EXPECTED_VARIANCE_SHA = "f26b507a2c28ec310d305877fdc5e24dcf0b09c5b7b4a3d2fa7970a79730c289"
EXPECTED_QUERY_SHA = "0d626704d44d8be36f6f3de45c57ad3eb377e9e5ec53608f01b11393560cbd98"
EXPECTED_GUARD_SHA = "228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def one_row(path: Path) -> dict[str, str]:
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1
    return rows[0]


def main() -> None:
    submission = json.loads((CANARY / "submission.json").read_text())
    lifecycle = json.loads((CANARY / "guard_lifecycle.json").read_text())
    launch = json.loads((CANARY / "LAUNCH_AUTHORIZATION.json").read_text())
    pattern = json.loads((CANARY / "SERVICE_STALL_PATTERN_20260814.json").read_text())
    initial = json.loads((CANARY / "INITIAL_POLL_SNAPSHOT_20260814.json").read_text())
    receipt = RECEIPT.read_text()

    assert sha(VARIANCE) == EXPECTED_VARIANCE_SHA
    assert submission["query_sha256"] == EXPECTED_QUERY_SHA
    assert submission["submission_attempts"] == 1
    assert submission["canary_only"] is True
    assert submission["full_manifest_auto_launches"] == 0
    assert submission["brickid_range"]["lo"] == 1
    assert submission["brickid_range"]["hi"] == 10000
    assert len(list(CANARY.glob("**/submission.json"))) == 1
    assert lifecycle["exception_state"] == "CLOSED"
    assert lifecycle["submissions_made"] == lifecycle["submission_limit"] == 1
    assert lifecycle["ordinary_guard_sha256_before"] == EXPECTED_GUARD_SHA
    assert lifecycle["ordinary_guard_sha256_after"] == EXPECTED_GUARD_SHA
    assert lifecycle["ordinary_guard_unchanged"] is True
    assert lifecycle["ordinary_guard_verified_rejects_query_before"] is True
    assert lifecycle["ordinary_guard_verified_rejects_query_after"] is True
    assert lifecycle["submitter_sha256"] == sha(CANARY / "executed_code_custody/run_footprint_variance_canary.py.txt")
    assert launch["submission_limit"] == 1
    assert launch["full_manifest_auto_launches_authorized"] == 0
    assert launch["variance_receipt_sha256_before"] == EXPECTED_VARIANCE_SHA
    assert initial["observations"] == [
        {"kind": "PHASE", "phase": "PENDING", "timestamp_utc": "2026-08-14T02:45:03Z"}
    ]
    assert len(pattern["stall_modes"]) == 2
    assert pattern["stall_modes"][0]["mode"] == "HTTP_502_THEN_REMOTE_404"
    assert pattern["stall_modes"][1]["mode"] == "HTTP_200_BUT_SCHEDULER_PENDING"
    assert pattern["stall_modes"][1]["facts"]["queue_stall_seconds"] == 2700

    lower = int(one_row(COUNT_LOWER)["n_cut6_inclination_dered"])
    superset = int(one_row(COUNT_SUPERSET)["n_cut6_inclination_dered"])
    assert lower == 2583 and superset == 23881 and lower + superset == 26464

    submitter_source = SUBMITTER.read_text()
    assert "Canary submission path is CLOSED after its one authorized POST" in submitter_source
    monitor_source = MONITOR.read_text()
    assert "doQuery" not in monitor_source
    assert 'method="POST"' not in monitor_source
    assert "run_partitioned_footprint_variance.py" not in monitor_source

    required = (
        "The 45-minute abort was the right call",
        "exactly `2700` seconds",
        "UWS job: `https://datalab.noirlab.edu/tap/async/k6fqyi9nuzfds6pt`",
        EXPECTED_QUERY_SHA,
        "initial phase: `PENDING`",
        "GET-only every 300 seconds",
        "leaves the remote job parked without an abort",
        "2583 <= n(1…10000) <= 26464",
        "state: **CLOSED**",
        "submissions made / limit: `1/1`",
        "live POST path: **DISABLED AFTER ONE SUBMISSION**",
        "Two service-stall modes observed locally in under one day",
        "HTTP_502_THEN_REMOTE_404",
        "HTTP_200_BUT_SCHEDULER_PENDING",
        "endpoint HTTP 200 proves reachability, not scheduler throughput",
        "Scientific variance state:** **UNRESOLVED — THRESHOLD VERDICT NONE",
        "variance receipt superseded by canary: **NO**",
        "UWS canary submissions: **1**",
        "replacement submissions: **0**",
        "full-manifest auto-launches: **0**",
        "object rows exported: **0**",
        "positions exported: **0**",
        "chirality computed: **0**",
        "handedness, spin, or CW/CCW fields joined or referenced: **0**",
        "dipole amplitude computed: **0**",
        "publication/acceptance/commit/push: **0**",
        sha(CANARY / "LAUNCH_AUTHORIZATION.json"),
        sha(CANARY / "submission.json"),
        sha(CANARY / "guard_lifecycle.json"),
        sha(CANARY / "INITIAL_POLL_SNAPSHOT_20260814.json"),
        sha(CANARY / "SERVICE_STALL_PATTERN_20260814.json"),
        EXPECTED_VARIANCE_SHA,
    )
    for literal in required:
        assert literal in receipt, literal
    forbidden = (
        "THRESHOLD VERDICT PASS",
        "THRESHOLD VERDICT FAIL",
        "full footprint variance measured",
        "full-manifest auto-launches: **1**",
        "variance receipt superseded by canary: **YES**",
    )
    for literal in forbidden:
        assert literal not in receipt, literal
    print(
        "footprint_variance_canary_receipt_verification=PASS "
        "submissions=1 initial_phase=PENDING guard=CLOSED full_auto_launches=0 variance=UNRESOLVED"
    )


if __name__ == "__main__":
    main()
