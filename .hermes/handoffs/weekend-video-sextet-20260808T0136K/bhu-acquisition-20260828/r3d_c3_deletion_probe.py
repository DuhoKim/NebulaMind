#!/usr/bin/env python3
"""C3 — deletion probe for R3-D. Executable, not a promise.

The control: DELETE the source-pinned field equations. If a unique positive floor STILL follows from
the injected relation alone, that relation is doing the work the source was supposed to do -- it is
circular -- and no derived-floor class may be filed.

Usage:  python3 r3d_c3_deletion_probe.py <relations.json>

Input JSON:
  {"target": "M",
   "relations": [{"id": "eq5",  "origin": "SOURCE_PINNED", "expr": "Eq(M, sqrt(hbar*c/G))"},
                 {"id": "injA", "origin": "INJECTED",      "expr": "Eq(M, 3*kg)"}],
   "symbols": ["M", "hbar", "c", "G", "kg"]}

Prints: retained ids, deleted ids, the injected relations, both solve results, and exactly one of
C3_DELETION_PROBE=PASS | FAIL | NOT_RUN.
  PASS  -- the floor does NOT follow from injected relations alone (source is doing the work)
  FAIL  -- a unique floor follows from injected alone (circular)
  NOT_RUN -- no injected relation, or the target does not resolve at all
Exit: 0 PASS, 1 FAIL, 2 NOT_RUN/usage.
"""
import json, sys, signal
import sympy as sp

CAP_SECONDS = 120  # matches the preregistration's stall guard


class Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise Timeout()


def solve_for(target, relations, symbols, constants):
    """Return (value_or_None, note). "determinate" means: a single solution whose free symbols are
    all §2b constants. A floor written in terms of G, c and hbar IS determinate; one still carrying a
    model parameter such as r0 is not. Getting this wrong was caught by the positive control below --
    the first version demanded ZERO free symbols and so scored a determinate Planck-scale floor as
    indeterminate, which would have made the probe unable to detect circularity at all."""
    if not relations:
        return None, "no relations"
    eqs = [sp.sympify(r["expr"], locals=symbols) for r in relations]
    try:
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(CAP_SECONDS)
        sols = sp.solve(eqs, symbols[target], dict=True)
        signal.alarm(0)
    except Timeout:
        return None, "SYMBOLIC_TIMEOUT"
    except Exception as e:
        signal.alarm(0)
        return None, f"unsolvable: {type(e).__name__}"
    vals = {sp.simplify(s[symbols[target]]) for s in sols if symbols[target] in s}
    if len(vals) != 1:
        return None, f"{len(vals)} solutions" if vals else "no solution for target"
    v = vals.pop()
    free = {str(x) for x in v.free_symbols} - {target}
    undetermined = sorted(free - set(constants))
    if undetermined:
        return v, f"indeterminate: free in {undetermined}"
    return v, "determinate"


def main():
    if len(sys.argv) != 2:
        print("usage: r3d_c3_deletion_probe.py <relations.json>")
        print("C3_DELETION_PROBE=NOT_RUN")
        return 2
    spec = json.load(open(sys.argv[1]))
    syms = {n: sp.Symbol(n, positive=True) for n in spec["symbols"]}
    constants = spec.get("constants", [])
    target = spec["target"]
    rel = spec["relations"]
    pinned = [r for r in rel if r["origin"] == "SOURCE_PINNED"]
    injected = [r for r in rel if r["origin"] == "INJECTED"]

    print(f"target            : {target}")
    print(f"retained (all)    : {[r['id'] for r in rel]}")
    print(f"DELETED (pinned)  : {[r['id'] for r in pinned]}")
    print(f"injected relations: {[(r['id'], r['expr']) for r in injected]}")

    print(f"§2b constants     : {constants}")
    full_v, full_note = solve_for(target, rel, syms, constants)
    print(f"with everything   : {full_v}   ({full_note})")

    if not injected:
        print("no injected relation to test")
        print("C3_DELETION_PROBE=NOT_RUN")
        return 2

    del_v, del_note = solve_for(target, injected, syms, constants)
    print(f"pinned DELETED    : {del_v}   ({del_note})")

    if del_v is not None and del_note == "determinate":
        print("VERDICT: a unique floor follows from the INJECTED relation alone -> CIRCULAR")
        print("C3_DELETION_PROBE=FAIL")
        return 1
    print("VERDICT: no unique floor without the source-pinned equations -> not circular")
    print("C3_DELETION_PROBE=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
