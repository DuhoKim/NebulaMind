#!/usr/bin/env python3
"""Blind Phase-5 P5 light-cone, transfer, and multipole computation.

This program intentionally consumes only the orbit CSV named by the P5 brief.
It does not import or inspect any earlier transfer scripts or receipts.
"""
from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

T0_K = 2.7255
DIPOLE_LIMIT_K = 3.7e-3
FRAC_LIMIT = DIPOLE_LIMIT_K / T0_K


@dataclass
class Orbit:
    t: np.ndarray
    sqrtN: np.ndarray
    v: np.ndarray
    log_sqrtN: PchipInterpolator
    log_v: PchipInterpolator

    @classmethod
    def read(cls, path: Path) -> "Orbit":
        data = np.genfromtxt(path, delimiter=",", names=True)
        required = {"t_over_tcrit", "sqrtN_hubble_lengths", "v_rhobar_over_rho"}
        if not required.issubset(data.dtype.names or ()):
            raise ValueError(f"missing required columns: {sorted(required - set(data.dtype.names or ())) }")
        order = np.argsort(data["t_over_tcrit"])
        t = np.asarray(data["t_over_tcrit"][order], float)
        sn = np.asarray(data["sqrtN_hubble_lengths"][order], float)
        v = np.asarray(data["v_rhobar_over_rho"][order], float)
        if np.any(t <= 0) or np.any(sn <= 0) or np.any(v <= 0) or np.any(np.diff(t) <= 0):
            raise ValueError("orbit inputs must be positive with strictly increasing time")
        return cls(t, sn, v, PchipInterpolator(np.log(t), np.log(sn)),
                   PchipInterpolator(np.log(t), np.log(v)))

    def at_eta(self, eta: float) -> tuple[float, float, float]:
        t = (eta / 2.0) ** 2
        # Root-bracket endpoint arithmetic can miss the tabulated endpoint by
        # a few ulps; clip only within a tight relative tolerance.
        tol = 1e-12
        if t < self.t[0] and t >= self.t[0] * (1.0-tol):
            t = float(self.t[0])
        if t > self.t[-1] and t <= self.t[-1] * (1.0+tol):
            t = float(self.t[-1])
        if not (self.t[0] <= t <= self.t[-1]):
            raise ValueError(f"eta gives t={t} outside orbit range")
        sn = math.exp(float(self.log_sqrtN(math.log(t))))
        v = math.exp(float(self.log_v(math.log(t))))
        return t, sn, v

    def radius(self, eta: float) -> float:
        _, sn, _ = self.at_eta(eta)
        return eta * sn


@dataclass
class Crossing:
    eta: float
    chi: float
    t: float
    sqrtN: float
    v: float
    cos_radial: float


def crossing(orbit: Orbit, eta_obs: float, xoff: float, mu: float) -> Crossing:
    """Solve |x_off zhat + chi n| = r_*(eta_obs-chi)."""
    eta_min = 2.0 * math.sqrt(orbit.t[0])
    # Stay just inside the interpolation domain at the upper root bracket.
    chi_max = eta_obs - eta_min * (1.0 + 1e-10)

    def f(chi: float) -> float:
        distance = math.sqrt(max(0.0, xoff*xoff + chi*chi + 2.0*xoff*chi*mu))
        return distance - orbit.radius(eta_obs - chi)

    if f(0.0) >= 0:
        raise ValueError("observer is not strictly inside the shock at eta_obs")
    chi = float(brentq(f, 0.0, chi_max, xtol=2e-14, maxiter=200))
    eta = eta_obs - chi
    t, sn, v = orbit.at_eta(eta)
    r = math.sqrt(max(0.0, xoff*xoff + chi*chi + 2.0*xoff*chi*mu))
    # n dot outward radial unit vector at the crossing.
    c = (chi + xoff*mu) / r
    return Crossing(eta, chi, t, sn, v, c)


def raw_temperature(c: Crossing, tau: float, source_fraction: float) -> float:
    """Dimensionless RJ/thermodynamic temperature before sky normalization.

    Formal transfer: T = D [exp(-tau) T_bg + (1-exp(-tau)) lambda T_ext].
    T_bg is the common crossing-independent CMB scale, T_ext/T_bg=v^(1/4),
    and 0<=lambda<=1 brackets no emissivity through LTE saturation.
    """
    beta = 1.0 / c.sqrtN
    if not (0.0 <= beta < 1.0):
        raise ValueError(f"non-subluminal beta={beta}")
    gamma = 1.0 / math.sqrt(1.0 - beta*beta)
    # Exterior fluid is inward in the local FRW frame; the received ray is inward.
    doppler = gamma * (1.0 + beta*c.cos_radial)
    q = c.v ** 0.25
    e = math.exp(-tau)
    return doppler * (e + (1.0-e)*source_fraction*q)


def multipoles(orbit: Orbit, eta_obs: float, epsilon: float, tau: float,
               source_fraction: float, nquad: int) -> tuple[float, float, float]:
    """Return monopole, normalized Legendre l=1 and l=2 coefficients."""
    mu, weight = np.polynomial.legendre.leggauss(nquad)
    r_obs = orbit.radius(eta_obs)
    xoff = epsilon * r_obs
    temp = np.array([raw_temperature(crossing(orbit, eta_obs, xoff, float(m)),
                                     tau, source_fraction) for m in mu])
    mean = 0.5 * float(np.dot(weight, temp))
    delta = temp / mean - 1.0
    p2 = 0.5 * (3.0*mu*mu - 1.0)
    a1 = 1.5 * float(np.dot(weight, delta*mu))
    a2 = 2.5 * float(np.dot(weight, delta*p2))
    return mean, a1, a2


def tau_grid() -> np.ndarray:
    # Dense near transparency plus explicit saturation points through tau=25.
    return np.unique(np.concatenate((np.linspace(0.0, 1.0, 21),
                                     np.linspace(1.25, 5.0, 16),
                                     np.array([6., 8., 10., 12., 15., 20., 25.]))))


def run(csv_path: Path, outdir: Path, epsilon: float, nquad: int) -> None:
    orbit = Orbit.read(csv_path)
    eta_obs = 2.0 * math.sqrt(float(orbit.t[-1]))
    r_obs = orbit.radius(eta_obs)
    c0 = crossing(orbit, eta_obs, 0.0, 0.0)
    rows = []
    for tau in tau_grid():
        row: dict[str, float] = {"tau": float(tau)}
        for label, lam in (("no_emission_bound", 0.0), ("lte", 1.0)):
            mean, a1, a2 = multipoles(orbit, eta_obs, epsilon, float(tau), lam, nquad)
            c1 = a1 / epsilon
            c2 = a2 / (epsilon*epsilon)
            bound = math.inf if c1 == 0.0 else FRAC_LIMIT / abs(c1)
            row[f"mean_raw_{label}"] = mean
            row[f"dipole_per_xoff_over_robs_{label}"] = c1
            row[f"quadrupole_per_xoff_over_robs_sq_{label}"] = c2
            row[f"bound_xoff_over_robs_{label}"] = bound
        rows.append(row)

    outdir.mkdir(parents=True, exist_ok=True)
    result_path = outdir / "p5_opacity_sweep.csv"
    with result_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    # Independent numerical and physical limiting checks.
    checks = []
    for eps in (2.5e-5, 5e-5, 1e-4, 2e-4):
        _, a1, a2 = multipoles(orbit, eta_obs, eps, 0.0, 1.0, nquad)
        checks.append(("epsilon_convergence_tau0", eps, a1/eps, a2/(eps*eps)))
        _, a1h, a2h = multipoles(orbit, eta_obs, eps, 25.0, 1.0, nquad)
        checks.append(("epsilon_convergence_tau25_lte", eps, a1h/eps, a2h/(eps*eps)))
    for nq in (64, 128, 256, 512):
        _, a1, a2 = multipoles(orbit, eta_obs, epsilon, 1.0, 1.0, nq)
        checks.append(("angular_quadrature_tau1_lte", float(nq), a1/epsilon,
                       a2/(epsilon*epsilon)))
    # Centered sky must be exactly isotropic for every opacity/source choice.
    centered = []
    for tau in (0.0, 1.0, 25.0):
        for lam in (0.0, 1.0):
            _, a1, a2 = multipoles(orbit, eta_obs, 0.0, tau, lam, 64)
            centered.append((tau, lam, a1, a2))

    with (outdir / "p5_checks.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["check", "resolution_parameter", "dipole_coefficient", "quadrupole_coefficient"])
        w.writerows(checks)
        w.writerow([])
        w.writerow(["centered_tau", "source_fraction", "a1", "a2"])
        w.writerows(centered)

    def row_at(tau: float) -> dict[str, float]:
        return min(rows, key=lambda r: abs(r["tau"]-tau))

    summary_lines = [
        "Blind P5 numerical summary",
        f"input_rows={len(orbit.t)}",
        f"t_obs/tcrit={orbit.t[-1]:.12g}",
        f"eta_obs={eta_obs:.12g}",
        f"normalizing_radius_rstar_obs={r_obs:.12g}",
        f"centered_crossing_t/tcrit={c0.t:.12g}",
        f"centered_crossing_sqrtN={c0.sqrtN:.12g}",
        f"centered_crossing_beta={1/c0.sqrtN:.12g}",
        f"centered_crossing_v={c0.v:.12g}",
        f"fractional_dipole_limit={FRAC_LIMIT:.12g}",
        "",
    ]
    for tau in (0.0, 0.15, 1.0, 5.0, 20.0, 25.0):
        r = row_at(tau)
        summary_lines.append(
            f"tau={r['tau']:g}  C1_LTE={r['dipole_per_xoff_over_robs_lte']:.9g}  "
            f"bound_LTE={r['bound_xoff_over_robs_lte']:.9g}  "
            f"C1_noem={r['dipole_per_xoff_over_robs_no_emission_bound']:.9g}  "
            f"bound_noem={r['bound_xoff_over_robs_no_emission_bound']:.9g}")
    (outdir / "summary.txt").write_text("\n".join(summary_lines) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--epsilon", type=float, default=5e-5)
    parser.add_argument("--nquad", type=int, default=256)
    args = parser.parse_args()
    run(args.input, args.outdir, args.epsilon, args.nquad)
