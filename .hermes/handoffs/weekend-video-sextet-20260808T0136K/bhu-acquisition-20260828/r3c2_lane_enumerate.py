#!/usr/bin/env python3
"""r3c2_lane_enumerate.py — the LANE's blind second route for limb A only (R3C2 run plan step 1). Sealed before dispatch,
opened after the tally (step 12), NEVER merged into the tally. Mechanical: a candidate is a non-blank line of a pinned text that
(a) contains a numeral with a decimal point, exponent or ×10^ form, or an integer followed by a unit token, and (b) contains a
result cue ("we find|we obtain|we get|our result|gives|yields|predict|estimate|approximately|≈|= ") and (c) is not excluded by a
crude kind test: years 1900–2099 alone, bracketed reference numbers, equation labels "(n.m)", page/line numbers, dates.
Output: candidates.json + exclusions.json in the census schema (declared counts), all included candidates outcome PENDING.
This is a heuristic scanner; it is compared to the seats' denominator at step 12 by set difference only."""
import re, json, sys, pathlib
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
man = pathlib.Path("R3C2_CORPUS_MANIFEST.md").read_text(encoding="utf-8")
files = re.findall(r"`([^`]+_clean\.txt)`", man)
NUM = re.compile(r"(?<![\w.])(\d+\.\d+(?:\s*[×x]\s*10\s*\^?\s*[−-]?\d+|e[−-]?\d+)?|\d+\s*[×x]\s*10\s*\^?\s*[−-]?\d+|\d+(?=\s*(?:M☉|Msun|M_\{?⊙|kg|K\b|Gyr|Myr|Mpc|kpc|km|s⁻¹|eV|GeV|MeV|Hz|σ|%|degrees|°)))")
CUE = re.compile(r"we (?:find|obtain|get|derive|estimate|predict)|our (?:result|estimate|prediction)|gives|yields|predict|approximately|≈|=\s*\d", re.I)
EXCL_YEAR = re.compile(r"^\D*(19|20)\d\d\D*$"); REF = re.compile(r"\[\d+(?:[,–-]\s*\d+)*\]"); EQL = re.compile(r"\(\d+(?:\.\d+)?\)\s*$")
cands, excls, cid = [], [], 0
for f in files:
    p = src / f
    if not p.exists(): continue
    for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
        if not line.strip(): continue
        nums = NUM.findall(line)
        if not nums: continue
        cid += 1; numeral = nums[0].strip()
        rec = {"candidate_id": f"L{cid:05d}", "source_file": f, "source_line": i, "numeral": numeral}
        if EXCL_YEAR.match(line): kind = "DATE"
        elif REF.search(line) and not CUE.search(line): kind = "REFERENCE_NUMBER"
        elif EQL.search(line) and not CUE.search(line): kind = "EQUATION_NUMBER"
        elif not CUE.search(line): kind = "ATTRIBUTED_NOT_DERIVED"
        else: kind = None
        if kind: rec["included"] = False; cands.append(rec); excls.append({"candidate_id": rec["candidate_id"], "kind": kind})
        else: rec.update({"included": True, "attempts": 0, "outcome": "PENDING"}); cands.append(rec)
inc = sum(1 for c in cands if c["included"])
json.dump({"declared_candidate_count": len(cands), "declared_included_count": inc, "declared_excluded_count": len(excls), "declared_attempt_count": 0, "candidates": cands}, open(out/"candidates.json", "w"), indent=1)
json.dump({"declared_exclusion_count": len(excls), "exclusions": excls}, open(out/"exclusions.json", "w"), indent=1)
print(f"texts={len(files)} candidates={len(cands)} included={inc} excluded={len(excls)}")
