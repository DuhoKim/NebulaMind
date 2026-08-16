#!/usr/bin/env python3
"""Round-2 written-contract tests for synthetic brick planning geometry."""

from __future__ import annotations

import hashlib
import json
import math
import tempfile
import unittest
import warnings
from pathlib import Path

import numpy as np
from astropy.io import fits
from astropy.utils.exceptions import AstropyWarning
from astropy.wcs import WCS

from make_boundary_fixtures import BRICK_SIZE, CUTOUT_SIZE
from make_boundary_fixtures_round2 import (
    FOOTPRINT_DEC_MAX_DEG,
    FOOTPRINT_DEC_MIN_DEG,
    VALUE_TOLERANCE,
    generate_round2_fixture_tree,
    output_wcs_contract,
    plan_source_ids,
    render_primary_only_shape_correct,
    render_round2_oracle,
)


class BoundaryFixtureRound2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._temporary = tempfile.TemporaryDirectory(prefix="_tmp_boundary_fixtures_round2_")
        cls.root = Path(cls._temporary.name)
        cls.manifest = generate_round2_fixture_tree(cls.root)
        cls.sidecar = json.loads((cls.root / "geometry_sidecar.json").read_text(encoding="utf-8"))
        cls.rows = json.loads((cls.root / "objects.json").read_text(encoding="utf-8"))
        cls.by_id = {row["object_id"]: row for row in cls.rows}
        cls.bricks = {row["brick_id"]: row for row in cls.sidecar["bricks"]}

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temporary.cleanup()

    def test_geometry_sidecar_replaces_scalar_and_uses_distinct_tangent_points(self) -> None:
        self.assertEqual(self.manifest["schema_version"], "yui-boundary-fixtures-round2-v1")
        self.assertTrue(self.manifest["synthetic_only"])
        self.assertEqual(VALUE_TOLERANCE, 1e-5)
        self.assertEqual(
            self.manifest["geometry_sidecar_sha256"],
            hashlib.sha256((self.root / "geometry_sidecar.json").read_bytes()).hexdigest(),
        )
        self.assertEqual(
            self.manifest["objects_sha256"],
            hashlib.sha256((self.root / "objects.json").read_bytes()).hexdigest(),
        )
        self.assertNotIn("source_overlap_pixels", self.manifest)
        self.assertNotIn("stride_pixels", self.manifest)
        self.assertEqual(
            self.sidecar["selected_footprint_declination_domain_deg"],
            [FOOTPRINT_DEC_MIN_DEG, FOOTPRINT_DEC_MAX_DEG],
        )
        self.assertEqual(len(self.bricks), 8)
        self.assertEqual(len(self.rows), 4)

        for group_id in {row["group_id"] for row in self.sidecar["bricks"]}:
            group = [row for row in self.sidecar["bricks"] if row["group_id"] == group_id]
            self.assertEqual(len(group), 2)
            tangent_points = {
                (row["wcs"]["CRVAL1"], row["wcs"]["CRVAL2"])
                for row in group
            }
            self.assertEqual(len(tangent_points), 2)
            for row in group:
                self.assertEqual(len(row["pixel_edge_sky_polygon_deg"]), 9)
                self.assertEqual(
                    row["pixel_edge_sky_polygon_deg"][0],
                    row["pixel_edge_sky_polygon_deg"][-1],
                )
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always", AstropyWarning)
                    with fits.open(self.root / row["relative_path"], memmap=False) as hdus:
                        self.assertEqual(hdus[1].data.shape, (BRICK_SIZE, BRICK_SIZE))
                        self.assertEqual(hdus[1].data.dtype, np.dtype("float32"))
                        self.assertEqual(hdus[1].header["CRVAL1"], row["wcs"]["CRVAL1"])
                        self.assertEqual(hdus[1].header["CRVAL2"], row["wcs"]["CRVAL2"])
                self.assertEqual(caught, [])

    def test_ra_wrap_plans_across_zero_without_plain_number_ordering(self) -> None:
        row = self.by_id["ra_wrap_crossing"]
        group = [self.bricks[source_id] for source_id in row["candidate_bricks"]]
        ras = sorted(source["wcs"]["CRVAL1"] for source in group)
        self.assertLess(ras[0], 1.0)
        self.assertGreater(ras[1], 359.0)
        self.assertGreater(abs(ras[1] - ras[0]), 358.0)

        ra1, dec1 = map(math.radians, (group[0]["wcs"]["CRVAL1"], group[0]["wcs"]["CRVAL2"]))
        ra2, dec2 = map(math.radians, (group[1]["wcs"]["CRVAL1"], group[1]["wcs"]["CRVAL2"]))
        cosine = math.sin(dec1) * math.sin(dec2) + math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2)
        separation_deg = math.degrees(math.acos(max(-1.0, min(1.0, cosine))))
        self.assertLess(separation_deg, 0.3)
        self.assertEqual(row["ra_deg"], 0.0)
        self.assertEqual(len(row["expected_bricks"]), 2)
        self.assertEqual(
            plan_source_ids(group, output_wcs_contract(row["ra_deg"], row["dec_deg"])),
            row["expected_bricks"],
        )

    def test_declination_extremes_change_ra_spacing_and_plan_by_polygon(self) -> None:
        high = self.by_id["selected_dec_max_crossing"]
        low = self.by_id["selected_dec_min_crossing"]
        self.assertEqual(high["dec_deg"], FOOTPRINT_DEC_MAX_DEG - 0.125)
        self.assertEqual(low["dec_deg"], FOOTPRINT_DEC_MIN_DEG + 0.125)

        def wrapped_spacing(case: dict[str, object]) -> float:
            ras = [self.bricks[source_id]["wcs"]["CRVAL1"] for source_id in case["candidate_bricks"]]
            difference = abs(ras[0] - ras[1])
            return min(difference, 360.0 - difference)

        high_spacing = wrapped_spacing(high)
        low_spacing = wrapped_spacing(low)
        self.assertGreater(low_spacing, high_spacing * 100.0)
        for row in (high, low):
            group = [self.bricks[source_id] for source_id in row["candidate_bricks"]]
            self.assertEqual(len(row["expected_bricks"]), 2)
            self.assertEqual(
                plan_source_ids(group, output_wcs_contract(row["ra_deg"], row["dec_deg"])),
                row["expected_bricks"],
            )

    def test_real_geometry_overlap_only_is_polygon_derived_not_scalar(self) -> None:
        row = self.by_id["geometry_overlap_only"]
        evidence = row["geometry_evidence"]
        self.assertFalse(evidence["output_crosses_unique_boundary"])
        self.assertTrue(evidence["output_intersects_neighbour_source_polygon"])
        self.assertGreater(evidence["derived_inward_offset_pixels"], CUTOUT_SIZE / 2)
        self.assertEqual(len(row["expected_bricks"]), 2)
        self.assertNotIn("overlap_pixels", evidence)

    def test_every_round2_case_compares_every_value_and_rejects_shape_correct_omission(self) -> None:
        for row in self.rows:
            expected = np.load(self.root / row["expected_array_path"], allow_pickle=False)
            forward, forward_receipt = render_round2_oracle(self.root, row)
            reverse, reverse_receipt = render_round2_oracle(
                self.root,
                row,
                source_order=list(reversed(row["expected_bricks"])),
            )
            np.testing.assert_array_equal(forward, expected)
            np.testing.assert_array_equal(reverse, expected)
            self.assertEqual(forward_receipt["output_array_sha256"], reverse_receipt["output_array_sha256"])
            self.assertEqual(forward_receipt["zero_coverage_pixels"], 0)
            self.assertGreaterEqual(forward_receipt["coverage_min"], 1)
            self.assertLessEqual(
                forward_receipt["bilinear_sample_max_abs_error"],
                forward_receipt["adapter_comparison_absolute_tolerance"],
            )

            broken = render_primary_only_shape_correct(self.root, row)
            self.assertEqual(broken.shape, expected.shape)
            self.assertEqual(broken.dtype, np.dtype("float32"))
            self.assertFalse(np.array_equal(broken, expected))
            self.assertGreater(np.count_nonzero(broken != expected), 0)

            expected_bits = expected.view(np.uint32)
            for probe in row["value_probes"]:
                self.assertEqual(
                    int(expected_bits[probe["y"], probe["x"]]),
                    probe["float32_bits"],
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
