#!/usr/bin/env python3
"""NOT A RECEIPT: controlled synthetic headroom experiment around bs3g_producer.py."""
from __future__ import annotations

import hashlib
import json
import sys
import time
import types
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
sys.path[:0] = [str(BASE / "gates"), str(BASE / "run"), str(BASE / "ref")]
import bs3g_producer as prod  # noqa: E402

A_HATS = (0.88, 0.90, 0.92, 0.95, 0.98)


def shifted_cal(frozen, a_hat):
    """Shift accuracy location only; preserve every margin, spread and covariance."""
    d = float(a_hat) - float(frozen["a_hat"])
    out = dict(frozen)
    for key in ("a_hat", "a_lb"):
        out[key] = float(frozen[key]) + d
    for key in ("a_b", "a_lb_b"):
        out[key] = np.asarray(frozen[key], dtype=np.float64).copy() + d
    out["cov_a"] = np.asarray(frozen["cov_a"], dtype=np.float64).copy()
    return out


def main():
    started = time.perf_counter()
    rv = prod.ruled_values()
    for name, (path, want) in prod.PINNED.items():
        if prod._sha(path) != want:
            raise prod.BS3GRefusal(f"pinned {name} digest mismatch")
    buffers, mods, mapping, saved = prod._load()
    v9, gcp = mods["successor_ref_v9"], mods["gain_counterfactual_path"]
    results = []
    try:
        mask, _ = gcp._fixture()
        if type(mask) is not v9.FixtureMask:
            raise prod.BS3GRefusal("fixture mask is not type-exact")
        frozen = gcp._CAL
        ep = prod.PINNED["estimator"][0]
        ens = {"__name__": "gain_gradient_estimator", "__file__": str(ep)}
        exec(compile(ep.read_bytes(), str(ep), "exec", dont_inherit=True, optimize=0), ens)
        c_bin = np.array([mask.c[mask.bin == b].mean() for b in range(v9.N_CAL_BINS)])
        c_bar = float(mask.c.mean())
        bin_radius = float(np.max(np.abs(c_bin - c_bar)))
        point_radius = float(np.max(np.abs(mask.c - c_bar)))
        prod.harness._JOURNAL.events.clear()
        prod.harness._JOURNAL.active = True
        for ah in A_HATS:
            one_start = time.perf_counter()
            cal = shifted_cal(frozen, ah)
            estimate, bad = ens["estimate_gamma"](cal["a_b"], cal["cov_a"], c_bin.tolist())
            if bad or estimate is None:
                raise prod.BS3GRefusal(f"estimator refused a_hat={ah}: {bad}")
            matrix = []
            mins = np.full(len(rv["grid"]), np.inf)
            cache = {}
            cal_inconclusive = 0
            any_inconclusive = 0
            for i in range(rv["n_draws"]):
                mp = mapping.make_mapping(i)
                row = []
                for j, gd in enumerate(rv["grid"]):
                    gamma = float(gd)
                    s_prime, cal_prime = mp(gamma, mask, cal)
                    mins[j] = min(mins[j], float(np.min(cal_prime["a_lb_b"])))
                    key = (s_prime.tobytes(), prod.canonical({k: (np.asarray(v).tolist()
                           if isinstance(v, np.ndarray) else v)
                           for k, v in cal_prime.items()}))
                    if key not in cache:
                        try:
                            out = gcp.evaluate_at(gamma, mask, cal, mp, stage=v9.STAGE_C,
                                                  prefix=11, trial=3, n_perm=rv["n_perm"])
                        except gcp.PathRefusal as exc:
                            cache[key] = prod._path_outcome(exc, v9)
                        else:
                            cache[key] = out["verdict"]
                    token = cache[key]
                    row.append(token)
                    any_inconclusive += token.startswith("INCONCLUSIVE-BY-")
                    cal_inconclusive += token == "INCONCLUSIVE-BY-CALIBRATION"
                matrix.append(row)
                print(f"a_hat={ah:.2f} draw {i + 1}/99", file=sys.stderr, flush=True)
            good_js = [j for j in range(len(rv["grid"]))
                       if all(matrix[i][j] != "INCONCLUSIVE-BY-CALIBRATION"
                              for i in range(rv["n_draws"]))]
            symmetric = [j for j in good_js if (len(rv["grid"]) - 1 - j) in good_js]
            widest = max((abs(float(rv["grid"][j])) for j in symmetric), default=0.0)
            jw = min(range(len(rv["grid"])),
                     key=lambda j: (abs(abs(float(rv["grid"][j])) - widest), j))
            baselines = [row[rv["j0"]] for row in matrix]
            held = all(x == row[rv["j0"]] for row in matrix for x in row)
            gap = float(np.max(np.asarray(cal["a_b"]) - np.asarray(cal["a_lb_b"])))
            analytic = min(float(rv["gamma"]), (ah - gap - v9.A_FLOOR) / bin_radius)
            results.append({
                "a_hat": ah, "admissible_gamma_measured": widest,
                "admissible_gamma_analytic": analytic,
                "ratio_sigma_gamma": widest / estimate["sigma_gamma"],
                "inconclusive_fraction": any_inconclusive / (rv["n_draws"] * len(rv["grid"])),
                "calibration_inconclusive_fraction": cal_inconclusive / (rv["n_draws"] * len(rv["grid"])),
                "min_a_lb_b_gamma0": float(mins[rv["j0"]]),
                "min_a_lb_b_widest": float(mins[jw]),
                "invariance_outcome": "HELD" if held else "FAILED",
                "gamma_hat": estimate["gamma_hat"], "sigma_gamma": estimate["sigma_gamma"],
                "runtime_seconds": time.perf_counter() - one_start,
            })
        prod.harness._JOURNAL.active = False
        stray, native = prod.harness._census(prod.harness._JOURNAL.events,
            {x[0] for x in prod.harness.MANIFEST} | {"successor_ref_v9",
             "gain_counterfactual_path", "gain_mapping_a", "gain_gradient_estimator"})
        if stray or native:
            raise prod.BS3GRefusal(f"loaded-object census refusal: {stray}, {native}")
        for _name, (_buf, path, got) in buffers.items():
            if prod._sha(path) != got:
                raise prod.BS3GRefusal(f"root changed after replay: {path}")
        payload = {"warning": "NOT A RECEIPT", "results": results,
                   "fixture": {"generator": "ref/gain_counterfactual_path.py::_fixture",
                               "n": mask.n, "seed": 7, "c_min": float(mask.c.min()),
                               "c_max": float(mask.c.max()), "c_bar": c_bar,
                               "c_bin_means": c_bin.tolist(), "bin_radius": bin_radius,
                               "point_radius": point_radius},
                   "total_runtime_seconds": time.perf_counter() - started}
        (HERE / "headroom_raw_NOT_A_RECEIPT.json").write_text(
            json.dumps(payload, sort_keys=True, indent=2) + "\n")
    finally:
        prod.harness._JOURNAL.active = False
        if saved is not None:
            sys.modules["successor_ref_v9"] = saved
        else:
            sys.modules.pop("successor_ref_v9", None)


if __name__ == "__main__":
    main()
