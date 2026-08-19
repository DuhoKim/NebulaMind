#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
from astropy.io import fits

import cutout_runner as runner


HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_brick(path: Path) -> tuple[dict[str, float], np.ndarray]:
    data = np.arange(3600 * 3600, dtype=np.float32).reshape(3600, 3600) / 1000.0
    header = fits.Header()
    header["CTYPE1"] = "RA---TAN"
    header["CTYPE2"] = "DEC--TAN"
    header["CRVAL1"] = 12.5
    header["CRVAL2"] = -30.0
    header["CRPIX1"] = 1800.5
    header["CRPIX2"] = 1800.5
    header["CD1_1"] = -0.262 / 3600.0
    header["CD1_2"] = 0.0
    header["CD2_1"] = 0.0
    header["CD2_2"] = 0.262 / 3600.0
    fits.HDUList([
        fits.PrimaryHDU(),
        fits.CompImageHDU(data=data, header=header, name="COMPRESSED_IMAGE"),
    ]).writeto(path)
    return {"ra": 12.5, "dec": -30.0}, data


def write_scaler(path: Path) -> None:
    path.write_text(
        "import numpy as np\n"
        "def scale(values, constants):\n"
        "    return np.asarray(values, dtype=np.float64) * float(constants['gain'])\n",
        encoding="utf-8",
    )


class CutoutRunnerContractTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(dir=HERE)
        self.root = Path(self.tmp.name)
        self.scaler = self.root / "frozen_scaler.py"
        write_scaler(self.scaler)
        self.slots = self.root / "slots.json"
        self.slots.write_text(json.dumps({
            "ic4_invalid_fraction_cap": 0.1,
            "ic5_scaling_map": {
                "module_path": str(self.scaler),
                "module_sha256": sha256(self.scaler),
                "callable": "scale",
                "constants": {"gain": 2.0},
            },
        }), encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_synthetic_fixture_runs_readpath_adapter_and_all_ic_stages(self) -> None:
        brick = self.root / "fixture.fits.fz"
        row, _ = write_brick(brick)
        output_dir = self.root / "outputs"
        receipt = runner.compose_object(
            runner.Position(ra=12.5, dec=-30.0, ls_id="SYNTH-FULL-PATH"),
            [runner.BrickSpec(path=brick, row=row, sha256=sha256(brick), brickname="synthetic")],
            slots_path=self.slots,
            output_dir=output_dir,
            synthetic=True,
        )
        self.assertEqual(receipt["status"], "PASS")
        self.assertTrue(all(receipt["ic_flags"][f"IC-{index}"] for index in range(1, 8)))
        self.assertEqual(receipt["tensor"]["shape"], [1, 128, 128])
        self.assertEqual(receipt["tensor"]["dtype"], "<f4")
        self.assertEqual(receipt["tensor"]["order"], "C")
        tensor_path = output_dir / receipt["tensor"]["path"]
        self.assertEqual(sha256(tensor_path), receipt["output_tensor_sha256"])
        self.assertEqual(receipt["brick_sha_refs"][0]["sha256"], sha256(brick))
        self.assertEqual(receipt["adapter_geometry_receipt"]["coverage_zero_count"], 0)
        claimed = receipt["receipt_content_sha256"]
        stable = dict(receipt)
        stable.pop("receipt_content_sha256")
        self.assertEqual(
            claimed,
            hashlib.sha256(
                json.dumps(stable, sort_keys=True, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
        )

    def test_ic1_wrong_shape_fails_closed(self) -> None:
        with self.assertRaises(runner.ContractError) as caught:
            runner.apply_input_contract(
                np.zeros((2, 128, 128), dtype=np.float32),
                slots_path=self.slots,
                real_sky=False,
            )
        self.assertEqual(caught.exception.code, "FAILED_IC1_SINGLE_PLANE")

    def test_null_slots_refuse_real_sky(self) -> None:
        null_slots = self.root / "null-slots.json"
        null_slots.write_text(json.dumps({
            "ic4_invalid_fraction_cap": None,
            "ic5_scaling_map": None,
        }), encoding="utf-8")
        with self.assertRaises(runner.ContractError) as caught:
            runner.apply_input_contract(
                np.zeros((128, 128), dtype=np.float32),
                slots_path=null_slots,
                real_sky=True,
            )
        self.assertEqual(caught.exception.code, "REFUSED_REAL_SKY_UNFILLED_SLOTS")

    def test_mirror_is_bit_exact_and_involutive(self) -> None:
        raster = np.arange(128 * 128, dtype="<f4").reshape(128, 128)
        tensor, _ = runner.apply_input_contract(raster, slots_path=self.slots, real_sky=False)
        mirrored = runner.mirror_tensor(tensor)
        restored = runner.mirror_tensor(mirrored)
        self.assertEqual(restored.tobytes(order="C"), tensor.tobytes(order="C"))
        self.assertEqual(mirrored[0].tobytes(order="C"), np.fliplr(tensor[0]).tobytes(order="C"))

    def test_positions_file_is_explicit_and_has_no_selection_logic(self) -> None:
        path = self.root / "positions.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["ra", "dec", "ls_id"])
            writer.writeheader()
            writer.writerow({"ra": "12.5", "dec": "-30", "ls_id": "abc-123"})
        self.assertEqual(runner.load_positions(path), [runner.Position(12.5, -30.0, "abc-123")])


if __name__ == "__main__":
    unittest.main(verbosity=2)
