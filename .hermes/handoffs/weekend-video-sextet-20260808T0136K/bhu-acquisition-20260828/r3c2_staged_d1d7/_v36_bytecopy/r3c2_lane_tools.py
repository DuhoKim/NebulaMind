#!/usr/bin/env python3
"""r3c2_lane_tools.py — the V27 lane-side tool, never given to a seat: merge two validated seat ledgers; compute root_origins and
per-claim rests_on from the merged ledger. Usage:
  /usr/bin/python3 r3c2_lane_tools.py merge   <ledger_seatA.json> <ledger_seatB.json> <merged.json>
  /usr/bin/python3 r3c2_lane_tools.py compute <merged.json> <out.json> <candidates.json>   (candidate file mandatory)
rests_on: DERIVED_STANDARD_OR_MEASURED_ONLY if every root origin is DERIVED, STANDARD or MEASURED; else the most severe root present,
USES_UNDECLARED > USES_IMPORTED > USES_FITTED > USES_CHOSEN; a disputed root gives a pair marked DISPUTED; a derived_from disagreement between seats is carried as derived_from_alt + PARENTS_DISPUTED and computed under both parent lists.
A ledger arriving with root_origins or rests_on set is REJECTED (exit 2)."""
import json, sys, pathlib

def load(p):
    d=json.loads(pathlib.Path(p).read_text())
    recs=d["records"] if isinstance(d,dict) else d
    assert isinstance(recs,list), "ledger records must be a list (an empty list is valid)"
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


# V27 label: DERIVED_STANDARD_OR_MEASURED_ONLY replaces the token DERIVED_ONLY (V10–V26) with identical membership (every root origin DERIVED, STANDARD or MEASURED); historical files keep the old token.
SEVERITY=["UNDECLARED","IMPORTED","FITTED","CHOSEN"]
def rests_on(rootset):
    if rootset<= {"DERIVED","STANDARD","MEASURED"}: return "DERIVED_STANDARD_OR_MEASURED_ONLY"
    for sev in SEVERITY:
        if sev in rootset: return "USES_"+sev
    return "DERIVED_STANDARD_OR_MEASURED_ONLY"


def disputed_reach(rec_by_id, rid, seen=None):
    """gate F4: True if any record reachable from rid (itself included), across claims, carries origin_alt or PARENTS_DISPUTED"""
    seen=seen or set()
    if rid in seen or rid not in rec_by_id: return False
    r=rec_by_id[rid]; seen=seen|{rid}
    if (r.get("origin_alt") and r["origin_alt"]!=r["origin"]) or r.get("PARENTS_DISPUTED"): return True
    return any(disputed_reach(rec_by_id,p,seen) for p in (r.get("derived_from") or [])) or any(disputed_reach(rec_by_id,p,seen) for p in (r.get("derived_from_alt") or []))

def cmd_compute(ledger,out,candidates=None):
    d,recs=load(ledger)
    for r in recs:
        if "root_origins" in r: print(f"REJECT: {r.get('input_id')} arrives with root_origins set"); return 2
        if "rests_on" in r: print(f"REJECT: {r.get('input_id')} arrives with rests_on set"); return 2
    by={r["input_id"]:r for r in recs}
    # V35: classification comes from the COMPLETE provenance graphs merge preserved — never from the per-input mixed PRIMARY/ALT view,
    # which is no graph any seat supplied. A ledger without provenance_graphs is accepted only if it is itself one complete graph
    # (no record carries an alternative branch); a ledger with alternatives but no graphs is refused.
    graphs=d.get("provenance_graphs")
    has_alt=any(r.get("origin_alt") or r.get("derived_from_alt") is not None or r.get("PARENTS_DISPUTED") for r in recs)
    if not graphs:
        if has_alt: print("FAIL: ledger carries alternative branches but no provenance_graphs (a mixed PRIMARY/ALT view is not a seat-supplied graph; compute accepts merge output)"); return 1  # PROBE:COMPUTE_NO_MIXED_GRAPH
        graphs=[recs]
    if len(graphs)>2: print("FAIL: more than two provenance graphs"); return 1
    gby=[{r["input_id"]:r for r in g} for g in graphs]
    for g in gby:
        if set(g)!=set(by): print("FAIL: a provenance graph does not cover the merged input_id set"); return 1
    claims=[{} for _ in gby]; disputed_claims=set()
    for r in recs:
        try: per=[roots(g,r["input_id"]) for g in gby]
        except ValueError as e: print("FAIL:",e); return 1
        r["root_origins"]=sorted(set().union(*per))
        for i,rs in enumerate(per): claims[i].setdefault(r["claim_id"],set()).update(rs)
        if disputed_reach(by, r["input_id"]): disputed_claims.add(r["claim_id"])  # PROBE:DISPUTE_PROPAGATES  (ONE resolver: every graph difference merge preserves is reachable as an alternative branch)
    out_claims={}
    for c in sorted(claims[0],key=str):   # V36 canon
        per=[cl[c] for cl in claims]
        if c in disputed_claims:
            pair=[rests_on(per[0]),rests_on(per[-1])]   # equal classifications are retained as a pair when the claim is disputed
            out_claims[c]={"root_origins":sorted(set().union(*per)),"root_origins_by_graph":[sorted(p) for p in per],"rests_on":pair,"DISPUTED":True}
        else:
            out_claims[c]={"root_origins":sorted(per[0]),"rests_on":rests_on(per[0])}
    if candidates:
        C=json.loads(pathlib.Path(candidates).read_text())["candidates"]; inc=[c["candidate_id"] for c in C if c.get("included")]
        for cid in inc:
            if cid not in out_claims: out_claims.update({cid:{"root_origins":[],"rests_on":"NOT_COMPUTED"}})  # PROBE:NOT_COMPUTED
        extra=[c for c in out_claims if c not in set(inc)]
        if extra: print("FAIL: ledger claims that are not included candidates:",extra); return 1
        if len(out_claims)!=len(inc): print(f"FAIL: rests_on rows {len(out_claims)} != included denominator {len(inc)}"); return 1
    result={"records":recs,"claims":out_claims}
    pathlib.Path(out).write_text(json.dumps(result,indent=1,sort_keys=True))   # V36 canon: JSON member order is one more meaningless ordering
    for c,v in sorted(out_claims.items(),key=lambda kv:str(kv[0])): print(f"{c}\trests_on={v['rests_on']}\troot_origins={v['root_origins']}"+("\tDISPUTED" if v.get("DISPUTED") else ""))
    return 0


def canon_key(r):
    """seat-blind canonical key of one seat's record: sha256 of its canonical JSON (sorted keys, no whitespace)"""
    import hashlib
    return hashlib.sha256(json.dumps(r,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def graph_key(g):
    import hashlib
    return hashlib.sha256(json.dumps(sorted(g,key=lambda r:r["input_id"]),sort_keys=True,separators=(",",":")).encode()).hexdigest()

def cmd_merge(a,b,out):
    """Merge two independently validated seat ledgers (same input_ids) into one: where origin differs, the merged record
    keeps the PRIMARY branch (the seat record with the smaller seat-blind canonical key — SEAT-PERMUTATION INVARIANCE) and carries the other seat's complete branch as origin_alt / origin_evidence_alt / origin_search_alt / derived_from_alt. Exit 0; exit 1 on id mismatch."""
    da,ra=load(a); db,rb=load(b); A={r["input_id"]:r for r in ra}; Bm={r["input_id"]:r for r in rb}
    if set(A)!=set(Bm):
        print("FAIL: input_id sets differ:", sorted(set(A)^set(Bm))); return 1
    out_recs=[]; ndis=0; npar=0; fails=[]
    # SPI enforcement: for every input the two seat records are ordered by their seat-blind canonical key; the smaller key is the PRIMARY branch.
    # Everything below reads P (primary) and Q (secondary) — never A/B — so the merged ledger is identical for merge(A,B) and merge(B,A).
    for k in sorted(A):
        P,Q=(A[k],Bm[k]) if canon_key(A[k])<=canon_key(Bm[k]) else (Bm[k],A[k])  # PROBE:SPI_CANONICAL
        for fld in ("status","value","source_file","source_line","symbol"):
            if str(P.get(fld))!=str(Q.get(fld)): fails.append(f"{k}: seats disagree on {fld} ({P.get(fld)!r} vs {Q.get(fld)!r}) — a value/status/coordinate disagreement is not silently resolved")  # PROBE:MERGE_FIELDS
        r=dict(P); r.pop("origin_alt",None); r.pop("origin_evidence_alt",None); r.pop("origin_search_alt",None); r.pop("derived_from_alt",None); r.pop("PARENTS_DISPUTED",None)
        ev_diff=(P.get("origin_evidence")!=Q.get("origin_evidence")); sil_q=(Q.get("origin_evidence") or {}).get("reason_code")=="ORIG_SILENT"
        search_diff=sil_q and (P.get("origin_search")!=Q.get("origin_search")); par_diff=(sorted(P.get("derived_from") or []) != sorted(Q.get("derived_from") or []))
        if Q["origin"]!=P["origin"]: ndis+=1
        if Q["origin"]!=P["origin"] or ev_diff or search_diff:
            # the secondary's COMPLETE branch is preserved whenever anything provenance-bearing differs — equal origin labels included
            r["origin_alt"]=Q["origin"]; r["origin_evidence_alt"]=Q["origin_evidence"]  # PROBE:MERGE_BRANCH
            if sil_q and "origin_search" in Q: r["origin_search_alt"]=Q["origin_search"]  # PROBE:MERGE_SEARCH_ALT
        if par_diff:
            r["derived_from_alt"]=Q.get("derived_from") or []; r["PARENTS_DISPUTED"]=True; npar+=1
        out_recs.append(r)
    for x in fails: print("FAIL:",x)
    print(f"PARENTS_DISPUTED={npar}"); print(f"FIELD_DISAGREEMENTS={len(fails)}")
    if fails: print("MERGE=FAIL"); return 1
    # V35: the two COMPLETE validated seat graphs are preserved as supplied (alt fields stripped), ordered by the sha256 of canonical JSON over
    # their records sorted by input_id (seat-blind); equal graphs are retained once. compute reads THESE graphs — never the per-input mixed view.
    graphs=[]
    for recs_ in (ra,rb):
        g=[{k:v for k,v in r.items() if k not in ("origin_alt","origin_evidence_alt","origin_search_alt","derived_from_alt","PARENTS_DISPUTED","root_origins","rests_on")} for r in sorted(recs_,key=lambda r:r["input_id"])]
        graphs.append(g)
    graphs.sort(key=graph_key)
    if len(graphs)==2 and graph_key(graphs[0])==graph_key(graphs[1]): graphs=graphs[:1]  # PROBE:MERGE_GRAPHS_EQUAL_ONCE
    pathlib.Path(out).write_text(json.dumps({"records":out_recs,"provenance_graphs":graphs},indent=1,sort_keys=True)); print(f"merged {len(out_recs)} records; origin disagreements={ndis}; provenance_graphs={len(graphs)}"); return 0  # PROBE:SPI_SORTED_BYTES (V34)


if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)==4 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2],a[3]))
    if len(a)==3 and a[0]=="compute": print("usage: compute <merged.json> <out.json> <candidates.json> — the candidate file is mandatory (every included claim gets a rests_on row)"); sys.exit(2)  # PROBE:COMPUTE_NEEDS_CANDIDATES
    if len(a)==4 and a[0]=="merge": sys.exit(cmd_merge(a[1],a[2],a[3]))
    print(__doc__); sys.exit(2)
