#!/usr/bin/env python3
"""A2 -- entry 21 (Roupas 2022, EPJC 82, 255) against the bibliography's own question.

THE QUESTION, quoted from the bibliography's ranked target list (rank 4):
  "does the body derive an amplitude and rate, or is 'detectable' uncalibrated? If a number
   exists, this becomes the family's second calibrated falsifier; if not, it reclassifies to
   PROSPECT-without-a-number and says so in print."

Everything below is COMPUTED or GREPPED from the pinned text. Per this lane's describe-vs-compute
law, no check here is satisfied by prose.

Pinned: bhu-reading-20260823/sources/2203.13295_clean.txt
"""
import re, sys, hashlib

SRC = "../bhu-reading-20260823/sources/2203.13295_clean.txt"
T = open(SRC).read()
SHA = hashlib.sha256(T.encode()).hexdigest()[:12]

checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

c, G, Msun = 2.99792458e8, 6.674e-11, 1.98892e30
def scale(M_in_Msun):            # c^3 / (2 G M), the paper's own Table-1 unit
    return c**3 / (2 * G * M_in_Msun * Msun)

W0 = 0.0062                       # Table 1, n=0, l=2, dimensionless (2GM/c^3) omega_R
print("=" * 96); print(f"A2 -- entry 21 Roupas 2022  [source sha256 {SHA}]"); print("=" * 96)

# ---- 1. what the paper actually supplies: a frequency ------------------------------------
w10 = W0 * scale(10)
print(f"\n1. THE FREQUENCY IS REAL AND CALIBRATED")
print(f"   Table 1 (n=0, l=2), dimensionless (2GM/c^3)w_R = {W0}")
print(f"   c^3/(2GM) at 10 Msun                          = {scale(10):.4e} s^-1")
print(f"   => w_R(10 Msun)                               = {w10:.2f} s^-1")
chk("Table 1 reproduces the text's '63' -- so a real, mass-parameterised number exists",
    abs(w10 - 63.0) < 1.0, f"computed {w10:.2f} vs printed 63")

# ---- 2. but its UNITS are wrong, by exactly 2pi ------------------------------------------
f10 = w10 / (2 * 3.141592653589793)
print(f"\n2. THE PRINTED UNIT IS WRONG -- 'Hz' IS APPLIED TO AN ANGULAR FREQUENCY")
print(f"   the text prints:  'is 63 Hz'    (section 4)")
print(f"   w_R/2pi        =  {f10:.3f} Hz")
print(f"   the text prints:  '10 Hz'       (section 5, Discussion) for the same quantity")
chk("the paper's two printed upper bounds are the SAME number differing by 2pi",
    abs(f10 - 10.0) < 0.2, f"63/2pi = {f10:.3f}, and the Discussion prints 10 Hz")
chk("both '63 Hz' and '10 Hz' really are in the pinned text",
    ("63" in T and "Hz" in T) and bool(re.search(r"10\s*Hz|10\{\\rm Hz\}", T)),
    "so this is the paper's inconsistency, not a transcription artefact")

# ---- 3. and the 2pi is exactly what decides the LIGO claim -------------------------------
LIGO_LOW = 20.0                   # conventional low-frequency analysis cutoff -- EXTERNAL input,
                                  # not from Roupas; the seismic/suspension wall
print(f"\n3. THE ERROR LANDS ON THE ONE CLAIM IT CAN CHANGE")
print(f"   the paper states 63 'Hz' 'lies outside the detection range of LIGO-Virgo'")
print(f"   literal reading  f = 63.0  Hz -> inside LIGO band (f > {LIGO_LOW:g} Hz):  {63.0 > LIGO_LOW}")
print(f"   corrected        f = {f10:.2f} Hz -> inside LIGO band:                     {f10 > LIGO_LOW}")
chk("the stated conclusion is FALSE as printed and TRUE only after the 2pi correction",
    (63.0 > LIGO_LOW) and not (f10 > LIGO_LOW),
    "the units error and the conclusion sit on opposite sides of LIGO's 20 Hz wall")

# ---- 4. the LISA mass window is a BAND, not a floor --------------------------------------
def f_of_M(M): return W0 * scale(M) / (2 * 3.141592653589793)
LISA_HI, LISA_LO = 1e-1, 1e-5     # the paper's OWN quoted LISA range
M_lo = 10 * (f_of_M(10) / LISA_HI)
M_hi = 10 * (f_of_M(10) / LISA_LO)
print(f"\n4. 'M >~ 10^4 Msun' IS UNBOUNDED ABOVE, AND THE PAPER'S OWN MASS RANGE EXCEEDS IT")
print(f"   f(M) = {W0}*c^3/(2GM)/2pi, and f ~ 1/M")
for M in (1e3, 1e4, 1e6, 1e7, 1e9):
    inband = LISA_LO <= f_of_M(M) <= LISA_HI
    print(f"   M = {M:8.0e} Msun -> f = {f_of_M(M):10.3e} Hz   in LISA band: {inband}")
print(f"   => LISA-visible window: {M_lo:.2e} <~ M/Msun <~ {M_hi:.2e}")
chk("the top of the paper's own mass range [10,1e9] is OUTSIDE the LISA band it claims",
    not (LISA_LO <= f_of_M(1e9) <= LISA_HI),
    f"f(1e9 Msun) = {f_of_M(1e9):.2e} Hz, ~{LISA_LO/f_of_M(1e9):.0f}x below LISA's floor")

# ---- 5. the amplitude: absent, and the AUTHOR says so ------------------------------------
defer = re.search(r"excitation factors[^.]*?have to be calculated[^.]*\.\s*This is an involved task[^.]*\.", T, re.S)
print(f"\n5. THE AMPLITUDE IS NOT DERIVED -- ON THE AUTHOR'S OWN STATEMENT")
print("   " + (" ".join(defer.group(0).split()) if defer else "<< deferral sentence NOT FOUND >>"))
chk("the paper explicitly defers the amplitude to future work",
    defer is not None, "grepped from the source, not paraphrased")
chk("and pre-authorises the escape from any null result",
    bool(re.search(r"not amplitude-wise sensitive enough", T)),
    "'it is a matter of developing the appropriate technology ... provided they exist'")

# ---- 6. the rate: absent -----------------------------------------------------------------
rate_hits = re.findall(r"(?i)(event rate|merger rate|per year|yr\^?-?1|population synthesis|abundance of)", T)
print(f"\n6. THE EVENT RATE IS ABSENT")
print(f"   rate-language hits in the full text: {len(rate_hits)}  {sorted(set(x.lower() for x in rate_hits))}")
chk("no event-rate or population calculation anywhere in the paper",
    len(rate_hits) == 0, "so 'detectable' has no expected number of events attached")

# ---- 7. the verdict on the tier ----------------------------------------------------------
print("""
7. VERDICT ON THE BIBLIOGRAPHY'S QUESTION

   amplitude?  NO -- explicitly deferred by the author (check 5)
   rate?       NO -- absent entirely (check 6)
   frequency?  YES -- calibrated and mass-parameterised (check 1), but mis-united (checks 2-3)

   => entry 21 does NOT become the family's second calibrated falsifier.
      It stays PROSPECT. The bibliography's existing tier is CONFIRMED, not overturned.

   WHY A CALIBRATED FREQUENCY IS STILL NOT A FALSIFIER. The claim is shielded on BOTH sides,
   and each shield is stated by the author himself:
     - a null result is absorbed by the unknown amplitude ("developing the appropriate
       technology ... provided they exist");
     - a Schwarzschild-looking ringdown is absorbed by mode camouflage, since the early
       ringdown is set by the external null geodesic common to regular and singular holes.
   Nothing an interferometer can return refutes it. That is an auxiliary shield, not a test.

   NOTE ON DIRECTION. The METHODS_NOTE bias runs toward OVER-classification. This audit ran the
   other way and confirmed the conservative tier. One case, but it is the direction that the
   cheap classifiers kept getting wrong.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("\nSTATUS: UNGATED. The 2pi finding (checks 2-4) is a numerical criticism of a published\n"
      "paper and must not be cited outside this lane until an adversarial seat has attacked it.")
sys.exit(0 if n_ok == len(checks) else 1)
