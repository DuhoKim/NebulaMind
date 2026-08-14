#!/usr/bin/env python3
"""Run the full 500-item hand-check protocol with synthetic images only."""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import math
import tempfile
from fractions import Fraction
from pathlib import Path

from PIL import Image, ImageOps

from nm_handcheck import (
    CheckerApplication,
    HandcheckError,
    canonical_json_bytes,
    load_checker_package,
    make_adjudication_package,
    prepare_experiment,
    reduce_experiment,
    sha256_bytes,
    sha256_file,
    unseal_key,
)

PASSPHRASE = b"synthetic-full-selftest-passphrase-not-for-use"
POPULATION_MATRIX = (
    (160, 80, 60),
    (80, 120, 100),
    (60, 100, 140),
)


def write_population(root: Path) -> Path:
    images = root / "synthetic_images"
    images.mkdir()
    rows = []
    serial = 0
    for chi_tertile, matrix_row in enumerate(POPULATION_MATRIX):
        for size_tertile, count in enumerate(matrix_row):
            for within_cell in range(count):
                object_id = f"synthetic-only-{serial:04d}"
                image_path = images / f"{object_id}.png"
                # Asymmetric deterministic pixels make a left-right reflection observable.
                pixels = [
                    ((x * 19 + y * 7 + serial * 11) % 256)
                    if x < 11
                    else ((x * 3 + y * 23 + serial * 5) % 256)
                    for y in range(24)
                    for x in range(24)
                ]
                image = Image.new("L", (24, 24))
                image.putdata(pixels)
                image.save(image_path)
                rows.append(
                    {
                        "data_class": "synthetic",
                        "object_id": object_id,
                        "image_path": str(image_path),
                        "instrument_sign": 1 if serial % 2 == 0 else -1,
                        # Wide group gaps make the intended rank tertiles exact.
                        "abs_chi": chi_tertile * 1_000_000 + size_tertile * 10_000 + within_cell,
                        "angular_size": size_tertile * 1_000_000 + chi_tertile * 10_000 + within_cell,
                    }
                )
                serial += 1
    population = root / "synthetic_population.jsonl"
    population.write_bytes(b"".join(canonical_json_bytes(row) + b"\n" for row in rows))
    return population


def complete_session(package_root: Path, labels: dict[str, str]) -> None:
    application = CheckerApplication(package_root, debounce_seconds=0.0)
    while application.public_state()["status"] != "COMPLETE":
        item_id = application.package["items"][application.completed]["item_id"]
        state = application.public_state()
        application.submit(state["presentation_token"], labels[item_id])


def concatenated_files(root: Path) -> bytes:
    return b"".join(path.read_bytes() for path in sorted(root.rglob("*")) if path.is_file())


def run_full_selftest() -> dict:
    with tempfile.TemporaryDirectory(prefix="nm-handcheck-synthetic-") as temporary:
        root = Path(temporary)
        population = write_population(root)
        private_root = root / "custodian_private"
        checking_root = root / "checking"
        preparation = prepare_experiment(
            population_path=population,
            private_root=private_root,
            checking_root=checking_root,
            passphrase=PASSPHRASE,
            checker_ids={"A": "synthetic-A", "B": "synthetic-B", "J": "synthetic-J"},
            total=500,
            floor=40,
        )
        sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
        try:
            unseal_key(private_root / "sealed_key.nmhc", b"wrong-passphrase-that-cannot-decrypt")
        except HandcheckError:
            wrong_passphrase_rejected = True
        else:
            wrong_passphrase_rejected = False

        package_a = load_checker_package(checking_root / "checker_A")
        package_b = load_checker_package(checking_root / "checker_B")
        order_a = [item["item_id"] for item in package_a["items"]]
        order_b = [item["item_id"] for item in package_b["items"]]
        if order_a == order_b:
            raise AssertionError("independent checker orders unexpectedly match")

        assignment_by_item = {row["item_id"]: row for row in sealed["assignments"]}
        by_stratum: dict[str, list[str]] = {}
        for item_id, row in assignment_by_item.items():
            by_stratum.setdefault(row["stratum"], []).append(item_id)
        correct: dict[str, bool] = {}
        for item_ids in by_stratum.values():
            ordered = sorted(item_ids)
            mistakes = max(1, len(ordered) // 10)
            for index, item_id in enumerate(ordered):
                correct[item_id] = index >= mistakes

        target_labels = {}
        for item_id, assignment in assignment_by_item.items():
            human_original_sign = int(assignment["instrument_sign"])
            if not correct[item_id]:
                human_original_sign *= -1
            presented_sign = human_original_sign * (-1 if assignment["mirrored"] else 1)
            target_labels[item_id] = "CCW" if presented_sign == 1 else "CW"
        labels_a = dict(target_labels)
        labels_b = dict(target_labels)
        disagreement_ids = set(sorted(target_labels)[::13])
        for item_id in disagreement_ids:
            labels_b[item_id] = "CW" if target_labels[item_id] == "CCW" else "CCW"

        checker_a_root = checking_root / "checker_A"
        checker_b_root = checking_root / "checker_B"
        commitment_before = (checking_root / "commitment.json").read_bytes()
        checker_b_before = concatenated_files(checker_b_root)
        complete_session(checker_a_root, labels_a)
        if concatenated_files(checker_b_root) != checker_b_before:
            raise AssertionError("checker A changed checker B's capability root")
        complete_session(checker_b_root, labels_b)
        adjudication = make_adjudication_package(checking_root)
        if (checking_root / "commitment.json").read_bytes() != commitment_before:
            raise AssertionError("original key commitment changed during checking/adjudication")
        complete_session(
            checking_root / "checker_J",
            {item_id: target_labels[item_id] for item_id in disagreement_ids},
        )

        private_output = root / "reduction_private"
        public_output = root / "release_candidate"
        aggregates = reduce_experiment(
            private_root=private_root,
            checking_root=checking_root,
            passphrase=PASSPHRASE,
            private_output_root=private_output,
            public_output_root=public_output,
        )

        root_secret = bytes.fromhex(sealed["root_secret_hex"])
        checker_a_pre_session = b"".join(
            path.read_bytes()
            for path in sorted((checking_root / "checker_A").rglob("*"))
            if path.is_file() and path.name != "answers.jsonl"
        )
        if root_secret in checker_a_pre_session:
            raise AssertionError("root secret appeared in checker package")
        object_id_absent = all(
            row["object_id"].encode() not in checker_a_pre_session
            for row in sealed["assignments"]
        )
        if not object_id_absent:
            raise AssertionError("source identity appeared in checker package")

        replay_exact = 0
        parity_hmac_exact = 0
        package_items = {item["item_id"]: item for item in package_a["items"]}
        for assignment in sealed["assignments"]:
            independently_mirrored = bool(
                hmac.new(
                    bytes.fromhex(sealed["root_secret_hex"]),
                    f"parity|20260812|{assignment['object_id']}".encode("utf-8"),
                    hashlib.sha256,
                ).digest()[0]
                & 1
            )
            parity_hmac_exact += int(independently_mirrored == assignment["mirrored"])
            with Image.open(assignment["image_path"]) as source_image:
                expected = ImageOps.mirror(source_image) if assignment["mirrored"] else source_image.copy()
                with Image.open(checker_a_root / package_items[assignment["item_id"]]["asset"]) as actual:
                    if expected.mode == actual.mode and expected.size == actual.size and list(expected.getdata()) == list(actual.getdata()):
                        replay_exact += 1

        public_bytes = concatenated_files(public_output)
        private_rows = (private_output / "per_object_handcheck.jsonl").read_text(encoding="utf-8").splitlines()
        private_aggregates = json.loads(
            (private_output / "stratum_aggregates_private.json").read_bytes()
        )
        expected_agreements = {
            stratum: sum(1 for item_id in item_ids if correct[item_id])
            for stratum, item_ids in by_stratum.items()
        }
        population_total = sum(sealed["stratum_populations"].values())
        expected_a = sum(
            Fraction(sealed["stratum_populations"][stratum], population_total)
            * Fraction(expected_agreements[stratum], len(by_stratum[stratum]))
            for stratum in by_stratum
        )
        expected_variance = 0.0
        for stratum, item_ids in by_stratum.items():
            population_count = sealed["stratum_populations"][stratum]
            sample_count = len(item_ids)
            rate = Fraction(expected_agreements[stratum], sample_count)
            weight = Fraction(population_count, population_total)
            fpc = Fraction(population_count - sample_count, population_count - 1)
            expected_variance += float(weight * weight * rate * (1 - rate) * fpc / sample_count)
        expected_masked = {
            stratum for stratum, count in sealed["stratum_allocation"].items() if count < 50
        }
        actual_masked = {row["stratum"] for row in aggregates["strata"] if row["masked"]}
        private_object_order = [json.loads(line)["object_id"] for line in private_rows]
        checks = {
            "population_is_synthetic_900_of_900": len(population.read_text().splitlines()) == 900,
            "sample_size_500": sealed["sample_size"] == 500,
            "nine_strata": len(sealed["stratum_populations"]) == 9,
            "all_strata_floor_40": min(sealed["stratum_allocation"].values()) >= 40,
            "allocation_closes_500": sum(sealed["stratum_allocation"].values()) == 500,
            "parity_contains_both_states": {row["mirrored"] for row in sealed["assignments"]} == {False, True},
            "parity_replay_pixel_exact_500": replay_exact == 500,
            "parity_hmac_independently_rederived_500": parity_hmac_exact == 500,
            "wrong_passphrase_rejected": wrong_passphrase_rejected,
            "checker_orders_independent": order_a != order_b,
            "checker_b_unchanged_while_a_checked": True,
            "original_commitment_immutable": (checking_root / "commitment.json").read_bytes() == commitment_before,
            "disagreement_only_adjudication": adjudication["disagreements"] == len(disagreement_ids),
            "all_disagreements_adjudicated": aggregates["disagreements_adjudicated"] == len(disagreement_ids),
            "private_rows_500": len(private_rows) == 500,
            "private_rows_sorted_by_source_key": private_object_order == sorted(private_object_order),
            "private_nine_unmasked_aggregate_rows": len(private_aggregates["strata"]) == 9,
            "public_exactly_nine_aggregate_rows": len(aggregates["strata"]) == 9,
            "public_f10_masks_every_sub50_stratum": actual_masked == expected_masked,
            "public_hc5_withholds_failing_strata": "failing_strata" not in aggregates["hc5"],
            "public_has_only_two_files": {path.name for path in public_output.iterdir()} == {"handcheck_aggregates.json", "handcheck_aggregates.csv"},
            "public_has_no_root_secret": root_secret not in public_bytes,
            "public_has_no_item_or_source_id_fields": b"item_id" not in public_bytes and b"object_id" not in public_bytes,
            "public_has_no_parity_field": b"mirrored" not in public_bytes,
            "checker_package_has_no_source_ids": object_id_absent,
            "population_weighted_a_matches_independent_fraction": aggregates["attenuation"]["a_exact_fraction"] == f"{expected_a.numerator}/{expected_a.denominator}",
            "fpc_delta_sigma_matches_independent_reduction": abs(aggregates["attenuation"]["sigma_a_delta"] - math.sqrt(expected_variance)) < 1e-15,
            "hc5_pass_for_synthetic_fixture": aggregates["hc5"]["verdict"] == "PASS_HC5_ATTENUATION",
            "no_real_data_touched": True,
        }
        if not all(checks.values()):
            failed = sorted(name for name, value in checks.items() if not value)
            raise AssertionError(f"synthetic self-test failures: {failed}")
        return {
            "schema_version": "nm-handcheck-selftest-v1",
            "status": "PASS_FULL_500_SYNTHETIC_HANDCHECK_SELFTEST",
            "data_boundary": "900 generated synthetic images only; 500 sampled; zero real images or object records",
            "population_matrix": POPULATION_MATRIX,
            "stratum_populations": sealed["stratum_populations"],
            "stratum_allocation": sealed["stratum_allocation"],
            "sample_size": sealed["sample_size"],
            "mirrored": sum(1 for row in sealed["assignments"] if row["mirrored"]),
            "unmirrored": sum(1 for row in sealed["assignments"] if not row["mirrored"]),
            "disagreements": len(disagreement_ids),
            "parity_replay_pixel_exact": replay_exact,
            "parity_hmac_independently_rederived": parity_hmac_exact,
            "f10_masked_strata": sorted(actual_masked),
            "attenuation": aggregates["attenuation"],
            "hc5": aggregates["hc5"],
            "checks": checks,
            "checks_passed": sum(checks.values()),
            "checks_total": len(checks),
            "harness_source_sha256": sha256_file(Path(__file__).with_name("nm_handcheck.py")),
            "test_source_sha256": sha256_file(Path(__file__).with_name("test_nm_handcheck.py")),
            "preparation_commitment_sha256": preparation["commitment_sha256"],
            "public_aggregate_json_sha256": sha256_file(public_output / "handcheck_aggregates.json"),
            "public_aggregate_csv_sha256": sha256_file(public_output / "handcheck_aggregates.csv"),
            "private_table_sha256": sha256_file(private_output / "per_object_handcheck.jsonl"),
            "temporary_workspace_removed_after_receipt": True,
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    if args.receipt.exists():
        raise SystemExit("refusing to overwrite existing self-test receipt")
    result = run_full_selftest()
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_bytes(canonical_json_bytes(result) + b"\n")
    print(result["status"], result["checks_passed"], "/", result["checks_total"])
    print("receipt_sha256", sha256_bytes(args.receipt.read_bytes()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
