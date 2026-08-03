# Kun Oversight Report Corrective Application Plan

> **For Hermes:** Use a fresh, bounded lane for each approved phase. Re-read this plan and `.hermes.md` before acting. Verify the prior phase’s receipt before starting the next gated phase.

**Goal:** Apply the useful findings from Kun’s NebulaMind oversight report without destroying untracked canonical work, regressing the live Lab, or crossing any git, cleanup, data, runtime, or publication gate.

**Architecture:** Preservation and truth reconciliation come first. Product information architecture is decided before branch mechanics. Research-state correction, worktree hygiene, product salvage, branch convergence, and test hygiene remain separate tracks with separate receipts and approvals.

**Tech stack:** Git; Python 3.11; pytest; SQLAlchemy/Alembic; FastAPI; Next.js; Markdown/JSON/JSONL research artifacts.

**Run:** `quartet-kun-application-plan-20260721T114246Z` — 2026-07-21 20:42:46 KST

**Status:** `PLANNING_ONLY` — no application work is authorized by this document.

**Execution phrase:** `NO ACTIVE EXECUTION PHRASE`

`QUARTET_KUN_REPORT_APPLICATION_PLAN_COMPLETE_20260721T114246Z`

---

## 1. Quartet assembly and verdict

The user-defined Quartet is **Trio + Kun**:

- **Hwao/Fable:** coordinator and final ratifier.
- **Tori/Hermes:** Trio relay, source verifier, plan assembler, and receipt verifier.
- **Goru:** mechanical feasibility, counts, and gate checks.
- **Kun/Kimi K3:** implementation and reproducibility oversight.

**Lana was consulted as a non-voting semantic and product-IA adviser.** Her advice informs the plan but does not change the Quartet’s membership.

### Receipt ledger

| Participant | Contribution | Receipt |
|---|---|---|
| Hwao/Fable | Final reconciliation and sequencing | `HWAO_QUARTET_KUN_APPLICATION_PLAN_SYNTHESIS_COMPLETE_20260721T114246Z` |
| Tori/Hermes | Direct-source verification, correction discovery, final plan and HTML | This canonical plan and its verification record |
| Goru | Mechanical action/gate matrix and scratch-convergence advice | `GORU_KUN_APPLICATION_PLAN_INPUT_COMPLETE_20260721T114246Z` |
| Kun/Kimi K3 | Implementation phases, file groups, stop and separation rules | `KUN_QUARTET_APPLICATION_PLAN_INPUT_COMPLETE_20260721T114246Z` |
| Lana, adviser | Semantic/product-IA correction and risk review | `LANA_KUN_APPLICATION_PLAN_INPUT_COMPLETE_20260721T114246Z` |

### Executive verdict

**Overall: ADOPTED WITH ONE MATERIAL CORRECTION.**

Kun was right about:

- development/live divergence;
- the stale branch and mixed working tree;
- the risk of losing real untracked tests and artifacts;
- the Lab source-of-truth conflict;
- SQLite test-file and teardown hygiene;
- the need to keep risky actions behind separate approval gates;
- the overall `HEALTHY_WITH_RISKS` verdict.

The material correction is:

> Claim Ledger Contract v1 is not missing or waiting to be built. It is already `COMPLETE / PASS`. The real defect is that the completed packet and the canonical Baseline documents are untracked while the board still says the ledger is “next.”

Direct evidence:

- Contract packet: 36 files.
- Validation: `PASS`.
- Ledger entries: 16.
- Evidence spans: 45.
- Stance rows: 45.
- Source rows and unique bibcodes: 26 / 26.
- Wording checks and sentence bindings: 16 / 16.
- Errors: 0.
- Safety counters: all 0.
- Git-tracked files in the packet: 0.

**Therefore, rebuilding Contract v1 is rejected.** The first work is preservation and state reconciliation.

Standing rule established by this review:

> The board is a mirror, not the authority. When a board and a completed, validated receipt disagree, the receipt wins and the board must be reconciled.

---

## 2. Current verified baseline

| Surface | Verified state |
|---|---|
| Development branch | `feat/surveys-atlas-ia-p1-20260627` |
| Divergence | 6 commits ahead and 66 behind `origin/main` |
| Working tree | 20 modified and 360 untracked entries |
| Ahead commits | 4 Lab commits; 1 wiki-source fix; 1 Surveys Atlas IA commit |
| Served source of truth | Clean live mirror on `main`; recent Lab fixes #97–#101 |
| Contract v1 | Complete and valid, but all 36 files are untracked |
| Canonical Baseline docs | Roadmap and board are also untracked |
| Focused backend baseline | 21/21 tests passed in Tori’s independent rerun |
| Surveys baseline | Atlas IA smoke test passed |
| Test artifacts | 18 on-disk `test*.db` files found across repo/backend |
| FK cycle | `Evidence.consensus_scorecard_id → jury_scorecards.id` and `JuryScorecard.evidence_id → evidence.id` |
| Tool-suite debt | Four reported Gemini staleness-window failures and one overnight-marker failure; exact node IDs not yet censused |
| Secret-adjacent item | One untracked `.env.redacted-*` filename; contents never opened |

These counts are a snapshot. Every future execution packet must recount before acting and stop on unexplained drift.

---

## 3. Final action matrix

| # | Kun recommendation | Quartet ruling | Correct application |
|---|---|---|---|
| 1 | Decide the stale branch’s fate | **Adopt, modify, and resequence last** | Perform a read-only conflict census only after preservation, hygiene inventory, and the Lab IA decision. Decide the four Lab commits, wiki fix, and Surveys commit independently. Every git write remains user-gated. |
| 2 | Sweep worktree hygiene | **Adopt with strict guards** | Inventory every path into `KEEP-COMMIT`, `ARCHIVE`, `DELETE-CANDIDATE`, or `UNKNOWN`. `UNKNOWN` defaults to `KEEP`. Never bulk-move 360 files or stash all 20 modifications. Quarantine precedes deletion. |
| 3 | Build Claim Ledger Contract v1 | **Superseded and replaced** | Revalidate and preserve the completed packet; reconcile the stale board; then design the optional docs-only status/debate-map gate. Never rebuild or edit v1 in place. |
| 4 | Reconcile Lab divergence | **Adopt and elevate** | This is the first product decision. Lana advises on IA; Hwao ratifies. The decision must precede rebase/cherry-pick/branch-close mechanics. |
| 5 | Fix FK-cycle and test-DB hygiene | **Adopt with metadata caution** | First move file-backed SQLite tests to `tmp_path`/memory and add a warning regression test. Prefer fixture/drop-order repair before changing production model metadata. If metadata changes are necessary, prove migration invariance. |
| 6 | Resolve five pre-existing tool-test failures | **Defer pending census** | Goru records exact failing node IDs and time dependencies. Hwao then assigns fixes. `xfail` requires an expiring, evidence-linked review decision; broad `skip` is prohibited. Tori verifies receipts, not fixes. |
| 7 | Move/delete `.env.redacted-*` | **Fold into hygiene, preserve separate gate** | Classify by filename/stat only. Never open contents. Any move or deletion requires its own explicit user approval line. |

### New corrective actions

- **N1 — Preserve Contract v1:** hash manifest, validator rerun, independent Kun check, and out-of-repo backup.
- **N2 — Reconcile the Baseline board:** ledger complete; status/debate map next; retire the stale Contract-v1 approval text.
- **N3 — Isolate trust semantics:** the trust-cap change and its dedicated test become a small main-based candidate PR.
- **N4 — Salvage product work topically:** unrelated changes become separate review units, never one “save the dirty tree” commit.
- **N5 — Design the next research gate:** optional docs-only status/debate-map refinement from the 16 validated ledger entries.

### Explicitly rejected suggestions

- Bulk-moving all untracked files.
- Stashing all modified work before classification.
- Rebuilding Contract v1.
- Combining the docs-only ledger track with DB schema or migration work.
- Rebasing before the Lab IA decision.
- Treating test execution as a deploy/runtime approval.
- Using security scanners as proof that historical gates were respected.
- Reading the secret-adjacent file’s contents.
- Treating `model_canary.py` as part of the trust-cap unit; the diffs are independent.
- Claiming the five tool failures are quarantined before a census and decision exist.

---

## 4. Dependency map

```text
P0.1 recount and source verification
  └─ P0.2 validate + hash + backup Contract v1
      ├─ P0.3 reconcile Baseline board
      ├─ P1 worktree classification ───────────────┐
      ├─ P2 Lab IA decision ───────────────────────┼─ P3 branch fate
      └─ Parallel track P                          │
         ├─ P.A trust-cap candidate                │
         ├─ P.B next research-gate design          │
         └─ P.C tool-failure census                │
                                                   └─ P5 remaining salvage units
P0.2 also unlocks P4 test/infra hygiene on a fresh main-based branch.
```

Critical path:

`P0 preservation → P2 Lab IA decision → P3 branch fate`

No branch convergence occurs before the Lab IA decision. No cleanup disposition occurs before the complete classification ledger exists.

---

## 5. Phase 0 — Preserve truth first

**Owners:** Hwao coordinates; Goru performs mechanical checks; Kun independently verifies; Tori verifies receipts.

**Future artifact root:** `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase0/`

### Task P0.1 — Recount without writes

1. Record current branch.
2. Recount ahead/behind.
3. Recount modified/untracked entries.
4. Confirm Contract v1 has 36 files and zero tracked files.
5. Confirm roadmap and board remain untracked.

**Acceptance:** counts either match the baseline or every difference is explained in the receipt.

**Stop:** unexplained drift means re-inventory before any later phase.

### Task P0.2 — Revalidate immutable Contract v1

**Read-only source:** `docs/claim_ledger_contract_v1_agn_20260703T0830Z/`

1. Rerun the existing validator.
2. Require exactly `PASS`, 16 entries, 45 spans, 45 stance rows, 26 source rows, 26 unique bibcodes, 16 wording checks, 16 bindings, 0 errors, and all safety counters 0.
3. Compute a deterministic SHA-256 manifest for all 36 files.
4. Kun recomputes and compares the manifest independently.

**Create only after G2 approval:** `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase0/CONTRACT_V1_SHA256_MANIFEST.txt`

**Stop:** any mismatch or validator failure. Do not “repair” v1. Changes require a new v1.1 packet.

### Task P0.3 — Back up the completed packet

**Destination after G2 approval:** `/Users/duhokim/HermesOps/backups/claim-ledger-contract-v1-20260721T114246Z/`

1. Copy the packet while preserving relative paths and timestamps.
2. Compare source and backup manifests.
3. Record both roots and the matching digest in the phase receipt.

**Acceptance:** 36/36 files and every digest match.

### Task P0.4 — Reconcile the stale board

**Modify only after G1 approval:** `.hermes/board/paper-prose-distillation-board.md`

Required content changes:

- `Claim/status ledger` → complete with the existing completion marker.
- `Status/debate map` → next.
- Stale “claim ledger contract” approval text → retired.
- New KST timestamp and a fresh board-reconciliation marker.
- No prose, DB, product, or exact-diff authorization.

**Acceptance:** the board mirrors the validated receipt and contains no claim that Contract v1 is still waiting to be built.

### Task P0.5 — Decide the future preservation commit, but do not execute it

Record whether the immutable packet, roadmap, and reconciled board will be:

- committed on a fresh main-based docs branch; or
- preserved after branch convergence.

The Quartet recommends a **fresh main-based docs branch** because the canonical artifacts should not depend on the stale Surveys/Lab branch.

**Gate:** every branch/commit/PR/merge action is G3 and requires separate approval.

---

## 6. Phase 1 — Read-only worktree classification

**Owner:** Goru; Hwao ratifies; Kun spot-checks protected categories.

**Future outputs:** 

- `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase1/WORKTREE_CLASSIFICATION.md`
- `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase1/WORKTREE_CLASSIFICATION.json`

### Task P1.1 — Freeze classification rules

Buckets:

- `KEEP-COMMIT`: real code/tests/docs that need isolated review.
- `ARCHIVE`: useful receipts, reports, or snapshots that should move only after approval.
- `DELETE-CANDIDATE`: reproducible/generated debris with evidence.
- `UNKNOWN`: default `KEEP`; requires human/Hwao adjudication.

Protected patterns that can never be swept:

- `.hermes/handoffs/**`
- `.hermes/plans/**`
- `.hermes/board/**`
- `docs/**` research packets
- `backend/tests/**`
- Contract v1 and its validators/receipts

### Task P1.2 — Classify all 380 status entries

Likely candidates to inspect by filename and references:

- root `test_*.applescript` files;
- `click.js`, `find_deep.js`, `wait_and_extract.py`;
- `tmp_build_2929_trust_packet.py`, `goru_temp_report.json`;
- `main.py.bak-labrunner` and dashboard-renderer backups;
- 18 `test*.db` artifacts;
- the secret-adjacent redacted environment filename.

**Acceptance:** bucket totals reconcile to the fresh status count. Zero moves, deletes, stashes, commits, or content reads of `.env*` occur.

### Task P1.3 — Prepare separate disposition packets

Do not combine:

1. archive moves;
2. ordinary generated-file quarantine;
3. secret-adjacent filename handling;
4. product commits;
5. research/docs preservation.

Each future disposition packet must list exact paths, pre/post counts, rollback source, and its own approval boundary.

---

## 7. Phase 2 — Decide the Lab information architecture

**Owner:** Hwao ratifies; Lana advises on semantics/product IA; Goru inventories; Kun checks reproducibility.

**Future output:** `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase2/LAB_IA_AUTHORITY_DECISION.md`

### Inputs

Served/live Lab family includes files such as:

- `stageData.ts`
- `subnavVideos.ts`
- `DraftBoard.tsx`
- `FlagshipStudies.tsx`
- `FrontierDrafts.tsx`
- `PipelineBoard.tsx`

Development refactor includes:

- `LabStages.tsx`
- `frontiersData.ts`
- `LabTopTabs.tsx`

Also consider shipped fixes #97–#101 and the navigation-video plan grounded on live `stageData.ts`.

### Decision requirements

1. Name the authoritative IA and why.
2. List authoritative files.
3. List the losing tree’s reusable ideas versus obsolete code.
4. Map each of the four ahead Lab commits to `retain`, `rework`, or `abandon`.
5. State the impact on planned Lab videos.
6. Keep the clean live mirror read-only.

**Acceptance:** Hwao-ratified decision with no code or git write.

**Stop:** “rebase and see” is prohibited before this decision.

---

## 8. Parallel track P

Start only after P0.1 confirms the source state. Each lane remains independent.

### P.A — Trust semantics candidate

**Likely files:**

- `backend/app/services/trust_calculation.py`
- `backend/tests/test_trust_debate_stance_caps.py`

The `model_canary.py` token-budget change and `test_model_canary.py` are **not** part of this unit.

**Future sequence:**

1. Create a clean branch from current `origin/main` after G3 approval.
2. Write/confirm the focused semantic-cap tests.
3. Apply only the cap and audit-note behavior.
4. Run the dedicated test plus the existing trust suite relevant to the change.
5. Review for human-override precedence and freshness-floor ordering.

**Acceptance:** focused tests pass; diff contains only trust semantics and its tests; no unrelated model-canary or frontend changes.

### P.B — Design the next research gate

**Inputs:** the 16-entry completed ledger, stance matrix, wording checks, sentence bindings, roadmap Step 6, and relevant C1r/r3 vocabulary.

**Output:** `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase-p/STATUS_DEBATE_MAP_GATE_PROPOSAL.md`

The proposal must:

- derive the map from existing ledger entries;
- preserve counterevidence and debate axes;
- never regenerate or edit Contract v1;
- authorize no prose, product mutation, DB write, or publication;
- present a future docs-only gate for user review.

### P.C — Census the five tool-test failures

**Likely test files:**

- `tools/tests/test_gemini_app_usage.py`
- `tools/tests/test_gemini_app_autofetch.py`
- `tools/tests/test_ge_autopilot_dr_overnight_report.py`

**Output:** `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase-p/TOOL_TEST_FAILURE_CENSUS.md`

Record exact node IDs, failure text, clock/time-window dependence, first known receipt, and whether each failure still reproduces.

**No quarantine is presumed.** Hwao decides `fix`, `time-freeze fixture`, `temporary xfail with expiry`, or `cannot reproduce`. Broad skip is rejected.

### P.D — Model-canary reliability candidate

**Likely files:**

- `backend/app/services/model_canary.py`
- `backend/tests/test_model_canary.py`

This is separate from trust semantics. Its acceptance evidence must show the increased token budget is needed for visible Ollama healthcheck output and does not loosen health criteria.

---

## 9. Phase 3 — Decide branch fate

**Dependencies:** Phase 0 preservation evidence, Phase 1 inventory, and Phase 2 IA decision.

**Owners:** Hwao decides; Goru runs mechanics; Kun verifies; Tori verifies receipts.

**Future output:** `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase3/BRANCH_FATE_DECISION.md`

### Task P3.1 — Read-only conflict census

Use `git merge-tree` or a disposable clone. Never trial-merge in the active dirty checkout or clean live mirror.

Report conflicts by unit:

- four Lab commits: `01e8afa`, `586fef1`, `fd15e8e`, `826e733`;
- wiki-source fix: `e5ceda8`;
- Surveys Atlas IA: `ac0608c`;
- modified but uncommitted product units;
- canonical docs preservation.

### Task P3.2 — Decide each unit independently

Allowed decisions:

- reimplement against main;
- cherry-pick to a clean branch;
- retain as historical reference;
- abandon because main supersedes it.

A single all-or-nothing branch rebase is not the default.

### Task P3.3 — Execute only approved git packets

Each topical branch/PR needs:

- exact file list;
- focused tests;
- no unrelated hunks;
- proof that #97–#101 remain intact where applicable;
- separate merge approval.

**Acceptance:** recorded fate for every ahead commit and modified unit; convergence is understandable from `git log`; no live-mirror write.

---

## 10. Phase 4 — Test and database-file hygiene

**Branch:** fresh branch from `origin/main`, after G3 approval.

**Owners:** Goru implements; Kun checks reproducibility and migration invariance.

### Tests likely requiring fixture-path changes

At minimum, inspect every test using `sqlite:///./test_*.db`, including:

- `backend/tests/test_trust_debate_stance_caps.py`
- `backend/tests/test_global_paper_directory_api.py`
- `backend/tests/test_page_source_surface_fallbacks.py`
- `backend/tests/test_jury_trust_mutation.py`
- `backend/tests/test_promote_provisional_evidence_script.py`
- `backend/tests/test_trust_stage3c_prep.py`
- `backend/tests/test_pages_api_hardening.py`
- `backend/tests/test_paper_profile_api.py`
- `backend/tests/test_cross_page_paper_footprint_api.py`

### Task P4.1 — Add regression evidence

1. Run focused suites with SQLAlchemy warnings elevated to errors.
2. Prove current tests create repo-local DB files.
3. Add a regression check that the new fixture leaves no repo-local DB.

### Task P4.2 — Move SQLite fixtures to temporary paths

Prefer `tmp_path` or in-memory SQLite where semantics allow it. Centralize fixture helpers only if neighboring tests can share them without obscuring schema setup.

### Task P4.3 — Fix teardown warning at the narrowest layer

Concrete cycle:

- `backend/app/models/claim.py:61`
- `backend/app/models/jury.py:68`

Try in order:

1. fixture-scoped explicit table drop order;
2. a named/deferred constraint appropriate to both SQLite tests and PostgreSQL metadata;
3. `use_alter=True` only if tests prove it necessary.

### Task P4.4 — Prove migration invariance

Run Alembic metadata checks against a disposable database configuration. Any generated schema change is a stop condition unless separately designed and approved.

**Acceptance:** warning-free focused runs, no new repo-local test DBs, no migration drift, and no production DB contact.

---

## 11. Phase 5 — Remaining product salvage units

Each unit receives its own branch, tests, review, receipt, and git approval:

1. **Trust semantics** — P.A.
2. **Model-canary reliability** — P.D.
3. **Pages/source APIs** — `backend/app/routers/pages.py` plus four paper/source API tests; keep frontend consumption review separate if the API contract changes.
4. **Wiki source presentation** — `WikiPageClient.tsx` and only its required API coupling.
5. **Surveys Atlas IA** — `ac0608c`, Surveys components, detail client, and smoke script.
6. **Ideas/home/navigation changes** — separate from Surveys unless a shared contract proves inseparable.
7. **Lab IA** — only what Phase 2 ratifies.
8. **Lab-runner literature grounding** — `tools/lab_runner_worker.py` and `tools/nm_fulltext_layer.py`; acceptance must expose when fail-open grounding did not run.
9. **Baseline docs preservation** — immutable packet/roadmap/board only.
10. **Test hygiene** — Phase 4 only.

Never combine product code, test debris deletion, research packet preservation, and branch cleanup in one commit.

---

## 12. Future validation commands and evidence

These are definitions for future approved packets. They were not executed while writing this plan.

### State recount

```bash
git branch --show-current
git rev-list --count origin/main..HEAD
git rev-list --count HEAD..origin/main
git status --short
```

Expected baseline: feature branch, 6 ahead, 66 behind, 20 modified, 360 untracked. Drift must be explained, not forced back to these numbers.

### Contract file count and tracked status

Use `search_files(target="files", pattern="*", path="docs/claim_ledger_contract_v1_agn_20260703T0830Z")` and a Python `Path.rglob()` count. Expected: 36 files. Then:

```bash
git ls-files docs/claim_ledger_contract_v1_agn_20260703T0830Z/
```

Expected before preservation: no output.

### Contract validator

```bash
backend/.venv/bin/python docs/claim_ledger_contract_v1_agn_20260703T0830Z/validation/validate_contract.py
```

Expected: `PASS`; counts `16/45/45/26/26/16/16`; `errors=[]`; all safety counters 0.

### Contract manifest algorithm

Use Python `pathlib` + `hashlib.sha256`, sort by repo-relative POSIX path, hash file bytes, and write one `<digest><two spaces><relative-path>` row per file through the guarded file tool. The manifest must include 36 rows and be independently recomputed by Kun.

### Trust semantics

```bash
cd backend
.venv/bin/python -m pytest -q tests/test_trust_debate_stance_caps.py
```

Also rerun neighboring trust tests selected during the clean-branch preflight. Do not use `test_model_canary.py` as evidence for trust semantics.

### Model canary

```bash
cd backend
.venv/bin/python -m pytest -q tests/test_model_canary.py
```

### Pages/source API baseline

```bash
cd backend
.venv/bin/python -m pytest -q \
  tests/test_cross_page_paper_footprint_api.py \
  tests/test_global_paper_directory_api.py \
  tests/test_page_source_surface_fallbacks.py \
  tests/test_paper_profile_api.py
```

Expected current baseline: 16 passed.

### Surveys baseline

```bash
cd frontend
node scripts/test-surveys-atlas-ia.mjs
```

Expected: `surveys atlas IA smoke checks passed`.

### Tool-failure census

Run only the three named tool-test files first. Capture exact node IDs and full failure reasons. Do not convert failures to skips during census.

### Board reconciliation

Use `search_files` to require:

- completion marker present;
- `Claim/status ledger` marked complete;
- `Status/debate map` marked next;
- stale Contract-v1 approval phrase absent.

---

## 13. Approval ledger

Every gate is separate; none is granted by this plan.

| Gate | Scope | Current state |
|---|---|---|
| G1 | Baseline board docs-only reconciliation | Held |
| G2 | Contract hash manifest and out-of-repo backup writes | Held |
| G3 | Any branch, commit, rebase, cherry-pick, PR, push, or merge | Held |
| G4a | Ordinary archive/quarantine moves | Held |
| G4b | Deletion after quarantine/dwell | Held |
| G4c | Secret-adjacent filename move/delete | Held separately; contents remain unread |
| G5 | DB/SQL/migration or production data action | Closed; not proposed |
| G6 | Optional status/debate-map docs-only run | Held pending proposal |
| G7 | Runtime/deploy/restart/publication/cockpit changes | Closed; not proposed |

Tests are not deployments. Future test packets may run under normal lane rules, but must use disposable paths and may not contact production services or data.

---

## 14. Stop rules

Stop and escalate if:

- Contract v1 validation or hashes differ from the completed receipt.
- Any action would edit Contract v1 in place rather than create a new version.
- A protected file enters `DELETE-CANDIDATE`.
- A cleanup action is proposed without a complete path list and rollback source.
- `.env*` contents would be opened or printed.
- A Lab merge/rebase is proposed before the IA decision.
- A topical change drags unrelated hunks.
- Test-hygiene changes produce Alembic/schema drift.
- A “pre-existing” test failure changes shape or cannot be tied to evidence.
- The live mirror would be written during planning, conflict testing, or salvage.
- Any DB, product, deployment, publication, cockpit, cron, billing, or git action lacks its explicit gate.

---

## 15. Out of scope and result of this run

This run performed planning and verification only.

It did not perform:

- Contract regeneration or board reconciliation;
- test execution beyond the previously reported baseline;
- file cleanup, movement, quarantine, or deletion;
- secret inspection;
- branch creation, commit, rebase, cherry-pick, PR, push, or merge;
- DB/SQL/migration work;
- runtime, deployment, restart, publication, cockpit, browser, network, cron, or billing changes.

The only repo artifacts produced by this run are this canonical plan and its standalone HTML report. The separately served HTML copy is a tailnet-only report artifact, not a product deployment.

`HWAO_QUARTET_KUN_APPLICATION_PLAN_SYNTHESIS_COMPLETE_20260721T114246Z`

`QUARTET_KUN_REPORT_APPLICATION_PLAN_COMPLETE_20260721T114246Z`
