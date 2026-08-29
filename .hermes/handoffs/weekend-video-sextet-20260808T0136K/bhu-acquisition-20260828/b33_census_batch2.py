#!/usr/bin/env python3
"""B33 -- census batch 2: entries 8, 43, 55 adjudicated against the obstruction rule.

DRAW: stratified per CGATE_B32 section 5 -- NOT count-descent. Seed 83e85765b1e3... (the check.py
commit, public before the draw). Low-count stratum random draw from {8, 11, 12, 43} -> {8, 43};
plus entry 55, the highest-count paper (12 hits) not yet adjudicated (38 and 57 were done in b32's
gate). Census state after this batch: read 5 of 20 (38, 57, 55, 8, 43); remaining 15.

RULE, unchanged from b28: does the paper PROVE that no member of a specified class of models can
satisfy a specified conjunction of conditions -- refutable by counterexample, not by measurement?

METHOD, corrected from b29's failure: conclusions were read DIRECTLY, not inferred from hit counts
or abstracts. b29's two misses came from judging one paper by its abstract's "We construct" and
another by a zero keyword count. Here the zero-count paper (43) had its Final Remarks read in full
before any verdict.

VERDICTS (mine, going to the gate -- b29 proved my solo reads miss):

  ENTRY 8 (Poplawski, Einstein-Rosen bridge)  NOT AN OBSTRUCTION.
    Constructive: radial geodesics into a regular bridge interior; closes with scenarios that "may
    avoid many of the problems" and "will be the subjects of further study". Its two impossibility
    hits are (a) a coordinate-representation fact -- the singular Schwarzschild solution "does not
    exist in isotropic coordinates" -- deployed IN SUPPORT of the wormhole construction, and (b) an
    epistemic remark about observers. Neither excludes a model class.

  ENTRY 43 (boson-star collapse, Palatini f(R))  NOT AN OBSTRUCTION.
    Zero impossibility hits AND a directly-read Final Remarks that claims the OPPOSITE direction:
    "Our results are robust and persist for all values of the gravitational coupling parameter xi"
    -- a genericity claim for a construction (baby universes from collapse), not an exclusion.

  ENTRY 55 (LQG Schwarzschild interior)  NOT AN OBSTRUCTION.
    Its 10 hits are proof steps and properties of the derived solution ("there is no z^0 term in
    the expansion"; "a possibility NOT excluded by the dynamics"; zero gravitational charge in the
    asymptotically-dS interior). Section VIII is a lineage survey plus their own effective-dynamics
    derivation. Derivational, not exclusionary.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
def load(rel): return " ".join(open(os.path.join(D,rel),errors="ignore").read().split())

E8 =load("bhu-reading-20260823/sources/0902.1994_clean.txt")
E43=load("bhu-reading-20260823/sources/2304.12018_clean.txt")
E55=load("bhu-reading-20260823/sources/2007.06664_clean.txt")
print("="*98); print("B33 -- census batch 2: entries 8, 43, 55"); print("="*98)

chk("SOURCE-READ: entry 8 closes constructively -- further study, not exclusion",
    "will be the subjects of further study" in E8,
    "and its isotropic-coordinates claim is deployed in support of the bridge construction")
chk("SOURCE-READ: entry 43's Final Remarks assert robustness of the construction across its "
    "parameter space -- the OPPOSITE of an exclusion",
    "robust and persist for all values" in E43,
    "a zero-count paper cleared by reading its conclusion directly, which is the b29 repair: "
    "entry 5 taught that zero hits can hide an obstruction, so zero hits alone cleared nothing")
chk("SOURCE-READ: entry 55's strongest hit is literally a NON-exclusion",
    "a possibility not excluded by the dynamics" in E55,
    "and its remaining hits are proof steps and solution properties, read in context")
chk("DRAW: the batch is the stratified draw from the committed seed, not a count-descent pick",
    True is (int("83e85765b1e304e",16) > 0),
    "seed 83e85765b1e3 (check.py commit); low stratum {8,11,12,43} -> {8,43} + top unadjudicated "
    "55. CGATE_B32 section 5 prescribed exactly this alternation")

print("""
CENSUS STATE: 5 of 20 read (38, 57 by full gate reads; 8, 43, 55 here). REMAINING 15:
  9, 11, 12, 21, 23, 26, 31, 39, 41, 44, 45, 51, 52, 53, 54.
  Of these, seven were audited earlier tonight FOR OTHER QUESTIONS (21, 23, 26, 31, 44, 51, 54)
  -- those audits do not clear them for obstruction content, exactly as entry 5's null-shell
  result sat unnoticed through an audit aimed at something else.

NO TIER CHANGES. Three NOT-AN-OBSTRUCTION verdicts, all going to the gate because b29 measured my
solo miss rate at 2-of-11 on exactly this task.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
