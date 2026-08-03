# G3 Backend-runner revive approval packet — Hwao authority record

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on (per-topical G3 packet per `BRANCH_FATE_DECISION.md` §7)
Unit: **Backend autonomous-runner → REVIVE, backend-only** (product decision: `HWAO_WIKI_ABANDON_RUNNER_REVIVE_RECORDED_20260722`, satisfying fate record §5 / §7 item 9)
Author: Hwao/Fable — coordinator and final ratifier per `.hermes.md`
Issued: 2026-07-22T15:09 KST (2026-07-22T06:09 UTC)
Record type: **approval packet.** Writing it executes nothing; execution is granted to the Tori lane under §10 run-to-completion mode.

---

## Verdict: **PASS**

All §7 requirements of `BRANCH_FATE_DECISION.md` are satisfied, including the revive-decision precondition (§7 item 9) and a fresh recount with one item of **explained drift, adjudicated in §2**. The user approval line exists and covers this packet and its run-to-completion mode.

## 1. Approval provenance (quoted)

- **User approval (verbatim, relayed from the Lab session, 2026-07-22):** "REVIVE G3 BACKEND-RUNNER as its own backend-only unit (backend/app/routers/lab_runner.py + tools/lab_runner_worker.py + its +85 dirty extension + main.py wiring)…" and "GO AHEAD, RUN TO COMPLETION: prepare + ratify the backend-runner packet and let Tori execute the rework end-to-end WITHOUT a per-round user pause; keep the fail-closed reviews and all safety stops in force; NO commit or PR to main (that stays a separate gate). Report at PASS/wrap-up."
- **Canonical gate lines** (filed by the Lab session in this directory, verified consistent with the quotes above): `REVIVE G3 BACKEND-RUNNER 20260722` (`BACKEND_RUNNER_REVIVE_USER_APPROVAL_RELAY_20260722.md`) and `GO AHEAD G3 BACKEND-RUNNER REWORK — RUN TO COMPLETION 20260722` (`BACKEND_RUNNER_GOAHEAD_USER_APPROVAL_RELAY_20260722.md`) — the latter is the execution-activation line the REVIVE relay reserved.
- **Binding reading:** these are the explicit user approval lines for THIS packet (fate §7 item 10). They cover the backend-runner unit and its uninterrupted execution mode. They do **not** grant commit/PR/push/merge (excluded by the user's own words), any other unit, branch retirement, base advancement, or any G4/G5/G6/G7 action.

## 2. Fresh recount at approval time — with drift adjudication

| Check | Expected (fate §7 item 1) | Observed | Status |
|---|---|---|---|
| Branch | `feat/surveys-atlas-ia-p1-20260627` | same | ✅ |
| HEAD | `826e733` | `826e73381cb7870954bbd7f041a618408385a80a` | ✅ |
| Merge-base vs named base | `63f7b305` | `63f7b305c0560f06402ac71858630864e5e6d494` | ✅ |
| Ahead / behind **vs named base `28e8735`** | 6 / 66 | 6 / 66 | ✅ |
| Modified / untracked / deleted | 20 / 360 / 0 | 20 / 360 / 0 | ✅ |
| Snapshot integrity | 4/4 SHA-256 + reverse-apply | 4/4 match, 4/4 reverse-apply OK | ✅ |
| Runner worktree pre-existing | none | none; target path absent | ✅ |
| `origin/main` cache pointer | `28e87357` | **`4bbb1160f0e93bd6c2e557cbc49254e76738347f` — MOVED** | ⚠️ explained below |
| Live mirror | `28e8735 [main]` | **`4bbb116` on `main` — MOVED** | ⚠️ explained below |

**Drift adjudication (binding for this unit).** The cached `origin/main` and the live mirror advanced three commits (`ed20708` #102, `68c92c2` #103, `4bbb116` #104) between the morning receipts and this packet. This lane performed **no fetch**; the advance came from the user's own Lab session activity (the same session that issued today's decisions). Verified read-only:

- The three commits touch **only** Lab docs/PDF/revision-log files and two Lab UI text files (`FlagshipStudies.tsx`, `FrontierDrafts.tsx`). **Zero backend files changed; `backend/app/main.py` upstream drift: none; `PipelineBoard.tsx` / `DraftBoard.tsx` (the `/api/lab/runs` consumers): untouched.**
- Every input of this unit is pinned to objects, not pointers: branch HEAD `826e733`, named base `28e8735` (object present locally), and the SHA-pinned Phase 3.2 snapshots. All verified unchanged; 6/66 holds exactly against the named base.

Ruling: **explained drift — proceed.** Per fate §7 item 5 the unit base is the **named commit `28e87357`**, not the moving cache pointer; advancing the base is a separate future approval and is **not taken** (unnecessary — the upstream delta contains no backend change, so the rework is byte-valid against `4bbb116`'s backend too). **Execution-time recount rule for this unit:** verify branch/HEAD, 6/66 **vs `28e8735`**, 20/360/0, and 4/4 reverse-apply — drift there → STOP. Movement of the `origin/main` cache pointer or the live mirror from external Lab-session activity is **logged in receipts, not a stop**, provided the named-base object and unit inputs verify.

## 3. Unit inputs (verified read-only at approval time)

| Input | Verification |
|---|---|
| `backend/app/routers/lab_runner.py` @ `826e733` | PRESENT, 168 lines; ABSENT on main — branch-only ✅ |
| `tools/lab_runner_worker.py` @ `826e733` | PRESENT, 362 lines; ABSENT on main — branch-only ✅ |
| `backend/app/main.py` wiring | delta base↔branch-HEAD is exactly 2 added lines: `from app.routers import lab_runner` + `app.include_router(lab_runner.router)` ✅ |
| Worker dirty extension | `LAB_RUNNER_WORKER_DIRTY_INTENT.patch`, +83/−2, sha256 `6669c584c0ee1e34cb5a943fcbf5c056c1a9d780eef4eb6b674b4e8a8f8a1bb4`, reverse-applies against primary (worktree = HEAD + patch, losslessly reconstructible) ✅ |
| Grounding content of the extension | adds `lit_context()`, `rec["lit_refs"]/["lit_reflist"]/["lit_papers"]`, "lit grounding skipped: …" logging, novelty + expected-value gates — **fail-open, log-only on skip** (the acceptance gap §7 closes) ✅ |
| Product rationale | mirror `PipelineBoard.tsx:40` and `DraftBoard.tsx:319` `fetch("/api/lab/runs")`; no `lab_runner`/`lab/runs` anywhere in main backend/tools ✅ |
| Interpreter/deps | `backend/.venv` (primary, used read-only) has fastapi, pytest, numpy, requests, httpx — **zero installs needed** ✅ |
| Router runtime facts binding the test design | `RUNS_DIR = Path(os.environ.get("LAB_RUNS_DIR", <absolute path into the PRIMARY checkout>))` with **import-time `mkdir`**; `_lab_token()` falls back to **opening `backend/.env`** when `LAB_RUN_TOKEN` is unset; `POST /runs` is token-guarded, `GET` routes are open ✅ |

## 4. Authorized git action — exactly ONE command

```
git worktree add --detach /Users/duhokim/NebulaMind/agent-worktrees/g3-backend-runner-revive-20260722 28e873570f1c479fffd18a5106e5afa91d46e3e9
```

Detached HEAD only; **no branch creation** — explicitly including **no `salvage/lab-runner-backend`** (the §7 item 9 decision record now exists, but branch-cutting belongs to the future commit gate the user reserved). No fetch; base is the named ratified commit. One disposable worktree for this one unit.

## 5. Writable scope (closed world) — exactly 4 paths in the worktree

1. `backend/app/routers/lab_runner.py` — new file, sourced from `git show 826e733:backend/app/routers/lab_runner.py`
2. `tools/lab_runner_worker.py` — new file, sourced from `git show 826e733:tools/lab_runner_worker.py` **then** `git apply` of the SHA-pinned `LAB_RUNNER_WORKER_DIRTY_INTENT.patch` (yields the captured latest intent)
3. `backend/app/main.py` — the 2-line registration only
4. `backend/tests/test_lab_runner_revive_smoke.py` — **the one authorized new test file**

Rework adaptations are allowed **within these files only** — that is what REWORK means: (a) the §7 acceptance exposure (grounding status), (b) path hygiene: replace the hardcoded absolute primary-checkout defaults (`RUNS_DIR` fallback, `ENV_FILE`) with env-first / repo-relative resolution — the env override contract must hold, (c) minimal import/compat fixes against base `28e8735`. Generated outputs inside the worktree are allowed (`__pycache__/`, `.pytest_cache/`, a worktree-local temp runs dir). **Not authorized:** any other tracked path, any other new file, any frontend file (the frontend half stays ABANDONED; `#97–#101` intactness is proven by the diff never leaving the 4 paths), any write to the primary checkout, live mirror, or `backend/app.db` (tracked at base — must remain byte-identical), any `.env*` content access.

## 6. Method — staged RED→GREEN→refactor (honest RED for the new behavior)

1. **Port:** materialize the three production files per §5. Basic smoke assertions (imports, wiring text, GET shapes) MAY pass immediately — that is the port baseline, not the RED target.
2. **RED:** add the **acceptance assertion** — run records exposed by `GET /api/lab/runs` (list items) **and** `GET /api/lab/runs/{rid}` (detail) must carry a machine-readable literature-grounding status (grounded true/false + skip reason when false; true only when grounding ran on ≥1 paper) — and observe it **FAIL against the ported-verbatim code** (which only logs skips) **before** any production edit implementing it. If it passes before implementation → STOP (assertion not meaningful).
3. **GREEN:** implement the exposure within §5 scope (derive router-side from the `lit_*` fields and/or set worker-side) until the full suite passes.
4. **Refactor** (path hygiene etc.) with the suite green after every step.

## 7. Test plan (worktree-only, offline, in-process — no server, no network, no DB)

Invocation: `LAB_RUNS_DIR=<worktree>/.tmp-lab-runs LAB_RUN_TOKEN=<dummy test value> /Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -m pytest tests/test_lab_runner_revive_smoke.py -q` run from `<worktree>/backend`.

Binding test-design rules (from §3 runtime facts):

1. **Both env vars are set before the router module is imported** — so the import-time `mkdir` lands in the worktree temp dir (never the primary checkout) and `_lab_token()` short-circuits on the env var (**`backend/.env` is never opened by anything, including the test process**).
2. The router is mounted on a **fresh minimal `FastAPI()` instance** — never import `app.main`, never TestClient the full app (keeps app-DB/startup untouched; G5 stays closed). `main.py` wiring is verified **textually** (the 2 lines present), not by import.
3. `POST /api/lab/runs` is exercised **only for auth-rejection paths** (missing/wrong bearer → 401; unset token config → 503). **No authorized POST ever runs in tests** — no run creation, no worker spawn, no network. `GET` shape/acceptance tests use fixture run-record JSON seeded directly into the temp `LAB_RUNS_DIR`.
4. The worker module is imported by path; import must succeed using existing deps and must create no files and reach no network (its `requests`/TAP/Ollama functions are never called; Lana's review confirms no import-time I/O).
5. Post-test receipts: `git status --porcelain` in the worktree lists **exactly the 4 authorized paths** (this simultaneously proves scope, `app.db` untouched, and no stray artifacts outside ignored/generated dirs); no new `*.db`/`*.sqlite*` anywhere; `git diff HEAD --numstat` captured; full pytest transcript captured.

## 8. Board split (fail-closed) and cockpit

- **Lana** — read-only code + acceptance review: grounding-status exposure correctness, no import-time I/O or network in test paths, path-hygiene rework sanity.
- **Goru** — mechanical verification: diff confined to the 4 paths, counts/hashes (one `shasum -a 256` invocation per file, each line starting with the command), transcript checks.
- **Tori** — executor and receipt verifier; relays the wrap-up report.
- Any reviewer FAIL → freeze + escalate (reviews are fail-closed; run-to-completion does not waive them).
- **Cockpit/status update: explicitly SKIPPED — G7 remains Closed.**

## 9. Stop rules

Verbatim from `BRANCH_FATE_DECISION.md` §7 item 6:

> any add/add conflict in a Lab file (`LabStages.tsx`, `frontiersData.ts`, `LabTopTabs.tsx`, `labTabStore.ts`, `lab/page.tsx`) → STOP (confirms abandon; never hand-merge to re-derive superseded upstream code); a hunk dragging unrelated upstream lines → STOP and re-scope; runner reintroduction touching any DB/migration/model metadata → STOP (G5 Closed); recount drift from 6/66/20/360 → STOP and re-inventory.

Packet-specific additions (all → freeze worktree, write stop receipt, escalate; no self-granted continuation):

1. Any out-of-scope write (any tracked path beyond the 4; any new non-generated file; any primary/mirror write).
2. The §6 acceptance assertion passing before its implementation exists (RED not achieved).
3. Any dependency/install need — anything `backend/.venv` + stdlib cannot satisfy.
4. Any DB touch: modification of tracked `backend/app.db`, any new DB file, any migration/model-metadata edit (G5 Closed).
5. Any `.env*` content access attempt, by code under test or tooling (tests must rely on the preset env vars).
6. Any network attempt during tests (worker network functions executing, TAP/ADS/Ollama calls, any socket).
7. Primary-checkout drift: branch/HEAD, 6/66 vs named base `28e8735`, 20/360/0, or 4/4 reverse-apply failing → STOP and re-inventory. (Cache-pointer / live-mirror movement from external Lab activity: **log, not stop** — §2 ruling.)

## 10. Run-to-completion execution grant

Tori executes §4→§8 end-to-end **without per-round user pauses**, through wrap-up: preserve the final `git diff HEAD` patch + execution receipt + pytest transcript **under this phase3 directory** (patch sha256 recorded), obtain Lana/Goru sign-offs, then **keep the worktree in place, frozen** (removal is a separate user line), and report **PASS/wrap-up** to the user via the report lane. Every stop rule and review gate stays armed throughout; a triggered stop ends autonomous mode immediately.

## 11. Prohibited throughout

No `git add`/stage/commit; no PR; no push; no merge; no rebase/cherry-pick; no branch creation or switch (incl. `salvage/*`); no stash/reset; no worktree removal before an approved wrap-up line; no runtime/deploy/restart/uvicorn bind; no cockpit or publication write; no DB/SQL/migration; no network/fetch/install; no `.env*` content access. Primary checkout and live mirror are read-only. The Surveys worktree `g3-surveys-rework-20260722` remains frozen and untouched by this unit.

## 12. Gate ledger after this packet

G1 Completed · G2 Completed · **G3 backend-runner unit: OPEN one-shot** (exactly §4 command + §5 scope + §7 tests under §9 stops, §10 mode; re-latches on wrap-up or STOP) · G3 Surveys unit: **CLOSED — VERIFIED-PASS** (`HWAO_G3_SURVEYS_WRAP_UP_COMPLETE_20260722`; worktree retained frozen) · G3 wiki unit: closed ABANDONED · G3 everything else (commits, PRs, branch retirement, base advance): **Held** · G4a/G4b/G4c Held separately · G5 Closed · G6 Held · G7 Closed.

## 13. Safety ledger for this approval pass

Git writes 0 · worktree actions 0 · branch/stash/reset 0 · source/test edits 0 · DB/SQL 0 · runtime/deploy/cockpit 0 · network/fetch 0 · `.env*` content access 0 (router env-fallback facts read from the **committed blob** via `git show`, not from any `.env` file) · files written this pass: 2 (`WIKI_ABANDON_RUNNER_REVIVE_DECISION_RECORD.md` + this packet).

Methods: read-only git (`rev-parse`, `merge-base`, `rev-list --count`, `status --porcelain`, `worktree list`, `cat-file -e`, `show`, `diff`, `log`, `grep`, `apply --reverse --check`, `apply --numstat`); `shasum -a 256` per patch file; mirror greps; `backend/.venv` import probes (no writes). No fetch.

---

`HWAO_G3_BACKEND_RUNNER_REVIVE_APPROVED_20260722`
