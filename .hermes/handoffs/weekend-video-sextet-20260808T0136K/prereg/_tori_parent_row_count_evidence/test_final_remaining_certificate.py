#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "render_remaining_receipt.py"


def load_target():
    spec = importlib.util.spec_from_file_location("final_renderer", TARGET)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_target()
    zero_row = {column: "" for column in module.COLUMNS}
    zero_row["n_join_rows"] = "0"
    assert module.normalize_result_values(zero_row) == {column: 0 for column in module.COLUMNS}

    bad_row = dict(zero_row)
    bad_row["n_join_rows"] = "1"
    try:
        module.normalize_result_values(bad_row)
    except RuntimeError as exc:
        assert "blank aggregate" in str(exc)
    else:
        raise AssertionError("blank SUM over nonempty parent was accepted")

    totals = dict(module.BASE_TOTALS)
    totals.update(
        {
            "n_cut5_parent_raw": 903913,
            "n_cut5_parent_dered": 1015881,
            "n_cut6_inclination_raw": 749914,
            "n_cut6_inclination_dered": 832393,
        }
    )
    manifest = {
        "partition_count": 55,
        "remaining_key_count": 541174,
        "stop_rule": {"deadline_utc": "2026-08-12T21:00:00Z"},
    }
    status = {
        "active_concurrency": 0,
        "totals": {
            "landed_new_partitions": 41,
            "landed_new_keys": 410000,
            "landed_total_keys": 531000,
            "contiguous_covered_hi": 531000,
            "all_landed_totals": totals,
        },
        "recovery_history": [
            {
                "detected_utc": "2026-08-12T14:40:53Z",
                "stop_reason": "partition_failure_201001-211000",
                "cause": "HTTP 502 Bad Gateway from nginx while polling three existing UWS /phase URLs",
                "runner_defect": "HTTP 502 was omitted from pressure handling",
                "recovery_action": "resumed same manifest serially",
            }
        ],
    }
    closure = {
        "status": "PASS",
        "verified_utc": "2026-08-12T20:30:00Z",
        "direct_full_chain": {
            "start_brickid": 1,
            "stop_brickid": 541000,
            "keyspace_units": 541000,
            "landed_new_partitions": 42,
        },
        "tail_zero_proof": {
            "start_brickid": 541001,
            "stop_brickid": 662174,
            "keyspace_units": 121174,
            "n_join_rows": 0,
            "query_sha256": "a" * 64,
            "result_sha256": "b" * 64,
            "job_url": "https://example.invalid/tap/async/tail",
            "phase": "COMPLETED",
        },
        "full_keyspace": {"start_brickid": 1, "stop_brickid": 662174, "keyspace_units": 662174},
        "stop_reconciliation": {
            "stale_status_landed_partitions": 41,
            "authoritative_landed_partitions": 42,
            "stale_status_updated_utc": "2026-08-12T20:07:02Z",
            "last_receipt_completed_utc": "2026-08-12T20:07:07Z",
            "crash_observed_utc": "2026-08-12T20:07:12Z",
            "cause": "unhandled SQL NULL SUM fields in an empty joined-parent block caused ValueError int blank",
            "classification": "runner crash after the 42nd receipt landed; not deliberate, not deadline, and not keyspace exhaustion",
        },
        "totals": totals,
        "direct_lower_bound_equals_exact_full_count": True,
    }
    text = module.render_text(manifest, status, [], status["recovery_history"], closure)
    for required in (
        "COMPLETE FULL-KEYSPACE COUNT — ZERO-TAIL CLOSURE",
        "541,000 of 662,174",
        "81.700580%",
        "541001…662174",
        "121,174",
        "n_join_rows = 0",
        "LOWER BOUND",
        "lower bound equals the exact full-keyspace count",
        "1,015,881",
        "832,393",
        "42 authoritative",
        "41",
        "not deliberate, not deadline, and not keyspace exhaustion",
        "HTTP 502 Bad Gateway",
        "BRICKID keyspace, not sky area",
        "sample rows exported: **0**",
        "publication/acceptance/commit/push: **0**",
    ):
        assert required in text, required
    for forbidden in (
        "remaining range is unmeasured",
        "footprint sky area is complete",
        "extrapolated tail count",
    ):
        assert forbidden not in text.lower(), forbidden

    print("final_remaining_certificate_test=PASS")


if __name__ == "__main__":
    main()
