#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "render_cut6_receipt.py"


def load_target():
    spec = importlib.util.spec_from_file_location("cut6_receipt", TARGET)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Cut 6 receipt renderer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    renderer = load_target()
    manifest = {
        "coverage": {
            "start_brickid": 1,
            "stop_brickid": 121000,
            "keyspace_total": 662174,
            "keyspace_fraction": 121000 / 662174,
            "keyspace_not_sky_area": True,
        },
        "threshold_expression": "POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551",
        "partition_count": 13,
        "entries": [],
    }
    partial_rows = [
        {
            "lo": 1,
            "hi": 1000,
            "elapsed_seconds": 12.5,
            "job_url": "https://datalab.noirlab.edu/tap/async/example",
            "query_sha256": "a" * 64,
            "result_sha256": "b" * 64,
            "n_cut5_parent_raw": 2111,
            "n_cut5_parent_dered": 3002,
            "n_cut6_inclination_raw": 1900,
            "n_cut6_inclination_dered": 2700,
        }
    ]
    partial = renderer.render_document(manifest, {"stop_reason": None}, partial_rows)
    for text in [
        "Cut 6 inclination count — fixed-range aggregate receipt",
        "PARTIAL LOWER BOUND",
        "BRICKID keyspace, not sky area",
        "1…121000",
        "18.273143%",
        "POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551",
        "Objects with `e >= 1` fail this threshold directly",
        "1…1000",
        "12.5",
        "2,111",
        "3,002",
        "1,900",
        "2,700",
        "No density, keyspace, or sky-area extrapolation",
        "sample rows exported: **0**",
        "positions exported: **0**",
        "trigonometric or axis-relative terms: **0**",
        "Independent reconstruction",
    ]:
        assert text in partial, text
    assert "COMPLETE FIXED-RANGE LOWER BOUND" not in partial

    complete_rows = partial_rows * 13
    complete = renderer.render_document(
        manifest, {"stop_reason": "fixed_range_1_121000_complete"}, complete_rows
    )
    assert "COMPLETE FIXED-RANGE LOWER BOUND" in complete
    assert "same frozen coverage as the Cut 5 certificate" in complete
    assert "does not reopen or extend the stopped sweep" in complete
    assert "accepted yield" in complete
    print("cut6_receipt_test=PASS")


if __name__ == "__main__":
    main()
