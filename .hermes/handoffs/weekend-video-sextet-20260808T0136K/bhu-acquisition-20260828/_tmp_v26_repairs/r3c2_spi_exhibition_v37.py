#!/usr/bin/env python3
"""r3c2_spi_exhibition.py — SEAT-PERMUTATION INVARIANCE (SPI) exhibition.
MEANINGLESS-ORDER INVARIANCE exhibition (one combined property). For each construction: run every combination of seat order {AB, BA} and PYTHONHASHSEED in SEEDS, plus one run with both seat ledgers' record lists reversed, one with the rederivation file's member order reversed, two with every dependency LIST reversed in both seat ledgers (both seat orders) and one with every dependency list reversed in the auditor's reconstruction; require identical merged bytes, identical lane compute exit code and output, identical audit exit code, identical ORDERED failure lines and identical complete C6_AUDIT.json (sealed_ledger_sha256 included); also assert the construction's expected verdict, required diagnostic and, where stated, a successful compute with a DISPUTED pair. --only SUBSTR restricts to constructions whose name contains SUBSTR (per-subcase fail-first); --seeds a,b,c overrides the seeds.
  /usr/bin/python3 -E r3c2_spi_exhibition.py <tools_dir> <work_dir>      prints SPI=PASS|FAIL and one line per construction."""
import json, subprocess, sys, pathlib, hashlib, shutil, itertools
TOOLS=pathlib.Path(sys.argv[1]).resolve(); W=pathlib.Path(sys.argv[2]).resolve(); shutil.rmtree(W,ignore_errors=True); W.mkdir(parents=True)
SEAT=TOOLS/"r3c2_ledger_tools.py"; LANE=TOOLS/"r3c2_lane_tools.py"; PY="/usr/bin/python3"
import os
ONLY=None; SEEDS=[0,1,2]
_argv=sys.argv[1:]
if "--only" in _argv: k=_argv.index("--only"); ONLY=_argv[k+1]; del _argv[k:k+2]
if "--seeds" in _argv: k=_argv.index("--seeds"); SEEDS=[int(x) for x in _argv[k+1].split(",")]; del _argv[k:k+2]
sys.argv=[sys.argv[0]]+_argv
SEED=None
def run(tool,*a):
    env=dict(os.environ)
    if SEED is not None: env["PYTHONHASHSEED"]=str(SEED)
    r=subprocess.run([PY,str(tool),*[str(x) for x in a]],capture_output=True,text=True,env=env); return r.returncode, r.stdout+r.stderr
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
def CX(iid,sym,origin,code,parents,evline,evtext,valline):
    return rec(iid=iid,symbol=sym,origin=origin,ev_reason_code=code,ev_source_file="p.txt",ev_source_line=evline,ev_verbatim=evtext,derived_from=parents,value="2",source_file="p.txt",source_line=valline)
# codex V35 F1: x is CHOSEN with parents; A x→y→r, B y→x→r; auditor = A.x + B.y + r is a matched graph with the cycle x→y→x through a CHOSEN record
F1A=[CX("x","x","CHOSEN","ORIG_CHOICE_STATED",["y"],1,"We choose x = 2 using y.",1),CX("y","y","DERIVED","ORIG_EQUATION",["r"],2,"y is calculated as 2 from r.",2),CX("r","r","MEASURED","ORIG_MEASURED",[],3,"We measure r = 2 using a ruler.",3)]
F1B=[CX("x","x","CHOSEN","ORIG_CHOICE_STATED",["r"],4,"We choose x = 2 using r.",1),CX("y","y","DERIVED","ORIG_EQUATION",["x"],5,"y is calculated as 2 from x.",2),CX("r","r","MEASURED","ORIG_MEASURED",[],3,"We measure r = 2 using a ruler.",3)]
# codex V35 F2: same topology, x DERIVED; the mixed auditor's matched graph is an all-DERIVED cycle — the diagnostic must be identical in every process
F2A=[CX("x","x","DERIVED","ORIG_EQUATION",["y"],1,"x is calculated as 2 from y.",1),CX("y","y","DERIVED","ORIG_EQUATION",["r"],2,"y is calculated as 2 from r.",2),CX("r","r","MEASURED","ORIG_MEASURED",[],3,"We measure r = 2 using a ruler.",3)]
F2B=[CX("x","x","DERIVED","ORIG_EQUATION",["r"],4,"x is calculated as 2 from r.",1),CX("y","y","DERIVED","ORIG_EQUATION",["x"],5,"y is calculated as 2 from x.",2),CX("r","r","MEASURED","ORIG_MEASURED",[],3,"We measure r = 2 using a ruler.",3)]
GI="graph integrity"
# codex V36 F1: x DERIVED from two measured parents — the only shape in which dependency-LIST order can differ while the dependency SET is equal
DP=[CX("x","x","DERIVED","ORIG_EQUATION",["y","z"],1,"x = 2 from y and z.",1),CX("y","y","MEASURED","ORIG_MEASURED",[],2,"We measure y = 2.",2),CX("z","z","MEASURED","ORIG_MEASURED",[],3,"We measure z = 2.",3)]
# source (c): several diagnostics at once — two missing dependencies and two mismatching inputs; their emitted ORDER must be identical under every seed
MD_A=[CX("x","x","DERIVED","ORIG_EQUATION",["y","r"],1,"x from y and r.",1),CX("y","y","DERIVED","ORIG_EQUATION",["r"],2,"y from r.",2),CX("r","r","MEASURED","ORIG_MEASURED",[],3,"We measure r = 2.",3)]
MD_AUD={"x":dict(full(MD_A[0]),derived_from=["q2","q1","y"]),"y":dict(full(MD_A[1]),value="9"),"r":dict(full(MD_A[2]),value="7")}
CONS=[
 ("same-origin, different complete searches (codex V32 F1); auditor = B", [SIL(S1)],[SIL(S2)], {"i1":dict(full(SIL(S2)),origin_search=S2)}, 0, "", None),
 ("structurally equal seat records, different top-level and nested member order (codex V33 F1); auditor = the record", [rec()],[rev(rec())], {"i1":full(rec())}, 0, "", None),
 ("two acyclic seat graphs whose per-input mix is a cycle (codex V34 F1: A x→y→r, B y→x→r); auditor = complete A", CYA, CYB, {"x":full(CYA[0]),"y":full(CYA[1]),"r":full(CYA[2])}, 0, "", "DISPUTED"),
 ("same two graphs; auditor = complete B", CYA, CYB, {"x":full(CYB[0]),"y":full(CYB[1]),"r":full(CYB[2])}, 0, "", "DISPUTED"),
 ("matched cycle through a CHOSEN record with parents (codex V35 F1): auditor = A.x + B.y + r", F1A, F1B, {"x":full(F1A[0]),"y":full(F1B[1]),"r":full(F1A[2])}, 1, GI, None),
 ("same seats; auditor = complete A (expected PASS control)", F1A, F1B, {"x":full(F1A[0]),"y":full(F1A[1]),"r":full(F1A[2])}, 0, "", "DISPUTED"),
 ("same seats; auditor = complete B (expected PASS control)", F1A, F1B, {"x":full(F1B[0]),"y":full(F1B[1]),"r":full(F1B[2])}, 0, "", "DISPUTED"),
 ("all-DERIVED matched cycle (codex V35 F2): auditor = A.x + B.y + r — diagnostic must be identical across fresh processes and seeds", F2A, F2B, {"x":full(F2A[0]),"y":full(F2B[1]),"r":full(F2A[2])}, 1, GI, None),
 ("missing dependency in the auditor's closure: auditor's x names parent q that no record supplies", F2A, F2B, {"x":dict(full(F2A[0]),derived_from=["q"]),"y":full(F2A[1]),"r":full(F2A[2])}, 1, GI, None),
 ("dependency-list order (codex V36 F1, MOI source f): x DERIVED from two measured parents; every run reverses nothing else", DP, DP, {"x":full(DP[0]),"y":full(DP[1]),"z":full(DP[2])}, 0, "", None),
 ("multi-diagnostic ordering (source c): two missing dependencies q1,q2 and two value mismatches — identical ordered failure set under every seed and order", MD_A, MD_A, MD_AUD, 1, GI, None),
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
def outcome(i, x, y, aud, name, seed, tag):
    """one complete run: merge(x,y) -> compute -> audit; returns (merged_sha, (compute rc, out), (audit rc, ordered FAIL lines, complete artefact)) or ("MERGE_FAIL", out)"""
    global SEED
    SEED=seed
    m=W/f"c{i}_{tag}.json"; rcm,om=run(LANE,"merge",x,y,m)
    if rcm!=0: SEED=None; return ("MERGE_FAIL",om)
    rcc,oc=run(LANE,"compute",m,W/f"c{i}_{tag}_compute.json",cands()); oc=oc.replace(str(W),"<W>")
    r=(hashlib.sha256(m.read_bytes()).hexdigest(), (rcc,oc), audit(f"c{i}{tag}", str(m), aud, wrong_owner=("wrong-owner" in name)))
    SEED=None; return r
for i,(name,A,B,aud,exp,must,comp) in enumerate(CONS):
    if ONLY and ONLY not in name: continue
    a=w(f"c{i}_A.json",{"records":A}); b=w(f"c{i}_B.json",{"records":B})
    ar=w(f"c{i}_Ar.json",{"records":list(reversed(A))}); br=w(f"c{i}_Br.json",{"records":list(reversed(B))})   # source (b): record arrival order
    def _revdep(recs_):   # source (f): dependency-list order — same edges, reversed list
        out=[]
        for r0 in recs_:
            r1=dict(r0)
            if r1.get("derived_from"): r1["derived_from"]=list(reversed(r1["derived_from"]))
            out.append(r1)
        return out
    ad=w(f"c{i}_Ad.json",{"records":_revdep(A)}); bd=w(f"c{i}_Bd.json",{"records":_revdep(B)})
    aud_revdep={k:(dict(v,derived_from=list(reversed(v["derived_from"]))) if isinstance(v,dict) and v.get("derived_from") else v) for k,v in aud.items()}
    aud_rev={k:aud[k] for k in reversed(list(aud))}                                                                # source (d)/(b): rederivation member order
    runs={}
    for perm,(x,y) in (("AB",(a,b)),("BA",(b,a))):
        for sd in SEEDS: runs[f"{perm}/seed{sd}"]=outcome(i,x,y,aud,name,sd,f"{perm}s{sd}")
    runs["AB/seed0/reversed-arrival"]=outcome(i,ar,br,aud,name,SEEDS[0],"ABrev")
    runs["AB/seed0/reversed-rederivation-order"]=outcome(i,a,b,aud_rev,name,SEEDS[0],"ABrd")
    runs["AB/seed0/reversed-dependency-order"]=outcome(i,ad,bd,aud,name,SEEDS[0],"ABdep")
    runs["BA/seed0/reversed-dependency-order"]=outcome(i,bd,ad,aud,name,SEEDS[0],"BAdep")
    runs["AB/seed0/reversed-auditor-dependency-order"]=outcome(i,a,b,aud_revdep,name,SEEDS[0],"ABauddep")
    keys=list(runs); base=runs[keys[0]]
    def AUD_BYTES_VARY(k): return ("reversed-rederivation-order" in k) or ("reversed-auditor-dependency-order" in k)
    def cmp_view(k):
        """the reversed-rederivation-order run delivers DIFFERENT BYTES to the auditor-file seal; that seal is the digest of what was delivered
        (an identity, not an ordering) and is the ONLY field allowed to differ in the variants that reorder the delivered auditor file — every finding, code, reason, verdict, merged byte
        and ledger digest must still be equal."""
        r=runs[k]
        if r[0]=="MERGE_FAIL" or not AUD_BYTES_VARY(k): return r
        art=dict(r[2][2]); art.pop("rederivation_seal",None); return (r[0],r[1],(r[2][0],r[2][1],art))
    base_v=cmp_view(keys[0]); base_rd=dict(base[2][2]) if base[0]!="MERGE_FAIL" else None
    if base_rd is not None: base_rd.pop("rederivation_seal",None); base_v=(base[0],base[1],(base[2][0],base[2][1],base_rd))
    merged_ok=all(runs[k][0]==base[0] for k in keys)
    whole_ok=all((runs[k]==base) if not AUD_BYTES_VARY(k) else (cmp_view(k)==base_v) for k in keys)
    v=sorted(set((runs[k][2][0] if runs[k][0]!="MERGE_FAIL" else "MERGE_FAIL") for k in keys),key=str)
    exp_ok=(v==[exp]) and all((must=="" or any(must in f for f in runs[k][2][1])) for k in keys if runs[k][0]!="MERGE_FAIL")
    comp_ok=(comp is None) or all(runs[k][0]!="MERGE_FAIL" and runs[k][1][0]==0 and comp in runs[k][1][1] for k in keys)
    ok=merged_ok and whole_ok and exp_ok and comp_ok; allok&=ok; results.append((name,ok))
    diff=[k for k in keys if ((runs[k]!=base) if not AUD_BYTES_VARY(k) else (cmp_view(k)!=base_v))]
    print(("ok  " if ok else "BAD ")+f"{name}: merged-bytes-equal={merged_ok} whole-outcome-equal={whole_ok} verdicts={v} expected={exp} diagnostic-present={exp_ok} compute-ok={comp_ok}"+("" if not diff else f" DIFFERING_RUNS={diff}"))
print(f"runs per construction: 2 seat orders x seeds {SEEDS} + reversed arrival + reversed rederivation order + reversed dependency order (both seat orders) + reversed auditor dependency order; ONLY={ONLY!r}")
print("SPI="+("PASS" if allok else "FAIL")); sys.exit(0 if allok else 1)
