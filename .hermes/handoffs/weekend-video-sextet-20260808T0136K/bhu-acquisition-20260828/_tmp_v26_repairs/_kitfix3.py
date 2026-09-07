import io
T="r3c2_staged_d1d7/r3c2_staged_tests.py"; t=io.open(T,encoding="utf-8").read()
lines=t.split("\n")
# 1. the V37 SETUP_ERRORS definition survives LATER in the file and would shadow the new one — remove it (one definition only)
idx=[i for i,l in enumerate(lines) if l.startswith("SETUP_ERRORS=")]
assert len(idx)==2, idx
del lines[idx[1]]
# 2. a tool's own usage banner is deliberate output (now paired with INVOCATION=REJECTED), not a harness launch failure
lines[idx[0]]=lines[idx[0]].replace(',"usage: ")',')')
# 3. the old setup_ok/def that belonged to the V37 helper block is now duplicated too — keep the first only
d=[i for i,l in enumerate(lines) if l.startswith("def setup_ok(out):")]
if len(d)==2:
    j=d[1]; k=j
    while k<len(lines) and (k==j or lines[k].startswith("    ")): k+=1
    del lines[j:k]
t="\n".join(lines)
# 4. write the captured expectation table at the end of a capture run
a='n_ok=sum(1 for _,o in results if o); print(f"deletion_probes={NPROBES}")'
assert t.count(a)==1
t=t.replace(a,'''if CAPTURE:
    EXACT_PATH.write_text(json.dumps(_CAPTURED,indent=1,sort_keys=True)); print(f"CAPTURED {len(_CAPTURED)} pinned expectations -> {EXACT_PATH.name}")
'''+a)
io.open(T,"w",encoding="utf-8").write(t); print("kit: single SETUP_ERRORS, usage allowed, capture writer added")
