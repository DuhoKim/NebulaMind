# Facility Registry Unification — Design v1

**Author:** Kun 🔬
**Date:** 2026-06-13 00:47 KST
**Status:** Design only — Papa approved D4; awaiting Tori implementation dispatch
**Live grounding:** Read against `docs/Audit_NonWikiTabs_v1.md` §3/§8, `backend/app/models/facility.py`, `backend/app/models/survey.py`, `backend/app/routers/news.py`, `backend/app/routers/calendar.py`, `backend/app/routers/surveys.py`, and live PostgreSQL (`nebulamind-postgres-1`, DB `nebulamind`, user `nebula`) on 2026-06-13 KST. Live counts: `surveys` = 50, `facility_profiles` = 6, `facility_news_items` = 307. The six facility profiles carry 149 facility-linked items: DESI 32, Euclid 35, Rubin/LSST 58, VLA 17, JWST 5, ALMA 2.

---

## 1. Problem

NebulaMind currently has two facility-like registries:

- `surveys` is the researcher-facing observational-data catalog: 50 rows, rich survey metadata, release timelines, catalog fields, logos, research-idea links, and survey detail pages.
- `facility_profiles` is the news/calendar roster: 6 rows, each with `facility_news_items` used by `/news`, `/calendar`, `/newsletter`, and social/news curation.

They overlap in the real world but not in the schema. Five profile slugs match a survey slug exactly (`alma`, `desi`, `euclid`, `jwst`, `vla`); Rubin is split as `facility_profiles.slug='lsst-rubin'` vs `surveys.slug='rubin-lsst'`. Because there is no relationship between the tables, `/surveys/[slug]` cannot show facility news/events even when the facility has active data.

The immediate D4 goal is narrow: enable a "News & Events" strip on survey detail pages without destabilizing either registry.

---

## 2. Current State

### 2.1 `surveys`

Owner: Surveys tab and survey detail pages.

Key fields already live: `slug`, `name`, `full_name`, `description`, `wavelength_band`, `status`, `archive_url`, `mission_url`, `logo_url`, `logo_bg`, numeric plot fields, `survey_data_releases`, `survey_datasets`, `survey_catalog_fields`.

The table is broad, researcher-oriented, and intentionally includes survey products as well as facilities. Examples: `DESI`, `SDSS`, `COSMOS2020`, `CDF-N`, `WISE`, `XMM-Newton`, `Rubin/LSST`.

### 2.2 `facility_profiles`

Owner: News/Calendar/Newsletter curation.

Schema columns: `slug`, `full_name`, `short_name`, `operator`, `operator_country`, `facility_kind`, `operating_status`, `data_portals`, `documentation_url`, `proposal_portal_url`, `homepage_url`, `first_light_date`, `decommission_date`, `last_verified_at`, `created_at`.

Live rows:

| facility slug | short name | matching survey | news count | future/current count |
|---|---:|---|---:|---:|
| `alma` | ALMA | `alma` | 2 | 1 |
| `desi` | DESI | `desi` | 32 | 2 |
| `euclid` | Euclid | `euclid` | 35 | 1 |
| `jwst` | JWST | `jwst` | 5 | 1 |
| `lsst-rubin` | Rubin/LSST | `rubin-lsst` | 58 | 1 |
| `vla` | VLA | `vla` | 17 | 0 |

### 2.3 `facility_news_items`

Owner: `/api/news`, `/api/calendar`, newsletter, news/social curation.

Every facility-specific item points to `facility_profiles.id`. News APIs currently filter by `facility_profiles.slug`, not by survey slug. The curation loops build `fac_map = {f.slug: f.id}` from `facility_profiles`, so `facility_profiles` is also the RSS/news ingestion roster.

This matters: deleting or merging `facility_profiles` into `surveys` would touch ingestion, calendar, newsletter, social drafts, and existing APIs. The D4 benefit does not justify that blast radius.

---

## 3. Design Decision

**Use an explicit link table, not a full merge and not a single nullable FK.**

Create `survey_facility_links`:

```sql
CREATE TABLE survey_facility_links (
    id                  SERIAL PRIMARY KEY,
    survey_id            INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    facility_profile_id  INT NOT NULL REFERENCES facility_profiles(id) ON DELETE CASCADE,
    relation_type        VARCHAR(40) NOT NULL DEFAULT 'same_facility',
    is_primary           BOOLEAN NOT NULL DEFAULT true,
    confidence           NUMERIC(3,2) NOT NULL DEFAULT 1.00,
    source               VARCHAR(80) NOT NULL DEFAULT 'manual_seed_20260613',
    notes                TEXT,
    created_at           TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE (survey_id, facility_profile_id, relation_type)
);

CREATE INDEX ix_sfl_survey ON survey_facility_links(survey_id);
CREATE INDEX ix_sfl_facility ON survey_facility_links(facility_profile_id);
```

Initial `relation_type` values:

- `same_facility`: the survey row and facility profile name the same operational facility or mission (`desi`, `euclid`, `rubin-lsst` ↔ `lsst-rubin`).
- `observed_by`: future use for survey products or fields that are not the facility itself (e.g. a Chandra field if a Chandra profile is added later).
- `operator_facility`: future use when the best news anchor is an operator/facility page rather than the survey itself.

Why link table:

- It solves today’s need with six seed rows.
- It handles the real shape of astronomy data: one facility can back many surveys, and one survey/product can be associated with multiple facilities.
- It avoids making `surveys` depend on the small, curated news roster.
- It avoids forcing `facility_profiles` to grow from 6 to 50 before the product needs it.
- It keeps news/calendar ingestion stable because those systems can continue owning `facility_profiles`.

Rejected alternatives:

- **Full merge into `surveys`:** too much blast radius. News/calendar curation loops and APIs expect a small facility roster; `surveys` contains catalog products and historical datasets that are not good RSS/news entities.
- **`surveys.facility_profile_id` nullable FK:** enough for the current six, but too rigid for future one-to-many/many-to-many cases (`CDF-N`/`CDF-S` observed by Chandra, SDSS and SDSS-V sharing a facility ecosystem, HST/JWST program products).
- **Name/slug matching view only:** Rubin already disproves exact matching, and fuzzy matching should not decide public links.

---

## 4. Initial Seed

Seed only manually verified, high-confidence links:

| survey slug | facility slug | relation | confidence | notes |
|---|---|---|---:|---|
| `alma` | `alma` | `same_facility` | 1.00 | Exact slug and mission URL match |
| `desi` | `desi` | `same_facility` | 1.00 | Exact slug; survey operator differs in wording only |
| `euclid` | `euclid` | `same_facility` | 1.00 | Exact slug; ESA mission |
| `jwst` | `jwst` | `same_facility` | 1.00 | Exact slug; mission URL variant NASA/ESA but same mission |
| `rubin-lsst` | `lsst-rubin` | `same_facility` | 1.00 | Same entity, slug-order mismatch only |
| `vla` | `vla` | `same_facility` | 1.00 | Exact slug; operator wording differs only |

Do **not** seed inferred links in v1. Examples: do not link `CDF-N`/`CDF-S` to Chandra until there is a `chandra` facility profile; do not link every HST/JWST dataset to a facility profile unless a real survey/product relationship is reviewed. This guard keeps the feature honest.

---

## 5. API Design

### 5.1 Add lightweight facility metadata to survey detail

Extend `GET /api/surveys/{slug}` with:

```json
"facility_profiles": [
  {
    "slug": "desi",
    "short_name": "DESI",
    "full_name": "Dark Energy Spectroscopic Instrument",
    "relation_type": "same_facility",
    "is_primary": true,
    "event_count": 32,
    "upcoming_count": 2
  }
]
```

This is small and lets the page decide whether to render the strip placeholder without making a second request.

### 5.2 New survey-scoped endpoint

Add:

`GET /api/surveys/{slug}/events?past_days=180&upcoming_days=730&limit=8`

Behavior:

- Resolve survey by slug.
- Join `survey_facility_links -> facility_profiles -> facility_news_items`.
- Return news/calendar items in the same shape as `/api/calendar/` cards already expect, plus `facility_slug`, `facility_name`, `facility_url`.
- Filter window: same default as current News audit context (`past_days=180`, `upcoming_days=730`), bounded like existing calendar/news endpoints.
- Order: future/upcoming soon first, then recent completed/release items. A practical SQL order:
  - `CASE WHEN fni.occurs_at >= NOW() THEN 0 ELSE 1 END`
  - `fni.featured DESC`
  - future rows `fni.occurs_at ASC`, past rows `fni.occurs_at DESC`
  - `fni.created_at DESC`
- If no link exists, return `{survey, count: 0, events: []}`.

Do not alter `/api/news` or `/api/calendar` in v1. They remain facility-centric.

### 5.3 Optional view for internal queries

If Tori wants simpler SQL, create a read-only DB view:

```sql
CREATE VIEW survey_facility_news_items AS
SELECT
  s.id AS survey_id,
  s.slug AS survey_slug,
  fp.id AS facility_profile_id,
  fp.slug AS facility_slug,
  sfl.relation_type,
  sfl.is_primary,
  fni.*
FROM survey_facility_links sfl
JOIN surveys s ON s.id = sfl.survey_id
JOIN facility_profiles fp ON fp.id = sfl.facility_profile_id
JOIN facility_news_items fni ON fni.facility_id = fp.id;
```

This is optional. I prefer keeping the join inline in the endpoint unless repeated queries emerge.

---

## 6. UI Spec

Add a **News & Events** section to `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`, after `Data Products & Catalogs` and before `Research Ideas`.

Rationale for placement: the detail page should read as:

1. What is this survey?
2. What data exists?
3. How is the data structured?
4. What is happening next or recently?
5. What ideas can I pursue?

### Component

Create `SurveyNewsEvents` inside the survey detail module first. Extract later only if reused.

Props:

```ts
type SurveyEvent = {
  id: number;
  slug: string;
  title: string;
  kind: string;
  track: string;
  summary: string | null;
  occurs_at: string | null;
  occurs_at_confidence: string | null;
  occurrence_status: string | null;
  source_url: string | null;
  data_portal_urls: string | null;
  featured: boolean | null;
  credibility_score: number | null;
  facility_slug: string | null;
  facility_name: string | null;
  facility_url: string | null;
};
```

Render:

- Section header: `News & Events`.
- Subcopy: `Latest data releases, proposal calls, and facility milestones linked to this survey.`
- Card strip: 3 cards on desktop, horizontal scroll on narrow screens.
- Each card: facility chip, kind chip, title, two-line summary, date/status, `Source ↗`.
- Link to `/calendar?facility=<facility_slug>` or `/news?facility=<facility_slug>` only after those pages actually support query-param hydration. For v1, use a simple footer link to `/calendar`.
- Empty state for unlinked surveys: do not render the whole section. Empty linked-but-no-events state is unlikely but should say `No tracked news or calendar events yet.`

Style: reuse existing survey detail card treatment (`#1e293b` panel, `#334155` border, primary `#f8fafc`, secondary `#94a3b8`). Do not introduce emoji badges; trust-level UI already established the direction away from decorative emoji badges.

---

## 7. Migration Steps

### Step 1 — Alembic migration

Create `facility_registry_links_v1.py`.

- Create `survey_facility_links` with idempotent table check.
- Seed the six links from §4 with SQL `INSERT ... SELECT ... ON CONFLICT DO NOTHING`.
- Do not modify or drop `facility_profiles`.
- Do not modify or drop `surveys`.

The migration is additive and reversible. Downgrade drops `survey_facility_links` only.

### Step 2 — ORM/model touch

Add `SurveyFacilityLink` to `backend/app/models/survey.py` or a new small model module. Because most current survey/news APIs use `text()` SQL, model wiring is not a blocker, but the table should be represented for future maintainability.

### Step 3 — API

In `backend/app/routers/surveys.py`:

- Add `_get_survey_facility_profiles(survey_id, db)`.
- Include `facility_profiles` in `get_survey()`.
- Add `GET /api/surveys/{slug}/events`.

Keep `/api/news` and `/api/calendar` unchanged.

### Step 4 — Frontend

In `SurveyDetailClient.tsx`:

- Add state/effect for `/api/surveys/${slug}/events`.
- Add `SurveyNewsEvents`.
- Render only when the survey has linked facility profiles or events.

### Step 5 — Verification

Manual API checks:

```bash
curl -s http://localhost:8000/api/surveys/desi | jq '.facility_profiles'
curl -s 'http://localhost:8000/api/surveys/desi/events?limit=3' | jq '.count, .events[].facility_slug'
curl -s 'http://localhost:8000/api/surveys/rubin-lsst/events?limit=3' | jq '.events[].facility_slug'
curl -s 'http://localhost:8000/api/surveys/sdss/events?limit=3' | jq '.count'
```

Expected:

- DESI returns `facility_profiles[0].slug == "desi"` and events.
- Rubin returns events with `facility_slug == "lsst-rubin"` despite the slug mismatch.
- SDSS returns count 0 and the frontend does not show an empty events strip.

---

## 8. Platoon Assignment

No model platoon required for v1.

- **Tori:** migration, seed links, API endpoint, frontend section, rebuild/restart verification.
- **Kun:** review the mapping and the rendered DESI/Rubin pages against this design; decide if any future links need a separate seed pass.
- **Deterministic Python/SQL only:** matching is manual and exact; no LLM should infer facility relationships.

Future expansion, if Papa wants broad facility coverage:

- Use deterministic candidate generation from slug/name/operator/url overlap.
- Kun reviews candidates manually.
- Only after review, seed additional `survey_facility_links`.

---

## 9. Acceptance Criteria

1. `survey_facility_links` exists and has exactly the six v1 seed rows listed in §4.
2. `GET /api/surveys/desi` includes one facility profile (`desi`) with `event_count >= 30`.
3. `GET /api/surveys/rubin-lsst/events?limit=5` returns events whose `facility_slug` is `lsst-rubin`.
4. `GET /api/surveys/sdss/events?limit=5` returns `count: 0` and no error.
5. `/surveys/desi` renders a News & Events strip with at least three event cards and working source links.
6. `/surveys/rubin-lsst` renders News & Events despite the slug mismatch.
7. `/surveys/sdss` does not render a misleading empty strip.
8. `/news`, `/calendar`, `/newsletter` still return the same facility items as before; no regression to existing facility-centric surfaces.

---

## 10. What Not To Build

- Do **not** merge `facility_profiles` into `surveys` in v1.
- Do **not** expand `facility_profiles` to all 50 surveys just to make the table counts match.
- Do **not** auto-link by fuzzy name matching.
- Do **not** create a broad observatory/instrument/facility ontology yet.
- Do **not** add News & Events strips to every survey by falling back to generic astronomy news; if there is no facility link, hide the section.
- Do **not** duplicate `facility_news_items` into survey-specific rows.
- Do **not** make the survey detail page depend on News/Calendar availability for its main content; this is an additive strip.

This v1 is intentionally small: six explicit links unlock cross-surface continuity for the facilities that already have curated news, while preserving the separate responsibilities of the survey catalog and the news/calendar roster.

— 🔬 Kun
