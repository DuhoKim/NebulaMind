# Codex/Kun K1 Surveys Frontend Atlas Report

Marker: `CODEX_KUN_K1_SURVEYS_FRONTEND_ATLAS_REPORT_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Status: `PASS_WITH_FINDINGS`

## Files inspected

- `frontend/src/app/surveys/page.tsx`
- `frontend/src/components/surveys/SurveysView.tsx`
- `frontend/src/components/surveys/ControlBar.tsx`
- `frontend/src/components/surveys/BandSpectrumStrip.tsx`
- `frontend/src/components/surveys/ChartView.tsx`
- `frontend/src/components/surveys/PlotA.tsx`
- `frontend/src/components/surveys/PlotB.tsx`
- `frontend/src/components/surveys/plotting.ts`
- `frontend/src/components/surveys/constants.ts`
- `frontend/src/components/surveys/FilterSheet.tsx`
- `frontend/src/components/surveys/SurveyCard.tsx`
- `frontend/src/components/surveys/SurveyPeek.tsx`
- `frontend/scripts/test-surveys-atlas-ia.mjs`
- `docs/survey_explorer_design_v1.md`

## Commands run

- `npm run test:surveys-atlas-ia` from `frontend/`
  - Result: PASS, `surveys atlas IA smoke checks passed`.
  - Writes observed/expected: none. The script is static file assertions only.

Other commands were read-only inspections: `sed`, `rg`, `nl`.

## Answers to brief questions

1. Current `/surveys` passes the Atlas IA smoke script, but it does not fully match the design intent. The biggest gaps are that default view is still List, PlotB is not mounted, and the primary band navigator is a horizontal strip rather than the v1.3 left-sidebar IA.
2. Accessibility is partially improved in PlotA, but gaps remain in List cards, BandSpectrumStrip, PlotB, FilterSheet, and SurveyPeek.
3. Axis params are robust via `parseAxisParam`; `band`, `statuses`, and `plottype` are not validated and can persist malformed URL state.
4. Yes. `PlotB`, `plotType`, `SET_PLOT_TYPE`, and the design's depth-vs-breadth path are currently dead/unused in the rendered Atlas.
5. Top 3 low-risk next changes: validate URL params, wire PlotB into ChartView, and convert clickable div controls to semantic buttons/dialogs.

## Findings

### High — PlotB/depth-vs-breadth exists but is not rendered

`PlotB.tsx` implements the fixed `num_sources_count × limiting_magnitude` plot, including band dimming, but `ChartView.tsx` imports and renders only `PlotA`. `SurveysView.tsx` even comments that `statusOpSurveys` is "used for counts and PlotB", but only `filteredSurveys` is passed to `ChartView`.

Impact: the Atlas misses one of the central design promises: two stacked plots and the depth-vs-breadth view. The unused `plotType` state/URL also suggests earlier design residue.

Concrete proposal, not applied:

```diff
diff --git a/frontend/src/components/surveys/ChartView.tsx b/frontend/src/components/surveys/ChartView.tsx
@@
-import PlotA from "./PlotA"
+import PlotA from "./PlotA"
+import PlotB from "./PlotB"
@@
   surveys: Survey[]
+  depthSurveys: Survey[]
@@
   surveys,
+  depthSurveys,
@@
       <div style={{ background: "#0f172a", border: "1px solid #1e293b", borderRadius: "6px", padding: "1rem 0.5rem" }}>
         <PlotA
@@
         />
       </div>
+      <div style={{ background: "#0f172a", border: "1px solid #1e293b", borderRadius: "6px", padding: "1rem 0.5rem" }}>
+        <PlotB
+          surveys={depthSurveys}
+          band={band}
+          hoverSlug={hoverSlug}
+          selectedSlug={selectedSlug}
+          onHover={(slug) => dispatch({ type: "SET_HOVER", slug })}
+          onClick={onSelect}
+        />
+      </div>
```

```diff
diff --git a/frontend/src/components/surveys/SurveysView.tsx b/frontend/src/components/surveys/SurveysView.tsx
@@
         <ChartView
           surveys={filteredSurveys}
+          depthSurveys={statusOpSurveys}
           band={state.band}
```

### Medium — URL validation is incomplete for `band`, `statuses`, and `plottype`

`xaxis` and `yaxis` are validated through `parseAxisParam`, but `band` is cast directly, `statuses` accepts arbitrary strings, and `plottype` is cast as `any`. Malformed params do not crash immediately, but they can create impossible state, misleading URLs, empty counts, and persisted dead query params.

Relevant code:
- `SurveysView.tsx`: `band: (params.get("band") as BandId) || "all"`
- `SurveysView.tsx`: `checkedStatuses: statusesParam ? statusesParam.split(",").filter(Boolean) : DEFAULT_STATUSES`
- `SurveysView.tsx`: `plotType: (params.get("plottype") as any) || "wavelength_redshift"`

Concrete proposal, not applied:

```diff
diff --git a/frontend/src/components/surveys/constants.ts b/frontend/src/components/surveys/constants.ts
@@
 export const BAND_ORDER: string[] = ["radio", "sub_mm", "infrared", "optical", "uv", "xray", "gamma", "multi"]
+export const VALID_BANDS = new Set<BandId>(["all", "radio", "sub_mm", "infrared", "optical", "uv", "xray", "gamma", "multi"])
+export const VALID_PLOT_TYPES = new Set(["coverage_year", "wavelength_redshift", "depth_sources"] as const)
```

```diff
diff --git a/frontend/src/components/surveys/SurveysView.tsx b/frontend/src/components/surveys/SurveysView.tsx
@@
-  DEFAULT_STATUSES,
+  DEFAULT_STATUSES,
+  VALID_BANDS,
+  VALID_PLOT_TYPES,
@@
   const statusesParam = params.get("statuses")
+  const rawBand = params.get("band")
+  const rawPlotType = params.get("plottype")
+  const checkedStatuses = statusesParam
+    ? statusesParam.split(",").filter(s => DEFAULT_STATUSES.includes(s))
+    : DEFAULT_STATUSES
@@
-    band: (params.get("band") as BandId) || "all",
-    checkedStatuses: statusesParam ? statusesParam.split(",").filter(Boolean) : DEFAULT_STATUSES,
+    band: rawBand && VALID_BANDS.has(rawBand as BandId) ? rawBand as BandId : "all",
+    checkedStatuses: checkedStatuses.length ? checkedStatuses : DEFAULT_STATUSES,
@@
-    plotType: (params.get("plottype") as any) || "wavelength_redshift",
+    plotType: rawPlotType && VALID_PLOT_TYPES.has(rawPlotType as any) ? rawPlotType as any : "wavelength_redshift",
```

### Medium — Semantic accessibility gaps in List and band controls

`PlotA` has `role="img"`, labels, keyboard-openable points, and an ARIA disclosure for not-plotted rows. But important controls remain non-semantic:

- `SurveyCard.tsx` uses a clickable `<div>` without `role`, `tabIndex`, or keyboard handlers.
- `BandSpectrumStrip.tsx` uses clickable `<div>` segments instead of a radio group or buttons; keyboard users cannot select bands.
- `ControlBar.tsx` search input has placeholder text but no stable label.
- `FilterSheet.tsx` and `SurveyPeek.tsx` behave as dialogs but do not expose `role="dialog"`, `aria-modal`, accessible names, initial focus, or focus return/trap.
- `PlotB.tsx` lacks the PlotA SVG `role="img"` / title / desc pattern and keyboard handlers on points.

Concrete low-risk proposal, not applied, for two immediate wins:

```diff
diff --git a/frontend/src/components/surveys/SurveyCard.tsx b/frontend/src/components/surveys/SurveyCard.tsx
@@
     <div
       className="survey-card"
       onClick={() => onOpen(survey.slug)}
+      role="button"
+      tabIndex={0}
+      aria-label={`Open ${survey.name} survey details`}
+      onKeyDown={(event) => {
+        if (event.key === "Enter" || event.key === " ") {
+          event.preventDefault()
+          onOpen(survey.slug)
+        }
+      }}
```

```diff
diff --git a/frontend/src/components/surveys/ControlBar.tsx b/frontend/src/components/surveys/ControlBar.tsx
@@
       <div className="control-bar__search">
+        <label htmlFor="surveys-search" className="sr-only">Search surveys</label>
         <span className="control-bar__search-icon">🔍</span>
         <input
+          id="surveys-search"
```

If the project lacks a global `sr-only`, use an inline visually-hidden style or add local CSS.

### Low — Current IA still diverges from the approved left-sidebar Explorer

The design doc says Explorer is default, `/surveys` or `?view=explorer` should open Explorer, and band navigation should live in a left sidebar. Current code defaults to `directory` and uses a horizontal `BandSpectrumStrip`.

This may be an intentional intermediate state because the smoke script accepts it. If not intentional, the low-risk first step is to flip default view only after product owner confirmation; the bigger left-sidebar layout is not a one-line patch.

Concrete proposal if Explorer should now be default, not applied:

```diff
diff --git a/frontend/src/components/surveys/SurveysView.tsx b/frontend/src/components/surveys/SurveysView.tsx
@@
-  let view: "directory" | "chart" = "directory"
+  let view: "directory" | "chart" = "chart"
@@
-    if (state.view !== "directory") p.set("view", state.view)
+    if (state.view !== "chart") p.set("view", "list")
```

This patch needs care because current internal state uses `"chart"` / `"directory"` while URLs accept `"explorer"` / `"list"`. A cleaner follow-up would rename internal state to `"explorer"` / `"list"`.

### Low — Axis options do not include the design's 7-axis set

`plotting.ts` exposes five selectable axes: sky coverage, wavelength, redshift max, data release year, and data volume. The design lists seven: those five plus `limiting_magnitude` and `num_sources_count`. Since PlotB is fixed on those two fields, excluding them from PlotA may be deliberate simplification, but it is a visible design mismatch.

Recommended action: leave PlotA at five axes if simpler, but document that deviation in code or the design status. If Tori wires PlotB, this becomes much less important.

## Top 3 low-risk next changes for Tori

1. Validate URL params for `band`, `statuses`, and `plottype` so malformed links cannot persist impossible state.
2. Wire `PlotB` into `ChartView`, passing `statusOpSurveys` from `SurveysView` so band selection dims non-band surveys instead of hiding them.
3. Add semantic keyboard accessibility to `SurveyCard`, `BandSpectrumStrip`, `FilterSheet`, `SurveyPeek`, and PlotB using the PlotA pattern as the local reference.

## Safety ledger

- Product files edited: `0`
- Generated public cockpit/dashboard files modified: `0`
- DB writes / SQL / migrations: `0`
- Live wiki/pages publish: `0`
- Deploy / restart: `0`
- git commit / push / PR: `0`
- Credentials / secrets / account / billing / API / GCP / OAuth / token surfaces: `0`
- Browser automation: `0`
- Report writes: `1` — this artifact-only report.

No patches were applied. All diffs above are proposals only.
