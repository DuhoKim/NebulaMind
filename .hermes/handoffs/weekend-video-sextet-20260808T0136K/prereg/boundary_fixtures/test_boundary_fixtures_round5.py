#!/usr/bin/env python3
"""Round-5 contract tests for a legitimate three-source T-junction."""

from __future__ import annotations

import hashlib
import json
import math
import tempfile
import unittest
from pathlib import Path

import numpy as np
from astropy.io import fits

from make_boundary_fixtures import FixtureSourceError, MissingNeighbourError
from make_boundary_fixtures_round5 import (
    GUARD_BRICK_IDS,
    LADDER_REQUESTS_PIXELS,
    MATCHED_REAL_ROWS,
    MEETING_BRICK_IDS,
    PINNED_GENERATOR_SHA256,
    REAL_GEOMETRY_SHA256,
    ROUND5_BRIEF_SHA256,
    generate_round5_fixture_tree,
    render_round5_oracle,
    verify_round5_fixture_tree,
)


FIXTURE_ROOT = Path(__file__).resolve().parent
PREREG_ROOT = FIXTURE_ROOT.parent
REAL_GEOMETRY_PATH = (
    PREREG_ROOT
    / "_tori_parent_row_count_evidence"
    / "footprint_variance_brick_counts_20260814"
    / "static"
    / "survey-bricks-dr10-south.fits.gz"
)


class BoundaryFixtureRound5Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._temporary = tempfile.TemporaryDirectory(
            prefix="_tmp_boundary_fixtures_round5_"
        )
        cls.root = Path(cls._temporary.name)
        cls.manifest = generate_round5_fixture_tree(cls.root)
        cls.sidecar = json.loads(
            (cls.root / "geometry_sidecar.json").read_text(encoding="utf-8")
        )
        cls.rows = json.loads(
            (cls.root / "objects.json").read_text(encoding="utf-8")
        )
        cls.by_id = {row["object_id"]: row for row in cls.rows}
        cls.bricks = {
            row["brick_id"]: row for row in cls.sidecar["bricks"]
        }

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temporary.cleanup()

    def test_real_dr10_geometry_proves_systematic_t_junctions_and_matched_triple(
        self,
    ) -> None:
        self.assertTrue(REAL_GEOMETRY_PATH.is_file())
        self.assertEqual(
            hashlib.sha256(REAL_GEOMETRY_PATH.read_bytes()).hexdigest(),
            REAL_GEOMETRY_SHA256,
        )
        with fits.open(REAL_GEOMETRY_PATH, memmap=False) as hdus:
            data = hdus[1].data
            columns = set(hdus[1].columns.names)
            self.assertTrue(
                {
                    "brickname",
                    "brickid",
                    "ra",
                    "dec",
                    "ra1",
                    "ra2",
                    "dec1",
                    "dec2",
                    "area",
                    "survey_primary",
                }.issubset(columns)
            )
            names = np.char.strip(np.asarray(data["brickname"]).astype(str))
            dec = np.asarray(data["dec"], dtype=np.float64)
            ra1 = np.asarray(data["ra1"], dtype=np.float64)
            ra2 = np.asarray(data["ra2"], dtype=np.float64)

            row_ra_counts: list[tuple[float, int]] = []
            for dec_value in np.unique(dec):
                row_index = np.flatnonzero(dec == dec_value)
                width = float(np.median(ra2[row_index] - ra1[row_index]))
                row_ra_counts.append((float(dec_value), int(round(360.0 / width))))
            adjacent_changes = sum(
                1
                for (dec_a, count_a), (dec_b, count_b) in zip(
                    row_ra_counts, row_ra_counts[1:]
                )
                if abs(dec_b - dec_a - 0.25) < 1e-12 and count_a != count_b
            )
            self.assertEqual(len(row_ra_counts), 503)
            self.assertEqual(adjacent_changes, 426)

            observed: dict[str, dict[str, float | int | bool | str]] = {}
            for source in MATCHED_REAL_ROWS:
                index = np.flatnonzero(names == source["brickname"])
                self.assertEqual(len(index), 1)
                i = int(index[0])
                observed[source["role"]] = {
                    "brickname": str(names[i]),
                    "brickid": int(data["brickid"][i]),
                    "ra": float(data["ra"][i]),
                    "dec": float(data["dec"][i]),
                    "ra1": float(data["ra1"][i]),
                    "ra2": float(data["ra2"][i]),
                    "dec1": float(data["dec1"][i]),
                    "dec2": float(data["dec2"][i]),
                    "area": float(data["area"][i]),
                    "survey_primary": bool(data["survey_primary"][i]),
                }
                for key, expected in source.items():
                    if key == "role":
                        continue
                    self.assertEqual(observed[source["role"]][key], expected)

        lower_west = observed["lower-west"]
        lower_east = observed["lower-east"]
        upper_span = observed["upper-span"]
        self.assertEqual(lower_west["ra2"], lower_east["ra1"])
        self.assertEqual(lower_west["dec2"], upper_span["dec1"])
        self.assertLess(upper_span["ra1"], lower_west["ra2"])
        self.assertLess(lower_west["ra2"], upper_span["ra2"])
        self.assertEqual(round(360.0 / (lower_west["ra2"] - lower_west["ra1"])), 1018)
        self.assertEqual(round(360.0 / (upper_span["ra2"] - upper_span["ra1"])), 1022)
        for row in (lower_west, lower_east, upper_span):
            projected_width = (row["ra2"] - row["ra1"]) * math.cos(
                math.radians(row["dec"])
            )
            self.assertGreater(projected_width, 0.245)
            self.assertLess(projected_width, 0.255)
            self.assertTrue(row["survey_primary"])

    def test_prior_generators_and_brief_remain_exactly_pinned(self) -> None:
        for filename, expected in PINNED_GENERATOR_SHA256.items():
            observed = hashlib.sha256((FIXTURE_ROOT / filename).read_bytes()).hexdigest()
            self.assertEqual(observed, expected)
            self.assertEqual(
                self.manifest["parent_generator_sha256"][filename], expected
            )
        observed_brief = hashlib.sha256(
            (PREREG_ROOT / "_tmp_yui_tjunction_fixtures_brief_20260816.md").read_bytes()
        ).hexdigest()
        self.assertEqual(observed_brief, ROUND5_BRIEF_SHA256)
        self.assertEqual(self.manifest["brief_sha256"], ROUND5_BRIEF_SHA256)

    def test_schema_has_nine_additive_cases_three_meeting_sources_and_two_guards(
        self,
    ) -> None:
        self.assertEqual(
            self.manifest["schema_version"], "yui-boundary-fixtures-round5-v1"
        )
        self.assertEqual(
            self.manifest["object_schema_compatible_with"],
            "yui-boundary-fixtures-round2-v1",
        )
        self.assertTrue(self.manifest["synthetic_only"])
        self.assertEqual(len(self.bricks), 5)
        self.assertEqual(len(self.rows), 9)
        self.assertEqual(set(self.by_id), set(LADDER_REQUESTS_PIXELS))
        self.assertEqual(set(MEETING_BRICK_IDS), {
            "tj-lower-east",
            "tj-lower-west",
            "tj-upper-span",
        })
        self.assertEqual(set(GUARD_BRICK_IDS), {
            "tj-upper-east-guard",
            "tj-upper-west-guard",
        })
        for brick in self.bricks.values():
            self.assertEqual(brick["canonicalized_gzip_tile_mtime_count"], 3600)
        for row in self.rows:
            self.assertEqual(set(row["candidate_bricks"]), set(self.bricks))
            self.assertEqual(set(row["expected_bricks"]), set(MEETING_BRICK_IDS))
            self.assertEqual(
                set(row["expected_contributing_bricks"]), set(MEETING_BRICK_IDS)
            )
            self.assertEqual(row["expected_zero_pixel_touch_bricks"], [])
            self.assertTrue(set(GUARD_BRICK_IDS).isdisjoint(row["expected_bricks"]))
        self.assertEqual(
            self.manifest["geometry_sidecar_sha256"],
            hashlib.sha256(
                (self.root / "geometry_sidecar.json").read_bytes()
            ).hexdigest(),
        )
        self.assertEqual(
            self.manifest["objects_sha256"],
            hashlib.sha256((self.root / "objects.json").read_bytes()).hexdigest(),
        )
        verification = self.manifest["real_geometry_verification"]
        self.assertTrue(verification["claim_verified"])
        self.assertEqual(
            verification["local_geometry_source"]["sha256"],
            REAL_GEOMETRY_SHA256,
        )
        self.assertEqual(
            verification["matched_junction"]["lower_row_ra_count"], 1018
        )
        self.assertEqual(
            verification["matched_junction"]["upper_row_ra_count"], 1022
        )
        self.assertEqual(
            verification["systematic_row_evidence"]["adjacent_row_count_changes"],
            426,
        )

    def test_requested_pixel_ladders_are_achieved_at_the_unique_area_junction(
        self,
    ) -> None:
        for object_id, requested in LADDER_REQUESTS_PIXELS.items():
            row = self.by_id[object_id]
            evidence = row["geometry_evidence"]
            achieved = evidence["achieved_signed_object_offset_pixels"]
            self.assertEqual(
                evidence["requested_signed_object_offset_pixels"], list(requested)
            )
            np.testing.assert_allclose(achieved, requested, rtol=0.0, atol=1e-8)
            self.assertLessEqual(evidence["solve_max_abs_error_pixels"], 1e-8)
            if object_id.startswith("vertical_"):
                self.assertLessEqual(abs(achieved[1]), 1e-8)
            if object_id.startswith("horizontal_"):
                self.assertLessEqual(abs(achieved[0]), 1e-8)
        exact = self.by_id["tjunction_exact"]["geometry_evidence"]
        np.testing.assert_allclose(
            exact["junction_output_pixel"], [64.5, 64.5], rtol=0.0, atol=1e-8
        )
        for object_id in (
            "vertical_subpixel_inside",
            "vertical_subpixel_outside",
            "horizontal_subpixel_inside",
            "horizontal_subpixel_outside",
        ):
            achieved = self.by_id[object_id]["geometry_evidence"][
                "achieved_signed_object_offset_pixels"
            ]
            nonzero = [abs(value) for value in achieved if abs(value) > 1e-8]
            self.assertEqual(len(nonzero), 1)
            self.assertGreater(nonzero[0], 0.0)
            self.assertLess(nonzero[0], 1.0)

    def test_two_consecutive_builds_have_identical_file_hashes(self) -> None:
        def inventory(tree: Path) -> dict[str, str]:
            return {
                path.relative_to(tree).as_posix(): hashlib.sha256(
                    path.read_bytes()
                ).hexdigest()
                for path in sorted(tree.rglob("*"))
                if path.is_file()
            }

        with tempfile.TemporaryDirectory(
            prefix="_tmp_boundary_fixtures_round5_identity_",
            dir=FIXTURE_ROOT,
        ) as directory:
            second_root = Path(directory)
            generate_round5_fixture_tree(second_root)
            self.assertEqual(inventory(second_root), inventory(self.root))

    def test_values_coverage_order_and_tree_replay_are_reproducible(self) -> None:
        for row in self.rows:
            expected = np.load(
                self.root / row["expected_array_path"], allow_pickle=False
            )
            forward, forward_receipt = render_round5_oracle(self.root, row)
            reverse, reverse_receipt = render_round5_oracle(
                self.root,
                row,
                source_order=list(reversed(row["expected_bricks"])),
            )
            np.testing.assert_array_equal(forward, expected)
            np.testing.assert_array_equal(reverse, expected)
            self.assertEqual(
                forward_receipt["output_array_sha256"],
                reverse_receipt["output_array_sha256"],
            )
            self.assertEqual(
                forward_receipt["coverage_array_sha256"],
                row["expected_coverage_sha256"],
            )
            self.assertEqual(forward_receipt["planned_bricks"], sorted(MEETING_BRICK_IDS))
            self.assertEqual(forward_receipt["opened_bricks"], sorted(MEETING_BRICK_IDS))
            self.assertEqual(
                forward_receipt["contributing_bricks"], sorted(MEETING_BRICK_IDS)
            )
            self.assertEqual(forward_receipt["zero_pixel_touch_bricks"], [])
            self.assertEqual(forward_receipt["coverage_min"], 3)
            self.assertEqual(forward_receipt["coverage_max"], 3)
            self.assertEqual(forward_receipt["zero_coverage_pixels"], 0)
            expected_bits = expected.view(np.uint32)
            for probe in row["value_probes"]:
                self.assertEqual(
                    int(expected_bits[probe["y"], probe["x"]]),
                    probe["float32_bits"],
                )
        verification = verify_round5_fixture_tree(self.root)
        self.assertEqual(verification["status"], "PASS")
        self.assertEqual(verification["cases_verified"], 9)
        self.assertEqual(verification["meeting_source_count"], 3)
        self.assertEqual(verification["guard_source_count"], 2)

    def test_missing_or_digest_mismatched_source_halts_before_output(self) -> None:
        row = self.by_id["tjunction_exact"]
        source = self.bricks[sorted(MEETING_BRICK_IDS)[0]]
        source_path = self.root / source["relative_path"]
        output_path = self.root / "must_not_exist.npy"

        held_path = source_path.with_name(source_path.name + ".held")
        source_path.rename(held_path)
        try:
            with self.assertRaises(MissingNeighbourError):
                render_round5_oracle(self.root, row, output_path=output_path)
            self.assertFalse(output_path.exists())
        finally:
            held_path.rename(source_path)

        with source_path.open("r+b") as handle:
            handle.seek(-1, 2)
            original_byte = handle.read(1)
            handle.seek(-1, 2)
            handle.write(bytes([original_byte[0] ^ 1]))
        try:
            with self.assertRaises(FixtureSourceError):
                render_round5_oracle(self.root, row, output_path=output_path)
            self.assertFalse(output_path.exists())
        finally:
            with source_path.open("r+b") as handle:
                handle.seek(-1, 2)
                handle.write(original_byte)


if __name__ == "__main__":
    unittest.main(verbosity=2)
