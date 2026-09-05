#!/usr/bin/env python3
"""r3c2_lane_tools.py — LANE-SIDE tool, never given to a seat: merge two validated seat ledgers; compute root_origins and
per-claim rests_on from the merged ledger. Usage:
  /usr/bin/python3 r3c2_lane_tools.py merge   <ledger_seatA.json> <ledger_seatB.json> <merged.json>
  /usr/bin/python3 r3c2_lane_tools.py compute <merged.json> <out.json>
rests_on: DERIVED_ONLY if every root origin is DERIVED, STANDARD or MEASURED; else the most severe root present,
USES_UNDECLARED > USES_IMPORTED > USES_FITTED > USES_CHOSEN; a disputed root gives a pair marked DISPUTED; a derived_from disagreement between seats is carried as derived_from_alt + PARENTS_DISPUTED and computed under both parent lists.
A ledger arriving with root_origins or rests_on set is REJECTED (exit 2)."""
import json, sys, pathlib

def load(p):
    d=json.loads(pathlib.Path(p).read_text())
    recs=d["records"] if isinstance(d,dict) else d
    assert isinstance(recs,list) and recs, "ledger has no records"
    return d,recs


def roots_alt(rec_by_id, rid):
    """root set when every disputed record takes its origin_alt instead of origin"""
    alt={k:dict(v) for k,v in rec_by_id.items()}
    for v in alt.values():
        if v.get("origin_alt"): v["origin"]=v["origin_alt"]
        if v.get("derived_from_alt") is not None: v["derived_from"]=v["derived_from_alt"]
    return roots(alt, rid)


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


SEVERITY=["UNDECLARED","IMPORTED","FITTED","CHOSEN"]
def rests_on(rootset):
    if rootset<= {"DERIVED","STANDARD","MEASURED"}: return "DERIVED_ONLY"
    for sev in SEVERITY:
        if sev in rootset: return "USES_"+sev
    return "DERIVED_ONLY"


def cmd_compute(ledger,out):
    d,recs=load(ledger)
    for r in recs:
        if "root_origins" in r: print(f"REJECT: {r.get('input_id')} arrives with root_origins set"); return 2
        if "rests_on" in r: print(f"REJECT: {r.get('input_id')} arrives with rests_on set"); return 2
    by={r["input_id"]:r for r in recs}
    claims={}; claims_alt={}; disputed_claims=set()
    for r in recs:
        try: rs=roots(by,r["input_id"]); ra=roots_alt(by,r["input_id"])
        except ValueError as e: print("FAIL:",e); return 1
        r["root_origins"]=sorted(rs)
        claims.setdefault(r["claim_id"],set()).update(rs); claims_alt.setdefault(r["claim_id"],set()).update(ra)
        if (r.get("origin_alt") and r["origin_alt"]!=r["origin"]) or r.get("PARENTS_DISPUTED"): disputed_claims.add(r["claim_id"])
    out_claims={}
    for c,rs in claims.items():
        if c in disputed_claims:
            out_claims[c]={"root_origins":sorted(rs),"rests_on":[rests_on(rs),rests_on(claims_alt[c])],"DISPUTED":True}
        else:
            out_claims[c]={"root_origins":sorted(rs),"rests_on":rests_on(rs)}
    result={"records":recs,"claims":out_claims}
    pathlib.Path(out).write_text(json.dumps(result,indent=1))
    for c,v in out_claims.items(): print(f"{c}\trests_on={v['rests_on']}\troot_origins={v['root_origins']}"+("\tDISPUTED" if v.get("DISPUTED") else ""))
    return 0


def cmd_merge(a,b,out):
    """Merge two independently validated seat ledgers (same input_ids) into one: where origin differs, the merged record
    keeps seat A's origin/evidence and carries origin_alt + origin_evidence_alt from seat B. Exit 0; exit 1 on id mismatch."""
    da,ra=load(a); db,rb=load(b); A={r["input_id"]:r for r in ra}; Bm={r["input_id"]:r for r in rb}
    if set(A)!=set(Bm):
        print("FAIL: input_id sets differ:", sorted(set(A)^set(Bm))); return 1
    out_recs=[]; ndis=0; npar=0
    for k in sorted(A):
        r=dict(A[k]); r.pop("origin_alt",None); r.pop("origin_evidence_alt",None); r.pop("derived_from_alt",None); r.pop("PARENTS_DISPUTED",None)
        if Bm[k]["origin"]!=A[k]["origin"]:
            r["origin_alt"]=Bm[k]["origin"]; r["origin_evidence_alt"]=Bm[k]["origin_evidence"]; ndis+=1
        if sorted(A[k].get("derived_from") or []) != sorted(Bm[k].get("derived_from") or []):
            r["derived_from_alt"]=Bm[k].get("derived_from") or []; r["PARENTS_DISPUTED"]=True; npar+=1
        out_recs.append(r)
    print(f"PARENTS_DISPUTED={npar}")
    pathlib.Path(out).write_text(json.dumps({"records":out_recs},indent=1)); print(f"merged {len(out_recs)} records; origin disagreements={ndis}"); return 0


if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)==3 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2]))
    if len(a)==4 and a[0]=="merge": sys.exit(cmd_merge(a[1],a[2],a[3]))
    print(__doc__); sys.exit(2)
