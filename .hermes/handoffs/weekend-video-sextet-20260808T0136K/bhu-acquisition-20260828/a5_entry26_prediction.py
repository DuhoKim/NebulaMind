#!/usr/bin/env python3
"""A5 -- entry 26 (Gaztanaga, Symmetry 14, 1984): is the stated prediction a falsifier?

GATED 2026-08-28 and SUBSTANTIALLY REPAIRED. Verdicts:
    CGATE_A5_VERDICT.md  AUDIT_CONFIRMED_TIER_ONLY / ANTHROPIC: FAIR / PATTERN: TIDY_STORY
    AGATE_A5_VERDICT.md  AUDIT_CONFIRMED_BOTH      / ANTHROPIC: FAIR / PATTERN: REAL

The seats split and I followed CGATE on every contested point, on the merits. AGATE agreed with
my framing almost throughout -- including where it was wrong -- and answered the band question
by asserting the algebra is exact, which nobody disputed. CGATE answered the question actually
asked, by deriving P(Delta) from Equation (11).

WHAT THE GATE FOUND WRONG IN MY FIRST VERSION -- four things, all mine:

 1. I WROTE THAT THE PAPER SUPPLIES NO NUMBER for the galaxy age. It does, and I missed it:
    "tau_O is the astronomical time needed for observers like us to exist. Its value must be
    close to tau_O ~= 13 Gyrs, corresponding to the age of our galaxy". Both seats found it.
    My whole attack-1 worry -- that 13.6 Gyr was MY import -- dissolves: the paper picks 13.

 2. I CONFLATED tau WITH tau_O. tau ~ 11 Gyr is the COLLAPSE TIME of the observed mass.
    tau_O ~ 13 Gyr is the OBSERVER TIME that serves as the model's input. Different quantities;
    I put them in one candidate table.

 3. MY CIRCULARITY CHARGE WAS WRONG and is withdrawn. The paper's intended chain runs
    tau_O -> M_O -> r_S -> Lambda_O, with tau_O supplied externally from the galaxy age:
    "an accurate estimation of tau_O provides a prediction for M_O and therefore a prediction
    for r_S ... and Lambda." That is a genuine predictive direction. My charge came from the
    tau/tau_O conflation in (2).

 4. THE BAND IS NOT AN ALLOWED INTERVAL. Equation (11) gives
    P(Delta) ~ (1+Delta)^(-3/2) Delta exp[-(M_O/M_*) Delta], whose PEAK moves to Delta = 0, 1, 2
    as M_O/M_* varies -- which is exactly the Lambda_O, Lambda_O/4, Lambda_O/9 spread. So the
    band is the ENVELOPE OF THE MODE'S LOCATION over an unspecified parameter, not a credible
    interval. P has support at every Delta > 0. My "allowed window / satisfies / IN / OUT"
    language claimed more than Equation (11) establishes.

WHAT SURVIVES is narrower and still worth having: with the paper's OWN tau_O, the observed
Lambda does not sit at ANY of the modal locations the paper claims. That is an internal-
consistency criticism, not a failed test. Stated that way below.

Pinned source: ../bhu-reading-20260823/sources/sym14101984_clean.txt
"""
import re, sys, hashlib

SRC = "../bhu-reading-20260823/sources/sym14101984_clean.txt"
T = open(SRC).read(); SHA = hashlib.sha256(T.encode()).hexdigest()[:12]
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

c, G, Msun = 2.99792458e8, 6.674e-11, 1.98892e30
GYR = 3.155760e16
KMSMPC_PER_INV_GYR = 977.792

print("=" * 96); print(f"A5 -- entry 26, the stated prediction  [GATED]  [source sha256 {SHA}]"); print("=" * 96)

# ---- 0. the formula, and a control that validates ONLY the unit conversion -----------------
GMsun_c3 = G * Msun / c**3
print(f"\n0. THE FORMULA AND THE UNIT CHAIN, kept separate")
print(f"   Equation (5)/(8): tau_BH = (2/3) r_S, and r_S = 2GM  =>  tau = 4GM/3")
print(f"   both seats verified that from the source; there is no hidden pi or free-fall factor")
print(f"   G*Msun/c^3 = {GMsun_c3*1e6:.4f} us   (textbook 4.9255 us)")
chk("(2/3)*r_S with r_S = 2GM is algebraically 4GM/3", abs((2.0/3.0)*2.0 - 4.0/3.0) < 1e-15,
    "the formula itself, checked as algebra")
chk("the mass->time UNIT conversion reproduces the textbook solar mass in time units",
    abs(GMsun_c3*1e6 - 4.9255) < 0.005,
    "CGATE: this control validates the conversion ONLY, not the formula -- so both are checked")

# ---- 1. the paper's algebra is internally consistent --------------------------------------
tau_sym = 7.0
chk("Lambda_O = 4/(3 tau_O^2) follows exactly from Lambda = 3/r_S^2 and r_S = 3 tau_O/2",
    abs(3.0/(1.5*tau_sym)**2 - 4.0/(3.0*tau_sym**2)) < 1e-12, "the derivation is not where this fails")

# ---- 2. F1: the paper's two stated numbers, at one significant figure ----------------------
M_paper = 6e22
tau_from_M = (4.0/3.0) * GMsun_c3 * M_paper / GYR
print(f"\n2. F1 -- the paper's own M and its own tau are 14% apart")
print(f"   tau = 4GM/3 at M = 6e22 Msun  ->  {tau_from_M:.2f} Gyr;  the paper states ~11 Gyr")
print(f"   M that would give 11 Gyr      ->  {11*GYR*3/(4*GMsun_c3)/1e22:.2f}e22 Msun")
chk("the two stated central values are mutually inconsistent, at a level consistent with ROUNDING",
    abs(tau_from_M - 11.0) > 1.0,
    f"{tau_from_M:.2f} vs 11 Gyr; both are one-significant-figure, so this is a minor internal "
    f"tension and NOT a precision defect -- CGATE required that caveat")

# ---- 3. what the band actually is: the envelope of the MODE -------------------------------
# Equation (11): P(Delta) ~ (1+Delta)^-3/2 * Delta * exp[-(M_O/M_*)Delta], M = M_O(1+Delta).
# Paper: peak at Delta=0 (M_O>>M_*), Delta=1 (M_O~M_*), Delta=2 (M_O<<M_*).
# tau ~ M so tau_mode = tau_O(1+Delta), and Lambda = 4/(3 tau^2) so Lambda_mode = Lambda_O/(1+Delta)^2.
print(f"\n3. THE BAND IS THE ENVELOPE OF THE PEAK, NOT AN ALLOWED INTERVAL  [repaired]")
print(f"   Delta=0 -> Lambda_O    Delta=1 -> Lambda_O/4    Delta=2 -> Lambda_O/9")
print(f"   so 'Lambda_O/9 < Lambda < Lambda_O' spans where the MODE sits as M_O/M_* varies.")
print(f"   Equation (11) has support at every Delta > 0; no credible interval is stated.")
chk("the three peak positions the paper names reproduce the quoted Lambda_O/9 ... Lambda_O span",
    abs(1.0/(1+2)**2 - 1.0/9.0) < 1e-12 and abs(1.0/(1+0)**2 - 1.0) < 1e-12,
    "so the span is a mode envelope over an unspecified M_O/M_*, not a probability interval")

# ---- 4. the surviving finding, stated at the strength the gate allows ----------------------
TAU_O_PAPER = 13.0     # the paper's OWN value, not an import
def H_L_of(tau): return (2.0/3.0)/tau * KMSMPC_PER_INV_GYR      # km/s/Mpc at the Delta-mode
print(f"\n4. WITH THE PAPER'S OWN tau_O = {TAU_O_PAPER:g} Gyr, WHERE DOES THE OBSERVED Lambda SIT?")
print(f"   {'mode':<10} {'tau_mode (Gyr)':>15} {'H_Lambda (km/s/Mpc)':>21}")
modes = []
for D in (0, 1, 2):
    tm = TAU_O_PAPER * (1 + D); modes.append(H_L_of(tm))
    print(f"   Delta={D:<4} {tm:>15.1f} {H_L_of(tm):>21.2f}")
res = {}
for lbl, H0, OL in [("Planck 2018 (67.36, 0.6847)", 67.36, 0.6847), ("the paper's quoted 0.75", 67.36, 0.75)]:
    H_obs = H0 * OL**0.5; res[lbl] = H_obs
    print(f"   observed, {lbl:<30} {H_obs:>21.2f}   -> Lambda_obs/Lambda_O = {(H_obs/modes[0])**2:.3f}")
chk("the observed Lambda lies ABOVE every modal location the paper names, on its own tau_O",
    all(res[k] > modes[0] for k in res),
    f"highest mode (Delta=0) is {modes[0]:.2f} km/s/Mpc; observed is {res['Planck 2018 (67.36, 0.6847)']:.2f}, "
    f"i.e. Lambda_obs = {(res['Planck 2018 (67.36, 0.6847)']/modes[0])**2:.2f} x Lambda_O")

print("""
5. WHAT THIS DOES AND DOES NOT SHOW  [rewritten at CGATE's instruction]

   DOES: on the paper's own tau_O ~ 13 Gyr, the observed Lambda sits ~24% above even the
   Delta=0 peak -- the largest value the modal envelope reaches. So the paper's own input does
   not place our Universe at any of the peak locations its own Equation (11) predicts.
   That is an INTERNAL-CONSISTENCY criticism.

   DOES NOT: show the model is excluded. Equation (11) has support everywhere, so an
   observation off-peak is improbable-by-some-unstated-measure, not forbidden. The earlier
   version of this file called the span an "allowed window" and printed IN/OUT verdicts. That
   was wrong and is withdrawn.

   WITHDRAWN ENTIRELY: the circularity charge. tau_O is an external input from the galaxy age,
   and the chain tau_O -> M_O -> r_S -> Lambda_O is a real predictive direction. I generated
   that charge by conflating tau_O with the collapse time tau of the observed mass.

6. THE ANTHROPIC OBJECTION, restated  [CGATE: FAIR, but my wording was too absolute]

   NOT: "no measurement can refute it."
   BUT: the paper states no quantitative rule by which an observation updates or rejects this
   observer model. It assumes a linear observer factor, leaves M_O/M_* unspecified, discusses
   only where the mode lands, and gives no normalised likelihood, tail probability or rejection
   criterion. Weinberg-style anthropic reasoning IS scientifically informative when it supplies
   a measure, a selection function and a bound. This paper supplies none of the three, so it has
   not delivered a calibrated falsifier -- which is a calibration ruling, not a dismissal of
   anthropic prediction as such.

7. THE ENTRY-21 / ENTRY-26 PATTERN  [demoted -- CGATE: TIDY_STORY, AGATE: REAL]

   Permitted: "both papers lack a completed quantitative bridge to observation."
   NOT permitted: "in each, the author supplies an auxiliary that absorbs any discrepancy."
   The mechanisms are materially different -- an omitted excitation amplitude in Roupas, an
   uncalibrated observer measure here -- and n=2 does not establish a recurring mechanism.
   This lane has demoted a tidy unifying story before, for exactly this reason. I flagged the
   risk in my own brief and then leaned on the claim anyway.

8. VERDICT ON THE TIER  -- unchanged, and the one thing both seats agree on

   NOT a calibrated falsifier. Entry 26 stays QUALITATIVE-DIRECTIONAL; the bibliography's
   existing tier is CONFIRMED.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
sys.exit(0 if n_ok == len(checks) else 1)
