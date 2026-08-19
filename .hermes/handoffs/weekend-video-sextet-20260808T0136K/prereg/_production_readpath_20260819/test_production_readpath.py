#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

import numpy as np
from astropy.io import fits

import production_readpath as rp


EXPECTED_ROOT = Path("/Users/duhokim/NebulaMindData/dr10_south_image_r")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_compressed_fixture(path: Path) -> tuple[np.ndarray, dict[str, float]]:
    data = np.arange(48, dtype=np.float32).reshape(6, 8)
    header = fits.Header()
    header["CTYPE1"] = "RA---TAN"
    header["CTYPE2"] = "DEC--TAN"
    header["CRVAL1"] = 12.5
    header["CRVAL2"] = -30.0
    header["CRPIX1"] = 4.5
    header["CRPIX2"] = 3.5
    header["CD1_1"] = -7.27777777777778e-05
    header["CD1_2"] = 0.0
    header["CD2_1"] = 0.0
    header["CD2_2"] = 7.27777777777778e-05
    fits.HDUList([
        fits.PrimaryHDU(),
        fits.CompImageHDU(data=data, header=header, name="COMPRESSED_IMAGE"),
    ]).writeto(path)
    row = {"ra": 12.5, "dec": -30.0}
    return data, row


def _first_accepted_real_brick() -> tuple[Path, dict, str] | None:
    explicit = os.environ.get("REAL_DR10_BRICK")
    receipts = EXPECTED_ROOT / "receipts.jsonl"
    if not receipts.is_file():
        return None
    accepted: dict[str, dict] = {}
    with receipts.open(encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            if record.get("outcome") == "ACCEPTED" and record.get("digest_verified") is True:
                accepted[record["brickname"]] = record
    candidates = [Path(explicit)] if explicit else []
    candidates.extend((EXPECTED_ROOT / "coadd").glob("*/*/*.fits.fz"))
    # The transfer currently retains accepted files under staging/coadd before
    # its final promotion. This is still receipt-gated, read-only source data.
    candidates.extend((EXPECTED_ROOT / "staging" / "coadd").glob("*/*/*.fits.fz"))
    for path in candidates:
        name = path.name
        brickname = name.removeprefix("legacysurvey-").removesuffix("-image-r.fits.fz")
        record = accepted.get(brickname)
        if path.is_file() and record and _sha256(path) == record["local_sha256"]:
            with fits.open(path, mode="readonly", memmap=False) as hdul:
                header = hdul[1].header
                row = {"ra": float(header["CRVAL1"]), "dec": float(header["CRVAL2"])}
            return path, row, record["local_sha256"]
    return None


class ProductionReadPathTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent)
        self.path = Path(self.tmp.name) / "fixture.fits.fz"
        self.expected, self.row = _write_compressed_fixture(self.path)
        self.expected_sha256 = _sha256(self.path)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_hdu1_reader_matches_adapter_source_interface_and_logs_wcs_custody(self) -> None:
        with rp.ProductionBrickSource(
            self.path, self.row, self.expected_sha256, expected_shape=(6, 8)
        ) as source:
            np.testing.assert_array_equal(source.array, self.expected)
            self.assertEqual(source.pixel(1, 1), float(self.expected[0, 0]))
            self.assertEqual(source.pixel(8, 6), float(self.expected[5, 7]))
            self.assertEqual(source.sha256, self.expected_sha256)
            self.assertEqual(source.cards["CTYPE1"], "RA---TAN")
            self.assertLess(source.wcs.cd_det, 0.0)
            self.assertTrue(source.gate_receipt["east_left"])
            self.assertTrue(source.gate_receipt["north_up"])
            receipt = source.header_receipt
            self.assertEqual(receipt["hdu_index"], 1)
            self.assertEqual(receipt["hdu_class"], "CompImageHDU")
            self.assertEqual(receipt["decompressor"], "astropy.io.fits")
            self.assertEqual(receipt["astropy_version"], "6.0.1")
            self.assertEqual(receipt["shape"], [6, 8])
            self.assertEqual(receipt["dtype"], "float32")
            self.assertEqual(receipt["wcs_custody"]["row_order_transform"], "array[iy-1, ix-1]")
            self.assertLess(receipt["wcs_custody"]["linear_determinant"], 0.0)
            self.assertTrue(receipt["wcs_custody"]["pc4_gate_passed"])
            self.assertEqual(receipt["array_sha256"], hashlib.sha256(self.expected.tobytes()).hexdigest())

    def test_two_reads_are_byte_identical(self) -> None:
        first = rp.ProductionBrickSource(
            self.path, self.row, self.expected_sha256, expected_shape=(6, 8)
        )
        second = rp.ProductionBrickSource(
            self.path, self.row, self.expected_sha256, expected_shape=(6, 8)
        )
        try:
            self.assertEqual(first.array.tobytes(), second.array.tobytes())
            self.assertEqual(first.header_receipt, second.header_receipt)
        finally:
            first.close()
            second.close()

    def test_header_receipt_is_logged_as_canonical_json(self) -> None:
        receipt_path = Path(self.tmp.name) / "header-receipt.json"
        with rp.ProductionBrickSource(
            self.path, self.row, self.expected_sha256, expected_shape=(6, 8)
        ) as source:
            written = source.write_header_receipt(receipt_path)
            self.assertEqual(written, receipt_path)
            self.assertEqual(json.loads(receipt_path.read_text()), source.header_receipt)
            self.assertTrue(receipt_path.read_bytes().endswith(b"\n"))

    def test_multiprocessing_reads_are_identical_and_receipt_is_schedule_stable(self) -> None:
        first = rp.multiprocess_determinism_check(
            self.path, self.row, self.expected_sha256, process_count=4,
            expected_shape=(6, 8),
            completion_delays=(0.6, 0.0, 0.4, 0.2),
        )
        second = rp.multiprocess_determinism_check(
            self.path, self.row, self.expected_sha256, process_count=4,
            expected_shape=(6, 8),
            completion_delays=(0.0, 0.6, 0.2, 0.4),
        )
        self.assertTrue(first["all_arrays_identical"])
        self.assertEqual(first["array_sha256"], hashlib.sha256(self.expected.tobytes()).hexdigest())
        self.assertEqual(first["stable_content"], second["stable_content"])
        self.assertEqual(first["content_sha256"], second["content_sha256"])
        self.assertEqual(first["stable_content"]["worker_result_count"], 4)
        self.assertNotEqual(first["observed_completion_order"], second["observed_completion_order"])
        self.assertEqual(
            first["stable_content"]["content_hash_excludes"],
            ["observed_completion_order", "recorded_utc"],
        )

    def test_digest_mismatch_fails_closed(self) -> None:
        with self.assertRaises(rp.ReadPathError) as caught:
            rp.ProductionBrickSource(self.path, self.row, "0" * 64, expected_shape=(6, 8))
        self.assertEqual(caught.exception.code, "FAILED_SOURCE_DIGEST")


class RealAcceptedBrickTest(unittest.TestCase):
    def test_real_accepted_dr10_brick_hdu1_and_determinism(self) -> None:
        real = _first_accepted_real_brick()
        if real is None:
            self.skipTest("no receipt-accepted DR10 South .fits.fz brick is present locally")
        path, row, expected_sha256 = real
        first = rp.ProductionBrickSource(path, row, expected_sha256)
        second = rp.ProductionBrickSource(path, row, expected_sha256)
        try:
            self.assertEqual(first.array.shape, (3600, 3600))
            self.assertEqual(first.array.dtype, np.dtype("float32"))
            self.assertEqual(first.array.tobytes(), second.array.tobytes())
            self.assertEqual(first.header_receipt, second.header_receipt)
            self.assertEqual(first.header_receipt["hdu_index"], 1)
            self.assertTrue(first.header_receipt["wcs_custody"]["pc4_gate_passed"])
        finally:
            first.close()
            second.close()
        mp_receipt = rp.multiprocess_determinism_check(
            path, row, expected_sha256, process_count=4,
            completion_delays=(0.03, 0.0, 0.02, 0.01),
        )
        self.assertTrue(mp_receipt["all_arrays_identical"])
        self.assertEqual(mp_receipt["array_sha256"], first.header_receipt["array_sha256"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
