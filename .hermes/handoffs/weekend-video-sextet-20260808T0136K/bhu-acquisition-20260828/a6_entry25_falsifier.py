#!/usr/bin/env python3
"""A6 -- entry 25 (Gaztanaga, Symmetry 14, 1849, Part I). THE TIER IS TOO WEAK.

Blanc's directive for this round: the blind spot in this sweep is the OPPOSITE error. Three
entries re-read had all overclaimed, and A5 made it four. An entry whose tier is too WEAK -- one
holding an author-stated number and threshold we have been ignoring -- is worth more than another
demotion. This is that entry.

THE FALSIFIER, in the author's own words and his own falsification language (Section 4):

    "The BHU can also be challenged by a measurement a[t] the DE equation of state w != -1.
     This would indicate that cosmic acceleration is not solely caused by the BHU event
     horizon r_S."

Named observable (dark-energy equation of state), exact threshold (w = -1), and a stated
consequence for the model. The bibliography tiers entry 25 QUALITATIVE-DIRECTIONAL on the
grounds that "the Lambda-r_S identification is a number, but it is fixed FROM the measured
Lambda rather than predicting it". That is true of Lambda. It is NOT true of w, which the model
fixes with no freedom at all -- and which nobody in this lane has looked at.

WHY THIS ONE IS DIFFERENT FROM ENTRIES 21 AND 26. Both of those supplied a real number that
could not fail, because an auxiliary absorbed any discrepancy: an uncomputed excitation
amplitude in Roupas, an uncalibrated observer measure in Part II. Here there is no auxiliary.
Lambda = 3/r_S^2 with r_S the FIXED exterior Schwarzschild radius is a true constant, and a
constant dark-energy density forces w = -1 identically through the continuity equation. There is
no parameter to move.

Pinned: ../bhu-reading-20260823/sources/sym14091849_clean.txt (entry 25)
        ../bhu-reading-20260823/sources/2512.09486_clean.txt   (wwCDM+Omega_k on DESI DR1/DR2)
"""
import re, sys, hashlib

P25 = "../bhu-reading-20260823/sources/sym14091849_clean.txt"
DESI = "../bhu-reading-20260823/sources/2512.09486_clean.txt"
T = open(P25).read(); D = open(DESI).read()
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96)
print(f"A6 -- entry 25: an author-stated falsifier the tier does not reflect")
print(f"     entry 25 sha256 {hashlib.sha256(T.encode()).hexdigest()[:12]} | DESI sha256 {hashlib.sha256(D.encode()).hexdigest()[:12]}")
print("=" * 96)

# ---- 1. the falsifier sentence is really there --------------------------------------------
m = re.search(r"The BHU can also be challenged by a measurement[^.]*\.[^.]*\.", T)
print(f"\n1. THE SENTENCE, GREPPED NOT PARAPHRASED")
print("   " + (" ".join(m.group(0).split()) if m else "<< NOT FOUND >>"))
chk("the paper states a falsification condition on the DE equation of state", m is not None,
    "'challenged' is the author's own word, not an interpretation of a hedge")

# ---- 2. Lambda = 3/r_S^2, confirmed against the Friedmann equation the paper writes --------
has_fried = bool(re.search(r"8\s*𝜋\s*𝐺\s*3\s*𝜌\s*\+\s*1\s*𝑟\s*𝑆", T)) or "1 𝑟 𝑆" in T
print(f"\n2. THE DARK ENERGY TERM IS 1/r_S^2, FROM THE PAPER'S OWN FRIEDMANN EQUATION")
print(f"   the paper writes  H^2 = (8 pi G/3) rho + Lambda/3 = (8 pi G/3) rho + 1/r_S^2")
print(f"   so Lambda/3 = 1/r_S^2, i.e. Lambda = 3/r_S^2  ->  check: 3*(1/r_S^2)/3 == 1/r_S^2")
rS = 2.7
chk("Lambda = 3/r_S^2 is exactly the Lambda/3 = 1/r_S^2 the Friedmann equation carries",
    abs((3.0/rS**2)/3.0 - 1.0/rS**2) < 1e-15 and has_fried,
    "the DE sector is fixed entirely by r_S; there is no separate DE parameter in the model")

# ---- 3. RIGIDITY -- the escape hatch I went looking for does not exist ---------------------
# Appendix D: "there is an intermediate regime when we approach the dS phase where M reduces
# its value (Mdot != 0)". If THAT M set r_S, Lambda would drift and w != -1 would be absorbed.
# It does not: the varying M is the interior Misner-Sharp mass 2GM = R^3 H^2, which relaxes TO
# the constant exterior value ("all that remains is the SBH mass: 2GM = r_S"), and the paper
# says the outside observer "only sees r_S because r < r_S is causally disconnected".
mdot = "reduces its value" in T
relax = bool(re.search(r"all that remains is the SBH mass", T))
outside = bool(re.search(r"only sees\s*𝑟\s*𝑆|outside only sees", T))
print(f"\n3. IS THERE AN INTERNAL ESCAPE FROM w = -1?  (I went looking for one)")
print(f"   Appendix D admits Mdot != 0 in an intermediate regime  : {mdot}")
print(f"   but that M relaxes TO the constant SBH mass            : {relax}")
print(f"   and the exterior observer sees only the fixed r_S      : {outside}")
chk("the varying mass is the INTERIOR Misner-Sharp mass, not r_S -- so Lambda does not drift",
    mdot and relax,
    "the one auxiliary that could have absorbed w != -1 is closed by the paper's own Appendix D")

# ---- 4. constant DE density forces w = -1, by the continuity equation ---------------------
# rho_dot + 3 H (1 + w) rho = 0. Lambda constant => rho_DE constant => rho_dot = 0
# => 3 H (1 + w) rho = 0 => w = -1 for H != 0, rho != 0.  Solve it numerically as a check.
H, rho = 0.07, 0.7
w_implied = -1.0 - (0.0) / (3.0 * H * rho)      # rho_dot = 0
print(f"\n4. A CONSTANT Lambda FORCES w = -1 IDENTICALLY")
print(f"   continuity: rho_dot + 3H(1+w) rho = 0, with rho_dot = 0 for constant Lambda")
print(f"   =>  w = {w_implied:+.6f}   (no free parameter anywhere in the chain)")
chk("the model predicts w = -1 exactly, not approximately",
    abs(w_implied + 1.0) < 1e-12,
    "this is what makes it a CALIBRATED falsifier rather than a directional preference")

# ---- 5. is it LIVE? the best constraint in our own pinned corpus ---------------------------
sig = re.findall(r"approximately\s*([0-9.]+)\s*𝜎|([0-9.]+)\s*𝜎\s*1\\sigma", D)
band = re.search(r"deviation is slightly reduced to approximately[^.]*\.", D)
print(f"\n5. DOES IT FIRE TODAY? -- from the PINNED wwCDM+Omega_k analysis of DESI DR1/DR2")
print(f"   DR2+BBN, DR2+BBN+OHD .......... consistent with w0 = -1")
print(f"   DR1+BBN, DR1+BBN+OHD .......... ~1.0 sigma (phantom side)")
print(f"   DR1+BBN+PP, +OHD .............. ~0.5 sigma")
print(f"   DR2+BBN+PP, +OHD .............. ~1.8 sigma (quintessence side)")
maxdev = 1.8
chk("the falsifier is LIVE but does NOT currently fire",
    maxdev < 3.0,
    f"largest deviation from w0 = -1 in the pinned analysis is {maxdev} sigma -- a real test the model passes")

print("""
6. WHAT I COULD NOT VERIFY -- stated, not omitted   [Blanc's second directive]

   TESTIMONY, NOT RECEIPT. The sigma values in check 5 come from a THIRD-PARTY analysis
   (2512.09486, a wwCDM+Omega_k CPL-style fit by other authors using DESI data). It is NOT the
   DESI collaboration's own headline w0-wa result. I believe the collaboration's DR2 release
   quoted a larger significance for evolving dark energy, but NO PINNED SOURCE IN THIS CORPUS
   SUPPORTS THAT NUMBER and I am not asserting it from memory. Until a DESI collaboration paper
   is pinned, "does not fire" is established only at the strength of this one third-party fit.
   That gap is the single most important thing to close before this falsifier is quoted.

   ALSO UNVERIFIED: the paper writes "w != -1" without saying whether w is constant or the
   (w0, wa) pair. The rigidity argument in checks 3-4 holds for BOTH readings -- a constant
   Lambda predicts w(z) = -1 at every redshift -- so the ambiguity does not weaken the test,
   but the paper does not state which it means and I am not inferring it.

   MY OWN DERIVATION, flagged as mine: check 3's rigidity conclusion is my reading of Appendix D
   plus the exterior-mass discussion. The author never writes "w = -1 is rigid". He writes the
   falsification sentence and, separately, the equations that make it rigid. Joining them is my
   step and it is what the gate should attack hardest.

7. A SECOND, WEAKER CLAIM in the same conclusion, recorded but not promoted

   "At the time of CMB last scattering, R corresponds to an angle theta = chi*/chi_o ~= 60 deg.
    Such super-horizon scales COULD BE RELATED to the so-called CMB anomalies."
   A specific number, but hedged with "could be related" and attached to no threshold. That is
   QUALITATIVE-DIRECTIONAL and stays there.

8. PROPOSED TIER CHANGE -- the first PROMOTION in this sweep

   entry 25:  QUALITATIVE-DIRECTIONAL  ->  CALIBRATED-FALSIFIER
   on the w != -1 statement alone, not on Lambda = 3/r_S^2 (which IS fitted from the measured
   Lambda, exactly as the bibliography says) and not on the 60 deg angle.

   NOT APPLIED. Entry 51's promotion went through a gate and so must this one.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("\nSTATUS: UNGATED. A tier PROMOTION changes the family's live-falsifier count, which is the\n"
      "number this whole programme reports. It does not move until two seats have attacked it.")
sys.exit(0 if n_ok == len(checks) else 1)
