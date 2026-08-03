# Unit-fate update — Wiki ABANDON · Backend-runner REVIVE — Hwao decision record

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on (updates `BRANCH_FATE_DECISION.md` §4/§5 rows 2–3 on the user's direction)
Author: Hwao/Fable — coordinator and final ratifier per `.hermes.md`
Issued: 2026-07-22T15:09 KST (2026-07-22T06:09 UTC)
Record type: **product/fate decision record.** Executes nothing. The runner execution authority is issued separately in `BACKEND_RUNNER_G3_APPROVAL_PACKET.md`.

---

## 1. User decisions (quoted verbatim, relayed from the Lab session, 2026-07-22)

1. > "ABANDON G3 WIKI UNIT — e5ceda8, the July-2 wiki sources-page fix; not worth reworking, focus is the Lab."
2. > "REVIVE G3 BACKEND-RUNNER as its own backend-only unit (backend/app/routers/lab_runner.py + tools/lab_runner_worker.py + its +85 dirty extension + main.py wiring) — it is the backend behind the Lab /api/lab/runs, so retiring the branch without it breaks the Draft-board Pipeline-runs."
3. > "GO AHEAD, RUN TO COMPLETION: prepare + ratify the backend-runner packet and let Tori execute the rework end-to-end WITHOUT a per-round user pause; keep the fail-closed reviews and all safety stops in force; NO commit or PR to main (that stays a separate gate). Report at PASS/wrap-up."

Canonical gate lines, independently filed by the Lab session as relay records in this directory (verified — the quotes above and the canonical lines agree): `WIKI_UNIT_ABANDON_USER_APPROVAL_RELAY_20260722.md` (`ABANDON G3 WIKI UNIT 20260722`, ~14:10 KST) · `BACKEND_RUNNER_REVIVE_USER_APPROVAL_RELAY_20260722.md` (`REVIVE G3 BACKEND-RUNNER 20260722`, ~14:12 KST) · `BACKEND_RUNNER_GOAHEAD_USER_APPROVAL_RELAY_20260722.md` (`GO AHEAD G3 BACKEND-RUNNER REWORK — RUN TO COMPLETION 20260722`, ~14:2x KST). The REVIVE relay adds the operational finding that live `/api/lab/runs` returns 200 today only because the deployed FastAPI backend runs off the un-merged feature branch — reviving onto main is what makes the Draft-board Pipeline-runs durable.

## 2. Fate update — unit #2, wiki claim-source fix (`e5ceda8`)

**RE-APPLY → ABANDON (user product decision).**

- `e5ceda8` ("fix: show claim sources on wiki sources page") is **not reworked and not re-applied**. It remains in the frozen branch history as read-only reference, like the Lab-frontend commits.
- The fate record's §7 item 3 wiki scope entry (`WikiSourcesClient.tsx` + `test-wiki-sources-page.mjs`) is retired; no wiki G3 packet will be issued.
- **Unaffected and explicitly out of this decision:** the dirty `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` (wiki *presentation*, plan Phase 5 #4, drift 14) and the rest of `BACKEND_WIKI_DIRTY_INTENT.patch` (sha256 `4e1da5b582f4c70cbb4fa709fbf7c033931de1102ee2e3da6ab1211a6d814128`). Those are parallel-track working-tree changes outside branch fate; they stay captured in the Phase 3.2 snapshots and are neither abandoned nor disposed of here.

## 3. Fate update — unit #3 backend half, autonomous-runner backend

**HOLD → REVIVE.** This section is the explicit revive-or-not product decision record required by `BRANCH_FATE_DECISION.md` §5 and §7 item 9 (plan Phase 5 #8). The decision is **REVIVE**, as a **backend-only unit**.

Evidence confirming the user's rationale (verified read-only at decision time):

- Main's shipped Lab UI calls the endpoint: `frontend/src/app/lab/PipelineBoard.tsx:40` and `frontend/src/app/lab/DraftBoard.tsx:319` both `fetch("/api/lab/runs")` (live mirror copy).
- The backend for it exists nowhere on main: `git grep "lab_runner|lab/runs"` against the main tree finds nothing in `backend/` or `tools/`; `backend/app/routers/lab_runner.py` and `tools/lab_runner_worker.py` are absent from main and present at branch HEAD `826e733` (168 and 362 lines).
- The `backend/app/main.py` wiring is exactly 2 added lines (import + `include_router`), with zero other main.py drift either branch-vs-base or base-vs-current-upstream.
- The +85 dirty extension (`LAB_RUNNER_WORKER_DIRTY_INTENT.patch`, +83/−2, sha256 `6669c584c0ee1e34cb5a943fcbf5c056c1a9d780eef4eb6b674b4e8a8f8a1bb4`) is the literature-grounding addition (`lit_context()`, `lit_refs`/`lit_reflist`/`lit_papers` fields, novelty and expected-value gates) — currently **fail-open, log-only on skip**, which is exactly the gap the fate record's acceptance clause requires the rework to close ("must expose when fail-open literature grounding did not run").

Scope per fate record §7 item 3 (runner): `backend/app/routers/lab_runner.py`, `backend/app/main.py` (2-line registration), `tools/lab_runner_worker.py` incl. the +85 extension. The frontend configurator half of `fd15e8e` **stays ABANDONED** — this decision does not revive any frontend file.

**§7 item 9 branch note:** the precondition ("decision record must exist before `salvage/lab-runner-backend` is cut") is now satisfied by this record — but **no salvage branch is cut in this unit**. The user's own line excludes commit/PR; the rework runs in a detached disposable worktree with preserved patches/receipts, exactly like the Surveys unit. Cutting the branch and committing remain behind the future commit gate.

## 4. Execution mode granted by decision (3)

Run-to-completion: Tori executes the runner rework end-to-end **without per-round user pauses**, under `BACKEND_RUNNER_G3_APPROVAL_PACKET.md`. Not waived and still fully in force: every stop rule (freeze + escalate on trigger), the fail-closed board reviews (Lana / Goru / Tori — any FAIL freezes the unit), the no-commit/no-PR/no-push/no-merge boundary, G5/G7 closures, and the no-network rule. "Run to completion" removes check-ins, not checks.

## 5. Branch salvage ledger after this record

| Unit | Fate | State |
|---|---|---|
| Surveys Atlas IA | REWORK | **CLOSED — VERIFIED-PASS** (`HWAO_G3_SURVEYS_WRAP_UP_COMPLETE_20260722`, 2026-07-22 14:08 KST: V2 PASS after three fail-closed reviews + two user-approved rescopes; worktree retained frozen as the V2 embodiment; removal requires its own line `REMOVE G3 SURVEYS WORKTREE 20260722`) |
| Wiki claim-source fix `e5ceda8` | **ABANDON** (this record) | Closed; reference-only in branch history |
| Backend runner (backend half of `fd15e8e`) | **REVIVE** (this record) | Packet issued: `HWAO_G3_BACKEND_RUNNER_REVIVE_APPROVED_20260722`; Tori to execute run-to-completion |
| Lab frontend (`fd15e8e` front half, `01e8afa`, `586fef1`, `826e733`) | ABANDON (unchanged) | Closed; reference-only |

Once the runner unit reaches PASS/wrap-up with receipts, all salvage value of `feat/surveys-atlas-ia-p1-20260627` is extracted; retirement of the branch container becomes eligible as its **own separate future G3 decision** (not granted here).

Gates unchanged by this record: G3 other units Held · G4a/G4b/G4c Held separately · G5 Closed · G6 Held · G7 Closed. Files written by this pass: 2 (this record + the runner packet). No git write, no source edit, no network.

---

`HWAO_WIKI_ABANDON_RUNNER_REVIVE_RECORDED_20260722`
