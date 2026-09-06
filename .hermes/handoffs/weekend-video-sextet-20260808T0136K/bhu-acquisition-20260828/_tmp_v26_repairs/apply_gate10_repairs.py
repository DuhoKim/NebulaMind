import io,sys,re
# V35 (codex V34 F1): merge preserves the two COMPLETE validated seat graphs (seat-blind order); compute takes each claim's pair
# from those graphs and never from the per-input mixed PRIMARY/ALT view; audit compare's unmatched-graph root computation is diagnostic only.
lane,seat=sys.argv[1],sys.argv[2]
s=io.open(lane,encoding="utf-8").read()
def rep(a,b):
    global s; assert s.count(a)==1,a[:80]; s=s.replace(a,b)
rep('    pathlib.Path(out).write_text(json.dumps({"records":out_recs},indent=1,sort_keys=True)); print(f"merged {len(out_recs)} records; origin disagreements={ndis}"); return 0  # PROBE:SPI_SORTED_BYTES (V34)',
'''    # V35: the two COMPLETE validated seat graphs are preserved as supplied (alt fields stripped), ordered by the sha256 of canonical JSON over
    # their records sorted by input_id (seat-blind); equal graphs are retained once. compute reads THESE graphs — never the per-input mixed view.
    graphs=[]
    for recs_ in (ra,rb):
        g=[{k:v for k,v in r.items() if k not in ("origin_alt","origin_evidence_alt","origin_search_alt","derived_from_alt","PARENTS_DISPUTED","root_origins","rests_on")} for r in sorted(recs_,key=lambda r:r["input_id"])]
        graphs.append(g)
    graphs.sort(key=graph_key)
    if len(graphs)==2 and graph_key(graphs[0])==graph_key(graphs[1]): graphs=graphs[:1]  # PROBE:MERGE_GRAPHS_EQUAL_ONCE
    pathlib.Path(out).write_text(json.dumps({"records":out_recs,"provenance_graphs":graphs},indent=1,sort_keys=True)); print(f"merged {len(out_recs)} records; origin disagreements={ndis}; provenance_graphs={len(graphs)}"); return 0  # PROBE:SPI_SORTED_BYTES (V34)''')
rep('def cmd_merge(a,b,out):','''def graph_key(g):
    import hashlib
    return hashlib.sha256(json.dumps(sorted(g,key=lambda r:r["input_id"]),sort_keys=True,separators=(",",":")).encode()).hexdigest()

def cmd_merge(a,b,out):''')
# compute: pair from the complete graphs
rep('''    by={r["input_id"]:r for r in recs}
    claims={}; claims_alt={}; disputed_claims=set()
    for r in recs:
        try: rs=roots(by,r["input_id"]); ra=roots_alt(by,r["input_id"])
        except ValueError as e: print("FAIL:",e); return 1
        r["root_origins"]=sorted(rs)
        claims.setdefault(r["claim_id"],set()).update(rs); claims_alt.setdefault(r["claim_id"],set()).update(ra)
        if disputed_reach(by, r["input_id"]): disputed_claims.add(r["claim_id"])  # PROBE:DISPUTE_PROPAGATES
    out_claims={}
    for c,rs in claims.items():
        if c in disputed_claims:
            out_claims[c]={"root_origins":sorted(rs),"rests_on":[rests_on(rs),rests_on(claims_alt[c])],"DISPUTED":True}
        else:
            out_claims[c]={"root_origins":sorted(rs),"rests_on":rests_on(rs)}''',
'''    by={r["input_id"]:r for r in recs}
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
        if disputed_reach(by, r["input_id"]) or any(per[0]!=p for p in per[1:]): disputed_claims.add(r["claim_id"])  # PROBE:DISPUTE_PROPAGATES
    out_claims={}
    for c in claims[0]:
        per=[cl[c] for cl in claims]
        if c in disputed_claims:
            pair=[rests_on(per[0]),rests_on(per[-1])]   # equal classifications are retained as a pair when the claim is disputed
            out_claims[c]={"root_origins":sorted(set().union(*per)),"root_origins_by_graph":[sorted(p) for p in per],"rests_on":pair,"DISPUTED":True}
        else:
            out_claims[c]={"root_origins":sorted(per[0]),"rests_on":rests_on(per[0])}''')
io.open(lane,"w",encoding="utf-8").write(s)
t=io.open(seat,encoding="utf-8").read()
a='''            audited_rests={"audit":sorted(ra),"sealed_under_matching_branch":sorted(rs),"sealed_primary":sorted(set().union(*[roots(full_by,i) for i in l_by.get(cid,{})]) if l_by.get(cid) else set()),"alt_branch_records":sorted(k for k in clos if branch_of.get(k)=="alt")}
            if ra!=rs: why.append(f"root_origins differ: audit {sorted(ra)} vs sealed {sorted(rs)}")'''
assert t.count(a)==1
t=t.replace(a,'''            audited_rests={"audit":sorted(ra),"sealed_under_matching_branch":sorted(rs),"alt_branch_records":sorted(k for k in clos if branch_of.get(k)=="alt")}
            if ra!=rs: why.append(f"root_origins differ: audit {sorted(ra)} vs sealed {sorted(rs)}")
            # V35: the unmatched PRIMARY view is a DIAGNOSTIC only — it is no graph a seat supplied; if its roots cannot be computed the report
            # records that fact and the verdict is unchanged (codex V34 F1). Only the MATCHED graph above decides.
            try: audited_rests["sealed_primary"]=sorted(set().union(*[roots(full_by,i) for i in l_by.get(cid,{})]) if l_by.get(cid) else set())
            except Exception as e: audited_rests["sealed_primary"]=None; audited_rests["sealed_primary_diagnostic_error"]=str(e)''')
io.open(seat,"w",encoding="utf-8").write(t); print("gate10 repair applied:",lane,seat)
