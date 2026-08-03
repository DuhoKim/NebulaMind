# Surveys test-gap audit report

Marker: `CODEX_KUN_K3_SURVEYS_TEST_GAP_REPORT_20260707T105700Z`

Status: `PASS_WITH_FINDINGS`

## Commands run and results

- `sed -n '1,240p' .hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/CODEX_KUN_K3_SURVEYS_TEST_GAP_BRIEF_20260707T105700Z.md`
  - Result: read the brief and confirmed artifact-only boundaries.
- `sed -n '1,260p' frontend/scripts/test-surveys-atlas-ia.mjs`
  - Result: inspected existing frontend static smoke script.
- `sed -n '1,220p' frontend/package.json`
  - Result: confirmed only Surveys npm test script is `test:surveys-atlas-ia`.
- `sed -n '1,260p' frontend/src/app/surveys/page.tsx`
  - Result: inspected Surveys Atlas page loading/stats/copy behavior.
- `sed -n '1,320p' frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
  - Result: inspected detail client types and rendering helpers.
- `ls frontend/src/components/surveys`
  - Result: listed Surveys components.
- `sed -n '1,340p' frontend/src/components/surveys/SurveysView.tsx`
  - Result: inspected reducer, URL sync, filters, search, band counts, modal wiring.
- `sed -n '1,340p' frontend/src/components/surveys/ChartView.tsx`
  - Result: inspected plotted/missing count behavior and axis controls.
- `sed -n '1,360p' frontend/src/components/surveys/PlotA.tsx`
  - Result: inspected PlotA plottability, missing-data chip, labels, SVG accessibility.
- `sed -n '1,280p' frontend/src/components/surveys/plotting.ts`
  - Result: inspected pure axis helpers.
- `sed -n '1,320p' frontend/src/components/surveys/constants.ts`
  - Result: inspected shared Survey, axis, band, status types/constants.
- `sed -n '1,360p' backend/app/routers/surveys.py`
  - Result: inspected list/detail/event/release/dataset/quality route helpers.
- `sed -n '1,360p' backend/app/services/survey_health.py`
  - Result: inspected deterministic survey quality scoring.
- `rg --files backend | rg '(^|/)test|tests|_test\.py$|test_.*\.py$'`
  - Result: backend test suite exists, but no obvious Surveys-specific backend test file was listed.
- `find backend -maxdepth 3 -type d -name '*test*' -o -name 'tests'`
  - Result: confirmed `backend/tests`.
- `sed -n '320,760p' backend/app/routers/surveys.py`
  - Result: inspected dataset, ideas, pages, quality route tails.
- `sed -n '1,280p' frontend/src/components/surveys/ControlBar.tsx`
  - Result: inspected mode toggle, debounced search, filter button.
- `cd frontend && npm run test:surveys-atlas-ia`
  - Result: PASS. Output: `surveys atlas IA smoke checks passed`.
- `rg -n "surveys|survey_health|Survey" backend/tests frontend/scripts frontend/src -g '*test*' -g '*.mjs' -g '*.py' -g '*.tsx'`
  - Result: found the static frontend script and app/component references; no dedicated backend Surveys tests found under `backend/tests`.
- `nl -ba frontend/scripts/test-surveys-atlas-ia.mjs | sed -n '1,220p'`
  - Result: captured line references for existing assertions.
- `nl -ba frontend/src/components/surveys/plotting.ts | sed -n '1,220p'`
  - Result: captured line references for helper gaps.
- `nl -ba backend/app/services/survey_health.py | sed -n '1,260p'`
  - Result: captured line references for health scorer gaps.

Backend tests inspected: existing backend test file names were listed and searched. No backend test command was run because the required verification only named the frontend script, and this audit did not identify an existing Surveys-specific backend test module to execute.

## Current coverage map

### Covered now

- `frontend/scripts/test-surveys-atlas-ia.mjs` statically verifies Surveys Atlas page copy and stats row presence in `frontend/src/app/surveys/page.tsx`.
- It verifies the visible mode toggle labels changed to `List` and `Explorer`, and that visible `Directory` / `Chart` toggle labels are absent.
- It verifies URL status sorting avoids direct reducer-state mutation by requiring `[...state.checkedStatuses].sort()` and rejecting `state.checkedStatuses.sort()`.
- It verifies ChartView static copy distinguishes plotted rows from matching filters and explains missing-data rows.
- It verifies PlotA source contains SVG `role="img"`, `aria-labelledby`, missing-data disclosure `aria-expanded` / `aria-controls`, low-density label gating, centralized missing-survey rendering, and zero-plotted-state missing-data rendering.
- It verifies `frontend/src/components/surveys/plotting.ts` exists and exports axis options, axis value conversion, plottability, and URL axis parsing helpers.
- It verifies malformed initial `xaxis` / `yaxis` URL params are passed through `parseAxisParam`.
- It verifies ChartView and PlotA import `./plotting`, and rejects stale private plottability / unused `statusOpSurveys` prop patterns.

### Not covered now

- No executable tests validate the pure plotting semantics in `frontend/src/components/surveys/plotting.ts`: valid/invalid axis parsing, wavelength unit conversion by band, `null` handling, zero/negative log-axis rejection, or linear-axis acceptance.
- No executable tests validate the filter/search/band-count behavior in `frontend/src/components/surveys/SurveysView.tsx`: astrometric-to-multi mapping, operator filtering, status filtering, search over name/full_name/operator/science goals, reset behavior, active-filter count, and URL serialization.
- No executable tests validate ChartView/PlotA rendered behavior. The current script checks source text, not rendered DOM, event handlers, keyboard activation, or actual missing-data count calculations.
- No tests cover `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx` formatting helpers, fallback states, nested API fetch behavior, release timeline current/planned/superseded handling, dataset catalog field rendering, facility profile/events rendering, or not-found/loading transitions.
- No dedicated backend tests were found for `backend/app/routers/surveys.py`: route serializer helpers, JSON list parsing, numeric coercions, graceful fallback when optional survey tables are absent, allowed sort mappings, 404 behavior, or query parameter constraints.
- No dedicated backend tests were found for `backend/app/services/survey_health.py`: scoring thresholds, retired freshness/program rules, dict-vs-object access, URL override behavior, utility-score clamping, and date-sensitive DR freshness.

## Easy static/smoke tests to add

1. `frontend/scripts/test-surveys-plotting-helpers.mjs`
   - Assertion intent:
     - `parseAxisParam(null, fallback)` and invalid strings return the fallback.
     - every `AXIS_OPTIONS[*].key` round-trips through `parseAxisParam`.
     - `getAxisLabel("wavelength_center_um", "radio")` uses the radio unit, while `"all"` uses microns.
     - `getSurveyAxisValue` returns `null` for missing numeric values.
     - log-scaled axes reject `0` and negative values via `surveyHasPlottableAxisValue`.
     - linear `dr_year` accepts `0` if present.
     - `surveyHasPlottableAxes` requires both selected axes to be plottable.
   - Feasibility: requires a small TS/ESM execution harness because `plotting.ts` imports via the `@/` alias and is TypeScript. This can still be browserless/serverless using `tsx`, `esbuild-register`, or a narrow JS helper extraction.

2. `frontend/scripts/test-surveys-view-static.mjs`
   - Assertion intent:
     - `makeInitial` accepts `view=explorer` and `view=chart` as chart, `view=list` and `view=directory` as directory.
     - URL sync writes canonical `view=chart`, omits default statuses, and includes non-default axes/search/operators.
     - source retains search fields `name`, `full_name`, `operator`, and `primary_science_goals`.
     - source retains astrometric-to-multi band mapping in both band counts and filtering.
     - reset returns band/status/operators/search to defaults but intentionally does not reset view/axis selections.
   - Feasibility: static source smoke is easy. Functional reducer tests would require exporting or moving pure state helpers out of the client component.

3. `frontend/scripts/test-surveys-detail-static.mjs`
   - Assertion intent:
     - detail client fetches `/api/surveys/${slug}`, `/ideas?include_stale=0`, `/datasets`, and `/events?limit=8`.
     - not-found branch displays `Survey not found`.
     - release timeline handles empty releases and statuses `planned`, `released`, `superseded`, `final`.
     - dataset catalog fields surface key fields and source URLs.
     - event cards surface facility, confidence/status/source/data portal fields.
   - Feasibility: static smoke is easy; functional rendering should wait for a component test harness.

4. `backend/tests/test_survey_health.py`
   - Assertion intent:
     - dict and object inputs produce equivalent component scores.
     - required-field completeness treats non-empty lists/dicts as filled and empty strings/lists as empty.
     - retired/decommissioned surveys get full `dr_freshness` and `programs_count`.
     - active surveys with no release year get zero `dr_freshness`.
     - URL override args take precedence over stored `url_archive_ok` / `url_mission_ok`.
     - `compute_quality` clamps utility below `0` and above `10`.
   - Feasibility: no DB/server/browser required. Date-sensitive DR freshness should use monkeypatching for `datetime.date.today()` or avoid exact current-date score assertions.

5. `backend/tests/test_surveys_router_serializers.py`
   - Assertion intent:
     - `_survey_row_to_dict` parses JSON strings and preserves list-valued JSON columns.
     - numeric fields are coerced to `float` / `int` and `None` is preserved.
     - `_release_row_to_dict`, `_catalog_field_row_to_dict`, `_dataset_row_to_dict`, and `_facility_profile_row_to_dict` perform expected coercions.
     - `_idea_counts_by_survey_id`, `_get_survey_releases`, `_get_survey_datasets_count`, and `_get_survey_facility_profiles` return safe fallback values when `db.execute` raises.
   - Feasibility: no DB/server required if tests use `types.SimpleNamespace` rows and fake DB objects.

## Tests that require fixture/API/server work and should wait

- End-to-end `/api/surveys` list route tests with realistic database rows, sort order, `wavelength_band`, `status`, and `q` filters.
- `/api/surveys/{slug}` detail route tests that exercise related wiki pages, releases, datasets count, and facility profiles against fixture tables.
- `/api/surveys/{slug}/events` tests for date-window filtering and ordering because they depend on `NOW()` and facility link/news fixtures.
- Frontend rendered component tests for `SurveysView`, `PlotA`, and `SurveyDetailClient` because the project currently has no React test runner configured in `frontend/package.json`.
- Browser accessibility/interaction tests for keyboard-opening PlotA points, ResizeObserver sizing, and modal/peek focus behavior. These should wait until a deliberate browser/component-test harness is selected.

## Suspicious dead assertions or stale assumptions

- `frontend/scripts/test-surveys-atlas-ia.mjs` line 68 uses a broad `/surveys\.length > 0[\s\S]*renderMissingSurveys\(\)/` regex. It proves the source contains both tokens in order, but not that `renderMissingSurveys()` is reachable only in the intended zero-plotted branch.
- Lines 54-58 check accessibility by source-token presence. They do not prove the rendered SVG/title/desc IDs are wired correctly, unique, or visible to assistive tech.
- Lines 73-76 check helper export names, but do not execute any helper logic. A helper could be exported and semantically wrong while this script still passes.
- Lines 77-78 require exact `parseAxisParam(params.get("xaxis"), "wavelength_center_um")` source text. This is useful as a regression tripwire but brittle to harmless refactors such as extracting defaults.
- Lines 81-83 assert absence of stale private plottability/prop names. These are useful cleanup guards, but the `statusOpSurveys` string still exists as a local filtered list in `SurveysView`; the assertion is narrowly scoped to the ChartView prop and could become confusing if the local name is renamed or reused legitimately.
- The script checks visible labels are not `Directory` / `Chart`, but comments still contain `Directory/Chart`. That is acceptable today because the regex targets visible button text, but it is a stale terminology smell in adjacent source comments.
- The script is entirely source-static. It would not catch a broken import alias, a TypeScript type error, a runtime render crash, or a mismatch between ChartView's `plottedCount` and PlotA's actual points if both source strings remain present.

## Exact patch proposals

These are proposals only. They were not applied.

### Proposal A: pure frontend plotting helper test

```diff
diff --git a/frontend/package.json b/frontend/package.json
--- a/frontend/package.json
+++ b/frontend/package.json
@@
-    "test:surveys-atlas-ia": "node scripts/test-surveys-atlas-ia.mjs"
+    "test:surveys-atlas-ia": "node scripts/test-surveys-atlas-ia.mjs",
+    "test:surveys-plotting": "tsx scripts/test-surveys-plotting-helpers.ts"
@@
-    "typescript": "^5"
+    "typescript": "^5",
+    "tsx": "^4.20.0"
diff --git a/frontend/scripts/test-surveys-plotting-helpers.ts b/frontend/scripts/test-surveys-plotting-helpers.ts
new file mode 100644
--- /dev/null
+++ b/frontend/scripts/test-surveys-plotting-helpers.ts
@@
+import assert from "node:assert/strict";
+import {
+  AXIS_OPTIONS,
+  getAxisLabel,
+  getSurveyAxisValue,
+  parseAxisParam,
+  surveyHasPlottableAxisValue,
+  surveyHasPlottableAxes,
+} from "../src/components/surveys/plotting";
+import type { Survey } from "../src/components/surveys/constants";
+
+const survey = {
+  wavelength_center_um: 1000,
+  sky_coverage_deg2: 0,
+  z_max: -1,
+  dr_year: 0,
+  data_volume_tb: null,
+} as Survey;
+
+assert.equal(parseAxisParam(null, "z_max"), "z_max");
+assert.equal(parseAxisParam("bad-axis", "dr_year"), "dr_year");
+for (const option of AXIS_OPTIONS) {
+  assert.equal(parseAxisParam(option.key, "z_max"), option.key);
+}
+
+assert.match(getAxisLabel("wavelength_center_um", "radio"), /\(GHz\)|\(MHz\)|\(m\)/);
+assert.equal(getAxisLabel("wavelength_center_um", "all"), "Wavelength (μm)");
+
+assert.equal(getSurveyAxisValue(survey, "data_volume_tb", "all"), null);
+assert.equal(surveyHasPlottableAxisValue(survey, "sky_coverage_deg2", "all"), false);
+assert.equal(surveyHasPlottableAxisValue(survey, "z_max", "all"), false);
+assert.equal(surveyHasPlottableAxisValue(survey, "dr_year", "all"), true);
+assert.equal(surveyHasPlottableAxes(survey, "dr_year", "sky_coverage_deg2", "all"), false);
+
+console.log("surveys plotting helper checks passed");
```

Note: exact wavelength unit assertion should be aligned with `frontend/src/lib/wavelengthUnits` before applying.

### Proposal B: backend survey health tests

```diff
diff --git a/backend/tests/test_survey_health.py b/backend/tests/test_survey_health.py
new file mode 100644
--- /dev/null
+++ b/backend/tests/test_survey_health.py
@@
+from types import SimpleNamespace
+
+from app.services.survey_health import compute_quality, compute_survey_health
+
+
+def complete_survey(**overrides):
+    base = {
+        "slug": "demo",
+        "name": "Demo",
+        "full_name": "Demo Survey",
+        "description": "A rich survey description. " * 12,
+        "wavelength_range": "optical",
+        "wavelength_band": "optical",
+        "sky_coverage_deg2": 1000,
+        "sky_coverage_note": "wide",
+        "redshift_range": "0 < z < 2",
+        "instruments_json": ["cam1", "cam2", "cam3", "cam4"],
+        "current_data_release": "DR 2026",
+        "data_volume": "10 TB",
+        "primary_science_goals": "Measure galaxies and dark matter across 1000 deg2.",
+        "flagship_programs_json": ["wide", "deep", "time"],
+        "operator": "Demo Org",
+        "status": "operational",
+        "archive_url": "https://example.test/archive",
+        "mission_url": "https://example.test",
+        "url_archive_ok": True,
+        "url_mission_ok": True,
+    }
+    base.update(overrides)
+    return base
+
+
+def test_compute_survey_health_accepts_dict_and_object_inputs():
+    data = complete_survey()
+    obj = SimpleNamespace(**data)
+    assert compute_survey_health(data).to_dict() == compute_survey_health(obj).to_dict()
+
+
+def test_retired_surveys_get_full_freshness_and_program_credit():
+    result = compute_survey_health(complete_survey(
+        status="retired",
+        current_data_release="Legacy final release",
+        flagship_programs_json=[],
+    ))
+    assert result.components.dr_freshness == 1.0
+    assert result.components.programs_count == 1.0
+
+
+def test_url_overrides_take_precedence_over_stored_values():
+    result = compute_survey_health(
+        complete_survey(url_archive_ok=False, url_mission_ok=False),
+        url_archive_ok=True,
+        url_mission_ok=False,
+    )
+    assert result.components.url_validity == 0.5
+
+
+def test_compute_quality_clamps_utility_score():
+    survey = complete_survey()
+    assert compute_quality(survey, utility_score=-10) == compute_quality(survey, utility_score=0)
+    assert compute_quality(survey, utility_score=99) == compute_quality(survey, utility_score=10)
```

### Proposal C: backend router serializer tests

```diff
diff --git a/backend/tests/test_surveys_router_serializers.py b/backend/tests/test_surveys_router_serializers.py
new file mode 100644
--- /dev/null
+++ b/backend/tests/test_surveys_router_serializers.py
@@
+from datetime import date, datetime
+from types import SimpleNamespace
+
+from app.routers import surveys
+
+
+def test_survey_row_to_dict_parses_json_and_coerces_numbers():
+    row = SimpleNamespace(
+        id=7,
+        slug="demo",
+        name="Demo",
+        full_name="Demo Survey",
+        description="desc",
+        emoji=None,
+        logo_url=None,
+        logo_bg=None,
+        wavelength_range="optical",
+        wavelength_band="optical",
+        sky_coverage_deg2="123.4",
+        sky_coverage_note=None,
+        redshift_range=None,
+        instruments_json='["cam"]',
+        current_data_release="DR1",
+        data_volume="1 TB",
+        primary_science_goals="goals",
+        flagship_programs_json='["wide"]',
+        operator="Demo Org",
+        status="operational",
+        archive_url=None,
+        mission_url=None,
+        updated_at=datetime(2026, 1, 2, 3, 4, 5),
+        wavelength_center_um="0.5",
+        z_max="2",
+        dr_year="2026",
+        data_volume_tb="1.25",
+        limiting_magnitude=None,
+        num_sources_count="42",
+    )
+    out = surveys._survey_row_to_dict(row, linked_count=3)
+    assert out["instruments"] == ["cam"]
+    assert out["flagship_programs"] == ["wide"]
+    assert out["linked_research_ideas_count"] == 3
+    assert out["sky_coverage_deg2"] == 123.4
+    assert out["dr_year"] == 2026
+    assert out["updated_at"] == "2026-01-02T03:04:05"
+
+
+def test_release_and_dataset_serializers_coerce_values():
+    release = surveys._release_row_to_dict(SimpleNamespace(
+        label="DR1",
+        release_date=date(2026, 1, 2),
+        release_year="2026",
+        summary="summary",
+        n_objects="100",
+        sky_coverage_deg2="10.5",
+        data_volume_tb="2.5",
+        doi=None,
+        bibcode=None,
+        url=None,
+        status="released",
+    ))
+    assert release["release_date"] == "2026-01-02"
+    assert release["n_objects"] == 100
+    assert release["data_volume_tb"] == 2.5
+
+    dataset = surveys._dataset_row_to_dict(SimpleNamespace(
+        slug="cat",
+        name="Catalog",
+        full_name="Catalog",
+        description="desc",
+        data_type="catalog",
+        release_label="DR1",
+        release_year="2026",
+        sample_size="100",
+        doi=None,
+        bibcode=None,
+        registry=None,
+        license=None,
+        primary_url="https://example.test",
+        archive_url=None,
+        url_verified_ok=True,
+    ), catalog_fields=[{"name": "id"}])
+    assert dataset["release_year"] == 2026
+    assert dataset["sample_size"] == 100
+    assert dataset["catalog_fields"] == [{"name": "id"}]
+
+
+class RaisingDb:
+    def execute(self, *args, **kwargs):
+        raise RuntimeError("missing optional table")
+
+
+def test_optional_router_helpers_fallback_on_db_errors():
+    db = RaisingDb()
+    assert surveys._idea_counts_by_survey_id(db) == {}
+    assert surveys._get_survey_releases(1, db) == []
+    assert surveys._get_survey_datasets_count(1, db) == 0
+    assert surveys._get_survey_facility_profiles(1, db) == []
```

## Safety ledger

- Wrote exactly one artifact file: `.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/CODEX_KUN_K3_SURVEYS_TEST_GAP_REPORT_20260707T105700Z.md`.
- Did not edit source, product, or test files.
- Did not commit, push, deploy, restart services, run migrations, run DB writes, publish wiki/pages, create cron, or use browser automation.
- Did not touch provider/account/billing/API/GCP/OAuth/token/credential surfaces.
- Ran only safe read-only inspections and the required frontend npm test command.
