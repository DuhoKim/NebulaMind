import io,sys
# V36 (Blanc 07:09): STRUCTURAL canonicalisation — every unordered container or externally-ordered mapping that can reach a verdict or an
# output line is traversed in sorted order at the point it is consumed, and every JSON write sorts keys. No downstream step can observe
# set/dict/file order. Seat tool + lane tool.
seat,lane=sys.argv[1],sys.argv[2]
t=io.open(seat,encoding="utf-8").read()
def rep(a,b,n=1):
    global t; assert t.count(a)==n,(a[:70],t.count(a)); t=t.replace(a,b)
rep('    for cid,c in cids.items():\n        if c.get("included") and cid in xids:','    for cid,c in sorted(cids.items(),key=lambda kv:str(kv[0])):   # V36 canon\n        if c.get("included") and cid in xids:')
rep('    for cid,x in xrows.items():\n        c=cids.get(cid)','    for cid,x in sorted(xrows.items(),key=lambda kv:str(kv[0])):   # V36 canon\n        c=cids.get(cid)')
rep('    for cid,r in RD.items():\n        if not isinstance(r,dict) or "outcome" not in r:','    for cid,r in sorted(RD.items(),key=lambda kv:str(kv[0])):   # V36 canon: the auditor\'s file member order carries no meaning\n        if not isinstance(r,dict) or "outcome" not in r:')
rep('        for iid,ar in (r.get("inputs") or {}).items():\n            if not isinstance(ar,dict): out.append(','        for iid,ar in sorted((r.get("inputs") or {}).items(),key=lambda kv:str(kv[0])):   # V36 canon\n            if not isinstance(ar,dict): out.append(')
rep('    for cid0,r0 in RD.items():\n        for iid0,ar0 in (r0.get("inputs") or {}).items():','    for cid0,r0 in sorted(RD.items(),key=lambda kv:str(kv[0])):   # V36 canon\n        for iid0,ar0 in sorted((r0.get("inputs") or {}).items(),key=lambda kv:str(kv[0])):',2)
rep('        for iid in (RD.get(cid,{}).get("inputs") or {}): sel_closure|=closure_of(iid, a_graph)','        for iid in sorted(RD.get(cid,{}).get("inputs") or {}): sel_closure|=closure_of(iid, a_graph)   # V36 canon')
io.open(seat,"w",encoding="utf-8").write(t)
s=io.open(lane,encoding="utf-8").read()
def rl(a,b):
    global s; assert s.count(a)==1,a[:70]; s=s.replace(a,b)
rl('    pathlib.Path(out).write_text(json.dumps(result,indent=1))\n    for c,v in out_claims.items(): print(','    pathlib.Path(out).write_text(json.dumps(result,indent=1,sort_keys=True))   # V36 canon: JSON member order is one more meaningless ordering\n    for c,v in sorted(out_claims.items(),key=lambda kv:str(kv[0])): print(')
rl('    for c in claims[0]:\n        per=[cl[c] for cl in claims]','    for c in sorted(claims[0],key=str):   # V36 canon\n        per=[cl[c] for cl in claims]')
io.open(lane,"w",encoding="utf-8").write(s); print("canonicalisation applied:",seat,lane)
