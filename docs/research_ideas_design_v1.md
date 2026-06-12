# Research Ideas Layer — Phase 3 Design v1

**Owner:** Kun 🔬  ·  **Implementer:** Tori  ·  **Status:** Draft, awaiting Papa sign-off
**Date:** 2026-05-14 (KST)
**Filename:** `docs/research_ideas_design_v1.md`
**Path note:** Papa's directive said `~/NebulaMind/docs/`; the real docs dir is `~/NebulaMind/NebulaMind/docs/`. This file is saved at the real path.

**Companion docs (read first):**
- `docs/research_ideas_tab_design_v1.md` — Phase 1/2 (UI tab, survey-combo prompts, seed ideas). Still the source of truth for tab UX, prompt skeletons, and the 15 galaxy-evolution seeds.
- `docs/surveys_directory_design_v1.md` — `surveys` table schema & 49 seeded surveys.
- `docs/autowiki_surveys_v1.md` — autoresearch loop keeping survey numeric fields current.
- `docs/galev_quality_roadmap.md` — galaxy-evolution flagship work, the pilot target.

---

## 0. TL;DR

Phase 3 promotes Research Ideas from a per-page list to a **structured, claim-anchored, dataset-verified knowledge layer**. Three things change:

1. **Anchor unit becomes the claim, not just the page.** Every idea points to exactly one *primary claim* (the question the idea would settle) plus 0+ supporting anchors. Ideas surface inline next to that claim, not only in the tab.
2. **Dataset cards become first-class.** A new `survey_datasets` table represents specific data products (DESI DR1 BGS, SDSS MPA-JHU, HST Hubble Deep Field) — a finer granularity than the existing `surveys` table (DESI, SDSS, HST). Ideas link to datasets, not surveys, because that's the unit a researcher actually loads.
3. **Verification pivots from arXiv to dataset registries.** ADS / VizieR / NASA-IPAC / mission archive whitelists replace the arXiv DOI check for the new dataset-link evidence. The existing arXiv evidence loop for *claims* is unchanged.

Trust gets a third axis: ideas are voted on **well-posed / feasible / novel** separately (not a single up-down). Pilot stays on `galaxy-evolution`; the page-level tab and per-claim chips light up together. v1 ships dataset cards + verification + per-claim anchoring; v1.1 adds the multi-axis jury; v2 opens to public idea submission.

---

## 1. Scope & relationship to existing design

### 1.1 What's already built (Phase 1/2 — do not re-design)

Per `research_ideas_tab_design_v1.md` and the existing `app/models/research_idea.py`:

- `research_ideas` table with `survey_combo`, `question`, `why_now`, `approach`, `systematics_json`, `novelty`, `feasibility`, `status`, `model_chain`, `saved_by_papa`, `seeded`.
- `research_idea_anchors(idea_id, kind, ref_id)` for many-to-many anchors to claims / debates / arxiv papers.
- `research_idea_votes(idea_id, user_id, value)` — single-axis save/stale signal.
- `research_idea_surveys(idea_id, survey_id)` — idea ↔ Survey (course-grained) M2M.
- `/api/research/ideas/{slug}` routes + admin regenerate.
- Frontend tab on `galaxy-evolution` with the 15 seed ideas.
- Rakon → AstroSage-70B → Atom-7B production pipeline.

### 1.2 What Phase 3 adds

| New | Description |
|---|---|
| `survey_datasets` table | Data products (DR1 BGS, MPA-JHU, HDF, etc.), parent-keyed to `surveys`. |
| `research_idea_datasets` M2M | Replaces `research_idea_surveys` as the primary join. Old table kept for back-compat for one release. |
| `claim_id` column on `research_ideas` | Direct FK to the *primary anchor* claim (nullable; supplements the anchors table). |
| Dataset verification pipeline | URL/DOI/registry checks against ADS / VizieR / NASA-IPAC / mission archives. |
| Multi-axis voting | Three vote axes: well_posed, feasible, novel. |
| Per-claim inline affordance | Ideas appear inline next to their primary-anchor claim, in addition to the tab. |
| `POST /api/ideas` (user submit, Papa-only in v1) | Authoring path for human-proposed ideas. |
| `GET /api/pages/{slug}/ideas` alias | Matches Papa's prompt convention. |
| `PUT /api/ideas/{id}/vote` | Multi-axis vote endpoint. |

### 1.3 What's explicitly out of scope for Phase 3

- ❌ Idea-versioning / edit history (Phase 4)
- ❌ Cross-page idea linking ("this idea also relevant to AGN-feedback") — deferred
- ❌ Public idea submission (Phase 4 / v2.0)
- ❌ Auto-detect when an idea has been published in arXiv (Phase 5)
- ❌ Threaded comments under ideas — handled by existing `comments.py` if Tori reuses

---

## 2. Data model

### 2.1 `survey_datasets` (NEW)

A **dataset** = a specific, citable data product. One survey produces many datasets (DESI → DR1 BGS, DR1 ELG, DR1 QSO, EDR …). The unit a researcher cites when they say "I used X."

```sql
CREATE TABLE survey_datasets (
    id                  SERIAL PRIMARY KEY,
    survey_id           INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    slug                VARCHAR(80) NOT NULL UNIQUE,         -- "desi-dr1-bgs"
    name                VARCHAR(120) NOT NULL,                -- "DESI DR1 BGS"
    full_name           VARCHAR(300) NOT NULL,                -- "DESI DR1 Bright Galaxy Survey"
    description         TEXT NOT NULL,                        -- 1-3 sentence purpose
    data_type           VARCHAR(40) NOT NULL,                 -- see §2.1.1
    release_year        INT,                                  -- 2024, 2026, ...
    release_label       VARCHAR(60),                          -- "DR1", "DR2", "Q1", "MPA-JHU"
    redshift_range      VARCHAR(60),                          -- "z = 0.01 - 0.6"
    sky_coverage_deg2   NUMERIC(10,2),                        -- 14000.00
    sample_size         BIGINT,                               -- ~14e6
    doi                 VARCHAR(200),                         -- 10.5281/zenodo.xxx
    primary_url         TEXT NOT NULL,                        -- canonical access page
    archive_url         TEXT,                                 -- e.g. NOIRLab archive
    bibcode             VARCHAR(40),                          -- ADS bibcode if exists
    registry            VARCHAR(40),                          -- see §5.1 whitelist
    license             VARCHAR(60),                          -- "CC-BY-4.0"
    status              VARCHAR(20) NOT NULL DEFAULT 'active',
                        -- active | superseded | embargoed | deprecated
    url_verified_at     TIMESTAMP,                            -- last successful registry check
    url_verified_ok     BOOLEAN,                              -- last check result
    url_verified_note   TEXT,                                 -- error / 'ok'
    created_at          TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX ix_survey_datasets_survey   ON survey_datasets(survey_id);
CREATE INDEX ix_survey_datasets_type     ON survey_datasets(data_type);
CREATE INDEX ix_survey_datasets_status   ON survey_datasets(status);
```

#### 2.1.1 `data_type` enum (extensible via VARCHAR)

`spectroscopic_catalog` · `photometric_catalog` · `imaging` · `time_domain` · `ifu_cube` · `interferometric_visibility` · `cmb_map` · `weak_lensing_catalog` · `cluster_catalog` · `qso_catalog` · `transient_alert_stream`

Used by the prompt to constrain "what surveys can deliver" sentences and by the verification step to pick the right registry check (e.g., spec-cat → VizieR mirror likely available; IFU cube → ALMA/JVO archive).

### 2.2 `research_idea_datasets` (NEW)

```sql
CREATE TABLE research_idea_datasets (
    id           SERIAL PRIMARY KEY,
    idea_id      INT NOT NULL REFERENCES research_ideas(id) ON DELETE CASCADE,
    dataset_id   INT NOT NULL REFERENCES survey_datasets(id) ON DELETE RESTRICT,
    role         VARCHAR(20) NOT NULL DEFAULT 'primary',
                 -- 'primary' | 'secondary' | 'support'
    note         TEXT,                                       -- optional, why this dataset
    created_at   TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (idea_id, dataset_id)
);
CREATE INDEX ix_rid_dataset ON research_idea_datasets(dataset_id);
```

`role='primary'` are the datasets the idea *requires* to answer the question (typically 2 — matching the survey-combo framing). `secondary` are nice-to-haves; `support` are calibration / validation sources.

### 2.3 `research_ideas` column additions

```sql
ALTER TABLE research_ideas
  ADD COLUMN claim_id              INT REFERENCES claims(id) ON DELETE SET NULL,
  ADD COLUMN well_posed_score      NUMERIC(3,2),    -- 0..1, populated by Phase 3 jury
  ADD COLUMN well_posed_updated_at TIMESTAMP,
  ADD COLUMN datasets_verified     BOOLEAN NOT NULL DEFAULT FALSE,
  ADD COLUMN datasets_verified_at  TIMESTAMP;

CREATE INDEX ix_research_ideas_claim ON research_ideas(claim_id);
```

`claim_id` is the **primary anchor claim** — the contested or under-supported claim the idea would settle. `research_idea_anchors` (existing) still holds the full anchor graph; `claim_id` is the shortcut for the inline UI affordance.

`well_posed_score` joins the existing `novelty` and `feasibility` triplet. v1.0 ships with default 0.5 (un-juried); v1.1 lights up the well-posed jury (§6).

`datasets_verified` is a derived bool: TRUE iff every `role='primary'` dataset has `url_verified_ok=TRUE` and verified-at within 30d. Computed by the verification cron (§5); persisted for fast filter.

### 2.4 Old `research_idea_surveys` — deprecation path

Keep the table for one release. Backfill it on insert: for every new `research_idea_datasets` row, also insert `research_idea_surveys(idea_id, survey_id=datasets.survey_id)` if not already present. Existing tab UI that joins on `research_idea_surveys` keeps working unchanged.

Drop the back-compat write in v1.2 once the frontend has been switched to query `research_idea_datasets`.

### 2.5 Alembic migration plan

Single migration `research_ideas_phase3_v1.py`:

1. `CREATE TABLE survey_datasets`
2. `CREATE TABLE research_idea_datasets`
3. `ALTER TABLE research_ideas ADD COLUMN …` (5 cols above)
4. Seed ~40 datasets from §3.2 in the same migration (idempotent INSERT … ON CONFLICT DO NOTHING by slug).
5. Backfill `research_idea_datasets` from `research_idea_surveys` where possible (a survey-only link maps to the survey's flagship dataset — see mapping table §3.3).

Zero-downtime: all additive. No data loss path.

---

## 3. Dataset registry (the seed catalog)

### 3.1 Seed criteria

A dataset enters the v1.0 registry iff:
- Has a canonical access URL (mission/archive page, ADS abstract, or VizieR catalog).
- Status is `active` or `superseded` (not embargoed, not announced-but-unreleased).
- Belongs to a survey already in the `surveys` table.
- Has a clear `data_type` from §2.1.1.

### 3.2 v1.0 seed list (~40 datasets, galaxy-evolution-relevant)

This is the implementation list Tori inserts in the migration. Full triples (slug, parent survey, data_type) are in `seeds/survey_datasets_v1.py` — the table below is a representative slice.

| Slug | Survey | data_type | Release | Notes |
|---|---|---|---|---|
| `desi-dr1-bgs` | DESI | spectroscopic_catalog | DR1 (2024) | ~14M low-z spec-z; Papa's primary work |
| `desi-dr1-lrg` | DESI | spectroscopic_catalog | DR1 (2024) | LRG sample |
| `desi-dr1-elg` | DESI | spectroscopic_catalog | DR1 (2024) | ELG z = 0.6-1.6 |
| `desi-dr1-qso` | DESI | qso_catalog | DR1 (2024) | quasar redshifts + Lyα |
| `sdss-mpa-jhu` | SDSS | spectroscopic_catalog | DR8 | classic MPA-JHU value-added |
| `sdss-dr17` | SDSS | spectroscopic_catalog | DR17 (2022) | last SDSS-IV |
| `hst-candels` | HST | imaging | 2014- | CANDELS WFC3/ACS |
| `hst-hdf` | HST | imaging | 1995 | Hubble Deep Field, foundational |
| `hst-hudf` | HST | imaging | 2004 | Ultra-Deep Field |
| `jwst-ceers` | JWST | imaging | 2023 | NIRCam + MIRI mosaics |
| `jwst-jades` | JWST | spectroscopic_catalog | 2024 | NIRSpec deep |
| `jwst-primer` | JWST | imaging | 2024 | NIRCam wide |
| `jwst-rubies` | JWST | spectroscopic_catalog | 2025 | NIRSpec MOS |
| `euclid-q1` | Euclid | photometric_catalog | Q1 (2026-03) | Quick Release 1, morphology |
| `euclid-edf` | Euclid | imaging | 2026 | Deep field photometry |
| `lsst-dp02` | LSST | photometric_catalog | DP0.2 | precursor sim release |
| `hsc-ssp-pdr3` | HSC | photometric_catalog | PDR3 (2024) | grizy Wide |
| `hsc-deep` | HSC | imaging | PDR3 | Deep+UltraDeep |
| `alma-aspecs` | ALMA | interferometric_visibility | 2020 | molecular gas survey |
| `alma-rebels` | ALMA | interferometric_visibility | 2022 | z=6-9 [CII] |
| `alma-cristal` | ALMA | interferometric_visibility | 2024 | resolved [CII] |
| `vla-cosmos` | VLA | imaging | 2019 | radio continuum in COSMOS |
| `vla-first` | VLA | imaging | 1995/2014 | wide-area 1.4 GHz |
| `gaia-dr3` | Gaia | photometric_catalog | DR3 (2022) | astrometry+photometry |
| `galex-gr67` | GALEX | photometric_catalog | GR6/7 | UV photometry |
| `wise-allwise` | WISE | photometric_catalog | 2014 | mid-IR all-sky |
| `2mass-xsc` | 2MASS | photometric_catalog | 2003 | extended-source catalog |
| `cosmos2020` | COSMOS | photometric_catalog | 2022 | multi-band catalog, Weaver+ |
| `cdf-s` | CDF-S | imaging | 2017 | Chandra Deep Field South |
| `eROSITA-edr` | eROSITA | photometric_catalog | eFEDS DR | X-ray catalog |
| `planck-pr3` | Planck | cmb_map | 2018 | full-mission CMB |
| `act-dr6` | ACT | cmb_map | 2024 | high-res CMB |
| `decals-dr10` | DECaLS | imaging | DR10 | DESI imaging legacy |
| `unions-dr1` | UNIONS | imaging | DR1 | u-band + r-band, north |
| `viking-dr5` | VIKING | photometric_catalog | DR5 | NIR survey |
| `pan-starrs-dr2` | Pan-STARRS | photometric_catalog | DR2 (2019) | grizy 3π |
| … | … | … | … | (full list in seed file) |

Target ~40 datasets for v1 covering the surveys in the existing 18 `ALLOWED_SURVEY_COMBOS` and a handful of supporting catalogs (Gaia, WISE, 2MASS, etc.) that show up as `role='support'` in many ideas.

### 3.3 Survey → flagship dataset mapping (for backfill)

Used by the migration step 5 (§2.5) to convert old `research_idea_surveys` rows to new dataset rows.

| Survey slug | Flagship dataset slug |
|---|---|
| `desi` | `desi-dr1-bgs` |
| `sdss` | `sdss-mpa-jhu` |
| `hst` | `hst-candels` |
| `jwst` | `jwst-ceers` |
| `euclid` | `euclid-q1` |
| `lsst` | `lsst-dp02` |
| `hsc` | `hsc-ssp-pdr3` |
| `alma` | `alma-aspecs` |
| `vla` | `vla-cosmos` |

If a survey isn't in this map, the backfill leaves `research_idea_datasets` empty for that idea and logs a warning; Tori fills in manually post-migration.

---

## 4. Agent workflow — extended idea generation

The Rakon → AstroSage-70B → Atom-7B pipeline from Phase 1/2 stays. Phase 3 adds two pre/post passes:

### 4.1 Pre-pass — dataset context bundler

Before calling Rakon, the bundler now joins **survey_datasets** into the context, not just claims/arxiv:

```
DATASETS AVAILABLE (filtered to combo surveys)
----------------------------------------------
DESI:    desi-dr1-bgs (DR1, 14M spec-z, z=0.01-0.6, primary_url=...)
         desi-dr1-elg (DR1, z=0.6-1.6, ELG selection)
         desi-dr1-qso (DR1, ~1.8M QSOs incl. Lyα)
JWST:    jwst-ceers (CEERS NIRCam+MIRI imaging, 100 arcmin²)
         jwst-jades (NIRSpec deep prism+G395M, ~5000 spectra)
         jwst-primer (NIRCam wide, ~400 arcmin² COSMOS+UDS)
         jwst-rubies (NIRSpec MOS targeted, ~5000 sources)
ALMA:    alma-aspecs (CO 3-2 → 6-5 in HUDF, 4.5 arcmin²)
         alma-rebels (z=6-9 [CII] survey, ~40 sources)
...
```

Rakon's prompt §3.3.1 (existing) gets two new constraints appended:

> `For each survey in the combo, name the SPECIFIC dataset slug(s) from the list above that would be loaded. Output them under "datasets_primary" (must reference combo surveys) and "datasets_support" (optional).`

> `If no dataset in the list can deliver the measurement, DROP the idea — do not propose data that doesn't exist as a citable product.`

This is the central quality gate: ideas are forced to bind to actual data products, not to "JWST [in general]."

### 4.2 Mid-pipeline — AstroSage polish unchanged

AstroSage-70B's prompt is appended with:

> `Verify each named dataset can support the proposed measurement. Reject the idea (plausible=no) if a dataset's redshift range, sample size, or data_type is wrong for the question (e.g., proposing molecular-gas measurements from a photometric catalog).`

The polish step gets the dataset rows in full as context.

### 4.3 Post-pass — dataset link verification (NEW, see §5)

After Atom-7B scoring but before INSERT:
- For every `role='primary'` dataset on every surviving idea, run the registry check in §5.
- If a primary dataset fails verification, mark `datasets_verified=FALSE`. The idea is still inserted, but the inline UI hides it from the default view (filter `datasets_verified=TRUE` is the default; admin toggle exposes unverified).
- A nightly job re-verifies all dataset URLs (independent of idea generation).

### 4.4 Idea JSON contract (updated)

Rakon's required output schema for each candidate:

```json
{
  "combo": "JWST+DESI",
  "question": "...",
  "primary_claim_id": 8421,
  "anchors": {
    "claim_ids": [8421, 8422, 8430],
    "debate_ids": [],
    "arxiv_ids": ["2026.12345"]
  },
  "datasets_primary": ["jwst-ceers", "desi-dr1-elg"],
  "datasets_support": ["hsc-ssp-pdr3"],
  "why_now_skeleton": "...",
  "approach_skeleton": "..."
}
```

`primary_claim_id` MUST be one of `anchors.claim_ids` and MUST belong to the target page; the post-processor enforces this and falls back to the first claim_id if violated.

---

## 5. Verification — dataset link integrity

The Phase 1/2 evidence loop verified arXiv DOIs. Phase 3 adds an analogous loop for **dataset URLs**, using a known-registry whitelist instead of arXiv's DOI prefix.

### 5.1 Registry whitelist

```python
DATASET_REGISTRIES = {
    "ads":         {"host": "ui.adsabs.harvard.edu",     "check": "ads_bibcode"},
    "vizier":      {"host": "vizier.cds.unistra.fr",     "check": "vizier_catalog"},
    "vizier_cfa":  {"host": "vizier.cfa.harvard.edu",    "check": "vizier_catalog"},
    "ipac":        {"host": "irsa.ipac.caltech.edu",     "check": "ipac_table"},
    "ned":         {"host": "ned.ipac.caltech.edu",      "check": "ned_objref"},
    "mast":        {"host": "mast.stsci.edu",            "check": "mast_doi"},
    "esa_archive": {"host": "archives.esac.esa.int",     "check": "esa_obs"},
    "noirlab":     {"host": "datalab.noirlab.edu",       "check": "noirlab_release"},
    "alma":        {"host": "almascience.nrao.edu",      "check": "alma_project"},
    "alma_eso":    {"host": "almascience.eso.org",       "check": "alma_project"},
    "jvo":         {"host": "jvo.nao.ac.jp",             "check": "jvo_archive"},
    "esa_euclid":  {"host": "eas.esac.esa.int",          "check": "euclid_dr"},
    "lsst":        {"host": "data.lsst.cloud",           "check": "rubin_dp"},
    "zenodo":      {"host": "zenodo.org",                "check": "zenodo_doi"},
}
```

`registry` column on `survey_datasets` MUST be a key from this dict. If the dataset is hosted elsewhere (rare), set `registry='other'` and the verification step performs only a generic HEAD-200 check.

### 5.2 Verification job

```
File:  backend/app/agent_loop/research_ideas/dataset_verify.py
Cron:  every Sunday 03:00 KST (weekly)
       + on-demand POST /api/admin/datasets/verify
       + auto-fired post-idea-generation for any newly-cited dataset

Per dataset:
  1. If `registry='other'` → HTTP HEAD primary_url with 10s timeout.
  2. If `registry` in whitelist → registry-specific probe (e.g., for ADS:
     hit /abs/{bibcode}/abstract, check 200 + presence of bibcode in body).
  3. If `doi` is set, also resolve doi.org/{doi} and check 200.
  4. Update url_verified_at, url_verified_ok, url_verified_note.

Failure handling:
  - Single failure → mark TRANSIENTLY failed; retry 24h later.
  - 3 consecutive failures → status='deprecated' + Discord webhook to #general.
  - Ideas referencing a now-deprecated dataset stay visible but get a
    yellow "dataset unverified" badge.

Politeness:
  - Sequential, not parallel (≤ 1 req/sec per host).
  - Cache: skip if `url_verified_at` within 3 days AND `url_verified_ok=TRUE`.
  - User-Agent: "NebulaMind-Verifier/1.0 (papa@duhokim.org)".
```

### 5.3 Why not just blanket HTTP HEAD?

Many archives return 200 on a parking page when the actual resource is gone (NOIRLab in particular). Registry-specific probes catch this: the ADS probe requires the bibcode to appear in the response body; VizieR probe requires `Catalog: J/...` line in the HTTP response or the JSON-API response. The check function is per-registry and lives in `dataset_verify.py`.

### 5.4 What this is *not*

Phase 3 verification does **not**:
- Verify the dataset's *scientific content* (size, coverage, etc.). Those values are entered manually at registry time and reviewed in `admin_surveys.py`-style UI.
- Cache the actual data files. Only the citation link.
- Mint new DOIs for NebulaMind. NebulaMind links to existing DOIs only.

---

## 6. Trust mechanics — multi-axis voting

### 6.1 Three axes, three signals

The existing `research_idea_votes(value)` is a single integer (+1 save / -1 stale / 0 cleared). Phase 3 keeps that semantics for the `Save ★` button, but adds three orthogonal axes captured by the **Phase 3 jury** (LLM-driven) and surfaced for human override:

| Axis | Definition | Range | Source |
|---|---|---|---|
| `well_posed` | Is the question falsifiable, with a clear measurement and pass/fail condition? | 0..1 | Jury (Buddle 32B, see §10), human override |
| `feasibility` | Existing field; tractability given current datasets. | 0..1 | Existing Atom-7B scoring |
| `novelty` | Existing field; degree of advance over published work. | 0..1 | Existing Atom-7B scoring |

### 6.2 The well-posed jury (NEW)

A separate `app/agent_loop/research_ideas/well_posed_jury.py` job:
- Runs Buddle (`deepseek-r1:32b`) on each newly-inserted idea with `well_posed_score IS NULL`.
- Prompt focuses on **operationality**: can a graduate student write a 1-page proposal whose success criterion is unambiguous from the idea text alone? If yes → near 1.0; if "explore X" or "understand Y" → near 0.0.
- Output: `{well_posed: 0-1, rationale: <one sentence>}`.
- Update `well_posed_score`, `well_posed_updated_at`.

Why Buddle, not Rakon: well-posedness checking is a verification chain, not generation; Buddle's 32B reasoning is sufficient and far cheaper than Rakon. Also avoids stealing Rakon cycles from the generation pipeline.

### 6.3 Multi-axis vote storage (table extension)

```sql
ALTER TABLE research_idea_votes
  ADD COLUMN axis VARCHAR(20) NOT NULL DEFAULT 'overall';
  -- 'overall' | 'well_posed' | 'feasible' | 'novel'

-- Old uniq constraint loosened:
ALTER TABLE research_idea_votes
  DROP CONSTRAINT uq_research_idea_votes,
  ADD CONSTRAINT uq_research_idea_votes
    UNIQUE (idea_id, user_id, axis);
```

This way:
- Existing `Save ★` button writes `axis='overall', value=+1`.
- Phase 3 multi-axis voting writes per-axis values (Papa can mark an idea well-posed but not novel, etc.).
- Aggregation queries trivially group by axis.

### 6.4 Display rules (frontend)

Idea card shows three small bars:
```
well-posed ●●●●○   feasible ●●●○○   novel ●●●●●
```
Dots = round(score × 5). Human override is shown as a tiny `★` next to the axis dots when at least one human vote exists.

Filter sidebar adds three axis sliders ("min well-posed", etc.). Default thresholds: well_posed ≥ 0.5, feasibility ≥ 0.4, novelty ≥ 0.4.

---

## 7. API endpoints

All routes live in `backend/app/routers/research_ideas.py` (already present from Phase 1/2). Phase 3 additions are listed inline.

### 7.1 Reads

```
GET  /api/pages/{slug}/ideas
       Query: ?combo=JWST+DESI&min_well_posed=0.5&verified_only=true
       Returns: { count, ideas: [...] }, ideas with full anchor + dataset payload.
       (Papa's prompt naming. The existing /api/research/ideas/{slug} stays
        as an alias for back-compat — single router function, two paths.)

GET  /api/ideas/{idea_id}
       Returns one idea with anchors, datasets, votes-by-axis aggregate.

GET  /api/pages/{slug}/claims/{claim_id}/ideas
       Returns ideas where claim_id == claim_id OR anchor 'claim'/ref_id matches.
       Powers the per-claim inline chip.

GET  /api/datasets
       Query: ?survey_id=, ?data_type=, ?verified=true
       Returns dataset cards for the Explorer-style picker (§8.3).

GET  /api/datasets/{slug}
       Single dataset card incl. verification status, license, parent survey.

GET  /api/pages/{slug}/ideas/stats
       Returns: { count_by_combo, count_by_dataset, last_run_at, survival_rate }.
```

### 7.2 Writes — admin/Papa-only in v1

```
POST /api/ideas                                       (Papa only)
       Body: { page_id, claim_id, survey_combo, question, why_now,
               approach, datasets_primary: ["..."], datasets_support: [...] }
       Manual authoring path. Sets seeded=TRUE, model_chain='papa-manual'.
       The 15 galaxy-evolution seeds from research_ideas_tab_design_v1.md §5
       are migrated to this path (one-shot script during deploy).

POST /api/ideas/{slug}/regenerate                     (admin)
       Phase 1/2 endpoint, unchanged. Rate-limited 6h per slug.

PUT  /api/ideas/{idea_id}/vote                        (Papa only in v1.0)
       Body: { axis: 'well_posed'|'feasible'|'novel'|'overall', value: +1|0|-1, note? }
       Replaces POST /api/research/ideas/{id}/save (kept as 'overall' axis alias).

POST /api/ideas/{idea_id}/mark-stale                  (admin)
       Sets status='stale'. Existing.

POST /api/admin/datasets/verify                       (admin)
       Triggers immediate run of §5.2 verification job. Returns task_id.

POST /api/admin/datasets                              (admin)
       Body: dataset insert payload. For curating new datasets outside the
       seed list.
```

### 7.3 Response shape

Single idea response (returned by all list and detail routes):
```json
{
  "id": 87,
  "page_slug": "galaxy-evolution",
  "claim_id": 8421,
  "combo": "JWST+DESI",
  "question": "...",
  "why_now": "...",
  "approach": "...",
  "systematics": ["...", "..."],
  "scores": {
    "well_posed": 0.72,
    "feasibility": 0.55,
    "novelty": 0.85
  },
  "datasets": {
    "primary": [
      {"slug": "jwst-ceers", "name": "JWST CEERS", "verified": true},
      {"slug": "desi-dr1-elg", "name": "DESI DR1 ELG", "verified": true}
    ],
    "support": [
      {"slug": "hsc-ssp-pdr3", "name": "HSC SSP PDR3", "verified": true}
    ],
    "all_verified": true
  },
  "anchors": {
    "claims": [{"id": 8421, "text": "..."}, ...],
    "debates": [...],
    "arxiv": ["2026.12345", "2025.98765"]
  },
  "votes": {
    "overall": {"saved_by_papa": true, "user_count": 1},
    "well_posed": {"mean": 0.72, "n": 3},
    "feasibility": {"mean": 0.55, "n": 2},
    "novelty": {"mean": 0.85, "n": 2}
  },
  "model_chain": "rakon→astrosage-70b→atom-7b",
  "status": "active",
  "created_at": "2026-05-14T03:21:09",
  "updated_at": "..."
}
```

---

## 8. Frontend

### 8.1 Two surfacing points (page-level tab + per-claim chip)

Phase 1/2 introduced the page-level tab. Phase 3 adds a **per-claim inline chip** next to each claim that has at least one idea with `claim_id` pointing at it:

```
═══════════════════════════════════════════════════════
  Claim: "The sSFR-environment slope steepens at log(M*)~10
  in z<0.4 BGS galaxies, but disagreement persists at
  log(M*)>10.5."   [debate]   💡 2 research ideas
═══════════════════════════════════════════════════════
```

Clicking the `💡 2 research ideas` chip opens an inline drawer (no nav away). The drawer shows the 2 idea cards in the §7.3 layout. From there, "View all ideas" jumps to the full tab.

### 8.2 Tab layout (unchanged from Phase 1/2 + 3 additions)

- Per Phase 1/2: combo filter, sort, regenerate button, card layout.
- **NEW:** dataset filter (multi-select dataset chips below combo filter).
- **NEW:** three axis-threshold sliders (well-posed / feasibility / novelty).
- **NEW:** "Show only verified datasets" toggle (default ON).

### 8.3 Dataset picker (under "Authoring" admin UI, v1.0)

Papa-only admin form to author a new idea:
- Auto-complete from `GET /api/datasets?verified=true` for `datasets_primary` and `datasets_support` fields.
- Each picked dataset shows its parent survey + last verification state.
- Submits to `POST /api/ideas`.

### 8.4 Component files (target paths Tori will create / edit)

```
frontend/src/app/wiki/[slug]/
  ResearchIdeasTab.tsx            (already exists; add §8.2 controls)
  ClaimBlock.tsx                  (add §8.1 chip)
  IdeaCard.tsx                    (NEW; reused by tab + drawer)
  IdeaDrawer.tsx                  (NEW; inline drawer under a claim)
  IdeaAuthorForm.tsx              (NEW; §8.3, admin only)

frontend/src/app/datasets/
  DatasetPickerCombobox.tsx       (NEW; reused by author form + filters)
  DatasetBadge.tsx                (NEW; shows verified state)
```

---

## 9. Pilot plan — galaxy-evolution

### 9.1 Why galaxy-evolution first

- Already has the 15 seed ideas from Phase 1/2.
- 280-ish claims, 25%+ tagged `claim_type='debate'` — the most idea-dense page.
- Papa's own active research is here (DESI DR1 BGS); usefulness signal is immediate.
- `surveys` already richly mapped via existing M2M.

### 9.2 Pilot scope (v1.0 acceptance)

A pilot is successful when **all** of the following hold:

- [ ] All 15 existing seeds backfilled to new schema: have `claim_id` set to the most-relevant existing claim, `research_idea_datasets` populated with primary/support datasets from §3.2, `datasets_verified=TRUE`.
- [ ] At least one new AI-generated idea per existing seed combo (so the auto-pipeline has shown it can write to the new schema).
- [ ] Every claim with `claim_type='debate'` on galaxy-evolution shows the inline `💡 N research ideas` chip OR is explicitly marked as having no idea (Tori logs which claims have zero ideas; Papa reviews).
- [ ] Dataset verification cron has run once; ≥95% of `role='primary'` dataset links return `url_verified_ok=TRUE`.
- [ ] `well_posed_score` populated for all 15 seeds via the Buddle jury.
- [ ] Papa can submit a manual idea via `POST /api/ideas` and see it appear inline within 10 seconds.

### 9.3 Migration order (deploy day)

1. Tori runs alembic migration `research_ideas_phase3_v1`.
2. Tori runs the seed-backfill script (one-shot): converts each `research_idea_surveys` row to `research_idea_datasets` using §3.3 mapping; sets `claim_id` for the 15 hand-written seeds by string-match on the question text against `claims.text`; manual Tori review of any failures.
3. Kun runs the well-posed jury one-shot on the 15 seeds (Buddle on Mac Pro, <5 min).
4. Tori deploys the new frontend code.
5. HwaO flips a `research_ideas:phase3_enabled` Redis flag.
6. First nightly run of the verifier; Discord ping to #general with stats.
7. Papa opens the page, sanity checks. If acceptance ❌, rollback by un-flipping the flag (frontend falls back to Phase 1/2 tab; new tables remain inert).

### 9.4 What to watch in the first 48h

- `papa_save_rate` (existing metric, axis='overall') — target ≥3 of the 15 + new AI ideas saved.
- Per-axis vote distribution from Papa: are well-posed and novel votes correlated? If yes, the jury isn't adding information; tune the jury prompt.
- Dataset verification false-negative rate: does any flagship URL keep flapping?
- Inline drawer load time (per-claim chip click): must be <300ms or the chip is annoying.

---

## 10. Platoon Assignment

(Every periodic / real-time job must name its model — per workspace policy.)

### 10.1 Generation chain (unchanged from Phase 1/2, restated)

| Step | Model | Tier | Host | Why this model |
|---|---|---|---|---|
| (a) Reasoning skeleton | **Rakon** (deepseek-r1:671b) | Heavy reasoner | Mac Pro · exclusive | Multi-step reasoning over claims + debates + arxiv + dataset constraints. Bottleneck is *combination*, not domain idiom. |
| (b) Domain polish | **AstroSage-70B** | Astronomy drafter | Mac Studio | Domain-precise rewriting of why_now/approach; instrument-mode and dataset-coverage sanity. |
| (c) Novelty/feasibility scoring | **Atom-Astronomy-7B** | Astronomy classifier | Mac Studio · ~5GB | High-volume per-idea scoring; co-resident-friendly. |

### 10.2 New Phase 3 jobs

| Job | Model | Tier | Host | Why this model |
|---|---|---|---|---|
| **Well-posed jury** (§6.2) | **Buddle** (deepseek-r1:32b) | Medium reasoner | Mac Pro | Verification chain — needs CoT, not generation. Cheaper than Rakon, faster cold-load (~20s vs minutes). Runs when Rakon is idle. |
| **Dataset verifier** (§5.2) | (no LLM — Python `httpx` + per-registry probe code) | — | Mac Studio (Celery) | URL/DOI checks. Deterministic; no model needed. Lives in `dataset_verify.py`. |
| **Seed claim_id backfill** (§9.3 step 2) | **Atom-7B** | Astronomy classifier | Mac Studio | One-shot string-match + best-fit scoring for 15 seeds. Atom is fast + astronomy-aware; Mima would also work but Atom is preferred per platoon-roster astronomy rule. |
| **Inline-drawer load** (per click) | (no LLM — DB read) | — | Mac Studio (FastAPI) | Just a JOIN. |
| **Manual idea author** (§7.2 POST /api/ideas) | (no LLM — Papa writes) | — | — | Bypasses pipeline by design. |

### 10.3 Scheduling — interaction with existing crons

Rakon is the choke point. Phase 3 jobs that touch Mac Pro must coordinate:

| Cron | Schedule (KST) | Host load | Reason for slot |
|---|---|---|---|
| `regenerate_research_ideas_nightly` | 04:00 | Rakon + AstroSage + Atom | Phase 1/2 slot, low-traffic hour. |
| `well_posed_jury_nightly` | 06:00 | Buddle (Mac Pro) | After Rakon batch is done; Rakon evicted by then. |
| `dataset_verifier_weekly` | Sun 03:00 | Mac Studio only | No Mac Pro load. |
| `dataset_verifier_post_insert` | trigger | Mac Studio | Fires post-idea-insert if a referenced dataset has not been verified in 7 days. |
| `deep_synthesis` (existing) | 10:00 | Rakon exclusive | Existing slot. |

Hard rule (existing from Phase 1/2): never run `regenerate_research_ideas_nightly` concurrent with `deep_synthesis`. Phase 3 adds: never run `well_posed_jury` concurrent with Rakon (Buddle gets evicted on Mac Pro when Rakon is resident).

### 10.4 Fallback chain

| Primary | Fallback 1 | Fallback 2 | Last resort |
|---|---|---|---|
| Rakon | Buddle (deepseek-r1:32b) | AstroSage-70B doing skeleton + polish | Skip; log `infra_unavailable` |
| AstroSage-70B | Blanc (llama3.3:70b) | Tera (gemma3:27b) | Skip polish, ship raw |
| Atom-7B | Mima (qwen3:30b) | Heuristic from idea-text length + anchor count |
| Buddle (well-posed jury) | Nutty (deepseek-r1:14b on Mac Studio) | Atom-7B heuristic (looser) | Default 0.5, mark `well_posed_updated_at=NULL` for manual review |

### 10.5 Cost & capacity audit

All v1.0 work is free/local. No Claude budget consumed in production (Kun/Tori burn budget only during design + integration). Per nightly run:
- Rakon dwell on Mac Pro: ~3-5 min (one page in v1 pilot).
- AstroSage-70B + Atom-7B on Mac Studio: ~2-3 min in parallel.
- Buddle well-posed pass: ~2 min for ~20 ideas.
- Dataset verifier (incremental): ~30 sec for new datasets only.

Total wall-time per nightly batch on `galaxy-evolution`: under 10 minutes. Cross-host parallelism is the lever for scaling to 10 pages in v1.1.

---

## 11. Phasing & deliverables

### 11.1 v1.0 — pilot (target: this week)

- Migration `research_ideas_phase3_v1`
- Backend: dataset model + router; idea router updates (claim_id, datasets, multi-axis votes)
- Backend: `dataset_verify.py`; `well_posed_jury.py`
- Frontend: per-claim chip, idea drawer, multi-axis vote bars, dataset picker
- Pilot: galaxy-evolution acceptance per §9.2

### 11.2 v1.1 — expand & polish (target: +2 weeks)

- Roll to 10 flagship pages
- Multi-axis voting open to logged-in non-admin users (`well_posed`, `feasibility`, `novelty`)
- Cross-page idea linking
- `papa_save_rate` dashboard

### 11.3 v1.2 — back-compat cleanup

- Drop `research_idea_surveys` (table + writes)
- Frontend fully switched to dataset M2M

### 11.4 v2.0 — public

- Public idea submission (adversarial-probe gate)
- Auto-stale on age
- Literature back-search for published-out-of-existence detection

---

## 12. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Rakon names a dataset slug that's not in the registry (hallucinated) | Medium | Medium | Post-processor drops unknown slugs; if all primaries hallucinated, idea is rejected with reason `dataset_unknown` and logged for prompt tuning. |
| Dataset URL goes 404 silently (parking page) | High | Medium | Registry-specific probes (§5.3) instead of blanket HEAD; deprecation cascade after 3 fails. |
| `claim_id` heuristic on seed backfill picks the wrong claim | Medium | Low (cosmetic) | Tori reviews all 15 manually post-script; Papa can fix any via `PUT /api/ideas/{id}` (v1.1). |
| Well-posed jury scores everything ~0.7 (saturation, per memory) | Medium | High | Use Buddle (R1 family, reasoning-tuned), per-axis prompt with concrete pass/fail anchors; if saturation observed, swap to per-dimension float rubric with conjunctive gate (per `feedback_judge_saturation_design.md`). |
| Inline drawer load >300ms on a heavy claim | Low | Low | DB query is a single JOIN with explicit indexes (§2.1, §2.3); FE preloads top-3 ideas with the claim payload to elide a roundtrip. |
| Dataset verifier hits a registry rate limit | Medium | Low | Sequential calls, 1 req/sec/host, weekly cadence, 3-day cache. ADS specifically has a known polite-usage doc — follow it. |
| Old `research_idea_surveys` rows desync from new `research_idea_datasets` during v1.2 transition | Medium | Low | Migration step 5 backfills atomically; deprecation read-only enforced before drop. |
| Multi-axis voting fragments Papa's signal — he only ever clicks `Save ★` | Medium | Medium | Default Save ★ button writes axis='overall'; multi-axis is opt-in. Track click-through, drop the axis UI in v1.2 if unused. |
| Papa-only `POST /api/ideas` becomes a junk drawer (Papa types fast, never curates) | Low | Low | seeded=TRUE flag visible in admin filter; quarterly review pass by Kun. |

---

## 13. Open questions for Papa (sign-off)

1. **`survey_datasets` vs the existing `surveys` table.** Phase 3 introduces datasets as a finer unit than surveys (DR1 BGS != DESI). Are you OK with this split, or do you prefer to overload the existing `surveys` table with a parent-child column?
   **Kun recommends:** split. Surveys and their releases are scientifically distinct citation units; conflating them muddles the data-type axis (DESI is a survey of multiple types; DR1 BGS is a specific spectroscopic catalog).

2. **`claim_id` primary anchor vs anchor table only.** Should the inline chip require a single canonical claim per idea, or can it show ideas with multiple claim anchors of equal weight?
   **Kun recommends:** require one primary `claim_id` for the inline affordance; multi-claim ideas still show in the tab via the anchors table. Two surfaces, two precisions.

3. **Phase 3 jury model — Buddle vs Rakon.** Well-posedness checking is a verification task. Buddle (32B, on Mac Pro) is cheaper and avoids Rakon contention. Rakon (671B) is technically stronger.
   **Kun recommends:** Buddle. The marginal accuracy lift from Rakon on a yes-no-ish verification task does not justify the schedule conflict with generation.

4. **Verification frequency.** Sunday weekly + on-demand vs. nightly.
   **Kun recommends:** weekly. Dataset URLs change on data-release cadence (years), not days. Nightly burns the cache without finding anything.

5. **Multi-axis voting visibility in v1.0.** Show three bars on each card or hide behind a "details" expand?
   **Kun recommends:** show all three. The point of Phase 3 is to make the *kind* of confidence explicit; collapsing it defeats the purpose.

6. **Manual idea authoring (`POST /api/ideas`) in v1.0.** Papa-only via admin form, or also expose to no-one? (The endpoint exists for migrating the 15 seeds either way; question is whether Papa needs a UI.)
   **Kun recommends:** ship the admin form. Papa is the primary content gardener in v1; cutting his authoring path means he edits SQL when he has a new idea.

7. **Existing `research_idea_surveys` table — drop in v1.0 or keep through v1.2?**
   **Kun recommends:** keep through v1.2 (per §2.4). Cost is negligible; safety against tab-UI regressions is real.

---

## 14. Acceptance criteria (for Tori sign-off)

A v1.0 ships when **all** are true:

- [ ] Migration `research_ideas_phase3_v1` applied without error on Mac Studio Postgres.
- [ ] `survey_datasets` seeded with ≥40 entries; all `url_verified_ok=TRUE` on first run.
- [ ] `research_ideas.claim_id` populated for all 15 galaxy-evolution seeds.
- [ ] `research_idea_datasets` populated for all 15 seeds with at least 2 `role='primary'` rows each.
- [ ] `GET /api/pages/galaxy-evolution/ideas` returns full Phase 3 payload (§7.3) for all 15 seeds + any new AI-generated ideas.
- [ ] Per-claim chip renders on `galaxy-evolution`, opens drawer in <300ms.
- [ ] `well_posed_score` populated for all 15 seeds (Buddle jury one-shot).
- [ ] `POST /api/ideas` accepts and persists a manual idea; round-trip <2s.
- [ ] `PUT /api/ideas/{id}/vote` writes to `research_idea_votes(axis='well_posed')`.
- [ ] Dataset verifier ran once; Discord webhook posted to #general with success count.
- [ ] Rollback path verified: flipping `research_ideas:phase3_enabled=0` reverts UI to Phase 1/2 tab; new tables remain inert.

---

## 15. Notes / out of scope

- **No new model weights.** All four models (Rakon, AstroSage-70B, Atom-7B, Buddle) are already platoon-resident.
- **No external API writes.** The verifier reads from registries; no submissions.
- **License:** generated text inherits the wiki's AGPL-3.0. Dataset descriptions are factual and not licensed.
- **PII:** none. `research_idea_votes.user_id` ties to existing `subscribers.id`.
- **Mac Studio Postgres** is the only DB. Verifier writes from Celery; idea writes from FastAPI. Reads from FastAPI.
- This doc is the implementation contract for Tori's Phase 3 v1.0. Divergences must be flagged back to Kun for design update.

---

*— Kun 🔬  ·  Mac Pro  ·  2026-05-14 (KST)*


---

## 16. Integrated autowiki improvement loop — galaxy-evolution (post-Phase 3 addendum)

**Status:** Design v1.6 addendum · added 2026-05-14 by Kun
**Trigger:** Papa directive after Phase 3 (`process_lightweight_event`) went live
**Scope:** redesign the **15-min `autowiki_tick`** for `page_id=57` (galaxy-evolution) so Research Ideas are a **first-class step in the loop**, not just a post-commit side effect.

### 16.1 Why this addendum exists

§9 framed Research Ideas as a separate Phase 3 surface (tab + per-claim chip). §10 listed independent nightly/weekly cadences. The post-commit hook in `autowiki/tasks.py` (last 30 lines of `_run_tick`) bolted J1 onto the tick after-the-fact.

That worked as an MVP but left two structural problems:

1. **The loop is one-way.** Autowiki commits → ideas regenerate. Nothing in the autowiki tick reads back from ideas. So a Papa-saved idea anchored to a thin-evidence claim does *not* nudge the next tick toward that claim. The signal dies.
2. **Live bug — J1 never fires for claim inserts.** `tasks.py:549` reads `if proposal_type == "claim_insert"`, but the actual values written by Step 4 are `"claim_insert_subtopic"` and `"claim_insert_debate"`. **The highest-signal event (a brand-new claim) silently bypasses Nutty.** Only `evidence_link` and `section_rewrite` reach J1 today. This must be fixed before any other §16 work; design assumes it is fixed.

This addendum **promotes Research Ideas to a feedback signal that shapes the next proposal**, closes the loop, and re-specifies the 15-min cadence with that closure in mind.

### 16.2 The closed loop (visual)

```
                ┌──────────────────────────────────────────────────┐
                │  15-min autowiki_tick (galaxy-evolution)        │
                │                                                 │
       (Step 3) │  U0 judge (deepseek-r1:14b)                     │
                │      │                                          │
        NEW ──▶ │  Step 3.5: IDEA SIGNALS (SQL, <50ms)            │
                │   • per-claim boost from open ideas             │
                │   • surface free-floating high-value ideas      │
                │      │                                          │
       (Step 4) │  Pick proposal_type (now idea-aware)            │
                │      │                                          │
       (Step 5) │  Proposer (AstroSage-70B) — biased by signals   │
                │      │                                          │
       (Step 9) │  Judge U1 → Δq                                  │
                │      │                                          │
      (Step 10) │  COMMIT iff Δq ≥ 0.02                           │
                │      │                                          │
       Post-cmt │  process_lightweight_event (FIXED dispatch) ──┐ │
                └────────────────────────────────────────────────│─┘
                                                                 │
                                                                 ▼
                                                  ┌──────────────────────────┐
                                                  │  J1 Nutty (≤8/hr/page)   │
                                                  │   • refresh anchored     │
                                                  │   • generate ≤3 drafts   │
                                                  │   • Atom-7B score        │
                                                  │   • persist as draft     │
                                                  └────────────┬─────────────┘
                                                               │
                                                               ▼
                                              ┌────────────────────────────────┐
                                              │ Nightly 06:00 Buddle           │
                                              │  well_posed jury on new drafts │
                                              │  → writes well_posed_score     │
                                              └────────────┬───────────────────┘
                                                           │
                                                           ▼
                                            ┌──────────────────────────────┐
                                            │  Papa saves idea (any time)  │
                                            │  → research_idea_votes flip  │
                                            │     axis='overall'           │
                                            └──────────────┬───────────────┘
                                                           │
                                                           ▼
                                            Closure: Step 3.5 of NEXT tick
                                            picks these up as boost signals.
```

The loop closes at Step 3.5: every tick now reads the idea state Papa + jury produced since the last tick.

### 16.3 New Step 3.5 — Idea Signals (between current Step 3 and Step 4)

**Owner:** no LLM. Pure SQL JOIN over `research_ideas` ↔ `research_idea_anchors` ↔ `research_idea_votes(axis='overall' OR axis='well_posed')`. Expected p95 < 50 ms (indices already exist on `research_idea_anchors(ref_id)` and `research_ideas(page_id, status)`).

**Computes two outputs:**

#### (a) Per-claim priority boost (`claim_boost: dict[int, float]`)

For every claim on the page, sum boost contributions from ideas anchored to it (`research_idea_anchors.kind='claim'`):

| Signal | Boost | Why |
|---|---:|---|
| Idea has `saved_by_papa=TRUE` | **+0.5** | Strongest possible signal — Papa explicitly flagged value. |
| Idea has `well_posed_score ≥ 0.7` (Buddle jury) | **+0.3** | Independent verification that the question is research-worthy. |
| Idea `status='active'` (promoted by J3) | **+0.2** | Rakon batched promotion = "we believe in this". |
| Each additional anchored idea, capped 3 | **+0.1** | Volume of attention is a weak signal but real. |

Total boost capped at **+1.0** per claim. A claim with no anchored ideas → boost = 0.

#### (b) Free-floating high-value ideas (`orphan_high_value: list[idea_id]`)

Ideas where `saved_by_papa=TRUE OR well_posed_score ≥ 0.7` **AND** no `research_idea_anchors` row of `kind='claim'`. These signal "the page is missing the claim this idea is about" — a high-precision push toward `claim_insert_debate`.

In v1.0 this list is logged only and surfaced to Papa in Discord. In v1.1 it becomes a hard input to Step 4 (see §16.4 (c)).

### 16.4 Step 4 modification — idea-aware proposal_type selection

Current Step 4 picks proposal_type from structural deficits:

```
if depth < 0.7 and missing_subtopics:   claim_insert_subtopic
elif debate_count < 4:                  claim_insert_debate
elif freshness < 0.6:                   evidence_link
elif hero_richness < 0.9:               hero_upgrade
else:                                   section_rewrite
```

**Revised order with idea signals (v1.0 — conservative):**

1. **Structural deficits keep top priority.** If `depth < 0.7 and missing_subtopics` (page is genuinely incomplete) or `debate_count < 4` (debate-impoverished), **ignore ideas** and proceed as today. Rationale: a thin page benefits more from structural fill than from idea-driven evidence chasing.

2. **Idea-driven `claim_insert_debate` boost** (only when structural deficits are clean). If `orphan_high_value` is non-empty AND `debate_count < 7`: pick `claim_insert_debate`, with the orphan idea's `question` text passed into the proposer as a topic hint. (Implementation: extend `propose_claim_insert(..., topic_hint=...)`; AstroSage-70B is already domain-grade, no model change.)

3. **Idea-driven `evidence_link` re-ranking** (this is the main change, runs whenever `evidence_link` is the selected type). Today's evidence_link sorts claims by `evidence_count ASC` and picks the first. New rule:
   ```
   ranking_score(claim_i) = evidence_count[i] - 2.0 * claim_boost[i]
   ```
   Sort ASC; lowest score gets the new evidence. A high-boost claim (boost = 1.0) effectively gets evidence even with **2 more evidence than its neighbors**. This is the load-bearing change: it converts "Papa saved an idea here" into "next tick adds evidence to that claim's anchor."

4. **`hero_upgrade` and `section_rewrite`** unchanged. Hero facts are content artifacts not idea-relevant; section_rewrite is governed by round-robin and structural quality, not idea attention.

**v1.1 (after Buddle nightly has proven stable):** the `orphan_high_value` list becomes a *hard* override at the top of Step 4 — orphan ideas trigger `claim_insert_debate` even when other structural deficits exist. Held back from v1.0 because we want one full week of jury data first.

### 16.5 Post-commit dispatch — P0 fix + restated trigger map

**P0 bug fix (must land before §16 rollout):** `app/agent_loop/autowiki/tasks.py:549` — replace
```python
if proposal_type == "claim_insert" and claim_ids_inserted:
```
with
```python
if proposal_type in ("claim_insert_subtopic", "claim_insert_debate") and claim_ids_inserted:
```

**Restated trigger map (post-fix):**

| Committed proposal_type | Fires J1? | Trigger string passed to `process_lightweight_event` | Cause id |
|---|:--:|---|---|
| `claim_insert_subtopic` | ✅ (after fix) | `claim_inserted` | new claim_id |
| `claim_insert_debate` | ✅ (after fix) | `claim_inserted` | new claim_id |
| `evidence_link` | ✅ today | `evidence_linked` | new evidence_id |
| `section_rewrite` | ✅ today | `section_rewritten` | `None` |
| `hero_upgrade` | ❌ intentionally | — | hero facts are not idea-relevant |

**Why not also fire J1 on `hero_upgrade`:** hero facts (5-bullet page summary) don't anchor to specific claims or debates. Firing J1 would burn the 8/hr Nutty budget without informational gain. Confirmed against Phase 3 §6 (well-posed jury operates on claim+arxiv anchors, not hero text).

### 16.6 Cadence — unchanged in number, sharper in role

| Cadence | Job | What it does in the new loop |
|---|---|---|
| **15 min** | `autowiki_tick` (galaxy-evolution only in v1) | Closes loop: Step 3.5 reads ideas → Step 4 picks idea-aware → commit → J1 enqueues |
| **Per-commit, ≤8/hr/page, 1h debounce** | `process_lightweight_event` (J1) | Refresh anchored drafts + generate up to 3 new drafts via Nutty (deepseek-r1:14b on Mac Studio) |
| **Nightly 06:00 KST** | `well_posed_jury_nightly` (Buddle) | Scores new drafts → `well_posed_score` becomes Step 3.5 boost input next morning |
| **Weekly Sun 03:00 KST** | `rakon_weekly_promotion_pass` (J3) | Promotes draft → active status → bigger Step 3.5 boost |

**Critical:** Keep the 15-min cadence. Step 3.5 is sub-50ms; Step 4 change is zero-cost; the loop is closed by **frequency**, not by adding more passes. Tightening to <15 min isn't useful (Papa's save events don't arrive faster than nightly anyway).

### 16.7 Platoon Assignment (per workspace policy — every step names its model)

| Step | Job | Model | Tier | Host | Why this model |
|---|---|---|---|---|---|
| §16.3 (Step 3.5) | Idea signals SQL | **no LLM** | — | Mac Studio (Celery in `autowiki` queue) | Pure DB read; sub-50ms; deterministic. An LLM here would be waste. |
| §16.4 Step 4 selection | Idea-aware proposal_type pick | **no LLM** | — | Mac Studio | Rule-based on Step 3.5 outputs + existing component scores. |
| §16.4 Step 5 (when topic_hint passed) | Proposer with idea-derived hint | **AstroSage-70B** | Astronomy drafter | Mac Studio | Unchanged from §10.1; passing one extra string in the prompt doesn't change the model choice. |
| §16.5 J1 fan-out | `process_lightweight_event` | **Nutty (deepseek-r1:14b)** generate + refresh; **Atom-7B** score | 14B reasoner + 7B classifier | Mac Studio | Per `platoon-roster.md`: Nutty = fast reasoning with CoT, cheap (~7-8 GB resident), ≤8/hr rate-limit fits comfortably. Atom-7B for scoring per existing §10. |
| §16.6 Nightly jury | `well_posed_jury_nightly` | **Buddle (deepseek-r1:32b)** via Mac Pro proxy `192.188.0.4:11435` | Medium reasoner | Mac Pro | Unchanged from §10.2. Verification chain needs CoT but not 671B; cold-load ~20s acceptable for nightly. Runs after Rakon idle (06:00 slot). |
| §16.6 Weekly promotion | `rakon_weekly_promotion_pass` (J3) | **Rakon (deepseek-r1:671b)** primary; Buddle fallback | Heavy reasoner | Mac Pro · exclusive | Unchanged from §10. Sunday 03:00 KST, low-contention slot. |

**No new model weights.** All assignments reuse the platoon already on Mac Studio + Mac Pro. Mac Pro reachability via proxy at `192.188.0.4:11435` is the only new piece of infra, and it's already live as of 2026-05-14.

### 16.8 New table fields / migration impact

Nothing structural. All inputs to Step 3.5 already exist:
- `research_ideas.saved_by_papa` (Phase 1)
- `research_ideas.well_posed_score` (Phase 3 §2.3 — already added)
- `research_ideas.status` (Phase 1)
- `research_idea_anchors(kind='claim', ref_id)` (Phase 1)

**One small addition** — a denormalized cache for telemetry, optional in v1.0:
```sql
ALTER TABLE autowiki_runs
  ADD COLUMN idea_signals_json JSONB;
-- {"claim_boosts": {claim_id: float, ...}, "orphan_count": int, "topic_hint": str|null}
```
Lets us look back and ask "did Step 3.5 actually move the needle?" without re-deriving from scratch. Cheap and revertable.

### 16.9 Acceptance criteria (v1.0 — galaxy-evolution pilot of §16)

- [ ] P0 bug fix landed: `claim_insert_subtopic` and `claim_insert_debate` both fire J1 after commit. Verifiable by inserting a claim and observing `research_ideas_lightweight` row in `autowiki_runs`.
- [ ] Step 3.5 implemented and writing `idea_signals_json` to `autowiki_runs` (telemetry on, even if §16.4 logic dark-launched).
- [ ] Step 4 honors `claim_boost` in `evidence_link` ranking. Verifiable by saving a Papa idea anchored to claim X (currently ≥3 evidence) and seeing the next tick pick X for `evidence_link` despite a leaner-evidence neighbor existing.
- [ ] `orphan_high_value` list surfaces in `autowiki_runs.idea_signals_json` and is Discord-pinged when non-empty (frequency: at most once per 24h).
- [ ] One full week of 15-min ticks runs with the new logic without latency regression (p95 tick < 180s, was ~120s pre-change).
- [ ] At least one observable closed-loop instance: Papa saves idea → within next 3 ticks the anchored claim gets new evidence via `evidence_link`. Logged to Discord.

### 16.10 Risk register (additions to §12)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Step 3.5 boost over-concentrates evidence on one claim (the "Papa-saved-it" claim hoovers all evidence_link ticks) | Medium | Medium | Cap per-claim boost at 1.0 (specified above); also subtract `0.1 × already_committed_evidence_via_boost_in_last_24h` from boost (de-saturation). v1.1 only — held back from v1.0 to keep behavior simple. |
| P0 bug fix lands but Nutty hits 8/hr ceiling because all 5 proposal types now fire J1 | Low | Low | Today's tick produces ≤4 commits/hr (15-min cadence × ~60% commit rate). Even 100% commit → 4 J1/hr < 8 ceiling. Per-page debounce (1h) adds headroom. Monitor `J1 rate_limited` log line; raise ceiling to 12 if seen. |
| `orphan_high_value` is empty for weeks (no signal) | Medium | Low | Telemetry-only in v1.0; no behavior depends on it. Confirms the "Papa rarely saves ideas without claim anchors" hypothesis or refutes it. |
| Step 3.5 SQL slowdown if `research_idea_anchors` grows past ~10k rows on one page | Low (galaxy-evolution today has 15 ideas) | Low | Index already exists on `(page_id, status)`; query plan vetted at <50ms for 1k-row scenarios in v1.1 expansion. |
| §16.4 rule-2 (orphan → `claim_insert_debate`) pushes a duplicate of an existing claim | Low | Medium | The proposer's existing Atom-7B alignment gate (Step 6) catches duplicates by semantic similarity. No change needed; Step 6 already gates this case. |

### 16.11 What's NOT in §16 (deferred to §16-v1.1+)

- Multi-page integrated loop (other 9 flagship pages get §16 treatment in v1.1, gated by galaxy-evolution data).
- Hard override of structural deficits by orphan_high_value (v1.1, post-data).
- Boost de-saturation per §16.10 risk row 1 (v1.1).
- Idea status auto-flip from `draft → ready` when its anchor claim gains 2+ evidence in one week (v1.2 — feedback in the other direction).

### 16.12 Tori work breakdown

| Item | File | Est |
|---|---|---|
| P0: post-commit dispatch fix | `app/agent_loop/autowiki/tasks.py:549` | 5 min + test |
| Step 3.5 SQL function | new: `app/agent_loop/autowiki/idea_signals.py` | 1 h |
| Step 4 integration | `app/agent_loop/autowiki/tasks.py` (around line 257) | 1 h |
| `propose_claim_insert(topic_hint=...)` extension | `app/agent_loop/autowiki/proposers.py` | 30 min |
| `evidence_link` ranking change | `app/agent_loop/autowiki/tasks.py` (sorted_claims block, line 305) | 30 min |
| `autowiki_runs.idea_signals_json` migration | new alembic | 20 min |
| Discord ping for `orphan_high_value` (24h cooldown via Redis) | reuse `_discord()` helper from `auto_improvement.py` | 20 min |
| Test: closed-loop integration (save idea → 3 ticks → evidence on anchor) | `tests/integration/test_autowiki_idea_loop.py` | 1.5 h |
| **Total** | | **~5h** |

— Kun 🔬 · §16 addendum · 2026-05-14 KST
