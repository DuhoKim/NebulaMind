# Surveys Three-Lane Design Studio — 20260626T132110Z

**Status:** design-only coordinator draft while Page58 audit is deferred.  
**DB writes:** 0.  
**Repo:** `/Users/duhokim/NebulaMind/NebulaMind`.

## Grounding from current repo/data

- `/surveys` exists: `frontend/src/app/surveys/page.tsx` + `frontend/src/components/surveys/SurveysView.tsx`.
- Detail pages exist: `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`.
- Backend APIs exist: `backend/app/routers/surveys.py`.
- Models exist: `backend/app/models/survey.py`.
- Prior design/audit docs exist: `docs/surveys_directory_design_v1.md`, `docs/survey_explorer_design_v1.md`, `docs/survey_detail_page_v1.md`, `docs/surveys_tab_functional_audit_v1.md`, `docs/autowiki_surveys_v1.md`.

Live read-only counts:

- Surveys: `50`
- Data-release rows: `107`
- Dataset rows: `57`
- Catalog-field rows: `644`
- Numeric coverage: `{'wavelength_center_um': 50, 'z_max': 49, 'dr_year': 42, 'data_volume_tb': 48, 'limiting_magnitude': 30, 'num_sources_count': 39}`
- Band counts: `{'optical': 17, 'infrared': 7, 'radio': 7, 'xray': 6, 'multi': 5, 'sub_mm': 5, 'astrometric': 1, 'gamma': 1, 'uv': 1}`
- Status counts: `{'operational': 26, 'retired': 16, 'planned': 5, 'commissioning': 3}`

## Three coordinated design lanes

### A · Survey Atlas: Make /surveys answer “where does this facility live in parameter space?” before it asks the user to read cards.

**Owner:** Product / IA lane  
**Primary surface:** `/surveys Explorer`

Key moves:
- Keep chart/explorer as the default mental model, but rename “Chart” to “Atlas” and “Directory” to “List”.
- Make the landing state explain what is plotted vs filtered; persistent labels only for ≤15 plotted surveys, hover labels otherwise.
- Keep retired/completed surveys visible by default because data products remain scientifically active.
- Add an explicit “missing from this axis” chip to every plot and count label: M plotted · N matching filters.

Acceptance: Cold desktop load shows JWST/HST/ALMA/Chandra-class observatories honestly, with missing-axis explanations instead of silent disappearance.

### B · Proposal Planner: The detail page should help a researcher decide whether a science idea is feasible with currently citable data.

**Owner:** Researcher workflow lane  
**Primary surface:** `/surveys/[slug]`

Key moves:
- Lead with release readiness: current release, planned next release, citable DOI/bibcode, and “what changed”.
- Keep catalog products close to release history; datasets + key fields are the evidence for feasibility.
- Add “research-use checklist” blocks: citable now, has catalog fields, linked ideas, archive link verified.
- Use honest empty states for planned observatories and fields not curated yet.

Acceptance: Opening /surveys/desi cold lets Papa answer: which release is citable, what products exist, which columns matter, and what is coming next.

### C · Freshness Cockpit: Surveys are curated metadata; the operator needs a safe queue showing what is stale, missing, or risky before auto-refreshes land.

**Owner:** Backend / operations lane  
**Primary surface:** `admin/operator report, not public reader UI first`

Key moves:
- Show quality_score components, stale DR strings, failing URLs, missing catalog fields, and latest release mismatch.
- Separate read-only freshness proposals from writes using the same backup/rollback approval discipline used on Page58.
- Create a release-check queue for T1 surveys before any cron/autowiki change.
- Treat catalog-field curation as manual/provenanced, not LLM-generated.

Acceptance: Operator can see the next 10 safest Surveys maintenance tasks without touching production data or guessing which rows matter.

## Recommended sequence

1. P0: Design only — finish three-lane synthesis and pick first implementation slice. No DB mutation.
2. P1: Frontend Explorer polish: naming, plotted/matching counts, missing-axis chip, label density, no schema changes.
3. P2: Detail page Planner surface: release timeline + dataset/catalog sections already backed by API; verify DESI/SDSS/ELT.
4. P3: Freshness cockpit read-only report: expose stale/missing metadata queue; no auto-writes.
5. P4: Only after P1–P3 are accepted, prepare any DB/write packet for seed/backfill or autowiki changes.

## Risks / guardrails

- Do not rebuild a second Surveys concept; current repo already has routes, models, APIs, numeric columns, release rows, datasets, and catalog fields.
- Avoid overclaiming catalog completeness: 644 fields exist, but source/provenance quality still needs spot checks by survey.
- Explorer charts must explain missing data; silent drops are the core UX failure identified in the prior audit.
- Any backend seed/backfill or autowiki write requires a separate production-data preflight packet.

## Files likely to change if we implement later

- `frontend/src/components/surveys/ControlBar.tsx` — rename toggles, improve search/filter copy.
- `frontend/src/components/surveys/ChartView.tsx` — plotted/matching count, missing-axis chip, chart header hierarchy.
- `frontend/src/components/surveys/PlotA.tsx` — label density and missing-data reporting.
- `frontend/src/components/surveys/constants.ts` — axis/view labels and interface cleanup.
- `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx` — Planner sections and research-use checklist polish.
- `backend/app/routers/surveys.py` — only if an existing endpoint misses a field needed by the Planner; avoid new APIs unless necessary.
- `docs/` or `frontend/public/agent-reports/` — read-only operator/freshness reports.

## Validation later

- `npm run build` from `frontend/`.
- Browser-verify `/surveys`, `/surveys/desi`, `/surveys/elt` on desktop.
- API smoke: `/api/surveys`, `/api/surveys/desi`, `/api/surveys/desi/datasets`, `/api/surveys/desi/releases`.
- No production data mutation without a separate approval packet.
