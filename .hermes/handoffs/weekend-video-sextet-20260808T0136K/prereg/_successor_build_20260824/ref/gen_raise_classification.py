import ast, hashlib
from pathlib import Path
b = Path(".hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824")
V = b/"ref/successor_ref_v9.py"
src = V.read_text(); tree = ast.parse(src)
owner = {}
for fn in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
    for ln in range(fn.lineno, (fn.end_lineno or fn.lineno)+1): owner.setdefault(ln, fn.name)

NUM = {1123,1134,1153, 1369,1397,1401,1403,1411,1435,1437,1439,1442,
       1209,1462,1464,1468, 1503,1513,1517,1537,1548,1554}
SOFT = {1209,1462,1464,1468}                      # domain-vs-computed, named as uncertain
PLAN = {963,973,986}                              # numerical but pre-run
WRAP = {168,1620,776}                             # propagation, not a distinct condition
CALLER = {215,217,262,938,1018,1022,1027,1032,1038,1040,1050,1053,1077,1099,1102,1108,1206,1460,1603,1675}
INTEG = {64,856,858,860,862,864,867,872,876,885,887,889,891,1020,1601,1605,1641,1643,1649,1677,1681,1687}

rows=[]
for n in ast.walk(tree):
    if not isinstance(n, ast.Raise): continue
    e=n.exc
    et = e.func.id if isinstance(e,ast.Call) and isinstance(e.func,ast.Name) else (e.id if isinstance(e,ast.Name) else "bare")
    a = e.args[0] if isinstance(e,ast.Call) and e.args else None
    msg = str(a.value) if isinstance(a,ast.Constant) else (
        "".join(v.value if isinstance(v,ast.Constant) else "{}" for v in a.values) if isinstance(a,ast.JoinedStr) else "")
    ln=n.lineno
    if et in ("InconclusiveByPower","InconclusiveByCalibration"): cls="TYPED-OUTCOME"
    elif et=="ManifestClosureError": cls="INTEGRITY"
    elif ln in NUM: cls="NUMERICAL"
    elif ln in PLAN: cls="NUMERICAL-PLANNING"
    elif ln in WRAP: cls="WRAPPER"
    elif ln in CALLER: cls="CALLER"
    elif ln in INTEG: cls="INTEGRITY"
    else: cls="UNASSIGNED"
    rows.append((ln, owner.get(ln,"?"), et, cls, ("soft" if ln in SOFT else ""), msg[:70]))
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
           "INTEGRITY covers failures already claimed by a VOID antecedent. NUMERICAL-PLANNING fires "
           "before the run exists. WRAPPER re-raises another site's failure.\n")
for k,v in sorted(c.items()): out.append(f"- **{k}** — {v}")
out.append(f"\n**Total {len(rows)} raise nodes.** Sites marked *soft* are ones I am least sure of; "
           "if they read as CALLER instead, the numerical class drops from 22 to 18.\n")
out.append("| line | function | exception | class | | message |")
out.append("|---|---|---|---|---|---|")
for ln,f,et,cls,soft,msg in rows:
    safe = msg.replace("|", "/")
    out.append(f"| {ln} | `{f}` | `{et}` | **{cls}** | {soft} | {safe} |")
(b/"ref/RAISE_SITE_CLASSIFICATION.md").write_text("\n".join(out)+"\n")
print("classes:", dict(c))
print("UNASSIGNED:", [(r[0],r[1],r[5][:40]) for r in unassigned])
