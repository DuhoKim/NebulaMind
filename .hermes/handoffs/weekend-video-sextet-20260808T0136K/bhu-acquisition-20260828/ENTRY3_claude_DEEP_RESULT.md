AUDIT_HOLDS_CONSISTENCY_ONLY

# Entry 3 deep audit — claude-seat (BLIND, independent) — 2026-09-02 21:13 KST

**Source read:** `../bhu-reading-20260823/sources/stuckey_1994_observable_universe_black_hole_ajp62_788.pdf`,
sha256 `91aa1fae9327b9f05f81fb3c0b5a37cccdee08f2d0d9870dc6420a9247ea64ce`. Read visually, every page. Pin note: the
PDF has **9 pages, not 8** as the brief says — an AIP cover sheet (PDF p.1) plus journal pp. 788–795 (PDF pp. 2–9).
Page 795 (Fig. 7, conclusion, acknowledgments, all references) IS present at PDF p.9; nothing is missing. Page
receipts below use the printed journal page numbers. Equation-dense pages (789, 790) were re-rasterized at 170 dpi
and read column by column. No ENTRY3_*RESULT*, SWEEP5_*, agy/codex/kimi file was opened.

## 1. The construction — what is actually shown

**Section II (p. 789), worked in full.** Stuckey defines a Schwarzschild-like areal radius in all three dust FRW
models, R = a sinχ / aχ / a sinhχ (Eq. 2), defines M as the mass inside R = R_n by M = 4πR_n³ρ/3 (Eqs. 3–4, the
Misner–Sharp mass), and asks where a worldline of constant R is null. Setting dR/dτ = 0 (Eq. 5) with a dχ/dτ = c
gives c = tanχ_n ȧ / χ_n ȧ / tanhχ_n ȧ (Eq. 6). With the dust solutions ȧ = c cot(η/2), (9B/4)^{1/3}·2/(3τ^{1/3}),
c coth(η/2) (Eq. 7) this yields χ_n = η/2 in all three models (Eq. 10), and then 2GM/c² = R_n identically (Eq. 11),
"as claimed" (p. 789). He states plainly what this sphere is: "There is a sphere R = R_n about the origin on which
constant R worldlines are null, and the Schwarzschild mass M within this sphere is R_n c²/2G" (p. 789). He then
shows a *non*-Schwarzschild feature: the proper mass M_p (Eq. 12) does not obey Eq. 11 except in the flat model;
instead M_p = 3τc³/4G in all three models (p. 789). On p. 790 he is explicit that "the R = R_n sphere (an apparent
horizon or Hubble sphere) is not an event horizon," that "there are no event horizons in either the flat or open
models," and that every comoving observer sits at the center of such a sphere "since space is everywhere isotropic
according to the cosmological principle." The Sec. II result is therefore an identity of the FRW apparent horizon,
and the paper says so: "The result R_n = 2GM/c² of Sec. II is only suggestive" (p. 788).

**Section III (pp. 790–793), worked in full.** The real content: an Oppenheimer–Snyder-type junction of a dust FRW
ball (all three k) at comoving χ = χ_0 to Schwarzschild vacuum (Fig. 2, p. 792), citing Birkhoff (ref. 13) and the
two junction conditions from MTW (ref. 14): (i) the induced 3-metric agrees — the interface worldline in Schwarzschild
coordinates is written for flat (Eq. 14), closed (Eqs. 15–16) and open (Eqs. 17–18) with α = B sinχ_0/4M etc., then
Eqs. 19–25 show the induced metrics match; (ii) the extrinsic curvature agrees — computed from the Friedmann side
(Eqs. 26–34: K⁰_i = 0, K¹_1 = K²_2 = −cosχ_0/(a sinχ_0) etc.) and from the Schwarzschild side (Eqs. 35–46: n_t, n_r,
the Christoffels of Eq. 43, K¹_1 = −cosχ_0/r), and shown equal. "Therefore, Eqs. (14)–(18) describe the connection
between Friedmann dust and Schwarzschild vacuum" (p. 793). Fig. 3 (p. 793) plots the interface worldlines of the
three models on the Kruskal plane.

**Section IV (pp. 793–795), argued in prose.** The dust may replace the *interior* (Figs. 2, 5) or the *exterior*
(Figs. 4, 6, 7) of the junction sphere; for the closed model the choice is fixed by the sign of n_r = cosχ_0
(exterior if χ_0 > π/2, interior if χ_0 < π/2; p. 794), for flat/open either is allowed. Interior-replacement
"precludes the possibility of a Schwarzschild throat" (p. 794); exterior-replacement leaves a Schwarzschild throat
between Kruskal regions I and III with the mass M "in the singularity at r = 0 ... Friedmann dust not ejected from
the Big Bang singularity" (p. 794), and then "region III lies through the black hole horizon of region I and vice
versa ... One may say the Friedmann dust lies inside the white or black hole of region III. (The converse statement
is equally true, of course.)" (p. 794).

**Cited, not worked:** Birkhoff's theorem (ref. 13, Weinberg), the junction conditions themselves (ref. 14, MTW),
the Schwarzschild interface trajectories Eq. 14 "adapted from ref. 14" (ref. 15), the dust solutions a(η), the
Kruskal extension, and the horizon nomenclature (ref. 12, Harrison; Ellis & Rothman).

**Adversarial checks on the algebra (all mine, from the paper's stated forms):**
- Eq. 8 as printed, "B = aȧ² = 8πGρa³/3 (is a constant)," is correct only for the flat model. For closed/open dust
  aȧ² = B cos²(η/2) resp. B cosh²(η/2), not a constant; only the second equality (B ≡ 8πGρa³/3) is constant and is
  what Eqs. 10–11 actually use via a = (B/c²) sin²(η/2) / sinh²(η/2). Harmless slip; no downstream result depends
  on it.
- Eqs. 6–7 → 10: verified (ȧ = c cot(η/2) from a = (B/c²)sin²(η/2), dη/dτ = c/a). Eq. 11 verified in all three
  models (see §2). Eq. 12 → M_p = 3τc³/4G verified in all three models (see §2).
- Tangential prose claim, p. 790: "The apparent horizon does reside at an event horizon of the closed universe at the
  point of maximum expansion." With the standard closed-dust relations χ_AH = η/2 (the paper's own Eq. 10) and
  χ_EH = 2π − η, the two coincide at η = 4π/3, not at maximum expansion η = π (where χ_AH = π/2, χ_EH = π). I could
  not consult ref. 12 to see whether a different definition is meant; the remark carries no weight in the argument.
- The junction algebra (Eqs. 33 vs 46, K¹_1 = −cosχ_0/(a sinχ_0) = −cosχ_0/r with r = a sinχ_0) is internally
  consistent and is the standard Oppenheimer–Snyder result; I did not find an error.

## 2. Numbers — there are none in the paper; recomputation of what it does state

**Finding:** the paper contains **no numerical input or output** — no H₀, no ρ, no age, no "mass of the observable
universe," no Schwarzschild radius in metres, no galaxy count. Every page was read; the only quantitative content is
the closed-form identities R_n = 2GM/c² (Eq. 11), R_n = 3cτ/2 in the flat model (Eq. 11, middle line), and
M_p = 3τc³/4G (p. 789). This paper is therefore not the source of any "M_universe ≈ its Schwarzschild radius"
number that circulates in the BHU literature; it supplies only the identity behind such numbers.

**Recomputation A — the identities themselves, from the paper's stated inputs (Eqs. 4, 6–8, 10, 12).**
Flat: a = (9B/4)^{1/3}τ^{2/3} ⇒ ȧ = (2/3)a/τ, χ_n = c/ȧ = (3cτ^{1/3}/2)(4/9B)^{1/3} (matches Eq. 10),
R_n = aχ_n = 3cτ/2 = c/H (matches Eq. 11). With ρ = 3H²/8πG = 1/(6πGτ²): M = 4πρR_n³/3 = (4π/3)(27c³τ³/8)/(6πGτ²)
= 3c³τ/4G, and 2GM/c² = 3cτ/2 = R_n. ✓ Closed: a = (B/c²)sin²(η/2), cτ = (B/2c²)(η − sinη);
M_p = 4πρa³(χ_n/2 − sin2χ_n/4) with χ_n = η/2 and 4πρa³ = 3B/2G gives (3B/8G)(η − sinη) = 3c³τ/4G ✓;
2GM/c² = (B/c²)sin³χ_n = a sinχ_n = R_n ✓. Open: same with sinh, M_p = (3B/8G)(sinhη − η) = 3c³τ/4G ✓,
2GM/c² = a sinhχ_n ✓. Numerically checked at η = 1.7 (B = c = G = 1): M_p/(3τ/4) = 1.000000, 2M/R_n = 1.000000
for both curved models.

**Recomputation B — an instantiation with an input the paper does NOT give (mine, for scale only).** Taking
τ = 13.8 Gyr in the paper's flat dust model: H = 2/3τ = 47.2 km s⁻¹ Mpc⁻¹, ρ = 4.19×10⁻²⁷ kg m⁻³,
R_n = 3cτ/2 = 1.958×10²⁶ m = 6.35 Gpc, M = M_p = 3c³τ/4G = 1.319×10⁵³ kg = 6.6×10²² M_⊙, and
2GM/c² = 1.958×10²⁶ m — ratio to R_n = 1.000000 by construction. Note the model-dependence this exposes: in the
real (ΛCDM) universe H₀τ₀ ≈ 0.95, not 2/3, so the paper's R_n = 3cτ/2 overshoots the actual Hubble radius
c/H₀ ≈ 4.4 Gpc by ~45 %; the identity R_H = 2G M(<R_H)/c² itself survives in any flat FRW model when M counts the
total density (including Λ), because it is just the Friedmann equation H² = 8πGρ/3 rewritten at R = c/H. In no case
is it a measured coincidence.

## 3. Claims about observation — IS / COULD / coordinate point?

**COULD, conditional, and explicitly symmetric.** Verbatim:
- Abstract (p. 788): "In the resulting cosmology model, the observable universe **may** lie inside a black or white
  hole."
- p. 788: introductory texts "stating that the Milky Way and all the galaxies of the observable universe may lie
  inside a black hole ... rarely establish the general relativistic (GR) context ... In this paper, we explain a GR
  cosmology model in which the observable universe may lie inside a black or white hole."
- p. 788: "The result R_n = 2GM/c² of Sec. II is only suggestive." and "While this result is not necessarily of
  astrophysical importance, the methodology has been used extensively by cosmologists and astrophysicists."
- p. 790: the identification requires abandoning isotropy — "But, if we discard the cosmological principle and allow
  the R = 0 observer to be at the center of a sphere of Friedmann dust surrounded by Schwarzschild vacuum, the
  R_n = 2GM/c² analogy is pertinent."
- p. 794: "we see **in what sense** the Friedmann dust (today in the form of galaxies) **may be said** to reside in a
  black or white hole." and "One may say the Friedmann dust lies inside the white or black hole of region III. (The
  converse statement is equally true, of course.)"
- p. 795: "In this manner, **if** it is part of a Friedmann dust, the observable universe **may** be inside a black or
  white hole."

So the paper never asserts the universe IS inside a black hole; it constructs a model in which the phrase can be given
a GR meaning, and it labels the meaning as a choice of which Kruskal region one calls "inside." The Sec. II
R_n = 2GM/c² relation is presented as a coordinate/teaching point (apparent horizon, not event horizon; every
comoving observer has one).

**Consequences an observation could contradict: none stated, and none derivable without a number the paper does
not give.** Curvature sign: the construction works for k = +1, 0, −1 alike (Eqs. 14–18, 23–25), so no sign is
predicted. Expansion history: inside the dust ball the metric is exactly FRW (Birkhoff), so no deviation from
standard dust expansion is predicted; the closed case "will then collapse to its final singularity (Big Crunch)
inside the black hole" (p. 794), which is just the closed-FRW fate restated. Limits: none. The one physical
commitment the model does carry — a finite dust ball with an edge at χ_0, i.e. a violation of the cosmological
principle at some scale — is left with χ_0 entirely free ("at any χ_0", p. 794) and is never connected to an
observable (no edge scale, no anisotropy amplitude, no CMB or count statistic). That is a missing *number*, not a
missing *threshold*, so under the brief's rule the lane cannot own it.

## 4. Tier consequence, argued

**CONSISTENCY-ONLY holds.** Argument:
- Against raising to PROSPECT: a prospect needs an observable the model points at. The paper offers none, declares
  the Sec. II result "only suggestive" and "not necessarily of astrophysical importance" (p. 788), and the
  Sec. III–IV construction is a demonstration that the junction is *allowed*, with the black/white-hole reading
  explicitly reversible (p. 794). Its only free parameter (χ_0) is unconstrained and unconnected to data.
- Against QUALITATIVE-DIRECTIONAL: no direction is predicted — not for the curvature sign (all three k are worked
  symmetrically), not for the expansion history (FRW inside by Birkhoff), not for any asymmetry.
- Against CALIBRATED-FALSIFIER: there are no stated inputs and no number to calibrate (§2).
- Against dropping below CONSISTENCY-ONLY: the paper does make a BHU statement in its own words (abstract, p. 794,
  p. 795) and gives it a correct, fully worked GR footing (Oppenheimer–Snyder junction in all three k), so it is a
  legitimate consistency result and belongs in the corpus at this tier.
- A(a) posture: no tier change proposed; the seat's verdict is that the existing tier is exactly right. The two
  findings the lane may want on record are (i) the Eq. 8 slip and the p. 790 event-horizon remark (both harmless to
  the tier), and (ii) the negative result that this paper is *not* a source for any numerical "the observable
  universe satisfies R = 2GM/c²" claim — it proves that relation is an FRW identity of the apparent horizon
  (H² = 8πGρ/3 at R = c/H), which is a useful weapon against pop-science citations of the coincidence as evidence.

## Plain language

This is a physics-teaching paper, and it does exactly what a good teaching paper does: it takes the popular line
"maybe our whole universe is inside a black hole" and works out, with all the equations, the one precise sense in
which general relativity lets you say that. The first half shows that in any expanding dust universe there is a
sphere around every observer whose mass and radius satisfy the black-hole formula R = 2GM/c² — and then immediately
explains that this is a built-in feature of the expansion (it is the Hubble sphere), not a black-hole horizon, and
calls it "only suggestive." I checked the algebra in all three curvature cases and it is right, apart from one
harmless slip in a defining equation; I also put in today's age of the universe to see the scale (about 6.6×10²²
solar masses inside about 6 billion parsecs), but the paper itself gives no numbers at all. The second half is the
real work: it glues a ball of expanding matter to empty black-hole spacetime, checks that the seam is legal, and
shows that depending on which side you call "inside," the matter can be described as sitting in a black or white
hole — adding that the reverse description "is equally true." Nothing here predicts anything a telescope could
confirm or refute; the paper says so itself. The existing CONSISTENCY-ONLY tier is exactly right, and the useful
by-product for the lane is that this paper is the clean proof that the "our universe fits its own Schwarzschild
radius" coincidence is not evidence of anything.
