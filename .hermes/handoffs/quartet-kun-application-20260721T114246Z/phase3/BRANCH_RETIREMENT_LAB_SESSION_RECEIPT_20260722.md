# feat branch retirement — executed by the Lab session

Run: quartet-kun-application-20260721T114246Z · step 2 (branch fate: retire)
By: Claude Code (Lab session) on Duho's explicit authorization ("proceed with the retirement").
Date: 2026-07-22 ~21:45 KST.

## What was done
- Preserved the branch's uncommitted parallel-track work first → pushed branch
  `save/branch-uncommitted-work-20260722` (daf77b0, 28 files, no secrets).
- Deleted `feat/surveys-atlas-ia-p1-20260627` LOCAL (was 826e733) and REMOTE. Confirmed gone both.
- All of feat's value accounted for: surveys IA + runner reworked & merged to main (#105 / 0674910);
  wiki fix abandoned; Lab-frontend commits abandoned/superseded; dirty tree preserved on the save branch.
- Primary checkout could NOT move onto `main` (owned by the live-deploy worktree NebulaMind-origin-main-live);
  it sits on the save branch @ daf77b0, tracked tree clean.

## IMPORTANT CAVEAT — live backend source
- The live FastAPI backend (uvicorn app.main:app, PID 67804) + celery run from the PRIMARY checkout
  `/Users/duhokim/NebulaMind/NebulaMind/backend/.venv`. Live API healthy (nebulamind.net/api/lab/runs = 200).
- The primary checkout is now on the save branch (which carries feat's history incl. the ORIGINAL runner),
  so the backend still serves the ORIGINAL runner — NOT the reworked one now on main (#105).
- To make the reworked runner live AND fully close Kun's "backend runs off a branch" finding, the backend
  needs to be (re)started from main-equivalent code. That is a deploy decision (and there is a structural
  wrinkle: the backend checkout can't be `main` while the frontend live-deploy worktree owns `main`).
  NOT done here — restarting the live backend unprompted is out of scope.
