#!/usr/bin/env python3
"""Frozen IC-5 map selected on synthetic inputs only.

The frozen estimator was trained and calibrated on the BS-3 generator's float32
values. The identity affine map is the unique zero-change fixed monotone choice
that preserves that already-frozen tensor scale and permits a bit-level witness.
"""
from __future__ import annotations

import numpy as np

EXPECTED_CONSTANTS = {
    "form": "tensor = float32(nanomaggy)",
    "gain": 1.0,
    "offset": 0.0,
}


def scale(values: np.ndarray, constants: dict) -> np.ndarray:
    """Apply the fixed monotone identity affine map without normalization."""
    if constants != EXPECTED_CONSTANTS:
        raise ValueError("IC-5 constants do not match the frozen identity map")
    return np.asarray(values, dtype=np.float32)
