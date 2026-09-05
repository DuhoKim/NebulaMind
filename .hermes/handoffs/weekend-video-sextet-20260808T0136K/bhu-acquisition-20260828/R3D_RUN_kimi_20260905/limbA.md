# LIMB A — R3D kimi seat, 2026-09-05

Task (§3): attempt to reproduce, from the stated inputs (the four pinned sources and nothing
else), a printed relation BINDING SIZE TO MASS OR BOUNDING THE MASS AT ALL. Census completed
first, per §2c, before this limb was chosen (C2_census_entry18/19/20/55.txt).

## Result: TWO such relations are reproduced. Limb A is passed; limb B is entered.

### Reproduction 1 — a printed relation binding size to mass

Entry 18, eq (13) with eq (6) (census rows B18-20, B18-12):

  r_*^3 = r0^2 r_g      (eq (13), lines 147-148, verbatim "and r ,3 = ro2ra. (13)")
  r_g   = 2GM/c^2       (eq (6),  lines 93-95,  verbatim "rg= 2GM c~' (6)")

Combined: r_*^3 = r0^2 * 2GM/c^2 — the characteristic core size r_* is bound to the mass M
(and the core scale r0). This is a closed printed relation between core scale, mass and size.

Corroboration inside the manifest (same solution family, clean print): entry 19 prints the
density profile "rho(r ) = rho0 exp (-r3 /r02 r g )" (lines 252-253, census B19-16) whose
exponent scale is exactly r_*^3 = r0^2 r_g, and eq (2)/(4) print R_g(r) = 2GM(r),
R_g(r -> inf) = r_g (census B19-13, B19-15).

### Reproduction 2 — a printed statement bounding the mass

Entry 19, lines 277-281 (census B19-18), verbatim:

  "Within the range of masses M >= Mcrit , where Mcrit corresponds to the double horizon, the
   de Sitter-Schwarzschild geometry (2) describes a regular black hole with the de Sitter
   interior [14,24], called a Lambda black hole (LambdaBH) in [26]. For M > Mcrit spacetime
   has two horizons, an event horizon r = r+ and an internal Cauchy horizon r = r- ."

This bounds the black-hole mass from below (M >= Mcrit). The sources print NO closed formula
for Mcrit; the double-horizon condition itself is derivable from the printed metric (limbB.md).

### Also recorded

- Entry 20 eq (2) prints another type-1 model's critical condition, "two horizons exist
  provided q^2 < (16/27) M^2" (census B20-09). That is the Bardeen model, not a Dymnikova
  regular-core metric — considered and set aside (WRONG_BRANCH for the study question).
- Entries 20 and 55 were censused in full; their own constructions (phantom black universes;
  LQG effective interior) carry no Dymnikova-core size-mass or mass-floor relation (census
  WRONG_BRANCH rows; candidate rows L14-L18 in C2_ledger.md considered and set aside).

Limb A wording, per protocol: it is NOT the case that "a relation binding size to mass, or
bounding the mass, was unreproduced from the stated inputs". A size-mass relation IS
reproduced (r_*^3 = r0^2 r_g with r_g = 2GM/c^2) and a mass bound IS printed (M >= Mcrit).
Limb B is therefore entered.
