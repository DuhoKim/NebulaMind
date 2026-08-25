HOLD_S2_DIPOLE_BOUND_MISNORMALIZED_AND_RESIDUAL_DEFECTS

# Phase 5 S0–S2 adversarial gate verdict — kimi seat (KGATE), 2026-08-25
Gating the CURRENT files: S2 as amended via S3, S0's optical depth withdrawn per
S0S2_DISPOSITION.md, codex's HOLD_S0_OPTICAL_DEPTH_AND_S2_EXCLUSION_UNDERIVED treated as an
independent input. Verification artifacts: _tmp_kgate_check.py (independent reimplementation,
written from the stated physics, not from s2/s3 code), plus fresh runs of all three scripts and
a sympy re-derivation of the S1 identity.

Headline: **S1's law PASSES every attack. The S0 withdrawal and the K4 stop are correct and are
endorsed. But the surviving bound figure in the current record — x_off/r_* < 1.05e-3, asserted
in S2_RECEIPT.md's amendment and S3_RECEIPT.md — is itself quantitatively wrong on the record's
own pattern, and codex's alternative figure (7.9e-4) is wrong too, by a different error in the
same overclaiming direction. The honest figure is ≈ 1.6e-3.**

## 1. Agreements with codex, independently verified (not inherited)

- **Obj 1 (tau_R is not an optical depth): endorsed.** The pinned source does say r̄ "is taken
  to be the timelike variable because we assume A(r̄) = 1−2M/r̄ ≡ 1−N < 0"
  (0210105_clean.txt:93-108, read directly). At the crossing √N = 2.5498, so A = 1−N = −5.5 < 0:
  the crossing sits inside the horizon, r̄ is timelike there, and κ·ρ̄·r̄ treats a timelike
  coordinate as a spatial column. Neither implementation computed
  τ = ∫σ_T n_e(−u·k)dλ. Withdrawal correct.
- **Obj 2 (n_e not fixed): endorsed.** At the crossing u = 0.105616, v = 0.429965 (gated A1
  row), so p̄/ρ̄ = u/v = 0.2456 — the exterior is relativistic, not a cold proton fluid. Worse
  for the blind double's evidentiary value: gpt1's README states n_e = ρ̄/m_p was adopted "as
  directed" by the brief. Agreement between two implementations of an INSTRUCTED assumption is
  not independent validation of that assumption. This is exactly K4; the stop is correct.
- **Obj 3 (S2 is not the transfer function): endorsed.** Both implementations compute only the
  local kinematic jump; no absorption, no emission term, no source function. The receipt's own
  amendment-era label ("kinematic branch") is the right one; "transfer function" was not.
- **Obj 6 (PINNED/DERIVED): endorsed, and the two relabels are confirmed in place**
  (S0_DERIVATION.md:16 now "DERIVED, Phase 4 (gated), NOT pinned"; s2_transfer.py docstring now
  marks the Phase-4 geometry DERIVED). One bullet of objection 6 is NOT fixed — see D3.2 below.
- **Obj 7 first half (no-jump test was a non-test): endorsed and now fixed.** The current LC1
  tests the physical limit — β_rel → 0 as the shock weakens (√N → ∞), at the 1/√N rate:
  measured β(1e3) = −1.000e-3 vs β(10) = −0.1000, rate ratio 0.999711. That is a real test and
  it passes. The other half of objection 7 (citation) is NOT fixed — see D3.3.

## 2. The S1 law: independently re-derived, EXACT, survives

Symbolic re-derivation (sympy) from pinned (4.3), (4.4), (4.5) plus the textbook shock-frame
product v₁v₂ = (p₂−p₁)/(e₂−e₁), side 1 = FRW, side 2 = TOV:

- v₂ = (X+YN)/((1+σ)√N) — matches the receipt's intermediate form identically;
- β_rel = (v₁−v₂)/(1−v₁v₂) ≡ −1/√N, with β_rel + 1/√N simplifying to 0 identically;
- the identity holds for SYMBOLIC σ, not just σ = 1/3 (numerator N(σ−u)²−(1+u)² is exactly
  −√N times the denominator's bracket).

No sign or factor error exists. The numerics on the gated orbit are consistent (max abs dev
1.9e-8, endpoint-limited by the disclosed σ−u cancellation on 10-digit stored u; the
constraint-resolved recompute collapses to machine precision monotonically — the conditioning
signature of an exact law, correctly diagnosed in the receipt).

Applicability of the textbook relation at THIS junction (kickoff attack 2): concur with codex —
applicable. Adding the concrete reasons: the junction worldsheet has a spacelike normal because
|s| < 1 on the whole gated orbit (LC2, 0 violations), so a local shock rest frame exists; the
pinned Lipschitz matching enforces Rankine–Hugoniot conservation with no delta-function source,
which is precisely the relation's premise; entropy condition (4.6) selects the compressive
branch, and the corrected LC3 verifies the required ordering (thinner TOV side upstream and
faster: |v₂| = 0.755 > |v₁| = 0.577 at mid-orbit). That r̄ is timelike inside the horizon does
not obstruct a local frame construction. The β = 1/z_c reciprocity is exact, not approximate:
the crossing condition gives 1+z = 1+√N identically (gpt1's exact solve: 3.5499471), so
z_c = √N and |β_rel| = 1/z_c with no gap; the 2.5496-vs-2.5498 mismatch in S0's receipt is
disclosed nearest-row lookup noise.

A further attack that did not break: post-crossing FRW redshift contributes no direction
dependence. A ray crossing at η_e samples the bath at T_FRW(η_e) and redshifts by
a(η_e)/a(η_o) to the observer; the bath's own redshift cancels the ratio exactly, leaving
T_obs(μ) = T_FRW(η_o)·D(μ). The crossing-time variation across directions is harmless.

## 3. Disagreements — this is where the current record is still wrong

### D1 (BLOCKING). The corrected bound 1.05e-3 is misnormalized by D₀; codex's 7.9e-4 has a factor-2 error; the honest figure is ≈1.6e-3

Independent recomputation of the record's own kinematic pattern (my code, from the stated
physics; reproduces their numbers: span slope 2.5925, c₁ = 1.2963×f, c₂ as tabulated,
D₀ = 1.5133957):

1. The monopole is absorbed — the record's own words: the uniform shift "rescales the mean
   temperature." Absorption means fitting the bath so the OBSERVED mean (2.7255 K) equals
   T_bath·D₀. The observable fractional dipole is therefore c₁·f/D₀, not c₁·f. At
   t_obs = t_crit the crossing region is the WHOLE SKY (both implementations agree), so no
   unshifted reference sky exists and the D₀ normalization is mandatory, not optional.
2. S3 compared raw c₁·f (a pre-crossing-temperature fraction) against B2.2 as a fraction of the
   observed mean: 1.358e-3/1.296 = 1.05e-3. **Too strong by exactly D₀ = 1.5134.**
3. Codex's objection-4 first half (normalize by D₀) is CORRECT — but its arithmetic then
   compared the full SPAN (2.5925/D₀ = 1.7130) against B2.2's AMPLITUDE bound. For a
   dipole-dominated pattern the span is twice the amplitude. **Too strong by exactly 2:**
   7.9e-4 instead of 1.58e-3.
4. Correct confrontation on the record's own pattern: c₁·f/D₀ < 3.7 mK/2.7255 K gives
   **x_off/r_* < 1.585e-3** (3.6 mK edge: 1.542e-3) — one part in ~630–650. Verified three
   ways: direct projection, the half-span identity (2.5925/2 = 1.29625 = c₁ slope), and
   2×codex's figure.
5. Same defect in S3's non-binding ℓ≥2 row: with c₂/D₀ < 1e-5 the figure is 5.5e-3, not
   4.47e-3.

Consequences: both prior figures err in the OVERCLAIMING direction for an exclusion. **No
downstream text may quote 1.05e-3, "1 in ~950", 7.9e-4, or 3.86e-6.** The qualitative
conclusion survives this correction — a ~0.15%-of-radius centring requirement is still a
fine-tuning, and the both-branches-exclude shape is untouched — but the record's current
numbers do not. This does not revive the ppm exclusion, and it does not kill the necessity
direction; it corrects the number. When Phase 5b rebuilds the confrontation, the
monopole-normalized multipoles (c_l/D₀) must be the quantities confronted with frozen rows.

### D2 (partial refutation of codex obj 5). The span and dipole amplitude ARE convention-independent at the order used

Under β → −β, D(μ;x) maps to the mirror pattern at leading order; the small-offset span
coefficient 2.5925 and c₁ slope 1.296 are invariant at O(f) — exactly the order of every bound
discussed. Codex's "finite-offset raw spans likewise change" is true only at O(f²) and is not
load-bearing for any linear-order conclusion. What survives of objection 5: the physical
emitter/receiver orientation is genuinely unfixed, and it must be derived before any SIGNED
statement is made (which side of the sky is hotter; the signs in S2b's −61%…+23% contrast
range). Magnitude-based claims at linear order do not depend on it.

### D3 (BLOCKING, record consistency). Residual defects in the CURRENT files

1. **s2_transfer.py still prints the superseded exclusion.** Re-run today, it emits
   "EXCLUSION: ... x_off/r_* < 3.857e-06 — 3.9 parts per million" — the exact figure the S2
   amendment forbids any downstream text to quote. The script was not aligned with the amended
   receipt.
2. **s1_crossing_shift.py:17-18 still carries the unlabelled optics inference** ("The metric
   matching is Lipschitz ..., so the photon 4-momentum is continuous ... ALL of the shift comes
   from the fluid-velocity discontinuity") — codex objection 6's third bullet, accepted in the
   disposition as "must be labelled DERIVED," not fixed. (The inference is physically correct —
   a Lipschitz connection makes parallel transport across the junction unambiguous, so k is
   continuous and ω = −k·u takes the whole shift from the fluid jump — which is precisely why
   it deserves the DERIVED label rather than a free pass.)
3. **The textbook citation is still generic.** "Landau & Lifshitz, Fluid Mechanics,
   relativistic shocks" carries no edition/section/equation (objection 7's other half,
   accepted, not fixed). This gate confirms the relation is standard and the script's second
   reference is real: Taub 1948, Phys. Rev. 74, 328; Thorne 1973, ApJ 179, 897–907 (verified
   via ADS). Cite one of them exactly, or LL by section and equation.
4. **No withdrawal pointers.** S0_RECEIPT.md read alone still asserts τ_R = 0.34 and a τ = 1
   anchor at 1.47e17 s; S3_RECEIPT.md read alone still asserts "BINDING BOUND 1.05e-3". The
   disposition withdraws the first and declines to claim the second, but neither receipt
   carries a dated pointer to that effect.

## 4. What this gate did NOT find wrong

- The freeze Addendum-1 branch logic (opacity → photosphere, not hiding) is sound and
  pre-registered.
- Scope: surviving claims stay in the gated Track A domain (photon channel, pre-horizon,
  σ = 1/3). t_obs = t_crit is the domain edge, inherited from Phase 4's gated EXCLUDED-regime
  geometry; the crossings themselves are pre-horizon (√N = 2.55 > 1 at emission).
- Blind-double arithmetic is genuine (12-digit S2 agreement; my independent reimplementation
  reproduces both the pattern and the multipoles) — with the D1/agreement-is-not-validation
  caveat about brief-directed assumptions.
- The disposition's K4 invocation and the stop-for-decision are the correct process; the
  commissioned Phase 5b plasma brief is consistent with this verdict (its P1 invariant-integral
  rebuild is the right repair for S0, and D1's normalization must ride into its confrontation
  stage).

## 5. To clear this HOLD

1. Restate the B2.2 confrontation with the monopole-normalized dipole (x_off/r_* < 1.58e-3 at
   the 3.7 mK edge), or mark every numeric bound in S2_RECEIPT's amendment and S3_RECEIPT as
   not claimed, per the disposition — with dated pointers in both receipts either way.
2. Align s2_transfer.py with the amended receipt (remove or banner the 3.86e-6 printout).
3. DERIVED label on s1's optics inference; exact textbook citation for the shock relation.
4. Withdrawal pointer in S0_RECEIPT.md.

S1's law β_rel = −1/√N is the phase's durable product and needs nothing further from this
gate.

HOLD_S2_DIPOLE_BOUND_MISNORMALIZED_AND_RESIDUAL_DEFECTS
