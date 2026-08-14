#!/usr/bin/env python3
"""Focused tests for the BS-3 R4/R5 synthetic receipt runner."""
from __future__ import annotations

import unittest

import numpy as np

from run_bs3_r4_r5 import (
    bad_interpolating_mirror,
    canary_identity_residual,
    canary_passes,
    flip_imbalance_contribution,
    pure_index_mirror,
)


class Bs3R4R5RunnerTests(unittest.TestCase):
    def test_pure_index_mirror_is_byte_exact_involution(self) -> None:
        image = np.arange(64, dtype=np.float32).reshape(8, 8)
        self.assertEqual(
            pure_index_mirror(pure_index_mirror(image)).tobytes(),
            image.tobytes(),
        )

    def test_interpolating_mirror_is_not_the_pure_index_mirror(self) -> None:
        image = np.arange(64, dtype=np.float32).reshape(8, 8)
        bad = bad_interpolating_mirror(image)
        self.assertEqual(bad.dtype, np.float32)
        self.assertFalse(np.array_equal(bad, pure_index_mirror(image)))
        self.assertNotEqual(
            bad_interpolating_mirror(bad).tobytes(),
            image.tobytes(),
        )

    def test_flip_imbalance_contribution_uses_both_raw_trunk_signs(self) -> None:
        self.assertEqual(flip_imbalance_contribution(2.0, 4.0), 1.0)
        self.assertEqual(flip_imbalance_contribution(-2.0, -4.0), -1.0)
        self.assertEqual(flip_imbalance_contribution(2.0, -4.0), 0.0)
        self.assertEqual(flip_imbalance_contribution(0.0, -4.0), -0.5)

    def test_canary_requires_strictly_more_than_one_hundredth(self) -> None:
        self.assertFalse(canary_passes([0.0, 0.01]))
        self.assertTrue(canary_passes([0.0, 0.0100001]))

    def test_canary_residual_runs_frozen_production_chi_on_bad_input(self) -> None:
        # chi(x) = (10 - 2) / 2 = 4; chi(bad(x)) = (3 - 1) / 2 = 1.
        # The exact spike replay is abs(chi(bad(x)) + chi(x)) = 5.
        self.assertEqual(canary_identity_residual(10.0, 2.0, 3.0, 1.0), 5.0)


if __name__ == "__main__":
    unittest.main()
