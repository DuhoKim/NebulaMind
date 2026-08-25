#!/usr/bin/env python3
"""Real reduction WITH the swap-then-removal phase the frozen local_pass performs."""
import sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import successor_ref_v4 as R
from reduce_fast import reduce_removals
from greedy_fast import greedy_prefix

d = np.load(Path(__file__).resolve().parent / "real_oracle_dr10.npz")
bid, c, nraw = d["brickid"], d["c"], d["n_eligible"]
nret = R.retained_counts(nraw)
target = R.L_PLAN_MARGIN * R.NEQ_MIN / 3.0
order, _l, _n = greedy_prefix(bid, c, nraw, nret, target)
o = np.array(order, dtype=np.int64)
print(f"greedy prefix: {len(o):,} bricks; target L_ret {target:,.1f}", flush=True)
t0 = time.time()
keep, L, removed = reduce_removals(bid[o], c[o], nret[o], target)
sel = o[keep]
print(f"\nreduction WITH swap phase ({time.time()-t0:.0f}s)")
print(f"  bricks           : {int(keep.sum()):,}  (removal-only gave 6,445)")
print(f"  moves            : {len(removed):,}  removed bricks {removed[:8]}{'...' if len(removed)>8 else ''}")
print(f"  raw objects      : {int(nraw[sel].sum()):,}")
print(f"  retained objects : {int(nret[sel].sum()):,}")
print(f"  L_ret {L:,.3f}   N_eq {3*L:,.3f}")
np.savez(Path(__file__).resolve().parent / "real_selection_swapped.npz",
         selected_idx=sel, selected_brickid=bid[sel], l_ret=L,
         removed=np.array(removed, dtype=np.int64))
print("wrote real_selection_swapped.npz")
