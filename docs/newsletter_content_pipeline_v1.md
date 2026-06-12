# Newsletter Content Pipeline — Design v1

**Owner:** Kun 🔬  ·  **Status:** Draft — needs Papa approval on §7 open questions, then ready for Tori
**Date:** 2026-05-18
**Context:** NebulaMind Daily newsletter renders 3 tracks (News / Data / Papers). Live inventory is anemic on two of three tracks.

---

## 1. Live audit — what's in the table right now

Pulled 2026-05-18 from `facility_news_items` on Mac Studio Postgres.

| Metric                                                  |  Count | Status |
| ------------------------------------------------------- | -----: | :----- |
| **News** — `track='results'`                            |  **5** | 🔴 thin |
| **Data** — `track IN ('data','facility')`               |     97 | 🟢 healthy |
| **Papers** — `track='highlights' + refereed_paper + DOI`| **14** | 🟡 capped by DOI gap |
| Refereed papers total                                   |     35 | — |
| Refereed papers with DOI                                |     14 | 21 missing |
| Refereed papers with arxiv_id (fallback)                |      0 | none |
| Newsletter recency: news/papers in last 7 d              | 4 / 14 | — |
| Newsletter recency: news/papers in last 14 d             | 5 / 14 | inventory ≠ daily slice |

Source-publication breakdown (general feeds):

| Source              | Items | Mostly routed to |
| ------------------- | ----: | ---------------- |
| AAS Nova            |    20 | `highlights` (18) |
| Nature Astronomy    |    12 | `highlights` (12) |
| ESO                 |    10 | `highlights` (5), `results` (4) |
| **A&A Highlights**  |     0 | 🔴 feed dead (HTTP 404) |
| **Chandra**         |     0 | 🔴 feed dead (HTTP 404) |
| **ESA Science**     |     0 | 🔴 feed dead (HTTP 404) |

The newsletter renderer (`_fetch_track_items`) has **no recency window** — it just pulls newest-first across all-time. So the 5/14 numbers are not "today's items": they're the entire inventory available to ever surface as News or Papers. Fixing this is mostly an **inventory problem**, not a filter problem.

---

## 2. Root-cause diagnosis

### 2.1 News track is starving for two distinct reasons

**A. Track-routing logic dumps the good stuff into `highlights`** — `news_curator.py:286-293`:

```python
if kind in ("refereed_paper", "preprint_highlight"):
    track = "highlights"   # ← refereed-paper coverage from AAS Nova / Nature Astronomy goes here
elif kind == "release":
    track = "data"
elif kind in ("proposal_call", "milestone"):
    track = "tools"
else:                                    # ← News bucket gets only the dregs
    track = "results"                    #   (press_release / anniversary / opinion / other)
```

→ AAS Nova produces 20 items, 18 of which are refereed-paper coverage that goes straight to `highlights`. The News track only sees press releases and other low-signal categories. Result: News looks empty even when feeds are healthy.

**B. Half of the configured general feeds are dead** — A&A Highlights, Chandra, and ESA Science all return HTTP 404. Confirmed by live probe. They were probably valid when added but the publishers reorganized URLs.

### 2.2 Papers track is capped by DOI resolution at ingest

Of 35 `kind='refereed_paper'` rows: 14 have DOIs, 0 have arxiv_ids, 21 have neither. The LLM prompt in `news_curator.py` asks for `paper_doi` and `paper_arxiv_id`, but RSS excerpts often don't contain them. Every missing-DOI row, however, has **title + paper_venue** (e.g., `"ApJ Letters"`, `"Nature Astronomy"`) — enough to resolve externally.

The newsletter filter (`paper_doi IS NOT NULL`) is correct policy (peer-reviewed → DOI is the canonical identifier) but the ingest pipeline has no fallback resolution step. **No backfill job exists.**

### 2.3 Data track is healthy

97 items, 44 in the last 7 days. Not a problem to solve, but Papa asked about additions — covered in §5 with one strategic add only.

---

## 3. Track 1 — News enrichment

### 3.1 Fix routing logic (1-line code change, biggest single win)

Change `news_curator.py:286-293` so editorial-venue refereed-paper coverage flows to the **News** track, not `highlights`:

```python
# Items from general editorial feeds (AAS Nova, Nature Astronomy, ESO, S&T) are NEWS
# regardless of advance_type — they are "things astronomers should know happened."
# The `highlights` track is reserved for our autowiki-generated paper picks.
track = "results"

# Keep `data` and `tools` carve-outs for genuine data releases / proposal calls only:
if advance_type == "data_release":
    track = "data"
elif advance_type in ("proposal_call",) and review.get("kind") == "proposal_call":
    track = "tools"
```

**Why this is safe:** the `highlights` track was being used as a dumping ground; the actual Papers track filter requires `kind='refereed_paper' AND paper_doi IS NOT NULL`, which auto-promotes the real peer-reviewed papers back into Papers once §4 DOI backfill runs. Net effect: News fills from ~5 to ~37+ items; Papers fills from 14 to ~30+ after backfill.

### 3.2 Repair / replace dead feeds

Update `GENERAL_FEEDS` in `news_curator.py:46-54`:

| Action  | Source                | Old URL → New URL / Replacement |
| :------ | --------------------- | ------------------------------- |
| Replace | ESA Science           | `…/Our_Activities/Space_Science` (404) → `https://www.esa.int/rssfeed/Science` (15 items, A-tier) |
| Replace | A&A Highlights        | (404, publisher restructured)    → **drop**; replace with **Sky & Telescope** `https://skyandtelescope.org/feed/` (10 items, B-tier editorial) |
| Replace | Chandra               | (404, all paths dead)            → **drop**; replace with **NOIRLab** `https://noirlab.edu/public/news/feed/` (10 items, A-tier — covers Rubin/Gemini/SOAR) |
| Keep    | AAS Nova / Nat-Astron / ESO | unchanged (working) |
| Add B   | **Sky & Telescope**   | (above) — B-tier (popular astronomy editorial; useful for non-paper news like instrument first-light, mission updates) |
| Add A   | **NOIRLab**           | (above) — A-tier (facility consortium; Rubin/LSST DR pipeline announcements land here first) |

**Validation pre-commit:** Tori adds a one-shot `python3 -m app.agent_loop.news_curator --probe-feeds` flag that GETs each configured URL and asserts HTTP 200 + `items > 0`. Run in CI; alert on regression. (No 404s ever again silently in production.)

### 3.3 Optional: arXiv astro-ph daily highlights as low-cost News supply

arXiv doesn't curate; volume is 100+/day. **Don't bulk-ingest into News** — would be noise. Instead:
- Reuse existing `ArxivPaper` rows where `category IN (astro-ph.HE, astro-ph.GA, ...)` AND `submitted=today` AND `astro_quality_score >= 0.85` (already scored by Mima)
- Surface top 2/day as `track='results'` items with `kind='preprint_highlight'`, source_publication='arXiv (Mima-curated)'
- This is **derivative content**, not a new feed — zero new infrastructure

Decision required from Papa (see Q1).

---

## 4. Track 2 — Papers DOI resolution

### 4.1 Strategy: two-source lookup with confidence-tiered acceptance

For each `refereed_paper` row missing `paper_doi`:

```
Input: title, paper_venue, summary (used only as tiebreaker context)

Step 1 — ADS API lookup (primary)
   GET https://api.adsabs.harvard.edu/v1/search/query
       ?q=title:"{title}" bibstem:"{venue_bibstem}"
       &fl=bibcode,title,doi,pub
       &rows=3
   Auth: settings.ADS_API_KEY  (already configured for paper_search.py)
   Match criteria: title-similarity ≥ 0.85 (token-set Jaccard) AND venue prefix match
   Rate limit: 5000 queries/day (free tier) — 21 backfills = trivial

Step 2 — CrossRef fallback (no auth, no rate limit pain)
   GET https://api.crossref.org/works
       ?query.bibliographic="{title}"
       &query.container-title="{venue}"
       &rows=3
   Match criteria: same — title-similarity ≥ 0.85 + container-title prefix match
   Polite-pool header: mailto=admin@nebulamind.net (per CrossRef etiquette)

Step 3 — Acceptance tiers (write to facility_news_items.paper_doi)
   confidence ≥ 0.90  → auto-apply DOI, log to doi_resolution_log
   0.70 – 0.89        → write to doi_resolution_log as 'needs_review'; Papa-queued
   < 0.70             → log as 'unresolved'; do not touch row
```

ADS already has the integration scaffolding (`paper_search.py:95-160`) — only the **reverse-direction lookup function** (`ads_lookup_by_title_and_venue()`) is missing. Add it next to `ads_lookup_doi()`.

### 4.2 New schema — `doi_resolution_log`

Minimal table, supports audit + revert + Papa review queue:

```python
class DOIResolutionLog(Base):
    __tablename__ = "doi_resolution_log"

    id: Mapped[int] = mapped_column(primary_key=True)
    news_item_id: Mapped[int] = mapped_column(ForeignKey("facility_news_items.id"), index=True)
    resolved_doi: Mapped[str | None] = mapped_column(String(200), nullable=True)
    confidence: Mapped[float] = mapped_column(Float)
    source_api: Mapped[str] = mapped_column(String(20))   # 'ads' | 'crossref'
    title_similarity: Mapped[float] = mapped_column(Float)
    venue_match: Mapped[bool] = mapped_column(Boolean)
    status: Mapped[str] = mapped_column(String(20))       # 'auto_applied' | 'needs_review' | 'unresolved' | 'reverted'
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
```

### 4.3 Backfill job + nightly sweep

**One-shot backfill** (Tori runs once after deploy):
```bash
python3 -m app.agent_loop.doi_backfill --all-unresolved
# Expected: 21 candidates → ~15 auto-applied + ~4 needs-review + ~2 unresolved
```

**Nightly Celery task** — `app.agent_loop.doi_backfill.sweep_recent_refereed`:
- Run after `curate_daily_news` finishes (chain or separate beat at 04:00 KST)
- Query: `WHERE kind='refereed_paper' AND paper_doi IS NULL AND created_at >= NOW() - INTERVAL '7 days'`
- Catches anything today's ingest missed

### 4.4 What happens to `needs_review` items

They render in a small **Papa admin page** at `/admin/doi-review` showing: title, venue, candidate DOI(s) with confidence, "Apply" / "Reject" buttons. Reuses existing admin auth. (~50 LoC frontend; not strictly required for v1 — if Papa wants, defer to v1.1.)

---

## 5. Track 3 — Data enrichment

Data is already healthy (97 items). One strategic add — no others justified:

### 5.1 NOIRLab feed (covered above in §3.2)

Same feed serves both News and Data — NOIRLab posts cover both Rubin/LSST commissioning milestones (News-routed) and value-added catalog releases (Data-routed). The LLM `advance_type` classifier already discriminates correctly.

### 5.2 Survey DR Calendar surfacing — reuse, don't re-ingest

Papa's existing `surveys_directory` flagship has a Survey Data Release Calendar (`surveys_directory_design_v1.md`). The Data track can **borrow** the next-7-day calendar cards without any new ingestion:

```python
# In newsletter.py _fetch_track_items for 'data':
# Append up to 2 calendar items at the top of the data list
calendar_items = db.query(SurveyCalendarEvent).filter(
    SurveyCalendarEvent.event_date.between(today, today + timedelta(days=7))
).order_by(SurveyCalendarEvent.event_date).limit(2).all()
data_items = [_render_calendar_as_news(c) for c in calendar_items] + data_items
```

→ Surfaces upcoming Roman LCRD, Rubin DR-1, Euclid DR1 milestones inline with daily Data — gives the section forward-looking texture without polling new feeds.

### 5.3 NOT recommended

- ❌ **MAST RSS** — feed exists but volume is dominated by routine pipeline reprocessing notes; signal/noise too low. Skip.
- ❌ **VizieR new catalogs** — no public RSS, would need scraping; out of v1 scope.
- ❌ **arXiv astro-ph.IM filter** — overlaps with Mima's already-running arxiv-classifier; would re-process same papers. Skip.

---

## 6. Platoon assignment

Every step that runs periodically or hits an external API needs an owning model (per standing protocol).

| Step                           | Owner   | Capability       | Cost / Speed                     | Justification |
| ------------------------------ | ------- | ---------------- | -------------------------------- | ------------- |
| RSS feed fetch + LLM scoring   | **Mima** | local LLM (astrosage-7B) | free / ~3 s per item | already runs `news_curator`; no model change |
| ADS API DOI lookup             | **Mima** | HTTP + JSON parse | $0 / ~400 ms per call | deterministic; no LLM needed |
| CrossRef fallback DOI lookup   | **Mima** | HTTP + JSON parse | $0 / ~600 ms per call | same |
| Title-similarity match acceptance | **Mima** | token-set Jaccard (Python) | $0 / instant | deterministic |
| Routing-logic change           | (one-time, Tori code)| — | — | code change, not a model decision |
| News-track preprint surfacing (§3.3) | **Mima** | reuses Mima's existing scores | free | derivative of existing run |
| Feed-health CI probe           | **Mima** | HTTP HEAD/GET | free | runs in test suite |
| Survey calendar borrow (§5.2)  | (no model; pure SQL) | — | — | direct join |
| Papa-review queue (§4.4)       | **Papa** (human) | — | — | only when confidence 0.70–0.89 |

**Total external API budget added:** ~25 ADS calls/day + ~25 CrossRef calls/day in steady state (assumes ~8 new refereed_paper items/day from §3.1 fix). Both within free tiers.

---

## 7. Open questions for Papa

| # | Question | Default if no answer |
| :- | :------- | :----------------- |
| Q1 | §3.3 — surface 2 Mima-curated arXiv preprints/day to News track? | **Off** until Papa OKs (avoid noise risk) |
| Q2 | §4.4 — build Papa-review admin page in v1 or defer to v1.1? | **Defer to v1.1**; needs-review items logged but not surfaced |
| Q3 | §4.1 — title-similarity threshold for auto-apply (0.85? 0.90?) | **0.85** (token-set Jaccard) — conservative but recoverable via revert |
| Q4 | §3.2 — add Hubble (`hubblesite.org`) feed in v1? Returns 431 KB but 0 RSS items — needs custom JSON-XML parser. | **Defer to v1.1**; not worth a parser detour for v1 |
| Q5 | §5.2 — does `SurveyCalendarEvent` table exist yet, or is this dependent on `surveys_directory` ship? | If table doesn't exist, defer §5.2 until surveys directory ships |

---

## 8. Acceptance criteria

After Tori deploys v1, all of these hold:

- [ ] **News inventory ≥ 30 items** in last 14 days (was 5)
- [ ] **Papers inventory ≥ 25 items with DOI** (was 14)
- [ ] All 6 general feeds return HTTP 200 + items > 0 in feed-health probe
- [ ] `doi_resolution_log` table exists and has ≥ 14 rows after one-shot backfill (the 21 candidates, allowing some unresolved)
- [ ] `curate_daily_news` task duration grows by < 30 s (routing change is local; DOI sweep is bounded by 50 calls/day)
- [ ] Newsletter renders without errors with new inventory
- [ ] No regressions in existing `track='data'` count (should stay ≥ 90 in last 14d)

---

## 9. Files Tori will touch

```
backend/app/agent_loop/news_curator.py       # §3.1 routing logic; §3.2 feed URLs
backend/app/agent_loop/doi_backfill.py       # NEW — §4 ADS+CrossRef resolver + sweep task
backend/app/agent_loop/newsletter.py         # §5.2 calendar borrow (optional, depends on Q5)
backend/app/models/external.py               # NEW model: DOIResolutionLog
backend/app/services/paper_search.py         # ADD: ads_lookup_by_title_and_venue()
backend/alembic/versions/XXXX_doi_log.py     # NEW migration
backend/tests/test_feed_health.py            # NEW — §3.2 probe
backend/app/agent_loop/worker.py             # ADD nightly beat for doi_backfill.sweep_recent_refereed
```

Estimated implementation: **3–5 hours** for v1 (routing + feed swap + DOI backfill + tests).

---

## 10. Risk register

| Risk | Likelihood | Impact | Mitigation |
| :--- | :--------- | :----- | :--------- |
| Routing change moves real `refereed_paper` items from Papers→News before DOI backfill catches up | Med | Low | Run §4.3 one-shot **before** deploying §3.1 routing change; or temporarily ship both in same release |
| ADS title-similarity false positives apply wrong DOI | Low | Med | `doi_resolution_log` is revertable; confidence threshold conservative; only ~1/10 papers will hit the ambiguous band |
| New feed (Sky & Telescope, NOIRLab) credibility drift over time | Med | Low | Mima credibility floor already filters per-tier; B-tier floor is stricter (0.75) than A-tier (0.65) |
| CrossRef rate-limit (50 req/sec polite-pool) | Very low | Low | 25 calls/day total — nowhere near limit |
| ESA Science replacement URL also dies | Low | Low | Feed-health CI probe (§3.2 acceptance) catches within 24 h |

---

**Status:** Draft ready for Papa review on §7 questions. Once answered, mark Papa-approved and hand to Tori.

— Kun 🔬
