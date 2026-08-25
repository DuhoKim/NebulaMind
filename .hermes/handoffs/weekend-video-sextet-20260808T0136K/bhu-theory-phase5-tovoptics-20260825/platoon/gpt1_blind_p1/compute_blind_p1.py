#!/usr/bin/env python3
"""Blind independent Phase 5b/P1 Thomson-depth calculation.

Reads only the Phase-4 orbit named in BRIEF_GPT1_BLIND_P1.md.  It does not
read any prior Phase-5 optical-depth implementation or receipt.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
PHASE4 = HERE.parents[2] / "bhu-theory-phase4-anisotropy-20260823" / "a1_results.csv"

W_VALUES = (0.001, 0.05, 0.2456, 0.30)
FB_VALUES = (1.0, 0.1, 0.01)
YE_VALUES = (1.0, 0.5)  # bracket: ionized H to one electron per two baryon masses
TCRIT_S = 4.35e17
SIGMA_T_M2 = 6.6524587321e-29
C_M_S = 299792458.0
G_SI = 6.67430e-11
M_P_KG = 1.67262192595e-27


def crossing_row(path: Path) -> tuple[int, dict[str, float], float]:
    """Return row minimizing |2 - 2 sqrt(t)(1+sqrtN)|."""
    best = None
    with path.open(newline="") as f:
        for line, raw in enumerate(csv.DictReader(f), start=2):
            row = {k: float(v) for k, v in raw.items()}
            residual = abs(2.0 - 2.0 * math.sqrt(row["t_over_tcrit"])
                           * (1.0 + row["sqrtN_hubble_lengths"]))
            if best is None or residual < best[0]:
                best = (residual, line, row)
    assert best is not None
    residual, line, row = best
    return line, row, residual


def integrate_geometry(w: float, ns: float, v: float) -> dict[str, float]:
    """Integrate y=r/r_s and K=I/(rho_s r_s) using z=sqrt(N-1).

    Closure gives rho/rho_s = [(N-1)/(N_s-1)]^alpha.  The z variable
    removes the explicit 1/sqrt(N-1) optical-depth endpoint factor.
    """
    if w <= 0:
        raise ValueError("This constant-w closure reduction requires w>0")
    alpha = (1.0 + w) / (2.0 * w)
    zs = math.sqrt(ns - 1.0)
    c_rho = 3.0 * v * ns  # kappa rho_s r_s^2

    def rhs(z: float, state: np.ndarray) -> list[float]:
        y, _k = state
        n = 1.0 + z*z
        # Written this way to underflow safely (rather than overflow) at small z.
        f = 0.0 if z == 0.0 else math.exp(2.0 * alpha * math.log(z / zs))
        denom = n / y + c_rho * w * y * f
        dydz = -2.0 * z / denom
        # dK/dz = (rho/rho_s)/z * dy/dz; cancel z analytically.
        dkdz = -2.0 * f / denom
        return [dydz, dkdz]

    sol = solve_ivp(rhs, (zs, 0.0), (1.0, 0.0), method="DOP853",
                    rtol=2e-12, atol=2e-14)
    if not sol.success:
        raise RuntimeError(sol.message)
    y_h, k = map(float, sol.y[:, -1])
    return {"alpha": alpha, "r_h_over_r_s": y_h, "K": k,
            "nfev": float(sol.nfev)}


def cutoff_check(w: float, ns: float, v: float) -> list[tuple[float, float]]:
    """Return truncated K(z_min) to demonstrate endpoint convergence."""
    alpha = (1.0 + w) / (2.0 * w)
    zs = math.sqrt(ns - 1.0)
    c_rho = 3.0 * v * ns

    def rhs(z: float, state: np.ndarray) -> list[float]:
        y, _k = state
        f = math.exp(2.0 * alpha * math.log(z / zs))
        denom = (1.0 + z*z) / y + c_rho * w * y * f
        return [-2.0*z/denom, -2.0*f/denom]

    out = []
    for qmin in (1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12):
        sol = solve_ivp(rhs, (zs, math.sqrt(qmin)), (1.0, 0.0),
                        method="DOP853", rtol=2e-12, atol=2e-14)
        if not sol.success:
            raise RuntimeError(sol.message)
        out.append((qmin, float(sol.y[1, -1])))
    return out


def main() -> None:
    line, row, residual = crossing_row(PHASE4)
    ns = row["N"]
    sqrt_ns = row["sqrtN_hubble_lengths"]
    v = row["v_rhobar_over_rho"]
    u = row["u_pbar_over_rho"]
    tratio = row["t_over_tcrit"]
    t_s = tratio * TCRIT_S

    # rho_s r_s = 3 v sqrt(N_s)/(16 pi t_s), in inverse seconds.
    rho_r = 3.0 * v * sqrt_ns / (16.0 * math.pi * t_s)
    tau_prefactor_s = SIGMA_T_M2 * C_M_S / (G_SI * M_P_KG)

    rows = []
    geoms = {}
    for w in W_VALUES:
        geom = integrate_geometry(w, ns, v)
        geoms[w] = geom
        i_s_inv = geom["K"] * rho_r
        j_tcrit = i_s_inv * TCRIT_S
        electron_column_ye1_fb1_m2 = C_M_S * i_s_inv / (G_SI * M_P_KG)
        for fb in FB_VALUES:
            rows.append({
                "w": w, "f_b": fb, "alpha": geom["alpha"],
                "r_h_over_r_s": geom["r_h_over_r_s"],
                "K_I_over_rhos_rs": geom["K"],
                "tcrit_times_Irho": j_tcrit,
                "Irho_s^-1": i_s_inv,
                "Ne_m^-2_Ye1": fb * electron_column_ye1_fb1_m2,
                "tau_Ye1": fb * tau_prefactor_s * i_s_inv,
                "tau_Ye0.5": 0.5 * fb * tau_prefactor_s * i_s_inv,
            })

    out_csv = HERE / "p1_optical_depth.csv"
    with out_csv.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    checks = []
    for w in W_VALUES:
        for qmin, kval in cutoff_check(w, ns, v):
            checks.append({"w": w, "Nminus1_cutoff": qmin,
                           "K_truncated": kval,
                           "fraction_of_endpoint_value": kval/geoms[w]["K"]})
    with (HERE / "p1_convergence.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(checks[0]))
        writer.writeheader()
        writer.writerows(checks)

    print(f"selected Phase-4 line={line}, residual={residual:.12g}")
    print(f"N_s={ns:.12g}, sqrtN={sqrt_ns:.12g}, u/v={u/v:.12g}, t/tcrit={tratio:.12g}")
    print(f"t_s={t_s:.12g} s, rho_s*r_s={rho_r:.12g} s^-1")
    print(f"tau prefactor sigma_T*c/(G*m_p)={tau_prefactor_s:.12g} s")
    print(f"w=0.2456, fb=Ye=1: tau={next(r['tau_Ye1'] for r in rows if r['w']==0.2456 and r['f_b']==1.0):.12g}")
    print(f"w=0.2456 endpoint K={geoms[0.2456]['K']:.12g}, r_h/r_s={geoms[0.2456]['r_h_over_r_s']:.12g}")
    print(f"w=0.2456 cutoff fractions: {[f'{r[1]:.12g}' for r in cutoff_check(0.2456,ns,v)]}")
    print(f"wrote {out_csv}")


if __name__ == "__main__":
    main()
