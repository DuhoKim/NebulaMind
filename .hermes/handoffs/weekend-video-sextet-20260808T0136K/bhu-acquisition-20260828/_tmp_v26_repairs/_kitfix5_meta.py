import io
T="r3c2_staged_d1d7/r3c2_staged_tests.py"; t=io.open(T,encoding="utf-8").read()
def rep(a,b):
    global t; assert t.count(a)==1,a[:100]; t=t.replace(a,b)
# probe machinery becomes callable in judge-only mode so meta-controls can exercise it
rep('def probe(name, tool, marker, *args, token, want_rc=0, artefact=None, gone_text=None):','def probe(name, tool, marker, *args, token, want_rc=0, artefact=None, gone_text=None, judge_only=False):')
rep('''    ok=not why; results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\\n   {why}\\n   rc={rc}\\n{out[-500:]}"))''',
'''    ok=not why
    if judge_only: return ok,why
    results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\\n   {why}\\n   rc={rc}\\n{out[-500:]}"))''')
rep('    global NPROBES; NPROBES+=1','    global NPROBES\n    if not judge_only: NPROBES+=1')
# ---- meta-controls on EVERY judge (codex V37 F3-continued; Blanc 09:07): a crash, an unrelated failure, a wrong diagnostic and an
#      undeleted diagnostic must each be REJECTED. These assert the judges themselves, and are counted as controls.
anchor='n_ok=sum(1 for _,o in results if o); print(f"deletion_probes={NPROBES}")'
assert t.count(anchor)==1
meta='''# ================= META-CONTROLS ON THE JUDGES THEMSELVES =================
def meta(label, cond, detail=""):
    results.append((label,bool(cond))); print(("ok  " if cond else "BAD ")+label+("" if cond else f"\\n   {detail}"))
_crash="FAIL: provenance graph 0: cycle at p.txt#x\\nTraceback (most recent call last):\\n  File \\"x\\", line 1\\nRuntimeError: injected infrastructure failure\\n"
_ok,_why=judge("(meta crash)",1,_crash,1,["cycle at p.txt#x"])
meta("meta-control on the exact-result evaluator: a REAL TRACEBACK is rejected even though its exit code and diagnostic row match (this is the case the retired general check credited)",(not _ok) and "traceback failure" in _why,_why)
_ok,_why=judge("(meta notoken)",1,"FAIL: provenance graph 0: cycle at p.txt#x\\n",1,["cycle at p.txt#x"])
meta("meta-control: output with no completion token line is rejected — a subcommand that never announces completion cannot serve as control evidence",(not _ok) and "completion token" in _why,_why)
_ok,_why=judge("(meta wrongdiag)",1,"FAIL: something else entirely\\nSEAT_VALIDATE=FAIL\\n",1,["cycle at p.txt#x"])
meta("meta-control: a control whose subcommand fails for a DIFFERENT stated reason is rejected",(not _ok) and "does not carry the declared expectation" in _why,_why)
_ok,_why=judge("(meta extrarows)",1,"FAIL: a\\nFAIL: b\\nSEAT_VALIDATE=FAIL\\n",1,["a"])
meta("meta-control: an unexpected EXTRA diagnostic row is rejected (the failure set is exact, not a lower bound)",(not _ok) and "expected exactly" in _why,_why)
_inert=W/"inert_tool.py"; _inert.write_text((SEAT.read_text()+"\\n# PROBE:INERT_MARKER — a marker on a line that disables nothing\\n"))
_ok,_why=probe("(meta inert)",_inert,"PROBE:INERT_MARKER","validate",_gled,_gsrc,_gcand,token="C3_NO_SUBSTITUTION=FAIL",want_rc=1,judge_only=True)
meta("meta-control on deletion probes: a marker RELOCATED to a line that disables nothing is rejected — no diagnostic vanished",(not _ok) and "NO diagnostic vanished" in _why,_why)
'''
t=t.replace(anchor,meta+anchor)
io.open(T,"w",encoding="utf-8").write(t); print("meta-controls added for every judge")
