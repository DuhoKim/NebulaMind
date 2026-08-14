#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "run_remaining_keyspace.py"
BASE_QUERY = ROOT / "partitions/query_111001_121000.adql"
EXPECTED_BASE_COLUMNS = [
    "n_join_rows",
    "n_cut1_primary_mask",
    "n_cut2_extended_flux",
    "n_photoz_joined_cut2",
    "n_cut3_photoz",
    "n_cut4_raw_mag",
    "n_cut4_dered_mag",
    "n_cut5_parent_raw",
    "n_cut5_parent_dered",
    "n_raw_allband_nobs",
    "n_dered_allband_nobs",
    "n_raw_allband_ngood",
    "n_dered_allband_ngood",
    "n_raw_allband_ivar",
    "n_dered_allband_ivar",
    "n_raw_shape_valid",
    "n_dered_shape_valid",
    "n_raw_native_covariates",
    "n_dered_native_covariates",
    "n_raw_all_countable_availability",
    "n_dered_all_countable_availability",
]
EXPECTED_COLUMNS = EXPECTED_BASE_COLUMNS + [
    "n_cut6_inclination_raw",
    "n_cut6_inclination_dered",
]
THRESHOLD = "POWER(t.shape_e1,2) + POWER(t.shape_e2,2) < 0.1836734693877551"


def load_target():
    assert TARGET.exists(), f"missing implementation: {TARGET}"
    spec = importlib.util.spec_from_file_location("remaining", TARGET)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def aliases(query: str) -> list[str]:
    normalized = " ".join(query.split())
    select = normalized[7 : normalized.upper().index(" FROM ")]
    return re.findall(r"\bAS\s+([A-Za-z_][A-Za-z0-9_]*)\b", select, re.I)


def main() -> None:
    module = load_target()
    assert module.START == 121001
    assert module.STOP == 662174
    assert module.WIDTH == 10000
    assert module.MAX_CONCURRENT == 3
    assert module.DEADLINE_UTC == "2026-08-12T21:00:00Z"
    assert module.RECEIPT_PATH.name == "TORI_FULL_KEYSPACE_SWEEP_20260813.md"
    assert module.COLUMNS == EXPECTED_COLUMNS

    manifest = module.build_manifest(dry_run=True)
    entries = manifest["entries"]
    assert len(entries) == 55
    assert (entries[0]["lo"], entries[0]["hi"]) == (121001, 131000)
    assert (entries[-1]["lo"], entries[-1]["hi"]) == (661001, 662174)
    assert manifest["remaining_key_count"] == 541174
    assert manifest["frozen_preceding_coverage"] == {"lo": 1, "hi": 121000}
    assert manifest["stop_rule"] == {
        "deadline_utc": "2026-08-12T21:00:00Z",
        "deadline_kst": "2026-08-13T06:00:00+09:00",
        "keyspace_exhaustion": 662174,
        "first_of": True,
    }
    assert manifest["columns"] == EXPECTED_COLUMNS
    assert manifest["partition_count"] == 55
    assert manifest["max_concurrent"] == 3
    assert manifest["server_pressure_backoff"] == "serial"
    assert manifest["no_requery_at_or_below"] == 121000

    cursor = 121001
    base = BASE_QUERY.read_text()
    base_select = " ".join(base.split())
    base_select = base_select[7 : base_select.upper().index(" FROM ")]
    assert aliases(base) == EXPECTED_BASE_COLUMNS
    for entry in entries:
        assert entry["lo"] == cursor
        assert entry["hi"] == min(entry["lo"] + 9999, 662174)
        query = module.render_query(entry["lo"], entry["hi"])
        assert aliases(query) == EXPECTED_COLUMNS
        assert query.count(THRESHOLD) == 2
        assert f"WHERE t.brickid BETWEEN {entry['lo']} AND {entry['hi']}" in query
        assert "BETWEEN 1 AND 121000" not in query
        assert entry["lo"] > 121000
        normalized = " ".join(query.split())
        select = normalized[7 : normalized.upper().index(" FROM ")]
        assert select.startswith(base_select)
        assert not re.search(
            r"\b(SIN|COS|TAN|ASIN|ACOS|ATAN|RADIANS|DEGREES|COSTHETA)\b",
            query.upper(),
        )
        module.validate_query(query, entry["lo"], entry["hi"])
        cursor = entry["hi"] + 1
    assert cursor == 662175

    for lo, hi in [(121000, 130999), (1, 10000), (662175, 662175)]:
        try:
            module.render_query(lo, hi)
        except ValueError:
            pass
        else:
            raise AssertionError(f"out-of-scope range accepted: {lo}..{hi}")

    with tempfile.TemporaryDirectory() as tmp:
        zero_path = Path(tmp) / "zero.csv"
        zero_path.write_text(",".join(EXPECTED_COLUMNS) + "\n0," + ",".join([""] * 22) + "\n")
        zero = module.one_row(zero_path)
        assert zero == {column: 0 for column in EXPECTED_COLUMNS}

        malformed_path = Path(tmp) / "malformed.csv"
        malformed_path.write_text(",".join(EXPECTED_COLUMNS) + "\n1," + ",".join([""] * 22) + "\n")
        try:
            module.one_row(malformed_path)
        except RuntimeError as exc:
            assert "blank aggregate" in str(exc)
        else:
            raise AssertionError("nonempty joined population accepted blank SUM aggregates")

    print("remaining_keyspace_contract_test=PASS")


if __name__ == "__main__":
    main()
