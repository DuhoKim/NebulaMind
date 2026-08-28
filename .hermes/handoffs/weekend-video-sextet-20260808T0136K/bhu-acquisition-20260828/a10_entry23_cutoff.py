#!/usr/bin/env python3
"""A10 -- entry 23 (Gaztanaga 2020, MNRAS 494, 2766, "The size of our causal Universe").

Tiered QUALITATIVE-DIRECTIONAL. I think that is TOO WEAK, and unlike the entry-25 attempt this
one is not built on a single sentence.

THE PREDICTION, with the author's own verb and his own error bar:

    "It also predicts that CMB temperature should not be correlated above theta > theta_S ~= 60 deg."
    "...we roughly estimate theta_S ~= 60 +/- 3 deg."

Named observable (the CMB two-point correlation cutoff angle), a value, AND an uncertainty.

WHY THE BIBLIOGRAPHY'S OBJECTION DOES NOT BITE. The ranked-target note warns of "the post-hoc-
fitting risk stated up front: the scale is fitted from the anomalies it explains." That is the
right question and the answer appears to be no: the causal scale is fixed by the MEASURED
Omega_Lambda ("for Omega_Lambda = Omega_S ~= 0.7"), and the angular scale then FOLLOWS as
theta_S = chi_S / chi_CMB. One observable in, a DIFFERENT observable out. That is a derivation,
not a fit.

WHAT I AM WATCHING FOR, having been burned at A6 where I promoted on a sentence and missed the
word "not solely" inside it: the hedge here is "roughly estimate", and the anomaly is a
POSTDICTION -- the missing large-angle CMB correlations were known long before 2020. Both are
recorded below rather than argued away.

NO TIER CHANGE IS APPLIED. Per the overnight rule a tier change is a CHOICE; the question goes to
OPEN_QUESTIONS_FOR_DUHO.md and to two gate seats.

Pinned: ../bhu-reading-20260823/sources/2003.11544_clean.txt
"""
import re, sys, hashlib

S = "../bhu-reading-20260823/sources/2003.11544_clean.txt"
T = " ".join(open(S).read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print(f"A10 -- entry 23  [sha256 {hashlib.sha256(open(S,'rb').read()).hexdigest()[:12]}]"); print("=" * 96)

# ---- 1. the author calls it a prediction, in his own verb ---------------------------------
pred = re.search(r"It also predicts that CMB temperature should not be correlated above[^.]*", T)
print(f"\n1. THE AUTHOR'S OWN VERB")
print("   " + (" ".join(pred.group(0).split())[:190] if pred else "<< not found >>"))
chk("entry 23 states a PREDICTION about an observable, in the author's own word",
    pred is not None, "'predicts', not 'is consistent with' -- the distinction that separates the tiers")

# ---- 2. and it carries an uncertainty, which is what makes it CALIBRATED -------------------
err = re.search(r"roughly estimate\s*θ§?\s*≃?\s*60\s*±\s*3", T) or ("60\\pm 3" in T) or ("60±3" in T.replace(" ",""))
print(f"\n2. IT HAS AN ERROR BAR")
print(f"   'we roughly estimate theta_S ~= 60 +/- 3 deg'  present: {bool(err)}")
chk("the prediction carries a stated uncertainty, not just a round number",
    bool(err),
    "60 +/- 3 deg is ~5% -- tight enough that a measured cutoff at 30 or 90 deg would fail it")

# ---- 3. WHICH WAY DOES THE DERIVATION RUN? the bibliography's post-hoc worry ---------------
chain = "θ§≡χ§χC​M​B" in T.replace(" ","") or "\\frac{\\chi_{\\lx@sectionsign}}{\\chi_{CMB}}" in T
from_ol = re.search(r"for\s*ΩΛ\s*=\s*Ω§\s*≃?\s*0", T) is not None or "for \\Omega_\\Lambda=\\Omega" in T
print(f"\n3. IS THE SCALE FITTED FROM THE ANOMALY, OR DERIVED FROM Omega_Lambda?")
print(f"   angular scale defined as theta_S = chi_S / chi_CMB ......... {chain}")
print(f"   evaluated 'for Omega_Lambda = Omega_S ~= 0.7' .............. {from_ol}")
chk("the causal scale is set by the MEASURED Omega_Lambda and the angle follows -- one "
    "observable in, a different observable out",
    chain and from_ol,
    "so the bibliography's post-hoc-fitting worry is not borne out for the DERIVATION; the "
    "anomaly is an independent check, not the input")

# ---- 4. hunt the qualification -- the A6 discipline, applied to a promotion ----------------
hedge_rough = "roughly estimate" in T
hedge_assum = "assuming that the causal scale is smaller than the observable Universe today" in T
print(f"\n4. THE QUALIFICATIONS, RECORDED RATHER THAN ARGUED AWAY")
print(f"   'we ROUGHLY estimate' ........................................ {hedge_rough}")
print(f"   the whole result is conditional on 'ASSUMING that the causal")
print(f"   scale is smaller than the observable Universe today' .......... {hedge_assum}")
chk("both hedges are present and are recorded here, not suppressed",
    hedge_rough and hedge_assum,
    "at the A6 gate I promoted on a sentence and missed the qualifier inside it; these are the "
    "qualifiers here and they are weaker -- an estimate's precision, and a stated premise")

# ---- 5. postdiction, not novel prediction --------------------------------------------------
observed = "anomalous lack of correlations observed in the CMB" in T
print(f"\n5. IS IT A NOVEL PREDICTION OR A POSTDICTION?")
print(f"   the paper describes the anomaly as already OBSERVED ......... {observed}")
chk("the CMB large-angle correlation anomaly predates the paper, so this is a POSTDICTION",
    observed,
    "that lowers its evidential weight but NOT its falsifiability -- the two are different "
    "questions and this lane has demoted a claim once for conflating them")

print("""
6. WHY THIS IS UNLIKE ENTRIES 21, 25 AND 26

   Each of those supplied a real number that could not fail, because the author also supplied the
   auxiliary that absorbs a discrepancy: an uncomputed excitation amplitude (21), "not solely
   caused by" (25), observer typicality with no rejection rule (26).

   Here the chain is Omega_Lambda -> chi_S -> theta_S = 60 +/- 3 deg, and I have not found a free
   parameter in it. That is the claim the gate should attack hardest, because it is exactly the
   claim I got wrong at A6.

7. PROPOSED, NOT APPLIED -- this is a CHOICE, so it goes to the file and to the seats

   entry 23:  QUALITATIVE-DIRECTIONAL  ->  CALIBRATED-FALSIFIER

   Eighth entry of the sweep and the second promotion candidate. The first was refused.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("\nSTATUS: UNGATED, and NO TIER CHANGE APPLIED.")
sys.exit(0 if n_ok == len(checks) else 1)
