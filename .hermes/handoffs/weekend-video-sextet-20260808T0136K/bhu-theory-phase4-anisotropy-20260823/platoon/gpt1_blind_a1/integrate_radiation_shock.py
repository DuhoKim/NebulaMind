#!/usr/bin/env python3
"""Independent integration of Smoller--Temple equations (4.1)--(4.3).

The implementation uses only the equations transcribed in README.md from the
pinned source.  Units are kappa=1 and the scale freedom is fixed by setting the
N=1 (White-Hole horizon) event to t=1.  For pure radiation this implies
r_shock=2 there.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

SIGMA = 1.0 / 3.0
KAPPA = 1.0
Q_MIN_DEFAULT = math.log(1.0e-10)  # q=log(S), S=1/N


def rhs_q(q: float, y: np.ndarray) -> np.ndarray:
    """Return d(u, log(rbar))/dq, q=log(S), from (4.1),(4.2)."""
    u = float(y[0])
    S = math.exp(q)
    delta = SIGMA - u
    ratio = ((3.0 * u - 1.0) * delta + 6.0 * u * (1.0 + u) * S) / (
        delta + (1.0 + u) * S
    )
    du_dq = (1.0 + u) * ratio / (2.0 * (1.0 + 3.0 * u))
    dlogr_dq = 1.0 / (1.0 + 3.0 * u)
    return np.array([du_dq, dlogr_dq], dtype=float)


def integrate(method: str, rtol: float, atol: float, q_min: float):
    # Theorem 1, source lines 211--219, gives u(1)=0.  Radiation plus
    # N=H^2 rbar^2 and H=1/(2t) gives rbar=2 at N=S=1 when t=1.
    return solve_ivp(
        rhs_q,
        (0.0, q_min),
        np.array([0.0, math.log(2.0)]),
        method=method,
        rtol=rtol,
        atol=atol,
        dense_output=True,
        max_step=0.10,
    )


def evaluate(sol, q: np.ndarray) -> dict[str, np.ndarray]:
    u, logr = sol.sol(q)
    S = np.exp(q)
    N = 1.0 / S
    rbar = np.exp(logr)
    # Flat radiation FRW: H=1/(2t), while shock matching gives N=H^2 rbar^2.
    t = 0.5 * rbar * np.sqrt(S)
    rho = 3.0 / (4.0 * KAPPA * t * t)  # equation (5.2), sigma=1/3
    p = SIGMA * rho
    delta = SIGMA - u
    # Equation (4.3), multiplied through by S to avoid large-N cancellation.
    v = (-SIGMA * (1.0 + u) * S + delta) / ((1.0 + u) * S + delta)
    rho_bar = v * rho
    p_bar = u * rho
    speed = delta / ((1.0 + u) * np.sqrt(S))  # equation (4.5)
    entropy_rhs = ((1.0 - u) / (1.0 + u)) * ((SIGMA - u) / (SIGMA + u))
    return {
        "t": t,
        "r_shock": rbar,
        "u": u,
        "v": v,
        "N": N,
        "rho_tov_at_shock": rho_bar,
        "p_tov_at_shock": p_bar,
        "S": S,
        "rho_frw": rho,
        "p_frw": p,
        "shock_speed": speed,
        "entropy_rhs": entropy_rhs,
    }


def write_csv(path: Path, data: dict[str, np.ndarray], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        for row in zip(*(data[k] for k in fields)):
            writer.writerow([f"{float(x):.16e}" for x in row])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--q-min", type=float, default=Q_MIN_DEFAULT)
    parser.add_argument("--samples", type=int, default=601)
    args = parser.parse_args()
    out = args.out_dir.resolve()
    if out != Path(__file__).resolve().parent:
        raise SystemExit("Refusing to write outside the assigned gpt1_blind_a1 directory")

    base = integrate("DOP853", 2e-12, 2e-14, args.q_min)
    tight = integrate("DOP853", 2e-13, 2e-15, args.q_min)
    radau = integrate("Radau", 2e-11, 2e-13, args.q_min)
    if not (base.success and tight.success and radau.success):
        raise RuntimeError({"base": base.message, "tight": tight.message, "radau": radau.message})

    q = np.linspace(args.q_min, 0.0, args.samples)
    data = evaluate(base, q)
    tight_data = evaluate(tight, q)
    radau_data = evaluate(radau, q)

    interior = slice(0, -1)
    scale = np.maximum(1.0, np.abs(tight_data["u"]))
    checks = {
        "solver_base_success": bool(base.success),
        "solver_tight_success": bool(tight.success),
        "solver_radau_success": bool(radau.success),
        "base_function_evaluations": int(base.nfev),
        "tight_function_evaluations": int(tight.nfev),
        "radau_function_evaluations": int(radau.nfev),
        "q_min": float(args.q_min),
        "S_min": float(math.exp(args.q_min)),
        "max_abs_u_base_minus_tight": float(np.max(np.abs(data["u"] - tight_data["u"]))),
        "max_rel_u_base_minus_tight_scaled": float(np.max(np.abs(data["u"] - tight_data["u"]) / scale)),
        "max_abs_u_base_minus_radau": float(np.max(np.abs(data["u"] - radau_data["u"]))),
        "max_abs_rshock_base_minus_tight": float(np.max(np.abs(data["r_shock"] - tight_data["r_shock"]))),
        "u_min": float(np.min(data["u"])),
        "u_max": float(np.max(data["u"])),
        "v_min": float(np.min(data["v"])),
        "v_max": float(np.max(data["v"])),
        "speed_min": float(np.min(data["shock_speed"])),
        "speed_max": float(np.max(data["shock_speed"])),
        "speed_at_S_min": float(data["shock_speed"][0]),
        "radiation_asymptotic_ratio": float((SIGMA - data["u"][0]) / math.sqrt(data["S"][0])),
        "target_asymptotic_ratio": 4.0 / 3.0,
        "max_abs_N_identity_error": float(np.max(np.abs(data["N"] - (data["r_shock"] / (2.0 * data["t"])) ** 2))),
        "max_rel_N_identity_error": float(np.max(np.abs(data["N"] - (data["r_shock"] / (2.0 * data["t"])) ** 2) / data["N"])),
        "strict_0_lt_u_lt_sigma_away_from_endpoint": bool(np.all((data["u"][interior] > 0) & (data["u"][interior] < SIGMA))),
        "strict_0_lt_v_lt_1_away_from_endpoint": bool(np.all((data["v"][interior] > 0) & (data["v"][interior] < 1))),
        "strict_pbar_lt_rhobar_away_from_endpoint": bool(np.all(data["p_tov_at_shock"][interior] < data["rho_tov_at_shock"][interior])),
        "entropy_bound_5_6_away_from_endpoint": bool(np.all(data["S"][interior] < data["entropy_rhs"][interior])),
        "monotone_t": bool(np.all(np.diff(data["t"]) > 0)),
        "monotone_rshock": bool(np.all(np.diff(data["r_shock"]) > 0)),
        "endpoint_u_zero": float(data["u"][-1]),
        "endpoint_v_zero": float(data["v"][-1]),
        "endpoint_t": float(data["t"][-1]),
        "endpoint_rshock": float(data["r_shock"][-1]),
        "endpoint_N": float(data["N"][-1]),
    }

    required = [
        "t", "r_shock", "u", "v", "N", "rho_tov_at_shock", "p_tov_at_shock",
        "S", "rho_frw", "p_frw", "shock_speed",
    ]
    write_csv(out / "shock_results.csv", data, required)
    write_csv(
        out / "tov_side_profile.csv",
        data,
        ["r_shock", "t", "rho_tov_at_shock", "p_tov_at_shock", "u", "v", "N", "S"],
    )
    (out / "checks.json").write_text(json.dumps(checks, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(checks, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
