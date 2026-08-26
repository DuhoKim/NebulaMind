from pathlib import Path
import math
import compute_blind_p2b as model

eta, sqn = model.load_orbit(Path("../../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv").resolve())
eta0 = model.brentq(lambda e: model.ETA_OBS-e-e*float(sqn(e)), float(eta[0]), model.ETA_OBS*(1-1e-10))
r0 = eta0*float(sqn(eta0))
mean, coeff, max_delta = model.multipoles(0.0, sqn, float(eta[0]), r0, nmu=256)
print("center_max_abs_delta", max_delta)
print("center_a1_to_a4", coeff[1:].tolist())
for tau, q in [(0,0), (0,1), (.15,0), (.15,1)]:
    weight = math.exp(-tau)/(math.exp(-tau)+(1-math.exp(-tau))*q)
    print("source_weight", tau, q, weight)
assert max_delta < 1e-14
assert max(abs(coeff[1:])) < 1e-13
assert abs(math.exp(-.15)-0.8607079764250578) < 1e-15
print("ALL_CHECKS_PASS")
