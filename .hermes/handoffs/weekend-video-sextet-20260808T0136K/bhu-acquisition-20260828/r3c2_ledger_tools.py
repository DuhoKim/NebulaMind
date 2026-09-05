#!/usr/bin/env python3
"""r3c2_ledger_tools.py — the C3 script the R3-C2 preregistration relies on, delivered.

  /usr/bin/python3 r3c2_ledger_tools.py compute  <ledger.json> <out.json>
      reads the input ledger (one record per input), computes for every record `root_origins` (origins at the
      leaves of its derived_from chain) and for every claim_id `rests_on`, writes <out.json> with both fields
      filled, and prints them. A seat never writes either field: any record that arrives with `root_origins`
      or any claim record with `rests_on` already set is REJECTED (exit 2).
  /usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> <sources_dir>
      asserts: every record has the schema fields; status in {PRINTED,STANDARD,ABSENT}; origin in
      {DERIVED,STANDARD,CHOSEN,FITTED,IMPORTED,UNDECLARED}; reason_code/origin pair is one of the allowed pairs;
      no ABSENT record carries a value; every PRINTED record's verbatim quotation is a substring of the cited
      source line; every STANDARD value is on the closed list; derived_from ids exist and the graph is acyclic.
      Exit 0 = PASS, 1 = FAIL (every failure printed), 2 = usage/schema error.

rests_on severity order is fixed by §3 of the preregistration:
  DERIVED_ONLY  if every root origin is DERIVED or STANDARD;
  else the most severe root origin present: USES_UNDECLARED > USES_IMPORTED > USES_FITTED > USES_CHOSEN.
"""
import json, sys, pathlib

STATUS={"PRINTED","STANDARD","ABSENT"}
ORIGIN={"DERIVED","STANDARD","CHOSEN","FITTED","IMPORTED","UNDECLARED"}
PAIRS={"ORIG_EQUATION":"DERIVED","ORIG_CONSTANT":"STANDARD","ORIG_CHOICE_STATED":"CHOSEN","ORIG_FIT_STATED":"FITTED","ORIG_CITATION":"IMPORTED","ORIG_SILENT":"UNDECLARED"}
SEVERITY=["UNDECLARED","IMPORTED","FITTED","CHOSEN"]   # most severe first
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
    if r["origin"]!="DERIVED" or not r.get("derived_from"): return {r["origin"]}
    out=set()
    for d in r["derived_from"]:
        if d not in rec_by_id: raise ValueError(f"{rid}: derived_from {d} not in ledger")
        out|=roots(rec_by_id,d,seen)
    return out

def rests_on(rootset):
    if rootset<= {"DERIVED","STANDARD"}: return "DERIVED_ONLY"
    for sev in SEVERITY:
        if sev in rootset: return "USES_"+sev
    return "DERIVED_ONLY"

def cmd_compute(ledger,out):
    d,recs=load(ledger)
    for r in recs:
        if "root_origins" in r: print(f"REJECT: {r.get('input_id')} arrives with root_origins set"); return 2
        if "rests_on" in r: print(f"REJECT: {r.get('input_id')} arrives with rests_on set"); return 2
    by={r["input_id"]:r for r in recs}
    claims={}
    for r in recs:
        try: rs=roots(by,r["input_id"])
        except ValueError as e: print("FAIL:",e); return 1
        r["root_origins"]=sorted(rs)
        claims.setdefault(r["claim_id"],set()).update(rs)
    result={"records":recs,"claims":{c:{"root_origins":sorted(rs),"rests_on":rests_on(rs)} for c,rs in claims.items()}}
    pathlib.Path(out).write_text(json.dumps(result,indent=1))
    for c,v in result["claims"].items(): print(f"{c}\trests_on={v['rests_on']}\troot_origins={v['root_origins']}")
    return 0

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
        if PAIRS.get(rc)!=r["origin"]: fails.append(f"{r['input_id']}: reason_code {rc} does not map to origin {r['origin']}")
        if r["status"]=="ABSENT" and r.get("value") not in (None,""): fails.append(f"{r['input_id']}: ABSENT record carries a value")
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

if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)==3 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2]))
    if len(a)==3 and a[0]=="validate": sys.exit(cmd_validate(a[1],a[2]))
    print(__doc__); sys.exit(2)
