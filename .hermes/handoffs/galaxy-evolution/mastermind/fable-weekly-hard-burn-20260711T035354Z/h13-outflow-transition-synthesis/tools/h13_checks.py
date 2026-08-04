#!/usr/bin/env python3
"""H13 offline arithmetic checks for m2_p1 + m2_p3 (hash-pinned snapshot inputs only).

Recomputes every derived numeral used in OUTFLOW_TRANSITION_MASS_SYNTHESIS.md:
exact fraction, binomial SE, nearest-rounding of graded-B strings, argmax/threshold
bins, spans, monotonicity, and the implied subset-vs-all sSFR gap.
Exits non-zero on any failure. No network, no writes.
"""
import json, math, sys

ROOT = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/fable-weekly-hard-burn-20260711T035354Z"
A_PATH = ROOT + "/h5-supplement-value-verification/sources-snapshot/m2_p1_outflow_escape_recycling/analysis_results.json"
B_PATH = ROOT + "/h5-supplement-value-verification/sources-snapshot/m2_p3_feedback_transition_mass/analysis_results.json"

fails = []
def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))
    if not cond:
        fails.append(name)

def nearest(x, dp):
    # decimal nearest-rounding as used by the RCA convention (round-half-away is
    # irrelevant here: no half-ties occur among these values)
    return f"{x:.{dp}f}"

A = json.load(open(A_PATH))
B = json.load(open(B_PATH))

# --- Artifact A ---
h = A["high_excitation_agn"]
chk("A: k/n exact fraction", h["k"] / h["n"] == h["fraction"] == 0.074,
    f"{h['k']}/{h['n']} = {h['k']/h['n']}")
se = math.sqrt(h["fraction"] * (1 - h["fraction"]) / h["n"])
chk("A: binomial SE matches stored se", math.isclose(se, h["se"], rel_tol=1e-12),
    f"recomputed {se!r} vs stored {h['se']!r}")
chk("A: -11.53 is nearest 2dp of subset median",
    nearest(A["median_log_sSFR_high_excitation"], 2) == "-11.53",
    repr(A["median_log_sSFR_high_excitation"]))
chk("A: -10.14 is nearest 2dp of full median",
    nearest(A["median_log_sSFR_all"], 2) == "-10.14",
    repr(A["median_log_sSFR_all"]))
gap = A["median_log_sSFR_high_excitation"] - A["median_log_sSFR_all"]
chk("A: implied subset-vs-all gap = -1.391465 dex",
    math.isclose(gap, -1.391465, abs_tol=1e-9), f"{gap!r}")
kin_keys = [k for k in A if any(w in k.lower() for w in ("vel", "esc", "halo", "mass_bin"))]
chk("A: contains no kinematic/mass fields", kin_keys == [], repr(kin_keys))

# --- Artifact B ---
agn = B["agn_fraction_by_mass"]; qf = B["quenched_fraction_by_mass"]; labels = B["mass_bin_labels"]
chk("B: 5 bins, labels as documented",
    labels == ["8.0-9.5", "9.5-10.0", "10.0-10.5", "10.5-11.0", "11.0-12.5"])
widths = []
for lab in labels:
    lo, hi = (float(v) for v in lab.split("-"))
    widths.append(round(hi - lo, 2))
chk("B: uneven bin widths 1.5/0.5/0.5/0.5/1.5 dex", widths == [1.5, 0.5, 0.5, 0.5, 1.5], repr(widths))
chk("B: all fractions in [0,1]", all(0 <= v <= 1 for v in agn + qf))
chk("B: both curves strictly increasing",
    all(a < b for a, b in zip(agn, agn[1:])) and all(a < b for a, b in zip(qf, qf[1:])))
chk("B: peak_agn_fraction equals max & argmax bin is 11.0-12.5",
    B["peak_agn_fraction"] == max(agn) == agn[4] and B["peak_agn_mass_bin"] == "11.0-12.5")
first = next(lab for lab, v in zip(labels, qf) if v > 0.5)
chk("B: first quenched>0.5 bin matches field",
    first == B["transition_mass_bin_quenched_fraction_gt_0p5"] == "11.0-12.5",
    f"qf[3]={qf[3]!r} < 0.5 < qf[4]={qf[4]!r}")
chk("B: 0.520 is nearest 3dp of peak", nearest(B["peak_agn_fraction"], 3) == "0.520",
    repr(B["peak_agn_fraction"]))
chk("B: SUP:169 quenched span 0.005-0.729",
    (nearest(min(qf), 3), nearest(max(qf), 3)) == ("0.005", "0.729"))
chk("B: SUP:169 AGN span 0.003-0.520",
    (nearest(min(agn), 3), nearest(max(agn), 3)) == ("0.003", "0.520"))
chk("B: no per-bin counts stored (SEs uncomputable offline)",
    not any("count" in k.lower() or k in ("k", "n_by_mass") for k in B), )

# --- Joint ---
chk("Joint: same denominator and source sample",
    A["sample_rows"] == B["sample_rows"] == 60000 and A["source_sample"] == B["source_sample"])
chk("Joint: same run_id", A["run_id"] == B["run_id"] == "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z")

print()
print(f"{'ALL CHECKS PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
sys.exit(1 if fails else 0)
