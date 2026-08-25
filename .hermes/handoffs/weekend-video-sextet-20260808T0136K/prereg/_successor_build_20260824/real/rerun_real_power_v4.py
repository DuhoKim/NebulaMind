#!/usr/bin/env python3
"""Re-run Stage P on the real geometry under v4's SELF-VERIFYING power gate.

The earlier 997/1000 was computed with calibrated decisions alone -- the logic both round-6
gates said was unsound. This re-runs it with the confirmation path that re-tests every
near-boundary success against an independent full permutation run.
"""
import sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
import successor_ref_v4 as R

HERE = Path(__file__).resolve().parent
d = np.load(HERE / "real_oracle_dr10.npz"); s = np.load(HERE / "real_selection_dr10.npz")
idx = s["selected_idx"]
bid, c, nraw = d["brickid"][idx], d["c"][idx], d["n_eligible"][idx]
nret = R.retained_counts(nraw)
pm = R._planning_mask(bid, c, nret)
print(f"real geometry: {len(idx):,} bricks, n={pm.n:,}, Var(c)={float(np.var(pm.c)):.6f}, "
      f"N_eq={3*R.sse(np.ones(pm.n), pm.c):,.0f}")
t0 = time.time()
succ, passed, audit = R.stage_power(pm, R.A_FLOOR, R.STAGE_P, 1, n_trials=R.N_TRIALS,
                                    confirm_perm=R.MC_CAL_PERM)
print(f"\n=== STAGE P, SELF-VERIFYING, REAL GEOMETRY ({time.time()-t0:.0f}s) ===")
print(f"calibrated successes : {succ}/{R.N_TRIALS}  (pass rule x >= {R.CP_PASS_X})")
print(f"boundary trials      : {audit['boundary_trials']}  confirmed {audit['confirmed']}  "
      f"refuted {len(audit['refuted'])}  (confirm_perm={audit['confirm_perm']:,})")
for r in audit["refuted"][:5]:
    print(f"   REFUTED trial {r['trial']}: p_cal {r['p_calibrated']:.2e} vs p_mc {r['p_monte_carlo']:.2e}")
print(f"VERDICT              : {'PASS' if passed else 'FAIL'}")
