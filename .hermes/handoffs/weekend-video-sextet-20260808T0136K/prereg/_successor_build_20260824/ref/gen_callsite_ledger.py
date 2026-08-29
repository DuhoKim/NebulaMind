#!/usr/bin/env python3
"""PER-CALL-SITE LEDGER — raise sites × the paths that reach them, over FROZEN v9.

V50 §11 requires the classification to attach to **failure paths and call sites**, not to `raise`
statements, because a helper may raise on behalf of a caller and the same condition can reach
different callers under different admissibility contracts. `RAISE_SITE_CLASSIFICATION.md` classifies
one row per raise statement — its enumeration is sound and its **unit is wrong**. This is the unit fix.

**v9 is read, never written.** The call graph is built by AST over `successor_ref_v9.py` and the file
is untouched at `6a9abbbd…`.

What this establishes
---------------------
**61 of 112 raise sites are reachable by more than one path.** The per-raise ledger collapses all of
them into a single row, so for more than half the corpus the old unit cannot express the
classification the rule asks for. `canon_f8` is the worked example and is carried in full below.

Three limits, stated because an honestly incomplete ledger beats a complete-looking one
---------------------------------------------------------------------------------------
**1. The module's call graph cannot see production entry points that live outside it.** Within this
file, almost every path roots at `run_fixtures` — the fixture harness — because
`run_production_verdict` is *also* called from it. In a real run the production entry is an external
caller this graph cannot observe. **So "reachable only via `run_fixtures`" is an artifact of scope,
not a finding, and no site is marked fixture-only on that basis.**

**2. The graph is name-based.** It resolves `ast.Name` callees only; a call through an attribute, an
alias or a dispatch table is invisible. **Paths here are a lower bound on reachability.**

**3. Where a path's admissibility context cannot be settled without running the study, the row is
marked `UNJUDGED` and says why.** That is the same rule written for `UNREACHABLE-BY-CONSTRUCTION`:
evidence named per edge, and no bucket for edges nobody wants to trace.
"""

import ast
import hashlib
import sys
from pathlib import Path

REF = Path(__file__).resolve().parent / "successor_ref_v9.py"

# Per-path classifications that DIFFER from the site's default, with the evidence for each.
# Only sites where context genuinely changes the answer appear here; everything else inherits.
# Keyed on a DISTINGUISHING NODE in the path, not its root. Keying on the root failed on the first
# run for exactly the reason limit 1 describes: `run_production_verdict` is a production entry that
# is *also* called by `run_fixtures` inside this module, so it never appears as a root and the
# context lookup missed it. The lesson is the limit, demonstrated on my own worked example.
CONTEXT = {
    (168, "parent_digest"): (
        "INTEGRITY",
        "a non-finite reaching the digest of the PINNED parent catalogue is corrupted input, not a "
        "failed computation — the parent is a frozen artefact and §5 claims digest deviation"),
    (168, "run_production_verdict"): (
        "NUMERICAL",
        "the same guard on the verdict path fires on a quantity the run just computed, which is a "
        "run-time numerical failure and terminates under the class rule"),
}


def graph():
    src = REF.read_text()
    tree = ast.parse(src)
    funcs = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    owner = {}
    for name, fn in funcs.items():
        for ln in range(fn.lineno, (fn.end_lineno or fn.lineno) + 1):
            owner.setdefault(ln, name)
    rev = {}
    for name, fn in funcs.items():
        for c in ast.walk(fn):
            if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id in funcs:
                rev.setdefault(c.func.id, set()).add(name)
    raises = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Raise):
            e = n.exc
            et = (e.func.id if isinstance(e, ast.Call) and isinstance(e.func, ast.Name)
                  else (e.id if isinstance(e, ast.Name) else "bare"))
            raises.append((n.lineno, owner.get(n.lineno, "?"), et))
    return funcs, rev, sorted(raises)


def paths_to(rev, target, seen=None, depth=0):
    seen = seen or set()
    if target in seen or depth > 6:
        return [[target]]
    seen = seen | {target}
    out = []
    for c in sorted(rev.get(target, [])):
        for p in paths_to(rev, c, seen, depth + 1):
            out.append(p + [target])
    return out or [[target]]


def main():
    funcs, rev, raises = graph()
    rows, multi = [], 0
    for ln, fn, et in raises:
        ps = paths_to(rev, fn)
        if len(ps) > 1:
            multi += 1
        for p in ps:
            entry = p[0]
            cls, why = (None, "")
            for (k_ln, k_node), v in CONTEXT.items():
                if k_ln == ln and k_node in p:
                    cls, why = v
                    break
            rows.append((ln, fn, et, entry, " → ".join(p), cls, why))

    out = ["# PER-CALL-SITE LEDGER — raise sites × reaching paths\n",
           f"**Subject:** `ref/successor_ref_v9.py`, sha256 "
           f"`{hashlib.sha256(REF.read_bytes()).hexdigest()}` — **read only, never written.**\n",
           f"**{len(raises)} raise sites; {multi} reachable by more than one path; "
           f"{len(rows)} (site, path) rows.** The per-raise ledger collapses those {multi} into one "
           "row each, which is why V50 §11 requires this unit.\n",
           "**Limits:** production entry points outside this module are invisible to an in-module "
           "call graph, so a path rooting at `run_fixtures` is not evidence of fixture-only "
           "reachability; the graph is name-based, so paths are a **lower bound**; and any row whose "
           "context cannot be settled without running the study is marked `UNJUDGED`.\n",
           "## The worked example — one raise, two contexts, two classifications\n"]
    for ln, fn, et, entry, path, cls, why in rows:
        if ln == 168 and cls:
            node = "parent_digest" if "parent_digest" in path else "run_production_verdict"
            out.append(f"- **L168 `{fn}` reached via `{node}` → {cls}** — {why}")
            out.append(f"  - path: `{path}`")
    out.append("\n**This is what the per-raise unit cannot express**: a single row for L168 must "
               "choose one of these, and either choice is wrong for the other path.\n")
    out.append("## Sites reachable by more than one path\n")
    out.append("| line | function | exception | paths | classification |")
    out.append("|---|---|---|---|---|")
    seen = set()
    for ln, fn, et, entry, path, cls, why in rows:
        if ln in seen:
            continue
        n = sum(1 for r in rows if r[0] == ln)
        if n > 1:
            seen.add(ln)
            mark = "**context-dependent, resolved**" if any(
                r[0] == ln and r[5] for r in rows) else "UNJUDGED — inherits the per-site class; "\
                "context not settled without running the study"
            out.append(f"| {ln} | `{fn}` | `{et}` | {n} | {mark} |")
    Path(REF.parent / "RAISE_CALLSITE_LEDGER.md").write_text("\n".join(out) + "\n")
    print(f"raise sites {len(raises)}  multi-path {multi}  (site,path) rows {len(rows)}")
    print(f"context-resolved rows: {sum(1 for r in rows if r[5])}")
    print(f"UNJUDGED multi-path sites: {multi - len({r[0] for r in rows if r[5]})}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
