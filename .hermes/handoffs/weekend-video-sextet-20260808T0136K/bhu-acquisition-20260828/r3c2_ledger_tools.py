#!/usr/bin/env python3
"""r3c2_ledger_tools.py — the seat's ledger tool for the R3-C2 census.

  /usr/bin/python3 r3c2_ledger_tools.py census   <candidates.json> <exclusions.json>
      C1: candidates.json = {declared_candidate_count, declared_included_count, declared_excluded_count,
      declared_attempt_count, candidates:[...]} — every included candidate carries attempts in {0,1,2}; exclusions.json =
      {declared_exclusion_count, exclusions:[...]}; every candidate has exactly one disposition; the declared counts are
      compared with the recomputed counts and any mismatch FAILS; exit 0 PASS / 1 FAIL.
  /usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> <sources_dir>
      asserts: every record has the schema fields and no field outside the schema; status in
      {PRINTED,STANDARD,ABSENT,BLOCKED}; origin in {CHOSEN,DERIVED,FITTED,IMPORTED,MEASURED,STANDARD,UNDECLARED};
      reason_code/origin pair is one of the allowed pairs; no ABSENT or BLOCKED record carries a value; a BLOCKED record
      (traced to a named source, no machine-matchable value) carries origin IMPORTED with ORIG_CITATION evidence and is
      never consumed; every PRINTED record's verbatim quotation is a substring of the cited source line; every STANDARD
      value is on the closed list; derived_from ids exist, a DERIVED record names its parents, and the graph is acyclic;
      an ORIG_SILENT record carries origin_search {query, files, matches}. Exit 0 = PASS, 1 = FAIL (every failure
      printed), 2 = usage/schema error.
"""
import json, sys, pathlib

STATUS={"PRINTED","STANDARD","ABSENT","BLOCKED"}
ORIGIN={"CHOSEN","DERIVED","FITTED","IMPORTED","MEASURED","STANDARD","UNDECLARED"}
PAIRS={"ORIG_EQUATION":"DERIVED","ORIG_CONSTANT":"STANDARD","ORIG_MEASURED":"MEASURED","ORIG_CHOICE_STATED":"CHOSEN","ORIG_FIT_STATED":"FITTED","ORIG_CITATION":"IMPORTED","ORIG_SILENT":"UNDECLARED"}
# when more than one reason code matches the cited sentence, the first applicable in this order is filed (a sentence
# naming an external source for the value is a citation whatever else it says):
# external source for the value is a citation whatever else it says):
CODE_PRECEDENCE=["ORIG_CITATION","ORIG_FIT_STATED","ORIG_CHOICE_STATED","ORIG_MEASURED","ORIG_EQUATION","ORIG_CONSTANT","ORIG_SILENT"]
STANDARD_LIST={"G":"6.67430e-11","c":"2.99792458e8","hbar":"1.054571817e-34","k_B":"1.380649e-23","H0":"67.36","Omega_m":"0.3153","Omega_L":"0.6847","Omega_b_h2":"0.02237","Omega_c_h2":"0.1200","n_s":"0.9649","sigma8":"0.8111","tau":"0.0544","ln1e10As":"3.044","age_Gyr":"13.797"}
FIELDS=["claim_id","input_id","symbol","status","origin","origin_evidence","derived_from","value","source_file","source_line"]

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

def cmd_census(candidates,exclusions):
    """C1: every candidate passage has exactly one disposition (included or excluded with a reason kind); counts recomputed."""
    Cd=json.loads(pathlib.Path(candidates).read_text()); Xd=json.loads(pathlib.Path(exclusions).read_text())
    fails=[]; KINDS={"EQUATION_NUMBER","REFERENCE_NUMBER","PAGE_OR_LINE_NUMBER","DATE","ATTRIBUTED_NOT_DERIVED"}
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
    inc=sum(1 for c in cids.values() if c.get("included")); exc=len(xids)
    att=sum(int(c.get("attempts",0)) for c in cids.values() if c.get("included"))
    for k,v in (("declared_candidate_count",len(cids)),("declared_included_count",inc),("declared_excluded_count",exc),("declared_attempt_count",att)):
        if k in Cd and Cd[k]!=v: fails.append(f"{k}={Cd[k]} but recomputed {v}")
    if "declared_exclusion_count" in Xd and Xd["declared_exclusion_count"]!=exc: fails.append(f"declared_exclusion_count={Xd['declared_exclusion_count']} but recomputed {exc}")
    for x in fails: print("FAIL:",x)
    print(f"declared: candidates={Cd.get('declared_candidate_count')} included={Cd.get('declared_included_count')} excluded={Cd.get('declared_excluded_count')} attempts={Cd.get('declared_attempt_count')} exclusions={Xd.get('declared_exclusion_count')}")
    print(f"recomputed: candidates={len(cids)} included={inc} excluded={exc} attempts={att} reconciled={'YES' if not fails and inc+exc==len(cids) else 'NO'}")
    print("C1_DENOMINATOR_PRINTED=" + ("PASS" if not fails and inc+exc==len(cids) else "FAIL")); return 0 if not fails and inc+exc==len(cids) else 1


if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)==3 and a[0]=="validate": sys.exit(cmd_validate(a[1],a[2]))
    if len(a)==3 and a[0]=="census": sys.exit(cmd_census(a[1],a[2]))
    print(__doc__); sys.exit(2)
