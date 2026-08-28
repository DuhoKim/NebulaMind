#!/usr/bin/env python3
"""A6 -- entry 25 (Gaztanaga, Symmetry 14, 1849, Part I): does it hold a promotable falsifier?

GATED 2026-08-29. BOTH SEATS REFUSED THE PROMOTION, on the same attack:
    CGATE_A6_VERDICT.md  PROMOTE_REFUTED_ATTACK1_QUALIFIED_CONSEQUENCE / RIGID NO / DISTINCTIVE NO / FIRES UNDETERMINED
    AGATE_A6_VERDICT.md  PROMOTE_REFUTED_ATTACK_1                      / RIGID NO / DISTINCTIVE NO / FIRES YES

WHAT KILLED IT, and it is one word inside the sentence I was promoting:

    "The BHU can also be challenged by a measurement a[t] the DE equation of state w != -1. This
     would indicate that cosmic acceleration is not SOLELY caused by the BHU event horizon r_S."

"Not solely" leaves the horizon contribution in place and assigns the remainder to another
cause. So the sentence is a calibrated test of the paper's SOLE-CAUSE ACCELERATION CLAIM, not a
falsifier of the BHU model family. CGATE: "Promoting entry 25 as a live family falsifier would
silently strengthen the author's stated consequence."

I quoted that sentence four times before a seat pointed at the word. It was the entry-54 error
with the sign flipped -- and the qualification was not even buried in the body, it was in the
line itself.

WHAT SURVIVED, and it is not nothing. Both seats confirmed the narrow rigidity: r_S is NOT
time-dependent in this construction, the intermediate Mdot != 0 is the interior Misner-Sharp mass
relaxing to a fixed asymptote, and for the isolated horizon term a constant Lambda does force
w = -1. CGATE searched for a later withdrawal and for any time-varying-Lambda mechanism and found
neither. What fails is the STRONGER claim I made -- "no auxiliary" -- because the author's own
"not solely" licenses an extra component, so w_eff can differ while the BHU horizon survives.

AND THE INSTRUMENT WAS WORSE THAN THE ARGUMENT. CGATE: "All five check names claim more than
their predicates test", and "the script's successful self-checks validate its hard-coded
assertions, not the promotion." Check 4 was a tautology; check 5 hard-coded its own answer;
checks 3 and 5 each computed a variable and then left it out of the predicate. Every check below
is rewritten to compute or parse what its name claims, and check 4 now carries a positive control.
"""
import re, sys, hashlib

P25  = "../bhu-reading-20260823/sources/sym14091849_clean.txt"
DESI = "../bhu-reading-20260823/sources/2512.09486_clean.txt"
T = open(P25).read(); D = open(DESI).read()
NT = " ".join(T.split())          # whitespace-normalised, for reliable phrase location
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96)
print("A6 -- entry 25: PROMOTION REFUSED by both seats. What the sentence actually supports.")
print(f"     entry25 {hashlib.sha256(T.encode()).hexdigest()[:12]} | DESI {hashlib.sha256(D.encode()).hexdigest()[:12]}")
print("=" * 96)

# ---- 1. the sentence AND its qualifier -- the qualifier is now the finding -----------------
sent = re.search(r"The BHU can also be challenged by a measurement[^.]*\.[^.]*\.", NT)
s = sent.group(0) if sent else ""
print(f"\n1. THE SENTENCE, AND THE WORD I MISSED IN IT")
print("   " + s)
chk("the falsification sentence carries its own qualifier 'not solely', which limits the consequence",
    bool(sent) and "not solely" in s and "equation of state" in s,
    "tests the OBSERVABLE, the sentence, AND the qualifier -- the earlier version tested only that a regex matched")

# ---- 2. locate the Friedmann equation itself, not a loose substring -----------------------
fried = re.search(r"𝐻\s*2\s*=\s*8\s*𝜋\s*𝐺\s*3\s*𝜌\s*\+\s*Λ\s*3\s*=\s*8\s*𝜋\s*𝐺\s*3\s*𝜌\s*\+\s*1\s*𝑟\s*𝑆", NT)
print(f"\n2. THE DE TERM IS 1/r_S^2, LOCATED IN THE PAPER'S OWN FRIEDMANN EQUATION")
print("   " + (fried.group(0) if fried else "<< EQUATION NOT LOCATED >>"))
chk("the equation H^2 = 8piG/3 rho + Lambda/3 = 8piG/3 rho + 1/r_S^2 is present in the source",
    fried is not None,
    "the earlier check paired an arbitrary r_S=2.7 identity with a two-character substring search")

# ---- 3. r_S constancy -- every clause the name claims is now IN the predicate --------------
relax   = "all that remains is the SBH mass" in NT
outside = bool(re.search(r"observer outside only sees", NT))
mdot    = "reduces its value" in NT
# and the negative half: no statement that Lambda or r_S evolves as part of the mechanism
drift   = re.search(r"(time[- ]varying|evolving)\s*(Λ|Lambda|𝑟\s*𝑆)", NT)
print(f"\n3. IS r_S CONSTANT? (all four conditions now enter the predicate)")
print(f"   admits intermediate Mdot != 0 .................. {mdot}")
print(f"   that M relaxes to the constant SBH mass ........ {relax}")
print(f"   exterior observer sees only r_S ................ {outside}")
print(f"   any time-varying Lambda/r_S mechanism stated ... {drift is not None}")
chk("QUOTED: the source states the mass relaxes to the SBH value and the exterior sees only "
    "r_S, and contains no time-varying Lambda/r_S statement (absence: see caveat)",
    mdot and relax and outside and drift is None,
    "CGATE independently: 'the text does not make the exterior Schwarzschild radius time-dependent'")

# ---- 4. w from a REAL derivative, with a positive control ---------------------------------
# w(a) = -1 - (1/3) dln rho / dln a. Differentiate numerically; check against known fluids.
def w_from(rho_of_a):
    import math
    a1, a2 = 1.0, 1.0001
    dlnrho = math.log(rho_of_a(a2)) - math.log(rho_of_a(a1))
    dlna   = math.log(a2) - math.log(a1)
    return -1.0 - dlnrho/(3.0*dlna)
w_const = w_from(lambda a: 0.7)          # constant Lambda
w_mat   = w_from(lambda a: 0.3*a**-3)    # matter   -> should give  0
w_rad   = w_from(lambda a: 1e-4*a**-4)   # radiation-> should give +1/3
print(f"\n4. A CONSTANT Lambda FORCES w = -1  [derived, with a positive control]")
print(f"   estimator w = -1 - (1/3) dln(rho)/dln(a), differentiated numerically")
print(f"   matter    rho ~ a^-3 -> w = {w_mat:+.5f}   (known  0.00000)")
print(f"   radiation rho ~ a^-4 -> w = {w_rad:+.5f}   (known +0.33333)")
print(f"   constant Lambda      -> w = {w_const:+.5f}   (claim -1.00000)")
chk("the estimator reproduces matter and radiation, THEN gives w = -1 for constant Lambda",
    abs(w_mat) < 1e-3 and abs(w_rad - 1.0/3.0) < 1e-3 and abs(w_const + 1.0) < 1e-9,
    "the earlier check set rho_dot=0 by hand and asserted -1.0 == -1.0, which tested nothing")

# ---- 5. PARSE the DESI constraints and compute the offsets ourselves ----------------------
rows = re.findall(r"-0\.(9\d\d)\^\{\+0\.(\d+)\}_\{-0\.(\d+)\}|-0\.(9\d\d)\\pm\s*0\.(\d+)", D)
vals = []
for m in rows:
    if m[0]: vals.append((float("0."+m[0]), float("0."+m[1])))
    elif m[3]: vals.append((float("0."+m[3]), float("0."+m[4])))
print(f"\n5. HOW FAR IS w0 FROM -1?  [parsed from the pinned table, offsets computed here]")
offs = []
for v, e in vals:
    off = (1.0 - v)/e; offs.append(off)
    print(f"   w0 = -{v:.3f} +/- {e:.3f}   ->  ({1.0:.0f} - {v:.3f})/{e:.3f} = {off:.2f} sigma from -1")
maxoff = max(offs) if offs else float("nan")
chk("the pinned third-party fit puts w0 within ~2 sigma of -1, computed not quoted",
    len(offs) >= 4 and maxoff < 2.0,
    f"largest computed offset {maxoff:.2f} sigma; the paper's prose rounds this to 'approximately 1.8', "
    f"which CGATE noted is tolerable but not reproduced exactly from the marginalised numbers")

print("""
6. THE SPLIT, RECORDED RATHER THAN RESOLVED   [Blanc's instruction]

   FIRES:  AGATE said YES.  CGATE said UNDETERMINED.  I record both and adopt neither.

   Both seats went outside the pinned corpus to the DESI collaboration itself, which is the gap
   I had flagged as testimony. CGATE gives the citation: DESI DR2 Results II, arXiv:2503.14738,
   published Phys. Rev. D 112, 083515 (2025), reporting w0waCDM preferred over LambdaCDM at
   3.1 sigma for BAO+CMB and 2.8-4.2 sigma once supernovae are added, depending on the sample.

   AGATE reads that as the falsifier firing. CGATE refuses the step, and its reasoning is the
   more careful one: the BHU paper supplies NO statistical rejection rule, my script invented the
   3 sigma threshold, DESI's preference is dataset- and model-dependent, and the author's stated
   consequence is only "not solely caused". So the honest value is UNDETERMINED.

   TESTIMONY, NOT RECEIPT: arXiv:2503.14738 is NOT pinned in this corpus. Both seats reached it
   by search. Nothing above is asserted on it. Pinning that paper is the single highest-value
   next acquisition in this lane, and it would settle FIRES.

   CGATE also corrected my "does not fire" in the other direction: the collaboration results
   "overturn the script's suggestion that the best reachable evidence is only the pinned 1.8
   sigma fit." My framing understated what is reachable.

7. WHAT ENTRY 25 ACTUALLY HOLDS, at the strength both seats allow

   NOT: a family-level calibrated falsifier.  Tier stays QUALITATIVE-DIRECTIONAL.
   BUT: a calibrated test of the paper's SOLE-CAUSE ACCELERATION CLAIM -- w != -1 would show the
   horizon is not the whole of the acceleration, which is a narrower and genuinely stated
   consequence. Worth a bibliography NOTE, not a tier change.

   DISTINCTIVE: NO from both. LambdaCDM predicts w = -1 too, so w != -1 rejects a pure
   cosmological-constant sector in both and selects between neither. Recording this separately
   from falsifiability, because this lane demoted a claim once for conflating the two.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("\nSTATUS: GATED. Promotion REFUSED by both seats. No tier change proposed.")
sys.exit(0 if n_ok == len(checks) else 1)
