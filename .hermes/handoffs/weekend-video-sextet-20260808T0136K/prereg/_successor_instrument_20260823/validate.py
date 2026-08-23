#!/usr/bin/env python3
"""Validation battery for the successor estimator. Synthetic skies only.

Runs every test on TWO footprints:
  SPHERE — uniform, the geometry the dead harness silently assumed;
  CAP    — the dead parent's REAL 208,407 positions (public geometry, no chi), the geometry
           that broke the predecessor. An estimator that only works on the sphere is the
           mistake this program already made once.

Battery (from the lapse note + SUCCESSOR_SCOPE): unbiasedness at A=+0.0408 and A=-0.0408;
A=0 false-positive rate at the one-sided threshold; MONOPOLE INJECTION M=0.01, A=0 — the
predecessor's uncentred estimator read that as A_hat=-0.019 on the cap; sigma calibration
(empirical scatter vs analytic sigma_a).
"""
import sys, csv, math
import numpy as np
sys.path.insert(0, ".")
from estimator import axis_cosines, estimate, synth_signs, permutation_p

RA0, DEC0 = 216.984434295527, 32.060611193471
rng = np.random.default_rng(20260823)

def load_cap(n=None):
    ra, dec = [], []
    p = "../_positions_20260820/positions_parent_20260820.csv"
    for r in csv.DictReader(open(p)):
        ra.append(float(r["ra"])); dec.append(float(r["dec"]))
    c = axis_cosines(np.array(ra), np.array(dec), RA0, DEC0)
    return c if n is None else c[rng.choice(c.size, n, replace=False)]

def sphere(n):
    return rng.uniform(-1.0, 1.0, n)

def trial_mean(cos, M, A, reps):
    a, s = [], []
    for _ in range(reps):
        r = estimate(synth_signs(cos, M, A, rng), cos)
        a.append(r["a_hat"]); s.append(r["sigma_a"])
    return np.mean(a), np.std(a), np.mean(s)

N = 50_000        # per-trial sample size, both footprints
REPS = 200
ok = True
def report(name, cond, detail):
    global ok
    ok &= cond
    print(f"{'PASS' if cond else 'FAIL'}  {name}: {detail}")

for label, cos in (("SPHERE", sphere(N)), ("CAP", load_cap(N))):
    vc = float(np.var(cos))
    print(f"\n== {label}:  n={cos.size:,}  mean(c)={cos.mean():+.4f}  Var(c)={vc:.4f} ==")

    m, sd, sig = trial_mean(cos, 0.0, +0.0408, REPS)
    report("unbiased at A=+0.0408", abs(m - 0.0408) < 3*sd/math.sqrt(REPS),
           f"mean a_hat {m:+.5f} (sd {sd:.5f}, analytic sigma {sig:.5f})")
    report("sigma calibrated", 0.8 < sd/sig < 1.2, f"empirical/analytic = {sd/sig:.3f}")

    m2, sd2, _ = trial_mean(cos, 0.0, -0.0408, REPS)
    report("sign preserved at A=-0.0408", abs(m2 + 0.0408) < 3*sd2/math.sqrt(REPS),
           f"mean a_hat {m2:+.5f}")

    m3, sd3, _ = trial_mean(cos, 0.01, 0.0, REPS)
    report("monopole M=0.01 does NOT leak", abs(m3) < 3*sd3/math.sqrt(REPS),
           f"mean a_hat {m3:+.6f}  (predecessor on cap: -0.019)")

    # false-positive rate at one-sided p<0.001 over null skies, cheap permutation count
    fp = 0; NULLREPS = 300
    for _ in range(NULLREPS):
        sgn = synth_signs(cos, 0.0, 0.0, rng)
        if permutation_p(sgn, cos, 999, rng) < 0.001: fp += 1
    report("null false-positive rate", fp <= 2, f"{fp}/{NULLREPS} at p<0.001")

print("\nALL PASS" if ok else "\nBATTERY FAILED")
sys.exit(0 if ok else 1)
