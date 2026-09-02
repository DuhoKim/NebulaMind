# The 60° causal cutoff: what the theory fixes, and what it does not

**Program (A) theory-side write-up — Duho's ruling "a then b" (2026-09-02). Revision 2: the first
draft was gated `WRITEUP_REFUTED` (`FREEDOM_MAP_GATE_codex.md`) for resurrecting claims this
program's own rounds had retracted; this revision repairs every finding. IN-LANE ONLY: the paper is
HELD; nothing outward. No tier is changed by this document; entries 23–27 remain
QUALITATIVE-DIRECTIONAL.**

## The question, and the answer in three sentences

The Gaztañaga causal-horizon model makes the BHU corpus's one genuinely a-priori CMB prediction: a
loss of correlation beyond ~60°. This program asked whether that prediction can be **calibrated** —
turned into a definite number for the large-angle statistic `S₁/₂` — or whether the amplitude is
permanently free. The answer: **the paper supplies no perturbation prescription at all, so every
route to a number passes through choices external to the theory; the specific natural constructions
computed here (with all external choices declared) give full-sky `S₁/₂` between 6,113 and 14,000
μK⁴ — a 2.5–5.7× suppression of ΛCDM's 34,924 — and the observed value enters only in phase (b),
because it is not comparable to these full-sky numbers.**

## 1. What the paper actually derives (verified from the source, with line numbers)

Source: arXiv 2003.11544 (`2003.11544_clean.txt`), entry 23, MNRAS 494:2766.

- **The imposed condition is Eq. 16–17, and it constrains Λ, not perturbations.** "we will require
  Φ(χ>χ§)=0 in Eq.16, so that there is no flux (i.e. no effects of gravity) beyond the causal scale.
  This implies" Eq. 17 (`Λ/8πG = (⟨ρ⟩§+3⟨p⟩§)/2`). Φ is a 4-volume integral of `R⁰₀` — a flux, not a
  field. (An early round misread Φ as a Dirichlet condition on the potential and manufactured a
  spurious "unique" prediction; refuted against the source.)
- **The scale chain is sound and non-circular.** Eq. 22 is solved with Ω_Λ = 0.69 ± 0.01 — measured
  from supernovae/BAO, not from the correlation under test — giving Eq. 23,
  `χ_§ = (3.149 ± 0.006) c/H₀ = 14,015 Mpc`, and `θ_§ = χ_§/χ(z=1100) = 57.4°`
  (`cutoffA_check_60deg_chain.py`; the paper rounds to 60±3). A seat's charge that the paper's own
  numbers give 22° was checked and refuted — it substituted the de Sitter radius for χ_§.
  *(Noted: L429 also runs Eq. 22 backwards, "predicting" Ω_Λ from the observed 60°; that is the same
  relation twice, not independent evidence.)*
- **The perturbation side is one sentence in expectational modality:** "There should be a smooth
  background across disconnected regions with an infrared cutoff in the spectrum of inhomogeneities
  for χ>χ§" (L250–251). "infrared" is a hapax (1 occurrence paper-wide). The matching reference is
  "could be matched as in Sanghai & Clifton 2015" (no equation adopted); the initial-conditions
  reference, Gaztañaga 2019, resolves at L558 to "**In preparation**". The author states the gap
  himself at L466: "**it is impossible to quantify this without a model for the initial
  conditions**."

## 2. The core negative result: no licensed perturbation condition

Three seats independently returned `READING_C` — the paper licenses **no** sharp mathematical
condition on the primordial spectrum (Claude-textual `CGATE_PROGRAM_A_STEP2_textual.md`, codex
`AGATE_PROGRAM_A_STEP2_codex.md`, kimi `KGATE_PROGRAM_A_STEP2_kimi.md`) — and the fourth seat
(Claude-physics, `AGATE_PROGRAM_A_STEP2_physics.md`) independently returned `CLASS_REFUTED` against
the proposed formalization, a compatible but distinct verdict. Decisive points: the cutoff sentence
carries none of the register the paper uses for its real condition ("we will require… This implies:"
+ numbered equation); L435 affirmatively contradicts the Fourier reading ("there are temperature
differences on scales larger θ§, but they are not correlated" — under `P(k<k_§)=0` those differences
would not exist); and the author's own L466 concession. **Two criticisms from those verdicts are
carried as open flags:** (i) equating absence of causal influence with zero correlation is a
non-sequitur — common initial conditions can correlate causally disconnected regions (the standard
inflationary point); (ii) the paper's one derived condition, `Φ(χ>χ§)=0`, has never been imposed on
the perturbed solution by anyone, including this program.

## 3. The two refinements computed here are mutually exclusive (computed, both directions)

The cutoff sentence admits two natural formalizations, and they cannot both hold
(`cutoffA_readings_incompatible.py`):

- **Reading A (Fourier support):** `P(k)=0` for `k<k_§`. Imposing it leaves `ξ(r)` with oscillatory
  tails at the 0.2% level out to `8χ_§` — real-space correlation does *not* vanish.
- **Reading B (real-space support):** `ξ(r)=0` for `r>χ_§`. Imposing it (positive-definite
  spherical-overlap window) forces `P(k)` **largest at the smallest k** — 729–1217× its value at
  `3k_§` — the opposite of a Fourier cut. This is the Paley–Wiener obstruction: compact support in
  `r` makes `P` entire in `k`, and a non-trivial entire function cannot vanish on an interval.

So no computation can serve both readings, and the paper selects neither. **These two are the
refinements computed here, not an exhaustive partition:** the step-2 physics verdict lists further
choices any causal completion must make — stochastic state/covariance, homogeneity and isotropy of
the patch, observer position, patch geometry and matching, realizability, transfer physics, and the
uncertainty in χ_§ — none of which the paper fixes and only some of which are varied below.

## 4. Reading A: a number, set by an unlicensed convention

Hard IR cut, spectrum otherwise ΛCDM (fixed by high-ℓ data; low-ℓ held out), full-sky unlensed CAMB,
validated `S₁/₂` operator (exact to ~1e-14; reproduces ΛCDM at 34,924–34,926 μK⁴ against the
independent ~34,900 reference) (`cutoffA_s12_machinery.py`, `cutoffA_pvalue_shift.py`):

| convention | S₁/₂ |
|---|---|
| `k_§ = 2π/χ_§` | **6,897 μK⁴** |
| `k_§ = π/χ_§` | **14,000 μK⁴** |

A factor 2 in the statistic from a convention the paper does not fix. Three smooth Fourier windows
were also tested (widths 0.3/1.0/3.0 × k_§): 6,113–10,095 μK⁴. **They are exactly that — three
tested smooth Fourier windows.** No claim is made that they realize Reading B or span causal
kernels; the C1 retraction (`PROGRAM_A_PVALUE_RESULT_20260901.md`) and the C2 gate both record that
this family establishes no bound.

## 5. Reading B: one explicit construction, computed to convergence

**The construction is external to the paper, and that must be said first.** Reading B as computed
here is a stack of declared choices the source does not make: the spherical-overlap window (one of
many compact positive-definite windows), the no-zero-mode subtraction, a homogeneous isotropic
scalar `P(k)`, standard ΛCDM transfer functions, and a high-k treatment. Its numbers are the
sensitivity of **one invented construction**, not the theory's own band.

With that scope fixed, the computation is clean:

1. **The naive version has no limit.** Without subtraction, `S₁/₂` tracks the IR regulator (252,066
   → 900,646 μK⁴ across a factor 1,000 in `k_min`; both seats independently) because the
   log-divergent, `r`-independent piece of `ξ` — an unobservable monopole — is converted by
   windowing into physical low-k power. **My first conclusion ("Reading B yields no number") was
   overturned** by the repair I had flagged against it: imposing no-zero-mode (`P_B(0)=0` via
   `c = ⟨ξ⟩_W`) makes `S₁/₂` **converge** (final fractional change 7.7e-11).
2. **Positivity was contested and is settled for this construction.** One grid showed `P_B` dipping
   negative; the ruled third seat settled it (`POSITIVITY_third_VERDICT.md`): the dips are aliasing
   (268 radians per grid step at the window scale, at `k≈1.6–1.9/Mpc`, irrelevant to `S₁/₂`), and
   `P_B ≥ 0` holds **for this specific construction and spectrum** — established by the full
   adjudication (exact regulator-free ξ, refinement-stable minima, Bochner controls), with the
   small-k behaviour separately confirmed by the local identity
   `P_B''(0) = −(4π/3)·Cov_μ(r², ξ) > 0` for decreasing ξ. The identity is the small-k check, not
   the global proof.
3. **A window bug — mine — cost two runs.** My brief gave the window transform with an unbound
   symbol; its natural reading doubles the support to 28,030 Mpc, and the first "converged" value
   (23,900) was for that wrong object (proven by closed-form match of the `c` values to 9
   significant figures; register §1at). Repaired: support 14,015 Mpc, audit in
   `MONOPOLE_FIXED_codex_RESULT.md`.

**Result:** `S₁/₂(B) = 8,777 μK⁴` with the high-k splice onto ΛCDM (the held-out-data constraint
this program imposed, not the paper) and `10,132 μK⁴` without it (the raw construction approaches
ΛCDM on its own, `P_B/P_ΛCDM = 1.053 → 1.0006` over `k = 0.01 → 2`, but carries a ~5% excess at
first-acoustic-peak scales that measured high-ℓ data would notice). **Corroboration is
branch-specific:** the independent second seat's 10,063 matches the **no-splice** branch to 0.7%
(`MONOPOLE_NORM_RESIDUAL_codex.md`); the spliced 8,777 is a corrected single-production result with
a regression check, not an independently reproduced one. The +15.4% spread is sensitivity to a
treatment choice **within this construction**.

## 6. The computed map

| object | S₁/₂ (μK⁴) | the choice that sets it |
|---|---|---|
| ΛCDM (this pipeline, full-sky unlensed) | 34,924 | — |
| Reading A, `2π/χ_§` | 6,897 | k-convention |
| Reading A, `π/χ_§` | 14,000 | k-convention |
| three smooth Fourier windows | 6,113–10,095 | window width |
| Reading B construction, spliced | 8,777 | high-k treatment |
| Reading B construction, no splice | 10,132 | high-k treatment |

**What this table is:** the outcomes of the specific implementations computed and gated in this
program. Across them, full-sky `S₁/₂` spans **6,113–14,000 μK⁴**, i.e. suppression of ΛCDM by
**2.5–5.7×**, with every number reachable only through at least one choice the paper does not make.

**What this table is not:** a bound over "all natural completions." Only enumerated implementations
were computed; the C1 retraction records that three window widths establish no extremum, the C2
gate records that this family does not span causal kernels, and the step-2 physics verdict exhibits
how far outside this range an unconstrained completion can go. **The calibration no-go is
therefore the licensing statement, not a band statement:** the paper fixes the *scale* (57.4°,
non-circularly) and fixes *nothing else* — no reading, no convention, no state — so no specific
`S₁/₂` value can be attributed to the theory, only to a declared completion of it.

## 7. What this document deliberately does NOT claim

- **No comparison to the observed value.** The literature's ~1,150 μK⁴ is a cut-sky,
  estimator-specific number; every value above is a full-sky spectrum statistic. Comparing them is
  the mismatch the C2 gate refused, and no "the model overshoots/undershoots the data" claim is made
  or implied here. **That comparison is phase (b), ruled and next:** apply the actual mask and a
  pseudo-C_ℓ estimator to every simulated sky, then compare like with like.
- **No p-value claims.** `S₁/₂` is quadratic in `C_ℓ` with a violently skewed sampling distribution
  (ΛCDM's sampling mean is 62,069 against its spectrum value of 34,924). Any distributional
  statement belongs after (b).
- **No ISW/lensing separation.** All values unlensed; the late-ISW cross term can carry either sign
  (computed counterexample: adding positive power at ℓ=4 *lowers* S₁/₂).
- **A structural assumption underlies every row:** standard infinite-volume ΛCDM transfer physics
  with only the primordial spectrum modified. As the C2 gate put it, this tests "ΛCDM transfer
  physics plus an infrared spectral window" — a genuine causal boundary could alter the mode
  structure, projection, or evolution themselves, and no receipt here constrains that.
- **No tier implication.** Whether this map bears on entries 23–27 is Duho's call, not this
  document's.

## 8. The record behind it

This program refuted its own constructions repeatedly before arriving here: the original
optimization method (an admissible class with an unpinned parameter; a decision rule that would
have refuted ΛCDM itself), two headline claims (C1, C2), my "Reading B has no number" (overturned by
the monopole repair), one seat's window (traced to my own brief's ambiguous symbol, §1at) — and the
first draft of **this document**, gated `WRITEUP_REFUTED` for re-importing retracted claims into the
synthesis. Each overturning is committed with its receipt. The surviving numbers passed, variously:
blind double computation (the naive-divergence finding and the no-splice branch), a
mandated-sanity-gate third-seat adjudication with closed-form cross-checks (positivity and the
window bug), regulator convergence to ~1e-10, and regression checks (the spliced branch). The
defect classes learned are `HARNESS_DEFECT_REGISTER.md` §1ak–§1at.

## Receipts index

`cutoffA_s12_machinery.py` (operator, validated) · `cutoffA_readings_incompatible.py` (§3) ·
`cutoffA_check_60deg_chain.py` (§1) · `cutoffA_pvalue_shift.py`, `cutoffA_afortiori_check.py` (§4) ·
`cutoffA_readingB.py`, `cutoffA_readingB_agy.py`, `READINGB_RECONCILIATION_20260902.md` (§5.1) ·
`cutoffA_monopole*.py`, `MONOPOLE_*_RESULT.md`, `POSITIVITY_third_VERDICT.md`,
`cutoffA_positivity_third.py` (§5.2–5.3) · `MONOPOLE_NORM_RESIDUAL_codex.md` (§5, §6) ·
step-2 gate verdicts ×4 (§2) · `FREEDOM_MAP_GATE_codex.md` (revision-1 refutation) ·
`2003.11544_clean.txt` (§1).
