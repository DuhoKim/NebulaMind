# HWAO_R2_PREFLIGHT_CORRECTION — marker-string uniqueness restored

Defect (caught before Goru preflight): `HWAO_R2_ONE_CANARY_PLAN.md` §2 quoted the literal in-prompt completion-marker string while §6 requires marker-string uniqueness across the R2 packet — the marker must occur only in the frozen prompt file so the capture/validation checks can treat any other occurrence as contamination.

Correction applied (the only change): the literal string is removed from the plan; §2 now refers to the marker indirectly as the R1 frozen prompt's final non-empty line, pinned by the prompt SHA-256 (`4d57fd71b49e74760cc1be1acc6fb50ce1e777b4c43907612830b346b471f42a`), with V1 unchanged in meaning. This correction note likewise avoids quoting the string. The prompt file, its hash, and every other contract clause are untouched. Within the R2 packet the marker string now exists solely in `prompt/GE_COMPARABILITY_CANARY.md` (once Goru byte-copies it), satisfying the §6 lint.

Next step: Goru runs the R2 preflight (byte-copy hash chain, eight-row check, marker-uniqueness lint, checklist freeze). Packet remains NOT ARMED.

HWAO_CONTENT_DR_R2_MARKER_UNIQUENESS_CORRECTED
