#!/usr/bin/env python3
"""Feasibility spike, section 10 item 1 — w(x), the chi wrapper, synthetic spirals.

BOUNDARY: synthetic images only. Nothing here reads, fetches, or points at any real
survey catalogue or sky position. No bulk acquisition.

Definitions (LANA_SPIN_DESIGN_BRIEF_20260812.md §0/§3):
    mirror(x) := np.fliplr(x)                      # pure index reversal, no resampling
    chi(x)    := (w(x) - w(mirror(x))) / 2
    identity  :  chi(mirror(x)) == -chi(x)  for ANY deterministic w

w(x) is deliberately crude and training-free (Ganalyzer-class): nearest-neighbour polar
binning (NO interpolation), per-radius azimuthal intensity peak, circular unwrap, then the
sign of d(theta)/d(ln r) via least squares. Positive w = arms wind counter-clockwise
outward (S-wise); negative = clockwise (Z-wise). Simplicity is the point: the identity must
hold for ANY w, and a simple w makes any violation attributable.
"""
from __future__ import annotations

import numpy as np

N = 128                     # image side (even on purpose: fliplr is still exact reversal)
R_MIN, R_MAX = 6.0, 56.0    # tracing annulus in pixels
N_RBINS, N_TBINS = 25, 90   # polar grid (4-degree azimuthal bins)


def mirror(x: np.ndarray) -> np.ndarray:
    """Left-right mirror by pure index reversal. mirror(mirror(x)) is bit-identical to x."""
    return np.fliplr(x)


# ------------------------------------------------------------------ w(x) ----
_yy, _xx = np.mgrid[0:N, 0:N]
_cx = (N - 1) / 2.0          # centre of the pixel grid; fliplr maps xx -> (N-1)-xx exactly
_dx = _xx - _cx
_dy = _yy - _cx
_rr = np.hypot(_dx, _dy)
_tt = np.arctan2(_dy, _dx)   # (-pi, pi]

_r_edges = np.linspace(R_MIN, R_MAX, N_RBINS + 1)
_r_idx = np.digitize(_rr.ravel(), _r_edges) - 1
_t_idx = np.minimum(((_tt.ravel() + np.pi) / (2 * np.pi) * N_TBINS).astype(np.int64),
                    N_TBINS - 1)
_in_annulus = (_r_idx >= 0) & (_r_idx < N_RBINS)
_flat_bin = _r_idx[_in_annulus] * N_TBINS + _t_idx[_in_annulus]
_bin_counts = np.bincount(_flat_bin, minlength=N_RBINS * N_TBINS).astype(np.float64)
_r_centers = 0.5 * (_r_edges[:-1] + _r_edges[1:])
_theta_centers = -np.pi + (np.arange(N_TBINS) + 0.5) * (2 * np.pi / N_TBINS)


def w(x: np.ndarray) -> float:
    """Deterministic arm-winding estimator. Input: (N, N) float64 image."""
    v = x.ravel()[_in_annulus]
    sums = np.bincount(_flat_bin, weights=v, minlength=N_RBINS * N_TBINS)
    prof = (sums / np.maximum(_bin_counts, 1.0)).reshape(N_RBINS, N_TBINS)
    peak_t = _theta_centers[np.argmax(prof, axis=1)]        # argmax: deterministic (first max)
    # arm-agnostic unwrap: a 2-armed profile is periodic in theta with period pi, so
    # inter-arm jumps of ~pi must be invisible to the winding slope. The first version of
    # this estimator wrapped diffs to (-pi, pi] and mapped every +pi inter-arm jump to -pi,
    # inverting the recovered sign systematically — kept on record in the receipt.
    d = np.diff(peak_t)
    d = (d + np.pi / 2) % np.pi - np.pi / 2
    track = np.concatenate(([peak_t[0]], peak_t[0] + np.cumsum(d)))
    lr = np.log(_r_centers)
    lr0 = lr - lr.mean()
    slope = float(np.dot(lr0, track) / np.dot(lr0, lr0))    # LSQ slope, fixed eval order
    return slope


def chi(x: np.ndarray) -> float:
    return (w(x) - w(mirror(x))) / 2.0


# --------------------------------------------------- synthetic spirals ----
def synth_spiral(parity: int, pitch_deg: float, incl_deg: float, snr: float,
                 seed: int, arms: int = 2, arm_amp: float = 0.9,
                 phase: float = 0.7) -> np.ndarray:
    """Analytic two-armed log-spiral disk, evaluated directly on the pixel grid.

    parity=+1 winds counter-clockwise outward (S-wise); -1 is its exact chirality
    opposite. Inclination is an analytic squeeze of the y coordinate BEFORE evaluation
    (no image resampling anywhere). Noise: seeded standard normal, scaled to the target
    peak signal-to-noise.
    """
    b = 1.0 / np.tan(np.radians(pitch_deg))
    q = np.cos(np.radians(incl_deg))
    dxp, dyp = _dx, _dy / q
    r = np.hypot(dxp, dyp)
    t = np.arctan2(dyp, dxp)
    r_safe = np.maximum(r, 0.5)
    disk = np.exp(-r_safe / 18.0)
    spiral = 1.0 + arm_amp * np.cos(arms * (t - parity * b * np.log(r_safe / 8.0) - phase))
    img = disk * spiral
    img[r > 60.0] = 0.0
    rng = np.random.default_rng(seed)
    noise = rng.standard_normal((N, N))
    img = img / img.max()
    return img + noise * (1.0 / snr)


def synth_disk(incl_deg: float, snr: float, seed: int) -> np.ndarray:
    """Armless disk — the chirality-free null used for tau calibration."""
    q = np.cos(np.radians(incl_deg))
    r = np.hypot(_dx, _dy / q)
    img = np.exp(-np.maximum(r, 0.5) / 18.0)
    img[r > 60.0] = 0.0
    rng = np.random.default_rng(seed)
    return img / img.max() + rng.standard_normal((N, N)) * (1.0 / snr)


def bits(f: float) -> int:
    return int(np.float64(f).view(np.uint64))
