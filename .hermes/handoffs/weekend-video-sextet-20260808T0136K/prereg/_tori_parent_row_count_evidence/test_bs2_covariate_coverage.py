#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "run_bs2_covariate_coverage.py"

spec = importlib.util.spec_from_file_location("bs2_coverage", TARGET)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load BS-2 coverage module")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.SUBMISSION_CLOSED is True
ranges = module.ranges()
assert len(ranges) == 67
assert ranges[0] == (1, 10000)
assert ranges[-1] == (660001, 662174)

query = module.render_query(*ranges[0])
module.validate_query(query, *ranges[0])
upper = " ".join(query.upper().split())
assert "GROUP BY" not in upper
assert "T.RA" not in upper and "T.DEC" not in upper
assert "IMAGE" not in upper and "CHIRAL" not in upper and "MORPHOLOGY" not in upper
assert "ARM_CONTRAST" not in upper and "N_ARM" not in upper
assert not any(token in upper for token in ("SIN(", "COS(", "RADIANS(", "COSTHETA"))
for alias in module.RESULT_COLUMNS:
    assert f" AS {alias.upper()}" in upper
where_clause = query.split("\nWHERE ", 1)[1]
for predicate in module.REQUIRED_PREDICATES:
    assert where_clause.count(predicate) == 1

sample = [
    dict(
        zip(
        module.RESULT_COLUMNS,
        map(str, [100, 100, 100, 100, 97, 100, 100, 100]),
        )
    )
]
summary = module.reduce_rows(sample)
assert summary["population"] == 100
assert summary["coverage"]["colour"]["count"] == 97
assert summary["coverage"]["colour"]["fraction"] == 0.97
assert summary["coverage"]["extinction"]["count"] == 100
assert summary["sample_rows_exported"] == 0
assert summary["positions_exported"] == 0
print("bs2_covariate_coverage_contract=PASS partitions=67 aggregate_rows=67 object_rows=0 positions=0")
