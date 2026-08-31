# CODEX mapping-convention referee — MAPCONV-V1

## Verdict

**DIVERGENT.** The subject identity was verified before reading: `ref/gain_mapping_a.py` SHA-256 is exactly `079abac055056c6c2d7b67c26b6afd9e21d66535f8dc9f0fb7dbd69e47ecffc4`. The implementation faithfully reproduces the ruled sign-redraw mechanics and correctly leaves the across-draw reduction to the sweep/replay layer. But it turns three conventions not fixed by the ruling into behavior: the definitions of `a0` and `c_bar`, pointwise clipping of the ruled linear field, and the exact transformation of the calibration object. All three may be defensible choices; none is thereby the principal's ruled choice. The mapping cannot yet be named THE ruled executable mapping without an amendment that freezes them.

## Point-by-point judgment

### 1. Intercept and centering population — compatible, but not ruled

The ruling fixes only the functional form `a(c) = a₀ + γ·(c − c̄)`. It does not define `a₀`, does not say that it is `cal["a_hat"]`, and does not define the population over which `c̄` is taken. The singular `a₀` is consistent with a global intercept rather than a separate per-bin intercept; `cal["a_hat"]` and the mean of the exact input mask are natural implementations. Production also uses the full-mask mean in `w_profile()` and `w_gradient()`. Those facts establish compatibility, not principal authorization. In particular, the executable choice “mean of whichever mask object the caller supplied” needs to be frozen as the sealed BS-2f/post-exclusion population rather than inferred from an implementation argument.

### 2. Redraw mechanics — faithful

This part matches the cited production shape exactly:

- latent sign: `+1` iff the first uniform is below `(1 + A_LONGO*c)/2`, else `−1`;
- accepted sign: flip the latent iff the second uniform is below `1 − a`;
- consumption order: `u[2k]` is object `k`'s latent draw and `u[2k+1]` its flip draw, byte-for-byte equivalent to `inject_signs()`'s two sequential `rng.random()` calls per object;
- common random variates: one interleaved `2*n` stream is materialized once per draw and reused across every γ.

Vectorizing the consumption does not change the PCG64 sequence or its object-wise ordering. The module's 9/9 self-test also executed successfully, including its real counterfactual-path integration control.

### 3. Worst case over draws — correctly outside this module

The ruling separates the stochastic mapping from its reduction. `MappingA(draw_index)` maps one committed draw across γ; the draft's replay/sweep contract owns the 99×51 verdict matrix and defines `HELD` by within-draw comparison to that draw's γ=0 cell. Therefore the module should not perform the worst-case reduction. Putting it here would mix a one-draw mapping primitive with the receipt-producing aggregate and duplicate the sweep runner's custody.

### 4. Physical clamp — an unruled model amendment

Clipping `a0 + γ(c−c_bar)` to `[0.5+1e-9, 1]` is not in option A. It changes the ruled linear field into a piecewise-linear saturated field at precisely the γ/object cells where the raw model leaves production's legal probability domain. Production does not clip: `inject_signs()` refuses accuracy outside `(0.5, 1]`. The ratified-range proposal likewise says gradients beyond calibration admissibility are to be caught by the calibration gate; it does not authorize replacing them by boundary probabilities before that gate is evaluated.

The module discloses the clamp in its own docstring and diagnostics, so it is not hidden from a code reader. It is nevertheless silent relative to the ruling: self-description cannot amend the principal's model. A filed amendment must choose clipping versus refusal (and the exact lower endpoint) and state how clipping interacts with the calibration-failure consequence.

### 5. `cal'` — joint movement is required; this exact construction is extra

The joint-counterfactual ruling requires the sign vector and calibration supplied to the real decision path to move together; returning unchanged `cal` would reintroduce the rejected amplitude-only/fixed-significance reduction. Computing per-bin means of the same `a_gamma` used for the redraw satisfies that minimum coherence requirement.

The ruling does not, however, prescribe the rest of this implementation: preserving every original lower-bound margin, preserving `sigma_a`, `sigma_ab`, and `cov_a`, using the full-mask mean for `a_hat'`, or retaining the original value for an empty bin. Those are additional statistical assumptions about what γ changes and what uncertainty remains fixed. They may be the intended “field moves, measurement noise does not” counterfactual, but that sentence originates in the module, not in the ruling. The executable mapping therefore needs an amendment that freezes this calibration transformation (including the empty-bin rule), or a narrower mapping contract plus a separately pinned calibration-transform contract.

## Held attacks

- I found no mismatch in the latent law, flip law, or two-uniform interleaving.
- I found no basis for requiring the one-draw mapping module itself to reduce the draw set.
- The mechanics commitment's zero-based spawn rule, 99 draws, master seed, PCG64 generator, and common-random policy agree with the implementation at the reviewed surface.

SEAT: CODEX
VERSION: MAPCONV-V1
VERDICT: DIVERGENT
COUNT: 3
F1 | `a0` / `c_bar` are implementation-selected, not ruled | The ruling says only “Option A: `a(c) = a₀ + γ·(c − c̄)`”; it does not identify `a₀` with `cal["a_hat"]` or define the population for `c̄`.
F2 | The clamp changes the ruled linear field | The ruling says “signs redrawn under the position-dependent accuracy,” while the cited production shape says “`s = −lat` with probability `1 − a_b`”; neither authorizes replacing out-of-domain linear values by `[0.5+1e-9, 1]` boundary values.
F3 | The exact `cal'` transform is an additional statistical convention | The joint-path ruling requires that “amplitude and significance move together,” but does not rule per-bin averaging, preserved lower-bound margins, unchanged `sigma_a`/`sigma_ab`/`cov_a`, or the empty-bin fallback.
