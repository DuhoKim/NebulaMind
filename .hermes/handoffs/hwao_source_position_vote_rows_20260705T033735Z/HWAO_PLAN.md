# HWAO PLAN — six vote-dependent source-position rows first

From: Hwao/Fable (coordinator) · To: Tori (relay/executor), Lana, Goru · Status: PLAN ISSUED — docs-only; no SQL, no DB, no apply files, no prose/runtime/git/public-cockpit mutation. User hard lock restated: **no SQL until all 36 rows have completed human/source decisions** — completing these six does not unlock SQL.

## 1. The exact six rows (verified against the vote snapshot; all six carry `requires_vote_dependency_decision: true`)

Grouped by paper so each source is read once:

| Queue ID | Evidence | Paper | Human-gold vote (id · value · gist) |
|---|---|---|---|
| `SPQ-2929-28060` | 28060 | SWAN NOEMA M51 (AGN feedback extent) | 5048 · **−1** · "confirm_weakening — row is about positive AGN feedback in general" |
| `SPQ-2929-28091` | 28091 | SWAN NOEMA M51 | 5049 · +1 · confirm |
| `SPQ-2929-28155` | 28155 | SWAN NOEMA M51 | 5053 · +1 · confirm |
| `SPQ-2929-28095` | 28095 | arXiv 2009.11175 (young radio AGN outflows) | 5050 · +1 · confirm |
| `SPQ-2929-28111` | 28111 | arXiv 2009.11175 | 5051 · +1 · confirm |
| `SPQ-2929-28141` | 28141 | arXiv 1706.08987 | 5052 · +1 · confirm |

**Special handling — 28060:** the only −1 vote, and its reason says the row concerns *positive* AGN feedback generally. Its adjudication must honor that human judgment: expected outcome is `limitation_or_caution` role or `retire_reject`/`leave_archival`/`route_kinetic_radio` decision — a plain `support`+`relink` outcome would contradict the human gold vote and requires an explicit written justification in `dependency_handling_action` if proposed.

## 2. Fields to fill per row (from the queue's own `required_source_position_fields` template)

**(a) Source-position block:** `source_accessed_url_or_path`, `source_type`, `section`, `pdf_page`, `figure_or_table` (if any), `paragraph_or_sentence_locator`, `exact_quote_or_paraphrase_source_span` (exact quote strongly preferred), `quote_context_before_after`, `matched_terms`, `source_position_note`, `source_position_verification_status` → `verified` (or `abstract_only_verified`, stated).
**(b) Adjudication block:** `selected_role` (from role_options), `selected_stance_if_visible_successor` and `accepted_target_stance` (from stance_options), `accepted_target_claim_id` / `target_claim_id_if_any` + `target_claim_text_if_any` (successors 2942–2947 only, or none), `accepted_support_role`, `accepted_for_docs_source_position` (pending→accepted/accepted_limited/rejected), `limitation_or_counter_reason` where the role is limitation/challenge.
**(c) Decision block:** `human_decision`, `human_decision_enum` (from `allowed_decision_enums`: relink / copy_source_fill / retire_reject / leave_archival / route_kinetic_radio), `decision_reason` + `decision_reason_plain_english`, `decision_confidence`, `decision_owner`, `human_reviewer`, `human_reviewed_at_utc`, `decision_timestamp_utc`, and — mandatory on all six — `dependency_handling_action` stating in one sentence how the existing human-gold vote was honored.
**(d) Checks:** `anti_duplicate_check_status` resolved against `duplicate_check_against_successor_evidence_ids`; `review_status` → reviewed.
**Untouched, verbatim:** `product_publication_gate` (stays `NO_GO_DB_OR_PRODUCT_PUBLICATION_UNDER_THIS_APPROVAL`), `write_lock`, and every field of the other 30 rows.

## 3. Lane order — yes, Lana and Goru run BEFORE any Tori edit

1. **Lana (semantic, first):** read the three papers (full text where held locally; otherwise authoritative abstract, labeled), fill blocks (a)+(b) and propose block (c) per row — one report + a six-row proposal JSONL in this handoff dir. Vote semantics are binding inputs: 28060 per the special handling above. Standing ask: if my grouping or sequencing looks wrong, attack it in the report.
2. **Goru (mechanical, second):** validate Lana's proposal — all required fields non-null or explicitly n/a, every enum value ∈ its options list, quotes non-empty with locators, target claim IDs ∈ {2942…2947, none}, **vote-consistency check** (no proposed stance contradicts a human vote without a `dependency_handling_action` justification), anti-duplicate statuses resolved. Verdict PASS/BLOCKED_WITH_GAPS; block→recheck pattern applies.
3. **Hwao (gate):** I review both reports and issue the edit go-ahead.
4. **Tori (only then):** apply the six rows' values to the queue artifacts as bounded docs-only edits — all four formats (`json`, `jsonl`, `csv`, `md`) updated consistently — and write a receipts note here. No other rows, no other files.

## 4. Boundaries (exact)

No `psql`; no DB queries or connections; no SQL files; no apply/rollback scripts; no execution phrases minted, rotated, or displayed; docs-only edits confined to the four queue files + reports/receipts in this handoff and the queue dir; no prose/wiki, no runtime, no git, no public cockpit. The user's hard lock governs everything: **SQL exists nowhere until 36/36 rows carry completed decisions**, and even then only via a new operator-approved packet.

## 5. Tori's post-edit validation checklist (all read-only)

1. Re-parse all four queue formats: row count still **36** in each; the six edited rows byte-consistent across json↔jsonl↔csv↔md; the other **30 rows byte-identical** to before (diff against a pre-edit copy).
2. Per edited row: `human_decision_enum ≠ pending`; required fields non-null per §2; enums valid; quote non-empty with locator; `dependency_handling_action` present and mentions the vote id; timestamps are real edit-time UTC.
3. `product_publication_gate` and `write_lock` unchanged on all 36 rows; no SQL-like strings introduced anywhere in the queue files.
4. Recompute/update any per-row `source_payload_hash` the queue maintains, and note old→new hashes in the receipts.
5. Write `TORI_EDIT_RECEIPTS.md` in this handoff dir: files touched, rows touched, validation results, and the standing count "6/36 adjudicated — SQL remains locked."

## 6. Cockpit: unchanged now

No cockpit update from this plan. After the six rows pass Tori's validation, I will direct a single line at the next regular cockpit update: *"2929 source-position queue: 6/36 vote-dependent rows adjudicated (docs-only); 30 remain; SQL locked until 36/36."* Phrase state remains `NO ACTIVE EXECUTION PHRASE` throughout.

HWAO_SOURCE_POSITION_VOTE_ROWS_PLAN_20260705T033735Z
