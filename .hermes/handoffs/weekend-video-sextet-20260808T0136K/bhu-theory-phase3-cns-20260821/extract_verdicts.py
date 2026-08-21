#!/usr/bin/env python3
"""Phase 3 verdict rows -> verdicts.json, same contract as Phase 2.

load_bearing is declared HERE, at authoring time, per the Phase 3 brief — Phase 2
designated them after the fact and that weakened the claim.
"""
import json, re, hashlib, pathlib

LOAD_BEARING = {
 "B-2":  "link (1), the vector manifestation, imported by citation",
 "B-4":  "link (2)'s density n_c ~ 3n0 is cited, never computed here",
 "B-5":  "link (3), M_max ~ 1.5 Msun — the number the falsifier tests — is imported",
 "B-17": "link (4): that CNS requires a low M_max",
}

# Gate A (HOLD_P3A_LOADBEARING) removed three rows from the load-bearing set and I accept all three:
#   B-9  (the Section III entropy remark) — BLR title it with "~=" and explicitly decline to address
#        CNS's mechanism, so it is a motivating gloss, not a step the falsifier runs through;
#   B-12 (the carbon/LUM argument) — it bounds M_max from BELOW, and neither limb of the falsifier
#        that actually fired tests a lower bound;
#   B-18 (the Smolin quotation) — UNVERIFIED-AT-GATE is an unread citation, not a failure, and
#        counting it as one was the tally leaning on it in exactly the way the prose refuses to.
SECONDARY = {
 "B-9":  "motivating gloss, not on the falsifier's critical path (Gate A)",
 "B-12": "bounds M_max from below; the fired falsifier does not test that (Gate A)",
}
UNVERIFIED = {"B-18": "quoted from sources not yet read; neither a pass nor a failure"}
PASSING = {"CHECK", "CHECK-AS-MECHANISM", "CHECK-AS-ASTROPHYSICS",
           "CHECK-AS-REPORTED", "CHECK-AS-OF-2008"}

src = pathlib.Path("TRACK_A_AUDIT.md")
rows = []
for line in src.read_text().splitlines():
    if not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 4 or not re.match(r"^B-\d+$", cells[0]):
        continue
    v = cells[2]
    rows.append({
        "id": cells[0], "claim": cells[1], "verdict": v, "verdict_raw": v,
        "passing": v in PASSING,
        "load_bearing": cells[0] in LOAD_BEARING,
        "load_bearing_why": LOAD_BEARING.get(cells[0]),
        "secondary_why": SECONDARY.get(cells[0]),
        "unverified": cells[0] in UNVERIFIED,
        "unverified_why": UNVERIFIED.get(cells[0]),
        "section": "Brown, Lee & Rho 2008 (PRL 101, 091101)",
    })

tally = {}
for r in rows:
    tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1

doc = {
 "generated_by": "Tori / BHU lane, Phase 3 Track A",
 "contract": [
  "A CHECK means the step reproduces. It does NOT mean the paper's conclusion holds.",
  "Do not render a pass percentage from this file.",
  "Rank or colour by load_bearing first, verdict second.",
  "There is no failing count. An imported citation is not a defect in a 4-page note, and an "
  "UNVERIFIED row is an unread source, not a failure. Do not derive one.",
 ],
 "audits": {"P3A": {
   "label": "Phase 3 Track A — Brown, Lee & Rho 2008 (the CNS falsifier paper)",
   "source_file": "TRACK_A_AUDIT.md",
   "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
   "n_rows": len(rows),
   "tally": dict(sorted(tally.items(), key=lambda kv: -kv[1])),
   "n_load_bearing": sum(1 for r in rows if r["load_bearing"]),
   # NOT "failing". Gate A: the prose calls citation-import normal practice for a 4-page note
   # while the tally called the same rows failures; both cannot be the register of record.
   # What is true and non-pejorative: these load-bearing links are imported, not derived here.
   "n_load_bearing_imported": sum(1 for r in rows if r["load_bearing"] and not r["passing"]),
   "n_unverified": sum(1 for r in rows if r["unverified"]),
   "rows": rows,
 }},
}
pathlib.Path("verdicts.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False))
a = doc["audits"]["P3A"]
print(f"{a['n_rows']} rows | load-bearing {a['n_load_bearing']}, "
      f"of which imported-not-derived: {a['n_load_bearing_imported']} | "
      f"unverified: {a['n_unverified']}")
print(a["tally"])
missing = set(LOAD_BEARING) - {r["id"] for r in rows}
print("declared load-bearing not found in table:", missing or "none")
