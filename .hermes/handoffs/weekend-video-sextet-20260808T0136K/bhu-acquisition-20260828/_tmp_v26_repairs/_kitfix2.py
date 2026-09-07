import io
T="r3c2_staged_d1d7/r3c2_staged_tests.py"; t=io.open(T,encoding="utf-8").read()
def rep(a,b):
    global t; assert t.count(a)==1,a[:90]; t=t.replace(a,b)
rep('    def neut(l): return l.replace("fails.append(","_probe_noop(")','    def neut(l): return l.replace("print(","_probe_noop(").replace("fails.append(","_probe_noop(")')
OLD = '''    F0=[norm_row(l) for l in out0.splitlines() if l.startswith("FAIL:")]; F1=[norm_row(l) for l in out.splitlines() if l.startswith("FAIL:")]
    gone=[l for l in F0 if l not in F1]; added=[l for l in F1 if l not in F0]
    why=(setup_ok(out0) and f"baseline run: {setup_ok(out0)}") or setup_ok(out) \\
        or ("" if token in out else f"expected token {token!r} absent after deletion") \\
        or ("" if rc==want_rc else f"exit {rc} != expected {want_rc}") \\
        or ("" if TOKEN_LINE.search(out) else "no completion token line after deletion") \\
        or ("" if gone else "NO diagnostic vanished — deleting the marked check changed nothing (a relocated marker cannot satisfy a probe)") \\
        or (f"the probed run INVENTED diagnostics that the unprobed run did not emit: {added}" if added else "")'''
NEW = '''    def diag(o): return [norm_row(l) for l in o.splitlines() if l.strip() and not TOKEN_LINE.match(norm_row(l))]
    D0,D1=diag(out0),diag(out)
    gone=[l for l in D0 if l not in D1]
    key="probe:"+name
    if CAPTURE: _CAPTURED[key]=gone
    why=(setup_ok(out0) and f"baseline run: {setup_ok(out0)}") or setup_ok(out) \\
        or ("" if token in out else f"expected token {token!r} absent after deletion") \\
        or ("" if rc==want_rc else f"exit {rc} != expected {want_rc}") \\
        or ("" if TOKEN_LINE.search(out) else "no completion token line after deletion") \\
        or ("" if gone else "NO diagnostic vanished — deleting the marked check changed nothing (a relocated marker cannot satisfy a probe)")
    if not why and not CAPTURE:
        pinned=EXACT_ROWS.get(key)
        if pinned is None: why=f"no pinned vanished-diagnostic text for {key!r} — a probe must declare exactly what its deletion removes"
        else:
            still=[l for l in pinned if l in D1]; missing=[l for l in pinned if l not in D0]
            if still: why=f"the targeted diagnostic is STILL PRESENT after deletion: {still}"
            elif missing: why=f"the pinned targeted diagnostic never appeared in the unprobed run: {missing}"'''
rep(OLD,NEW)
t=t.replace('"full":    dict(rc=0,token="SPI=PASS",rows=20,','"full":    dict(rc=0,token="SPI=PASS",rows=26,').replace('MOI property (delivered tools): 20 constructions','MOI property (delivered tools): 26 constructions')
io.open(T,"w",encoding="utf-8").write(t); print("kit fixes applied")
