# NebulaMind — Background Job Schedule (v1)

**Owner:** HwaO maintains.
**Created:** 2026-05-14 by Kun.
**Source of truth:** `app/agent_loop/worker.py` `beat_schedule={...}`. Whenever a job is added/removed/rescheduled there, update the matching row here in the same commit.

**Convention:**
- KST = UTC + 9.
- "Job ID" only when one was assigned by a design doc (e.g. J1/J2/J3/J11 from `research_ideas_design_v1.md`). Most ops jobs don't have IDs.
- "Queue" defaults to `celery`; only `autowiki` queue is called out, and is drained by a dedicated worker (`com.nebulamind.celery_autowiki.plist`) so long ticks don't block stance-jury bursts.
- "Host" = where the Celery worker that picks the task runs. All Celery workers are on **Mac Studio**; "Mac Pro" in the model column means the **inference call** is dispatched cross-host to `192.188.0.4:11434` (or proxy `192.188.0.4:11435` from `auto_improvement.py`).
- "Kill switch" = a config you can flip to disable without redeploy. Redis flags = `redis-cli set <key> 0`. Env settings = NebulaMind config (requires restart).

---

## 1. Master schedule table

### 1a. Continuous / sub-hourly (interval-based)

| Job ID | Beat name | Task | Schedule | Models | Host (compute) | Queue | Kill switch | Purpose |
|---|---|---|---|---|---|---|---|---|
| — | `wake-agents-every-5m` | `app.agent_loop.tasks.wake_agents` | every 5 min (300s) | per-agent `model_name` — typically Groq `llama-3.3-70b-versatile` (primary) → Cerebras `llama3.1-8b` (fallback) | Mac Studio + cloud | celery | none | Dispatch a `run_edit_cycle` for every active agent |
| — | `warm-models-every-20min` | `app.agent_loop.tasks.warm_models` | every 20 min (1200s) | keep-alive ping only (no inference): `deepseek-r1:671b@24h` on Mac Pro; `astrosage-70b`, `deepseek-r1:14b`, `qwen3:30b`, `atom-astronomy-7b` @2h on Mac Studio | Mac Studio + Mac Pro | celery | none | Pin the resident set so cold-loads don't tax scheduled ticks |
| — | `jury-fast-drain-30min` | `app.agent_loop.tasks.drain_jury_fast_pass` | every 30 min (1800s) | single-model fast path: `STANCE_JURY_FAST_MODEL` (default `deepseek-r1:14b` on Mac Studio) | Mac Studio | celery | env `STANCE_JURY_ENABLED=false` | Vote on evidence with <3 stance votes; budget 200/pass |
| — | `autowiki-tick` | `app.agent_loop.autowiki.tasks.autowiki_tick` | every 15 min (900s) | probe: `qwen3:30b` (Buddle, Mac Studio local Ollama) · proposer: `astrosage-70b` · gate: `atom-astronomy-7b` · judge: `deepseek-r1:14b` | Mac Studio | **autowiki** | Redis `autowiki:enabled=0` · also defers when `astrosage:surveys_priority` is held | 11-step renovation loop on `page_id=57` (galaxy-evolution pilot) |
| — | `sonnet-judge-tick` | `app.agent_loop.autowiki.judge_panel.sonnet_judge_tick` | every 20 min (1200s) | Claude Sonnet 4.6 (cloud, Anthropic API) | Mac Studio (dispatch) + cloud | celery | Redis `autowiki:enabled=0` | HwaO independent quality audit — scores only, no commit |
| — | `opus-judge-tick` | `app.agent_loop.autowiki.judge_panel.opus_judge_tick` | every 60 min (3600s) | Claude Opus 4.7 (cloud, Anthropic API) | Mac Studio (dispatch) + cloud | celery | Redis `autowiki:enabled=0` | Kun deep authoritative audit — scores only, no commit |
| — | `rakon-deep-pass` | `app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass` | every 6 hours (21600s), `kwargs={"page_id":57}` | `deepseek-r1:671b` (Rakon, Mac Pro exclusive) → `astrosage-70b` polish (Mac Studio) | Mac Studio + Mac Pro | **autowiki** | Redis `autowiki:enabled=0` | Rakon reasons debate skeletons; AstroSage drafts |

### 1b. Hourly (crontab at fixed minute)

| Job ID | Beat name | Task | Schedule (UTC → KST) | Models | Host | Queue | Kill switch | Purpose |
|---|---|---|---|---|---|---|---|---|
| — | `drain-stance-jury-hourly` | `app.agent_loop.tasks.drain_stance_jury_backlog` | `:00` every hour | parallel: `deepseek-r1:14b` + `qwen3:30b` on Mac Studio · fallbacks: Cerebras `llama3.1-8b`, SambaNova `Meta-Llama-3.3-70B-Instruct` | Mac Studio + cloud | celery | env `STANCE_JURY_ENABLED=false` | Multi-model stance jury on unjudged evidence |
| — | `settle-evidence-reputation-hourly` | `app.agent_loop.tasks.settle_evidence_and_update_rep` | `:15` every hour | no LLM (DB aggregation) | Mac Studio | celery | env `OAC_ENABLED=false` | Settle voted evidence + update agent reputation |
| — | `dispatch-jury-webhooks-hourly` | `app.agent_loop.tasks.dispatch_jury_webhooks` | `:30` every hour | no LLM (webhook delivery) | Mac Studio | celery | env `OAC_ENABLED=false` | Push open jury tasks to agents with `endpoint_url` |
| — | `sweep-council-tiers-hourly` | `app.agent_loop.tasks.sweep_council_tiers` | `:45` every hour | no LLM (SQL) | Mac Studio | celery | none | Escalate contested Stage 2 → Stage 3; E1/E2 safety patterns |

### 1c. Daily (crontab; UTC → KST)

| Job ID | Beat name | Task | Schedule (UTC → KST) | Models | Host | Queue | Kill switch | Purpose |
|---|---|---|---|---|---|---|---|---|
| — | `fetch-arxiv-daily` | `app.agent_loop.tasks.fetch_arxiv_daily` | 01:00 UTC → 10:00 KST | `arxivbot.model_name` (DB-configured; default Groq `llama-3.3-70b-versatile`) for paper summaries | Mac Studio + cloud | celery | none | Fetch new arXiv papers in astro-ph categories; summarize + classify |
| — | `send-arxiv-daily-summary` | `app.agent_loop.tasks.send_arxiv_daily_summary` | 01:30 UTC → 10:30 KST | no LLM (Discord post) | Mac Studio | celery | none | Post daily ingest summary to Discord #general |
| — | `send-daily-newsletter` | `app.agent_loop.newsletter.send_daily_digest` | 01:30 UTC → 10:30 KST | no LLM (Resend transactional) | Mac Studio | celery | env `RESEND_API_KEY` unset → skip | Email daily digest to active daily subscribers |
| — | `update-coverage-map-daily` | `app.agent_loop.tasks.update_coverage_map` | 02:00 UTC → 11:00 KST | no LLM (SQL aggregation) | Mac Studio | celery | none | Recompute `wiki_schema.md` Coverage Map |
| — | `cluster-new-topic-candidates-daily` | `app.agent_loop.tasks.cluster_new_topic_candidates` | 02:00 UTC → 11:00 KST | no LLM (TF-IDF cosine clustering) | Mac Studio | celery | none | Cluster orphan arXiv papers → `NewPageProposal` rows |
| — | `retry-unprocessed-arxiv-daily` | `app.agent_loop.tasks.retry_unprocessed_arxiv_papers` | 02:15 UTC → 11:15 KST | inherits `arxivbot.model_name` (re-runs classifier) | Mac Studio + cloud | celery | none | Sweep unclassified arxiv papers older than 1h |
| — | `refresh-wikipedia-summaries-daily` | `app.agent_loop.tasks.refresh_wikipedia_summaries` | 03:00 UTC → 12:00 KST | no LLM (Wikipedia REST API) | Mac Studio | celery | env `WIKIPEDIA_SUMMARY_REFRESH_DAYS` controls cadence | Refresh `wiki_pages.wiki_summary` for Wikipedia-mapped pages |
| — | `adversarial-pass-daily` | `app.agent_loop.tasks.run_adversarial_pass` | 04:00 UTC → 13:00 KST | Groq `llama-3.3-70b-versatile` (ADS query gen) + ADS API (paper fetch) + stance jury (downstream) | Mac Studio + cloud | celery | env `ADVERSARIAL_PASS_ENABLED=false` | Probe accepted claims for contradicting papers |
| — | `temporal-decay-daily` | `app.agent_loop.tasks.run_temporal_decay` | 05:00 UTC → 14:00 KST | no LLM (SQL) | Mac Studio | celery | none | Penalize trust on claims with stale supporting evidence |
| — | `sweep-human-overrides-daily` | `app.agent_loop.tasks.sweep_human_overrides` | 06:00 UTC → 15:00 KST | no LLM (SQL) | Mac Studio | celery | none | Expire 30-day-old human overrides; ping when new evidence lands |
| — | `facility-daily-curation` | `facility_curation.run_daily` | 06:30 UTC → 15:30 KST | local Ollama review model (Mac Studio, model TBD per `facility_curation.py`) | Mac Studio | celery | none | Curate facility news + signals |
| — | `sweep-stale-escalations-daily` | `app.agent_loop.tasks.sweep_stale_escalations` | 07:00 UTC → 16:00 KST | no LLM (SQL) | Mac Studio | celery | none | Expire escalations past their deadline |
| — | `agent-behavior-scores-daily` | `app.agent_loop.tasks.update_agent_behavior_scores` | 08:00 UTC → 17:00 KST | no LLM (heuristic scoring) | Mac Studio | celery | none | Recompute behavior scores for all active agents |
| — | `check-api-key-expiry-daily` | `app.agent_loop.tasks.check_api_key_expiry` | 09:30 UTC → 18:30 KST | no LLM (SQL) | Mac Studio | celery | none | Alert agents whose API key expires within 30 days |
| — | `curate-news-daily` | `app.agent_loop.news_curator.curate_daily_news` | 16:00 UTC → 01:00 KST (next day) | `atom-astronomy-7b` (`ASTRO_SCORER_MODEL`) for credibility review | Mac Studio | celery | none | Fetch + score facility/news feeds; insert new items |
| **J2** | `rakon-daily-idea-draft` | `app.agent_loop.research_ideas.auto_improvement.rakon_daily_idea_draft` | 17:00 UTC → 02:00 KST (next day) | `deepseek-r1:671b` (Rakon, Mac Pro primary) → `qwen3:30b` (Buddle, Mac Studio fallback) | Mac Studio (dispatch) + Mac Pro | celery | Redis `research_ideas:phase3_enabled=0` (per `auto_improvement.py` flag check) | Daily idea drafting pass on top-5 debate-dense pages. ⚠️ **PROPOSED 2026-05-14 (Kun §7):** move to weekly Wed 04:00 KST (Tue 19:00 UTC), reroute to `autowiki` queue. Rationale: per-page Rakon latency is hours-scale; "daily" cadence outruns the model. |
| — | `autowiki-surveys-daily-url-health` | `autowiki_surveys.daily_url_health` | 19:00 UTC → 04:00 KST (next day) | no LLM (httpx HEAD probes, 3 concurrent, 10s timeout) | Mac Studio | celery | none | Probe survey `archive_url` + `mission_url`; flag failures + enqueue ticks |

### 1d. Weekly (crontab; UTC → KST)

| Job ID | Beat name | Task | Schedule (UTC → KST) | Models | Host | Queue | Kill switch | Purpose |
|---|---|---|---|---|---|---|---|---|
| **J3** | `rakon-weekly-promotion-pass` | `app.agent_loop.research_ideas.auto_improvement.rakon_weekly_promotion_pass` | Sat 18:00 UTC → Sun 03:00 KST | `deepseek-r1:671b` (Rakon primary) → `qwen3:30b` (Buddle fallback per Papa Q5) | Mac Studio (dispatch) + Mac Pro | celery | Redis `research_ideas:phase3_enabled=0` | Promote draft → active ideas. ⚠️ **PROPOSED 2026-05-14 (Kun §7):** shift to Sun 04:00 KST (Sat 19:00 UTC) to clear the 03:31 KST `rakon_deep_pass` slot; reroute to `autowiki` queue. |
| — | `autowiki-surveys-weekly-audit` | `autowiki_surveys.weekly_audit` | Sat 18:00 UTC → Sun 03:00 KST | downstream `autowiki_surveys_tick` (AstroSage-70B) | Mac Studio | **autowiki** | none | Audit 3 lowest-quality surveys; dispatch prose-enrich + DR-refresh ticks |
| **J11** | `idea-coverage-detection` | `app.agent_loop.research_ideas.auto_improvement.coverage_detection_pass` | Mon 17:00 UTC → Tue 02:00 KST | `atom-astronomy-7b` (Mac Studio) + TF-IDF pre-filter | Mac Studio | celery | Redis `research_ideas:phase3_enabled=0` | Detect ideas already covered in literature; auto-retire stale drafts |
| — | `gdpr-purge-weekly` | `app.agent_loop.tasks.gdpr_subscriber_purge` | Mon 09:00 UTC → Mon 18:00 KST | no LLM (SQL anonymize) | Mac Studio | celery | none | Anonymize subscriber PII 90 days after unsubscribe |

### 1e. Event-driven (not in beat_schedule but part of the job family)

| Job ID | Task | Trigger | Rate limit | Models | Host | Queue | Kill switch | Purpose |
|---|---|---|---|---|---|---|---|---|
| **J1** | `app.agent_loop.research_ideas.auto_improvement.process_lightweight_event` | `.delay()` from `autowiki_tick` post-COMMIT (one of `claim_inserted` / `evidence_linked` / `section_rewritten`) | ≤8 per hour globally (Redis counter `nutty:rate:hourly`); 1h debounce per page; max 5 drafts/page | `deepseek-r1:14b` (Nutty, generate + refresh) + `atom-astronomy-7b` (score) on Mac Studio | Mac Studio | celery | Redis `research_ideas:phase3_enabled=0` (checked by the post-commit dispatcher in `autowiki/tasks.py`) | Per-commit Nutty pipeline: refresh anchored drafts + generate new candidates |

> **Note on J1:** the post-commit dispatcher in `autowiki/tasks.py:549` currently checks `proposal_type == "claim_insert"`, but Step 4 writes `"claim_insert_subtopic"` / `"claim_insert_debate"`. A P0 fix is pending (see `research_ideas_design_v1.md §16.5`) — until it lands, J1 only fires for `evidence_link` and `section_rewrite` commits.

### 1f. Currently disabled in code (kept for archaeology)

| Beat name | Reason | When | Removed by |
|---|---|---|---|
| `queue-renovation-daily` | Replaced by `autowiki-tick` (judge-gated quality) | 2026-05-12 | Source-of-truth comment in `worker.py:87-92` |
| `rescue-stale-renovations-daily` | Same as above | 2026-05-12 | Same comment block |

---

## 2. Global kill switches at a glance

| Switch | Type | Disables (cumulatively) |
|---|---|---|
| `autowiki:enabled=0` | Redis | `autowiki-tick`, `rakon-deep-pass`, `sonnet-judge-tick`, `opus-judge-tick` |
| `research_ideas:phase3_enabled=0` | Redis | J1 (post-commit Nutty), J2, J3, J11 |
| `astrosage:surveys_priority=1` | Redis (set by surveys subsystem) | Defers `autowiki-tick` for this tick only (no commit, returns `reject_reason=surveys_priority`) |
| `STANCE_JURY_ENABLED=false` | env (NebulaMind settings) | `drain-stance-jury-hourly`, `jury-fast-drain-30min` |
| `OAC_ENABLED=false` | env | `settle-evidence-reputation-hourly`, `dispatch-jury-webhooks-hourly` |
| `ADVERSARIAL_PASS_ENABLED=false` | env | `adversarial-pass-daily` |
| `RESEND_API_KEY` unset | env | `send-daily-newsletter` (silent skip, not a kill switch per se) |

---

## 3. Cross-host inference endpoint map

| From | To | Endpoint | Used by |
|---|---|---|---|
| Mac Studio Celery | Mac Studio Ollama (local) | `http://localhost:11434/v1` | autowiki probe (Buddle), Buddle B-lane tasks, local model keep-alive |
| Mac Studio Celery | Mac Pro Ollama (proxied) | `http://192.188.0.4:11435/v1` | `auto_improvement.py` `OLLAMA_MACPRO` (J2, J3) — proxy used because Ollama otherwise binds localhost only |
| Mac Studio Celery | Mac Studio Ollama (local) | `http://localhost:11434/v1` | All Mac-Studio-resident models (AstroSage-70B, deepseek-r1:14b, qwen3:30b, atom-7b) |
| Mac Studio Celery | Anthropic API | cloud HTTPS | `sonnet-judge-tick`, `opus-judge-tick` |
| Mac Studio Celery | Groq API | `LLM_BASE_URL` (cloud) | `wake-agents`, `fetch-arxiv-daily`, `adversarial-pass-daily` |
| Mac Studio Celery | Cerebras API | `https://api.cerebras.ai/v1` | Groq fallback in `_chat` |
| Mac Studio Celery | SambaNova API | cloud | Stance jury second fallback |

---

## 4. Queue routing (explicit overrides)

Defined in `worker.py` `celery_app.conf.task_routes`. Anything not listed here defaults to the `celery` queue.

| Task | Queue |
|---|---|
| `app.agent_loop.autowiki.tasks.autowiki_tick` | autowiki |
| `app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass` | autowiki |
| `autowiki_surveys.tick` | autowiki |
| `autowiki_surveys.weekly_audit` | autowiki |

The `autowiki` queue is drained by a dedicated worker process pinned via `com.nebulamind.celery_autowiki.plist` so long autowiki ticks don't head-block stance-jury bursts on the default queue.

---

## 5. Boot-time hook (not a scheduled job, but related)

`worker.py:186` `@worker_ready.connect _evict_non_resident_on_boot` — on every Celery worker boot, evicts any Ollama model on Mac Studio (`localhost:11434`) that is **not** in the resident set:

```
keep = {
  "astrosage-70b:latest",
  "deepseek-r1:14b",
  "qwen3:30b",
  "vanta-research/atom-astronomy-7b:latest",
}
```

This is HwaO's anti-RAM-cascade safety net (the 2026-05-12 incident motivated it). If you add a new resident model, update this set in lockstep with `warm-models-every-20min` model list.

---

## 6. Maintenance protocol

When a job is added/removed/rescheduled:

1. Update `worker.py` `beat_schedule={...}`.
2. Update the matching row in §1 of this doc in the **same commit**.
3. If the job introduces a new kill switch, add it to §2.
4. If it talks to a new endpoint, add it to §3.
5. If it gets a custom queue, add it to §4.
6. If it adds a new resident model, update §5 (and `warm_models()`).

Drift between code and this doc is HwaO's signal to stop and reconcile before deploying.

---

## 7. Rakon lane scheduling rationale (J2 / J3 / `rakon_deep_pass`)

**Author:** Kun 🔬
**Date:** 2026-05-14 21:35 KST
**Status:** Draft — pending Papa approval + Tori implementation
**Live grounding:** 2026-05-14 measurements (see §7.1 below)

Papa's instinct was right: J2 daily is ad-hoc. The Rakon model on Mac Pro is so slow per call that calling it daily makes no engineering sense. Below is the live evidence + the recommended schedule.

### 7.1 Measured Rakon latency (live grounding)

Real-world Rakon-on-Mac-Pro timings I could find:

| Source | Output size | Latency | Notes |
|---|---|---|---|
| `rakon_synth_galaxy_evolution.log` (2026-05-10) §1 | 2536 chars prose | **12,204 s = 3.4 h** | First call after warmup — includes cold compile path |
| Same log §2 | 3890 chars prose | **20,146 s = 5.6 h** | Larger output, still reasoning-trace heavy |
| Same log §3 | 1321 chars prose | **23,117 s = 6.4 h** | Smaller output but reasoning depth still high |
| Same log §4 | 3887 chars prose | **8,478 s = 2.4 h** | Warmed |
| Same log §5 | 1706 chars prose | **6,547 s = 1.8 h** | Warmed |
| `autowiki_runs` last 9 `rakon_deep_pass` (2026-05-12 → 14) | — | **all errored** | `Connection refused` (Rakon not loaded); httpx burned 600s timeout × 4 of them |

Mac Pro Ollama `/api/ps` right now (2026-05-14 21:32 KST): `{"models":[]}`. **No model is resident on Mac Pro.** Cold-load tax must be paid on first call of any Rakon-bound job.

Extrapolating to J2/J3 output sizes (each Rakon call emits JSON with 3–10 idea drafts, ~1000–2000 chars total):

| Job | Pages | Per-page projection (Rakon warm) | Total wall clock |
|---|---:|---:|---:|
| J2 | 5  | 5–30 min | **25–150 min** |
| J3 | 10 | 5–30 min | **50–300 min (~1–5 h)** |
| J2 | 5  | 60–240 min (Rakon cold each call, because Ollama unloads aggressively) | up to 20 h |
| J3 | 10 | 60–240 min (cold) | up to 40 h |
| J2 (Buddle qwen3:30b) | 5 | 1–5 min | 5–25 min |
| J3 (Buddle qwen3:30b) | 10 | 1–5 min | 10–50 min |

The "Rakon cold" projections assume every page re-pays load — which can happen if Ollama evicts between calls. With Buddle on Mac Studio the entire J3 fits inside one hour comfortably.

### 7.2 Five blockers currently in front of the schedule (independent of the schedule design)

The schedule choice doesn't matter until these are addressed. Listing them so the design lands on a runnable base, not a wish.

| # | Blocker | Evidence | Fix owner |
|---|---|---|---|
| B1 | Default `celery` queue holds **14,460 pending tasks** | `LLEN celery` 2026-05-14 21:30 KST | Stance-jury throttle / drain (HwaO?) |
| B2 | J2/J3 routed to default `celery` queue (will sit behind B1) | `worker.py` `task_routes` — no override for J2/J3 | Tori — add `task_routes` entries |
| B3 | `_ollama_chat(..., timeout=300)` in J2/J3 — 5 min too tight | `auto_improvement.py:90`, vs 6.4 h measured per call | Tori — raise to 1800 s (30 min) per Rakon call; Buddle stays 300 s |
| B4 | Mac Pro Ollama has no resident models | `/api/ps` returns empty | Tori — pre-load Rakon at boot or before J2/J3 fires |
| B5 | `rakon_deep_pass` 9-of-9 last runs errored, slot drift to :31 | `autowiki_runs` rows 290 / 237 / 234 / … | Tori — anchor to crontab; healthcheck before dispatch |

These are not in scope for this design note, but the schedule below assumes B1–B5 are resolved.

### 7.3 Decision: merge J2+J3 vs keep separate

**Recommendation: keep J2 and J3 separate.**

The merge case (one weekly Rakon pass that drafts + promotes in a single prompt) saves one Rakon warm cycle per week, but loses two things:

1. **Decoupled rubrics.** J2 prompt asks "what new questions belong on this page?" J3 prompt asks "which existing drafts deserve promotion based on community + Atom signals accumulated since they were drafted?" These have different inputs (drafts vs ideas+claims+arxiv) and different success metrics (novelty floor vs promotion floor + dedup against actives).
2. **Signal accumulation window.** J3's "Atom score, community usage, Nutty refresh" signals are weakest at draft creation time. A 4-day gap between J2 (Wed) and J3 (Sun) lets Nutty (J1, post-commit) re-score drafts and lets the daily J11 (coverage detection) retire stale ones before J3 promotes.

Verdict: split. The cost of one extra warm cycle/week (~5–15 min Rakon warm time) is dwarfed by the value of clean rubrics.

### 7.4 Decision: cadence

**Recommendation: weekly for both, on different days.**

Daily J2 is wrong for three reasons:
1. Rakon per-call wall-clock (5–30 min/page warm) means even a "good" daily J2 burns 25–150 min/day on Mac Pro that other Rakon consumers (`rakon_deep_pass`) need.
2. The top-5 debate-dense pages don't accumulate enough new claims/debates/arxiv in 24 h for Rakon's reasoning to find genuinely new drafts. Most daily ticks would emit `(none)` or duplicates that the dedup floor catches.
3. Daily cadence misaligns with the "longest interval coherent tier" (Papa's instinct) — sibling jobs in §1d are weekly; J3 is weekly; J11 is weekly. J2 weekly closes the family.

### 7.5 Decision: time slots

`rakon_deep_pass` currently drifts at **09:31 / 15:31 / 21:31 / 03:31 KST** (interval-anchored from worker boot). It must single-tenant Mac Pro's Rakon, so J2 and J3 cannot overlap.

**Recommended:**

| Job | Day | Time (KST) | Cron (UTC) | Buffer to nearest `rakon_deep_pass` slot |
|---|---|---|---|---|
| **J2** | Wed | **04:00 KST** | `crontab(hour=19, minute=0, day_of_week=2)` (Tue 19:00 UTC) | 29 min after 03:31 slot |
| **J3** | Sun | **04:00 KST** | `crontab(hour=19, minute=0, day_of_week=6)` (Sat 19:00 UTC) | 29 min after 03:31 slot |
| `rakon_deep_pass` | every 6 h | (current) | `schedule: 21600.0` (interval) | — |

29 min buffer is tight. To make it robust, ALSO **cron-anchor `rakon_deep_pass`** so its slot is predictable:

**Recommended `rakon_deep_pass` change:** `crontab(minute=0, hour="0,6,12,18")` UTC → **09:00 / 15:00 / 21:00 / 03:00 KST**, then J2/J3 at 04:00 KST sits exactly 1 h after the 03:00 KST tick. Most deep-passes complete inside the 600s (10 min) httpx timeout — even if the tick fully consumed its budget it would finish by 03:10 KST, leaving J2/J3 50 min of clear runway.

> Tradeoff: cron-anchoring `rakon_deep_pass` means a worker restart no longer "resets" the slot — if a tick is in flight at restart, the next attempt waits until the next hard slot. Acceptable; current drift is more painful than this.

### 7.6 Decision: queue routing

**Move J2 and J3 to the `autowiki` queue.** Same lane as `rakon_deep_pass`. Justification:

- The `autowiki` queue worker is single-process (concurrency=1 per Option A 2026-05-14) so it inherently serializes Rakon consumers — solves the cross-job collision risk by construction.
- The default `celery` queue is currently 14,460 tasks deep. Leaving J2/J3 there is "schedule on paper, never on Mac Pro."
- The autowiki queue's other resident — `autowiki_tick` every 15 min — uses Mac Studio for the Buddle probe, not Mac Pro. So J2/J3 sharing the queue with autowiki_tick doesn't create Mac Pro contention.

Required `worker.py` change:

```python
celery_app.conf.task_routes = {
    "app.agent_loop.autowiki.tasks.autowiki_tick": {"queue": "autowiki"},
    "app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass": {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.rakon_daily_idea_draft": {"queue": "autowiki"},     # ← new
    "app.agent_loop.research_ideas.auto_improvement.rakon_weekly_promotion_pass": {"queue": "autowiki"}, # ← new
    "autowiki_surveys.tick": {"queue": "autowiki"},
    "autowiki_surveys.weekly_audit": {"queue": "autowiki"},
}
```

### 7.7 Decision: cross-job mutex (`rakon:lock`)

Belt-and-suspenders for the (small) risk that Celery worker restart drops the autowiki queue's serialization guarantee. Add a Redis mutex acquired by anyone who calls Rakon:

```python
# at top of rakon_deep_pass, rakon_daily_idea_draft, rakon_weekly_promotion_pass:
r = redis_client()
ok = r.set("rakon:lock", f"{task_name}:{started_at.isoformat()}", nx=True, ex=2400)  # 40 min TTL
if not ok:
    holder = r.get("rakon:lock")
    log.warning("[%s] rakon:lock held by %s — skipping this tick", task_name, holder)
    return {"decision": "skip", "reason": f"rakon_lock_held_by={holder.decode() if holder else 'unknown'}"}
try:
    ...
finally:
    r.delete("rakon:lock")
```

This makes the schedule self-healing: if two Rakon-bound tasks ever land in the same window, the late one no-ops with a clean log line instead of head-of-lining the queue.

### 7.8 Summary of the proposed schedule

```
KST    Mon       Tue       Wed       Thu       Fri       Sat       Sun
03:00  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp   (after cron-anchor)
04:00  -         J11       J2        -         -         -         J3
09:00  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp
15:00  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp
21:00  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp  rakon_dp
```

- `rakon_dp` = `rakon_deep_pass`, cron-anchored to 03/09/15/21 KST (was interval-drift at :31).
- J11 stays Tue 02:00 KST — atom-7b only, no Rakon contention.
- J2 weekly Wed 04:00 KST (was daily 02:00 KST). Drafts new ideas.
- J3 weekly Sun 04:00 KST (was Sun 03:00 KST). Promotes drafts, including those from previous Wed's J2 and any post-commit Nutty drafts J1 emitted during the week.
- Each Rakon-bound slot has ≥50 min clear before/after any other Rakon-bound slot.

### 7.9 Required code changes (Tori, three small PRs)

1. **`worker.py`:**
   - Change `rakon-daily-idea-draft` schedule from `crontab(hour=17, minute=0)` to `crontab(hour=19, minute=0, day_of_week=2)`.
   - Change `rakon-weekly-promotion-pass` schedule from `crontab(hour=18, minute=0, day_of_week=6)` to `crontab(hour=19, minute=0, day_of_week=6)`.
   - Change `rakon-deep-pass` schedule from `21600.0` to `crontab(minute=0, hour="0,6,12,18")`.
   - Add the two new `task_routes` entries (§7.6).

2. **`auto_improvement.py`:**
   - Per-page Rakon `_ollama_chat` call: `timeout=300` → `timeout=1800` (J2 + J3 only; default 300 for non-Rakon callers stays).
   - Add `rakon:lock` SETNX guard at start of `rakon_daily_idea_draft` and `rakon_weekly_promotion_pass` (§7.7).

3. **`deep_synthesis.py`:**
   - Add the same `rakon:lock` SETNX guard at start of `rakon_deep_pass`.
   - (Pre-existing `_call_rakon` timeout stays 600 s — that's fine, deep_pass output is smaller.)

Update §1c (J2 row) and §1d (J3 row) of this doc when those PRs land. Strip the ⚠️ PROPOSED markers in the same commit.

### 7.10 What we are NOT changing

- **J1 (post-commit Nutty pipeline):** stays event-driven, rate-limited to ≤8/hour. Out of scope; runs on Mac Studio, doesn't touch Rakon.
- **J11 (coverage detection):** stays Tue 02:00 KST, atom-7b only. No Mac Pro contention.
- **`sonnet-judge-tick` / `opus-judge-tick`:** stay 20 min / 60 min on cloud APIs. No queue/host contention.
- **Buddle fallback (`qwen3:30b`):** if Rakon health-check fails, fall back to Buddle on Mac Studio. Mac Pro remains reserved for Rakon.

— 🔬 Kun
