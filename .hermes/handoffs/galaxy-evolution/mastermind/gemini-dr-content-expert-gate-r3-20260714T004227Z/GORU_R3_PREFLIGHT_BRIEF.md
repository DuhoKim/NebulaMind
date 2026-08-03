# Goru R3 local-only preflight brief

Packet: `gemini-dr-content-expert-gate-r3-20260714T004227Z`
Status: NOT ARMED

Read the R3 direction/plan and the complete R2 custody chain. No browser/network or external action.

Required outputs only inside R3:

1. Byte-copy R2 `prompt/GE_COMPARABILITY_CANARY.md` and both hash files into R3 `prompt/`; verify R1 bytes == R2 bytes == R3 bytes and SHA-256 == pin `4d57fd71b49e74760cc1be1acc6fb50ce1e777b4c43907612830b346b471f42a`.
2. Verify exactly eight numbered rows, required prompt schema/vocabulary/forbidden-token discipline, and R3 prompt final non-empty line equals R2's.
3. Verify that final-line marker string occurs exactly once across the R3 packet. Never echo the literal marker outside the prompt.
4. Recompute and match the four Gate B source hashes and accepted Gate A capture-script hash from R2.
5. Verify one zero-byte root NOT_ARMED, no ARMED, and exactly one current Goru R3 GREEN/NOT_GREEN marker after decision.
6. Write `preflight/GORU_R3_PREFLIGHT.md` with actual/expected hashes and explicit pass/fail rows, avoiding the literal in-prompt marker; end standalone `GORU_CONTENT_DR_R3_PREFLIGHT_DONE`.
7. If all pass, create zero-byte `markers/GORU_R3_PREFLIGHT_GREEN_20260714T004227Z`; otherwise only `markers/GORU_R3_PREFLIGHT_NOT_GREEN_20260714T004227Z`.

Use an explicit `cd` to the absolute R3 packet path before any relative file operation. Do not arm or modify R1/R2.
