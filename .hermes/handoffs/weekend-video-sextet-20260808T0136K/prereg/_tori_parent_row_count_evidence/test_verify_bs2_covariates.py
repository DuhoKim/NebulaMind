#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import hashlib
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "verify_bs2_covariates.py"
spec = importlib.util.spec_from_file_location("verify_bs2", TARGET)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load BS-2 verifier")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.worst_case_accepted_coverage(832393, 831159, 100000) == 0.98766
assert module.worst_case_accepted_coverage(832393, 832393, 100000) == 1.0
assert module.worst_case_accepted_coverage(832393, 827393, 100000) == 0.95
assert module.worst_case_accepted_coverage(832393, 827392, 100000) < 0.95

available = {
    "imaging_depth": 831159,
    "seeing_psf": 831173,
    "galactic_extinction": 832393,
    "stellar_density": 832393,
    "crowding": 832393,
    "angular_size": 832393,
    "axis_ratio": 832393,
    "colour_g_minus_r": 830000,
    "magnitude_r": 832393,
    "arm_contrast": 0,
}
products = {name: True for name in available}
products["arm_contrast"] = False
matrix = module.build_core_matrix(832393, 100000, available, products)
assert len(matrix) == 10
assert sum(row["survives"] for row in matrix) == 9
assert next(row for row in matrix if row["covariate"] == "arm_contrast")["drop_reason"] == "product_not_defined"
assert next(row for row in matrix if row["covariate"] == "colour_g_minus_r")["worst_case_accepted_coverage"] == 0.97607

with tempfile.TemporaryDirectory() as temporary:
    scope = Path(temporary)
    entries = []
    values = [
        [60, 60, 60, 60, 58, 60, 60, 60],
        [40, 40, 40, 40, 39, 40, 40, 40],
    ]
    for index, row_values in enumerate(values):
        query_path = scope / f"query_{index}.adql"
        projections = ", ".join(f"COUNT(*) AS {name}" for name in module.DIRECT_RESULT_COLUMNS)
        query_path.write_text(f"SELECT {projections} FROM table_name\n")
        tap = scope / f"run_{index}" / "tap"
        tap.mkdir(parents=True)
        result = ",".join(module.DIRECT_RESULT_COLUMNS) + "\n" + ",".join(map(str, row_values)) + "\n"
        result_path = tap / "result.csv"
        result_path.write_text(result)
        receipt = {
            "query_sha256": hashlib.sha256(query_path.read_bytes()).hexdigest(),
            "result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
            "result_columns": module.DIRECT_RESULT_COLUMNS,
            "result_row_count": 1,
            "sample_rows_exported": 0,
            "positions_exported": 0,
            "images_requested": 0,
            "chirality_computed": False,
            "sky_statistics_computed": False,
        }
        (tap / "receipt.json").write_text(json.dumps(receipt))
        entries.append({
            "query_path": str(query_path),
            "query_sha256": receipt["query_sha256"],
            "run_dir": str(tap.parent),
        })
    (scope / "manifest.json").write_text(json.dumps({"partition_count": 2, "entries": entries}))
    independent = module.independent_direct_census(scope)
    assert independent["partition_count"] == 2
    assert independent["aggregate_rows_returned"] == 2
    assert independent["population"] == 100
    assert independent["coverage"]["colour"]["count"] == 97
print("bs2_independent_verifier_contract=PASS threshold=0.95 minimum_accepted=100000")
