# Pace-statistic contract v1 — frozen BEFORE the forecast (design-v2 F1 law)

Authored: Hwao, 2026-08-04 ~22:3x KST. Status: DRAFT until Kun's review approves; FROZEN (sha'd,
chmod 444) immediately on approval — every downstream artifact (forecast, prediction entries,
T3 script) consumes THIS and may not redefine any element.

## 1. Magnitude frame
- Rest-frame UV absolute magnitude at **1500 Å**, AB system. Per-catalog conversions from other
  conventions (1450/1600 Å) applied via the chain-disclosure conversion field; a catalog whose
  UV convention cannot be determined is census-only (Class-X-by-rule).

## 2. Bright-end definition (fixed thresholds, chosen for map-dispersion contrast)
- **Primary cut: M_UV ≤ −20.0.** Secondary robustness cut: **M_UV ≤ −21.0** (reported alongside,
  never substituted). Cumulative number density n(< M_cut) per slice — cumulative, not per-bin
  φ, to reduce binning freedom.

## 3. Redshift slices (fixed edges)
- **[8.0, 9.0), [9.0, 10.0), [10.0, 11.5), [11.5, 14.0)** — Δz widens where photo-z scatter and
  count thinness grow. Slice midpoints for pace pairs: 8.5, 9.5, 10.75, 12.75.
- z ≥ 14 objects: candidate-population lane only (A7-style discipline), never in the pace.

## 4. The pace statistic (functional form, fixed)
- **Per catalog**: pace_k = Δlog10 n(<M_cut) / Δz between adjacent slice midpoints (three pace
  values per catalog per cut where populated).
- **Summary within catalog**: weighted linear fit of log10 n vs z across populated slices; the
  fitted slope is the catalog's pace; per-pair values reported alongside.
- **Cross-catalog merged pace**: SECONDARY, labelled, computed only where the F2 seam test
  passes (overlap-slice densities consistent within combined declared uncertainties); never
  silently averaged.

## 5. Uncertainty model (both terms, always)
- **Poisson term**: bootstrap over the object list within catalog/slice (seed 20260804, 2000
  resamples).
- **Cosmic-variance term (structural, never bootstrap-estimated)**: per catalog/slice from the
  cited recipe — **Trenti & Stiavelli (2008) cosmic-variance methodology as implemented in the
  Moster et al. (2011) prescription** (σ_CV as a function of survey area, Δz, mean density).
  The recipe is NAMED here; its numeric instantiation happens ONCE in the forecast, using T1's
  manifest areas, and is FROZEN there — never recomputed smaller after any result exists.
- Adjacent-pace covariance from photo-z scatter: per catalog, the published σ_z (chain field)
  propagated as a stated correlated-systematic band on pace pairs; reported, never absorbed.

## 5b. Frozen clauses from Kun's contract review (C1–C6, verbatim intent)
- **C1**: a slice is populated at N≥1; an N=0 slice enters the fit as an upper limit at the
  84% one-sided Poisson confidence (Gehrels 1986, N<1 equivalent), never silently dropped.
- **C2**: σ_CV's density input is the forecast's EXPECTED density per slice; realized densities
  never re-enter the CV term, in either direction.
- **C3**: ⊕ means addition in quadrature; the tension test is two-sided; the sign of every pace
  difference is always reported.
- **C4**: the photo-z band is instantiated ONCE, in the forecast artifact (same site as the CV
  term), via analytic slice-migration from each catalog's published σ_z; frozen before T3.
- **C5**: the §4 fit is inverse-variance weighted with the frozen combined term (Poisson ⊕ CV)
  as the weight — the weight definition cannot be tuned to data.
- **C6**: rest-UV conversions are catalog-published or ONE frozen lane rule named at T2 before
  any density is computed; a catalog with neither is census-only (Class-X discipline extended).

## 6. Verdict rule (T2b-style, fixed)
- A pace difference from a prediction is **in-tension** only if it exceeds
  max(2 × combined[Poisson ⊕ CV ⊕ photo-z band], the prediction's own stated uncertainty);
  otherwise **consistent**. Non-confrontable states (not-numeric-in-frame, frame-mismatch,
  seam-fail, census-only) are verdicts, never defaults.
- Honest-null template: "at the frozen thresholds/slices, paces steeper than X (units: dex/Δz)
  are excluded per catalog; the census cannot distinguish models within ±Y" — X, Y from the
  frozen forecast.
