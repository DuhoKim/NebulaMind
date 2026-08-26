#!/usr/bin/env python3
"""STAGE P, EXACT — every trial judged against its OWN null, no shared reference.

WHY THIS EXISTS
---------------
Stage P measured ONE reference null per prefix and applied it to all 1,000 trials, on the
argument that standardizing by sigma_exact removes the sign multiset's leading effect. Round 8's
referees said that had never been shown conservative. The check added in response measured it
and found it false on the reduced geometry: 2 of 8 sampled trials had their own standardized
critical value ABOVE the shared reference (3.1672 and 3.1957 against 3.1220), while the residual
margin PWR_CONSERVATISM is only 1.01. For those trials the shared null sets the bar too low, so
a success could be counted that the trial's own null would not grant. The 997/1000 PASS on the
pre-reduction geometry predates that check entirely.

`REAL_GEOMETRY_RESULT_20260825.md` recorded three possible repairs: (a) an envelope over sampled
nulls plus a margin, (b) per-trial nulls, (c) a larger deflation constant.

This implements (b), and more of it than that entry proposed. (a) and (c) both replace an
unproven assumption with a better-argued one: an envelope over K sampled trials is the maximum
of a sample, and the maximum of 24 samples does not bound the maximum of 1,000 — it sits around
the 96th percentile, so 1,000 trials would exceed it routinely. A deflation constant fitted to
this geometry is a constant fitted to this geometry.

(b) removes the assumption instead of improving it. Every trial gets its own permutation null and
its own p-value, so there is no shared reference in the counting path and nothing left to be
conservative or not. It costs 7.7 s per trial single-threaded — 2.1 hours for 1,000 — which is
why it was passed over. This machine has 32 cores.

WHAT IS AND IS NOT ESTABLISHED HERE
-----------------------------------
This is a MEASUREMENT harness, not a change to the reference implementation. `successor_ref_v7.py`
is in front of a referee as the closure check right now and is not being edited mid-gate. If this
measurement holds, folding an exact Stage P into the reference implementation is a v8 change that
gets its own fixtures and its own gate.

Determinism: each trial's permutation stream is addressed by (stage, prefix, 10_000 + t, role),
exactly as the existing audit addresses its confirmations. The address does not depend on
execution order, so the parallel result equals the serial one.

    python3 stagep_exact.py --workers 24 --out STAGEP_EXACT_RECEIPT.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing as mp
import os
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "ref"))
import successor_ref_v7 as R  # noqa: E402

ORACLE = HERE / "real_oracle_dr10.npz"
SELECTION = HERE / "real_selection_swapped.npz"
_MASK = None


def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def build_mask():
    """The geometry the frozen chain actually produces — the reduced set, not the pre-reduction
    one the retracted 997/1000 was measured on."""
    d = np.load(ORACLE)
    s = np.load(SELECTION)
    idx = s["selected_idx"]
    bid, c, nraw = d["brickid"][idx], d["c"][idx], d["n_eligible"][idx]
    return R._planning_mask(bid, c, R.retained_counts(nraw)), len(idx)


def _init():
    global _MASK
    _MASK, _ = build_mask()


def _trial(t):
    """One trial, judged only by its own permutation null.

    Returns (t, p_own, p_shared_placeholder). The shared-null comparison is computed in the
    parent, where the reference null exists; a worker never sees it, so it cannot influence
    what this function counts.
    """
    m = _MASK
    sm = m.with_signs(R.inject_signs(m, R.A_FLOOR, R.STAGE_P, 2, t))
    p_own = R.perm_record(sm, R.STAGE_P, 2, 10_000 + t, R.MC_CAL_PERM)[2]
    return t, float(p_own)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--workers", type=int, default=max(1, min(24, (os.cpu_count() or 4) - 8)))
    ap.add_argument("--trials", type=int, default=R.N_TRIALS)
    ap.add_argument("--out", default="STAGEP_EXACT_RECEIPT.json")
    args = ap.parse_args()

    mask, nbricks = build_mask()
    var_c = float(np.var(mask.c))
    n_eq = 3.0 * R.sse(np.ones(mask.n), mask.c)
    print(f"geometry: {nbricks:,} bricks, n={mask.n:,}, Var(c)={var_c:.6f}, N_eq={n_eq:,.0f}",
          flush=True)
    print(f"exact Stage P: {args.trials:,} trials, each against its own {R.MC_CAL_PERM:,}-"
          f"permutation null, {args.workers} workers", flush=True)

    # The shared reference null, kept ONLY so its verdict can be reported beside the exact one.
    # It takes no part in the exact count.
    t0 = time.time()
    ref = mask.with_signs(R.inject_signs(mask, R.A_FLOOR, R.STAGE_P, 2, 1))
    ref_z = R.reference_null_z(ref, R.STAGE_P, 2)
    ref_crit = float(np.quantile(ref_z, 1.0 - R.P_REPRODUCED))
    print(f"shared reference z* = {ref_crit:.4f} (reported for comparison only, "
          f"{time.time()-t0:.0f}s)", flush=True)

    shared = {}
    for t in range(1, args.trials + 1):
        sm = ref if t == 1 else mask.with_signs(R.inject_signs(mask, R.A_FLOOR, R.STAGE_P, 2, t))
        shared[t] = float(R.calibrated_p(sm, ref_z))

    t0 = time.time()
    results = {}
    with mp.Pool(args.workers, initializer=_init) as pool:
        for i, (t, p_own) in enumerate(pool.imap_unordered(_trial, range(1, args.trials + 1)), 1):
            results[t] = p_own
            if i % 50 == 0 or i == args.trials:
                el = time.time() - t0
                print(f"  {i:>5,}/{args.trials:,} trials · {el/60:.1f} min · "
                      f"eta {(el/i)*(args.trials-i)/60:.1f} min", flush=True)
    secs = time.time() - t0

    exact_succ = sum(1 for p in results.values() if p < R.P_REPRODUCED)
    shared_succ = sum(1 for p in shared.values() if p < R.P_REPRODUCED)
    # Trials the shared null would have granted and their own null does not: the counting error
    # the round-8 audit predicted. And the reverse, which would be the shared null being
    # over-strict rather than under-strict.
    granted_only_by_shared = sorted(t for t in results
                                    if shared[t] < R.P_REPRODUCED <= results[t])
    granted_only_by_own = sorted(t for t in results
                                 if results[t] < R.P_REPRODUCED <= shared[t])
    passed = exact_succ >= R.CP_PASS_X

    receipt = {
        "what": "Stage P with per-trial nulls; no shared reference in the counting path",
        "subject": {"path": "../ref/successor_ref_v7.py", "sha256_12": sha12(HERE.parent / "ref" / "successor_ref_v7.py")},
        "harness_sha256_12": sha12(Path(__file__)),
        "inputs": {"oracle": sha12(ORACLE), "selection": sha12(SELECTION)},
        "geometry": {"bricks": nbricks, "n": int(mask.n), "var_c": var_c, "n_eq": n_eq},
        "settings": {"trials": args.trials, "a_floor": R.A_FLOOR, "perms": R.MC_CAL_PERM,
                     "p_reproduced": R.P_REPRODUCED, "pass_rule_x_at_least": R.CP_PASS_X},
        "exact": {"successes": exact_succ, "passes_rule": passed},
        "shared_null_for_comparison": {"successes": shared_succ, "z_critical": ref_crit,
                                       "granted_only_by_shared": granted_only_by_shared,
                                       "granted_only_by_own": granted_only_by_own},
        "seconds": round(secs, 1),
        "p_own_by_trial": {str(t): results[t] for t in sorted(results)},
    }
    Path(args.out).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")

    print()
    print(f"=== STAGE P, EXACT ({secs/60:.1f} min) ===")
    print(f"exact successes (own null)   : {exact_succ}/{args.trials}   (rule x >= {R.CP_PASS_X})")
    print(f"shared-null successes        : {shared_succ}/{args.trials}   (comparison only)")
    print(f"granted by shared, not by own: {len(granted_only_by_shared)} {granted_only_by_shared[:8]}")
    print(f"granted by own, not by shared: {len(granted_only_by_own)} {granted_only_by_own[:8]}")
    print(f"VERDICT                      : {'PASS' if passed else 'FAIL'}")
    print(f"receipt                      : {args.out}")
    return 0 if passed else 2


if __name__ == "__main__":
    sys.exit(main())
