#!/usr/bin/env python3
"""Validate the BS-5 synthetic raster WCS parity before model inference.

This file contains no model import and no image generator. It writes a parity-only
receipt for a position-free synthetic North-up/East-left WCS template.
"""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
PIXEL_SCALE_DEG = 1.0 / 3600.0
PC3_QUOTE = (
    "Per-object WCS parity: CD/PC·CDELT determinant logged; row-order transform determinant "
    "logged; combined pixel→sky sign logged; handedness evaluated in sky coordinates "
    "(winding East-of-North)."
)
FROZEN_PREREG_SHA256 = "da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308"
DRAFT_CARRY_SHA256 = "ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590"


def determinant_2x2(matrix: list[list[float]]) -> float:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def multiply_2x2(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return [
        [
            left[row][0] * right[0][column]
            + left[row][1] * right[1][column]
            for column in range(2)
        ]
        for row in range(2)
    ]


def build_parity_receipt(
    *, east_left: bool = True, row_order_reversed: bool = False
) -> dict:
    """Build a position-free synthetic WCS parity receipt.

    Logical production raster axes are column-right and FITS-native row-up. Sky
    tangent axes are East and North. North-up/East-left therefore maps column+
    to East- and row+ to North+, giving a negative CD/PC·CDELT determinant.
    """
    east_scale = -PIXEL_SCALE_DEG if east_left else PIXEL_SCALE_DEG
    cd = [[east_scale, 0.0], [0.0, PIXEL_SCALE_DEG]]
    row_order = [[1.0, 0.0], [0.0, -1.0 if row_order_reversed else 1.0]]
    combined = multiply_2x2(cd, row_order)
    cd_det = determinant_2x2(cd)
    row_det = determinant_2x2(row_order)
    combined_det = determinant_2x2(combined)
    north_up = combined[1][1] > 0.0
    east_is_left = combined[0][0] < 0.0
    return {
        "scope": "position-free synthetic WCS template only; no image, sky position, survey row, or real object",
        "validation_order": "parity gate executes before model load and before synthetic spiral generation",
        "binding_pc3_quote": PC3_QUOTE,
        "binding_pc3_source": "PREREG_LONGO_AMPLITUDE_TEST_20260812.md:186-188, carried unchanged by frozen preregistration section 6",
        "frozen_preregistration_sha256": FROZEN_PREREG_SHA256,
        "carried_draft_sha256": DRAFT_CARRY_SHA256,
        "raster": [128, 128],
        "logical_pixel_axes": ["column increases right", "FITS-native row increases up"],
        "sky_tangent_axes": ["East", "North"],
        "crval_or_sky_position": None,
        "pixel_scale_degrees": PIXEL_SCALE_DEG,
        "pc_matrix": [[1.0, 0.0], [0.0, 1.0]],
        "cdelt_degrees": [east_scale, PIXEL_SCALE_DEG],
        "cd_pc_cdelt_matrix": cd,
        "cd_pc_cdelt_determinant": cd_det,
        "cd_pc_cdelt_sign": -1 if cd_det < 0.0 else 1 if cd_det > 0.0 else 0,
        "row_order_transform_matrix": row_order,
        "row_order_transform_determinant": row_det,
        "combined_pixel_to_sky_matrix": combined,
        "combined_pixel_to_sky_determinant": combined_det,
        "combined_pixel_to_sky_sign": -1 if combined_det < 0.0 else 1 if combined_det > 0.0 else 0,
        "linear_wcs_parity": "REVERSING" if combined_det < 0.0 else "PRESERVING",
        "east_direction_on_raster": "left" if east_is_left else "right",
        "north_direction_on_raster": "up" if north_up else "down",
        "winding_convention": "position angle increasing North through East",
        "increasing_pa_visual_winding": (
            "counter-clockwise" if north_up and east_is_left else "not counter-clockwise"
        ),
        "distortion_keywords": [],
        "distortion_branch": "synthetic linear template; no SIP/PV/CPDIS/DET2IM",
        "does_not_substitute_for_future_per_object_pc3": True,
    }


def parity_predicates(receipt: dict) -> dict[str, bool]:
    return {
        "position_free": receipt["crval_or_sky_position"] is None,
        "production_raster": receipt["raster"] == [128, 128],
        "cd_nonzero": receipt["cd_pc_cdelt_determinant"] != 0.0,
        "cd_reversing": receipt["cd_pc_cdelt_determinant"] < 0.0,
        "row_order_preserved": receipt["row_order_transform_determinant"] == 1.0,
        "combined_parity_reversing": receipt["combined_pixel_to_sky_determinant"] < 0.0,
        "east_left": receipt["east_direction_on_raster"] == "left",
        "north_up": receipt["north_direction_on_raster"] == "up",
        "east_of_north_is_ccw": receipt["increasing_pa_visual_winding"] == "counter-clockwise",
        "no_distortion": receipt["distortion_keywords"] == [],
        "future_pc3_not_claimed": receipt["does_not_substitute_for_future_per_object_pc3"] is True,
    }


def main() -> None:
    receipt = build_parity_receipt()
    checks = parity_predicates(receipt)
    receipt["checks"] = checks
    receipt["status"] = "PASS_WCS_PARITY_FIRST" if all(checks.values()) else "FAIL_WCS_PARITY"
    destination = OUT / "wcs_parity.json"
    destination.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
