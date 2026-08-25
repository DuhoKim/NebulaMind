PASS_S0S2_FIXED

# Phase 5 S0–S2 re-gate verdict — kimi seat (KREGATE), 2026-08-25
Verifying the four fixes required by KGATE_S0S2_VERDICT.md §5, then attacking the fixes.
Verification artifacts: _tmp_kregate_check.py and _tmp_kregate_check2.py (fresh independent
implementations — trapezoid integration on a 40001-point grid and full nonlinear root-finds,
not the lane's leggauss/linear-slope route), plus fresh runs of all three scripts, a sympy
re-derivation of the in-lane Taub algebra, and my prior gate script _tmp_kgate_check.py re-run
unchanged. No gated file modified; codex's REGATE_S0S2_VERDICT.md read as an independent input.

## The four items

**1. Withdrawal pointers + the 1.585e-3 figure — VERIFIED, and the agreement is not coincidence.**
Dated (2026-08-25) WITHDRAWAL POINTER sections are present in S0_RECEIPT.md, S2_RECEIPT.md and
S3_RECEIPT.md; each declares every numeric bound NOT CLAIMED and names the live successors
(P1_RECEIPT.md, P2_P4_RECEIPT.md) with the live figure. The figure itself triangulates across
three independent computations:
- my prior gate script (raw pattern, then divide by D0): 1.585e-3, one part in 631;
- the lane's p2p4_transfer_confront.py (normalised pattern directly): 1.585e-3, 631, 6/6 checks;
- my fresh regate script (normalised pattern, different integrator, full nonlinear solve):
  1.584961e-3 (3.7 mK edge), 1.542124e-3 (3.6 mK edge), ℓ≥2 → 5.502152e-3.
Underlying values reproduced from the CSV, not inherited: mono = +0.5133957, D0 = 1.5133957,
raw c1 slope = 1.296254, span slope 2.5925, normalised c1 slope = 0.856520; B2.2 =
3.7e-3/2.7255 = 1.357549e-3. The frozen row (TRACK_B_FREEZE.md:59) reads "|Δ1,int| < 3.6–3.7 mK
(95% CI)"; the confrontation uses the weak 3.7 edge, which is the conservative choice for an
exclusion. "One part in 631" is exact (630.9). The dipole row still binds (1.585e-3 < 5.502e-3).

**2. s2_transfer.py banner — VERIFIED.** A fresh run prints a three-line
"WITHDRAWN OUTPUT — SUPERSEDED and NOT CLAIMED" banner immediately above the stale 3.857e-6
figure, names both defects (span-vs-dipole, pre-normalisation) and points to P2_P4_RECEIPT.md.
The number cannot be mistaken for a live result. 4/4 checks pass.

**3. s1_crossing_shift.py DERIVED label + in-lane Taub derivation — VERIFIED.**
- The optics inference now carries an explicit DERIVED label (docstring lines 25–30: the step
  from pinned Lipschitz matching + Rankine–Hugoniot to "k continuous, all shift from the fluid
  jump" is OURS). The generic Landau & Lifshitz citation is gone, replaced by the in-lane
  derivation the kickoff sanctioned.
- The derivation checked line by line, symbolically (sympy): momentum-flux balance with the
  energy-flux condition reduces identically to J(v1−v2) = p2−p1; substituting it,
  e2−e1 − J(v1−v2)/(v1v2) ≡ 0 and (p2−p1)/(e2−e1) − v1v2 ≡ 0. No sign or factor error, no
  hidden textbook dependency; the premises are the pinned junction conditions already gated.
  6/6 checks pass; β_rel = −1/√N whole orbit (max abs dev 1.9e-8, endpoint-limited as
  documented).
- Note on codex's REGATE verdict (HOLD_OPTICS_INFERENCE_STILL_UNLABELLED, 21:05): correct at
  issue time against the then-current file. The label landed at 21:07 (file mtime) explicitly
  citing the codex re-gate; the current file satisfies it. Its HOLD is moot as of the current
  state, and its other verifications agree with mine.

**4. S0_RECEIPT.md withdrawal pointer — VERIFIED** (same dated block as S2/S3, pointing to the
P1 invariant integral and the P2_P4 bound).

## Attack 5 — is the monopole normalisation itself right? YES, and its soft spot does not bite.

The fractional anisotropy against the measured sky mean is exactly (vals−mono)/(1+mono); the
implementation divides the whole monopole-subtracted pattern and recomputes mono at each
offset. At t_obs = t_crit the crossing region is the whole sky, so no unshifted reference
exists and the normalisation is mandatory, not optional.

The soft spot I attacked: normalising by (1+mono) reintroduces dependence on the O(0.5)
monopole, whose SIGN is the objection-5 orientation question — a receding orientation gives
mono = −0.3392, and if the raw dipole were unchanged the bound would move by the factor
1.5134/0.6608 = 2.29. Direct computation kills the concern: the raw dipole response scales
with the Doppler factor itself, so the NORMALISED dipole slope is orientation-invariant —
0.8566584 / 0.8565352 / 0.856520 at f = 1e-5 / 1e-4 / 1e-3 in the blueshift orientation, and
the same digits (to <1e-7 relative) in the receding one. The 1.585e-3 figure does not depend on
the orientation fix at all. This STRENGTHENS my KGATE D2: magnitudes are convention-invariant
not merely at O(f) on the raw pattern, but after monopole normalisation as well.

The orientation fix itself is independently correct anyway: at the crossing, shock-frame
kinematics gives ω_FRW/ω_TOV = γ(v1)(1−v1)/[γ(v2)(1−v2)] = 1.513444 > 1 — the upstream (TOV,
thinner) fluid moves inward relative to the FRW receiver, an approaching emitter, blueshift,
hotter crossing — and equals γ_rel(1+|β_rel|) exactly. Only signed statements (which side is
hotter) remain orientation-dependent, as D2 held.

## Attack 6 — the blind-double method finding: SOUND, one imprecision (non-blocking).

Core claim verified against the artifacts: BRIEF_GPT1_BLIND_S0.md instructs "Assume the
exterior is fully ionized hydrogen (Thomson opacity σ_T/m_p)", and gpt1's README assumption 2
says "as directed". Agreement on an instructed closure validates only the arithmetic downstream
of it; the finding's self-report about S0_CROSSCHECK.md ("S0 stands" presented as confirmation
without the line) is accurate, and the three briefing changes are sound and proportionate.

The imprecision: "it justified the path-length choice I had hand-waved" drops the conditional.
gpt1's exactness argument holds only under ρ̄ ∝ r̄⁻², a profile it explicitly flagged as NOT
supplied (S0_CROSSCHECK.md states this correctly). And the precedent itself sits on the
withdrawn line: both seats used r̄ as a spatial column length — the defect that killed S0 —
which neither was briefed to check and which the finding's three lessons would not have caught
(the brief supplied r̄ = 2ct√N without flagging its timelike character inside the horizon).
One caveat sentence would make the method note exact; as written it over-compresses but makes
no false physics claim. Not blocking.

## Minor nits (non-blocking, for the record)

- N1. P2_P4_RECEIPT.md P3: "the transfer at P1's τ bound moves it by 6.8% … (LC5)". 6.8% is
  the UNNORMALISED dipole move (1−e^{−0.07} = 6.76%); LC5 measures the NORMALISED move, 3.73%.
  Both far under the 10.5% allowance; the bound uses the kinematic pattern regardless.
- N2. GATE_NOTICE_S2_SUPERSEDED.md still asserts "the bound is x_off/r_* < 1.05e-3, one part
  in ~950" with no dated pointer into the withdrawal/normalisation chain. It is a historical
  routing notice and the receipts are clean, but a lone reader could take 1.05e-3 as live.
- N3 (adequacy note, not a defect): P2_P4's P4 body still shows the bold 1.05e-3 binding line
  above the dated CORRECTION — the lane's amend-in-place convention, and the correction is
  explicit and dated. Adequate.

## Disposition

All four required fixes are present and correct; the new load-bearing addition (the in-lane
Taub derivation) is exact; the normalisation survives attack including its orientation soft
spot; the method finding is sound with a one-sentence caveat recommended. Codex's regate HOLD
was valid when issued and is moot in the current state. Nothing here revives the withdrawn
line, changes the S1 law, or gates Phase 5b's P1 physics (P2_P4's numbers remain conditional
on P1's blind double, as its receipt states).

PASS_S0S2_FIXED
