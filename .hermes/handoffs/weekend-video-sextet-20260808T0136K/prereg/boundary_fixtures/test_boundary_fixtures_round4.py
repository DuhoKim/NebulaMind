#!/usr/bin/env python3
"""Round-4 production-shaped RICE_1 image-HDU-1 read-path fixtures."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
from astropy.io import fits

import make_boundary_fixtures as round1
import make_boundary_fixtures_round2 as round2
import make_boundary_fixtures_round3 as round3
from make_boundary_fixtures_round4 import (
    PINNED_ROUND1_SHA256,
    PINNED_ROUND2_SHA256,
    PINNED_ROUND3_SHA256,
    REQUIRED_RAW_COMPRESSION_KEYWORDS,
    ROUND4_BRIEF_SHA256,
    ROUND4_CASE_IDS,
    generate_round4_fixture_tree,
    verify_round4_fixture_tree,
)

EXPECTED_BRIEF_SHA256 = "17641b84ff89811534b1cb297d91c2da894dcd5ad3350920da0e528464748db2"
EXPECTED_CASE_ROLES = {
    "centre": "centre",
    "dec_max_exact_boundary": "edge",
    "corner_north_west_exact": "corner",
}


def _read_raw_header_cards(blob: bytes, offset: int) -> tuple[dict[str, bytes], int]:
    """Parse one FITS header directly from 2880-byte blocks."""
    cards: dict[str, bytes] = {}
    cursor = offset
    while True:
        block = blob[cursor : cursor + 2880]
        if len(block) != 2880:
            raise AssertionError("truncated FITS header block")
        for card_offset in range(0, 2880, 80):
            card = block[card_offset : card_offset + 80]
            keyword = card[:8].decode("ascii").strip()
            if keyword and keyword not in cards:
                cards[keyword] = card
            if keyword == "END":
                return cards, cursor + 2880
        cursor += 2880


class BoundaryFixtureRound4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = Path(__file__).resolve().parent
        cls._temporary = tempfile.TemporaryDirectory(
            prefix="_tmp_boundary_fixtures_round4_",
            dir=fixture_root,
        )
        cls.root = Path(cls._temporary.name)
        cls.manifest = generate_round4_fixture_tree(cls.root)
        cls.rows = json.loads((cls.root / "objects.json").read_text(encoding="utf-8"))
        cls.by_id = {row["object_id"]: row for row in cls.rows}
        cls.bricks = {row["brick_id"]: row for row in cls.manifest["bricks"]}

        cls.round1_rows = {row["object_id"]: row for row in round1.fixture_cases()}
        round3_geometry, round3_rows = round3.build_geometry_and_cases()
        cls.round3_rows = {row["object_id"]: row for row in round3_rows}
        cls.round3_bricks = {row["brick_id"]: row for row in round3_geometry}

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temporary.cleanup()

    def _parent_expected(self, row: dict[str, object]) -> np.ndarray:
        source_round = row["source_round"]
        source_object_id = str(row["source_object_id"])
        if source_round == "round1":
            parent = self.round1_rows[source_object_id]
            return round1.expected_cutout(parent["center_x"], parent["center_y"])
        if source_round == "round3":
            parent = self.round3_rows[source_object_id]
            expected, _ = round2._analytic_expected(parent, self.round3_bricks)
            return expected
        raise AssertionError(f"unexpected parent round: {source_round}")

    def _parent_source_data(self, brick: dict[str, object]) -> np.ndarray:
        if brick["source_round"] == "round1":
            return round1.brick_pattern(int(brick["origin_x"]), int(brick["origin_y"]))
        if brick["source_round"] == "round3":
            return round2._source_pattern(brick["wcs"], float(brick["value_offset"]))
        raise AssertionError(f"unexpected source round: {brick['source_round']}")

    def test_parent_generators_and_round4_brief_are_exactly_pinned(self) -> None:
        fixture_root = Path(__file__).resolve().parent
        observed = {
            "round1": hashlib.sha256((fixture_root / "make_boundary_fixtures.py").read_bytes()).hexdigest(),
            "round2": hashlib.sha256(
                (fixture_root / "make_boundary_fixtures_round2.py").read_bytes()
            ).hexdigest(),
            "round3": hashlib.sha256(
                (fixture_root / "make_boundary_fixtures_round3.py").read_bytes()
            ).hexdigest(),
        }
        self.assertEqual(observed["round1"], PINNED_ROUND1_SHA256)
        self.assertEqual(observed["round2"], PINNED_ROUND2_SHA256)
        self.assertEqual(observed["round3"], PINNED_ROUND3_SHA256)
        self.assertEqual(ROUND4_BRIEF_SHA256, EXPECTED_BRIEF_SHA256)
        self.assertEqual(
            self.manifest["parent_generator_sha256"],
            observed,
        )
        self.assertEqual(self.manifest["brief_sha256"], EXPECTED_BRIEF_SHA256)

    def test_manifest_declares_read_path_scope_without_new_geometry(self) -> None:
        self.assertEqual(self.manifest["schema_version"], "yui-boundary-fixtures-round4-v1")
        self.assertTrue(self.manifest["synthetic_only"])
        self.assertEqual(self.manifest["compression_type"], "RICE_1")
        self.assertEqual(self.manifest["image_hdu_index"], 1)
        self.assertEqual(self.manifest["object_count"], 3)
        self.assertEqual(list(ROUND4_CASE_IDS), list(EXPECTED_CASE_ROLES))
        self.assertEqual([row["object_id"] for row in self.rows], list(EXPECTED_CASE_ROLES))
        self.assertEqual(
            {row["object_id"]: row["fixture_role"] for row in self.rows},
            EXPECTED_CASE_ROLES,
        )

        scope = self.manifest["scope"]
        self.assertTrue(scope["tests_production_shaped_fits_fz_hdu1_read_path"])
        self.assertTrue(scope["tests_raw_compressed_table_header_axes"])
        self.assertTrue(scope["tests_exact_selected_parent_expectations"])
        self.assertFalse(scope["introduces_new_geometry"])
        self.assertFalse(scope["validates_production_adapter"])
        self.assertFalse(scope["uses_real_survey_data"])
        self.assertFalse(scope["uses_network"])

    def test_expected_arrays_are_exact_round1_and_round3_expectations(self) -> None:
        observed_parent_rounds: set[str] = set()
        for row in self.rows:
            observed_parent_rounds.add(str(row["source_round"]))
            expected = np.load(self.root / row["expected_array_path"], allow_pickle=False)
            parent_expected = self._parent_expected(row)
            np.testing.assert_array_equal(expected, parent_expected)
            self.assertEqual(expected.dtype, np.dtype("float32"))
            self.assertEqual(expected.shape, (round1.CUTOUT_SIZE, round1.CUTOUT_SIZE))
            self.assertEqual(
                row["expected_data_sha256"],
                hashlib.sha256(expected.tobytes(order="C")).hexdigest(),
            )
            self.assertEqual(
                row["expected_array_sha256"],
                round1.sha256_path(self.root / row["expected_array_path"]),
            )
        self.assertEqual(observed_parent_rounds, {"round1", "round3"})

    def test_every_brick_is_raw_rice_tile_compressed_with_empty_primary_and_image_at_hdu1(self) -> None:
        axis_divergence_count = 0
        for brick in self.bricks.values():
            path = self.root / brick["relative_path"]
            blob = path.read_bytes()
            self.assertTrue(blob.startswith(b"SIMPLE  ="))
            self.assertFalse(blob.startswith(b"\x1f\x8b"))

            primary_cards, extension_offset = _read_raw_header_cards(blob, 0)
            extension_cards, _ = _read_raw_header_cards(blob, extension_offset)
            self.assertIn(b"NAXIS   =                    0", primary_cards["NAXIS"])
            for keyword in REQUIRED_RAW_COMPRESSION_KEYWORDS:
                self.assertIn(keyword, extension_cards)
                self.assertEqual(
                    brick["raw_compression_header_cards"][keyword],
                    extension_cards[keyword].decode("ascii"),
                )

            with fits.open(path, memmap=False, disable_image_compression=True) as raw_hdus:
                self.assertEqual(len(raw_hdus), 2)
                raw_header = raw_hdus[1].header
                self.assertTrue(raw_header["ZIMAGE"])
                self.assertEqual(raw_header["ZCMPTYPE"], "RICE_1")
                self.assertEqual(
                    (raw_header["ZNAXIS2"], raw_header["ZNAXIS1"]),
                    (round1.BRICK_SIZE, round1.BRICK_SIZE),
                )
                self.assertGreater(raw_header["ZTILE1"], 0)
                self.assertGreater(raw_header["ZTILE2"], 0)
                if (
                    raw_header["NAXIS1"] != raw_header["ZNAXIS1"]
                    and raw_header["NAXIS2"] != raw_header["ZNAXIS2"]
                ):
                    axis_divergence_count += 1
                self.assertEqual(
                    brick["raw_table_axes"],
                    {
                        "NAXIS1": raw_header["NAXIS1"],
                        "NAXIS2": raw_header["NAXIS2"],
                        "ZNAXIS1": raw_header["ZNAXIS1"],
                        "ZNAXIS2": raw_header["ZNAXIS2"],
                        "ZTILE1": raw_header["ZTILE1"],
                        "ZTILE2": raw_header["ZTILE2"],
                    },
                )

            with fits.open(path, memmap=False) as logical_hdus:
                self.assertEqual(len(logical_hdus), 2)
                self.assertIsNone(logical_hdus[0].data)
                self.assertIsInstance(logical_hdus[1], fits.CompImageHDU)
                self.assertEqual(logical_hdus[1].compression_type, "RICE_1")
                restored = np.asarray(logical_hdus[1].data)
                parent_source = self._parent_source_data(brick)
                np.testing.assert_array_equal(restored, parent_source)
                self.assertEqual(
                    brick["data_sha256"],
                    hashlib.sha256(restored.tobytes(order="C")).hexdigest(),
                )

        self.assertGreaterEqual(axis_divergence_count, 1)

    def test_generated_tree_replay_reverifies_every_file_and_parent_expectation(self) -> None:
        receipt = verify_round4_fixture_tree(self.root)
        self.assertEqual(receipt["status"], "PASS_REPLAYED_SYNTHETIC_BOUNDARY_FIXTURES_ROUND4")
        self.assertEqual(receipt["case_ids"], list(ROUND4_CASE_IDS))
        self.assertEqual(receipt["brick_count"], 5)
        self.assertEqual(receipt["object_count"], 3)
        self.assertEqual(receipt["raw_tile_compression_proof_count"], 5)
        self.assertEqual(receipt["exact_source_roundtrip_count"], 5)
        self.assertEqual(receipt["compressed_table_axis_divergence_count"], 5)
        self.assertEqual(receipt["exact_parent_expectation_count"], 3)
        self.assertGreater(receipt["total_generated_bytes"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
