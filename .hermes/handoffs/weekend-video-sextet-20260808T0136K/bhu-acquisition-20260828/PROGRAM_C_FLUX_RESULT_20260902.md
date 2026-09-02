# Program (C) result — the flux condition, imposed on the perturbed solution, produces no cutoff

**Date:** 2026-09-02 16:45 KST · **Coordinator:** Tori · **Ordered by Duho:** "go ahead with the flux
condition route" (direct chat, chat-confirmed: `PROVENANCE_DIRECT_CHAT_20260902.md`).
**Prereg:** `PROGRAM_C_FLUX_PREREG_20260902.md`, committed 6c813f967 before any derivation existed.
**Status:** lane-owned result. Closes freedom-map flag (ii). Gated `RESULT_SOUND_WITH_REPAIRS` (codex, `FLUX_RESULT_GATE_codex.md`; two tier-language sentences removed per prereg §5 grammar).

## The question in everyday words
Gaztañaga's paper has exactly one condition it actually derives: the gravitational "flux" through
the edge of our causal region must vanish. He uses it to fix the cosmological constant. Nobody had
asked what the same condition says about the lumps and ripples in the universe, which is where a CMB
cutoff would have to come from. We asked, two ways.

## Result, in one line each
- **F1 (the paper's own usage, our causal region only): FLUX_ALPHA.** The condition is one number,
  the spherical average of the lumpiness inside our causal sphere. By rotational symmetry it touches
  only the sky's monopole, ℓ = 0, which is unobservable. Every C_ℓ for ℓ ≥ 1, and hence S₁/₂, is
  exactly unchanged.
- **F2 (the condition for every observer): FLUX_GAMMA.** It becomes a convolution equation
  `W ⋆ δ = 0`; in Fourier space `W̃(k) δ̃(k) = 0`. A compactly supported window has an entire
  transform (Paley–Wiener) with isolated zeros, so δ̃ may live only on a measure-zero set of shells:
  no continuous power spectrum survives except P ≡ 0. Incompatible with the observed acoustic spectrum.

Neither reading is FLUX_BETA. Corollary (claude-seat, checked): the paper's hoped-for "infrared cutoff in the spectrum of inhomogeneities" is not a solution of F2 — every k off the window's zero shells must vanish, not just k < k_§ — and |W̃(k)| is largest at k → 0, so where F2 bears hardest on large scales it says "zero", not "suppress". **The flux condition is not the missing perturbation prescription;
imposed on the perturbed solution it says either nothing about anisotropies or too much to be true.**

## Independent derivations (blind, one brief, four model families)

| seat | F1 | F2 | notes |
|---|---|---|---|
| codex (OpenAI) | FLUX_ALPHA | FLUX_GAMMA | conformal Newtonian gauge; Schur-type invariance argument; notes the gauge subtlety of a coordinate-fixed window |
| agy (Gemini) | FLUX_ALPHA | FLUX_GAMMA | synchronous gauge; Wigner–Eckart argument |
| kimi (Moonshot) | FLUX_ALPHA | FLUX_GAMMA | comoving slicing; numerically verified W̃(0) and the zeros to 1e-14 |
| claude-seat (Fable, fresh context) | FLUX_ALPHA | FLUX_GAMMA | comoving-synchronous gauge; Haar-average form of the Schur argument; F2 strengthened through the transfer functions (K(k) = Σ_A∫dη c_A W̃ T_A, entire in k); adversarial audit of seven failure routes, none opens; corollary: an IR cutoff P = 0 for k < k_§ does NOT satisfy F2 either |

All four derive `δR⁰₀ = 4πG(δρ+3δp)` at linear order with the metric entering only through
`δ√−g · R̄⁰₀`; all four obtain the top-hat transform `(4πR³/3)·3j₁(kR)/(kR)` with zeros at
kR = 4.4934, 7.7253. Files `FLUX_{codex,agy,kimi,claude}.md`.

## Coordinator's numeric control (`flux_monopole_check.py` → `_tmp_flux_check.out`)
Gaussian field with a smooth positive P(k), top-hat window radius R, shell radius 0.6R, 400
realisations. Cross-correlation of the window functional δ_§ with the shell multipoles:

| (ℓ,m) | ⟨δ_§ a_ℓm⟩ | ± | |mean|/err |
|---|---|---|---|
| (0,0) | +1.712 | 0.124 | 13.9 |
| (1,0) | +0.061 | 0.065 | 0.9 |
| (1,1) | +0.015 | 0.065 | 0.9 |
| (2,0) | +0.001 | 0.048 | 0.0 |
| (2,1) | +0.019 | 0.048 | 0.6 |
| (2,2) | +0.050 | 0.046 | 1.1 |

Analytic ℓ = 0 value from P(k): +1.747 (MC/analytic agree to 0.3σ). The control that must fire,
fired (ℓ = 0 at 14σ); the ones that must not, did not (all ℓ ≥ 1 within 1.1σ of zero). F2 control:
∫P|W̃|²k²dk/(2π²) = 0.0988 > 0, so ⟨(W⋆δ)²⟩ cannot vanish for a positive spectrum. First run of this
script carried a field-normalisation error (MC and analytic ℓ = 0 differed by 10⁶ while the zero
pattern was already right); fixed before anything was filed, noted here so the receipt is honest.

## What this does and does not establish
- Establishes: for ANY spherically symmetric 4-window about the observer (the paper does not fix
  M_§'s shape; this covers every choice), F1 constrains only the monopole — a symmetry result, not a
  numerical one. And F2 admits no continuous spectrum for ANY compactly supported window.
- Does not establish: anything about a causal completion that changes transfer physics, matching,
  or the observer's position (freedom map §7's structural caveat stands). The flux condition itself
  is the only thing tested here.
- Gauge: the split of δΦ into fluid and volume-element pieces is gauge-dependent; the conclusion
  (monopole-only / convolution) uses only the window's spherical symmetry and compact support, which
  hold in any gauge in which M_§ is defined as the paper defines it (comoving χ ≤ χ_§).

## Consequence for the record
Freedom-map §2 flag (ii) — "Φ(χ>χ_§)=0 has never been imposed on the perturbed solution by anyone" —
is closed: it has now been imposed, and it does not generate a cutoff. The "open route" clause in the
entries 23–27 Phase (b) map is updated to point here.
