#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "render_remaining_receipt.py"


def load_target():
    assert TARGET.exists(), f"missing implementation: {TARGET}"
    spec = importlib.util.spec_from_file_location("remaining_receipt", TARGET)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_target()
    columns = module.COLUMNS
    baseline = dict(module.BASE_TOTALS)
    row = {column: 10 for column in columns}
    row.update(
        {
            "n_cut1_primary_mask": 1000,
            "n_cut2_extended_flux": 800,
            "n_cut3_photoz": 600,
            "n_cut4_raw_mag": 400,
            "n_cut4_dered_mag": 450,
            "n_cut5_parent_raw": 300,
            "n_cut5_parent_dered": 350,
            "n_cut6_inclination_raw": 240,
            "n_cut6_inclination_dered": 280,
        }
    )
    manifest = {
        "partition_count": 55,
        "remaining_key_count": 541174,
        "stop_rule": {
            "deadline_utc": "2026-08-12T21:00:00Z",
            "deadline_kst": "2026-08-13T06:00:00+09:00",
            "keyspace_exhaustion": 662174,
            "first_of": True,
        },
        "entries": [
            {"lo": 121001, "hi": 131000, "key_count": 10000},
            {"lo": 131001, "hi": 141000, "key_count": 10000},
        ],
    }
    status = {
        "started_utc": "2026-08-12T14:15:00Z",
        "updated_utc": "2026-08-12T14:25:00Z",
        "active_concurrency": 3,
        "totals": {
            "landed_new_partitions": 1,
            "landed_new_keys": 10000,
            "landed_total_keys": 131000,
            "contiguous_new_partitions": 1,
            "contiguous_covered_hi": 131000,
            "all_landed_totals": {column: baseline[column] + row[column] for column in columns},
            "contiguous_totals": {column: baseline[column] + row[column] for column in columns},
        },
    }
    landed = [
        {
            "lo": 121001,
            "hi": 131000,
            "elapsed_seconds": 321.0,
            "values": row,
            "query_sha256": "a" * 64,
            "result_sha256": "b" * 64,
        }
    ]
    text = module.render_text(manifest, status, landed)
    required = [
        "RUNNING LOWER BOUND",
        "131,000 of 662,174 BRICKID keyspace units counted",
        "Contiguous completed frontier: `BRICKID 1…131000`",
        "19.783320%",
        "121001…131000",
        "321.0",
        f"{baseline['n_cut1_primary_mask'] + 1000:,}",
        f"{baseline['n_cut5_parent_raw'] + 300:,}",
        f"{baseline['n_cut5_parent_dered'] + 350:,}",
        f"{baseline['n_cut6_inclination_raw'] + 240:,}",
        f"{baseline['n_cut6_inclination_dered'] + 280:,}",
        "POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551",
        "2026-08-13 06:00 KST",
        "server-side aggregate rows returned: **1**",
        "sample rows exported: **0**",
        "positions exported: **0**",
        "images requested: **0**",
        "chirality/handedness computed: **0**",
        "sky statistics computed: **0**",
        "bulk downloads: **0**",
        "publication/acceptance/commit/push: **0**",
        "No spiral fraction, retention factor, or other external factor is multiplied",
        "Frozen `BRICKID 1…121000` certificates are inputs only and are not modified",
    ]
    for value in required:
        assert value in text, value
    for forbidden in [
        "sky fraction",
        "footprint is",
        "accepted yield",
        "PARTIAL LOWER BOUND" if False else "EXACT FULL-KEYSPACE COUNT",
    ]:
        assert forbidden not in text, forbidden

    complete_status = dict(status)
    complete_status["stop_reason"] = "remaining_keyspace_exhausted"
    complete_status["finished_utc"] = "2026-08-12T20:30:00Z"
    complete_status["totals"] = dict(status["totals"])
    complete_status["totals"]["landed_new_partitions"] = 55
    complete_status["totals"]["landed_new_keys"] = 541174
    complete_status["totals"]["landed_total_keys"] = 662174
    complete_status["totals"]["contiguous_new_partitions"] = 55
    complete_status["totals"]["contiguous_covered_hi"] = 662174
    complete = module.render_text(manifest, complete_status, landed)
    assert "COMPLETE FULL-KEYSPACE COUNT" in complete
    assert "662,174 of 662,174 BRICKID keyspace units counted" in complete

    print("remaining_receipt_test=PASS")


if __name__ == "__main__":
    main()
