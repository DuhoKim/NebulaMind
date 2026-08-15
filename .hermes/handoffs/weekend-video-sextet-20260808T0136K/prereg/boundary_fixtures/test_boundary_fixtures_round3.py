#!/usr/bin/env python3
"""Round-3 sub-pixel knife-edge tests at both declination extremes."""

from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import numpy as np

from make_boundary_fixtures_round3 import (
    PINNED_ROUND1_SHA256,
    PINNED_ROUND2_SHA256,
    generate_round3_fixture_tree,
    render_round3_oracle,
)


class BoundaryFixtureRound3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._temporary = tempfile.TemporaryDirectory(prefix="_tmp_boundary_fixtures_round3_")
        cls.root = Path(cls._temporary.name)
        cls.manifest = generate_round3_fixture_tree(cls.root)
        cls.sidecar = json.loads((cls.root / "geometry_sidecar.json").read_text(encoding="utf-8"))
        cls.rows = json.loads((cls.root / "objects.json").read_text(encoding="utf-8"))
        cls.by_id = {row["object_id"]: row for row in cls.rows}
        cls.bricks = {row["brick_id"]: row for row in cls.sidecar["bricks"]}

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temporary.cleanup()

    def test_round1_and_round2_generators_remain_exactly_pinned(self) -> None:
        fixture_root = Path(__file__).resolve().parent
        observed_round1 = hashlib.sha256((fixture_root / "make_boundary_fixtures.py").read_bytes()).hexdigest()
        observed_round2 = hashlib.sha256((fixture_root / "make_boundary_fixtures_round2.py").read_bytes()).hexdigest()
        self.assertEqual(observed_round1, PINNED_ROUND1_SHA256)
        self.assertEqual(observed_round2, PINNED_ROUND2_SHA256)
        self.assertEqual(self.manifest["parent_generator_sha256"]["round1"], PINNED_ROUND1_SHA256)
        self.assertEqual(self.manifest["parent_generator_sha256"]["round2"], PINNED_ROUND2_SHA256)

    def test_schema_and_complete_ten_case_ladder(self) -> None:
        self.assertEqual(self.manifest["schema_version"], "yui-boundary-fixtures-round3-v1")
        self.assertEqual(self.manifest["object_schema_compatible_with"], "yui-boundary-fixtures-round2-v1")
        self.assertTrue(self.manifest["synthetic_only"])
        self.assertEqual(len(self.bricks), 4)
        self.assertEqual(len(self.rows), 10)
        self.assertEqual(
            self.manifest["geometry_sidecar_sha256"],
            hashlib.sha256((self.root / "geometry_sidecar.json").read_bytes()).hexdigest(),
        )
        self.assertEqual(
            self.manifest["objects_sha256"],
            hashlib.sha256((self.root / "objects.json").read_bytes()).hexdigest(),
        )
        expected_ids = {
            f"{prefix}_{suffix}"
            for prefix in ("dec_max", "dec_min")
            for suffix in (
                "inside",
                "exact_boundary",
                "one_pixel_beyond",
                "subpixel_just_inside",
                "subpixel_just_outside",
            )
        }
        self.assertEqual(set(self.by_id), expected_ids)

    def test_offsets_are_solved_in_source_pixel_space_and_record_achieved_values(self) -> None:
        expected_dec = {"dec_max": 32.25, "dec_min": -89.875}
        expected_axis = {"dec_max": "x", "dec_min": "y"}
        expected_offsets = {
            "inside": -10.0,
            "exact_boundary": 0.0,
            "one_pixel_beyond": 1.0,
            "subpixel_just_inside": -0.25,
            "subpixel_just_outside": 0.25,
        }
        for prefix in ("dec_max", "dec_min"):
            for suffix, requested in expected_offsets.items():
                row = self.by_id[f"{prefix}_{suffix}"]
                evidence = row["geometry_evidence"]
                achieved = evidence["achieved_edge_offset_pixels"]
                self.assertEqual(row["dec_deg"], expected_dec[prefix])
                self.assertEqual(evidence["boundary_axis"], expected_axis[prefix])
                self.assertEqual(evidence["requested_edge_offset_pixels"], requested)
                self.assertLessEqual(abs(achieved - requested), 1e-8)
                self.assertEqual(
                    evidence["achieved_subpixel_fraction"],
                    abs(achieved - round(achieved)),
                )
                self.assertEqual(
                    achieved,
                    max(evidence["sampled_edge_inward_offsets_pixels"]),
                )
                self.assertEqual(
                    self.manifest["achieved_edge_offsets_pixels"][row["object_id"]],
                    achieved,
                )
                self.assertEqual(
                    self.manifest["achieved_subpixel_fractions"][row["object_id"]],
                    evidence["achieved_subpixel_fraction"],
                )

            just_inside = self.by_id[f"{prefix}_subpixel_just_inside"]["geometry_evidence"]
            just_outside = self.by_id[f"{prefix}_subpixel_just_outside"]["geometry_evidence"]
            self.assertGreater(abs(just_inside["achieved_edge_offset_pixels"]), 0.0)
            self.assertLess(abs(just_inside["achieved_edge_offset_pixels"]), 1.0)
            self.assertGreater(abs(just_outside["achieved_edge_offset_pixels"]), 0.0)
            self.assertLess(abs(just_outside["achieved_edge_offset_pixels"]), 1.0)

    def test_source_set_flips_only_after_positive_area_crossing(self) -> None:
        for prefix in ("dec_max", "dec_min"):
            rows = {
                suffix: self.by_id[f"{prefix}_{suffix}"]
                for suffix in (
                    "inside",
                    "exact_boundary",
                    "one_pixel_beyond",
                    "subpixel_just_inside",
                    "subpixel_just_outside",
                )
            }
            target = rows["inside"]["knife_edge_source_brick"]
            primary = rows["inside"]["primary_brick"]
            self.assertEqual(rows["inside"]["expected_bricks"], [primary])
            self.assertEqual(rows["exact_boundary"]["expected_bricks"], [primary])
            self.assertEqual(rows["subpixel_just_inside"]["expected_bricks"], [primary])
            self.assertEqual(set(rows["one_pixel_beyond"]["expected_bricks"]), {primary, target})
            self.assertEqual(set(rows["subpixel_just_outside"]["expected_bricks"]), {primary, target})
            self.assertIn(target, rows["subpixel_just_outside"]["expected_zero_pixel_touch_bricks"])
            # At these curved projection edges, even a +1 polygon-edge offset can
            # intersect positive area without enclosing an output pixel centre.
            self.assertIn(target, rows["one_pixel_beyond"]["expected_zero_pixel_touch_bricks"])

    def test_all_round3_values_coverage_and_order_are_reproducible(self) -> None:
        for row in self.rows:
            expected = np.load(self.root / row["expected_array_path"], allow_pickle=False)
            forward, forward_receipt = render_round3_oracle(self.root, row)
            reverse, reverse_receipt = render_round3_oracle(
                self.root,
                row,
                source_order=list(reversed(row["expected_bricks"])),
            )
            np.testing.assert_array_equal(forward, expected)
            np.testing.assert_array_equal(reverse, expected)
            self.assertEqual(forward_receipt["output_array_sha256"], reverse_receipt["output_array_sha256"])
            self.assertEqual(forward_receipt["coverage_array_sha256"], row["expected_coverage_sha256"])
            self.assertEqual(forward_receipt["planned_bricks"], sorted(row["expected_bricks"]))
            self.assertEqual(forward_receipt["contributing_bricks"], sorted(row["expected_contributing_bricks"]))
            self.assertEqual(forward_receipt["zero_pixel_touch_bricks"], sorted(row["expected_zero_pixel_touch_bricks"]))
            self.assertEqual(forward_receipt["zero_coverage_pixels"], 0)
            self.assertGreaterEqual(forward_receipt["coverage_min"], 1)
            self.assertLessEqual(
                forward_receipt["bilinear_sample_max_abs_error"],
                forward_receipt["adapter_comparison_absolute_tolerance"],
            )
            expected_bits = expected.view(np.uint32)
            for probe in row["value_probes"]:
                self.assertEqual(
                    int(expected_bits[probe["y"], probe["x"]]),
                    probe["float32_bits"],
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
