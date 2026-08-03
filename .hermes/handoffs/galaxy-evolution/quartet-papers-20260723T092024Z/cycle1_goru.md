# Cycle 1 — Goru (rigor lane): non-circularity + defensible-conclusion audit

Two axes judged per paper. Read the full manuscript bodies (PDFs) + referee logs. Adversarial; no praise.

### 1. z9–10 unlensed metallicity deficit
- **Non-circularity:** clean — the deficit is a genuine differential (independent high-z Te abundances vs a local anchor); the anchor is used as an anchor, not relabeled as the result. Robustness is demonstrated, not asserted: swapping Curti+20↔Andrews&Martini13 moves it 0.04 dex, and an independent ~1500-gal Isobe stack reproduces it via a different method. Shared Te zero-point is the only common calibration, and it is explicitly carried as a 0.15 dex floor.
- **Conclusion defensible?** yes — deflates its own formal ~22σ to ~4.5σ effective, states "not a detection," reports sign-robust / magnitude-systematic-limited. Textbook discipline.
- **The one fix:** grow the strictly-unlensed *z≈9–10-specific* individual-Te sample beyond N=5–6 (GN-z11 makes 6); the headline z9–10 value still rests on a handful of points — Isobe confirms z=4–10, not z9–10.

### 2. reionization f_esc photon-budget landscape
- **Non-circularity:** clean — it is a designed sensitivity analysis; no data are fit and then tested. The O32-only vs β-only swap is an explicit non-circularity check and leaves the verdict unchanged.
- **Conclusion defensible?** yes — "the crisis is a restatement of the adopted ξion/SFRD priors" is exactly what the corner-grid demonstrates (crisis-onset moves 3.5 redshift units); it refuses to favour either literature camp. No overclaim.
- **The one fix:** this is a re-quantified known degeneracy with no new discriminating datum — add one genuinely new constraint (e.g. a direct high-z ξion anchor) so the paper narrows the envelope rather than only mapping it; on rigor it passes, on originality it is thin.

### 3. galaxy scaling relations z0→JWST
- **Non-circularity:** at-risk — the metallicity offset is a legitimate differential, BUT the SFMS "elevation" (+0.8→+1.9 dex) is largely produced by the emission-line selection that biases the high-z samples toward high-sSFR; the paper concedes this inflates it. Input selection ≈ output signal. (Choosing PP04 O3N2 to match the high-z scale is defensible scale-matching, not the circularity problem here.)
- **Conclusion defensible?** overclaims — "favours rapid early enrichment toward an evolving equilibrium" is an interpretive scenario claim drawn from a flat −0.4 dex offset with ~0.5 dex scatter, small z>6 bins (n=46), and uncorrected selection. The offset is real; the physical story is not earned.
- **The one fix:** forward-model the emission-line selection function onto the SDSS anchor (or apply matched sSFR/EW cuts) before quoting the SFMS elevation, and demote the enrichment-scenario language to a bounded offset.

### 4. TNG massive-galaxy abundance systematics
- **Non-circularity:** clean — TNG n(>M*) are predictions, the JWST counts are independent, and massive-end abundance at z5–6 is not a TNG tuning target; disjoint by construction.
- **Conclusion defensible?** yes — a bounded *null* ("data do not require a departure from ΛCDM," not a consistency measurement), and it honestly carves out the spectroscopic z>6 quiescent ~2 dex excess as unresolved.
- **The one fix:** the null rests entirely on the assumed ~1 dex mass budget being real and applicable — consistency is cheap when a 0.28 dex shift buys it; commit to a specific defensible budget and state the budget value at which the tension would revive, making the null falsifiable.

### 5. MZR aperture/calibration framework
- **Non-circularity:** clean (trivially) — it is a synthesis/review and makes no measurement, so there is no result to be circular.
- **Conclusion defensible?** yes — accurately scoped as a framework/recommendations, explicitly "not a new measurement."
- **The one fix:** it is rigor-safe but empty of a testable result; one original IFU-vs-fiber aperture measurement would convert it from review to result. (Its standing rejection is a novelty-gate problem, outside these two axes.)

### 6. TNG validation (calibration≠validation)
- **Non-circularity:** at-risk — the two-level differencing (subtract TNG's own z≈0 residual, compare internal evolution) genuinely defuses the "tested on what it was tuned to" trap and is the paper's real strength. But the observed anchor it confronts TNG against is the *same selection-biased sample as paper 3*, and TNG aperture mass (2R½) vs SED masses is a mismatched, uncorrected mass definition comparable in size to the signal.
- **Conclusion defensible?** yes (mostly) — the SFR over-evolution is flagged as the one robust, calibration-independent result (and is conservative w.r.t. the selection bias), while the metallicity result is honestly downgraded to "suggestive" once scales are matched. Soft spot: the headline +1.3–1.6 vs +0.8–1.0 dex gap is quoted against an unmatched mass definition.
- **The one fix:** match stellar-mass definitions (forward-model TNG onto SED-mass + the emission-line selection) before quoting the SFR gap — otherwise the load-bearing discrepancy carries an uncorrected systematic of comparable magnitude.

---
**Ranking.** Most rigor-sound: **#1 (z9–10 deficit)** — truly differential, robustness-tested across two anchors and two samples, and disciplined enough to refuse a detection claim; **#4** is a close second as a clean bounded null. Most likely to stay rejected on rigor grounds: **#3 (scaling relations)** — its SFMS elevation is a selection artifact and it overclaims a chemical-evolution scenario (#5 will also stay rejected, but on novelty, not rigor). Single highest-value fixable rigor gap across the portfolio: **the emission-line selection bias inflating the observed SFMS elevation** — forward-modeling that selection onto the SDSS/TNG side simultaneously repairs #3's overclaim and de-risks #6's load-bearing SFR discrepancy.
