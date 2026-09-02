AUDIT_HOLDS_THEORETICAL_OBSTRUCTION

# Entry 5 — Khakshournia (2010), "A note on Pathria's model" — claude-seat deep audit (BLIND)

Seat: claude-seat (Fable 5.1). Stamped 2026-09-02 20:55 KST (`date`). Source read: ONLY
`../bhu-reading-20260823/sources/khakshournia_2010_note_pathria_arxiv1412.0105_clean.txt` (236 lines). No ENTRY5_*
result file and no codex/kimi file opened. Line receipts are `L<n>` into that file. The extrinsic-curvature jump was
re-derived from scratch below (not copied from the paper's intermediate lines, which are OCR-garbled at L152–157).

## 1. The junction — what is set up, what is computed, what is cited

**Interior (−):** pressureless closed FRW with Λ, written in retarded-null coordinates, eq. (1) at L67
`ds²₋ = −a² dv(2dχ + dv) + a² sin²χ dΩ²`, with `dv = dt/a − dχ` (eq. 2, L72–73), Friedmann eqs. (3)–(4) at L77–80
(`ȧ²/a² + 1/a² − Λ/3 = 8πρ/3`, `ä/a − Λ/3 = −4πρ/3`). Checked: substituting dt = a(dv+dχ) into −dt² + a²dχ² gives
exactly (1). The surface Σ is the ingoing radial null cone (`2dχ = −dv`, eq. 7 L102).

**Exterior (+):** eq. (5)–(6) at L86–90, `ds²₊ = −du(f du + 2dr) + r² dΩ²`, `f = 1 − 2M/r − Λr²/3` — i.e.
Schwarzschild–de Sitter with the SAME Λ (abstract/conclusion say "vacuum Schwarzschild", but eq. 6 carries Λ).
Dust-mass relation L91: `M = 4π∫ρr²dr = (4π/3)ρ r³|Σ`, "a constant for a dust-filled universe" (L91–92).

**Identification surface:** the horizon of the exterior is identified with the FRW radius at maximum expansion
(L18–21, L38–41); the paper notes this makes the separating surface "(instantaneously) a null hypersurface"
(L49–51); the computation is done "at χ = π/2, corresponding to the maximum expansion" (L160–161); conclusion
L184–186, L194–197.

**Formalism:** Barrabès–Israel null-shell formalism, cited [3] (L54–55, L222–223) and [5] (L227), with Poisson [4]
(L126, L225) for the n = e_u choice. Cited: the definition K_ab = e_a^μ e_b^ν ∇_μ N_ν (L138), the pseudo-inverse
g*^ab (L134), the pressure formula p = −(1/8π) n^a n^b [K_ab] (L173–176).
Computed in the paper (its own application): first junction conditions (7) L101–103; tangent bases (8)–(9)
L109–112; du/dχ (10) L116–123; transverse null vectors N (11)–(12) L128–131; induced metric and g* L132–136;
K_θθ|− (13) L141–147; K_uu|− (14) L152–157; K_θθ|+, K_uu|+ (15)–(16) L164–168; the jump and p (17) L169–179.

### Re-derivation (claude-seat, from the two metrics only)

Interior inverse metric in the (v,χ) block: g^vv = 0, g^vχ = −1/a², g^χχ = 1/a². Exterior (u,r) block:
g^uu = 0, g^ur = −1, g^rr = f.

- Tangent to Σ: interior e_u = (dχ/du)(−2,1,0,0), null: (dχ/du)²[4(−a²) + 2(−a²)(−2)] = 0. Matches (8).
  Exterior e_u = (1, −f/2, 0, 0), null: −f + 2(−1)(−f/2) = 0. Matches (9).
- Transverse N (N·n = −1, N·N = 0, N·e_A = 0): interior N_μ = (½ du/dχ, 0,0,0); exterior N_μ = (−1,0,0,0).
  Matches (11)–(12).
- Induced metric: diag(0, r², r² sin²θ) both sides once r = a sinχ. Matches L133.
- du/dχ along Σ: dr/dχ|Σ = (∂_χ a + ∂_v a·(dv/dχ)) sinχ + a cosχ = (aȧ − 2aȧ) sinχ + a cosχ =
  −aȧ sinχ + a cosχ, and f du = −2dr, so du/dχ = (−2/f)(a cosχ − aȧ sinχ). Matches (10) L119–123.
- Christoffels used (interior): Γ^v_θθ = ȧ sin²χ + sinχ cosχ; Γ^v_vv = ȧ; Γ^v_vχ = Γ^v_χχ = 0;
  Γ^χ_vv = 0; Γ^χ_vχ = ȧ; Γ^χ_χχ = 2ȧ (with ∂_χ a|_v = ∂_v a|_χ = aȧ).
  (exterior): Γ^u_θθ = r; Γ^u_uu = −f_,r/2; Γ^u_ur = Γ^u_rr = 0.
- K_θθ|+ = Γ^u_θθ = r. Matches (15).
- K_uu|+ = Γ^u_μν e^μ e^ν = −f_,r/2. Matches (16). (This is the inaffinity of ∂_u on the horizon.)
- K_θθ|− = −Γ^v_θθ N_v = −(½ du/dχ) sinχ(ȧ sinχ + cosχ) = (a sinχ/f)(cos²χ − ȧ² sin²χ). Matches (13) middle
  line L143–145. Then with M = (4π/3)ρ r³ and Friedmann (3): f = 1 − r²(8πρ/3 + Λ/3) = 1 − sin²χ(ȧ² + 1) =
  cos²χ − ȧ² sin²χ, so K_θθ|− = a sinχ = r. Matches (13) last line L147. Hence [K_θθ] = 0.
- K_uu|− = e^μ e^ν(∂_μ N_ν − Γ^λ_μν N_λ). With w ≡ du/dχ: K_uu|− = −(dw/dχ)/w² − 2ȧ/w. Using w = −2a/(cosχ +
  ȧ sinχ) (the paper's identity f = cos²χ − ȧ² sin²χ), dt/dχ|Σ = −a, and g ≡ cosχ + ȧ sinχ:
  K_uu|− = (ȧg − dg/dχ)/(2a) = sinχ (1 + ȧ² + aä)/(2a).
  By (3)+(4): 1 + ȧ² + aä = a²(4πρ + 2Λ)/3, so K_uu|− = a sinχ (2πρ/3 + Λ/3); at χ = π/2: **K_uu|− =
  (2πρ/3 + Λ/3) a**. And −f_,r/2 at r = a with M = (4π/3)ρa³: f_,r = (8π/3)ρa − (2Λ/3)a, so
  −f_,r/2 + 2πρa = (−4πρ/3 + Λ/3 + 2πρ) a = (2πρ/3 + Λ/3) a. **Identical to the paper's L157**
  `K_uu|− = −½ f_,r + 2πρa|Σ`. (The paper's intermediate expression L152–156 is OCR-garbled and was not used.)

**The jump ([F] = F₊ − F₋, the Barrabès–Israel convention; the paper's sign in (17) requires it):**
[K_uu] = (−f_,r/2) − (−f_,r/2 + 2πρa) = **−2πρa**, [K_θθ] = 0, [K_uA] = 0 by spherical symmetry.
p = −(1/8π)[K_uu] = **ρa/4**. Matches (17) L175–179. Energy density μ = −(1/8π) g*^AB [K_AB] = 0 (L172 "vanishing
energy density"). Numerical check (Λ = 0, a = 1 at turnaround ⇒ ρ = 3/8π, M = ½, r_s = 1): K_uu|+ = −½,
K_uu|− = ¼, [K_uu] = −¾ = −2πρa ✓, p = 3/(32π) = ρa/4 ✓.

Cross-check of the formula p = −(1/8π)[K_uu]: with the same normalisation, μ = −(1/8π)σ^AB[K_AB] reproduces the
textbook infalling Schwarzschild null shell μ = (M₊ − M₋)/(4πr²), so the paper's normalisation is the standard one.

## 2. The result — derived with sign and magnitude?

Yes, inside the paper's setup: [K_uu] = −2πρa ≠ 0 for any ρ > 0 (dust present), sign negative under [F] = F₊ − F₋,
giving p = +ρa/4 > 0. "Pressure-only" rests on [K_θθ] = 0 (L169–170), which I confirm follows from
f|Σ = cos²χ − ȧ² sin²χ, i.e. from the dust-mass relation L91 plus Friedmann (3). Note a fact the paper does not
state: the Λ-terms cancel between K_uu|+ and K_uu|−, so **[K_uu] = −2πρa is Λ-independent**; the only way the jump
could vanish is ρ = 0, which is not Pathria's model.

**Rigor caveat (auditor's own analysis, does not change the domain but bounds the strength of "p = ρa/4").**
The identification is really of a single 2-sphere: the FRW equator at turnaround has both null expansions zero
(dr = ȧ sinχ dt + a cosχ dχ = 0 there), i.e. it is the analogue of the bifurcation sphere of the SdS horizon; the
paper's own word is "instantaneously" (L50–51). Along the interior null cone, r = a sinχ = a_m − 2πρa_m³ δ² + O(δ³)
(δ = χ − π/2, using dt/dχ|Σ = −a and 1 − äa = 4πρa²), whereas along the exterior horizon r ≡ r_s. So the first
junction condition r|₋ = r|₊ (L101) holds only ON the sphere, and the third condition f du = −2dr (L103) reads
0 = 0 on the horizon, so it does not fix the parameter map u(χ). The paper fixes it by (10) with the identity
f = cos²χ − ȧ² sin²χ, which for a constant-M exterior is true only at χ = π/2 (L91–92 treats (4π/3)ρr³|Σ as constant;
along Σ it equals M sin³χ). K_uu is a derivative along Σ, so its value depends on this extension. In the alternative,
metric-continuous extension (keep M constant, take the exterior null ray f du = −2dr with r = a sinχ), I find
K_uu|− = −f_,r/4, so [K_uu] = −f_,r/4 = −(a/6)(4πρ − Λ), p = (4πρ − Λ)a/(48π) (= ρa/12 at Λ = 0, a factor 3 below
the paper's value), AND [K_θθ] = 3/(a(4πρ − Λ)) ≠ 0, i.e. the shell is no longer pressure-only. What is
extension-independent: in every extension the junction is NOT smooth (some [K_ab] ≠ 0; the paper's one gives
[K_uu] ≠ 0, the metric-continuous one gives [K_θθ] ≠ 0 and, for Λ < Λ_c, [K_uu] ≠ 0 as well). What is
extension-dependent: the specific "pressure-only, p = ρa/4". The record's clause "[K_uu] ≠ 0" is safe; the clause
"p = ρa/4" should be read as the paper's formal value in its χ = π/2 evaluation, not as an invariant of the setup.

## 3. Domain — exactly as stamped?

- **0 ≤ Λ ≤ Λ_c:** Pathria's range, L31–32, L40. The derivation needs Λ only for the existence of R_max = R_s
  (L38–41); the jump −2πρa does not depend on Λ, and it stays nonzero at the endpoint Λ = Λ_c (there K_uu|+ = 0 since
  f_,r = 0, but K_uu|− = 2πρa). Nothing in the paper widens the range beyond Pathria's. (Minor: L32 prints
  Λ_c = (2πρR³)⁻²; from f = f_,r = 0 with C = 2M = (8π/3)ρR³ one gets Λ_c = 4/(9C²) = (4πρR³)⁻²; OCR or a paper
  typo, immaterial to the jump.)
- **Dust-mass relation:** essential. L91 is used to get f = cos²χ − ȧ² sin²χ (L143–147, the [K_θθ] = 0 step) and in
  f_,r inside (14)/(16). With any other M the shell acquires surface energy density and the sphere is not at the
  horizon.
- **Surface choice:** essential. The evaluation is at χ = π/2 at maximum expansion (L98–99, L160–161, L184–185).
  The paper does not examine any other null surface; it does not claim the result for other surfaces.
- **Timelike junction:** the paper's own words (L204–209): Knutsen's timelike matching is a different treatment; the
  paper only remarks that "in the limit when the timelike hypersurface … is moved to the Schwarzschild horizon, it
  becomes a null hypersurface" studied here. No exclusion of timelike junctions is claimed here.
- **Does it claim more than stamped?** No. Abstract L21–23: "the matching is not smooth, and in fact, the null
  hypersurface is the history of a null shell admitting a surface pressure." Conclusion L194–197: the transition
  "can only be done through a null shell which is simply characterized by a surface pressure." The word "untenable"
  (L206) is attributed to Knutsen, not asserted by the author. So the stamped closing sentence ("Shell-bearing
  realizations and other FRW/black-hole junction classes are not excluded") is exactly the paper's own scope.

## 4. Ownership of proof

Formalism is cited ([3] L54–55, [5] L227, [4] L225): definition of K_ab, pseudo-inverse, the p and μ formulas. The
application — the two metrics, the null surface, the tangent/transverse vectors, K_θθ and K_uu on both sides, the
jump, and p = ρa/4 — is the paper's own (L98–186). Knutsen [6] is referenced only in the "Note added" (L198–209)
as a parallel, timelike treatment; nothing of the present result is imported from it. The no-smooth-junction result
is proved HERE, at the level of rigor described in §2 (formal evaluation on the χ = π/2 sphere).

## 5. Tier consequence

THEORETICAL-OBSTRUCTION holds with the stamped domain. The operative result of the paper IS the exclusion: the
abstract (L21–23) and the conclusion (L194–197) state that the identification R_max ≡ R_s cannot be realized as a
smooth junction — a null shell is required. This is not a parameter exclusion inside a construction (entry-37
convention): the paper builds no model of its own; its only output is that Pathria's shell-free identification fails
the second junction condition. Domain: neither wider (the paper excludes only the smooth realization of Pathria's
specific surface/exterior/mass relation, and says so) nor narrower (every element of the stamped domain is used and
none is dropped; the Λ range is Pathria's and the jump is nonzero throughout it, endpoint included). Not
CONSISTENCY-ONLY: the paper is not checking Pathria's numbers for coherence, it is proving a no-go for the smooth
case. Tier-adjacent note for the record-keeper (no tier change proposed): the sub-clause "pressure-only null shell,
p = ρa/4" is the paper's formal value in its χ = π/2 evaluation and is extension-dependent (§2); "[K_uu] ≠ 0" and
"not smooth" are the robust content. If the record wants to be bullet-proof, append "(as computed in the paper's
evaluation at χ = π/2)" after "p = ρa/4"; the tier and the stamped domain do not move.

## Plain-language paragraph

Pathria said: a closed dust universe reaches its biggest size exactly at the radius where an outside observer would
see a black-hole horizon, so maybe our universe sits inside a black hole. Khakshournia asks: if you actually try to
sew the inside universe to the outside black hole along that horizon, do the two pieces of spacetime fit together
seamlessly? I redid the sewing calculation from the two metrics myself. The angular parts fit, but the part along the
light-like seam does not: the mismatch is −2πρa, which is never zero as long as there is any matter inside, and it
does not even depend on the cosmological constant. So a seamless join is impossible; you would need a thin sheet of
"surface pressure" at the horizon — the paper's number for it is ρa/4 — and that is exactly what the record says. My
one caution: the seam is really just one sphere at one instant, so the exact size of that pressure depends on how
you extend the calculation slightly off the sphere (a different, equally natural extension gives a different number
and also a nonzero surface energy), but "no seamless join" survives every way of doing it. The obstruction tier and
its stamped domain stand.
