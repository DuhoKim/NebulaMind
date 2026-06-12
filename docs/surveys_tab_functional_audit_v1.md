# Surveys Tab — Functional Audit v1

**Author:** Kun · **Date:** 2026-06-12 · **Status:** audit + fix design, for Papa review then Tori implementation
**Scope (per HwaO brief, corrected):** does the Surveys tab do its core job — browse, filter, compare surveys — cleanly? Priority: Explorer correctness, plot usefulness, data surfacing. Mobile framing explicitly out of scope (Papa is on Chrome desktop). Fix/redesign what's broken before adding anything new.

All findings verified against the live system on 2026-06-12: prod DB (50 `surveys` rows), live API (`/api/surveys`, 200, all numeric fields present), deployed build (BUILD_ID 2026-06-12 15:40, newer than all survey source mtimes → deployed = source read here).

---

## 1. Verdict

The architecture is sound and the bones are good: numeric plot columns in the DB (no more regex-parsing display strings — the old `SurveyExplorer.tsx` that did that is dead code), a clean API, reducer-based filter state with URL sync, linked-hover across two plots, and a solid detail page. **But the default landing view silently shows only 19 of 50 surveys**, and several plot/filter defaults are tuned for the wrong subset of the data. The tab *browses* adequately, *filters* adequately, and *compares* poorly on first load. Nothing needs a rebuild; it needs five targeted fixes (§3) and one deliberate product decision (§3-F2).

---

## 2. What works (keep)

- **Data model**: `wavelength_center_um / z_max / dr_year / data_volume_tb / limiting_magnitude / num_sources_count` are first-class numeric columns; coverage is decent (50/49/42/48/30/39 of 50). Unit conversions in `wavelengthUnits.ts` are physically correct (c = 299792.458 μm·GHz; hc = 1.2398 eV·μm).
- **State design** (`SurveysView.tsx`): reducer + URL sync of durable filter state only (transient hover correctly excluded), debounced hover→focus, band counts derived from status/operator-filtered set. Good engineering.
- **PlotB's missing-data chip** — an expandable "+N surveys not shown" footnote naming the missing surveys. This is the right honesty pattern; PlotA lacks it (F1).
- **Detail page** (`/surveys/[slug]`): parameter table always renders all rows with "—" for nulls (honest), formatters are correct (keV/MeV conversion, source-count humanization), linked research ideas + related wiki pages wired to real joins.
- **Backend** (`routers/surveys.py`): straightforward, parameterized SQL, returns everything the frontend needs in one call. Client-side filtering of 50 rows is the right call; no pagination needed.

---

## 3. Findings — broken or misleading (P0)

### F1 — Default landing plot silently drops 31 of 50 surveys
Default axes are `sky_coverage_deg2` × `dr_year`; default statuses exclude `retired`. Only **19 surveys** satisfy all three conditions. The drops are silent: PlotA has no missing-data indicator, and the "N surveys" label shows the *filter* count, not the *plotted* count.

Worse, the missing set is precisely the marquee facilities: **HST, JWST, ALMA, Chandra, XMM-Newton, VLA, MeerKAT, SDSS-V, Roman, ELT, SKA** all have NULL `sky_coverage_deg2` (they are pointed observatories — the NULL is semantically correct) and/or NULL `dr_year`. A first-time visitor sees a scatter plot of the Surveys universe with no JWST in it.

**Fix (three parts):**
1. Change default axes to `wavelength_center_um` (X, log — 50/50 coverage) × `z_max` (Y — 49/50 coverage). 49 of 50 surveys plot on landing (only PFS-like rows missing z drop). This is also the scientifically natural "where does each survey live" map.
2. Add PlotA the same missing-data chip PlotB already has ("+N not shown", expandable list). One component, reuse it in both.
3. Change the count label to "M plotted · N matching filters" when M < N.

### F2 — `retired` excluded by default hides 16 archival workhorses
Default status checkboxes are operational/commissioning/planned. The 16 hidden surveys include **2MASS, GALEX, Planck, DES, KiDS, GAMA, DEEP2, zCOSMOS, VIPERS, UKIDSS, ROSAT** — *finished* surveys whose final data releases are among the most-cited datasets in astronomy. In Papa's own field, DESI BGS environment work is benchmarked against GAMA/SDSS-era catalogs constantly. Survey data does not retire when the facility does.

**Fix:** include `retired` in `DEFAULT_STATUSES`. Optionally relabel the UI string "Retired" → "Completed (archival)" — `retired` as a DB value can stay. This is a product call for Papa, but my recommendation is firm: a directory that anchors research should default to showing completed surveys.

### F3 — Redshift axis is destroyed by CMB experiments
`z_max` is linear in `AXIS_OPTIONS`. Four surveys (Planck, ACT, SPT, CMB-S4) carry z_max = 1100 (recombination). On a linear axis every galaxy survey (z ≤ 27, mostly ≤ 7) is crushed into the leftmost ~2% of the plot. The axis is useless whenever any CMB survey passes the filter — which on landing (post-F2) is always.

**Fix:** make `z_max` log-scale. Verified: min positive z_max = 0.04, no zeros/negatives in current data → log domain [≈0.02, 2200] works and spreads galaxy surveys across ~3 decades while keeping CMB points honestly placed. Guard: if a future row has z_max ≤ 0, drop it from the log axis via the existing null-filter path (and it then shows in the F1 missing chip).

### F4 — PlotB is a ghost plot for half the bands
PlotB is fixed at `num_sources_count` × `limiting_magnitude`. Limiting *magnitude* is an optical/IR/UV concept; all radio (7), sub_mm (5), X-ray (6), and gamma (1) surveys have NULL `limiting_magnitude` — correctly. So selecting Radio/Sub-mm/X-ray/Gamma in the band filter leaves PlotB with **zero active points**: every dot dims to 0.15 opacity and the plot conveys nothing for that band.

**Fix (minimal, honest):** when the active band has 0 points with both fields, replace PlotB's plot area with a one-line explanation: "Limiting magnitude is not defined for {band} surveys (flux-density limited)" + the existing missing chip. Do **not** invent a depth proxy per band in this pass — that's new scope, and per the brief we fix before we add. (A per-band sensitivity axis — μJy for radio, erg/s/cm² for X-ray — is a defensible v2; it needs new columns and seeding, so park it.)

### F5 — PlotA renders all ~50 labels unconditionally → clutter
Every point always draws its name at a fixed offset (`x+9`). With 35–49 points and clustered regions (optical surveys bunch at 0.5–1 μm; post-F3 the z axis spreads but wavelength clusters remain), labels overlap into illegibility. PlotB already does this right: label on hover only.

**Fix:** label on hover always; persistent labels only when the plotted count ≤ ~15 (i.e., after band filtering), else suppress. Cheap, no collision-detection library needed.

---

## 4. Findings — quality/correctness, fix opportunistically (P1)

- **P1-a · Dead code:** `src/components/SurveyExplorer.tsx` (555 lines, the old regex-parser explorer) is imported by nothing. Delete it. Its parsers are superseded by the DB numeric columns.
- **P1-b · Interface lies:** `Survey` interface in `SurveysView.tsx` declares `id` and `quality_score`, but `_survey_row_to_dict` returns neither. Nothing consumes them today. Either trim the interface (preferred) or return the fields. Same for `SurveyDetailClient`'s unused fields if any after trim.
- **P1-c · In-place mutation:** `SurveysView.tsx:198` — `state.checkedStatuses.sort()` mutates reducer state during the URL-sync comparison. Use `[...state.checkedStatuses].sort()`. Latent re-render footgun, not a live bug.
- **P1-d · No name search:** backend supports `?q=` but the UI has no search box. With 50 surveys a client-side name/full_name substring filter in the sidebar is ~20 lines and meaningfully improves *browse*. (This is the one "addition" I'd allow in this pass; it serves the basic-functionality goal directly.)
- **P1-e · Tab naming:** page is titled "Astronomical Surveys Directory"; the two view tabs are "Explorer" and "Directory". A directory inside a directory. Rename the list tab "List".
- **P1-f · Data backfill (one-shot, manual):** `num_sources_count` missing for 11 (incl. ALMA, SKA, ngVLA — fine, no catalogs yet; but ASKAP/EMU=250k exists so check stragglers), `dr_year` missing for 8 (mostly `planned` — correct), `limiting_magnitude` missing for 2 multi-band surveys that plausibly have one (check Euclid/Rubin rows). Kun can do a seeding pass; not blocking any fix above.
- **P1-g · Facility-vs-survey tension (note, no action):** HST/JWST/ALMA/VLA/Chandra/ELT are observatories, not surveys; their per-row "sky coverage" and "limiting magnitude" are program-dependent. The NULLs are the honest encoding. Post-F1 defaults stop punishing them. A `kind: survey|observatory` column is a v2 consideration only.

---

## 5. Explicitly out of scope (per corrected brief)

- Mobile/responsive work (the `isMobile` Explorer lockout stays as-is).
- New visualizations, compare-table features, per-band sensitivity axes (§3-F4 v2 note).
- The git-custody problem (all survey code is untracked — `?? frontend/src/app/surveys/`, `?? backend/app/routers/surveys.py`) is real but owned by the strategic-evaluation P1 git-custody track, not this audit.

## 6. Implementation order for Tori

1. **F1 + F3 together** (default axes + log z + missing chip + count label) — one PR, the landing-view fix. Acceptance: fresh `/surveys` load plots ≥ 48 of 50 with `retired` included (after F2), JWST/HST visible, CMB points at top of log z axis, chip lists the ≤2 hidden.
2. **F2** (DEFAULT_STATUSES + label) — one-line + copy change, needs Papa's nod (§3-F2).
3. **F4 + F5** (PlotB empty-band message; label policy) — small, independent.
4. **P1-a/b/c/e** sweep — cleanup PR.
5. **P1-d** search box.
6. **P1-f** data seeding (Kun, manual; no platoon/model jobs involved — this is all static frontend + one-shot seed; no Platoon Assignment section required).

Each step needs `npm run build` + redeploy (`next start` serves a static build — fixes are invisible until rebuild+restart; verified BUILD_ID practice from the rendering-overhaul track applies here too).

## 7. Acceptance test (behavioral)

Papa opens `/surveys` cold on Chrome desktop and, without touching any control: sees ≥48 surveys on the map including JWST/HST/Planck/2MASS, can read the z–λ landscape at a glance, hovers any point and gets the info panel, clicks through to a detail page with a complete parameter table. Then filters to Radio and gets a meaningful PlotA plus an honest explanation (not a ghost plot) for PlotB.
