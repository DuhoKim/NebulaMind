#!/usr/bin/env python3
"""FAIL-FIRST KIT — the two rules that kept lapsing, made mechanical (Blanc 08:51 KST 2026-09-07; first ordered 05:09 for track 12, re-applied by hand in track 13,
reintroduced in track 14 — which is the proof that a per-track instruction is not enough).

RULE 1 — ONE OUTCOME ASSERTION PER METHOD. A method that bundles assertions stops at the first and silently proves less than it claims (track-14 v1's 1c never
reached its second assertion). Every test method must carry exactly ONE outcome assertion in its own body. Assertions inside helpers are not counted; a method may
declare fixture preconditions through `self.precondition(...)`, which is not an outcome assertion.

RULE 2 — A METHOD THAT DID NOT FAIL AGAINST THE PREDECESSOR IS NOT REPRODUCTION. Every method must label itself in the FIRST LINE of its docstring with either
`FAIL-FIRST:` (it must appear as a failure in the retained predecessor log) or `POSITIVE-REGRESSION:` (it must appear as a pass there — kept so a repair cannot lose
it). A FAIL-FIRST method that passed against the predecessor has no standing and the kit refuses it; a POSITIVE-REGRESSION that failed is equally refused.

Usage:  failfirst_kit.py <test_module.py> [--against <retained predecessor log>]
Exit 0 = conforms; 2 = refused (every reason printed); 3 = usage. Reads only; never edits the module or the log."""
import ast, re, sys, argparse
OUTCOME = re.compile(r"^assert(?!Warns|Logs)")          # self.assertX(...) — assertWarns/assertLogs are context managers, not outcome claims
def methods(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for f in node.body:
                if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)) and f.name.startswith("test_"): yield node.name, f
def outcome_assertions(fn):
    n = 0
    for node in ast.walk(fn):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == "self" and OUTCOME.match(node.func.attr): n += 1
    return n
def label(fn):
    doc = ast.get_docstring(fn) or ""
    first = doc.strip().split("\n")[0]
    if first.startswith("FAIL-FIRST:"): return "FAIL-FIRST"
    if first.startswith("POSITIVE-REGRESSION:"): return "POSITIVE-REGRESSION"
    return None
def log_status(text):
    st = {}
    for m in re.finditer(r"^(test_\S+) \(([^)]+)\)(?:\n[^\n]*)? \.\.\. (ok|FAIL|ERROR)", text, re.M): st[m.group(1)] = m.group(3)
    return st
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("module"); ap.add_argument("--against", help="retained log of this module run against the PREDECESSOR bytes")
    a = ap.parse_args(); bad = []
    try: src = open(a.module, encoding="utf-8").read(); tree = ast.parse(src)
    except OSError as e: print(f"FAIL-FIRST KIT: FAIL — cannot read module: {e}"); sys.exit(3)
    labels = {}
    for cls, fn in methods(tree):
        n = outcome_assertions(fn); lab = label(fn); labels[fn.name] = lab
        if n != 1: bad.append(f"{cls}.{fn.name}: {n} outcome assertions in the method body (exactly one required — RULE 1)")
        if lab is None: bad.append(f"{cls}.{fn.name}: its docstring's first line declares neither 'FAIL-FIRST:' nor 'POSITIVE-REGRESSION:' (RULE 2)")
    if a.against:
        try: st = log_status(open(a.against, encoding="utf-8", errors="replace").read())
        except OSError as e: print(f"FAIL-FIRST KIT: FAIL — cannot read the predecessor log: {e}"); sys.exit(3)
        if not st: bad.append(f"the predecessor log {a.against} contains no verbose per-method results (run with -v)")
        for name, lab in labels.items():
            got = st.get(name)
            if got is None: bad.append(f"{name}: absent from the predecessor log — no evidence of what it did against the predecessor bytes")
            elif lab == "FAIL-FIRST" and got == "ok": bad.append(f"{name}: labelled FAIL-FIRST but PASSED against the predecessor — it reproduces nothing and cannot be counted as reproduction (RULE 2)")
            elif lab == "POSITIVE-REGRESSION" and got != "ok": bad.append(f"{name}: labelled POSITIVE-REGRESSION but {got} against the predecessor — it is not an already-holding behaviour (RULE 2)")
    if bad: print("FAIL-FIRST KIT: REFUSED — " + "; ".join(bad)); sys.exit(2)
    n_ff = sum(1 for v in labels.values() if v == "FAIL-FIRST"); n_pr = len(labels) - n_ff
    print(f"FAIL-FIRST KIT: PASS — {len(labels)} test methods, each with exactly one outcome assertion in its body and an explicit label; {n_ff} FAIL-FIRST" + (f" (each observed FAILING in {a.against})" if a.against else " (no predecessor log checked)") + f"; {n_pr} POSITIVE-REGRESSION" + (" (each observed passing there)" if a.against else ""))
    sys.exit(0)
if __name__ == "__main__": main()
