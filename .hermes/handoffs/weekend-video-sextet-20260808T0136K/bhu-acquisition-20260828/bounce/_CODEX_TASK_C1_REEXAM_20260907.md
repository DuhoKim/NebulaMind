# BOUNDED CODEX TASK — re-examine C1 with the two matter rows correctly distinguished (Tori, 2026-09-07)

Your earlier C1=FAIL (`B1_DERIVATION_20260907.md`) compared a FLUID-row expression with a DIRAC-row one. Read
`B1_SIGN_RESOLUTION_20260907.md` first: PRD 85, 107502 uses the DIRAC spin tensor (eps_tilde = -p_tilde = -alpha n^2,
alpha = 9kappa/16); GRG 53, 18 uses the WEYSSENHOFF SPIN FLUID (eps_tilde = eps - alpha n_f^2, p_tilde = p - alpha n_f^2,
alpha = kappa(hbar c)^2/32). They are different physics, not a contradiction. Redo the comparison with the rows kept apart.

## Boundaries
- Write ONLY under `bounce/`. No pinned census file, no kit, no census version, no Hwao data.
- Do not resolve anything by authority or by preferring a paper. Show algebra.
- Where you state what a paper says, cite the equation number; the local publisher PDF is
  `bounce/prd_publisher_verify_20260907/prd_pdf.pdf` for the PRD paper.

## Do exactly this
1. **C1 restated, per row.** State the C1 recovery test separately for each row: (a) FLUID row — does the anisotropic system of
   GRG 53,18, with shear set to zero and no production, reduce to a consistent isotropic bounce IN ITS OWN TERMS? (b) DIRAC row —
   does the PRD system reproduce its own published cusp, Eqs. (14)-(17)? Report C1_FLUID and C1_DIRAC separately with PASS/FAIL
   and the compared expressions. A cross-row comparison is NOT a C1 test; if you report one, label it as a contrast, not a gate.
2. **State plainly whether the original C1=FAIL survives.** If the failure was entirely an artefact of mixing rows, say so in one
   sentence: "the original C1=FAIL does not survive; it compared rows." If part of it survives for an independent reason — the
   temperature-law mismatch, the conserved-number relation, the cusp-versus-smooth-turning-point distinction — state exactly
   which part and show it within a single row.
3. **The K3 ratio for the FLUID row.** K3 step 3 computed R = |eps_tilde|/eps = alpha h_n^2 T^2 / h_star = 2/3 at the DIRAC
   row's turning point with alpha = 9kappa/16. Recompute the analogous self-consistency ratio for the FLUID row, at the FLUID
   row's own turning point, with alpha = kappa/32 in hbar=1 units, using the same thermal forms
   (eps = h_star T^4, p = eps/3, n = h_n T^3). Print: the fluid row's turning-point temperature, the ratio there, and whether it
   clears the 0.1 threshold K3 declared. Show the algebra; do not reuse the Dirac number.
4. Everything symbolic in `bounce/c1_reexam.py`, runnable as `/usr/bin/python3 c1_reexam.py`, printing C1_FLUID, C1_DIRAC, the
   fluid-row ratio, and a token ORIGINAL_C1_FAIL=SURVIVES or ORIGINAL_C1_FAIL=WITHDRAWN. No writes outside `bounce/`.

## Output: `bounce/C1_REEXAM_20260907.md` and `bounce/c1_reexam.py`
Print both sha256s and the four tokens as your final answer. Do not evaluate the B1 criterion and do not run C2/C3.
