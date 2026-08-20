#!/usr/bin/env python3
"""Synthetic-only contract tests for the blinded hand-check harness."""
from __future__ import annotations

import hashlib
import hmac
import json
import tempfile
import threading
import unittest
from decimal import Decimal
from pathlib import Path
from unittest import mock
from urllib import error, request

from http.server import ThreadingHTTPServer

from PIL import Image, ImageOps

from nm_handcheck import (
    CHECKER_HTML,
    CheckerApplication,
    HandcheckError,
    _summarize_strata,
    _hc1h_public_projection,
    allocate_neyman,
    allocate_proportional_floor,
    canonical_json_bytes,
    hc5_verdict,
    hc1h_statistics,
    hc1h_verdict,
    make_checker_http_handler,
    load_checker_package,
    make_adjudication_package,
    prepare_hc1h_experiment,
    prepare_experiment,
    reduce_hc1h_experiment,
    reduce_experiment,
    unseal_key,
)


PASSPHRASE = b"synthetic-self-test-passphrase-not-for-production"
HC1H_STATES = ("agree-confident", "disagree", "low-confidence")
HC1H_STRATA = tuple(f"{state}|{chi}" for state in HC1H_STATES for chi in range(3))


def write_synthetic_population(root: Path, *, repeats: int = 2) -> Path:
    image_root = root / "synthetic_images"
    image_root.mkdir()
    rows = []
    ordinal = 0
    for chi_tertile in range(3):
        for size_tertile in range(3):
            for repeat in range(repeats):
                object_id = f"SYNTHETIC-{ordinal:04d}"
                image_path = image_root / f"image_{ordinal:04d}.png"
                image = Image.new("L", (17, 13), color=20 + ordinal)
                image.putpixel((1 + repeat, 2 + chi_tertile), 240)
                image.putpixel((12 + size_tertile, 8), 90)
                image.save(image_path)
                rows.append(
                    {
                        "data_class": "synthetic",
                        "object_id": object_id,
                        "image_path": str(image_path),
                        "instrument_sign": 1 if ordinal % 2 == 0 else -1,
                        "abs_chi": 100.0 * chi_tertile + 10.0 * size_tertile + repeat,
                        "angular_size": 100.0 * size_tertile + 10.0 * chi_tertile + repeat,
                    }
                )
                ordinal += 1
    population = root / "synthetic_population.jsonl"
    population.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )
    return population


def write_hc1h_pools(
    root: Path,
    *,
    real_per_stratum: int = 8,
    synthetic_per_stratum: int = 4,
) -> tuple[Path, Path, dict[str, Decimal]]:
    image_root = root / "hc1h_synthetic_images"
    image_root.mkdir()
    real_rows = []
    injection_rows = []
    serial = 0
    for state_index, state in enumerate(HC1H_STATES):
        for chi_tertile in range(3):
            for within in range(real_per_stratum):
                object_id = f"HC1H-REAL-SYNTHETIC-{serial:05d}"
                image_path = image_root / f"real_{serial:05d}.png"
                image = Image.new("L", (19, 19), color=30 + (serial % 100))
                image.putpixel((2 + state_index, 3 + chi_tertile), 245)
                image.putpixel((15, 12), 70)
                image.save(image_path)
                real_rows.append(
                    {
                        "data_class": "synthetic",
                        "object_id": object_id,
                        "image_path": str(image_path),
                        "instrument_sign": 1 if serial % 2 == 0 else -1,
                        "abs_chi": chi_tertile * 100_000 + state_index * 1_000 + within,
                        "committee_state": state,
                    }
                )
                serial += 1
    for state_index, state in enumerate(HC1H_STATES):
        for chi_tertile in range(3):
            for within in range(synthetic_per_stratum):
                synthetic_id = f"HC1H-INJECTION-{state_index}-{chi_tertile}-{within:03d}"
                image_path = image_root / f"injection_{state_index}_{chi_tertile}_{within:03d}.png"
                image = Image.new("L", (19, 19), color=45 + (within % 80))
                image.putpixel((2 + state_index, 3 + chi_tertile), 245)
                image.putpixel((15, 12), 70)
                image.save(image_path)
                injection_rows.append(
                    {
                        "data_class": "synthetic",
                        "synthetic_id": synthetic_id,
                        "image_path": str(image_path),
                        "truth_sign": 1 if within % 2 == 0 else -1,
                        "abs_chi": chi_tertile * 100_000 + state_index * 1_000 + within,
                        "committee_state": state,
                    }
                )
    real_path = root / "hc1h_real_population.jsonl"
    injection_path = root / "hc1h_injection_pool.jsonl"
    real_path.write_bytes(b"".join(canonical_json_bytes(row) + b"\n" for row in real_rows))
    injection_path.write_bytes(
        b"".join(canonical_json_bytes(row) + b"\n" for row in injection_rows)
    )
    real_path.with_suffix(real_path.suffix + ".provenance.json").write_text(
        json.dumps({"population_role": "accepted_population", "provenance": "synthetic"}),
        encoding="utf-8",
    )
    injection_path.with_suffix(injection_path.suffix + ".provenance.json").write_text(
        json.dumps({"population_role": "blind_injection_pool", "provenance": "synthetic"}),
        encoding="utf-8",
    )
    prior_rates = {
        f"{state}|{chi}": Decimal("0.80") + Decimal(state_index + chi) / Decimal("50")
        for state_index, state in enumerate(HC1H_STATES)
        for chi in range(3)
    }
    return real_path, injection_path, prior_rates


def complete_session(package_root: Path, labels_by_item: dict[str, str]) -> None:
    application = CheckerApplication(package_root, debounce_seconds=0.0)
    while application.public_state()["status"] != "COMPLETE":
        state = application.public_state()
        if state["status"] == "BREAK_REQUIRED":
            application.acknowledge_break()
            continue
        if application.package["role"] == "H":
            queue, cursor, _reserves, _systematic, _flags = application._hc1h_runtime()
            item_id = queue[cursor]["item_id"]
        else:
            item_id = application.package["items"][application.completed]["item_id"]
        application.submit(state["presentation_token"], labels_by_item[item_id])


class AllocationTests(unittest.TestCase):
    def test_neyman_recomputes_after_capacity_caps_before_fixing_low_quota(self) -> None:
        allocation = allocate_neyman(
            {"0": 24, "1": 68, "2": 73},
            {"0": Decimal("0.001"), "1": Decimal("0.5"), "2": Decimal("0.5")},
            total=151,
            floor=5,
        )
        self.assertEqual(allocation, {"0": 10, "1": 68, "2": 73})

    def test_hc1h_neyman_allocation_honours_floor_30_and_closes_to_500_real(self) -> None:
        populations = {
            "agree-confident|0": 1000,
            "agree-confident|1": 800,
            "agree-confident|2": 600,
            "disagree|0": 500,
            "disagree|1": 400,
            "disagree|2": 300,
            "low-confidence|0": 250,
            "low-confidence|1": 200,
            "low-confidence|2": 150,
        }
        prior_rates = {
            "agree-confident|0": Decimal("0.98"),
            "agree-confident|1": Decimal("0.90"),
            "agree-confident|2": Decimal("0.80"),
            "disagree|0": Decimal("0.70"),
            "disagree|1": Decimal("0.60"),
            "disagree|2": Decimal("0.50"),
            "low-confidence|0": Decimal("0.40"),
            "low-confidence|1": Decimal("0.30"),
            "low-confidence|2": Decimal("0.20"),
        }

        allocation = allocate_neyman(populations, prior_rates, total=500, floor=30)

        self.assertEqual(
            allocation,
            {
                "agree-confident|0": 47,
                "agree-confident|1": 80,
                "agree-confident|2": 80,
                "disagree|0": 76,
                "disagree|1": 65,
                "disagree|2": 50,
                "low-confidence|0": 41,
                "low-confidence|1": 31,
                "low-confidence|2": 30,
            },
        )
        self.assertEqual(sum(allocation.values()), 500)
        self.assertTrue(all(value >= 30 for value in allocation.values()))
        self.assertTrue(all(allocation[key] <= populations[key] for key in populations))

    def test_floor_40_is_honoured_and_remainder_is_redistributed_proportionally(self) -> None:
        populations = {
            "00": 1000,
            "01": 800,
            "02": 600,
            "10": 400,
            "11": 300,
            "12": 200,
            "20": 100,
            "21": 80,
            "22": 60,
        }
        allocation = allocate_proportional_floor(populations, total=500, floor=40)
        self.assertEqual(
            allocation,
            {
                "00": 107,
                "01": 86,
                "02": 64,
                "10": 43,
                "11": 40,
                "12": 40,
                "20": 40,
                "21": 40,
                "22": 40,
            },
        )
        self.assertEqual(sum(allocation.values()), 500)
        self.assertTrue(all(value >= 40 for value in allocation.values()))
        self.assertTrue(all(allocation[key] <= populations[key] for key in populations))


class PreparationTests(unittest.TestCase):
    def test_hc1h_population_data_class_must_match_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            real_population.with_suffix(real_population.suffix + ".provenance.json").write_text(
                json.dumps(
                    {"population_role": "accepted_population", "provenance": "authorized_measurement"}
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(HandcheckError, "provenance disagrees"):
                prepare_hc1h_experiment(
                    real_population_path=real_population,
                    synthetic_pool_path=injection_pool,
                    neyman_prior_rates=prior_rates,
                    private_root=root / "private",
                    checking_root=root / "checking",
                    passphrase=PASSPHRASE,
                    checker_id="synthetic-duho",
                    real_total=18,
                    synthetic_total=9,
                    repeat_total=6,
                    real_floor=2,
                )

    def test_authorized_hc1h_requires_covariance_and_cannot_override_frozen_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            rows = [json.loads(line) for line in real_population.read_text().splitlines()]
            for row in rows:
                row["data_class"] = "authorized_measurement"
            real_population.write_bytes(
                b"".join(canonical_json_bytes(row) + b"\n" for row in rows)
            )
            real_population.with_suffix(real_population.suffix + ".provenance.json").write_text(
                json.dumps(
                    {"population_role": "accepted_population", "provenance": "authorized_measurement"}
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(HandcheckError, "additional covariance"):
                prepare_hc1h_experiment(
                    real_population_path=real_population,
                    synthetic_pool_path=injection_pool,
                    neyman_prior_rates=prior_rates,
                    private_root=root / "bad_full_private",
                    checking_root=root / "bad_full_checking",
                    passphrase=PASSPHRASE,
                    checker_id="synthetic-duho",
                    mode="full",
                    real_total=499,
                    synthetic_total=200,
                    repeat_total=150,
                    real_floor=30,
                )
            with self.assertRaisesRegex(HandcheckError, "requires real/synthetic/repeat/floor"):
                prepare_hc1h_experiment(
                    real_population_path=real_population,
                    synthetic_pool_path=injection_pool,
                    neyman_prior_rates=prior_rates,
                    private_root=root / "bad_full_counts_private",
                    checking_root=root / "bad_full_counts_checking",
                    passphrase=PASSPHRASE,
                    checker_id="synthetic-duho",
                    mode="full",
                    real_total=499,
                    synthetic_total=200,
                    repeat_total=150,
                    real_floor=30,
                    additional_covariance=Decimal("0"),
                )
            with self.assertRaisesRegex(HandcheckError, "requires real/synthetic/repeat/floor"):
                prepare_hc1h_experiment(
                    real_population_path=real_population,
                    synthetic_pool_path=injection_pool,
                    neyman_prior_rates=prior_rates,
                    private_root=root / "bad_pilot_private",
                    checking_root=root / "bad_pilot_checking",
                    passphrase=PASSPHRASE,
                    checker_id="synthetic-duho",
                    mode="pilot",
                    real_total=90,
                    synthetic_total=39,
                    repeat_total=20,
                    real_floor=10,
                    additional_covariance=Decimal("0"),
                )

    def test_hc1h_full_stream_is_one_checker_blind_18_real_9_injections_6_later_mirrored_repeats(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            private_root = root / "hc1h_private"
            checking_root = root / "hc1h_checking"

            receipt = prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                mode="full",
                real_total=18,
                synthetic_total=9,
                repeat_total=6,
                real_floor=2,
            )

            self.assertEqual(receipt["labels_required"], 33)
            self.assertEqual(receipt["power_bound_n"], 130076)
            self.assertEqual(receipt["power_gate"], "0.7905")
            self.assertEqual(receipt["category_counts"], {"real": 18, "synthetic": 9, "repeat": 6})
            self.assertFalse((checking_root / "checker_A").exists())
            package = load_checker_package(checking_root / "checker_H")
            self.assertEqual(package["role"], "H")
            self.assertEqual(len(package["items"]), 33)
            checker_bytes = b"".join(
                path.read_bytes() for path in checking_root.rglob("*") if path.is_file()
            )
            for forbidden in (
                b"category",
                b"synthetic_id",
                b"object_id",
                b"truth_sign",
                b"instrument_sign",
                b"replacement_group",
                b"dependent_item_id",
                b"parent_anchor_item_id",
                b"session_mac_key_hex",
            ):
                self.assertNotIn(forbidden, checker_bytes)
            self.assertTrue((private_root / "checker_H_control.json").is_file())

            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            lower_cut, upper_cut = sealed["chi_tertile_cutpoints_from_real_population"]
            for assignment in sealed["assignments"]:
                if assignment["category"] != "synthetic":
                    continue
                expected_tertile = (
                    0
                    if assignment["abs_chi"] <= lower_cut
                    else 1
                    if assignment["abs_chi"] <= upper_cut
                    else 2
                )
                self.assertEqual(assignment["stratum"].rsplit("|", 1)[1], str(expected_tertile))
            assignments = {row["item_id"]: row for row in sealed["assignments"]}
            repeated_parent_ids = {
                row["parent_item_id"]
                for row in sealed["assignments"]
                if row["category"] == "repeat"
            }
            reserve_repeat_parent_ids = [
                row["parent_item_id"]
                for row in sealed["reserve_assignments"]
                if row["category"] == "repeat"
            ]
            self.assertTrue(repeated_parent_ids.isdisjoint(reserve_repeat_parent_ids))
            self.assertEqual(len(reserve_repeat_parent_ids), len(set(reserve_repeat_parent_ids)))
            self.assertEqual(
                {category: sum(row["category"] == category for row in assignments.values()) for category in ("real", "synthetic", "repeat")},
                {"real": 18, "synthetic": 9, "repeat": 6},
            )
            order = [item["item_id"] for item in package["items"]]
            position = {item_id: index for index, item_id in enumerate(order)}
            for assignment in assignments.values():
                if assignment["category"] == "repeat":
                    parent = assignments[assignment["parent_item_id"]]
                    self.assertGreater(position[assignment["item_id"]], position[parent["item_id"]])
                    self.assertEqual(assignment["mirrored"], not parent["mirrored"])

    def test_sealed_key_is_absent_from_checker_path_and_reproduces_every_parity(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            population = write_synthetic_population(root)
            private_root = root / "custodian_private"
            checking_root = root / "checking"
            receipt = prepare_experiment(
                population_path=population,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )

            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            commitment = json.loads((checking_root / "commitment.json").read_text(encoding="utf-8"))
            self.assertEqual(
                hashlib.sha256(canonical_json_bytes(sealed)).hexdigest(),
                commitment["sealed_key_plaintext_sha256"],
            )
            self.assertEqual(receipt["commitment_sha256"], (checking_root / "commitment.sha256").read_text().strip())

            checker_bytes = b"".join(
                path.read_bytes() for path in checking_root.rglob("*") if path.is_file()
            )
            self.assertNotIn(bytes.fromhex(sealed["root_secret_hex"]), checker_bytes)
            for assignment in sealed["assignments"]:
                self.assertNotIn(assignment["object_id"].encode(), checker_bytes)

            package = load_checker_package(checking_root / "checker_A")
            self.assertEqual(len(package["items"]), 18)
            assignment_by_item = {row["item_id"]: row for row in sealed["assignments"]}
            root_secret = bytes.fromhex(sealed["root_secret_hex"])
            independently_derived_parities = set()
            for assignment in sealed["assignments"]:
                digest = hmac.new(
                    root_secret,
                    f"parity|20260812|{assignment['object_id']}".encode("utf-8"),
                    hashlib.sha256,
                ).digest()
                expected_mirrored = bool(digest[0] & 1)
                self.assertEqual(assignment["mirrored"], expected_mirrored)
                independently_derived_parities.add(expected_mirrored)
            self.assertEqual(independently_derived_parities, {False, True})
            source_rows = {
                row["object_id"]: row
                for row in (
                    json.loads(line)
                    for line in population.read_text(encoding="utf-8").splitlines()
                )
            }
            for item in package["items"]:
                assignment = assignment_by_item[item["item_id"]]
                source = Image.open(source_rows[assignment["object_id"]]["image_path"])
                expected = ImageOps.mirror(source) if assignment["mirrored"] else source
                actual = Image.open(checking_root / "checker_A" / item["asset"])
                self.assertEqual(actual.mode, expected.mode)
                self.assertEqual(actual.size, expected.size)
                self.assertEqual(actual.tobytes(), expected.tobytes())

    def test_authorized_measurement_cannot_override_frozen_500_and_floor_40(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            population = write_synthetic_population(root)
            rows = [json.loads(line) for line in population.read_text(encoding="utf-8").splitlines()]
            for row in rows:
                row["data_class"] = "authorized_measurement"
            population.write_bytes(b"".join(canonical_json_bytes(row) + b"\n" for row in rows))
            with self.assertRaisesRegex(HandcheckError, "frozen total=500 and floor=40"):
                prepare_experiment(
                    population_path=population,
                    private_root=root / "custodian_private",
                    checking_root=root / "checking",
                    passphrase=PASSPHRASE,
                    checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                    total=18,
                    floor=1,
                )


class CheckerSessionTests(unittest.TestCase):
    def test_hc1h_session_events_require_private_control_mac_and_cannot_be_rehashed_from_package(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            private_root = root / "private"
            checking_root = root / "checking"
            prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                real_total=18,
                synthetic_total=9,
                repeat_total=6,
                real_floor=2,
            )
            package_root = checking_root / "checker_H"
            with self.assertRaises(HandcheckError):
                CheckerApplication(package_root, debounce_seconds=0.0)
            application = CheckerApplication(
                package_root,
                control_path=private_root / "checker_H_control.json",
                debounce_seconds=0.0,
            )
            state = application.public_state()
            application.submit(state["presentation_token"], "CCW")
            session_path = package_root / "answers.jsonl"
            events = [json.loads(line) for line in session_path.read_text().splitlines()]
            events[1]["label"] = -events[1]["label"]
            payload = dict(events[1])
            payload.pop("event_hash")
            events[1]["event_hash"] = hashlib.sha256(canonical_json_bytes(payload)).hexdigest()
            session_path.write_bytes(
                b"".join(canonical_json_bytes(event) + b"\n" for event in events)
            )
            with self.assertRaises(HandcheckError):
                CheckerApplication(
                    package_root,
                    control_path=private_root / "checker_H_control.json",
                    debounce_seconds=0.0,
                )

    def test_hc7_replacement_reserve_exhaustion_records_hard_inconclusive(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=root / "private",
                checking_root=root / "checking",
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                real_total=18,
                synthetic_total=9,
                repeat_total=6,
                real_floor=2,
                replacement_reserve_per_group=1,
            )
            application = CheckerApplication(
                root / "checking" / "checker_H",
                control_path=root / "private" / "checker_H_control.json",
                debounce_seconds=0.0,
            )
            group_counts: dict[str, int] = {}
            for item in application.package["items"]:
                group_counts[item["replacement_group"]] = group_counts.get(item["replacement_group"], 0) + 1
            target_group = next(group for group, count in group_counts.items() if count >= 2)
            flags = 0
            state = application.public_state()
            while application.public_state()["status"] == "ACTIVE":
                state = application.public_state()
                queue, cursor, _reserves, _systematic, _count = application._hc1h_runtime()
                if queue[cursor]["replacement_group"] == target_group:
                    state = application.flag_exposure(state["presentation_token"])
                    flags += 1
                    if state["status"] == "INCONCLUSIVE_HC7_SYSTEMATIC_EXPOSURE":
                        break
                else:
                    application.submit(state["presentation_token"], "CCW")
            self.assertEqual(flags, 2)
            self.assertEqual(state["status"], "INCONCLUSIVE_HC7_SYSTEMATIC_EXPOSURE")
            self.assertEqual(application._events[-1]["event_type"], "REPLACEMENT_RESERVE_EXHAUSTED_HC7")

    def test_hc7_systematic_exposure_is_hard_inconclusive_before_key_open(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            private_root = root / "private"
            checking_root = root / "checking"
            prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                real_total=18,
                synthetic_total=9,
                repeat_total=6,
                real_floor=2,
            )
            application = CheckerApplication(
                checking_root / "checker_H",
                control_path=private_root / "checker_H_control.json",
                debounce_seconds=0.0,
            )
            state = application.flag_exposure(
                application.public_state()["presentation_token"], systematic=True
            )
            self.assertEqual(state["status"], "INCONCLUSIVE_HC7_SYSTEMATIC_EXPOSURE")
            unseal_called = False

            def tripwire(*args: object, **kwargs: object) -> dict:
                nonlocal unseal_called
                unseal_called = True
                raise AssertionError("unseal must not be reached")

            with mock.patch("nm_handcheck.unseal_key", side_effect=tripwire):
                result = reduce_hc1h_experiment(
                    private_root=private_root,
                    checking_root=checking_root,
                    passphrase=PASSPHRASE,
                    private_output_root=root / "private_output",
                    public_output_root=root / "public_output",
                )
            self.assertFalse(unseal_called)
            self.assertEqual(result["status"], "HARD_INCONCLUSIVE_HC7_IDENTITY_EXPOSURE")
            self.assertTrue(result["event_published"])
            self.assertFalse(result["sealed_key_opened"])
            self.assertTrue((root / "public_output" / "hc1h_integrity_event.json").is_file())

    def test_hc7_flagged_real_parent_replaces_its_future_repeat_before_key_open(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            private_root = root / "private"
            checking_root = root / "checking"
            prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                real_total=18,
                synthetic_total=9,
                repeat_total=6,
                real_floor=2,
            )
            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            assignments = {
                row["item_id"]: row
                for row in sealed["assignments"] + sealed["reserve_assignments"]
            }
            application = CheckerApplication(
                checking_root / "checker_H",
                control_path=private_root / "checker_H_control.json",
                debounce_seconds=0.0,
            )
            flagged_parent = False
            while application.public_state()["status"] == "ACTIVE":
                state = application.public_state()
                queue, cursor, _reserves, _systematic, _flags = application._hc1h_runtime()
                public_item = queue[cursor]
                assignment = assignments[public_item["item_id"]]
                if not flagged_parent and public_item["dependent_item_id"] is not None:
                    application.flag_exposure(state["presentation_token"])
                    flagged_parent = True
                    continue
                truth = assignment.get("truth_sign", assignment.get("instrument_sign"))
                presented = -truth if assignment["mirrored"] else truth
                application.submit(
                    state["presentation_token"], "CCW" if presented == 1 else "CW"
                )
            self.assertTrue(flagged_parent)
            result = reduce_hc1h_experiment(
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                private_output_root=root / "private_output",
                public_output_root=root / "public_output",
            )
            self.assertEqual(result["counts_used"], {"real": 18, "synthetic": 9, "repeat": 6})
            self.assertEqual(result["specific_hc7_flags_replaced"], 1)

    def test_hc7_specific_exposure_flag_discards_item_and_appends_same_blind_group_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=root / "private",
                checking_root=root / "checking",
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                real_total=18,
                synthetic_total=9,
                repeat_total=6,
                real_floor=2,
                replacement_reserve_per_group=1,
            )
            package_root = root / "checking" / "checker_H"
            application = CheckerApplication(
                package_root,
                control_path=root / "private" / "checker_H_control.json",
                debounce_seconds=0.0,
            )
            before = application.public_state()
            first_asset = application.current_asset(before["presentation_token"])[0]
            after = application.flag_exposure(before["presentation_token"])
            self.assertEqual(after["progress"], {"completed": 0, "total": 33})
            self.assertEqual(after["hc7_specific_flags"], 1)
            self.assertNotEqual(
                application.current_asset(after["presentation_token"])[0], first_asset
            )
            application = CheckerApplication(
                package_root,
                control_path=root / "private" / "checker_H_control.json",
                debounce_seconds=0.0,
            )
            self.assertEqual(application.public_state()["hc7_specific_flags"], 1)
            self.assertEqual(application.completed, 0)
            self.assertIn(b"Flag suspected synthetic/repeat exposure", CHECKER_HTML)

    def test_single_key_is_append_only_debounced_isolated_and_lossless_on_resume(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            population = write_synthetic_population(root)
            prepare_experiment(
                population_path=population,
                private_root=root / "custodian_private",
                checking_root=root / "checking",
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            package_a = root / "checking/checker_A"
            package_b = root / "checking/checker_B"
            app_a = CheckerApplication(package_a, debounce_seconds=0.35)
            initial = app_a.public_state()
            self.assertEqual(initial["progress"], {"completed": 0, "total": 18})
            self.assertNotIn("item_id", canonical_json_bytes(initial).decode())
            first_token = initial["presentation_token"]

            after_first = app_a.submit(first_token, "CCW", monotonic_value=10.0)
            self.assertEqual(after_first["progress"], {"completed": 1, "total": 18})
            with self.assertRaises(HandcheckError):
                app_a.submit(first_token, "CW", monotonic_value=10.01)
            with self.assertRaises(HandcheckError):
                app_a.submit(after_first["presentation_token"], "CW", monotonic_value=10.1)

            session_path = package_a / "answers.jsonl"
            before_resume = session_path.read_bytes()
            resumed = CheckerApplication(package_a, debounce_seconds=0.35)
            self.assertEqual(resumed.public_state()["progress"], {"completed": 1, "total": 18})
            self.assertEqual(session_path.read_bytes(), before_resume)
            resumed.submit(resumed.public_state()["presentation_token"], "CW", monotonic_value=11.0)
            self.assertEqual(len(session_path.read_text(encoding="utf-8").splitlines()), 3)

            app_b = CheckerApplication(package_b)
            state_b = app_b.public_state()
            self.assertEqual(state_b["progress"], {"completed": 0, "total": 18})
            self.assertFalse((package_b / "answers.jsonl").exists())
            self.assertNotIn("answers", canonical_json_bytes(state_b).decode())

    def test_two_resumed_processes_cannot_append_the_same_next_item(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            checking_root = root / "checking"
            prepare_experiment(
                population_path=write_synthetic_population(root),
                private_root=root / "custodian_private",
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            package = checking_root / "checker_A"
            initial = CheckerApplication(package, debounce_seconds=0.0)
            initial.submit(initial.public_state()["presentation_token"], "CCW")
            first = CheckerApplication(package, debounce_seconds=0.0)
            stale = CheckerApplication(package, debounce_seconds=0.0)
            token = first.public_state()["presentation_token"]
            first.submit(token, "CW")
            stable_bytes = (package / "answers.jsonl").read_bytes()
            with self.assertRaises(HandcheckError):
                stale.submit(token, "CCW")
            self.assertEqual((package / "answers.jsonl").read_bytes(), stable_bytes)
            resumed = CheckerApplication(package, debounce_seconds=0.0)
            self.assertEqual(resumed.public_state()["progress"]["completed"], 2)

    def test_http_checking_path_serves_only_current_blinded_image_and_no_peer_or_key_material(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            population = write_synthetic_population(root)
            private_root = root / "custodian_private"
            checking_root = root / "checking"
            prepare_experiment(
                population_path=population,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            app_a = CheckerApplication(checking_root / "checker_A", debounce_seconds=0.0)
            app_a.submit(app_a.public_state()["presentation_token"], "CCW")
            peer_session_hash = hashlib.sha256(
                (checking_root / "checker_A/answers.jsonl").read_bytes()
            ).hexdigest().encode()
            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)

            app_b = CheckerApplication(checking_root / "checker_B", debounce_seconds=0.0)
            server = ThreadingHTTPServer(("127.0.0.1", 0), make_checker_http_handler(app_b))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = f"http://127.0.0.1:{server.server_port}"
            try:
                html = request.urlopen(base + "/", timeout=3).read()
                state = json.loads(request.urlopen(base + "/api/state", timeout=3).read())
                image = request.urlopen(base + state["asset_url"], timeout=3).read()
                self.assertTrue(image.startswith(b"\x89PNG"))
                exposed = html + canonical_json_bytes(state)
                self.assertNotIn(bytes.fromhex(sealed["root_secret_hex"]), exposed)
                self.assertNotIn(peer_session_hash, exposed)
                for assignment in sealed["assignments"]:
                    self.assertNotIn(assignment["object_id"].encode(), exposed)
                self.assertIn(b"event.repeat", html)
                self.assertIn(b"locked", html)

                for forbidden_route in (
                    "/package.json",
                    "/answers.jsonl",
                    "/sealed_key.nmhc",
                    "/../custodian_private/sealed_key.nmhc",
                    "/checker_A/answers.jsonl",
                ):
                    with self.assertRaises(error.HTTPError) as caught:
                        request.urlopen(base + forbidden_route, timeout=3)
                    self.assertEqual(caught.exception.code, 404)

                payload = canonical_json_bytes(
                    {"presentation_token": state["presentation_token"], "label": "CCW"}
                )
                posted = request.Request(
                    base + "/api/answer",
                    data=payload,
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                next_state = json.loads(request.urlopen(posted, timeout=3).read())
                self.assertEqual(next_state["progress"], {"completed": 1, "total": 18})
                with self.assertRaises(error.HTTPError) as caught:
                    request.urlopen(posted, timeout=3)
                self.assertEqual(caught.exception.code, 409)
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=3)


class AdjudicationTests(unittest.TestCase):
    def test_adjudicator_package_contains_only_disagreements_and_preserves_original_commitment(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            population = write_synthetic_population(root)
            checking_root = root / "checking"
            private_root = root / "custodian_private"
            prepare_experiment(
                population_path=population,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            package_a = load_checker_package(checking_root / "checker_A")
            item_ids = sorted(item["item_id"] for item in package_a["items"])
            labels_a = {item_id: ("CCW" if index % 2 == 0 else "CW") for index, item_id in enumerate(item_ids)}
            labels_b = dict(labels_a)
            disagreements = set(item_ids[:4])
            for item_id in disagreements:
                labels_b[item_id] = "CW" if labels_a[item_id] == "CCW" else "CCW"
            complete_session(checking_root / "checker_A", labels_a)
            complete_session(checking_root / "checker_B", labels_b)

            original_commitment = (checking_root / "commitment.json").read_bytes()
            receipt = make_adjudication_package(checking_root)
            self.assertEqual(receipt["disagreements"], 4)
            self.assertEqual((checking_root / "commitment.json").read_bytes(), original_commitment)

            package_j = load_checker_package(checking_root / "checker_J")
            self.assertEqual({item["item_id"] for item in package_j["items"]}, disagreements)
            for item in package_j["items"]:
                self.assertEqual(set(item["prior_labels"]), {"A", "B"})
                self.assertNotEqual(item["prior_labels"]["A"], item["prior_labels"]["B"])
            app_j = CheckerApplication(checking_root / "checker_J")
            self.assertEqual(set(app_j.public_state()["prior_labels"]), {"A", "B"})

            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            adjudicator_bytes = b"".join(
                path.read_bytes()
                for path in (checking_root / "checker_J").rglob("*")
                if path.is_file()
            )
            self.assertNotIn(bytes.fromhex(sealed["root_secret_hex"]), adjudicator_bytes)
            for assignment in sealed["assignments"]:
                self.assertNotIn(assignment["object_id"].encode(), adjudicator_bytes)


class ReductionMathTests(unittest.TestCase):
    def test_f10_masked_public_projection_does_not_name_failing_strata(self) -> None:
        statistics = {
            "strata": [
                {"stratum": stratum, "trials": 30, "corrected_rate": 0.5}
                for stratum in HC1H_STRATA
            ],
            "verdict": {
                "verdict": "INCONCLUSIVE-BY-POWER",
                "failing_strata": ["disagree|1"],
                "gates": {
                    "all_corrected_strata_ge_0_70": False,
                    "epsilon_le_0_05": True,
                },
            },
        }
        public_statistics, public_strata = _hc1h_public_projection(statistics)
        self.assertTrue(all(row["masked"] for row in public_strata))
        self.assertNotIn("failing_strata", public_statistics["verdict"])
        self.assertEqual(public_statistics["verdict"]["verdict"], "WITHHELD_F10_MASKED_STRATA")
        self.assertFalse(public_statistics["verdict"]["decision_public"])
        self.assertNotIn(
            "all_corrected_strata_ge_0_70",
            public_statistics["verdict"]["non_stratum_gates"],
        )
        self.assertTrue(public_statistics["verdict"]["non_stratum_gates"]["epsilon_le_0_05"])
        self.assertEqual(statistics["verdict"]["failing_strata"], ["disagree|1"])

    def test_hc1h_pilot_is_150_labels_requires_ui_ergonomics_and_excludes_40_injections_from_full(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(
                root, real_per_stratum=12, synthetic_per_stratum=10
            )
            private_root = root / "pilot_private"
            checking_root = root / "pilot_checking"
            receipt = prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                mode="pilot",
                real_total=90,
                synthetic_total=40,
                repeat_total=20,
                real_floor=10,
            )
            self.assertEqual(receipt["labels_required"], 150)
            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            assignments = {
                row["item_id"]: row
                for row in sealed["assignments"] + sealed["reserve_assignments"]
            }
            application = CheckerApplication(
                checking_root / "checker_H",
                control_path=private_root / "checker_H_control.json",
                debounce_seconds=0.0,
            )
            while application.public_state()["status"] not in {"AWAITING_ERGONOMICS", "COMPLETE"}:
                state = application.public_state()
                if state["status"] == "BREAK_REQUIRED":
                    application.acknowledge_break()
                    continue
                queue, cursor, _reserves, _systematic, _flags = application._hc1h_runtime()
                assignment = assignments[queue[cursor]["item_id"]]
                truth = assignment.get("truth_sign", assignment.get("instrument_sign"))
                presented = -truth if assignment["mirrored"] else truth
                application.submit(
                    state["presentation_token"], "CCW" if presented == 1 else "CW"
                )
            self.assertEqual(application.public_state()["status"], "AWAITING_ERGONOMICS")
            self.assertEqual(
                sum(
                    event.get("event_type") == "BREAK_ACKNOWLEDGED"
                    for event in application._events[1:]
                ),
                2,
            )
            completed = application.record_ergonomics(True)
            self.assertEqual(completed["status"], "COMPLETE")
            result = reduce_hc1h_experiment(
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                private_output_root=root / "pilot_private_output",
                public_output_root=root / "pilot_public_output",
            )
            self.assertEqual(result["pilot_outcome"], "PASS-TO-FULL-HC1H")
            self.assertEqual(result["counts_used"], {"real": 90, "synthetic": 40, "repeat": 20})
            self.assertFalse(result["boundaries"]["pilot_synthetics_count_toward_full"])
            self.assertNotIn("attenuation", result["statistics"])
            self.assertNotIn("strata", result["statistics"])
            self.assertNotIn("repeat_diagnostic", result["statistics"])
            full_receipt = prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=root / "full_private_after_pilot",
                checking_root=root / "full_checking_after_pilot",
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                real_total=18,
                synthetic_total=9,
                repeat_total=6,
                real_floor=2,
                pilot_private_root=private_root,
                pilot_public_result_path=root
                / "pilot_public_output"
                / "hc1h_aggregates.json",
            )
            self.assertFalse(full_receipt["pilot_exclusion"]["pilot_synthetics_reused"])
            full_sealed = unseal_key(
                root / "full_private_after_pilot" / "sealed_key.nmhc", PASSPHRASE
            )
            pilot_ids = {
                row["synthetic_id"]
                for row in sealed["assignments"] + sealed["reserve_assignments"]
                if row["category"] == "synthetic"
            }
            full_ids = {
                row["synthetic_id"]
                for row in full_sealed["assignments"] + full_sealed["reserve_assignments"]
                if row["category"] == "synthetic"
            }
            self.assertTrue(pilot_ids.isdisjoint(full_ids))

    def test_hc1h_reduction_uses_one_checker_and_excludes_injections_and_repeats_from_real_a(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            real_population, injection_pool, prior_rates = write_hc1h_pools(root)
            private_root = root / "private"
            checking_root = root / "checking"
            prepare_hc1h_experiment(
                real_population_path=real_population,
                synthetic_pool_path=injection_pool,
                neyman_prior_rates=prior_rates,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_id="synthetic-duho",
                real_total=18,
                synthetic_total=9,
                repeat_total=6,
                real_floor=2,
            )
            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            assignments = {
                row["item_id"]: row
                for row in sealed["assignments"] + sealed["reserve_assignments"]
            }
            application = CheckerApplication(
                checking_root / "checker_H",
                control_path=private_root / "checker_H_control.json",
                debounce_seconds=0.0,
            )
            while application.public_state()["status"] == "ACTIVE":
                state = application.public_state()
                queue, cursor, _reserves, _systematic, _flags = application._hc1h_runtime()
                assignment = assignments[queue[cursor]["item_id"]]
                truth = assignment.get("truth_sign", assignment.get("instrument_sign"))
                presented = -truth if assignment["mirrored"] else truth
                application.submit(
                    state["presentation_token"], "CCW" if presented == 1 else "CW"
                )
            result = reduce_hc1h_experiment(
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                private_output_root=root / "private_output",
                public_output_root=root / "public_output",
            )
            self.assertEqual(result["counts_used"], {"real": 18, "synthetic": 9, "repeat": 6})
            self.assertEqual(result["statistics"]["epsilon_exact_fraction"], "0/1")
            self.assertEqual(result["statistics"]["attenuation_exact_fraction"], "1/1")
            self.assertEqual(result["statistics"]["repeat_diagnostic"]["nonflips"], 0)
            self.assertEqual(
                result["statistics"]["repeat_diagnostic"]["by_session_block"],
                [
                    {
                        "session_block": 1,
                        "trials": 6,
                        "nonflips": 0,
                        "nonflip_rate_exact": "0/1",
                        "enters_primary_repeat_gate": False,
                    }
                ],
            )
            self.assertEqual(len(result["machine_committee_diagnostic"]), 3)
            for row in result["machine_committee_diagnostic"]:
                self.assertEqual(row["disagree_rate_exact"], "1/3")
                self.assertFalse(row["enters_attenuation"])
            private_rows = (root / "private_output" / "per_presentation_hc1h.jsonl").read_text().splitlines()
            self.assertEqual(len(private_rows), 33)
            self.assertNotIn("object_id", (root / "public_output" / "hc1h_aggregates.json").read_text())

    def test_hc1h_exact_lower_bound_quality_floor_is_never_rounded_up(self) -> None:
        rates = {f"{state}|{chi}": Decimal("0.90") for state in HC1H_STATES for chi in range(3)}
        below = hc1h_verdict(
            attenuation=Decimal("0.849"),
            sigma=Decimal("0"),
            stratum_rates=rates,
            epsilon=Decimal("0.02"),
            repeat_compatible=True,
            synthetic_diagnostics_compatible=True,
            hc7_systematic_exposure=False,
        )
        edge = hc1h_verdict(
            attenuation=Decimal("0.850"),
            sigma=Decimal("0"),
            stratum_rates=rates,
            epsilon=Decimal("0.05"),
            repeat_compatible=True,
            synthetic_diagnostics_compatible=True,
            hc7_systematic_exposure=False,
        )
        self.assertEqual(below["verdict"], "INCONCLUSIVE-BY-POWER")
        self.assertEqual(edge["verdict"], "PASS_HC1H_ATTENUATION")
        self.assertTrue(edge["decision_used_unrounded_values"])
        self.assertEqual(edge["power_bound_n"], 130076)
        self.assertEqual(edge["power_threshold_exact"], "0.7905")

    def test_hc1h_noise_correction_and_shared_epsilon_covariance_are_explicit(self) -> None:
        populations = {f"{state}|{chi}": 1000 for state in HC1H_STATES for chi in range(3)}
        real_counts = {
            stratum: {"trials": 50, "raw_agreements": 47} for stratum in populations
        }
        synthetic_counts = {
            stratum: {"trials": 20, "errors": 1} for stratum in populations
        }
        result = hc1h_statistics(
            real_counts=real_counts,
            stratum_populations=populations,
            synthetic_counts=synthetic_counts,
            repeat_nonflips=6,
            repeat_trials=150,
        )
        self.assertEqual(result["epsilon_exact_fraction"], "1/20")
        self.assertEqual(result["attenuation_exact_fraction"], "89/90")
        self.assertGreater(result["variance"]["shared_epsilon_component"], 0.0)
        self.assertGreater(result["variance"]["total"], result["variance"]["independent_raw_component"])
        self.assertTrue(result["repeat_diagnostic"]["compatible_with_global_epsilon_2sigma"])
        self.assertEqual(result["verdict"]["verdict"], "PASS_HC1H_ATTENUATION")
        with_extra = hc1h_statistics(
            real_counts=real_counts,
            stratum_populations=populations,
            synthetic_counts=synthetic_counts,
            repeat_nonflips=6,
            repeat_trials=150,
            additional_covariance=Decimal("0.0004"),
        )
        self.assertAlmostEqual(
            with_extra["variance"]["total"] - result["variance"]["total"],
            0.0004,
            places=12,
        )
        self.assertEqual(with_extra["variance"]["additional_covariance_exact"], "0.0004")
        self.assertGreater(with_extra["sigma"], result["sigma"])

    def test_incomplete_checking_fails_before_unseal_is_called(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            private_root = root / "custodian_private"
            checking_root = root / "checking"
            prepare_experiment(
                population_path=write_synthetic_population(root),
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            with mock.patch("nm_handcheck.unseal_key", side_effect=AssertionError("early unseal")) as patched:
                with self.assertRaisesRegex(HandcheckError, "complete before unsealing"):
                    reduce_experiment(
                        private_root=private_root,
                        checking_root=checking_root,
                        passphrase=PASSPHRASE,
                        private_output_root=root / "private_output",
                        public_output_root=root / "public_output",
                    )
            patched.assert_not_called()

    def test_private_reduction_output_cannot_be_placed_in_a_checker_capability(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            private_root = root / "custodian_private"
            checking_root = root / "checking"
            prepare_experiment(
                population_path=write_synthetic_population(root),
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            with self.assertRaisesRegex(HandcheckError, "private reduction output cannot overlap checking"):
                reduce_experiment(
                    private_root=private_root,
                    checking_root=checking_root,
                    passphrase=PASSPHRASE,
                    private_output_root=checking_root / "checker_A/private_reduction",
                    public_output_root=root / "public_output",
                )

    def test_unrounded_0849_is_inconclusive_and_exact_threshold_is_not_nudged(self) -> None:
        healthy_strata = {f"{chi}{size}": Decimal("0.90") for chi in range(3) for size in range(3)}
        below = hc5_verdict(Decimal("0.849"), healthy_strata)
        self.assertEqual(below["verdict"], "INCONCLUSIVE-BY-POWER")
        self.assertEqual(below["overall_a_exact"], "0.849")

        exact = hc5_verdict(Decimal("0.850"), healthy_strata)
        self.assertEqual(exact["verdict"], "PASS_HC5_ATTENUATION")
        weak = dict(healthy_strata)
        weak["22"] = Decimal("0.699")
        self.assertEqual(
            hc5_verdict(Decimal("0.90"), weak)["verdict"],
            "INCONCLUSIVE-BY-POWER",
        )
        weak["22"] = Decimal("0.700")
        self.assertEqual(hc5_verdict(Decimal("0.85"), weak)["verdict"], "PASS_HC5_ATTENUATION")
        with self.assertRaisesRegex(HandcheckError, "exactly nine strata"):
            hc5_verdict(Decimal("0.90"), {"00": Decimal("0.90")})

    def test_nonuniform_mixed_rates_pin_population_weighting_wilson_and_fpc_delta_math(self) -> None:
        populations = {
            "00": 160, "01": 80, "02": 60,
            "10": 80, "11": 120, "12": 100,
            "20": 60, "21": 100, "22": 140,
        }
        sample_counts = {
            "00": 86, "01": 43, "02": 40,
            "10": 43, "11": 65, "12": 54,
            "20": 40, "21": 54, "22": 75,
        }
        agreements = {
            "00": 80, "01": 35, "02": 30,
            "10": 40, "11": 55, "12": 50,
            "20": 32, "21": 50, "22": 65,
        }
        counts = {
            stratum: {"sample_count": sample_counts[stratum], "agreements": agreements[stratum]}
            for stratum in populations
        }
        strata, overall, sigma_a, _ = _summarize_strata(counts, populations)
        self.assertEqual(f"{overall.numerator}/{overall.denominator}", "11914853/13583700")
        self.assertAlmostEqual(float(overall), 0.8771434145335955, places=15)
        self.assertAlmostEqual(sigma_a, 0.00955343512459575, places=15)
        self.assertAlmostEqual(2.0 * sigma_a, 0.0191068702491915, places=15)
        row00 = {row["stratum"]: row for row in strata}["00"]
        self.assertAlmostEqual(row00["wilson_68_lower"], 0.8977416154744382, places=15)
        self.assertAlmostEqual(row00["wilson_68_upper"], 0.9529411780659609, places=15)
        self.assertEqual(row00["finite_population_correction_exact"], "74/159")

    def test_reduction_unseals_after_all_labels_and_separates_private_rows_from_public_aggregates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            population = write_synthetic_population(root)
            private_root = root / "custodian_private"
            checking_root = root / "checking"
            prepare_experiment(
                population_path=population,
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            target = {
                row["item_id"]: (
                    "CCW"
                    if row["instrument_sign"] * (-1 if row["mirrored"] else 1) == 1
                    else "CW"
                )
                for row in sealed["assignments"]
            }
            labels_a = dict(target)
            labels_b = dict(target)
            disagreement_ids = sorted(target)[:4]
            for item_id in disagreement_ids:
                labels_b[item_id] = "CW" if target[item_id] == "CCW" else "CCW"
            complete_session(checking_root / "checker_A", labels_a)
            complete_session(checking_root / "checker_B", labels_b)
            make_adjudication_package(checking_root)
            complete_session(
                checking_root / "checker_J",
                {item_id: target[item_id] for item_id in disagreement_ids},
            )

            private_output = root / "reduction_private"
            public_output = root / "release_candidate"
            result = reduce_experiment(
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                private_output_root=private_output,
                public_output_root=public_output,
            )
            self.assertEqual(result["hc5"]["verdict"], "PASS_HC5_ATTENUATION")
            self.assertEqual(result["attenuation"]["a_exact_fraction"], "1/1")
            self.assertEqual(len(result["strata"]), 9)
            self.assertTrue(all(row["masked"] for row in result["strata"]))
            self.assertTrue(all(set(row) == {"stratum", "masked", "mask_reason"} for row in result["strata"]))
            private_aggregates = json.loads(
                (private_output / "stratum_aggregates_private.json").read_bytes()
            )
            self.assertTrue(
                all(row["agreement_rate_exact"] == "1/1" for row in private_aggregates["strata"])
            )

            public_files = {path.name for path in public_output.iterdir()}
            self.assertEqual(public_files, {"handcheck_aggregates.json", "handcheck_aggregates.csv"})
            private_rows = (private_output / "per_object_handcheck.jsonl").read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(private_rows), 18)
            private_objects = [json.loads(line)["object_id"] for line in private_rows]
            self.assertEqual(private_objects, sorted(private_objects))
            public_bytes = b"".join(path.read_bytes() for path in public_output.iterdir())
            self.assertNotIn(bytes.fromhex(sealed["root_secret_hex"]), public_bytes)
            self.assertNotIn(b"item_id", public_bytes)
            self.assertNotIn(b"object_id", public_bytes)
            self.assertNotIn(b"mirrored", public_bytes)
            self.assertNotIn(b"failing_strata", public_bytes)
            for assignment in sealed["assignments"]:
                self.assertNotIn(assignment["object_id"].encode(), public_bytes)

    def test_zero_disagreements_requires_no_adjudicator_keystrokes_or_session_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            private_root = root / "custodian_private"
            checking_root = root / "checking"
            prepare_experiment(
                population_path=write_synthetic_population(root),
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            labels = {
                row["item_id"]: (
                    "CCW"
                    if row["instrument_sign"] * (-1 if row["mirrored"] else 1) == 1
                    else "CW"
                )
                for row in sealed["assignments"]
            }
            complete_session(checking_root / "checker_A", labels)
            complete_session(checking_root / "checker_B", labels)
            receipt = make_adjudication_package(checking_root)
            self.assertEqual(receipt["disagreements"], 0)
            app_j = CheckerApplication(checking_root / "checker_J")
            self.assertEqual(app_j.public_state()["status"], "COMPLETE")
            self.assertFalse((checking_root / "checker_J/answers.jsonl").exists())

            result = reduce_experiment(
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                private_output_root=root / "private_output",
                public_output_root=root / "public_output",
            )
            self.assertEqual(result["disagreements_adjudicated"], 0)
            self.assertEqual(
                result["commitments"]["adjudicator_session_sha256"],
                "NONE_NO_DISAGREEMENTS",
            )

    def test_rehashed_public_commitment_tampering_fails_against_private_custody_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            private_root = root / "custodian_private"
            checking_root = root / "checking"
            prepare_experiment(
                population_path=write_synthetic_population(root),
                private_root=private_root,
                checking_root=checking_root,
                passphrase=PASSPHRASE,
                checker_ids={"A": "synthetic-alice", "B": "synthetic-bob", "J": "synthetic-jules"},
                total=18,
                floor=1,
            )
            commitment_path = checking_root / "commitment.json"
            commitment = json.loads(commitment_path.read_bytes())
            commitment["public_boundary"] = "tampered after preparation"
            tampered_bytes = canonical_json_bytes(commitment) + b"\n"
            commitment_path.write_bytes(tampered_bytes)
            (checking_root / "commitment.sha256").write_text(
                hashlib.sha256(tampered_bytes).hexdigest() + "\n",
                encoding="utf-8",
            )

            sealed = unseal_key(private_root / "sealed_key.nmhc", PASSPHRASE)
            labels = {
                row["item_id"]: (
                    "CCW"
                    if row["instrument_sign"] * (-1 if row["mirrored"] else 1) == 1
                    else "CW"
                )
                for row in sealed["assignments"]
            }
            complete_session(checking_root / "checker_A", labels)
            complete_session(checking_root / "checker_B", labels)
            make_adjudication_package(checking_root)
            with self.assertRaisesRegex(HandcheckError, "private preparation receipt"):
                reduce_experiment(
                    private_root=private_root,
                    checking_root=checking_root,
                    passphrase=PASSPHRASE,
                    private_output_root=root / "private_output",
                    public_output_root=root / "public_output",
                )


if __name__ == "__main__":
    unittest.main()
