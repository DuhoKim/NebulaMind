#!/usr/bin/env python3
"""A9 -- entry 52 (Unger & Poplawski 2019, ApJ 870, 78): is CONSISTENCY-ONLY too weak?

Blanc's standing directive: hunt an entry tiered too weak -- a CONSISTENCY-ONLY holding an
author-stated number and threshold. Entry 52 is the best candidate in the corpus, because our
OWN record already says it has one. METHODS_NOTE_CLASSIFIER_BIAS.md:

    "...including entry 52, whose threshold is C > 1.9e48, an inequality on a model parameter
     rather than an observable, and the exact case the field was added to catch."

So there is a specific prior claim of ours to test, in both directions.

RESULT: the tier is CORRECT, and our note's reasoning is IMPRECISE. Both matter.

Pinned: ../bhu-reading-20260823/sources/1808.08327_clean.txt
"""
import re, sys, hashlib

S = "../bhu-reading-20260823/sources/1808.08327_clean.txt"
T = " ".join(open(S).read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print(f"A9 -- entry 52  [sha256 {hashlib.sha256(open(S,'rb').read()).hexdigest()[:12]}]"); print("=" * 96)

# ---- 1. the threshold is real and author-stated --------------------------------------------
thr = re.search(r"condition for the absence of turning points in a late universe: C >[^.]*", T)
print(f"\n1. THE THRESHOLD OUR NOTE FLAGGED IS REAL")
print("   " + (" ".join(thr.group(0).split())[:200] if thr else "<< not found >>"))
chk("entry 52 states an explicit numeric threshold, as our note said", thr is not None,
    "C > 1.9e48 -- so the note was right that a number and threshold are present")

# ---- 2. BUT the paper is CONDITIONAL and never claims our universe is closed ---------------
cond = "a closed universe exists only when the product of the scale factor and temperature is higher than a particular threshold" in T
unres = "which are not restricted" in T or "are not restricted by such a condition" in T
print(f"\n2. IS IT A PREDICTION ABOUT OUR UNIVERSE?  No -- the paper is explicitly conditional")
print(f"   'a closed universe exists ONLY WHEN ...' ................. {cond}")
print(f"   '... flat and open universes are NOT RESTRICTED' ......... {unres}")
chk("the paper analyses all three curvature cases and commits to none for our Universe",
    cond and unres,
    "it says what EACH case requires; a claim that cannot fail because nothing is asserted to hold")

# ---- 3. the threshold is DERIVED FROM the observed Lambda, not predicted -------------------
lam = re.search(r"λ\s*=\s*1\s*3[^.]{0,80}?5\.0\s*×\s*10\s*−\s*124", T) or ("5.0\\times 10^{-124}" in T)
from_obs = "This small value results from the small cosmological constant" in T
must_reach = "must reach the threshold" in T
print(f"\n3. WHICH WAY DOES THE INFERENCE RUN?")
print(f"   lambda fixed at 5.0e-124 from the OBSERVED Lambda ........ {bool(lam) and from_obs}")
print(f"   and C 'must reach the threshold' so the model matches ..... {must_reach}")
chk("QUOTED: the source fixes lambda from the observed Lambda and says C 'must reach the "
    "threshold' -- direction of inference read from the text, not computed here",
    bool(lam) and from_obs and must_reach,
    "'must reach the threshold (51) so that the Universe could start the observed current "
    "acceleration' -- a requirement on the model, not a prediction that could fail")

# ---- 4. our own note's reasoning is imprecise, and the imprecision is worth fixing ---------
what_c = "representing the product of the scale factor and temperature" in T
xeq    = "x_{\\textrm{eq}}" in T or "x eq" in T
print(f"\n4. WHAT IS C, EXACTLY?  [our note calls it 'a model parameter']")
print(f"   the paper: C represents the PRODUCT OF SCALE FACTOR AND TEMPERATURE .. {what_c}")
print(f"   normalised by bounce-scale quantities (a_cr, T_cr; x_eq = T_eq/T_cr) . {xeq}")
chk("C is NOT a free model parameter -- it is an observable quantity (aT, conserved) over a "
    "theory-determined bounce scale",
    what_c and xeq,
    "so the honest objection is not 'not an observable' but 'not INDEPENDENTLY CHECKABLE': the "
    "numerator is measurable, the denominator comes from the torsion theory being tested")

print("""
5. VERDICT

   TIER CONFIRMED: CONSISTENCY-ONLY is correct, and for a stronger reason than our note gave.
   The paper never asserts our Universe is closed -- it derives what EACH curvature case would
   require. Nothing is claimed to hold, so nothing can fail.

   OUR OWN NOTE NEEDS A CORRECTION, and it is small but real. METHODS_NOTE calls C "an inequality
   on a model parameter rather than an observable". C is the product of scale factor and
   temperature -- aT, which is conserved and measurable -- divided by a bounce scale the torsion
   theory supplies. The right objection is NOT that C is unobservable. It is that C is not
   INDEPENDENTLY checkable, because its normalisation comes from the very theory under test.

   That distinction matters for the sweep's own method: "no observable here" would let us skip
   such entries, while "observable numerator, theory-supplied denominator" tells us exactly what
   an independent test would have to pin down first.

   SEVENTH ENTRY, SEVENTH TIER UNCHANGED.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("\nSTATUS: UNGATED. No tier change proposed, so nothing here alters what the programme claims.")
sys.exit(0 if n_ok == len(checks) else 1)
