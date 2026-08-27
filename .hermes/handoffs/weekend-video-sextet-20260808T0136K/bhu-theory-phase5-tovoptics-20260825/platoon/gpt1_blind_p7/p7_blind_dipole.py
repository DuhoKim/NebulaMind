#!/usr/bin/env python3
"""Blind independent search for the signed crossing-imprint dipole.

Reads only the orbit table named in BRIEF_GPT1_BLIND_P7.md.  It writes all
products beside this script; no other project artifact is read or modified.
"""
from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
DATA = HERE.parent.parent.parent / "bhu-theory-phase4-anisotropy-20260823" / "a1_results.csv"
T0_K = 2.7255
DIPOLE_LIMIT_K = 3.7e-3
W_MIN, W_MAX = 0.005, 0.999


@dataclass(frozen=True)
class Rays:
    mu: np.ndarray
    weight: np.ndarray
    eta: np.ndarray
    q: np.ndarray
    beta: np.ndarray
    gamma: np.ndarray
    rho: np.ndarray
    eta_center: float
    r_center: float


class Orbit:
    def __init__(self, path: Path = DATA):
        d = pd.read_csv(path)
        eta = 2.0 * np.sqrt(d["t_over_tcrit"].to_numpy(float))
        if not np.all(np.diff(eta) > 0):
            raise ValueError("orbit time is not strictly increasing")
        self.eta_lo, self.eta_hi = float(eta[0]), float(eta[-1])
        self.sqrt_n = PchipInterpolator(eta, d["sqrtN_hubble_lengths"].to_numpy(float))
        self.v = PchipInterpolator(eta, d["v_rhobar_over_rho"].to_numpy(float))
        self.eta_center = brentq(
            lambda e: e * float(self.sqrt_n(e)) - (2.0 - e),
            self.eta_lo,
            self.eta_hi,
            xtol=2e-14,
            rtol=4*np.finfo(float).eps,
        )
        self.r_center = 2.0 - self.eta_center

    def rstar(self, eta: float | np.ndarray) -> float | np.ndarray:
        return eta * self.sqrt_n(eta)

    def rho_bar(self, eta: float | np.ndarray) -> float | np.ndarray:
        # t=(eta/2)^2 and rho_FRW=3/(32*pi*t^2)=3/(2*pi*eta^4)
        return self.v(eta) * 3.0 / (2.0 * np.pi * np.asarray(eta)**4)

    def rays(self, order: int, offset_fraction: float, crossing_xtol: float = 2e-13) -> Rays:
        mu, weight = leggauss(order)
        x = offset_fraction * self.r_center
        etas = np.empty(order)
        qs = np.empty(order)
        for i, m in enumerate(mu):
            def residual(chi: float) -> float:
                eta = 2.0 - chi
                radius = np.sqrt(x*x + chi*chi + 2.0*x*chi*m)
                return float(radius - self.rstar(eta))
            chi = brentq(
                residual, 0.0, 2.0-self.eta_lo,
                xtol=crossing_xtol,
                rtol=4*np.finfo(float).eps,
            )
            eta = 2.0 - chi
            radius = float(self.rstar(eta))
            etas[i] = eta
            # n dot outward radial unit vector at the crossing.
            qs[i] = (chi + x*m) / radius
        sqrt_n = self.sqrt_n(etas)
        beta = 1.0 / sqrt_n
        gamma = 1.0 / np.sqrt(1.0-beta*beta)
        return Rays(mu, weight, etas, qs, beta, gamma, self.rho_bar(etas),
                    self.eta_center, self.r_center)


def source_log_temperature(rays: Rays, orbit: Orbit, w: float, rtol: float) -> np.ndarray:
    """Adiabatically integrate d ln(T)/d eta = w/(1+w) d ln(rho)/d eta.

    The IVP is deliberately used rather than replacing the result by the
    closed-form endpoint ratio, so integrator-tolerance stability is testable.
    """
    power = w/(1.0+w)
    lo = min(float(np.min(rays.eta)), rays.eta_center)
    hi = max(float(np.max(rays.eta)), rays.eta_center)

    def rhs(e: float, _y: np.ndarray) -> np.ndarray:
        v = float(orbit.v(e))
        dlnrho = float(orbit.v.derivative()(e))/v - 4.0/e
        return np.array([power*dlnrho])

    # One solve in each direction from the centered crossing avoids crossing
    # the initial point while preserving a single physical normalization.
    vals = np.empty_like(rays.eta)
    center_logrho = np.log(float(orbit.rho_bar(rays.eta_center)))
    for forward in (False, True):
        mask = rays.eta < rays.eta_center if not forward else rays.eta >= rays.eta_center
        if not np.any(mask):
            continue
        end = lo if not forward else hi
        sol = solve_ivp(
            rhs, (rays.eta_center, end), [power*center_logrho],
            rtol=rtol, atol=max(1e-14, rtol*1e-3), dense_output=True,
            method="DOP853",
        )
        if not sol.success:
            raise RuntimeError(sol.message)
        vals[mask] = sol.sol(rays.eta[mask])[0]
    return vals


def signed_coefficient(
    w: float,
    rays: Rays,
    orbit: Orbit,
    offset_fraction: float,
    integrator_rtol: float,
) -> float:
    # Inside the horizon the future-directed comoving exterior is along
    # decreasing areal radius.  With q defined for the outward sight line,
    # the exterior-to-FRW junction frequency factor is gamma*(1+beta*q).
    doppler = rays.gamma * (1.0 + rays.beta*rays.q)
    log_tsrc = source_log_temperature(rays, orbit, w, integrator_rtol)
    log_beam_t = np.log(doppler) + log_tsrc

    # Bolometric transfer: I is proportional to (D*T_source)^4.  Intensities
    # are normalized first; their fourth root is the temperature observable.
    shift = float(np.max(4.0*log_beam_t))
    intensity = np.exp(4.0*log_beam_t-shift)
    imean = 0.5*np.dot(rays.weight, intensity)
    theta = (intensity/imean)**0.25
    tmean = 0.5*np.dot(rays.weight, theta)
    theta /= tmean
    a1 = 1.5*np.dot(rays.weight, rays.mu*theta)
    return float(a1/offset_fraction)


def root_and_interval(orbit: Orbit, order: int, eps: float, rtol: float):
    rays = orbit.rays(order, eps)
    cache: dict[float, float] = {}
    def c(w: float) -> float:
        key = float(w)
        if key not in cache:
            cache[key] = signed_coefficient(key, rays, orbit, eps, rtol)
        return cache[key]

    scan_w = np.linspace(W_MIN, W_MAX, 401)
    scan_c = np.array([c(float(w)) for w in scan_w])
    brackets = [(float(a), float(b)) for a,b,ca,cb in zip(scan_w[:-1],scan_w[1:],scan_c[:-1],scan_c[1:]) if ca*cb < 0]
    if len(brackets) != 1:
        raise RuntimeError(f"expected a uniquely bracketed signed null, got {brackets}")
    root = brentq(c, *brackets[0], xtol=2e-13, rtol=1e-12)
    threshold = DIPOLE_LIMIT_K/T0_K
    left = brentq(lambda w: c(w)-threshold, W_MIN, root, xtol=2e-13, rtol=1e-12)
    right = brentq(lambda w: c(w)+threshold, root, W_MAX, xtol=2e-13, rtol=1e-12)
    return rays, c, root, left, right, threshold, scan_c


def run(args: argparse.Namespace) -> None:
    orbit = Orbit(args.data)
    rays, coeff, root, left, right, threshold, scan_c = root_and_interval(
        orbit, args.order, args.offset, args.rtol
    )

    # Inclusive 0.001 grid plus exact interval edges and root.
    ws = list(np.round(np.arange(W_MIN, W_MAX+0.0005, 0.001), 6))
    ws.extend([left, root, right])
    ws = sorted(set(float(w) for w in ws if W_MIN <= w <= W_MAX))
    table_path = HERE / "signed_dipole_vs_w.csv"
    with table_path.open("w", newline="") as f:
        out = csv.writer(f)
        out.writerow(["w", "signed_temperature_dipole_coefficient_per_xoff_over_rcenter"])
        for w in ws:
            out.writerow([f"{w:.12f}", f"{coeff(w):.12e}"])

    stability = {"quadrature": [], "offset": [], "integrator_rtol": []}
    for order in (32, 64, 128, 256):
        _, _, rr, ll, uu, _, _ = root_and_interval(orbit, order, args.offset, args.rtol)
        stability["quadrature"].append({"order": order, "root_w": rr, "left_w": ll, "right_w": uu})
    for eps in (1e-3, 3e-4, 1e-4, 3e-5):
        _, _, rr, ll, uu, _, _ = root_and_interval(orbit, args.order, eps, args.rtol)
        stability["offset"].append({"xoff_over_rcenter": eps, "root_w": rr, "left_w": ll, "right_w": uu})
    for tol in (1e-8, 1e-10, 1e-12):
        _, _, rr, ll, uu, _, _ = root_and_interval(orbit, args.order, args.offset, tol)
        stability["integrator_rtol"].append({"rtol": tol, "root_w": rr, "left_w": ll, "right_w": uu})

    result = {
        "data": str(args.data.resolve()),
        "eta_center": orbit.eta_center,
        "r_center": orbit.r_center,
        "sqrtN_center": float(orbit.sqrt_n(orbit.eta_center)),
        "beta_center": float(1.0/orbit.sqrt_n(orbit.eta_center)),
        "quadrature_order": args.order,
        "xoff_over_rcenter": args.offset,
        "integrator_rtol": args.rtol,
        "root_w": root,
        "unconstrainable_left_w": left,
        "unconstrainable_right_w": right,
        "unconstrainable_width_w": right-left,
        "threshold_abs_coefficient": threshold,
        "scan_min_coefficient": float(np.min(scan_c)),
        "scan_max_coefficient": float(np.max(scan_c)),
        "stability": stability,
    }
    (HERE/"results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--data", type=Path, default=DATA)
    p.add_argument("--order", type=int, default=128)
    p.add_argument("--offset", type=float, default=1e-4)
    p.add_argument("--rtol", type=float, default=1e-10)
    return p.parse_args()


if __name__ == "__main__":
    run(parse_args())
