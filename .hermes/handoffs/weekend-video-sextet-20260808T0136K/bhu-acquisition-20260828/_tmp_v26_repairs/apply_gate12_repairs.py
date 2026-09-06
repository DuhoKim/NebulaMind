import io,sys
# V37 — codex V36 F1 (dependency-list order is a meaningless ordering: canonicalise it at merge before keys/dedup/branch selection/serialisation)
#     and codex V36 F2 (origin-independent graph integrity at the C3 boundaries: seat `validate` and lane `compute`, before output).
lane,seat=sys.argv[1],sys.argv[2]
s=io.open(lane,encoding="utf-8").read()
def rl(a,b):
    global s; assert s.count(a)==1,("lane",a[:70]); s=s.replace(a,b)
rl('''    da,ra=load(a); db,rb=load(b); A={r["input_id"]:r for r in ra}; Bm={r["input_id"]:r for r in rb}''',
'''    da,ra=load(a); db,rb=load(b)
    # V37 (codex V36 F1): dependency-list ORDER carries no meaning. Every derived_from list of both seat ledgers is normalised to sorted
    # input-id order HERE — before canonical record keys, graph digests, branch selection, graph deduplication and serialisation — so no
    # later step can observe it. This does not reorder a paper's computational operations: derived_from records dependency edges, not an
    # execution sequence.
    for _r in list(ra)+list(rb):
        if _r.get("derived_from") is not None: _r["derived_from"]=sorted(_r["derived_from"])  # PROBE:MERGE_DEP_CANON
        if _r.get("derived_from_alt") is not None: _r["derived_from_alt"]=sorted(_r["derived_from_alt"])
    A={r["input_id"]:r for r in ra}; Bm={r["input_id"]:r for r in rb}''')
rl('''def canon_key(r):''','''def graph_integrity(graph, starts):
    """V37 (codex V36 F2): every derived_from edge reachable from `starts` checked for a missing record and for a cycle, INDEPENDENTLY of
    origin — a cycle through CHOSEN/FITTED/IMPORTED/MEASURED/STANDARD/UNDECLARED is still a cycle. Sorted traversal, so the reported
    problems are identical in every process. Returns a sorted list of problems; empty = intact."""
    problems=set(); done=set()
    def walk(n, path):
        if n in path: problems.add(f"cycle at {n}"); return
        if n in done or n not in graph: return
        for p in sorted(graph[n].get("derived_from") or []):
            if p not in graph: problems.add(f"missing dependency {p} of {n}"); continue
            walk(p, path+[n])
        done.add(n)
    for st in sorted(starts): walk(st, [])
    return sorted(problems)


def canon_key(r):''')
rl('''    claims=[{} for _ in gby]; disputed_claims=set()''',
'''    # V37 (codex V36 F2): each COMPLETE provenance graph is checked for origin-independent integrity BEFORE any classification is written.
    for gi,g in enumerate(gby):
        probs=graph_integrity(g, list(g))
        if probs:
            for p_ in probs: print(f"FAIL: provenance graph {gi}: {p_}")  # PROBE:COMPUTE_GRAPH_INTEGRITY
            return 1
    claims=[{} for _ in gby]; disputed_claims=set()''')
io.open(lane,"w",encoding="utf-8").write(s)
t=io.open(seat,encoding="utf-8").read()
a='''    by={r["input_id"]:r for r in recs}
    for r in recs:
        for dfrom in r.get("derived_from") or []:
            if dfrom not in by: fails.append(f"{r['input_id']}: derived_from {dfrom} absent")'''
assert t.count(a)==1
t=t.replace(a,'''    by={r["input_id"]:r for r in recs}
    # V37 (codex V36 F2): the complete input graph is checked for cycles INDEPENDENTLY of origin, before root classification; a missing
    # dependency is reported by the per-record check below (itself origin-independent). Stopping root traversal at a non-DERIVED origin
    # never substitutes for either check.
    for g in graph_integrity(by, list(by)):
        if g.startswith("cycle"): fails.append(f"graph integrity: {g}")  # PROBE:VALIDATE_GRAPH_INTEGRITY
    for r in recs:
        for dfrom in r.get("derived_from") or []:
            if dfrom not in by: fails.append(f"{r['input_id']}: derived_from {dfrom} absent")''')
io.open(seat,"w",encoding="utf-8").write(t); print("gate12 repairs applied:",lane,seat)
