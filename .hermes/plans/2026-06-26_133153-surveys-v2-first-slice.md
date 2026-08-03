# Surveys Three-Lane Synthesis v2 — 20260626T133153Z

**Status:** design-only synthesis of the 3-agent Survey design sprint.  
**DB writes:** 0.  
**Implementation:** not started; this is a decision record and recommended first slice.  
**Repo:** `/Users/duhokim/NebulaMind/NebulaMind`.

## Executive recommendation

Do **not** create a parallel Surveys product. Evolve the existing `/surveys` stack into:

1. **Survey Atlas** — the public `/surveys` explorer/list workspace.
2. **Proposal Planner** — the existing `/surveys/[slug]` detail page polished for research feasibility.
3. **Freshness Cockpit** — a later read-only `/admin/surveys` operator surface for stale/missing/broken metadata.

The first implementation slice should be **P1 · Atlas IA polish**: frontend-only, no schema, no DB, no autowiki writes.

## Grounding

- Existing public routes: `/surveys`, `/surveys/[slug]`.
- Existing frontend components: `SurveysView`, `BandSpectrumStrip`, `ControlBar`, `FilterSheet`, `SurveyCard`, `SurveyPeek`, `ChartView`, `PlotA`, unused `PlotB`, `SurveyLogo`.
- Existing backend APIs: `/api/surveys`, `/api/surveys/{slug}`, `/events`, `/releases`, `/datasets`, `/ideas`, `/pages`, `/quality`.
- Existing admin APIs: `/api/admin/surveys/proposals`, approve/reject, autoapply log.
- Live read-only data: 50 surveys, 107 releases, 57 datasets, 644 catalog fields.
- Numeric coverage: {'wavelength_center_um': '50/50', 'z_max': '49/50', 'dr_year': '42/50', 'data_volume_tb': '48/50', 'limiting_magnitude': '30/50', 'num_sources_count': '39/50'}.

## Synthesis decisions

### D1. Keep top-level nav label as Surveys for now, but use page/surface copy “Astronomical Surveys & Facilities”.

Why: The data mixes surveys, facilities, observatories, experiments, and fields; rebranding the nav is unnecessary, but the page must be honest.

### D2. Make existing /surveys the canonical Survey Atlas, not a new route or second product.

Why: All three lanes found substantial existing implementation: route, components, APIs, releases, datasets, catalog fields, docs, and admin endpoints.

### D3. Rename modes to Explorer | List and treat Explorer/Atlas as the primary desktop mental model.

Why: The core job is comparing observational capability in wavelength/redshift/coverage space; List remains the fallback and mobile-friendly mode.

### D4. Defer PlotB; do not wire a second chart until PlotA is honest, accessible, and uncluttered.

Why: PlotB exists but is unused and risks reviving stale two-plot docs. First fix plotted/matching counts, missing-axis explanation, labels, and hover/focus.

### D5. Use /surveys/[slug] as the Proposal Planner detail page, not a new planner route.

Why: The detail page already has parameters, releases, datasets/catalogs, events, ideas, and wiki links; the work is hierarchy, CTAs, anchors, and checklist polish.

### D6. Treat /admin/surveys as a later Freshness Cockpit backed by existing admin_surveys.py endpoints.

Why: Admin proposal/autoapply APIs already exist; the safe next step is a read-only stale/missing/broken queue before any autowiki writes.

### D7. No schema/data mutation for the first slice.

Why: Backend lane found migration/schema drift risks: id/quality_score response mismatch, logo columns/model drift, status vocabulary drift, Alembic head risk.

## Recommended first implementation slice

### P1 · Atlas IA polish, zero DB/schema changes

Goal: Make the existing Surveys landing immediately understandable, honest about missing plot data, and navigable from atlas to profile.

Scope:
- `frontend/src/app/surveys/page.tsx`
  - Copy: “Astronomical Surveys & Facilities”.
  - Subtitle: “50 observational programs, facilities, and survey data products.”
  - Add lightweight stats row if data already loaded.
- `frontend/src/components/surveys/ControlBar.tsx`
  - Rename Directory → List.
  - Rename Chart → Explorer or Atlas; recommended visible label: Explorer.
  - Keep URL compatibility for ?view=directory|list|chart|explorer.
- `frontend/src/components/surveys/ChartView.tsx`
  - Header should say M plotted · N matching filters when some rows cannot plot on selected axes.
  - Add chart-purpose microcopy: “Map surveys by physical reach; missing-data rows remain listed below/inside chip.”
  - Reserve space for right info panel in later slice, but do not build compare yet.
- `frontend/src/components/surveys/PlotA.tsx`
  - Persistent point labels only when plotted count ≤15; otherwise hover/focus labels only.
  - Keep/strengthen missing-data chip.
  - Add accessible title/description for SVG and keyboard/list fallback note if feasible.
- `frontend/src/components/surveys/SurveysView.tsx`
  - Avoid in-place sort mutation in URL sync: use [...state.checkedStatuses].sort().
  - Add active filter chips if small enough; otherwise leave for P1b.
  - Keep retired/completed visible by default.
- `frontend/src/components/surveys/constants.ts`
  - Align visible labels and optionally trim/handle id + quality_score interface mismatch, or pair with backend response patch if needed.

Explicitly out of scope:
- DB/schema migrations
- seed/backfill changes
- autowiki survey writes
- new compare tray
- PlotB integration
- new public planner route
- admin approve/reject UI

Acceptance tests:
- Cold /surveys desktop load clearly says Surveys & Facilities and shows 50 total.
- A user can search DESI/JWST/ALMA, switch Explorer/List, and open detail/peek.
- Explorer states plotted vs matching counts and never silently drops rows because of null axes.
- Label clutter is reduced on all-survey view; labels remain available on hover/focus.
- Retired/completed survey data products remain visible by default.
- No DB rows change; npm build passes; browser console has no new errors.

## Later slices

### P2 · Proposal Planner polish

Scope:
- Add mini-TOC/anchors on /surveys/[slug].
- Lead with release readiness and citable DOI/bibcode when available.
- Add research-use checklist: citable now, catalog fields curated, archive verified, linked ideas available.
- Add “See all ideas using this survey” path or query mode.
- Surface provenance/source URLs for releases/catalog fields where existing data supports it.

Acceptance: Opening /surveys/desi answers: current citable release, products/catalogs available, key columns, archive link, and linked ideas.

### P3 · Freshness Cockpit read-only report

Scope:
- Use existing /api/admin/surveys/proposals and autoapply log as inputs.
- Add read-only report for stale DR strings, broken URLs, low quality_score, missing logo/catalog fields, and release mismatch.
- No approval/write UI until production-data preflight exists.

Acceptance: Operator sees next 10 safest survey maintenance tasks without changing production data.

## Risks to resolve before backend/schema work

- Frontend type/API mismatch: Survey interface expects id and quality_score, but list serializer may not return them.
- Logo schema drift: API/frontend expect logo_url/logo_bg; model inspection did not show canonical columns in Survey ORM.
- Status vocabulary drift across operational/retired/planned/commissioning vs active/completed/decommissioned.
- Migration graph risk: backend parser found multiple apparent heads; verify in real Alembic environment before schema work.
- Research ideas need a stronger survey-filtered “see all” path, but this can wait until detail-page polish.
- Catalog field count is high but provenance/completeness should not be overclaimed.

## Coordinator next recommendation

If Papa approves implementation, start with P1 Atlas IA polish only. It is the safest useful slice because it improves the public Surveys experience without touching production data or schema. Defer Planner, Freshness Cockpit, PlotB, compare tray, and autowiki until the Atlas surface is honest and stable.
