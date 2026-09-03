# K3 step 1 pre-registration — one spin average or two? Deriving the unpolarized Dirac-spin closure behind the torsion-bounce chain (entries 9, 10, 11; propagates to 39, 52, 53, 59)

**Tori, 2026-09-03 19:18 KST. Ordered by Duho (verbatim "k3", relay via Blanc 19:17 KST): K3 FIRST STEP ONLY; the full transfer function (n_s, r)
is NOT ordered. Written and committed BEFORE any derivation. Gated by a fresh seat via `nm_referee_dispatch.sh` (ACCESS_SHA proof
or no verdict) before filing. Results ship with a one-page check sheet and an independent second route. Paper HOLD; nothing
outward; tiers untouched; stamps are Duho's.**

## 0. Why this exists
The Einstein–Cartan torsion-bounce chain (entries 8–12, 40, 41, 51, 53, 59; ten warrant cells at `W_MIXED`/`W_UNDERIVED`,
`WARRANT_TABLE_20260903.md`) rests on one closure: the square of the spin density of an UNPOLARIZED fermion fluid as a function of
number density n. Two closures are in print in this corpus, and entry 10 prints both on one page:
- **Spin-fluid closure:** s² ≡ ½ s_ij s^ij = ⅛ (ℏcn)² — entry 9 `1007.0587_clean.txt` L90–91 ("for a fluid consisting of fermions with
  no spin polarization"); entry 11 `1410.3881_clean.txt` L84–85 (cited to Gasperini 1986 and Nurgaliev & Ponomariev 1983); entry 10
  `1111.4595v2_poplawski_prd85_clean.txt` L121 ("s² = ½ s_ik s^ik = ⅛ n² [8, 9]", units c = ℏ = 1).
- **Dirac-pseudovector closure:** with s^i = ½ ψ̄γ^iγ⁵ψ (entry 10 Eq. 4, L75–77), "The average value of its square is ⟨s²⟩ = ¾ n²"
  — entry 10 L113–114.
The two coefficients differ by a factor of six. Neither paper derives its closure; the warrant column marks them borrowed/asserted
(rows 9, 10, 11). The first-step question is whether ONE ensemble average over unpolarized Dirac spins yields both, one, or neither.

## 1. Objects, every symbol bound
- **Dirac spin pseudovector** s^i = ½ ψ̄ γ^i γ⁵ ψ (entry 10 L75–77, Eq. 4; ℏ = c = 1 there). The completely antisymmetric spin tensor
  s_ijk = −e_ijkl s^l (same lines).
- **Spin-fluid spin tensor** s_ij with s_ijk = s_ij u_k, s_ij u^j = 0 (entry 10 L118–119, the Hehl–von der Heyde–Kerlick approximation;
  entry 9 L66–73 and entry 11 L74–81 define s² = ½ s_ij s^ij).
- **n** — the fermion number density (entry 10 L114). **Unpolarized ensemble** — spin orientations uniformly distributed on the
  sphere in the fluid rest frame, uncorrelated between particles; occupation statistics enter only through n at this order.
- **The two printed closures**, C_fluid: s² = ⅛ (ℏcn)² and C_Dirac: ⟨s_i s^i⟩ = ¾ n², as quoted above.

## 2. The question, exactly
Starting from single-particle Dirac spinors (plane-wave, normalised so ψ̄γ⁰ψ integrates to one particle) and the unpolarized
ensemble of §1, compute (i) ⟨s_i s^i⟩ for the macroscopic pseudovector density and (ii) ½⟨s_ij s^ij⟩ for the macroscopic spin-fluid
tensor, keeping track of how each scales with n (a mean of a square of a sum of N uncorrelated random spins scales as N, a square of
a mean or an RMS convention scales as N²). Then state: which printed coefficient, if either, follows; whether the two refer to the
same object; and whether the n² scaling itself follows from the unpolarized average or is a convention.

## 3. Outcome classes — declared now
- **CLOSURE_18_DERIVED:** the spin-fluid coefficient ⅛ follows for ½⟨s_ij s^ij⟩ with the n² scaling, under a stated prescription.
- **CLOSURE_34_DERIVED:** the Dirac coefficient ¾ follows for ⟨s_i s^i⟩ with the n² scaling, under a stated prescription.
- **CLOSURE_BOTH_CONSISTENT:** both follow and refer to different objects related by a derived identity (state it); no conflict.
- **CLOSURE_CONFLICT:** both cannot hold for the same object — a proof that the two printed closures contradict each other (which
  entry 10 uses simultaneously at L113 and L121); the factor-six gap is an inconsistency, not a change of object.
- **CLOSURE_SCALING_FAILS:** the unpolarized average of either square scales as n, not n²; the printed n² closures are RMS or
  coherence conventions, not results of the average (state the convention that would produce each coefficient).
- **CLOSURE_PRESCRIPTION_DEPENDENT:** the coefficient depends on an averaging or normalisation choice the papers do not fix and the
  ensemble does not determine → INCONCLUSIVE; name the free choice and the coefficient each choice gives.
More than one class may hold for different objects; report each object's class separately, and one headline for the chain.

## 4. What counts as a verdict either way
A symbolic derivation (gamma-matrix algebra executed and checked by script, every trace printed) from the §1 objects to the two
averages, with the n-scaling shown explicitly, ending in one class per object. A verdict that rests on citing Gasperini 1986 or
Nurgaliev & Ponomariev 1983 (not pinned; paywalled) instead of deriving is not a verdict; those papers are acquisition targets for
context only.

## 5. Controls (must pass before any class is filed)
- **C1 single particle:** the script must return s_i s^i = ¾ (units ℏ = 1) for one Dirac particle at rest with the stated
  normalisation — the spin-½ Casimir s(s+1). Failure = the spinor machinery is wrong; stop; no class.
- **C2 fully polarized limit:** replacing the orientation average by all spins along +z must return the polarized macroscopic
  closure s_z = n/2 (ℏ = 1) and s_i s^i = n²/4 with n² scaling. Failure = stop; no class.
- **C3 units:** restoring ℏ and c must reproduce the (ℏcn)² form of entries 9 and 11 for the fluid object. Failure = stop.
- **C4 deletion probe:** removing the orientation average (i.e., running C2's ensemble through the unpolarized pipeline) must change
  the class of at least one object; the exact expected change is stated by the seat before running it.

## 6. Seat plan, blind double, cost
- Route 1: codex and the Claude seat, blind, each its own sympy gamma-matrix script (`K3S1_<seat>_spin.py`) and result
  (`K3S1_<seat>_RESULT.md`, written only when complete). Third seat agy via `nm_referee_dispatch.sh` on any split. Kimi
  (`--provider moonshot`, agent.log checked for no fallback line) audits the pin/check sheet arithmetic.
- Route 2 (Duho's "both" standard, dispatched after route 1 lands): a fresh seat, blind to route 1, by the DENSITY-MATRIX route —
  the unpolarized single-particle state ρ = ½·1 in spin space, Tr(ρ Σ_i Σ_j) and the fluid sum — no explicit spinor components.
- Cost (planning estimate, not a corpus number): two to four seat-days; no data; no compute beyond a laptop.

## 7. What would make it INCONCLUSIVE
CLOSURE_PRESCRIPTION_DEPENDENT for the headline object; or C1–C3 failing in both seats after two attempts; or the seats disagreeing
on which object entry 10's L113 average refers to after a third seat.

## 8. Non-circularity
No cosmological data enters. The printed coefficients are the things under test, not inputs; the derivation starts from the Dirac
spinor and the ensemble definition. Downstream cells (39, 52, 53, 59) are touched only by annotation after Duho's ruling.

## 9. Acquisition targets (context, non-blocking)
Gasperini, Phys. Rev. Lett. 56, 2873 (1986); Nurgaliev & Ponomariev, Phys. Lett. B 130, 378 (1983); Hehl & Datta, J. Math. Phys.
12, 1334 (1971). Paywalled, pre-arXiv; if Duho downloads them they are pinned and the derivation compared to theirs.
