# Astronomical Surveys Directory — Design v1 — **Papa-approved, ready for Tori**

**Owner:** Kun 🔬  ·  **Status:** ✅ Papa-approved 2026-05-13 — ready for Tori implementation  ·  **Implementer:** Tori
**Date:** 2026-05-13 (KST)
**Filename:** `docs/surveys_directory_design_v1.md`
**Sibling design:** `docs/research_ideas_tab_design_v1.md` — these two ship together; cross-linking is described in §5.

---

## 0. TL;DR

A new **top-level section** at `/surveys` cataloguing the major astronomical surveys (SDSS, DESI, JWST, ALMA, Euclid, HSC-SSP, 2MASS, WISE, Chandra, XMM-Newton, Gaia, eROSITA, Rubin/LSST, …). Each survey has a slug, a description, an archive link, and a structured metadata table (wavelength, sky coverage, redshift range, instruments, current data release, data volume, primary science goals).

- **Standalone** — NOT a wiki tab. New nav entry between **Wiki** and **Directory**.
- **Static-first** — v1.0 is a curated directory; no scheduled scraping. Metadata is hand-seeded from official survey pages and updated by news-curator hooks when a new DR is announced (v1.2+).
- **Connects to Research Ideas** — `research_ideas.survey_combo` currently stores a stringly-typed combo like `"JWST+DESI"`. v1.0 introduces a `research_idea_surveys` join table that resolves each combo into FK references, so the survey detail page can show "ideas that use this survey" and idea cards can deep-link to survey pages.
- **Seeds:** 18 surveys hand-curated by Kun, inserted in the migration.
- **No new models** required — this is data + UI, not synthesis.

---

## 1. Why this section, and why now

### 1.1 The gap

The wiki captures **what we know** (claims) and the Research Ideas tab captures **what to investigate next** (survey-anchored questions). Neither captures **what the surveys actually are** — their footprints, depths, instruments, data releases.

Today this knowledge is implicit in:
- News curator (which knows DR dates for 6 surveys),
- Wiki claims that mention surveys in prose,
- Papa's head.

That's not enough. The Research Ideas v1 design assumes the reader already knows what `"JWST+DESI"` means in terms of sample size, redshift range, and overlap area. A visiting astronomer reading an idea card needs **one click** to pull up the survey's parameters and decide whether the proposed sample is actually achievable.

### 1.2 Why standalone (not a wiki tab)

Surveys are **objects**, not topics. A wiki page (Galaxy Evolution, Dark Energy, Active Galactic Nuclei) is a topic — a body of knowledge under continuous debate. A survey (JWST, DESI) is a fixed observational facility with mostly-stable metadata. Putting surveys under wiki tabs would either:

- Force every wiki page to host the same survey-summary panels (duplication), or
- Embed surveys in only the most-relevant wiki page (which one is JWST's? Galaxy Evolution? AGN? Both?).

Neither works. Surveys deserve their own top-level namespace, the way `/agents`, `/calendar`, and `/news` already do.

### 1.3 Top feature priority

Papa flagged this with Research Ideas as paired v1 deliverables. Treat the bar for this directory as **"would Papa, looking at the JWST page, immediately see the sample-size and footprint numbers he uses when judging a research idea?"** If no, the design has failed regardless of test coverage.

---

## 2. Feature spec — what the section looks like

### 2.1 Navigation placement

`NavBar.tsx` desktop nav currently reads:
```
Home  Wiki  Directory  Explore▾  Council  Appeals  Agents  ...
```

Insert **Surveys** between Wiki and Directory:
```
Home  Wiki  Surveys  Directory  Explore▾  Council  ...
```

The link goes to `/surveys` (the list page). Mobile menu mirrors the same placement.

> Rationale: Wiki (topics) → Surveys (facilities) → Directory (people/agents) — each one a level of indexing the site offers.

### 2.2 List page — `/surveys`

```
┌── Astronomical Surveys Directory ──────────────────────────────────────┐
│  18 surveys · sortable, filterable                                     │
│                                                                         │
│  Filter: [ Wavelength ▾ ] [ Status ▾ ] [ Sky access ▾ ]   Search: [__] │
│  Sort:   [ Active ▾ ] [ Sky coverage ▾ ] [ Most recent DR ▾ ]          │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────────┐│
│  │  🔭 JWST — James Webb Space Telescope                              ││
│  │     Infrared 0.6–28 μm · Space (L2) · operational since 2022       ││
│  │     Primary: high-z galaxy formation, exoplanet atmospheres        ││
│  │     DR: GO Cycle 4 (ongoing)   Archive: MAST                       ││
│  │     Used in 4 Research Ideas on this site                          ││
│  └────────────────────────────────────────────────────────────────────┘│
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────────┐│
│  │  🌌 DESI — Dark Energy Spectroscopic Instrument                    ││
│  │     Optical 0.36–0.98 μm · Kitt Peak (Mayall 4 m)                  ││
│  │     14,000 deg² · z = 0.0–3.5 (LyA z=2.1–4.2)                      ││
│  │     Primary: BAO, RSD, dark energy EOS                             ││
│  │     DR: DR1 (Mar 2025)   Archive: data.desi.lbl.gov                ││
│  │     Used in 6 Research Ideas on this site                          ││
│  └────────────────────────────────────────────────────────────────────┘│
│  ...                                                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

Card content fields (compact): emoji thumbnail, name + acronym, wavelength + facility, key constraint (sky coverage **or** redshift range, whichever is more distinctive), primary science, current DR, archive name, count of linked Research Ideas.

### 2.3 Detail page — `/surveys/{slug}`

```
┌── JWST — James Webb Space Telescope ───────────────────────────────────┐
│  🔭                                                                     │
│  Space-based infrared observatory at Sun-Earth L2.                      │
│  Operational since 2022. PI institution: NASA / ESA / CSA.              │
│                                                                         │
│  ┌─ Key parameters ─────────────────────────────────────────────────┐  │
│  │ Wavelength range      │ 0.6 – 28 μm (NIR + MIR)                  │  │
│  │ Sky coverage          │ Pointed mission (no all-sky survey)      │  │
│  │ Redshift range        │ z ≈ 0 – 20 (limited by photometric depth)│  │
│  │ Key instruments       │ NIRCam, NIRSpec, MIRI, NIRISS, FGS       │  │
│  │ Current data release  │ GO Cycle 4 (ongoing) — ERS, GO/AR public │  │
│  │ Approx. data volume   │ ~50 TB / year, ~250 TB cumulative        │  │
│  │ Primary science       │ Reionization-era galaxies, JWST/NIRSpec  │  │
│  │                       │ deep spectroscopy, exoplanet atmospheres │  │
│  │ Sample-survey programs│ CEERS, JADES, PRIMER, COSMOS-Web,        │  │
│  │                       │ UNCOVER, PEARLS                          │  │
│  │ Operator              │ STScI (NASA), ESA, CSA                   │  │
│  │ Status                │ ✅ Operational                            │  │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  Archive: MAST — https://mast.stsci.edu/  ↗                            │
│  Mission page: https://webb.nasa.gov/  ↗                                │
│                                                                         │
│  ┌─ Research Ideas using JWST on this site ────────────────────────┐  │
│  │  → Galaxy Evolution · "JWST+DESI: sSFR-clumpiness slope at z~2" │  │
│  │  → AGN · "JWST+ALMA: dust torus geometry in obscured AGN"       │  │
│  │  → Reionization · "JWST+VLA: 21cm-Lyα cross-correlation"        │  │
│  │  → Cosmic Web · "JWST+HSC: low-mass satellites in z=1 fields"   │  │
│  │  See all 4 ideas → [/research-ideas?survey=jwst]                │  │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌─ Related wiki pages ────────────────────────────────────────────┐  │
│  │  Galaxy Evolution · AGN · Reionization · Exoplanet Atmospheres  │  │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  Last metadata update: 2026-05-13 (manual seed by Kun)                  │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.4 Required fields per survey

| Field | Type | Example | Source |
|---|---|---|---|
| `slug` | string, unique | `"jwst"` | manual |
| `name` | string | `"JWST"` | manual |
| `full_name` | string | `"James Webb Space Telescope"` | manual |
| `description` | text | (1–2 paragraphs) | manual, AGPL-licensed |
| `wavelength_range` | string | `"0.6–28 μm (NIR + MIR)"` | manual |
| `sky_coverage_deg2` | numeric or null | `14000` for DESI; `null` for pointed | manual |
| `sky_coverage_note` | string | `"Pointed mission — no all-sky survey"` | manual |
| `redshift_range` | string | `"z ≈ 0–20 (depth limited)"` | manual |
| `instruments` | string[] | `["NIRCam", "NIRSpec", "MIRI", ...]` | manual |
| `current_data_release` | string | `"GO Cycle 4 (ongoing)"` | manual + news hook v1.2 |
| `data_volume` | string | `"~50 TB/yr, ~250 TB cumulative"` | manual |
| `primary_science_goals` | text | (2–3 sentences) | manual |
| `flagship_programs` | string[] | `["CEERS", "JADES", "PRIMER", ...]` | manual |
| `operator` | string | `"STScI / NASA / ESA / CSA"` | manual |
| `status` | enum | `"operational"` \| `"commissioning"` \| `"planned"` \| `"retired"` | manual |
| `archive_url` | url | `"https://mast.stsci.edu/"` | manual |
| `mission_url` | url | `"https://webb.nasa.gov/"` | manual |
| `emoji` | string | `"🔭"` | manual |
| `wavelength_band` | enum | `"radio"` \| `"sub_mm"` \| `"infrared"` \| `"optical"` \| `"uv"` \| `"xray"` \| `"gamma"` \| `"astrometric"` \| `"multi"` | manual; powers filter |
| `created_at` | timestamp | auto |
| `updated_at` | timestamp | auto |

### 2.5 What this section is *not* doing in v1.0

- ❌ Auto-scraping survey home pages for DR announcements → news-curator hook in v1.2.
- ❌ Showing live data product counts (papers, samples). v1.1 adds claim/idea counts; live arXiv counts deferred.
- ❌ User submissions of surveys (only Papa or admin can add). v2.0 if needed.
- ❌ Detailed instrument-mode pages (e.g. JWST/NIRSpec/IFU sub-page). Out of scope.
- ❌ Coverage maps / footprint plots. Plain text descriptions only in v1.0.

---

## 3. Data model

### 3.1 New tables

```sql
-- 3.1.a — Surveys
CREATE TABLE surveys (
    id                    SERIAL PRIMARY KEY,
    slug                  VARCHAR(40) NOT NULL UNIQUE,
    name                  VARCHAR(60) NOT NULL,
    full_name             VARCHAR(200) NOT NULL,
    description           TEXT NOT NULL,
    wavelength_range      VARCHAR(120) NOT NULL,
    wavelength_band       VARCHAR(20) NOT NULL,        -- enum, see §2.4
    sky_coverage_deg2     NUMERIC(10,2),                -- nullable for pointed
    sky_coverage_note     VARCHAR(200),
    redshift_range        VARCHAR(60),
    instruments_json      JSONB NOT NULL DEFAULT '[]',  -- string[]
    current_data_release  VARCHAR(120),
    data_volume           VARCHAR(120),
    primary_science_goals TEXT NOT NULL,
    flagship_programs_json JSONB NOT NULL DEFAULT '[]', -- string[]
    operator              VARCHAR(120),
    status                VARCHAR(20) NOT NULL DEFAULT 'operational',
    archive_url           TEXT,
    mission_url           TEXT,
    emoji                 VARCHAR(10),
    created_at            TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at            TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX ix_surveys_wavelength_band ON surveys(wavelength_band);
CREATE INDEX ix_surveys_status          ON surveys(status);
```

### 3.2 Link to Research Ideas

`research_ideas` (introduced in `research_ideas_tab_design_v1.md`) currently stores `survey_combo VARCHAR(40)` — a string like `"JWST+DESI"`. That works for display but is brittle for reverse queries ("show me all ideas that use JWST").

**v1 introduces a join table:**

```sql
-- 3.2.a — Research Ideas ↔ Surveys (many-to-many)
CREATE TABLE research_idea_surveys (
    id          SERIAL PRIMARY KEY,
    idea_id     INT NOT NULL REFERENCES research_ideas(id) ON DELETE CASCADE,
    survey_id   INT NOT NULL REFERENCES surveys(id) ON DELETE RESTRICT,
    UNIQUE (idea_id, survey_id)
);
CREATE INDEX ix_research_idea_surveys_idea   ON research_idea_surveys(idea_id);
CREATE INDEX ix_research_idea_surveys_survey ON research_idea_surveys(survey_id);
```

**Backfill on migration:**

The migration parses every existing `research_ideas.survey_combo` string (format: `"A+B"`), splits on `+`, looks up each token in `surveys.slug` (case-insensitive match against name AND slug), and inserts the corresponding `research_idea_surveys` rows. Tokens that don't resolve are logged and skipped (do NOT raise — better to ship with a few unlinked combos than block the migration).

**Going forward:**

When the Research Ideas pipeline writes a new idea (`generate_research_ideas.py` per the sibling design), it MUST also write the `research_idea_surveys` rows in the same transaction. The `survey_combo` string is preserved for display; the join table is the source of truth for queries.

### 3.3 Link to wiki pages (optional, v1.0)

```sql
-- 3.3.a — Surveys ↔ Wiki pages (many-to-many)
CREATE TABLE survey_wiki_pages (
    id        SERIAL PRIMARY KEY,
    survey_id INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    page_id   INT NOT NULL REFERENCES wiki_pages(id) ON DELETE CASCADE,
    UNIQUE (survey_id, page_id)
);
```

Hand-curated. Used to render "Related wiki pages" on the detail page (§2.3). Optional in v1.0 — if not seeded, the section renders empty and the page still works.

### 3.4 Why not extend `facilities` table

The existing `app/models/facility.py` (used by `news_curator`) tracks **news-emitting** facilities for the news pipeline. Conceptually overlapping but operationally different:

- `facilities` is about "what news feed does this entity emit?" (URL, RSS, watch keywords).
- `surveys` is about "what observational asset is this?" (parameters, archive, DR).

A survey may have 0 or 1 news-feed entries (e.g. JWST has both the STScI press feed and the JWST mission feed). A facility may not be a survey at all (e.g. an observatory site).

**Decision:** keep them separate. Add an optional FK `facilities.survey_id → surveys.id` later if news-curator wants to cross-reference. Out of scope for v1.0.

---

## 4. API design

### 4.1 New router: `app/routers/surveys.py`

```python
@router.get("/api/surveys")                  # list, with filters
@router.get("/api/surveys/{slug}")           # detail by slug
@router.get("/api/surveys/{slug}/ideas")     # ideas using this survey
@router.get("/api/surveys/{slug}/pages")     # wiki pages tagged with this survey
```

### 4.2 `GET /api/surveys`

Query params (all optional):
- `wavelength_band` — filter (`infrared`, `optical`, ...)
- `status` — filter (`operational`, `planned`, ...)
- `sort` — `name` (default), `-sky_coverage_deg2`, `-updated_at`
- `q` — full-text search over `name + full_name + description + primary_science_goals`

Response shape:
```json
{
  "count": 18,
  "surveys": [
    {
      "slug": "jwst",
      "name": "JWST",
      "full_name": "James Webb Space Telescope",
      "emoji": "🔭",
      "wavelength_range": "0.6–28 μm (NIR + MIR)",
      "wavelength_band": "infrared",
      "sky_coverage_deg2": null,
      "sky_coverage_note": "Pointed mission — no all-sky survey",
      "redshift_range": "z ≈ 0–20 (depth limited)",
      "primary_science_one_line": "Reionization-era galaxies, JWST/NIRSpec deep spectroscopy, exoplanet atmospheres",
      "current_data_release": "GO Cycle 4 (ongoing)",
      "archive_url": "https://mast.stsci.edu/",
      "status": "operational",
      "linked_research_ideas_count": 4
    },
    ...
  ]
}
```

Note: `linked_research_ideas_count` is computed via `SELECT count(*) FROM research_idea_surveys WHERE survey_id = ?` and joined in a single query. If `research_ideas` table doesn't exist yet (sibling design not yet shipped), default to 0.

### 4.3 `GET /api/surveys/{slug}`

Returns the full detail row + `linked_research_ideas_count` + `related_wiki_page_slugs`:

```json
{
  "slug": "jwst",
  "name": "JWST",
  "full_name": "James Webb Space Telescope",
  "description": "Space-based infrared observatory...",
  "wavelength_range": "0.6–28 μm (NIR + MIR)",
  "wavelength_band": "infrared",
  "sky_coverage_deg2": null,
  "sky_coverage_note": "Pointed mission",
  "redshift_range": "z ≈ 0–20 (depth limited)",
  "instruments": ["NIRCam", "NIRSpec", "MIRI", "NIRISS", "FGS"],
  "current_data_release": "GO Cycle 4 (ongoing) — ERS, GO/AR public",
  "data_volume": "~50 TB/yr, ~250 TB cumulative",
  "primary_science_goals": "Reionization-era galaxies, ...",
  "flagship_programs": ["CEERS", "JADES", "PRIMER", "COSMOS-Web", "UNCOVER", "PEARLS"],
  "operator": "STScI / NASA / ESA / CSA",
  "status": "operational",
  "archive_url": "https://mast.stsci.edu/",
  "mission_url": "https://webb.nasa.gov/",
  "emoji": "🔭",
  "linked_research_ideas_count": 4,
  "related_wiki_page_slugs": ["galaxy-evolution", "active-galactic-nuclei", "reionization", "exoplanet-atmospheres"],
  "updated_at": "2026-05-13T07:00:00Z"
}
```

404 if no survey matches the slug. No auth required (this is public-read directory data).

### 4.4 `GET /api/surveys/{slug}/ideas`

```json
{
  "survey": { "slug": "jwst", "name": "JWST" },
  "count": 4,
  "ideas": [
    {
      "id": 17,
      "page_slug": "galaxy-evolution",
      "page_title": "Galaxy Evolution",
      "survey_combo": "JWST+DESI",
      "question": "Does the sub-kpc clumpy structure JWST/NIRCam resolves...",
      "novelty": 0.78,
      "feasibility": 0.65,
      "saved_by_papa": true,
      "status": "active"
    },
    ...
  ]
}
```

Pulls from `research_ideas` joined via `research_idea_surveys`. Honors `status != 'stale'` and `status != 'rejected'` by default; `?include_stale=1` to see all.

### 4.5 `GET /api/surveys/{slug}/pages`

Returns the wiki pages tagged with this survey via `survey_wiki_pages`:
```json
{
  "survey": { "slug": "jwst", "name": "JWST" },
  "pages": [
    { "slug": "galaxy-evolution", "title": "Galaxy Evolution", "is_featured": true },
    ...
  ]
}
```

### 4.6 Admin endpoints (v1.1)

`POST /api/admin/surveys` and `PATCH /api/admin/surveys/{slug}` — admin-only. Out of scope for v1.0; metadata is updated via Alembic migrations or hand-run SQL until the news-curator hook lands in v1.2.

---

## 5. Frontend

### 5.1 New route: `/surveys/page.tsx`

Top-level list page. Server-renders the surveys list via `GET /api/surveys`. Filters and search are client-side over the loaded set (18 surveys is small enough; no need for server-side filtering in v1.0).

### 5.2 New route: `/surveys/[slug]/page.tsx`

Detail page. Server-renders via `GET /api/surveys/{slug}`. Sections, in order:
1. Header (emoji + name + full_name + 1-paragraph description)
2. Key-parameter table (§2.3)
3. Archive and mission link buttons
4. Research Ideas using this survey (server-render up to 5, "see all" link)
5. Related wiki pages
6. Metadata footer (last update, status)

### 5.3 NavBar update

`frontend/src/app/components/NavBar.tsx` — insert a `/surveys` link in both `NAV_LINKS` (or as a top-level link like Wiki/Directory) AND the mobile dropdown. Suggested code change (kept minimal — no new component needed):

```tsx
// Inside desktop nav, after the /wiki link and before /directory:
<a href="/surveys" style={...}>Surveys</a>

// Mobile mirror inserts the same in the mobile dropdown.
```

### 5.4 Cross-link from Research Ideas tab

The Research Ideas tab (sibling design §2.3) renders idea cards with `survey_combo` displayed as plain text (`"JWST + DESI"`). v1.0 extends this rendering to **deep-link each survey name** in the combo string to `/surveys/{slug}`. Resolution uses the `research_idea_surveys` join table; if not resolvable, fall back to plain text.

### 5.5 What this section is NOT (frontend constraints)

- No new heavy UI library. Uses the inline-style + Tailwind utility patterns already in `NavBar.tsx` and `WikiPageClient.tsx`.
- No D3 / Plotly / coverage-map widgets in v1.0. Plain HTML tables only.
- No client-side caching layer. Pages are server-rendered per request; surveys data is tiny and Vercel/Next caches at the edge for ~5 min.

---

## 6. Seed data — 18 surveys

These are the seeds inserted in the Alembic migration. Hand-curated from official survey pages and current literature as of 2026-05-13. Format below is condensed; the migration inserts the full §2.4 field set.

| Slug | Name | Band | Status | Sky cov. | Archive | Notes |
|---|---|---|---|---|---|---|
| `sdss` | Sloan Digital Sky Survey | optical | operational | 14,000 deg² | SAS @ utah | SDSS-V (operational) |
| `desi` | DESI | optical | operational | 14,000 deg² | data.desi.lbl.gov | DR1 Mar 2025 |
| `jwst` | JWST | infrared | operational | pointed | MAST | GO Cycle 4 ongoing |
| `hst` | HST | uv+optical+nir | operational | pointed | MAST | 35+ years |
| `alma` | ALMA | sub_mm | operational | pointed | ALMA Science Archive | Cycle 11 |
| `euclid` | Euclid | optical+nir | operational | 14,000 deg² (final 6yr) | ESA Cosmology Archive | Q1 release Mar 2025 |
| `hsc-ssp` | Hyper Suprime-Cam SSP | optical | operational | 1,400 deg² (final ~1,200) | HSC SSP @ NAOJ | PDR3 |
| `2mass` | 2MASS | infrared | retired | all-sky | IRSA | Complete 2003 |
| `wise` | WISE / NEOWISE | infrared | operational (NEOWISE-R) | all-sky | IRSA | unWISE coadds public |
| `chandra` | Chandra X-ray Observatory | xray | operational | pointed | CXC HelpDesk / CDA | Cycle 27 |
| `xmm` | XMM-Newton | xray | operational | pointed | XSA @ ESAC | AO-24 |
| `gaia` | Gaia | astrometric | operational | all-sky | Gaia Archive | DR3 (2022), DR4 expected 2026 |
| `erosita` | eROSITA | xray | operational (limited) | all-sky (DE-half) | eROSITA-DE archive | eROSITA-DE DR1 |
| `rubin-lsst` | Rubin / LSST | optical+nir | commissioning | 18,000 deg² (planned) | LSST Data Facility (planned) | DP0.2 public; first light 2026 |
| `roman` | Nancy Grace Roman Space Telescope | nir | planned | 2,000 deg² (HLWAS planned) | MAST (planned) | Launch ~2027 |
| `vla` | Karl G. Jansky Very Large Array | radio | operational | pointed | NRAO Archive | VLASS DR4 |
| `pfs` | Subaru PFS | optical | commissioning | 1,400 deg² (planned) | NAOJ (planned) | SSP starts ~2026 |
| `planck` | Planck | microwave+sub_mm | retired | all-sky | Planck Legacy Archive | PR4 / NPIPE final |

**Why 18 (and not 25)?** Seeds are curated for breadth across all bands and current relevance to NebulaMind's existing wiki/idea content. Adding more surveys later is a single INSERT; over-seeding the migration with cold entries wastes review time. Notable absences and rationale:

- **SKA, CMB-S4, LISA** — planned/future, no current data products. Add when first DR is announced.
- **Pan-STARRS** — superseded by Rubin for the same science use cases. Add if Papa wants it.
- **Spitzer, Herschel, Kepler/K2** — retired but still cited heavily. Reasonable v1.1 add.
- **VLT, Keck, Subaru-prime, Gemini** — these are *facilities*, not surveys. Out of scope; would land in a separate `facilities` directory.
- **CGRO, INTEGRAL, NICER, IXPE** — niche bandpass coverage; v1.1 if Papa requests.

The full seed dataset (each row with all §2.4 fields filled) is delivered in:
```
backend/alembic/versions/surveys_directory_v1.py  (migration body)
```
as a Python `SEEDS = [...]` list inserted with `op.bulk_insert(surveys, SEEDS)`. Tori writes the bulk_insert; Kun supplies the dataset as `data/seed_surveys.json` checked into the repo.

---

## 7. Platoon Assignment

This is a static directory in v1.0. The only ongoing work is metadata updates when data releases land, and most of that is one-line edits.

| Step | Owner | Why this member | Frequency | Hardware footprint |
|---|---|---|---|---|
| Initial seed authoring (18 rows) | **Kun (manual)** | Domain knowledge + judgment on what fields actually matter to a working astronomer. No model in the platoon is better than Kun for this one-shot curation. | One-shot, pre-launch | API only |
| Migration implementation | **Tori** | Standard Alembic + bulk_insert. Sonnet handles this comfortably. | One-shot, on Tori's normal cadence | API only |
| New survey row additions (post v1.0) | **HwaO or Papa direct** | Trivial INSERTs; no model reasoning needed. | Ad hoc | None |
| DR-string metadata refresh (v1.2+, news-curator hook) | **Mima** | Already runs news curation at KST 01:00 (`NM_OLLAMA_EDITOR = qwen3:30b`); detecting "new DR announced" from news headlines is in her wheelhouse — non-astronomy classification of news triage. Atom-7B is overkill for "extract DR version string from press-release title". | When news-curator flags a DR-class headline; estimated <1 call/week per survey | ~18 GB on Mac Studio; no schedule change |
| Survey description prose extension (v1.2+, on-demand) | **Blanc** | Description text is non-astronomy-domain enough (operational specifics, mission history) that the general-domain drafter handles it. AstroSage-70B reserved for science prose, not press-release rewriting. | On Papa request only | ~42 GB Mac Studio; not co-load with AstroSage-70B |

**Members explicitly NOT assigned:**

- **Rakon** — no synthesis work in v1.0; static facts don't need 671B reasoning.
- **AstroSage-70B** — descriptions are mission/facility framing, not science synthesis.
- **Atom-7B** — no scoring task in v1.0.
- **Buddle, Tera, Nutty, Takji** — no fit.

**Rakon explicitly excluded** because there's nothing for him to do here — the v1.0 dataset is hand-authored and the v1.2 refresh is news-triage. If a future version adds science-summary regeneration ("describe what each survey is contributing to Galaxy Evolution this quarter"), that's a separate design and Rakon (skeleton) → AstroSage-70B (prose) would be the right chain.

---

## 7.5 Roster check

Per `feedback_platoon_assignment.md`: read the live roster before locking platoon assignments.

**Snapshot (2026-05-13 KST) from `~/.openclaw/workspace/memory/platoon-roster.md`:**

| Member | Status | Current job | v1.0 conflict? |
|---|---|---|---|
| 🦖 Rakon | (assumed ACTIVE on Galaxy Evolution) | Galaxy Evolution synthesis | **Not assigned here** — no conflict |
| Mima | 🔄 ACTIVE | Evidence linking, agent loop | v1.2 use only (post-launch). Compatible — DR-refresh is rare and off-peak. |
| Blanc | 🔄 ACTIVE | Biblio mining | v1.2 use only (post-launch). Compatible — Blanc work is on-demand only. |
| Tori | 🔄 ACTIVE | Tasks 14 & 15 | Tori handles the implementation; standard Sonnet cadence, no conflict |
| Kun | (this work) | This design + seed dataset | Self-assigned. |
| Others | (active) | various | **Not assigned** — no conflict |

**Net summary:** Zero v1.0 hardware conflicts because v1.0 has zero scheduled model jobs. v1.2 assignments (Mima, Blanc) are both compatible with their current loads — both are infrequent on-demand calls. If the roster shifts between design lock and v1.2 implementation, re-evaluate before enabling the news-curator DR-refresh hook.

---

## 8. Migration plan

Migration: `backend/alembic/versions/surveys_directory_v1.py`

Steps in order:

1. `CREATE TABLE surveys` (§3.1).
2. `CREATE TABLE survey_wiki_pages` (§3.3).
3. `bulk_insert` the 18 seeds with `SEEDS` list.
4. If `research_ideas` table exists (i.e. sibling migration has run): `CREATE TABLE research_idea_surveys` and run the backfill loop (§3.2).
5. If `research_ideas` does not yet exist: skip step 4 with a log warning. The sibling migration (`research_ideas_v1`) handles the join table itself if it runs second. **Both migrations must check for the other and create the join table whichever runs second.**

Downgrade: drop in reverse order.

---

## 9. Rollout

### 9.1 v1.0 — Static directory + cross-link (this design)
- Schema, seeds, list page, detail page, NavBar entry
- Backfill `research_idea_surveys` from existing `research_ideas.survey_combo` strings
- Research Ideas idea cards deep-link survey names to `/surveys/{slug}`

### 9.2 v1.1 — Filter polish + admin
- Wavelength-band filter
- Status filter
- Search (frontend-only, no server-side)
- Admin POST/PATCH endpoints behind admin auth
- "Related wiki pages" section populated for the 5 most-cited surveys

### 9.3 v1.2 — News-curator hook
- News-curator pipeline detects DR-class headlines (Mima, KST 01:00 window)
- Auto-PR (writes `update_surveys.py` script) updates `current_data_release` field
- Discord webhook to #general on each auto-update

### 9.4 v2.0 — Coverage maps + community
- Footprint sky-projection visual (Aitoff projection PNG generated nightly)
- Optional community-submitted survey entries with adversarial gate

---

## 10. Decisions log (all resolved 2026-05-13)

All open questions raised during design review have been resolved by Papa. This section records the final decisions; nothing here is open.

| # | Question | Papa's decision | Implementation locus |
|---|---|---|---|
| Q1 | Include planned surveys (Roman, Rubin-LSST commissioning, PFS commissioning)? | **Yes** ✅ — list with `status='planned'` badge. They're cited in current Research Ideas seeds; excluding them would break cross-links. | §6 seed list (already populated); §2.4 status enum |
| Q2 | Migration coupling with `research_ideas` for `research_idea_surveys` join table | **Conditional-create pattern approved** ✅ — each migration checks for the other table and creates the join whichever runs second. Tori documents this clearly in both migration files. | §3.2 backfill, §8 migration step 4-5 |
| Q3 | Include retired surveys (2MASS, Planck, etc.)? | **Yes** ✅ — they're still load-bearing for current cross-survey science. `status='retired'` badge. A retired-but-cited survey is exactly what a researcher needs when reading a JWST+2MASS color cross-match idea. | §6 seed list (already populated); §2.4 status enum |
| Q4 | Seed JSON location | **Separate file: `backend/data/seed_surveys.json`** ✅ — easier hand-edits between migrations, keeps migration file readable. Tori writes a `json.load` in the migration. | §6 ("seed dataset is delivered in...") |
| Q5 | Mobile UX for the parameter table | **CSS-only `<dl>` stack below 640px** ✅ — no separate mobile component. | §5.5 (no new heavy UI library) |

---

## 11. Acceptance criteria (for Tori sign-off)

v1.0 ships when **all** of the following are true:

- [ ] `surveys` table exists with the §3.1 schema.
- [ ] `research_idea_surveys` table exists (created by whichever sibling migration runs second).
- [ ] `survey_wiki_pages` table exists.
- [ ] 18 seeds inserted with all required §2.4 fields populated (no nulls in `name`, `full_name`, `description`, `wavelength_range`, `wavelength_band`, `primary_science_goals`).
- [ ] `GET /api/surveys` returns 18 entries, sortable and filterable per §4.2.
- [ ] `GET /api/surveys/jwst` returns the full §4.3 shape.
- [ ] `GET /api/surveys/jwst/ideas` joins through `research_idea_surveys` and returns at least 4 entries (assuming Research Ideas seeds are loaded).
- [ ] `/surveys` route renders the list page per §2.2 with no console errors.
- [ ] `/surveys/jwst` route renders the detail page per §2.3.
- [ ] NavBar shows the `Surveys` link in both desktop and mobile menus.
- [ ] Research Ideas idea cards' survey combo names are clickable and deep-link to `/surveys/{slug}`; unresolvable slugs render as plain text without breaking the layout.
- [ ] Backfill of `research_idea_surveys` from existing `research_ideas.survey_combo` strings succeeds (or completes with a logged skip-list).
- [ ] Migration is reversible (downgrade runs clean against a fresh DB).
- [ ] Papa, on first visit to `/surveys/desi`, finds the page accurate enough to recommend it to a CNU colleague without reservation (subjective; recorded by Papa in #general).

---

## 12. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Hand-seeded metadata goes stale within 6 months (DR strings, status). | High | Medium | v1.2 news-curator hook for `current_data_release`; manual quarterly refresh until then. `updated_at` is shown on the detail page so visitors see the recency. |
| Sibling migration `research_ideas_v1` lands first and the backfill fails on the string-parse step. | Medium | Low | Backfill logs and skips; never raises. Manual reconciliation is a one-time SQL. |
| Survey acronym disambiguation (e.g. "ALMA" vs "the ALMA Cycle 11 release"). | Medium | Low | Slug is the canonical key. Display name is the short acronym. Tooltips show full_name on hover (v1.1). |
| Two surveys with overlapping acronyms (none in v1.0, but e.g. "SDSS" vs "BOSS" / "eBOSS" sub-surveys). | Low | Low | v1.0 lists only top-level surveys. Sub-surveys (BOSS, eBOSS, MaNGA) are mentioned in the parent `flagship_programs` field. |
| Visitor expects coverage map and finds plain text instead. | Low | Low | v2.0 adds maps. v1.0 sets expectations via the section header "Astronomical Surveys Directory" (not "Survey Footprint Explorer"). |
| Detail page is bare for surveys without linked Research Ideas. | Low (only for very obscure surveys) | Low | v1.0's 18 seeds are all well-cited surveys; near-zero risk of bare pages. v1.1 adds wiki-page links to broaden detail-page content. |

---

## 13. Notes / out of scope

- **License:** all hand-authored survey descriptions are AGPL-3.0 (matches existing wiki content license). Field values that are factual (wavelength, sky coverage) are not copyrightable.
- **No PII** stored.
- **No external API calls** at request time; the directory is fully self-contained in our DB.
- **No new model weights** downloaded.
- **No new dependencies** on either backend or frontend.
- This doc is the contract for Tori's v1.0 implementation. Any divergence in implementation must be flagged back to Kun for design update.

---

*— Kun 🔬  ·  Mac Pro  ·  2026-05-13*
