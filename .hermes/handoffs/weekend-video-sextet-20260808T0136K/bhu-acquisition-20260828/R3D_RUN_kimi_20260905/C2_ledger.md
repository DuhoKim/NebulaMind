# C2 COMPLETION LEDGER — R3D kimi seat, 2026-09-05

One row per candidate premise or relation considered. Status vocabulary: SOURCE_DERIVED /
ADDED_COMPLETION / UNRESOLVED. Every SOURCE_DERIVED row carries the pinned source path, the
line locator, and verbatim supporting text. Census row ids refer to
C2_census_entry18.txt / _entry19.txt / _entry20.txt / _entry55.txt (PART 2), which contain the
complete numbered dump of each source.

Paths below are relative to the protocol's directory.

## SOURCE_DERIVED rows

- L1 — the metric of the Dymnikova solution. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 139-148 (census B18-20):
    "ds2= ( 1 Ra-( r r)) c2dt2_ l_(Ra(r)/r ) d 2 -r2(dO2+sin20d~2), (11) where
     Ra(r)=r a 1 - e x p - (12) and r ,3 = ro2ra. (13)"
    (PDF-extraction scrambling; reads ds^2 = (1 - R_g(r)/r)c^2dt^2 - (1 - R_g(r)/r)^{-1}dr^2 - r^2dOmega^2,
     R_g(r) = r_g[1 - exp(-r^3/r_*^3)], r_*^3 = r0^2 r_g. Reading corroborated by the clean parallel
     print in entry 19 eq (2) and by the paper's own line 150: "for r >> r, practically coincides
     with the Schwarzschild solution and for r << r, behaves like the de Sitter solution".)
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 198-218 (census B19-13):
    "ds2 = 1- R g (r ) / r dt2 - dr2 / (1 - R g (r )/r) - r2 dOmega2 ; R g (r ) = 2G M(r ), (2)"

- L2 — size-mass binding r_*^3 = r0^2 r_g. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 147-148 (census B18-20):
    "and r ,3 = ro2ra. (13)"
  - corroboration within the manifest, `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt`
    lines 252-253 (census B19-16): "the exact analytic solution has been found for the density profile
    rho(r ) = rho0 exp (-r3 /r02 r g )" — the combination r_*^3 = r0^2 r_g is exactly the exponent scale.

- L3 — r_g = 2GM/c^2 with M the remote-observer mass. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 93-96 (census B18-12):
    "rg= 2GM c~' (6) and M is the mass of a source measured by a distant observer."
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 33-35 (census B19-03):
    "where r g = 2GM is the Schwarzschild horizon".

- L4 — core scale fixed by the limiting density: r0^2 = 3c^4/(8 pi G e0) = 3/Lambda. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 124-127 (census B18-17):
    "where r0 is connected with e0 by the de Sitter relation r~- 87CGeo' (9)"
    (numerator '3c 4' printed on line 126).
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 31-33 (census B18-02):
    "where r02 --- 3 / A , with the cosmological constant A responsible for the geometry."
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 244-252 (census B19-15):
    "; r02 = , 2 8 pi G rho0 r0 (4) where rho0 is the vacuum density at r = 0."
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` line 35 (census B19-03):
    "r0 = sqrt(3/Lambda) is the de Sitter horizon."

- L5 — density profile rho(r) = rho0 exp(-r^3/(r0^2 r_g)). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 118-122 (census B18-17):
    "Now we have to make one assumption concerning the specific form of the stress-energy tensor (4).
     If we assume that T O = e0 exp - (8)"
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 252-254 (census B19-16):
    "the exact analytic solution has been found for the density profile rho(r ) = rho0 exp (-r3 /r02 r g ),
     representing vacuum polarization in a spherical gravitational field estimated in the frame of a
     simple semiclassical model [17,24]."

- L6 — mass function M(r) = 4 pi Integral rho x^2 dx. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 220-230 (census B19-14):
    "The mass function M(r ) reads: M(r ) = 4 pi Zr rho( x ) x2 dx. (3)"
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 129-133 (census B18-18):
    "then the standard formula for the mass [6] ... (10)" (display garbled in extraction).

- L7 — finite total mass and exterior limit R_g(r -> inf) = r_g. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 232-240 (census B19-15):
    "M = 4 pi Zinf rho( x ) x2 dx < inf; R g (r -> inf) = r g ; R g (r -> 0) = r3/(3c2) r0^2 ..."
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 137-138 (census B18-19):
    "gives at r ~ oo the whole mass M connected with r a by the Schwarzschild relation (6)."

- L8 — interior de Sitter limit: R_g(r -> 0) behaviour and finite de Sitter curvature. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 238-244 (census B19-15):
    "R g (r -> 0) = 0 r3 3c2 ; r02 = ..." (R_g ~ r^3/r0^2 as r -> 0).
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 221-223 (census B18-28):
    "For r ~ 0, TO.2 remains finite and tends to the de Sitter value 7~02 = 24/r 4 which naturally
     appears to be the limiting value of the space-time curvature. All other invariants are also finite."

- L9 — horizons r+ (event) and r- (Cauchy). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 185-187 (census B18-25):
    "The metric (11) has two event horizons located approximately at
     r+ ~ rg[1 - O(exp(-r~/r~))1 r_ .~ r0[1 - O(ro/4ra)]. (17)"
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 189-193 (census B18-26):
    "Here r+ is the external event horizon. ... The internal horizon r_ is the Cauchy horizon [11]."
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 279-280 (census B19-18):
    "For M > Mcrit spacetime has two horizons, an event horizon r = r+ and an internal Cauchy horizon r = r- ."

- L10 — the printed mass-range bound M >= Mcrit (Mcrit = double-horizon mass, no closed form printed
  in any manifest source). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 277-279 (census B19-18):
    "Within the range of masses M >= Mcrit , where Mcrit corresponds to the double horizon, the
     de Sitter-Schwarzschild geometry (2) describes a regular black hole with the de Sitter interior [14,24]."

- L11 — regularity (nonsingular core). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 221-223 (census B18-28)
    (quoted under L8) and lines 210-211: "the solution presented here is nonsingular everywhere."
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 560-562 (census B19-20):
    "black and white holes (BH, W H) whose singularities are replaced with the future and past regular
     cores RC asymptotically de Sitter as r -> 0".

- L12 — stress-energy structure p_r = -rho, p_perp = -rho - (r/2) rho'. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 264-271 (census B19-17):
    "pr = - rho (r ); p _|_ = - rho (r ) - r d rho(r ) / 2 dr (5)"
  - `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` lines 165-168 (census B19-11):
    "solutions describing de Sitter-Schwarzschild transition belong to the class of solutions to the
     Einstein equations with the source term such that Trr = Ttt ( pr = -rho ). (1)"
  - `../bhu-reading-20260823/sources/dymnikova_1992_grg24_235_vor_clean.txt` lines 73-76 (census B18-08): eq (4).

- L13 — the algebraic condition epsilon = -p_r and the cosmological-constant equation of state at a
  regular centre (entry 20's restatement of the Dymnikova structure). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/gr-qc_0611022_clean.txt` lines 150-157 (census B20-09):
    "the stress-energy tensor of the matter source satisfies the condition T 0 0 == T 1 1 , or, in other
     words, epsilon = - p_r ... and at a regular centre in this case the matter equation of state has
     necessarily the form of a cosmological constant [17]".

- L14 — Bardeen example's horizon condition (a DIFFERENT type-1 model's critical size-mass relation,
  recorded because it is printed in a manifest source). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/gr-qc_0611022_clean.txt` lines 143-148 (census B20-09):
    "a particular BH configuration with r == rho, A(rho) = 1 - M rho^2/(rho^2+q^2)^{3/2}, (2) where
     M, q = const, and two horizons exist provided q^2 < (16/27) M^2 ."
  - Bearing: the Bardeen model is not a Dymnikova regular-core metric; the row is considered and set
    aside as WRONG_BRANCH content for the study question (see limbA.md).

- L15 — de Sitter-limit condition lambda = 3/l^2 (entry 55, Appendix A review). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/2007.06664_clean.txt` lines 1189-1190 (census B55-04):
    "Here l^_ is the cosmological length-scale associated with the cosmological constant that is given
     by lambda = 3/l^_^2 . ... The cosmological horizons are located at r = l^_ ."
  - Bearing: coordinate review of de Sitter geometry; carries no mass content.

- L16 — entry 55's emergent cosmological constant lambda = 0.06/(l_P^2 j). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/2007.06664_clean.txt` lines 1092-1098 (census B55-01):
    "lambda = 0.06 l_P^2 j . (67) At first sight, lambda appears to be unconstrained since j is a
     priori a free parameter".
  - Bearing: LQG effective-interior construction; binds lambda to the free spin j, not to a Dymnikova
    core scale, and bounds no black-hole mass.

- L17 — entry 55's bounce radius R_b(m,j) ~ (Gm)^{1/3} (l_P^2 j)^{1/3}. Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/2007.06664_clean.txt` lines 1112-1118 (census B55-02):
    "R b (m,j) ~ (Gm)^{1/3} (l_P^2 j)^{1/3} . (69) If one wants to strictly confine quantum effects to
     within the Planckian curvature region, then this relation could be used to argue for an upper
     bound on j of order ~ 10^6 or so for large enough black holes."
  - Bearing: LQG bounce model; no Dymnikova-core binding and no mass floor (it bounds j, not m).

- L18 — entry 55's mass <-> cosmological-constant estimate lambda_bar ~ c^4/(G^2 m^2). Status: SOURCE_DERIVED.
  - `../bhu-reading-20260823/sources/2007.06664_clean.txt` lines 1124-1144 (census B55-03):
    "j_bar ~ j_i N_i^2 ~ G^2 m^2/l_P^2 , (70) ... lambda_bar ~ c^4/(G^2 m^2) . (71) ... setting
     m ~= 1.46 x 10^53 kg , then we obtain lambda_bar ~= 0.85 x 10^-52 m^-2".
  - Bearing: an LQG renormalization-proposal estimate relating lambda to the (universe's) mass m;
    not a Dymnikova-core relation; bounds no black-hole mass from below.

## ADDED_COMPLETION rows

NONE. The completion-free derivation adds nothing, and each of the four completion kinds has its
object BOUND by a census row, so no kind is instantiated:

- Euclidean volume: its object (a volume-mass conversion for the core) is BOUND by the printed mass
  function (census row L6: entry 19 eq (3) lines 220-230; entry 18 eq (10) lines 129-133).
- Uniform interior: its object (the density profile) is BOUND (census row L5: entry 19 lines 252-254;
  entry 18 eq (8) lines 118-122).
- Order-unity coefficient set to 1: every coefficient in the relations among core scale, mass and
  horizon is printed exactly — coefficient 2 in r_g = 2GM/c^2 (L3), 3 in r0^2 = 3c^4/(8 pi G e0) (L4),
  1 in r_*^3 = r0^2 r_g (L2); the horizon-criticality coefficient is derived from the printed metric
  by calculus (limbB.md), not assumed. No unbound order-unity coefficient exists.
- GR exterior: its object (the exterior form and the identification of M) is BOUND (census rows L3
  and L7: entry 18 lines 93-96, 137-138; entry 19 eq (4) lines 232-240).

The admissible reading set is therefore the completion-free derivation alone.

## UNRESOLVED rows

NONE. Note on extraction state: several entry-18 displays are scrambled by the PDF extraction
(eqs (2),(3),(5),(8),(10),(14),(16)). Every relation this run uses is corroborated either by that
source's own context lines (which name and number the equation) or by the clean parallel print in
entry 19 (same author, same solution family; e.g. eq (13) r_*^3 = r0^2 r_g is corroborated by the
cleanly printed exponent scale r0^2 r_g in entry 19's density profile, lines 252-253). No candidate
premise or relation remains unresolved.

C2_COMPLETION_LEDGER=PASS
