#!/usr/bin/env python3
"""Independent Phase-B blind implementation from the preregistration and amendments."""

import time
from pathlib import Path

import healpy as hp
import numpy as np
from numpy.polynomial.legendre import leggauss


NSIDE = 64
LMAX = 3 * NSIDE - 1
FWHM = np.deg2rad(160.0 / 60.0)
NMC = 500
ROW_SEEDS = {
    "lcdm": 731_021,
    "A_2pi": 731_022,
    "A_pi": 731_023,
    "B_spliced": 731_024,
    "B_nosplice": 731_025,
}
ROWS = tuple(ROW_SEEDS)


def remove_monopole_dipole(m, good, design):
    """Fit [monopole,x,y,z] on good pixels and subtract it everywhere."""
    beta, *_ = np.linalg.lstsq(design, m[good], rcond=None)
    out = m.copy()
    x, y, z = hp.pix2vec(NSIDE, np.arange(len(m)))
    out -= beta[0] + beta[1] * x + beta[2] * y + beta[3] * z
    return out


def bin_legendre_integrals(edges_deg, lmax):
    """Integral of P_l(x) over each angular bin (constant factors cancel)."""
    # For theta=[a,b], x runs [cos(b),cos(a)].  High-order GL is effectively
    # exact for the degree-191 polynomials and avoids endpoint recurrences.
    qx, qw = leggauss(256)
    ans = np.empty((len(edges_deg) - 1, lmax + 1))
    for k, (a, b) in enumerate(zip(edges_deg[:-1], edges_deg[1:])):
        lo, hi = np.cos(np.deg2rad(b)), np.cos(np.deg2rad(a))
        x = (hi - lo) * qx / 2 + (hi + lo) / 2
        ans[k] = (hi - lo) / 2 * np.polynomial.legendre.legvander(x, lmax).T @ qw
    return ans


def main():
    here = Path(__file__).resolve().parent
    t0 = time.time()

    # Explicit ordering makes the NESTED Planck inputs unambiguous.
    mask_hi = hp.read_map(
        here / "planck_data/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits",
        field=0, nest=True, dtype=np.float32, verbose=False,
    )
    mask_low = hp.ud_grade(mask_hi, NSIDE, order_in="NESTED", order_out="RING")
    del mask_hi
    good = mask_low > 0.9
    mask = good.astype(float)
    fsky = good.mean()

    pix = np.flatnonzero(good)
    vx, vy, vz = hp.pix2vec(NSIDE, pix)
    design = np.column_stack((np.ones(len(pix)), vx, vy, vz))

    data_hi = hp.read_map(
        here / "planck_data/COM_CMB_IQU-smica_2048_R3.00_full.fits",
        field=0, nest=True, dtype=np.float32, verbose=False,
    )
    data = hp.ud_grade(data_hi, NSIDE, order_in="NESTED", order_out="RING") * 1e6
    del data_hi
    data = hp.smoothing(data, fwhm=FWHM, lmax=LMAX, iter=0, verbose=False)
    data = remove_monopole_dipole(data, good, design)

    edges = np.arange(0.0, 180.0 + 3.0, 3.0)
    centers = (edges[:-1] + edges[1:]) / 2
    pint = bin_legendre_integrals(edges, LMAX)
    ell = np.arange(LMAX + 1)
    factor = (2 * ell + 1) / (4 * np.pi)
    denom = pint @ (factor * hp.anafast(mask, lmax=LMAX, iter=0))
    gx, gw = leggauss(256)
    quad_x = 0.75 * gx - 0.25
    quad_w = 0.75 * gw
    quad_theta = np.rad2deg(np.arccos(quad_x))

    def statistic(sky):
        cl = hp.anafast(mask * sky, lmax=LMAX, iter=0)
        chat = (pint @ (factor * cl)) / denom
        # Fixed 256-node Gauss-Legendre quadrature on x in [-1, 1/2].
        ci = np.interp(quad_theta, centers, chat)
        return np.sum(quad_w * ci * ci)

    obs = statistic(data)
    models = np.load(here / "phaseB_model_cls.npz", allow_pickle=False)

    print("Independent Phase-B blind cut-sky S_1/2")
    print(f"nside={NSIDE} lmax={LMAX} bins=3 deg FWHM=160 arcmin")
    print("Implementation choices: harmonic evaluation of exact 3-degree bin-integrated pair sums;")
    print("  256-point Gauss-Legendre quadrature; linear interpolation from bin centers.")
    print(f"f_sky={fsky:.8f} ({good.sum()}/{good.size})")
    print(f"S_1/2_obs={obs:.9g} uK^4")
    if not (1000.0 <= obs <= 1300.0):
        print("C2_STOP: observed value is outside the preregistered literature range [1000,1300] uK^4.")
        return

    print(f"MC n_per_row={NMC}")
    print("seed policy: NumPy legacy RNG reset once per row; each listed seed starts that row's stream")
    print("row seed median_uK4 p05_uK4 P_le_obs")
    beam = hp.gauss_beam(FWHM, lmax=LMAX)
    for name in ROWS:
        seed = ROW_SEEDS[name]
        np.random.seed(seed)
        cl = np.asarray(models[name], float)[: LMAX + 1]
        vals = np.empty(NMC)
        for i in range(NMC):
            alm = hp.synalm(cl, lmax=LMAX, new=True)
            sky = hp.alm2map(hp.almxfl(alm, beam), NSIDE, lmax=LMAX, verbose=False)
            sky = remove_monopole_dipole(sky, good, design)
            vals[i] = statistic(sky)
        print(f"{name} {seed} {np.median(vals):.9g} {np.percentile(vals, 5):.9g} {np.mean(vals <= obs):.6f}")
    print(f"elapsed_seconds={time.time() - t0:.3f}")


if __name__ == "__main__":
    main()
