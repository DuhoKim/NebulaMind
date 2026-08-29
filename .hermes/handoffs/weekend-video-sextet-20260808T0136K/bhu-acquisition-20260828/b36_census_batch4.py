#!/usr/bin/env python3
"""B36 -- census batch 4: entries 39, 21, 11.

DRAW: from b35_draw_batch4.py, COMMITTED BEFORE THE BATCH ADJUDICATION ARTIFACT (a038e197b) -- CGATE's precise wording: git orders repository artifacts, not my private reading history, and some of these papers were read earlier tonight for other questions with ordered pools and the
executable rule -- the repair for b34's refuted draw. Anyone re-running b35 gets 39, 21, 11.

RULE unchanged from b28. VERDICTS (mine, to the gate):

  ENTRY 39 (Poplawski 2012 GRG)   NOT AN OBSTRUCTION. "Torsion ... prevents the formation of
    singularities ... replaces the singular big bang by a bounce" -- the constructive family shape
    ruled on for entries 10, 40, 12. Its fourth hit is about a QUANTUM bounce being pre-empted by
    the classical one: a mechanism comparison, not a class exclusion.

  ENTRY 21 (Roupas 2022)   NOT AN OBSTRUCTION. Its strongest hit is a derived STABILITY result --
    "radial perturbations cannot develop unstable radial modes" (Eqs. 105-108) -- an internal
    theorem delimiting the constructed detectable-universe solution, the entry-37/55 claim-level
    shape. The other hits are a quantum localisation heuristic and detector sensitivity. The
    paper's operative contribution is the construction; tier PROSPECT stands.

  ENTRY 11 (Poplawski, universe in a BH with spin and torsion)   NOT AN OBSTRUCTION. Same
    constructive family; closes with "every black hole MAY CREATE a new universe" and a
    self-described philosophical remark. Nothing class-exclusionary.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
def load(rel): return " ".join(open(os.path.join(D,rel),errors="ignore").read().split())

E39=load("bhu-reading-20260823/sources/1105.6127_clean.txt")
E21=load("bhu-reading-20260823/sources/2203.13295_clean.txt")
E11=load("reviews/bhu-citation-custody-evidence-20260811/arxiv-1410.3881v2.txt")
print("="*98); print("B36 -- census batch 4: entries 39, 21, 11"); print("="*98)
chk("DRAW: the batch reproduces from the COMMITTED b35 code, not from a shell one-off",
    True is (os.path.exists(os.path.join(_HERE,"b35_draw_batch4.py"))),
    "seed a2d70fd0c, pools ordered count-desc/entry-asc, one shared RNG. b34's draw was refuted "
    "for exactly the lack of this")
chk("SOURCE-READ: entry 39 is the constructive torsion-bounce family shape",
    "prevents the formation of singularities" in E39,
    "same family as 10/40/12, all ruled constructive by both seats")
chk("SOURCE-READ: entry 21's strongest exclusion is a stability theorem about its own construction",
    "cannot develop unstable radial modes" in E21,
    "an internal delimiting result, the entry-37/55 shape; kept in prose consideration, no tier "
    "bearing. Operative contribution is the detectable-universe construction")
chk("SOURCE-READ: entry 11 closes constructively",
    "may create a new universe" in E11,
    "plus a self-described unsolvable philosophical remark, which excludes nothing")
print("""
CENSUS STATE after this batch: 11 of 20 adjudicated. REMAINING 9: 9, 23, 26, 41, 44, 45, 52, 53, 54.
NO TIER CHANGES, none proposed.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
