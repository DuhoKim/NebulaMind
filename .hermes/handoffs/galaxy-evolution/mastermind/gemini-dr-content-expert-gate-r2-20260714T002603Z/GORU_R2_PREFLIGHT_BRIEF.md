# Goru R2 local-only preflight brief

Packet: `gemini-dr-content-expert-gate-r2-20260714T002603Z`
Status: NOT ARMED

Read the R2 direction, Hwao plan, Hwao correction, and the complete R1 packet. No browser/network, agents, git, DB, product, dashboard, deploy, cron, account, or external action.

Required outputs, only inside the R2 packet:

1. Byte-copy R1 `prompt/GE_COMPARABILITY_CANARY.md` to R2 `prompt/GE_COMPARABILITY_CANARY.md` without retyping or normalization.
2. Write `prompt/GE_COMPARABILITY_CANARY.md.sha256` and `prompt/GE_COMPARABILITY_CANARY.sha256` from the copied bytes.
3. Verify copied hash == R1 prompt hash == pinned hash `4d57fd71b49e74760cc1be1acc6fb50ce1e777b4c43907612830b346b471f42a`.
4. Verify exactly eight numbered comparison rows, required schema fields, forbidden tokens, answer-shape bounds, and that the copied prompt's final non-empty line equals R1's final non-empty line.
5. Verify that final-line marker string occurs exactly once across the entire R2 packet after copy. Do not echo that literal string in the brief, report, checks, filenames, or console output; derive it from the R1 prompt bytes.
6. Recompute and compare the four Gate B source-input hashes and the accepted Gate A capture-script hash from the prior GREEN preflight.
7. Verify R2 marker state: one zero-byte root NOT_ARMED, no ARMED, and exactly one current Goru GREEN/NOT_GREEN marker after decision.
8. Write `preflight/GORU_R2_PREFLIGHT.md` with actual/expected hashes and explicit pass/fail rows, but never echo the in-prompt completion marker. End standalone `GORU_CONTENT_DR_R2_PREFLIGHT_DONE`.
9. If every check passes, create zero-byte `markers/GORU_R2_PREFLIGHT_GREEN_20260714T002603Z`; otherwise create only `markers/GORU_R2_PREFLIGHT_NOT_GREEN_20260714T002603Z` and report blockers.

Do not arm. Do not modify R1.
