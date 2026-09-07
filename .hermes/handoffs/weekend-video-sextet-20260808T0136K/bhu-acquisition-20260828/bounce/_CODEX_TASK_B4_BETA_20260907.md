# BOUNDED CODEX TASK — B4: does the source supply usable production-coefficient values? (Tori, 2026-09-07)

Completing a DECLARED pre-registration deliverable that B3 omitted: the required beta range must be "stated and compared with
S1's own values". Establish whether the inspected source supplies usable values and a normalisation, or whether the comparison
is unresolvable from it. You do NOT file a class and you do NOT re-open the B3 result.

## Boundaries
- Write ONLY under `bounce/`. No pinned census file, no kit, no census version, no Hwao data, no new framework.
- Bind every equation claim to the exact version you inspect and name it. The Springer publisher page is behind a cookie
  handshake; if you cannot reach it, say so and do not claim publisher identity.
- Published peer-reviewed sources for physics; label preprints.

## Do exactly this
1. In the inspected text of Poplawski, GRG 53, 18 / arXiv 2007.11556v2, find every place the particle-production law is given
   (the Psi = beta H^4 form and its neighbours, its equations (33)-(38) region) and quote VERBATIM with equation numbers:
   the law, the definition of beta, and any NUMERICAL value, estimate, order of magnitude or bound the paper gives for beta or
   for the quantities beta is built from.
2. Establish the DIMENSIONS and normalisation of beta as the paper uses it, explicitly, and the unit system in force. State what
   would have to be known to convert the paper's beta into the dimensionless units b3_rescue.py integrates in. If the paper
   gives beta only implicitly (e.g. through a particle-production rate per unit volume, a cross-section, or a cutoff), say so
   and give the chain that would be needed.
3. VERDICT, one of exactly these, with your evidence:
   BETA_VALUES=SUPPLIED (with the values and their equation numbers)
   BETA_VALUES=DERIVABLE (with the exact chain and the missing inputs named)
   BETA_VALUES=UNRESOLVABLE_FROM_SOURCE (with what you searched and what is absent)
4. If SUPPLIED or DERIVABLE, convert into the script's units and state where the paper's beta sits relative to the exploratory
   range [0.001, 10] used in B3 — as a comparison, not as a validation of B3.
5. Keep exploratory script units and source physical parameters visibly separate throughout.

## Output: `bounce/B4_BETA_COMPARISON_20260907.md`
Print the file's sha256 and the verdict token as your final answer.
