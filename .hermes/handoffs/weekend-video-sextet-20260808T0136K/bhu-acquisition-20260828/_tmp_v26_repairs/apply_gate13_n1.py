import io,sys
# V38 — codex V37 N1: origin_search.files and origin_search.matches are UNORDERED evidence inventories. One shared canonical-search
# function sorts their entries by canonical JSON (query preserved, nothing dropped or altered); merge applies it before canonical keys,
# graph digests, branch selection and serialisation, and C6 applies it to both reconstructed and sealed search evidence before branch
# matching and comparison.
CANON = '''def canon_search(s):
    """V38 (codex V37 N1): canonical form of an origin_search object — `files` and `matches` are UNORDERED evidence inventories, so their
    entries are sorted by canonical JSON; `query` is an ordered field and is preserved exactly. Nothing is dropped, added or altered."""
    if not isinstance(s,dict): return s
    out=dict(s)
    for f in ("files","matches"):
        if isinstance(out.get(f),list): out[f]=sorted(out[f],key=lambda e: json.dumps(e,sort_keys=True,separators=(",",":")))
    return out


'''
lane,seat=sys.argv[1],sys.argv[2]
s=io.open(lane,encoding="utf-8").read()
def rl(a,b):
    global s; assert s.count(a)==1,("lane",a[:70]); s=s.replace(a,b)
rl("def graph_integrity(graph, starts):", CANON+"def graph_integrity(graph, starts):")
rl('''        if _r.get("derived_from") is not None: _r["derived_from"]=sorted(_r["derived_from"])  # PROBE:MERGE_DEP_CANON
        if _r.get("derived_from_alt") is not None: _r["derived_from_alt"]=sorted(_r["derived_from_alt"])''',
'''        if _r.get("derived_from") is not None: _r["derived_from"]=sorted(_r["derived_from"])  # PROBE:MERGE_DEP_CANON
        if _r.get("derived_from_alt") is not None: _r["derived_from_alt"]=sorted(_r["derived_from_alt"])
        if _r.get("origin_search") is not None: _r["origin_search"]=canon_search(_r["origin_search"])  # PROBE:MERGE_SEARCH_CANON
        if _r.get("origin_search_alt") is not None: _r["origin_search_alt"]=canon_search(_r["origin_search_alt"])''')
io.open(lane,"w",encoding="utf-8").write(s)
t=io.open(seat,encoding="utf-8").read()
def rs(a,b):
    global t; assert t.count(a)==1,("seat",a[:70]); t=t.replace(a,b)
rs("def graph_integrity(graph, starts):", CANON+"def graph_integrity(graph, starts):")
rs('''        matches_primary=matches_primary and (sev.get("reason_code")!="ORIG_SILENT" or ar.get("origin_search")==sr.get("origin_search"))''',
   '''        matches_primary=matches_primary and (sev.get("reason_code")!="ORIG_SILENT" or canon_search(ar.get("origin_search"))==canon_search(sr.get("origin_search")))  # PROBE:C6_SEARCH_CANON_MATCH''')
rs('''            expected_search = sr.get("origin_search_alt") if (branch=="alt" and "origin_search_alt" in sr) else sr.get("origin_search")
            if ar.get("origin_search")!=expected_search: diffs.append("origin_search differs (structural comparison against the matched branch's search)")  # PROBE:C6_SEARCH_BRANCH''',
   '''            expected_search = sr.get("origin_search_alt") if (branch=="alt" and "origin_search_alt" in sr) else sr.get("origin_search")
            if canon_search(ar.get("origin_search"))!=canon_search(expected_search): diffs.append("origin_search differs (structural comparison against the matched branch's search)")  # PROBE:C6_SEARCH_BRANCH''')
io.open(seat,"w",encoding="utf-8").write(t); print("N1 canonical-search applied:",lane,seat)
