# Gemini/Goru G4 autonomous Surveys docs-vs-implementation drift audit
Marker: `GORU_G4_SURVEYS_DOC_DRIFT_REPORT_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Target lane: Gemini / Goru mechanical lane
Status: Completed

## Safety Ledger
- Read-only inspection performed on explicitly listed `docs/`, `frontend/`, and `backend/` files.
- No DB writes, SQL, deployments, git actions, or API/Cloud configurations were executed.
- No source or public files were modified.

## 10 Explicit Design Requirements vs. Implementation Status

| # | Requirement | Source Doc | Status | Evidence Path |
|---|---|---|---|---|
| 1 | Left sidebar as primary band navigator (not top tabs or strip). | `survey_explorer_design_v1.md` | **Missing** | `frontend/src/components/surveys/SurveysView.tsx` uses a horizontal `BandSpectrumStrip` instead of a left sidebar. |
| 2 | Two stacked d3 scatter plots (Plot A and Plot B) in Explorer. | `survey_explorer_design_v1.md` | **Partially Implemented** | `frontend/src/components/surveys/ChartView.tsx` renders `PlotA` but omits `PlotB`, though `PlotB.tsx` exists in the repo. |
| 3 | Band selection switches Plot A X-axis to native units (GHz for radio, keV for X-ray). | `survey_explorer_design_v1.md` | **Missing** | `frontend/src/components/surveys/SurveysView.tsx` hardcodes X-axis to `wavelength_center_um` on band selection instead of native units. |
| 4 | Plot B dims non-band surveys to 0.15 opacity rather than hiding them. | `survey_explorer_design_v1.md` | **Implemented** | `frontend/src/components/surveys/PlotB.tsx` sets `opacity: active ? 1 : 0.15` correctly. |
| 5 | Mobile (<800px) forces List view; Explorer toggle disabled with "View on desktop" note. | `survey_explorer_design_v1.md` | **Missing** | `frontend/src/app/surveys/page.tsx` and `SurveysView.tsx` lack viewport checks or mobile disable logic for the Explorer view. |
| 6 | Two new sections (Data Releases, Data Products & Catalogs) inserted before Primary Science Goals. | `survey_detail_page_v1.md` | **Implemented** | `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx` renders `ReleaseTimeline` and `DatasetCatalogs` immediately before "Primary Science Goals". |
| 7 | Dataset Catalogs accordion with >15 visible rows gets client-side substring filter input. | `survey_detail_page_v1.md` | **Missing** | `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`'s `DatasetCard` component has no filter input for columns. |
| 8 | Newest released entry in Data Releases gets `#6366f1` accent border and "Current" badge. | `survey_detail_page_v1.md` | **Implemented** | `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx` applies the correct border and badge text based on `isCurrent`. |
| 9 | `GET /api/surveys/{slug}` returns `data_releases` and `datasets_count`. | `survey_detail_page_v1.md` | **Implemented** | `backend/app/routers/surveys.py` populates these keys in the detail payload. |
| 10 | `GET /api/surveys/{slug}/datasets` returns datasets with nested `catalog_fields` ordered by `is_key DESC, sort_order`. | `survey_detail_page_v1.md` | **Implemented** | `backend/app/routers/surveys.py` performs the correct query and ordering for the nested catalog fields. |

## Top 5 Doc Drift Items Impacting Users

1. **Plot B is completely missing from the Explorer view.** The depth-vs-breadth analysis (Plot B) is built but not rendered in `ChartView.tsx`, depriving astronomers of a critical comparative capability specifically designed for evaluating dataset depth.
2. **Left sidebar navigation is missing.** The UI uses a horizontal `BandSpectrumStrip` instead of the specified left sidebar, which was explicitly chosen in the spec to handle the 17x range in per-band density and improve scanability.
3. **Axis units do not adapt to native band units.** When selecting Radio or X-ray, the X-axis switches to `wavelength_center_um` instead of the expected `frequency_ghz` or `energy_kev`, forcing astronomers to perform mental conversions contrary to the design spec.
4. **No mobile breakpoint fallback for Explorer.** Mobile users (<800px) are shown the dense scatter plot instead of being forced to the List view, resulting in an unreadable and broken mobile experience.
5. **No client-side column filtering in Datasets.** Users viewing large catalogs (e.g., DESI zcatalog) with >15 columns have no way to substring filter the field list, breaking the intended UX for extensive datamodels.

Done marker: TORI_GORU_DISPATCH_DONE_20260707T105908Z
