# Gemini/Goru G4 autonomous Surveys docs-vs-implementation drift audit

Marker: `GORU_G4_SURVEYS_DOC_DRIFT_BRIEF_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Target lane: Gemini / Goru mechanical lane

## Mission

Use Gemini/Goru quota for a bounded docs-vs-implementation drift audit for NebulaMind Surveys pages. Produce a report; do not modify product files.

## Absolute boundaries

- Artifact/report only.
- Do not edit product/source/generated public files.
- No DB writes, SQL, migrations, deploy/restart, git, wiki publish, cron, browser automation, provider/account/billing/API/GCP/OAuth/token/credential activity.
- Read-only file inspection and simple counts are allowed.

## Inspect these paths

Repo root: `/Users/duhokim/NebulaMind/NebulaMind`

Docs:
- `docs/survey_explorer_design_v1.md`
- `docs/survey_detail_page_v1.md`
- `docs/autowiki_surveys_v1.md`

Implementation:
- `frontend/src/app/surveys/page.tsx`
- `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
- `frontend/src/components/surveys/SurveysView.tsx`
- `frontend/src/components/surveys/ChartView.tsx`
- `frontend/src/components/surveys/PlotA.tsx`
- `frontend/src/components/surveys/PlotB.tsx`
- `backend/app/routers/surveys.py`

## Mechanical tasks

1. Extract 10 explicit design requirements from the docs.
2. Mark each as implemented / partially implemented / missing / obsolete.
3. Include exact source path evidence for each classification.
4. Identify the top 5 doc drift items that would matter to a user of Surveys pages.
5. Avoid broad redesign suggestions; keep to concrete deltas.

## Required output

Write exactly one report file:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/GORU_G4_SURVEYS_DOC_DRIFT_REPORT_20260707T105700Z.md`

Report must include marker `GORU_G4_SURVEYS_DOC_DRIFT_REPORT_20260707T105700Z`, status, 10-row requirement table, path references, and safety ledger.
