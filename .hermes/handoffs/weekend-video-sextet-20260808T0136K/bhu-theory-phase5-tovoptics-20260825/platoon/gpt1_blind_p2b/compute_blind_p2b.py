#!/usr/bin/env python3
"""Blind Phase-5b P2b computation using only the brief and gated A1 orbit CSV."""
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss, legval
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

T0_K = 2.7255
DIPOLE_LIMIT_K = 3.7e-3
TAU_MAX = 0.15
ETA_OBS = 2.0                 # t_obs/t_crit = 1
SLOPE_EPS = (1e-3, 5e-4, 2e-4, 1e-4)


def load_orbit(path: Path, stride: int = 1):
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    t = np.asarray([float(r["t_over_tcrit"]) for r in rows])[::stride]
    sqn = np.asarray([float(r["sqrtN_hubble_lengths"]) for r in rows])[::stride]
    eta = 2.0 * np.sqrt(t)
    # Shape-preserving interpolation avoids splines overshooting beta=1/sqrtN.
    return eta, PchipInterpolator(eta, sqn, extrapolate=True)


def crossing_eta(mu: float, xoff: float, sqn, eta_min: float, eta_obs: float = ETA_OBS):
    """Solve |x_off + chi*n| = eta_c*sqrtN(eta_c), chi=eta_obs-eta_c."""
    def residual(eta_c):
        chi = eta_obs - eta_c
        lhs = math.sqrt(max(0.0, xoff*xoff + chi*chi + 2.0*xoff*chi*mu))
        return lhs - eta_c * float(sqn(eta_c))
    return brentq(residual, eta_min, eta_obs * (1.0 - 1e-10), xtol=2e-14, rtol=2e-14)


def raw_transfer(mu: float, xoff: float, sqn, eta_min: float):
    """FRW propagation times SR frame transfer at the shock.

    n points from observer toward the crossing. The photon propagates along -n.
    c=n.e_r.  For u_FRW=gamma(u_TOV+beta e_r), nu_FRW/nu_TOV=
    gamma(1+beta*c). Radiation-era propagation then contributes eta_c/eta_obs.
    """
    eta_c = crossing_eta(mu, xoff, sqn, eta_min)
    chi = ETA_OBS - eta_c
    radius = eta_c * float(sqn(eta_c))
    c = (xoff * mu + chi) / radius
    beta = 1.0 / float(sqn(eta_c))
    gamma = 1.0 / math.sqrt(1.0 - beta*beta)
    return (eta_c / ETA_OBS) * gamma * (1.0 + beta*c)


def multipoles(epsilon: float, sqn, eta_min: float, rstar0: float, nmu: int = 512, lmax: int = 4):
    mu, w = leggauss(nmu)
    xoff = epsilon * rstar0
    temp = np.asarray([raw_transfer(float(m), xoff, sqn, eta_min) for m in mu])
    mean = 0.5 * np.dot(w, temp)
    delta = temp / mean - 1.0
    coeff = []
    for ell in range(lmax + 1):
        p = legval(mu, [0.0] * ell + [1.0])
        coeff.append((2*ell + 1) * 0.5 * np.dot(w, delta*p))
    return mean, np.asarray(coeff), float(np.max(np.abs(delta)))


def compute(input_csv: Path, output_dir: Path, stride: int = 1):
    eta, sqn = load_orbit(input_csv, stride=stride)
    eta_min = float(eta[0])
    eta0 = brentq(lambda e: ETA_OBS - e - e*float(sqn(e)), eta_min, ETA_OBS*(1-1e-10),
                  xtol=2e-14, rtol=2e-14)
    sqrt_n0 = float(sqn(eta0))
    rstar0 = eta0 * sqrt_n0
    beta0 = 1.0 / sqrt_n0
    f0 = raw_transfer(0.0, 0.0, sqn, eta_min)

    rows = []
    slopes = []
    for eps in SLOPE_EPS:
        mean_p, a_p, max_p = multipoles(eps, sqn, eta_min, rstar0)
        mean_m, a_m, max_m = multipoles(-eps, sqn, eta_min, rstar0)
        odd_slope = (a_p[1] - a_m[1]) / (2.0*eps)
        slopes.append(odd_slope)
        rows.append((eps, mean_p, *a_p, max_p, odd_slope))
    c1 = float(slopes[-1])
    c1_abs = abs(c1)

    frac_limit = DIPOLE_LIMIT_K / T0_K
    # Passive isotropic source bracket: q=S/T_inc in [0,1].  In the maximally
    # diluting placement, W=e^-tau/(e^-tau+(1-e^-tau)q), hence e^-tau<=W<=1.
    w_min = math.exp(-TAU_MAX)
    c_lo, c_hi = w_min*c1_abs, c1_abs
    bound_lo = frac_limit / c_hi
    bound_hi = frac_limit / c_lo

    # Check finite-offset multipoles at the strict and conservative bounds.
    _, a_strict, _ = multipoles(bound_lo, sqn, eta_min, rstar0, nmu=768)
    _, a_cons, _ = multipoles(bound_hi, sqn, eta_min, rstar0, nmu=768)

    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "p2b_results.csv").open("w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["epsilon_xoff_over_rstar0", "mean_raw_transfer", "a0", "a1", "a2", "a3", "a4", "max_abs_delta", "odd_a1_slope"])
        wr.writerows(rows)

    summary = {
        "eta_cross_center": eta0,
        "t_cross_center_over_tcrit": eta0*eta0/4.0,
        "sqrtN_cross_center": sqrt_n0,
        "beta_cross_center": beta0,
        "rstar_center": rstar0,
        "raw_common_transfer_center": f0,
        "fractional_dipole_limit": frac_limit,
        "a1_per_xoff_over_rstar_pre_source": c1,
        "abs_a1_coefficient_source_range_min": c_lo,
        "abs_a1_coefficient_source_range_max": c_hi,
        "bound_xoff_over_rstar_min": bound_lo,
        "bound_xoff_over_rstar_max": bound_hi,
        "strict_bound_multipoles_a1_a2_a3_a4": a_strict[1:].tolist(),
        "conservative_bound_multipoles_a1_a2_a3_a4": a_cons[1:].tolist(),
        "slope_sequence": slopes,
        "opacity_weight_range": [w_min, 1.0],
        "orbit_stride": stride,
    }
    with (output_dir / "summary.txt").open("w") as f:
        for k, v in summary.items():
            f.write(f"{k}={v}\n")
    return summary


def main():
    here = Path(__file__).resolve().parent
    default_input = (here / "../../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv").resolve()
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, default=default_input)
    ap.add_argument("--output-dir", type=Path, default=here)
    ap.add_argument("--stride", type=int, default=1)
    args = ap.parse_args()
    summary = compute(args.input.resolve(), args.output_dir.resolve(), args.stride)
    for k, v in summary.items():
        print(f"{k}={v}")


if __name__ == "__main__":
    main()
