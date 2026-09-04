# K4 limb 2 — blind seat brief (the a-priori check, before any Planck pixel)

**Authority:** Duho, "k4", relayed 2026-09-04 13:15 KST. **Governing document:**
`K4_BOUNDARY_TRANSFER_PREREG_20260904.md` (frozen V2) — read it in full first; it binds you.

**BLIND.** Do NOT open, list, grep or infer the contents of any file whose name contains `K4_claude`, `K4_codex`,
`K4_LIMB2_RESULT`, `K4_ROUTE2`, `K4_CHECK` or `K4_RECONCIL`. You MAY read the prereg, `K2_RESULT_20260903.md`,
`K2_CHECK_SHEET_20260903.md`, `PROGRAM_C_FLUX_RESULT_20260902.md`, `PROGRAM_C_FLUX_PREREG_20260902.md`,
`PROGRAM_A_FREEDOM_MAP_20260902.md`, and the source `../bhu-reading-20260823/sources/gaztanaga_mass_mnras_clean.txt`.

**DO NOT TOUCH THE PLANCK DATA.** Do not open `planck_data/`, do not load a map, do not call the estimator. This limb
is decided before any pixel. A seat that reads the map fails the run.

## The single question

Prereg §4 limb 2: **does the PERTURBED Darmois junction at the comoving edge of K2's B1 cell reduce to an F1/F2-type
condition?**

- **F1** (`PROGRAM_C_FLUX_RESULT_20260902.md` L15–18) touches only the monopole `ℓ = 0`; every `C_ℓ` for `ℓ ≥ 1` is
  exactly unchanged.
- **F2** (same file, L19–22) forces `W̃(k) δ̃(k) = 0`, so no continuous power spectrum survives except `P ≡ 0`.

If the perturbed junction reduces to either, the route is dead a priori and the study stops without touching a pixel.
If it does not, say exactly what it does impose instead.

## What you must derive

1. **The background you are perturbing**, restated from K2: `k = 0`, `Λ = 0` comoving dust top-hat of comoving radius
   `χ*`, `M = (4/3)π χ*³ ρ₀`, matched to Schwarzschild across a comoving timelike surface, class `J_SMOOTH_EXPANDING`.
2. **Declare your gauge in the script header BEFORE the code that uses it.**
3. **The perturbed Darmois conditions** at the comoving edge — the first and second fundamental forms continuous at
   linear order — written out for scalar perturbations, multipole by multipole.
4. **What they impose on the interior modes.** Be explicit and structural: does the condition (a) annihilate the
   perturbation, (b) touch only `ℓ = 0`, (c) select a discrete set of radial modes for each `ℓ`, (d) relate interior
   modes to exterior vacuum modes without constraining the interior spectrum, or (e) something else? Name it and show
   why. Treat the exterior as Schwarzschild vacuum and say what Birkhoff's theorem does and does not give you there.
5. **Compare to F1 and F2 explicitly**, and state whether the condition is of that type. This is the deliverable.
6. **The `ℓ` and `k` structure**: if the condition discretises the radial spectrum, give the spacing in terms of `χ*`
   and say how it compares with the causal scale `χ_§ = 3.149 c/H₀ = 14,015 Mpc`.

## Deliverables — exactly two files, nothing else changed

1. `K4_limb2_<seat>.py` — self-contained, runs under `python3`, prints everything it claims. **Run it.** Under prereg
   §7 a named script is not a receipt until someone runs it: if a claim is not printed by your script, do not make it.
2. `K4_LIMB2_<seat>_RESULT.md` — first line exactly one of:
   `LIMB2_REDUCES_TO_F1` · `LIMB2_REDUCES_TO_F2` · `LIMB2_NOT_F1_F2` · `LIMB2_UNDETERMINED`
   and nothing else on that line. Then the derivation in prose with your script's printed lines as receipts.

## Rules

- If the perturbed junction admits a family of boundary conditions the Darmois conditions do not fix, say
  `LIMB2_UNDETERMINED` and name the freedom exactly — which multipole, which parameter, which range. **Do not
  manufacture a boundary condition.**
- Inherit K2's limits and restate them: dust only, exact spherical symmetry, `0 ≤ Λ ≤ Λ_c`.
- Every numeral traces to a source line you cite or to a quantity your script printed.
- You have no authority over any tier, warrant token, standing or stamp.

K4_LIMB2_SEAT_BRIEF_COMPLETE
