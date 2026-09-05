#!/usr/bin/env python3
"""Shared control library for BHU round-3 preregs (Rule 4 of R3_PREREG_DESIGN_RULES_20260905.md):
every control is one printed command, its printed output, an exit status, and an exact token set.
A FAIL anywhere exits 1 (unlike the b-battery's exit-0 convention)."""
import json, re, subprocess, sys, unicodedata, pathlib
LIG = {"ﬀ":"ff","ﬁ":"fi","ﬂ":"fl","ﬃ":"ffi","ﬄ":"ffl","−":"-","–":"-","—":"-","’":"'","“":'"',"”":'"'}
def normalise(s: str) -> str:
    s = "".join(LIG.get(ch, ch) for ch in s)
    s = "".join(ch for ch in s if unicodedata.category(ch)[0] != "C" or ch in "\n\t")
    return re.sub(r"[ \t]+", " ", s)
CHECKS = []
def chk(name, ok, detail=""):
    if not isinstance(ok, bool): raise TypeError("chk needs a computed predicate")
    CHECKS.append((name, ok)); print(("PASS " if ok else "FAIL ") + name + (("  -- " + detail) if detail else ""))
def token(code, ok): print(f"{code}=" + ("PASS" if ok else "FAIL")); return ok
def finish():
    fails = [n for n, ok in CHECKS if not ok]
    print(f"\n{len(CHECKS)-len(fails)}/{len(CHECKS)} checks pass" + (f"  FAILING: {fails}" if fails else ""))
    sys.exit(1 if fails else 0)
def c1_identity(source, anchors, code):
    """anchors: list of (line_no, expected_substring_after_normalisation). Prints repr() of each line."""
    p = pathlib.Path(source); lines = p.read_text(encoding="utf-8", errors="replace").split("\n")
    allok = True
    for ln, exp in anchors:
        raw = lines[ln-1] if ln-1 < len(lines) else ""
        found = ln if normalise(exp) in normalise(raw) else next((i+1 for i, l in enumerate(lines) if normalise(exp) in normalise(l)), None)
        if found and found != ln: raw = lines[found-1]
        print(f"  L{ln} (found L{found}) repr: {raw!r}"[:300])
        ok = found is not None
        chk(f"C1 anchor L{ln}->L{found}: {exp[:50]!r}", ok, "" if found == ln else f"line drift {ln}->{found}; freeze pins the found line"); allok &= ok
    return token(code, allok)
def c4_harness(wrapper="r3c2_timeout.py", code="C4_HARNESS"):
    cmd = ["/usr/bin/python3", wrapper, "120", "--", "/usr/bin/python3", "-c", "import sympy; print(sympy.__version__)"]
    print("  $ " + " ".join(cmd)); r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout.strip()[:400]); ok = ("WRAPPER_EXIT=0" in r.stdout) or (r.returncode == 0 and re.search(r"\d+\.\d+", r.stdout) is not None)
    chk("C4 harness: sympy version printed live through the wrapper, exit 0", ok); return token(code, ok)
def deletion_probe(relations: dict, required: list, deleted: list, code_missing: str):
    """Exact-failure-set discipline: with `deleted` removed from `relations`, the probe must report exactly {code_missing}."""
    have = {k: v for k, v in relations.items() if k not in deleted}
    codes = set()
    for k in required:
        if k not in have: codes.add(code_missing)
    print(f"  probe deleted={deleted} -> codes={sorted(codes)}")
    ok = (codes == {code_missing}) if deleted else (codes == set())
    chk(f"C3 deletion probe: deleting {deleted or 'nothing'} yields exactly {sorted(codes)}", ok); return ok
