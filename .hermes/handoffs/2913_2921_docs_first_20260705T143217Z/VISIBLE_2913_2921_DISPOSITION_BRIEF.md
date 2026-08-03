# 2913/2921 docs-first disposition board — visible lane brief

Task ID: `2913_2921_DOCS_FIRST_DISPOSITION_20260705T143217Z`

User steer:
- Move to 2913/2921 dispositions next.
- Docs-first.
- No SQL/apply until a future exact packet.
- Full-text pinning is the alternate if dispositions are not ready.
- Leverage all available resources, including Gemini web/app usage, but keep safety locks.

Current public state:
- Marker: `GALAXY_2913_2921_DOCS_FIRST_DISPOSITION_RUNNING_20260705T143217Z`
- Public phrase: `NO ACTIVE EXECUTION PHRASE`

Hard locks for this lane:
- No DB writes.
- No SQL/apply/rollback files.
- No trust recompute.
- No prose/wiki/page_versions publish.
- No deploy/restart.
- No git commit/push/merge.
- No rollback.
- Any future DB/prose/git/rollback action needs a fresh explicit packet/approval.

Important discovered state:
- The earlier 2913/2921 board decision was accepted on 2026-07-04.
- A separate exact write packet `galaxy_2913_2921_exact_write_preflight_20260704T134546Z` was later executed and verified on 2026-07-04.
- Fresh read-only current-state snapshot for this lane confirms the executed disposition still holds:
  - claim 2948 exists.
  - claim 2913 is `parent_replaced`.
  - claim 2921 is `parent_replaced`.
  - evidence 26678 -> claim 2948.
  - evidence 26679 -> claim 2948.
  - evidence 26694 -> claim 2546.
  - dependency rows for target evidence: 0.
- Snapshot files:
  - `.hermes/handoffs/2913_2921_docs_first_20260705T143217Z/CURRENT_STATE_READONLY_SNAPSHOT.md`
  - `.hermes/handoffs/2913_2921_docs_first_20260705T143217Z/CURRENT_STATE_READONLY_SNAPSHOT.json`

Source/full-text artifacts available from old decision packet:
- `docs/galaxy_2913_2921_readonly_decision_packet_20260704T131018Z/source_text/2605.31052v1_pdf_text.txt`
- `docs/galaxy_2913_2921_readonly_decision_packet_20260704T131018Z/source_text/2210.03747v2_pdf_text.txt`
- `docs/galaxy_2913_2921_readonly_decision_packet_20260704T131018Z/source_text/1308.5224v1_pdf_text.txt`
- targeted snippets JSON files for all three.

Lane asks:
- Hwao/Fable: coordinate verdict. Are 2913/2921 dispositions already complete, making the next safe work full-text pinning/read-only source-hardening? Or is there a docs-only disposition gap remaining?
- Lana: science/source-position verdict. Are the 2913/2921 disposition outcomes still epistemically sound from the read-only artifacts? Identify any full-text pinning gaps.
- Goru: mechanical validation. Confirm no SQL/apply artifacts are created in this new lane, current-state checks match the prior executed state, and public phrase/cockpit locks remain correct.
- Kun: reproducibility/checker. Verify the current snapshot can be reproduced from local artifacts/read-only state and outline a no-SQL checker shape for full-text pinning.

Return concise verdicts with this marker:
`2913_2921_DOCS_FIRST_LANE_VERDICT_20260705T143217Z`
