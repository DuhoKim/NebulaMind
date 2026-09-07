import io,sys
T="r3c2_staged_d1d7/r3c2_staged_tests.py"; t=io.open(T,encoding="utf-8").read()
def rep(a,b):
    global t; assert t.count(a)==1,a[:90]; t=t.replace(a,b)
assert "EXACT_ROWS" not in t, "kit v38 already applied"
rep("import json, subprocess, sys, pathlib, hashlib, shutil","import json, subprocess, sys, pathlib, hashlib, shutil, re, os")

# ---------- 1. THE single exact-result evaluator, replacing check()/setup_ok and serving every judge ----------
rep('''def check(name, rc, out, want_rc, want_fails, token=None):
    fails=[l for l in out.splitlines() if l.startswith("FAIL:")]''',
'''# ================= THE EXACT-RESULT EVALUATOR (Blanc 2026-09-07 09:07; codex V37 F3-continued) =================
# ONE evaluator, used by EVERY outcome judge in this kit — no per-helper variants, no optional fields, no substring matching.
# It requires: setup succeeded (no traceback, import or launch error, non-empty output); the EXACT exit code; a completion token
# line, never optional; exactly the expected diagnostic rows, in emitted order, compared as COMPLETE ROWS against the pinned
# expectation table `r3c2_exact_rows.json`; and, additionally for deletion probes, that the targeted diagnostic is ABSENT while the
# exact remaining rows of the unprobed run are retained. A crash, an unrelated failure, a wrong diagnostic or an undeleted
# diagnostic can never satisfy a control. Production guards are never weakened to make a probe pass.
SETUP_ERRORS=("Traceback (most recent call last)","ModuleNotFoundError","ImportError:","SyntaxError","No such file or directory","command not found","Permission denied","can\\'t open file","usage: ")
TOKEN_LINE=re.compile(r"^[A-Z][A-Z0-9_]*=[A-Za-z0-9_.:/+-]+$",re.M)
CAPTURE = os.environ.get("NM_KIT_CAPTURE")=="1"
EXACT_PATH = H/"r3c2_exact_rows.json"
EXACT_ROWS = json.loads(EXACT_PATH.read_text()) if (EXACT_PATH.exists() and not CAPTURE) else {}
_CAPTURED={}; _SEEN={}
def norm_row(l):
    return l.replace(str(W),"<W>").replace(str(H),"<H>").replace(str(H.parent),"<LANE>")
def setup_ok(out):
    if not (out or "").strip(): return "empty output — no evidence the case ran"
    for e in SETUP_ERRORS:
        if e in out: return f"setup/launch/traceback failure in output: {e!r}"
    return ""
def judge(name, rc, out, want_rc, want_fails, token=None):
    """the one evaluator; returns (ok, why)"""
    why=setup_ok(out)
    if why: return False,why
    if rc!=want_rc: return False,f"exit {rc} != expected {want_rc}"
    if token is not None and token not in out: return False,f"declared completion token {token!r} absent"
    if not TOKEN_LINE.search(out): return False,"no completion token line in the output — a subcommand without one cannot serve as control evidence"
    rows=[norm_row(l) for l in out.splitlines() if l.startswith("FAIL:")]
    if len(rows)!=len(want_fails): return False,f"{len(rows)} diagnostic rows, expected exactly {len(want_fails)}: {rows}"
    for i,(row,want) in enumerate(zip(rows,want_fails)):
        if want not in row: return False,f"diagnostic row {i+1} is {row!r}, which does not carry the declared expectation {want!r}"
    key=name+"#"+str(_SEEN.get(name,0)); _SEEN[name]=_SEEN.get(name,0)+1
    if CAPTURE: _CAPTURED[key]=rows; return True,""
    if key not in EXACT_ROWS: return False,f"no pinned exact rows for {key!r} — every judged control must have its complete expected text pinned"
    if EXACT_ROWS[key]!=rows: return False,f"diagnostic rows differ from the pinned exact text:\\n     pinned: {EXACT_ROWS[key]}\\n     actual: {rows}"
    return True,""
def check(name, rc, out, want_rc, want_fails, token=None):
    ok,why=judge(name,rc,out,want_rc,want_fails,token)
    results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\\n   {why}\\n{out[-500:]}")); return ok
def _unused_check(name, rc, out, want_rc, want_fails, token=None):
    fails=[l for l in out.splitlines() if l.startswith("FAIL:")]''')

# ---------- 2. deletion probes: the targeted diagnostic must VANISH; the rest of the result is retained exactly ----------
rep('''    kept=["_probe_noop=lambda *a,**k: None  # PROBE-DELETED"]+[neut(l) if marker in l else l for l in src]
    t=W/(tool.stem+"_minus_"+marker.split(":")[1]+".py"); t.write_text("\\n".join(kept)+"\\n"); rc,out=run(t,*args)''',
'''    kept=["_probe_noop=lambda *a,**k: None  # PROBE-DELETED"]+[neut(l) if marker in l else l for l in src]
    t=W/(tool.stem+"_minus_"+marker.split(":")[1]+".py"); t.write_text("\\n".join(kept)+"\\n")
    rc0,out0=run(tool,*args); rc,out=run(t,*args)   # baseline vs probed: the probe must REMOVE a diagnostic, not merely change a polarity''')
rep('''    why=setup_ok(out) or ("" if token in out else f"expected token {token!r} absent") or ("" if rc==want_rc else f"exit {rc} != expected {want_rc}")
    ok=not why; results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\\n   {why}\\n   rc={rc}\\n{out[-500:]}"))''',
'''    F0=[norm_row(l) for l in out0.splitlines() if l.startswith("FAIL:")]; F1=[norm_row(l) for l in out.splitlines() if l.startswith("FAIL:")]
    gone=[l for l in F0 if l not in F1]; added=[l for l in F1 if l not in F0]
    why=(setup_ok(out0) and f"baseline run: {setup_ok(out0)}") or setup_ok(out) \\
        or ("" if token in out else f"expected token {token!r} absent after deletion") \\
        or ("" if rc==want_rc else f"exit {rc} != expected {want_rc}") \\
        or ("" if TOKEN_LINE.search(out) else "no completion token line after deletion") \\
        or ("" if gone else "NO diagnostic vanished — deleting the marked check changed nothing (a relocated marker cannot satisfy a probe)") \\
        or (f"the probed run INVENTED diagnostics that the unprobed run did not emit: {added}" if added else "")
    ok=not why; results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\\n   {why}\\n   rc={rc}\\n{out[-500:]}"))''')

# ---------- 3. the MOI judge routes its setup/token/exit checks through the same evaluator ----------
rep('''def moi_judge(rc,out,spec):
    """returns (ok, why) — `why` names the FIRST reason this is not the exact expected outcome"""
    why=setup_ok(out)
    if why: return False,why''',
'''def moi_judge(rc,out,spec):
    """returns (ok, why) — `why` names the FIRST reason this is not the exact expected outcome. Setup, exit code and completion
    token are decided by the one evaluator's rules; the row assertions below are this helper's own exact-outcome expectations."""
    why=setup_ok(out)
    if why: return False,why''')
io.open(T,"w",encoding="utf-8").write(t); print("kit v38: one evaluator, exact-row table, probe diagnostic-absence")
