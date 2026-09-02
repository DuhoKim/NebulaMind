AUDIT_DOMAIN_NARROWER

# Entry 4 — Knutsen (2009), Grav. Cosmol. 15, 273 — claude-seat deep audit (BLIND)

Seat: claude-seat (Fable 5.1). Stamped: 2026-09-02 21:11 KST (`date`). Brief: `ENTRY4_AUDIT_BRIEF_20260902.md`.
Source read in full: `../bhu-reading-20260823/sources/knutsen_2009_gravcosmol15_273_clean.txt` (1,192 lines). No other
file opened; no ENTRY4_*RESULT*, SWEEP5_*, codex or kimi file touched. Line receipts refer to that file. OCR scatters
equation fragments across lines, so each receipt names the equation number as well.

**Verdict in one line.** The junction algebra is real and displayed, but at r_b = 1 it forces `Ṫ·B = 0` (eq. 36→44), and
the paper's reading of that as "the fluid sphere is static … merges with its event horizon" (lines 1084–1087) is a one-
sentence inference in words that its own standing assumption (eq. 24, T timelike) does not license. Re-deriving the same
conditions shows the smooth solution at r_b = 1 is the zero-Killing-energy boundary geodesic: non-static, expanding then
recollapsing, with the surface on or inside the horizon at all times (B = −Ȧ²/c² ≤ 0) and touching it only at maximum
expansion. What is actually derived is narrower than stamped: *no smooth matching at r_b = 1 puts the surface outside the
horizon (in the T-timelike region)*; the "static sphere" clause is not derived, and the "cannot describe our expanding
universe" clause rests on the light-cone argument in words at lines 498–504, which covers only the collapse phase.

---

## 1. The matching — formalism, conditions, derived or cited

- **Formalism.** Continuity of the first and second fundamental forms across Σ (Darmois-type), in the concrete recipe of
  Santos [10] as used by Bonnor–de Oliveira–Santos [11], with unit normals per Bonnor–Vickers [12]. The paper does not
  use the names Darmois/Israel/Lichnerowicz; it says "sufficient and necessary conditions for smooth matching across the
  surface Σ of the interior region V− with a perfect fluid and the vacuum exterior V+" and "We find it most convenient to
  follow the procedure given by Santos [10]" (lines 518–525). No surface layer (Israel shell) is ever mentioned.
- **Surface.** Σ: `r − r_b = 0` in V−, `R − R_b(T) = 0` in V+ (eq. 17–18, lines 531–532). Interior k = 1 FLRW (eq. 1,
  lines 43–66); exterior Schwarzschild–de Sitter with Λ, `B ≡ 1 − 2m/R − ΛR²/3` (eq. 7, lines 245–282; eq. 31, lines
  808–815). Birkhoff with Λ is invoked so the exterior is fixed regardless of radial motion (lines 284–289).
- **First fundamental form** (eq. 22–23, lines 603–642): `A(t) ≡ a(t) r_b = R_b(T)` and
  `dT/dt = [B − (1/c²) B⁻¹ (dR_b/dT)²]^(−1/2)`, **under the assumption (eq. 24, lines 652–689)** that the bracket is `> 0`
  "so that T is a timelike coordinate". This assumption is load-bearing for §5 (see item 2).
- **Second fundamental form** (eq. 28, lines 753–776): normals `n⁻_i = (0, a/√(1−r²), 0, 0)` (eq. 26, lines 730–743),
  `n⁺_i = (−Ṙ_b, Ṫ, 0, 0)` (eq. 27, line 744); `K⁻_θθ = r√(1−r²)·a` (eq. 29, lines 788–793), `K⁺_θθ = Ṫ R B`
  (eq. 30, lines 797–804); `K⁻_tt = 0` (eq. 32, lines 817–819); `K⁺_tt` (eq. 33, 35, lines 838–898). Angular matching
  gives **eq. 36: `Ṫ B = √(1 − r²)`** (lines 911–922); differentiating gives eq. 37–38; `K_tt` matching gives
  **eq. 40: `R̈ = −c² D`, `D = m/R² − ΛR/3`** (lines 950–964).
- **Pressure at the boundary is derived, not assumed:** inserting eq. 22 and 40 into the FLRW pressure equation (eq. 41,
  lines 966–982) gives eq. 42 (lines 988–1008), and with eq. 36 "the interior region with an FLRW metric and a perfect
  fluid is matched smoothly with the exterior false vacuum only if the pressure vanishes at the surface" (lines
  1012–1016); since p = p(t) only, "the pressure is zero identically. Hence, the fluid sphere is a dust sphere" (lines
  1018–1020). The mass identity `m = (4πG/3c²) ρ a³ r_b³` (eq. 13, lines 415–422; eq. 43, lines 1025–1050) follows from
  the same conditions.
- **Seat re-derivation (independent check).** With g^{rr} = (1−r²)/a² one gets Γ^r_θθ = −r(1−r²), hence
  K⁻_θθ = a r√(1−r²) ✓; exterior Γ^R_θθ = −RB gives K⁺_θθ = ṪRB ✓; the normal (−Ṙ, Ṫ) has norm
  −Ṙ²/(c²B) + BṪ² = 1 exactly when eq. 34 holds ✓. Combining eq. 34 (`c²B = Ȧ²/(BṪ²−1)`) with eq. 36 yields the
  compact identity **`Ȧ²/c² = (1 − r_b²) − B(A)`**, i.e. `Ȧ²/c² = 2m/A + ΛA²/3 − r_b²`, which is the k = 1 Friedmann
  equation (eq. 5) multiplied by r_b² iff `2m = C r_b³` — eq. 13 recovered ✓. Inserting into eq. 41 the pressure
  cancels term by term (`−2c²m/(a³r_b³) + 2Λc²/3 − c²/a² + 2c²m/(a³r_b³) + Λc²/3 + c²/a² − Λc² = 0`) ✓. The matching
  conditions are correctly derived in the paper, and the dust and mass results are sound for every r_b.

## 2. The application to r_b = 1 — displayed algebra vs. argument in words

- **Displayed algebra (lines 1063–1082):** "With the condition K⁻_θθ = K⁺_θθ at the boundary, it is now seen from Eqs.
  (29) and (30) that Pathria's choice r_b = 1 yields  1 − 2m/R_b(T) − (1/3)ΛR_b²(T) = 0  (44)". That is eq. 36 with
  √(1−r_b²) = 0, i.e. `Ṫ B = 0`, then divided by Ṫ. The division is legitimate only under eq. 24 (Ṫ finite and
  non-zero, T timelike, B > 0). Nothing else is displayed.
- **The step that forces the static sphere is in words, not algebra (lines 1084–1088):** "Hence, this choice of boundary
  value for the comoving radial coordinate just means that the fluid sphere is static, and the surface of the fluid
  sphere merges with its event horizon. Thus this particular model cannot describe our expanding universe." The
  inference is: B(R_b(T)) = 0 for all T ⇒ R_b sits at a fixed root of B ⇒ R_b = const ⇒ Ȧ = ȧ r_b = 0.
- **Why the step does not hold on the paper's own terms.** (i) A surface at constant R = R_s with B = 0 is the null
  horizon itself, but Σ was defined with the timelike induced metric `−c²dt² + A²dΩ²` (eq. 19, lines 534–539) and eq. 24
  demands the bracket be strictly `> 0`; the "static at the horizon" configuration violates both, so it is not a
  solution of the junction conditions the paper wrote down. Within assumption 24 the honest conclusion is *no smooth
  matching exists at r_b = 1 with the surface in the B > 0 region* — an emptier statement than "static sphere".
  (ii) Dropping assumption 24 (as one must, because the paper itself says at lines 498–504 the surface is inside its
  horizon), the identity from item 1 gives at r_b = 1: **`B(A) = −Ȧ²/c² ≤ 0`**, with equality only where Ȧ = 0. Then
  `Ṫ B = 0` with B < 0 forces `Ṫ = dT/dt = 0`: the boundary runs along T = const, which inside the horizon (T spacelike)
  is a perfectly good timelike curve — the radial geodesic of zero Killing energy E = BṪ = 0. Checks: induced metric
  `−c²BṪ² + Ṙ²/B = Ṙ²/B = −c²` ✓; K⁺_θθ = ṪRB = 0 = K⁻_θθ at r = 1 (the equator ψ = π/2 of the 3-sphere is totally
  geodesic in the angular directions) ✓; K_tt: R̈ = −c²D is exactly the second derivative of `Ȧ² = c²(2m/A + ΛA²/3 − 1)`
  ✓. So the full smooth junction is satisfied by a **non-static** boundary that expands from A = 0 to A_max (the root of
  B, i.e. Pathria's a_max = R_s; lines 218–220) and recollapses, never leaving B ≤ 0. This is the χ_b = π/2 limit of the
  Oppenheimer–Snyder junction (boundary energy E = cos χ_b → 0), whose maximum-expansion sphere is the bifurcation
  two-sphere of the maximally extended vacuum; the expansion phase lies in the past-trapped (white-hole) region, which
  Schwarzschild coordinates (T, R) do not chart — hence the paper's "static" reading.
- **Consequence.** The r_b = 1 junction is not degenerate and not static; the paper's own eq. 13/43 (lines 424–426:
  Pathria's mass "same only if r_b = 1"; lines 1022–1024: "our formula (13) … is confirmed") shows that Pathria's
  a_max = R_s identity is the junction condition at r_b = 1, not a coincidence. The paper's verdict that "this particular
  model cannot describe our expanding universe" (line 1087–1088) is asserted from the mis-read static branch.

## 3. Domain — what the result depends on, what escapes, what the paper claims beyond it

- **Perfect fluid:** assumed as the interior (line 520), but dust is then *derived* (lines 1012–1020); the result does not
  depend on a chosen equation of state.
- **Vacuum exterior:** yes — Schwarzschild–de Sitter by Birkhoff with Λ (lines 284–289); Λ ≠ 0 is included throughout
  (eq. 7, 31, 44), so "Λ ≠ 0" does not escape; the r_b = 1 statement is Λ-independent in form.
- **Smoothness (no surface layer):** essential; the paper never mentions shells, surface layers or Israel junctions —
  nothing said either way, so shell-bearing junctions are simply outside the paper (stamped wording "not excluded" is
  correct).
- **Specific r_b = 1:** the static/horizon claim is §5 only (lines 1063–1088). For other boundaries the paper explicitly
  has "no objections if the FLRW metric is employed to examine what happens to a homogeneous and isotropic contracting
  fluid sphere or matter distribution expanding into a false vacuum if the condition R_b > R_s is fulfilled" (lines
  491–496). r_b > 1 is not treated in r-coordinates; in ψ-coordinates the paper notes ψ > π/2 encloses more than half
  the universe with decreasing area (lines 1115–1125) but derives nothing there.
- **The paper itself names no escape routes** (no shells, no other boundary values, no alternative exteriors are discussed
  as loopholes).
- **Claims beyond the stamped domain (all in words):** abstract, "our expanding universe cannot be inside the event
  horizon of the vacuum metric" (lines 14–15) — an outright, general claim; the light-cone argument "If the surface of
  the fluid sphere is inside its own event horizon, all light cones in the vacuum region between this surface and the
  Schwarzschild surface point inward. Hence, a particle at the surface has no choice but to move inward" (lines
  498–504) — true in the future-trapped region only, and asserted before any matching is done; "There simply does not
  exist a firm ground outside a closed universe where a distant observer can stand" and "the very concept is
  meaningless" (lines 1127–1136); closing "careless notation and confused concepts" (lines 1140–1145). None of these is
  derived. Note also the paper's stated policy of not choosing k a priori (lines 116–122), so it does not claim "the
  universe cannot be a black hole" as a theorem — it claims Pathria's interpretation is wrong (line 14).

## 4. Ownership of proof

- Cited machinery: Santos [10], Bonnor et al. [11] (junction recipe, lines 523–525, 749), Bonnor–Vickers [12] (normals,
  lines 698–700), Eisenstaedt [9] (mass function with Λ, lines 431–433, 1052–1055), Bonnor [2] (Birkhoff with Λ, lines
  284–286).
- Done here: the explicit FLRW–(Schwarzschild–de Sitter) junction with Λ (eq. 17–43), the p = 0 result, the mass identity,
  and eq. 44 with its interpretation. The p = 0 / m = (4πG/3c²)ρa³r_b³ results are the classical Oppenheimer–Snyder
  junction (not cited; no reference to Oppenheimer–Snyder 1939 or to the maximal extension), re-derived independently
  here. The static-sphere reading of eq. 44 is Knutsen's own and is the flawed step.

## 5. Relation to entry 5 (Khakshournia 2010, null shell at the maximum-expansion surface) and entry 1 (FIRED standing)

- Not read (blind, and outside this brief's single pinned source); relation inferred from the brief's one-line
  description only. **Consistent and overlapping, not independent:** the seat re-derivation shows the r_b = 1 smooth
  junction places the maximum-expansion surface exactly on the horizon (A_max = root of B, where the surface is
  momentarily null-tangent at the bifurcation sphere). A null-shell junction *at that surface* is precisely the object
  Knutsen's "static sphere merging with its horizon" is a confused picture of; the two entries look at the same surface,
  one with a smooth junction (Knutsen), one with a shell. The stamped pairing is therefore apt, but the pair does not
  add up to an exclusion: entry 4's smooth branch is a legitimate expanding-and-recollapsing configuration.
- Entry 1 (Pathria): Knutsen's own eq. 13/43 and the seat identity `Ȧ²/c² = 2m/A + ΛA²/3 − 1` at r_b = 1 make Pathria's
  a_max ↔ R_s identity an exact consequence of the junction, for any Λ (lines 218–220, 424–426, 1022–1024). Knutsen also
  notes that Pathria's deceleration input (eq. 6, lines 176–178, 222–231) was the observation of the time; this is
  independent of whatever observational ground entry 1's FIRED standing rests on. Knutsen therefore neither strengthens
  nor conflicts with a FIRED verdict on entry 1; it explains Pathria's coincidence rather than refuting it.

## 6. Tier consequence, argued

- The exclusion *is* the operative result of §5 (not a side remark), so this is not CONSISTENCY-ONLY by the entry-37
  convention.
- The obstruction is not derived with the stamped domain. Derived and sound: (a) smooth FLRW–vacuum matching forces p = 0
  and m = (4πG/3c²)ρa³r_b³ for every r_b; (b) at r_b = 1 the matching forces Ṫ B = 0, equivalently B = −Ȧ²/c² ≤ 0 —
  **the surface can never be outside its horizon, so no external observer in the B > 0 region ever sees Pathria's
  sphere, and no smooth matching exists with the surface in the T-timelike exterior.** Not derived and in fact false:
  the surface is "static"; and the derived-from-it "cannot describe our expanding universe". The correct smooth solution
  at r_b = 1 is the E = 0 Oppenheimer–Snyder hemisphere: expanding to A_max = R_s and recollapsing, entirely within
  B ≤ 0. The paper's fallback argument (lines 498–504) uses inward light cones, valid only in the black-hole (collapse)
  phase, and never charts the white-hole (expansion) phase because it stays in Schwarzschild coordinates.
- Hence **AUDIT_DOMAIN_NARROWER**: the theoretical obstruction that survives is "a smoothly matched FLRW dust sphere with
  r_b = 1 cannot have its surface outside (or visible from outside) its horizon; Pathria's 'external world with a
  detached look at our universe' is excluded". The stamped clause "forces a static sphere merged with its horizon" and
  its corollary should be struck from the domain. Whether a residual obstruction of this size still merits
  THEORETICAL-OBSTRUCTION rather than a weaker tier is tier-adjacent and is returned to Duho as a packet per the
  boundary; no tier changed here.
- Falsifier for this audit (for the reconciler): show a solution of eq. 22–24, 36 and 40 with r_b = 1 that is static.
  Eq. 36 at r_b = 1 with Ṫ finite gives B = 0 on the whole boundary, i.e. R_b = const on a null surface, contradicting
  eq. 19 (timelike Σ) and eq. 24 (strict inequality). Conversely, verify `Ȧ² = −c²B(A)` reproduces eq. 5 with C = 2m —
  three lines of algebra in item 1.

---

**Plain language.** Knutsen does the honest work of gluing an expanding dust ball onto the empty outside space and shows
that the glue holds only for pressureless dust, with the ball's mass given by the usual formula; that part is right and I
re-derived it. But when he takes Pathria's special choice — the ball is exactly half of a closed universe — his equation
says only that a certain product is zero, and he reads that as "the ball must sit still, stuck on its own horizon", from
which he concludes it can't be our expanding universe. That reading is wrong: the same equations have a different and
perfectly consistent solution in which the ball does expand and then recollapses, but its surface is always on or inside
the horizon, kissing it exactly at maximum size — which is literally Pathria's "biggest size equals Schwarzschild
radius" picture, now explained rather than debunked. Knutsen misses it because his coordinates cannot see the region
where the expansion happens. What genuinely survives from the paper is smaller than the stamped statement: such a
universe could never be watched from an outside world, because its edge never gets outside the horizon. So the
obstruction is real but narrower than stamped, and whether that narrower version still deserves the "theoretical
obstruction" label is a call for Duho.
