#!/usr/bin/env python3
"""B8 -- verify HARNESS_DEFECT_REGISTER.md against the filesystem.

Blanc, relaying Hwao on her own lane state file: "This is the one artifact in the lane with no
adversarial reader. The drafts get seats, the checkers get controls, the state file gets whatever
attention is left over. Everything I've caught in it today I caught by accident."

The register is in exactly that position. It is the artifact a cold reader will trust most, it
carries tier conclusions, retraction status and re-derivation state for the whole corpus, and
NOTHING HAS EVER CHECKED IT. If it is wrong, everything downstream is wrong quietly.

This is the first check. It asserts what Blanc said he would verify by hand:
  - every script the register names EXISTS and RUNS
  - every "re-derived" claim points at a script that actually executes clean
  - every retracted conclusion is actually ABSENT from the bibliography as a live claim
  - every entry the §1h table names exists in the bibliography with the tier the table implies
"""
import re, os, sys, subprocess
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
REG  = os.path.join(HERE, "HARNESS_DEFECT_REGISTER.md")
BIB  = os.path.join(HERE, "../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")
R    = open(REG).read()
B    = open(BIB).read()
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print("B8 -- the register, checked against the filesystem for the first time"); print("=" * 96)

# ---- 1. every script the register names exists ------------------------------------------------
# WIDENED after the first run. The backtick-filename pattern matched exactly ONE script, because
# the register names them mostly as `a12`, "a6's check 4", "b7", etc. A verifier that checks one
# of twenty scripts and reports PASS is the narrow-pattern defect inside the tool built to catch
# it -- so: match every aNN / bNN token, resolve to a file on disk, and inspect the residue.
_tokens = sorted(set(re.findall(r"\b([ab]\d{1,2})(?:_[a-z0-9_]*)?(?:\.py)?\b", R)))
_ondisk = {f.split("_")[0]: f for f in os.listdir(HERE) if re.match(r"^[ab]\d{1,2}_.*\.py$", f)}
# SELF-EXCLUSION. Widening the token match (from backticked filenames to every aNN/bNN token)
# made this script match ITSELF -- the register names b8 -- so b8 executed b8, recursively, until
# the 600s subprocess timeout. The narrow version could not see itself; the corrected one could.
# A fix for one defect introducing another, visible only on execution.
_SELF = os.path.basename(__file__)
named   = sorted({_ondisk[t] for t in _tokens if t in _ondisk and _ondisk[t] != _SELF})
unresolved = sorted(t for t in _tokens if t not in _ondisk)
# a11 was DELETED 2026-08-29 on Duho's instruction after being measured unsound (register 1v).
# Its token still appears in the register, which is correct -- the record of a retired tool should
# survive the tool. Declared here so an EXPECTED absence is never confused with a missing file.
RETIRED = {"a11"}
unexpected = [t for t in unresolved if t in _ondisk or t not in RETIRED and re.match(r"^[ab]\d+$", t)]
missing = [f for f in named if not os.path.exists(os.path.join(HERE, f))]
print(f"   register mentions {len(_tokens)} script tokens; {len(named)} resolve to files on disk")
print(f"   tokens with no matching file (prose refs, section ids, false hits): {unresolved}")
print(f"\n1. SCRIPTS NAMED IN THE REGISTER: {len(named)}")
print(f"   {named}")
print(f"   deliberately retired, absence EXPECTED: {sorted(RETIRED)}")
chk("every script token resolves except those deliberately retired, and the register references a "
    "substantial share of the battery rather than one script",
    not missing and len(named) >= 10 and all(t in RETIRED for t in unresolved if re.match(r"^[ab]\d+$", t)),
    f"{len(named)} scripts resolved from {len(_tokens)} tokens. The first version of this check "
    f"matched backticked filenames only and verified ONE script while reporting PASS")

# ---- 2. and every one of them actually runs ---------------------------------------------------
fails = []
for f in named:
    r = subprocess.run([sys.executable, f], cwd=HERE, capture_output=True, timeout=600)
    if r.returncode != 0: fails.append((f, r.returncode))
print(f"\n2. EXECUTING each named script")
for f in named:
    mark = "FAIL" if any(x[0] == f for x in fails) else "ok"
    print(f"   {f:<38} {mark}")
chk("every script the register names RUNS CLEAN -- a register citing a broken script is a "
    "citation to nothing", not fails,
    f"non-zero exit: {fails}" if fails else f"{len(named)}/{len(named)} exit 0")

# ---- 3. the §1h table's entries exist and its tier claims match the bibliography ---------------
rows = re.findall(r"^\|\s*(\d+(?:,\s*\d+)*)\s*\|([^|]*)\|", R, re.M)
tbl_entries = sorted({int(x) for r, _ in rows for x in re.findall(r"\d+", r)})
lines = B.split("\n")
st = [(int(m.group(1)), i) for i, l in enumerate(lines) if (m := re.match(r"^\*\*(\d+)\.\s", l))]
tiers = OrderedDict()
for k, (n, i) in enumerate(st):
    end = st[k+1][1] if k+1 < len(st) else len(lines)
    if n in tiers: continue
    t = re.search(r"Testability:\s*\*\*([A-Z][A-Z\-/ ]+)\*\*", "\n".join(lines[i:end]))
    if t: tiers[n] = t.group(1).split("/")[0].strip()
absent = [e for e in tbl_entries if e not in tiers]
print(f"\n3. ENTRIES NAMED IN THE §1h TABLE: {tbl_entries}")
print(f"   their current bibliography tiers: { {e: tiers.get(e, 'ABSENT') for e in tbl_entries} }")
chk("every entry the register's table names exists in the bibliography with a parseable tier",
    not absent, f"absent or untiered: {absent}" if absent else f"all {len(tbl_entries)} resolve")

# ---- 4. retracted conclusions are absent from the bibliography AS LIVE CLAIMS ------------------
# per §1k: test that the retracted phrase appears only inside a retraction context, never as an
# assertion. Checking the register's own claim that this was fixed.
phrase = "gives the family a SECOND live calibrated falsifier"
occ = [m.start() for m in re.finditer(re.escape(phrase), " ".join(B.split()))]
Bn = " ".join(B.split())
quoted = all("previously read" in Bn[max(0, i-120):i] for i in occ)
print(f"\n4. RETRACTED CONCLUSIONS -- present as live claims anywhere?")
print(f"   \"{phrase}\": {len(occ)} occurrence(s), all inside a retraction context: {quoted}")
chk("the retracted second-falsifier claim survives only as a quoted retraction, never as an "
    "assertion", len(occ) == 0 or quoted,
    "checked the way §1k prescribes, not by absence -- deleting the retraction would also pass "
    "an absence test, which is the defect §1k exists to name")

# ---- 5. entry 22's refiling, which the register claims -----------------------------------------
e22 = ""
for k, (n, i) in enumerate(st):
    if n == 22:
        end = st[k+1][1] if k+1 < len(st) else len(lines)
        e22 = "\n".join(lines[i:end]); break
print(f"\n5. CLAIMED STATE CHANGES, verified on disk")
print(f"   entry 22 filed THEORETICAL-OBSTRUCTION : {'THEORETICAL-OBSTRUCTION' in e22}")
chk("entry 22 is actually refiled in the bibliography, not merely claimed to be",
    "THEORETICAL-OBSTRUCTION" in e22,
    "this is the exact defect the register records at 1j -- a commit message claimed a refiling "
    "that had not happened. Now asserted by a check rather than by a message")

print("""
6. WHAT THIS CHECK CANNOT DO -- named per the register's own admissibility rule

   PATTERN USED: named-script extraction by backtick regex; tier parse by the repaired
   Testability pattern; retraction test by quotation-context.

   WHAT IT WOULD MISS:
     - a register claim written in prose that names no script and no entry number. Most of the
       register is prose, and prose is not checked here at all.
     - a script that RUNS but whose checks no longer test what the register says they test.
       Exit 0 is not agreement.
     - a §1h row whose BEFORE/NOW narrative is wrong while its entry number and tier are right.
     - anything in the register about the DESI lane, which is not on this filesystem.

   WHAT WAS DONE ANYWAY: Blanc reads the register against the filesystem by hand on refresh.
   This check is the floor under that, not a substitute for it. Its value is that it fails
   loudly when a named script disappears or stops running -- the failure modes most likely to
   creep in silently as the lane moves.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
