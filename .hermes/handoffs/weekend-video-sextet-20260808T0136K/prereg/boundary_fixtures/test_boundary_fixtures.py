#!/usr/bin/env python3
"""Contract tests for Tori §6 synthetic brick-boundary fixtures."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
from astropy.io import fits
from astropy.wcs import WCS

from make_boundary_fixtures import (
    BRICK_SIZE,
    CD_DEG_PER_PIXEL,
    CUTOUT_SIZE,
    FixtureSourceError,
    MissingNeighbourError,
    PIXEL_SCALE_ARCSEC,
    STRIDE,
    brick_header,
    expected_cutout,
    fixture_cases,
    generate_fixture_tree,
    planned_bricks,
    render_fixture_oracle,
)


class BoundaryFixtureTests(unittest.TestCase):
    @staticmethod
    def _broken_primary_only(root: Path, row: dict[str, object]) -> np.ndarray:
        broken = np.zeros((CUTOUT_SIZE, CUTOUT_SIZE), dtype=np.float32)
        with fits.open(root / "bricks/synthetic-r+0c+0-image-r.fits.fz", memmap=False) as hdus:
            primary = np.asarray(hdus[1].data)
        center_x = int(row["center_x"])
        center_y = int(row["center_y"])
        source_x0 = center_x + (BRICK_SIZE - CUTOUT_SIZE) // 2
        source_y0 = center_y + (BRICK_SIZE - CUTOUT_SIZE) // 2
        valid_x0 = max(source_x0, 0)
        valid_x1 = min(source_x0 + CUTOUT_SIZE, BRICK_SIZE)
        valid_y0 = max(source_y0, 0)
        valid_y1 = min(source_y0 + CUTOUT_SIZE, BRICK_SIZE)
        broken[
            valid_y0 - source_y0 : valid_y1 - source_y0,
            valid_x0 - source_x0 : valid_x1 - source_x0,
        ] = primary[valid_y0:valid_y1, valid_x0:valid_x1]
        return broken

    def test_generator_emits_exact_spec_bricks_and_value_oracle(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_boundary_fixtures_") as temporary:
            root = Path(temporary)
            manifest = generate_fixture_tree(root)

            self.assertEqual(BRICK_SIZE, 3600)
            self.assertEqual(CUTOUT_SIZE, 128)
            self.assertEqual(PIXEL_SCALE_ARCSEC, 0.262)
            self.assertEqual(STRIDE, 3472)
            self.assertEqual(len(manifest["bricks"]), 9)
            for brick_record in manifest["bricks"]:
                polygon = brick_record["pixel_edge_polygon_global"]
                self.assertEqual(len(polygon), 9)
                self.assertEqual(polygon[0], polygon[-1])

            brick = manifest["bricks"][0]
            brick_path = root / brick["relative_path"]
            with fits.open(brick_path, memmap=False) as hdus:
                data = np.asarray(hdus[1].data)
                header = hdus[1].header
                compression_type = hdus[1].compression_type
            self.assertEqual(data.shape, (BRICK_SIZE, BRICK_SIZE))
            self.assertEqual(data.dtype, np.dtype("float32"))
            self.assertTrue(np.all(data > 0.0))
            self.assertEqual(compression_type, "GZIP_2")
            self.assertEqual(header["CTYPE1"], "RA---TAN")
            self.assertEqual(header["CTYPE2"], "DEC--TAN")
            self.assertAlmostEqual(header["CD1_1"], -CD_DEG_PER_PIXEL, places=16)
            self.assertAlmostEqual(header["CD2_2"], CD_DEG_PER_PIXEL, places=16)

            expected = expected_cutout(0, 0)
            self.assertEqual(expected.shape, (CUTOUT_SIZE, CUTOUT_SIZE))
            self.assertEqual(expected.dtype, np.dtype("float32"))
            self.assertTrue(np.all(expected > 0.0))
            self.assertFalse(np.array_equal(expected[0], expected[1]))
            self.assertFalse(np.array_equal(expected[:, 0], expected[:, 1]))

            object_rows = json.loads((root / "objects.json").read_text(encoding="utf-8"))
            self.assertGreater(len(object_rows), 0)

    def test_expected_values_follow_the_exact_object_centred_output_tan_wcs(self) -> None:
        row = next(row for row in fixture_cases() if row["object_id"] == "corner_north_west_exact")
        output_wcs = WCS(row["output_wcs"])
        yy, xx = np.indices((CUTOUT_SIZE, CUTOUT_SIZE), dtype=np.float64)
        world = output_wcs.all_pix2world(
            np.column_stack(((xx + 1).ravel(), (yy + 1).ravel())),
            1,
        )
        common_wcs = WCS(brick_header(0, 0, 0, 0))
        common_pixels = common_wcs.all_world2pix(world, 1)
        global_x = common_pixels[:, 0] - 1800.5
        global_y = common_pixels[:, 1] - 1800.5
        independently_expected = (
            20.0 + global_y * 0.002 + global_x * 0.0001
        ).astype(np.float32).reshape(CUTOUT_SIZE, CUTOUT_SIZE)
        np.testing.assert_array_equal(
            expected_cutout(row["center_x"], row["center_y"]),
            independently_expected,
        )
        edge_pixels = np.array(
            [
                [0.5, 0.5],
                [64.5, 0.5],
                [128.5, 0.5],
                [128.5, 64.5],
                [128.5, 128.5],
                [64.5, 128.5],
                [0.5, 128.5],
                [0.5, 64.5],
                [0.5, 0.5],
            ],
            dtype=np.float64,
        )
        edge_world = output_wcs.all_pix2world(edge_pixels, 1)
        edge_common = np.asarray(common_wcs.all_world2pix(edge_world, 1)) - np.array(
            [1800.5, 1800.5]
        )
        np.testing.assert_allclose(
            np.asarray(row["output_pixel_edge_polygon_global"]),
            edge_common,
            rtol=0.0,
            atol=1e-10,
        )

    def test_object_table_covers_every_edge_corner_exact_boundary_and_overlap(self) -> None:
        cases = {row["object_id"]: row for row in fixture_cases()}
        self.assertEqual(len(cases), 29)
        self.assertEqual(cases["centre"]["expected_bricks"], ["r+0c+0"])

        for direction in ("north", "south", "east", "west"):
            self.assertEqual(len(cases[f"edge_{direction}_no_neighbour"]["expected_bricks"]), 1)
            self.assertEqual(len(cases[f"edge_{direction}_overlap_only"]["expected_bricks"]), 2)
            self.assertEqual(len(cases[f"edge_{direction}_within_63px"]["expected_bricks"]), 2)
            self.assertEqual(len(cases[f"edge_{direction}_exact"]["expected_bricks"]), 2)
            self.assertEqual(len(cases[f"edge_{direction}_beyond"]["expected_bricks"]), 2)

        expected_corners = {
            "corner_north_east_exact": {"r+0c+0", "r+0c-1", "r+1c+0", "r+1c-1"},
            "corner_north_west_exact": {"r+0c+0", "r+0c+1", "r+1c+0", "r+1c+1"},
            "corner_south_east_exact": {"r+0c+0", "r+0c-1", "r-1c+0", "r-1c-1"},
            "corner_south_west_exact": {"r+0c+0", "r+0c+1", "r-1c+0", "r-1c+1"},
        }
        for object_id, expected in expected_corners.items():
            self.assertEqual(set(cases[object_id]["expected_bricks"]), expected)
            beyond_id = object_id.replace("_exact", "_beyond")
            self.assertEqual(set(cases[beyond_id]["expected_bricks"]), expected)

        self.assertEqual(planned_bricks(0, 0), ["r+0c+0"])

        with tempfile.TemporaryDirectory(prefix="_tmp_boundary_fixtures_") as temporary:
            root = Path(temporary)
            generate_fixture_tree(root)
            rows = json.loads((root / "objects.json").read_text(encoding="utf-8"))
            self.assertEqual({row["object_id"] for row in rows}, set(cases))
            for row in rows:
                self.assertEqual(len(row["output_pixel_edge_polygon_global"]), 9)
                self.assertEqual(
                    row["output_pixel_edge_polygon_global"][0],
                    row["output_pixel_edge_polygon_global"][-1],
                )
                self.assertEqual(len(row["source_set_signature_sha256"]), 64)
                expected = np.load(root / row["expected_array_path"], allow_pickle=False)
                np.testing.assert_array_equal(
                    expected,
                    expected_cutout(row["center_x"], row["center_y"]),
                )
                self.assertTrue(np.all(expected > 0.0))
                self.assertEqual(len(row["value_probes"]), 5)
                expected_bits = expected.view(np.uint32)
                for probe in row["value_probes"]:
                    self.assertEqual(
                        int(expected_bits[probe["y"], probe["x"]]),
                        probe["float32_bits"],
                    )

    def test_value_oracle_detects_shape_correct_edge_truncation_and_is_order_invariant(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_boundary_fixtures_") as temporary:
            root = Path(temporary)
            generate_fixture_tree(root)
            rows = {
                row["object_id"]: row
                for row in json.loads((root / "objects.json").read_text(encoding="utf-8"))
            }
            row = rows["edge_west_beyond"]
            forward, forward_receipt = render_fixture_oracle(root, row)
            reverse, reverse_receipt = render_fixture_oracle(
                root,
                row,
                source_order=list(reversed(row["expected_bricks"])),
            )
            expected = np.load(root / row["expected_array_path"], allow_pickle=False)
            np.testing.assert_array_equal(forward, expected)
            np.testing.assert_array_equal(reverse, expected)
            self.assertEqual(forward_receipt["output_array_sha256"], reverse_receipt["output_array_sha256"])
            self.assertGreaterEqual(forward_receipt["coverage_min"], 1)
            self.assertEqual(forward_receipt["zero_coverage_pixels"], 0)

            # Deliberately emulate the dangerous failure: one primary-brick crop,
            # with unavailable pixels silently padded to the requested shape.
            broken = self._broken_primary_only(root, row)
            self.assertEqual(broken.shape, expected.shape)
            self.assertGreater(np.count_nonzero(broken == 0.0), 0)
            with self.assertRaises(AssertionError):
                np.testing.assert_array_equal(broken, expected)

    def test_every_fixture_renders_every_expected_value_and_stress_crops_are_detected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_boundary_fixtures_") as temporary:
            root = Path(temporary)
            generate_fixture_tree(root)
            rows = json.loads((root / "objects.json").read_text(encoding="utf-8"))
            for row in rows:
                actual, receipt = render_fixture_oracle(
                    root,
                    row,
                    source_order=list(reversed(row["expected_bricks"])),
                )
                expected = np.load(root / row["expected_array_path"], allow_pickle=False)
                np.testing.assert_array_equal(actual, expected)
                self.assertEqual(receipt["planned_bricks"], sorted(row["expected_bricks"]))
                self.assertEqual(receipt["opened_bricks"], sorted(row["expected_bricks"]))
                self.assertEqual(receipt["contributing_bricks"], sorted(row["expected_bricks"]))
                self.assertEqual(receipt["zero_coverage_pixels"], 0)
                self.assertGreaterEqual(receipt["coverage_min"], 1)

            stress_ids = {
                *(f"edge_{direction}_beyond" for direction in ("north", "south", "east", "west")),
                *(f"corner_{corner}_beyond" for corner in ("north_east", "north_west", "south_east", "south_west")),
            }
            by_id = {row["object_id"]: row for row in rows}
            for object_id in stress_ids:
                expected = np.load(root / by_id[object_id]["expected_array_path"], allow_pickle=False)
                broken = self._broken_primary_only(root, by_id[object_id])
                self.assertEqual(broken.shape, expected.shape)
                self.assertGreater(np.count_nonzero(broken == 0.0), 0)
                self.assertFalse(np.array_equal(broken, expected))

    def test_missing_required_corner_neighbour_is_terminal_and_writes_no_cutout(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_boundary_fixtures_") as temporary:
            root = Path(temporary)
            manifest = generate_fixture_tree(root)
            rows = {
                row["object_id"]: row
                for row in json.loads((root / "objects.json").read_text(encoding="utf-8"))
            }
            row = rows["corner_north_east_exact"]
            brick_records = {record["brick_id"]: record for record in manifest["bricks"]}
            missing_id = "r+1c-1"
            (root / brick_records[missing_id]["relative_path"]).unlink()
            output_path = root / "must_not_exist.npy"

            with self.assertRaisesRegex(MissingNeighbourError, r"r\+1c-1"):
                render_fixture_oracle(root, row, output_path=output_path)
            self.assertFalse(output_path.exists())
            self.assertFalse((root / "must_not_exist.npy.tmp").exists())

    def test_digest_mismatched_required_neighbour_is_terminal(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_boundary_fixtures_") as temporary:
            root = Path(temporary)
            manifest = generate_fixture_tree(root)
            rows = {
                row["object_id"]: row
                for row in json.loads((root / "objects.json").read_text(encoding="utf-8"))
            }
            brick_records = {record["brick_id"]: record for record in manifest["bricks"]}
            damaged_id = "r+0c+1"
            damaged_path = root / brick_records[damaged_id]["relative_path"]
            with damaged_path.open("r+b") as handle:
                handle.seek(-1, 2)
                original = handle.read(1)
                handle.seek(-1, 2)
                handle.write(bytes([original[0] ^ 1]))

            output_path = root / "must_not_exist.npy"
            with self.assertRaisesRegex(FixtureSourceError, r"r\+0c\+1.*digest mismatch"):
                render_fixture_oracle(root, rows["edge_west_exact"], output_path=output_path)
            self.assertFalse(output_path.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
