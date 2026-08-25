#!/usr/bin/env python3
"""Vectorized equivalent of successor_ref_v3.greedy_ledger, for production-scale exploration.

This is NOT a second definition. The frozen definition is greedy_ledger() in the pinned
reference. This module exists because that implementation is O(n^2) with a Python inner loop
and will not run at 270,577 bricks -- itself a finding to carry into the prereg. Agreement with
the frozen implementation is PROVEN on random small cases before any production use.
"""
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
import successor_ref_v3 as R


def greedy_prefix(brickid, c, n_raw, n_ret, target_l_ret, max_steps=None):
    """Same rule as the frozen greedy: accept argmax of delta = (N*nj/(N+nj))*(cj-cbar)^2,
    ties by larger |c| then smaller brickid; scan order ascending brickid. Stops once the
    RETAINED leverage of the accepted prefix reaches target_l_ret."""
    bid = np.asarray(brickid, dtype=np.int64)
    cc = np.asarray(c, dtype=np.float64)
    nr = np.asarray(n_raw, dtype=np.int64)
    nt = np.asarray(n_ret, dtype=np.int64)
    keep = np.nonzero(nr > 0)[0]
    keep = keep[np.argsort(bid[keep], kind="stable")]      # frozen scan order
    cand_c, cand_n, cand_b = cc[keep], nr[keep].astype(np.float64), bid[keep]
    alive = np.ones(len(keep), dtype=bool)
    order = []
    N = cbar = 0.0
    # retained accumulators for the stopping test
    rN = rSum = rSumSq = 0.0
    steps = max_steps or len(keep)
    for step in range(steps):
        if N == 0.0:
            delta = np.zeros(len(keep), dtype=np.float64)
        else:
            d = cand_c - cbar
            delta = (N * cand_n / (N + cand_n)) * d * d
        delta = np.where(alive, delta, -np.inf)
        best = float(delta.max())
        tied = np.nonzero(delta == best)[0]
        if len(tied) > 1:                                   # frozen tie rule
            a = np.abs(cand_c[tied])
            tied = tied[a == a.max()]
            tied = tied[np.argmin(cand_b[tied])] if len(tied) > 1 else tied[0]
            i = int(tied)
        else:
            i = int(tied[0])
        alive[i] = False
        nj = float(cand_n[i])
        cbar = (cbar * N + cand_c[i] * nj) / (N + nj)
        N += nj
        order.append(int(keep[i]))
        k = float(nt[keep[i]])
        if k > 0:
            rN += k
            rSum += k * cand_c[i]
            rSumSq += k * cand_c[i] * cand_c[i]
        l_ret = (rSumSq - rSum * rSum / rN) if rN > 0 else 0.0
        if target_l_ret is not None and l_ret >= target_l_ret:
            return order, l_ret, rN
    l_ret = (rSumSq - rSum * rSum / rN) if rN > 0 else 0.0
    return order, l_ret, rN


def prove_agreement(trials=40, seed=7):
    """Random small cases: the vectorized order must equal the frozen order exactly."""
    rng = np.random.default_rng(seed)
    for t in range(trials):
        n = int(rng.integers(3, 14))
        bid = rng.permutation(np.arange(100, 100 + n)).astype(np.int64)
        c = np.round(rng.uniform(-1, 1, n), 3)
        nraw = rng.integers(0, 30, n).astype(np.int64)
        if (nraw > 0).sum() < 2:
            continue
        ref_order, _ledger = R.greedy_ledger(bid, c, nraw)
        fast_order, _l, _n = greedy_prefix(bid, c, nraw, R.retained_counts(nraw), None)
        if ref_order != fast_order:
            raise AssertionError(f"ORDER MISMATCH trial {t}: ref {ref_order} fast {fast_order}")
    return trials


if __name__ == "__main__":
    print(f"agreement with the frozen greedy proven on {prove_agreement()} random cases")
