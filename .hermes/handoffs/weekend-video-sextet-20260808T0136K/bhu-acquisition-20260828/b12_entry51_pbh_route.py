#!/usr/bin/env python3
"""B12 -- entry 51 has a LIVE falsification route the record does not track.

B11 established that the LHC route is bounded: CMS reaches 8.7 TeV, the floor is 39 decades up,
and no collider closes that gap. That reads like "the falsifier cannot be fired". It is wrong,
and the reason is in Poplawski's own sentence.

THE SCOPE QUESTION, settled from the source rather than assumed. Poplawski's bound is on DENSITY,
not on a production mechanism: "The mass density of a black hole also cannot exceed rho_Ce, from
which its minimum mass in the ECKS theory is ~10^16 kg." The LHC appears in the NEXT sentence as
an illustration ("Therefore the LHC ... cannot produce micro black holes"). The floor is therefore
a statement about ANY black hole of that mass, however it formed -- so PRIMORDIAL black holes are
in scope, and the record has been reading the illustration as the scope.

PINNED FOR THE MEASUREMENT SIDE: 2002.12778 (Carr, Kohri, Sendouda, Yokoyama, "Constraints on
primordial black holes", Rept. Prog. Phys.).
"""
import math, sys
S="../bhu-reading-20260823/sources/"
P=" ".join(open(S+"0910.1181_clean.txt").read().split())
C=" ".join(open(S+"2002.12778_clean.txt").read().split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B12 -- entry 51: the primordial-black-hole route"); print("="*98)

print("\n1. THE FLOOR IS A DENSITY BOUND, SO IT IS NOT ABOUT COLLIDERS")
chk("SOURCE: Poplawski derives the floor from a maximum DENSITY that applies to a black hole as "
    "such, with the LHC named only as a consequence",
    "mass density of a black hole also cannot exceed" in P and "minimum mass in the ECKS theory" in P,
    "'The mass density of a black hole also cannot exceed rho_Ce, from which its minimum mass ... "
    "is ~10^16 kg' -- then 'Therefore the LHC ... cannot produce micro black holes'. Scope first, "
    "illustration second; the record has been carrying the illustration as the scope")

print("\n2. WHERE THE FLOOR SITS ON THE PBH MASS AXIS")
M_floor_g = 1e16*1e3
print(f"   Poplawski floor            {M_floor_g:.0e} g   (10^16 kg)")
win_lo, win_hi = 1e17, 1e23
print(f"   open PBH dark-matter window {win_lo:.0e} - {win_hi:.0e} g   (Carr et al., current)")
chk("SOURCE: the review states the open all-dark-matter window has SHIFTED to 10^17-10^23 g",
    "10 17 ​ – ​ 10 23" in C or "middle mass window has shifted to" in C,
    "'the middle mass window has shifted to 10^17-10^23 g, with the both mass limits having "
    "decreased' -- the decade-ago figures (asteroid 10^16-10^17, sublunar 10^20-10^26) are the "
    "review's HISTORY sentence, not its current claim")
inside = win_lo < M_floor_g < win_hi
chk("COMPUTED: the floor lands INSIDE the open window rather than outside it",
    inside,
    f"{M_floor_g:.0e} g is {math.log10(M_floor_g/win_lo):.0f} decades above the window's floor and "
    f"{math.log10(win_hi/M_floor_g):.0f} below its ceiling -- it CUTS the window in two")

print("\n3. WHAT THAT MEANS -- and it is a live test, not a bounded one")
print(f"   {win_lo:.0e} - {M_floor_g:.0e} g   PBHs here are FORBIDDEN by entry 51.")
print( "                          A dark-matter detection in this band FIRES the falsifier.")
print(f"   {M_floor_g:.0e} - {win_hi:.0e} g   PBHs here are ALLOWED. A detection fires nothing.")
print( "   Both bands are open right now. Neither is excluded. The test is available.")

# how close is each route to the floor?
GeV_kg=1.78266192e-27
M_cms_g = 8.7e3*GeV_kg*1e3
gap_lhc = M_floor_g/M_cms_g
gap_pbh = M_floor_g/win_lo
print("\n4. THE TWO ROUTES, COMPARED ON THE ONE AXIS THAT MATTERS")
print(f"   CMS reach 8.7 TeV        = {M_cms_g:.2e} g   -> {math.log10(gap_lhc):.0f} decades below the floor")
print(f"   PBH window bottom        = {win_lo:.0e} g   -> {math.log10(gap_pbh):.0f} decades below the floor")
chk("COMPUTED: the collider gap reproduces Poplawski's own '39 orders of magnitude' figure, so "
    "this arithmetic is checked against the author rather than only against itself",
    abs(math.log10(gap_lhc)-39) < 1.0 and "39 orders of magnitude" in P,
    f"computed {math.log10(gap_lhc):.1f} decades; the paper says '39 orders of magnitude larger "
    f"than the maximum beam energy currently available at the LHC'")
chk("COMPUTED: the PBH route is ~37 decades closer to the floor than the collider route",
    math.log10(gap_lhc/gap_pbh) > 35,
    f"{math.log10(gap_lhc/gap_pbh):.0f} decades closer. The collider route is bounded because no "
    f"collider closes 39 decades; the PBH route needs to close TWO, and observations already "
    f"operate inside it")

print("""
5. WHAT I COULD NOT VERIFY -- stated plainly, because it moves the answer

   I CANNOT REPRODUCE THE FLOOR FROM THE DENSITY THE PAPER QUOTES. Inverting rho_Ce ~ 1e51 kg/m^3
   through the Schwarzschild mean density rho = 3c^6/(32 pi G^3 M^2) gives the number printed
   below, not 1e16 kg. Both of Poplawski's figures carry "~" and "on the order of", and he may use
   a different radius or density convention that the pinned text does not spell out. I am NOT
   calling this an error. I am recording that the floor's PLACEMENT INSIDE THE WINDOW is uncertain
   at the one-to-two decade level -- which is the whole quantity of interest in section 3, since
   the forbidden band is only two decades wide.

   THE REVIEW'S OWN CAVEAT, which cuts the same way: "most of the limits assume that PBH mass
   spectrum is quasi-monochromatic ... and it could well be extended". An extended spectrum
   straddles the floor by construction.

   VINTAGE. Carr et al. is a 2020-21 review and the record's CMS claim was dated 2025-12. Window
   edges move; the edges used here are the review's, not today's.
""")
M_inv = math.sqrt(3*(2.99792458e8)**6/(32*math.pi*(6.674e-11)**3*1e51))
print(f"   inverted from the paper's own rho_Ce : {M_inv:.2e} kg = {M_inv*1e3:.2e} g")
print(f"   the paper's stated floor             : 1.00e+16 kg = 1.00e+19 g")
print(f"   ratio                                : {1e16/M_inv:.0f}x  ({math.log10(1e16/M_inv):.1f} decades)")
print("""
   AT THE INVERTED VALUE the floor sits at ~3e17 g -- near the BOTTOM edge of the open window, so
   the forbidden band nearly vanishes and the route weakens sharply. AT THE PAPER'S VALUE it sits
   two decades in and the band is real. The route's strength depends on which is right, and
   settling that needs the published PLB version, not the preprint text pinned here.

6. NO TIER CHANGE IS PROPOSED. Entry 51 stays CALIBRATED-FALSIFIER / LIVE. This finding does not
   move the tier -- it identifies an untracked route by which the existing tier could actually be
   exercised, and one uncertainty that governs how strong that route is.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)
