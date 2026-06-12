# Design: Introduction-Section Augmentation for the Evidence Pipeline (v1)

**Author:** Kun · 2026-06-12
**Status:** Proposed — awaiting Papa review, then Tori dispatch (§6)
**Scope:** `backend/app/agent_loop/tasks.py`, `backend/app/services/paper_search.py`, new `backend/app/services/intro_fetch.py`, one Alembic migration, `worker.py` beat schedule.

---

## 0. Executive summary and an honest reframe

The brief asks where to inject paper-introduction text into the evidence pipeline to attack the
300 zero-evidence claims. The audit confirms intro text is valuable — but it is **not the dominant
cause** of the zero-evidence backlog. Live DB (2026-06-12):

| Population | Count | Cause |
|---|---|---|
| Total claims | 1,075 | — |
| Unverified | 326 | — |
| **Zero-evidence claims** | **300** | breakdown below |
| ├─ unverified / established | 171 | **Linker has never run on them** (see below) |
| ├─ debated / debate | 122 | Excluded by design (`claim_type='established'` filter) |
| └─ unverified / debate | 7 | Same exclusion |
| Zero-evidence claims ever searched (`evidence_search_attempted_at` set) | **7 / 300** | scheduling gap |
| Unverified claims **with** evidence (avg 2.6 ev, 3.9 votes) | 148 | trust-calc thresholds, not retrieval |

The forward linker (`_run_evidence_linker_v2`, tasks.py:1757) works, but its only scheduled entry
point is `drain-evidence-p57` (worker.py:263–268): **weekly, page 57 only, batch of 10**. The other
six pages with zero-evidence established claims (Reionization 15, ISM 14, Cosmic Web 11, BAO 9,
Exoplanet Detection 8, Hubble Constant 4) are never visited, and even page 57's 110 claims cannot
drain at 10/week with a 7-day retry cooloff.

**Therefore this design pairs two things:**

- **D0 (prerequisite, no intro needed):** widen the evidence drain from "weekly, page 57" to "hourly,
  all pages." This is a ~10-line change and is what actually moves the 171.
- **D1–D5 (the intro augmentation proper):** make each searched claim *succeed more often and more
  honestly* by giving the verifier and the stance jury introduction text when abstracts are terse,
  missing, or tangential. Immediate measurable targets: 106 evidence rows with an arXiv ID but a
  NULL/short abstract (today auto-skipped by every jury), and 834 rows with terse (100–600 char)
  abstracts judged on thin context.

The 122 debate-type claims stay out of linker scope on purpose (they are fed by the adversarial and
research-ideas lanes); Papa should not expect this design to zero them out.

---

## 1. What exists today (live-verified)

### 1.1 Citation-context miner (already uses intros)
- `citation_context/miner.py:259` `extract_arxiv_intro_context()` — fetches
  `https://ar5iv.labs.arxiv.org/html/{arxiv_id}`, strips tags, scans first ~30 KB after
  "Introduction" for a sentence citing the seminal work. Priority 3 fallback after S2 context and
  abstract (`extract_context_for_record`, miner.py:286–303). Budget `DEFAULT_ARXIV_INTRO_CAP = 5`
  per run (miner.py:37). Same pattern in `dynamic_miner.py:346–357`.
- No caching: every fetch is a live HTTP GET, result discarded after the run.

### 1.2 Main pipeline (abstract-only everywhere)
- **Daily fetch** `arxiv_fetch.py:54–121` — ADS query requests `fl=identifier,title,abstract,author,pubdate,pub,doi`. No full-text field (ADS does not return full text anyway).
- **Classification** `arxiv_classifier.py:95–100` — TF-IDF on `title + abstract[:1200]`.
- **Linker v2** `tasks.py:1757` — query gen (4 local models) → `search_papers()` (ADS/S2) →
  `verify_for_claim()` → insert. Verification hard-drops any record without an abstract
  (`paper_search.py:449–450`) and computes keyword overlap on the abstract alone
  (paper_search.py:459–465).
- **Stance pre-judge** `_llm_stance_verify` (paper_search.py:399) — Nutty (gpt-oss:20b),
  `abstract[:600]`.
- **4-model jury** `run_stance_jury_for_evidence` (tasks.py:2706) — skips evidence with
  `abstract < STANCE_JURY_MIN_ABSTRACT_CHARS` (=100) at tasks.py:2717; prompt uses
  `abstract[:2000]` (tasks.py:2733).
- **Fast jury** `run_stance_jury_single` (tasks.py:4680) — same skip at tasks.py:4698 (hardcoded
  100); prompt uses `abstract[:600]` (tasks.py:4712).
- **Drains** `drain_stance_jury_backlog` (tasks.py:2871–2872) and `drain_jury_fast_pass`
  (tasks.py:4821–4822, 4857–4858) — SQL-filter on `length(abstract) >= 100`, so NULL-abstract
  evidence is permanently invisible to juries. 106 such rows have a fetchable arXiv ID today.

### 1.3 ar5iv reliability (measured 2026-06-12, n=16 spanning 2007–2026)
- **16/16 HTTP 200**, payload 95 KB–1.7 MB (real conversions, not stubs).
- Latency 0.26–1.36 s (median ≈ 0.4 s), 25 s timeout never approached.
- Native `arxiv.org/html/{id}vN`: 200 only for ≥ 2024 submissions (6/6), **404 for all pre-2024**
  (10/10). ar5iv covers both eras, including a May-2026 paper.
- Conclusion: ar5iv primary, native arXiv HTML as fallback for recent papers, no third source
  needed. Semantic Scholar's free tier exposes `openAccessPdf` links only (PDF parsing — out of
  scope).

---

## 2. Decisions on the five scope points

### D1. Retrieval stage — keep abstract as the gate; broaden via ADS `full:` queries, not intro fetches
Fetching intros to *select* candidates inverts the cost model: retrieval sees ~12–24 candidates per
claim and would need an HTTP fetch per candidate before any ranking signal exists. Instead:

- **Add one ADS full-text query variant** per claim in linker v2 query generation. ADS supports the
  `full:"..."` operator server-side, which searches body text including introductions — this is
  exactly "find papers whose intro engages the claim" at zero fetch cost. One extra query string
  (`full:"<top claim keyphrase>"`), capped within the existing 6-query dedupe.
- **Intro-rescue inside `verify_for_claim`** (not retrieval): two specific rescues, both gated on
  the record having an arXiv ID:
  1. *Missing abstract*: the hard gate at paper_search.py:449 currently drops the record. New
     behavior — if `record.arxiv_id` and intro fetch succeeds, use the intro excerpt as the
     abstract-equivalent for keyword overlap and stance hint.
  2. *Terse/tangential abstract*: if keyword overlap lands below the drop floor
     (`EVIDENCE_MIN_QUALITY_FOR_ACCEPTED * 0.75`), recompute overlap once on
     `abstract + intro_excerpt`; keep the better score. Quality formula weights unchanged.

### D2. Stance jury — yes, `abstract + intro_excerpt`, deterministic excerpting, fixed budgets
- **Excerpt selection is deterministic, not LLM** (marker-audit lesson: no model-transcribed
  source text). From the cached intro, score sentences by claim-keyword hits (reuse
  `_claim_keywords` from paper_search.py:365), take the top 3–5 contiguous-ish sentences, cap
  **1,200 chars** — matching the miner's existing 1,200-char convention.
- **4-model jury** (tasks.py:2728–2736): append a block
  `Introduction excerpt (claim-relevant):\n{excerpt[:1200]}` after the abstract. Total added
  ≈ 300 tokens/juror — negligible for gemini-2.5-flash, Groq gpt-oss-20b, and local models.
- **Fast jury** (tasks.py:4709–4715): abstract stays `[:600]`, excerpt capped `[:800]` (Mima's
  local context is the constraint).
- **Gate change (both juries + both drains):** evidence qualifies if
  `length(abstract) >= 100 OR length(intro_excerpt) >= 200`. This unlocks the 106 NULL-abstract
  arXiv rows. The SQL drains add `OR length(e.intro_excerpt) >= 200` to their filters.
- Excerpt is stored per evidence row (see D4), so jury runs never block on HTTP.

### D3. Fetch strategy — ar5iv primary, native arXiv HTML fallback, validated 200s
- Order: `ar5iv.labs.arxiv.org/html/{id}` (timeout 20 s) → `arxiv.org/html/{id}v1` (timeout 15 s,
  ≥2024 papers only). One attempt each, no retries within a run.
- **Stub guard:** a 200 is accepted only if payload > 20 KB *and* contains "ntroduction" — ar5iv
  can return a shell page for failed conversions.
- Failures recorded in the cache with `http_status` so a paper is not refetched more than once per
  30 days.
- New module `app/services/intro_fetch.py`; `extract_arxiv_intro_context` in miner.py is refactored
  to call it (the miner's seminal-citation sentence scan stays in miner.py — only the
  fetch/strip/cache layer moves). Miner behavior is unchanged except it now hits the cache.

### D4. Budget & caching — `paper_intros` cache table + per-evidence excerpt column
Two layers, matching how the data is used:

1. **`paper_intros`** (new table, claim-agnostic raw cache):
   ```
   arxiv_id      VARCHAR(30) PRIMARY KEY
   intro_text    TEXT            -- tag-stripped, ≤ 40 KB
   http_status   SMALLINT        -- 200 | 404 | 0 (timeout/error) | 204 (stub)
   source        VARCHAR(10)     -- 'ar5iv' | 'arxiv'
   fetched_at    TIMESTAMP NOT NULL
   ```
   1,610 distinct papers in evidence today → worst-case ~64 MB if every intro were 40 KB;
   realistically ~15 MB. Trivial for Postgres.
2. **`evidence.intro_excerpt`** (new nullable TEXT column, ≤ 1,200 chars) + index-friendly
   `evidence.intro_fetch_attempted_at TIMESTAMP NULL`. The excerpt is claim-specific (keyword
   selection against *this* claim), so it lives on the evidence row; juries read it with zero joins
   against HTTP.

**Budgets (no fetch storms):**
- Linker v2 forward path: ≤ 4 intro fetches per claim run (only for rescue cases, D1).
- Jury drains: excerpt backfill task processes ≤ 30 evidence rows/run, 0.5 s spacing — same pacing
  discipline as the miner's `arxiv_intro_cap`.
- Cache hit = no HTTP, ever. At 1,610 papers the steady state is almost all hits.

### D5. Coverage targeting — both, with the sweep carrying the real weight
- **Forward pipeline:** D1 + D2 land in linker v2 and juries; every future claim benefits.
- **Retroactive sweep (the lever for the 300):**
  - **D0:** new beat task `drain_evidence_all_pages` — hourly, iterates pages with unverified
    established claims having < 2 evidence, batch 10 claims/run (reuses
    `drain_evidence_for_page` logic minus the hardcoded page). At ~10/hour the 171-claim backlog
    drains in < 2 days of wall time; the 7-day cooloff then governs steady state. The weekly p57
    entry is retired (superseded).
  - **Excerpt backfill sweep** `backfill_intro_excerpts` — every 2 h, targets (a) the 106
    NULL-abstract arXiv rows, (b) jury-pending rows with terse abstracts, oldest first.
  - The 148 unverified-with-evidence claims are *not* a retrieval problem (avg 3.9 votes already);
    they are trust-calculator threshold territory and explicitly out of scope here.

---

## 3. Architecture delta

```
                       ┌──────────────────────┐
 ADS/S2 search ──────► │ verify_for_claim     │──── quality < floor & arxiv_id?
 (+1 full:"…" query)   │ (abstract first)     │           │ yes (≤4/claim-run)
                       └──────────────────────┘           ▼
                                  ▲              ┌──────────────────┐    miss   ┌──────────┐
                                  │ rescue       │ paper_intros     │◄─────────►│ ar5iv /  │
                                  └──────────────│ cache (PG)       │   fetch   │ arxiv.org│
                                                 └──────────────────┘           └──────────┘
                                                          │ raw intro
                                                          ▼
                                              deterministic keyword excerpt
                                              (claim-specific, ≤1200 chars)
                                                          │
                                                          ▼
                                              evidence.intro_excerpt ──► stance juries
                                                                         (abstract + excerpt)
```

---

## 4. Exact changes (file / function / anchor)

| # | File | Anchor | Change |
|---|---|---|---|
| 1 | new `app/services/intro_fetch.py` | — | `fetch_intro(arxiv_id, db) -> str|None` (cache-first, ar5iv→arxiv fallback, stub guard, writes `paper_intros`); `select_excerpt(intro_text, claim_text, cap=1200) -> str|None` (keyword-sentence scorer reusing `_claim_keywords`) |
| 2 | Alembic migration | single head after `survey_releases_catalog_v1` | `paper_intros` table; `evidence.intro_excerpt TEXT NULL`; `evidence.intro_fetch_attempted_at TIMESTAMP NULL` |
| 3 | `app/services/paper_search.py` | `verify_for_claim` L435; hard gate L449; overlap L459–465 | optional `intro_provider` callable param; missing-abstract rescue; below-floor overlap recompute on `abstract+excerpt` (D1) |
| 4 | `app/services/paper_search.py` | `_llm_stance_verify` L399 | optional `extra_context: str` appended (≤800 chars) when abstract < 600 chars |
| 5 | `app/agent_loop/citation_context/miner.py` | `extract_arxiv_intro_context` L259 | delegate fetch/strip to `intro_fetch.fetch_intro`; keep seminal-sentence scan local; signature unchanged |
| 6 | `app/agent_loop/tasks.py` | `run_stance_jury_for_evidence` gate L2717, prompt L2728–2736 | gate: `abstract>=100 OR intro_excerpt>=200`; prompt: append excerpt block (≤1200) |
| 7 | `app/agent_loop/tasks.py` | `run_stance_jury_single` gate L4698, prompt L4709–4715 | same gate; excerpt ≤800 in prompt |
| 8 | `app/agent_loop/tasks.py` | `drain_stance_jury_backlog` L2871–2872; `drain_jury_fast_pass` L4821–4822, L4857–4858 | SQL filters: `... >= 100 OR length(intro_excerpt) >= 200` |
| 9 | `app/agent_loop/tasks.py` | `_run_evidence_linker_v2` query-gen L1790–1820 | add one `full:"<keyphrase>"` ADS query variant; pass `intro_provider` into `verify_for_claim` |
| 10 | `app/agent_loop/tasks.py` | new tasks near L1917 | `drain_evidence_all_pages` (D0) and `backfill_intro_excerpts` (D5), both with run caps + spacing |
| 11 | `app/agent_loop/worker.py` | beat dict L263–268 | replace `drain-evidence-p57` with `drain-evidence-all` (hourly); add `backfill-intro-excerpts` (q2h); mirror in `_REGISTRY_BEAT_ENTRIES` L296 |

Settings additions (`app/config.py`): `INTRO_FETCH_ENABLED: bool = True`,
`INTRO_FETCH_TIMEOUT_S: int = 20`, `INTRO_EXCERPT_MIN_CHARS: int = 200`,
`INTRO_FETCH_PER_LINKER_RUN: int = 4`, `INTRO_BACKFILL_BATCH: int = 30`,
`EVIDENCE_DRAIN_GLOBAL_BATCH: int = 10`.

---

## 5. Platoon assignment

No new inference steps are introduced — excerpt selection is deterministic Python. Existing
assignments, with the only change being slightly longer prompts:

| Step | Model | Why | Cost/speed |
|---|---|---|---|
| Linker query gen (+`full:` variant) | existing `query_gen` route (4 local models via `llm_routing`) | unchanged; string template change only | free/local |
| Stance pre-judge in `verify_for_claim` | **Nutty** (gpt-oss:20b, Ollama local) | already the verify model (paper_search.py:396); +800 chars context is well inside its window; fast JSON-safe | free, ~1–2 s |
| Fast jury `run_stance_jury_single` | **Mima** (qwen3.6:35b-a3b-nvfp4, `STANCE_JURY_FAST_MODEL`) | unchanged; +800 chars; `no_think` already set; batch-guard (`guard_batch_model`) keeps premium models out | free, local |
| 4-model jury | gemini-2.5-flash + Groq gpt-oss-20b + Mima + **Atom-7b** (existing `STANCE_JURY_MODELS`, tasks.py:110) | unchanged roster; +~300 tokens/juror is inside free-tier and local budgets | free tiers / local |
| Intro fetch + excerpt | none (HTTP + regex) | deterministic, auditable, no transcription risk | ~0.4 s/paper, cached forever |

Explicitly **not** assigned: Rakon/Buddle (deepseek-r1) — empty-content JSON limitation makes them
unusable for the jury paths (TOOLS.md platoon limits); no Opus/Sonnet anywhere in these loops
(batch guard already enforces).

---

## 6. Tori dispatch spec (staged order — later stages depend on earlier)

1. **Migration + models** (item 2): `paper_intros`, `evidence.intro_excerpt`,
   `evidence.intro_fetch_attempted_at`. Verify single Alembic head. **Deploy gate: nothing reads
   the columns yet — safe.**
2. **`intro_fetch.py`** (item 1) + unit tests: cache hit/miss, stub guard (feed a <20 KB body),
   404 path, excerpt determinism (same input → same excerpt).
3. **Miner delegation** (item 5): refactor `extract_arxiv_intro_context` to use the cache. Run
   `run_ccm_cycle(dry_run=True)` on 2 maps and diff context output against pre-refactor — must be
   identical sentences.
4. **`verify_for_claim` rescue + `_llm_stance_verify` context** (items 3–4). Unit test: record with
   `abstract=None, arxiv_id=<cached>` passes gates and yields quality > 0.
5. **Jury prompt + gate changes** (items 6–8). Test: evidence row with NULL abstract but 1,200-char
   excerpt gets jury votes end-to-end on staging DB.
6. **Linker `full:` variant + intro_provider wiring** (item 9).
7. **New beat tasks + schedule swap** (items 10–11). Start `drain_evidence_all_pages` with
   `EVIDENCE_DRAIN_GLOBAL_BATCH=5` for the first 24 h, then raise to 10 after checking ADS quota
   burn (each claim run ≈ 6 ADS queries; 10 claims/h ≈ 1,440 queries/day — within ADS's 5,000/day
   personal limit, but verify the shared-key headroom before raising).
8. **Kick `backfill_intro_excerpts`** manually once; confirm the 106 NULL-abstract rows get
   excerpts or a recorded failure status.

Do **not** delete the weekly p57 beat entry until step 7's hourly task has produced one clean run
(same staging discipline as the Surveys-tab fork removal).

---

## 7. Acceptance criteria

1. **Cache behavior:** second `fetch_intro` call for the same arXiv ID issues zero HTTP requests
   (assert via mock); failed fetches are not retried within 30 days.
2. **Fetch success:** ≥ 80% of a 50-paper random sample from `evidence.arxiv_id` yields a stored
   intro ≥ 2,000 chars (measured: expect ~100% based on §1.3, threshold left conservative).
3. **Rescue path live:** at least 50 of the 106 NULL-abstract arXiv evidence rows carry
   `intro_excerpt` after one backfill cycle, and previously jury-invisible rows appear in
   `drain_jury_fast_pass` candidate counts.
4. **Jury integrity:** for evidence with both abstract and excerpt, prompts contain both blocks
   (log assertion); vote JSON parse rate does not regress (baseline: current parse failures raise
   and retry — compare retry counts week-over-week).
5. **Coverage movement (the headline number):** zero-evidence *established* claims drop from 171
   to ≤ 60 within 14 days of `drain_evidence_all_pages` going live. (Not all will resolve — some
   claims legitimately find no papers; those must show `evidence_search_attempted_at` set, i.e.
   searched-and-empty rather than never-searched. "Never-searched zero-evidence established"
   must be ≈ 0.)
6. **No regression in miner:** CCM dry-run context output unchanged post-refactor (step 3 diff).
7. **Budget respected:** no run logs more than the configured fetch cap; ADS daily usage stays
   under the agreed headroom.

---

## 8. Risks and non-goals

- **ar5iv drift:** it is a labs service; the stub guard plus `http_status` bookkeeping means a
  future outage degrades to "abstract-only behavior," never blocks juries.
- **Excerpt ≠ paper's stance:** an introduction often *describes* a claim while the paper goes on
  to challenge it. The jury prompt labels the block "Introduction excerpt" so jurors weigh it as
  framing, not findings; the abstract remains primary when present. This is also why excerpts never
  replace abstracts when both exist.
- **Non-goal:** the 122 debate-type zero-evidence claims (adversarial/research-ideas lanes own
  those) and the 148 unverified-with-evidence claims (trust-calculator thresholds; separate audit
  if Papa wants it).
- **Non-goal:** TF-IDF classification (`arxiv_classifier.py`) stays abstract-only — intros would
  add ~80 fetches/day for the daily feed and dilute term vectors with boilerplate.

---

*Evidence for every count in this doc: live queries against `nebulamind-postgres-1` and curl probes
run 2026-06-12 on the Mac Studio; file/line anchors verified against the working tree at
`~/NebulaMind/NebulaMind/backend`.*
