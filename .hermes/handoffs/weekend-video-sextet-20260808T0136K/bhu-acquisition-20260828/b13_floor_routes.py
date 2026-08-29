#!/usr/bin/env python3
"""B13 -- trying to FIND Poplawski's 1e16 kg, not merely to fail to reproduce it.

GATED 2026-08-29, both seats, and both recomputed every number independently:
  AGATE_B13_VERDICT.md  ARITH_CONFIRMED                        (agy, Gemini 3.1 Pro)
  CGATE_B13_VERDICT.md  ARITH_NARROWED_NONEXHAUSTIVE_APPROXIMATION  (codex gpt-5.6-sol)

THE ARITHMETIC SURVIVED INTACT. CGATE reproduced every value to ten significant figures; AGATE
verified them separately. Neither seat could find any route reaching 1e16 kg.

THE FRAMING DID NOT, and this version is rewritten for it:
  - I called the computed density "EXACT". It is not. Eq. (33) is a scaling relation with "~";
    solving it as an equality IMPOSES a unit coefficient. Both seats flagged this. The word is
    gone from this file -- it is a NORMALISATION, and every result is conditional on it.
  - I wrote "EVERY route". Five is not every. CGATE named four the paper admits and I did not
    try, and computed one of them itself (extremal Kerr, added below as row 6 -- it also falls
    short). The claim is now "none of the six tested".
  - Checks 1, 2, 4 and 5 named conclusions their predicates did not test. Both seats, independently
    and in almost the same words. All four rewritten; check 4 was an INTERPRETIVE claim wearing a
    numerical predicate and is now split into the number and the reading, with the reading in prose.

WHERE THE SEATS SPLIT, I TOOK THE NARROWER READING AND AM NOT ADJUDICATING:
  - exhaustiveness: AGATE "exhausts all physically plausible interpretations"; CGATE "demonstrably
    nonexhaustive". Taken: CGATE's.
  - claim 5: AGATE "the forbidden band entirely vanishes"; CGATE "a valid conditional scenario"
    whose ordering sits 0.0467 decade from reversing. Taken: CGATE's.
  Declining the stronger form of my own finding is not picking a winner between seats.

OPEN QUESTION 2 IS NOW CLOSED, and this file's restraint was the right call. Duho returned the
decision with "answer question 2". THE RULING: an unreproduced step, NOT an error.

TWO FACTS DECIDED IT, and one of them destroyed my own recommendation. I had recommended getting
the journal version first, on the assumption we held only a preprint. WE HOLD THE PUBLISHED PAPER —
Phys. Lett. B 690(1) 73-77, (c) Elsevier — so that option was already exhausted and I had not
checked. The published text carries no step either: 86 characters separate the density claim from
the mass figure, and the derivation is the phrase "from which".

WHY NOT "ERROR", ON THE MERITS RATHER THAN AS A FALLBACK. The two options record the SAME verifiable
content -- six routes, none reaches it, 3.1-4.1 decades short, no step shown. They differ only in
asserting something about the author that cannot be checked. And this file explicitly refuses to
prove that no route exists; "error" asserts exactly that. CGATE's rule from a later gate applies
unchanged: a gap is not a defect unless we can show the stronger claim, and we cannot.
"""
import math, sys
S="../bhu-reading-20260823/sources/"
P=" ".join(open(S+"0910.1181_clean.txt").read().split())
G=6.67430e-11; c=2.99792458e8; hbar=1.054571817e-34; me=9.1093837015e-31
TARGET=1e16
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B13 -- can Poplawski's 1e16 kg be reached from his own quantities?  [GATED]")
print("="*98)

print("\n1. THE CARTAN RADIUS, FROM EQ. (33) -- SOLVED AS AN EQUALITY, WHICH IT IS NOT")
r_Ce=(G*hbar**2/(c**4*me))**(1/3); rho_n=me/r_Ce**3
print(f"   eq.(33) m/r_C^3 ~ (G/c^4)(hbar/r_C^3)^2  =>  r_C = [G hbar^2/(c^4 m)]^(1/3)")
print(f"   r_Ce = {r_Ce:.4e} m      the paper states '~10^-27 m'   -> agreement to a factor 2.15")
print(f"   rho_n = m_e/r_Ce^3 = {rho_n:.4e} kg/m^3   the paper states '~10^51'  -> 9.03x higher")
chk("COMPUTED: solving eq. (33) as an equality lands within half a decade of the radius the paper "
    "prints, which is what licenses using it as a NORMALISATION -- not as an exact value",
    abs(math.log10(r_Ce)+27) < 0.5,
    f"{r_Ce:.3e} m vs the stated ~1e-27 m. CGATE: 'exact only relative to B13's imposed unit "
    f"coefficient'; it does not recover coefficients suppressed in the energy-momentum term, the "
    f"spin term, the wave-function normalisation or the effective particle volume, and CUBING THE "
    f"RADIUS makes even modest hidden coefficients matter for the density")

print("\n2. SIX ROUTES FROM A DENSITY TO A MINIMUM BLACK-HOLE MASS -- none of them reaches it")
def M_mean(rho,rad=2.0):  # rho = M / (4/3 pi (rad*GM/c^2)^3)
    return math.sqrt(3*c**6/(4*math.pi*G**3*rho*rad**3))
def M_nogeo(rho):         # rho = M / r_s^3, geometry dropped
    return math.sqrt(c**6/(8*G**3*rho))
rows=[("paper's quoted rho ~1e51","mean density, r_s",M_mean(1e51)),
      ("paper's quoted rho ~1e51","M/r_s^3, no geometry",M_nogeo(1e51)),
      ("eq.(33) normalisation","mean density, r_s",M_mean(rho_n)),
      ("eq.(33) normalisation","M/r_s^3, no geometry",M_nogeo(rho_n)),
      ("paper's quoted rho ~1e51","extremal Kerr, r_+ = GM/c^2",M_mean(1e51,1.0)),
      ("--","horizon = Cartan radius",r_Ce*c**2/(2*G))]
print(f"   {'density used':<26} {'criterion':<28} {'M_min':>11} {'short by':>10}")
for lab,f,M in rows: print(f"   {lab:<26} {f:<28} {M:>11.2e} {TARGET/M:>9.3g}x")
best=min(rows,key=lambda r: abs(math.log10(r[2]/TARGET)))
chk("COMPUTED: none of the SIX tested routes lands within a decade of 1e16 kg",
    all(abs(math.log10(M/TARGET))>1.0 for _,_,M in rows),
    f"nearest is {best[2]:.2e} kg, {math.log10(TARGET/best[2]):.2f} decades short. NOT 'no route "
    f"exists' -- CGATE names four the paper admits and this does not try: Kerr-Newman geometry, a "
    f"local rest-frame proper density, a full nonsingular ECKS or toroidal interior, and "
    f"coefficients suppressed in eq. (33). Row 5 IS one of them, computed by CGATE itself, and it "
    f"falls short too")

print("\n3. DIRECTION UNDER THE ONE SUBSTITUTION THAT COULD HAVE CURED IT")
Mq,Mp=M_mean(1e51),M_mean(rho_n)
print(f"   quoted rho 1e51        M_min = {Mq:.2e} kg  -> {TARGET/Mq:.0f}x short")
print(f"   eq.(33) normalisation  M_min = {Mp:.2e} kg  -> {TARGET/Mp:.0f}x short")
chk("COMPUTED: replacing the paper's ROUNDED density with the eq.(33) normalisation widens the "
    "shortfall rather than closing it",
    TARGET/Mp > TARGET/Mq,
    f"{TARGET/Mq:.0f}x becomes {TARGET/Mp:.0f}x. CGATE's precise scope, adopted: this rules out "
    f"THAT substitution as a cure. It does not rule out rounding in general, because coefficients "
    f"suppressed elsewhere are untested")

print("\n4. THE SIZE OF THE THING TO BE EXPLAINED")
need=3*c**6/(32*math.pi*G**3*TARGET**2)
print(f"   a 1e16 kg floor under the mean-density criterion needs rho = {need:.3e} kg/m^3")
print(f"   the paper's quoted rho_Ce is {1e51/need:.0f}x higher   ({math.log10(1e51/need):.2f} decades)")
print(f"   the eq.(33) normalisation is {rho_n/need:.0f}x higher   ({math.log10(rho_n/need):.2f} decades)")
chk("COMPUTED: the density shortfall exceeds three decades under both densities",
    math.log10(1e51/need)>3.0 and math.log10(rho_n/need)>3.0,
    f"{math.log10(1e51/need):.2f} and {math.log10(rho_n/need):.2f} decades. THE NUMBER ONLY -- the "
    f"earlier version named this check for what such hedging 'conventionally covers', which is a "
    f"reading, not an arithmetic fact. Both seats flagged it. The reading is in the prose below "
    f"and is offered to Duho as an observation, not asserted here")

print("\n5. WHAT IT DOES TO MY OWN B12 CLAIM -- a THIRD candidate, conditionally")
Mg=Mp*1e3; edge=1e17
print(f"   floor under the eq.(33) normalisation: {Mg:.3e} g   window lower edge: {edge:.0e} g")
print(f"   margin: {math.log10(edge/Mg):.4f} decade  ({(edge/Mg-1)*100:.1f}%)")
chk("COMPUTED: under this normalisation the floor falls below the window edge, and the margin by "
    "which it does is under 0.05 decade",
    Mg < edge and math.log10(edge/Mg) < 0.05,
    f"{Mg:.3e} g < 1e17 g by {math.log10(edge/Mg):.4f} decade. CGATE, adopted: this is 'a valid "
    f"conditional scenario, not a robust removal of the route' -- a suppressed coefficient of 1.24 "
    f"in the density-to-mass relation, or 1.07 in the radius, REVERSES THE ORDERING. AGATE called "
    f"the band vanished; I am taking the narrower reading of my own result")

print("""
6. WHAT THIS ESTABLISHES, at the width both gates allow

   THE FLOOR DOES NOT FOLLOW from the printed density by any of six routes reconstructible from
   this paper; the shortfall is 3.1-4.1 decades in density; and the one substitution most likely
   to have cured it makes it worse. Neither seat found a route that reaches 1e16 kg.

   IT DOES NOT ESTABLISH that no such route exists. CGATE: "because local proper density and a
   nonsingular ECKS interior are not specified, I also cannot prove that no admitted route or
   suppressed coefficient can reach it. B13's finite enumeration cannot bear that universal
   conclusion." The paper states the two numbers consecutively and shows nothing between them.

   FOR B12's PBH ROUTE there are now THREE candidate floors -- 1e19 g printed, 2.7e17 g inverted
   from the quoted density, 9.0e16 g under the eq.(33) normalisation -- giving forbidden bands of
   2.00 decades, 0.43 decades, and none. They disagree about whether there is anything to look for,
   and the third sits 0.047 decade from flipping back. THE ROUTE IS CONDITIONAL ON A NUMBER THE
   PAPER DOES NOT DERIVE, which is the honest summary of the whole evening's work on entry 51.

   NO TIER CHANGE. Entry 51 stays CALIBRATED-FALSIFIER / LIVE.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
