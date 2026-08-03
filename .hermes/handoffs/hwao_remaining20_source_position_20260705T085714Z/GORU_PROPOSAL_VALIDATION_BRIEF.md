# GORU remaining-20 proposal validation brief

Task: mechanically validate the corrected 20-row docs-only proposal. Do not edit files.

Inputs:
- Hwao plan: HWAO_REMAINING20_PLAN_20260705T085714Z.md
- Corrected proposal: TORI_CORRECTED_REMAINING20_PROPOSAL.md and tori_corrected_remaining20_proposal.jsonl
- Lana review + fix recheck: LANA_REMAINING20_REVIEW.md, LANA_REMAINING20_FIX_RECHECK.md

Validate:
- exactly 20 rows, all pending IDs once, grouped B4=8 B5=5 B6=2 B7=3 B8=2;
- every decision enum is in allowed set;
- every accepted/relinked visible row is accepted_limited and non-pending;
- archival/rejected rows do not set target claim IDs;
- product_publication_gate and write_lock are exact no-go strings;
- Gemini web quota not used;
- no SQL/DB/prose/runtime/git/cron/cloud/account/secret action is implied.

Return concise PASS/BLOCKED with count table and marker GORU_REMAINING20_PROPOSAL_VALIDATION_20260705T085714Z.
