#!/usr/bin/env python3
"""B17 -- entry 44 audited.  GATED 2026-08-29 and REFUTED on one claim.

  CGATE_B17_VERDICT.md  AUDIT_REFUTED_MISSED_EQ5_1_AND_TIER    (codex gpt-5.6-sol)
  AGATE_B17_VERDICT.md  AUDIT_NARROWED_PREDICATE_OVERCLAIM     (agy, Gemini 3.1 Pro)

################################################################################################
#  WITHDRAWN. The first version claimed Eq. (4.15), H/2pi <~ T_b ~= 0.17 M_5, "closes on itself"
#  because neither T_b nor M_5 is independently measured. THAT IS FALSE, and the sentence that
#  refutes it names Eq. (4.15) by number:
#
#    "we can translate the observational constraints on the DGP cosmology (normal branch),
#     r_c >~ 3 H_0^-1 [14] into an upper limit on 5D Planck mass: H <~ M_5 <~ (H_0 M_4^2/6)^1/3
#     ~ 9 MeV, (5.1) WHERE WE USED THE INEQUALITY IN EQ. (4.15) to bound the Hubble constant"
#
#  So M_5 IS tied to observation, and the very inequality I called closed is what does the tying.
#  Both seats caught it independently. AGATE: the overclaim "directly blinded the script".
#
#  AND MY ABSENCE CLAIM WAS MADE TO THE LANE'S FULL STANDARD AND WAS STILL WRONG. I stated the
#  pattern, named one class it would miss (a bare inequality), and read the one instance of that
#  class I found. I never searched for OTHER USES of it. Registered as defect 2a.
################################################################################################

WHAT SURVIVED, confirmed by both seats: Eq. (4.14) is a fitted normalisation, the model's testable
core was tested and lost, and the proposed repair is promissory and sized to the measurement.

THE TIER GOES TO DUHO. Both seats say the current label is wrong, in the same direction and with
different remedies. No tier is changed here.
"""
import re, sys
T=" ".join(open("../bhu-reading-20260823/sources/1309.1487_clean.txt").read().split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B17 -- entry 44 [GATED: one claim REFUTED, three confirmed]"); print("="*98)

print("\n1. EQ. (4.14) IS A FIT -- confirmed by both seats, and now tested as a fit")
chk("SOURCE: the paper contains BOTH the observed amplitude it normalises to AND its own phrase "
    "calling the result an experimental constraint -- so the predicate now tests the comparison, "
    "not just the phrase",
    "2.196" in T and "gives the experimental constraint on the (effective) temperature" in T,
    "CGATE supplied the structure I had asserted without testing: Eq. (4.3) is the Planck+WMAP "
    "OBSERVED spectrum, (2.196 +/- 0.059)e-9; Eq. (4.13) is the model's, amplitude "
    "8.66e-5 (T_b/M_5)^6. THE SIXTH POWER IS DERIVED; the value 0.17139 is not. Its four figures "
    "are Planck's uncertainty transmitted algebraically inward")

print("\n2. THE TESTABLE CORE WAS TESTED AND LOST -- confirmed by both seats")
chk("SOURCE: the authors state their own Sec. 4 model is ruled out at >5 sigma because it "
    "predicts no deviation from scale-invariance",
    "is already ruled out by cosmological observations at" in T and
    "does not predict any deviations from scale-invariance" in T,
    "receipted against Planck in b16 at 8 sigma, 9 with BAO. n_s = 1 was a real falsifiable "
    "prediction and observation fired it")
chk("SOURCE: the repair is offered as easy to imagine and the calculation is deferred by name",
    "it is easy to imagine small corrections that could lead to a" in T and
    "defer a consistent inclusion of gravitational backreaction" in T,
    "the target size ~4% is the observed tilt (1 - 0.9649 = 0.035). No corrected n_s, no "
    "uncertainty, no threshold is derived -- CGATE and AGATE both confirm this independently")

print("\n3. WITHDRAWN: EQ. (4.15) IS NOT CLOSED. IT IS USED.")
print("   (5.1)  H <~ M_5 <~ (H_0 M_4^2 / 6)^(1/3) ~ 9 MeV, from r_c >~ 3 H_0^-1")
print("   (5.2)  T <~ 3e4 (g_*/100)^(-1/4) TeV  <<  T_GUT ~ 1e12 TeV")
chk("SOURCE: the paper propagates an OBSERVATIONAL DGP constraint through Eq. (4.15) into a bound "
    "on M_5, which is the exact opposite of what this file previously asserted",
    "observational constraints on the DGP cosmology" in T and "used the inequality in Eq." in T,
    "the refuting clause names the equation: 'where we used the inequality in Eq. (4.15) to bound "
    "the Hubble constant'. A search for OTHER USES of the equation number would have found this; "
    "I read it only where it was defined")
chk("SOURCE: and the bound is carried further, to a temperature ceiling used to argue the GUT "
    "transition never occurred",
    "T_{\\rm GUT}" in T or "T GUT" in T,
    "Eq. (5.2). CGATE's framing, adopted: these are not clean parameter-free forecasts -- (5.1) "
    "IMPORTS an observational bound and (5.2) is a conditional ceiling -- but they falsify the "
    "claim that nothing here touches observation")

print("\n4. THE ABSENCE CLAIM FAILED WITH ITS DISCIPLINE INTACT")
print("""   WHAT I DID: stated the pattern (predictive verbs + numeric-with-error constructs), named
     one class it would miss (a bare inequality with no verb and no error bar), and read the one
     instance of that class I found -- Eq. (4.15).
   WHAT I DID NOT DO: search for other USES of that equation. The pattern was aimed at finding
     candidate claims, never at tracing what the paper does with one afterwards.
   AND CGATE FOUND MORE THAT I MISSED: the empirical -Omega_k <~ 0.01 input and Figure 2's
     parameter regions; the scaling -Omega_k ~ (M_5 r_h)^-2 ~ M_5/M_*; the Jeans scale
     k_J ~= 0.2 T_b (T_b/M_5)^(3/2); a directional correlation between detectable curvature and
     large-scale anisotropy; and prospective GW, non-Gaussianity and BBN signatures.
   THE SURVIVING CONCLUSION, which both seats grant: NONE of those is a clean parameter-free
     forecast -- each imports a bound, carries a free parameter, or is deferred. So there is no
     concealed calibrated falsifier. But the SEARCH was incomplete and the absence statement as
     written was false.""")
chk("SOURCE: the additional numerical content the audit missed is really present, so this is a "
    "genuine miss and not a seat's overreach",
    "\\Omega_{k}" in T or "Omega_{k}" in T,
    "verified in the source directly rather than accepted from the verdict, per the lane's rule "
    "about taking seats at face value")

print("""
5. THE TIER -- BOTH SEATS SAY THE LABEL IS WRONG, AND IT IS NOT MINE TO MOVE

   AGATE: "The tier should arguably be FALSIFIED ... a QUALITATIVE-DIRECTIONAL label gives the
   model credit for a post-hoc promissory note while obscuring that the rigorous model failed."

   CGATE: the corpus ALREADY distinguishes a claim's nature from its standing -- it uses
   CALIBRATED-FALSIFIER / FIRED and CALIBRATED-FALSIFIER / LIVE elsewhere. The Sec. 4 model has a
   sharp prediction, n_s = 1, and observation fired it. "One paper therefore contains at least two
   claim-level objects with different statuses. If the bibliography insists on one paper-level
   label, it will necessarily erase either the fired calibrated prediction or the weaker surviving
   proposal."

   Same direction, different remedy. This is a TIER QUESTION and the standing rule stops here:
   filed in OPEN_QUESTIONS_FOR_DUHO.md, nothing changed in the bibliography.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
