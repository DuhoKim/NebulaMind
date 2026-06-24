# Neutral Seed Vote Guard Implementation

Timestamp: 2026-06-23T07:44:30Z

## Scope

Implemented the guarded neutral auto-seed configuration for page-58 prep. This is code and report only. No live page write, service restart, deploy, alembic, DB migration, or stance lock was run.

## Code Changes

- `backend/scripts/page58_sign_suppressed_gate_score.py`
  - Page-58 sign-suppressed seed plan now explicitly marks auto-seeds as:
    - `evidence_stance_for_write = "none"`
    - `stance_jury_run_at_for_write = "now()"`
    - `create_jury_task = false`
- `backend/app/agent_loop/tasks.py`
  - Added shared neutral exclusion tuple: `("none", "neutral", "related_different_facet")`.
  - `schedule_stance_jury` excludes neutral stances.
  - `drain_stance_jury_backlog` excludes neutral stances.
  - `drain_jury_fast_pass` priority 1 excludes neutral stances.
  - `drain_jury_fast_pass` priority 2 excludes neutral stances, covering the low-vote retry path that does not rely on `stance_jury_run_at IS NULL`.
  - `run_stance_jury_for_evidence` short-circuits neutral evidence before any model call or vote write, marks `stance_jury_run_at`, and releases inflight state.
  - `run_stance_jury_single` short-circuits neutral evidence before any model call or vote write, marks `stance_jury_run_at`, and releases inflight state.
  - `_maybe_create_jury_task` returns without creating a task for neutral evidence.
- `backend/app/routers/jury.py`
  - `/api/jury/tasks` skips stale open tasks whose evidence stance is neutral.
  - `/api/jury/tasks/{task_id}/vote` rejects direct votes against neutral evidence with HTTP 409.

## Verification

Commands run:

```bash
backend/.venv/bin/python -m py_compile backend/app/agent_loop/tasks.py backend/app/routers/jury.py backend/scripts/page58_sign_suppressed_gate_score.py
```

Static guard audit:

- PASS: `schedule_stance_jury` excludes neutral stances.
- PASS: `_maybe_create_jury_task` skips neutral evidence.
- PASS: `run_stance_jury_for_evidence` has neutral short-circuit before model/vote writes.
- PASS: `run_stance_jury_single` has neutral short-circuit before model/vote writes.
- PASS: `drain_stance_jury_backlog`, fast-pass priority 1, and fast-pass priority 2 all include neutral exclusions.
- PASS: `/api/jury/tasks` hides neutral evidence tasks before assignment creation.
- PASS: `/api/jury/tasks/{task_id}/vote` rejects neutral evidence.
- PASS: page-58 seed plan writes `stance="none"`, `stance_jury_run_at=now()`, and no `JuryTask`.

Neutral seeded row selection result:

- `stance="none"`: excluded by all named auto-vote selectors and direct runners.
- `stance="neutral"`: excluded by all named auto-vote selectors and direct runners.
- `stance="related_different_facet"`: excluded by all named auto-vote selectors and direct runners.

Regression check:

- The exclusion tuple only removes `none`, `neutral`, and `related_different_facet`.
- Existing trust-bearing stances such as `supports` and `challenges` remain eligible for the normal jury paths.
- Confirmed contradiction write stance remains `challenges`, not `contradicts`.

## Containment

- NM HEAD: `4ba9675`
- `db_write_count`: 0
- Live page write: no
- Page-57/58 write: no
- Alembic/migration: no
- Service restart/deploy: no
- Paid lane touched: false
- Tau/gold changes: no
