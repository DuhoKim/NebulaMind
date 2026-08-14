#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
SCOPE = ROOT / "footprint_variance_20260813"
RUN = SCOPE / "run"
QUERY = SCOPE / "query.adql"
RECEIPT = PREREG / "TORI_FOOTPRINT_VARIANCE_RECEIPT.md"
ORDINARY = ROOT / "run_aggregate_tap.py"
DISABLED = ROOT / "run_authorized_footprint_variance.py"
EXPECTED_QUERY = "5d4c7812331419eff0ec7dca4e40f690203cb94cc71b6309d7b8694299249ff1"
EXPECTED_ORDINARY = "228a045a9c896ca7bef6dc199e5988bbd0d222e5c027cdee3c1d6d23842a1a51"
EXPECTED_EXECUTED = "0ffeb0d79f0b70faa37b0e0ef17db52988adba9516163b409c663e4c349bd826"
EXPECTED_DISABLED = "5ff98618c6d8dd8ed1f19d2ba7843fe94ce78af503247212df2ce8a6d1d91de9"
EXPECTED_ROUTE = "3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87"
EXPECTED_CUT6 = "ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651"
EXPECTED_FULL = "9d62960718b4f7aa1bb2eb67a9fddb83d6712698e1bc323fb1d21d1f4965e020"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_ordinary():
    spec = importlib.util.spec_from_file_location("ordinary", ORDINARY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    for path in (QUERY, RUN / "submission.json", RUN / "abort_receipt.json", RUN / "aborted_job.xml", RUN / "guard_lifecycle.json", RUN / "execution_runner.py.txt", ORDINARY, DISABLED, RECEIPT):
        assert path.exists(), path
    assert sha(QUERY) == EXPECTED_QUERY
    assert sha(ORDINARY) == EXPECTED_ORDINARY
    assert sha(RUN / "execution_runner.py.txt") == EXPECTED_EXECUTED
    assert sha(DISABLED) == EXPECTED_DISABLED
    assert sha(PREREG / "TORI_SURVEY_ROUTE_BINDING_20260812.md") == EXPECTED_ROUTE
    assert sha(PREREG / "TORI_CUT6_INCLINATION_COUNT_20260812.md") == EXPECTED_CUT6
    assert sha(PREREG / "TORI_FULL_KEYSPACE_SWEEP_20260813.md") == EXPECTED_FULL
    assert sha(RUN / "submission.json") == "b8a11ab632131d2daebc08d48a0c92d0d63a9695bee5b5e540bd722baca79912"
    assert sha(RUN / "abort_receipt.json") == "c49d43f81c3f245bb349b7b69c77a7d319a6849c273866933a17a243fc73483b"
    assert sha(RUN / "aborted_job.xml") == "7f762a6ca94152b8d2026c7c2e3af755431bcff6fe554ae64bb8833126bd2b80"
    assert sha(RUN / "guard_lifecycle.json") == "af8f71f5dcb1a4a965a175b828919c4751f390cc2a70e27f15d8666ec6bd22ab"

    query = QUERY.read_text()
    assert "WHERE t.brickid BETWEEN 1 AND 662174" in query
    assert query.count("POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551") == 1
    assert query.upper().count("SELECT") == 1 and "GROUP BY" not in query.upper()
    assert not re.search(r"\b(CHIRALITY|HANDEDNESS|CLOCKWISE|COUNTERCLOCKWISE|CW_CCW|DIPOLE_AMPLITUDE)\b", query.upper())
    try:
        load_ordinary().validate_aggregate_only(query)
    except ValueError as exc:
        assert "sky-statistic/trigonometric construct forbidden" in str(exc)
    else:
        raise AssertionError("ordinary guard no longer rejects variance query")

    submission = json.loads((RUN / "submission.json").read_text())
    abort = json.loads((RUN / "abort_receipt.json").read_text())
    lifecycle = json.loads((RUN / "guard_lifecycle.json").read_text())
    assert submission["submission_attempts"] == submission["submission_limit"] == 1
    assert submission["query_sha256"] == abort["query_sha256"] == EXPECTED_QUERY
    assert submission["job_url"] == abort["job_url"] == "https://datalab.noirlab.edu/tap/async/v0d4e15lm8hkz7zv"
    assert abort["phase_before_abort"] == "EXECUTING"
    assert abort["phase_after_abort"] == "ABORTED"
    assert abort["result_retrieved"] is False
    assert abort["aggregate_result_rows_exported"] == 0
    assert abort["sample_rows_exported"] == abort["positions_exported"] == 0
    assert abort["chirality_computed"] is False and abort["handedness_joined_or_referenced"] is False
    assert lifecycle["exception_state"] == "CLOSED"
    assert lifecycle["ordinary_guard_sha256_before"] == lifecycle["ordinary_guard_sha256_after"] == EXPECTED_ORDINARY
    assert lifecycle["ordinary_guard_unchanged"] is True
    assert lifecycle["ordinary_guard_verified_rejects_query_before"] is True
    assert lifecycle["ordinary_guard_verified_rejects_query_after"] is True
    assert lifecycle["exception_runner_disabled"] is True
    assert lifecycle["exception_runner_execution_sha256"] == EXPECTED_EXECUTED
    assert lifecycle["exception_runner_disabled_sha256"] == EXPECTED_DISABLED
    assert not list(SCOPE.rglob("result.csv"))
    assert not (RUN / "receipt.json").exists()
    assert not (SCOPE / "partitioned").exists()

    disabled_source = DISABLED.read_text()
    assert "DISABLED" in disabled_source and "SystemExit" in disabled_source
    assert "urllib" not in disabled_source and "requests" not in disabled_source

    md = RECEIPT.read_text()
    required = (
        "UNRESOLVED — ONE AUTHORIZED QUERY ABORTED WITHOUT A RESULT",
        "**Threshold verdict:** **NONE — no moments were returned**",
        "03:09:56",
        "This is not a failing below-threshold result",
        "No replacement global query and no partition query was submitted",
        "BRICKID keyspace is not sky area",
        "aggregate rows returned: **0**",
        "sample rows exported: **0**",
        "positions exported: **0**",
        "chirality computed: **0**",
        "handedness joined or referenced: **0**",
        "partition queries submitted: **0**",
        "exception state: **CLOSED**",
        EXPECTED_QUERY,
        EXPECTED_ORDINARY,
        EXPECTED_EXECUTED,
        EXPECTED_DISABLED,
        EXPECTED_ROUTE,
        EXPECTED_CUT6,
        EXPECTED_FULL,
        submission["job_url"],
    )
    for literal in required:
        assert literal in md, literal
    assert "Kun BS-1 variance verdict: PASS" not in md
    assert "Kun BS-1 variance verdict: FAIL" not in md
    assert "var_pop_cos_theta =" not in md
    print("footprint_variance_receipt_verification=PASS status=UNRESOLVED submissions=1 results=0 guard=CLOSED")


if __name__ == "__main__":
    main()
