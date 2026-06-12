# Survey Detail Page v1 — Data Releases + Catalog Metadata

**Author:** Kun 🔬 · **Date:** 2026-06-12 · **Status:** Design — for Papa review, then Tori implementation
**Goal:** a researcher on `/surveys/[slug]` can develop a *realistic* research idea grounded in what data actually exists (release history) and how it is structured (catalog metadata).
**Live grounding (all verified 2026-06-12 on Mac Studio prod DB):** 50 `surveys` rows; 30 `survey_datasets` rows covering 19 surveys; 0 `research_idea_datasets` links; 0 catalog-field metadata anywhere; detail page = `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx` (412 lines).
**Companion docs:** `surveys_tab_functional_audit_v1.md` (Explorer fixes, separate track), `surveys_logo_audit_v1.md` (logos, separate track), `autowiki_surveys_v1.md` (freshness loop this design plugs into).

---

## 1. Audit — what exists vs. what's missing

### 1.1 What exists today

| Asset | State | Useful for this goal? |
|---|---|---|
| `surveys.current_data_release` (VARCHAR 120, free text) | 50/50 populated, rich strings like "DR1 (March 2025) — Year 1 BAO + full shape" | Latest release only. No history, no DOI, no structure. `dr_year` (42/50) is regex-derived from it. |
| `surveys.num_sources_count / data_volume_tb / limiting_magnitude` | 39 / 48 / 30 of 50 | Survey-level aggregates, already shown in the parameter table. |
| **`survey_datasets`** (created by `research_ideas_phase3_v1` migration, 2026-05-14) | 30 rows / 19 surveys. Schema already has: `release_year`, `release_label`, `sample_size`, `doi`, `bibcode`, `registry`, `license`, `primary_url`, `url_verified_*` | **Yes — this is half the answer, already built.** But: DOI/bibcode are 0/30 populated; 31 surveys have no rows; and the survey detail page never queries it. It was built as the citable-dataset registry for research ideas (`research_idea_datasets` FK), which has 0 links so far. |
| `dataset_verify` agent loop (`app/agent_loop/dataset_verify.py`) | All 30 dataset URLs verified OK | Reusable for any URLs we add. |
| Autowiki Surveys loop (`autowiki_surveys_v1.md`, weekly, Mac Studio) | Live; its charter explicitly includes "(a) data releases land" and `dr_freshness` is 15% of structural score | Freshness mechanism exists; it just has nothing structured to update yet. |
| Detail page UI | Parameter table (honest "—" for nulls), science goals, ideas, wiki links | No release history section, no datasets/catalog section. |

### 1.2 The two gaps

**Gap A — Release history.** `current_data_release` collapses a survey's whole release timeline into one string. A researcher asking "can I do my analysis on DESI DR1 or do I need to wait for DR2? what did DR1 add over EDR?" gets nothing. No dates, no DOIs, no per-release object counts, no "what changed".

**Gap B — Catalog structure.** Nothing in the DB describes what's *inside* any catalog: column names, units, descriptions. The single highest-leverage artifact for "develop a realistic idea" — "BGS has `Z`, `ZWARN`, `SPECTYPE`, `FLUX_G/R/Z`, stellar masses come from a separate VAC" — does not exist at any layer.

### 1.3 Design decision: extend, don't duplicate

- **Releases are survey-level versioned snapshots** → new table `survey_data_releases`. Do **not** overload `survey_datasets`: a dataset (BGS catalog, MPA-JHU VAC, CEERS imaging) is a *product*; a release (DR1, PDR3) is a *version event*. DESI DR1 contains four of our dataset rows.
- **Catalog fields belong to datasets, not surveys** → new table `survey_catalog_fields` with FK to `survey_datasets`. Column lists differ per catalog (DESI BGS vs. QSO; SDSS photoObj vs. MPA-JHU), so attaching them to the survey would force exactly the kind of lossy flattening we're fixing.
- This makes **expanding `survey_datasets` coverage** (19 → all surveys with public data, ≈42) part of this work, which simultaneously unblocks the dormant `research_idea_datasets` pipeline. One seed effort, two consumers.
- Rejected alternative — JSONB columns on `surveys`: cheaper to seed but unqueryable (no "which surveys' catalogs carry stellar masses?" later), no per-row URL verification, and it repeats the regex-parsing mistake the numeric-columns migration just cleaned up.

---

## 2. DB schema additions

One Alembic revision: `survey_releases_catalog_v1`. Idempotent guards (check `get_table_names()`) like phase3 did.

### 2.1 `survey_data_releases`

```sql
CREATE TABLE survey_data_releases (
    id                SERIAL PRIMARY KEY,
    survey_id         INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    label             VARCHAR(60) NOT NULL,      -- "DR1", "PDR3", "GR6/7", "eRASS1"
    release_date      DATE,                      -- exact when known
    release_year      INT,                       -- always set when known (display + sort fallback)
    summary           TEXT NOT NULL,             -- 1–3 sentences: WHAT CHANGED vs previous release
    n_objects         BIGINT,
    sky_coverage_deg2 NUMERIC(10,2),
    data_volume_tb    DOUBLE PRECISION,
    doi               VARCHAR(200),
    bibcode           VARCHAR(40),               -- release/overview paper
    url               TEXT,                      -- release documentation page
    status            VARCHAR(20) NOT NULL DEFAULT 'released',  -- planned | released | superseded | final
    created_at        TIMESTAMP NOT NULL DEFAULT now(),
    updated_at        TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE (survey_id, label)
);
CREATE INDEX ix_sdr_survey ON survey_data_releases(survey_id);
```

Status semantics: `released` = current/citable; `superseded` = older DR still public; `final` = last-ever release of a completed survey (2MASS Final, UKIDSS DR11); `planned` = announced, no data (DESI DR2, Gaia DR4, Rubin DP1). Frontend renders `planned` dimmed, newest non-planned highlighted.

**Not** auto-syncing `surveys.current_data_release` in v1 — it stays the denormalized one-liner for list/Explorer views. Consistency guard instead: extend `compute_survey_health()` with a cheap check that the newest non-planned release label appears inside `current_data_release`; mismatch lowers `dr_freshness`, which the existing autowiki loop is already incentivized to fix. ORM model goes in `app/models/survey.py` beside `Survey`.

### 2.2 `survey_catalog_fields`

```sql
CREATE TABLE survey_catalog_fields (
    id          SERIAL PRIMARY KEY,
    dataset_id  INT NOT NULL REFERENCES survey_datasets(id) ON DELETE CASCADE,
    name        VARCHAR(80) NOT NULL,    -- column name as in the actual catalog: "Z", "ZWARN", "FLUX_R"
    dtype       VARCHAR(20),             -- float64 / int64 / string / bool / array
    unit        VARCHAR(40),             -- "mag", "nanomaggies", "deg", "km/s", NULL if dimensionless
    ucd         VARCHAR(80),             -- optional IVOA UCD, e.g. "src.redshift" (nice-to-have, nullable)
    description TEXT NOT NULL,
    example     VARCHAR(120),            -- optional representative value
    is_key      BOOLEAN NOT NULL DEFAULT false,  -- the ~10–25 columns a researcher reads first
    sort_order  INT NOT NULL DEFAULT 0,
    source_url  TEXT,                    -- datamodel page this row was transcribed from (provenance)
    UNIQUE (dataset_id, name)
);
CREATE INDEX ix_scf_dataset ON survey_catalog_fields(dataset_id);
```

`is_key` is the curation lever: we seed *key* columns (the ones that shape a science case), not full datamodels (DESI zcatalog alone has 100+ columns; transcribing all is noise and a maintenance trap). `source_url` is mandatory in practice (seeding rule, not DB constraint) — every row must be traceable to an official datamodel page.

### 2.3 `survey_datasets` — no schema change, two data obligations

1. **Coverage expansion:** every survey with public data (≈42 of 50; excludes ELT/ngVLA/SKA1/CMB-S4/Roman/PFS/4MOST-pre-DR/WEAVE-pre-DR class) gets ≥1 row for its flagship catalog.
2. **Citation backfill:** `doi` + `bibcode` populated for all rows (currently 0/30) via ADS lookup. This also serves research-idea citability.

---

## 3. Seed strategy

### 3.1 Format: versioned JSON seed files in git

`backend/seeds/survey_releases/{survey_slug}.json` and `backend/seeds/catalog_fields/{dataset_slug}.json`, applied by two idempotent scripts (`scripts/seed_survey_releases.py`, `scripts/seed_catalog_fields.py`, upsert on the natural keys). Same pattern as the existing survey seeding; git-reviewable, re-runnable, and the seed files double as the provenance record. **No LLM generation for catalog fields** — the Galaxy-Evolution marker audit showed LLM-transcribed structured data drifts from source text; catalog columns must be transcribed from official datamodels by hand (Kun).

### 3.2 Sources, in priority order

1. **Official data-release / datamodel pages** — DESI `data.desi.lbl.gov/doc/releases/`, SDSS `skyserver` schema browser + `data.sdss.org` datamodel, Gaia `gea.esac.esa.int` data model, Euclid Q1 docs, Rubin DP docs, survey DR pages generally. Primary source for both releases and fields.
2. **ADS** — release/overview paper bibcodes + DOIs (`scripts/` one-shot, ADS API token already used elsewhere in backend).
3. **Existing `surveys.current_data_release` strings** — bootstrap: every survey gets its current release as row 1 mechanically (label/year parsed, summary = the existing string), then history is added on top. Guarantees no survey regresses below today's information level.

### 3.3 Tiered effort (realistic scoping)

| Tier | Surveys | Releases | Catalog fields |
|---|---|---|---|
| **T1 (full treatment)** | DESI, SDSS, Gaia, Euclid, DES, KiDS, HSC-SSP, Rubin, eROSITA, GAMA, COSMOS2020, JWST (≈12) | Full DR timeline (3–8 rows each) | Key fields for each flagship catalog (10–25/catalog) |
| **T2** | Remaining released surveys (≈30) | Current + final + 1–2 majors (1–3 rows) | Flagship catalog only, ~10 key fields, best-effort |
| **T3 (no public data)** | ELT, ngVLA, SKA1, CMB-S4, Roman, PFS, 4MOST, WEAVE (≈8) | 1 `planned` row | none (honest empty state) |

Estimate: T1 ≈ 60 release rows + ~20 catalogs × ~18 fields ≈ 360 field rows; T2 ≈ 60 release rows + ~300 field rows. All hand-curated by Kun; a few focused sessions. T1 ships first — the page design must not assume full coverage.

### 3.4 Freshness (after seed)

Owned by the existing **Autowiki Surveys loop** (weekly, Mac Studio) — extended with a `release_check` edit type: probe T1 release pages, propose new `survey_data_releases` rows through the existing proposal/scoring/rollback machinery. **Platoon assignment for that step:** page fetch + diff = pure Python (no model); structured extraction of a detected new release into a row = **Claude Sonnet API** (the one model verified reliable for sync structured JSON — deepseek-r1/qwen3 return empty content under saturation, per platoon limits log); judge scoring unchanged from autowiki_surveys_v1. Catalog fields have no automated freshness — datamodels are immutable per release; new release ⇒ Kun curates fields for its flagship catalog. This is a v1.1 extension; v1 ships with manual seed only and no new cron jobs.

---

## 4. API changes (backend, `routers/surveys.py`)

1. **`GET /api/surveys/{slug}`** — add to the existing response:
   - `data_releases`: full list, ordered `release_date/year DESC NULLS LAST`, each `{label, release_date, release_year, summary, n_objects, sky_coverage_deg2, data_volume_tb, doi, bibcode, url, status}`. ≤10 rows/survey; no pagination.
   - `datasets_count`: int (cheap COUNT, drives section visibility without a second fetch).
2. **`GET /api/surveys/{slug}/datasets`** (new) — datasets for the survey, each with nested `catalog_fields` ordered by `is_key DESC, sort_order`: `{slug, name, full_name, description, data_type, release_label, release_year, sample_size, doi, bibcode, registry, license, primary_url, archive_url, url_verified_ok, catalog_fields: [{name, dtype, unit, description, example, is_key}]}`. Fetched when the section mounts (it's below the fold); worst case (DESI: 4 datasets × ~20 fields) is a few KB.

Both read-only, parameterized SQL, same style as the existing router. Graceful degradation: missing tables → empty lists (same try/except pattern as `_idea_counts_by_survey_id`).

---

## 5. UI spec for Tori (`SurveyDetailClient.tsx`)

Two new sections inserted **after the Survey Parameters table, before Primary Science Goals** — they are the page's new core purpose (what data exists → how it's structured → then why/science). Existing visual language: `#1e293b` cards, `#162032` headers, uppercase section labels, honest "—"/empty states.

### 5.1 Section "Data Releases" — `ReleaseTimeline` component

- Vertical timeline, newest first. Per entry: **label chip** (e.g. `DR1`) + date (`March 2025`, year-only if no date) + status badge, then summary text (the "what changed" line), then a small metadata row: `~18.7M objects · 14,000 deg² · DOI ↗ · Release notes ↗` (omit missing parts silently).
- Newest `released/final` entry: accent border (`#6366f1`) + "Current" badge. `planned` entries: 0.55 opacity + "Planned" badge, shown at top (they're the future). `superseded` entries: normal rows.
- Empty state (T3 surveys, no rows or only-planned): keep section, one line — "No public data releases yet" + the planned row if any. Never hide the section: absence of data is information for a researcher.
- No new dependencies, no chart library — flexbox + a left border line.

### 5.2 Section "Data Products & Catalogs" — `DatasetCatalogs` component

- Render only when `datasets_count > 0`; fetch `/api/surveys/{slug}/datasets` on mount.
- One **accordion card per dataset** (collapsed by default; auto-expand when exactly one dataset). Header row: name + `data_type` chip (`spectroscopic_catalog` → "Spectroscopic catalog") + release label + sample size (reuse existing `formatSources`) + license. Header right: `Data ↗` (primary_url; append the existing url-verified pattern — render the link dead-styled with a "link unverified" title when `url_verified_ok === false`).
- Expanded body: description paragraph, citation line (`bibcode` linking to `https://ui.adsabs.harvard.edu/abs/{bibcode}` + DOI link), then the **catalog field table**:
  - Columns: **Column · Type · Unit · Description** (4-col grid, same `ParamRow` zebra styling; monospace for Column).
  - `is_key` rows first; if non-key rows exist, fold them behind "Show all N columns".
  - \>15 visible rows → client-side substring filter input over name+description.
  - No fields seeded yet → single line: "Column-level metadata not yet curated for this catalog." (section still shows the dataset card — partial data must not look broken).
- Mobile: the field table grid may collapse to stacked rows; fine — the Explorer's desktop-only lockout does not apply to the detail page.

### 5.3 Touch-ups in the same PR

- Parameter table's "Data Release" row: append `· N releases ↓` anchor-linking to the timeline when `data_releases.length > 1`.
- Footer "manual seed by Kun" line unchanged — still true.
- Build/deploy reality (from functional audit): `npm run build` + restart required; verify BUILD_ID after deploy.

---

## 6. Acceptance criteria

**DESI (`/surveys/desi`) — T1 reference:**
1. Timeline shows ≥3 entries: EDR (June 2023, SV data), **DR1 (March 2025, "Current", ~18.7M redshifts, DOI + release-page links working)**, DR2 (`planned`, dimmed).
2. Catalogs section lists ≥4 datasets (BGS, LRG, ELG, QSO) with sample sizes; BGS expands to ≥12 key columns (`TARGETID`, `Z`, `ZWARN`, `SPECTYPE`, `ZERR`, `FLUX_G/R/Z`, `RA`, `DEC`, …) each with type, unit where applicable, and a description matching the official DESI datamodel (`source_url` recorded in seed).
3. Every external link resolves (DOI → doi.org, bibcode → ADS, release URL → 200).

**SDSS (`/surveys/sdss`):** timeline carries the major arc (EDR/DR7/DR12/DR16/DR17-final era, ≥4 rows incl. DR17 as current legacy); MPA-JHU dataset expands with stellar-mass/SFR columns.

**ELT (`/surveys/elt`) — honest-empty:** Data Releases section renders "No public data releases yet" + planned first-light note; no catalogs section; nothing looks broken.

**Behavioral test:** Papa opens `/surveys/desi` cold and can answer, without leaving the page: *which release is citable today, what it contains, what columns the BGS catalog gives him, and what's coming next* — i.e., enough to scope a real DR1-based project.

**Non-regression:** `/api/surveys` list endpoint unchanged; Explorer untouched; surveys with zero new seed rows render exactly as today plus an honest empty timeline bootstrap row (§3.2-3 guarantees ≥1).

---

## 7. Implementation order

1. **Tori:** Alembic migration + ORM models + API (§2, §4) — mergeable alone, returns empty lists.
2. **Kun:** bootstrap seed (current_data_release → 1 row × 50 surveys) + T1 release timelines + DOI/bibcode backfill on existing 30 datasets.
3. **Tori:** UI sections (§5) against the seeded API; acceptance pass on DESI/SDSS/ELT.
4. **Kun:** T1 catalog fields, then T2 rolling — UI already tolerates partial coverage by design.
5. **v1.1 (separate approval):** autowiki `release_check` extension (§3.4).

Steps 1–2 parallelize; 3 needs both.

---

## 8. Out of scope (explicit)

- Cross-survey field search / "which surveys have stellar masses" UI (schema supports it later; no v1 surface).
- Full datamodel mirroring (>25 columns/catalog) — curation, not replication.
- Auto-sync of `surveys.current_data_release` from release rows (health-check nudge only, §2.1).
- Explorer changes (functional-audit track) and logos (logo-audit track).
- TAP/VO live queries against archives — far future.
