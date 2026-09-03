# DRAFT — NOT ORDERED — K3 step 2 pre-registration: does an exchange correlation restore an n² spin-density term? (Tori, 2026-09-03 20:09 KST)

**Status:** drafted on Blanc's continuation note (20:03 KST) so that a future "k3 step 2" starts from a gated text. No derivation,
no seats beyond the referee gate. Becomes live only on Duho's word; then it is re-gated at that time.

## 0. Why this would exist
K3 step 1 (`K3S1_RESULT_20260903.md`) found the unpolarized average of the squared spin density linear in n at leading order
(uncorrelated particles). The Claude seat named the one route by which a genuine n² term could return: a Fermi-statistics exchange
correlation in the four-fermion Hehl–Datta operator (the term entry 10 writes at L88–89, `1111.4595v2_poplawski_prd85_clean.txt`:
the axial-current squared, (ψ̄γ^kγ⁵ψ)(ψ̄γ_kγ⁵ψ)). The question is bounded: compute the two-particle correlation contribution to
⟨s_i s^i⟩ for a degenerate unpolarized Fermi gas and state its n-dependence.

## 1. Objects, every symbol bound
- The macroscopic pseudovector s^i = ½ ψ̄γ^iγ⁵ψ (entry 10 L75–77) as a field operator over an unpolarized free Fermi gas of number
  density n at temperature T = 0 (degenerate) and, as a control, T → ∞ (classical, uncorrelated — must reproduce step 1).
- The exchange (Fock) term of ⟨s_i(x) s^i(x)⟩: the connected two-point piece from antisymmetrisation, evaluated at coincident points
  with the standard Fermi-sea occupation n_p = θ(p_F − |p|), p_F³ = 3π²n (the relation between p_F and n is a textbook constant,
  pinned at step 1 by a receipted derivation in the seat's script).
- The direct (Hartree) term: zero for the unpolarized state (step 1's result).

## 2. The question, exactly
What is the exchange contribution to ⟨s_i s^i⟩ as a function of n, and does any part of it scale as n² at fixed volume (as the
printed closures require), or as n^(5/3), n, or otherwise? Which, if any, of the printed coefficients (⅛, ¾) does it reproduce?

## 3. Outcome classes — declared now
- **EXCHANGE_N2_RESTORED:** an n² term appears with a derived coefficient; state whether it equals ⅛ or ¾ or neither.
- **EXCHANGE_OTHER_POWER:** the exchange term scales as a different power of n (e.g. n^(5/3) from p_F⁵); the printed n² law is not
  restored; report the power and coefficient.
- **EXCHANGE_NEGLIGIBLE:** the exchange term is sub-leading to the step-1 n/V term at all densities the bounce papers use
  (their densities pinned at step 1 from entries 9–11).
- **EXCHANGE_PRESCRIPTION_DEPENDENT:** the coincident-point limit needs a regularisation the papers do not fix → INCONCLUSIVE.

## 4. What counts as a verdict either way
A symbolic or numerically converged evaluation of the exchange integral with the n-scaling shown explicitly, one class filed.

## 5. Controls
- **C1:** the T → ∞ (uncorrelated) limit must return step 1's linear-in-n result. Failure = stop; no class.
- **C2:** the fully polarized Fermi sea must return the polarized closure n²/4 at leading order. Failure = stop; no class.
- **C3:** the exchange integral for a scalar density (no spin) must reproduce the textbook exchange hole normalisation (pinned
  at step 1 by derivation). Failure = stop; no class.
- **C4 deletion probe:** removing antisymmetrisation must remove the exchange term entirely; the seat states this before running.
  Failure = stop; no class.

## 6. Seat plan, blind double, cost
Two blind seats (codex, Claude seat; field-theory evaluation by script), third seat via `nm_referee_dispatch.sh` on a split, a
density-matrix or momentum-space second route for the "both" standard, Kimi on the check-sheet arithmetic. Two to five seat-days;
no data.

## 7. What would make it INCONCLUSIVE
EXCHANGE_PRESCRIPTION_DEPENDENT; or C1/C2 failing in both seats after two attempts.

## 8. Non-circularity
No cosmological input; the printed coefficients are under test, not inputs. Downstream cells are touched only by annotation
after Duho's ruling.
