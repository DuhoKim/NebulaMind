AUDIT_HOLDS_CONSISTENCY_ONLY

# Entry 36 deep audit — claude-seat (blind; codex/kimi results not opened)
Smoller & Temple (2000), "Cosmology with a shock-wave," CMP 210, 275–308. Source read in full:
`../bhu-reading-20260823/sources/smoller_temple_2000_clean.txt` (3,797 lines). Line numbers below refer to that file.
Written 2026-09-02 20:38 KST. Arithmetic re-derived from the paper's own constants (7.15)–(7.23), not copied.

## 1. The construction — what is proved, and what R* is

- Interior: k = 0 FRW with the post-decoupling standard equation of state, radiation P = α/R⁴ plus pressureless matter
  Q_m = β/R³ (eqs. 4.13–4.14, lines 1583–1590). Exterior: static TOV. Interface: an outgoing shock across which
  Rankine–Hugoniot holds and no delta sources appear (Theorem 3, lines 1118–1150).
- Theorems actually proved: Theorem 1 (ODE 3.10 ⇒ conservation 3.11, line 500); Corollary 1; Lemma 1 (3.36 ⇒ TOV eq.
  2.8); Theorem 2 (the closed system 3.41–3.42 for (r, P̄), line 999); Theorem 3 (matched metric is a weak shock
  solution, C^{1,1} transformation, line 1118 — proof imported from ref. [13]); Theorem 4 (phase plane of 5.16–5.17:
  a unique orbit w_crit bounded for all R, with 1/9 < w < σ̄ = √17−4 ≈ .1231 along it, lines 2011–2028, 2471);
  Lemmas 3–4 / Theorem 5 (Q̄ > 0 and Q̄ > P̄, once true at R*, stay true for R > R*, lines 2542, 2772, 2867).
- What is NOT proved: no Lax/entropy condition is proved — "entropy" appears only as motivation (lines 76, 164); the
  admissibility actually imposed is positivity Q̄ > 0 and Q̄ > P̄, called "physically reasonable" (line 2487).
  Subluminal shock speed is a hypothesis of Theorem 3 (line 1125), not a result. Uniqueness is only of the bounded
  P̄-orbit; the paper says outright that this orbit "does not constrain either the initial shock position or the TOV
  energy density" (lines 147–149). Restricting to the critical orbit is itself a modelling choice (lines 2918–2920).
- R*: "starting time" — the scale factor "at which we start the shock–wave" (line 231); "the earliest time at which the
  shock–wave solution has settled down to the point where our model applies" (lines 161–166). It is FREE. Its only
  constraint is the lower bound (7.29) R* ≥ T₀/T_dec ≈ 6.75×10⁻⁴ from decoupling at ≤ 4000 K (line 3365; the printed
  "2.2/4000 = 6.75×10⁻⁴" is a typo for 2.7/4000), and the paper ranges it over "2.7/4000 ≤ R* ≤ 1" (line 3467) and
  plots r_max against it over the whole interval (Figure 2, line 3745). A second free quantity is the initial shock
  position r* at R*, restricted only by the window (7.34). R* is therefore NOT the shock position at a reference
  time; it is the epoch from which the model is declared to apply, and it is unmeasured and unfixed.

## 2. The claim at lines 98–104 — what is actually computed

Traced: (i) the excess travel r² − r*² between R* and R = 1 (eq. 7.31, line 3399), (ii) the initial-position window
(7.34, line 3459), (iii) their combination, the present bounds (7.37)–(7.38, lines 3563, 3591). Every one of them
carries R*. The result is a ONE-PARAMETER FAMILY OF WINDOWS, indexed by R*, not a number:

    r_min(R*) = H₀⁻¹ (5.1×10⁻⁴)(T₀²/h₀) √ln(1/R*)                       (7.37)
    r_max(R*) = H₀⁻¹ √[ .76 R*/(1 + 4.6×10⁻⁷ T₀⁴/(h₀² R*²)) + 2.6×10⁻⁷ (T₀⁴/h₀²) ln(1/R*) ]   (7.35)

Arithmetic (h₀ = .55, T₀ = 2.736 K, T₀⁴ = 56.04, â = 4.6852×10⁻²⁷ lty⁻²K⁻⁴, H₀ = 1.023h₀×10⁻¹⁰ lty⁻¹):
- (7.24) α/β = âT₀⁴/(3H₀²) → coefficient 1.4923×10⁻⁷ T₀⁴/h₀²  [paper 1.492×10⁻⁷ — reproduces].
- (7.27)–(7.28) with a = 2(3+w)(1−w)/w·α/β², b = −6(1−w)/w·α/β² from integrating (7.7): a₊+b₊ = 2(1−σ̄)α/β² →
  2.618×10⁻⁷, a₋+b₋ = 2(1−1/9)α/β² → 2.653×10⁻⁷  [paper 2.62 / 2.65×10⁻⁷ — reproduces; note the 1/w cancels].
- (7.31)→(7.33): 2.62×10⁻⁷ × 56.04/0.3025 × ln(4000/2.7 = 1481; ln = 7.30) = 3.54×10⁻⁴ H₀⁻²; √ = 0.0188 H₀⁻¹
  [paper "(.019)² H₀⁻²", line 3418 — reproduces]. Keeping the neglected A, B terms: 3.43–3.48×10⁻⁴ H₀⁻² (3% shift).
- (7.34): (1−σ̄/3)/(1+σ̄) × (1−1/9) = 0.8539 × 0.8889 = 0.759 [reproduces; the paper used w = 1/9, the loosest
  bound]. r*² < 0.759 R*/[H₀²(1 + 0.127)] = 4.55×10⁻⁴ H₀⁻² → r*_max = 0.0213 H₀⁻¹ at R* = 2.7/4000.
- Present window at the paper's own fiducial R* = 2.7/4000:  0.019 H₀⁻¹ ≤ r ≤ 0.029 H₀⁻¹,
  i.e. with H₀⁻¹ = 1.78×10¹⁰ lty (h₀ = .55): 3.4–5.1×10⁸ lty ≈ 100–160 Mpc.
- Present window at R* = 1: 0 ≤ r ≤ √0.76 H₀⁻¹ = 0.87 H₀⁻¹ ≈ 4,750 Mpc.
  r_max(R*) rises monotonically: 0.029 (R*=6.75e-4), 0.066 (0.01), 0.27 (0.1), 0.62 (0.5), 0.87 (1).
So across the admissible family the present shock position spans 0 to 0.87 H₀⁻¹ — a factor ≈ 45 in r_max, and a
lower envelope of zero. The abstract's "comparable to the Hubble distance" (line 14) and Section 1's "the shock
position is comparable to the Hubble length" (line 312) hold only at the R* → 1 end, where the model's whole
motivation (FRW settled by decoupling, lines 1476–1484) is abandoned. At the paper's own preferred R* (decoupling)
the shock sits at ~2–3% of the Hubble length. Line 103–104's "not determined by any adjustable parameters ... other
than H₀ and T₀" is contradicted by the paper's own text (lines 161–166, 231, 3466–3469) and its own Figure 2.
- The one R*-insensitive statement is the R*-INDEPENDENCE of r² − r*² from r* (line 3410), and the global upper
  bound r ≤ 0.87 H₀⁻¹ (the R* = 1 envelope). Both are distances from an unlocated centre; neither is an observable.
- Printed-formula check: in (7.34)–(7.36) the correction term carries R*² in the denominator (lines 3459–3529), but
  the derivation from (6.24) — αr² < c(1−w)R²/(3+w+(β/α)R), i.e. r² < c(1−w)R²/((3+w)α + βR) — gives the FIRST
  power of R*. With R*² literally, the correction at R* = 6.75×10⁻⁴ is 189 (not 0.13) and r_max collapses to the
  lower bound, 0.019 H₀⁻¹; with the derived R*, r_max = 0.029 H₀⁻¹. Either way the decoupling-end answer is
  0.019–0.029 H₀⁻¹; the typo is immaterial for R* ≳ 0.05. Also (8.6): from the paper's own (7.26) α/β² = 8.34×10⁻⁶
  /(h₀²H₀²) one gets 1/√α = 346 h₀H₀⁻¹, not the printed 118 h₀H₀⁻¹ (line 3688; 118 is reproduced only by using
  α = 3âT₀⁴ with T₀ = 2.7 — a factor-9 slip in α). That affects only the β = 0 comparison case, (8.7) 36h₀/H₀ →
  ~106h₀/H₀ (lines 3695–3699): "significantly beyond the Hubble length" (line 299) survives, the number does not.

## 3. Observability

- Position relative to us: NOT stated. The paper never places the observer; it says only that the picture "would
  place our solar system in a special position relative to the center" (line 59). All distances are from the centre.
- Relative to the Hubble length / light cone: at the fiducial R*, 0.02–0.03 H₀⁻¹ (in EdS, comoving distance
  ⇔ z ≈ 0.02–0.03 — deep inside the observed Hubble flow); at R* = 1, up to 0.87 H₀⁻¹ (z ≈ 2.1 in EdS). Inside
  the horizon in every case, so in principle visible from a centred observer — but the paper does not say so.
- Signature: NONE. There is no temperature edge, density jump, anisotropy, or any sentence with a sign or magnitude.
  The paper explicitly disclaims: "one's first reaction is that nothing quantitative could be said about the position
  of the shock without knowing ... the spacetime beyond the shock–wave ... And to a large extent this must be true"
  (lines 302–306). The only outward-looking sentence is a rhetorical question about seeing "other similar
  explosions ... beyond the shock–wave" (lines 318–335). CMB isotropy is acknowledged as "the strongest support for
  the Copernican Principle" that the model violates (lines 66–69), with no computation of the model's anisotropy.
  The pure-radiation comparison (Section 8) is a different model that, by the paper's own admission, does not
  reproduce H₀ at T = T₀ (lines 295–298, 3602–3607).

## 4. What "accounts for H₀ and T₀" means — inputs, not outputs

Inputs, by construction. R₀ = 1 is fixed by the k = 0 rescaling freedom (footnote at lines 1400–1403, and line
1785); then (5.6) Q₀ = 3α + β = H₀² (line 1791), (7.13) α = âT₀⁴/3 (line 3180), (7.14) β = H₀² − âT₀⁴ (line 3183).
The section opens "We now evaluate α and β in terms of the present value of the Hubble constant H₀ and the observed
microwave background radiation temperature T₀" (lines 3137–3139). "Present time" is DEFINED as the FRW epoch at which
these two numbers agree with observation (lines 98–101). The interior is exactly the standard flat radiation+matter
FRW solution, so every interior observable — Hubble rate, CMB temperature, their history — is reproduced identically
and cannot discriminate. No output of the model is compared with anything: the two derived scales, √(α)/β ≈
5×10⁻³ H₀⁻¹ (sets r² − r*²) and √0.76 H₀⁻¹ (sets r_max), are lengths from an unobserved centre, not measurements.
Under the scheme, H₀ and T₀ are borrowed from the data and normalise the model; nothing calibrates.

## 5. Tier consequence

- CALIBRATED-FALSIFIER: no. No observable is named, no signature is derived, and the "prediction" is a one-parameter
  family of windows whose lower envelope is zero (r ≥ 0 at R* = 1). A number exists (0.019 H₀⁻¹ excess travel;
  0.87 H₀⁻¹ envelope) but the missing piece is not a threshold — it is the observable itself and the observer's
  location, which the lane may not supply.
- PROSPECT: no. The paper proposes no measurement and no future test; it proposes the model "as a natural and simple
  starting point for a further investigation" (lines 335–338).
- QUALITATIVE-DIRECTIONAL (the 08-28 flag): does NOT survive. The only qualitative claim, "comparable to the Hubble
  length," is not a direction the model fixes: at the paper's own fiducial R* the answer is 0.02–0.03 H₀⁻¹, and it
  becomes ~1 only as R* → 1. Even the qualitative content is set by the free parameter, and it attaches to no
  observable in any case.
- Verdict: AUDIT_HOLDS_CONSISTENCY_ONLY. The paper is a genuine existence construction (Theorems 1–5) showing that a
  k = 0 FRW interior normalised to H₀ and T₀ can be matched across an admissible shock to a TOV exterior, with an
  internal bound on where the shock can be. That is consistency, exactly as tiered.
- Candidate for Duho (recorded, not promoted): the only R*- and r*-independent derived statement is the envelope
  r_present ≤ √0.76 H₀⁻¹ ≈ 0.87 H₀⁻¹ — the shock cannot lie beyond ~0.87 Hubble lengths from the explosion centre
  (from (7.34) at R* = 1; H₀-only, T₀ negligible). Turning it into a test would require the lane to add the
  observer's position and a signature for a TOV exterior, i.e. more than a threshold. Not tier-adjacent on my reading;
  flagged so the packet is complete. Secondary findings for the record: printed R*² vs derived R* in (7.34)–(7.36);
  (8.6) 118 vs 346 h₀H₀⁻¹ inconsistent with (7.26); "2.2/4000" typo at (7.29).

## Plain language

This paper builds a toy universe: the ordinary expanding universe on the inside, a still, static universe on the
outside, and an explosion front (a shock wave) in between. The authors ask how far out that front could be today.
They do get formulas, but the formulas depend on a knob they cannot set — the moment the model is supposed to have
"switched on" — and on where the front happened to be at that moment. Turn the knob to the value the paper itself
prefers (the CMB decoupling era) and the front would be only a few percent of the way to the edge of the observable
universe; turn it to "today" and the front could be almost anywhere out to about 87% of the Hubble length. The
Hubble constant and CMB temperature do not come out of the model; they are put in to set its scale, so the model
reproduces them automatically and proves nothing by doing so. Nowhere does the paper say what an observer would
actually see at the front, or in which direction. So the earlier suggestion that this paper makes a directional
prediction does not hold up; it is a mathematically careful consistency construction, which is how it is already
tiered. Two of the paper's own numbers in the side calculations (Section 8) do not match its main-text constants,
but that does not change the verdict.
