# GATE BRIEF — B13, verifying arithmetic that WEAKENS my own prior claim

Fresh context. `b13_floor_routes.py`, 5/5, exit 0. Source:
`../bhu-reading-20260823/sources/0910.1181_clean.txt` (Poplawski). Read it yourself.

You gated B12 earlier and split on whether Poplawski's 1e16 kg floor is an arithmetic error or a
loose order-of-magnitude estimate. Both of you inverted the SAME route (Schwarzschild mean density,
2.7e14 kg). B13 uses an input neither of you used: the paper DEFINES the Cartan radius in eq. (33),

    m / r_C^3  ~  (G/c^4)(hbar/r_C^3)^2    =>    r_C = [G hbar^2 / (c^4 m)]^(1/3)

so rho_Ce can be COMPUTED rather than taken at its rounded 1e51.

## WHAT B13 CLAIMS

1. Eq. (33) gives r_Ce = 4.655e-28 m, matching the paper's stated "~1e-27 m" to a factor of 2, and
   hence rho_Ce = 9.03e51 kg/m^3 — 9x above the rounded value both of you used.
2. FIVE routes from a density to a minimum black-hole mass were tried. The closest lands at
   5.52e14 kg, still 18x (1.26 decades) below the printed 1e16 kg. None comes within a decade.
3. Refining rho_Ce from 1e51 to the exact 9.03e51 makes the discrepancy WORSE — 37x becomes 111x.
   So the gap is not an artefact of rounding; rounding runs the other way.
4. The required density for a 1e16 kg floor is 7.29e47, i.e. the paper's own figure is 3.14 decades
   (quoted) or 4.09 decades (exact) too high.
5. **This weakens my own B12 finding.** On the exact density the floor sits at 8.98e16 g, BELOW the
   open PBH window's 1e17 g lower edge — so there would be NO forbidden band and the PBH route I
   proposed would not exist at all.

## ATTACK THESE

1. **Check every number.** r_Ce, rho_Ce, all five M_min values, the required density, the decade
   counts. Recompute independently. An arithmetic slip here is the main risk, because the
   conclusion is congenial to a tidy story ("the gap is robust").
2. **Is eq. (33) being read correctly?** Does it really define r_C the way b13 solves it? Is the
   `m` in it the electron mass? Am I entitled to treat "~" in eq. (33) as an equality?
3. **Is the route list actually exhaustive of what the paper admits?** Name any route from rho_Ce
   to a minimum black-hole mass that b13 did NOT try and that could reach 1e16 kg. This is the
   attack most likely to succeed — I explicitly concede I cannot show what Poplawski did.
4. **Does claim 5 hold?** Is 8.98e16 g really below the window edge, and does that really remove
   the band, or does the window edge move too under the same reasoning?
5. **Does any check name more than its predicate tests?** Both of you caught this in B12.

## VERDICT FORMAT

First line one token: `ARITH_CONFIRMED` / `ARITH_REFUTED_<what>` / `ARITH_NARROWED_<what>`.
Write to `<C or A>GATE_B13_VERDICT.md` here. Say plainly what you could not verify.
Do NOT rule on error-vs-estimate — that is filed for the human and is not yours or mine.
