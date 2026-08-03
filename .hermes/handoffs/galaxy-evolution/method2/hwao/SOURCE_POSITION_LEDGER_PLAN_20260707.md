# Method2 / SFA — S1 source-position ledger plan (Hwao coordinator)

Marker: OVERNIGHT_AUTONOMOUS_GO_20260706T155128Z
Method packet marker: GALAXY_EVOLUTION_METHOD2_ULTRA_FORMAT_ROLE_SPLIT_20260707
Related: METHOD2_SAME_FORMAT_ROLE_TABLE_PACKET_20260707 (hwao/), GALAXY_EVOLUTION_METHOD2_P1_SOURCE_POSITION_LEDGER_20260706T142132Z (p1/)
Role: Hwao-m2, coordinator/planner. S1 deliverable per overnight GO sequence step 1.

## S1 status: COMPLETE

A full P1 source-position ledger already exists in this handoff root (marker 20260706T142132Z, decision timestamps 2026-07-05, human gold votes incorporated, approval phrase consumed: `APPROVE METHOD2 P1 DOCS-ONLY SOURCE-POSITION LEDGER`). S1 therefore does NOT re-derive the ledger. S1 adopts the existing P1 artifacts as the method's raw material and defines the skeleton, target-paper list, and role-table sequencing needed to ratify it under the quintet protocol. The P2/P3 artifacts in this root also predate the role-table correction and are OUT OF SCOPE tonight; they may not be treated as team-verified until a later Hwao-sequenced packet ratifies them after S2.

## Ledger skeleton (adopted from P1, to be verified by Kun in S4)

Canonical ledger: `p1/P1_SOURCE_POSITION_LEDGER_20260706T142132Z.jsonl` (36 rows; accepted/rejected splits in sibling JSONL files; counts in `P1_SOURCE_POSITION_LEDGER_SUMMARY_20260706T142132Z.json`).

Observed row fields (from packet tables + first-row inspection; truncated view — S4 verifies the full schema):
- `evidence_id`, `marker`, `method`, `approval_phrase_consumed`, `paper{arxiv ids, title}`
- `adjudication{accepted_support_role, accepted_target_claim_id/text/stance, anti_duplicate_check_status, decision_confidence, decision_owner, decision_reason, decision_reason_plain_english, decision_timestamp_utc, dependency_handling_action, duplicate_check_against_successor_evidence_ids, human_decision_enum, limitation_or_counter_reason, review_status}`
- Status vocabulary: `accepted` | `accepted_limited` | `rejected`; role vocabulary: `support` | `limitation_or_caution` | `background_only`; public-sentence-use vocabulary: `MAY_SUPPORT_PUBLIC_WIKI_SENTENCE_AFTER_LATER_CLAIM_STATUS_AND_PROSE_GATE` | `MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE[_ABSTRACT_ONLY_CAP]` | `LIMITED_CAUTION_ONLY_NO_CURRENT_TARGET_CLAIM_SUPPORT` | `MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE`.
- Verification statuses: abstract_only_verified 28, docs_verified 7, source_record_verified 1.
- Read-only upstream input: `docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.jsonl`.

## Target-paper list (13 source groups, 36 rows)

| # | source group | rows | accepted/limited | rejected | target claims |
|---|---|---|---|---|---|
| 1 | arxiv:0901.1880 | 3 | 28075, 28131 | 28110 | 2945, 2947 |
| 2 | arxiv:1203.2926 | 2 | — | 28114, 28118 | — |
| 3 | arxiv:1507.06366 | 1 | — | 28082 | — |
| 4 | arxiv:1706.08987 | 1 | 28141 (accepted) | — | 2943 |
| 5 | arxiv:2009.11175 | 5 | 28087, 28095 (accepted), 28108, 28111, 28133 | — | 2942, 2943, 2947 |
| 6 | arxiv:2111.01801 | 1 | 28140 | — | 2943 |
| 7 | arxiv:2403.17145 | 6 | 28123, 28151, 28158 | 28127, 28139, 28143 | 2942, 2946 |
| 8 | arxiv:2508.06707 | 3 | 28062, 28089, 28144 | — | 2943, 2946, 2947 |
| 9 | arxiv:2512.05584 | 4 | 28066, 28069, 28073 | 28070 | 2944, 2945 |
| 10 | arxiv:2512.21927 (Perseus superbubble) | 4 | — | 28076, 28080, 28083, 28084 | — |
| 11 | arxiv:2604.15438 (SWAN IV, M51) | 4 | 28060, 28074, 28091, 28155 | — | 2942, 2943 |
| 12 | arxiv:2604.22922 (UFOs >0.3c) | 1 | 28148 | — | 2943 |
| 13 | arxiv:2605.03008 (env. quenching JWST) | 1 | 28088 | — | 2944 |

Claim targets in play: 2942 (AGN feedback scoped, not universal), 2943 (AGN outflows remove/suppress star-forming gas), 2944 (stellar-feedback alternatives/qualifiers), 2945 (gas-removal/recycling cautions), 2946 (maintenance/preventive heating, model-dependent), 2947 (kinetic/radio-mode jets).

## Public-sentence support criteria (method rule applied)

1. Only `accepted` or `accepted_limited` rows may ever support a public wiki sentence, and only after the later claim-status and prose gates.
2. Rows with `ABSTRACT_ONLY_CAP` support only qualified/limited sentences; no full-text-strength wording.
3. `limitation_or_caution` rows must travel with their target claim wherever it is used in prose.
4. `rejected` and no-target rows are preserved as blockers/archival; they must never be silently upgraded.
5. Any status/role/use inconsistency found in S2 is recorded as a docs-only erratum for the next Hwao packet — the P1 files themselves are not mutated.

## Sequencing (tonight, per overnight GO)

- S2 — Lana-m2 (gated on this file existing — gate now open): ratify or flag each of the 36 P1 adjudications with science-caution review. Scrutinize: status/role/use internal consistency; single-source stacking per claim; abstract-only caps; review-paper vs primary-detection weighting; sign errors (positive vs negative feedback). Deliver `lana/LANA_SFA_SOURCE_ADJUDICATION_20260707.md`. May name at most one exact Ultra-worthy contested question or `ULTRA_NOT_NEEDED`.
- S3 — Goru-m2: mechanical recount of ledger vs summary (36/2/22/12/13; claim-id histogram 2942:4, 2943:6, 2944:3, 2945:2, 2946:3, 2947:5, None:13; human decisions 14/17/5; verification 28/7/1). Deliver `goru/GORU_SFA_FORMAT_COUNTS_20260707.md`.
- S4 — Kun-m2 (after S1–S3): rebuild check — can the ledger be regenerated from the read-only queue input + human votes without hidden state; verify full row schema. Deliver `kun/KUN_SFA_REBUILD_CHECK_20260707.md`.
- S5 — Tori-m2 (last): receipts verification. Deliver `receipts/TORI_SFA_S5_RECEIPT_20260707.md`.
- NOT tonight: same-format Markdown draft conversion (needs S2 acceptance + a later Hwao packet); P2/P3 ratification; any claims/prose authorization.

## Ultra doctrine

ULTRA_NOT_NEEDED for S1. No Ultra/Gemini/Antigravity invocation tonight by any Method2 lane; S2 may only name a future contested question.

## Safety ledger

Zero DB/SQL/live wiki/page_versions/deploy/restart/git/cloud/API/GCP/billing/account/payment/credits/OAuth/browser/Ultra actions. Writes confined to the Method2 handoff root.
