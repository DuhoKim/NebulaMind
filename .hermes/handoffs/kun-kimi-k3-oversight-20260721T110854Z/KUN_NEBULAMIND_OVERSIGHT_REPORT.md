# KUN NEBULAMIND OVERSIGHT REPORT — 2026-07-21

Task ID: `kun-kimi-k3-oversight-20260721T110854Z`
Coordinator: Hwao/Fable
Reviewer: Kun on Hermes via Nous Portal route `moonshotai/kimi-k3`
Date: 2026-07-21

KUN_KIMI_K3_NEBULAMIND_OVERSIGHT_COMPLETE_20260721T110854Z

---

## 1. Executive verdict

`HEALTHY_WITH_RISKS`

NebulaMind is an active, multi-surface AI-built astronomy wiki and research lab with a coherent canonical doctrine (ledger-primary paper distillation), a working FastAPI+Next.js product, a live public mirror, and an unusually disciplined handoff/receipt culture. Focused tests executed in this pass all passed. The principal risks are (a) a heavily dirty working tree with 20 modified and ~360 untracked files mixing product code, experiments, and junk; (b) the working branch (`feat/surveys-atlas-ia-p1-20260627`) is 6 commits ahead of and 66 commits behind `origin/main`, while the separately cloned live mirror `NebulaMind-origin-main-live` sits clean on `main` — meaning the development checkout and the served product are meaningfully diverged and the development branch is stale relative to its own origin; and (c) the canonical Baseline (paper→ledger→map→prose) pipeline remains in pre-implementation/docs-only state with DB/prose gates correctly held, so the flagship research mission has not yet crossed into verified production execution. No safety-gate violations were observed; receipts show gates being respected.

## 2. What NebulaMind currently is

Verified from `README.md`, `wiki_schema.md`, backend/frontend layout, and live handoffs:

- **Product:** An astronomy wiki ("AstroBotPedia") built and maintained by AI agents. FastAPI backend (port 8000, ~35 routers: pages, claims, jury, council, edits, wiki, surveys, lab_runner, qa, graph, etc.), Next.js frontend (port 3000: wiki, surveys, ideas, lab, council, explore, agents, benchmark, news, calendar, directory), PostgreSQL+Redis, Celery agent loop, and an MCP server exposing the knowledge base to external AI clients. Agent governance: editors propose `EditProposal`s, reviewers vote (≥3 approvals auto-apply), jury tasks review evidence stances, everything versioned in `PageVersion`.
- **Research mission ("The Baseline"):** Turn large volumes of published papers into trustworthy prose without losing scope, uncertainty, contradiction, or provenance. Canonical primitive (`.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md`, board `paper-prose-distillation-board.md`): `papers -> claim/status ledger -> research-status/debate map -> prose -> derived claims/evidence/trust`. Invariants: ledger-primary; every prose sentence binds to a ledger entry; prose modality never exceeds ledger certainty; evidence-hunting to rescue overbroad claims is forbidden by name.
- **Lab surface:** A public "Lab" (galaxy-evolution autonomous research) with Topic/Data/Methods/Paper stage navigation, an autonomous lab runner (`tools/lab_runner_worker.py`, Ollama-based drafting with NASA ADS/arXiv full-text literature grounding added in the working tree), and a companion YouTube explainer program (V8 public clips shipped 2026-07-21 per `YOUTUBE_V8_PUBLIC_V6_UNLISTED_CLEAN_LINEUP_20260721.md`; three more stage-overview videos planned in `nav-video-expansion-20260721`).
- **Operations culture:** Hwao/Fable coordinates; Tori/Hermes relays and verifies receipts; Lana (high-reasoning), Goru (mechanical), Kun (implementation/reproducibility oversight) lanes; durable markdown handoffs under `.hermes/handoffs/` (52 directories/files) and board protocol under `.hermes/board/`; tmux-pane based execution; strict explicit-approval gates for DB writes, deploys, git writes, publication, browser/cloud/cron/billing actions.

## 3. What is working well

- **Gate discipline is real, not decorative.** Multiple 2026-07-21 receipts show bounded execution with explicit user authorization recorded before action: `TORI_ANTIGRAVITY_QUOTA_EXPERIMENT_USER_AUTHORIZED_20260721T103613Z.md` documents a quota probe with pre-stated stop conditions, verified before/after readings, and an honestly reported parser defect it exposed (plus the focused TDD fix: 14 focused tests pass, broader sets itemized with pre-existing failures separated from new ones). `MACBOOK_COMPUTER_USE_VERIFIED_20260721.md` records an installation with exact verification evidence (doctor JSON ok, screenshot hash) and an honest note about a Hermes/CuaDriver version formatting mismatch with a workaround.
- **Trust semantics being hardened with tests.** Working tree adds `_apply_debate_stance_semantic_cap` in `backend/app/services/trust_calculation.py`: claims marked `mixed_debated` or `model_bounded` can no longer render as `accepted`/`consensus` merely because attached evidence is currently supportive; human locked overrides still win. The new `backend/tests/test_trust_debate_stance_caps.py` plus `test_model_canary.py` pass (5 passed, run in this pass). This is exactly the Baseline invariant "prose/status modality may not exceed evidence certainty" being enforced in code.
- **Focused test suites pass.** In this pass: 5/5 trust-cap+canary tests, 16/16 paper-API tests (cross-page footprint, global paper directory, page source surface fallbacks, paper profile), 8/8 source-surface fallback tests (separate run), and the frontend `scripts/test-surveys-atlas-ia.mjs` smoke checks passed.
- **The live mirror is clean and current on `main`.** `NebulaMind-origin-main-live` is on `main`, zero dirty files, tip `28e8735 fix(lab): eliminate SSR hydration error on the Lab page (#101)` — a steady cadence of numbered, reviewed lab-page fixes (#97–#101).
- **Video/explainer program shipped with receipts.** Public V8 female-voice replacements for Embedding/Clustering/Activity-Overlay/Ranking are live with exact YouTube IDs recorded; V6 duplicates preserved unlisted, not deleted — a conservative, reversible publication pattern.
- **Research pipeline design is genuinely conservative.** The decomposed galaxy-research pipeline plan (2026-07-12) replaces one-shot Deep Research prompts with per-simulation atomic evidence units, deterministic assembly, fail-closed validators, and "assembler must never invent/paraphrase/repair — emit blocked report instead." Sealed C1r artifacts are hash-pinned and immutable.

## 4. Top risks/blockers, ordered by severity

1. **Development/live divergence and branch staleness (high).** Working branch is 6 ahead / 66 behind `origin/main`. The lab frontend files differ substantially between the two checkouts (live has `DraftBoard.tsx`, `FlagshipStudies.tsx`, `FrontierDrafts.tsx`, `PipelineBoard.tsx`, `stageData.ts`, `subnavVideos.ts`, etc., that the dev checkout lacks; dev has refactored `LabStages.tsx`/`frontiersData.ts`/`LabTopTabs.tsx` not on main). Meanwhile recent dev commits refactor the same Lab surface ("dissolve frontier map into Topic tab"). Risk: an eventual merge/rebase of a month-old surveys branch onto a fast-moving main will be painful and error-prone; the nav-video plan itself was grounded against the *live* checkout's `stageData.ts`, not the dev tree.
2. **Dirty-worktree entropy (high).** 20 modified + ~360 untracked files in the dev checkout, including stray root-level artifacts (`click.js`, many `test_*.applescript`, `wait_and_extract.py`, `find_deep.js`, root-level `test*.db` files, `goru_temp_report.json`, `tmp_build_2929_trust_packet.py`), backup files (`main.py.bak-labrunner`, 8 timestamped `.bak` copies of `render_ge_autopilot_dashboard_v2.py`), and an untracked `backend/.env.redacted-before-disable-gemini-20260708_174609` (redacted, but secret-adjacent clutter). Untracked new backend tests (6 files) are real work at risk of loss. Mixed concerns in one tree make any future commit risky and dilute reviewability.
3. **Baseline pipeline not yet implemented (medium-high).** The canonical paper→ledger→map→prose pipeline is in "pre-implementation review patched" state since 2026-07-03; board shows Claim/status ledger as "next", debate map and prose preview blocked behind it, exact-diff/product change locked. Correctly gated, but the flagship mission is ~3 weeks stalled at the same stage; the risk is drift between doctrine and the code that actually ships (the trust-cap fix is good, but it patches the *production* trust calculator, not the Baseline ledger that does not yet exist).
4. **SQLite test-DB hygiene (medium).** Tests create on-disk SQLite files (`test_*.db`) at repo root and backend root; a pre-existing SQLAlchemy FK-cycle warning (`evidence`, `jury_scorecards` drop-order) appears in test output. Cosmetic now, but it means test schema teardown is not clean and test DBs pollute the tree.
5. **Known pre-existing test failures acknowledged in receipts (low-medium).** The Tori quota receipt honestly notes 4 unrelated pre-existing Gemini-consumer staleness-window failures and 1 stale overnight-marker failure in broader tool test sets. Not regressions, but they are unfixed red in the broader suite.
6. **Python toolchain mismatch (low).** System `python3` is 3.9.6 while `python`/pip map to 3.11; backend `.venv` is 3.11 and works. Anyone following README setup casually can land on the wrong interpreter.

## 5. Architecture and source-of-truth map

- **Product runtime:** `backend/app` (FastAPI: routers/, services/, models/, agent_loop/) ← PostgreSQL+Redis ← Celery workers; `frontend/src/app` (Next.js App Router); `mcp/` MCP server pointed at the live API.
- **Served product:** `NebulaMind-origin-main-live` (clean clone of `origin/main`, tip #101). The dev checkout `NebulaMind/NebulaMind` is the working tree on `feat/surveys-atlas-ia-p1-20260627`. These are two distinct checkouts of the same repo, currently diverged both directions.
- **Research doctrine:** `.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md` (canonical Baseline) + `.hermes/board/paper-prose-distillation-board.md` (stage state). Supporting pipeline plans: `2026-07-12_075713-galaxy-research-decomposed-pipeline.md` (offline, deterministic, fail-closed).
- **Trust implementation:** `backend/app/services/trust_calculation.py` (`recalculate_trust_v2`: numeric scoring → bucket → debate-stance semantic cap → freshness floor → human override), `trust_mutation.py`, `sentence_trust.py`, jury services; tests under `backend/tests/`.
- **Lab pipeline:** `tools/lab_runner_worker.py` (autonomous runner; working tree adds `lit_context` grounding via `tools/nm_fulltext_layer.py` against NASA ADS + arXiv full text, non-fatal fallback), `tools/galaxy_evolution_autopilot.py`, dashboard renderers.
- **Coordination:** `.hermes/board/communication-protocol.md` (Hermes Kanban canonical; repo-local markdown durable handoffs), `.hermes/handoffs/` receipts.
- **Cockpit/dashboard:** stable-cockpit renderer + guard in `tools/`, protected markers, Tori-owned GE dashboard; per `.hermes.md`, public cockpit writes are Hwao-gated (not inspected in depth this pass).

## 6. Evidence/trust assessment

- **Doctrine:** Ledger-primary, sentence-binding, modality-capped-by-certainty, no evidence-hunting. Coherent and unusually well-specified (enum registry, stance matrix, wording contract, countercase quota all enumerated pre-implementation).
- **Enforcement in code:** The new debate-stance semantic cap closes a real leak where supportive-only evidence could visually promote a deliberately-scoped claim to `accepted`/`consensus`. Verified by reading the diff and running its tests.
- **Provenance in research runner:** The working-tree `lit_context` addition grounds drafts in retrieved ADS/arXiv passages with [Key] citation tags and explicitly forbids copying literature numbers into the Result paragraph (result may state only the single given measurement). Fail-open by design (non-fatal skip) — reasonable for drafting, but it means lit grounding is not guaranteed; downstream review must not assume it ran.
- **Receipt culture:** Handoffs consistently carry markers, exact commands, counts, hashes, and honest "pre-existing failure" separation. This is the strongest trust signal in the project.
- **Gap:** The Baseline ledger schema exists on paper only; there is no machine-checked ledger artifact in production yet, so "every prose sentence binds to the ledger" is currently aspirational for new prose.

## 7. Engineering/reproducibility assessment

- **Tests run this pass (all green):**
  - `backend`: `pytest tests/test_trust_debate_stance_caps.py tests/test_model_canary.py` → 5 passed.
  - `backend`: `pytest tests/test_cross_page_paper_footprint_api.py tests/test_global_paper_directory_api.py tests/test_page_source_surface_fallbacks.py tests/test_paper_profile_api.py` → 16 passed.
  - `backend`: `pytest tests/test_page_source_surface_fallbacks.py` (rerun) → 8 passed.
  - `frontend`: `node scripts/test-surveys-atlas-ia.mjs` → "surveys atlas IA smoke checks passed".
- **Not run (out of scope/time):** full backend suite, frontend `next build`/lint, migrations, live API checks. Receipts indicate broader tool suites have 4+1 known pre-existing failures.
- **Reproducibility concerns:** dirty tree + untracked tests + `.bak` proliferation + on-disk test DBs mean the exact state that produced current behavior is not fully reconstructible from git alone; the live mirror is the only clean reproducible anchor. Test FK-cycle SAWarning on teardown should be fixed (`use_alter=True` or sorted drop) before it masks a real problem.
- **Commit cadence on main is healthy** (numbered PRs #20–#101 visible in history), but the dev branch has not been rebased in ~3+ weeks while main moved 66 commits.

## 8. Operational/safety-gate assessment

- **No gate violations observed.** Every 2026-07-21 side-effecting action found (quota experiment, computer-use install, monitor restart, YouTube publication) carries a user-authorization record, pre-stated boundaries, stop conditions, and post-hoc verification. The quota receipt's monitor restart was separately approved, PID-backed-up, single-pane-scoped.
- **Kun's own constraints held:** this pass was read-only except the sole report path; no git writes, no process actions, no secrets inspection (`.env*` files were listed but never opened), no subagents.
- **Board hygiene:** `.hermes.md` Hwao-led roles are being followed; cockpit preservation rules documented with protected markers; communication protocol designates Kanban + repo markdown, Obsidian retired due TCC.
- **Watch item:** the untracked `backend/.env.redacted-...` file is redacted by name but should be moved out of the repo tree or deleted to keep the secret-adjacent surface at zero.

## 9. Prioritized next actions (owner / action / expected evidence / gate)

1. **Hwao + user — Decide the fate of `feat/surveys-atlas-ia-p1-20260627`.** Either rebase/merge the 6 ahead commits onto current `origin/main` (66 behind) and open a PR, or deliberately shelve the branch. Evidence: a clean merge plan or a recorded close decision; `git log` showing convergence. Gate: user approval for any git write.
2. **Hwao/Goru — Worktree hygiene sweep (mechanical, read-only inventory first).** Classify the ~360 untracked files into keep (commit candidates like the 6 new backend tests), archive (docs/ handoff HTML), and delete (root `test_*.applescript`, `click.js`, stray `test*.db`, `tmp_*.py`, `.bak` files). Evidence: inventory report + reduced `git status` count. Gate: user approval before any deletion/commit.
3. **Lana + Hwao — Unblock the Baseline Claim Ledger Contract v1 (the "next" stage since 2026-07-03).** Produce the docs-only ledger contract per the roadmap, then the first machine-checkable ledger JSONL for the 26 AGN papers. Evidence: contract doc + validating JSONL + Goru schema check receipt. Gate: existing docs-only gate; DB write remains separately gated.
4. **Kun/Lana — Reconcile the Lab frontend divergence deliberately.** The nav-video plan and live site use live-tree `stageData.ts`; the dev tree refactored the same surface. Decide which tree is authoritative for Lab going forward before more parallel edits. Evidence: a recorded decision + single-source file list. Gate: Hwao decision.
5. **Goru — Fix the test-teardown FK cycle warning** (`evidence`/`jury_scorecards` drop order) and stop tests from writing `test_*.db` into repo roots (tmp-path fixtures). Evidence: warning-free focused runs; `git status` clean of test DBs. Gate: normal code review.
6. **Tori — Track down the 5 known pre-existing tool-test failures** (4 Gemini-consumer staleness-window, 1 stale overnight-marker) and either fix or formally quarantine them. Evidence: green broader suite or quarantine notes. Gate: none (read-only/tests).
7. **Hwao — Move or delete `backend/.env.redacted-before-disable-gemini-20260708_174609`** out of the repo tree. Evidence: file absent from `git status`. Gate: user approval (secret-adjacent).

## 10. Evidence ledger — what was actually inspected

Commands (read-only):
- `git status --short` (380 lines; counted 20 modified / ~360 untracked), `git log --oneline -15`, `git branch --show-current` → `feat/surveys-atlas-ia-p1-20260627`
- `git log HEAD..origin/main | wc -l` → 66; `git log origin/main..HEAD | wc -l` → 6
- `git diff --stat` (20 files, +1381/-153); `git diff` on `backend/app/services/trust_calculation.py`, `tools/lab_runner_worker.py`, `wiki_schema.md`
- In `NebulaMind-origin-main-live`: `git branch` → main; `git status` → 0 dirty; `git log -5` → tip 28e8735 (#101); `diff -rq frontend/src` vs dev tree
- `backend/.venv/bin/python -m pytest tests/test_trust_debate_stance_caps.py tests/test_model_canary.py -q` → 5 passed
- `pytest tests/test_cross_page_paper_footprint_api.py tests/test_global_paper_directory_api.py tests/test_page_source_surface_fallbacks.py tests/test_paper_profile_api.py -q` → 16 passed; rerun of fallbacks → 8 passed
- `frontend: node scripts/test-surveys-atlas-ia.mjs` → passed

Files read (content, not just names):
- `.hermes.md` (operating contract), `README.md`, `wiki_schema.md`
- `.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md` (Baseline, first 50 lines)
- `.hermes/plans/2026-07-12_075713-galaxy-research-decomposed-pipeline.md` (first 100 lines)
- `.hermes/board/paper-prose-distillation-board.md`, `.hermes/board/communication-protocol.md`
- `.hermes/handoffs/TORI_ANTIGRAVITY_QUOTA_EXPERIMENT_USER_AUTHORIZED_20260721T103613Z.md`
- `.hermes/handoffs/MACBOOK_COMPUTER_USE_VERIFIED_20260721.md`
- `.hermes/handoffs/YOUTUBE_V8_PUBLIC_V6_UNLISTED_CLEAN_LINEUP_20260721.md`
- `.hermes/handoffs/nav-video-expansion-20260721/HWAO_VIDEO_EXPANSION_PLAN.md` (first 50 lines)
- `.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/` brief/report headers
- `backend/tests/test_trust_debate_stance_caps.py` (first 60 lines)
- Directory listings: repo root, `backend/`, `backend/app/{routers,services}`, `frontend/`, `frontend/src/app`, `.hermes/{board,plans,handoffs,state,agents}`, tools/

## 11. Uncertainties and what Kun deliberately did not inspect

- **Not inspected:** any `.env`/credential/token content (excluded by brief); the live public cockpit HTML/JSON (content verified only indirectly via the Tori receipt); the production database; running processes/tmux panes; the MCP server's live behavior; `autowiki/`, `cloudflare/`, `playwright_test/`, `memory/`, `logs/`; full backend test suite and frontend production build (time-boxed; only focused suites run).
- **Unknowns:** whether the public site is actually serving the live mirror's tip right now (no HTTP probe was permitted/needed); the true state of the Celery agent loop in production; whether the 6-ahead branch commits are already partially duplicated on main; current ADS/API quota states; the content of `.claude/` (untracked, not opened).
- **Inference vs fact:** "branch is stale and merge will be painful" is inference from ahead/behind counts and file-level diffs, not from an attempted merge. "Baseline is stalled" is inference from board timestamps (2026-07-03) vs today (2026-07-21); there may be off-repo progress Kun did not see.

## 12. Model/route note

This oversight pass was executed on the requested route: **Nous Portal / moonshotai/kimi-k3**. No claims are made about which billing bucket, quota pool, or subscription backed the route beyond that.

---

KUN_KIMI_K3_NEBULAMIND_OVERSIGHT_COMPLETE_20260721T110854Z
