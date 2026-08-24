#!/usr/bin/env python3
"""Independent checks of the generated shock table."""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SIGMA = 1.0 / 3.0


def main() -> None:
    path = HERE / "shock_results.csv"
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0])
    a = {k: np.array([float(r[k]) for r in rows]) for k in fields}
    q = np.log(a["S"])
    u = a["u"]
    S = a["S"]
    delta = SIGMA - u

    expected_v = (-SIGMA * (1.0 + u) * S + delta) / ((1.0 + u) * S + delta)
    expected_rho = 3.0 / (4.0 * a["t"] ** 2)
    expected_pbar = u * expected_rho
    expected_rhobar = expected_v * expected_rho

    # A finite-difference check is deliberately independent of solve_ivp's
    # internal derivative.  Ignore two endpoint-adjacent samples.
    du_num = np.gradient(u, q, edge_order=2)
    logr_num = np.gradient(np.log(a["r_shock"]), q, edge_order=2)
    ratio = ((3.0 * u - 1.0) * delta + 6.0 * u * (1.0 + u) * S) / (
        delta + (1.0 + u) * S
    )
    du_rhs = (1.0 + u) * ratio / (2.0 * (1.0 + 3.0 * u))
    logr_rhs = 1.0 / (1.0 + 3.0 * u)
    core = slice(2, -2)

    report = {
        "rows": len(rows),
        "required_columns_present": all(
            x in fields
            for x in ["t", "r_shock", "u", "v", "N", "rho_tov_at_shock", "p_tov_at_shock"]
        ),
        "max_abs_constraint_v_error": float(np.max(np.abs(a["v"] - expected_v))),
        "max_rel_rho_tov_error": float(np.max(np.abs(a["rho_tov_at_shock"] - expected_rhobar) / np.maximum(1.0, np.abs(expected_rhobar)))),
        "max_rel_p_tov_error": float(np.max(np.abs(a["p_tov_at_shock"] - expected_pbar) / np.maximum(1.0, np.abs(expected_pbar)))),
        "max_abs_finite_difference_du_dq_residual": float(np.max(np.abs(du_num[core] - du_rhs[core]))),
        "max_abs_finite_difference_dlogr_dq_residual": float(np.max(np.abs(logr_num[core] - logr_rhs[core]))),
        "finite_difference_q_step": float(q[1] - q[0]),
        "N_strictly_decreases_with_t": bool(np.all(np.diff(a["N"]) < 0)),
        "t_strictly_increases": bool(np.all(np.diff(a["t"]) > 0)),
        "rshock_strictly_increases": bool(np.all(np.diff(a["r_shock"]) > 0)),
        "all_finite": bool(all(np.all(np.isfinite(x)) for x in a.values())),
    }
    (HERE / "verification_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
