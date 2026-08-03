# G3 Surveys-only approval packet — Hwao authority record

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on (per-topical G3 packet per `BRANCH_FATE_DECISION.md` §7)
Unit: **Surveys Atlas IA → REWORK** (the one unit ratified REWORK in `HWAO_PHASE3_BRANCH_FATE_DECISION_COMPLETE_20260721` §4/§5)
Author: Hwao/Fable — coordinator and final ratifier per `.hermes.md`
Issued: 2026-07-22T08:50 KST (2026-07-21T23:50 UTC)
Record type: **approval packet.** This document itself executes nothing — no worktree, no source action occurs by writing it. It grants a one-shot, closed-world G3 authority for exactly the action and scope in §5–§6, to be executed in a subsequent lane step under the board split in §9.

---

## Verdict: **PASS**

All ten §7 requirements of `BRANCH_FATE_DECISION.md` are satisfied and independently re-verified read-only by Hwao at approval time (evidence §2–§4). The one explicit user approval line exists and covers exactly this packet (§1).

---

## 1. Approval provenance (quoted)

- **User approval line (verbatim):** "**go ahead with the next step**" — given 2026-07-22, immediately after Tori presented the next-step choice.
- **Tori's presented interpretation that the user approved (verbatim as relayed):** "**G3 Surveys only: one disposable worktree from cached origin/main, exact Surveys rework unit, tests, no commit/PR/push/merge.**"
- **Binding reading (Hwao):** this is the one explicit user approval line for THIS packet only, per `BRANCH_FATE_DECISION.md` §7 item 10. It is **not blanket G3**. No other unit (wiki re-apply, runner revival, branch retirement, any commit/PR/push/merge anywhere) inherits anything from it. When this packet's unit completes or stops, G3 re-latches to Held for everything.

## 2. Fresh recount at approval time (independent, read-only, no fetch)

Recounted live by Hwao in this lane; also matches Tori's fresh recount relayed with the request.

| Check | Required (§7 item 1) | Observed | Match |
|---|---|---|---|
| Branch | `feat/surveys-atlas-ia-p1-20260627` | same | ✅ |
| HEAD | `826e733` | `826e73381cb7870954bbd7f041a618408385a80a` | ✅ |
| `origin/main` (locally cached, no fetch) | `28e87357` | `28e873570f1c479fffd18a5106e5afa91d46e3e9` | ✅ |
| Merge-base | `63f7b305` | `63f7b305c0560f06402ac71858630864e5e6d494` | ✅ |
| Ahead / behind | 6 / 66 | 6 / 66 | ✅ |
| Modified / untracked / deleted | 20 / 360 / 0 | 20 / 360 / 0 | ✅ |
| G3 Surveys worktree pre-existing | none | none — `git worktree list` has no g3-surveys entry; target path `/Users/duhokim/NebulaMind/agent-worktrees/g3-surveys-rework-20260722` does not exist | ✅ |
| Clean live mirror | at cached main | `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live` at `28e8735 [main]` | ✅ |

Note: the pre-existing worktree `/Users/duhokim/NebulaMind/agent-worktrees/page58-surveys-overnight-20260627` (`20ccad5`) is an unrelated older lane artifact. It is NOT this packet's worktree, is not written, and must not be reused or removed under this authority.

Methods: `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD`, `git rev-parse origin/main`, `git merge-base`, `git rev-list --count` both directions, `git status --porcelain` code counts, `git worktree list`, `ls`. Read-only throughout; no fetch; no `.env*` content touched.

## 3. Snapshot integrity re-check (§7 item 2) — 4/4 PASS

SHA-256 recomputed by Hwao on all four Phase 3.2 patches; `git apply --reverse --check` run from repo root against the primary working tree; patch path union diffed against `git diff --name-only`.

| Patch | SHA-256 recomputed vs manifest | Reverse-apply |
|---|---|---|
| `SURVEYS_DIRTY_INTENT.patch` (10 paths) | `f083c5d388567a24ca4c69c77140a563e2bcbe39e2c9c4a7f12435c7972a927b` ✅ | ✅ OK |
| `LAB_RUNNER_WORKER_DIRTY_INTENT.patch` (1) | `6669c584c0ee1e34cb5a943fcbf5c056c1a9d780eef4eb6b674b4e8a8f8a1bb4` ✅ | ✅ OK |
| `BACKEND_WIKI_DIRTY_INTENT.patch` (5) | `4e1da5b582f4c70cbb4fa709fbf7c033931de1102ee2e3da6ab1211a6d814128` ✅ | ✅ OK |
| `IDEAS_NAV_DIRTY_INTENT.patch` (4) | `a696975d0760a649a6ba8e8629225391b3b180bfff19baa690f3b9da5ebd39ce` ✅ | ✅ OK |

- Path union vs `git diff --name-only`: **exact 20/20 set match, no extras, no gaps.**
- Consequence: the dirty tree still exactly equals the snapshots — the latest Surveys intent is captured and losslessly reconstructible; nothing has drifted since `TORI_PHASE3_DIRTY_INTENT_SNAPSHOTS_COMPLETE_20260721`.
- Surveys patch numstat (rework-intent size, add/del): `package.json` 2/0, `test-surveys-atlas-ia.mjs` 43/2, `SurveyDetailClient.tsx` 4/1, `BandSpectrumStrip.tsx` 15/4, `ChartView.tsx` 18/0, `FilterSheet.tsx` 3/0, `PlotB.tsx` 94/55, `SurveyCard.tsx` 7/2, `SurveyPeek.tsx` 3/0, `SurveysView.tsx` 23/3 — consistent with the census (§5 of the fate record).

## 4. P0 preservation receipt confirmed in place (§7 item 4)

- `phase0/PHASE0_PRESERVATION_RECEIPT.md` present: Contract v1 `PASS` (16/45/45, 26/26, 16/16, 0 errors), marker `PHASE0_CONTRACT_V1_PRESERVATION_COMPLETE_20260721T114246Z`.
- Manifest SHA-256 recomputed now: `b7f0de4df74929d7c0aeaad20ec796b7795ac1c5132dfe8ddb3c54c13f443abd` — matches the receipt.
- Out-of-repo backup `/Users/duhokim/HermesOps/backups/claim-ledger-contract-v1-20260721T114246Z/` present with **36 files** (= 36 manifest rows).

## 5. Authorized action — exactly ONE git command, nothing else

```
git worktree add --detach /Users/duhokim/NebulaMind/agent-worktrees/g3-surveys-rework-20260722 28e873570f1c479fffd18a5106e5afa91d46e3e9
```

- **Detached HEAD only. NO branch creation** — no `-b`, no `salvage/*`, no branch switch or checkout anywhere, in the worktree or the primary.
- Base = named cached `origin/main` `28e87357` (§7 item 5). **No fetch/pull** — advancing the base is a separate future approval; network stays gated.
- One disposable worktree for this one unit. No second worktree, no re-add after removal without a fresh packet.
- This packet issues the authority; it does **not** perform the command. Execution happens in the follow-on lane step.

## 6. Writable scope (closed world)

**Tracked-file writes inside the worktree are limited to exactly these 10 paths** (the `SURVEYS_DIRTY_INTENT.patch` set, verbatim from the Phase 3.2 manifest):

1. `frontend/package.json`
2. `frontend/scripts/test-surveys-atlas-ia.mjs`
3. `frontend/src/components/surveys/ChartView.tsx`
4. `frontend/src/components/surveys/SurveysView.tsx`
5. `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
6. `frontend/src/components/surveys/BandSpectrumStrip.tsx`
7. `frontend/src/components/surveys/FilterSheet.tsx`
8. `frontend/src/components/surveys/PlotB.tsx`
9. `frontend/src/components/surveys/SurveyCard.tsx`
10. `frontend/src/components/surveys/SurveyPeek.tsx`

- The rework re-derives the captured intent (§3 numstat; `SURVEYS_DIRTY_INTENT.patch` as reference) onto base `28e87357`. The patch was cut against branch HEAD `826e733`, so a mechanical `git apply` onto the base is not assumed and not required — REWORK per the fate record, cherry-pick prohibited.
- **Generated build/test outputs inside the worktree are allowed** (e.g. `.next/`, `*.tsbuildinfo`, test logs, and `node_modules` provisioned per §10). They are disposable with the worktree.
- **New source files are NOT authorized.** Any tracked path outside the 10, or any new non-generated file → out-of-scope write → STOP (§11). No Lab, backend, wiki, ideas/nav hunks (§7 item 3 closed-world rule).
- **Primary dirty checkout** `/Users/duhokim/NebulaMind/NebulaMind` — **read-only** for the entire unit. Never written, never stashed, never reset, never checked out.
- **Clean live mirror** `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live` — **read-only**, never written.
- No `.env*` content is opened, read, printed, or hashed at any point (G4c discipline).

## 7. Method — strict RED→GREEN→refactor

1. **Baseline:** in the fresh worktree, run the focused smoke exactly as in §8 and record its baseline result.
2. **RED first:** add the meaningful new failing assertion(s) to `frontend/scripts/test-surveys-atlas-ia.mjs` — capturing the Surveys rework acceptance — and observe it FAIL **before any production edit**. If the focused smoke passes before a meaningful new assertion exists, that is a STOP (§11), not permission to start editing.
3. **GREEN:** minimal production edits strictly within the 10 paths until the focused smoke passes.
4. **Refactor:** within-scope cleanup only, tests re-run green after each step.

## 8. Test plan (worktree only; no server started or deployed)

Run inside `/Users/duhokim/NebulaMind/agent-worktrees/g3-surveys-rework-20260722`:

1. Focused smoke (verbatim per fate record §7 item 7): `cd frontend && node scripts/test-surveys-atlas-ia.mjs` → expected final line `surveys atlas IA smoke checks passed`.
2. **Related survey tests if found:** read-only discovery (e.g. `frontend/scripts/*survey*`, test files referencing surveys components); run any found. If none found, record "none found".
3. `cd frontend && npx tsc --noEmit` — clean.
4. `cd frontend && npm run build` — completes.
5. **Local build artifact / route marker inspection only:** verify the surveys route output exists in the build artifacts (e.g. `.next/` server app output for `/surveys` and `/surveys/[slug]`, route manifest entries). **No `next start`, no `next dev`, no port bound, no deploy, no runtime restart** — G7 is Closed; tests are not deployments and use disposable paths only.

## 9. Board split for execution

- **Lana** — read-only UX/acceptance review of the reworked Surveys surfaces against the captured intent; no writes.
- **Goru** — mechanical verification: worktree diff confined to the 10 paths, counts, SHA/receipt arithmetic, test transcript check.
- **Tori** — receipt verification and relay to the user; bounded executor only where Hwao directs.
- **Hwao** — coordination and final ratification of the execution receipt.
- **Cockpit/status update: explicitly SKIPPED for this unit — G7 remains Closed.** No cockpit, publication, or status-page write accompanies this packet or its execution; Hwao will decide cockpit reporting separately if and when G7 work is ever proposed.

## 10. Dependencies / network (hard boundary)

- **Existing on-disk dependencies only.** No network of any kind: no fetch/pull, no `npm|pnpm|yarn install`, no registry, proxy, or download.
- `node_modules` for the worktree may be provisioned **only by local copy or link from an already-present on-disk checkout** (e.g. the primary checkout's `frontend/node_modules`, read-only source).
- If the build/tests cannot proceed without an install or a new dependency (including anything the `package.json` rework would introduce) → STOP (§11). No offline-install workaround is authorized.

## 11. Stop rules

Verbatim from `BRANCH_FATE_DECISION.md` §7 item 6:

> any add/add conflict in a Lab file (`LabStages.tsx`, `frontiersData.ts`, `LabTopTabs.tsx`, `labTabStore.ts`, `lab/page.tsx`) → STOP (confirms abandon; never hand-merge to re-derive superseded upstream code); a hunk dragging unrelated upstream lines → STOP and re-scope; runner reintroduction touching any DB/migration/model metadata → STOP (G5 Closed); recount drift from 6/66/20/360 → STOP and re-inventory.

Additional stop rules binding on this packet:

1. **Any out-of-scope write** — any tracked path outside the 10 in §6, any new non-generated file, any write to the primary checkout or live mirror → STOP.
2. **Focused smoke passing before a meaningful new assertion has been added (RED not achieved)** → STOP; re-derive the assertion; do not touch production code.
3. **Dependency/install need** — anything requiring network, package install, or a new dependency → STOP.
4. **Any DB/backend/Lab/wiki/ideas/nav touch** — read is fine, write of any such surface → STOP (those units are Phase 5 / separate packets; G5 Closed).
5. **Primary or live-mirror drift** — at execution start and at each checkpoint re-run the §2 recount; primary no longer `feat/surveys-atlas-ia-p1-20260627` @ `826e733` with 20/360/0 and 4/4 reverse-apply OK, or mirror no longer `28e8735 [main]` → STOP and re-inventory before anything else.

On any STOP: freeze the worktree, write a stop receipt, report to the user via Tori. No self-granted continuation.

## 12. Rollback

- Discard = **`git worktree remove` of the disposable worktree ONLY, and only after preserving a patch/receipt of whatever work exists** (`git -C <worktree> diff` captured into this handoff directory with a receipt) — the same lossless-snapshot discipline as Phase 3.2.
- Verbatim per fate record §7 item 8: no `stash`/`reset` of the primary checkout at any point; `git reflog` covers branch-local mistakes; no live-mirror write.

## 13. Prohibited throughout (unchanged by this packet)

No `git add`/stage/commit; no PR; no push; no merge; no rebase/cherry-pick; no branch creation or switch; no stash/reset; no runtime/deploy/restart; no cockpit or publication write; no DB/SQL/migration; no file moves/deletes outside worktree-generated outputs; no `.env*` content access; no network. The branch container `feat/surveys-atlas-ia-p1-20260627` stays frozen read-only; its retirement remains a separate future G3 decision.

## 14. Gate ledger after this packet

| Gate | State |
|---|---|
| G1 board reconciliation | Completed (`HWAO_G1_BOARD_RECONCILIATION_VERIFIED_20260721`) |
| G2 manifest + backup | Completed (`PHASE0_CONTRACT_V1_PRESERVATION_COMPLETE_20260721T114246Z`) |
| **G3 — this Surveys unit only** | **OPEN, one-shot**: exactly the §5 command + §6 scope + §8 tests, under §11 stops; re-latches to Held on unit completion or STOP |
| G3 — everything else (wiki re-apply, runner, branch retirement, any commit/PR/push/merge) | **Held**; each needs its own packet + its own user approval line |
| G4a / G4b / G4c | **Held**, each separately (per `HWAO_PHASE4_DISPOSITION_PACKETS_RATIFIED_20260722`) |
| G5 DB/SQL/migration | **Closed** |
| G6 status/debate-map docs run | **Held** |
| G7 runtime/deploy/publication/cockpit | **Closed** — hence §9 cockpit skip |

## 15. Safety ledger for this approval pass (all git-write counters zero)

Branch/checkout/switch 0 · worktree creation 0 · rebase/cherry-pick 0 · add/stage/commit/PR/push/merge 0 · stash/reset 0 · file move/delete 0 · product/source/test edit 0 · DB/SQL 0 · runtime/deploy 0 · network/fetch 0 · publication/cockpit 0 · `.env*` content access 0 · **files written 1 (this packet)**.

Methods: read-only reads of `.hermes.md`, Phase 0 receipt, `BRANCH_FATE_DECISION.md`, `PATCH_SNAPSHOT_MANIFEST.json`, Phase 4 ratification, patch headers; read-only git (`rev-parse`, `merge-base`, `rev-list --count`, `status --porcelain`, `worktree list`, `diff --name-only`, `apply --reverse --check`, `apply --numstat`); `shasum -a 256`; `ls`/`find` metadata only.

---

`HWAO_G3_SURVEYS_ONLY_APPROVED_20260722`
