# Goru G1 Surveys Filemap & Surface Audit Report

Marker: `GORU_G1_SURVEYS_FILEMAP_REPORT_20260707T105700Z`
Status: READ-ONLY MECHANICAL AUDIT COMPLETED

## 1. File Map
**Pages:**
- `frontend/src/app/surveys/page.tsx`
- `frontend/src/app/surveys/[slug]/page.tsx`
- `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`

**Components (`frontend/src/components/surveys/`):**
- `BandSpectrumStrip.tsx`
- `ChartView.tsx`
- `ControlBar.tsx`
- `FilterSheet.tsx`
- `PlotA.tsx`
- `PlotB.tsx`
- `SurveyCard.tsx`
- `SurveyLogo.tsx`
- `SurveyPeek.tsx`
- `SurveysView.tsx`
- `constants.ts`
- `plotting.ts`

## 2. Interactive Controls Count
Found **8** components containing target interactive elements (`<button>`, `<a>`, `<select>`, `<input>`, `role="button"`):
1. `ChartView.tsx` (`<select>`)
2. `ControlBar.tsx` (`<button>`, `<input>`)
3. `FilterSheet.tsx` (`<button>`, `<input>`)
4. `PlotA.tsx` (`<button>`, `role="button"`)
5. `PlotB.tsx` (`<button>`)
6. `SurveyPeek.tsx` (`<button>`)
7. `SurveysView.tsx` (`<button>`)
8. `SurveyDetailClient.tsx` (`<a>`, `<button>`)

## 3. Route/API Endpoints
Identified from `backend/app/routers/surveys.py`:
- `GET /api/surveys`
- `GET /api/surveys/{slug}`
- `GET /api/surveys/{slug}/events`
- `GET /api/surveys/{slug}/releases`
- `GET /api/surveys/{slug}/datasets`
- `GET /api/surveys/{slug}/ideas`
- `GET /api/surveys/{slug}/pages`
- `GET /api/surveys/{slug}/quality`

## 4. Unused/Dead Files
- **`PlotB.tsx`**: Exists in `frontend/src/components/surveys/PlotB.tsx` but is entirely orphaned/dead. A grep search across the frontend directory confirms it is never imported. A comment in `SurveysView.tsx` mentions it, but the component is not actually rendered or imported.

## 5. Top 5 Places for Tori to Inspect Next
1. **`frontend/src/components/surveys/PlotB.tsx`**: Assess whether to delete this orphaned file or hook it up to fulfill the "Plot B: depth-vs-breadth" spec in the design doc.
2. **`frontend/src/components/surveys/SurveysView.tsx`**: Verify where `PlotB` should be integrated alongside `ChartView` and `PlotA`.
3. **`backend/app/models/survey.py`**: Check if the derived numeric columns (`wavelength_center_um`, `z_max`, `dr_year`, `data_volume_tb`, `limiting_magnitude`, `num_sources_count`) and their SQLAlchemy parsing hooks have been implemented as required by the design doc.
4. **`backend/app/routers/surveys.py`**: Ensure the API endpoint `GET /api/surveys` returns the 6 new fields per the v1 explorer design.
5. **`frontend/scripts/test-surveys-atlas-ia.mjs`**: Ensure test coverage is updated to include `PlotB` rendering and missing-data assertions (currently it only checks `PlotA`).

## Safety Ledger
- Read-only inspection via grep, list_dir, and view_file.
- No database mutations, deploy steps, Git changes, or credential reads were performed.
- Output strictly restricted to this report artifact.

TORI_GORU_DISPATCH_DONE_20260707T105908Z
