import ast, hashlib
from pathlib import Path
b = Path(".hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824")
V = b/"ref/successor_ref_v9.py"
src = V.read_text(); tree = ast.parse(src)
owner = {}
for fn in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
    for ln in range(fn.lineno, (fn.end_lineno or fn.lineno)+1): owner.setdefault(ln, fn.name)

UNREACH_BOTH = set()   # WITHDRAWN V54 - no site meets the evidence bar
UNREACH_MEAS = set()   # WITHDRAWN V54 - the harness froze the budget argument
NUM = {1123,1134,1153, 1369,1397,1401,1403,1411,1435,1437,1439,1442,
       1503,1513,1517,1537,1548,1554}
# 1462/1468 moved NUMERICAL -> CALLER at V89 (GPT56-V88 F8): each tests a supplied argument's
# admissibility before the function computes anything - the as-supplied boundary as written,
# the same move 1464 made earlier. V89 edited the OUTPUT and not this generator (CODEX-V89 F4
# executed the generator and caught the drift); the resolution now lives HERE, where it
# regenerates instead of reviving.
RESOLVED = {1462,1468}
PLAN = {963,973}          # caller/setup: infeasible against a SUPPLIED l_plan
PLAN_INTERNAL = {986, 1331, 1341}   # 986: MOVE_CAP (below). 1331/1341: _plan raises the TYPED
                          # OUTCOME exception InconclusiveByPower AT PLANNING (CODEX-V68 F3) -
                          # before a run exists, so no run outcome is produced; the typed
                          # exception is the operator-stop MECHANISM, and the outcome CLASS is
                          # produced only by the run-time guards. The AST inventory still counts
                          # these nodes by exception TYPE, so '2 InconclusiveByPower' stays true
                          # as a type count.     # MOVE_CAP: an internal cap against a frozen constant, fired AFTER a
                          # feasible prefix exists. NOT a caller error - calling it one violated
                          # the supplied-argument boundary (GPT56-V64 F4, CODEX-V64 F6). NOT an
                          # outcome class either: no terminal consequence, because a failure
                          # before a run exists cannot terminate a run. The draft said
                          # PLANNING-INTERNAL and this generator still said CALLER - the text
                          # moved and the ledger did not, which is the drift I keep repairing.   # MOVED to CALLER by principal ruling 2026-08-29: a planning failure fires
                       # before a run exists, so it cannot be a run outcome of any kind - nothing has
                       # started, so nothing can be voided or declared inconclusive. The sites are
                       # MOVED and not deleted: they are setup errors against a caller-supplied
                       # l_plan and still need a disposition. NUMERICAL-PLANNING is gone as a class.
WRAP = {168,1620,776}                             # propagation, not a distinct condition
CALLER = {215,217,262,938,1464,1209,1020,1018,1022,1027,1032,1038,1040,1050,1053,1077,1099,1102,1108,1206,1460,1603,1675}
INTEG = {64,856,858,860,862,864,867,872,876,885,887,889,891,1601,1605,1641,1643,1687}
# 1677/1681 moved INTEGRITY -> CALLER at V92 (GPT56-V91 F8): both test the SUPPLIED
# (photoz_available, resolution_date) pair's admissibility at the pre-run choice point -
# no VOID antecedent owns them and nothing has run that could be voided; the boundary as
# written. Encoded here, where it regenerates (the raise-ledger lesson, applied again).
# 1649 (require_complete_sample) moved INTEGRITY -> CALLER (CODEX-V75 F6): the guard compares two
# CALLER-SUPPLIED integers and verifies no parent-to-receipt partition - section 5's own recorded
# limit says so, and the ledger contradicted the draft's recorded limit for four revisions.
CALLER = CALLER | {1649} | RESOLVED | {1677, 1681}

rows=[]
for n in ast.walk(tree):
    # GPT56-V94 F9: the corpus holds ONE production assert (1622) the Raise-only walk
    # missed - AssertionError is a failure path like any raise, so ast.Assert joins the
    # enumeration with its own exception type label.
    if isinstance(n, ast.Assert):
        msg = n.msg.value if isinstance(n.msg, ast.Constant) else ""
        rows.append((n.lineno, owner.get(n.lineno, "?"), "AssertionError",
                     "INTEGRITY", "assert", str(msg)[:70]))
        continue
    if not isinstance(n, ast.Raise): continue
    e=n.exc
    et = e.func.id if isinstance(e,ast.Call) and isinstance(e.func,ast.Name) else (e.id if isinstance(e,ast.Name) else "bare")
    a = e.args[0] if isinstance(e,ast.Call) and e.args else None
    msg = str(a.value) if isinstance(a,ast.Constant) else (
        "".join(v.value if isinstance(v,ast.Constant) else "{}" for v in a.values) if isinstance(a,ast.JoinedStr) else "")
    ln=n.lineno
    if ln in PLAN_INTERNAL: cls="PLANNING-INTERNAL"
    elif et in ("InconclusiveByPower","InconclusiveByCalibration"): cls="TYPED-OUTCOME"
    elif et=="ManifestClosureError": cls="INTEGRITY"
    elif ln in UNREACH_BOTH: cls="UNREACHABLE-BY-CONSTRUCTION"
    elif ln in UNREACH_MEAS: cls="UNREACHABLE-MEASURED-ONLY"
    elif ln in NUM: cls="NUMERICAL"
    elif ln in WRAP: cls="WRAPPER"
    elif ln in CALLER or ln in PLAN: cls="CALLER"
    elif ln in INTEG: cls="INTEGRITY"
    else: cls="UNASSIGNED"
    note = "moved" if (ln in PLAN or ln in PLAN_INTERNAL) else ("resolved" if ln in RESOLVED else "")
    rows.append((ln, owner.get(ln,"?"), et, cls, note, msg[:70]))
rows.sort()
from collections import Counter
c=Counter(r[3] for r in rows)
unassigned=[r for r in rows if r[3]=="UNASSIGNED"]

out=[]
out.append("# RAISE-SITE CLASSIFICATION — every `raise` in the frozen reference, classified per site\n")
out.append(f"**Subject:** `ref/successor_ref_v9.py`, sha256 `{hashlib.sha256(V.read_bytes()).hexdigest()}` (FROZEN).\n")
out.append("**Generated 2026-08-29 by AST enumeration; the CLASS column is a human reading, not a "
           "pattern match.** V50 §11 requires the classification be recorded per site — this is that "
           "record. It exists so a seat can check the reading line by line instead of accepting a "
           "count. **The counts below are a consequence of the table, not an input to it.**\n")
out.append("**Boundary applied** (V50 §5): a raise is a CALLER error if it tests a property of an "
           "argument as supplied; a run outcome if it tests a value computed from admissible data. "
           "INTEGRITY covers failures already claimed by a VOID antecedent. WRAPPER re-raises another "
           "site's failure.\n")
out.append("**Planning failures are not run outcomes** (principal ruling, 2026-08-29). Of the "
           "`local_pass` sites that fire during plan construction, **L963 and L973 are CALLER** (setup errors "
           "against a supplied l_plan) and **L986 is PLANNING-INTERNAL**, all marked *moved* below — this "
           "header said all three were CALLER for two revisions after L986 moved (CODEX-V69 F7), the header/table "
           "drift one paragraph above the table it drifted from. They were briefly given their own class while this corpus was being "
           "classified; a failure that fires before a run exists cannot be a run outcome, because "
           "nothing has started that could be voided or declared inconclusive. They are moved rather "
           "than deleted: L963 and L973 are setup errors against a caller-supplied `l_plan`; L986 is NOT - "
           "it fails against an internal frozen constant (CODEX-V72 F8 caught this paragraph still "
           "saying 'each' three clauses after L986 stopped being one) - and all three still need a "
           "disposition. **L986 is PLANNING-INTERNAL** - a disposition, not an outcome class, carrying no "
           "terminal consequence - because MOVE_CAP is an internal cap against a frozen constant "
           "that fires after a feasible prefix exists, so it is not an error in any supplied "
           "argument. `RAISE_CALLSITE_LEDGER.md` finds no path to them through "
           "`run_production_verdict`; that ledger's graph is name-based and a lower bound, so this is "
           "*no run-time path found*, not *no run-time path exists*.\n")
for k,v in sorted(c.items()): out.append(f"- **{k}** — {v}")
out.append(f"\n**Total {len(rows)} failure sites — 112 `raise` nodes and 1 production `assert` (v9:1622, INTEGRITY: a post-statistic calibration-path change is state corruption on the verdict path; enumerated since GPT56-V94 F9).** The two sites once marked *soft* (L1462, "
           "L1468) were resolved to CALLER at V89 under the boundary as written — each tests a "
           "supplied argument's admissibility before the function computes anything (GPT56-V88 "
           "F8), the 20 → 18 drop the *soft* marking itself predicted, and the same move L1464 "
           "made earlier on the identical argument. Sites marked *moved* were reclassified by "
           "ruling, not by reading; *resolved* marks the two boundary applications — encoded in "
           "this generator at V90 after V89 edited only the output (CODEX-V89 F4: a checked-in "
           "artifact that can drift from its generator will).\n")
out.append("**ADDENDUM — known IMPLICIT exception paths, hand-enumerated as found "
           "(GPT56-V95 F5, CODEX-V95 F7; append-only; CORRECTED AT V97 from the actual "
           "bytes after GPT56-V96 F4 showed two of three rows misread — the lesson this "
           "corpus keeps teaching, applied to its own ledger):** "
           "L1493–1496 `adjudicate_path` — dict subscripts `cal[...]` and numpy reductions: "
           "implicit KeyError/TypeError, UNCAUGHT on the verdict path → process death, no "
           "verdict record (the operator-observed platform family; loud, never a silent "
           "verdict); L1609 `run_production_verdict` — the `adjudicate_path(cal)` call, the "
           "propagation site of the same, same disposition; L1647–1648 "
           "`require_complete_sample` — `int()` casts of supplied counts: implicit "
           "ValueError/TypeError, CALLER by the as-supplied boundary (its explicit raise at "
           "1649 is already a row).**\n")
out.append("| line | function | exception | class | | message |")
out.append("|---|---|---|---|---|---|")
ANNOT = {
    1462: " (tests supplied `n_counts` before the function computes anything; resolved "
          "CALLER under the as-supplied boundary — GPT56-V88 F8)",
    1677: " (tests the supplied choice-point pair pre-run; no VOID antecedent owns it — "
          "moved CALLER, GPT56-V91 F8)",
    1681: " (tests the supplied choice-point pair pre-run; no VOID antecedent owns it — "
          "moved CALLER, GPT56-V91 F8)",
    1468: " (tests supplied `epsilon_hat` before the function computes anything; resolved "
          "CALLER under the as-supplied boundary — GPT56-V88 F8)",
}
for ln,f,et,cls,soft,msg in rows:
    safe = msg.replace("|", "/") + ANNOT.get(ln, "")
    out.append(f"| {ln} | `{f}` | `{et}` | **{cls}** | {soft} | {safe} |")
import sys
content = "\n".join(out)+"\n"
target = b/"ref/RAISE_SITE_CLASSIFICATION.md"
if "--check" in sys.argv:
    ok = target.read_text() == content
    print("raise ledger --check:", "byte-equal to generator output" if ok else "DRIFTED from generator")
    raise SystemExit(0 if ok else 1)
target.write_text(content)
print("classes:", dict(c))
print("UNASSIGNED:", [(r[0],r[1],r[5][:40]) for r in unassigned])
