#!/usr/bin/env python3
"""Footprint-aware dipole estimator — successor reference implementation. SYNTHETIC ONLY.

Implements SUCCESSOR_SCOPE_20260821.md requirements 3-5, the repairs for the three defects
that killed the predecessor's statistical protocol:

  R3  normalisation as a PROCEDURE over the accepted positions, never the constant 3*D
      (the constant is a full-sky special case that over-responded 42.76% on the dead cap);
  R4  the monopole PROJECTED OUT by centring, not merely reported
      (the dead cap's leakage coefficient was -1.939 per unit monopole);
  R5  sigma from the exact permutation variance Var(s)*Var(c)/(N-1), never sqrt(1/(3N)).

The estimator, for signs s_i in {-1,+1} at positions with axis-cosines c_i:

    A_hat = sum((s - s_bar)(c - c_bar)) / sum((c - c_bar)^2)

— the through-origin slope on centred variables. E[A_hat] = A for ANY footprint under
E[s|c] = M + A*c, because centring annihilates M and the denominator carries the footprint's
own second moment. Longo's own fit (a*cos(gamma), uncentred) differs by his footprint's mean;
comparisons to his amplitude are made at the ESTIMAND level, not by copying his estimator.

This file contains no I/O against any real-sky product and refuses none — it takes arrays.
Freezing, authorization gating and refuse-paths belong to the successor prereg's runner, which
wraps this; the mathematics is what is validated here.
"""
import numpy as np


def axis_cosines(ra_deg, dec_deg, axis_ra_deg, axis_dec_deg):
    ra, dec = np.radians(ra_deg), np.radians(dec_deg)
    ra0, dec0 = np.radians(axis_ra_deg), np.radians(axis_dec_deg)
    return (np.sin(dec) * np.sin(dec0)
            + np.cos(dec) * np.cos(dec0) * np.cos(ra - ra0))


def estimate(signs, cosines):
    """Centred dipole amplitude with footprint-exact moments. Returns dict of scalars."""
    s = np.asarray(signs, dtype=float)
    c = np.asarray(cosines, dtype=float)
    n = s.size
    sc, cc = s - s.mean(), c - c.mean()
    denom = float(cc @ cc)                       # n * Var(c): the footprint's own leverage
    a_hat = float(sc @ cc) / denom
    var_s = float(sc @ sc) / n                   # population variances, per the exact
    var_c = denom / n                            # permutation derivation (re-gate, 2026-08-21)
    var_perm_D = var_s * var_c / (n - 1)         # exact Var of D = mean(s_perm * cc) under permutation
    sigma_a = np.sqrt(var_perm_D) * n / denom    # slope sigma: D/(Var(c)) scaling
    return {"n": n, "a_hat": a_hat, "sigma_a": float(sigma_a),
            "var_c": var_c, "leverage": denom, "monopole": float(s.mean())}


def permutation_p(signs, cosines, n_perm, rng, alternative_positive=True):
    """One-sided permutation p at the frozen axis. Sign convention is the CALLER's problem,
    stated per the successor's BS-5 successor slot; this function is polarity-neutral."""
    s = np.asarray(signs, dtype=float)
    c = np.asarray(cosines, dtype=float)
    cc = c - c.mean()
    obs = float((s - s.mean()) @ cc)
    null = np.empty(n_perm)
    for i in range(n_perm):
        p = rng.permutation(s)
        null[i] = float((p - p.mean()) @ cc)
    if alternative_positive:
        return float((np.sum(null >= obs) + 1) / (n_perm + 1))
    return float((np.sum(null <= obs) + 1) / (n_perm + 1))


def synth_signs(cosines, monopole, amplitude, rng):
    """Signs from P(+1|c) = clip(0.5*(1 + monopole + amplitude*c)). The generative model the
    estimand is defined against; clipping is reported by the caller's battery when it binds."""
    p = np.clip(0.5 * (1.0 + monopole + amplitude * np.asarray(cosines)), 0.0, 1.0)
    return np.where(rng.random(p.size) < p, 1.0, -1.0)
