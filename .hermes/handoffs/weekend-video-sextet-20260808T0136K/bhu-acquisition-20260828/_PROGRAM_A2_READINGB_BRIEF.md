# BUILD READING B AND COMPUTE ITS S_1/2 — Program (A), no-go branch

Duho ruled "topic A": calibrate or formally kill the 60° cutoff. Four seats already established the
paper licenses **no** sharp perturbation condition (`READING_C`, unanimous). The deliverable is now
the **no-go, made quantitative**: show that the two mutually-exclusive refinements of the paper's
one perturbation sentence give **different answers**, so the number depends on a choice the theory
does not make.

Reading A (Fourier cut) is already computed. **Reading B has never been built. Build it.**

## What is already established (do not redo, do not contradict without evidence)

- Source: arXiv 2003.11544. Its only *derived* condition is `Φ(χ>χ§)=0` (Eq. 16, a 4-volume flux
  integral of `R⁰₀`) which **implies Eq. 17**, fixing Λ. It is **not** a perturbation boundary
  condition.
- Its only perturbation sentence: "There should be a smooth background across disconnected regions
  **with an infrared cutoff in the spectrum of inhomogeneities for χ>χ§**." Tentative modality, one
  occurrence, no equation.
- `χ_§ = (3.149 ± 0.006) c/H₀` (Eq. 23) = 14,015 Mpc. `θ_§ = χ_§/χ(z=1100) = 57.4°`.
- **A and B are mutually exclusive** (verified numerically + Paley–Wiener): compact `ξ` forces `P`
  entire, so it cannot vanish on `[0,k_§)`; a hard cut in `P` leaves oscillatory `ξ` tails past `χ_§`.
- **Reading A result:** `P(k)=0` for `k<k_§=2π/χ_§` gives full-sky unlensed `S₁/₂ = 6,897 μK⁴`
  (ΛCDM: 34,924; observed: ~1,150).
- `S₁/₂ = ∫_{-1}^{1/2} C(θ)² d cos θ`. Operator validated to 1e-14 and reproduces ΛCDM 34,926.

## YOUR TASK

**Construct Reading B and compute its `S₁/₂`, full-sky unlensed, same pipeline as A.**

Reading B is `ξ(r) = 0` for `r > χ_§` on the primordial field. The natural construction:

    ξ_B(r) = ξ_ΛCDM(r) · W(r),    W compactly supported on [0, χ_§]

Use a **positive-definite** window so `P_B ≥ 0` is guaranteed rather than hoped — e.g. the
spherical-overlap kernel `W(r) = (1-x)²(2+x)/2`, `x = r/χ_§`, whose transform is `[3j₁(ka)/(ka)]² ≥ 0`.
Product of two positive-definite functions is positive-definite (Schur/Bochner), so state that as the
guarantee. Then `P_B(k) = 4π ∫₀^{χ_§} dr r² ξ_B(r) sinc(kr)`, normalized so `P_B → P_ΛCDM` at
`k ≫ 2π/χ_§` (the high-ℓ data is held out and must not be refit).

**THE TRAP YOU MUST CONFRONT, NOT AVOID.** For a near-scale-invariant primordial spectrum,
`ξ(r) = ∫ dk/k Δ²(k) sinc(kr)` is **log-divergent in the infrared**. The divergence is
`r`-independent (a constant `c`), and a constant in `ξ` is an unobservable monopole — **but**
multiplying by `W` and transforming back contributes `c·W̃(k)`, and `W̃` is concentrated at
`k ≲ 2π/χ_§`, i.e. exactly the multipoles that dominate `S₁/₂`.

So: **does `S₁/₂` under Reading B depend on the IR regulator?** Compute it for several `k_min`
spanning at least 3 decades below `k_§` and report the dependence explicitly. **If it depends on
`k_min`, that is a RESULT, not a bug** — it means Reading B's prediction is set by a regulator the
theory does not fix, which is the no-go appearing concretely. Do not hide it by fixing `k_min`
silently.

## Deliverables

1. `P_B(k)` construction, with the positive-definiteness argument stated and `P_B ≥ 0` verified
   numerically on the grid.
2. `S₁/₂` for Reading B, full-sky unlensed, via CAMB `set_initial_power_table`
   (`effective_ns_for_nonlinear=n_s`, `NonLinear_none`, `lens_potential_accuracy=0`), ℓ_max ≥ 100.
3. **The `k_min` sensitivity table.** This is the most important output.
4. A one-line comparison: ΛCDM 34,924 · Reading A 6,897 · **Reading B ?** · observed ~1,150.
5. State whether A and B land on the **same or opposite sides** of 1,150. kimi predicted opposite.

## Rules

- Cosmology: H0=67.36, ombh2=0.02237, omch2=0.1200, tau=0.0544, As=2.1e-9, ns=0.9649, mnu=0.06.
- Write a runnable script `cutoffA_readingB.py` in this directory and **run it to completion**;
  paste its actual output. No claimed results without execution.
- Do not fit anything to low-ℓ data. Do not tune `χ_§`.
- If the construction is ill-posed, say so and say exactly why — a proof that Reading B cannot be
  built is as valuable as a number.
