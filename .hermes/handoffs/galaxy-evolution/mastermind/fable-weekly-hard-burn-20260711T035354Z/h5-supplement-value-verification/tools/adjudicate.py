#!/usr/bin/env python3
"""H5 adjudication layer over RESULTS_RAW.json (verify_values.py output).

Applies documented validity rules to raw occurrence matches, dismisses
false-positive near-misses with stated reasons, annotates every ABSENT value
as expected/unexpected, and emits RESULTS_ADJUDICATED.json plus a console
summary. Rules are explicit so the adjudication is reproducible.
"""
import json
from pathlib import Path

OWN = Path(__file__).resolve().parent.parent
raw = json.load(open(OWN / "RESULTS_RAW.json"))

# Comma-grouped counts that are shared-denominator quantities: an exact string
# match anywhere in the supplement is semantically unambiguous (cross-reference).
SHARED_COUNTS = {"60,000", "9,298", "5,695", "6,729", "8,146", "4,440",
                 "15,000", "3,456", "2,710"}
# Mass-bin edges shared between m2_p3 by-mass arrays and the m3_p3
# simulation-vector table (same binning scheme).
BIN_EDGES = {"8.0", "9.5", "10.0", "10.5", "11.0", "12.5"}

# Explicit per-occurrence VALID overrides: (slug, path, line, raw) -> reason
VALID_OVERRIDES = {
    # L92 "...0.032 +/- 0.004, corresponding to an approximate 3.2
    # percentage-point increase..." — explicit x100 restatement.
    ("m1_rp2_environment_quenching", "lpm_high_density_coeff", 92, "3.2"):
        "explicit percentage-point restatement of 0.032",
    ("m1_rp2_environment_quenching", "result_bullets[3]<text>", 92, "3.2"):
        "explicit percentage-point restatement of 0.032",
    # L158 references the log Mstar >= 10.8 maintenance-heating subset.
    ("m1_rp3_maintenance_heating", "result_bullets[0]<text>", 158, "10.8"):
        "cross-reference to the 10.8 threshold in the m3_p2 note",
    # P1 RCA sect 2.3: L169 'Across mass bins' spans are the min/max of the
    # per-mass-bin arrays; m2_p3 array endpoints are the same quantities.
    ("m2_p3_feedback_transition_mass", "agn_fraction_by_mass[0]", 169, "0.003"):
        "L169 span minimum = this array's min (RCA sect 2.3 referent)",
    ("m2_p3_feedback_transition_mass", "agn_fraction_by_mass[4]", 169, "0.520"):
        "L169 span maximum = this array's max (RCA sect 2.3 referent)",
    ("m2_p3_feedback_transition_mass", "quenched_fraction_by_mass[0]", 169, "0.005"):
        "L169 span minimum = this array's min (RCA sect 2.3 referent)",
    ("m2_p3_feedback_transition_mass", "quenched_fraction_by_mass[4]", 169, "0.729"):
        "L169 span maximum = this array's max (RCA sect 2.3 referent)",
}

# Near-miss dismissals: (slug, path-prefix, line, raw) -> reason
NEAR_DISMISS = {
    (92, "0.004"): "L92's 0.004 is the LPM SE (different referent), "
                   "coincidentally 1 ulp from this binomial SE",
    (93, "0.02"): "L93's 0.02 is the redshift-slice lower edge 0.02<z<0.12, "
                  "not a rendering of this value",
    (136, "0.5"): "L136's 0.5 is the artifact's own transition threshold "
                  "(transition_mass_bin_quenched_fraction_gt_0p5); the flagged "
                  "bin-4 fractions are never quoted in prose",
    (158, "40.061"): "prose 40.061 is the correct 3-dp nearest-rounding of raw "
                     "leaf 40.06117405071403; the artifact bullet's own 2-dp "
                     "string 40.06 is a coarser rounding of the same value — "
                     "precision-choice difference, not numeric drift (same "
                     "re-derive-from-raw signature as P1 RCA sect 3)",
}

SPAN_ONLY = {
    "m2_p3_feedback_transition_mass": "prose quotes the threshold-crossing bin,"
        " the peak bin, and the across-bins spans (L169); interior-bin values"
        " are never quoted",
    "m3_p1_multiphase_census": "prose quotes the census span endpoints"
        " (0.136 to 0.418) and their ratio; interior tracer fractions are"
        " never quoted",
}


def absent_reason(slug, v, doc="supplement"):
    p, canon = v["path"], v["canon"]
    if doc != "supplement":
        return ("expected", "stretch scope: the flagship is the RP-1 paper "
                            "and only cross-references shared denominators; "
                            "topic-specific atlas values are not expected "
                            "there")
    if v.get("se") or p.endswith(".se"):
        return ("expected", "standard errors are never quoted in the atlas")
    if ".k" in p or p.endswith(".n") or "rows" in p:
        return ("expected", "numerator/denominator count behind a quoted "
                            "fraction; the atlas quotes fractions plus the "
                            "denominators it names, not every k/n")
    if slug in SPAN_ONLY and ("_by_mass" in p or "tracer_prevalence" in p):
        return ("expected", SPAN_ONLY[slug])
    if p == "result_bullets[1]<text>" and canon == "40.06":
        return ("expected", NEAR_DISMISS[(158, "40.061")])
    return ("UNEXPECTED", "no rule covers this absence — review")


out = {}
for doc, topics in raw.items():
    out[doc] = {}
    for slug, rep in topics.items():
        rows = []
        for v in rep["values"]:
            valid, invalid = [], []
            for o in v["occ"]:
                key = (slug, v["path"], o["line"], o["raw"])
                if key in VALID_OVERRIDES:
                    o["why"] = VALID_OVERRIDES[key]
                    o["xref"] = not o["in_scope"]
                    valid.append(o)
                elif o["kind"] == "percent_x100":
                    o["why"] = ("dismissed: bare token without percent "
                                "context (bibliography volume numbers, S/N "
                                "thresholds, unrelated tokens)")
                    invalid.append(o)
                elif o["in_scope"]:
                    o["xref"] = False
                    valid.append(o)
                elif o["kind"] in ("exact", "int") and o["raw"] in SHARED_COUNTS:
                    o["why"] = "shared-denominator count; exact grouped string"
                    o["xref"] = True
                    valid.append(o)
                elif o["kind"] in ("exact",) and o["raw"] in BIN_EDGES and \
                        slug == "m2_p3_feedback_transition_mass":
                    o["why"] = ("shared mass-bin edge (same binning scheme "
                                "as the simulation-vector table)")
                    o["xref"] = True
                    valid.append(o)
                else:
                    o["why"] = "dismissed: out-of-section rounded coincidence"
                    invalid.append(o)
            near = []
            for n in v["near"]:
                n["why"] = NEAR_DISMISS.get(
                    (n["line"], n["raw"]), "UNREVIEWED near-miss")
                near.append(n)
            if valid:
                cls = "PASS"
                note = ""
            elif any(n["why"] == "UNREVIEWED near-miss" for n in near):
                cls = "DRIFT"
                note = "unreviewed near-miss"
            else:
                cls = "ABSENT"
                exp, why = absent_reason(slug, v, doc)
                note = f"{exp}: {why}"
            rows.append(dict(path=v["path"], canon=v["canon"], cls=cls,
                             note=note, valid=valid, invalid=invalid,
                             near=near))
        n = len(rows)
        p = sum(1 for r in rows if r["cls"] == "PASS")
        d = sum(1 for r in rows if r["cls"] == "DRIFT")
        a = sum(1 for r in rows if r["cls"] == "ABSENT")
        au = sum(1 for r in rows if r["cls"] == "ABSENT"
                 and r["note"].startswith("UNEXPECTED"))
        cov = sum(1 for r in rows
                  if any(o["manifest"] for o in r["valid"]))
        nocov = [
            dict(path=r["path"], line=o["line"], raw=o["raw"])
            for r in rows for o in r["valid"] if not o["manifest"]
        ]
        out[doc][slug] = dict(n=n, PASS=p, DRIFT=d, ABSENT=a,
                              ABSENT_unexpected=au, manifest_covered=cov,
                              uncovered_valid_occurrences=nocov, values=rows)

(OWN / "RESULTS_ADJUDICATED.json").write_text(json.dumps(out, indent=1))

for doc, topics in out.items():
    print(f"=== {doc} ===")
    tot = dict(n=0, PASS=0, DRIFT=0, ABSENT=0, cov=0, nocov=0)
    for slug, r in topics.items():
        print(f"| {slug} | {r['n']} | {r['PASS']} | {r['DRIFT']} | "
              f"{r['ABSENT']} ({r['ABSENT_unexpected']} unexpected) | "
              f"{r['manifest_covered']} | {len(r['uncovered_valid_occurrences'])} |")
        tot["n"] += r["n"]; tot["PASS"] += r["PASS"]; tot["DRIFT"] += r["DRIFT"]
        tot["ABSENT"] += r["ABSENT"]; tot["cov"] += r["manifest_covered"]
        tot["nocov"] += len(r["uncovered_valid_occurrences"])
    print(f"| TOTAL | {tot['n']} | {tot['PASS']} | {tot['DRIFT']} | "
          f"{tot['ABSENT']} | {tot['cov']} | {tot['nocov']} |")
    for slug, r in topics.items():
        for v in r["values"]:
            if v["cls"] == "DRIFT" or v["note"].startswith("UNEXPECTED"):
                print(f"  !! {slug} {v['path']} {v['cls']} {v['note']}")
        for o in r["uncovered_valid_occurrences"]:
            print(f"  addcand? {slug} {o}")
