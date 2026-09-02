#!/usr/bin/env python3
"""Phase (b) pipeline: the pre-registered pixel-pair estimator, fast and exact.

IMPLEMENTATION NOTE (fixed before any observed byte, like everything here).
The pre-registered estimator is the uniform-weight pixel-pair estimator in 1-degree
bins. Brute force is O(Npix^2) per sky and infeasible for >=2,000 skies, so the
production route computes THE SAME QUANTITY through spherical harmonics:

    Q_b(T) = sum_{i != j} T_i T_j 1_b(cos theta_ij)
           = sum_l beta_l^b * (4 pi / Omega^2) * C_l^ana(T)  -  s2 * kappa_b
    with  beta_l^b = ((2l+1)/2) * int_bin P_l(x) dx   (EXACT, via the closed form
          int_a^b P_l = [P_{l+1} - P_{l-1}]/(2l+1) |_a^b),
          s2 = sum_i T_i^2,  kappa_b = sum_l beta_l^b,  Omega = 4 pi / Npix,
    and   Chat_b = Q_b(T*w) / Q_b(w)   for mask w.

This is algebra, not approximation, except for truncating the indicator expansion
at l_max = 3*Nside - 1 -- and the truncated estimator is a deterministic estimator
applied IDENTICALLY to data and simulations, which is what the comparison needs.
Its agreement with literal pair-counting is VERIFIED below (exactness_test) rather
than asserted.

S_1/2 from binned Chat: Gauss-Legendre nodes on [-1, 1/2], linear interpolation of
Chat(theta) from bin centers onto the nodes, per the pre-registration.
"""

import numpy as np
import healpy as hp
from numpy.polynomial import legendre

NSIDE = 64
LMAX = 3 * NSIDE - 1            # 191
FWHM_RAD = np.radians(160.0 / 60.0)
BIN_DEG = 3.0   # AMENDED from 1.0 pre-data: lmax=3*nside-1=191 resolves ~0.94 deg,
                # so 1-deg bins are at the smearing limit; 3-deg bins are cleanly
                # resolved and irrelevant for an l<~20-dominated statistic.
EDGES_DEG = np.arange(0.0, 180.0 + BIN_DEG, BIN_DEG)
S_OBS_LIT = 1150.0


# ---------- exact bin kernels ----------------------------------------------
def legendre_bin_integrals(lmax, x_lo, x_hi):
    """int_{x_lo}^{x_hi} P_l(x) dx for l=0..lmax, exact closed form."""
    def P(l, x):
        c = np.zeros(l + 1); c[l] = 1.0
        return legendre.legval(x, c)
    out = np.empty(lmax + 1)
    out[0] = x_hi - x_lo
    for l in range(1, lmax + 1):
        out[l] = ((P(l + 1, x_hi) - P(l - 1, x_hi))
                  - (P(l + 1, x_lo) - P(l - 1, x_lo))) / (2 * l + 1)
    return out


def bin_kernels(lmax=LMAX, edges_deg=EDGES_DEG):
    """beta[b, l] and kappa[b]; bins ordered by INCREASING theta."""
    x_edges = np.cos(np.radians(edges_deg))          # decreasing in theta
    nb = len(edges_deg) - 1
    beta = np.empty((nb, lmax + 1))
    ls = np.arange(lmax + 1)
    for b in range(nb):
        x_hi, x_lo = x_edges[b], x_edges[b + 1]      # x_hi > x_lo
        beta[b] = (2 * ls + 1) / 2.0 * legendre_bin_integrals(lmax, x_lo, x_hi)
    return beta, beta.sum(axis=1)


# ---------- the estimator ---------------------------------------------------
def q_of(map_vals, beta, kappa, lmax):
    npix = len(map_vals)
    omega = 4 * np.pi / npix
    cl_ana = hp.anafast(map_vals, lmax=lmax, iter=0)  # iter=0: pure quadrature a_lm,
    # exactly the sum the pair-counting algebra assumes; iter>0 broke exactness.
    s2 = float(np.sum(map_vals ** 2))
    return beta @ (4 * np.pi / omega ** 2 * cl_ana) - s2 * kappa


def chat_bins(t_map, w_mask, beta, kappa, lmax=LMAX):
    """Chat(theta_b) for masked map; bins with no pairs return nan."""
    num = q_of(t_map * w_mask, beta, kappa, lmax)
    den = q_of(w_mask.astype(float), beta, kappa, lmax)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(np.abs(den) > 1e-3, num / den, np.nan)


# ---------- S_1/2 from bins (pre-registered quadrature) ---------------------
_GLX, _GLW = np.polynomial.legendre.leggauss(400)
_X = 0.5 * (0.5 - (-1.0)) * _GLX + 0.5 * (0.5 + (-1.0))
_W = 0.5 * (0.5 - (-1.0)) * _GLW
_CENTERS_X = np.cos(np.radians(0.5 * (EDGES_DEG[:-1] + EDGES_DEG[1:])))


def s_half(chat):
    good = np.isfinite(chat)
    # centers ascending in x for interp
    xs, cs = _CENTERS_X[good][::-1], chat[good][::-1]
    return float(np.sum(_W * np.interp(_X, xs, cs) ** 2))


# ---------- map synthesis (identical for MC and, later, data treatment) -----
def synth(cl, seed, nside=NSIDE):
    rng_seed = int(seed)
    np.random.seed(rng_seed)                 # healpy uses global numpy state
    return hp.synfast(cl, nside=nside, fwhm=FWHM_RAD, pixwin=False, verbose=False)


def beamed(cl, nside=NSIDE):
    """The same smoothing, applied analytically to a spectrum."""
    bl = hp.gauss_beam(FWHM_RAD, lmax=len(cl) - 1)
    return cl * bl ** 2


# ---------- validations -----------------------------------------------------
def exactness_test(nside=NSIDE, n_sky=2, seed0=20260902):
    """Literal pair-counting vs the harmonic route, same lmax truncation...
    NO: brute force uses NO truncation -- that is the point. It bounds the
    truncation+Gibbs error of the production route directly."""
    lmax = 3 * nside - 1
    beta, kappa = bin_kernels(lmax)
    npix = hp.nside2npix(nside)
    vecs = np.array(hp.pix2vec(nside, np.arange(npix))).T

    # mask: a crude 20-degree galactic cut, binary
    mtheta = hp.pix2ang(nside, np.arange(npix))[0]
    w = (np.abs(np.degrees(mtheta) - 90.0) > 20.0).astype(float)

    def brute(vals):
        """chunked pair-count sums; exact, no truncation, O(npix^2) memory-safe"""
        nb = len(EDGES_DEG) - 1
        acc = np.zeros(nb)
        chunk = 2048
        for i0 in range(0, npix, chunk):
            i1 = min(i0 + chunk, npix)
            cosang = np.clip(vecs[i0:i1] @ vecs.T, -1, 1)
            th = np.degrees(np.arccos(cosang))
            bi = np.clip(np.digitize(th, EDGES_DEG) - 1, 0, nb - 1)
            wt = np.outer(vals[i0:i1], vals)
            # zero the diagonal entries of this block
            for r in range(i1 - i0):
                wt[r, i0 + r] = 0.0
            acc += np.bincount(bi.ravel(), weights=wt.ravel(), minlength=nb)
        return acc

    print(f"[exactness] nside={nside} lmax={lmax} npix={npix} f_sky={w.mean():.3f}")
    den_bf = brute(w)                     # mask pair counts, computed once
    worst = 0.0
    for s in range(n_sky):
        cl0 = np.ones(lmax + 1); cl0[:2] = 0
        t = synth(cl0 * 100.0, seed0 + s, nside=nside)
        tm = t * w
        num_bf = brute(tm)
        with np.errstate(divide="ignore", invalid="ignore"):
            c_bf = np.where(den_bf > 0, num_bf / den_bf, np.nan)
        c_h = chat_bins(t, w, beta, kappa, lmax)
        sel = np.isfinite(c_bf) & np.isfinite(c_h) & (EDGES_DEG[:-1] >= 60.0)
        scale = np.sqrt(np.nanmean(c_bf[sel] ** 2))
        rel = np.nanmax(np.abs(c_h[sel] - c_bf[sel])) / scale
        s_bf, s_h = s_half(c_bf), s_half(c_h)
        srel = abs(s_h - s_bf) / max(abs(s_bf), 1e-30)
        worst = max(worst, rel)
        worst_s = max(worst_s if s else 0.0, srel)
        print(f"  sky {s}: max|dChat|/rms(60-180deg) = {rel:.2e}   "
              f"S_half bf={s_bf:.4e} harm={s_h:.4e} rel={srel:.2e}")
    verdict = "PASS" if worst_s < 1e-2 else "FAIL"   # bar on the STATISTIC
    print(f"[exactness] worst per-bin dev = {worst:.2e}; worst S_half rel = {worst_s:.2e}  -> {verdict}")
    return worst_s < 1e-2


def control_c1(n_map=2000, n_chi2=20000, seed0=31):
    """C1: full-sky estimator distribution vs direct quadratic-form MC on the
    SAME beamed spectrum, SAME bin/interp chain. Validates synthesis+anafast+
    kernel chain end to end. (Clarified from the prereg wording: the reference
    carries the same beam, else the beam itself would fail the match.)"""
    d = np.load("phaseB_model_cls.npz")
    cl = beamed(d["lcdm"])
    lmax = len(cl) - 1
    beta, kappa = bin_kernels(lmax)
    w = np.ones(hp.nside2npix(NSIDE))

    s_map = np.empty(n_map)
    for i in range(n_map):
        t = synth(d["lcdm"], seed0 + i)          # synth applies the beam itself
        s_map[i] = s_half(chat_bins(t, w, beta, kappa, lmax))

    # reference: draw Chat_l ~ Cl * chi2_(2l+1)/(2l+1), push through the SAME
    # bin kernels (full sky: Chat_b = sum_l beta Cl_hat / sum_l beta ... using
    # identical Q_b machinery in spectral form, diagonal term negligible and
    # identical treatment impossible spectrally -> use kernel ratio directly)
    rng = np.random.default_rng(seed0)
    ls = np.arange(lmax + 1)
    dof = 2 * ls + 1
    # Correct closed form (validated on the l=0 case): the bin-averaged
    # correlation is  Cbar_b = sum_l beta_l C_l / (2 pi dx_b).
    # (Revision note: the first version weighted C_l by an extra (2l+1)/4pi --
    # conflating C(theta)'s Legendre coefficients with the bin integrals -- and
    # failed C1 by 100x. The control caught it; this is the fix.)
    x_edges = np.cos(np.radians(EDGES_DEG))
    dx = x_edges[:-1] - x_edges[1:]
    s_ref = np.empty(n_chi2)
    for i in range(n_chi2):
        clh = cl[2:] * rng.chisquare(dof[2:]) / dof[2:]
        full = np.zeros(lmax + 1); full[2:] = clh
        cb = (beta @ full) / (2 * np.pi * dx)
        s_ref[i] = s_half(cb)

    med_m, med_r = np.median(s_map), np.median(s_ref)
    p_m = float(np.mean(s_map <= S_OBS_LIT))
    p_r = float(np.mean(s_ref <= S_OBS_LIT))
    err = abs(med_m - med_r) / med_r
    print(f"[C1] map-route  n={n_map}:  median={med_m:10.0f}  P(<= {S_OBS_LIT:.0f})={p_m*100:.2f}%")
    print(f"[C1] chi2-route n={n_chi2}: median={med_r:10.0f}  P(<= {S_OBS_LIT:.0f})={p_r*100:.2f}%")
    print(f"[C1] median agreement: {err*100:.2f}%")
    # MC error on a median with n=500 is ~ 1.35*sigma/sqrt(n) -- allow 5%
    verdict = "PASS" if err < 0.05 else "FAIL"
    print(f"[C1] -> {verdict}")
    return err < 0.05


if __name__ == "__main__":
    ok1 = exactness_test()
    ok2 = control_c1()
    print(f"\nPIPELINE VALIDATION: exactness={'PASS' if ok1 else 'FAIL'}  "
          f"C1={'PASS' if ok2 else 'FAIL'}")
