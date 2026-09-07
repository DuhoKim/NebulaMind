# A1 — REVIEWER IDENTITY AND LINEAGE, stated explicitly (2026-09-07 11:49 KST; Blanc 11:48)
Under Codex-first routing the author/reviewer separation is the thing most at risk, so it is recorded here rather than assumed.

| role | engine | instance | what it did |
|---|---|---|---|
| AUTHOR of A1, the clause disposition and the decision sheet | **codex-cli / gpt-6-astra** | bounded worker pids 12195 (draft) and 62015 (reviewability edit + sheet), dispatched by me with explicit file boundaries | drafted; explicitly told it is an author and may not review or sign off its own work |
| AUTHOR of the trimmed selection path | **codex-cli / gpt-6-astra** | bounded worker pid 22357 (after 17755 STOPPED rather than guess) | wrote `select_sample.py` + 7 tests |
| **INDEPENDENT REVIEWER of A1** | **agy / Gemini** | wrapper pid 13136, dispatched 2026-09-07 11:40:31 KST via `nm_referee_dispatch.sh` (live v1, digest fd3aa3b9…, ACCESS_SHA proof required) | reviewing; **did not author any part of the package** |
| lane owner / coordination | Claude Opus 5 (this session) | — | scope, owner decisions, dispatch, reconciliation |

**Different engine, and no shared authorship**: the reviewer is Gemini, the authors are Codex. No Codex instance reviews Codex output in this round. If routing ever forced one engine to both author and review, the round stops and Blanc is told.

**THE REVIEWER READS THE SOURCE DOCUMENT, NOT A DERIVED EXTRACT** (Blanc 11:48, from Tori's lane this hour: two engines agreeing is not independence when they share an input — hers both read the same extracted equations and both missed the disambiguating prose on the publisher page). The sandbox `/Users/duhokim/.claude/jobs/5b2f0371/tmp/a1_review_huFUfaZh/_stage2_image_analysis_20260901` contains the ACTUAL signed V15 (`OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md`, sha256 fdd9eedd…), the actual run record and the actual selection code — not only `AGREEMENT_RUN_V15_CLAUSE_DISPOSITION_20260907.md`, which is the AUTHOR'S DERIVED EXTRACT of V15. The brief directs the reviewer to check the disposition's DROP rows and a sample of KEEP/DEFER rows **against V15's actual text**, and to read `select_sample.py` itself rather than its description. A finding that rests only on the extract agreeing with the extract is not evidence and is not to be counted as one.

| FINAL INDEPENDENT PASS on the changed bytes | **agy / Gemini** | wrapper pid 38415, dispatched 2026-09-07 14:02 KST | same reviewer as the first pass, still NOT an author of any change; the changes were written by Codex workers |
