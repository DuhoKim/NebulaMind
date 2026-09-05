#!/usr/bin/env python3
"""SMOKE TEST on synthetics — three training-free chirality estimators under degradations. This is NOT evidence of
fitness on real galaxies (the CE-ResNet scored 100% on synthetics and 54.7% on real ones); it checks that each
estimator's sign behaves as its construction claims and shows which degradations each is sensitive to.
Deterministic seeds; no real pixel; output JSON + Markdown beside this script."""
import sys, json, time
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[3] / "spike" / "yui_identity"))
import fourier_chirality as fc
from w_chi import synth_spiral, chi as ridge_chi
N = 128; yy, xx = np.mgrid[0:N, 0:N]; dx = xx - 63.5; dy = yy - 63.5; rr = np.hypot(dx, dy)
def degrade(img, rng, bulge, bar, gradient, mask):
    out = img.copy(); peak = out.max()
    if bulge:
        out += rng.uniform(0.5, 3.0) * peak * np.exp(-rr ** 2 / (2 * 4.0 ** 2))
    if bar:
        pa = rng.uniform(0, np.pi); xb = dx * np.cos(pa) + dy * np.sin(pa); yb = -dx * np.sin(pa) + dy * np.cos(pa)
        out += rng.uniform(0.3, 1.5) * peak * np.exp(-(xb ** 2 / (2 * 12.0 ** 2) + yb ** 2 / (2 * 3.0 ** 2)))
    if gradient:
        psi = rng.uniform(0, 2 * np.pi); out += 0.3 * peak * (dx * np.cos(psi) + dy * np.sin(psi)) / 64.0   # MEDIUM-like scattered-light ramp
    if mask:
        fill = np.sort(out.ravel())[(out.size - 1) // 2]                                                     # lower median (§8.9c-like)
        for _ in range(13):                                                                                  # 13 blocks of 8x8 = 832 px ~ 5%
            i, j = rng.integers(0, N - 8, size=2); out[i:i + 8, j:j + 8] = fill
    core = out[48:80, 48:80].max()
    return out / core if core > 0 else out                                                                 # §8.15-style normalisation
def fourier_nodep(x):
    fc.DEPROJECT = False; c = float(fc.chi(x)); fc.DEPROJECT = True; return c
EST = {"fourier_deproj": lambda x: float(fc.chi(x)), "fourier_nodeproj": fourier_nodep, "ridge_w_chi": lambda x: float(ridge_chi(x))}
COND = {"clean": {}, "bulge": {"bulge": 1}, "bar": {"bar": 1}, "gradient": {"gradient": 1}, "mask5pct": {"mask": 1},
        "all": {"bulge": 1, "bar": 1, "gradient": 1, "mask": 1}}
NS = 300
ref = {k: np.sign(f(synth_spiral(1, 20, 0, 1e9, seed=0))) for k, f in EST.items()}        # each estimator's own sign convention
res = {}
for cname, flags in COND.items():
    acc = {k: 0 for k in EST}; ties = {k: 0 for k in EST}
    for i in range(NS):
        rng = np.random.default_rng(10_000 + i); par = int(rng.choice([1, -1])); pitch = float(rng.uniform(10, 40))
        inc = float(rng.uniform(0, 65)); snr = float(np.exp(rng.uniform(np.log(2), np.log(50))))
        img = synth_spiral(par, pitch, inc, snr, seed=20_000 + i)
        img = degrade(img, rng, flags.get("bulge"), flags.get("bar"), flags.get("gradient"), flags.get("mask"))
        for k, f in EST.items():
            c = f(img)
            if c == 0 or not np.isfinite(c): ties[k] += 1
            elif np.sign(c) == par * ref[k]: acc[k] += 1
    res[cname] = {k: {"correct": acc[k], "ties_or_nonfinite": ties[k], "n": NS, "accuracy": acc[k] / NS} for k in EST}
    print(cname, {k: round(v["accuracy"], 3) for k, v in res[cname].items()}, flush=True)
out = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "n_per_condition": NS, "pitch_deg": "U(10,40)", "incl_deg": "U(0,65)", "snr": "logU(2,50)",
       "fourier_constants": {"R_MIN": fc.R_MIN, "R_MAX": fc.R_MAX, "N_U": fc.N_U, "N_T": fc.N_T, "M_MODE": fc.M_MODE, "P_MIN": fc.P_MIN, "P_MAX": fc.P_MAX, "Q_MIN": fc.Q_MIN},
       "results": res, "caveat": "synthetics only; not evidence of fitness on real galaxies"}
(HERE / "synthetics_smoke_results_20260905.json").write_text(json.dumps(out, indent=1))
lines = ["| condition | " + " | ".join(EST) + " |", "|---|" + "---|" * len(EST)]
for c, r in res.items(): lines.append(f"| {c} | " + " | ".join(f"{r[k]['accuracy']:.3f}" for k in EST) + " |")
(HERE / "synthetics_smoke_results_20260905.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
