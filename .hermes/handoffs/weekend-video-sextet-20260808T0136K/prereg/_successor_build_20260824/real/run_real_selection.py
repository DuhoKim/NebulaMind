#!/usr/bin/env python3
"""The real polar selection on DR10 geometry. Positions and counts only -- no chi, no images."""
import sys, time, json
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import successor_ref_v3 as R
from greedy_fast import greedy_prefix, prove_agreement

print(f"agreement with the frozen greedy re-proven on {prove_agreement()} random cases")
d = np.load(Path(__file__).resolve().parent / "real_oracle_dr10.npz")
bid, c, nraw = d["brickid"], d["c"], d["n_eligible"]
nret = R.retained_counts(nraw)
print(f"universe {len(bid):,} bricks; positive-raw {int((nraw>0).sum()):,}; "
      f"objects raw {int(nraw.sum()):,} retained {int(nret.sum()):,}")

L_REQ = R.NEQ_MIN / 3.0
print(f"frozen requirement: N_eq >= {R.NEQ_MIN:,}  =>  L_ret >= {L_REQ:,.1f}")

t0 = time.time()
order, l_ret, rN = greedy_prefix(bid, c, nraw, nret, L_REQ)
dt = time.time() - t0
sel = np.array(order, dtype=np.int64)
print(f"\n=== SELECTION AT THE FROZEN REQUIREMENT ===")
print(f"bricks accepted : {len(sel):,}   ({dt:.1f}s)")
print(f"retained objects: {int(rN):,}")
print(f"raw objects     : {int(nraw[sel].sum()):,}")
print(f"L_ret           : {l_ret:,.1f}")
print(f"N_eq            : {3*l_ret:,.1f}")
csel = c[sel]
print(f"|cos t| range   : [{np.abs(csel).min():.4f}, {np.abs(csel).max():.4f}]")
print(f"Var(cos t) ret  : {np.average((csel-np.average(csel,weights=nret[sel]))**2, weights=nret[sel]):.6f}")

# with the frozen 1.2 planning margin
t0 = time.time()
order_m, l_m, rN_m = greedy_prefix(bid, c, nraw, nret, R.L_PLAN_MARGIN * L_REQ)
dt = time.time() - t0
selm = np.array(order_m, dtype=np.int64)
print(f"\n=== WITH THE FROZEN 1.2 MARGIN (L_plan) ===")
print(f"bricks accepted : {len(selm):,}   ({dt:.1f}s)")
print(f"retained objects: {int(rN_m):,}   raw objects: {int(nraw[selm].sum()):,}")
print(f"L_ret {l_m:,.1f}   N_eq {3*l_m:,.1f}")

print(f"\n=== COMPARISON TO THE DEAD RUN ===")
print(f"dead run   : 208,407 objects, Var 0.0580, N_eq 36,253 (never reached 100,000)")
print(f"successor  : {int(nraw[selm].sum()):,} raw objects, N_eq {3*l_m:,.0f} "
      f"-- {3*l_m/36253:.1f}x the dead run's leverage")
print(f"image bytes: ~{len(selm)*12.2/1024:.1f} GB at the predecessor's 12.2 MB/brick "
      f"(vs 735.9 GB for the dead run)")

np.savez(Path(__file__).resolve().parent / "real_selection_dr10.npz",
         selected_idx=selm, selected_brickid=bid[selm], l_ret=l_m, n_ret=rN_m)
print("\nwrote real_selection_dr10.npz")
