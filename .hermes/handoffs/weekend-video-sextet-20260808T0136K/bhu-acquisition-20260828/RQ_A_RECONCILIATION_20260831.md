# RQ-A reconciliation — the Roupas amplitude (BHU Lane 2, task 1)

**Tori, 2026-08-31.** Blind-double derivation of the QNM excitation amplitude Roupas 2022 (entry 21)
deferred, run on **codex** (gpt-5.6-sol, 6m10s) and **agy** (Gemini 3.1 Pro), each independent.
Sources: `RQ_A_codex_RESULT.md`, `RQ_A_agy_RESULT.md`, brief `RQ_A_DERIVATION_BRIEF_20260831.md`.
**Tier move NOT made here — this is a decision for Duho (OPEN_QUESTIONS).**

## Reconciled verdict: entry 21 is NOT a new calibrated falsifier

Both seats independently computed the ringdown characteristic strain and **converged**:

- **Same formalism.** Energy-fraction model `E_rd = ε_rd M c²`; finite-mission characteristic strain
  `h_c = h_0 √(f T_obs)` with `T_obs = 4 yr` — NOT `√(f τ)`. Both explicitly refused to grant LISA
  the full damping-time integration (which would be a spurious detectability claim).
- **Same killer physics.** From Roupas Table 1 (`(2GM/c³)ω_I = −1.53×10⁻¹⁷`), the fundamental mode's
  **damping time is 2×10⁸ yr (10⁴ M⊙) to 2×10¹⁰ yr (10⁶ M⊙)** — astronomically longer than any
  mission. The mode radiates its energy far too slowly to build a detectable instantaneous strain.
- **Amplitudes agree.** At `D = 1 Gpc`, optimistic excitation: codex `h_c = 2.35×10⁻²²` (ε=0.03) →
  scales as √ε to `1.36×10⁻²²` at ε=0.01, matching agy's `1.3×10⁻²²`. Both sit **below** the
  Robson–Cornish–Liu LISA floor (~1–2×10⁻²¹) even at absurdly optimistic excitation (SNR < 0.2).
- **Same conclusion.** Roupas gives a *frequency* in-band (for M ≳ 10⁴ M⊙) but **no excitation
  factor and no event population**, so no guaranteed amplitude exists. **Entry 21 →
  PROSPECT-without-a-number by derivation.** "Detectable" is a frequency statement dressed as a
  detectability statement.

## The one nuance (not a disagreement — a difference in how far each went)

- **codex:** declined to estimate `ε_rd` (uncomputable from the paper; could approach zero), so it
  reported the honest residual: detectable *only* under an optimistic ceiling (ε=0.03) AND
  exceptional proximity (SNR-8 horizons of tens of Mpc for 10⁴–10⁵ M⊙, sub-Mpc for 10⁶). Verdict
  label: STRADDLES_OPTIMISTIC_ONLY → no calibrated falsifier.
- **agy:** *did* estimate a physical `ε_rd`: trapped interior modes are excited only through the
  potential-barrier transmission coefficient `~|ω_I|/ω_R ~ 10⁻¹⁵`, so `ε_rd ~ 10⁻¹⁷` and `h_c ~
  10⁻³⁰` — **~7 orders below LISA.** Verdict label: UNDETECTABLE.
- **Both routes → not a falsifier.** agy's barrier-transmission estimate makes the negative stronger;
  codex's refusal-to-estimate makes it more conservative. Neither yields a number LISA could be
  said to test against a population. **The disagreement is only in degree of negativity, and both
  degrees are on the same side of the falsifier threshold.**

## Bonus finding — a genuine defect in Roupas's paper (codex)

Roupas's perturbation is `exp(−iωt)`, so `ω` is **angular** frequency, yet the paper labels
`(2GM/c³)ω_R = 0.0062` at 10 M⊙ as **"63 Hz."** The physically correct cyclic frequency is
`f = ω_R/2π ≈ 10 Hz`. The distinctive-mode frequencies are a factor 2π lower than the paper's
"Hz" labels. This does not change the verdict (still in the LISA band for large M, still
undetectable in amplitude), but it is a real unit error worth recording against entry 21.

## The honest blocker (both seats, per the strict-model standard)

The Leaver/Berti–Cardoso excitation-factor calculation **cannot be closed from Roupas's paper**: it
needs a merger source term, normalized QNM eigenfunctions, the Green-function residue, and the
source–mode overlap — none of which the paper provides (Roupas said so himself). Neither seat
fabricated it. A model-owned conservative amplitude would require a numerical inhomogeneous
perturbation calculation that is genuinely new work, not extractable from the pinned source.

## What this means for the tier (Duho's call — see OPEN_QUESTIONS)

Entry 21 stays PROSPECT; RQ-A shows its "detectable" claim is **not** a falsifiable number. The
recommended record update is an annotation (not a tier change): note that the amplitude was
derived (blind-double), found undetectable at realistic distances, and that entry 21 is
PROSPECT-**without-a-number** — plus the Roupas 2π unit error. Every figure here traces to
`2203.13295_clean.txt` (Table 1) and the two seat results.
