# Runtime Checkout Hygiene Plan

> **For Hermes:** This is a planning-only artifact. Do not reset, stash, switch, rebase, deploy, restart, or write DB rows while following this plan unless the user gives the explicit approval phrase for that stage.

**Goal:** Reconcile the dirty running NebulaMind backend checkout with `origin/main` without losing local work, without breaking the currently healthy live source surfaces, and without production DB writes.

**Architecture:** Keep the current runtime untouched until a clean candidate has been built and verified in parallel. Treat the running checkout as production state that must be snapshotted first, then create a clean `origin/main` candidate worktree and prove parity before any service switch. Prefer a launchd working-directory switch to a verified clean candidate over resetting the live checkout in-place.

**Tech Stack:** macOS launchd, git worktrees, Python/FastAPI backend, Next.js frontend/static report service, SQLite/SQLAlchemy source tables.

---

## Current state captured

Captured: `2026-06-29T13:27:28Z` / `2026-06-29 22:27:28 KST`

Runtime checkout:

- Path: `/Users/duhokim/NebulaMind/NebulaMind`
- Backend cwd: `/Users/duhokim/NebulaMind/NebulaMind/backend`
- Runtime branch: `feat/surveys-atlas-ia-p1-20260627`
- Runtime HEAD: `ac0608c`
- `origin/main`: `cc4ced2`
- Divergence: `origin/main...HEAD = 41 1`
  - The runtime branch is missing 41 `origin/main` commits.
  - The runtime branch has 1 branch-only commit.
- Services:
  - backend: PID `20187`, launchd label `com.nebulamind.backend`
  - frontend report/static service: PID `21203`, launchd label `com.nebulamind.frontend`

Live read-only baseline:

- Local citations: HTTP 200, 102 rows, malformed arXiv abs URLs 0
- Public citations: HTTP 200, 102 rows, malformed arXiv abs URLs 0
- Local fact-sources: HTTP 200, 8 rows, malformed arXiv abs URLs 0
- Public fact-sources: HTTP 200, 8 rows, malformed arXiv abs URLs 0
- `page_citation_links = 1351`
- `fact_sources = 391`

Runtime dirty state summary:

- Tracked dirty files: 7
- Untracked paths: 159
- Untracked by top-level:
  - `.hermes`: 1
  - `backend`: 4
  - `docs`: 147
  - `frontend`: 7

Tracked dirty files:

```text
 M backend/app/routers/pages.py
M  backend/app/services/model_canary.py
A  backend/tests/test_model_canary.py
 M frontend/package.json
 M frontend/src/app/wiki/[slug]/WikiPageClient.tsx
 M frontend/src/app/wiki/[slug]/sources/WikiSourcesClient.tsx
 M wiki_schema.md
```

Unstaged tracked diff stat:

```text
backend/app/routers/pages.py                       | 716 +++++++++++++++++++--
frontend/package.json                              |   2 +
frontend/src/app/wiki/[slug]/WikiPageClient.tsx    | 183 +++++-
frontend/src/app/wiki/[slug]/sources/WikiSourcesClient.tsx | 10 +-
wiki_schema.md                                     |   2 +-
5 files changed, 837 insertions(+), 76 deletions(-)
```

Staged diff stat:

```text
backend/app/services/model_canary.py |  5 +++-
backend/tests/test_model_canary.py   | 57 ++++++++++++++++++++++++++++++++++++
2 files changed, 61 insertions(+), 1 deletion(-)
```

The one branch-only commit is:

```text
ac0608c feat(surveys): polish Atlas IA
```

It touches:

```text
M frontend/package.json
A frontend/scripts/test-surveys-atlas-ia.mjs
M frontend/src/app/surveys/page.tsx
M frontend/src/components/surveys/ChartView.tsx
M frontend/src/components/surveys/ControlBar.tsx
M frontend/src/components/surveys/PlotA.tsx
M frontend/src/components/surveys/SurveysView.tsx
A frontend/src/components/surveys/plotting.ts
```

PR #67/#68/#69 scoped source-surface files compared to `origin/main`:

- `backend/tests/test_page_source_surface_fallbacks.py`: same content as `origin/main`, but currently untracked in runtime because the runtime branch predates the file.
- `docs/galaxy_v2_source_surface_reconciliation_20260629.md`: same content as `origin/main`, but currently untracked in runtime because the runtime branch predates the file.
- `backend/app/routers/pages.py`: differs from `origin/main` by one blank-line deletion at the `/paper-directory` route decorator. Behavior should be equivalent, but a future clean candidate should use the exact `origin/main` file.

---

## Recommendation

Do not reset or clean the live runtime checkout in-place.

Preferred path:

1. Snapshot the current dirty runtime state into a timestamped artifact directory.
2. Create a backup branch/ref for the runtime HEAD.
3. Build a separate clean candidate runtime worktree from `origin/main`.
4. Verify the clean candidate with the same backend tests and source-surface probes on an alternate port.
5. Decide whether the branch-only Atlas IA frontend commit `ac0608c` must be ported to `origin/main` via a normal PR before switching any runtime service.
6. Only after a clean candidate passes, switch launchd to that candidate in a narrow maintenance step.
7. Keep DB writes locked at zero throughout.

This avoids the main failure mode: accidentally deleting or overwriting local/staged/untracked runtime artifacts while trying to make the backend checkout clean.

---

## Stage 0: Snapshot-only packet

**Status:** planned only; not executed.

**Objective:** Preserve enough local state to recover the current runtime checkout before any hygiene operation.

**Requires approval phrase:**

```text
APPROVE HYGIENE SNAPSHOT ONLY 20260629T132728
```

**Files/directories to create if approved:**

- `/Users/duhokim/NebulaMind/runtime-hygiene/20260629T132728/manifest.json`
- `/Users/duhokim/NebulaMind/runtime-hygiene/20260629T132728/status-porcelain.txt`
- `/Users/duhokim/NebulaMind/runtime-hygiene/20260629T132728/git-diff.patch`
- `/Users/duhokim/NebulaMind/runtime-hygiene/20260629T132728/git-diff-cached.patch`
- `/Users/duhokim/NebulaMind/runtime-hygiene/20260629T132728/untracked-manifest.json`
- `/Users/duhokim/NebulaMind/runtime-hygiene/20260629T132728/live-baseline.json`

**Read-only checks to repeat before writing snapshot files:**

```bash
RUNTIME=/Users/duhokim/NebulaMind/NebulaMind
git -C "$RUNTIME" fetch origin --prune
git -C "$RUNTIME" status --short
git -C "$RUNTIME" rev-list --left-right --count origin/main...HEAD
curl -fsS 'http://127.0.0.1:8000/api/pages/galaxy-evolution-v2/citations?fresh=hygiene-snapshot'
curl -fsS 'http://127.0.0.1:8000/api/pages/galaxy-evolution-v2/fact-sources?fresh=hygiene-snapshot'
```

**Snapshot commands to run only after approval:**

```bash
RUNTIME=/Users/duhokim/NebulaMind/NebulaMind
OUT=/Users/duhokim/NebulaMind/runtime-hygiene/20260629T132728
mkdir -p "$OUT"
git -C "$RUNTIME" status --porcelain=v1 > "$OUT/status-porcelain.txt"
git -C "$RUNTIME" diff --binary > "$OUT/git-diff.patch"
git -C "$RUNTIME" diff --cached --binary > "$OUT/git-diff-cached.patch"
git -C "$RUNTIME" ls-files --others --exclude-standard -z > "$OUT/untracked-files.zlist"
```

Use Python or a vetted script to hash untracked files into `untracked-manifest.json`; do not copy large untracked artifacts blindly until the manifest is reviewed.

**Verification:**

- Snapshot files exist and are non-empty where expected.
- Manifest records runtime branch/head/origin-main, service PIDs, dirty counts, and live endpoint counts.
- Production source-table counts remain unchanged.

**Stop condition:** Stop after writing snapshot artifacts. Do not clean, reset, switch, or restart.

---

## Stage 1: Backup refs and clean candidate worktree

**Status:** planned only; not executed.

**Objective:** Create a recoverable git ref for the current runtime HEAD and a separate clean candidate from `origin/main` without touching the running checkout.

**Requires approval phrase:**

```text
APPROVE CLEAN CANDIDATE BUILD 20260629T132728
```

**Planned commands:**

```bash
RUNTIME=/Users/duhokim/NebulaMind/NebulaMind
CANDIDATE=/Users/duhokim/NebulaMind/runtime-candidates/origin-main-cc4ced2-20260629T132728
BACKUP_REF=backup/runtime-feat-surveys-atlas-ia-p1-20260627-20260629T132728

git -C "$RUNTIME" branch "$BACKUP_REF" ac0608c
git -C "$RUNTIME" worktree add "$CANDIDATE" origin/main
```

**Important:** This creates refs/worktrees only. It does not reset the running runtime checkout.

**Candidate verification commands:**

```bash
PY=/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python
cd "$CANDIDATE/backend"
$PY -m py_compile app/routers/pages.py tests/test_page_source_surface_fallbacks.py
$PY -m pytest tests/test_page_source_surface_fallbacks.py -q
$PY -m pytest tests -q
```

**Service-parity check on alternate port:**

If candidate backend launch is approved, start it on an alternate port such as 8010, not replacing live PID 20187:

```bash
cd "$CANDIDATE/backend"
PORT=8010 "$PY" -m uvicorn app.main:app --host 127.0.0.1 --port 8010
```

Then probe:

```bash
curl -fsS 'http://127.0.0.1:8010/api/pages/galaxy-evolution-v2/citations?fresh=candidate'
curl -fsS 'http://127.0.0.1:8010/api/pages/galaxy-evolution-v2/fact-sources?fresh=candidate'
```

**Stop condition:** Stop with a candidate-verification report. Do not point launchd at the candidate yet.

---

## Stage 2: Decide what to do with runtime-only work

**Status:** planned only; not executed.

**Objective:** Determine whether local runtime work should be preserved, PR'd, archived, or intentionally dropped before switching runtime to a clean candidate.

**Items requiring review:**

1. Branch-only Atlas IA commit `ac0608c`.
   - It is a frontend/surveys polish commit.
   - It is not in `origin/main`.
   - Decide whether it is still needed in production.
   - If needed, create a clean PR from `origin/main` that ports only that commit or a narrowed version.

2. Staged model canary changes.
   - `backend/app/services/model_canary.py`
   - `backend/tests/test_model_canary.py`
   - These are staged and should not be lost.
   - Decide whether to turn them into a clean PR or archive them as local experimental work.

3. Unstaged frontend/wiki changes.
   - `frontend/package.json`
   - `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
   - `frontend/src/app/wiki/[slug]/sources/WikiSourcesClient.tsx`
   - `wiki_schema.md`
   - Decide whether they are intended feature work, report drift, or stale local changes.

4. Untracked artifacts.
   - 159 untracked paths, mostly under `docs/` and `frontend/public/agent-reports/`.
   - Do not delete them automatically.
   - Classify them into: keep as public reports, archive outside repo, commit as docs, or discard after explicit approval.

**Recommended output:**

- `/Users/duhokim/NebulaMind/runtime-hygiene/20260629T132728/classification.md`
- A table with each dirty/staged/untracked group and proposed disposition.

**Stop condition:** No file deletion, reset, stash, or branch switch in the runtime checkout.

---

## Stage 3: Optional clean PRs for valuable local work

**Status:** planned only; not executed.

**Objective:** Preserve valuable local changes via normal GitHub PRs before runtime cleanup.

**Possible PRs:**

1. `feat: preserve Atlas IA survey polish`
   - Source: branch-only commit `ac0608c`
   - Clean base: `origin/main`
   - Tests: frontend build/smoke plus any survey script.

2. `test: add model canary coverage`
   - Source: staged model canary changes
   - Clean base: `origin/main`
   - Tests: `backend/tests/test_model_canary.py` plus backend suite.

3. Optional wiki UI PR, only if the unstaged wiki changes are intentional.

**Rules:**

- Use temporary clean worktrees from `origin/main`.
- Copy only the intended hunks/files.
- Verify local and GitHub diff file counts before PR creation.
- Do not use the dirty runtime checkout as the PR branch.
- Do not deploy these PRs automatically after merge.

---

## Stage 4: Runtime switch plan after clean candidate passes

**Status:** planned only; not executed.

**Objective:** Move the backend launchd runtime to a clean candidate only after candidate parity and local-work disposition are complete.

**Requires a separate approval phrase:**

```text
APPROVE RUNTIME SWITCH 20260629T132728
```

**Preconditions:**

- Stage 0 snapshot exists and was verified.
- Candidate worktree tests pass.
- Candidate alternate-port probes match current live behavior:
  - citations HTTP 200, 102 rows, malformed arXiv abs URLs 0
  - fact-sources HTTP 200, 8 rows, malformed arXiv abs URLs 0
- Source table counts unchanged before/after candidate probes.
- Local work classification completed.
- Launchd plist diff reviewed.

**Switch approach:**

- Prefer editing launchd service configuration to point backend cwd at the clean candidate worktree, or create a new candidate service label for validation.
- Do not reset the old runtime checkout in-place.
- Keep the old runtime checkout and backup branch intact until the new runtime has survived monitoring.

**Post-switch verification:**

- Record old/new backend PIDs.
- `http://127.0.0.1:8000/api/stats` returns HTTP 200.
- Local and public citations/fact-sources remain HTTP 200.
- Malformed URL counts remain zero.
- `page_citation_links` and `fact_sources` counts remain unchanged.

---

## Risks and mitigations

| Risk | Why it matters | Mitigation |
|---|---|---|
| In-place reset deletes local work | Runtime has 7 tracked dirty files and 159 untracked paths | Snapshot first; use clean candidate worktree instead |
| Runtime branch lacks 41 main commits | Reset/pull could have broad behavior changes | Test clean candidate separately before switch |
| PR #67/#68/#69 files are locally patched/untracked | The live source surfaces are healthy now | Candidate from `origin/main` already contains these commits; verify probes on alternate port |
| Branch-only Atlas IA commit is not in main | Could disappear if switching to clean main | Decide whether to PR/port it before switching frontend/product runtime |
| Report artifacts may be mistaken for app code | 147 untracked docs and 7 frontend public report paths | Classify artifacts; archive or ignore intentionally |
| DB mutation accidentally triggered | User explicitly wants no DB writes | Use only read-only queries/probes; compare table counts before/after every stage |

---

## Immediate next step

The safest executable next step is Stage 0 snapshot only.

If you want Hermes to perform only that snapshot step, paste exactly:

```text
APPROVE HYGIENE SNAPSHOT ONLY 20260629T132728
```

Anything else keeps this plan read-only.
