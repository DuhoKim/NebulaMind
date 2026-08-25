#!/usr/bin/env python3
"""Stage P on the REAL selected geometry. Positions and counts only -- no chi, no images."""
import sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ref"))
import successor_ref_v3 as R

HERE = Path(__file__).resolve().parent
d = np.load(HERE / "real_oracle_dr10.npz")
s = np.load(HERE / "real_selection_dr10.npz")
idx = s["selected_idx"]
bid, c, nraw = d["brickid"][idx], d["c"][idx], d["n_eligible"][idx]
nret = R.retained_counts(nraw)
print(f"selected {len(idx):,} bricks, {int(nret.sum()):,} retained planning objects")

pm = R._planning_mask(bid, c, nret)
print(f"planning mask: n={pm.n:,}  Var(c)={float(np.var(pm.c)):.6f}  "
      f"N_eq={3*R.sse(np.ones(pm.n), pm.c):,.0f}")

t0 = time.time()
ref = pm.with_signs(R.inject_signs(pm, R.A_FLOOR, R.STAGE_P, 1, 1))
ref_z = R.reference_null_z(ref, R.STAGE_P, 1)
print(f"measured null: {len(ref_z):,} permutations in {time.time()-t0:.1f}s; "
      f"z* = {float(np.quantile(ref_z, 1-R.P_REPRODUCED)):.4f} "
      f"(normal reference {R.Z_0001:.4f})")

t0 = time.time()
succ = 0
for t in range(1, R.N_TRIALS + 1):
    sm = ref if t == 1 else pm.with_signs(R.inject_signs(pm, R.A_FLOOR, R.STAGE_P, 1, t))
    if R.calibrated_success(sm, ref_z):
        succ += 1
    if t % 200 == 0:
        print(f"  {t}/{R.N_TRIALS} trials, {succ} successes ({time.time()-t0:.0f}s)")
print(f"\n=== STAGE P ON REAL GEOMETRY ===")
print(f"successes {succ}/{R.N_TRIALS}   pass rule x >= {R.CP_PASS_X}   "
      f"=> {'PASS' if succ >= R.CP_PASS_X else 'FAIL'}")
print(f"at the frozen labelling floor a = {R.A_FLOOR}, injected A = {R.A_LONGO}")
