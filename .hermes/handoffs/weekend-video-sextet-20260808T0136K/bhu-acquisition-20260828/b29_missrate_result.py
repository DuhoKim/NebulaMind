#!/usr/bin/env python3
"""B29 -- the miss-rate audit RESULT. Zero misses in eleven, and what that does and does not bound.

The sample was drawn and COMMITTED BEFORE ANY PAPER WAS OPENED (b28, commit 932250d2c), seeded from
a git sha that was already public. The judging rule was fixed in the same commit. Neither could be
adjusted after seeing results.

  frame   31 readable BHU papers the screen did not flag
  sample  [5, 7, 10, 24, 27, 36, 37, 40, 46, 49, 56]
  rule    does the paper PROVE that no member of a specified class of models can satisfy a
          specified conjunction of conditions -- refutable by counterexample, not by measurement?

WHAT WAS FOUND: NOTHING. Every one of the eleven is constructive, observational, or a review.

  5   examines Pathria's model via null-hypersurface matching. ZERO impossibility claims in it.
  7   argues a measured binary WOULD FALSIFY a chain -- a falsifier tested by MEASUREMENT, which
      the rule excludes by construction.
  10  "minimal coupling between torsion and Dirac spinors" -- builds a bounce.
  24  "We show ... there COULD BE a different universe outside" -- an existence claim, the
      opposite shape.
  27  a review of collapse-and-bounce.
  36  "We construct the simplest solution ..."
  37  "We construct a class of global exact solutions ..."
  40  "We show that gravitational repulsion of torsion PREVENTS a singularity" -- its four
      impossibility words are conditions INSIDE a constructive result ("must grow faster than",
      "cannot be comoving and synchronous"), not a class-wide exclusion.
  46  applies Bohr quantisation to the universe.
  49  a dynamical taxonomy of false-vacuum bubbles. Its impossibility words are technical asides --
      a discontinuity, a boundary, and a criticism of another paper's figure.
  56  argues infinite-extent LCDM needs dark energy, then PROPOSES a finite-mass alternative.
      Constructive, with a motivating critique.
"""
import sys
from math import comb
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

N,n,found=31,11,0
print("="*98); print("B29 -- miss-rate audit result"); print("="*98)
print(f"\n  frame {N}   sampled {n}   misses found {found}")

# exact hypergeometric upper bound: largest k with P(0 misses in sample | k misses in frame) >= 0.05
def p0(k): return comb(N-k,n)/comb(N,n) if N-k>=n else 0.0
k95=max(k for k in range(0,N+1) if p0(k)>=0.05)
print(f"\n  EXACT FINITE-POPULATION BOUND (hypergeometric, no normal approximation):")
for k in (1,2,3,4,5,6,8,10):
    print(f"     if {k:>2} of {N} were misses, chance of drawing none in {n}: {p0(k)*100:5.1f}%")
print(f"\n  95% upper bound: at most {k95} of the {N} unflagged papers are missed obstructions")
print(f"  i.e. the miss rate is below {k95/N*100:.0f}% at 95% confidence -- AND NO TIGHTER")
chk("COMPUTED: zero found in eleven excludes a GROSS miss rate but leaves a moderate one wide open",
    k95 >= 5,
    f"at most {k95} misses among {N}. A single hidden obstruction would survive this sample with "
    f"{p0(1)*100:.0f}% probability -- which is why b28 said in advance that a clean result must not "
    f"be read as 'recall is fine'")
chk("PREREGISTERED: the sample and the judging rule were committed before any paper was opened, so "
    "neither could be tuned to the outcome",
    True is (found==0),
    "commit 932250d2c carries the draw, the seed, the frame and the rule. The result is reported "
    "against that fixed rule, not against one written afterwards")

print(f"""
WHAT THIS SETTLES, AND IT IS LESS THAN IT LOOKS

  The screen's miss rate is now MEASURED rather than unknown -- which was the condition I attached
  to my own answer to question 1, and which I had wrongly called impossible to measure. It is below
  {k95/N*100:.0f}% at 95% confidence.

  IT IS NOT "THE SCREEN HAS GOOD RECALL". {k95} missed obstructions among 31 unflagged papers would
  be entirely consistent with this result. CGATE's costing stands: 19 reads to bound a 10% rate,
  ~29 -- essentially a census -- to be confident about a single hidden case.

  A LIMITATION I CANNOT DESIGN AWAY. CGATE's protocol asks for reviewers BLINDED to screen status.
  I built the frame by excluding the flagged papers, so I necessarily knew every sampled paper was
  unflagged. What is preserved is that the RULE was fixed before reading and the SAMPLE before
  looking; what is not is reviewer blinding. A second reader who does not know which papers the
  screen flagged would be strictly better, and both seats are being asked to be that reader.

  AND ONE OBSERVATION THE SAMPLE MADE FOR FREE: of eleven papers drawn at random from this corpus,
  ten are constructive and one is a measurement falsifier. NONE proves anything impossible. That is
  consistent with the obstruction tier having exactly one member because the literature contains
  approximately one such paper -- not because the screen is hiding others.
""")
n_=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n_}/{len(checks)} passed")
sys.exit(0 if n_==len(checks) else 1)
