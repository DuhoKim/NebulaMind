"""§8.9a–§8.9d pixel rejection, VERSION 2 — the pipeline identity fixed by the signed option A rule V15 §6
(2026-09-06T00:04:07Z) and to be frozen by Tier-C V36 (§17.6 amendment of V35). Source grid only; nothing here interpolates.

Changes from `pixel_rejection.py` (Tier-C V35 §8.9a, SHA-256 8f66bc1c…, which stays byte-identical and pinned by V35):
  1. Bit 11 MEDIUM is NOT rejecting. It is CARRIED through §8.9d and reported per raster as a covariate (`medium_count`).
  2. Source pixels with nexp-r == 0 are REJECTING: replaced by the §8.9c lower median and flagged — in place of the
     all-or-nothing §8.12 refusal. §8.14a (F ≤ 819; no flagged pixel inside T, r_T = 23) is unchanged and still refuses
     a raster whose zero-exposure pixel lands inside the protected region.
  3. Replacement statistic unchanged: lower median of ACCEPTED source pixels; fewer than 16 accepted → NO-ACCEPTED-PIXELS.
Both integer planes are required as integers; a resampled maskbits or nexp plane is refused.
"""
from __future__ import annotations
import numpy as np

# DR9/DR10 bitmask definitions, https://www.legacysurvey.org/dr10/bitmasks/
REJECT_BITS = (1, 3, 6, 10, 13)               # BRIGHT SATUR_R ALLMASK_R BAILOUT CLUSTER
MEDIUM_BIT = 11                               # carried, reported, NOT rejecting (V15 §6)
REJECT_MASK = 0
for _b in REJECT_BITS:
    REJECT_MASK |= (1 << _b)
NOT_REJECTED = (0, 12, 2, 4, MEDIUM_BIT)      # NPRIMARY, GALAXY, SATUR_G, SATUR_Z, MEDIUM
MIN_ACCEPTED = 16
NO_ACCEPTED_PIXELS = "NO-ACCEPTED-PIXELS"


def _integer(plane: np.ndarray, name: str) -> np.ndarray:
    a = np.asarray(plane)
    if not np.issubdtype(a.dtype, np.integer):
        raise ValueError(f"{name} must be integer; a resampled {name} plane is not admissible")
    return a


def bit_rejection_mask(maskbits: np.ndarray) -> np.ndarray:
    """Boolean rejection from the INTEGER maskbits plane alone, by exact bitwise test (five bits)."""
    return (_integer(maskbits, "maskbits") & REJECT_MASK) != 0


def zero_exposure_mask(nexp: np.ndarray) -> np.ndarray:
    """Boolean rejection from the INTEGER nexp-r plane: exposure count == 0 (negative counts are refused as corrupt)."""
    n = _integer(nexp, "nexp")
    if (n < 0).any():
        raise ValueError("nexp plane carries a negative exposure count")
    return n == 0


def rejection_mask(maskbits: np.ndarray, nexp: np.ndarray) -> np.ndarray:
    """§8.9a (v2): rejected = rejecting bit set OR nexp-r == 0. Shapes must agree."""
    b = bit_rejection_mask(maskbits); z = zero_exposure_mask(nexp)
    if b.shape != z.shape:
        raise ValueError("maskbits and nexp planes differ in shape")
    return b | z


def medium_mask(maskbits: np.ndarray) -> np.ndarray:
    """Which pixels carry MEDIUM — reported, never used for rejection."""
    return (_integer(maskbits, "maskbits") & (1 << MEDIUM_BIT)) != 0


def replacement_value(image: np.ndarray, reject: np.ndarray) -> float:
    """Lower median of the ACCEPTED source pixels (§8.9c, unchanged). Refuses if too few survive."""
    accepted = np.asarray(image)[~reject]
    if accepted.size < MIN_ACCEPTED:
        raise ValueError(NO_ACCEPTED_PIXELS)
    ordered = np.sort(accepted.astype(np.float64, copy=False).ravel())
    return float(ordered[(ordered.size - 1) // 2])       # lower median, always an observed value


def clean_source(image: np.ndarray, maskbits: np.ndarray, nexp: np.ndarray):
    """Replace rejected source pixels BEFORE reprojection. Returns (cleaned, fill, n_rejected, n_zero_exposure, n_medium)."""
    reject = rejection_mask(maskbits, nexp)
    fill = replacement_value(image, reject)
    cleaned = np.array(image, dtype=np.float64, copy=True)
    cleaned[reject] = fill
    return cleaned, fill, int(reject.sum()), int(zero_exposure_mask(nexp).sum()), int(medium_mask(maskbits).sum())


def flagged_output(rendered_maskbits: np.ndarray, rendered_nexp: np.ndarray) -> np.ndarray:
    """Which OUTPUT pixels drew on a rejected source pixel (§8.9d): rejecting bit OR zero exposure, read exactly from the
    nearest-neighbour-sampled integer planes. MEDIUM does not flag."""
    return rejection_mask(rendered_maskbits, rendered_nexp)


def medium_count(rendered_maskbits: np.ndarray) -> int:
    """The per-raster covariate V15 §6 requires: number of OUTPUT pixels carrying MEDIUM."""
    return int(medium_mask(rendered_maskbits).sum())
