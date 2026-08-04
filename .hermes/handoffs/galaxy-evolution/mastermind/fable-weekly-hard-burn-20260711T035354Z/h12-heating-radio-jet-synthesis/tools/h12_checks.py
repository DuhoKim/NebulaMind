#!/usr/bin/env python3
"""H12 derivation checks: recompute every numeric in the m1_rp3 and m2_p2 artifacts,
verify prose roundings (RCA nearest-rounding convention), and compute the
cross-artifact implied quantities used in the joint synthesis.
Read-only on inputs; prints a report to stdout."""
import json, math

ROOT = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z"
A_PATH = ROOT + "/h5-supplement-value-verification/sources-snapshot/m1_rp3_maintenance_heating/analysis_results.json"
B_PATH = ROOT + "/h5-supplement-value-verification/sources-snapshot/m2_p2_radio_jet_environment/analysis_results.json"

def r3(x):
    return f"{x:.3f}"

def binom_se(p, n):
    return math.sqrt(p * (1 - p) / n)

A = json.load(open(A_PATH))
B = json.load(open(B_PATH))

print("== Artifact A (m1_rp3 maintenance heating) ==")
for key in ("massive_agn_fraction", "massive_quenched_agn_fraction"):
    f = A[key]
    frac = f["k"] / f["n"]
    se = binom_se(frac, f["n"])
    print(f"{key}: k/n = {f['k']}/{f['n']} = {frac:.10f} (stored {f['fraction']:.10f}, "
          f"match {abs(frac - f['fraction']) < 1e-12}); nearest-3dp = {r3(frac)}; "
          f"binomial SE = {se:.9f} (stored {f['se']:.9f}, match {abs(se - f['se']) < 1e-12})")
print(f"massive_rows = {A['massive_rows']}, massive_quenched_rows = {A['massive_quenched_rows']}, "
      f"quenched share of massive = {A['massive_quenched_rows']/A['massive_rows']:.4f}")
k_nq = A["massive_agn_fraction"]["k"] - A["massive_quenched_agn_fraction"]["k"]
n_nq = A["massive_rows"] - A["massive_quenched_rows"]
f_nq = k_nq / n_nq
print(f"IMPLIED massive NON-low-sSFR AGN fraction: {k_nq}/{n_nq} = {f_nq:.4f}")

print()
print("== Artifact B (m2_p2 radio-jet environment) ==")
for key in ("high_density_massive_agn", "low_density_massive_agn"):
    f = B[key]
    frac = f["k"] / f["n"]
    se = binom_se(frac, f["n"])
    print(f"{key}: k/n = {f['k']}/{f['n']} = {frac:.10f} (stored {f['fraction']:.10f}, "
          f"match {abs(frac - f['fraction']) < 1e-12}); nearest-3dp = {r3(frac)}; "
          f"binomial SE = {se:.9f} (stored {f['se']:.9f}, match {abs(se - f['se']) < 1e-12})")
ci = B["high_minus_low_ci"]
print(f"bootstrap high-minus-low CI = [{ci[0]:.10f}, {ci[1]:.10f}] -> nearest-3dp [{r3(ci[0])}, {r3(ci[1])}]")
fh = B["high_density_massive_agn"]; fl = B["low_density_massive_agn"]
diff = fh["fraction"] - fl["fraction"]
se_d = math.sqrt(fh["se"]**2 + fl["se"]**2)
lo, hi = diff - 1.96 * se_d, diff + 1.96 * se_d
print(f"point diff = {diff:.5f}; normal-approx 95% CI = [{lo:.5f}, {hi:.5f}] "
      f"(bootstrap CI contains point diff: {ci[0] < diff < ci[1]})")

print()
print("== Cross-artifact identities and implications ==")
print(f"massive_rows identical A vs B: {A['massive_rows']} vs {B['massive_rows']} -> {A['massive_rows'] == B['massive_rows']}")
print(f"same run_id: {A['run_id'] == B['run_id']} ({A['run_id']})")
print(f"same source_sample: {A['source_sample'] == B['source_sample']}")
print(f"same sample_rows: {A['sample_rows']} vs {B['sample_rows']}")
n_mid = A["massive_rows"] - fh["n"] - fl["n"]
k_mid = A["massive_agn_fraction"]["k"] - fh["k"] - fl["k"]
print(f"IMPLIED middle-half (Q2+Q3) massive AGN fraction: {k_mid}/{n_mid} = {k_mid/n_mid:.4f} "
      f"(between low {fl['fraction']:.3f} and high {fh['fraction']:.3f}: {fl['fraction'] < k_mid/n_mid < fh['fraction']})")
print(f"massive hosts per density quartile: high {fh['n']}, low {fl['n']} "
      f"(unequal -> quartiles NOT defined within the massive subset; if 60k-wide 15,000-quartiles: "
      f"high share {fh['n']/15000:.3f}, low share {fl['n']/15000:.3f}, overall massive share {A['massive_rows']/60000:.3f})")

print()
print("== Composition (mediation) model: can A's quenching lever explain B's gradient? ==")
f_q = A["massive_quenched_agn_fraction"]["fraction"]
for name, f_obs in (("high-density quartile", fh["fraction"]), ("low-density quartile", fl["fraction"])):
    q = (f_obs - f_nq) / (f_q - f_nq)
    print(f"{name}: observed AGN fraction {f_obs:.3f} reproduced by composition alone if "
          f"low-sSFR share q = {q:.3f} (vs overall massive q = {A['massive_quenched_rows']/A['massive_rows']:.3f})")
