#!/usr/bin/env python3
"""A10 -- entry 23 (Gaztanaga 2020, MNRAS 494, 2766, "The size of our causal Universe").

GATED 2026-08-29. BOTH SEATS REFUSED THE PROMOTION.
    CGATE_A10_VERDICT.md  HOLD_UNCALIBRATED_CUTOFF   RIGID: YES | DERIVED: YES | MATCHES: CONTESTED
    AGATE_A10_VERDICT.md  PROMOTE_REFUTED_ATTACK_5   RIGID: NO  | DERIVED: NO  | MATCHES: CONTESTED

THE KILL, AND I HANDED IT TO THEM AS ATTACK 5 WITHOUT SEEING IT MYSELF. I quoted "we roughly
estimate theta_S ~= 60 +/- 3 deg" and stopped at "deg." The sentence continues:

    "We can also PREDICT Omega_Lambda FROM the lack of CMB correlations. From Fig.3 we roughly
     estimate theta_S ~= 60 +/- 3 deg. TO FIND (using Eq.22) Omega_Lambda = 0.7 +/- 0.1."

The +/-3 is READ OFF THE OBSERVED CMB CURVE and used as an INPUT to infer Omega_Lambda. It is not
a propagated forward uncertainty on a prediction. My check 2 -- "the prediction carries a stated
uncertainty" -- was simply wrong about which inference that uncertainty belongs to.

THIS IS THE THIRD TIME TONIGHT. A6: I quoted the w != -1 sentence four times and missed "not
solely" inside it. A7: I cited "no defects or discontinuities" and missed three sentences on the
same pages saying the junction is null, degenerate and non-comoving. Now A10: I stopped one clause
early again. That is a systematic reading failure of mine, not three separate slips: I stop at the
phrase that supports the claim I am forming.

WHAT SURVIVES, and CGATE is careful to preserve it: the FORWARD chain is real. Eq.19 gives
rho_Lambda = rho_S, Eq.22 maps the measured density to chi_S = (3.149 +/- 0.006) c/H_0 from
Omega_Lambda = 0.69 +/- 0.01, and theta_S = chi_S/chi_CMB follows. So the ~60 deg IS derived from
a measured quantity. What is absent is a CALIBRATION -- no propagated angular uncertainty, no
likelihood, no confidence level. A derived direction without a calibrated threshold is exactly
QUALITATIVE-DIRECTIONAL, which is where the entry already sits.

Tiered QUALITATIVE-DIRECTIONAL. TIER CONFIRMED -- and for a sharper reason than the bibliography
gave: not "the scale is fitted from the anomalies" (the derivation is sound), but "the error bar
is borrowed from the anomaly it is checked against".

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
# REPAIRED: the +/-3 belongs to the REVERSE inference. Test the direction, not the presence.
reverse = "We can also predict" in T and "to find (using Eq.22)" in T.replace("Eq.22","Eq.22")
fwd_err = re.search(r"θ§\s*=\s*[0-9.]+\s*±", T) is not None
print(f"   direction: 'predict Omega_Lambda FROM the lack of CMB correlations' .. {reverse}")
print(f"   any propagated FORWARD uncertainty on theta_S ................. {fwd_err}")
chk("the +/-3 is an OBSERVATIONAL read-off feeding the reverse inference, not a forward "
    "prediction uncertainty -- so the claim is NOT calibrated",
    reverse and not fwd_err,
    "my original check tested that an uncertainty EXISTS; it never tested which inference "
    "it belonged to, and both seats killed the promotion on exactly that")

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
6. FURTHER QUALIFICATIONS CGATE FOUND THAT I HAD NOT

   "As we dont know the values of a_i or rho(t_i) it seems impossible to estimate how large
    chi_S is from current observations or first principles."
   "this rough estimate does not take into account the foreground (late) ISW and lensing
    effects ... This requires further investigation."
   the CMB-inferred boundary "might be slightly different to the value near us", and such
    differences are "impossible to quantify ... without a model for the initial conditions".
   "More work is needed to account for the late ISW and lensing and to interpret the CMB
    measurements with a metric that is not homogeneous."

   Five hedges, none of which I found. I reported two.

7. MATCHES: CONTESTED -- and the reason is circular in a way I missed

   Both seats agree the large-angle correlation deficit is real in COBE/WMAP/Planck but is not a
   cleanly established cutoff at 60 +/- 3 deg. CGATE's decisive point: the S_1/2 statistic ITSELF
   integrates above 60 degrees, and that boundary was chosen a posteriori. So "matches the
   anomaly at 60 deg" is partly matching a number the anomaly literature also chose after the
   fact. Using it to manufacture a calibration is circular.

8. THE SPLIT, RECORDED

   RIGID and DERIVED: CGATE says YES to both, AGATE says NO to both. CGATE is the more careful
   reading and I follow it: the paper DOES contain the forward chain (Eq.19 -> Eq.22 -> chi_S =
   3.149 +/- 0.006 c/H_0), so the direction of inference is genuinely Omega_Lambda -> theta_S.
   AGATE's NO overstates -- it collapses "the error bar runs backwards" into "the whole
   derivation runs backwards", and those are different failures. The promotion dies either way.

9. WHY THIS IS UNLIKE ENTRIES 21, 25 AND 26

   Each of those supplied a real number that could not fail, because the author also supplied the
   auxiliary that absorbs a discrepancy: an uncomputed excitation amplitude (21), "not solely
   caused by" (25), observer typicality with no rejection rule (26).

   Here the chain is Omega_Lambda -> chi_S -> theta_S = 60 +/- 3 deg, and I have not found a free
   parameter in it. That is the claim the gate should attack hardest, because it is exactly the
   claim I got wrong at A6.

10. OUTCOME

   NO PROMOTION. entry 23 stays QUALITATIVE-DIRECTIONAL, confirmed by both seats.
   Eighth entry, eighth tier unchanged. Second promotion candidate, second refusal.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("\nSTATUS: GATED. Promotion REFUSED by both seats. Tier unchanged.")
sys.exit(0 if n_ok == len(checks) else 1)
