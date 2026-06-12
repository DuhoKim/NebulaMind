# Astronomy News Curator v2 — Professional-Grade Beyond the Six Facilities

**Author:** Kun
**Date:** 2026-05-10
**Status:** DRAFT
**Scope:** Expand `news_curator.py` from 6 facilities to general professional astronomy news. Audience: working astronomers, not popsci.
**Sibling docs:** `arxiv_wiki_feed_design_v1.md` (deduplication source-of-truth on arXiv side)
**Audience:** Tori (implementer), HwaO (coordinator), Papa

The directive: Papa wants the newsletter to surface professional-level astronomy news (research highlights from journals, AAS Nova, ESO, Chandra, etc.) — distinguishing genuine research advances from press releases.

---

## 1. What's live today (`news_curator.py`)

`curate_daily_news` runs once per day and scrapes RSS for the **six tracked facilities** only:

```python
FACILITY_FEEDS = {
    "desi":    [DESI feed, DESI news category feed],
    "jwst":    [STScI Webb releases, NASA Webb newsroom],
    "euclid":  [Euclid Consortium feed, ESA Space Science feed],
    "lsst-rubin": [LSST news, Rubin Observatory news, LSST community.lsst.org],
    "alma":    [ALMA news, ALMA press releases],
    "vla":     [NRAO public news, NRAO science news],
}
```

For each item: parse RSS → dedupe by `slug = facility-{md5(title)[:8]}` → score with single-pass `qwen3:30b` → store `FacilityNewsItem` if `credibility_score >= 0.5`. Top 3 by credibility are marked `featured` for the day. Newsletter renders these in three tracks (Data, Tools, Results) keyed on `kind`.

**Limits of v1:**
- Only 6 facilities. Misses AAS journals, Nature Astronomy, ESO/Chandra non-facility releases, A&A highlights, RAS press, ESA/JAXA/CSA non-Webb.
- Single prompt covers "is this a release vs PR fluff"; no separate detection of *journal paper coverage* vs *press release*.
- No arXiv-ID / DOI extraction → news items can duplicate arXiv papers we already ingest.
- `credibility_score >= 0.5` floor is permissive; 0.5–0.7 band is "general facility news, partnership announcements" per the existing rubric — still mostly PR.

This v2 fixes those gaps without rewriting v1.

---

## 2. Source list — proposed additions

Tiered by *signal-to-noise for working astronomers*. Tier A is "almost always research-grade." Tier C is "include but score harshly." Tier D is "skip."

### 2.1 Tier A — primary research highlights, low popsci ratio

Add to `news_curator.py` as `GENERAL_FEEDS` (separate from `FACILITY_FEEDS`).

| Source | RSS / Feed URL | What it covers | Notes |
|---|---|---|---|
| **AAS Nova** | `https://aasnova.org/feed/` | Daily research highlights of AAS journal papers (ApJ, AJ, ApJL, RNAAS) | **Highest signal source.** Each post is a 1-page summary of a refereed paper, written for astronomers. Almost all qualify. |
| **Nature Astronomy** | `https://www.nature.com/natastron.rss` | Articles, Letters, News & Views, Comments, Editorials | Mix; News & Views and editorials are reliable signals. Filter on doc type via prompt. |
| **A&A Highlights** | `https://www.aanda.org/component/syndicate/?format=feed` | Editor-selected A&A papers each issue | Refereed-only; ~20/month. Direct paper coverage. |
| **MNRAS Highlights** | *(no clean RSS — see §2.4 fallback)* | Editor's-choice flagged MNRAS papers | Use ADS query for `bibstem:MNRAS doctype:editorial` as a synthetic feed. |
| **ESO Science Releases** | `https://www.eso.org/public/news/feed/` | Mix of science announcements + facility PR | Filter sharply via prompt — distinguish science result from "VLT had its 25th anniversary." |
| **Chandra X-ray Observatory** | `https://chandra.harvard.edu/photo/cycle.rss` | "Photo album" feed but most posts have a refereed-paper backbone | Each post links to the underlying paper. |
| **ESA Science Exploration** | `https://www.esa.int/rssfeed/Science_Exploration/Science` | ESA science programmes (excludes industry / launches) | Already used by news_curator for Euclid; promote one URL to general. |
| **NASA APOD** | `https://apod.nasa.gov/apod.rss` | Daily Astronomy Picture; brief commentary often cites refereed papers | Lower priority — add only if Tier A volume is low. |

### 2.2 Tier B — useful with strict filtering

| Source | RSS / Feed URL | Notes |
|---|---|---|
| **Royal Astronomical Society press** | `https://ras.ac.uk/feed` | UK research press releases; often ahead of journal publication. Some PR-heavy items. |
| **CfA / SAO press** | `https://www.cfa.harvard.edu/news/feed` | Center for Astrophysics — covers Chandra and many ground-based programs. Mixed quality. |
| **JPL / Caltech astronomy** | `https://www.jpl.nasa.gov/feeds/news` | Filter to astronomy keywords in prompt; mostly mission ops + PR. |
| **PhysicsWorld astronomy** | `https://physicsworld.com/c/astronomy-and-space/feed/` | Reasonable quality; adjacent to working physicists. |

### 2.3 Tier C — popsci-leaning, include only with score floor ≥ 0.75

| Source | RSS / Feed URL | Notes |
|---|---|---|
| **Phys.org astronomy** | `https://phys.org/rss-feed/space-news/astronomy/` | High volume; mix of paper coverage and reposted PR. Worth keeping for *coverage* of journal papers we'd otherwise miss. Score harshly. |

### 2.4 Tier D — skip

- **Space.com, Universe Today, Sky & Telescope news, EarthSky** — popsci framing dominates; signal too low.
- **NASA general news** — already covered for Webb via news_curator; rest is mission ops + PR.

### 2.5 Notes on missing feeds (MNRAS Letters, ApJL)

Major journals don't expose clean RSS for "letters" or "editor's choice." Two workarounds:

1. **ADS-derived feeds** (preferred): query ADS for `bibstem:MNRAS doctype:letter` or `bibstem:ApJL` filtered to last 24h. Format as our own RSS-equivalent and feed into the curator. Costs an ADS quota slot per day. Implementation: a small `_fetch_ads_letters()` helper that returns the same `{title, content, link}` dict shape as `_fetch_feed`.
2. **arXiv announcement filter** (already partial): `astro-ph` papers with `journal-ref` containing `MNRAS Letters` or `ApJL`. Our existing `fetch_arxiv_daily` already ingests these — Letter status is a downstream filter applied at evidence-quality scoring. The dedup logic in §5 collapses them.

Recommendation: ship without MNRAS-Letters / ApJL synthetic feeds in v2.0; add them as v2.1 if the AAS Nova + A&A Highlights coverage proves insufficient.

---

## 3. Curation criteria — what counts as "professional astronomer relevance"

The v1 prompt has a single 0–1 credibility scale tuned for facility news. v2 needs sharper distinctions because the source mix is wider.

### 3.1 Decision tree (applied per item)

```
1. Is this a press release (PR), a research advance, or facility news?
2. If research advance: is the underlying work refereed, on arXiv, or speculative?
3. Does it report quantitative results, or only qualitative claims?
4. Is the framing professional (results, methods, uncertainties) or popsci
   (e.g. "could rewrite the textbooks", "scientists are baffled")?
5. Is there a paper / arXiv ID / DOI to cite? Extract it.
```

### 3.2 New scoring rubric (replaces v1's per-facility rubric for general feeds)

| Score | Type | Examples |
|---|---|---|
| **0.95+** | Refereed-paper coverage with quantitative results, *or* primary data release | AAS Nova post on a new ApJL; A&A Highlight; new HSC public DR |
| **0.80–0.94** | Refereed-paper coverage with mostly qualitative summary, *or* arXiv preprint highlight from a high-credibility venue (AAS Nova, Nature Astronomy editorial) | "New JWST paper finds…" with the paper linked |
| **0.65–0.79** | Press release tied to a specific paper but written for general audience; instrument milestone with science context | RAS press on *Nature Astronomy* paper, with paper linked |
| **0.50–0.64** | Press release without a clear paper anchor; conference / collaboration update | Non-refereed conference proceedings overview |
| **0.30–0.49** | Anniversary, human-interest, mission-ops update | "Hubble at 36" |
| **<0.30** | Speculation, opinion, popsci framing, "could rewrite" headlines | Skip |

**Score floor for inclusion:** 0.65 for Tier A/B sources, 0.75 for Tier C. Both higher than v1's 0.5.

### 3.3 Updated credibility prompt (single-pass, qwen3:30b)

```python
GENERAL_NEWS_PROMPT = """\
You review astronomy news for professional astronomers and astrophysicists. \
Distinguish genuine research advances from press releases or popular-science framing. \
Your audience reads ApJ, MNRAS, A&A regularly.

Title: {title}
Excerpt: {excerpt}
Source: {source}     # e.g. "AAS Nova", "Nature Astronomy", "ESO", "Chandra"
Source tier: {tier}  # A (research-grade) | B (mixed) | C (popsci-leaning)

Reply with ONLY valid JSON, no extra text:
{{
  "credibility_score": <float 0.0-1.0; see scoring guide>,
  "advance_type": "<refereed_paper|preprint_highlight|data_release|press_release|milestone|anniversary|opinion|other>",
  "summary": "<2-3 sentences in professional voice — what was found, methods, key numbers if available. NO popsci framing.>",
  "paper_arxiv_id": "<XXXX.XXXXX or null>",
  "paper_doi": "<10.xxxx/yyyy or null>",
  "paper_venue": "<journal/preprint name or null, e.g. 'ApJL', 'Nature Astronomy', 'arXiv'>",
  "is_press_release": <true|false>,
  "popsci_flags": [<list of red-flag phrases found, e.g. "rewrite the textbooks", "stunning images", "scientists baffled">],
  "topic_tags": [<2-4 short tags, e.g. "exoplanet", "high-z galaxies", "binary pulsar", "weak lensing">]
}}

Scoring guide (be strict):
  0.95+: Refereed paper coverage with quantitative results, OR primary data release.
         Examples: AAS Nova summary citing a new ApJL; new SDSS-V DR.
  0.80-0.94: Refereed-paper coverage with mostly qualitative summary, OR arXiv
         preprint highlighted by a high-credibility editorial venue.
  0.65-0.79: Press release tied to a specific paper, written for general audience,
         but the paper is identified and linkable.
  0.50-0.64: Press release with no clear paper anchor; conference/collaboration update.
  0.30-0.49: Anniversary, human-interest, mission-ops update.
  <0.30: Speculation, opinion, popsci framing.

Hard rules:
- If `popsci_flags` is non-empty, cap the score at 0.65.
- If `advance_type` is "anniversary" or "opinion", cap at 0.45.
- If `paper_arxiv_id` and `paper_doi` are both null AND `advance_type` is
  "refereed_paper" or "preprint_highlight", cap at 0.70 (we couldn't verify the source).
"""
```

The output gives us:
- `credibility_score` for ranking.
- `paper_arxiv_id` / `paper_doi` for dedup against `arxiv_papers` (§5).
- `is_press_release` for the newsletter to choose framing ("AAS Nova on…" vs "Press release:").
- `popsci_flags` as a tunable signal — if it grows fast, the prompt or sources need adjustment.
- `topic_tags` for future "topic of the week" newsletter slots and per-page wiki linking.

---

## 4. Integration into existing pipeline

### 4.1 Schema changes — extend `FacilityNewsItem`, don't fork

`FacilityNewsItem` already has the right shape (slug, title, summary, source_url, kind, credibility_score, featured, occurs_at). Two minimal additions let it carry general news without a separate model:

```sql
ALTER TABLE facility_news_items
  ADD COLUMN source_publication VARCHAR(80) NULL,    -- e.g. 'AAS Nova', 'Nature Astronomy', 'ESO'
  ADD COLUMN source_tier CHAR(1) NULL,               -- 'A' | 'B' | 'C'
  ADD COLUMN paper_arxiv_id VARCHAR(40) NULL,        -- extracted arXiv ID for dedup
  ADD COLUMN paper_doi VARCHAR(200) NULL,            -- DOI when extractable
  ADD COLUMN paper_venue VARCHAR(80) NULL,           -- 'ApJL', 'Nature Astronomy', 'arXiv', etc.
  ADD COLUMN is_press_release BOOLEAN NULL,
  ADD COLUMN advance_type VARCHAR(40) NULL,          -- from prompt: refereed_paper|preprint_highlight|...
  ADD COLUMN popsci_flags TEXT NULL,                 -- JSON array of detected flags
  ADD COLUMN topic_tags TEXT NULL,                   -- JSON array
  ALTER COLUMN facility_id DROP NOT NULL;            -- general news has no facility

CREATE INDEX idx_fni_paper_arxiv_id ON facility_news_items(paper_arxiv_id) WHERE paper_arxiv_id IS NOT NULL;
CREATE INDEX idx_fni_source_publication ON facility_news_items(source_publication) WHERE source_publication IS NOT NULL;
```

`facility_id` becomes nullable; general news rows have `facility_id=NULL` and `source_publication` set instead. Newsletter renderer already JOINs `facility_profiles` — extend it to coalesce `facility_name = COALESCE(fp.short_name, fni.source_publication)`.

Migration: single Alembic revision, all-additive, zero downtime. Backfill: not needed (existing rows have `facility_id` set; the new columns stay null).

### 4.2 New track in newsletter — "Highlights"

Add a fourth track between Tools and Results, dedicated to general-astronomy research highlights. Keeps the existing Data/Tools/Results facility-focused tracks intact and clearly separates "the wider literature" from "what our six facilities did."

```python
# newsletter.py — extend TRACK_KINDS / TRACK_CONFIG
TRACK_KINDS = {
    "data":       {"release"},
    "tools":      {"proposal_call", "milestone"},
    "highlights": {"refereed_paper", "preprint_highlight"},   # NEW — general news paper coverage
    "results":    {"facility_news", "news"},
}

TRACK_CONFIG = {
    "data":       {"icon": "📦", "label": "Data",       "color": "#3b82f6", "desc": "New datasets & survey releases"},
    "tools":      {"icon": "🔧", "label": "Tools",      "color": "#f59e0b", "desc": "Proposal calls & milestones"},
    "highlights": {"icon": "📖", "label": "Highlights", "color": "#5B2D8E", "desc": "Refereed-paper coverage from AAS Nova, Nature Astronomy, A&A Highlights"},  # NEW
    "results":    {"icon": "🔭", "label": "Results",    "color": "#22c55e", "desc": "Science announcements & facility news"},
}
```

The "Highlights" track:
- Pulls items where `advance_type IN ('refereed_paper', 'preprint_highlight')` and `kind IN ('refereed_paper', 'preprint_highlight')`.
- Renders with `source_publication` as the badge (instead of facility name) — `📖 AAS Nova`, `📖 A&A Highlights`.
- Each card shows `paper_venue` and a "📄 Read paper" link if `paper_doi` or `paper_arxiv_id` is present.

Press releases (`is_press_release=true` and `advance_type='press_release'`) flow into the existing Results track with `kind='news'` to mirror facility press behavior.

### 4.3 New `kind` values

Add to `KIND_LABELS`:

```python
KIND_LABELS = {
    # …existing…
    "refereed_paper":      "📄 Refereed Paper",
    "preprint_highlight":  "📑 Preprint Highlight",
    "press_release":       "📢 Press Release",      # falls into Results track
    "anniversary":         "🎉 Anniversary",        # filtered out at score floor most days
    "opinion":             "💬 Opinion",            # filtered out at score floor
}
```

### 4.4 Curator code changes — `news_curator.py`

Three changes, ~60 lines total:

1. **Add `GENERAL_FEEDS` dict** parallel to `FACILITY_FEEDS`, with each entry tagged by `(source_publication, tier)`.
2. **Add a `_curate_general_feeds()` helper** that fetches RSS, calls a new `_ollama_general_review()` (using `GENERAL_NEWS_PROMPT`), maps `advance_type` to `kind`, and runs dedup against arxiv_papers (§5).
3. **Call it from `curate_daily_news()`** after the facility loop. Flag-gated by `GENERAL_NEWS_ENABLED` (default False on first deploy; flip to True after Tori smoke-tests one source).

Pseudo-shape:

```python
# news_curator.py additions

GENERAL_FEEDS = [
    {"source_publication": "AAS Nova",        "tier": "A", "url": "https://aasnova.org/feed/"},
    {"source_publication": "Nature Astronomy","tier": "A", "url": "https://www.nature.com/natastron.rss"},
    {"source_publication": "A&A Highlights",  "tier": "A", "url": "https://www.aanda.org/component/syndicate/?format=feed"},
    {"source_publication": "ESO",             "tier": "A", "url": "https://www.eso.org/public/news/feed/"},
    {"source_publication": "Chandra",         "tier": "A", "url": "https://chandra.harvard.edu/photo/cycle.rss"},
    {"source_publication": "ESA Science",     "tier": "A", "url": "https://www.esa.int/rssfeed/Science_Exploration/Science"},
    {"source_publication": "RAS",             "tier": "B", "url": "https://ras.ac.uk/feed"},
    {"source_publication": "CfA",             "tier": "B", "url": "https://www.cfa.harvard.edu/news/feed"},
    # Tier C — score floor 0.75
    {"source_publication": "Phys.org astronomy", "tier": "C", "url": "https://phys.org/rss-feed/space-news/astronomy/"},
]

GENERAL_SCORE_FLOOR = {"A": 0.65, "B": 0.65, "C": 0.75}

def _curate_general_feeds(db) -> tuple[int, int]:
    """Fetch GENERAL_FEEDS, score, dedup, store. Return (added, skipped)."""
    added, skipped = 0, 0
    for src in GENERAL_FEEDS:
        items = _fetch_feed(src["url"])
        for raw in items:
            slug = _slug(src["source_publication"].lower().replace(" ", "-"), raw["title"])
            if db.query(FacilityNewsItem).filter_by(slug=slug).first():
                skipped += 1
                continue
            review = _ollama_general_review(raw["title"], raw["content"], src["source_publication"], src["tier"])
            if not review:
                skipped += 1
                continue
            cred = review.get("credibility_score", 0.0)
            if cred < GENERAL_SCORE_FLOOR[src["tier"]]:
                skipped += 1
                continue
            # Dedup against arxiv_papers (see §5)
            arxiv_id = review.get("paper_arxiv_id") or _extract_arxiv_id(raw["title"], raw["content"], raw.get("link"))
            if arxiv_id and _is_dup_of_arxiv(db, arxiv_id):
                skipped += 1
                continue
            kind_map = {
                "refereed_paper": "refereed_paper",
                "preprint_highlight": "preprint_highlight",
                "data_release": "release",
                "press_release": "press_release",
                "milestone": "milestone",
                "anniversary": "anniversary",
                "opinion": "opinion",
            }
            kind = kind_map.get(review.get("advance_type"), "news")
            track = "highlights" if kind in ("refereed_paper", "preprint_highlight") else \
                    ("data" if kind == "release" else
                     ("tools" if kind in ("proposal_call", "milestone") else "results"))
            item = FacilityNewsItem(
                facility_id=None,
                title=raw["title"][:300],
                slug=slug,
                kind=kind,
                track=track,
                summary=review.get("summary", raw["content"][:500]),
                source_url=raw.get("link"),
                credibility_score=cred,
                credibility_model=OLLAMA_MODEL,
                source_publication=src["source_publication"],
                source_tier=src["tier"],
                paper_arxiv_id=arxiv_id,
                paper_doi=review.get("paper_doi"),
                paper_venue=review.get("paper_venue"),
                is_press_release=bool(review.get("is_press_release")),
                advance_type=review.get("advance_type"),
                popsci_flags=json.dumps(review.get("popsci_flags") or []),
                topic_tags=json.dumps(review.get("topic_tags") or []),
                featured=False,
            )
            db.add(item)
            db.flush()
            added += 1
    return added, skipped
```

Featured-of-the-day logic at the end of `curate_daily_news` already picks the top 3 from today's items by `credibility_score` — that selection naturally now includes general news; no change needed.

### 4.5 Celery beat schedule

`curate_daily_news` already runs daily (UTC 16:00 = KST 01:00 per `worker.py:101`). General feeds piggyback on the same task; no new schedule entry needed.

If the per-task wall-clock with general feeds exceeds ~10 min (currently ~2-3 min for 6 facilities), split into two tasks (`curate_facility_news` + `curate_general_news`) running 30 min apart. Defer until measured.

### 4.6 Platoon assignment — which model owns which step

Every job in this pipeline is assigned to one platoon member. The principle: pick the smallest model that meets the capability bar, escalate only when the cheaper model demonstrably underperforms. This keeps the daily curate loop fast and the platoon's higher-end members available for harder work.

| Step | Volume / day | Owner | Model | Why this owner |
|---|---:|---|---|---|
| RSS fetch + parse | ~135 raw items (9 feeds × 15) | — | (no model — `feedparser` only) | Pure I/O. No LLM ever. |
| Per-item credibility scoring + summary + arXiv-ID/DOI/popsci-flag extraction (§3.3 prompt) | ~50–100 items after dedup | **Mima** | `qwen3:30b` (Mac Studio) | Production-incumbent for facility curator; reliable structured-JSON output, ~3-5s/call cold, fits volume in <8 min wall-clock total. Capability bar: multi-field JSON + popsci discrimination — Mima clears it on Tier A/B today. Escalate to Blanc only if §10 Q&A flags Tier C accuracy. |
| Regex arXiv-ID / DOI extraction (§5.1, §5.2 fallback) | per item | — | (no model) | Deterministic. The LLM extraction in the same call is the primary; this is just a safety net. |
| Title-cosine dedup (§5.3) | per news item | — | (no model — TF-IDF reuses `arxiv_classifier._tokenize/_tfidf_vector/_cosine`) | Pure retrieval. Faster than any LLM, and the existing corpus cache is warm from `fetch_arxiv_daily`. |
| Featured-of-the-day selection (top 3 by `credibility_score`) | 1 invocation | — | (no model — heuristic sort) | Deterministic; honors `do_not_feature` flag. |
| Daily Discord summary (`📰 General news 2026-MM-DD: AAS Nova 4/5, Phys.org 1/12 …` per §7.6) | 1 invocation | — | (no model — string formatting) | Cheap. Emits the per-source counters that drive future tuning. |
| Social post drafting (existing `draft_posts_for_featured`) | up to 3 featured items | **Blanc** | `llama3.3:70b` (Mac Studio) | Already wired (`NM_OLLAMA_WRITER`). Tweets / threads need creative concise writing; the 70B reliably hits voice + length without prompt acrobatics. Volume is small (≤3/day) so the speed cost is invisible. |
| Newsletter HTML rendering | 1 invocation | — | (no model — Jinja-style string templating) | Existing `_render_*` helpers. |

**Escalation paths (deferred to v2.1+):**

| Step | Trigger to escalate | Escalated owner | Why |
|---|---|---|---|
| Tier-C borderline rescoring (Phys.org item with Mima score in 0.55–0.75) | If Mima Tier-C reject rate > 80% AND Phys.org accept rate < 5% over a 14-day window — i.e. Mima is being either too strict or too noisy on this source | **Blanc** | 70B handles ambiguous popsci-vs-research framing better. Volume tiny (~1–3 borderline items/day), so the cost stays minimal even at Blanc's speed. |
| LLM-extracted arxiv_id integrity check (§7.2 — verify token-overlap ≥ 0.20 between news title and matched paper title before suppressing) | Always — but as a heuristic, not a model call | — (heuristic) | If we ever decide a model is needed here, **Takji** (`phi4:14b`) is the right pick: cheap, good at short-text comparisons. Defer until heuristic proves insufficient. |
| MNRAS Letters / ApJL synthetic-feed summary generation (v2.1 §2.5) | When the synthetic feed ships | **Mima** | Same prompt shape as the main credibility call; volume ~20–30/day. Uses the same `qwen3:30b` instance and prompt template. |

**Naming.** `Mima = qwen3:30b` (NM_OLLAMA_EDITOR), `Blanc = llama3.3:70b` (NM_OLLAMA_WRITER), `Takji = phi4:14b` (NM_OLLAMA_ARXIV). All three live on Mac Studio. Heavy-synthesis member `Rakon = deepseek-r1:671b` (Mac Pro, scheduled warm windows only) is **not** used by this pipeline — the news curator is real-time and small per-call, so paying Rakon's warm-window cost would be wasteful.

**Implementation note.** The existing `news_curator.py` hard-codes `OLLAMA_MODEL = "qwen3:30b"` at module level (line 14). v2 should refactor this to read `NM_OLLAMA_EDITOR` from settings so the platoon name → model binding lives in one place. The new `_ollama_general_review()` helper from §4.4 uses the same constant, so no second model reference appears.

### 4.7 Roster check (2026-05-11 00:31 KST snapshot)

Read against `~/.openclaw/workspace/memory/platoon-roster.md` before finalizing this doc.

| Member | Roster status | Roster job | This doc's ask | Verdict |
|---|---|---|---|---|
| Mima | 🔄 ACTIVE | Evidence linking, agent loop | Per-item credibility scoring (~50–100 calls/day at KST 01:00 fixed slot) | **Compatible.** Curate window is 5–8 min off-peak; agent-loop traffic is light at KST 01:00. No saturation risk. |
| Blanc | 🔄 ACTIVE | Biblio mining (8 thin-evidence pages) | Social post drafting (≤3 calls/day at KST 01:00) | **Compatible but tight.** Biblio mining is a heavy continuous task. Volume here is tiny (≤3 calls), so impact is negligible — but if biblio mining is still running v2.0 launch day, schedule curate→social drafting *after* the curate-finished signal so Blanc gets the calls in series, not in parallel with biblio. Already the case today (`draft_posts_for_featured` runs at the end of `curate_daily_news`). |
| Takji | 🔄 ACTIVE | Agent loop (writer/reviewer) | v2.1 fallback only — arXiv-ID integrity check (heuristic-first, model only if heuristic insufficient) | **Deferred.** No assignment in v2.0; revisit if heuristic underperforms in production. |
| Rakon | 🔥 ACTIVE | Galaxy Evolution final section | None | **No assignment** — explicitly excluded (real-time pipeline, doesn't fit warm-window model). |
| Buddle | 🔄 ACTIVE | Stance jury drain | None | Not used here. |

**Net:** v2.0 assignments are compatible with the current roster. No re-routing needed. If the roster changes materially before Tori starts implementation (e.g. Mima takes on a heavier base load), revisit this section before code lands.

---

## 5. Deduplication against arXiv

Three layers, in order. First match wins; no further checks.

### 5.1 arXiv-ID extraction (cheap, deterministic)

The credibility prompt asks the LLM to extract `paper_arxiv_id`. As fallback, regex on title + excerpt + link URL:

```python
_ARXIV_ID_RE = re.compile(r"(?:arxiv[:/]\s*|arxiv\.org/abs/)(\d{4}\.\d{4,5})", re.IGNORECASE)

def _extract_arxiv_id(title: str, content: str, link: str | None) -> str | None:
    for s in (title, content, link or ""):
        if m := _ARXIV_ID_RE.search(s):
            return m.group(1)
    return None
```

Then:

```python
def _is_dup_of_arxiv(db, arxiv_id: str) -> bool:
    return db.query(ArxivPaper).filter_by(arxiv_id=arxiv_id).first() is not None
```

If the news item maps to an arxiv_paper we already have, **suppress the news item** (don't store it). The newsletter will already render the arXiv paper itself in the Results section. Logging: write a row to `ExternalSourceLog` (the same audit table arxiv_ingest uses) with `decision='news_item_dup_of_arxiv', external_id=news_slug, notes=arxiv_id`.

Rationale for suppression rather than cross-link: news items rephrase the arXiv abstract; rendering both creates redundancy. Power users care about the original; casual readers don't need both.

### 5.2 DOI extraction (fallback)

If no arXiv ID, but the LLM extracted a DOI: query `evidence.doi` and `arxiv_papers` (no DOI column today — *gap, see §7*). For v2.0, only check against `evidence.doi` and `facility_news_items.paper_doi`. If matched, suppress.

### 5.3 Title similarity (last-resort fallback)

For news items where neither arXiv ID nor DOI was extractable, do a 30-day-window TF-IDF cosine against `arxiv_papers.title`. Threshold 0.70. Reuse the existing `arxiv_classifier._tokenize` + `_tfidf_vector` + `_cosine` helpers.

```python
def _is_dup_by_title(db, title: str) -> str | None:
    """Return matching arxiv_id if title cosine ≥ 0.70 against any arxiv paper from last 30 days, else None."""
    cutoff = datetime.utcnow() - timedelta(days=30)
    candidates = db.query(ArxivPaper).filter(ArxivPaper.created_at >= cutoff).all()
    if not candidates:
        return None
    from app.services.arxiv_classifier import _tokenize, _tfidf_vector, _cosine, _corpus
    news_tokens = _tokenize(title)
    news_vec = _tfidf_vector(news_tokens, _corpus.idf or {})
    for p in candidates:
        p_vec = _tfidf_vector(_tokenize(p.title), _corpus.idf or {})
        if _cosine(news_vec, p_vec) >= 0.70:
            return p.arxiv_id
    return None
```

If matched, suppress with `decision='news_item_dup_by_title'` for audit.

### 5.4 What we don't dedup

- News items between Tier-A sources (e.g., AAS Nova + Phys.org both covering the same paper). The arXiv-ID dedup catches the most common case (both link to the arXiv preprint or a paper we've already ingested). Cross-source dedup adds complexity for a small win — defer to v2.1.
- Facility-news items vs general news. The 6 facilities have their own slugs (`desi-…`, `jwst-…`); general news uses `aas-nova-…` etc. Title-overlap is rare.

---

## 6. Configuration knobs

Add to `app/config.py`:

```python
# === General astronomy news curator (v2) ===
GENERAL_NEWS_ENABLED        = False      # feature flag; flip to True after Tori smoke-tests one source
GENERAL_NEWS_SCORE_FLOOR_A  = 0.65
GENERAL_NEWS_SCORE_FLOOR_B  = 0.65
GENERAL_NEWS_SCORE_FLOOR_C  = 0.75
GENERAL_NEWS_DEDUP_TITLE_COSINE = 0.70
GENERAL_NEWS_DEDUP_LOOKBACK_DAYS = 30
GENERAL_NEWS_MAX_ITEMS_PER_FEED  = 15    # matches existing _fetch_feed limit
```

Source list itself stays in `news_curator.py` as `GENERAL_FEEDS` — it's a structured constant, not a knob.

---

## 7. Gaps and known limitations

| # | Issue | Impact | Resolution |
|---|---|---|---|
| 7.1 | `arxiv_papers` has no `doi` column | Tier-2 dedup partial (DOI check only against evidence and FNI) | Add `doi` column in a future migration; backfill via ADS lookup for top-N papers. Out of scope here. |
| 7.2 | LLM-extracted arXiv IDs may be wrong (rare) | Could suppress a real news item that doesn't actually map to that arxiv_paper | Add an integrity check: if the LLM returns an arxiv_id, verify the paper exists in `arxiv_papers` AND a token-overlap score with the news title ≥ 0.20 before suppressing. |
| 7.3 | A&A Highlights and AAS Nova feeds may have rate limits | 429s would silently produce zero items | Add per-source success-counter logging; alert if a Tier-A source produces 0 items for 3 consecutive days. |
| 7.4 | New `topic_tags` field has no consumer yet | Stored but unused | Acceptable in v2.0; v2.1 surfaces tags as a chip row in newsletter cards and as a wiki-page back-link signal. |
| 7.5 | Feature-flag default `False` means the curator is dark on first deploy | Designed; flip after smoke test | Tori: deploy with flag off → run `curate_daily_news` once → eyeball ~10 items in DB → flip flag to True for next day. |
| 7.6 | Per-source weekly volume isn't measured yet | Can't tune score floors empirically | Add a post-task summary block: `📰 General news 2026-MM-DD: AAS Nova 4/5 ingested, Phys.org 1/12 ingested (most below 0.75 floor)`. Mirrors the daily Discord summary recommended in `arxiv_wiki_feed_design_v1.md` §6.5. |

---

## 8. Phase rollout

| Phase | Items | Effort |
|---|---|---:|
| **v2.0** | Tier-A feeds (6 sources), schema migration, prompt, dedup §5.1+§5.3, "Highlights" newsletter track, score floors, feature flag | ~2.5 d Tori |
| **v2.1** | Tier-B/C feeds (3 sources) added, post-task source summary (§7.6), arXiv `doi` column + backfill (§7.1), MNRAS Letters / ApJL ADS-derived feeds (§2.5) | ~1.5 d Tori |
| **v2.2** | Tag-driven wiki page back-links (§7.4 surfaces topic_tags), cross-source dedup (§5.4) | ~1 d Tori |

**Phase v2.0 is the minimum-viable shipment** and answers Papa's directive: professional-astronomer news flowing into the newsletter beyond the 6 facilities.

---

## 9. Acceptance criteria for v2.0 ship

- [ ] `facility_news_items.facility_id` is nullable; new columns added per §4.1
- [ ] Tier-A general feeds (6 sources) ingested daily
- [ ] Items below `score_floor` for their tier are dropped with audit log
- [ ] arXiv-ID dedup (§5.1) catches at least 80% of same-paper duplicates in 7-day window
- [ ] Title-cosine dedup (§5.3) catches the rest where no arXiv ID is extractable
- [ ] Newsletter renders the new "Highlights" track between Tools and Results, with `source_publication` badges
- [ ] No regression in the 6 facility tracks (Data / Tools / Results unchanged)
- [ ] Feature flag `GENERAL_NEWS_ENABLED` ships False; smoke test → flip True for next day
- [ ] Daily AAS Nova item appears in the Highlights track within 24h of the source post
- [ ] No item with `popsci_flags` non-empty AND score > 0.65 (prompt's hard rule enforced)

---

## 10. Open questions for Papa

1. **Ship Tier B/C in v2.0 or hold for v2.1?** Recommendation: hold. v2.0 with Tier A only proves the pipeline; Tier C (Phys.org) needs prompt tuning observation before it ships.
2. **Suppress vs cross-link arXiv duplicates.** Recommendation: suppress (§5.1). If you want both rendered with a "📖 AAS Nova on this paper" badge on the arXiv card, that's a v2.1 UX feature — small change to the arXiv paper card renderer.
3. **Newsletter ordering.** Where does Highlights sit? Recommendation: between Tools and Results (`Data → Tools → Highlights → Results`). Highlights is the "wider literature" before our facility-specific Results.
4. **APOD inclusion.** Tier A but daily — could dominate volume. Recommendation: skip in v2.0; Papa's call.

---

## 11. References

- Code: `backend/app/agent_loop/news_curator.py` (244 lines), `newsletter.py` (319 lines)
- Code: `backend/app/agent_loop/worker.py` — `curate-news-daily` beat at `crontab(hour=16)`
- Code: `backend/app/services/arxiv_classifier.py` — TF-IDF helpers reused in §5.3
- Models: `app/models/facility.py` (`FacilityProfile`, `FacilityNewsItem`)
- Sibling design: `arxiv_wiki_feed_design_v1.md` — arXiv pipeline this curator dedups against

— 🔬 Kun
