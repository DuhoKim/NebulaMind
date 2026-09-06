import io,sys
# V36 (codex V35 F1+F2): origin-independent graph integrity before root classification; deterministic (sorted) traversal everywhere in the audit.
seat=sys.argv[1]; t=io.open(seat,encoding="utf-8").read()
def rep(a,b):
    global t; assert t.count(a)==1,a[:80]; t=t.replace(a,b)
rep('''def roots(rec_by_id, rid, seen=None):
    seen=seen or set()''','''def graph_integrity(graph, starts):
    """V36: every derived_from edge reachable from `starts` is checked for a missing record and for a cycle, INDEPENDENTLY of origin
    (a cycle through a CHOSEN/FITTED/IMPORTED/MEASURED/STANDARD/UNDECLARED record is still a cycle). Traversal is sorted, so the
    reported problems are identical in every process. Returns a sorted list of problem strings; empty = intact."""
    problems=set(); done=set()
    def walk(n, path):
        if n in path: problems.add(f"cycle at {n}"); return
        if n in done: return
        if n not in graph: return
        for p in sorted(graph[n].get("derived_from") or []):
            if p not in graph: problems.add(f"missing dependency {p} of {n}"); continue
            walk(p, path+[n])
        done.add(n)
    for s in sorted(starts): walk(s, [])
    return sorted(problems)

def roots(rec_by_id, rid, seen=None):
    seen=seen or set()''')
rep('''    for d in r["derived_from"]:
        if d not in rec_by_id: raise ValueError(f"{rid}: derived_from {d} not in ledger")
        out|=roots(rec_by_id,d,seen)''','''    for d in sorted(r["derived_from"]):   # V36: sorted — deterministic diagnostics
        if d not in rec_by_id: raise ValueError(f"{rid}: derived_from {d} not in ledger")
        out|=roots(rec_by_id,d,seen)''')
rep('''        for p_ in graph[iid].get("derived_from") or []: closure_of(p_, graph, seen)''','''        for p_ in sorted(graph[iid].get("derived_from") or []): closure_of(p_, graph, seen)   # V36: sorted''')
rep('''        own=set(r.get("inputs") or {}); clos=set()
        for iid in own: clos|=closure_of(iid, a_graph)''','''        own=set(r.get("inputs") or {}); clos=set()
        for iid in sorted(own): clos|=closure_of(iid, a_graph)   # V36: sorted''')
rep('''        for iid in l_by.get(cid,{}):
            if iid not in own: inputs_res[iid]={"result":"MISMATCH","why":["not reconstructed by the auditor"]}; why.append(f"input {iid}: not reconstructed")
        try:
            ra=set(); [ra.update(roots(a_graph,i)) for i in own if i in a_graph]
            rs=set(); [rs.update(roots(sealed_view,i)) for i in l_by.get(cid,{})]''','''        for iid in sorted(l_by.get(cid,{})):
            if iid not in own: inputs_res[iid]={"result":"MISMATCH","why":["not reconstructed by the auditor"]}; why.append(f"input {iid}: not reconstructed")
        # V36 (codex V35 F1): GRAPH INTEGRITY — every derived_from edge of the auditor's closure and of the matched sealed closure is checked for
        # a missing record or a cycle, independently of origin, BEFORE root classification. Stopping at a non-DERIVED origin never substitutes for it.
        gi_a=graph_integrity(a_graph, [i for i in own if i in a_graph]); gi_s=graph_integrity(sealed_view, list(l_by.get(cid,{})))
        for g in gi_a: why.append(f"graph integrity (auditor closure): {g}")  # PROBE:C6_GRAPH_INTEGRITY
        for g in gi_s: why.append(f"graph integrity (matched sealed closure): {g}")
        inputs_res["_graph_integrity"]={"auditor":gi_a,"matched_sealed":gi_s}
        try:
            ra=set(); [ra.update(roots(a_graph,i)) for i in sorted(own) if i in a_graph]   # V36: sorted
            rs=set(); [rs.update(roots(sealed_view,i)) for i in sorted(l_by.get(cid,{}))]''')
rep('''            try: audited_rests["sealed_primary"]=sorted(set().union(*[roots(full_by,i) for i in l_by.get(cid,{})]) if l_by.get(cid) else set())''',
    '''            try: audited_rests["sealed_primary"]=sorted(set().union(*[roots(full_by,i) for i in sorted(l_by.get(cid,{}))]) if l_by.get(cid) else set())''')
io.open(seat,"w",encoding="utf-8").write(t); print("gate11 repair applied:",seat)
