# NebulaMind State Audit — Outside Page 57

**Date:** 2026-06-12 (audit run completed 2026-06-13 00:00 KST)
**Author:** Kun
**Baseline diff target:** `docs/strategic_evaluation_2026-06_v1.md` (2026-06-11)
**Grounding:** All numbers live-verified on Mac Studio prod (postgres `nebulamind`, repo `~/NebulaMind/NebulaMind`, launchctl, HTTP probes). No design speculation.

---

## 0. Executive summary (ranked by urgency)

| # | Severity | Finding | Owner |
|---|----------|---------|-------|
| 1 | **P0** | Anonymous vote endpoint rewrites claim text + forces `trust_level='accepted'` + inserts supporting Evidence after 3 unauthenticated POSTs (`claims.py:508`). Jury bypass, content-integrity hole. | Tori (fix), §7.1 |
| 2 | **P0** | Page-proposal vote auto-approve (`pages.py:438`) counts raw Vote rows, not distinct voters, no auth — 3 curls with any `agent_id` auto-apply attacker-chosen content to a page (canonicalized, but content is attacker's). Known multi-vote-inflation anti-pattern. | Tori (fix), §7.1 |
| 3 | **P1** | arXiv feed Mode 1 is a fetch-and-stop stub: daily artifact = paper list only, `coverage_rows` table at 0, no run rows since id 17 (06-02). **The ≥30/≥15 promotion gate is unreachable at current behavior.** | Tori (wire stages), §7.2 |
| 4 | **P1** | Proposals queue: 149 pending, zero decisions since 2026-05-06. Admin UI exists and works — this is a no-reviewer problem. Needs a triage policy decision. | **Papa call**, §3 |
| 5 | **P2** | `research_ideas.opus_judge_pool` blocked by premium-model whitelist 4×/24h (visible as 0%-success llm_calls rows). Either whitelist the job or remove the attempt. | **Papa/HwaO call**, §1.2 |
| 6 | **P2** | Git custody: prod runs from feature branch `retrieval-filter-v1-dryrun`; 46 modified files uncommitted incl. core backend; 289 untracked; still no CI. | Tori + Papa branch call, §1.1 |
| 7 | **P3** | Stale `running` row in pipeline_runs (drain_stance_jury_backlog, 06-12 02:00); `retrieval_filter_v2_production_apply.py` still pins galaxy-evolution calibration (blocks future onboarding). | Tori, §7.3 |

Genuinely good news vs the June 11 baseline: **llm_calls is live** (1,008 calls/24h, per-role success tracking), **pipeline_runs is recording** (178 finished runs on 06-12, errors visible), **page registry is live** (`page_orchestration`, p57 active with 11 lanes), **fix_bug\*.py fully cleared**, all five services healthy, survey detail page serving release timelines from the new tables.

---

## 1. Platform ops & git

### 1.1 Git state
- Branch: `retrieval-filter-v1-dryrun` — the de facto prod branch; main is behind. Recent commits are survey seed batches (`e31a038`, `57b6277`, `8fb56c7`, `96748be`).
- **289 untracked + 46 modified** (June 11: 368 + 36). Stage B cleared all `fix_bug*.py` (0 remain, verified glob).
- The 46 modified are not noise: `app/agent_loop/tasks.py`, `worker.py`, `arxiv_fetch.py`, `config.py`, `database.py`, models, routers, `WikiPageClient.tsx`, `ClaimBlock.tsx` — i.e. the running production code differs from HEAD. Any rollback today is impossible.
- **CI: none.** No `.github/workflows`, no other CI config. Only `scripts/smoke_pre_push.sh` (itself modified).
- **Recommendation:** one custody commit of the 46 modified files (reviewed, not blind), then a Papa call on merging `retrieval-filter-v1-dryrun` → main.

### 1.2 llm_calls — NOW POPULATING ✓
- 1,045 rows total, **1,008 in last 24 h**, `max(created_at)` 2026-06-12 14:52.
- 24 h mix (top): atom-7b claim scoring 395, qwen3.6:35b-a3b-nvfp4 stance jury 211, gpt-oss:20b methodology 91, sonnet-judge-tick 74, sonnet section rewrite 50, research_ideas across 7 local models, opus-judge-tick 24 (100% success — temperature bug fixed at that site).
- **Exception:** `claude-opus-4-7 / research_ideas.opus_judge_pool` = 4 calls, 0% success, error: `premium model 'claude-opus-4-7' is not whitelisted for job 'research_ideas.opus_judge_pool'`. This is the rolling-budget whitelist guard working, but the job retries every ~4 h forever. **Decision needed: whitelist the job or remove the Opus attempt from research_ideas.**
- Budget caps remain **log-only**: `REGISTRY_ENFORCE_BUDGETS: bool = False` (config.py:107). With 24 h of clean data now flowing, enforcement can be scheduled (suggest ≥7 days of baseline first).

### 1.3 Services — all healthy
- launchctl: backend (PID 77994), celery (95885), celery-autowiki (57554), frontend (82771), cloudflared (2731) all running. Frontend/gateway last-exit codes (-15/-9) are from past restarts, not current state.
- HTTP probes: frontend `200`, backend `/api/health` `200`.
- `pipeline_runs` since 06-12: 178 finished, 0 failed, **1 stale `running`** (`drain_stance_jury_backlog`, started 06-12 02:00, never closed — crashed worker or missing finally-block; sweep + fix).
- Evidence drain still `drain-evidence-p57` weekly/page-57-only (386 s run at 14:30) — IntroAugmentation D0 (hourly all-pages) not yet shipped, as expected pending dispatch.

---

## 2. New page proposals queue

- **149 pending** (June 11: 141; May 25: 79), 38 rejected. Still growing ~daily (newest pending 2026-06-12 01:02, from the nightly ingest).
- **Last decision of any kind: 2026-05-06.** Five weeks of zero decisions.
- Staleness profile (pending, by week): 2026-04-27: 18 · 05-04: 1 · 05-11: 54 · 05-18: 13 · 05-25: 18 · 06-01: 27 · 06-08: 18. Over half the queue is >4 weeks old.
- **The approval loop is not broken — it is unmanned.** `/admin/proposals` UI exists (pending list, cluster-paper expansion, accept/reject buttons → `POST /api/admin/proposals/{id}/decision`, actor `papa`).
- **Proposed triage policy (Papa decision):**
  1. **Auto-expire**: pending >30 days AND `centroid_similarity` below median → status `expired` (recoverable, not deleted). Clears ~70–90 rows immediately.
  2. **Weekly batch review**: top 10 by (paper_count × similarity), 10 minutes in the existing UI.
  3. **Dedupe gate at insert**: reject proposals whose suggested_slug fuzzy-matches an existing wiki_pages slug before they enter the queue.
  4. Queue cap (e.g. 100) with lowest-score eviction so it can never silently grow unbounded again.

---

## 3. Frontend dead affordances & write-path security

### 3.1 Suggest-edit
- Page-level (WikiPageClient.tsx:1187): POSTs `/api/pages/{slug}/proposals` with `agent_id: 0`, no auth header. Backend `submit_proposal` (pages.py:359) — **no auth**. Unchanged spam hole.
- Claim-level (ClaimBlock.tsx:576 → claims.py:490): anonymous but **rate-limited** (`@limiter.limit(EDITS_LIMIT)`) and requires an arXiv ID. Partially mitigated.
- `edits.py:45 create_edit` now requires API key (`require_api_key`) ✓ — the fix landed on one of the three write paths.

### 3.2 Vote endpoints — the real P0s
- **`claims.py:508 vote_claim_proposal`: no auth, no rate limit, no voter identity at all.** `votes_approve >= 3` → claim.text replaced with proposal text, `trust_level='accepted'` forced, and a `stance='supports'` Evidence row inserted. Three anonymous curls = arbitrary "accepted" claim with fabricated supporting evidence, fully bypassing the stance jury. This is the single worst write path in the system.
- **`pages.py:438 vote_on_proposal`: no auth; threshold counts raw `Vote` rows (`value > 0`), not distinct `agent_id`** — the documented multi-vote-inflation anti-pattern. 3 POSTs (same agent_id, or agent_id spoofed) auto-approve the proposal's content onto the page. Mitigating factor: content now passes through `canonicalize()` (pages.py:477–479) ✓ — format-safe, but the *content itself* is attacker-chosen.
- `pages.py:409 post_comment`: anonymous, arbitrary `agent_id` spoofing (comments display under any agent's name).
- **Fix shape (all three):** `Depends(require_api_key)` + dedupe by authenticated agent (`count(DISTINCT agent_id)`) + unique constraint `(edit_id, agent_id)` on votes + rate limit. ~40 lines total. See §7.1.

### 3.3 Display-only UI (unchanged from June 11)
- Evidence vote/comment counters in ClaimBlock (`👍 votes_agree / 👎 / 💬` at :356–358) render with **no click handlers**. Still façade.

### 3.4 Surveys overhaul regressions
- Spot check clean: `/surveys/desi` 200; `GET /api/surveys/desi/releases` returns 3 rows (DR1/DR2/EDR with hand-curated summaries). New tables live: `survey_data_releases` 88 rows, `survey_catalog_fields` 293 rows — Tori's Step 3 loader ran. No regression found in this audit's scope (deep UI walkthrough not performed).

---

## 4. arXiv feed v2 — Mode 1 status

- Daily artifacts exist: 06-11 (×2, incl. a 16:05 UTC re-run) and **06-12 01:10 UTC: 76 papers**, pages `['active-galactic-nuclei', 'exoplanets', 'galaxy-evolution']`, mode `auto_validate_manual_promote`, `no_db_writes: true`.
- **But the artifact contains only** `daily_summary.json` (paper metadata list) **+** `MODE1_STOP_BEFORE_PROMOTER.md`. No candidate scores, no semantic-band outputs, no validator verdicts. The `pipeline` key lists 6 stage names but no stage outputs exist anywhere.
- `arxiv_wiki_feed_coverage_rows`: **0 rows.** `arxiv_wiki_feed_runs`: max id still **17** (2026-06-02, `candidates_built`). Runs 16–17 backlog from the v2.0 design is also still unprocessed.
- **Verdict: Mode 1 as deployed is fetch-and-archive, not auto-validate.** Coverage-ready rows are not accumulating, therefore the ≥30 rows / ≥15 claims promotion gate can never be crossed no matter how many weeks pass. The "≥4 weeks of Mode 1 before Mode 2" clock has not actually started.
- `pipeline_runs` since 06-12: no failures (the daily task itself completes; it just doesn't do the work).
- Fix: §7.2. Design reference: `arxiv_wiki_feed_design_v1.md` v2.0 stages [A]–[E] + run-row write.

---

## 5. Pages 9 (AGN) + 11 (exoplanets) — onboarding readiness

Not proposing activation — Papa's bar is "page 57 first." This is the effort map for when the time comes.

| Dimension | p57 (galaxy-evolution) | p9 (AGN) | p11 (exoplanets) |
|---|---|---|---|
| Registry status | `active`, 11 lanes | `onboarding`, 1 lane (arxiv_feed_l2) | same |
| Content | 52 KB | 8 KB | 13 KB |
| Claims | 499 | 20 | 13 |
| Evidence rows | ~775 | 141 | 652 (†) |
| Calibration YAML | ✓ `page_retrieval_calibration.galaxy-evolution.v2.yaml` | ✗ | ✗ |

(†) p11's 652 evidence rows on 13 claims is anomalous — almost certainly legacy bulk mining; quality unaudited. Worth a 30-minute sanity check before ever counting it as an asset.

**Activation checklist (per page), in dependency order:**
1. **Calibration YAML** — `page_retrieval_calibration.<slug>.v2.yaml`; exists only for galaxy-evolution. The synonym bands / thresholds are page-specific by design and are the long pole (needs a domain pass, ~half a day each).
2. **Unpin `retrieval_filter_v2_production_apply.py`** — LIVE_CONFIG hardcodes the galaxy-evolution YAML (line ~32). The `--slug` arg precondition from `page_registry_design_v1.md` is **not done**. Blocking, small (§7.3).
3. **Claim base build** — 20/13 claims vs 499. Claim extraction + canonicalizer pass + marker embedding on an 8–13 KB page. Moderate; the verbatim-sync lesson (93% text-mismatch failure mode) applies — markers must be embedded against final prose.
4. **Lane ramp** — enable per registry: evidence_drain → judges/jury → research_ideas → section_rewrite, in that order, each behind one clean run.
5. Already in place for free: L2 daily feed *already queries both pages' categories* (06-12 artifact includes them) — once Mode 1 actually materializes coverage rows (§4), candidate flow for 9/11 starts with zero extra work.

Honest estimate per page once Mode 1 is fixed: **2–3 focused days** (calibration 0.5d, claim base 1–1.5d, lane ramp + verification 0.5–1d).

---

## 6. Surveys T2 follow-up

- Enriched so far: 11/28 (batch 1: ALMA, HST, Chandra, VLA, 2MASS, GALEX, ROSAT · batch 2: Planck, WISE, PanSTARRS, XMM incl. fresh 5XMM-DR15 promotion).
- **17 bootstrap-only T2 surveys remain:** act, askap-emu, cdf-n, cdf-s, deep2, fermi-lat, h-atlas, hetdex, hipass, lofar, meerkat, spt, ukidss, unions, viking, vipers, zcosmos.
  (The other 9 single-row surveys — 4most, cmb-s4, elt, ngvla, pfs, roman, ska1, spherex, weave — are T3 planned-only, already hand-curated as honest "planned" rows. Not backlog.)
- Effort calibration from batch 2: 4 surveys ≈ one focused session (~2–3 h incl. ADS bibcode verification).
- Remaining profile: 10 of the 17 are static/legacy (cdf-n/s, deep2, zcosmos, vipers, viking, ukidss, h-atlas, spt, act) — single-final-release records, fast. The active radio set (lofar, meerkat, askap-emu) + fermi-lat + hetdex/unions/hipass carry real release history.
- **Estimate: 4 batches ≈ 4 sessions** (suggest: legacy-optical batch, X-ray/γ batch, radio batch, stragglers). No decisions needed; I can continue rolling these between dispatches.

---

## 7. Tori dispatch briefs (straightforward fixes only)

### 7.1 Write-path lockdown (P0, ship first)
1. `claims.py:508 vote_claim_proposal`: add `Depends(require_api_key)`; count `DISTINCT` authenticated agent approvals; add `@limiter.limit(EDITS_LIMIT)`. **Remove the direct `claim.text =` / `trust_level='accepted'` / Evidence-insert side effect entirely** — route approval through the existing proposal→jury path instead (a vote should never mint evidence).
2. `pages.py:438 vote_on_proposal`: add `Depends(require_api_key)`; threshold on `count(DISTINCT Vote.agent_id)`; unique constraint `(edit_id, agent_id)` on `votes` (migration).
3. `pages.py:359 submit_proposal`, `pages.py:409 post_comment`: add `require_api_key`; derive `agent_id` from the key, ignore body value (anti-spoof).
4. Acceptance: anonymous POST to all four endpoints → 401; same-agent triple-vote → threshold not reached; existing platoon agents (with keys) unaffected.

### 7.2 Mode 1 stage wiring (P1)
1. In the daily task (`arxiv_fetch.py:294` region): after the paper fetch, actually invoke stages [A] candidate build → [B] retrieval filter v2 → [C] semantic band → [D] coverage materialization → [E] validator, per `arxiv_wiki_feed_design_v1.md` v2.0. Stop before promoter (unchanged).
2. Write a run row to `arxiv_wiki_feed_runs` (status per stage reached) and coverage rows to `arxiv_wiki_feed_coverage_rows` — Mode 1's whole point is accumulating evidence for the ≥30/≥15 gate.
3. Process the runs 16–17 backlog through the same path.
4. Acceptance: next daily run leaves a run row with status ≥ `validator_complete`, coverage_rows > 0, artifact includes per-stage outputs.

### 7.3 Small ops sweep (P3)
1. Close/fail the stale `drain_stance_jury_backlog` row (06-12 02:00) and add a finally-block status close to that task.
2. `retrieval_filter_v2_production_apply.py`: replace the hardcoded `LIVE_CONFIG` with `--slug` arg (default galaxy-evolution for back-compat).
3. Custody commit of the 46 modified files (reviewed diff, no blind `git add -A`).

---

## 8. Papa decisions needed

| # | Decision | Default recommendation |
|---|----------|------------------------|
| D1 | Proposals triage policy (§2): approve auto-expire >30d + weekly top-10 review? | Yes — queue is unmanned, tooling exists |
| D2 | `research_ideas.opus_judge_pool`: whitelist Opus or drop the attempt? | Drop — opus-judge-tick already covers Opus judging 24×/day |
| D3 | Branch strategy: merge `retrieval-filter-v1-dryrun` → main after custody commit? | Yes, then main becomes prod branch again |
| D4 | Budget enforcement flip (`REGISTRY_ENFORCE_BUDGETS=true`) after 7 days of llm_calls baseline? | Yes, with log-compare week first |

---

*All file:line references verified against working tree at audit time. DB queries run against `nebulamind-postgres-1` (user `nebula`). This doc is untracked until the next custody commit.*
