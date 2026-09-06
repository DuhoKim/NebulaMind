#!/usr/bin/env python3
"""V32 gate repair as ONE PATTERN (Blanc 04:37): SEAT-PERMUTATION INVARIANCE (SPI) — the audit verdict is invariant under permutation of the census seats.
Single enforcement point: `merge`. It (1) preserves the second branch whenever origin, evidence, a required search or the parent set differs (equal origin
labels included) and (2) chooses the PRIMARY branch by a seat-blind canonical key (the lexicographically smaller sha256 of each seat's canonical-JSON
record), so the merged ledger is a function of the SET of the two seat records — no downstream step (compare, compute, roots, report ordering) can observe
which seat came first. The origin-disagreement count and the authoritative full-record guard are unchanged."""
import io,re
def rep(t,a,b):
    assert t.count(a)==1,(a[:70],t.count(a)); return t.replace(a,b)
Lt="r3c2_lane_tools.py"; l=io.open(Lt,encoding="utf-8").read()
l=rep(l,'''def cmd_merge(a,b,out):''','''def canon_key(r):
    """seat-blind canonical key of one seat's record: sha256 of its canonical JSON (sorted keys, no whitespace)"""
    import hashlib
    return hashlib.sha256(json.dumps(r,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def cmd_merge(a,b,out):''')
l=rep(l,'''    out_recs=[]; ndis=0; npar=0; fails=[]
    for k in sorted(A):''','''    out_recs=[]; ndis=0; npar=0; fails=[]
    # SPI enforcement: for every input the two seat records are ordered by their seat-blind canonical key; the smaller key is the PRIMARY branch.
    # Everything below reads P (primary) and Q (secondary) — never A/B — so the merged ledger is identical for merge(A,B) and merge(B,A).
    for k in sorted(A):
        P,Q=(A[k],Bm[k]) if canon_key(A[k])<=canon_key(Bm[k]) else (Bm[k],A[k])  # PROBE:SPI_CANONICAL''')
l=rep(l,'''        for fld in ("status","value","source_file","source_line","symbol"):
            if str(A[k].get(fld))!=str(Bm[k].get(fld)): fails.append(f"{k}: seats disagree on {fld} ({A[k].get(fld)!r} vs {Bm[k].get(fld)!r}) — a value/status/coordinate disagreement is not silently resolved")  # PROBE:MERGE_FIELDS''',
'''        for fld in ("status","value","source_file","source_line","symbol"):
            if str(P.get(fld))!=str(Q.get(fld)): fails.append(f"{k}: seats disagree on {fld} ({P.get(fld)!r} vs {Q.get(fld)!r}) — a value/status/coordinate disagreement is not silently resolved")  # PROBE:MERGE_FIELDS''')
l=rep(l,'''        r=dict(A[k]); r.pop("origin_alt",None); r.pop("origin_evidence_alt",None); r.pop("origin_search_alt",None); r.pop("derived_from_alt",None); r.pop("PARENTS_DISPUTED",None)
        if Bm[k]["origin"]!=A[k]["origin"]:
            r["origin_alt"]=Bm[k]["origin"]; r["origin_evidence_alt"]=Bm[k]["origin_evidence"]; ndis+=1
            if (Bm[k].get("origin_evidence") or {}).get("reason_code")=="ORIG_SILENT" and "origin_search" in Bm[k]: r["origin_search_alt"]=Bm[k]["origin_search"]  # PROBE:MERGE_SEARCH_ALT
        if sorted(A[k].get("derived_from") or []) != sorted(Bm[k].get("derived_from") or []):
            r["derived_from_alt"]=Bm[k].get("derived_from") or []; r["PARENTS_DISPUTED"]=True; npar+=1''',
'''        r=dict(P); r.pop("origin_alt",None); r.pop("origin_evidence_alt",None); r.pop("origin_search_alt",None); r.pop("derived_from_alt",None); r.pop("PARENTS_DISPUTED",None)
        ev_diff=(P.get("origin_evidence")!=Q.get("origin_evidence")); sil_q=(Q.get("origin_evidence") or {}).get("reason_code")=="ORIG_SILENT"
        search_diff=sil_q and (P.get("origin_search")!=Q.get("origin_search")); par_diff=(sorted(P.get("derived_from") or []) != sorted(Q.get("derived_from") or []))
        if Q["origin"]!=P["origin"]: ndis+=1
        if Q["origin"]!=P["origin"] or ev_diff or search_diff:
            # the secondary's COMPLETE branch is preserved whenever anything provenance-bearing differs — equal origin labels included
            r["origin_alt"]=Q["origin"]; r["origin_evidence_alt"]=Q["origin_evidence"]  # PROBE:MERGE_BRANCH
            if sil_q and "origin_search" in Q: r["origin_search_alt"]=Q["origin_search"]  # PROBE:MERGE_SEARCH_ALT
        if par_diff:
            r["derived_from_alt"]=Q.get("derived_from") or []; r["PARENTS_DISPUTED"]=True; npar+=1''')
l=l.replace("keeps seat A's origin/evidence and carries origin_alt + origin_evidence_alt from seat B","keeps the PRIMARY branch (the seat record with the smaller seat-blind canonical key — SEAT-PERMUTATION INVARIANCE) and carries the other seat's complete branch as origin_alt / origin_evidence_alt / origin_search_alt / derived_from_alt",1)
io.open(Lt,"w",encoding="utf-8").write(l)
S="r3c2_ledger_tools.py"; s=io.open(S,encoding="utf-8").read()
s=rep(s,'''        has_alt=bool(sr.get("origin_alt")) or (s_par_alt is not None)''','''        has_alt=bool(sr.get("origin_alt")) or bool(sr.get("origin_evidence_alt")) or (s_par_alt is not None)''')
s=rep(s,'''        alt_ev_full=sev2 if sr.get("origin_alt") else sev''','''        alt_ev_full=sev2 if sr.get("origin_evidence_alt") else sev''')
s=rep(s,'''        matches_alt=has_alt and str(ar.get("origin"))==alt_origin_full and all(str(aev.get(f2))==str(alt_ev_full.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim")) and a_par==alt_par_full and (alt_ev_full.get("reason_code")!="ORIG_SILENT" or ar.get("origin_search")==(sr.get("origin_search_alt") if sr.get("origin_alt") else sr.get("origin_search")))''',
'''        matches_alt=has_alt and str(ar.get("origin"))==alt_origin_full and all(str(aev.get(f2))==str(alt_ev_full.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim")) and a_par==alt_par_full and (alt_ev_full.get("reason_code")!="ORIG_SILENT" or ar.get("origin_search")==(sr.get("origin_search_alt") if "origin_search_alt" in sr else sr.get("origin_search")))''')
s=rep(s,'''            expected_search = sr.get("origin_search_alt") if (branch=="alt" and sr.get("origin_alt")) else sr.get("origin_search")''','''            expected_search = sr.get("origin_search_alt") if (branch=="alt" and "origin_search_alt" in sr) else sr.get("origin_search")''')
io.open(S,"w",encoding="utf-8").write(s); print("SPI enforcement applied: merge canonical primary + complete-branch preservation; compare reads branches only")
