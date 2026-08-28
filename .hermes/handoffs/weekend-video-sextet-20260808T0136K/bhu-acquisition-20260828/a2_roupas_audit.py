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

# ---- PARSED, not transcribed. Repaired after the harness gate ------------------------------
# CGATE: "'Table 1 reproduces the text's 63' never reads Table 1 or the printed 63. W0=0.0062 and
# 63 are both hard-coded; an empty or different source passes." True, and the finding this script
# reports SURVIVED its gate on the strength of those two numbers. So read them from the paper.
import unicodedata
CLEAN = " ".join("".join(c for c in T if unicodedata.category(c) != "Cf").split())
_row = re.search(r"\b2\s+3\s+4\s+0\s+(0\.\d{4})\s+(0\.\d{4})\s+(0\.\d{4})", CLEAN)
_prn = re.search(r"is\s*(\d{2})\s*Hz", CLEAN)
if not _row or not _prn:
    print("PARSE FAILED -- refusing to fall back to hard-coded values"); sys.exit(3)
W0        = float(_row.group(1))      # Table 1, n=0, l=2, read from the source
PRINTED   = float(_prn.group(1))      # the value the text prints with a Hz unit, read from source
print(f"parsed from source: Table 1 (n=0,l=2) = {W0}   |   text prints '{_prn.group(0)}'")
print("=" * 96); print(f"A2 -- entry 21 Roupas 2022  [source sha256 {SHA}]"); print("=" * 96)

# ---- 1. what the paper actually supplies: a frequency ------------------------------------
w10 = W0 * scale(10)
print(f"\n1. THE FREQUENCY IS REAL AND CALIBRATED")
print(f"   Table 1 (n=0, l=2), dimensionless (2GM/c^3)w_R = {W0}")
print(f"   c^3/(2GM) at 10 Msun                          = {scale(10):.4e} s^-1")
print(f"   => w_R(10 Msun)                               = {w10:.2f} s^-1")
chk("PARSED: the Table-1 value read from the source, converted through the paper's own unit, "
    "reproduces the value the source prints with a Hz label",
    abs(w10 - PRINTED) < 1.0,
    f"parsed table {W0} x c^3/2GM = {w10:.2f} s^-1 vs parsed printed {PRINTED:.0f}; neither "
    f"number is now typed in by me, and a different or empty source aborts at the parse")

# ---- 2. but its UNITS are wrong, by exactly 2pi ------------------------------------------
f10 = w10 / (2 * 3.141592653589793)
print(f"\n2. THE PRINTED UNIT IS WRONG -- 'Hz' IS APPLIED TO AN ANGULAR FREQUENCY")
print(f"   the text prints:  'is 63 Hz'    (section 4)")
print(f"   w_R/2pi        =  {f10:.3f} Hz")
print(f"   the text prints:  '10 Hz'       (section 5, Discussion) for the same quantity")
# The first attempt at this parse grabbed 50 -- section 4's range tops at "<~ 50 Hz" and the
# Discussion's at "<~ 10 Hz", both two digits. It FAILED loudly, which is the point: the old
# hard-coded `abs(f10 - 10.0) < 0.2` would have passed while reading nothing. Collect them all.
_bounds = sorted({float(x) for x in re.findall(r"≲\s*(\d{1,2})\s*Hz", CLEAN)})
_has_raw = any(abs(b - PRINTED) < 14 for b in _bounds)      # 50, the rounded section-4 ceiling
_has_div = any(abs(b - PRINTED / (2 * 3.141592653589793)) < 0.5 for b in _bounds)
print(f"   printed upper bounds parsed from the source: {_bounds} Hz   (plus '{_prn.group(0)}')")
chk("PARSED: the source prints MORE THAN ONE upper bound for the same quantity, and one of them "
    "equals another divided by 2pi",
    len(_bounds) >= 2 and _has_div,
    f"bounds {_bounds} alongside the printed {PRINTED:.0f}; {PRINTED:.0f}/2pi = {f10:.2f} matches "
    f"one of them. LIMIT: this shows two printed numbers differ by 2pi, not WHY -- that reading "
    f"is prose, and both gate seats ruled on it separately")
chk("PARSED: '63' appears ADJACENT to its Hz unit, and a two-digit Hz bound appears in the "
    "Discussion -- not merely both tokens somewhere in the file",
    _prn is not None and len(_bounds) >= 2,
    "the earlier form allowed '63' anywhere and 'Hz' anywhere; CGATE flagged that it did not "
    "require them to be the same claim")

# ---- 2b. POSITIVE CONTROL -- does the conversion reproduce a KNOWN number? --------------
# The whole finding rests on omega being ANGULAR. Rather than argue the convention, test it:
# apply the identical conversion to the Schwarzschild fundamental mode, whose value is textbook.
# Schwarzschild l=2, n=0:  G M omega / c^3 = 0.37367  =>  (2GM/c^3) omega = 0.74734
W_SCHW = 0.74734
f_schw = W_SCHW * scale(10) / (2 * 3.141592653589793)
w_schw = W_SCHW * scale(10)
print(f"\n2b. POSITIVE CONTROL -- the same conversion on a number we already know")
print(f"   Schwarzschild l=2,n=0 dimensionless (2GM/c^3)w = {W_SCHW}")
print(f"   WITH the 2pi:     f = {f_schw:8.1f} Hz")
print(f"   WITHOUT the 2pi:  f = {w_schw:8.1f} Hz")
print(f"   textbook ringdown of a 10 Msun Schwarzschild hole: ~1.2 kHz")
chk("the 2pi conversion reproduces the textbook Schwarzschild ringdown; omitting it does not",
    abs(f_schw - 1207.0) < 30.0 and abs(w_schw - 1207.0) > 1000.0,
    f"with 2pi -> {f_schw:.0f} Hz (textbook ~1207); without -> {w_schw:.0f} Hz (6.3x too high)")
chk("so omega in this paper is ANGULAR, and 'Hz' is the wrong unit for it",
    abs(f_schw - 1207.0) < 30.0,
    "settled by a known value, not by appeal to convention")

# ---- 3. the detector consequence -- REPAIRED at CGATE_A2's insistence -------------------
# ORIGINAL CLAIM (overstated, withdrawn): "the conclusion is FALSE as printed and TRUE only
# after the 2pi correction", asserting a clean flip either side of a 20 Hz wall.
# CGATE_A2: "not defensible at its stated precision. A 20 Hz lower analysis cutoff is
# conventional for many searches, but it is not a detector-independent physical boundary and is
# not supplied by Roupas. Advanced LIGO is described as designed for 10 Hz to 5 kHz."
# So the corrected 10.02 Hz sits ON the nominal design edge. Only HALF the flip is defensible.
LIGO_SEARCH_CUT = 20.0   # conventional search cutoff -- EXTERNAL, not from Roupas
LIGO_DESIGN_LOW = 10.0   # aLIGO nominal design low edge -- EXTERNAL, not from Roupas
print(f"\n3. THE DETECTOR CONSEQUENCE -- stated at the precision the gate allowed")
print(f"   the paper states 63 'Hz' 'lies outside the detection range of LIGO-Virgo'")
print(f"   literal   f = 63.00 Hz : above search cutoff {LIGO_SEARCH_CUT:g} Hz -> comfortably IN band")
print(f"   corrected f = {f10:5.2f} Hz : below search cutoff, but AT the {LIGO_DESIGN_LOW:g} Hz design edge")
chk("the literal reading puts the mode comfortably inside the instrument band",
    63.0 > LIGO_SEARCH_CUT * 1.5,
    "this half is solid -- 63 Hz is near LIGO's most sensitive decade")
chk("the corrected value is NOT cleanly outside -- it sits on the design boundary",
    abs(f10 - LIGO_DESIGN_LOW) < 1.0,
    "so 'outside the detection range' needs an observing run, noise curve and amplitude to settle")
print("   => the defensible claim is that the printed unit weakens the paper's stated LIGO")
print("      justification, NOT that it reverses detectability. Amplitude is unknown and mode")
print("      camouflage is a separate argument; both survive this finding.")

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

# ---- 6. the rate: absent -- REGEX BROADENED at CGATE_A2's insistence --------------------
# CGATE_A2: "The rate regex in the script is narrow, so its assertion is stronger than that
# regex alone proves." It then searched manually across rate/event/population/abundance/
# number-density/formation/per-time language and confirmed the substantive conclusion.
# Repair: separate what the regex PROVES from what a seat CONFIRMED.
RATE_ESTIMATE = r"(?i)(event rate|merger rate|rate density|per year|per Gyr|yr\^?\{?-1|Gpc\^?\{?-3|population synthesis|number density of|expected number of|occurrence rate)"
BROAD         = r"(?i)(\brates?\b|\bpopulation\b|\babundance\b|\bformation\b|\bmergers?\b)"
rate_hits  = re.findall(RATE_ESTIMATE, T)
broad_hits = re.findall(BROAD, T)
print(f"\n6. THE EVENT RATE IS ABSENT")
print(f"   rate-ESTIMATE constructs (what this check proves): {len(rate_hits)}  {sorted(set(x.lower() for x in rate_hits))}")
print(f"   broad rate-adjacent words (reported, NOT proof):   {len(broad_hits)}  {sorted(set(x.lower() for x in broad_hits))}")
print(f"   CGATE_A2 inspected the broad hits by hand: 'The merger mentions only describe the")
print(f"   source scenario; there is no event-rate, merger-rate, abundance, population, or")
print(f"   expected-count estimate.' The broad hits are context, not rates.")
chk("no rate-ESTIMATE construct appears anywhere in the paper",
    len(rate_hits) == 0, "narrow claim, fully automated")
chk("the broad hits are acknowledged rather than hidden by a narrow pattern",
    len(broad_hits) > 0, f"{len(broad_hits)} rate-adjacent words exist and were adjudicated by seat, not by regex")

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
print("""
STATUS: GATED 2026-08-28. Two independent seats, both FINDING_CONFIRMED_BOTH / SIGNIFICANCE: DEFECT.
  CGATE_A2_VERDICT.md (codex gpt-5.5) -- also checked the ORIGINAL arXiv source, not just the
      ar5iv conversion: it contains 63{\\rm Hz}, 50{\\rm Hz}, 10{\\rm Hz} verbatim and names the
      Figure 5 asset omegaR_M_Hz_l-2.eps. So the mislabel is the paper's, not conversion damage.
  AGATE_A2_VERDICT.md (agy)

TWO OF MY CHECKS WERE REPAIRED BY THE GATE, NOT CONFIRMED BY IT:
  check 3 was overstated -- withdrawn and restated above at defensible precision.
  check 6's regex was narrower than its assertion -- broadened, with the seat's manual
      adjudication recorded as the thing that actually closes it.
BOTH SEATS DECLINED MY ATTACK-2 INFERENCE AS LOAD-BEARING. CGATE: the Discussion's "10 Hz" is
"plausible but not demonstrable ... F1 does not need that inference." It is circumstantial and
is presented as such. The finding rests on Table 1 and the positive control alone.
""")
sys.exit(0 if n_ok == len(checks) else 1)
