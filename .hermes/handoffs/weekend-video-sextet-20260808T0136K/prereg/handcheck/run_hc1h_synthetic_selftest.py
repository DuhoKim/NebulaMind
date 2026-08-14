#!/usr/bin/env python3
"""Full accepted-shape HC-1H synthetic self-test. No survey object is read."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from nm_handcheck import (
    HC1H_STRATA,
    CheckerApplication,
    canonical_json_bytes,
    load_checker_package,
    prepare_hc1h_experiment,
    reduce_hc1h_experiment,
    sha256_file,
    unseal_key,
)
from test_nm_handcheck import PASSPHRASE, write_hc1h_pools


def label_for(value: int) -> str:
    return "CCW" if value == 1 else "CW"


def complete_with_scripted_synthetic_labels(
    package_root: Path,
    control_path: Path,
    assignments: dict[str, dict],
    *,
    synthetic_errors: int,
    repeat_nonflips: int,
    flag_one_synthetic: bool,
) -> dict:
    application = CheckerApplication(
        package_root, control_path=control_path, debounce_seconds=0.0
    )
    presented_by_item: dict[str, int] = {}
    synthetic_seen = 0
    repeat_seen = 0
    flagged = False
    while application.public_state()["status"] not in {"COMPLETE", "AWAITING_ERGONOMICS"}:
        state = application.public_state()
        if state["status"] == "BREAK_REQUIRED":
            application.acknowledge_break()
            continue
        queue, cursor, _reserves, _systematic, _flags = application._hc1h_runtime()
        assignment = assignments[queue[cursor]["item_id"]]
        if flag_one_synthetic and not flagged and assignment["category"] == "synthetic":
            application.flag_exposure(state["presentation_token"])
            flagged = True
            continue
        if assignment["category"] == "synthetic":
            original = int(assignment["truth_sign"])
            if synthetic_seen < synthetic_errors:
                original = -original
            synthetic_seen += 1
            presented = -original if assignment["mirrored"] else original
        elif assignment["category"] == "repeat":
            parent_presented = presented_by_item[assignment["parent_item_id"]]
            presented = -parent_presented
            if repeat_seen < repeat_nonflips:
                presented = parent_presented
            repeat_seen += 1
        else:
            original = int(assignment["instrument_sign"])
            presented = -original if assignment["mirrored"] else original
        application.submit(state["presentation_token"], label_for(presented))
        presented_by_item[assignment["item_id"]] = presented
    return {
        "labels": application.completed,
        "breaks_acknowledged": sum(
            event.get("event_type") == "BREAK_ACKNOWLEDGED" for event in application._events[1:]
        ),
        "specific_hc7_flags": application.public_state()["hc7_specific_flags"],
        "synthetic_labels": synthetic_seen,
        "repeat_labels": repeat_seen,
        "end_hash": application._events[-1]["event_hash"],
    }


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="nm-hc1h-selftest-") as temporary:
        root = Path(temporary)
        real_population, synthetic_pool, priors = write_hc1h_pools(
            root, real_per_stratum=120, synthetic_per_stratum=30
        )

        full_private = root / "full_private"
        full_checking = root / "full_checking"
        full_prepare = prepare_hc1h_experiment(
            real_population_path=real_population,
            synthetic_pool_path=synthetic_pool,
            neyman_prior_rates=priors,
            private_root=full_private,
            checking_root=full_checking,
            passphrase=PASSPHRASE,
            checker_id="synthetic-duho",
            mode="full",
            real_total=500,
            synthetic_total=200,
            repeat_total=150,
            real_floor=30,
            replacement_reserve_per_group=1,
        )
        assert full_prepare["labels_required"] == 850
        assert sum(full_prepare["real_allocation"].values()) == 500
        assert min(full_prepare["real_allocation"].values()) >= 30
        assert set(full_prepare["real_allocation"]) == set(HC1H_STRATA)
        package = load_checker_package(full_checking / "checker_H")
        assert package["role"] == "H" and len(package["items"]) == 850
        assert not (full_checking / "checker_A").exists()
        package_bytes = (full_checking / "checker_H" / "package.json").read_bytes()
        for forbidden in (b"object_id", b"synthetic_id", b"truth_sign", b"instrument_sign", b"category"):
            assert forbidden not in package_bytes

        full_sealed = unseal_key(full_private / "sealed_key.nmhc", PASSPHRASE)
        full_assignments = {
            row["item_id"]: row
            for row in full_sealed["assignments"] + full_sealed["reserve_assignments"]
        }
        order = {item["item_id"]: index for index, item in enumerate(package["items"])}
        repeat_later = 0
        repeat_complement = 0
        for assignment in full_sealed["assignments"]:
            if assignment["category"] != "repeat":
                continue
            parent = full_assignments[assignment["parent_item_id"]]
            repeat_later += int(order[assignment["item_id"]] > order[parent["item_id"]])
            repeat_complement += int(assignment["mirrored"] is not parent["mirrored"])
        assert repeat_later == 150 and repeat_complement == 150

        full_session = complete_with_scripted_synthetic_labels(
            full_checking / "checker_H",
            full_private / "checker_H_control.json",
            full_assignments,
            synthetic_errors=10,
            repeat_nonflips=6,
            flag_one_synthetic=True,
        )
        assert full_session["labels"] == 850
        assert full_session["breaks_acknowledged"] == 17
        assert full_session["specific_hc7_flags"] == 1
        full_result = reduce_hc1h_experiment(
            private_root=full_private,
            checking_root=full_checking,
            passphrase=PASSPHRASE,
            private_output_root=root / "full_private_output",
            public_output_root=root / "full_public_output",
        )
        assert full_result["counts_used"] == {"real": 500, "synthetic": 200, "repeat": 150}
        assert full_result["statistics"]["epsilon_exact_fraction"] == "1/20"
        assert full_result["statistics"]["repeat_diagnostic"]["nonflips"] == 6
        assert full_result["statistics"]["verdict"]["verdict"] == "WITHHELD_F10_MASKED_STRATA"
        full_private_summary = json.loads(
            (root / "full_private_output" / "hc1h_private_summary.json").read_bytes()
        )
        assert full_private_summary["statistics"]["verdict"]["verdict"] == "PASS_HC1H_ATTENUATION"

        pilot_private = root / "pilot_private"
        pilot_checking = root / "pilot_checking"
        pilot_prepare = prepare_hc1h_experiment(
            real_population_path=real_population,
            synthetic_pool_path=synthetic_pool,
            neyman_prior_rates=priors,
            private_root=pilot_private,
            checking_root=pilot_checking,
            passphrase=PASSPHRASE,
            checker_id="synthetic-duho",
            mode="pilot",
            real_total=90,
            synthetic_total=40,
            repeat_total=20,
            real_floor=10,
            replacement_reserve_per_group=1,
        )
        assert pilot_prepare["labels_required"] == 150
        pilot_sealed = unseal_key(pilot_private / "sealed_key.nmhc", PASSPHRASE)
        pilot_assignments = {
            row["item_id"]: row
            for row in pilot_sealed["assignments"] + pilot_sealed["reserve_assignments"]
        }
        pilot_session = complete_with_scripted_synthetic_labels(
            pilot_checking / "checker_H",
            pilot_private / "checker_H_control.json",
            pilot_assignments,
            synthetic_errors=2,
            repeat_nonflips=1,
            flag_one_synthetic=False,
        )
        assert pilot_session["labels"] == 150
        assert pilot_session["breaks_acknowledged"] == 2
        pilot_application = CheckerApplication(
            pilot_checking / "checker_H",
            control_path=pilot_private / "checker_H_control.json",
            debounce_seconds=0.0,
        )
        assert pilot_application.public_state()["status"] == "AWAITING_ERGONOMICS"
        pilot_application.record_ergonomics(True)
        pilot_result = reduce_hc1h_experiment(
            private_root=pilot_private,
            checking_root=pilot_checking,
            passphrase=PASSPHRASE,
            private_output_root=root / "pilot_private_output",
            public_output_root=root / "pilot_public_output",
        )
        assert pilot_result["pilot_outcome"] == "PASS-TO-FULL-HC1H"
        assert pilot_result["boundaries"]["pilot_synthetics_count_toward_full"] is False

        fresh_full_private = root / "fresh_full_private_after_pilot"
        fresh_full_checking = root / "fresh_full_checking_after_pilot"
        fresh_full_prepare = prepare_hc1h_experiment(
            real_population_path=real_population,
            synthetic_pool_path=synthetic_pool,
            neyman_prior_rates=priors,
            private_root=fresh_full_private,
            checking_root=fresh_full_checking,
            passphrase=PASSPHRASE,
            checker_id="synthetic-duho",
            mode="full",
            real_total=500,
            synthetic_total=200,
            repeat_total=150,
            real_floor=30,
            replacement_reserve_per_group=1,
            pilot_private_root=pilot_private,
            pilot_public_result_path=root
            / "pilot_public_output"
            / "hc1h_aggregates.json",
        )
        fresh_full_sealed = unseal_key(fresh_full_private / "sealed_key.nmhc", PASSPHRASE)
        pilot_injection_ids = {
            row["synthetic_id"]
            for row in pilot_sealed["assignments"] + pilot_sealed["reserve_assignments"]
            if row["category"] == "synthetic"
        }
        fresh_full_injection_ids = {
            row["synthetic_id"]
            for row in fresh_full_sealed["assignments"] + fresh_full_sealed["reserve_assignments"]
            if row["category"] == "synthetic"
        }
        assert pilot_injection_ids.isdisjoint(fresh_full_injection_ids)
        assert fresh_full_prepare["pilot_exclusion"]["pilot_synthetics_reused"] is False

        receipt = {
            "status": "PASS_HC1H_SYNTHETIC_SELFTEST",
            "synthetic_only": True,
            "full": {
                "labels": full_session["labels"],
                "counts": full_result["counts_used"],
                "strata": 9,
                "allocation_floor_min": min(full_prepare["real_allocation"].values()),
                "allocation_total": sum(full_prepare["real_allocation"].values()),
                "repeat_later": repeat_later,
                "repeat_parity_complement": repeat_complement,
                "specific_hc7_flags_replaced": full_result["specific_hc7_flags_replaced"],
                "breaks_acknowledged": full_session["breaks_acknowledged"],
                "epsilon_exact_fraction": full_result["statistics"]["epsilon_exact_fraction"],
                "repeat_nonflips": full_result["statistics"]["repeat_diagnostic"]["nonflips"],
                "private_fixture_verdict": full_private_summary["statistics"]["verdict"]["verdict"],
                "public_f10_verdict": full_result["statistics"]["verdict"]["verdict"],
            },
            "pilot": {
                "labels": pilot_session["labels"],
                "counts": pilot_result["counts_used"],
                "outcome": pilot_result["pilot_outcome"],
                "synthetics_count_toward_full": False,
                "breaks_acknowledged": pilot_session["breaks_acknowledged"],
                "fresh_full_exclusion_verified": True,
                "pilot_synthetic_ids_excluded": len(pilot_injection_ids),
            },
            "artifacts": {
                "harness_sha256": sha256_file(Path(__file__).with_name("nm_handcheck.py")),
                "tests_sha256": sha256_file(Path(__file__).with_name("test_nm_handcheck.py")),
            },
        }
        output_path = Path(__file__).with_name("hc1h_synthetic_selftest_receipt.json")
        output_path.write_bytes(canonical_json_bytes(receipt) + b"\n")
        print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
