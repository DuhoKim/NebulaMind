#!/usr/bin/env python3
"""B30 -- three CONSISTENCY-ONLY entries that may be theoretical obstructions. A TIER PROPOSAL.

FOUND BY the miss-rate audit (b29), as a by-product: a random draw from the papers the screen did
not flag turned up entries 5, 37 and 49 meeting the preregistered obstruction rule. A recall check
is not a tier audit, so this is the audit.

WHY THE CURRENT TIER IS THE WRONG ONE, IN THE RECORD'S OWN WORDS. CONSISTENCY-ONLY is defined here
as a paper that shows compatibility and states no prediction -- "SILENT about what cannot happen".
An obstruction is the opposite: it says something CANNOT EXIST. If these three prove impossibilities
then CONSISTENCY-ONLY is not merely imprecise, it asserts the negation of what they do.

NO TIER IS CHANGED BY THIS FILE. Every tier change is Duho's by standing rule, and "sweep on" is not
a delegation of one. This audits and files.

AND TWO OF THE THREE CARRY PRIOR SIGNALS NOBODY ACTED ON:
  entry 5's own note says "the matching defect it identifies is exactly what a strict
    junction-condition audit would re-derive" -- the record knew, and filed it CONSISTENCY-ONLY.
  entry 37 was BLIND-FLAGGED 2026-08-28 for promotion to QUALITATIVE-DIRECTIONAL and deliberately
    not gated, because that sweep had failed its own control. The flag was right that something was
    wrong and wrong about which way.
"""
import re, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))
def load(rel):
    p=os.path.join(D,rel)
    if p.endswith(".pdf"):
        import fitz; d=fitz.open(p); return " ".join(" ".join(pg.get_text() for pg in d).split())
    return " ".join(open(p,errors="ignore").read().split())

E5 =load("reviews/bhu-citation-custody-evidence-20260811/arxiv-1412.0105v1.txt")
E37=load("bhu-reading-20260823/sources/0210105_clean.txt")
E49=load("bhu-reading-20260823/sources/blau_guendelman_guth_1987_prd35_1747.pdf")
BIB=" ".join(open(os.path.join(D,"bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md")).read().split())

print("="*98); print("B30 -- three CONSISTENCY-ONLY entries audited against the obstruction rule"); print("="*98)
print("""
THE RULE, unchanged from b28's preregistration:
   does the paper PROVE that no member of a specified class of models can satisfy a specified
   conjunction of conditions -- refutable by counterexample in that domain, not by measurement?
""")

print("ENTRY 5 -- Khakshournia 2010, currently CONSISTENCY-ONLY")
chk("SOURCE: the paper states a general class, not one model -- it formulates 'the general problem "
    "of gluing a FRW metric to a vacuum Schwarzschild one along a null hypersurface'",
    "the general problem of gluing a FRW metric to a vacuum" in E5.lower() or
    "general problem of gluing" in E5.lower(),
    "a class-level formulation is what separates an obstruction from a comment on one model")
chk("SOURCE: and it concludes the smooth case is EXCLUDED for that class -- the matching is not "
    "smooth and requires a null shell with surface pressure",
    "the matching is not smooth" in E5.lower() and "surface pressure" in E5.lower(),
    "derived from the discontinuity of the uu component of extrinsic curvature across Sigma, not "
    "asserted. A smooth shell-free counterexample in that class would refute it; no measurement can")

print("\nENTRY 37 -- Smoller & Temple 2003, currently CONSISTENCY-ONLY")
chk("SOURCE: an explicit iff partition of its own parameter class, excluding sigma > 1/3 from the "
    "everywhere-subluminal condition",
    "if and only if" in E37.lower() and "1/3" in E37,
    "'s_sigma(S) < 1 for all 0 < S <= 1, if and only if sigma <= 1/3', with Theorem 3 giving shock "
    "speed 0, infinity or 1 as sigma is below, above or equal to 1/3")

print("\nENTRY 49 -- Blau, Guendelman & Guth 1987, currently CONSISTENCY-ONLY")
chk("SOURCE: it states the impossibility, names the domain and names the escape",
    "cannot be avoided" in E49.lower() or "initial singularity" in E49.lower(),
    "under exact spherical symmetry and the weak energy condition the initial singularity cannot be "
    "avoided, by the Penrose theorem, with quantum WEC violation as the escape")
chk("SOURCE: BUT the full proof is delegated to the companion paper, which is entry 48 of this same "
    "corpus -- so entry 49 states an obstruction it does not itself prove",
    "farhi" in E49.lower() or "work currently in progress" in E49.lower(),
    "CGATE_B29 and AGATE_B29 AGREE on this and disagree on what follows. Under b28's rule as "
    "written -- 'does the paper prove' -- applying the Penrose theorem counts. Under a 'full proof "
    "printed here' convention it does not. THAT CONVENTION WAS NEVER PREREGISTERED")

print("""
WHAT IS PROPOSED, AND IT IS A PROPOSAL

  ENTRIES 5 AND 37: both seats agree these are source-contained obstructions. CONSISTENCY-ONLY
  asserts the negation of what they do. THEORETICAL-OBSTRUCTION is the tier the record already has
  for exactly this, and entry 22 is the precedent.

  ENTRY 49: the seats agree on the FACTS and split on the CONVENTION. It states an obstruction and
  delegates the proof to entry 48. Whether that is an obstruction paper or a paper reporting one is
  a scheme question, not a reading question, and it is the same shape as the question Duho already
  answered about claim shape versus claim strength.

  AND THIS TOUCHES A FOURTH ENTRY NOBODY HAS LOOKED AT. If entry 49 reports the obstruction and
  entry 48 proves it, THEN ENTRY 48 IS THE OBSTRUCTION PAPER -- and entry 48 has never been audited.
  It is not in the readable set, so it cannot be audited without acquiring it.

  NO TIER CHANGED. Filed for Duho with these three options and their costs.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
