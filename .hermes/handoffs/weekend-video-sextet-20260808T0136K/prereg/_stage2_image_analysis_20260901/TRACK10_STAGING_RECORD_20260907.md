# TRACK 10 — ONE RESOLVER FOR THE WHOLE PRECEDENCE PATTERN (NOT GATED, NOT ADOPTED) — 2026-09-07 03:39 KST

Under Blanc's order of 03:20 KST (`BLANC_ORDER_PRECEDENCE_IS_ONE_PATTERN.md`): V27-1, V27-2, V28-1/2, V29-1 and V29-2 are one pattern — a check returning before the rule that governs it — so track 10 is not a sixth point fix. Nothing Duho has approved is touched (the signed V15 and the installed Tier-C V39 are unchanged; everything here is a staged successor). Successor files only: provenance_designs_v10, run_configurations_v14, beacon_record_drand_v30, build_corpus_identity_v30 (+ tests v14/v30/v30), track10/test_track10_fail_first.py (4 tests), track10/test_track10_text_v30.py, track10/exhibit_precedence_pairs.py, track1/coherent_attacks_v30.py. Candidate text `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V30_20260907.md` (SHA-256 98881c7ecba0ac3bb718983f8534aaa55d325efeb4314d72b31b64b95af2abb9; diff `V29_TO_V30.diff`).

| Blanc's item | done | evidence |
|---|---|---|
| 1. state the precedence order once | `provenance_designs_v10.PRECEDENCE` = LOCAL-TERMINAL > FORGED > NOT-EARLIEST > EXPIRED > DERIVED-TERMINAL > RETRY-UNAVAILABLE > RETRY-INCOMPLETE > ACCEPT, with each class defined in the v10 header and in §3c of the V30 text (the same words in both) | v10 header; V30 §3c |
| 2. one place enforces it | `provenance_designs_v10.resolve`; driver v14's `composed_resolver` runs four CONTRIBUTING stages (A local sweep of both retained events; B one retrieval — approval authentication and the open event's same-id check; C seed re-derivation; D history continuation) and none decides; the v13 stage-by-stage `composed_provenance` is removed; class-0 findings raised in the fixed offline sequence are consistent with the order because nothing outranks class 0; within a class the fixed stage sequence decides | driver v14; `I['_findings']` records every finding |
| 3. exhibit pairwise | `V30_PRECEDENCE_EXHIBIT_20260907.md`: 21 class pairs, both derivation orders, same winner, always the higher class; plus the complete-path pairs of tracks 8–10 listed with their executed outcomes | exhibit file; `test_track10_fail_first.Resolver` |
| 4. keep every existing precedence test; add the resolver's own | tracks 8 and 9 (8 tests) re-run against v10/v14 — OK; the resolver's pairwise test added (fail-first: no resolver in the V29 copy) | receipt run 2b / run 1b |

| codex V29 | answer (staged) | evidence |
|---|---|---|
| V29-1 [MAJOR] seed re-derivation retry before approval precedence | stage C contributes REDERIVE-RETRY as RETRY-UNAVAILABLE; stages A/B's LOCAL-TERMINAL / FORGED findings outrank it | receipt run 2, rows 1–3 |
| V29-2 [MAJOR] remote-head / approval-feed retries before local open-event mismatches | stage A sweeps the open event (type / pinned repository / protected ref) before any retrieval or remote call; stage B checks its same-id contradictions on the one retrieval; stage D's RETRY-REMOTE-UNAVAILABLE is outranked | receipt run 2, rows 4–7 |
| V29-3 [MINOR] labels / literal backreferences | the four digests written out (the V28/V29 edit scripts had used regex backreference syntax in a plain replacement — present since V28); labels name the executed modules; the V30 edit builds those clauses with a function and the text test asserts no such token remains | `V29_3_Text` |
| V29-4 [MINOR] equal-time edge | NOT-EARLIEST only on a STRICTLY earlier qualifying event; codex's clause verbatim | `V29_4_StrictEarlier` |

Inspection: `coherent_attacks_v30.py` — every row's verdict equals V29's (35 rows). Aggregate: 141 tests / 24 suites OK, warning-strict. Nothing gated, adopted, signed, frozen, sealed or drawn. Next: the V30 complete-package review, both seats, fresh sandbox.
