# BOUNDED CODEX TASK — B1 steps C2, C3 and the criterion, both rows (Tori, 2026-09-07)

C1's status is now settled: `C1_REEXAM_20260907.md` reports C1_FLUID=PASS, C1_DIRAC=PASS, ORIGINAL_C1_FAIL=WITHDRAWN. The gate
that blocked C2/C3 is therefore lifted. Work strictly within the pre-registration
`B1_PREREG_BIANCHI_I_BOUNCE_20260907.md` INCLUDING ITS AMENDMENT 1, and keep the two matter rows apart throughout.

## Boundaries
- Write ONLY under `bounce/`. No pinned census file, no kit, no census version, no Hwao data.
- Carry alpha as a symbol; report results for BOTH rows (fluid alpha_F = kappa hbar^2/32, Dirac alpha_D = 9 kappa/16). Never
  pick a single numeric alpha at the bounce, and do not import the free-gas closure there as though it were controlled.
- Do not file an outcome class. I file classes. You produce the algebra and the tokens.

## Do exactly this
1. **C2 — formalism reduction.** Show whether the Bianchi I Einstein-Cartan system you use reduces to the combined
   energy-momentum forms of Hehl, von der Heyde, Kerlick & Nester, Rev. Mod. Phys. 48, 393 (1976) in the stated limit — the
   publisher PDF is at `bounce/prd_publisher_verify_20260907/rmp_pdf.pdf`, equations (3.23)-(3.24) and the p. 400 passage.
   Report C2_FLUID and C2_DIRAC with PASS/FAIL and the compared expressions.
2. **C3 — well-posedness BEFORE any interpretation.** For the Bianchi I system with shear, spin-torsion and (separately) with a
   particle-production term, verify that the Hamiltonian (Friedmann) constraint is propagated by the evolution equations. Print
   the constraint residual symbolically. Report C3_FLUID and C3_DIRAC with PASS/FAIL. If a residual is non-zero, that is the
   result — state it and stop interpreting that case physically.
3. **The criterion, no production.** With eps = eps_0 a^-4, n = n_0 a^-3, shear sigma^2 = Sigma^2/a^6 in Bianchi I:
   (a) FLUID row: solve 3H^2 = kappa(eps - alpha_F n^2) + Sigma^2/a^6 for H = 0 at finite a. Print the exact bounce criterion,
       a_min, and state explicitly whether the shear term and the torsion term share the a^-6 scaling — the pre-registration
       claims they do and that the criterion is therefore a comparison of CONSTANTS. Verify or REFUTE that, showing the algebra.
   (b) DIRAC row: do the same, using that row's effective density, and state whether its criterion differs in form.
   (c) For each row, evaluate the ratio |eps_tilde|/eps AT the bounce the criterion defines, WITH shear present. Say whether it
       exceeds K3's declared 0.1 small-correction threshold, and whether the value is a derived consequence or true by
       construction (the flat shear-free fluid case gives 1 by construction — say so where that is the reason).
4. **The production pivot, stated not solved.** Write down, without solving, what changes when a production term is added: which
   scaling breaks, and what would have to be true of the production law for the criterion to stop being a comparison of
   constants. Cite GRG 53,18's own production equations by number. Do NOT evaluate whether production rescues the bounce.
5. Everything symbolic in `bounce/b1_criterion.py`, runnable as `/usr/bin/python3 b1_criterion.py`, printing
   C2_FLUID, C2_DIRAC, C3_FLUID, C3_DIRAC, the two criteria, the two a_min expressions, the two ratios, and
   SCALING_DEGENERATE=YES|NO for each row. No writes outside `bounce/`.

## Output: `bounce/B1_CRITERION_20260907.md` and `bounce/b1_criterion.py`
State every assumption you add that the sources do not print. Print both sha256s and all tokens as your final answer.
