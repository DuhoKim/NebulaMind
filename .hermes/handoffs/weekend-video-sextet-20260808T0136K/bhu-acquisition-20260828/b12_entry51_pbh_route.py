#!/usr/bin/env python3
"""B12 -- entry 51's primordial-black-hole route.  GATED 2026-08-29, and NARROWED by both seats.

  CGATE_B12_VERDICT.md  ROUTE_NARROWED_FLOOR_AND_DETECTION_NOT_PINNED   (codex gpt-5.6-sol)
  AGATE_B12_VERDICT.md  ROUTE_NARROWED_MATH_ERROR                       (agy, Gemini 3.1 Pro)

The first version of this file claimed a live, open, two-decade forbidden band ~37 decades better
than the collider route. THAT CLAIM IS NARROWED, on four counts, and one number in it was simply
wrong. What survives is a conditional astrophysical route -- which is still more than the record
had, because the record had only the LHC.

WHAT BOTH SEATS AGREED, and is applied below:
  - C1's DIRECTION holds: the floor is a density bound and the LHC is a corollary, so the record
    has been carrying Poplawski's illustration as his scope.
  - C1's STRENGTH does not: "any black hole however formed" exceeds the derivation. See sec 1.
  - The window quotation is the review's CURRENT sentence, not its historical one -- but it is a
    CAVEATED summary window, not an unqualified open region.
  - My checks 1 and 2 named conclusions their predicates did not test. Both rewritten.
  - 8.7 TeV WAS NOT IN THE SOURCE. See the box at section 4.

WHAT THE SEATS SPLIT ON -- filed for Duho, not decided here: whether Poplawski's 1e16 kg is an
arithmetic error (agy) or a stacked order-of-magnitude estimate that must not be called one
(codex). Both compute the same 2.7e14 kg. The split does not change any action below.
"""
import math, sys
S="../bhu-reading-20260823/sources/"
P=" ".join(open(S+"0910.1181_clean.txt").read().split())
C=" ".join(open(S+"2002.12778_clean.txt").read().split())
M=" ".join(open(S+"2604.10732_clean.txt").read().split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B12 -- entry 51: the PBH route  [GATED, NARROWED BY BOTH SEATS]"); print("="*98)

print("\n1. THE FLOOR IS A DENSITY BOUND -- AND ITS REACH IS NARROWER THAN I CLAIMED")
i_den = P.find("mass density of a black hole also cannot exceed")
i_lhc = P.find("Large Hadron Collider", i_den if i_den>0 else 0)
chk("ORDERED: the density bound is stated BEFORE the LHC consequence, so the LHC is a corollary "
    "of the floor and not its scope",
    i_den > 0 and i_lhc > i_den and (i_lhc - i_den) < 700,
    f"density sentence at {i_den}, LHC at {i_lhc}, {i_lhc-i_den} chars later in the same passage. "
    "The earlier version of this check tested two disjoint substrings and NAMED a logical "
    "derivation -- both seats flagged that independently")
ferm = ("ordinary matter composed of quarks" in P) and ("Dirac particles cannot be compressed" in P)
chk("SOURCE: the derivation is about FERMIONIC matter, which is why 'any black hole however "
    "formed' overreaches it",
    ferm,
    "the density is 'the maximum density of ordinary matter composed of quarks and leptons', and "
    "the mechanism is that 'Dirac particles cannot be compressed to densities higher than the "
    "densities of its components'. CGATE: it supports a PBH formed by collapse of matter with "
    "spin; it does NOT pin a theorem covering radiation overdensities, scalar condensates, "
    "false-vacuum bubbles or domain walls, which Carr et al. list as PBH formation routes")

print("\n2. WHERE THE FLOOR SITS -- inside a CAVEATED window, not an open one")
M_floor_g=1e19; win_lo,win_hi=1e17,1e23
chk("SOURCE: 10^17-10^23 g is the review's CURRENT window, not the decade-ago figures it also "
    "prints -- both seats checked this independently",
    "middle mass window has shifted to" in C,
    "the historical sentence gives asteroid 10^16-10^17 g and sublunar 10^20-10^26 g; the current "
    "one says the middle window 'has shifted to' 10^17-10^23 g. AGATE confirmed from a second "
    "passage; CGATE confirmed the distinction is correctly drawn")
caveat = ("quasi-monochromatic" in C) and ("sometimes argued" in C)
chk("SOURCE: the review itself caveats that window, so calling the band 'presently open' "
    "overstates it",
    caveat,
    "'the lowest and highest mass windows have now narrowed and it is sometimes argued that they "
    "are excluded'; 'most of the limits assume that PBH mass spectrum is quasi-monochromatic ... "
    "and it could well be extended'. Both seats: sub-10^18 g PBHs are reported at <1% of DM under "
    "some assumptions (AGATE cites Laha et al. SPI/INTEGRAL), and rotating-hole evaporation "
    "constraints can close the lower window")
chk("COMPUTED: on the PRINTED floor the arithmetic placement is right -- it does lie inside the "
    "quoted endpoints",
    win_lo < M_floor_g < win_hi,
    "this is the one part of section 2 that is pure arithmetic and survived both gates intact")

print("\n3. THE FORBIDDEN BAND IS UNCERTAIN BY THE WIDTH OF ITSELF")
M_inv=math.sqrt(3*(2.99792458e8)**6/(32*math.pi*(6.674e-11)**3*1e51))*1e3
print(f"   on the paper's PRINTED floor  1e19 g -> forbidden band 1e17-1e19 g   = 2.00 decades")
print(f"   on the INVERTED floor    {M_inv:.2e} g -> forbidden band 1e17-{M_inv:.1e} g = "
      f"{math.log10(M_inv/win_lo):.2f} decades")
chk("COMPUTED: the two candidate floors give bands differing by more than a factor of four in "
    "log width, so the route's strength is not determined by the pinned text",
    2.0/math.log10(M_inv/win_lo) > 4.0,
    f"2.00 vs {math.log10(M_inv/win_lo):.2f} decades. CGATE independently reproduced 2.70e14 kg "
    "and added that dropping geometrical factors or using r ~ GM/c^2 moves it only by order-unity, "
    "not to 1e16 kg. The paper supplies no radius, density convention or intermediate equation")

print("\n4. THE COLLIDER COMPARISON -- with a number I had wrong and a mismatch I had missed")
print("""   ################################################################################
   #  8.7 TeV WAS NEVER IN THE SOURCE. An earlier extraction returned the digit
   #  truncated and I supplied '7'. The abstract reports a model-dependent RANGE:
   #  8.4-11.4 TeV for black holes, 9.0-10.7 TeV for string balls. b11 printed 8.7
   #  as a single value and the bibliography inherited it. Both are corrected.
   ################################################################################""")
chk("SOURCE: the exclusion is a model-dependent range, and no predicate in the earlier version "
    "pinned the value it printed",
    "8.4–11.4" in M and "9.0–10.7" in M,
    "'semiclassical black holes and string balls with masses below 8.4-11.4 TeV and 9.0-10.7 TeV, "
    "respectively, depending on the model and the number of extra dimensions'")
chk("SOURCE: the collider gap can still be cross-checked against the AUTHOR, which does not "
    "depend on the CMS number at all",
    "39 orders of magnitude" in P,
    "Poplawski computes it himself from LHC BEAM energy ~1e4 GeV against his 1e43 GeV floor. That "
    "is the defensible collider statement; it needs no CMS figure")
print("""   AND THE TWO ARE NOT THE SAME KIND OF NUMBER -- CGATE's point, which I had missed entirely.
   CMS's limit is derived IN A LARGE-EXTRA-DIMENSIONS MODEL. Poplawski's floor is four-dimensional
   ECKS. Quoting one against the other compares a production bound in one theory with a density
   bound in another. The comparison is illustrative, not a shared axis.""")

print("""
5. WHAT THE ROUTE ACTUALLY IS, after both gates

   NOT: "a live open two-decade band, 37 decades better than the collider route."
   BUT: a CONDITIONAL ASTROPHYSICAL ROUTE -- and the record should carry it, because the record
   currently carries only the LHC, and the LHC route is bounded by 39 decades that no collider
   closes. This one is bounded by observation quality instead, which improves.

   WHAT WOULD FIRE IT (CGATE's correction, and it makes the route BROADER than I wrote it):
   a securely identified black hole below the applicable ECKS floor that is established to be
   primordial. It does NOT have to constitute the dark matter -- "PBH dark-matter detection" was
   unnecessarily restrictive. A trace sub-population fires it just as well.

   WHAT IS NOT ESTABLISHED: that such an identification is presently achievable. The pinned review
   gives prospective sensitivities and contested constraints -- the GRB femtolensing bound over
   5e16-1e19 g is disputed on finite-source and wave-optics grounds and is omitted from the master
   plot; GRB parallax and X-ray-pulsar microlensing are described as prospects. Population-level
   inferences from Hawking radiation or induced GWs are not mass-tagged identifications of an
   individual hole. NO PRESENT DETECTION PROTOCOL IS PINNED.

6. NO TIER CHANGE. Entry 51 stays CALIBRATED-FALSIFIER / LIVE.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
