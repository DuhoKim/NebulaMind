#!/usr/bin/env python3
"""Offline tests for nm_brick_read_stage.py; synthetic fixtures only."""
from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

import numpy as np
from astropy.io import fits

import nm_brick_read_stage as stage

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
ROUND4 = PREREG / "boundary_fixtures" / "generated_round4"
tori = stage.tori


def west_geometry_row():
    manifest = json.loads((ROUND4 / "fixture_manifest.json").read_text())
    record = next(b for b in manifest["bricks"] if b["brick_id"] == "knife-dec-max-west")
    return record, {
        "brickname": record["brick_id"],
        "brickid": 1,
        "ra": record["wcs"]["CRVAL1"],
        "dec": record["wcs"]["CRVAL2"],
        "ra1": record["unique_ra_bounds_deg"][0] % 360.0,
        "ra2": record["unique_ra_bounds_deg"][1] % 360.0,
        "dec1": record["unique_dec_bounds_deg"][0],
        "dec2": record["unique_dec_bounds_deg"][1],
    }


def write_compressed(path, data, header_cards, *, compression_type="RICE_1", primary_data=None):
    header = fits.Header()
    for key, value in header_cards.items():
        header[key] = value
    image = fits.CompImageHDU(
        data=data, header=header, compression_type=compression_type,
        quantize_level=-1e-7, name="IMAGE",
    )
    fits.HDUList([fits.PrimaryHDU(data=primary_data), image]).writeto(path, overwrite=True)


class ReadStageTests(unittest.TestCase):
    tmp: Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = Path(tempfile.mkdtemp(prefix="_tmp_readstage_", dir=HERE))
        cls.record, cls.row = west_geometry_row()
        cls.source = ROUND4 / cls.record["relative_path"]

    @classmethod
    def tearDownClass(cls) -> None:
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def small_cards(self):
        return {
            "CTYPE1": "RA---TAN", "CTYPE2": "DEC--TAN",
            "CRVAL1": self.row["ra"], "CRVAL2": self.row["dec"],
            "CRPIX1": 1800.5, "CRPIX2": 1800.5,
            "CD1_1": tori.OUT_CD[0][0], "CD1_2": 0.0,
            "CD2_1": 0.0, "CD2_2": tori.OUT_CD[1][1],
            "SYNTHET": True,
        }

    def expect_code(self, code, path, row=None, **kwargs):
        with self.assertRaises(stage.ReadStageError) as ctx:
            stage.read_production_brick(path, row or self.row, self.tmp / "staged_fail", **kwargs)
        self.assertEqual(ctx.exception.code, code)

    def test_positive_read_chains_and_matches_direct_staging(self) -> None:
        root_a = self.tmp / "staged_a"
        receipt = stage.read_production_brick(
            self.source, self.row, root_a, expected_file_sha256=self.record["file_sha256"]
        )
        self.assertEqual(receipt["decompressed_array_sha256"], self.record["data_sha256"])
        self.assertEqual(receipt["raw_compression_cards"]["ZCMPTYPE"], "RICE_1")
        self.assertEqual(receipt["raw_compression_cards"]["ZBITPIX"], -32)
        self.assertEqual(receipt["content_hash_excludes"], ["content_sha256", "recorded_utc"])
        staged = root_a / receipt["adapter_input_relpath"]
        self.assertTrue(staged.is_file())
        self.assertEqual(
            hashlib.sha256(staged.read_bytes()).hexdigest(), receipt["adapter_input_file_sha256"]
        )
        # Byte-identical to direct uncompressed staging of the same array.
        with fits.open(self.source, memmap=False) as hdus:
            data = np.ascontiguousarray(hdus[1].data, dtype=np.float32)
        root_b = self.tmp / "staged_b"
        direct = tori.write_synthetic_brick(
            root_b, self.row, data_big_endian=np.ascontiguousarray(data.astype(">f4")).tobytes()
        )
        self.assertEqual(
            hashlib.sha256(direct.read_bytes()).hexdigest(),
            receipt["adapter_input_file_sha256"],
        )
        # Receipt file exists and the content hash reproduces on a second run.
        receipt_path = root_a / "read_receipts" / f"{self.row['brickname']}.json"
        self.assertTrue(receipt_path.is_file())
        second = stage.read_production_brick(
            self.source, self.row, self.tmp / "staged_c",
            expected_file_sha256=self.record["file_sha256"],
        )
        self.assertEqual(second["content_sha256"], receipt["content_sha256"])
        recomputed = hashlib.sha256(
            json.dumps(
                {k: v for k, v in receipt.items() if k not in ("content_sha256", "recorded_utc")},
                sort_keys=True, separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        self.assertEqual(recomputed, receipt["content_sha256"])
        lock = receipt["decoder_environment_lock"]
        self.assertIn("astropy_version", lock)
        self.assertTrue(
            any(name.startswith("_compression.") for name in lock["astropy_tiled_compression_module_sha256"])
        )

    def test_missing_and_digest_mismatch(self) -> None:
        self.expect_code("FAILED_SOURCE_MISSING", self.tmp / "nonexistent.fits.fz")
        self.expect_code("FAILED_SOURCE_DIGEST", self.source, expected_file_sha256="0" * 64)

    def test_wrong_compression_type_rejected(self) -> None:
        path = self.tmp / "gzip.fits.fz"
        write_compressed(path, np.zeros((128, 128), dtype=np.float32), self.small_cards(),
                         compression_type="GZIP_2")
        self.expect_code("FAILED_COMPRESSION_CONTRACT", path)

    def test_wrong_zbitpix_rejected(self) -> None:
        path = self.tmp / "int16.fits.fz"
        write_compressed(path, np.zeros((128, 128), dtype=np.int16), self.small_cards())
        self.expect_code("FAILED_COMPRESSION_CONTRACT", path)

    def test_wrong_dimensions_rejected(self) -> None:
        path = self.tmp / "small.fits.fz"
        write_compressed(path, np.zeros((128, 128), dtype=np.float32), self.small_cards())
        self.expect_code("FAILED_COMPRESSION_CONTRACT", path)

    def test_nonempty_primary_rejected(self) -> None:
        path = self.tmp / "primary.fits.fz"
        write_compressed(
            path, np.zeros((128, 128), dtype=np.float32), self.small_cards(),
            primary_data=np.zeros((4,), dtype=np.float32),
        )
        self.expect_code("FAILED_PRIMARY_NOT_EMPTY", path)

    def test_wcs_mismatch_against_sidecar_rejected(self) -> None:
        wrong_row = dict(self.row, ra=self.row["ra"] + 0.25)
        self.expect_code("FAILED_WCS_MISMATCH", self.source, row=wrong_row)

    def test_missing_synthetic_marker_rejected(self) -> None:
        cards = self.small_cards()
        cards.pop("SYNTHET")
        path = self.tmp / "nosynth.fits.fz"
        write_compressed(path, np.zeros((tori.SRC_N, tori.SRC_N), dtype=np.float32), cards)
        self.expect_code("FAILED_BUILD_ONLY_SCOPE", path)

    def test_nothing_staged_on_failure(self) -> None:
        fail_root = self.tmp / "staged_fail"
        if fail_root.exists():
            staged_files = [p for p in fail_root.rglob("*") if p.is_file()]
            self.assertEqual(staged_files, [])


if __name__ == "__main__":
    unittest.main()
