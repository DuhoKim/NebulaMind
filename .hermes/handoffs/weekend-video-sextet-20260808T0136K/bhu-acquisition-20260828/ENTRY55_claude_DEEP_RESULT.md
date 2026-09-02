AUDIT_HOLDS_CONSISTENCY_ONLY

# Entry 55 deep audit — claude-seat (blind, independent) — 2026-09-02 KST

Source read in full: `../bhu-reading-20260823/sources/2007.06664_clean.txt` (lines 1–1856). No other file consulted.
Arithmetic below re-done from the printed equations (scipy, Struve functions via H_{-1} = 2/π − H_1).

## 1. The construction — what is derived here vs imported

- Framework: quantum reduced loop gravity (QRLG), a partial gauge fixing of the full LQG kinematical Hilbert space, then
  expectation value of the (non-graph-changing, Thiemann-regularised, spin-1/2, fixed-graph) Hamiltonian constraint on
  coherent states peaked on spherically symmetric data (lines 104, 321–338). The base effective Hamiltonian is
  **imported** from Alesci–Bahrami–Pranzetti 2018c (line 321, 340–341); the interior dynamics, the Struve-function
  feature and the "no white hole" result are **imported** from Alesci et al. 2019 (lines 110, 115–118, 1246 fn 23).
- **New in this paper:** (i) inverse-volume and coherent-state sub-leading corrections, eqs. (25a–c), with three new free
  spread parameters δ_r, δ_θ, δ_φ (line 463: "free dimensionless parameters at this stage"), re-parameterised as
  (δ, ν, δ_x) by the ansatz (34a–c) (line 621); (ii) the simplicity-constraint choice j = γ j_x, eq. (32) (lines
  582–588: "it is consistent to require"), which makes α/β = √(2π)/(8γ) (fn 14, line 808) — this is the ONLY route by
  which γ enters the asymptotic equations; (iii) the asymptotic-series analysis of Sec. VI; (iv) the Sec. VII speculation.
- Minisuperspace: homogeneous interior foliation (2), phase space (R, Λ, P_R, P_Λ) (line 184), quantum parameters
  ε = α/R, ε_x = β/Λ with α = 2π√(γ j_x) ℓ_P, β = 4√(8πγ) j ℓ_P/√j_x (eq. 31, line 567–571).
- Approximations: large spins j̃ ≫ 1 (line 436), δ j̃² ≫ 1 (eq. 33), continuum limit ε, ε_x ≪ 1 (line 547), Lorentzian
  coherent-state corrections dropped as sub-leading (line 443), lapse (39) chosen for convenience (line 683–689), and
  the asymptotic Laurent ansatz (45a–d)/(78) truncated at three orders (line 866).

## 2. The de Sitter result — computed condition, but a tuned point, not a derived phase

- Procedure: **assume** the asymptotic form (45a–d) — which is already the de Sitter form (76) in these coordinates —
  and demand it solve the constraint + three Hamilton equations to three orders in z (line 813, 866). This yields 12
  algebraic equations in 11 parameters (L0, L1, R0, R1, R2, γ, ξ, ν, δ, δ_x, β); one is identically zero, two vanish
  when L1 = 0 (line 867), and L1 = 0 is forced by (54) (line 927). Net: 10 quantities fixed, **one free (β, i.e. the
  spin j)** (line 126: "solved by fixing all the free parameters of the theory, up to a free remaining quantum spin
  number"; line 1032).
- γ is fixed together with ξ by the two γ-only equations (52) and (53) (lines 906–919): it is a **computed root of a
  transcendental system**, not a scan and not a hand-picked value. **Re-derived:** solving (52)–(53) I obtain, for the
  + sign, (ξ, γ) = (0.974474, 0.274344) and for the − sign (0.956957, 0.226702) — Table 1 (lines 949–955) reproduced.
- But the state parameters (δ, ν, δ_x) are **tuned** to make it work, in the authors' own words: line 903 "this
  consistency mandates fine tuning for most of our quantum parameters"; Table 1 caption line 969 "parameters of the
  model that were tuned to bring about an asymptotically de Sitter geometry"; line 1229 "found by tuning most of the
  quantum parameters"; line 1354 "if we tune ξ, γ, δ, δ_x and ν"; line 135 "it precisely fine tunes the effective
  trajectory". Line 1032 argues the dS geometry "fixes all the ambiguities left in the definition of the coherent
  states" — that is the logic inverted: dS is the input that selects the state, then the state yields dS. The
  "converse" of Appendix B (line 1229) only shows: tuned parameters + Laurent ansatz ⇒ dS; robustness (line 132) is
  w.r.t. initial data (line 1354–1358), NOT w.r.t. the regularisation/state/simplicity choices in §1.
- Effective cosmological constant: eq. (59)/(67): λ = 0.06/(ℓ_P² j) — Planck units, set by the collective spin j only,
  **independent of the black-hole mass** (Gm cancels between N0 and ℓ; I verified λ = 3/(N0²ℓ²) = 6ξ²(2 sin ι + π h0)²/(πβ²)
  and, with β² = 128π γ² ℓ_P² j from (31)+(32), λ ℓ_P² j = 0.0602 for the + root — matches (67)). Bounds on j:
  1 ≪ √j ≪ Gm/ℓ_P (line 1099), coherent states fine from j ~ 100 (line 1099), curvature argument j ≲ 10⁶ (line 1118).
  Authors' own status: line 1118 "the effective theory framework leaves j, and thereby λ, largely unconstrained."
  For j = 10²–10⁶, λ ≈ 6×10⁻⁴ – 6×10⁻⁸ ℓ_P⁻², i.e. 10¹¹⁴–10¹¹⁸ × Λ_obs (= 2.85×10⁻¹²² ℓ_P⁻²). The derived λ is Planckian.

## 3. The coincidence (line 41) — an a-posteriori match, "exact" only at three digits

- Values quoted: γ₁^E ≈ 0.237 (U(1)), γ₂^E ≈ 0.274 (SU(2)), sourced to Agullo et al. 2010 (eq. 61, lines 1016–1022;
  also Engle et al. 2010 at line 132). The dS roots: γ₁^dS ≈ 0.227, γ₂^dS ≈ 0.274 (eq. 60, line 1010).
- The paper says "exact coincidence" (line 41), "exact matching" (line 1023), "precisely" (line 1016) — but quotes both
  sides to three significant figures only and gives **no precision on its own root**. My solution of (52)–(53) gives
  γ₂^dS = 0.27434; the SU(2) counting value is 0.274067 (Agullo et al. 2010; Engle–Noui–Perez–Pranzetti). They agree
  to 3 s.f. and **differ at the 4th (0.1 %)**. The other pair, 0.2267 vs 0.2375, misses by **4.6 %** and is still
  called "surprisingly close" (line 1023). With one match at ~10⁻³ and one accepted at 5×10⁻², this is a coincidence
  reported at whatever precision fits, not a controlled prediction.
- Prediction vs selection: the value was **selected by the demand** for dS asymptotics (line 126: "the demand for the
  formation of an asymptotically de Sitter universe … selects the following numerical value"; line 1089 "achieved by
  selecting a specific value for the Barbero–Immirzi parameter"); the entropy value was known before (2010) and was
  not used as input (line 1025). So it is an **independent post-hoc consistency check** between two model outputs, not
  a prediction of anything observable. The authors call it "a striking coincidence and … a long sought-after
  confirmation" (line 1028) and "consistency check" (line 1166).
- Is 0.274 unique? Within (52)–(53) the paper reports "two sets of solutions" (line 919). My root scan of the same
  two equations finds **additional roots** on both sign branches with ξ → 1 (e.g. + branch γ ≈ 0.102, 0.062, 0.035;
  − branch γ ≈ 0.095, 0.060, 0.034, …), not mentioned in the paper. Caveat: I did not test these against the
  higher-order equations (55), (56) and condition (33), which could exclude them; but the paper's uniqueness statement
  rests on (52)–(53) alone, so "unique" is at minimum under-argued. More fundamentally the number depends on the
  simplicity choice (32) (footnote 14: γ enters via α/β), the regularisation list (lines 323–338), the ansatz (34), the
  lapse (39) and the truncation order — none of which is varied. Line 1029: only the + branch is reached from
  Schwarzschild data (numerical claim, no figure), so 0.274 is "unique" only for that branch and those choices.

## 4. Observation-facing content — the identification is made, conditionally, in Sec. VII only

Sections II–VI are a black-hole-interior statement: "asymptotically Schwarzschild–de Sitter" interior with a spacelike
scri ℐ⁺_int (line 1069), zero gravitational charge (line 1073–1082), symmetry group ℝ⋊SO(3) not maximally symmetric
(line 1085: "the symmetry Lie group of the interior region remains isomorphic to ℝ⋊SO(3)"), Kantowski–Sachs expanding
universe inside the horizon (line 1164–1165). Sentences bearing on "universe inside":
- line 41: "strongly suggestive of deep ties between the area gap in loop quantum gravity, black hole physics, and the
  observable universe … an intriguing relation between the measured value of the cosmological constant and the
  observed mass in the universe from a proposal for a spin quantum number renormalization effect".
- line 137: "whether … can provide an alternative viable 'black hole cosmology' scenario with possible experimental
  tests clearly depends on the value of the cosmological constant … While we intend to address this intriguing
  scenario in a separate work".
- line 1140: "if our universe hides behind a black hole event horizon, then this quantity as perceived by an observer
  in the mother universe should correspond to the mass of the matter content of our observable baby universe" —
  with m ≃ 1.46×10⁵³ kg (baryons, Planck 2018) ⇒ λ̄ ≃ 0.85×10⁻⁵² m⁻² vs λ_obs ≃ 1.1×10⁻⁵² m⁻² (line 1144).
- line 1146: "Before leaving this intriguing observation as a starting point for future investigations about possible
  observables effects of our model … We leave the details of this proposal for future work."
- line 1150–1155: places itself in the Pathria 1972 / Frolov–Markov–Mukhanov lineage; line 1173: "lends credence to
  … cosmological natural selection".

**Status of the number.** It is not an output of the model. The derived λ is 0.06/(ℓ_P² j) (Planckian). The observed
value is reached only through eq. (70), j̄ ~ j_i N_i² ~ (Gm/ℓ_P)², which is a **proposal** justified by dimensional
analysis (line 1138: "we are left with no natural option") and explicitly conditional (line 1140: "If the expression
(71) … can indeed be obtained"); O(1) factors are dropped (fn 21, line 1143) — including the 0.06 itself.
**Arithmetic check:** Gm/c² = 1.084×10²⁶ m ⇒ c⁴/(G²m²) = 8.5×10⁻⁵³ m⁻² (paper's 0.85×10⁻⁵² ✓); Planck-18 Λ = 3H0²Ω_Λ/c²
= 1.09×10⁻⁵² m⁻² ✓. Required j̄ = 2.1×10¹²⁰ vs (Gm/ℓ_P)² = 4.5×10¹²¹ — the "0.06" would spoil the match by ×20 if kept.
**What the coincidence actually is:** 1.46×10⁵³ kg is the baryon mass inside R ≈ 14 Gpc ≈ 3.2 c/H0 (the particle
horizon). Then Gm/c² = Ω_b (H0R/c)³/2 · c/H0 = 0.79 c/H0, so λ̄ = 1.6 H0²/c² vs Λ_obs = 3Ω_Λ H0²/c² = 2.05 H0²/c².
The match is the flatness relation R_s(M) ~ R_H rephrased with Ω_b × geometric factor ≈ 0.8 — no information about
the model survives in it. Using total matter (Ω_m = 0.315) instead of baryons gives λ̄/Λ_obs = 0.019 (factor 52 short);
the choice "baryons only" (fn 21) is what makes the number land. Not a test; not falsifiable as stated.

## 5. Tier consequence — HOLDS at CONSISTENCY-ONLY; Sec. VII is tier-adjacent (PROSPECT-candidate), returned as a packet

- **Not AUDIT_FLAG_MEMBERSHIP:** the paper does make the corpus identification (line 1140), conditionally, and its
  title/discussion place it in the black-universe lineage (lines 1150–1166). Membership fine.
- **Not CALIBRATED-FALSIFIER:** the only number (λ̄ ≈ 0.85 vs 1.1 ×10⁻⁵² m⁻²) is not derived (eq. 70 is a proposal), has
  no stated tolerance (O(1) conceded, and the derived prefactor 0.06 is silently dropped), depends on a free choice of
  which mass to insert (baryons vs total: factor 52), and reduces to the flatness coincidence. "The lane may own a
  missing threshold, never a missing number": here the number exists but is not the model's — a lane threshold would
  be calibrating dimensional analysis, not the paper. Fails.
- **Not QUALITATIVE-DIRECTIONAL:** the sign Λ > 0 is an input of the ansatz (45)/(76) (the Ashtekar–Bonga–Kesavan 2015
  positive-Λ criterion is what is imposed), not an output; and it is conditional on the tuned point. The genuinely
  qualitative interior statements (ℝ⋊SO(3) symmetry, Kantowski–Sachs anisotropy, no inner horizon, immediate
  inflation after the bounce, lines 1085/1163–1165) are not connected by the paper to any observable of our universe.
- **PROSPECT?** The one honest case for a change: the paper names a mechanism (emergent Λ ∝ 1/j, renormalised to
  c⁴/G²m²), attaches it to a corpus quantity (mass of our universe as seen from the mother universe), and labels it a
  "starting point for future investigations about possible observable effects" (line 1146), with a follow-up paper
  promised (line 137). If the lane's PROSPECT tier admits an author-deferred, non-derived route, Sec. VII qualifies as
  one; the constructive body of the paper (Secs. III–VI) does not. My reading is that a proposal whose only numerical
  content is degenerate with flatness does not constitute a prospect the lane could ever cash, so I hold the tier and
  flag Sec. VII for Duho rather than promote it. (Brief's "A(a)" clause not resolvable from the brief alone; if it
  means "adjudicate on the paper's actual result, not its speculation", it points the same way — hold.)
- The b33 finding (strong branch/parameter exclusions, zero gravitational charge) is confirmed from the source (lines
  1029, 1073–1082, Table 1) and untouched.

## Plain language

This paper asks whether the inside of a black hole, once quantum effects stop it from crushing to a point, could open
out into an ever-expanding space like the one we live in. The answer it gets is "yes, but only if you dial the knobs
just so": three settings of the quantum state and one fundamental constant of loop quantum gravity (γ) have to take
specific values, and the authors themselves repeatedly call this "tuning". The headline is that the value of γ that
comes out, 0.274, is the same number another group had found years earlier from counting black-hole entropy. I redid
their equations and got the same 0.274 — but only to three digits; at the fourth digit the two numbers part ways
(0.2743 vs 0.2741), and the paper's second root misses its entropy partner by 5 %. So it is a real, interesting
coincidence between two calculations, not a prediction of anything we can observe. The one place the paper talks about
OUR universe is a short speculation at the end: if you assume a large "renormalisation" of the quantum spin (which
they do not derive), the dark-energy constant comes out near the measured one — but I checked, and that match is just
the old fact that a universe at critical density has a Schwarzschild radius about the size of its horizon; pick the
total mass instead of baryons only and the match is off by fifty. So: a consistency construction inside a black hole,
plus a speculative footnote about us. The tier holds where it is; the end-section speculation goes to Duho as a
note, not as a promotion.
