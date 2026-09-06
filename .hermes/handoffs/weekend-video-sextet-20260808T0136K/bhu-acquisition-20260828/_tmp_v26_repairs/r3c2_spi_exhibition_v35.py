#!/usr/bin/env python3
"""r3c2_spi_exhibition.py — SEAT-PERMUTATION INVARIANCE (SPI) exhibition.
For each reviewer construction, merge both seat orders and require identical merged bytes; run seal-enumeration, select, seal-rederivation and compare with one fixed auditor reconstruction; require identical exit codes, failure lines in emitted order and complete C6_AUDIT.json artefacts including sealed_ledger_sha256; also assert the construction's expected verdict and required diagnostic. V35: lane compute runs on each merged ledger too; its exit code and stdout join the compared outcome, and a construction may require compute to succeed with a DISPUTED pair.
  /usr/bin/python3 -E r3c2_spi_exhibition.py <tools_dir> <work_dir>      prints SPI=PASS|FAIL and one line per construction."""
import json, subprocess, sys, pathlib, hashlib, shutil, itertools
TOOLS=pathlib.Path(sys.argv[1]).resolve(); W=pathlib.Path(sys.argv[2]).resolve(); shutil.rmtree(W,ignore_errors=True); W.mkdir(parents=True)
SEAT=TOOLS/"r3c2_ledger_tools.py"; LANE=TOOLS/"r3c2_lane_tools.py"; PY="/usr/bin/python3"
def run(tool,*a): r=subprocess.run([PY,"-E",str(tool),*[str(x) for x in a]],capture_output=True,text=True); return r.returncode, r.stdout+r.stderr
def w(name,obj): p=W/name; p.write_text(json.dumps(obj,indent=1)); return str(p)   # fixture writer does NOT normalise member order (codex V33 F1)
def rev(d): return {k:(rev(d[k]) if isinstance(d[k],dict) else d[k]) for k in reversed(list(d))}   # same JSON object, reversed member order
def rec(cid="c1",iid="i1",**k):
    r={"claim_id":cid,"input_id":iid,"symbol":"a","status":"PRINTED","origin":"IMPORTED","origin_evidence":{"reason_code":"ORIG_CITATION","source_file":"paperA.txt","source_line":3,"verbatim":"We adopt a = 2 from paperB (2020)"},"derived_from":[],"value":"2","source_file":"paperB.txt","source_line":5}
    for kk,v in k.items():
        if kk.startswith("ev_"): r["origin_evidence"]=dict(r["origin_evidence"],**{kk[3:]:v})
        else: r[kk]=v
    return r
def full(r): return {k:r.get(k) for k in ("symbol","origin","status","value","source_file","source_line","derived_from","origin_evidence")}
CH=lambda **k: rec(**{**dict(origin="CHOSEN",ev_reason_code="ORIG_CHOICE_STATED",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2"),**k})
SIL=lambda search,**k: dict(rec(**{**dict(origin="UNDECLARED",ev_reason_code="ORIG_SILENT",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim=""),**k}),origin_search=search)
FIT=lambda **k: rec(**{**dict(origin="FITTED",ev_reason_code="ORIG_FIT_STATED",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2"),**k})
DER=lambda parents,**k: rec(**{**dict(origin="DERIVED",ev_reason_code="ORIG_EQUATION",ev_source_file="paperA.txt",ev_source_line=4,ev_verbatim="Then y",derived_from=parents),**k})
STD=lambda iid: {"claim_id":"c1","input_id":iid,"symbol":"c","status":"STANDARD","origin":"STANDARD","origin_evidence":{"reason_code":"ORIG_CONSTANT","source_file":"paperA.txt","source_line":4,"verbatim":"Then y"},"derived_from":[],"value":"2.99792458e8","source_file":"paperA.txt","source_line":4}
S1={"query":["a","choose","adopt","fit"],"files":["fixture.txt"],"matches":["fixture.txt:1"]}; S2={"query":["a","choose","adopt","fit","estimate"],"files":["fixture.txt"],"matches":["fixture.txt:1"]}
# constructions: (name, seatA records, seatB records, auditor inputs for c1, EXPECTED audit exit code in BOTH orders, diagnostic that must appear in both orders or "")
NEITHER="record matches neither complete declared branch"
def CY(iid,sym,parents,evline,evtext,valline):
    return rec(iid=iid,symbol=sym,origin=("MEASURED" if not parents else "DERIVED"),ev_reason_code=("ORIG_MEASURED" if not parents else "ORIG_EQUATION"),ev_source_file="p.txt",ev_source_line=evline,ev_verbatim=evtext,derived_from=parents,value="2",source_file="p.txt",source_line=valline)
def _ck(r): return hashlib.sha256(json.dumps(r,sort_keys=True,separators=(",",":")).encode()).hexdigest()   # the tool's seat-blind canonical key, reproduced here only to BUILD the adversarial fixture
def _mixed_cycle():
    """codex V34 F1: two acyclic graphs (A x→y→r, B y→x→r) whose PER-INPUT canonical primaries come from different seats, so the mixed
    primary view is the cycle x↔y that no seat supplied. The evidence quotations carry a small deterministic tag so that the canonical
    keys select A's x and B's y (the search is deterministic; the fixture is printed with its tag)."""
    for s in range(200):
        A=[CY("x","x",["y"],2,f"x = y = 2. [{s}]",2),CY("y","y",["r"],4,f"y = r = 2. [{s}]",4),CY("r","r",[],1,"We measure r = 2.",1)]
        B=[CY("x","x",["r"],3,f"x = r = 2. [{s}]",2),CY("y","y",["x"],5,f"y = x = 2. [{s}]",4),CY("r","r",[],1,"We measure r = 2.",1)]
        if _ck(A[0])<=_ck(B[0]) and _ck(B[1])<_ck(A[1]): return A,B,s
        if _ck(B[0])<=_ck(A[0]) and _ck(A[1])<_ck(B[1]): return A,B,s
    raise SystemExit("could not build the mixed-cycle fixture")
CYA,CYB,_tag=_mixed_cycle(); print(f"mixed-cycle fixture tag={_tag}")
CONS=[
 ("same-origin, different complete searches (codex V32 F1); auditor = B", [SIL(S1)],[SIL(S2)], {"i1":dict(full(SIL(S2)),origin_search=S2)}, 0, "", None),
 ("structurally equal seat records, different top-level and nested member order (codex V33 F1); auditor = the record", [rec()],[rev(rec())], {"i1":full(rec())}, 0, "", None),
 ("two acyclic seat graphs whose per-input mix is a cycle (codex V34 F1: A x→y→r, B y→x→r); auditor = complete A", CYA, CYB, {"x":full(CYA[0]),"y":full(CYA[1]),"r":full(CYA[2])}, 0, "", "DISPUTED"),
 ("same two graphs; auditor = complete B", CYA, CYB, {"x":full(CYB[0]),"y":full(CYB[1]),"r":full(CYB[2])}, 0, "", "DISPUTED"),
 ("same-origin, different searches; auditor = A", [SIL(S1)],[SIL(S2)], {"i1":dict(full(SIL(S1)),origin_search=S1)}, 0, "", None),
 ("ORIG_SILENT alternative vs CHOSEN (codex V31 F1); auditor = the silent branch", [CH()],[SIL(S1)], {"i1":dict(full(SIL(S1)),origin_search=S1)}, 0, "", None),
 ("complete alternative branch: CHOSEN vs FITTED; auditor = FITTED", [CH()],[FIT()], {"i1":full(FIT())}, 0, "", None),
 ("complete parent-only alternative: identical origin and evidence, auditor matches the second parent set (was mislabelled a hybrid — codex V33 F2)", [DER(["i2"]),STD("i2"),STD("i3")],[DER(["i3"]),STD("i2"),STD("i3")], {"i1":full(DER(["i3"])),"i2":full(STD("i2")),"i3":full(STD("i3"))}, 0, "", None),
 ("hybrid direction 1: A's origin+evidence (DERIVED, equation) with B's parents (B = CHOSEN, choice evidence, parents [i3])", [DER(["i2"]),STD("i2"),STD("i3")],[dict(CH(),derived_from=["i3"]),STD("i2"),STD("i3")], {"i1":dict(full(DER(["i2"])),derived_from=["i3"]),"i2":full(STD("i2")),"i3":full(STD("i3"))}, 1, NEITHER, None),
 ("hybrid direction 2: B's origin+evidence (CHOSEN) with A's parents [i2]", [DER(["i2"]),STD("i2"),STD("i3")],[dict(CH(),derived_from=["i3"]),STD("i2"),STD("i3")], {"i1":dict(full(CH()),derived_from=["i2"]),"i2":full(STD("i2")),"i3":full(STD("i3"))}, 1, NEITHER, None),
 ("agreeing root sets, differing evidence quotation; auditor = fabricated third", [CH()],[CH(ev_verbatim="we choose a = 2 (sic)")], {"i1":full(CH(ev_verbatim="fabricated"))}, 1, NEITHER, None),
 ("wrong-owner dependency: i9 belongs to c2 but reconstructed under cZ", [DER(["i9"]),rec("c2","i9")],[DER(["i9"]),rec("c2","i9")], {"i1":full(DER(["i9"]))}, 1, "", None),
 ("transitive: dependency in another claim disputed, auditor matches its alternative", [DER(["i9"]),rec("c2","i9",origin="CHOSEN",ev_reason_code="ORIG_CHOICE_STATED",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2")],[DER(["i9"]),rec("c2","i9",origin="FITTED",ev_reason_code="ORIG_FIT_STATED",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2")], {"i1":full(DER(["i9"]))}, 0, "", None),
]
def cands(): return w("sc.json",{"declared_candidate_count":3,"declared_included_count":3,"declared_excluded_count":0,"declared_attempt_count":1,"candidates":[{"candidate_id":"c1","source_file":"paperA.txt","source_line":4,"numeral":"4","included":True,"attempts":1,"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4"},{"candidate_id":"c2","source_file":"paperB.txt","source_line":9,"numeral":"7","included":True,"attempts":0,"outcome":"REPRO_NOT_EVALUABLE"},{"candidate_id":"cZ","source_file":"paperB.txt","source_line":11,"numeral":"8","included":True,"attempts":0,"outcome":"REPRO_NOT_EVALUABLE"}]})
def audit(tag, merged, extra_inputs, wrong_owner=False):
    sc=cands(); sx=w("sx.json",{"declared_exclusion_count":0,"exclusions":[]}); ac=sc; ax=sx
    s1=W/f"{tag}_s1.txt"; sel=W/f"{tag}_sel.json"; s2=W/f"{tag}_s2.txt"
    run(SEAT,"audit","seal-enumeration",ac,ax,s1); run(SEAT,"audit","select",sc,"0123456789abcdef"*4,s1,sel)
    S=json.loads(sel.read_text()); rd={cid:{"outcome":("REPRO_WITHIN_STATED_PRECISION" if cid=="c1" else "REPRO_NOT_EVALUABLE"),"printed_value":"4","reproduced_value":"4","inputs":(extra_inputs if cid=="c1" else {})} for cid in S["audited_ids"]}
    # dependency records for other claims (transitive / wrong-owner constructions)
    if "i9" in json.dumps(extra_inputs) or wrong_owner:
        owner="cZ" if wrong_owner else "c2"; rd[owner]=rd.get(owner,{"outcome":"REPRO_NOT_EVALUABLE","printed_value":None,"reproduced_value":None,"inputs":{}})
        mrec=[r for r in json.loads(pathlib.Path(merged).read_text())["records"] if r["input_id"]=="i9"][0]
        alt=full(mrec)
        if mrec.get("origin_alt"): alt=dict(alt,origin=mrec["origin_alt"],origin_evidence=mrec["origin_evidence_alt"])
        rd[owner]["inputs"]["i9"]=alt
    rdp=w(f"{tag}_rd.json",rd); run(SEAT,"audit","seal-rederivation",rdp,s2)
    rc,out=run(SEAT,"audit","compare",s1,ac,ax,sc,sx,merged,sel,s2,rdp,W/f"{tag}_C6.json")
    fails=[l for l in out.splitlines() if l.startswith("FAIL:")]   # emitted order, not sorted
    art=json.loads((W/f"{tag}_C6.json").read_text()) if (W/f"{tag}_C6.json").exists() else {}
    return rc, fails, art
results=[]; allok=True
for i,(name,A,B,aud,exp,must,comp) in enumerate(CONS):
    a=w(f"c{i}_A.json",{"records":A}); b=w(f"c{i}_B.json",{"records":B}); outs=[]
    for perm,(x,y) in enumerate(((a,b),(b,a))):
        m=W/f"c{i}_m{perm}.json"; rcm,om=run(LANE,"merge",x,y,m)
        if rcm!=0: outs.append(("MERGE_FAIL",om)); continue
        rcc,oc=run(LANE,"compute",m,W/f"c{i}_m{perm}_compute.json",cands()); oc=oc.replace(str(W),"<W>")
        outs.append((hashlib.sha256(m.read_bytes()).hexdigest(), audit(f"c{i}p{perm}", str(m), aud, wrong_owner=("wrong-owner" in name)), (rcc,oc)))
    same_bytes = (outs[0][0]==outs[1][0]); same_outcome = (outs[0][1]==outs[1][1] and outs[0][2]==outs[1][2]) if all(len(o)==3 and o[0]!="MERGE_FAIL" for o in outs) else False
    v=[(o[1][0] if o[0]!="MERGE_FAIL" else "MERGE_FAIL") for o in outs]
    exp_ok = (v==[exp,exp]) and all((must=="" or any(must in f for f in o[1][1])) for o in outs if o[0]!="MERGE_FAIL")
    comp_ok = (comp is None) or all(len(o)==3 and o[2][0]==0 and comp in o[2][1] for o in outs)
    exp_ok = exp_ok and comp_ok
    ok=same_bytes and same_outcome and exp_ok; allok&=ok; results.append((name,ok,same_bytes,same_outcome,exp_ok))
    print(("ok  " if ok else "BAD ")+f"{name}: merged-bytes-equal={same_bytes} outcome-equal={same_outcome} verdict(AB,BA)={v} expected={exp} diagnostic-present={exp_ok} compute={[o[2][0] if len(o)==3 else None for o in outs]}")
print("SPI="+("PASS" if allok else "FAIL")); sys.exit(0 if allok else 1)
