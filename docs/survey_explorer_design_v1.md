# Survey Explorer v1 — interactive scatter plot for /surveys

**Owner:** Kun 🔬 (design) → Tori (implementation)
**Status:** Papa-approved 2026-05-13 (KST) — v1.3 final: band navigation moved into left sidebar (top tabs removed)
**Date:** 2026-05-13 (KST)
**Filename:** `docs/survey_explorer_design_v1.md`
**References:**
- `docs/surveys_directory_design_v1.md` — directory schema & seed (now 49 surveys live)
- `docs/autowiki_surveys_v1.md` — autoresearch loop that will maintain numeric fields over time
- `frontend/src/app/surveys/page.tsx` — current card list (becomes the secondary view; Explorer is default)

---

## 0. The one-paragraph version

The card list is one row per survey at full width — comprehension scales poorly past ~20 surveys (we have 49). Astronomers reason about surveys by their **place in parameter space** (what wavelength, how much sky, how deep, how recent, how many sources), not by alphabetical name. So **the Explorer becomes the default view** of /surveys; the card list survives as a secondary toggle (`?view=list`). Each survey is rendered as its acronym (no marker dot — the text *is* the marker) in **two stacked d3 scatter plots**: (1) wavelength × sky-coverage — the EM-spectrum-vs-breadth view; and (2) num_sources × limiting_magnitude — the depth-vs-breadth view, unified across all bands. **Band navigation lives in the left sidebar** (`[All Surveys]` + 8 single-select band rows with live counts); selecting a band filters both plots and switches Plot A's axes to that band's native units (radio uses frequency in GHz, X-ray uses energy in keV, etc.). Color encodes wavelength band on both plots. Hover shows a tooltip; **click opens a detail modal in-place** (no navigation away from the Explorer). Most numeric fields are already in the schema but stored as free-text strings — the design's main backend lift is a one-shot parser that materializes 4 derived numeric columns (`wavelength_center_um`, `z_max`, `dr_year`, `data_volume_tb`) plus 2 small new fields (`limiting_magnitude`, `num_sources_count`). Band-specific axis units (frequency, energy) are pure client-side derivations from `wavelength_center_um` — no new columns.

---

## 1. Plot concept

**Two stacked scatter plots**, both with **acronym-only labels** (no marker dot). The label IS the point. Each plot ~700×500, full width of the /surveys page (max 1200px wide), stacked vertically with a ~3rem gap.

- **Plot A (top): wavelength × sky coverage** — the canonical "EM spectrum vs breadth" view (axes are still user-selectable from the 7 options in §2; these are the defaults).
- **Plot B (bottom): num_sources × limiting_magnitude** — the **depth-vs-breadth view**: how many objects a survey delivers vs how faint it can see. Critical for astronomers choosing a dataset for a target science question ("at mag 24 limiting, who has the most galaxies?"). Same acronym-label style, same color-by-band scheme; status opacity tiering identical.

Plot B is a fixed-axes plot in v1 (no dropdowns) because the depth-vs-breadth framing is the entire point of having a second view. Surveys with NULL on either axis are excluded from B with a footnote-chip (most radio/X-ray catalogs lack a meaningful optical limiting_magnitude, and time-domain/imaging-only surveys lack a num_sources_count). Plot A axes remain user-selectable per §2.

The card-list layout below illustrates Plot A only; Plot B has the same visual style.

```
       Sky coverage (deg²)  ↑
                   ALL-SKY  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
                            │                                              │
                            │              GAIA   PLANCK   FERMI-LAT       │
                  10,000 ─  │   ASKAP-EMU    SDSS-V       DESI             │
                            │                                              │
                            │            DES         RUBIN-LSST            │
                   1,000 ─  │              HSC-SSP    UNIONS               │
                            │                                              │
                     100 ─  │      H-ATLAS    HETDEX                       │
                            │                                              │
                      10 ─  │       VIPERS                                 │
                            │                                              │
                       1 ─  │  COSMOS2020    CDF-S                         │
                            │                                              │
                            └──────────────────────────────────────────────→
                              1 GHz   10 μm   1 μm   0.5 μm   1 keV  10 GeV
                                          Wavelength (center)
```

(That's just to fix intuition — the actual axes are selectable.)

**Why no marker dot?** 49 acronyms is a tight count. With labels as glyphs the chart reads as a *map* — no separate visual hierarchy of dot-then-label needed. Acronyms are mostly 3–8 chars; that's the whole point of the convention.

---

### 1.5 Per-band density (live, 2026-05-13) — the case for sidebar navigation

```
optical        n=17  4MOST DEEP2 DES DESI ELT GAMA HETDEX HSC-SSP KIDS PFS
                     PANSTARRS SDSS SDSS-V UNIONS VIPERS WEAVE ZCOSMOS
radio          n=7   ASKAP-EMU HIPASS LOFAR MEERKAT SKA1 VLA NGVLA
infrared       n=7   2MASS JWST ROMAN SPHEREX UKIDSS VIKING WISE
xray           n=6   CDF-N CDF-S CHANDRA ROSAT XMM EROSITA
multi          n=5   COSMOS2020 EUCLID HST PLANCK RUBIN-LSST
sub_mm         n=5   ACT ALMA CMB-S4 H-ATLAS SPT
gamma          n=1   FERMI-LAT
uv             n=1   GALEX
astrometric    n=1   GAIA
```

**Range = 17×.** Optical alone is 17 acronyms; UV, Gamma, Astrometric have 1 each.

**Layout choice (v1.3): Left sidebar as primary band navigator** — single-select list, not tabs, not small multiples, not accordion.

- **Sidebar (chosen, v1.3).** `[All Surveys]` row + 8 band rows with live counts. Click a band → both plots filter to that band, Plot A's axes switch to native units (GHz / keV / μm). Active band is highlighted. Status + Operator filters live in the same sidebar below a divider. **Rationale:** Papa flagged that top tabs + sidebar checkboxes were redundant; one source of band selection is enough. The sidebar reads left-to-right with the plot in the central column — natural for a "pick your regime" workflow.
- **Top tabs (rejected in v1.3, was the v1.2 choice).** Worked, but having both top tabs AND sidebar filter checkboxes was cluttered. Removed.
- **Small multiples (rejected).** A 3×3 grid of mini-scatters would have UV/Gamma/Astrometric cells holding a single acronym in a vast empty space — looks broken; each cell ~300×200 with 17 optical acronyms is unreadable.
- **Accordion (rejected).** Default-collapsed sections force a click before any plot is visible.

The **Multi** sidebar row merges `multi` (5) and `astrometric` (1 = Gaia) → **6 surveys** in that bucket (Papa's prototype spec wrote "(5)" but the live count is 6 with Gaia included; sidebar should show `🔭 Multi (6)`).

Plot B (depth-vs-breadth) does NOT filter exclusively — comparing num_sources × limiting_magnitude across bands is one of its key purposes. When a band is selected in the sidebar, Plot B **dims** non-band surveys to opacity 0.15 (rather than hiding) to preserve cross-band context.

### 1.6 Band-specific axis defaults — Plot A

When a band is selected in the left sidebar, Plot A's axes auto-switch to native units for that band. User can still override via the axis dropdowns.

| Sidebar selection | Default X | Default Y | Notes |
|---|---|---|---|
| **All Surveys** | wavelength_center_um (log) | sky_coverage_deg2 (log) | v1.1 baseline; spans ~10 orders. |
| **Radio** | frequency_ghz (log) | sky_coverage_deg2 (log) | Radio astronomers think in GHz/MHz. `frequency_ghz = 299792.458 / wavelength_center_um` (client-side). |
| **Sub-mm** | frequency_ghz (log) | sky_coverage_deg2 (log) | Same — sub-mm regime sits at the GHz↔THz boundary, freq is native. |
| **Infrared** | wavelength_center_um (linear) | sky_coverage_deg2 (log) | μm is native; 0.6–28 μm is sub-decade enough that linear reads cleanly. |
| **Optical** | wavelength_center_um (linear, μm) | sky_coverage_deg2 (log) | Tight range (0.3–1.1 μm). Linear better than log here. Optionally show Å on hover. |
| **UV** | wavelength_center_um (linear) | sky_coverage_deg2 (log) | n=1; mostly placeholder. |
| **X-ray** | energy_kev (log) | sky_coverage_deg2 (log) | X-ray astronomers think in keV. `energy_kev = 1.2398 / wavelength_center_um` (client-side; photon E×λ = 1.2398 keV·μm). |
| **Gamma** | energy_kev (log) | sky_coverage_deg2 (log) | n=1; placeholder. Could extend to MeV/GeV/TeV labels later. |
| **Multi** (incl. Astrometric) | wavelength_center_um (log) | sky_coverage_deg2 (log) | Spans multiple regimes (HST/Euclid/Rubin/Planck/Gaia); log range is appropriate. Sidebar label `🔭 Multi (6)`. |

**No new DB columns.** `frequency_ghz` and `energy_kev` derive from `wavelength_center_um` (which the migration adds). A 6-line `frontend/src/lib/wavelengthUnits.ts` utility handles the math.

---

## 2. Selectable axes (Plot A only)

Plot A's X and Y are user-selectable from two dropdowns above the plot. Both default values listed in §5. **Plot B's axes are fixed** at `num_sources_count` (X) × `limiting_magnitude` (Y) — that pairing IS the second plot's purpose.

| Field | Source | Type | Scale | Notes |
|---|---|---|:-:|---|
| **Wavelength (center)** | `wavelength_center_um` (NEW derived) | μm | log | Computed from `wavelength_range` parser; CMB → mm regime; X-ray/γ → μm via E=hc/λ. ~10 orders of magnitude — log axis required. |
| **Sky coverage** | `sky_coverage_deg2` (existing) | deg² | log | Full sky ≈ 41253. Pointed observatories (ALMA, JWST, HST) have NULL → excluded from this axis (see §9). |
| **Redshift reach** | `z_max` (NEW derived) | dimensionless | log (since CMB→1100) OR linear (default, z_max clamped to 10) | Parsed from `redshift_range`. CMB experiments toggleable (see §9). |
| **Data release year** | `dr_year` (NEW derived) | year | linear | Parsed from `current_data_release`. NULL for `planned` status surveys. |
| **Data volume** | `data_volume_tb` (NEW derived) | TB | log | Parsed from `data_volume` (handles GB/TB/PB/EB; cumulative ≠ per-year is documented limitation). |
| **Limiting magnitude** | `limiting_magnitude` (NEW field) | mag | linear (inverted) | Manual seed for v1; only applies to optical/IR/UV surveys. NULL for radio/X-ray → grayed out when wavelength_band filter excludes those. |
| **Number of sources** | `num_sources_count` (NEW field) | count | log | Manual seed; for survey catalogs that count discrete sources (galaxies, stars, AGN). NULL for time-domain / imaging-only. |

That's **7 axis options**. Either dropdown can pick any; the unused 5 axes inform the tooltip.

---

## 3. Visual encoding

- **Position (X, Y):** the two selected axes.
- **Color:** wavelength_band. Reuse the band labels already in the page (radio / sub_mm / infrared / optical / uv / xray / gamma / astrometric / multi). One distinct color per band; 9 colors is at the edge of distinguishable — use the page's existing `STATUS_COLORS` palette as inspiration, but reserve a clean ColorBrewer "Set1"-like 9-class set in `frontend/src/lib/wavelengthBandColors.ts`.
- **Size:** fixed. Acronym font-size = 12px. No data-driven size. Rationale: the label IS the marker and labels of different sizes are visually confusing for a text-as-glyph plot. (Papa's option-3 mentioned sizing by sky coverage — recommend declining for v1, revisit if Papa wants it.)
- **Opacity by status:** `operational` = 1.0, `commissioning` = 0.85, `planned` = 0.6 (dashed outline if we want extra emphasis), `retired` = 0.5. Reads as "live / coming / future / past" at a glance.
- **Outline (subtle):** 1px stroke around each label same color as fill but darker, so labels remain readable against the dark page background. d3 handles this with `text-shadow: 0 0 3px <bg>`.

---

## 4. Interactions

| Interaction | Behavior |
|---|---|
| **Hover label** | Tooltip card (~280px wide): name + full_name + DR + 1–2 sentence `primary_science_goals` snippet + the 5 axes NOT currently plotted (for context). Tooltip follows cursor with 12px offset, stays inside viewport. |
| **Click label** | Opens a **detail modal in-place** (no full-page navigation). Modal contents: emoji + name + full_name + status pill, wavelength band + wavelength_range, sky_coverage + redshift_range, current_data_release, primary_science_goals (full text, not truncated), instruments list, flagship_programs list, archive_url + mission_url buttons, linked_research_ideas_count with link to `/research-ideas?survey={slug}`, and a "Open full detail page →" link to `/surveys/{slug}` at the bottom for users who want the dedicated page. ESC or backdrop-click closes. Modal URL pushed as `?focus={slug}` so it's shareable; Back button closes the modal. |
| **Hover band-legend chip** | Plot fades all non-matching surveys to 0.15 opacity. |
| **Click band-legend chip** | Toggles filter (chip stays active, plot stays filtered). Click again or click empty chip to clear. |
| **Status pill row** | Below the band legend: 4 chips (operational / commissioning / planned / retired). Same toggle semantics — defaults to all 4 on. |
| **Drag** | Pan within current scale. |
| **Scroll wheel** | Zoom (mouse position is the focal point). |
| **Double-click background** | Reset zoom + pan. |
| **Axis dropdowns change** | Animate transition (~400ms d3 transition) — labels glide to new positions; helps astronomer track which survey moved where. |
| **Keyboard `/`** | Focuses an "Find a survey..." input. Type → matching survey pulses + plot pans/zooms to center on it. |

No selection state — the plot is exploratory, not for picking. Selection lives in the card list (which keeps its existing filter behavior).

---

## 5. Default axes — recommendation

**X = Wavelength (center), log scale**
**Y = Sky coverage (deg²), log scale**

Why: this is the **fundamental survey tradeoff plot**. Astronomers internalize surveys as "what part of the EM spectrum × how much sky." Plotting these two reveals the natural clusters (all-sky radio surveys top-left, pointed JWST/HST bottom-right) and the gaps (almost nothing at very high sky-coverage in the X-ray regime except eROSITA & ROSAT). Z-max and DR year are secondary explorations.

Color = wavelength_band (gives X-axis an immediate sanity check — bands should sort along X).
Status = all 4 on.

---

## 6. Layout — where on /surveys?

The /surveys landing IS the Explorer. Card list is a secondary mode reached via toggle.

```
┌────────────────────────────────────────────────────────────────────────────┐
│  Astronomical Surveys Directory                                            │
│  50 surveys catalogued — …                                                 │
│                                                                            │
│  ┌──────────────┬──────────┐                                               │
│  │  Explorer ●  │   List   │   ← Explorer/List toggle                      │
│  └──────────────┴──────────┘                                               │
├──────────────────┬─────────────────────────────────────────┬───────────────┤
│ ◉ All Surveys    │  [X axis ▼]  [Y axis ▼]                 │  Info         │
│ ─────────────    │                                         │  ─────        │
│ 📻 Radio (7)     │  ┌───────────────────────────────────┐  │  (hover any   │
│ 〰️ Sub-mm (5)    │  │                                   │  │   acronym)    │
│ 🌡️ Infrared (7)  │  │   Plot A                          │  │               │
│ 🔵 Optical (17)  │  │   wavelength × sky coverage       │  │   full_name   │
│ 💜 UV (1)        │  │                                   │  │   DR          │
│ ⚡ X-ray (6)     │  │                                   │  │   λ range     │
│ ☢️ Gamma (1)     │  └───────────────────────────────────┘  │   sky cov.    │
│ 🔭 Multi (6)     │                                         │   archive 🔗  │
│ ─────────────    │  ┌───────────────────────────────────┐  │   science     │
│ Status:          │  │                                   │  │     goals     │
│  ☑ Operational   │  │   Plot B                          │  │     (~3 ln)   │
│  ☑ Commissioning │  │   num_sources × limiting_mag      │  │               │
│  ☑ Planned       │  │   (dims non-band, doesn't hide)   │  │               │
│  ☐ Retired       │  └───────────────────────────────────┘  │               │
│ ─────────────    │                                         │               │
│ Operator: [▼]    │  Showing N of 50 surveys                │               │
└──────────────────┴─────────────────────────────────────────┴───────────────┘
   ~220px              ~720px center                          ~280px
```

**Sidebar behavior:**
- The band rows + `[All Surveys]` form a **single-select radio group** (only one active). Click `📻 Radio` → both plots filter to the 7 radio surveys, Plot A axes switch to `frequency_ghz (log) × sky_coverage_deg2 (log)`. Click `[All Surveys]` to return to the full landscape.
- Status checkboxes (`☑ Operational ☑ Commissioning ☑ Planned ☐ Retired`) and Operator (multi-select dropdown) are **AND-applied** on top of the band selection — these are filters, not navigation.
- Counts in parentheses are **static live counts** (always 7/5/7/17/1/6/1/6), not filtered counts. Reflects the directory size; reassures the user that selecting Gamma will only show 1 survey.
- Active band row gets a left-border accent + background tint. Hover state: row gets a subtle tint, no count change.

- **Default = Explorer**, with sidebar selection = **All Surveys**. Full landscape — every survey visible.
- Toggle persists in URL: `/surveys` (or `?view=explorer`) = Explorer, `?view=list` = List view.
- **Sidebar band selection persists in URL:** `?band=optical`, `?band=radio`, etc. Default omitted = All. Change uses `router.replace` so back-button navigates band history.
- Local state in React `useSearchParams` + `router.replace` — no full reload.
- The two views share the *same* `surveys` state array. Switching is instant after first fetch.
- Explorer view has its own controls row (axis selectors for Plot A + band legend + status pills + "Find a survey..." input). The List view keeps its current search/filter row.

**Why default to Explorer?** Papa's directive: comprehension is the point. The card list at 49 rows is hard to scan; the Explorer makes survey relationships visible at a glance. List view is preserved for accessibility and for the use-case "I just want to scroll through them."

**Mobile note:** Viewports <800px force List view (Explorer toggle disabled with a "View on desktop for Explorer" hint). 49 labels at <800px is unreadable; saves us a tedious mobile-scatter implementation.

**Deep-link compatibility:** `/surveys/{slug}` (the detail-page route) is untouched — still exists, still works, still linked from the modal's "Open full detail page →". Outside-the-explorer links Papa or anyone else has shared continue to land on the per-survey page.

---

## 7. Tech stack — recommendation

**D3 (already installed).** `d3` ^7.9.0 + `@types/d3` ^7.4.3 are in `frontend/package.json` already (but unused — `grep -rln "from 'd3'" frontend/src` = empty). This is the lowest-friction path.

Why not Recharts:
- Recharts isn't in deps; adding it = +130KB and a new dependency to maintain.
- Recharts is declarative and assumes axis types are stable — switching scale type at runtime (linear ↔ log) is awkward in its props model.
- Animated axis swaps look bad in Recharts; d3 transitions are the right primitive.

Why not Plotly / Observable Plot / visx:
- Plotly: heavy (~3MB), great for engineers, the d3 work here is shallow enough not to need it.
- Observable Plot: nice API, but requires importing `@observablehq/plot` (+~150KB) when we already have raw d3.
- visx: thin wrapper on d3, would still need us to write the label-collision avoidance.

What we'll actually use from d3:
- `d3-scale` (scaleLinear, scaleLog, scaleOrdinal)
- `d3-axis` (axisBottom, axisLeft)
- `d3-zoom` (pan + zoom)
- `d3-transition` (animated axis change)
- `d3-selection` (DOM updates)
- Maybe `d3-force` for label-collision repulsion if overplotting is bad (see §11).

Implementation: a single client component `frontend/src/app/surveys/SurveyExplorer.tsx` (~400 LoC), no SSR. Refs into a `<svg>` element; React owns the controls, d3 owns the SVG mutations inside a `useEffect`. Standard pattern.

---

## 8. New DB fields needed

Six new columns on `surveys`:

| Column | Type | Source | Maintenance |
|---|---|---|---|
| `wavelength_center_um` | `NUMERIC(12,6)` nullable | DERIVED from `wavelength_range` | Auto: parser on insert/update; one-shot backfill |
| `z_max` | `NUMERIC(6,2)` nullable | DERIVED from `redshift_range` | Auto |
| `dr_year` | `SMALLINT` nullable | DERIVED from `current_data_release` | Auto + Mima refresh on `EVENT_DR_REFRESH` |
| `data_volume_tb` | `NUMERIC(12,3)` nullable | DERIVED from `data_volume` | Auto |
| `limiting_magnitude` | `NUMERIC(5,2)` nullable | NEW manual field | Mima FieldPatch from operator/mission page |
| `num_sources_count` | `BIGINT` nullable | NEW manual field | Mima FieldPatch from DR paper/page |

**Derive vs. add: the call.** All 6 are added as columns rather than computed in the API. Three reasons:
1. Parsing edge cases get committed and reviewable — bad parses surface in dashboard and Mima audits, not in transient API responses.
2. The autowiki_surveys loop already has FieldPatch infrastructure for editing typed fields (`survey_revisions` table). Numeric fields ride that exact pipeline.
3. Indexable/sortable — keeps the door open for `?sort=-z_max` later without recomputation.

**Backfill strategy.** A Python parser (`scripts/parse_survey_numeric_fields.py` on Mac Studio) runs once after the migration lands; populates all 4 derived columns from the existing string fields. Targeted regexes per column; documented test fixtures for the corner cases (CMB experiments, log z ranges, "ongoing" DRs). For `limiting_magnitude` and `num_sources_count`, the script populates from a hand-curated `scripts/seed_extra_fields.json` (Kun writes during pilot — ~3h work, 49 rows × ~30s each).

**Auto-refresh on edit.** Add a SQLAlchemy event listener on `Survey.__table__` `before_update`: if `wavelength_range` / `redshift_range` / `current_data_release` / `data_volume` changed, re-run their corresponding parser into the derived column. Implemented in `app/models/survey.py` next to the model definition.

---

## 9. API changes

**Option A (recommended):** Extend `GET /api/surveys` — add the 6 new fields to `_survey_row_to_dict` (line 12 of `app/routers/surveys.py`). Payload size delta: ~+90 bytes per survey × 49 = ~4.4 KB extra. Currently the response is ~80 KB; this is a 5% bump. Single endpoint, single fetch, no client cache invalidation games.

**Option B (rejected):** New `GET /api/surveys/explorer` endpoint with only numeric fields. Saves ~50 KB but doubles the fetch surface for what is effectively the same data. Reject unless payload bloats past 200 KB later.

**Detail-page endpoint** (`GET /api/surveys/{slug}`) — same extension, returns the derived fields too (tooltip can use the live numeric, not have to re-parse).

**Explorer-specific filtering:** None at the API level. The Explorer fetches the same list; React filters client-side on band/status. 49 surveys × 9 fields fits in 80 KB easily.

---

## 10. Platoon assignment

Per `feedback_platoon_assignment.md`: every step that involves model judgment or recurring work names its owner.

| Step | Member | Host | Why |
|---|---|---|---|
| 10.1 One-shot parser to backfill 4 derived numeric fields | **Pure Python** (regex + unit conversions) | Mac Studio | Deterministic — no model needed. Edge cases captured as test cases in `tests/test_survey_parsers.py`. Cost: 0. Speed: <5s for 49 rows. |
| 10.2 One-shot seed of `limiting_magnitude` + `num_sources_count` (49 rows × 2 fields) — **load-bearing for Plot B** | **Mima** (`qwen3:30b`) — supervised by Kun for first pass | Mac Studio | Pattern-recognition over operator/mission pages + DR papers. Kun reviews the 98 values before commit; subsequent updates flow through Mima FieldPatch in the autowiki_surveys loop. Cost: free. Speed: ~30s per value × 98 ≈ 50 min batched. **Priority: seed these before Plot B ships** — otherwise the bottom plot is mostly empty. |
| 10.3 Per-edit re-parse hook (when `wavelength_range` / `redshift_range` / `current_data_release` / `data_volume` is updated) | **Pure Python** SQLAlchemy event listener | Studio | Deterministic. Cost: 0. |
| 10.4 `dr_year` refresh when `EVENT_DR_REFRESH` fires from news-curator | **Mima** — already runs at KST 01:00 | Studio | Reuses existing autowiki_surveys_v1.md §5.11 trigger. New `dr_year` column auto-updates as part of the DR string edit. Cost: free. |
| 10.5 Routine `limiting_magnitude` / `num_sources_count` re-check (quarterly) | **Mima** FieldPatch via WEEKLY_AUDIT in autowiki_surveys_v1.md §4.2 | Studio | Fits into existing tick cadence; no new beat needed. Mima proposes, Atom-7B verifies, Python validator gates. Cost: free. |
| 10.6 Plot UI itself (no model loop — pure frontend) | **Tori** (implementation) | n/a | One client component, ~400 LoC, hooks into existing /surveys page. No model judgment at runtime. |
| 10.7 Quarterly audit: "is the Explorer still useful? Are the right axes the default? Did Mima introduce bad numeric values?" | **Kun (Claude Opus)** — quarterly | cloud | Cross-cutting design review. Compares plot vs. card-list engagement (analytics — out of scope for v1). |

**Net new resident model load:** zero. Every step rides existing platoon members on existing hardware.

---

## 11. Risks & mitigations

| Risk | Likelihood | Mitigation |
|---|:-:|---|
| **Label overplot** — multiple surveys at near-identical positions (e.g. several optical wide-field surveys) | High in default view | (a) Status opacity tiering already separates active from retired; (b) implement light label-collision avoidance: priority by status (operational stays put, retired nudged outward) using d3-force simulation, capped at 50ms. If too jittery, fall back to "show only top-1 by status, others on hover." |
| **Parser misreads `wavelength_range`** for compound strings (e.g. "0.55–1.85 μm + 0.92–2.0 μm slitless") | Medium | Parser takes the *envelope* (min low → max high); if envelope spans >2 decades, mark `wavelength_center_um=NULL` and surface in autowiki dashboard for Mima FieldPatch. |
| **Pointed observatories have NULL `sky_coverage_deg2`** (ALMA, JWST, HST, ELT, VLA, …) | By design | Y=sky_coverage axis excludes them with a "+N pointed observatories not shown on this axis" footnote-chip below the plot. Other Y-axes (e.g. wavelength) include them normally. |
| **CMB experiments compress the z-axis** (z≈1100) | Medium | z_max axis uses log by default; status legend lets the user mute `retired` (hides Planck) or `sub_mm` band (hides CMB-S4/SPT/ACT). |
| **Acronym collisions** — e.g. `2MASS` and `Pan-STARRS` are long | Low | Cap label at 10 chars (truncate with ellipsis); full name in tooltip. Most acronyms are already short. |
| **Color-blindness on 9-band palette** | Medium | Use a known CB-safe Set1/Paired hybrid; keep saturation high. Provide a "Color by status instead" toggle in v1.1 if Papa hears feedback. |
| **Page weight regression** | Low | d3 tree-shaken to ~30KB gzipped (only the modules we use). No new heavy deps. Plot only loads when `?view=explorer` (lazy-import via `next/dynamic`). |
| **Lonely band rows** — UV / Gamma have 1 survey each | Low (data fact, not bug) | When user selects them, show the single survey with a contextual note: "Only 1 survey is currently catalogued in this band. Click `All Surveys` for full context." Don't hide the row — the row's count `(1)` and the row itself signal what they'll see. |
| **Band-specific axis unit confusion** — user picks a band, axes change units, user is surprised | Medium | Sidebar selection animates the axis swap (~400ms d3 transition) AND shows a small "Showing: GHz (radio convention)" caption under the axis on non-All bands. Caption disappears on All Surveys. |
| **Bad seed for `limiting_magnitude` / `num_sources_count`** (Mima hallucinates) | Medium | Kun reviews the 98 seed values before commit; source URL recorded for each value in `survey_revisions` (already exists). Bad values → autowiki rollback path. |

---

## 12. Acceptance criteria for v1

- [ ] Migration adds 6 columns to `surveys`; downgrade reverses cleanly.
- [ ] Parser script populates 4 derived columns for all 49 surveys; <2 NULLs per column (justified — pointed obs, planned status, etc.).
- [ ] Seed of `limiting_magnitude` populated for all optical/IR/UV operational+commissioning surveys (~25 rows); `num_sources_count` for all catalog-producing surveys (~30 rows).
- [ ] `GET /api/surveys` returns the new fields.
- [ ] `/surveys` page renders the Explorer/List toggle; **Explorer is default**; `?view=list` deep-links work; `/surveys/{slug}` detail page still works.
- [ ] Explorer renders **two stacked d3 scatters** with acronym labels for all 49 surveys (excluding NULLs on chosen axes with footnote-chip).
- [ ] **Left sidebar = primary band navigator**: `[All Surveys]` + 8 single-select band rows with live counts (📻 Radio (7) / 〰️ Sub-mm (5) / 🌡️ Infrared (7) / 🔵 Optical (17) / 💜 UV (1) / ⚡ X-ray (6) / ☢️ Gamma (1) / 🔭 Multi (6)). Default = All Surveys; `?band=<slug>` persists. **No top tabs.**
- [ ] Band selection triggers Plot A axis defaults per §1.6 (radio → GHz, X-ray → keV, etc.) with a "Showing: <unit> (<convention>)" caption under the axis.
- [ ] Plot A default (All Surveys): wavelength_center_um (log) × sky_coverage_deg2 (log), axes user-selectable, color by band, all statuses visible.
- [ ] Plot B fixed: num_sources_count (log) × limiting_magnitude (linear, inverted), color by band; non-band surveys fade to 0.15 opacity when a band is selected in the sidebar (dim, don't hide).
- [ ] Axis dropdowns on Plot A (7 options each) work; scale switches (linear ↔ log) where appropriate.
- [ ] Hover tooltip shows name + full_name + DR + science goal snippet + 5 unplotted axis values.
- [ ] Click opens **detail modal in-place** with full specs + "Open full detail page →" link. `?focus={slug}` is pushed; ESC/backdrop/Back closes.
- [ ] Band-legend and status-pill toggles filter the plot.
- [ ] Pan + zoom + double-click-reset works; axis-change animation is smooth (<500ms, no FOUC).
- [ ] Mobile (<800px) renders List only; Explorer toggle hidden with a "View on desktop for Explorer" note.
- [ ] Lighthouse perf delta: ≤5 points on Performance on /surveys page (lazy-load d3 keeps initial JS budget intact).

---

## 13. Out of scope for v1 (future work)

- **Sizing by a third numeric axis** (Papa's option-3) — defer; readability of acronym labels at varying sizes is unclear, want user feedback first.
- **Time-slider** (animate the plot across DR years to show survey-landscape evolution) — natural v1.5 add once `dr_year` data quality is proven.
- **Trail / "where did this survey come from"** linking SDSS → SDSS-V or DES → Rubin-LSST as small connecting strokes — needs a `lineage` relation column on `surveys`, out of scope.
- **Annotations** ("the JWST notch", "the CMB cluster") — pure CSS labels, but each one is a maintenance burden; ship without and let astronomers see the structure themselves.
- **Per-band drilldown** — clicking a band-legend chip could open a sub-plot of just that band with finer axes (e.g. radio sub-bands). Defer; v1 single plot is enough surface.
- **Tooltip with embedded mini-images / preview** (survey mission patch / first-light image) — needs an image-store column; tasteful but expensive. Defer.

---

## §TODO — Density expansion options (partially promoted)

**Update 2026-05-13 (Papa):** Filter sidebar + info panel **promoted to v1.1 sprint scope** (ship alongside v1, not deferred). Remaining 4 options stay deferred. Implementation notes sent to Tori directly; no separate spec doc.

Papa asked whether we should add more density to the Explorer. Options on the table, ranked by Kun's estimate of effort vs payoff:

| Option | Status | Effort | Payoff | Notes |
|---|---|:-:|:-:|---|
| **Persistent left sidebar — primary band navigator + status/operator filters** (single-select band list w/ live counts, status checkboxes, operator multi-select, sticky on scroll, instant cross-plot filter) | ✅ **v1.1 sprint** (v1.3 redesigned — band is now navigation not filter) | Low | High | Sidebar OWNS band selection (single-select, like tabs). Status + Operator remain multi-select filters, AND-applied on top of band. Replaces both the v1.2 top band tabs (removed) and the v1.1 band-checkbox sidebar (removed) with one unified navigator. |
| **Persistent right info panel** (hover acronym → specs appear in column to the right; click still opens modal) | ✅ **v1.1 sprint** | Medium | High | Per Papa 2026-05-13: hover preview, no click required. Modal remains for "stay on this survey" interactions. Both coexist. |
| **Parallel coordinates plot as Plot C** (all 7 numeric axes on one chart, one polyline per survey, color by band) | ⏸ Deferred | Medium | Medium | Powerful for spotting outliers across all dims at once; but 49 polylines is right at the readability ceiling. Filter sidebar (now v1.1) would help when this lands later. |
| **All-sky map (Aitoff projection) as Plot C** (each survey footprint drawn at its sky_coverage, color by band, hover = same tooltip) | ⏸ Deferred | High | Medium-High | Visually striking and astronomer-native. But footprint geometry isn't in the schema — we have only `sky_coverage_deg2` (a scalar) and the descriptive `sky_coverage_note`. Would need a new column with simplified polygon JSON or center-RA/Dec + extent. Real work; ship in v1.3 if Papa wants it. |
| **Density histogram strip below each axis** (mini-histograms showing how many surveys are at each X / Y range) | ⏸ Deferred | Low | Low-Medium | Cheap d3 addition. Useful for "where are the gaps?" — survey landscape visualization. |
| **Selected-survey lasso** (drag to select multiple acronyms → list view on the side shows their specs side-by-side) | ⏸ Deferred | High | High | Compare-3-surveys workflow. Probably worth its own design pass before implementing. |

**v1.1 sprint scope locked:** left filter sidebar + right info panel. Implementation notes sent to Tori directly via HwaO.

---

## Appendix A — Parser rules (informative, for Tori)

**`wavelength_center_um`** from `wavelength_range`:
1. Match `(\d+\.?\d*)\s*[–\-]\s*(\d+\.?\d*)\s*(μm|nm|mm|cm|GHz|MHz|keV|MeV|GeV|TeV)`.
2. Convert both endpoints to μm:
   - nm → ×1e-3, mm → ×1e3, cm → ×1e4
   - GHz: λ_μm = 299792.458 / freq_GHz
   - MHz: λ_μm = 299792458 / freq_MHz
   - keV/MeV/GeV/TeV: λ_μm = 1.2398 / energy_keV (and unit scale)
3. Center = geometric mean (sqrt(low × high)) — appropriate for log axis.
4. Failure → NULL, log to `parse_failures` table for Mima review.

**`z_max`** from `redshift_range`:
1. Match `z\s*[=≈~]\s*\d+\.?\d*\s*[–\-]\s*(\d+\.?\d*)` → z_max = group 1.
2. CMB phrases ("z ≈ 1100", "CMB surface") → z_max = 1100.
3. Stellar / RV-only phrases ("Milky Way stars", "Galactic stars (RV km/s)") → NULL.
4. Failure → NULL.

**`dr_year`** from `current_data_release`:
1. First match of `(19|20)\d{2}` → that year.
2. "No data yet" / "underconstruction" → NULL.
3. Range "(2024–2025)" → take latter year.

**`data_volume_tb`** from `data_volume`:
1. Match first `~?(\d+\.?\d*)\s*(GB|TB|PB|EB)` → numeric × {1e-3, 1, 1e3, 1e6} respectively.
2. Prefer "raw" or "release" mentions over "per night" / "per year" if both appear.
3. Failure → NULL.

All four parsers are pure functions, easy to unit-test. `tests/test_survey_parsers.py` has one case per current value + 3 known-tricky strings (CMB-S4, JWST-multi-instrument, ELT-planned).
