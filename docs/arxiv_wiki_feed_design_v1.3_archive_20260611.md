# arXiv → Wiki Feed Design v1

**Owner:** Kun 🔬  ·  **Implementer:** Tori  ·  **Status:** v1.3 — 2026-05-25 Track B Phase 2 validator design
**Date:** 2026-05-10 (v1) · 2026-05-12 (v1.1) · 2026-05-20 (v1.2) · **2026-05-25 (v1.3 — current)**
**Filename:** `docs/arxiv_wiki_feed_design_v1.md`
**Path note:** Main session referenced `~/NebulaMind/docs/`; real docs dir is `~/NebulaMind/NebulaMind/docs/`. Saved at the real path.

**Companion docs (read first):**
- `docs/beat_schedule_v3.md` — full Celery beat layout this pipeline plugs into.
- `docs/ollama_model_policy_v1.md` — platoon roster (Blanc / Mima / Takji / Rakon / Buddle / ArxivBot) and capability matrix.
- `docs/research_ideas_design_v1.md` — Phase 3 design for the *forward-looking* layer (datasets, hypotheses); this doc is its *backward-looking* sibling (papers → evidence).
- `docs/autowiki_surveys_v1.md` — survey-directory autoresearch loop, same idempotency/audit shape.
- `~/.openclaw/agents/kun/workspace/설계_AgentLoopQualityGuards_v1.md` — quality guards (multi-vote dedup, length retention, claim preservation, filler pre-filter) that every editor including ArxivBot now passes through.

---

## 0. TL;DR

Daily Celery task fetches new astro-ph papers from arXiv, classifies each one against the live wiki corpus (TF-IDF cosine, no LLM), and routes the paper to one of four outcomes:

- **`claim_evidence`** — paper matched a specific claim → ADS-verify → insert `Evidence` row with `source_channel='arxiv_ingest'`.
- **`page_extension`** — paper matched a page but no claim → ArxivBot drafts a 1–3 sentence edit → `EditProposal` enters the council queue (subject to all Quality Guards).
- **`new_topic_candidate`** — paper matched no existing page above floor → cluster against pending candidates → when cluster size ≥ 3, emit `NewPageProposal` to moderator.
- **`unrelated`** — only an audit row.

The directive (Papa, 2026-05-10): **arXiv updates feed the wiki, not just the newsletter.** v1.2 confirms the pipeline is live and high-volume on intake (~50 papers/day) but yield-collapsed on the most important output (`claim_evidence`: 0 in last 7 days; 10 in last 30). The §11 P0 below addresses that.

---

## 1. Live state baseline (2026-05-20 production audit, Mac Studio)

Direct queries against prod Postgres on `100.84.12.101`:

| Metric | v1 (2026-05-10) | v1.1 (2026-05-12) | **v1.2 (2026-05-20)** | Trend |
|---|---:|---:|---:|---|
| `arxiv_papers` total | 687 | 687 | **1,243** | ↑ +556 in 8 days (~70/d) — intake healthy |
| `arxiv_papers` 7-day intake | n/a | n/a | **356** (~51/d) | ≥ target 30/d ✅ |
| `arxiv_papers` 24h | n/a | n/a | 73 | within range |
| match_type 7d: `unrelated` | n/a | n/a | **323 (90.7%)** | very high — see §11.1 |
| match_type 7d: `new_topic_candidate` | n/a | n/a | 30 | clustering active |
| match_type 7d: `claim_evidence` | n/a | n/a | **2** | very low |
| match_type 7d: `page_extension` | n/a | n/a | **1** | very low |
| `evidence` rows via arXiv channels (total) | 9 | 3 | **13** | recovering |
| `evidence` rows via arXiv channels (7d) | n/a | n/a | **0** | 🚨 P0 — see §11.2 |
| `evidence_inserted` audit rows 30d | n/a | n/a | 10 | 0.33/day, target ≥ 5/day |
| `verify_failed` 30d | n/a | 8 (7d) | 8 | ADS sometimes 500s |
| `verify_rejected` 30d | n/a | n/a | **21** | ADS rejects ~0.7/d — see §11.2 |
| ArxivBot proposals 7d (APPROVED/REJECTED) | n/a | 155 / 7 | **0 / 1** | quality guards bit hard |
| ArxivBot proposals 30d (APPROVED/REJECTED) | n/a | 950 / 2456 | **305 / 2,285** (11.8%) | dropped from 27.9% — guards working |
| ArxivBot proposals 24h | n/a | 24 / 1 | **0 / 0** | flow paused — see §11.3 |
| `NewPageProposal` pending | 57 | 49 | **79** | moderation surface still absent — §11.4 |
| `NewPageProposal` rejected | n/a | n/a | 38 | someone *is* SQL-rejecting |
| `centroid_similarity` distribution (pending) | all 0.0 | all 0.0 | **min 0.0 / max 0.42 / avg 0.094** | partial fix — §11.5 |

### What this tells us (one-paragraph reading)

Intake is solid. The classifier is doing its job — 90.7% `unrelated` is the **honest** answer when the wiki has 43 pages and astro-ph publishes 80–100 papers/day across four subcategories. The actual problem is that **of the ~9% of papers the classifier judges related, fewer than 1% become evidence** — the `claim_evidence` path narrows from ~30 candidates/week (papers ≥ 0.45 cosine on a claim) to 0 actual `Evidence` rows. The verify-step is the leak. Meanwhile the Quality Guards landed two weeks ago (`설계_AgentLoopQualityGuards_v1.md` P0/P1) and they correctly dropped ArxivBot's approval rate from 27.9% to 11.8% — that is the system working, not failing. The pipeline is **intake-healthy, evidence-starved, edit-throttled, and moderation-blocked**, in that order.

---

## 2. End-to-end pipeline (live in production)

```
                 ┌──────────────────────────────────────────────────────┐
                 │            Celery beat: crontab(hour=1, minute=0)    │
                 │      [fetch_arxiv_daily — tasks.py:4335-4447]        │
                 │      Trigger: UTC 01:00 = KST 10:00                  │
                 └────────────────┬─────────────────────────────────────┘
                                  │
              ┌───────────────────┴──────────────────────┐
              │  for cat in ARXIV_CATEGORIES (4 cats):   │
              │    papers = _parse_arxiv_rss(cat)        │
              │  (astro-ph.GA, .CO, .HE, .SR)            │
              └───────────────────┬──────────────────────┘
                                  │
                  ┌───────────────┴─────────────────┐
                  │ dedup on arxiv_id (DB query)    │
                  └───────────────┬─────────────────┘
                                  │
                  ┌───────────────┴─────────────────────────────┐
                  │ LLM summary (ArxivBot, 2-3 sent., for       │
                  │ newsletter) + _match_wiki_pages (legacy KW) │
                  └───────────────┬─────────────────────────────┘
                                  │
                       INSERT ArxivPaper
                                  │
                   ┌──────────────┴──────────────┐
                   │ ARXIV_INTEGRATION_ENABLED?  │
                   └──────────────┬──────────────┘
                          (True)  │
                                  ▼
                ┌──────────────────────────────────────────────┐
                │  classify_match_type(paper, db)              │  arxiv_classifier.py
                │  TF-IDF cosine, no LLM, no embeddings        │
                │  refresh_page_vectors() at the top of fetch  │
                └──────────────┬───────────────────────────────┘
                               │
        ┌──────────────────────┼──────────────────────┬──────────────────┐
        │                      │                      │                  │
        ▼                      ▼                      ▼                  ▼
 claim_evidence          page_extension         new_topic_         unrelated
  (claim cos ≥ 0.45)      (page cos ≥ 0.50)      candidate          (audit row only)
        │                      │                  (page cos ≥ 0.30)
        ▼                      ▼                      │
 handle_claim_evidence   handle_page_extension        ▼
  - paper_search.         - skip-if-pending     handle_new_topic
    verify_for_claim        (1 per page)         - cluster on TF-IDF
    (ADS lookup)          - daily cap            - centroid sim ≥ 0.25
  - INSERT Evidence       - LLM draft (_chat)   - aggregate into
    source_channel=         ↳ ArxivBot model      NewPageProposal
    'arxiv_ingest'        - INSERT              - Discord notify when
  - schedule stance jury    EditProposal          cluster ≥ MIN_SIZE
  - recalculate_trust       (→ council queue)
    .delay(page_id)         (→ Quality Guards)
        │                      │                      │
        └──────────────────────┴──────────────────────┘
                               │
                               ▼
                    INSERT ExternalSourceLog
              (audit row — every paper produces ≥1)
                               │
                               ▼
              ┌──────────────────────────────────────┐
              │   Daily sweep — UTC 02:15            │
              │   retry_unprocessed_arxiv_papers     │
              │   (papers with NULL match_type < 24h)│
              └──────────────────────────────────────┘
                               │
                               ▼
              ┌──────────────────────────────────────┐
              │   Daily summary — UTC 01:30          │
              │   send_arxiv_daily_summary → Discord │
              └──────────────────────────────────────┘
```

Every step survives a worker crash because of the audit log + idempotency layer (§5, §6).

---

## 3. arXiv polling strategy

### 3.1 Categories

Hard-coded in `tasks.py:ARXIV_CATEGORIES`:

```python
ARXIV_CATEGORIES = [
    "astro-ph.GA",   # Astrophysics of Galaxies
    "astro-ph.CO",   # Cosmology and Nongalactic Astrophysics
    "astro-ph.HE",   # High Energy Astrophysical Phenomena
    "astro-ph.SR",   # Solar and Stellar Astrophysics
]
```

Decision rationale: these four cover ≥95% of the topics our current 43 wiki pages map onto. `.EP` (Earth & Planetary) and `.IM` (Instrumentation & Methods) are intentionally excluded — they push the unrelated-rate higher and current page coverage is thin there. **Add `.EP` only when planetary pages grow past 5** (we're at 2: `planetary-formation`, `asteroid-belt`).

### 3.2 Cadence

| Schedule | Cron (UTC) | KST | Behavior |
|---|---|---|---|
| Primary fetch | `hour=1, minute=0` | 10:00 | One pass over all 4 categories. astro-ph announces around UTC 20:00; UTC 01:00 catches yesterday's batch with ~5h lag. |
| Retry sweep | `hour=2, minute=15` | 11:15 | `retry_unprocessed_arxiv_papers` re-runs classifier on rows with `match_type IS NULL AND created_at > now() - 24h`. Closes the per-paper-commit + classifier-crash gap. |
| Daily summary | `hour=1, minute=30` | 10:30 | `send_arxiv_daily_summary` posts a 5-line Discord digest. Pulls counts from `ExternalSourceLog` for the last 24h. |

Single-pass intake (not multi-pass): astro-ph RSS is monotonic on `published`; one polling window catches everything since the last one, provided the date param is set (§3.4). No webhook from arXiv — RSS only.

### 3.3 Query construction

Current implementation reads the arXiv RSS feed via:

```
http://export.arxiv.org/rss/{category}
```

`_parse_arxiv_rss(category, limit)` parses the Atom feed, extracts `<id>`, `<title>`, `<summary>`, `<author>`, `<arxiv:primary_category>`, `<published>`, and a normalized `arxiv_id` (regex strip of `arXiv:` prefix and version suffix).

Cap: `limit` was 8/category in v1, raised to 20/category in v1.1 (item #8 of Phase C), confirmed via the 73 papers/24h observed in v1.2. With 4 categories × 20 = 80/day max — matches astro-ph's announcement volume.

**Gap (§11.6):** RSS doesn't accept a `published_after` parameter, so dedup at insert time is doing the work. For high-volume catch-up (e.g., after a worker outage), migrate to the arXiv API (`http://export.arxiv.org/api/query`) which *does* support date filtering. Not urgent: 8-day uptime gives confidence dedup is sufficient.

### 3.4 What we *don't* poll

- **No keyword queries.** All filtering happens downstream in `classify_match_type`. Keeps the polling layer purely time-based.
- **No author / institution filters.** Same reason.
- **No cross-listing handling.** A paper cross-listed to both `astro-ph.GA` and `astro-ph.CO` is fetched twice; dedup on `arxiv_id` collapses to one row.

---

## 4. Relevance scoring — how a paper matches a wiki page/claim

`classify_match_type(paper, db)` in `app/services/arxiv_classifier.py`. Pure Python, no embeddings, no LLM, no external API.

### 4.1 Corpus construction

`_corpus` (module-level cache) holds:
- `idf` — global token-level IDF computed from all wiki page content
- `page_vectors` — `page_id → TF-IDF dict`
- `page_content_map` — `page_id → raw text` (for audit + future hover)

`refresh_page_vectors()` rebuilds it; `_ensure_corpus()` lazily triggers on first call after a process restart. v1.1 Phase C item #7 added `refresh_page_vectors()` at the **top of `fetch_arxiv_daily`** — so the corpus reflects any wiki edits from the last 23 hours before today's intake is classified.

### 4.2 Paper vectorization

`_paper_text(paper)` concatenates `title + abstract[:1200]`. Tokenize → drop the astronomy-extended stopword list (in `arxiv_classifier.py:_STOPWORDS`) → drop tokens shorter than 3 chars → compute TF-IDF dict using the cached `idf`.

The LLM-generated `abstract_summary` (ArxivBot) is **NOT** used for classification — only `title + abstract`. This is intentional: keeps the routing decision deterministic and independent of LLM noise.

### 4.3 Decision matrix

Compute cosine of paper vs each page; sort descending. Take the top page. Then compute cosine of paper vs each `Claim` belonging to the top page; sort descending.

| Condition (in order) | Label | Config knob |
|---|---|---|
| `best_claim_score ≥ 0.45` | `claim_evidence` | `ARXIV_CLAIM_MATCH_THRESHOLD = 0.45` |
| else `best_page_score ≥ 0.50` | `page_extension` | `ARXIV_PAGE_EXTENSION_THRESHOLD = 0.50` |
| else `best_page_score ≥ 0.30` | `new_topic_candidate` | `ARXIV_PAGE_MATCH_THRESHOLD = 0.30` |
| else | `unrelated` | — |

v1.1 → v1.2 change: `ARXIV_CLAIM_MATCH_THRESHOLD` lowered from 0.55 → 0.45 (Phase C item #4). Did not increase yield as projected — see §11.2 for diagnosis.

### 4.4 Returned metadata

`classify_match_type` returns `(match_type, meta)` where `meta` includes:
- `best_page_id`, `best_page_score`
- `best_claim_id`, `best_claim_score`
- `top_pages` — top-3 candidates with scores (for audit + later hover UX)
- `top_claims` — top-5 candidates with scores
- `matched_keywords` — tokens that contributed most to the page match

`meta` is JSON-serialized into `arxiv_papers.match_meta`. It's the basis for any future "why was this paper rejected / routed here?" debugging.

### 4.5 Why no embeddings (yet)

`ARXIV_MATCH_USE_EMBEDDINGS = False` exists in config but the path isn't implemented. TF-IDF is ~10ms/paper after corpus warmup; embeddings would be 50–200ms/paper plus a ~200MB model load. Worth doing if §11.2 diagnosis points to vocabulary mismatch (e.g., "baryonic feedback" paper vs "AGN quenching" page) — currently unclear whether the leak is here or in `verify_for_claim`. **Defer to Phase D pending diagnosis.**

---

## 5. Evidence candidate creation flow

`handle_claim_evidence(arxiv_id, meta, db)` in `arxiv_ingest.py`. Six steps:

1. **Idempotency check** — `_already_processed(arxiv_id, source_channel='arxiv_ingest')`. If an Evidence row already exists for this paper from this channel, return early.
2. **Per-paper evidence cap** — count existing Evidence rows for `arxiv_id`. If ≥ `ARXIV_MAX_EVIDENCE_PER_PAPER = 3`, write `skipped_evidence_cap` audit row and return.
3. **Claim existence check** — re-fetch `Claim` by `best_claim_id`. If it was deleted between classification and this handler, write `skipped_claim_missing` and return.
4. **ADS verification** — call `paper_search.verify_for_claim(arxiv_id, claim_text)`. This hits the ADS API, looks up the paper's metadata, and judges whether the paper actually supports the claim (LLM-assisted stance check inside). Returns either a verified `PaperSearchHit` or `None`.
   - If raises → write `verify_failed`, return.
   - If returns `None` → write `verify_rejected`, return.
5. **Insert Evidence row** — `Evidence(arxiv_id=..., claim_id=..., source_channel='arxiv_ingest', stance='supports', authors=..., year=..., quality=..., summary=...)`. Stance defaults to `'supports'` and gets refined by the stance jury (§6 quality gating).
6. **Trust recompute** — `recalculate_trust.delay(page_id)` to update the page's overall trust score with the new evidence weight.

Schema (live):

```sql
-- evidence (existing table; arxiv pipeline writes a subset of columns)
CREATE TABLE evidence (
    id            SERIAL PRIMARY KEY,
    claim_id      INT NOT NULL REFERENCES claims(id),
    arxiv_id      VARCHAR(64),        -- nullable: other source_channels don't have it
    doi           VARCHAR(255),
    title         VARCHAR(512),
    authors       VARCHAR(1024),
    year          INT,
    summary       TEXT,
    stance        VARCHAR(32),        -- supports | refutes | neutral
    quality       NUMERIC(3,2),       -- 0..1, from verify_for_claim
    source_channel VARCHAR(64),       -- 'arxiv_ingest' for this pipeline
    superseded_at TIMESTAMP,
    created_at    TIMESTAMP DEFAULT NOW(),
    updated_at    TIMESTAMP DEFAULT NOW()
);
```

No new tables required for this pipeline. The only schema touch is the existing `external_source_log` (audit) — no migrations pending.

---

## 6. Quality gating — what filters before evidence/edits hit the DB

Six overlapping layers, in order of encounter:

### 6.1 Dedup at RSS fetch (`tasks.py:4359`)

```python
exists = db.query(ArxivPaper).filter(ArxivPaper.arxiv_id == arxiv_id).first()
if exists: continue
```

A paper saved on a prior fetch is skipped entirely — no re-classification, no LLM cost, no evidence row. **First and cheapest filter.**

### 6.2 Idempotency at evidence insertion

```python
_already_processed(db, arxiv_id, source_channel='arxiv_ingest')
```

Keyed on `(arxiv_id, source_channel)`. A paper inserted via `wikipedia_biblio` does NOT block re-insert via `arxiv_ingest`, but is correctly attributed by channel. Live state: 13 `arxiv_ingest` rows vs 11,129 `wikipedia_biblio` rows — separation is working.

### 6.3 Per-paper evidence cap

```python
ARXIV_MAX_EVIDENCE_PER_PAPER = 3
```

A single very-relevant paper can't saturate evidence slots across many claims on the same page.

### 6.4 Per-page edit throttles (`handle_page_extension`)

Three checks before generating an LLM draft:

| Check | Audit decision when triggered |
|---|---|
| `ARXIV_SKIP_PAGE_IF_PENDING_PROPOSALS = True` and any pending proposal exists | `skipped_pending_proposals` |
| `ExternalSourceLog` already has `(source='arxiv', external_id=arxiv_id, page_id, decision='page_extension_proposed')` | (silent skip) |
| Today's count of `page_extension_proposed` for this page ≥ `ARXIV_MAX_PAGE_EDITS_PER_PAGE_PER_DAY = 1` | `skipped_daily_cap` |

Effective cap: "1 active proposal per page at a time" + a daily cooldown.

### 6.5 ADS verification floor (`paper_search.verify_for_claim`)

Hits ADS, judges fit-to-claim, returns a `quality ∈ [0, 1]`. Acts as a quality floor; below threshold (defined inside `paper_search.py`) returns `None` → `verify_rejected`. **This is currently the dominant leak — see §11.2.**

### 6.6 Agent-Loop Quality Guards (post-proposal, council-side)

Every `EditProposal` from `handle_page_extension`, like every editor's, passes through:

| Guard | Source | Effect on ArxivBot |
|---|---|---|
| Multi-vote dedup (single agent_id counts once) | `설계_AgentLoopQualityGuards_v1.md` §1.5 | Stops vote inflation; ArxivBot can't approve alone |
| Length-retention guard (≥ 80% of populated page) | same §P0.2 | Blocks proposals that gut the page |
| Claim-preservation guard (≥ 75% of linked-claim tokens retained) | same §P0.3 | Stops ArxivBot from inadvertently dropping claims |
| Generic-filler pre-filter (≥ 3 hits → reject) | `app/services/content_guards.py` | Filters "plays a crucial role" / "complex and dynamic field" / etc. |
| Tiered VOTE_THRESHOLD (2/3/4 by health) | `vote_threshold_for_page` | High-health pages need 4 votes; new pages still 2 |

Net effect: ArxivBot 30d approval rate dropped from 27.9% → 11.8% in 8 days. **This is the system working as intended** — the pipeline's job is to feed *candidates*, not auto-approvals.

### 6.7 Stance jury (deferred, post-insertion)

A separate beat task `drain_stance_jury_backlog` (hourly) revisits newly-inserted Evidence rows and refines `stance` from the default `'supports'`. Currently scheduled but the arXiv pipeline doesn't explicitly enqueue — see §11.7.

---

## 7. Beat task registration

Lives in `backend/app/agent_loop/worker.py:beat_schedule`. Current entries relevant to this pipeline:

```python
"fetch-arxiv-daily": {
    "task": "app.agent_loop.tasks.fetch_arxiv_daily",
    "schedule": crontab(hour=1, minute=0),       # UTC 01:00 = KST 10:00
},
"send-arxiv-daily-summary": {
    "task": "app.agent_loop.tasks.send_arxiv_daily_summary",
    "schedule": crontab(hour=1, minute=30),      # UTC 01:30 = KST 10:30
},
"retry-unprocessed-arxiv-daily": {
    "task": "app.agent_loop.tasks.retry_unprocessed_arxiv_papers",
    "schedule": crontab(hour=2, minute=15),      # UTC 02:15 = KST 11:15
},
"cluster-new-topic-candidates-daily": {
    "task": "app.agent_loop.tasks.cluster_new_topic_candidates",
    "schedule": crontab(hour=2, minute=0),       # UTC 02:00 = KST 11:00
},
"drain-stance-jury-hourly": {
    "task": "app.agent_loop.tasks.drain_stance_jury_backlog",
    "schedule": crontab(minute=0),               # every hour at :00
},
```

Plus `recalculate_trust.delay(page_id)` fires event-driven from `handle_claim_evidence` (no beat slot).

### Sequencing intent

- **01:00 fetch** → 01:30 summary lets Papa see "what landed" before lunch (KST 10:30).
- **02:00 cluster sweep** is a secondary pass over `new_topic_candidate` rows (the per-paper handler clusters opportunistically; this catches anything missed).
- **02:15 retry sweep** picks up papers where `match_type IS NULL` — handles transient classifier failures and per-paper commit gaps.
- **Hourly stance drain** keeps the stance jury moving (also used by `wikipedia_biblio` and other channels).

### Slots NOT used by this pipeline

The wider beat layout in `docs/beat_schedule_v3.md` includes adversarial pass (UTC 04:00), temporal decay (UTC 05:00), human overrides sweep (UTC 06:00), survey-directory weekly audits (Sundays), and the autowiki loop (every 5 min). None of those write to `arxiv_papers` directly; they consume the Evidence rows this pipeline produces.

---

## 8. Platoon assignment

Per Papa's standing rule: every cron/ingest/scheduler design names the model owning each step (Blanc / Mima / Takji / Rakon / Buddle / ArxivBot) with capability + cost + speed justification. ArxivBot is the dedicated arxiv-pipeline model; see `docs/ollama_model_policy_v1.md` for the wider roster.

| Step | Model | Cost | Speed | Why this model |
|---|---|---|---|---|
| 3.3 RSS fetch + parse | n/a (HTTP/XML) | $0 | <100 ms/cat | No LLM needed. Pure parsing. |
| 2 / `_match_wiki_pages` legacy keyword dict | n/a (Python regex) | $0 | <1 ms | Newsletter still uses; classifier path ignores. Slated for retirement (§11.10). |
| 4 / `classify_match_type` (TF-IDF) | n/a (Python NumPy) | $0 | ~10 ms/paper | Deterministic. No LLM in the routing decision by design — keeps routing reproducible. |
| 4 / abstract_summary (ArxivBot per-paper) | **ArxivBot** (`qwen2.5:7b` via `app/levels.py` editor role) | $0 (local) | ~2-3 s/paper | Cheap, fast, 2-3 sentence newsletter blurb. No quality gates apply because not used for routing. |
| 5 / `paper_search.verify_for_claim` (ADS check + stance pre-judgement) | **Rakon** (`deepseek-r1:14b`) when LLM stance pre-judge is needed | $0 (local) | ~5-15 s/paper | R1 family is good at "does this abstract support this claim" inference; conjunctive rubric. |
| 6.4 / `handle_page_extension` LLM draft | **ArxivBot** (single-model `_chat`, not parallel) | $0 (local) | ~10-20 s/draft | v1.1 fix: downgraded from 4-way parallel to single-model `_chat` because page_extension volume is naturally low (~1-2/week post-guards) and parallel was overkill. |
| 6.6 / council vote (reviewers) | **Mima** (`qwen2.5:14b`) + **Takji** (`llama3.1:8b`) + **Buddle** (`deepseek-r1:32b`) panel | $0 (local) | ~30-60 s/proposal | Standard 3-vote panel per Quality Guards; deduplicated by `agent_id`. |
| 6.7 / stance jury (refine `'supports'`) | **Rakon** (`deepseek-r1:14b`) | $0 (local) | ~5 s/evidence | Stance is a 3-way classification; R1-14b is the smallest model that reliably distinguishes supports/refutes/neutral with conjunctive rubric. |
| 7 / daily summary narration | **Blanc** (`qwen2.5:7b`) | $0 (local) | <2 s | 5-line Discord digest, ≤200 tokens. Smallest model producing coherent Korean+English prose. |
| 7 / `recalculate_trust` | n/a (NumPy) | $0 | <100 ms/page | Deterministic math over `claim_evidence` weights. |

**Total LLM cost per day: $0.** Everything runs on the local Mac Studio Ollama stack. No external paid API call in this pipeline.

**Capability rationale (one paragraph):** ArxivBot owns generation lines because qwen2.5:7b is the right tradeoff for high-volume short-form output (newsletter blurbs, page-extension drafts) — fast enough to keep the fetch under 5 minutes total even at 80 papers/day, accurate enough that Quality Guards catch its remaining noise. Rakon (R1-14b) owns the inference lines (verify-for-claim, stance jury) because R1's chain-of-thought is the load-bearing capability for "does evidence support claim?" — the 32b variant is overkill for stance, and the 7b doesn't reliably distinguish supports vs neutral on borderline abstracts. Mima/Takji/Buddle form the council panel (not arxiv-specific). Blanc handles the narration end (digest) because it just needs to read a count and write a friendly summary — smallest viable model.

---

## 9. Audit trail — `ExternalSourceLog`

Every handler writes exactly one `ExternalSourceLog` row per paper-event. Schema:

```sql
external_source_log:
  id, source, external_id, page_id, claim_id, decision, notes, created_at
```

Decision values currently emitted by the arxiv pipeline:

| Decision | Handler | Meaning | 30d count |
|---|---|---|---:|
| `evidence_inserted` | `handle_claim_evidence` | Evidence row created | 10 |
| `skipped_no_claim` | `handle_claim_evidence` | meta lacked `best_claim_id` | n/a |
| `skipped_evidence_cap` | `handle_claim_evidence` | ≥ MAX_EVIDENCE_PER_PAPER already | n/a |
| `skipped_claim_missing` | `handle_claim_evidence` | claim deleted between classify and handler | n/a |
| `verify_failed` | `handle_claim_evidence` | `verify_for_claim` raised | 8 |
| `verify_rejected` | `handle_claim_evidence` | `verify_for_claim` returned None | 21 |
| `page_extension_proposed` | `handle_page_extension` | EditProposal inserted | ~30 |
| `skipped_pending_proposals` | `handle_page_extension` | page already has pending | many |
| `skipped_daily_cap` | `handle_page_extension` | daily cap reached | many |
| `page_extension_llm_failed` | `handle_page_extension` | `_chat` raised or returned empty | 0 (post-v1.1 fix) |
| `new_topic_staged` | `handle_new_topic` | added to cluster | 30 (7d) |

This log is the basis for `send_arxiv_daily_summary` and any future dashboard.

---

## 10. Configuration knobs

Live in `app/config.py`. All tunable without code changes (env vars override):

```python
# Master switch
ARXIV_INTEGRATION_ENABLED      = True

# Classifier thresholds
ARXIV_PAGE_MATCH_THRESHOLD     = 0.30   # below → unrelated
ARXIV_PAGE_EXTENSION_THRESHOLD = 0.50   # ≥ this and no claim hit → page_extension
ARXIV_CLAIM_MATCH_THRESHOLD    = 0.45   # ≥ this on best claim → claim_evidence
                                        # (was 0.55 in v1, lowered in v1.1)

# Per-paper caps
ARXIV_MAX_EVIDENCE_PER_PAPER   = 3

# Per-page throttles
ARXIV_MAX_PAGE_EDITS_PER_PAGE_PER_DAY = 1
ARXIV_SKIP_PAGE_IF_PENDING_PROPOSALS  = True

# new_topic clustering
ARXIV_NEW_TOPIC_LOOKBACK_DAYS         = 14
ARXIV_NEW_TOPIC_CENTROID_THRESHOLD    = 0.25   # was 0.40 in v1, tuned to 0.25
ARXIV_NEW_TOPIC_MIN_CLUSTER_SIZE      = 3
NEW_PAGE_PROPOSAL_NOTIFY_BATCH_SIZE   = 5
NEW_PAGE_PROPOSAL_NOTIFY_FLUSH_HOURS  = 24

# Embedding upgrade — wired in config but path not implemented yet
ARXIV_MATCH_USE_EMBEDDINGS     = False  # see §11.8
```

---

## 11. Current gaps (P0 / P1 / P2 — by impact on yield)

### §11.1 P1 — `unrelated` rate is 90.7% — page coverage gap, not bug

7d match_type distribution: 323 unrelated out of 356 papers. This is the classifier's honest answer when 43 wiki pages can't cover what 4 astro-ph subcategories publish. **Not a defect.** But the implication is: the bottleneck for evidence yield isn't the classifier loosening; it's **wiki page coverage**. Phase 3 (Research Ideas) and the renovation work (`설계_WikiRenovation_v1.md`) both depend on the page list growing.

**Action:** none from the arxiv side. The 30 `new_topic_candidate` rows/week are exactly the signal that grows page coverage — when a cluster reaches 3, the `NewPageProposal` is the lever for adding pages. See §11.4.

### §11.2 P0 — `claim_evidence` yield collapsed (7d=0, 30d=10) 🚨

Of the 30+ papers/week the classifier routes to `claim_evidence` (cosine ≥ 0.45 on a specific claim), only ~2/week become actual Evidence rows in good periods, and 0 in the last 7 days. Two leak points:

**(a) `verify_for_claim` ADS rejection rate.** 30d: 21 `verify_rejected` + 8 `verify_failed` = 29 rejections against ~30 candidates routed. ADS rejects nearly everything routed. Hypotheses, in descending probability:

1. **ADS lag.** Fresh arXiv papers (< 48 h) aren't yet in ADS, so `verify_for_claim` returns `None` → `verify_rejected`. Most arXiv papers we fetch are < 24 h old → guaranteed reject. **Most likely cause.**
2. **`verify_for_claim` quality floor too strict.** The LLM stance pre-judge inside `paper_search.py` may be rejecting anything where the abstract doesn't *explicitly* mention the claim's exact terms. Possible.
3. **Claim text too short.** Many claims are 1-2 sentences. ADS metadata + arXiv abstract isn't enough overlap for a confident `supports` judgement.

**(b) Threshold lowering didn't help as projected.** v1.1 dropped `ARXIV_CLAIM_MATCH_THRESHOLD` from 0.55 → 0.45 expecting 3-5× yield. Yield went from 9 → 13 (total) — essentially flat. Confirms the leak is downstream of the classifier.

**Recommended fix sequence (Phase D-1, this week):**

1. **Add a 48h-lag retry path.** When `verify_for_claim` returns `None`, mark the paper for retry 48h later instead of dropping. Schema: add `arxiv_papers.verify_retry_at TIMESTAMP NULL` and a `process_pending_verify_retries` beat task at `crontab(hour=8, minute=0)` UTC.
2. **Split `verify_rejected` into `verify_rejected_ads_lag` vs `verify_rejected_quality`.** Use ADS response status to distinguish "paper not yet in ADS" from "ADS returned the paper but stance LLM said no". Then we know which lever to pull.
3. **Sample 5 `verify_rejected` rows manually** — Kun audits, decides whether the LLM stance judge is too strict.

Owner: Tori (item 1-2, 1d) + Kun (item 3, 1h). **Highest single-impact unblock.**

### §11.3 P1 — ArxivBot 24h proposal volume is 0

A pipeline producing 73 papers/day but 0 ArxivBot proposals/day in the last 24h means **the page_extension path is starved**. 7d page_extension: 1. This is partly correct (the Quality Guards working), but partly suspicious — even at 11.8% approval, 7d should produce some proposals for the council.

Diagnosis hypothesis: when *all* `claim_evidence` route attempts get `verify_rejected`, papers with claim_score ∈ [0.45, 0.55] should *fall back* to `page_extension` if `best_page_score ≥ 0.50`. They don't, because the classifier emits a single label — `claim_evidence` — and the handler returns silently on verify_rejected without re-routing.

**Recommended fix:** when `handle_claim_evidence` writes `verify_rejected`, check if `meta.best_page_score ≥ ARXIV_PAGE_EXTENSION_THRESHOLD` and re-route to `handle_page_extension`. Trivial wiring (5 lines). Owner: Tori, 0.5h.

### §11.4 P1 — Moderation surface for `NewPageProposal` still absent (79 pending) 🚨

The Discord notification links to `/admin/proposals` which doesn't exist. The 79 pending have been there for weeks. The 38 `rejected` ones suggest someone is reviewing via SQL — which doesn't scale.

**Recommendation:** thin React admin page at `/admin/new-page-proposals`:
- Table: slug, title, papers (links), centroid_sim, cluster size, created_at, [Accept] [Reject]
- Backend: `routers/admin_proposals.py` with `POST /api/admin/new-page-proposals/{id}/{accept|reject}` (auth-gated)
- On accept: spawn the wiki-page-creation flow with the cluster's papers pre-loaded as candidate evidence

Owner: Tori, 1.5d. Independent of the §11.2 / §11.3 work — can ship in parallel.

### §11.5 P2 — `centroid_similarity` recompute is partial

v1.2 audit: pending proposals have `centroid_similarity ∈ [0.0, 0.42], avg=0.094`. v1.1's fix landed (recompute on append in `arxiv_ingest.py:385`), but ~half the pending proposals are still 0.0 — likely because they started life as size-1 clusters and never got new papers appended (cluster reset happens on each new candidate, not via the recompute path).

**Recommendation:** when `handle_new_topic` writes a brand-new cluster (size=1), set `centroid_similarity = 1.0` (a single paper is perfectly self-coherent) so the field is a meaningful signal, not a bug-flag. Owner: Tori, 0.25h.

### §11.6 P2 — RSS doesn't accept date filter; depend on dedup

Currently OK because dedup is reliable. Becomes a problem if the worker is offline for > 24h — RSS only returns the top-N latest, so a 2-day outage loses papers. **Recommendation:** add a fallback to the arXiv API (`http://export.arxiv.org/api/query?search_query=cat:astro-ph.GA&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending`) gated by a heartbeat check — if last-successful fetch is > 12h ago, use the API path. Owner: Tori, 0.5d.

### §11.7 P2 — Stance jury hook unclear for new arxiv_ingest evidence

`drain_stance_jury_backlog` runs hourly. Does it pick up newly-inserted `arxiv_ingest` evidence with `stance='supports'`? Need to verify. **Recommendation:** explicit enqueue in `handle_claim_evidence` after `db.flush()` — write the new evidence's `id` to whatever queue table the stance jury reads. Owner: Tori (after audit), 0.25h. If the jury already picks up by polling, no-op.

### §11.8 P2 — Embedding upgrade path not implemented

`ARXIV_MATCH_USE_EMBEDDINGS = False`. The TF-IDF classifier is fine for now; only worth implementing if §11.2 diagnosis points to vocabulary mismatch rather than ADS-lag as the dominant leak. **Defer to Phase E.**

### §11.9 P2 — Beat-schedule comment for newsletter task is mislabeled

`worker.py:21` says `# UTC 08:30 = KST 17:30 (30min after arxiv fetch)` but the actual cron value is `hour=1, minute=30` → UTC 01:30 = KST 10:30. The schedule is correct (newsletter goes out at KST 10:30 ≈ morning briefing). The comment is wrong. **Fix:** 1-line comment correction. Owner: Tori, trivial.

### §11.10 P3 — Legacy `_match_wiki_pages` keyword dict still active

`fetch_arxiv_daily` still calls the 14-keyword legacy matcher for newsletter compat. The classifier path doesn't use it. Eventually replace newsletter's `arxiv_papers.related_pages` consumption with the classifier's `match_meta.top_pages`. **Defer.**

---

## 12. Phase D recommendations — ranked

Phase A (v1 design, 2026-05-10) and Phase C (v1.1 ranked items, 2026-05-12) are largely shipped. Open work, ranked by impact-per-day:

| # | Item | Source | Effort | Impact |
|---|---|---:|---:|---|
| 1 | **48h-lag retry path for `verify_rejected`** | §11.2 (1) | 1d | Should recover ~70-80% of currently-lost claim_evidence yield |
| 2 | **Split `verify_rejected` into `_ads_lag` vs `_quality`** | §11.2 (2) | 0.5d | Diagnostic — needed for #1 to be measurable |
| 3 | **Manual sample 5 `verify_rejected` rows** | §11.2 (3) | 1h | Kun work; informs whether stance LLM judge is too strict |
| 4 | **Fallback re-route `verify_rejected` → page_extension** | §11.3 | 0.5h | Restores page_extension flow when ADS lags |
| 5 | **Admin moderation page (`/admin/new-page-proposals`)** | §11.4 | 1.5d | Unblocks 79 pending; independent, can parallel with #1-4 |
| 6 | **Set `centroid_similarity = 1.0` for size-1 clusters** | §11.5 | 0.25h | Restores signal interpretability |
| 7 | **arXiv API fallback when RSS stale > 12h** | §11.6 | 0.5d | Resilience |
| 8 | **Stance-jury enqueue audit** | §11.7 | 0.25h Kun + 0.25h Tori if needed | Confirms or fixes stance refinement |
| 9 | **Beat-schedule comment fix** | §11.9 | trivial | Hygiene |
| 10 | **Embedding reranker for borderline TF-IDF (0.30-0.50)** | §11.8 | 2d | Defer until §11.2 diagnosis points here |
| 11 | **Retire legacy `_match_wiki_pages`** | §11.10 | 0.5d | Defer until newsletter consumer reworked |

**Phase D minimum-viable scope: items #1-4 + #6 + #9 ≈ 2.5 days Tori + 1h Kun.** Item #5 (1.5d) is independent and runs in parallel. Items #10-11 stay in Phase E backlog.

---

## 13. Acceptance criteria for Phase D ship

- [ ] `evidence` rows via `source_channel='arxiv_ingest'` **≥ 5/day** (7-day moving average) within 14 days of item #1 deploy
- [ ] `verify_rejected_ads_lag` and `verify_rejected_quality` are distinct decisions in `ExternalSourceLog` (item #2)
- [ ] **Zero** papers stuck in `verify_rejected` for > 96 hours without retry (item #1 working)
- [ ] `page_extension_proposed` rate **≥ 3/week** (item #4 working)
- [ ] `NewPageProposal` `pending` count **< 30** within 30 days of admin page deploy (item #5)
- [ ] `centroid_similarity > 0` on **100%** of pending NewPageProposals (item #6)
- [ ] ArxivBot 30d approval rate stays in **[10%, 30%]** band — neither auto-approved (no guards) nor zero (something blocking)
- [ ] No regression in newsletter (still receives `arxiv_papers` rows with `related_pages` populated)

---

## 14. Open questions for Papa

1. **48h retry window** — is 48h the right wait for ADS lag, or should we go longer (72h, given some preprints take 4-5 days to index)? My recommendation: 48h first, with a `process_pending_verify_retries` task at UTC 08:00 daily. If we still see lag, extend to 72h after 14 days of data.
2. **Verify-quality LLM** — is `paper_search.verify_for_claim`'s internal stance LLM (currently inside the function) the right model? It's not in the platoon doc explicitly. My recommendation: route it to Rakon (`deepseek-r1:14b`) explicitly and document it in `ollama_model_policy_v1.md`.
3. **Admin moderation page priority** — ship inline with Phase D (item #5, 1.5d) or defer to its own ticket? My recommendation: ship inline. 79 pending proposals is approaching a hygiene problem.
4. **Fetch timing** — UTC 01:00 (current) catches yesterday's batch with ~5h lag. UTC 20:00 (post-announcement) would catch the freshest set with ~no lag. My recommendation: shift to UTC 20:00 only after item #1 stabilizes; otherwise we just amplify the ADS-lag problem.

---

## 15. Version history

### v1.0 — 2026-05-10 (HwaO stand-in)
- Initial design when arXiv → wiki integration was scoped. Pipeline diagram, RSS source, classifier shape. Preserved in git history.

### v1.1 — 2026-05-12 (Kun audit + post-Quality-Guards rescoping)
- Refreshed live state vs v1.
- Identified `arxiv_ingest.py:267` `_chat_parallel` signature bug (item #1, since fixed by downgrading to single-model `_chat`).
- Identified `published_after` missing from RSS request (item #2, since addressed by raising limit to 20/cat; arXiv API migration deferred).
- Re-ranked Phase C items 1-13.
- Set v1.1 acceptance: ArxivBot 7d approval ≤ 30% within 72h (✅ — now 0% in 7d), page_extension_llm_failed → 0 (✅), `evidence` ≥ 5/day (❌ — still 0 in 7d, drives §11.2 P0), arxiv_papers daily ≥ 30/d (✅ — 51/d).
- Platoon table introduced.

### v1.2 — 2026-05-20 (this version, Kun)
- Refreshed live state to 8-day production observation.
- Confirmed Phase C items #1, #2, #4, #6 shipped; item #7 partial; item #8 shipped.
- Identified new P0: `claim_evidence` yield collapsed (7d=0). ADS-lag is the dominant cause.
- Identified new P1: ArxivBot 24h volume = 0 (page_extension starved when claim_evidence path rejects).
- Restructured the doc into a single coherent v1 design instead of layered audits (history moved here, §15).
- Phase D recommendations replace v1.1's Phase C (which is mostly shipped).

---

## 16. References

### Live code
- `backend/app/services/arxiv_classifier.py` — TF-IDF classifier, decision matrix
- `backend/app/services/arxiv_ingest.py` — `handle_claim_evidence`, `handle_page_extension`, `handle_new_topic`
- `backend/app/services/paper_search.py` — `verify_for_claim` (ADS lookup + stance pre-judge)
- `backend/app/services/content_guards.py` — generic-filler pre-filter (used by Quality Guards)
- `backend/app/agent_loop/tasks.py:4335` — `fetch_arxiv_daily`
- `backend/app/agent_loop/tasks.py` — `send_arxiv_daily_summary`, `retry_unprocessed_arxiv_papers`, `cluster_new_topic_candidates`, `drain_stance_jury_backlog`
- `backend/app/agent_loop/worker.py:beat_schedule` — Celery beat layout
- `backend/app/config.py` — all `ARXIV_*` knobs
- `backend/app/levels.py` — ArxivBot model assignment (qwen2.5:7b editor role)

### Models
- `app/models/arxiv.py` — `ArxivPaper`
- `app/models/external.py` — `ExternalSourceLog`, `NewPageProposal`
- `app/models/evidence.py` — `Evidence` (existing, shared with other source_channels)
- `app/models/edit.py` — `EditProposal` (existing, shared with all editors)

### Companion design docs (referenced above)
- `docs/beat_schedule_v3.md`
- `docs/ollama_model_policy_v1.md`
- `docs/research_ideas_design_v1.md`
- `docs/autowiki_surveys_v1.md`
- `~/.openclaw/agents/kun/workspace/설계_AgentLoopQualityGuards_v1.md`
- `~/.openclaw/agents/kun/workspace/설계_WikiRenovation_v1.md`

### Live audit (2026-05-20, Mac Studio prod)
- `arxiv_papers` total: 1,243 (+556 in 8 days)
- `arxiv_papers` 7d: 356 (~51/day)
- `evidence` (`source_channel='arxiv_ingest'`): 13 total, 0 in last 7 days
- `evidence_inserted` audit rows 30d: 10
- `verify_rejected` 30d: 21 · `verify_failed` 30d: 8
- ArxivBot proposals 30d: 305 APPROVED / 2,285 REJECTED (11.8% approval, down from 27.9% in v1.1)
- ArxivBot proposals 7d: 0 APPROVED / 1 REJECTED
- `NewPageProposal`: 79 pending, 38 rejected
- `centroid_similarity` on pending: min=0.0, max=0.42, avg=0.094

— 🔬 Kun, 2026-05-20 KST

---

## 17. Track B Element-Level Phase 2 Validator Design (v1.3, 2026-05-25)

**Author:** Kun 🔬  
**Date:** 2026-05-25 KST  
**Status:** Draft design for Tori implementation; no code or DB writes performed by Kun  
**Live grounding:** Papa approved Track B Option (a): accept claim `1653` as a permanent atomizer failure and close Phase 1.5 at **320/321 parseable claims**. Grounded against Track B artifacts in `/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/atomize_galaxy_evolution_20260524T174549Z/` and `/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/atomize_galaxy_evolution_20260524T174549Z_phase15_retry_20260524T235035Z/`. Phase 1 attempted 321 claims, parsed 312 (97.20%), emitted 832 elements, and failed 9 atomizations. Phase 1.5 retried those 9 with AstroSage, recovered 8, and left claim `1653` as the only permanent failure after 7 retries. Combined Track B atomization is therefore 320/321 parseable. This design also respects the May 24 v1 verdict: whole-claim validation on page 57 produced only 3-7 viable rows from 1,403 candidates depending on manifest/version, and count gate failure is structural.

### 17.1 Phase 2 Goal

Phase 2 builds a shadow element-level validator for page `galaxy-evolution` without changing production evidence.

The goal is not to promote rows immediately. The goal is to answer one question with auditable artifacts:

> If each claim is decomposed into required elements, can the arXiv feed honestly find enough claim-paper support to clear the production gate without Tier B false positives?

Phase 2 succeeds only if it produces a manifest where each promoted candidate can be traced from paper abstract span -> element vote -> claim-level aggregate -> `validated_ready` decision.

### 17.2 Inputs and Scope

Use the Track B Phase 1 + Phase 1.5 atomization artifacts as immutable inputs:

- Primary Phase 1 elements: `arxiv_wiki_feed_v2/atomize_galaxy_evolution_20260524T174549Z/elements.jsonl`
- Phase 1 meta: `arxiv_wiki_feed_v2/atomize_galaxy_evolution_20260524T174549Z/atomize_meta.json`
- Phase 1.5 recovered elements: `arxiv_wiki_feed_v2/atomize_galaxy_evolution_20260524T174549Z_phase15_retry_20260524T235035Z/elements.jsonl`
- Phase 1.5 meta: `arxiv_wiki_feed_v2/atomize_galaxy_evolution_20260524T174549Z_phase15_retry_20260524T235035Z/phase15_meta.json`
- Permanent failure: claim `1653`, excluded from Phase 2 validator scope and recorded as `atomizer_permanent_failure`.

Candidate paper scope should start with the existing page-57 v1 candidate universe, then optionally widen after the first Phase 2 report:

1. Required first run: reuse the latest page-57 arXiv candidate set from the May 24 v1 galaxy-evolution runs, including the 1,403 claim-paper pairs used for the tuned validator analysis.
2. Optional second run: rebuild candidates with element text as retrieval queries, because element-level matching may uncover papers that whole-claim retrieval missed.
3. Do not write to production `evidence`, `evidence_votes`, `claims`, or feed-run tables in Phase 2.

### 17.3 Data Model for Shadow Artifacts

Phase 2 can be implemented as files first. If Tori prefers DB-backed shadow tables for repeatability, use names that cannot collide with production evidence.

Minimum file outputs:

```text
element_claims_merged.jsonl
element_candidate_pairs.jsonl
element_votes_atom.jsonl
element_votes_astrosage.jsonl
element_votes_rakon_audit.jsonl
element_vote_summary.jsonl
claim_candidate_aggregate.jsonl
promotion_manifest_phase2_shadow.json
phase2_validator_report.md
```

Recommended DB shadow tables if persisted:

```text
arxiv_wiki_element_runs
arxiv_wiki_claim_elements
arxiv_wiki_element_candidate_pairs
arxiv_wiki_element_votes
arxiv_wiki_claim_candidate_aggregates
```

Every row must carry:

- `run_key`
- `claim_id`
- `element_id`
- `candidate_id` or deterministic candidate key
- `arxiv_id`
- `paper_title`
- `paper_abstract_snapshot`
- `model_name`
- `prompt_version`
- `source_artifact`
- `created_at`

The candidate key should be stable across reruns:

```text
sha256(page_id + claim_id + arxiv_id + normalized_paper_title + candidate_source)
```

### 17.4 Element Merge Rule

Build `element_claims_merged.jsonl` by taking all parseable Phase 1 elements and overlaying Phase 1.5 recovered elements for the 8 recovered claims:

- Recovered IDs: `1641`, `1682`, `1686`, `1735`, `1742`, `1784`, `1787`, `1822`
- Permanent failure ID: `1653`
- Parseable final denominator: `320/321`

If a recovered claim exists in both files, the Phase 1.5 record wins because it came from the stricter JSON retry prompt and repaired parser path.

Do not synthesize elements for claim `1653` during Phase 2. Treat it as a hard exclusion. If later editorial work rewrites claim `1653`, that is a new Track A/claim-rewrite task, not a validator retry.

### 17.5 Per-Element Validation Labels

Each model vote labels one `(candidate, element)` pair:

- `supported`: abstract directly supports the element as written.
- `partial`: abstract supports a nearby, weaker, broader, or scope-shifted version.
- `missing`: abstract does not address the element.
- `contradicted`: abstract directly conflicts with the element.
- `needs_human`: malformed input, ambiguous abstract, model parse failure, or requires full text.

Required output schema:

```json
{
  "run_key": "arxiv_wiki_feed_v2_phase2_<ts>",
  "candidate_key": "...",
  "claim_id": 1865,
  "element_id": "claim-1865-e04",
  "element_type": "relationship",
  "required": true,
  "arxiv_id": "2512.16208v1",
  "model_name": "vanta-research/atom-astronomy-7b:latest",
  "label": "supported",
  "stance": "supports",
  "score": 0.92,
  "quoted_evidence_span": "AGN feedback is the primary quenching mechanism...",
  "matched_subject": "massive quenched galaxies",
  "matched_mechanism": "AGN feedback",
  "matched_regime": "z >= 2",
  "rationale": "The abstract directly identifies AGN feedback as the primary quenching mechanism for massive quenched galaxies at high redshift.",
  "failure_mode": null,
  "latency_seconds": 1.8,
  "prompt_version": "arxiv_wiki_feed_v2_element_validator_phase2_20260525"
}
```

### 17.6 Validator Flow

Phase 2 should run as a conservative cascade:

1. **Load and lint elements.** Reject malformed element rows, duplicate element IDs, missing parent claim IDs, or rows whose `required` flag is absent.
2. **Build candidate-element pairs.** For each claim-paper candidate, join all required and optional elements for that claim.
3. **Deterministic precheck.** Mark obvious mismatches before model calls where possible: missing all claim keywords, impossible redshift regime, impossible quantity/unit, duplicate already-active evidence.
4. **Atom-7B bulk vote.** Score all non-prechecked candidate-element pairs.
5. **AstroSage review.** Review all Atom `supported`, all Atom `partial` on required elements, all redshift/environment elements, all quantity/threshold elements with score >= 0.50, and every candidate whose preliminary aggregate could become `strict_support` or `strict_challenge`.
6. **Rakon audit.** Audit only the highest-risk set: promotion candidates, model disagreements that affect promotion, contradiction candidates, and a seeded random sample.
7. **Deterministic aggregation.** Convert element votes into claim-candidate labels.
8. **Manifest and report.** Write a shadow promotion manifest plus an audit report. No production apply in Phase 2.

### 17.7 Claim-Level Aggregation

The aggregate label is deterministic. Models vote on elements; code decides claim status.

`strict_support`:

- Every required element has final status `supported`.
- No required element is `contradicted`, `missing`, or unresolved `needs_human`.
- Redshift/environment elements are exact or explicitly compatible.
- Mechanism elements match the same physical mechanism, not merely the same topic family.
- Quantity/threshold elements match numerically or within a documented tolerance.
- At least Atom-7B and AstroSage agree on every required element, or the row receives human/Rakon audit approval.

`adjacent_support`:

- At least one required element is `supported`.
- At least one required element is `partial` or `missing`.
- No required element is directly `contradicted`.
- The paper is useful context or rewrite guidance but not production evidence for the current claim.

`strict_challenge`:

- At least one central required element is `contradicted`.
- The contradiction is direct and not merely absence of evidence.
- Missing unrelated elements do not erase a direct challenge.

`needs_human`:

- Promotion-affecting model disagreement remains unresolved.
- Required element depends on full text.
- Atomizer boundary is questionable enough that support would depend on a different decomposition.

`neutral_or_unclear`:

- No required element is supported or contradicted strongly enough to matter.

### 17.8 Promotion Manifest Rule

Phase 2 may emit `promotion_manifest_phase2_shadow.json`, but the manifest is **not executable** by the existing v1 promote script.

Manifest eligibility:

- `claim_level_label in {"strict_support", "strict_challenge"}`
- all relevant required-element gates pass
- duplicate check against existing production arXiv evidence passes
- evidence summary cites only spans present in the abstract snapshot
- aggregate includes a complete element vote table
- Rakon/human audit status is either `passed` or `not_required_by_sampling_rule`

The production count gate remains unchanged for a later apply decision:

- at least 30 `validated_ready` rows
- at least 15 distinct claims
- audited precision target >= 0.95

If Phase 2 does not clear 30/15, the report should say so plainly. The result is still useful because it identifies which elements are unsupported and whether the bottleneck is claim granularity, candidate retrieval, or abstract-only evidence coverage.

### 17.9 Calibration and Audit Plan

Use three calibration sets before trusting the manifest:

1. **Known positives:** the 3-5 v1 rows already judged production-worthy or near-production-worthy, including the active arXiv-wiki evidence rows from the May 24 smoke result.
2. **Tier B traps:** sampled rows from the rejected Tier B aggregation where wrong-redshift, wrong-mechanism, topic-generic, or hallucinated-span errors appeared.
3. **Boundary sample:** 30 claims sampled from Track B atomization output, including compound, citation-heavy, quantity-heavy, and debate claims.

Minimum audit metrics:

- element-level Atom/AstroSage agreement by element type
- claim-level strict-support precision on sampled manifest rows
- false-positive modes by category
- percent of promotion candidates blocked by one missing element
- percent of candidates downgraded from whole-claim support to `adjacent_support`
- latency and retry counts by model

Stop conditions:

- Any model emits unverifiable quoted spans in more than 2% of audited promotion candidates.
- Strict-support audited precision falls below 0.95.
- Redshift/environment false positives recur in the Tier B trap set.
- Rakon transport is unhealthy and no human audit replacement is available for promotion candidates.

### 17.10 Platoon Assignment

This is the required model ownership map for Phase 2.

| Step | Owner model/agent | Why this owner | Output |
|---|---|---|---|
| Phase 1/1.5 atomization source of truth | AstroSage-70B | Astronomy-domain decomposition is prose/semantics-heavy; Track B already used AstroSage and closed at 320/321. | `element_claims_merged.jsonl` |
| Element schema merge and deterministic lint | Tori | Pure implementation and artifact hygiene. | lint report, merged elements |
| Candidate rebuild / candidate-element join | Tori | Deterministic DB/artifact work on Mac Studio. | `element_candidate_pairs.jsonl` |
| Bulk per-element validation | Atom-7B | Fast astronomy scorer; can cover thousands of element pairs cheaply. | `element_votes_atom.jsonl` |
| Promotion-eligible review | AstroSage-70B | Domain reviewer for supported/partial/quantity/redshift elements where precision matters. | `element_votes_astrosage.jsonl` |
| Redshift, mechanism, and quantity compatibility rules | Tori implements; AstroSage calibrates examples | Deterministic rules must be code-owned, but astronomy examples need domain grounding. | compatibility config + report section |
| Adversarial audit | Rakon | Heavy reasoner for semantic traps, disagreement, contradiction, and high-impact promotions. | `element_votes_rakon_audit.jsonl` |
| Rakon fallback if transport unhealthy | Human/HwaO audit sample, not model fallback | Prior Rakon transport was unreliable; silent model fallback would weaken the audit claim. | audit replacement note |
| Claim-level aggregation | Tori | Must be deterministic and reproducible. | `claim_candidate_aggregate.jsonl` |
| Design judgment / gate interpretation | Kun | Phase verdict and system-design interpretation. | final Phase 2 review |
| Coordination / Papa-facing decision packet | HwaO | HwaO owns cross-agent routing and concise Papa handoff. | system event / approval menu |

Do not route bulk scoring to Rakon. Do not route astronomy element validation to generic non-astronomy models unless the report explicitly marks it as fallback/diagnostic and excludes those rows from promotion eligibility.

### 17.11 Implementation Notes for Tori

Recommended script shape:

```text
backend/scripts/arxiv_wiki_feed_v2_validate_elements.py
  --page-slug galaxy-evolution
  --phase1-elements <path>
  --phase15-elements <path>
  --candidate-run <path-or-run-key>
  --out-dir <artifact-dir>
  --no-db-write
```

Expected phases:

```text
merge-elements
build-pairs
atom-vote
astrosage-review
rakon-audit
aggregate
report
```

All model calls must be resumable. Each phase should be restart-safe by checking existing JSONL rows keyed by `(candidate_key, element_id, model_name, prompt_version)`.

Operational constraints:

- Run NebulaMind Python scripts on Mac Studio, not Mac Pro.
- No DB writes unless a later Papa/HwaO dispatch explicitly authorizes shadow tables.
- No production evidence apply in Phase 2.
- No silent model fallback.
- AstroSage and Blanc must not be co-loaded intentionally; use AstroSage for astronomy review.
- Rakon is audit-only; if unavailable, report `rakon_status="transport_unhealthy"` and use a human/HwaO sample replacement rather than pretending the audit happened.

### 17.12 Phase 2 Deliverables

Tori should produce:

1. `phase2_validator_report.md`
2. `element_claims_merged.jsonl`
3. `element_candidate_pairs.jsonl`
4. `element_votes_atom.jsonl`
5. `element_votes_astrosage.jsonl`
6. `element_votes_rakon_audit.jsonl` or `rakon_deferred_audit_replacement.md`
7. `claim_candidate_aggregate.jsonl`
8. `promotion_manifest_phase2_shadow.json`
9. `phase2_metrics.json`

The report must include:

- final denominator: 320 parseable claims, 1 excluded permanent atomizer failure (`1653`)
- number of candidate-element pairs scored
- element-level agreement by type
- claim-level label counts
- shadow `validated_ready` row count and distinct-claim count
- whether 30/15 gate would pass
- audited precision estimate
- top false-positive failure modes
- explicit statement that no production evidence was written

### 17.13 Phase 2 Verdict Rules

After Phase 2, choose one of these outcomes:

- **Proceed to Phase 3 shadow-table/apply design** if 30/15 passes and audited precision is >=0.95.
- **Improve candidate retrieval** if many claims have supported elements but papers were missed by whole-claim candidate generation.
- **Prefer Track A rewrite** if many candidates are downgraded because one or two parent-claim elements are never supported together.
- **Stop arXiv abstract-only promotion for this page** if even element-level validation cannot find enough strict evidence and the missing evidence likely lives in full text or older cited literature.

My prior is that Phase 2 will improve precision substantially and convert many false positives into useful `adjacent_support`, but it may or may not clear 30/15 on abstract-only evidence. The design should treat that as a legitimate scientific outcome, not a failure to tune prompts.

### v1.3 — 2026-05-25 (Kun)
- Added Track B Phase 2 validator design after Papa approved accepting claim `1653` as a permanent atomizer failure.
- Recorded Track B Phase 1.5 result: 8/9 failed atomizations recovered, final denominator 320/321 parseable.
- Defined element-level validator flow, shadow artifacts, aggregation rules, calibration gates, stop conditions, and Platoon Assignment.
- Explicitly blocked production evidence writes during Phase 2.
