#!/usr/bin/env python3
"""Blind Phase-5 S0 Thomson-depth calculation from the supplied Phase-4 table."""

from __future__ import annotations

import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUT = (
    HERE
    / "../../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv"
).resolve()
OUTPUT = HERE / "s0_optical_depth_vs_tcrit.csv"

# SI constants. c is exact; the remaining values are CODATA/NIST values.
C = 299_792_458.0                 # m s^-1
G = 6.67430e-11                   # m^3 kg^-1 s^-2
SIGMA_T = 6.6524587321e-29        # m^2
M_P = 1.67262192369e-27           # kg


def load_table(path: Path) -> tuple[list[float], list[float], list[float]]:
    rows: list[tuple[float, float, float]] = []
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            x = float(row["t_over_tcrit"])
            sqrt_n = float(row["sqrtN_hubble_lengths"])
            v = float(row["v_rhobar_over_rho"])
            if x > 0.0 and sqrt_n > 0.0 and v > 0.0:
                rows.append((x, sqrt_n, v))
    rows.sort()
    if len(rows) < 2:
        raise RuntimeError("Phase-4 table has fewer than two usable rows")
    return ([r[0] for r in rows], [r[1] for r in rows], [r[2] for r in rows])


def log_interp(x: float, xs: list[float], ys: list[float]) -> float:
    """Linear interpolation in log(x), with no extrapolation."""
    if not xs[0] <= x <= xs[-1]:
        raise ValueError(f"x={x:.17g} outside table [{xs[0]:.17g}, {xs[-1]:.17g}]")
    lo, hi = 0, len(xs) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if xs[mid] <= x:
            lo = mid
        else:
            hi = mid
    if x == xs[lo]:
        return ys[lo]
    if x == xs[hi]:
        return ys[hi]
    q = (math.log(x) - math.log(xs[lo])) / (math.log(xs[hi]) - math.log(xs[lo]))
    return ys[lo] + q * (ys[hi] - ys[lo])


def crossing_solution(
    xs: list[float], sqrt_ns: list[float], vs: list[float]
) -> tuple[float, float, float, float]:
    # eta_obs = eta_e(1+sqrt(N)); for t_obs=t_crit this is
    # f(x)=sqrt(x)*(1+sqrtN(x))-1=0, where x=t_e/t_crit.
    def f(x: float) -> float:
        return math.sqrt(x) * (1.0 + log_interp(x, xs, sqrt_ns)) - 1.0

    brackets: list[tuple[float, float]] = []
    f_prev = f(xs[0])
    for i in range(1, len(xs)):
        f_now = f(xs[i])
        if f_prev == 0.0:
            brackets.append((xs[i - 1], xs[i - 1]))
        elif f_prev * f_now < 0.0:
            brackets.append((xs[i - 1], xs[i]))
        f_prev = f_now
    if not brackets:
        raise RuntimeError("No light-cone crossing root is bracketed by the supplied table")
    if len(brackets) != 1:
        raise RuntimeError(f"Expected one crossing root; found {len(brackets)}")

    lo, hi = brackets[0]
    if lo != hi:
        for _ in range(100):
            mid = math.sqrt(lo * hi)
            if f(lo) * f(mid) <= 0.0:
                hi = mid
            else:
                lo = mid
            if abs(math.log(hi / lo)) < 2e-15:
                break
        x = math.sqrt(lo * hi)
    else:
        x = lo

    sqrt_n = log_interp(x, xs, sqrt_ns)
    v = log_interp(x, xs, vs)
    residual = math.sqrt(x) * (1.0 + sqrt_n) - 1.0
    return x, sqrt_n, v, residual


def tau_prefactor_seconds(x: float, sqrt_n: float, v: float) -> float:
    # rho=3/(32*pi*G*t_e^2) for sigma=1/3; rbar=2*c*t_e*sqrtN.
    # With L_eff=rbar, tau=(sigma_T/m_p)*v*rho*rbar=A/t_crit.
    return (SIGMA_T / M_P) * v * (3.0 * C * sqrt_n) / (16.0 * math.pi * G * x)


def main() -> None:
    xs, sqrt_ns, vs = load_table(INPUT)
    x, sqrt_n, v, residual = crossing_solution(xs, sqrt_ns, vs)
    redshift_factor = 1.0 / math.sqrt(x)
    a_seconds = tau_prefactor_seconds(x, sqrt_n, v)

    anchors = [10.0**k for k in range(0, 21)]
    with OUTPUT.open("w", newline="") as f:
        fieldnames = [
            "tcrit_seconds",
            "t_emit_over_tcrit",
            "sqrtN_at_crossing",
            "v_at_crossing",
            "one_plus_z",
            "tau_thomson",
            "regime",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tcrit in anchors:
            tau = a_seconds / tcrit
            writer.writerow(
                {
                    "tcrit_seconds": f"{tcrit:.10e}",
                    "t_emit_over_tcrit": f"{x:.12e}",
                    "sqrtN_at_crossing": f"{sqrt_n:.12e}",
                    "v_at_crossing": f"{v:.12e}",
                    "one_plus_z": f"{redshift_factor:.12e}",
                    "tau_thomson": f"{tau:.12e}",
                    "regime": "thick" if tau > 1.0 else ("thin" if tau < 1.0 else "unity"),
                }
            )

    print(f"input_rows={len(xs)}")
    print(f"table_x_range=[{xs[0]:.12e}, {xs[-1]:.12e}]")
    print(f"x_cross={x:.15e}")
    print(f"sqrtN_cross={sqrt_n:.15e}")
    print(f"v_cross={v:.15e}")
    print(f"one_plus_z={redshift_factor:.15e}")
    print(f"crossing_residual={residual:.3e}")
    print(f"tau=A/tcrit, A={a_seconds:.15e} s")
    print(f"tau_unity_tcrit={a_seconds:.15e} s")
    print(f"wrote={OUTPUT}")


if __name__ == "__main__":
    main()
