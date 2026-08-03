# Hwao Deepening Gate 3 Request

Marker: `OVERNIGHT_PAPER_BOARD_HWAO_GATE3_REQUEST_V1`

Do not write memory or configuration.

Read:
- `reviews/lana/LANA_C2_V2_RECEIPT.md`
- V2 `candidate.tex`, rendered PDF text, `COMPILE_NOTE.md`, and `V1_TO_V2_DIFF.md`
- `reviews/hwao/HWAO_C2_REDTEAM_ADJUDICATION.md`

Write under the approved output root only:

1. `reviews/hwao/HWAO_C2_V2_BUILD_ACCEPTANCE.md`
   - Provisional status pending independent checks.
   - Verify V1/source preservation and F1–F4 intent.

2. `packets/C-candidate-build/KUN_C2_V2_CONTRACT_AUDIT_BRIEF.md`
   - Lane: Codex gpt-5.5 using ChatGPT Pro subscription only.
   - Read-only mechanical audit of V2: source/V1/V2 hashes; V1→V2 diff limited to F1–F4 plus header; rendered PDF strings; old overclaim and `reproducible` absent; all five references; citation split; caveats; figure byte identity; compile evidence; V2 receipt concordance.
   - Write only a `kun-c2-v2-audit/` deliverable plus `reviews/kun/KUN_C2_V2_AUDIT_RECEIPT.md`.

3. `publication/GORU_C2_V2_NEW_RUN_MAPPING_BRIEF.md`
   - Lane: Antigravity/Gemini subscription only.
   - Read-only mapping for the safer NEW run id `gated-e2e-demo-c2-v2`; do not overwrite the baseline run.
   - Map exact ABSENT/create paths, source-code route coupling, candidate V2 hashes, preview-manifest field requirements, create-only backup/rollback plan, and HTTP/SHA/visible-label verification plan.
   - Write only `publication/goru-v2-new-run-map/` plus `publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT.md`.
   - No live HTTP, browser, public/current-Lab/source writes.

4. `reviews/hwao/HWAO_DEEPENING_GATE3_DISPATCH_RECEIPT.md`

Return exact marker: `HWAO_C2_V2_AUDIT_BRIEFS_READY`.

Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.
