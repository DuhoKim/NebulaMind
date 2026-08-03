# LANA BRIEF — top-20 source-gap reasoning lane

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


Lane role: high-reasoning source selection and claim-citation strategy.

Task:
1. Read the verification matrix, source gaps, metadata issues, and accepted snippets.
2. Identify the highest-quality direct source families/papers needed to fill unresolved gaps. Prefer review papers, primary measurement papers, mission/analysis papers, or exact historical sources as appropriate.
3. For each source-gap cluster, state whether the right move is:
   - source fill: find direct citation/snippet;
   - claim rewrite: current wording is too specific for available sources;
   - reject/defer: insufficient direct source in scope.
4. Prioritize the first 8–12 source acquisition targets that would unlock the most top-20 units.
5. Flag metadata/source-text corruption risks, especially evidence 2215.

Write your final report to exactly:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/board-source-gap-fill-20260701T142548Z/lana_source_gap_recommendations.md

Required report shape:
- Title and timestamp.
- PASS/BLOCKED status.
- Top source-gap clusters.
- Prioritized source targets with arXiv/DOI/search-query suggestions and which unit IDs they unlock.
- Claims that should be rewritten rather than source-filled.
- Risks/unknowns.
- Safety statement confirming no DB/deploy/git/runtime/OpenClaw mutation.
- Standalone final line exactly:
LANA_TOP20_SOURCE_GAP_REASONING_DONE_20260701T142548Z

Do not wait for Hermes. Do the lane work and write the report.
