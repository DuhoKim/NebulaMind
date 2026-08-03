# LANA review brief — remaining-20 draft proposal

Role: Lana = judgment/methods reviewer. Hwao coordinates; Tori drafted row decisions only to give the board something concrete to review.

Task: Review Tori's 20-row docs-only draft proposal for semantic/source-position safety. Do not rewrite the whole queue. Return PASS if the draft is safe for Hwao to gate, or ISSUES with exact row fixes.

Hard locks: no DB, no SQL/apply/rollback, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git commit/push/merge, no cron/cloud/account/secret changes. Gemini web quota held.

Review for:
- same-source stacking and duplicates;
- non-AGN stellar/local rows not inflating AGN claims;
- kinetic/radio rows routed to 2947 only when appropriate;
- source verification not overclaiming full PDF pinning;
- all visible successor rows capped accepted_limited unless clearly stronger;
- whether any row must stay pending for a supervised Gemini second opinion.

Output concise Markdown:
- Verdict: PASS or ISSUES.
- If ISSUES, list exact evidence_id and replacement decision.
- If PASS, state any caveats Hwao must preserve.
- End with marker LANA_REMAINING20_REVIEW_20260705T085714Z.
