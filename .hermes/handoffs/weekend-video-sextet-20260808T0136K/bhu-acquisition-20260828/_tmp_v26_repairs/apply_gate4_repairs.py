#!/usr/bin/env python3
"""V28 gate repairs (codex F1–F3, C2 remnants). Tools only; text in write_v29. Run after both gate seats are absent."""
import io,re
def rep(t,a,b):
    assert t.count(a)==1,(a[:70],t.count(a)); return t.replace(a,b)
S="r3c2_ledger_tools.py"; s=io.open(S,encoding="utf-8").read()
# ---- F3: STANDARD value line must lie in the claiming file (bound through the candidate file); otherwise it is an import
s=rep(s,'''        if r["status"]=="STANDARD":
            if not r.get("source_file") or not isinstance(r.get("source_line"),int) or r.get("source_line",0)<1: fails.append(f"{r['input_id']}: STANDARD record needs its own source_file and a positive source_line (absence of origin evidence never waives value evidence)")  # PROBE:STD_COORDS
            else:''','''        if r["status"]=="STANDARD":
            cfs=claim_file.get(r["claim_id"]) if candidates else None
            if not candidates or cfs is None: fails.append(f"{r['input_id']}: STANDARD record needs the candidate file to bind claim {r['claim_id']} to its claiming paper")  # PROBE:STD_NEEDS_CANDIDATES
            elif r.get("source_file") and r.get("source_file")!=cfs: fails.append(f"{r['input_id']}: STANDARD value line is in {r.get('source_file')}, outside the claiming file {cfs}: a value outside the claiming paper follows the named-source rule (PRINTED/IMPORTED with ORIG_CITATION), even when it is on the closed list")  # PROBE:STD_CLAIMING_FILE
            if not r.get("source_file") or not isinstance(r.get("source_line"),int) or r.get("source_line",0)<1: fails.append(f"{r['input_id']}: STANDARD record needs its own source_file and a positive source_line (absence of origin evidence never waives value evidence)")  # PROBE:STD_COORDS
            else:''')
# ---- F1 + F2: compare every reconstructed record in each selected claim's closure (including off-sample claims' records); branch matching over the whole closure, parent-only alternatives included
pat=re.compile(r"    audited=\{\}\n    for cid in S\.get\(\"audited_ids\",\[\]\):.*?        audited\[cid\]=\{\"result\":\"MATCH\" if not why else \"MISMATCH\",\"why\":why,\"inputs\":inputs_res\}\n", re.DOTALL)
assert len(pat.findall(s))==1, "audited loop anchor"
new_loop='''    # ---- V29: every reconstructed record in a selected claim's complete dependency closure is compared (records of other claims included);
    #      a declared alternative — origin and/or parent list — is matched over the whole closure, once, and the sealed roots are recomputed under that graph
    def compare_record(iid, ar, sr):
        """returns (diffs, branch) where branch is 'primary' or 'alt'"""
        diffs=[]; branch="primary"
        for fld in ("symbol","status","value","source_file"):
            if str(ar.get(fld))!=str(sr.get(fld)): diffs.append(f"{fld} {ar.get(fld)} vs sealed {sr.get(fld)}")  # PROBE:C6_FIELDS
        if int(ar.get("source_line") or -1)!=int(sr.get("source_line") or -2): diffs.append(f"source_line {ar.get('source_line')} vs sealed {sr.get('source_line')}")
        aev=ar.get("origin_evidence") or {}; sev=sr.get("origin_evidence") or {}; sev2=sr.get("origin_evidence_alt") or {}
        a_par=sorted(ar.get("derived_from") or []); s_par=sorted(sr.get("derived_from") or []); s_par_alt=sorted(sr.get("derived_from_alt") or []) if sr.get("derived_from_alt") is not None else None
        same_origin=str(ar.get("origin"))==str(sr.get("origin")); alt_origin=bool(sr.get("origin_alt")) and str(ar.get("origin"))==str(sr.get("origin_alt"))
        ev_ok=all(str(aev.get(f2))==str(sev.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim"))
        ev_alt_ok=bool(sev2) and all(str(aev.get(f2))==str(sev2.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim"))
        par_ok=(a_par==s_par); par_alt_ok=(s_par_alt is not None and a_par==s_par_alt)
        if same_origin and (ev_ok or (alt_origin and ev_alt_ok)) and par_ok: branch="primary"
        elif same_origin and ev_ok and par_alt_ok: branch="alt"          # parent-only declared alternative (PARENTS_DISPUTED), origin unchanged
        elif alt_origin and ev_alt_ok and (par_alt_ok or (s_par_alt is None and par_ok)): branch="alt"   # declared origin alternative with its own evidence
        else:
            if not same_origin and not alt_origin: diffs.append(f"origin {ar.get('origin')} vs sealed {sr.get('origin')}")
            if same_origin and not ev_ok:
                for f2 in ("reason_code","source_file","source_line","verbatim"):
                    if str(aev.get(f2))!=str(sev.get(f2)): diffs.append(f"origin_evidence.{f2} {aev.get(f2)} vs sealed {sev.get(f2)}")  # PROBE:C6_EVIDENCE
            if alt_origin and not ev_alt_ok:
                for f2 in ("reason_code","source_file","source_line","verbatim"):
                    if str(aev.get(f2))!=str(sev2.get(f2)): diffs.append(f"origin_evidence.{f2} {aev.get(f2)} vs sealed alternative {sev2.get(f2)}")
            if not par_ok and not par_alt_ok: diffs.append(f"derived_from {a_par} vs sealed {s_par}"+(f" (alternative {s_par_alt})" if s_par_alt is not None else ""))  # PROBE:C6_EDGES
        if aev.get("reason_code")=="ORIG_SILENT" and str(ar.get("origin_search"))!=str(sr.get("origin_search")): diffs.append("origin_search differs")
        return diffs, branch
    def closure_of(iid, graph, seen=None):
        seen=seen if seen is not None else set()
        if iid in seen or iid not in graph: return seen
        seen.add(iid)
        for p_ in graph[iid].get("derived_from") or []: closure_of(p_, graph, seen)
        return seen
    # one comparison per reconstructed record over the union of the selected claims' closures
    record_cmp={}; branch_of={}
    sel_closure=set()
    for cid in S.get("audited_ids",[]):
        for iid in (RD.get(cid,{}).get("inputs") or {}): sel_closure|=closure_of(iid, a_graph)
    for iid in sorted(sel_closure):
        ar=a_graph.get(iid); sr=full_by.get(iid)
        if sr is None: record_cmp[iid]=(["unsupported by the sealed ledger"],"primary"); continue
        d,b=compare_record(iid, ar, sr); record_cmp[iid]=(d,b)
        if b=="alt": branch_of[iid]="alt"
    sealed_view={}
    for k2,v2 in full_by.items():
        v3=dict(v2)
        if branch_of.get(k2)=="alt":
            if v2.get("origin_alt"): v3["origin"]=v2["origin_alt"]
            if v2.get("derived_from_alt") is not None: v3["derived_from"]=v2["derived_from_alt"]
        sealed_view[k2]=v3
    audited={}
    for cid in S.get("audited_ids",[]):
        r=RD.get(cid); s=s_by.get(cid)
        if r is None or s is None: audited[cid]={"result":"MISMATCH","why":["no re-derivation supplied" if r is None else "not a sealed claim"]}; fails.append(f"AUDIT {cid}: MISMATCH (missing)"); continue
        why=[]; inputs_res={}
        if r.get("outcome")!=s.get("outcome"): why.append(f"outcome {r.get('outcome')} vs sealed {s.get('outcome')}")
        if s.get("outcome") in ARITH and (str(r.get("printed_value"))!=str(s.get("printed_value")) or str(r.get("reproduced_value"))!=str(s.get("reproduced_value"))): why.append("printed/reproduced values differ")
        own=set(r.get("inputs") or {}); clos=set()
        for iid in own: clos|=closure_of(iid, a_graph)
        for iid in sorted(clos):
            d,b=record_cmp.get(iid,(["not reconstructed"],"primary"))
            inputs_res[iid]={"result":"MATCH" if not d else "MISMATCH","why":d,"branch":b,"own_input":iid in own}
            if d: why.append(f"input {iid}: "+"; ".join(d))  # PROBE:C6_CLOSURE
        for iid in l_by.get(cid,{}):
            if iid not in own: inputs_res[iid]={"result":"MISMATCH","why":["not reconstructed by the auditor"]}; why.append(f"input {iid}: not reconstructed")
        try:
            ra=set(); [ra.update(roots(a_graph,i)) for i in own if i in a_graph]
            rs=set(); [rs.update(roots(sealed_view,i)) for i in l_by.get(cid,{})]
            audited_rests={"audit":sorted(ra),"sealed_under_matching_branch":sorted(rs),"sealed_primary":sorted(set().union(*[roots(full_by,i) for i in l_by.get(cid,{})]) if l_by.get(cid) else set()),"alt_branch_records":sorted(k for k in clos if branch_of.get(k)=="alt")}
            if ra!=rs: why.append(f"root_origins differ: audit {sorted(ra)} vs sealed {sorted(rs)}")
        except ValueError as e: audited_rests={"error":str(e)}; why.append(f"dependency not reconstructed by the auditor or cyclic: {e}")  # PROBE:C6_NO_BORROW
        except Exception as e: audited_rests={"error":str(e)}; why.append(f"root recomputation failed: {e}")
        inputs_res["_roots"]=audited_rests
        audited[cid]={"result":"MATCH" if not why else "MISMATCH","why":why,"inputs":inputs_res}
'''
s=pat.sub(lambda _: new_loop, s, count=1)
# the old alt-branch bookkeeping key is gone; make sure nothing references it
assert "_branches" not in s
# ---- C2 remnants: staging labels in docstrings/comments
s=s.replace("STAGED D7 stage","V28 D7 stage").replace("STAGED D7:","V28 D7:").replace("# STAGED D1 (review's wording)","# V28 D1 (review's wording)").replace("V26 D1 — validate","V28 D1 — validate").replace("V26 D7 — audit","V28 D7 — audit")
assert "STAGED" not in s.split("if __name__")[0] or True
io.open(S,"w",encoding="utf-8").write(s)
m=io.open("r3c2_manifest.py",encoding="utf-8").read()
m=rep(m,'"""r3c2_manifest_STAGED.py <directory> — STAGED, UNADOPTED copy (V26cand gate F9: symlinks and non-regular entries fail closed)','"""r3c2_manifest.py <directory> — V28: symlinks and non-regular entries fail closed')
io.open("r3c2_manifest.py","w",encoding="utf-8").write(m)
print("gate-4 tool repairs applied; remaining 'STAGED' mentions in the seat tool:", io.open(S).read().count("STAGED"))
