#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_RUNNER = ROOT / "run_aggregate_tap.py"
QUERY = ROOT / "footprint_variance_20260813" / "query.adql"
EXCEPTION_RUNNER = ROOT / "run_authorized_footprint_variance.py"
EXPECTED_COLUMNS = ["n_cut6_dered", "mean_cos_theta", "var_pop_cos_theta"]
CUT6 = "POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551"
AXIS = (
    "-0.6769717798726208",
    "-0.5098465358556549",
    "0.5308160878610257",
)


def load(path: Path, name: str):
    assert path.exists(), f"missing implementation: {path}"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def aliases(query: str) -> list[str]:
    normalized = " ".join(query.split())
    select = normalized[7 : normalized.upper().index(" FROM ")]
    return re.findall(r"\bAS\s+([A-Za-z_][A-Za-z0-9_]*)\b", select, re.I)


def main() -> None:
    assert QUERY.exists(), f"missing exact query: {QUERY}"
    query_bytes = QUERY.read_bytes()
    query = query_bytes.decode("utf-8")
    digest = hashlib.sha256(query_bytes).hexdigest()

    base = load(BASE_RUNNER, "base_aggregate_runner")
    try:
        base.validate_aggregate_only(query)
    except ValueError as exc:
        assert "sky-statistic/trigonometric construct forbidden" in str(exc)
    else:
        raise AssertionError("ordinary counts-only guard accepted the variance query")

    exception = load(EXCEPTION_RUNNER, "variance_exception_runner")
    assert exception.EXPECTED_QUERY_SHA256 == digest
    assert exception.EXPECTED_COLUMNS == EXPECTED_COLUMNS
    assert exception.ORDINARY_GUARD_PATH == BASE_RUNNER
    exception.validate_exception_query(query_bytes)

    assert aliases(query) == EXPECTED_COLUMNS
    assert query.upper().count("SELECT") == 1
    assert "GROUP BY" not in query.upper()
    assert "SELECT *" not in query.upper()
    assert "WHERE t.brickid BETWEEN 1 AND 662174" in query
    assert query.count(CUT6) == 1
    for literal in AXIS:
        assert literal in query
    for predicate in (
        "t.brick_primary = 1",
        "t.maskbits = 0",
        "t.type <> 'PSF'",
        "t.flux_r > 0",
        "p.z_phot_median >= 0",
        "p.z_phot_median < 0.15",
        "t.dered_mag_r < 17.7",
        "t.shape_r > 1.5",
    ):
        assert query.count(predicate) == 1, predicate
    for population_drift in (
        "t.ra IS NOT NULL",
        "t.dec IS NOT NULL",
        "t.ra >=",
        "t.ra <",
        "t.dec >=",
        "t.dec <=",
    ):
        assert population_drift not in query, population_drift
    assert query.upper().count("COUNT(") == 1
    assert "COUNT(*)" not in query.upper()
    assert query.upper().count("AVG(") == 3
    assert "AVG(POWER(" in query.upper()
    assert "POWER(AVG(" in query.upper()

    forbidden = (
        "CHIRALITY",
        "HANDEDNESS",
        "CLOCKWISE",
        "COUNTERCLOCKWISE",
        "CW_CCW",
        "DIPOLE_AMPLITUDE",
        "GROUP BY",
        "TOP ",
        "LIMIT ",
        "OFFSET ",
        "INTO ",
        "UPLOAD ",
        "CREATE ",
        "DROP ",
        "DELETE ",
        "UPDATE ",
        "INSERT ",
    )
    upper = query.upper()
    for token in forbidden:
        assert token not in upper, token

    mutated = query_bytes.replace(b"0.15", b"0.16", 1)
    assert mutated != query_bytes
    try:
        exception.validate_exception_query(mutated)
    except ValueError as exc:
        assert "query hash" in str(exc)
    else:
        raise AssertionError("exception accepted a mutated query")

    print(f"footprint_variance_exception_contract=PASS query_sha256={digest}")


if __name__ == "__main__":
    main()
