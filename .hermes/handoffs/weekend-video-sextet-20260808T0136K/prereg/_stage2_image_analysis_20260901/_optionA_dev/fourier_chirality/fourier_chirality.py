#!/usr/bin/env python3
"""2DFFT-class chirality estimator, configuration-driven — OPTION (A) candidate family (development code, not a study pin
until the selection rule is signed). Every searchable constant lives in a configuration dict; ALL configuration-dependent
state is recomputed inside Estimator.__init__, never at import time, so a pinned driver can instantiate each of the
enumerated configurations from the same bytes.

w(x): nearest-neighbour log-polar map of a 128x128 raster on an annulus (optionally on the moment-deprojected plane),
azimuthal-mean removal per radius, 2-D DFT in (u = ln r, theta), and the signed asymmetry of m = 2 power between positive
and negative radial frequency p, bounded in [-1, 1]. chi(x) = (float32 w(x) - float32 w(mirror x))/2 is value-antisymmetric
for finite unequal w-values; a tie yields +0.0 in both orders and a non-finite w yields NaN - both are MEASUREMENT-FAIL
under the study's §9.6, never scores.
"""
from __future__ import annotations
import hashlib, itertools, json
import numpy as np

N = 128
# Enumerated search space (selection rule §7). Key order IS the lexicographic enumeration order. Nothing else varies.
CONFIG_GRID = {
    "R_MIN": [4, 6, 8],
    "R_MAX": [48, 56],
    "DEPROJECT": [True, False],
    "Q_MIN": [0.35, 0.50],
    "P_MIN": [1, 2],
    "MOMENT_APERTURE": ["annulus", "inner32"],
}
FIXED = {"N_U": 64, "N_T": 128, "M_MODE": 2, "P_MAX": 40}       # fixed, not searched
DEFAULT_CFG = {"R_MIN": 6, "R_MAX": 56, "DEPROJECT": True, "Q_MIN": 0.35, "P_MIN": 1, "MOMENT_APERTURE": "annulus"}


def enumerate_configs():
    """All configurations in the stated lexicographic order (itertools.product over CONFIG_GRID in key order)."""
    keys = list(CONFIG_GRID)
    return [dict(zip(keys, vals)) for vals in itertools.product(*(CONFIG_GRID[k] for k in keys))]


def config_id(cfg) -> str:
    """Canonical serialization: JSON, sorted keys, no spaces; id = SHA-256 of that string."""
    s = json.dumps(cfg, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(s.encode()).hexdigest()


def mirror(x: np.ndarray) -> np.ndarray:
    return np.fliplr(x)


class Estimator:
    def __init__(self, cfg=None):
        cfg = dict(DEFAULT_CFG if cfg is None else cfg)
        if set(cfg) != set(CONFIG_GRID):
            raise ValueError(f"configuration keys must be exactly {sorted(CONFIG_GRID)}; got {sorted(cfg)}")
        for k in CONFIG_GRID:
            if cfg[k] not in CONFIG_GRID[k]:
                raise ValueError(f"configuration value outside the enumerated grid: {k}={cfg[k]!r}")
        self.cfg = cfg; self.config_id = config_id(cfg)
        self.r_min, self.r_max = float(cfg["R_MIN"]), float(cfg["R_MAX"])
        self.deproject, self.q_min, self.p_min = bool(cfg["DEPROJECT"]), float(cfg["Q_MIN"]), float(cfg["P_MIN"])
        self.n_u, self.n_t, self.m_mode, self.p_max = FIXED["N_U"], FIXED["N_T"], FIXED["M_MODE"], float(FIXED["P_MAX"])
        self.cx = (N - 1) / 2.0
        du = (np.log(self.r_max) - np.log(self.r_min)) / self.n_u
        self.u = np.log(self.r_min) + (np.arange(self.n_u) + 0.5) * du
        self.t = -np.pi + (np.arange(self.n_t) + 0.5) * (2 * np.pi / self.n_t)
        self.r = np.exp(self.u); self.ct, self.st = np.cos(self.t), np.sin(self.t)
        self.ix0 = np.rint(self.cx + self.r[:, None] * self.ct[None, :]).astype(np.int64)
        self.iy0 = np.rint(self.cx + self.r[:, None] * self.st[None, :]).astype(np.int64)
        assert self.ix0.min() >= 0 and self.ix0.max() < N and self.iy0.min() >= 0 and self.iy0.max() < N
        self.p = np.fft.fftfreq(self.n_u, d=du) * 2 * np.pi
        self.pos = (self.p >= self.p_min) & (self.p <= self.p_max); self.neg = (self.p <= -self.p_min) & (self.p >= -self.p_max)
        yy, xx = np.mgrid[0:N, 0:N]; self.dx = xx - self.cx; self.dy = yy - self.cx; rr = np.hypot(self.dx, self.dy)
        self.aperture = rr <= (self.r_max if cfg["MOMENT_APERTURE"] == "annulus" else 32.0)

    def moments(self, v):
        wgt = np.where(self.aperture, np.maximum(v - np.median(v[self.aperture]), 0.0), 0.0); s = wgt.sum()
        if s <= 0.0: return 0.0, 1.0
        cxx = float((wgt * self.dx * self.dx).sum() / s); cyy = float((wgt * self.dy * self.dy).sum() / s); cxy = float((wgt * self.dx * self.dy).sum() / s)
        tr, det = cxx + cyy, cxx * cyy - cxy * cxy; disc = max(tr * tr / 4.0 - det, 0.0) ** 0.5
        l1, l2 = tr / 2.0 + disc, max(tr / 2.0 - disc, 0.0)
        if l1 <= 0.0: return 0.0, 1.0
        return float(0.5 * np.arctan2(2.0 * cxy, cxx - cyy)), float(min(1.0, max(self.q_min, (l2 / l1) ** 0.5)))

    def logpolar(self, x):
        v = np.asarray(x, dtype=np.float64)
        if not self.deproject: return v[self.iy0, self.ix0]
        phi, q = self.moments(v)
        xp = self.r[:, None] * self.ct[None, :]; yp = self.r[:, None] * self.st[None, :]
        X = self.cx + xp * np.cos(phi) - q * yp * np.sin(phi); Y = self.cx + xp * np.sin(phi) + q * yp * np.cos(phi)
        return v[np.clip(np.rint(Y).astype(np.int64), 0, N - 1), np.clip(np.rint(X).astype(np.int64), 0, N - 1)]

    def w(self, x) -> float:
        lp = self.logpolar(x); lp = lp - lp.mean(axis=1, keepdims=True)
        a = np.fft.fft2(lp)[:, self.m_mode]; pw = a.real ** 2 + a.imag ** 2
        pos, neg = float(pw[self.pos].sum()), float(pw[self.neg].sum()); tot = pos + neg
        return 0.0 if tot <= 0.0 else (pos - neg) / tot

    def chi(self, x) -> np.float32:
        a = np.float32(self.w(x)); b = np.float32(self.w(mirror(x)))
        return np.float32((a - b) / np.float32(2))

    def sign(self, x) -> int:
        c = self.chi(x)
        return 0 if c == 0 or not np.isfinite(c) else (1 if c > 0 else -1)


# Module-level default instance (development convenience; the driver instantiates Estimator(cfg) explicitly).
_default = Estimator(DEFAULT_CFG)
R_MIN, R_MAX, N_U, N_T, M_MODE, P_MIN, P_MAX, Q_MIN = 6.0, 56.0, 64, 128, 2, 1.0, 40, 0.35
def logpolar(x): return _default.logpolar(x)
def w(x): return _default.w(x)
def chi(x): return _default.chi(x)
def sign(x): return _default.sign(x)
