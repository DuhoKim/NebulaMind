# G3 Backend research-runner — REVIVE (product decision) — USER APPROVAL RELAY (not a crew receipt)

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 · per-unit disposition (the split-unit product decision)
Relayed by: Claude Code (Lab session) on Duho's explicit instruction (Universal Control unreliable). Records a
user decision line for Hwao/Tori; NOT a Hwao ratification; executes nothing (no source/test edit, no git/index/
worktree mutation). One file written (this relay).

## User decision line (verbatim, relayed)
`REVIVE G3 BACKEND-RUNNER 20260722` — given by Duho 2026-07-22 (~14:12 KST), answering the split-unit product
gate in BRANCH_FATE_DECISION.md #3(a) ("backend runner+worker = separate product decision — revive as its own
backend unit only if an autonomous runner is still wanted") and Phase 5 #8.

## Decision + rationale
- **The autonomous research runner IS still wanted → REVIVE it as its own backend unit** (reworked onto fresh main).
- Rationale (operational): the runner is the only piece genuinely absent from main and it is the backend behind
  the Lab's `/api/lab/runs`. `/api/lab/runs` currently returns 200 live ONLY because the FastAPI backend is
  running off the un-merged `feat` branch (Kun's divergence finding). If the branch is retired without reviving
  the runner, the Draft board's "Pipeline runs" feature loses its backend. Reviving onto main makes it durable.

## Unit scope (backend-only; frontend configurator stays ABANDONED per branch-fate #3(b)/#4-6)
- `backend/app/routers/lab_runner.py` (168 lines), the `backend/app/main.py` router wiring (+2), and
  `tools/lab_runner_worker.py` (362 lines) + its dirty-tree extension (`M tools/lab_runner_worker.py`, +85).
- Consumer on main = the Draft board "Pipeline runs" section (a NEW UI that reaches `/api/lab/runs`); the old
  LabConfigurator/RecentRuns UI stays abandoned.

## What this authorizes / does NOT
- Authorizes the crew to PREPARE a G3 backend-runner rework packet (fresh recount, disjoint scope, RED-first,
  disposable worktree), same discipline as the Surveys unit.
- Does NOT authorize execution yet: the rework EXECUTION needs its own explicit user activation line (same as
  Surveys). Committing/PR-ing onto main is a further separate G3 packet. No git authority granted; G3 stays Held.

## State at relay (read-only)
- Primary `feat/surveys-atlas-ia-p1-20260627` @ `826e733`; 20 modified / 360 untracked. ✅ unchanged.

## Next step (crew)
Hwao: record runner fate = REWORK/REVIVE (backend-only); prepare the G3 backend-runner approval packet and
present its activation gate. Nothing here bypasses ratification or grants git authority.
