#!/usr/bin/env python3
"""Verify the load-bearing algebra of the sensitivity-gradient control by simulation.

CLAIM, verified below: if the latent handedness carries a monopole `mu` and the sign accuracy varies
with cos theta as g(c) = gbar(1 + gamma*c), the dipole estimator recovers

    A + gamma * (mu + A*kappa),        kappa = Cov(c^2, c) / Var(c)

`kappa` is a skewness term of the REALISED cos theta distribution, not a free parameter.

TWO THINGS THIS SCRIPT FOUND, both by failing first:

1. The naive form `A + gamma*mu` omits `A*kappa`. This script does NOT falsify it: at these
   replicate counts the standard error is ~0.001 and A*kappa is 0.000208, so both forms pass every
   case. The kappa term is ALGEBRAIC, found by expanding Cov(s,c)/Var(c) - not by this simulation.
   Do not cite this script as evidence for kappa; cite it for the gamma*mu structure.
2. v9 requires accuracy in (0.5, 1.0] (`inject_signs`, v9:1207). Since a = (1 + gbar(1+gamma*c))/2
   and c is in [-1, 1], that bounds |gamma| <= 1/gbar - 1. The first run of this script silently
   exceeded that domain, numpy clamped the flip probability, and it reported a false mismatch
   against the CORRECT formula. So out-of-domain parameters are now REFUSED, not clamped: a check
   that quietly repairs its own input cannot be trusted to report a failure.

Design: `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` §3.
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
import bs2a_quality_gate as G          # noqa: E402
import successor_ref_v9 as V9          # noqa: E402


def load_cos_theta(acquire: Path) -> np.ndarray:
    """cos theta over the 49,211 retained objects, frozen axis, v9's own function."""
    ev, _ = G.build_evidence(acquire / "positions_selected.csv", acquire / "quality_selected.csv")
    raw = G.verified_bytes(acquire / "positions_selected.csv", G.PARENT_SHA256).decode("utf-8")
    pos = {(r["brickid"].strip(), r["objid"].strip()): r for r in csv.DictReader(io.StringIO(raw))}
    keep = [e for e in ev if e["quality_pass"]]
    ra = np.array([float(pos[(e["brickid"], e["objid"])]["ra"]) for e in keep])
    dec = np.array([float(pos[(e["brickid"], e["objid"])]["dec"]) for e in keep])
    return V9.cos_theta(ra, dec)


def kappa_of(c: np.ndarray) -> float:
    return float(np.cov(c ** 2, c, ddof=1)[0, 1] / c.var(ddof=1))


def simulate(c, mu: float, gamma: float, gbar: float, reps: int = 60, seed: int = 20260828):
    """Return (mean recovered amplitude, standard error) or (None, None) if out of v9's domain."""
    a = (1.0 + gbar * (1.0 + gamma * c)) / 2.0
    if a.min() <= 0.5 or a.max() > 1.0:
        return None, None                      # REFUSE. Do not clamp.
    rng = np.random.default_rng(seed)
    A, out = V9.A_LONGO, []
    for _ in range(reps):
        lat = np.where(rng.random(len(c)) < (1.0 + mu + A * c) / 2.0, 1.0, -1.0)
        s = np.where(rng.random(len(c)) < (1.0 - a), -lat, lat)
        out.append(np.cov(s, c, ddof=1)[0, 1] / c.var(ddof=1) / gbar)
    return float(np.mean(out)), float(np.std(out, ddof=1) / np.sqrt(reps))


# (mu, gamma, gbar). Includes negative mu and negative gamma, and two deliberately out-of-domain
# rows that must be REFUSED rather than silently produce a number.
CASES = (
    (0.00, 0.00, 0.80), (0.00, 0.20, 0.80), (0.10, 0.00, 0.80), (0.10, 0.20, 0.80),
    (0.10, -0.20, 0.80), (0.05, 0.25, 0.80), (0.05, 0.40, 0.60), (0.00, 0.60, 0.60),
    (0.10, 0.50, 0.60), (-0.10, 0.30, 0.70),
)
OUT_OF_DOMAIN = ((0.05, 0.40, 0.80), (0.00, 0.60, 0.80))


def main() -> int:
    acquire = Path(__file__).resolve().parent.parent / "acquire"
    if not (acquire / "positions_selected.csv").is_file():
        print(f"  FAIL sources not found under {acquire}")
        return 1
    c = load_cos_theta(acquire)
    k, A = kappa_of(c), V9.A_LONGO
    print(f"N = {len(c):,}   A_LONGO = {A}   Var(cos theta) = {c.var(ddof=1):.6f}")
    print(f"kappa = Cov(c^2,c)/Var(c) = {k:+.6f}   A*kappa = {A*k:+.6f}\n")
    print(f"{'mu':>6} {'gamma':>7} {'gbar':>6} | {'exact':>10} | {'naive':>10} | {'recovered':>19} | verdict")

    fails = []
    for mu, gamma, gbar in CASES:
        exact, naive = A + gamma * (mu + A * k), A + gamma * mu
        got, se = simulate(c, mu, gamma, gbar)
        if got is None:
            fails.append(f"({mu},{gamma},{gbar}) unexpectedly out of domain")
            print(f"{mu:6.2f} {gamma:7.2f} {gbar:6.2f} | REFUSED (should be in domain)")
            continue
        ok = abs(got - exact) < max(4 * se, 0.002)
        if not ok:
            fails.append(f"({mu},{gamma},{gbar}) exact {exact:.5f} vs {got:.5f}")
        print(f"{mu:6.2f} {gamma:7.2f} {gbar:6.2f} | {exact:10.5f} | {naive:10.5f} | "
              f"{got:12.5f}+/-{se:.5f} | {'OK' if ok else 'MISMATCH'}")

    print("\ndomain control — these MUST be refused, not clamped:")
    for mu, gamma, gbar in OUT_OF_DOMAIN:
        got, _ = simulate(c, mu, gamma, gbar)
        ok = got is None
        if not ok:
            fails.append(f"({mu},{gamma},{gbar}) ran out of domain instead of refusing")
        print(f"  {'OK  ' if ok else 'FAIL'} mu={mu} gamma={gamma} gbar={gbar}: "
              f"{'refused' if ok else f'returned {got:.5f}'}")

    print(f"\n{len(CASES)} in-domain cases, {len(OUT_OF_DOMAIN)} domain controls, {len(fails)} failure(s)")
    for f in fails:
        print(f"  - {f}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
