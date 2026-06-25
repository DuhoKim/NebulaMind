# Page-58-Local Neutral Seed Vote Guard Proposal

Timestamp: 2026-06-23T08:08:37Z

## Scope

This redo intentionally does not change shared jury selectors or API behavior. `backend/app/agent_loop/tasks.py` and `backend/app/routers/jury.py` were inspected only and left untouched.

The proposed containment is page-58-local: write neutral auto-seed evidence rows so they are not eligible for the existing jury selectors.

## Proposed Page-58 Seed-Write Spec

For every page-58 sign-suppressed neutral auto-seed:

- `stance = "none"`
- `stance_jury_run_at = now()`
- do not create a `JuryTask`
- `abstract = NULL`
- `intro_excerpt = NULL`
- keep trust-bearing confirmed contradiction writes, if later human-approved, as `stance = "challenges"` rather than `contradicts`

The no-text fields are load-bearing. `stance_jury_run_at = now()` blocks the normal first-pass enqueue paths, but `abstract = NULL` and `intro_excerpt = NULL` close the length predicates if a later retry path is reached.

## Per-Path Analysis

| Path | Current selection / write predicate | Page-58 local seed result |
| --- | --- | --- |
| `schedule_stance_jury(claim_id)` | Same `claim_id`; `Evidence.stance_jury_run_at IS NULL`; `Evidence.abstract IS NOT NULL`; not held; then enqueues `run_stance_jury_for_evidence`. | Skipped. `stance_jury_run_at = now()` fails the main predicate. `abstract = NULL` also fails the abstract predicate if `run_at` is ever accidentally omitted. |
| `run_stance_jury_for_evidence(evidence_id)` | Direct task loads evidence; returns only if missing or `stance_jury_run_at IS NOT NULL`; otherwise checks text length and can write `EvidenceVote`. | Skipped when called normally because `stance_jury_run_at = now()`. If manually forced after clearing `run_at`, `abstract = NULL` and `intro_excerpt = NULL` hit the insufficient-text branch, mark run-at, and write no vote. |
| `drain_stance_jury_backlog()` | `stance_jury_run_at IS NULL`; `length(abstract) >= STANCE_JURY_MIN_ABSTRACT_CHARS OR length(intro_excerpt) >= INTRO_EXCERPT_MIN_CHARS`; not held; then enqueues 4-model jury. | Skipped by `stance_jury_run_at = now()`. Also skipped by NULL text fields. |
| `drain_jury_fast_pass()` priority 1 | `stance_jury_run_at IS NULL`; `length(abstract) >= 100 OR length(intro_excerpt) >= INTRO_EXCERPT_MIN_CHARS`; claim trust in `accepted/consensus`; `count(EvidenceVote.id) = 0`. | Skipped by `stance_jury_run_at = now()`. Also skipped by NULL text fields. |
| `drain_jury_fast_pass()` priority 2 | `stance_jury_run_at IS NOT NULL`; `stance_jury_run_at < low_vote_retry_cutoff`; text length predicate; claim trust in `accepted/debated`; `vote_count > 0`; `vote_count < 3`. | `run_at = now()` alone only defers. A fresh neutral row with zero votes still does not qualify later because `vote_count > 0` fails. If some outside path adds 1-2 votes, populated text would make it eligible after the cutoff. Setting `abstract = NULL` and `intro_excerpt = NULL` fully closes the p2 selector for the seed row. |
| `run_stance_jury_single(evidence_id)` | Direct task loads evidence; returns if missing or `stance_jury_run_at IS NOT NULL`; otherwise checks text length and can write one `EvidenceVote`. | Skipped when called normally because `stance_jury_run_at = now()`. If manually forced after clearing `run_at`, NULL text fields hit the insufficient-text branch and write no vote. |
| `_maybe_create_jury_task(db, evidence_id, claim_id, page_id)` | If no existing `JuryTask`, creates one unconditionally for the evidence id. | Closed only by page-58 writer behavior: do not call this helper and do not insert a `JuryTask` for neutral seeds. |
| `/api/jury/tasks` | Lists open `JuryTask` rows, optionally filtered by assignment/category/agent affinity; then exposes evidence and creates `JuryAssignment` for authenticated agents. | Skipped because no `JuryTask` exists. |
| `/api/jury/tasks/{task_id}/vote` | Requires a valid open `JuryTask`; writes `EvidenceVote` for that task's evidence. | Skipped because no task id exists for the neutral seed. |
| `dispatch_jury_webhooks()` | Selects open `JuryTask` rows and delivers them to active webhook agents. | Skipped because no `JuryTask` exists. |
| `settle_evidence_and_update_rep()` | Does not create votes. It settles evidence with `stance_jury_run_at < cutoff`, no consensus fields, and enough existing votes. | No effect if the seed has zero votes. It cannot create the first vote. |
| `sweep_council_tiers()` | Does not create votes. It evaluates settled/recent evidence votes for escalation triggers. | No effect if the seed has zero votes. |
| Citation-context miners (`citation_context/miner.py`, `citation_context/dynamic_miner.py`) | They create new supportive evidence rows and immediately write their own positive `EvidenceVote`; they do not select an existing neutral seed row for voting. | Not a selector for the page-58 seed row. No page-58-local guard needed for this row. |
| Direct `/api/evidence/{evidence_id}/vote` | Historical state: loaded evidence by id and wrote `EvidenceVote` directly. As of `a0909a2`, this legacy route is deprecated/no-write and points callers to `/api/jury/tasks/{task_id}/vote`. | Historical residual manual/API path; now closed for writes by the shared endpoint freeze. |

## Decision Point

A page-58-local seed-writing approach can close all automatic jury selection paths without changing shared selectors, if and only if the seed writer uses the full spec above, especially `abstract = NULL` and `intro_excerpt = NULL`.

Historical residual: direct `/api/evidence/{evidence_id}/vote` could not be closed by seed-writing alone. It is now closed for writes by the shared endpoint freeze in `a0909a2`; replacement trust mutation is `/api/jury/tasks/{task_id}/vote`.

## Page-58-Local Code Adjustment

`backend/scripts/page58_sign_suppressed_gate_score.py` was adjusted so the dry-run seed plan now records:

- `abstract_for_write = null`
- `intro_excerpt_for_write = null`
- existing page-58-local fields: `evidence_stance_for_write = "none"`, `stance_jury_run_at_for_write = "now()"`, `create_jury_task = false`

No shared jury production file was changed.

## Verification

Commands run:

```bash
backend/.venv/bin/python -m py_compile backend/scripts/page58_sign_suppressed_gate_score.py
```

Inspection results:

- `backend/app/agent_loop/tasks.py`: inspected only; unchanged.
- `backend/app/routers/jury.py`: inspected only; unchanged.
- Page-58 seed-plan script compiles.

## Containment

- NM HEAD: `4ba9675`
- `db_write_count`: 0
- Shared jury selector/API edits: no
- Live page-57/page-58 write: no
- Deploy/restart: no
- Alembic/migration: no
- Paid lane touched: false
- Files touched in this redo:
  - `backend/scripts/page58_sign_suppressed_gate_score.py`
  - `docs/page58_slice2b_stance_gold_rebalance_20260623T043618Z/page58_local_neutral_seed_guard_proposal_20260623T080837Z.md`
