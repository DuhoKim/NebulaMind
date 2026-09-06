#!/usr/bin/env python3
"""V31 gate repairs: codex F1 (merge preserves origin_search_alt; compare checks the matched branch's search), F2 (structural comparison of origin_search), C1 (README probe contract). Tools + kit; text in write_v32."""
import io,re
def rep(t,a,b):
    assert t.count(a)==1,(a[:70],t.count(a)); return t.replace(a,b)
# ---- lane tool: merge preserves the alternative branch's origin_search when it uses ORIG_SILENT
Lt="r3c2_lane_tools.py"; l=io.open(Lt,encoding="utf-8").read()
l=rep(l,'''        if Bm[k]["origin"]!=A[k]["origin"]:
            r["origin_alt"]=Bm[k]["origin"]; r["origin_evidence_alt"]=Bm[k]["origin_evidence"]; ndis+=1''',
'''        if Bm[k]["origin"]!=A[k]["origin"]:
            r["origin_alt"]=Bm[k]["origin"]; r["origin_evidence_alt"]=Bm[k]["origin_evidence"]; ndis+=1
            if (Bm[k].get("origin_evidence") or {}).get("reason_code")=="ORIG_SILENT" and "origin_search" in Bm[k]: r["origin_search_alt"]=Bm[k]["origin_search"]  # PROBE:MERGE_SEARCH_ALT''')
l=l.replace('r.pop("origin_alt",None); r.pop("origin_evidence_alt",None); r.pop("derived_from_alt",None); r.pop("PARENTS_DISPUTED",None)','r.pop("origin_alt",None); r.pop("origin_evidence_alt",None); r.pop("origin_search_alt",None); r.pop("derived_from_alt",None); r.pop("PARENTS_DISPUTED",None)',1)
io.open(Lt,"w",encoding="utf-8").write(l)
# ---- seat tool: compare checks the matched branch's search structurally (JSON equality, not string display)
S="r3c2_ledger_tools.py"; s=io.open(S,encoding="utf-8").read()
s=rep(s,'''        if aev.get("reason_code")=="ORIG_SILENT" and str(ar.get("origin_search"))!=str(sr.get("origin_search")): diffs.append("origin_search differs")''',
'''        if aev.get("reason_code")=="ORIG_SILENT":
            expected_search = sr.get("origin_search_alt") if (branch=="alt" and sr.get("origin_alt")) else sr.get("origin_search")
            if ar.get("origin_search")!=expected_search: diffs.append("origin_search differs (structural comparison against the matched branch's search)")  # PROBE:C6_SEARCH_BRANCH''')
# the complete-alternative predicate must also require the alternative's search when the alternative uses ORIG_SILENT
s=rep(s,'''        matches_alt=has_alt and str(ar.get("origin"))==alt_origin_full and all(str(aev.get(f2))==str(alt_ev_full.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim")) and a_par==alt_par_full''',
'''        matches_alt=has_alt and str(ar.get("origin"))==alt_origin_full and all(str(aev.get(f2))==str(alt_ev_full.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim")) and a_par==alt_par_full and (alt_ev_full.get("reason_code")!="ORIG_SILENT" or ar.get("origin_search")==(sr.get("origin_search_alt") if sr.get("origin_alt") else sr.get("origin_search")))
        matches_primary=matches_primary and (sev.get("reason_code")!="ORIG_SILENT" or ar.get("origin_search")==sr.get("origin_search"))''')
io.open(S,"w",encoding="utf-8").write(s)
# the validator's schema allows origin_search_alt on merged (lane-side) ledgers only: validate rejects extra fields on SEAT ledgers — merged ledgers never pass through validate, so nothing to change; the sealed ledger given to compare is the merged one.
# ---- README: the probe contract as it actually is
Rm="r3c2_staged_d1d7/README_STAGED_UNADOPTED.md"; r=io.open(Rm,encoding="utf-8").read()
r=re.sub(r"deletion probes \(the check on a marked line\s+is neutralised in a copy of the tool; the matching negative must then PASS\)","deletion probes (the check on a marked line is neutralised in a copy of the tool; the matching negative must then either PASS or, where an authoritative guard overlaps the neutralised diagnostic, still FAIL on that guard with the diagnostic line absent — a guard is never weakened to make a probe killable)",r,count=1)
io.open(Rm,"w",encoding="utf-8").write(r)
print("gate-7 repairs applied to lane tool, seat tool, README")
