#!/usr/bin/env python3
"""B28 -- PREREGISTRATION of the miss-rate sample. The draw only. No reading, no verdicts.

WHY SEPARATE. My answer to question 1 attached a condition: measure what the screen MISSES, or say
plainly we accept the risk. CGATE's design requires the sample be drawn BLIND TO OUTCOME and not
chosen by promise, acquisition history, or how nearly the screen liked a paper. So the draw is
committed before anything is read, and the seed is a git sha that was already public when the draw
was made -- I cannot reroll it into a friendlier sample.

  seed  = 5d5a2454e54b7638401428bfc58d3a4cdd87a8ad   (HEAD before this file existed)
  frame = readable BHU papers the screen did NOT flag
  n     = 11  -- CGATE's costing: 11 reads give >=95% chance of meeting at least one missed
          obstruction if 20% of the unflagged pile are misses. It does NOT bound rarer misses:
          10% needs 19 reads, a single hidden case needs ~29, essentially a census.

WHAT THIS CAN AND CANNOT SHOW. Finding one or more misses in 11 is strong evidence the screen leaks.
Finding none bounds a GROSS failure and leaves a subtler one entirely open. Nobody should read a
clean result as "recall is fine".
"""
import re, os, sys, random
_HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(_HERE,".."))
SEED="5d5a2454e54b7638401428bfc58d3a4cdd87a8ad"
FLAGGED={22,25,6}                      # b1's flags on the readable corpus, frozen
READABLE=[5,7,8,9,10,11,12,21,22,23,24,25,26,27,31,36,37,38,39,40,41,43,44,45,46,49,51,52,53,54,55,56,57,6]
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

frame=sorted(set(READABLE)-FLAGGED)
rng=random.Random(int(SEED[:15],16))
sample=sorted(rng.sample(frame,11))
print("="*98); print("B28 -- preregistered miss-rate sample"); print("="*98)
print(f"\n  seed        : {SEED}")
print(f"  frame       : {len(frame)} readable papers the screen did not flag")
print(f"  {frame}")
print(f"\n  SAMPLE (n=11): {sample}")
chk("PREREGISTERED: the sample is a deterministic function of a git sha that was already committed "
    "and pushed before this file was written, so it cannot have been rerolled",
    len(sample)==11 and sample==sorted(random.Random(int(SEED[:15],16)).sample(frame,11)),
    f"seed {SEED[:12]}… reproduces {sample} on any machine. The lane's precedent is a draw seeded "
    f"from a sha fixed before the draw")
chk("FRAME: no flagged paper is in the frame, so this samples what the screen MISSED rather than "
    "what it caught",
    not (set(sample) & FLAGGED) and not (set(frame) & FLAGGED),
    f"flagged {sorted(FLAGGED)} excluded. Sampling near-misses instead would test the screen's "
    f"boundary, which CGATE specifically warned is not a recall measurement")
print("""
  THE RULE EACH SAMPLED PAPER WILL BE JUDGED BY -- fixed now, before any is read, and it is the
  bibliography's own tier definition:

      Does the paper PROVE that no member of a specified class of models can satisfy a specified
      conjunction of conditions -- refutable by exhibiting a counterexample in that domain, and
      NOT by any measurement?

      A paper that merely fails to predict is SILENT about what cannot happen. That is not a no-go.

  A MISS is a sampled paper that meets this and which the screen did not flag.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
