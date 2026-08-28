#!/usr/bin/env python3
"""A11 -- audit my OWN check battery for the name/predicate gap.

Blanc, after two seats found the same defect in two consecutive gates:

    "That is the describe-vs-compute law operating inside your own harness: the name describes,
     the predicate computes, and the gap between them is where a false PASS lives. Audit the rest
     of your check battery for it before you gate another entry."

Six consecutive gates have found this. Once it was an outright tautology
(a6 check 4: `w_implied = -1.0 - (0.0)/(3*H*rho)`, then asserting it equals -1).

METHOD. Parse every a*.py with `ast`, find each chk(name, predicate, detail) call, and classify
the PREDICATE EXPRESSION by what it can actually vary on:

  TAUTOLOGY   the predicate contains no name bound to source data; it cannot fail
  LITERAL     compares only hard-coded numbers to each other
  STRING      only membership/regex-presence tests over a source text
  MIXED       string presence AND some computation
  COMPUTED    arithmetic or parsed values drive the outcome

WHAT THIS TOOL DOES NOT DO, stated plainly because the whole point is not to overclaim: it
cannot read the NAME's meaning. It classifies predicate FORM only. A STRING predicate is not
automatically wrong -- "this sentence appears in the paper" is honestly testable by a string
search. The gap appears when the NAME asserts a semantic property (a causal direction, a
derivation, an absence of alternatives) that a presence test cannot reach. That judgement stays
human. This tool narrows where to look.
"""
import ast, glob, os, re, sys

DATA_HINTS = ("T", "A", "G", "D", "R", "NT", "N", "doc", "body", "txt")   # names bound to sources

# --- FIXES APPLIED TO THIS TOOL, and it is the same defect it audits for -----------------
# v1 classified only the predicate EXPRESSION. A predicate like `mdot and relax and drift is
# None` therefore looked variable-free and was reported TAUTOLOGY -- even though those booleans
# were computed from the source text three lines above. v1 reported 22 tautologies; almost all
# were its own artefact. The tool's NAME ("TAUTOLOGY") claimed more than its PREDICATE tested.
# Fix 1: resolve assignments transitively before classifying.
# Fix 2 (v3): also follow AugAssign (`ok_all &= ...`) and FunctionDef bodies. v2 still reported
# three tautologies, two of which were flags built with `&=` in a loop -- artefacts again. Two
# rounds of the tool's own name outrunning its own predicate, on the exact defect it exists to
# find. Recorded rather than quietly patched, because it is the best evidence that this failure
# mode is easy and not a lapse of attention.

def binding_map(tree, src):
    """name -> set of identifiers/calls appearing in its RHS, for transitive data-flow."""
    m = {}
    for n in ast.walk(tree):
        if isinstance(n, (ast.Assign, ast.AugAssign)):
            rhs = set()
            for x in ast.walk(n.value):
                if isinstance(x, ast.Name): rhs.add(x.id)
                if isinstance(x, ast.Call):
                    f = x.func
                    rhs.add("()" + (f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")))
            targets = n.targets if isinstance(n, ast.Assign) else [n.target]
            for t in targets:
                for x in ast.walk(t):
                    if isinstance(x, ast.Name): m.setdefault(x.id, set()).update(rhs)
        # a function whose body touches source data makes its CALLERS data-driven
        if isinstance(n, ast.FunctionDef):
            rhs = set()
            for x in ast.walk(n):
                if isinstance(x, ast.Name): rhs.add(x.id)
                if isinstance(x, ast.Call):
                    f = x.func
                    rhs.add("()" + (f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")))
            m.setdefault(n.name, set()).update(rhs)
            m.setdefault("()" + n.name, set()).update(rhs)
    return m

def expand(names, bmap, depth=6):
    seen, frontier = set(names), set(names)
    for _ in range(depth):
        nxt = set()
        for nm in frontier:
            nxt |= bmap.get(nm, set())
        nxt -= seen
        if not nxt: break
        seen |= nxt; frontier = nxt
    return seen

def classify(node, src, bmap=None):
    """Classify a predicate by what can make it vary, following variable bindings."""
    seg = ast.get_source_segment(src, node) or ""
    names, calls, has_num_cmp, has_arith = set(), set(), False, False
    for n in ast.walk(node):
        if isinstance(n, ast.Name): names.add(n.id)
        if isinstance(n, ast.Call):
            f = n.func
            calls.add(f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", ""))
        if isinstance(n, ast.Compare):
            if any(isinstance(c, ast.Constant) and isinstance(c.value, (int, float)) for c in n.comparators):
                has_num_cmp = True
        if isinstance(n, ast.BinOp): has_arith = True
    # follow bindings: a bare name may carry a data-driven computation from earlier
    reach = expand(names, bmap or {})
    reach_calls = {r[2:] for r in reach if r.startswith("()")}
    calls |= reach_calls
    names |= {r for r in reach if not r.startswith("()")}
    string_test = ("In" in seg or " in " in seg) or bool(calls & {"search", "findall", "match", "startswith"})
    # a predicate is a tautology if nothing in it is bound to source data or to a parsed value
    data_driven = bool(names & set(DATA_HINTS)) or bool(calls & {"search", "findall", "match", "len", "abs", "max", "min", "all", "any"})
    if not data_driven and (has_num_cmp or has_arith): return "LITERAL", seg
    if not data_driven: return "TAUTOLOGY", seg
    if string_test and (has_arith or has_num_cmp): return "MIXED", seg
    if string_test: return "STRING", seg
    return "COMPUTED", seg

rows = []
for path in sorted(glob.glob("a*.py")):
    if path.startswith("a11"): continue
    src = open(path).read()
    try: tree = ast.parse(src)
    except SyntaxError: continue
    bmap = binding_map(tree, src)
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "chk" and len(n.args) >= 2:
            name = n.args[0]
            nm = ast.literal_eval(name) if isinstance(name, ast.Constant) else \
                 (" ".join(ast.literal_eval(x) for x in name.values if isinstance(x, ast.Constant))
                  if isinstance(name, ast.JoinedStr) else "<dynamic>")
            if isinstance(name, ast.BinOp):  # implicit concat of two string literals
                try: nm = ast.literal_eval(name)
                except Exception: nm = "<concat>"
            kind, seg = classify(n.args[1], src, bmap)
            rows.append((path, kind, (nm or "")[:78], " ".join(seg.split())[:96]))

order = {"TAUTOLOGY": 0, "LITERAL": 1, "STRING": 2, "MIXED": 3, "COMPUTED": 4}
rows.sort(key=lambda r: (order.get(r[1], 9), r[0]))
print("=" * 118); print("A11 -- name/predicate gap across my own check battery"); print("=" * 118)
print(f"{'file':<26} {'form':<10} check name")
print("-" * 118)
for p, k, nm, seg in rows:
    print(f"{p:<26} {k:<10} {nm}")
    if k in ("TAUTOLOGY", "LITERAL", "STRING"):
        print(f"{'':<26} {'':<10}   predicate: {seg}")
from collections import Counter
c = Counter(k for _, k, _, _ in rows)
print("-" * 118)
print(f"total checks: {len(rows)}   " + "  ".join(f"{k}={c[k]}" for k in order if c[k]))
weak = c["TAUTOLOGY"] + c["LITERAL"] + c["STRING"]
print(f"\nPREDICATES THAT CANNOT REACH A SEMANTIC CLAIM: {weak}/{len(rows)} ({100*weak/max(len(rows),1):.0f}%)")
print("""
READ THIS BEFORE ACTING ON IT

A STRING result is NOT automatically a defect. "the paper states X" is honestly testable by
searching for X. The defect is a NAME that asserts something a presence test cannot reach --
a causal direction, a derivation, the ABSENCE of an alternative reading. Those need a human.

The three forms above are ranked by how little they can vary:
  TAUTOLOGY -- cannot fail at all. Delete or rewrite; this is the a6-check-4 defect.
  LITERAL   -- compares constants. Passes regardless of the paper.
  STRING    -- can fail, but only if the text changes. Fine for "X appears"; wrong for "X implies".
""")
sys.exit(0)

# ============================================================================================
# HAND-ADJUDICATED RESULT -- the part the tool cannot do, done by reading each name.
#
# The tool classifies predicate FORM. Whether a NAME outruns its predicate is a semantic
# judgement. After three rounds of fixing the tool itself, the honest tally is:
#
#   1 TAUTOLOGY   -- an artefact: `ok_all` is set inside an if-branch, which the dataflow does
#                    not model. Not a real defect.
#   1 LITERAL     -- a2 "the literal reading puts the mode comfortably inside the instrument
#                    band", predicate `63.0 > 20.0*1.5`. The CLAIM is about two numbers, so
#                    name and predicate actually agree. Not a defect either.
#
# So the tautology problem is essentially gone -- the one real instance (a6 check 4) was fixed
# when the gate caught it. The live problem is different and Blanc named it exactly:
#
# REAL NAME/PREDICATE GAPS -- name asserts semantics, predicate tests presence:
#
#   a10  "the causal scale is set by the MEASURED Omega_Lambda and the angle follows"
#        -> predicate confirms two equations APPEAR. Asserts a causal direction it cannot see.
#   a6   "r_S is a fixed asymptote, not an evolving quantity, so Lambda is constant"
#        -> four presence tests. Asserts a physical conclusion.
#   a9   "observation constrains the model parameter, not the reverse"
#        -> presence tests. Asserts a direction of inference.
#   a8   "entry 25 states NO statistical rejection rule"
#        -> ABSENCE of a regex match. Weakest form of all: a pattern that misses is
#           indistinguishable from a thing that is not there. Same defect codex found in
#           a2's rate regex ("its assertion is stronger than that regex alone proves").
#   a10  "the +/-3 is an OBSERVATIONAL read-off feeding the reverse inference"
#        -> presence test, though here the quoted strings really are decisive.
#
# FIVE, not thirty-two. And the pattern across them is one thing: I write a NAME that states the
# CONCLUSION I drew from reading, and a PREDICATE that tests the EVIDENCE I read it from. Those
# are different claims, and the gap between them is where a false PASS lives.
#
# RULE ADOPTED, and it is cheap to follow:
#   - a presence test may only be named "X appears in the source".
#   - any name asserting a direction, a derivation, an implication or an ABSENCE must either
#     compute the thing, or say in the name that it rests on quoted text.
#   - absence claims get an explicit caveat naming what the pattern would miss.
