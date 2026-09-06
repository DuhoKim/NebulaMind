#!/usr/bin/env python3
"""V27 gate repairs: codex F1–F4, C2 (tools + kit); C1 and text in write_v28. Write-at-end; anchors asserted. Run after both gate seats are absent."""
import io,re
def rep(t,a,b):
    assert t.count(a)==1,(a[:70],t.count(a)); return t.replace(a,b)
S="r3c2_ledger_tools.py"; s=io.open(S,encoding="utf-8").read()
# ---- F4: the ordinary PRINTED branch checks the VALUE at the value line only; the quotation was already checked at its own evidence line
s=rep(s,'''            if rc!="ORIG_SILENT" and ev.get("verbatim","") not in line: fails.append(f"{r['input_id']}: verbatim not found at {r['source_file']}:{r['source_line']}")
            if str(r.get("value")) not in line: fails.append(f"{r['input_id']}: value {r.get('value')} not at cited line")''',
'''            if not token_in(r.get("value"), line): fails.append(f"{r['input_id']}: value {r.get('value')} is not a numeric token at {r['source_file']}:{r['source_line']}")  # PROBE:PRINTED_VALUE_LINE''')
# ---- F3: STANDARD value-line check unconditional (even ORIG_SILENT; coordinates required); BLOCKED evidence file bound to the claiming file
s=rep(s,'''        if r["status"]=="STANDARD" and rc!="ORIG_SILENT":
            if r.get("source_file"):''','''        if r["status"]=="STANDARD":
            if not r.get("source_file") or not isinstance(r.get("source_line"),int) or r.get("source_line",0)<1: fails.append(f"{r['input_id']}: STANDARD record needs its own source_file and a positive source_line (absence of origin evidence never waives value evidence)")  # PROBE:STD_COORDS
            else:''')
s=rep(s,'''        if r["status"]=="BLOCKED":
            if r.get("value") not in (None,""): fails.append(f"{r['input_id']}: BLOCKED record carries a value")''','''        if r["status"]=="BLOCKED":
            if r.get("value") not in (None,""): fails.append(f"{r['input_id']}: BLOCKED record carries a value")
            cfb=claim_file.get(r["claim_id"]) if candidates else None
            if not candidates or cfb is None: fails.append(f"{r['input_id']}: BLOCKED record needs the candidate file to bind claim {r['claim_id']} to its claiming paper")  # PROBE:BLOCKED_NEEDS_CANDIDATES
            elif str(ev.get("source_file",""))!=cfb: fails.append(f"{r['input_id']}: BLOCKED naming evidence is in {ev.get('source_file')}, but claim {r['claim_id']} belongs to {cfb}")  # PROBE:BLOCKED_CLAIMING_FILE''')
# ---- F1: seal-rederivation validates the reconstruction schema; compare requires every C3 field, never borrows a dependency from the sealed side
s=rep(s,'''def cmd_audit_seal_rederivation(red, out):
    """STAGED D7 stage 2b (custodian): first-write seal of the auditor's re-derivations BEFORE any sealed ledger is released."""
    return first_write(out, f"AUDITOR_REDERIVATIONS_SHA256={sha(red)}\\n")''',
'''RECON_FIELDS=("symbol","status","value","source_file","source_line","origin","origin_evidence","derived_from")
def recon_schema_fails(RD):
    """every reconstructed input carries every C3 field (origin_search when ORIG_SILENT); returns the list of failures"""
    out=[]
    for cid,r in RD.items():
        if not isinstance(r,dict) or "outcome" not in r: out.append(f"{cid}: re-derivation lacks outcome"); continue
        for iid,ar in (r.get("inputs") or {}).items():
            if not isinstance(ar,dict): out.append(f"{cid}/{iid}: input reconstruction must be a full record, not a label"); continue
            miss=[f for f in RECON_FIELDS if f not in ar]
            if miss: out.append(f"{cid}/{iid}: reconstruction missing {miss}")
            ev=ar.get("origin_evidence")
            if isinstance(ev,dict):
                m2=[f for f in ("reason_code","source_file","source_line","verbatim") if f not in ev]
                if m2: out.append(f"{cid}/{iid}: origin_evidence missing {m2}")
                if ev.get("reason_code")=="ORIG_SILENT" and "origin_search" not in ar: out.append(f"{cid}/{iid}: ORIG_SILENT reconstruction needs origin_search")
            elif "origin_evidence" in ar: out.append(f"{cid}/{iid}: origin_evidence must be an object")
    return out

def cmd_audit_seal_rederivation(red, out):
    """STAGED D7 stage 2b (custodian): validates the reconstruction schema, then first-write seals the auditor's re-derivations BEFORE any sealed ledger is released."""
    RD=json.loads(pathlib.Path(red).read_text()); sf=recon_schema_fails(RD)
    if sf:
        for x in sf: print("FAIL:",x)
        print("re-derivation NOT sealed: the reconstruction is incomplete"); return 1  # PROBE:C6_RECON_SCHEMA
    return first_write(out, f"AUDITOR_REDERIVATIONS_SHA256={sha(red)}\\n")''')
s=rep(s,'''    s_by={c["candidate_id"]:c for c in SC}; l_by={}; full_by={}
    for r in SL: l_by.setdefault(r["claim_id"],{})[r["input_id"]]=r.get("origin"); full_by[r["input_id"]]=r''',
'''    s_by={c["candidate_id"]:c for c in SC}; l_by={}; full_by={}
    for r in SL: l_by.setdefault(r["claim_id"],{})[r["input_id"]]=r.get("origin"); full_by[r["input_id"]]=r
    for x in recon_schema_fails(RD): fails.append("C6_RECONSTRUCTION: "+x)  # PROBE:C6_RECON_COMPLETE
    # the auditor's OWN graph, across every audited claim; a dependency it did not reconstruct is never borrowed from the sealed side
    a_graph={}
    for cid0,r0 in RD.items():
        for iid0,ar0 in (r0.get("inputs") or {}).items():
            if isinstance(ar0,dict): a_graph[iid0]=dict(ar0,input_id=iid0,origin=ar0.get("origin","UNDECLARED"),derived_from=list(ar0.get("derived_from") or []))''')
s=rep(s,'''            diffs=[]
            for fld in ("origin","status","value","source_file"):
                if fld in ar and str(ar.get(fld))!=str(sr.get(fld)): diffs.append(f"{fld} {ar.get(fld)} vs sealed {sr.get(fld)}")
            if "source_line" in ar and int(ar["source_line"])!=int(sr.get("source_line") or -1): diffs.append(f"source_line {ar['source_line']} vs sealed {sr.get('source_line')}")
            if "derived_from" in ar and sorted(ar.get("derived_from") or [])!=sorted(sr.get("derived_from") or []): diffs.append(f"derived_from {sorted(ar.get('derived_from') or [])} vs sealed {sorted(sr.get('derived_from') or [])}")  # PROBE:C6_EDGES
            if sr.get("origin_alt") and "origin" in ar and str(ar.get("origin"))==str(sr.get("origin_alt")) and diffs and diffs[0].startswith("origin "): diffs[0]+=" (matches the sealed alternative classification: carried as ORIGIN_DISPUTED, not a mismatch)"; diffs=[d for d in diffs if not d.startswith("origin ")]''',
'''            diffs=[]; alt_branch=False
            for fld in ("symbol","status","value","source_file"):
                if str(ar.get(fld))!=str(sr.get(fld)): diffs.append(f"{fld} {ar.get(fld)} vs sealed {sr.get(fld)}")  # PROBE:C6_FIELDS
            if int(ar.get("source_line") or -1)!=int(sr.get("source_line") or -2): diffs.append(f"source_line {ar.get('source_line')} vs sealed {sr.get('source_line')}")
            aev=ar.get("origin_evidence") or {}; sev=sr.get("origin_evidence") or {}
            if str(ar.get("origin"))==str(sr.get("origin")):
                for f2 in ("reason_code","source_file","source_line","verbatim"):
                    if str(aev.get(f2))!=str(sev.get(f2)): diffs.append(f"origin_evidence.{f2} {aev.get(f2)} vs sealed {sev.get(f2)}")  # PROBE:C6_EVIDENCE
            elif sr.get("origin_alt") and str(ar.get("origin"))==str(sr.get("origin_alt")):
                alt_branch=True; sev2=sr.get("origin_evidence_alt") or {}
                for f2 in ("reason_code","source_file","source_line","verbatim"):
                    if str(aev.get(f2))!=str(sev2.get(f2)): diffs.append(f"origin_evidence.{f2} {aev.get(f2)} vs sealed alternative {sev2.get(f2)}")
            else: diffs.append(f"origin {ar.get('origin')} vs sealed {sr.get('origin')}")
            s_parents=sorted(sr.get("derived_from_alt") or []) if (alt_branch and sr.get("derived_from_alt") is not None) else sorted(sr.get("derived_from") or [])
            if sorted(ar.get("derived_from") or [])!=s_parents: diffs.append(f"derived_from {sorted(ar.get('derived_from') or [])} vs sealed {s_parents}")  # PROBE:C6_EDGES
            if ar.get("origin_evidence",{}).get("reason_code")=="ORIG_SILENT" and str(ar.get("origin_search"))!=str(sr.get("origin_search")): diffs.append("origin_search differs")
            if alt_branch: inputs_res.setdefault("_branches",{})[iid]="sealed alternative classification (ORIGIN_DISPUTED carried, compared like with like)"''')
s=rep(s,'''        try:
            a_by={i:dict(v,input_id=i) for i,v in (r.get("inputs") or {}).items() if isinstance(v,dict)}
            for v in a_by.values(): v.setdefault("origin","UNDECLARED"); v.setdefault("derived_from",[])
            ra=set(); [ra.update(roots(dict(full_by,**a_by),i)) for i in a_by]
            rs=set(); [rs.update(roots(full_by,i)) for i in l_by.get(cid,{})]
            audited_rests={"audit":sorted(ra),"sealed":sorted(rs)}
            if ra!=rs: why.append(f"root_origins differ: audit {sorted(ra)} vs sealed {sorted(rs)}")
        except Exception as e: audited_rests={"error":str(e)}; why.append(f"root recomputation failed: {e}")''',
'''        try:
            # F1: roots from the auditor's OWN graph only (a missing dependency is a MISMATCH, never borrowed); F2: sealed roots under the matching branch
            ra=set(); [ra.update(roots(a_graph,i)) for i in (r.get("inputs") or {}) if i in a_graph]
            branches=(inputs_res.get("_branches") or {})
            sealed_view={}
            for k2,v2 in full_by.items():
                v3=dict(v2)
                if k2 in branches:
                    if v2.get("origin_alt"): v3["origin"]=v2["origin_alt"]
                    if v2.get("derived_from_alt") is not None: v3["derived_from"]=v2["derived_from_alt"]
                sealed_view[k2]=v3
            rs=set(); [rs.update(roots(sealed_view,i)) for i in l_by.get(cid,{})]
            audited_rests={"audit":sorted(ra),"sealed_under_matching_branch":sorted(rs),"sealed_primary":sorted(set().union(*[roots(full_by,i) for i in l_by.get(cid,{})]) if l_by.get(cid) else set())}
            if ra!=rs: why.append(f"root_origins differ: audit {sorted(ra)} vs sealed {sorted(rs)}")
        except ValueError as e: audited_rests={"error":str(e)}; why.append(f"dependency not reconstructed by the auditor or cyclic: {e}")  # PROBE:C6_NO_BORROW
        except Exception as e: audited_rests={"error":str(e)}; why.append(f"root recomputation failed: {e}")''')
io.open(S,"w",encoding="utf-8").write(s)
# ---- C2: docstrings of the adopted lane and batch tools
for p,a,b in (("r3c2_lane_tools.py","r3c2_lane_tools_STAGED.py — STAGED, UNADOPTED copy (V26cand gate F2/F4 repairs) of the LANE-SIDE tool","r3c2_lane_tools.py — the V27 lane-side tool"),
              ("r3c2_batch_tools.py","r3c2_batch_tools_STAGED.py — STAGED, UNADOPTED (batch-reading candidate, repaired 2026-09-06 after two independent reviews). LANE-SIDE.","r3c2_batch_tools.py — the V27 lane-side ownership partition, batch seal, join and coverage tool.")):
    t=io.open(p,encoding="utf-8").read()
    if a in t: t=t.replace(a,b); io.open(p,"w",encoding="utf-8").write(t); print("docstring fixed:",p)
    else: print("docstring anchor absent (already fixed?):",p, t.splitlines()[1][:80])
print("gate-3 tool repairs applied")
