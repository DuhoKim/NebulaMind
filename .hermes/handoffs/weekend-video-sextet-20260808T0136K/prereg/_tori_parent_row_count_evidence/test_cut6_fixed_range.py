#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "run_cut6_fixed_range.py"
EXPECTED_RANGES = [
    (1, 1000),
    (1001, 11000),
    *[(lo, lo + 9999) for lo in range(11001, 111002, 10000)],
]
EXPECTED_COLUMNS = [
    "n_cut5_parent_raw",
    "n_cut5_parent_dered",
    "n_cut6_inclination_raw",
    "n_cut6_inclination_dered",
]
THRESHOLD = "0.1836734693877551"


def load_target():
    spec = importlib.util.spec_from_file_location("cut6", TARGET)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Cut 6 target module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    cut6 = load_target()
    runner = cut6.load_guard()
    assert cut6.RANGES == EXPECTED_RANGES
    assert cut6.RANGES[0][0] == 1
    assert cut6.RANGES[-1][1] == 121000
    assert all(b[0] == a[1] + 1 for a, b in zip(cut6.RANGES, cut6.RANGES[1:]))

    for lo, hi in cut6.RANGES:
        query = cut6.render_query(lo, hi)
        runner(query)
        normalized = " ".join(query.split())
        assert f"WHERE t.brickid BETWEEN {lo} AND {hi}" in normalized
        assert "121001" not in query
        assert "GROUP BY" not in query.upper()
        assert re.search(r"\b(SIN|COS|TAN|RADIANS|DEGREES)\b", query.upper()) is None
        assert "RA" not in {token.upper() for token in re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", query)}
        assert "DEC" not in {token.upper() for token in re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", query)}
        projections = cut6.projected_aliases(query)
        assert projections == EXPECTED_COLUMNS, projections
        assert query.count("POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < " + THRESHOLD) == 2
        assert query.count("AND t.shape_r > 1.5") == 4
        assert query.count("AND t.brick_primary = 1") == 4
        assert query.count("AND t.maskbits = 0") == 4
        assert query.count("AND t.type <> 'PSF'") == 4
        assert query.count("AND t.flux_r > 0") == 4
        assert query.count("AND p.z_phot_median >= 0") == 4
        assert query.count("AND p.z_phot_median < 0.15") == 4
        assert query.count("AND t.mag_r < 17.7") == 2
        assert query.count("AND t.dered_mag_r < 17.7") == 2

    manifest = cut6.build_manifest(dry_run=True)
    assert manifest["coverage"] == {
        "start_brickid": 1,
        "stop_brickid": 121000,
        "keyspace_total": 662174,
        "keyspace_fraction": 121000 / 662174,
        "keyspace_not_sky_area": True,
    }
    assert manifest["partition_count"] == 13
    assert manifest["columns"] == EXPECTED_COLUMNS
    assert manifest["threshold_expression"] == (
        "POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551"
    )
    assert manifest["no_coverage_extension"] is True
    for entry, bounds in zip(manifest["entries"], EXPECTED_RANGES):
        assert (entry["lo"], entry["hi"]) == bounds
        assert Path(entry["query_path"]).name == f"query_{bounds[0]:06d}_{bounds[1]:06d}.adql"
        assert Path(entry["run_dir"]).name == f"run_{bounds[0]:06d}_{bounds[1]:06d}"
        assert len(entry["query_sha256"]) == 64

    print(json.dumps({"status": "PASS", "partitions": 13, "coverage_hi": 121000}))


if __name__ == "__main__":
    main()
