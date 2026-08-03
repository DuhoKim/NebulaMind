# Goru G2 Surveys Data-Shape Audit Report

**Marker:** GORU_G2_SURVEYS_DATA_SHAPE_REPORT_20260707T105700Z
**Run:** SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z

## 1. Seed Survey Counts & Distributions
- **Total Rows:** 50
- **Band Distribution:** optical (17), infrared (7), radio (7), xray (6), sub_mm (5), multi (5), gamma (1), uv (1), astrometric (1)
- **Status Distribution:** operational (26), retired (16), planned (5), commissioning (3)

## 2. Null/Filled Counts for Plotting Fields
Inspected from `backend/data/seed_surveys.json`:
- `wavelength_center_um`: 50 Null, 0 Filled
- `z_max`: 50 Null, 0 Filled
- `dr_year`: 50 Null, 0 Filled
- `data_volume_tb`: 50 Null, 0 Filled
- `limiting_magnitude`: 50 Null, 0 Filled
- `num_sources_count`: 50 Null, 0 Filled
- `sky_coverage_deg2`: 13 Null, 37 Filled

## 3. Backend vs. Frontend Field Comparison
Compared `_survey_row_to_dict` in `backend/app/routers/surveys.py` against `Survey` interface in `frontend/src/components/surveys/constants.ts`:
- **Mismatch - `id`**: Frontend expects `id: number`, but `_survey_row_to_dict` completely omits `id` (only returning `slug`).
- **Mismatch - `quality_score`**: Frontend expects `quality_score: number | null`, but `_survey_row_to_dict` does not return it (it is only computed/returned by the `/{slug}/quality` endpoint).

## 4. PlotA/PlotB Plottability & Log-Scale Logic
- **Null Handling:** Both PlotA and PlotB successfully filter out nulls (`surveyHasPlottableAxes` for PlotA, `!= null` checks for PlotB).
- **Log-Scale Non-Positive Values:**
  - **PlotA:** The logic in `surveyHasPlottableAxisValue` explicitly filters out `value <= 0` when the scale is "log".
  - **PlotB:** `num_sources_count` uses `scaleLog` but only checks for `!= null`. If a survey had 0 sources, it would pass the filter and be rendered at the clamped minimum bound (`Math.max(xMin * 0.5, 1)`) via d3's `clamp(true)`, producing a potentially misleading visual result at the left edge.

## 5. High-Risk Data Assumptions
1. **Critical Missing Data:** 6 out of 7 plotting fields are 100% missing (null) in the seed data. The frontend plots (PlotA and PlotB) will be completely empty or render only missing-data footers, leading to a degraded user experience.
2. **Exclusion of Local Universe Surveys:** Because `z_max` is strictly treated as a "log" scale axis in PlotA (which filters out values `<= 0`), surveys of the Local Group, Milky Way, or strictly local universe where `z_max = 0` (e.g., Gaia) are physically valid but will be silently dropped from the plot.
3. **Missing `id` in List API:** The frontend likely relies on `survey.id` for React keys or routing, but the backend list/detail endpoints omit it. This could cause rendering errors or undefined behaviors.

## Path References Inspected
- `/Users/duhokim/NebulaMind/NebulaMind/backend/data/seed_surveys.json`
- `/Users/duhokim/NebulaMind/NebulaMind/backend/app/routers/surveys.py`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/src/components/surveys/constants.ts`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/src/components/surveys/plotting.ts`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/src/components/surveys/PlotA.tsx`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/src/components/surveys/PlotB.tsx`

## Safety Ledger
- Completed exact tasks via read-only inspection and local script counting.
- No files modified.
- No DB reads/writes, no git commands, no external API calls.
- Confined to the explicit Goru mechanical lane scope.

**STATUS:** PASS / COMPLETE
