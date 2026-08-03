# GORU BRIEF — top-20 source-gap mechanical inventory lane

Context: The user corrected the workflow: Hermes must keep the cockpit/board current while Lana and Goru do the source-gap work. This is NebulaMind paper→claim→evidence→contradiction→trusted prose work, not frontend feature work.

Input packet paths:
- Verification matrix: /Users/duhokim/NebulaMind/NebulaMind/docs/paper_citation_snippet_verification_top20_20260701T141717Z/paper_citation_snippet_verification_top20_20260701T141717Z_verification_matrix.md
- Full citation packet: /Users/duhokim/NebulaMind/NebulaMind/docs/paper_citation_snippet_verification_top20_20260701T141717Z/paper_citation_snippet_verification_top20_20260701T141717Z_citation_snippet_packet.md
- Unit verifications JSONL: /Users/duhokim/NebulaMind/NebulaMind/docs/paper_citation_snippet_verification_top20_20260701T141717Z/paper_citation_snippet_verification_top20_20260701T141717Z_unit_verifications.jsonl
- Source gaps JSONL: /Users/duhokim/NebulaMind/NebulaMind/docs/paper_citation_snippet_verification_top20_20260701T141717Z/paper_citation_snippet_verification_top20_20260701T141717Z_source_gaps.jsonl
- Accepted snippets JSONL: /Users/duhokim/NebulaMind/NebulaMind/docs/paper_citation_snippet_verification_top20_20260701T141717Z/paper_citation_snippet_verification_top20_20260701T141717Z_verified_snippets.jsonl
- Candidate snippet reviews JSONL: /Users/duhokim/NebulaMind/NebulaMind/docs/paper_citation_snippet_verification_top20_20260701T141717Z/paper_citation_snippet_verification_top20_20260701T141717Z_candidate_snippet_reviews.jsonl
- Metadata issues JSONL: /Users/duhokim/NebulaMind/NebulaMind/docs/paper_citation_snippet_verification_top20_20260701T141717Z/paper_citation_snippet_verification_top20_20260701T141717Z_metadata_issues.jsonl

Hard stops for both lanes:
- No DB writes, SQL mutations, migrations, deploy/restart, production config changes, OpenClaw relay, runtime source edits, git commit/push/merge, secrets, or unrelated paths.
- You may read local docs/JSON/JSONL/Markdown and, if your lane has browsing/search capability, use public scholarly sources/arXiv pages only for source identification. Do not use API keys or private credentials.
- Write only your assigned Markdown output file under /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/board-source-gap-fill-20260701T142548Z; do not edit any other file.
- Helper output is advisory; Hermes will independently verify before anything becomes product/DB work.


Lane role: mechanical exact counts, inventories, source maps, and consistency checks.

Task:
1. Parse the JSONL inputs mechanically.
2. Produce exact counts by page_title, unit verification status, docs_gate, product_gate, gap category, and candidate review status.
3. Build a unit-by-unit inventory: unit_id, source_claim_id, exact claim prefix, status, accepted_evidence_ids, source_gap_count, metadata_issue_count, candidate rows reviewed, and first recommended mechanical next action.
4. Identify duplicate/repeated source gaps that can be solved by one source family.
5. List evidence IDs and arXiv IDs involved in metadata/source-text issues.
6. Cross-check that candidate_snippet_reviews row count matches the packet summary, and that every source_gap unit_id exists in unit_verifications.

Write your final report to exactly:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/board-source-gap-fill-20260701T142548Z/goru_source_gap_inventory.md

Required report shape:
- Title and timestamp.
- PASS/BLOCKED status.
- Exact counts table.
- Unit-by-unit table.
- Repeated-gap clusters.
- Metadata issue table.
- Consistency checks with PASS/FAIL.
- Safety statement confirming no DB/deploy/git/runtime/OpenClaw mutation.
- Standalone final line exactly:
GORU_TOP20_SOURCE_GAP_INVENTORY_DONE_20260701T142548Z

Use only local files and read-only shell/file inspection. Do not edit any file except your assigned Markdown output.
