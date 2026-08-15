#!/usr/bin/env python3
"""Contract tests for the BS-5 synthetic WCS-parity gate."""
from __future__ import annotations

import unittest

from validate_wcs_parity import build_parity_receipt, parity_predicates


class WcsParityContractTests(unittest.TestCase):
    def test_north_up_east_left_synthetic_wcs_has_required_logged_parity(self) -> None:
        receipt = build_parity_receipt()
        checks = parity_predicates(receipt)
        self.assertTrue(all(checks.values()), checks)
        self.assertLess(receipt["cd_pc_cdelt_determinant"], 0.0)
        self.assertEqual(receipt["row_order_transform_determinant"], 1.0)
        self.assertLess(receipt["combined_pixel_to_sky_determinant"], 0.0)
        self.assertEqual(receipt["east_direction_on_raster"], "left")
        self.assertEqual(receipt["north_direction_on_raster"], "up")
        self.assertEqual(receipt["winding_convention"], "position angle increasing North through East")
        self.assertEqual(receipt["increasing_pa_visual_winding"], "counter-clockwise")

    def test_parity_flipped_east_right_wcs_is_rejected(self) -> None:
        receipt = build_parity_receipt(east_left=False)
        checks = parity_predicates(receipt)
        self.assertFalse(checks["east_left"])
        self.assertFalse(checks["combined_parity_reversing"])
        self.assertFalse(all(checks.values()))

    def test_silent_row_flip_is_rejected(self) -> None:
        receipt = build_parity_receipt(row_order_reversed=True)
        checks = parity_predicates(receipt)
        self.assertFalse(checks["row_order_preserved"])
        self.assertFalse(checks["combined_parity_reversing"])
        self.assertFalse(all(checks.values()))


if __name__ == "__main__":
    unittest.main()
