# G3 Backend-runner rework — GO-AHEAD (proceed to completion) — USER APPROVAL RELAY (not a crew receipt)

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 · backend-runner unit · execution authorization
Relayed by: Claude Code (Lab session) on Duho's explicit instruction ("okay then let her go ahead"), Universal
Control to the crew session being unreliable. Records a user authorization line for Hwao/Tori; NOT a Hwao
ratification; executes nothing itself. One file written (this relay). Follows BACKEND_RUNNER_REVIVE_USER_APPROVAL_RELAY_20260722.md.

## User line (relayed)
`GO AHEAD G3 BACKEND-RUNNER REWORK — RUN TO COMPLETION 20260722` — Duho, 2026-07-22 (~14:2x KST).

## What this authorizes
- Tori proceeds with the backend-runner REVIVE rework END-TO-END under standing lane discipline, WITHOUT a
  separate per-round user line at each review-fix round (the per-round pause is waived for this unit):
  Hwao prepares the packet → Tori reworks RED-first in a fresh disposable worktree off cached `origin/main`
  → the fail-closed review rounds run to a PASS → wrap-up. Hwao still ratifies each structural gate.
- Scope: backend-only — `backend/app/routers/lab_runner.py`, the `backend/app/main.py` router wiring, and
  `tools/lab_runner_worker.py` (+ its dirty +85 extension). Frontend configurator stays ABANDONED. Consumer on
  main = the Draft board "Pipeline runs" section.

## What this does NOT authorize (unchanged, still gated)
- The fail-closed reviews STILL stop on any security/logic/scope finding, and the run STILL halts on custody/pin
  drift or a phantom-stage claim — "run to completion" waives the per-round USER approval, not the safety stops.
- NO commit/PR/push/merge onto main: landing V2 (or the runner) on main remains a SEPARATE future G3 packet with
  its own fresh recount + approval. G3 stays Held for all git-to-main actions.
- Nothing here touches the primary checkout, deletes/moves anything (G4 held), or grants worktree removal.

## State at relay (read-only)
- Primary `feat/surveys-atlas-ia-p1-20260627` @ `826e733`; 20 modified / 360 untracked. ✅ unchanged.

## Next step (crew)
Hwao: record REVIVE (if not yet) → prepare + ratify the backend-runner packet → let Tori run the rework to a
PASS and wrap up, no per-round user pause. Report at PASS/wrap-up. Commit-to-main stays a separate later gate.
