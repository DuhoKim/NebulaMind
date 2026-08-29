#!/usr/bin/env python3
"""B17 -- entry 44 audited.  The sweep's standing hunt: is it tiered TOO WEAK?

Entry 44 (Pourhasan, Afshordi & Mann 2014, JCAP 04 005) sits at QUALITATIVE-DIRECTIONAL and had
been read once, for one sentence. It surfaced this evening as a real sweep candidate. Source
already pinned: 1309.1487_clean.txt.

THE HUNT, unchanged from the overnight sweep: an entry tiered too weak, concealing a number and a
threshold. Six such candidates were tested overnight and every one turned out to carry a number
BORROWED from the data it was checked against, placed beyond observability, or holding a free
parameter. Entry 44 is the seventh, and it is the most convincing-looking yet.
"""
import re, sys
T=" ".join(open("../bhu-reading-20260823/sources/1309.1487_clean.txt").read().split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B17 -- entry 44: is there a concealed calibrated falsifier?"); print("="*98)

print("\n1. THE CANDIDATE -- and it looks the part")
print("   Eq. (4.14):  T_b / M_5 = 0.17139 +/- 0.00077     at k ~ 0.05 Mpc^-1")
print("   four significant figures, an explicit error bar, 0.45% precision.")
chk("SOURCE: the paper carries a four-significant-figure value with an error bar, which is exactly "
    "the shape a concealed calibrated falsifier would have",
    "0.17139" in T and "0.00077" in T,
    "if the hunt were run by pattern rather than by reading, this is the entry it would promote")

print("\n2. WHAT IT ACTUALLY IS -- the paper's own word for it")
chk("SOURCE: the paper introduces that number as an EXPERIMENTAL CONSTRAINT obtained by comparing "
    "its own equations, not as a prediction confronted with data",
    "gives the experimental constraint on the (effective) temperature" in T,
    "'Comparing Eq. (4.13) with Eq. (4.3) gives the experimental constraint on the (effective) "
    "temperature of the atmosphere: T_b/M_5 = 0.17139 +/- 0.00077'. The precision is the precision "
    "OF THE OBSERVED AMPLITUDE, propagated inward. It is a fitted parameter wearing four "
    "significant figures -- the seventh instance of the borrowed-number pattern, and the first "
    "to reach four figures")

print("\n3. THE PAPER'S TESTABLE CONTENT WAS TESTED. IT FAILED. THE AUTHORS SAY SO.")
chk("SOURCE: the authors state their own model is already ruled out by observation at >5 sigma, "
    "because it predicts no deviation from scale-invariance",
    "is already ruled out by cosmological observations at" in T and
    "does not predict any deviations from scale-invariance" in T,
    "'the simple model of cosmological perturbations, developed in Sec. 4 is already ruled out by "
    "cosmological observations at >5 sigma level, as it does not predict any deviations from "
    "scale-invariance.' Receipted against Planck in b16: 8 sigma, 9 with BAO")

print("\n4. AND THE REPAIR IS NOT COMPUTED -- the 4% is read off the observation")
chk("SOURCE: the proposed fix is offered as something easy to IMAGINE, at a size taken from the "
    "measurement it must reproduce",
    "it is easy to imagine small corrections that could lead to a" in T,
    "'it is easy to imagine small corrections that could lead to a ~4% deviation from "
    "scale-invariance'. The observed tilt IS ~4% (1 - 0.9649 = 0.035). The number is the target, "
    "not a consequence")
chk("SOURCE: and the calculation that would turn the gesture into a prediction is explicitly "
    "deferred by the authors",
    "defer a consistent inclusion of gravitational backreaction" in T,
    "'We defer a consistent inclusion of gravitational backreaction on the 5d thermal power "
    "spectrum (which should account for the impact of Jeans instability) to a future study.' Same "
    "structure as entry 21's uncomputed amplitude and entry 26's typicality without a threshold")

print("\n5. THE ABSENCE CLAIM, stated to the lane's standard")
verbs={w:len(re.findall(w,T,re.I)) for w in ["predict","we find","observable","testab","falsif"]}
print(f"   predictive-verb counts: {verbs}")
print("""   PATTERN USED: predictive verbs above, plus numeric-with-error-bar constructs, read in
     context rather than counted.
   ONE CLASS IT WOULD MISS: a prediction stated as a bare inequality or scaling relation, with no
     verb and no error bar.
   WHAT WAS DONE ABOUT THAT CLASS: the paper contains exactly such a construct -- Eq. (4.15),
     H/2pi <~ T_b ~= 0.17 M_5 -- and it was read directly rather than left to the pattern. It
     relates the Hubble rate to a bulk temperature in units of the 5D Planck mass. NEITHER T_b NOR
     M_5 IS INDEPENDENTLY MEASURED, so the inequality cannot be confronted with anything. It is an
     internal consistency condition, not an observable.""")
chk("SOURCE: the one bare-inequality construct in the paper is expressed in quantities the paper "
    "itself does not tie to an independent measurement",
    "\\lesssim T_{b}\\simeq 0.17~M_{5}" in T or "T_{b}\\simeq 0.17" in T,
    "Eq. (4.15). M_5 is the 5D Planck mass, a model parameter; T_b is fixed only through the "
    "fitted 4.14. The inequality closes on itself")

print("""
6. VERDICT

   TIER CONFIRMED: QUALITATIVE-DIRECTIONAL. No change is proposed and none would be defensible.

   BUT THE ENTRY UNDERSTATES WHAT IT IS. Our record says the paper shows "rare self-honesty" in
   conceding its base model is ruled out. That is true and it is not the whole thing. THE PAPER
   IS A MODEL THAT MADE A REAL PREDICTION, HAD IT TESTED AGAINST REAL DATA, AND LOST. Exact
   scale-invariance is a genuine falsifiable claim; Planck falsified it at 8 sigma. Almost nothing
   else in this corpus has been through that.

   WHAT SURVIVES IS PROMISSORY. A ~4% correction sized to the measurement it must reproduce, a
   direction (graviton polarizations unfreezing in the IR, cascading gravity), and a deferred
   calculation. So the entry is directional going forward and refuted looking back, and those are
   two different facts that the single tier label cannot carry.

   THE SEVENTH BORROWED NUMBER. 0.17139 +/- 0.00077 is the most precise-looking value the sweep
   has turned up and it is a fit. That the hunt keeps finding this same shape across four author
   lines is now the sweep's most repeatable result -- more repeatable than any tier change, of
   which there have been none.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
