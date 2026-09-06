#!/usr/bin/env python3
"""protected_region_v2 (Tier-C V38 draft): identical to its V35 predecessor except that r_T is a binary64 value with NO integer truncation — the
signed §8.14 formula min(64, max(23, 2·shape_r/0.262)) prescribes none; codex (V37 gate) exhibited shape_r = 3.1309 → 23.9 truncated to 23, so a
flag at distance 23.505 was accepted inside the prescribed T. ORIGINAL DOCSTRING FOLLOWS.
§8.14 / §9B.2d protected target region; standard library only.

ONE word, ONE meaning, TWO paths. `shape_r` is the DR10-south Tractor half-light
radius in arcseconds, read from the sealed §16.1 snapshot. Every frozen-sample
object has one, because Tier C is by construction DR10-matched. No §9B validation
object has one, because the pool is by construction NO-DR10. Through V30 the
validation path was routed through §8.14 unchanged, so every validation object hit
"missing shape_r -> DATA-INTEGRITY-FAIL" and the gate could not lawfully pass. A
referee found it; the corpus had to be pinned precisely enough to expose it.

The chain, as code so it can be tested end to end:
    shape_r --(r_t_main)--> r_T --(in_protected_region)--> T --(refuse_on_central)--> §8.14a(ii)
The validation path replaces only the FIRST arrow (r_t_validation), never the rest.
"""
from __future__ import annotations

import math

PIXEL_SCALE_ARCSEC = 0.262
R_T_FLOOR = 23          # §8.14: covers the §8.15 32x32 aperture, whose corners lie at sqrt(2)*16 = 22.63 px
R_T_CAP = 64
R_T_VALIDATION = 23     # §9B.2d: the floor, and nothing else, because no catalogue size exists
F_CEILING = 819         # §8.14a(i): 5% of 16,384 output pixels
CENTRE = 63.5           # 0-based centre of a 128x128 raster (FITS CRPIX 64.5)
DATA_INTEGRITY_FAIL = "DATA-INTEGRITY-FAIL"


def r_t_main(shape_r) -> float:
    """§8.14, the Tier-C measurement path. UNCHANGED by V31."""
    if shape_r is None or not isinstance(shape_r, (int, float)) or isinstance(shape_r, bool):
        raise ValueError(DATA_INTEGRITY_FAIL + ": shape_r missing")
    if not math.isfinite(shape_r) or shape_r < 0:
        raise ValueError(DATA_INTEGRITY_FAIL + ": shape_r not finite or negative")
    return float(min(R_T_CAP, max(R_T_FLOOR, 2.0 * shape_r / PIXEL_SCALE_ARCSEC)))   # v2 (Tier-C V38): binary64, NO truncation — §8.14 prescribes none (codex V37 FATAL 1)


def r_t_validation() -> float:
    """§9B.2d, the validation path: a constant. Takes NO catalogue argument on purpose, so
    a call site cannot accidentally hand it a main-path value or vice versa."""
    return float(R_T_VALIDATION)


def in_protected_region(row: int, col: int, r_t: float) -> bool:
    """§8.14: output pixel (row, col) lies within radius r_T of the raster centre."""
    return math.hypot(row - CENTRE, col - CENTRE) <= r_t


def refuse_on_contamination(flagged: list, r_t: float) -> str | None:
    """§8.14a, identical for both paths: refuse if F > 819 OR any flagged pixel is inside T.
    Returns the refusal reason or None."""
    if len(flagged) > F_CEILING:
        return DATA_INTEGRITY_FAIL + ": F exceeds 5% ceiling"
    for row, col in flagged:
        if in_protected_region(row, col, r_t):
            return DATA_INTEGRITY_FAIL + ": flagged pixel inside protected region"
    return None
