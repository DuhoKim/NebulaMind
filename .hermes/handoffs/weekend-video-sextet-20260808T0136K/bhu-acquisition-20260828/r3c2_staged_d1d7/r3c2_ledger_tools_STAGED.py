#!/usr/bin/env python3
"""r3c2_ledger_tools_STAGED.py — STAGED, UNADOPTED (D1 + D7 candidates, 2026-09-06); NOT the pinned seat tool. The seat's ledger tool for the R3-C2 census.

  /usr/bin/python3 -E r3c2_ledger_tools.py census   <candidates.json> <exclusions.json>
      C1: candidates.json = {declared_candidate_count, declared_included_count, declared_excluded_count,
      declared_attempt_count, candidates:[...]} — every included candidate carries attempts in {0,1,2} and outcome (a section-3 token or PENDING; `census ... final` rejects PENDING and requires printed_value/reproduced_value on arithmetic outcomes); exclusions.json =
      {declared_exclusion_count, exclusions:[...]}; every candidate has exactly one disposition; every exclusion row carries source_file, source_line and numeral equal to its candidate row (retained, not discarded); the AUTHOR_SPECIFIED_INPUT count is printed beside the denominator; the declared counts are
      compared with the recomputed counts and any mismatch FAILS; exit 0 PASS / 1 FAIL.
  STAGED (D1, UNADOPTED): a PRINTED record with reason_code ORIG_CITATION is an imported value — its verbatim is matched at the
      CLAIMING paper's citing sentence (origin_evidence.source_file/source_line) and its value at the EXTERNAL value line
      (record source_file/source_line), which must be an enumerable text of R3C2_CORPUS_MANIFEST.md in <sources_dir>; no
      reason-code test is applied to the external line's own wording.
  STAGED (D7, UNADOPTED): audit subcommands — see cmd_audit_*: `audit seal-enumeration`, `audit select`, `audit compare`.
  /usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> <sources_dir>
      asserts: every record has the schema fields and no field outside the schema; status in
      {PRINTED,STANDARD,ABSENT,BLOCKED}; origin in {CHOSEN,DERIVED,FITTED,IMPORTED,MEASURED,STANDARD,UNDECLARED};
      reason_code/origin pair is one of the allowed pairs; no ABSENT or BLOCKED record carries a value; a BLOCKED record
      (traced to a named source, no machine-matchable value) carries origin IMPORTED with ORIG_CITATION evidence and is
      never consumed; every PRINTED record's verbatim quotation is a substring of the cited source line; every STANDARD
      value is on the closed list; derived_from ids exist, a DERIVED record names its parents, and the graph is acyclic;
      an ORIG_SILENT record carries origin_search {query, files, matches}. Exit 0 = PASS, 1 = FAIL (every failure
      printed), 2 = usage/schema error.
"""
import json, sys, pathlib, hashlib, random, math

STATUS={"PRINTED","STANDARD","ABSENT","BLOCKED"}
OUTCOMES={"REPRO_WITHIN_STATED_PRECISION","REPRO_FAILED","REPRO_BLOCKED","REPRO_INPUT_ABSENT","REPRO_NOT_EVALUABLE","REPRO_NO_DERIVATION_STATED"}
ARITH={"REPRO_WITHIN_STATED_PRECISION","REPRO_FAILED"}
ORIGIN={"CHOSEN","DERIVED","FITTED","IMPORTED","MEASURED","STANDARD","UNDECLARED"}
PAIRS={"ORIG_EQUATION":"DERIVED","ORIG_CONSTANT":"STANDARD","ORIG_MEASURED":"MEASURED","ORIG_CHOICE_STATED":"CHOSEN","ORIG_FIT_STATED":"FITTED","ORIG_CITATION":"IMPORTED","ORIG_SILENT":"UNDECLARED"}
# when more than one reason code matches the cited sentence, the first applicable in this order is filed (a sentence
# naming an external source for the value is a citation whatever else it says):
# external source for the value is a citation whatever else it says):
CODE_PRECEDENCE=["ORIG_CITATION","ORIG_FIT_STATED","ORIG_CHOICE_STATED","ORIG_MEASURED","ORIG_EQUATION","ORIG_CONSTANT","ORIG_SILENT"]
STANDARD_LIST={"G":"6.67430e-11","c":"2.99792458e8","hbar":"1.054571817e-34","k_B":"1.380649e-23","H0":"67.36","Omega_m":"0.3153","Omega_L":"0.6847","Omega_b_h2":"0.02237","Omega_c_h2":"0.1200","n_s":"0.9649","sigma8":"0.8111","tau":"0.0544","ln1e10As":"3.044","age_Gyr":"13.797"}
FIELDS=["claim_id","input_id","symbol","status","origin","origin_evidence","derived_from","value","source_file","source_line"]

def read_line(srcdir, f, n):
    try: return (pathlib.Path(srcdir)/str(f)).read_text(errors="replace").splitlines()[int(n)-1]
    except Exception: return None

def enumerable(srcdir, f):
    m=pathlib.Path(srcdir)/"R3C2_CORPUS_MANIFEST.md"
    if m.exists(): return ("`"+str(f)+"`") in m.read_text(errors="replace")
    return (pathlib.Path(srcdir)/str(f)).exists()

def load(p):
    d=json.loads(pathlib.Path(p).read_text())
    recs=d["records"] if isinstance(d,dict) else d
    assert isinstance(recs,list) and recs, "ledger has no records"
    return d,recs


def roots(rec_by_id, rid, seen=None):
    seen=seen or set()
    if rid in seen: raise ValueError(f"cycle at {rid}")
    r=rec_by_id[rid]; seen=seen|{rid}
    if r["origin"]=="DERIVED" and not r.get("derived_from"): raise ValueError(f"{rid}: DERIVED record with no derived_from (a derived input must name what it was derived from)")
    if r["origin"]!="DERIVED": return {r["origin"]}
    out=set()
    for d in r["derived_from"]:
        if d not in rec_by_id: raise ValueError(f"{rid}: derived_from {d} not in ledger")
        out|=roots(rec_by_id,d,seen)
    return out



def cmd_validate(ledger,srcdir):
    d,recs=load(ledger); fails=[]; ids=set()
    for r in recs:
        missing=[f for f in FIELDS if f not in r]
        if missing: fails.append(f"{r.get('input_id')}: missing {missing}"); continue
        if r["input_id"] in ids: fails.append(f"{r['input_id']}: duplicate id")
        ids.add(r["input_id"])
        if r["status"] not in STATUS: fails.append(f"{r['input_id']}: bad status {r['status']}")
        if r["origin"] not in ORIGIN: fails.append(f"{r['input_id']}: bad origin {r['origin']}")
        ev=r["origin_evidence"]; rc=ev.get("reason_code")
        extra=[k for k in r if k not in FIELDS+["origin_search"]]
        if extra: fails.append(f"{r['input_id']}: seat-authored ledger carries a field outside the schema: {extra}")
        if rc=="ORIG_SILENT":
            srch=r.get("origin_search")
            if not isinstance(srch,dict) or not all(k in srch for k in ("query","files","matches")): fails.append(f"{r['input_id']}: ORIG_SILENT requires origin_search {{query, files, matches}}")
        if PAIRS.get(rc)!=r["origin"]: fails.append(f"{r['input_id']}: reason_code {rc} does not map to origin {r['origin']}")
        if r["status"]=="ABSENT" and r.get("value") not in (None,""): fails.append(f"{r['input_id']}: ABSENT record carries a value")
        if r["status"]=="BLOCKED":
            if r.get("value") not in (None,""): fails.append(f"{r['input_id']}: BLOCKED record carries a value")
            if r["origin"]!="IMPORTED" or rc!="ORIG_CITATION": fails.append(f"{r['input_id']}: BLOCKED record must carry origin IMPORTED with ORIG_CITATION evidence from the claiming paper")
        if r["status"]=="STANDARD" and str(r.get("value"))!=STANDARD_LIST.get(r["symbol"]): fails.append(f"{r['input_id']}: STANDARD value {r.get('value')} for {r['symbol']} not on the closed list")
        if r["status"]=="PRINTED" and rc=="ORIG_CITATION":
            # STAGED D1 — an imported value: verbatim at the claiming paper's citing sentence, value at the external value line
            ef=str(ev.get("source_file","")); el=ev.get("source_line")
            if ef==r["source_file"]: fails.append(f"{r['input_id']}: IMPORTED PRINTED record names its own file as the external source")
            if not enumerable(srcdir, r["source_file"]): fails.append(f"{r['input_id']}: external source {r['source_file']} is not an enumerable text of the manifest")
            cl=read_line(srcdir, ef, el)
            if cl is None: fails.append(f"{r['input_id']}: cannot read citing sentence {ef}:{el}")
            elif ev.get("verbatim","") not in cl: fails.append(f"{r['input_id']}: verbatim not found at citing sentence {ef}:{el}")  # PROBE:D1_VERBATIM_SITE
            vl=read_line(srcdir, r["source_file"], r["source_line"])
            if vl is None: fails.append(f"{r['input_id']}: cannot read external value line {r['source_file']}:{r['source_line']}")
            elif str(r.get("value")) not in vl: fails.append(f"{r['input_id']}: value {r.get('value')} not at external value line {r['source_file']}:{r['source_line']}")  # PROBE:D1_VALUE_SITE
            continue
        if r["status"]=="PRINTED":
            f=pathlib.Path(srcdir)/r["source_file"]
            try: line=f.read_text(errors="replace").splitlines()[int(r["source_line"])-1]
            except Exception as e: fails.append(f"{r['input_id']}: cannot read {r['source_file']}:{r['source_line']} ({e})"); continue
            if rc!="ORIG_SILENT" and ev.get("verbatim","") not in line: fails.append(f"{r['input_id']}: verbatim not found at {r['source_file']}:{r['source_line']}")
            if str(r.get("value")) not in line: fails.append(f"{r['input_id']}: value {r.get('value')} not at cited line")
    by={r["input_id"]:r for r in recs}
    for r in recs:
        for dfrom in r.get("derived_from") or []:
            if dfrom not in by: fails.append(f"{r['input_id']}: derived_from {dfrom} absent")
        try: roots(by,r["input_id"])
        except ValueError as e: fails.append(str(e))
    for x in fails: print("FAIL:",x)
    print("C3_NO_SUBSTITUTION=" + ("PASS" if not fails else "FAIL")); return 0 if not fails else 1

def cmd_census(candidates,exclusions,final=False):
    """C1: every candidate passage has exactly one disposition (included or excluded with a reason kind); counts recomputed."""
    Cd=json.loads(pathlib.Path(candidates).read_text()); Xd=json.loads(pathlib.Path(exclusions).read_text())
    fails=[]; KINDS={"AUTHOR_SPECIFIED_INPUT","ATTRIBUTED_NOT_DERIVED","DATE","EQUATION_NUMBER","PAGE_OR_LINE_NUMBER","REFERENCE_NUMBER"}
    if not isinstance(Cd,dict) or "candidates" not in Cd: print("FAIL: candidates file must be an object {declared_candidate_count, declared_included_count, declared_excluded_count, candidates:[...]}"); print("C1_DENOMINATOR_PRINTED=FAIL"); return 1
    if not isinstance(Xd,dict) or "exclusions" not in Xd: print("FAIL: exclusions file must be an object {declared_exclusion_count, exclusions:[...]}"); print("C1_DENOMINATOR_PRINTED=FAIL"); return 1
    C=Cd["candidates"]; X=Xd["exclusions"]
    for k in ("declared_candidate_count","declared_included_count","declared_excluded_count","declared_attempt_count"):
        if k not in Cd: fails.append(f"candidates file: missing {k}")
    if "declared_exclusion_count" not in Xd: fails.append("exclusions file: missing declared_exclusion_count")
    cids={}
    for n,c in enumerate(C,1):
        if not isinstance(c,dict) or "candidate_id" not in c:
            fails.append(f"candidate #{n}: missing candidate_id"); continue
        for f in ["source_file","source_line","numeral","included"]:
            if f not in c: fails.append(f"candidate {c.get('candidate_id')}: missing {f}")
        if c.get("included"):
            if "attempts" not in c or c["attempts"] not in (0,1,2): fails.append(f"candidate {c.get('candidate_id')}: included claim must carry attempts in {{0,1,2}}")
            oc=c.get("outcome")
            if oc is None: fails.append(f"candidate {c.get('candidate_id')}: included claim must carry outcome (a section-3 token, or PENDING before limb B)")
            elif oc not in OUTCOMES and oc!="PENDING": fails.append(f"candidate {c.get('candidate_id')}: outcome {oc!r} is not a section-3 token")
            elif oc=="PENDING" and final: fails.append(f"candidate {c.get('candidate_id')}: outcome still PENDING in final census")
            elif oc in ARITH and not (isinstance(c.get("printed_value"),str) and isinstance(c.get("reproduced_value"),str)): fails.append(f"candidate {c.get('candidate_id')}: arithmetic outcome must carry printed_value and reproduced_value as strings")
        if c.get("candidate_id") in cids: fails.append(f"candidate {c['candidate_id']}: duplicate")
        cids[c.get("candidate_id")]=c
    xids=set()
    for n,x in enumerate(X,1):
        if not isinstance(x,dict) or "candidate_id" not in x: fails.append(f"exclusion #{n}: missing candidate_id"); continue
        if x.get("candidate_id") not in cids: fails.append(f"exclusion {x.get('candidate_id')}: not a candidate")
        if x.get("kind") not in KINDS: fails.append(f"exclusion {x.get('candidate_id')}: kind {x.get('kind')} not predeclared")
        if x.get("candidate_id") in xids: fails.append(f"exclusion {x.get('candidate_id')}: duplicate")
        xids.add(x.get("candidate_id"))
    for cid,c in cids.items():
        if c.get("included") and cid in xids: fails.append(f"candidate {cid}: included AND excluded")
        if not c.get("included") and cid not in xids: fails.append(f"candidate {cid}: excluded with no exclusion row")
    xrows={x.get("candidate_id"): x for x in Xd.get("exclusions",[]) if isinstance(x,dict)}
    for cid,x in xrows.items():
        c=cids.get(cid)
        for f in ("source_file","source_line","numeral"):
            if f not in x: fails.append(f"exclusion {cid}: missing {f} (the excluded numeral and its line are retained in the exclusion ledger)")
            elif c is not None and x.get(f)!=c.get(f): fails.append(f"exclusion {cid}: {f} differs from the candidate row")
    inc=sum(1 for c in cids.values() if c.get("included")); exc=len(xids)
    att=sum(int(c.get("attempts",0)) for c in cids.values() if c.get("included"))
    for k,v in (("declared_candidate_count",len(cids)),("declared_included_count",inc),("declared_excluded_count",exc),("declared_attempt_count",att)):
        if k in Cd and Cd[k]!=v: fails.append(f"{k}={Cd[k]} but recomputed {v}")
    if "declared_exclusion_count" in Xd and Xd["declared_exclusion_count"]!=exc: fails.append(f"declared_exclusion_count={Xd['declared_exclusion_count']} but recomputed {exc}")
    for x in fails: print("FAIL:",x)
    print(f"declared: candidates={Cd.get('declared_candidate_count')} included={Cd.get('declared_included_count')} excluded={Cd.get('declared_excluded_count')} attempts={Cd.get('declared_attempt_count')} exclusions={Xd.get('declared_exclusion_count')}")
    oc_t={}
    for c in cids.values():
        if c.get("included"): oc_t[c.get("outcome")]=oc_t.get(c.get("outcome"),0)+1
    print("outcomes:", " ".join(f"{k}={v}" for k,v in sorted(oc_t.items(), key=lambda kv: str(kv[0]))))
    asi=sum(1 for x in Xd.get("exclusions",[]) if isinstance(x,dict) and x.get("kind")=="AUTHOR_SPECIFIED_INPUT")
    print(f"author_specified_input={asi}")
    print(f"recomputed: candidates={len(cids)} included={inc} excluded={exc} attempts={att} reconciled={'YES' if not fails and inc+exc==len(cids) else 'NO'}")
    print("C1_DENOMINATOR_PRINTED=" + ("PASS" if not fails and inc+exc==len(cids) else "FAIL")); return 0 if not fails and inc+exc==len(cids) else 1


def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def ckey(c): return (str(c.get("source_file")), int(c.get("source_line")), str(c.get("numeral")))

def cmd_audit_seal(ac, ax, out):
    """STAGED D7 stage-1 seal: the custodian records the auditor's OWN enumeration digests BEFORE any sealed ledger is revealed."""
    pathlib.Path(out).write_text(f"AUDITOR_CANDIDATES_SHA256={sha(ac)}\nAUDITOR_EXCLUSIONS_SHA256={sha(ax)}\n"); print(pathlib.Path(out).read_text(), end=""); return 0

def cmd_audit_select(sc, seed_hex, out):
    """STAGED D7 stage-2 selection (custodian): every arithmetic-group claim + k of the remaining, seeded from outside."""
    if not (isinstance(seed_hex,str) and len(seed_hex)==64 and all(ch in "0123456789abcdef" for ch in seed_hex)): print("FAIL: seed must be 64 lowercase hexadecimal characters"); return 1
    C=json.loads(pathlib.Path(sc).read_text())["candidates"]
    inc=sorted(c["candidate_id"] for c in C if c.get("included")); arith=sorted(c["candidate_id"] for c in C if c.get("included") and c.get("outcome") in ARITH)
    rem=sorted(set(inc)-set(arith)); N=len(inc); R=len(rem); k=min(max(1,math.ceil(0.20*N)),R)
    samp=sorted(random.Random(int(seed_hex,16)).sample(rem,k)) if k>0 else []
    sel={"sealed_candidates_sha256":sha(sc),"seed_hex":seed_hex,"N":N,"R":R,"k":k,"arithmetic_group_ids":arith,"remaining_ids":rem,"sampled_ids":samp,"audited_ids":sorted(set(arith)|set(samp))}
    pathlib.Path(out).write_text(json.dumps(sel,indent=1,sort_keys=True)); print(f"N={N} R={R} k={k} audited={len(sel['audited_ids'])}"); return 0

def cmd_audit_compare(seal, ac, ax, sc, sx, sl, sel, red, out):
    """STAGED D7 stage-3: only after the stage-1 seal and the selection exist are the sealed ledgers compared with the auditor's."""
    fails=[]; sealtxt=pathlib.Path(seal).read_text()
    if f"AUDITOR_CANDIDATES_SHA256={sha(ac)}" not in sealtxt or f"AUDITOR_EXCLUSIONS_SHA256={sha(ax)}" not in sealtxt: fails.append("C6_STAGE_ORDER: the auditor's enumeration differs from its stage-1 seal (enumeration must be sealed before any sealed ledger is revealed)")  # PROBE:C6_STAGE_ORDER
    S=json.loads(pathlib.Path(sel).read_text())
    if S.get("sealed_candidates_sha256")!=sha(sc): fails.append("C6_SELECTION: selection was computed over a different sealed candidate file")
    AC=json.loads(pathlib.Path(ac).read_text())["candidates"]; AX=json.loads(pathlib.Path(ax).read_text())["exclusions"]
    SC=json.loads(pathlib.Path(sc).read_text())["candidates"]; SX=json.loads(pathlib.Path(sx).read_text())["exclusions"]
    SL=json.loads(pathlib.Path(sl).read_text()); SL=SL["records"] if isinstance(SL,dict) else SL
    RD=json.loads(pathlib.Path(red).read_text())
    a_inc={ckey(c) for c in AC if c.get("included")}; a_all={ckey(c):c for c in AC}
    s_inc={ckey(c):c for c in SC if c.get("included")}; s_all={ckey(c):c for c in SC}
    comp={"sealed_included_absent_from_audit_enumeration":[], "audit_included_absent_from_sealed":[], "inclusion_disputed":[], "exclusion_kind_differs":[]}
    for k,c in s_inc.items():
        if k not in a_all: comp["sealed_included_absent_from_audit_enumeration"].append(list(k))
        elif k not in a_inc: comp["inclusion_disputed"].append(list(k))
    for k in a_inc:
        if k not in s_all: comp["audit_included_absent_from_sealed"].append(list(k))
        elif k not in s_inc: comp["inclusion_disputed"].append(list(k))
    akind={ckey(x):x.get("kind") for x in AX}; skind={ckey(x):x.get("kind") for x in SX}
    for k in set(akind)&set(skind):
        if akind[k]!=skind[k]: comp["exclusion_kind_differs"].append([list(k),skind[k],akind[k]])
    for k in comp["sealed_included_absent_from_audit_enumeration"]: fails.append(f"COMPLETENESS sealed_included_absent_from_audit_enumeration: {k}")  # PROBE:C6_SEALED_MISSING
    for k in comp["audit_included_absent_from_sealed"]: fails.append(f"COMPLETENESS audit_included_absent_from_sealed: {k}")  # PROBE:C6_BOTH_SEATS_MISSED
    # an inclusion disagreement on a passage BOTH sides list is a dispute, not an omission: listed and counted; above 10% of the sealed denominator it fails
    comp["inclusion_disputed_count"]=len(comp["inclusion_disputed"]); comp["inclusion_disputed_rate"]=(len(comp["inclusion_disputed"])/len(s_inc)) if s_inc else 0.0
    if s_inc and len(comp["inclusion_disputed"])/len(s_inc)>0.10: fails.append(f"AUDIT_INCLUSION_DISPUTED above 10% of the sealed denominator: {len(comp['inclusion_disputed'])}/{len(s_inc)}")  # PROBE:C6_DISPUTE_RATE
    s_by={c["candidate_id"]:c for c in SC}; l_by={}
    for r in SL: l_by.setdefault(r["claim_id"],{})[r["input_id"]]=r.get("origin")
    audited={}
    for cid in S["audited_ids"]:
        r=RD.get(cid); s=s_by.get(cid)
        if r is None or s is None: audited[cid]={"result":"MISMATCH","why":"no re-derivation supplied" if r is None else "not a sealed claim"}; fails.append(f"AUDIT {cid}: MISMATCH (missing)"); continue
        why=[]
        if r.get("outcome")!=s.get("outcome"): why.append(f"outcome {r.get('outcome')} vs sealed {s.get('outcome')}")
        if s.get("outcome") in ARITH and (str(r.get("printed_value"))!=str(s.get("printed_value")) or str(r.get("reproduced_value"))!=str(s.get("reproduced_value"))): why.append("printed/reproduced values differ")
        for iid,og in (r.get("inputs") or {}).items():
            if l_by.get(cid,{}).get(iid)!=og: why.append(f"origin {iid}: {og} vs sealed {l_by.get(cid,{}).get(iid)}")
        for iid in l_by.get(cid,{}):
            if iid not in (r.get("inputs") or {}): why.append(f"origin {iid}: not re-classified")
        audited[cid]={"result":"MATCH" if not why else "MISMATCH","why":why}
        if why: fails.append(f"AUDIT {cid}: MISMATCH ({'; '.join(why)})")
    tok="PASS" if not fails else "FAIL"
    res={"sealed_denominator":S["N"],"receipt_T_sealed_candidates_sha256":S["sealed_candidates_sha256"],"seed_hex":S["seed_hex"],"arithmetic_group_ids":S["arithmetic_group_ids"],"remaining_ids":S["remaining_ids"],"k":S["k"],"sampled_ids":S["sampled_ids"],"stage1_seal":sealtxt,"completeness":comp,"audited":audited,"C6_AUDIT_SAMPLE":tok}
    pathlib.Path(out).write_text(json.dumps(res,indent=1,sort_keys=True))
    for x in fails: print("FAIL:",x)
    print(json.dumps(res,indent=1,sort_keys=True)); print("C6_AUDIT_SAMPLE="+tok); return 0 if tok=="PASS" else 1


if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)==3 and a[0]=="validate": sys.exit(cmd_validate(a[1],a[2]))
    if len(a)==5 and a[0]=="audit" and a[1]=="seal-enumeration": sys.exit(cmd_audit_seal(a[2],a[3],a[4]))
    if len(a)==5 and a[0]=="audit" and a[1]=="select": sys.exit(cmd_audit_select(a[2],a[3],a[4]))
    if len(a)==11 and a[0]=="audit" and a[1]=="compare": sys.exit(cmd_audit_compare(*a[2:]))
    if len(a) in (3,4) and a[0]=="census" and (len(a)==3 or a[3]=="final"): sys.exit(cmd_census(a[1],a[2],final=(len(a)==4)))
    print(__doc__); sys.exit(2)
