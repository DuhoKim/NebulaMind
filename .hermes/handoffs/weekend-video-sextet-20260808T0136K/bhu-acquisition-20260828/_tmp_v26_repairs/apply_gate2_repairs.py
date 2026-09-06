#!/usr/bin/env python3
"""V26 gate (round 2) repairs: codex F1–F7, C1–C3 (+ kimi, folded in by hand). Tools first; text anchors are whitespace-tolerant. Write-at-end."""
import io,re,sys
def rep_ws(text,a,b,count=1):
    pat=r"\s+".join(re.escape(t) for t in a.split()); hits=re.findall(pat,text); assert len(hits)==count,(a[:60],len(hits)); return re.sub(pat,lambda _: b,text,count=count)
def rep(text,a,b):
    assert text.count(a)==1,(a[:60],text.count(a)); return text.replace(a,b)
# ---------- seat tool: F1 shared evidence check before every branch; F2 audit compares reconstructed records + edges and recomputes rests_on
S="r3c2_ledger_tools.py"; s=io.open(S,encoding="utf-8").read()
s=rep(s,'''        if PAIRS.get(rc)!=r["origin"]: fails.append(f"{r['input_id']}: reason_code {rc} does not map to origin {r['origin']}")''',
'''        if PAIRS.get(rc)!=r["origin"]: fails.append(f"{r['input_id']}: reason_code {rc} does not map to origin {r['origin']}")
        if rc!="ORIG_SILENT":
            # gate-2 F1: before any status-specific branch, EVERY non-silent record carries a non-empty quotation found at its declared evidence coordinates
            ef=str(ev.get("source_file","")); el=ev.get("source_line")
            if not str(ev.get("verbatim","")).strip(): fails.append(f"{r['input_id']}: empty quotation (every non-ORIG_SILENT record quotes its evidence line)"); continue  # PROBE:EV_EMPTY_ALL
            try: elp=int(el); assert elp>=1
            except Exception: fails.append(f"{r['input_id']}: origin_evidence.source_line {el!r} is not a positive line number"); continue  # PROBE:EV_LINE_POS
            cl0=read_line(srcdir, ef, elp)
            if cl0 is None: fails.append(f"{r['input_id']}: cannot read evidence line {ef}:{elp}"); continue  # PROBE:EV_LINE_ALL
            if ev.get("verbatim","") not in cl0: fails.append(f"{r['input_id']}: quotation not found at evidence line {ef}:{elp}"); continue  # PROBE:EV_VERBATIM_ALL''')
# the STANDARD/BLOCKED block added last round now duplicates the shared check; keep only its STANDARD value-line part
s=rep(s,'''        if rc!="ORIG_SILENT" and r["status"] in ("STANDARD","BLOCKED"):
            # gate F3: the promised byte-level evidence check applies to every status, not only PRINTED
            ef=str(ev.get("source_file","")); el=ev.get("source_line"); cl=read_line(srcdir, ef, el)
            if not str(ev.get("verbatim","")).strip(): fails.append(f"{r['input_id']}: {r['status']} record with an empty quotation")  # PROBE:EV_EMPTY_ANY
            elif cl is None: fails.append(f"{r['input_id']}: cannot read evidence line {ef}:{el}")  # PROBE:EV_LINE_ANY
            elif ev.get("verbatim","") not in cl: fails.append(f"{r['input_id']}: quotation not found at evidence line {ef}:{el}")  # PROBE:EV_VERBATIM_ANY
            if r["status"]=="STANDARD" and r.get("source_file"):''','''        if r["status"]=="STANDARD" and rc!="ORIG_SILENT":
            if r.get("source_file"):''')
# F2: compare reconstructed input records and dependency edges; recompute rests_on both ways
s=rep(s,'''        for iid,og in (r.get("inputs") or {}).items():
            ok_=(l_by.get(cid,{}).get(iid)==og); inputs_res[iid]={"audit_origin":og,"sealed_origin":l_by.get(cid,{}).get(iid),"result":"MATCH" if ok_ else "MISMATCH"}
            if not ok_: why.append(f"origin {iid}: {og} vs sealed {l_by.get(cid,{}).get(iid)}")
        for iid in l_by.get(cid,{}):
            if iid not in (r.get("inputs") or {}): inputs_res[iid]={"audit_origin":None,"sealed_origin":l_by[cid][iid],"result":"MISMATCH"}; why.append(f"origin {iid}: not re-classified")''',
'''        # gate-2 F2: the auditor's inputs are full reconstructed records; every field and every dependency edge is compared
        for iid,ar in (r.get("inputs") or {}).items():
            ar=ar if isinstance(ar,dict) else {"origin":ar}
            sr=full_by.get(iid)
            if sr is None: inputs_res[iid]={"result":"MISMATCH","why":"auditor reconstructed an input the sealed ledger lacks"}; why.append(f"input {iid}: unsupported by the sealed ledger"); continue
            diffs=[]
            for fld in ("origin","status","value","source_file"):
                if fld in ar and str(ar.get(fld))!=str(sr.get(fld)): diffs.append(f"{fld} {ar.get(fld)} vs sealed {sr.get(fld)}")
            if "source_line" in ar and int(ar["source_line"])!=int(sr.get("source_line") or -1): diffs.append(f"source_line {ar['source_line']} vs sealed {sr.get('source_line')}")
            if "derived_from" in ar and sorted(ar.get("derived_from") or [])!=sorted(sr.get("derived_from") or []): diffs.append(f"derived_from {sorted(ar.get('derived_from') or [])} vs sealed {sorted(sr.get('derived_from') or [])}")  # PROBE:C6_EDGES
            if sr.get("origin_alt") and "origin" in ar and str(ar.get("origin"))==str(sr.get("origin_alt")) and diffs and diffs[0].startswith("origin "): diffs[0]+=" (matches the sealed alternative classification: carried as ORIGIN_DISPUTED, not a mismatch)"; diffs=[d for d in diffs if not d.startswith("origin ")]
            inputs_res[iid]={"result":"MATCH" if not diffs else "MISMATCH","why":diffs}
            if diffs: why.append(f"input {iid}: "+"; ".join(diffs))
        for iid in l_by.get(cid,{}):
            if iid not in (r.get("inputs") or {}): inputs_res[iid]={"result":"MISMATCH","why":"not reconstructed by the auditor"}; why.append(f"input {iid}: not reconstructed")
        # rests_on recomputed from both reconstructions (seat tool's roots over the auditor's records vs the sealed ledger)
        try:
            a_by={i:dict(v,input_id=i) for i,v in (r.get("inputs") or {}).items() if isinstance(v,dict)}
            for v in a_by.values(): v.setdefault("origin","UNDECLARED"); v.setdefault("derived_from",[])
            ra=set(); [ra.update(roots(dict(full_by,**a_by),i)) for i in a_by]
            rs=set(); [rs.update(roots(full_by,i)) for i in l_by.get(cid,{})]
            audited_rests={"audit":sorted(ra),"sealed":sorted(rs)}
            if ra!=rs: why.append(f"root_origins differ: audit {sorted(ra)} vs sealed {sorted(rs)}")
        except Exception as e: audited_rests={"error":str(e)}; why.append(f"root recomputation failed: {e}")
        inputs_res["_roots"]=audited_rests''')
s=rep(s,'''    s_by={c["candidate_id"]:c for c in SC}; l_by={}
    for r in SL: l_by.setdefault(r["claim_id"],{})[r["input_id"]]=r.get("origin")''','''    s_by={c["candidate_id"]:c for c in SC}; l_by={}; full_by={}
    for r in SL: l_by.setdefault(r["claim_id"],{})[r["input_id"]]=r.get("origin"); full_by[r["input_id"]]=r''')
io.open(S,"w",encoding="utf-8").write(s)
# ---------- lane tool: F3 compute requires the candidate file (two-arg form exits 2)
Lt="r3c2_lane_tools.py"; l=io.open(Lt,encoding="utf-8").read()
l=rep(l,'''    if len(a)==3 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2]))
    if len(a)==4 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2],a[3]))''','''    if len(a)==4 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2],a[3]))
    if len(a)==3 and a[0]=="compute": print("usage: compute <merged.json> <out.json> <candidates.json> — the candidate file is mandatory (every included claim gets a rests_on row)"); sys.exit(2)  # PROBE:COMPUTE_NEEDS_CANDIDATES''')
l=l.replace("  /usr/bin/python3 r3c2_lane_tools.py compute <merged.json> <out.json>","  /usr/bin/python3 r3c2_lane_tools.py compute <merged.json> <out.json> <candidates.json>   (candidate file mandatory)",1)
io.open(Lt,"w",encoding="utf-8").write(l)
# ---------- manifest: F7 root symlink / non-directory refused
Mf="r3c2_manifest.py"; mf=io.open(Mf,encoding="utf-8").read()
mf=rep(mf,'''    root = os.path.abspath(root); rows = []; errors = 0''','''    if os.path.islink(root) or not os.path.isdir(root): print(f"ERROR={root}: root is a symlink or not a directory (refused)"); sys.exit(1)  # PROBE:MANIFEST_ROOT
    root = os.path.abspath(root); rows = []; errors = 0''')
io.open(Mf,"w",encoding="utf-8").write(mf)
print("tools repaired: seat tool (F1 shared evidence, F2 edges + roots), lane tool (F3 mandatory candidates), manifest (F7 root)")
