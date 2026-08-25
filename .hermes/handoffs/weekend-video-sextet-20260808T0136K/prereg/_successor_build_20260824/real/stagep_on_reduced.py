#!/usr/bin/env python3
"""Stage P on the REDUCED selection, under the widened round-8 audit.

V10 discloses that 997/1000 was measured on the PRE-reduction geometry. This measures the set
the frozen chain actually produces (6,445 bricks), with the audit that now also confirms a
sample of non-boundary successes and tests whether the shared reference null is conservative
against individual trials' own nulls.
"""
import sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
import successor_ref_v4 as R

HERE = Path(__file__).resolve().parent
d = np.load(HERE / "real_oracle_dr10.npz")
s = np.load(HERE / "real_selection_swapped.npz")     # full frozen algorithm output
idx = s["selected_idx"]
bid, c, nraw = d["brickid"][idx], d["c"][idx], d["n_eligible"][idx]
nret = R.retained_counts(nraw)
pm = R._planning_mask(bid, c, nret)
print(f"REDUCED geometry: {len(idx):,} bricks, n={pm.n:,}, Var(c)={float(np.var(pm.c)):.6f}, "
      f"N_eq={3*R.sse(np.ones(pm.n), pm.c):,.0f}", flush=True)
t0 = time.time()
succ, passed, audit = R.stage_power(pm, R.A_FLOOR, R.STAGE_P, 2, n_trials=R.N_TRIALS,
                                    confirm_perm=R.MC_CAL_PERM)
print(f"\n=== STAGE P ON THE REDUCED SET ({time.time()-t0:.0f}s) ===")
print(f"calibrated successes   : {succ}/{R.N_TRIALS}   (rule x >= {R.CP_PASS_X})")
print(f"audited trials         : {audit['boundary_trials']} (boundary band + sampled far)")
print(f"confirmed / refuted    : {audit['confirmed']} / {len(audit['refuted'])}")
print(f"reference z*           : {audit['ref_standardized_critical']:.4f}")
print(f"non-conservative nulls : {len(audit['nonconservative_nulls'])}")
for r in audit["refuted"][:3]:
    print(f"   REFUTED t{r['trial']}: p_cal {r['p_calibrated']:.2e} p_mc {r['p_monte_carlo']:.2e}")
for r in audit["nonconservative_nulls"][:3]:
    print(f"   NON-CONSERVATIVE t{r['trial']}: ref {r['ref_crit']:.4f} own {r['own_crit']:.4f}")
print(f"VERDICT                : {'PASS' if passed else 'FAIL'}")
