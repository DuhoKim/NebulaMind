# C4 GR BENCHMARK — R3D kimi seat, 2026-09-05

For every relation used in the limb-B derivation: the stated-limit algebra showing equality
with the Schwarzschild form in the exterior limit, and the premise list showing that no
interior premise entered. Relations and ledger rows are those of limbB.md.

## Relation R1 — metric function (ledger L1)

Printed: g_tt(r) = 1 - R_g(r)/r with R_g(r) = r_g(1 - exp(-r^3/r_*^3))
(entry 18 eqs (11),(12) census B18-20; entry 19 eq (2) census B19-13).

Stated-limit algebra (exterior limit r/r_* -> infinity):
  exp(-r^3/r_*^3) -> 0  (super-exponential decay)
  R_g(r)/r = r_g(1 - exp(-r^3/r_*^3))/r -> r_g/r
  g_tt(r) -> 1 - r_g/r
With R3 (r_g = 2GM/c^2):
  g_tt(r) -> 1 - 2GM/(c^2 r)  — the Schwarzschild form. EQUALITY shown.

Premise list for this algebra:
  - printed metric (entry 18 eqs (11)-(12); entry 19 eq (2))
  - printed r_g = 2GM/c^2 (entry 18 eq (6))
  No interior premise entered: the interior limit R_g(r) ~ r^3/r0^2 as r -> 0, the density
  profile's small-r behaviour, and the de Sitter-limit condition play no role in the
  exterior-limit algebra above.

## Relation R2 — r_*^3 = r0^2 r_g (ledger L2)

Printed: entry 18 eq (13) census B18-20.
Stated-limit role: r_* is a constant of the metric (no r-dependence); in the exterior limit
it enters only through the decaying exponential of R1, whose limit is computed above. The
relation itself is a printed algebraic identity among constants r_*, r0, r_g; the exterior
Schwarzschild form of R1 is recovered for every value of r_* — EQUALITY unaffected.

Premise list: printed eq (13) only. No interior premise entered.

## Relation R3 — r_g = 2GM/c^2 (ledger L3)

Printed: entry 18 eq (6) census B18-12 ("rg= 2GM c~' (6) and M is the mass of a source
measured by a distant observer"); entry 19 line 33 census B19-03.
Stated-limit role: this IS the Schwarzschild identification of the horizon scale with the
remote-observer mass; substituting it into the exterior limit of R1 yields
1 - 2GM/(c^2 r) — EQUALITY by the printed relation itself.
Entry 19 eq (4) corroborates: "R g (r -> inf) = r g" (census B19-15), so the exterior limit
of R_g is exactly the printed r_g.

Premise list: printed eq (6) (entry 18), printed eq (4) limit (entry 19), printed line 33
(entry 19). No interior premise entered.

## Relation R4 — r0^2 = 3c^4/(8 pi G e0) (ledger L4)

Printed: entry 18 eq (9) census B18-17; entry 19 eq (4) census B19-15.
Stated-limit role: used only to state that the core scale r0 is tied to the free limiting
density and is itself unbounded as a value (limbB.md §3). It does not enter the exterior
limit algebra; the Schwarzschild form of R1 is recovered independently of it. EQUALITY
unaffected.

Premise list: printed eq (9), printed eq (4). No interior premise entered in the exterior
algebra.

## Relation R5 — the mass-range statement M >= Mcrit (ledger L10)

Printed: entry 19 lines 277-281 census B19-18.
Stated-limit role: the criticality coefficient of limbB.md is derived from R1-R3 (printed
relations) by maximising the printed function R_g(r)/r; the exterior limit of that function,
r_g/r, is the Schwarzschild form shown under R1. The derivation introduces no exterior
assumption beyond the printed relations.

Premise list: printed lines 277-281 (entry 19); printed metric (R1). No interior premise
entered.

C4_GR_BENCHMARK=PASS
