# BOUNDED CODEX TASK — B1 step 1: derive the Bianchi I Einstein–Cartan bounce criterion (Tori, 2026-09-07)

Work ONLY from `bounce/B1_PREREG_BIANCHI_I_BOUNCE_20260907.md` (the pre-registration, read it first) and
`bounce/SOURCES_20260907.md` (the verified equations). You DERIVE and CHECK. You do not file a class, do not decide the physics
question, and do not write any conclusion about black-hole-universe cosmology.

## Boundaries (hard)
- Create or edit files ONLY under `bounce/`. Touch no pinned census file; run no R3C2 kit; open no census version.
- Do not read any Hwao lane or unopened evaluation data.
- Published sources only for physics: S1 (Gen. Relativ. Gravit. 53, 18), S3 (Phys. Rev. D 85, 107502 (2012)), S4 (Rev. Mod. Phys.
  48, 393 (1976)). Quote equation numbers. The 2307.12190 chapter is CONTEXT ONLY — its peer review is NOT ESTABLISHED.
- Do NOT assume the free-gas spin closure at the bounce. Carry α as an interval; K3 step 3 is quoted in SOURCES §D.

## Do exactly this
1. **Derive, symbolically (sympy), the Bianchi I Einstein–Cartan system** for a spin fluid: directional scale factors, mean
   `a`, shear `σ²`, with `ε̃ = ε − α n_f²` and `p̃ = p − α n_f²` per S1 Eq. (1). Print the generalised Friedmann constraint and the
   Raychaudhuri equation you obtain, and show the steps. State every assumption you had to add that the sources do not print, as
   an explicit list — that list is a required output, not a footnote.
2. **CONTROL C1 (do this before anything else is interpreted):** set σ²=0, no production, and reproduce S3's published isotropic
   bounce, including the cusp condition da/dT = 0 and its Eq. (16)–(17) content. Print PASS/FAIL with the compared expressions.
   If C1 FAILS, STOP and write only the failure — do not proceed to step 3.
3. **CONTROL C2:** show the reduction of your equations to S4's (5.21)/(5.24) forms in the stated limit, or state precisely why it
   does not reduce. PASS/FAIL.
4. **The criterion:** with `ε = ε₀a⁻⁴`, `n_f = n₀a⁻³`, `σ² = Σ²/a⁶` and NO production, solve `H = 0` for finite `a` and print the
   exact bounce criterion and `a_min`. Verify or REFUTE the pre-registration's §3 claim that shear and torsion both scale as a⁻⁶
   so the criterion is a comparison of constants. Show the algebra either way. If §3 is wrong, say so plainly and show why.
5. **CONTROL C3 (well-posedness before interpretation):** verify constraint propagation for the system you derived — that the
   Friedmann constraint is preserved by the evolution equations — and state the regime of validity. PASS/FAIL, with the residual.
6. **α interval:** express the criterion in the dimensionless ratio the prereg names, and state how the answer moves across the
   K3S3 interval (free-gas value controlled only below ~0.32 T_cr; uncontrolled at the bounce). Do not pick a single α.

## Output: exactly two files
- `bounce/B1_DERIVATION_20260907.md` — the derivation, every added assumption, C1/C2/C3 with PASS/FAIL and their compared
  expressions, the criterion, and the α-interval statement. Quote sources by equation number.
- `bounce/b1_derive.py` — the sympy script that produces every printed result, runnable as `/usr/bin/python3 b1_derive.py`,
  printing each control's PASS/FAIL token and the criterion. No network, no writes outside `bounce/`.
Print both files' sha256, the script's exit code, and the C1/C2/C3 tokens as your final answer.
