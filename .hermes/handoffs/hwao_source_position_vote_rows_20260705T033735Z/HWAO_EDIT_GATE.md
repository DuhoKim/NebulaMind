# HWAO EDIT GATE — six vote-dependent rows: Tori may apply the docs-only edits

From: Hwao/Fable (coordinator) · To: Tori (executor), cc Lana/Goru · Gate issued after reviewing both lane outputs directly (Lana report + all six JSONL rows field-level; Goru validation 8/8 PASS; my own spot-check of limitation-reason and position-note fields: none missing). Hard locks unchanged: no SQL, no DB, no apply/rollback files, no prose/runtime/git/public-cockpit mutation. The user's standing lock holds: **completing these six does not unlock SQL — 36/36 first.**

## 1. Verdict: **PASS — Tori may apply the six-row docs-only queue edits** from `lana_source_position_proposal.jsonl` as-is.

Why this passes my adversarial bar, briefly: the proposal is *zone-honest* (five of six spans are correctly identified as introduction/background review, not the papers' own findings — flagged `accepted_limited` where that matters, which is exactly the anti-quote-mining discipline the Baseline demands); the one −1 human-gold vote (28060) is honored precisely as my plan required — `limitation_or_caution` + `leave_archival`, never overridden into support, with the positive-feedback content gap recorded; the two kinetic rows are correctly re-routed to successor **2947**, fixing the stale pre-2947 matrix targets; all six `dependency_handling_action` fields name their vote ids; source access is honestly labeled `abstract_only_verified` with full-text pinning deferred rather than faked.

## 2. Changes required relative to Lana's proposal: **NONE substantive.** Two carry-through conditions on the edit itself:

- **C1 — the abstract-only caveat must land in the queue rows** (it is in Lana's JSONL — carry it verbatim): `source_position_verification_status = abstract_only_verified`, position notes stating full-text page/paragraph pinning is pending, and 28141's note that the later full-text pass should prefer the paper's own ALMA anti-correlation sentence over the quoted prior-work review. SQL-time must be able to see these rows are not yet full-text-pinned.
- **C2 — the DB-dedup deferral stays visible:** the anti-duplicate fields record docs-level resolution; the note that 28095/28111 require a DB-level dedup check against 2947's live evidence (26681–26685) at SQL time must ride into the queue rows, not remain only in the report.

## 3. Exact files Tori may edit — these four, nothing else:

1. `docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.json`
2. `…/queue/source_position_human_adjudication_queue.jsonl`
3. `…/queue/source_position_human_adjudication_queue.csv`
4. `…/queue/source_position_human_adjudication_queue.md`

Plus one new receipts file: `.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/TORI_EDIT_RECEIPTS.md`. Only the six rows `SPQ-2929-28060/-28091/-28095/-28111/-28141/-28155` change; `product_publication_gate` and `write_lock` fields stay verbatim on all 36 rows.

## 4. Validation Tori must run (all read-only, results in the receipts file)

0. **Before editing:** verify the pre-edit snapshot manifest still matches the live queue files (hash compare). If anything drifted since 033735Z, stop and re-snapshot before applying.
1. Re-parse all four formats after editing: row count **36** in each; the six edited rows semantically consistent across json↔jsonl↔csv↔md.
2. The other **30 rows byte-identical** to the pre-edit snapshot (diff proof).
3. Per edited row: `human_decision_enum ∈ {leave_archival, relink, route_kinetic_radio}` as proposed (no `pending` remains); all required fields non-null or explicitly n/a; enums valid against each row's own options lists; quote non-empty with section-level locator; `dependency_handling_action` present and naming the vote id; C1/C2 notes present; timestamps are real edit-time UTC.
4. `product_publication_gate = NO_GO…` and `write_lock` unchanged on all 36 rows; no SQL-like strings introduced anywhere in the queue files.
5. Update any per-row `source_payload_hash` and record old→new in the receipts; end the receipts with the standing count line: **"6/36 adjudicated (docs-only) — 30 remain — SQL locked until 36/36."**

## 5. Cockpit

Unchanged during the edits. **After** Tori's validation passes, the single pre-authorized line may ride the next regular Tori-rendered update: *"2929 source-position queue: 6/36 vote-dependent rows adjudicated (docs-only); 30 remain; SQL locked until 36/36."* Phrase state remains `NO ACTIVE EXECUTION PHRASE`. No other cockpit change is authorized by this gate.

— Hwao/Fable. Next coordination step after receipts: I will issue the batching plan for the remaining 30 rows (grouped by source paper, same lane order), unless the user redirects.

HWAO_SOURCE_POSITION_VOTE_ROWS_EDIT_GATE_20260705T033735Z
