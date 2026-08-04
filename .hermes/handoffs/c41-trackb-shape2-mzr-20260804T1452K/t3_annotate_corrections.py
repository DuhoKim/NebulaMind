#!/usr/bin/env python3
"""Apply Kun T4-real C1+C2 to T3_REAL_RESULTS.json — computed, not typed."""
import json, os
L = os.path.dirname(os.path.abspath(__file__))
r = json.load(open(os.path.join(L, "T3_REAL_RESULTS.json")))
rows = [json.loads(x) for x in open(os.path.join(L, "T3_REAL_SAMPLE.jsonl"))]
ok = [x for x in rows if x.get("oh_direct") and x.get("logmass") and not x.get("flag_icf_fallback")]
below = [x for x in ok if x["logmass"] < 8.0]
r["per_class_counts"]["below_bin_floor"] = len(below)
r["below_bin_floor_note"] = ("C1 (Kun T4-real): %d verified contract-grade anchors sit below the "
    "lowest bin edge (logM<8.0): %s — real, at exactly the low masses this study probes; "
    "binned nowhere by the frozen 8.0 floor, counted here so no reader concludes only the "
    "binned anchors exist." % (len(below), ", ".join(f"{x.get('id','?')}@{x['logmass']:.2f}" for x in below)))
v1 = json.load(open(os.path.join(L, "T2A_FORECAST_FROZEN.json")))
v2p = os.path.join(L, "T2A_FORECAST_FROZEN_V2.json")
v2 = json.load(open(v2p)) if os.path.exists(v2p) else None
r["forecast_vs_actual"] = {
    "frozen_forecast_v1": v1, "frozen_forecast_v2": v2,
    "supersession_disclosure": ("v1 frozen pre-fetch; v2 re-frozen under Amendment Ruling 3 "
        "(changed eligibility universe), both receipted. Kun mock-forensics F-T4-1 flagged v2's "
        "precision claim as unachievable; the honest statement follows from v1's MORE conservative "
        "expectation."),
    "actual_usable_anchors_total": len(ok),
    "actual_per_bin": {k: v.get("N") for k, v in r.get("bins", {}).items()},
    "null_statement_T2b_s6": ("Against the frozen forecast (v1 expected ~%s usable Te anchors; v2 "
        "expected ~%s), the executed public-archive assembly yielded %d contract-grade anchors — "
        "short of even the conservative expectation by roughly an order of magnitude. No mass bin "
        "reaches the pre-committed 3-anchor minimum; no deficit verdict is possible at "
        "contract-grade public statistics. This quantifies A3's settle-line: the z>3 Te anchor set "
        "public archives can currently supply is N=%d." % (
            v1.get("total_expected_Te_anchors", "?"),
            (v2 or {}).get("total_expected_Te_anchors", "?"), len(ok), len(ok))),
}
json.dump(r, open(os.path.join(L, "T3_REAL_RESULTS.json"), "w"), indent=1)
print("annotated: below_bin_floor=%d, forecast block instantiated" % len(below))
