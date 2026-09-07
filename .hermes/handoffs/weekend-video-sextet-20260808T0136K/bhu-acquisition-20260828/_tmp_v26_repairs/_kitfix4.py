import io
T="r3c2_staged_d1d7/r3c2_staged_tests.py"; t=io.open(T,encoding="utf-8").read()
def rep(a,b):
    global t; assert t.count(a)==1,a[:100]; t=t.replace(a,b)
# (1) a marked line that is an ASSIGNMENT guard must also be deletable: the whole marked statement becomes a no-op, preserving structure
rep('    def neut(l): return l.replace("print(","_probe_noop(").replace("fails.append(","_probe_noop(")',
'''    def neut(l):
        s2=l.strip()
        if s2.startswith(("elif ","else:","except ","finally:")) or "=" not in s2.split("#")[0] or any(k in l for k in ("fails.append(","print(","diffs.append(","why.append(","out.append(")):
            return l.replace("print(","_probe_noop(").replace("fails.append(","_probe_noop(")''')
rep('''.replace("out.append(","_probe_noop(").replace("out_cl''','''.replace("out.append(","_probe_noop(").replace("out_cl''')
# (2) probes whose effect is in an ARTEFACT rather than stdout declare the text that must vanish from it
rep('def probe(name, tool, marker, *args, token, want_rc=0):','def probe(name, tool, marker, *args, token, want_rc=0, artefact=None, gone_text=None):')
rep('''    rc0,out0=run(tool,*args); rc,out=run(t,*args)   # baseline vs probed: the probe must REMOVE a diagnostic, not merely change a polarity''',
'''    rc0,out0=run(tool,*args); base_art=(pathlib.Path(artefact).read_text() if artefact and pathlib.Path(artefact).exists() else None)
    rc,out=run(t,*args); probed_art=(pathlib.Path(artefact).read_text() if artefact and pathlib.Path(artefact).exists() else None)   # baseline vs probed: the probe must REMOVE the check's effect, not merely change a polarity''')
rep('''        or ("" if gone else "NO diagnostic vanished — deleting the marked check changed nothing (a relocated marker cannot satisfy a probe)")''',
'''        or ("" if (gone or gone_text) else "NO diagnostic vanished — deleting the marked check changed nothing (a relocated marker cannot satisfy a probe)") \\
        or ("" if gone_text is None else ("" if (base_art is not None and gone_text in base_art) else f"the declared artefact evidence {gone_text!r} was absent from the UNPROBED artefact")) \\
        or ("" if gone_text is None else ("" if (probed_art is not None and gone_text not in probed_art) else f"the declared artefact evidence {gone_text!r} SURVIVED the deletion"))''')
rep('''    if not why and not CAPTURE:
        pinned=EXACT_ROWS.get(key)''','''    if gone_text is not None: pass   # an artefact-effect probe pins its vanished evidence in the call itself
    if not why and not CAPTURE and gone_text is None:
        pinned=EXACT_ROWS.get(key)''')
# (3) the one probe whose deletion shows only in the merged artefact declares it
rep('probe("gate-7 F1 probe: deleting the preservation drops the alternative\'s search",LANE,"PROBE:MERGE_SEARCH_ALT","merge",mA,mB,W/"silAB_p.json",token="merged 1 records")',
    'probe("gate-7 F1 probe: deleting the preservation drops the alternative\'s search",LANE,"PROBE:MERGE_SEARCH_ALT","merge",mA,mB,W/"silAB_p.json",token="merged 1 records",artefact=W/"silAB_p.json",gone_text="origin_search_alt")')
io.open(T,"w",encoding="utf-8").write(t); print("kit: assignment guards deletable; artefact-effect probe declares its vanished evidence")
