#!/usr/bin/env python3
"""H14 joint cross-checks: m3_p1 multiphase census vs m3_p2 gas depletion efficiency.

Offline only. Reads the two hash-verified snapshot artifacts, recomputes every
derived numeric used in the cycle-5 supplement, and prints the joint
census<->depletion consistency arithmetic. No writes outside stdout.
"""
import json, math

ROOT = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z"
P1 = f"{ROOT}/h5-supplement-value-verification/sources-snapshot/m3_p1_multiphase_census/analysis_results.json"
P2 = f"{ROOT}/h5-supplement-value-verification/sources-snapshot/m3_p2_gas_depletion_efficiency/analysis_results.json"

p1 = json.load(open(P1))
p2 = json.load(open(P2))

def se_binom(p, n):
    return math.sqrt(p * (1 - p) / n)

print("== A. Artifact-internal recomputation (unit audit) ==")
tot = 0.0
for name, t in sorted(p1["tracer_prevalence"].items(), key=lambda kv: kv[1]["fraction"]):
    f = t["k"] / t["n"]
    se = se_binom(f, t["n"])
    ok_f = abs(f - t["fraction"]) < 1e-12
    ok_se = abs(se - t["se"]) < 1e-9
    tot += f
    print(f"  {name:<18} k={t['k']:>6} n={t['n']} f={f:.6f} (stored {t['fraction']:.6f} {'OK' if ok_f else 'MISMATCH'}) "
          f"se={se:.7f} ({'OK' if ok_se else 'MISMATCH'})")
print(f"  sum of 5 tracer fractions = {tot:.4f}  (>1 => tracer sets overlap; NOT a partition — sums need not be 1)")
lo = min(t["fraction"] for t in p1["tracer_prevalence"].values())
hi = max(t["fraction"] for t in p1["tracer_prevalence"].values())
ratio = hi / lo
print(f"  widest/narrowest = {hi:.6f}/{lo:.6f} = {ratio:.9f} (stored {p1['prevalence_ratio_widest_to_narrowest']:.9f} "
      f"{'OK' if abs(ratio - p1['prevalence_ratio_widest_to_narrowest']) < 1e-9 else 'MISMATCH'})")

a = p2["agn_fraction_in_denominator"]
f2 = a["k"] / a["n"]
se2 = se_binom(f2, a["n"])
print(f"  p2 AGN fraction: {a['k']}/{a['n']} = {f2:.7f} (stored {a['fraction']:.7f} "
      f"{'OK' if abs(f2 - a['fraction']) < 1e-12 else 'MISMATCH'}), se={se2:.9f} "
      f"({'OK' if abs(se2 - a['se']) < 1e-9 else 'MISMATCH'})")
print(f"  p2 denominator rows: {p2['massive_transition_quenched_rows']} of parent {p2['sample_rows']} "
      f"= {p2['massive_transition_quenched_rows']/p2['sample_rows']:.4f} of common denominator")

print("\n== B. Supplement rounding derivations (grade-B evidence) ==")
for label, raw, nd, expect in [
    ("SUP-TRACER-LO 0.136", lo, 3, "0.136"),
    ("SUP-TRACER-HI 0.418", hi, 3, "0.418"),
    ("SUP-TRACER-RATIO 3.1", ratio, 1, "3.1"),
    ("SUP-GAS-BPT 0.549", a["fraction"], 3, "0.549"),
    ("SUP-GAS-LHA 40.061", p2["median_log_lha_denominator"], 3, "40.061"),
    ("SUP-GAS-DEX 0.66", abs(p2["median_log_lha_offset_vs_massive_sf"]), 2, "0.66"),
]:
    got = f"{raw:.{nd}f}"
    print(f"  {label:<22} raw={raw:.10f} -> round({nd}dp)={got}  {'OK' if got == expect else 'MISMATCH vs prose ' + expect}")

print("\n== C. Joint census <-> depletion cross-checks ==")
bpt = p1["tracer_prevalence"]["BPT AGN"]
lowssfr = p1["tracer_prevalence"]["low-sSFR+emission"]
red = p1["tracer_prevalence"]["red+emission"]
k2 = a["k"]
print(f"  C1 shared parent: p1 sample_rows={p1['sample_rows']}, p2 sample_rows={p2['sample_rows']}, "
      f"same run_id={p1['run_id'] == p2['run_id']}, same source_sample={p1['source_sample'] == p2['source_sample']}")
print(f"  C2 BPT AGN counts: census k={bpt['k']} (60k); depletion-subset AGN k={k2} (of {a['n']}). "
      f"Subset condition k2<=k1: {'OK' if k2 <= bpt['k'] else 'VIOLATED'}")
print(f"     -> implied share of ALL census BPT AGN residing in the 6,729 subset = {k2}/{bpt['k']} = {k2/bpt['k']:.4f}")
print(f"  C3 flagship linkage: census BPT AGN k={bpt['k']} vs flagship matched-pair count 8,146: "
      f"{'IDENTICAL' if bpt['k'] == 8146 else 'DIFFERENT'}")
print(f"  C4 nesting vs low-sSFR+emission tracer: 6,729 <= {lowssfr['k']}: "
      f"{'OK (necessary cond.)' if 6729 <= lowssfr['k'] else 'VIOLATED'}; share if nested = {6729/lowssfr['k']:.4f}")
print(f"  C5 nesting vs red+emission tracer: 6,729 <= {red['k']}: "
      f"{'OK (necessary cond.)' if 6729 <= red['k'] else 'VIOLATED'}")
enh = a["fraction"] / bpt["fraction"]
print(f"  C6 AGN enhancement in quenched/transition subset: {a['fraction']:.4f}/{bpt['fraction']:.4f} = {enh:.4f}x")
ha_factor = 10 ** abs(p2["median_log_lha_offset_vs_massive_sf"])
ha_factor_2dp = 10 ** 0.66
print(f"  C7 Halpha-proxy suppression factor: 10^{abs(p2['median_log_lha_offset_vs_massive_sf']):.4f} = {ha_factor:.3f}x "
      f"(prose 2dp: 10^0.66 = {ha_factor_2dp:.3f}x)")
print(f"     -> IF SFR ~ LHa and gas mass were EQUAL, t_dep(quenched)/t_dep(SF) ~ {ha_factor:.2f}; "
      f"IF t_dep equal, M_gas lower by ~{ha_factor:.2f}x. Degenerate without CO/HI (artifact guard).")
print(f"  C8 sanity vs m3_p3 mass-bin BPT fractions (supplement Table, 10.5-12.5 bins span 0.209-0.610): "
      f"0.549 within bracket: {'OK' if 0.209 <= a['fraction'] <= 0.610 else 'OUT OF RANGE'}")
