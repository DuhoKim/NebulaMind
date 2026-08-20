#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np
from PIL import Image

from tensor_to_png import RenderContractError, render_tensor_to_png


HERE = Path(__file__).resolve().parent


class TensorToPngTests(unittest.TestCase):
    def test_same_tensor_renders_byte_identical_png(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            root = Path(raw)
            values = np.linspace(-2.0, 2.0, 128 * 128, dtype="<f4").reshape(1, 128, 128)
            source = root / "tensor.f32le"
            source.write_bytes(values.tobytes(order="C"))
            first = root / "first.png"
            second = root / "second.png"

            render_tensor_to_png(source, first)
            render_tensor_to_png(source, second)

            self.assertEqual(first.read_bytes(), second.read_bytes())
            with Image.open(first) as image:
                self.assertEqual(image.mode, "L")
                self.assertEqual(image.size, (128, 128))
                expected = np.floor((np.clip(values[0], -1.0, 1.0) + 1.0) * 127.5 + 0.5).astype(np.uint8)
                self.assertEqual(np.asarray(image).tobytes(order="C"), expected.tobytes(order="C"))

    def test_nonfinite_tensor_is_refused(self) -> None:
        with tempfile.TemporaryDirectory(dir=HERE) as raw:
            root = Path(raw)
            values = np.zeros((1, 128, 128), dtype="<f4")
            values[0, 0, 0] = np.nan
            source = root / "tensor.f32le"
            source.write_bytes(values.tobytes(order="C"))
            with self.assertRaises(RenderContractError):
                render_tensor_to_png(source, root / "output.png")


if __name__ == "__main__":
    unittest.main(verbosity=2)
