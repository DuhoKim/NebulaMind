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
       1462,1468, 1503,1513,1517,1537,1548,1554}
SOFT = {1462,1468}                      # domain-vs-computed, named as uncertain
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
INTEG = {64,856,858,860,862,864,867,872,876,885,887,889,891,1601,1605,1641,1643,1649,1677,1681,1687}

rows=[]
for n in ast.walk(tree):
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
    note = "moved" if (ln in PLAN or ln in PLAN_INTERNAL) else ("soft" if ln in SOFT else "")
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
out.append("**Planning failures are not run outcomes** (principal ruling, 2026-08-29). The three "
           "`local_pass` sites that fire during plan construction — L963, L973, L986 — are **CALLER**, "
           "marked *moved* below. They were briefly given their own class while this corpus was being "
           "classified; a failure that fires before a run exists cannot be a run outcome, because "
           "nothing has started that could be voided or declared inconclusive. They are moved rather "
           "than deleted: each is a setup error against a caller-supplied `l_plan` and still needs a "
           "disposition. **L986 is PLANNING-INTERNAL** - a disposition, not an outcome class, carrying no "
           "terminal consequence - because MOVE_CAP is an internal cap against a frozen constant "
           "that fires after a feasible prefix exists, so it is not an error in any supplied "
           "argument. `RAISE_CALLSITE_LEDGER.md` finds no path to them through "
           "`run_production_verdict`; that ledger's graph is name-based and a lower bound, so this is "
           "*no run-time path found*, not *no run-time path exists*.\n")
for k,v in sorted(c.items()): out.append(f"- **{k}** — {v}")
out.append(f"\n**Total {len(rows)} raise nodes.** Sites marked *soft* are ones I am least sure of; "
           f"if they read as CALLER instead, the numerical class drops from {c['NUMERICAL']} to "
           f"{c['NUMERICAL'] - len(SOFT)}. Sites marked *moved* were reclassified by ruling, not by "
           "reading.\n")
out.append("| line | function | exception | class | | message |")
out.append("|---|---|---|---|---|---|")
for ln,f,et,cls,soft,msg in rows:
    safe = msg.replace("|", "/")
    out.append(f"| {ln} | `{f}` | `{et}` | **{cls}** | {soft} | {safe} |")
(b/"ref/RAISE_SITE_CLASSIFICATION.md").write_text("\n".join(out)+"\n")
print("classes:", dict(c))
print("UNASSIGNED:", [(r[0],r[1],r[5][:40]) for r in unassigned])
