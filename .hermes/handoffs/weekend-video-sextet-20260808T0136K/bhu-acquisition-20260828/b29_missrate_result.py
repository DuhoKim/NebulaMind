#!/usr/bin/env python3
"""B29 -- the miss-rate audit.  MY RESULT WAS ZERO. IT IS AT LEAST TWO. WITHDRAWN AND CORRECTED.

  CGATE_B29  MISSRATE_REFUTED_THREE_MISSES_IN_SAMPLE
  AGATE_B29  MISSRATE_CONFIRMED_JUDGMENTS_BUT_REFUTED_FRAME

THE SEATS SPLIT AND IT IS RESOLVABLE ON THE SOURCES, WHICH I DID BEFORE WRITING THIS.
AGATE confirmed my zero -- but its own verdict says it "specifically investigat[ed] Entries 49, 40,
and 56", which are the three I NAMED IN THE BRIEF. It never examined entries 5 and 37. CGATE read
all eleven and found two I had not flagged. And AGATE's arithmetic is wrong: it gives k=5 -> 7.3%
and k=6 -> 3.6%, concluding the bound is 5. The true values are 9.12% and 5.26%, so the bound is 6.
Verified here, and CGATE independently agrees. One seat did the work; the other checked my homework.

THE TWO MISSES, verified in the pinned text by me, not accepted from a verdict:

  ENTRY 5. Its central result: "It turns out that the matching is NOT SMOOTH, and in fact, the null
  hypersurface is the history of a null shell admitting a surface pressure." No member of the stated
  FRW/Schwarzschild null-junction class has a smooth shell-free matching. A smooth counterexample
  would refute it; no measurement is involved. MY CHECK REPORTED "0 IMPOSSIBILITY-WORD HITS" for
  this paper -- because my pattern had no "not smooth" and no "can only". A false absence from a
  narrow pattern, for the seventh time in this lane.

  ENTRY 37. "s_sigma(S) < 1 for all 0 < S <= 1, IF AND ONLY IF sigma <= 1/3", with Theorem 3 giving
  shock speed 0, infinity, or 1 according as sigma <, >, or = 1/3. So no member of the stated exact
  shock family with sigma > 1/3 is everywhere subluminal. An explicit parameter-space exclusion.
  I RULED IT CONSTRUCTIVE FROM ITS ABSTRACT'S "We construct" AND NEVER LOOKED AT ITS THEOREMS.

  ENTRY 49 is a third under the rule as preregistered -- it states that under exact spherical
  symmetry and the weak energy condition "the initial singularity cannot be avoided", names the
  Penrose theorem as the method and quantum WEC violation as the escape. CGATE notes the full proof
  is delegated to the companion Farhi-Guth paper, so a "proof must be printed here" convention would
  exclude it. THAT CONVENTION WAS NOT PREREGISTERED, so it is reported both ways rather than chosen
  now -- choosing after seeing the result is exactly what preregistration exists to prevent.

CGATE'S BOUNDARY, which is why 10 and 40 are still not misses: entries 10 and 40 establish a
MECHANISM and exhibit its outcome, so "prevents a singularity" is constructive; entries 5 and 37
EXCLUDE A REGION of a stated class. Without that line, any existence theorem could be relabelled an
obstruction by negating it.
"""
import re, os, sys
from math import comb
_HERE=os.path.dirname(os.path.abspath(__file__))
D=os.path.abspath(os.path.join(_HERE,".."))
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

N,n=31,11
print("="*98); print("B29 -- miss-rate audit [ZERO WITHDRAWN; AT LEAST TWO]"); print("="*98)

# CGATE: "B29 never opens or scores any of the eleven source files. Its result is hardcoded."
E5=" ".join(open(os.path.join(D,"reviews/bhu-citation-custody-evidence-20260811/arxiv-1412.0105v1.txt"),errors="ignore").read().split())
E37=" ".join(open(os.path.join(D,"bhu-reading-20260823/sources/0210105_clean.txt"),errors="ignore").read().split())
chk("SOURCE-READ, not hardcoded: entry 5's own text states the matching is NOT SMOOTH and requires "
    "a null shell -- an exclusion over its stated junction class",
    "the matching is not smooth" in E5.lower() and "null shell" in E5.lower(),
    "the previous version of this file never opened a single sampled paper; its result was the "
    "literal `found = 0` assigned three lines above the check that 'verified' it")
chk("SOURCE-READ: entry 37 carries an explicit iff partition excluding sigma > 1/3 from the "
    "everywhere-subluminal condition",
    "if and only if" in E37.lower() and "1/3" in E37,
    "'s_sigma(S) < 1 for all 0 < S <= 1, if and only if sigma <= 1/3', plus Theorem 3. I ruled this "
    "paper constructive from the word 'construct' in its abstract")

def ple(x,k): return sum(comb(k,i)*comb(N-k,n-i) for i in range(0,x+1) if 0<=n-i<=N-k)/comb(N,n)
b2=max(k for k in range(N+1) if ple(2,k)>=0.05)
b3=max(k for k in range(N+1) if ple(3,k)>=0.05)
print(f"\n  observed misses: 2 definite (5, 37); 3 under the rule as written (adding 49)")
print(f"  X=2 -> 95% upper bound {b2} of {N}  ({b2/N*100:.1f}%)")
print(f"  X=3 -> 95% upper bound {b3} of {N}  ({b3/N*100:.1f}%)")
chk("COMPUTED: the corrected bounds are far weaker than the withdrawn one and do NOT exclude a "
    "gross miss rate -- they are consistent with a third to a half of the unflagged pile",
    b2 >= 13 and b3 >= 16,
    f"{b2}/{N} and {b3}/{N}. The withdrawn zero gave 6/31. CGATE reached the same two numbers "
    f"independently. The likelihood is maximised near 5/31 for X=2")
chk("ARITHMETIC: AGATE's tail probabilities are wrong, which is why its bound of 5 is wrong",
    abs(comb(N-5,n)/comb(N,n)-0.0912)<0.001 and abs(comb(N-6,n)/comb(N,n)-0.0526)<0.001,
    "AGATE: k=5 -> 7.3%, k=6 -> 3.6%. True: 9.12% and 5.26%. Not a judgement call")

print("""
WHAT THIS MEANS, and it reverses the headline

  THE SCREEN LEAKS. A random sample of eleven unflagged papers contains at least two -- possibly
  three -- papers that meet the preregistered obstruction rule. That is direct evidence, on a
  preregistered draw, that verifying every flag does not make the screen safe: hand-checking flags
  cannot see a paper that was never flagged.

  AND IT BEARS DIRECTLY ON A CLOSED DECISION. My answer to question 1 was "screen, then hand-check
  every flag", with the condition "either run the miss-rate audit or explicitly accept the risk".
  THE AUDIT IS RUN AND THE ANSWER IS ADVERSE. I am not silently reversing a closed decision;
  the result is recorded against it and flagged for Duho.

  THE FREE OBSERVATION IS WITHDRAWN. I wrote that ten of eleven papers being constructive supports
  the tier having one member because the literature holds about one such paper. CGATE: factually
  wrong after source reading, and structurally invalid anyway -- a sample conditioned on what the
  screen did not flag cannot estimate the literature's prevalence.

  WORDING CORRECTED: 6/31 is 19.35%, so the withdrawn claim "below 19%" was false even on its own
  terms; and a confidence bound is not a posterior probability about the realised population.
""")
n_=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n_}/{len(checks)} passed")
sys.exit(0 if n_==len(checks) else 1)
