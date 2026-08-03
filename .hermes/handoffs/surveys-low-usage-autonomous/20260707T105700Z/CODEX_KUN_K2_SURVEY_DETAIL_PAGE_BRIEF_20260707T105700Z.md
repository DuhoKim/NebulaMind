# Codex/Kun K2 autonomous Survey detail page audit

Marker: `CODEX_KUN_K2_SURVEY_DETAIL_PAGE_BRIEF_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Target lane: Codex / Kun, gpt-5.5 subscription lane

## Mission

Work on NebulaMind Survey detail pages by auditing `/surveys/[slug]` frontend and read-only API integration against the design docs. Produce an artifact-only report with precise findings and patch proposals.

## Absolute boundaries

- Artifact/report only.
- Do not edit product files.
- No DB writes, SQL, migrations, deploy/restart, git commit/push/merge, wiki/page publish, cron, browser automation, or provider/account/billing/API/GCP/OAuth/token/credential activity.
- You may inspect files and run safe read-only tests. Redirect caches/temp outside the repo if needed.

## Repo and files to inspect

Repo root: `/Users/duhokim/NebulaMind/NebulaMind`

Primary files:
- `frontend/src/app/surveys/[slug]/page.tsx`
- `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
- `backend/app/routers/surveys.py`
- `backend/app/models/survey.py`
- `docs/survey_detail_page_v1.md`
- `docs/autowiki_surveys_v1.md`

## Specific questions

1. Does the detail page implement Data Releases, Data Products & Catalogs, News & Events, related wiki pages, and ideas safely?
2. Are fetch paths and loading/error states robust for missing tables/empty data?
3. Does the UI match the design: current release, planned rows, empty state, dataset accordions, key fields, citation links?
4. Are there likely bugs in Next params/API base usage, client fetch, URL handling, or encoded ADS links?
5. What are the top 3 low-risk changes Tori should consider next?

## Required verification

At minimum inspect source. If safe, run:
- `cd frontend && npm run test:surveys-atlas-ia`
Do not start servers or hit production DB.

## Required output

Write exactly one report file:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/CODEX_KUN_K2_SURVEY_DETAIL_PAGE_REPORT_20260707T105700Z.md`

Report must include:
- Marker: `CODEX_KUN_K2_SURVEY_DETAIL_PAGE_REPORT_20260707T105700Z`
- Status: PASS / PASS_WITH_FINDINGS / BLOCKED
- Files inspected with path references
- Commands run and results
- Findings ranked High/Medium/Low
- Exact proposed patches, if any, but do not apply
- Safety ledger confirming no forbidden actions
