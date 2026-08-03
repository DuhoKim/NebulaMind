FABLE_HARD_BURN_H11_SYNTHESIS_20260711T035354Z

# Deep synthesis — environment quenching (m1_rp2), cycle-5 canon vs custody artifact

Lane H11, burn `fable-weekly-hard-burn-20260711T035354Z` (T0 `2026-07-11T03:53:54Z`). Written 2026-07-11 ≈04:35–04:40Z, fully offline.
Author: Fable H11. Scope: deep synthesis per brief; **value-level verification of the supplement is H5's lane** — numeric statements here are custody-anchored context for synthesis, not a substitute for H5's audit.

**Inputs.** All hash-pinned inputs recomputed and matched before reading (full pinned-vs-recomputed table in `H11_RECEIPT.md`): the m1_rp2 artifact (`c0421620…`), cycle-5 supplement (`a4e3d66c…`, cited as SUP:line), cycle-5 flagship (`63b3920e…`, FLG:line), `INVARIANT_MANIFEST.json` (`f4eb857e…`, MAN ids), `RCA_NUMERIC_DRIFT.md` (`45223b56…`, rounding/drift conventions), `INTRODUCTION_LITERATURE_REFERENCE.md` (`874794a1…`, GATED external-value protocol). Helper: `tools/derivation_checks.py` (output reproduced in §1.3; 12/12 PASS).

---

## 1. Artifact anatomy — `m1_rp2_environment_quenching/analysis_results.json`

### 1.1 Measurement design in plain language

The pilot asks one question (artifact `pilot_question`): *"Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample?"*

- **Sample.** The fixed 60,000-row SDSS DR17 optical emission-line cache (`sample_rows`; `source_sample` = `analysis_sample_bpt.csv` from run `SDSS_AGN_SFR_PILOT_20260708T122000Z` — the same retained denominator as the flagship). This is the four-line S/N≥3, `specObjID`-capped, 0.02<z<0.12 selection-limited cache; it is not volume-complete and already excludes emission-weak passive galaxies (SUP:13, FLG:19).
- **Environment metric.** An internally computed 10th-nearest-neighbour density proxy; galaxies are ranked and split into quartiles of 15,000 (= 60,000/4). Per SUP:93 prose the rank is the 10th nearest companion in *projected sky separation* over the full redshift slice with *no line-of-sight velocity window* — this definition is prose-only, not an artifact field (see add-candidate §2.3).
- **Denominators/statistic.** In the top ("high-density") and bottom ("low-density") quartiles, the fraction of galaxies classified quenched/low-sSFR: k successes of n=15,000. Contrast statistics: (a) the raw high-minus-low fraction difference with a bootstrap interval, and (b) a linear probability model (LPM) coefficient on the high-density indicator, adjusted for log stellar mass and redshift.
- **Uncertainties.** Per-quartile binomial standard errors sqrt(p(1−p)/n) (verified §1.3); a bootstrap interval for the raw difference; an (unspecified-estimator) SE for the LPM coefficient.
- **Guard rails.** `interpretation_guard`: "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page." `full_proposal_requires`: "group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions." `method`: "packet-gated-paper-to-wiki-reconciliation".

### 1.2 Every field, with units and role

| field | value | units | role |
|---|---|---|---|
| `card_id` | `rp-2` | — | research-proposal card key |
| `slug` | `m1_rp2_environment_quenching` | — | topic key, joins artifact↔prose↔manifest |
| `short_title` | "SDSS density proxy for environmental quenching" | — | display title |
| `proposal_title` | "Separating internal and environmental quenching across stellar mass, halo mass, and redshift" | — | parent proposal (full scope, NOT what the pilot measures) |
| `pilot_question` | (quoted in §1.1) | — | the only question the artifact answers |
| `run_id` | `SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z` | — | producing run |
| `source_sample` | `…SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv` | path | input denominator (shared with flagship) |
| `figure_pdf` | `…/figures/m1_rp2_environment_quenching_figure1.pdf` | path | quartile-curve figure; file lives in the runs tree, NOT in any pinned snapshot — unverifiable offline |
| `sample_rows` | 60000 | galaxies | full denominator size |
| `high_density_quenched.fraction` | 0.2304 | dimensionless fraction | quenched/low-sSFR fraction, top density quartile |
| `high_density_quenched.k` | 3456 | galaxies | numerator, top quartile |
| `high_density_quenched.n` | 15000 | galaxies | quartile size |
| `high_density_quenched.se` | 0.003438176260752203 | fraction | binomial SE (verified) |
| `low_density_quenched.fraction` | 0.18066666666666667 | fraction | quenched/low-sSFR fraction, bottom quartile |
| `low_density_quenched.k` | 2710 | galaxies | numerator, bottom quartile |
| `low_density_quenched.n` | 15000 | galaxies | quartile size |
| `low_density_quenched.se` | 0.0031414033193486656 | fraction | binomial SE (verified) |
| `high_minus_low_ci` | [0.04059666666666669, 0.059135] | fraction difference | bootstrap 95% interval for raw high−low |
| `lpm_high_density_coeff` | 0.03249480778035638 | probability (≈percentage points/100) | high-density effect at fixed log M★ and z |
| `lpm_high_density_se` | 0.003707733046841099 | probability | SE of the LPM coefficient |
| `result_bullets` | 4 strings | — | canonical prose seeds; NOTE: bullets say "quenched fraction", supplement prose says "low-sSFR emission-line fraction" (see §2.4) |
| `interpretation_guard`, `full_proposal_requires`, `method` | (quoted §1.1) | — | scope guards |

### 1.3 Internal consistency and rounding (helper `tools/derivation_checks.py`, run 04:33Z)

All 12 checks PASS: fractions = k/n exactly (0.2304 = 3456/15000; 0.180667 = 2710/15000); both SEs are exact binomial sqrt(p(1−p)/n); quartile n = sample_rows/4; the point difference 0.049733 sits essentially at the centre of the bootstrap interval (mid 0.049866). Every rounded numeral in SUP:92 is the **nearest-rounding** of its artifact field per the RCA convention: 0.230←0.2304, 0.181←0.180667, [0.041, 0.059]←[0.040597, 0.059135], 0.032←0.032495, 0.004←0.003708, "3.2 percentage-point"←3.24948. **Unlike the flagship CI upper bound (RCA group D1), no environment-quenching canon string deviates from nearest-rounding — this topic has no D1-style re-derivation trap.**

Derived diagnostics (pure arithmetic on artifact fields): naive two-proportion z ≈ 10.7; LPM z ≈ 8.8; mass/redshift adjustment attenuates the raw difference by 34.7% (0.0497 → 0.0325); raw relative excess = 27.5% (0.2304/0.1807 − 1).

---

## 2. Claim inventory — every cycle-5 passage about environment quenching

Grades: **A** direct artifact value · **B** derived/rounded (derivation shown §1.3) · **C** interpretive, no direct number · **X** unsupported/contradicted. **No X grades were found.**

### 2.1 Supplement (`supplementary_denominator_atlas.tex`)

| # | loc | claim (verbatim span) | artifact field(s) | manifest entry | grade |
|---|---|---|---|---|---|
| S1 | SUP:39 | "Relative neighbor-count baseline & …REMAINING_TOPIC_PILOTS… & m1_rp2_environment_quenching/analysis_results.json & c0421620…" (custody table row) | the artifact file itself — quoted sha256 = my recomputed hash of the pinned artifact | SUP-ROW-039 (table_row) | **A** |
| S2 | SUP:59 | "Environment & low-sSFR vs.\ 10th-neighbor rank (60,000 total; 15,000 per quartile) & m1_rp2" | `sample_rows`=60000; `n`=15000 | SUP-ROW-059 (table_row); SUP-15000; SUP-NEIGHBOR-ORD ("10th") | **A** |
| S3 | SUP:76 | "Environment & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test" (follow-up table row) | `full_proposal_requires` — row **drops** "morphology" + "multi-redshift selection functions" and **adds** "fiber-collision correction" | none surfaced (condensed checklist row) | **C** (consistent condensation; delta noted) |
| S4 | SUP:92 | "The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index." | `sample_rows`; `result_bullets[0]` | SUP-NEIGHBOR-ORD; 60,000 scalar (see §2.3 scan note) | **A** |
| S5 | SUP:92 | "The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000)" | `high_density_quenched` {fraction, k, n} | SUP-ENV-HI ("0.230"); SUP-ENV-HI-RATIO ("3,456/15,000") | **B** (0.230 nearest of 0.2304; counts direct **A**) |
| S6 | SUP:92 | "while the low-index quartile has 0.181 (2,710/15,000)" | `low_density_quenched` | SUP-ENV-LO ("0.181"); SUP-ENV-LO-RATIO ("2,710/15,000") | **B** (0.181 nearest of 0.180667; counts **A**) |
| S7 | SUP:92 | "The bootstrap high-minus-low interval is [0.041, 0.059]" | `high_minus_low_ci` | SUP-ENV-CI (ci_interval) | **B** (nearest both ends) |
| S8 | SUP:92 | "a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004" | `lpm_high_density_coeff`, `lpm_high_density_se`; `result_bullets[3]` | SUP-ENV-COEF ("0.032 +/- 0.004") | **B** (nearest both) |
| S9 | SUP:92 | "corresponding to an approximate 3.2 percentage-point increase in low-sSFR incidence at fixed mass and redshift" | 100×`lpm_high_density_coeff` = 3.24948 | "3.2" scalar (see §2.3 scan note) | **B** |
| S10 | SUP:93 | "the rank of the 10th nearest companion in projected sky separation within the full $0.02<z<0.12$ slice, with no additional line-of-sight velocity window" | **no artifact field** states projection/velocity-window; only "10th" is manifest-covered (SUP-NEIGHBOR-ORD, method_parameter) | add-candidate MAN-ADD-1 | **C** (methodological definition, prose-only — must come from run config; not verifiable from pinned inputs) |
| S11 | SUP:93 | "should not be interpreted as a physical environmental volume density or halo density … fiber-collision-biased projected-neighbor rank" | consistent with `interpretation_guard` | — | **C** |
| S12 | SUP:93 | "The follow-up ingredients are group catalogues, robust central/satellite labels, halo masses, a spectroscopic fiber-collision correction at the 55-arcsec scale, morphology, and multi-redshift selection functions." | `full_proposal_requires` item-for-item, **plus** the fiber-collision correction (supplement's own addition, motivated by SUP:24) | — | **B** (mapping shown; one added item flagged) |
| S13 | SUP:97 | figure caption: "low-sSFR emission-line fraction as a function of the 10th-neighbor index …" | `figure_pdf` (path only; PDF not in any pinned snapshot) | add-candidate MAN-ADD-2 | **C** (content unverifiable offline) |
| S14 | SUP:13, SUP:24 | atlas-level environment caveats: "fiber-collision-biased projected-rank proxies only, not physical density estimates"; 55-arcsec collision limit; ordinal-proxy status; `specObjID` non-random selection | consistent with `interpretation_guard`; no numerals | — | **C** |
| S15 | SUP:125 | radio-jet environment baseline (m2_p2): "high-index quartile has a broad optical BPT-selected fraction of 0.509 … low-index 0.367 … interval is [0.112, 0.170]" — *same neighbor ranking, adjacent topic* | supporting artifact is `m2_p2…/analysis_results.json` (`4e1ff701…`, SUP:42) — **not in the H11 pin set**; listed for completeness, not graded against an artifact I could open | SUP-JET-HI, SUP-JET-LO, SUP-JET-CI, SUP-ROW-042 | ungraded here (H5 owns) |

### 2.2 Flagship (`rp1_flagship_polished.tex`) — carries **zero** environment numerals; every mention is a scope exclusion

| # | loc | claim (verbatim span) | support | grade |
|---|---|---|---|---|
| F1 | FLG:13 | "The companion supplement inventories missing structural, environmental, gas, radio/X-ray, and IFU observables required for future real-data tests." | SUP Table `tab:atlas-followup` (SUP:76) exists | **C** |
| F2 | FLG:22 | "The present scope also excludes … environment labels …" | consistent with artifact `interpretation_guard` | **C** |
| F3 | FLG:25 | "it does not include … group membership, halo mass … as matching variables" | consistent | **C** |
| F4 | FLG:28 | "The remaining requirements are … group or halo membership …" | mirrors `full_proposal_requires` | **C** |
| F5 | FLG:70 | "see Supplement Sections 5.1 and 5.7 for the neighbor-rank/fiber-collision and CO/HI requirements" | cross-reference accurate: SUP:92–93 is the neighbor-rank/fiber-collision entry | **C** |
| F6 | FLG:74 | "No measured result in this paper should be read as a gas-mass, environment-density, or feedback-efficiency estimate." | negative-scope claim; nothing in FLG contradicts the artifact | **C** |
| F7 | FLG:75 | environment/context citations (peng2010, ellison2011, piotrowska2022, wetzel2013, dekel2006) "cited as examples of missing observables … not as validation" | role-separated literature pointers; no external numerals present | **C** / GATED-EXTERNAL pointers |

### 2.3 Manifest coverage and add-candidates

Manifest entries confirmed for this topic: SUP-ENV-HI, SUP-ENV-HI-RATIO, SUP-ENV-LO, SUP-ENV-LO-RATIO, SUP-ENV-CI, SUP-ENV-COEF, SUP-15000, SUP-NEIGHBOR-ORD, SUP-ROW-039, SUP-ROW-059 (and adjacent SUP-JET-HI/LO/CI, SUP-ROW-042). *Scan note:* the initial token scan omitted "60,000"/"3.2"; a follow-up grep (04:39Z) confirmed both as manifest scalars — `SUP-60000` (`exact_string: "60,000"`) and an `exact_string: "3.2"` entry (manifest line 619) — so S4 and S9 are manifest-covered as well; both are nearest-rounding-clean (§1.3).

**Add-candidates** (for Duho / a future manifest change, NOT applied by this lane):
- **MAN-ADD-1** — the neighbor-metric definition (projected separation; no Δv window; full-slice ranking; k=10) as a `method_parameter` group, custody-pinned from run config. Today it exists only as SUP:93 prose (S10).
- **MAN-ADD-2** — sha256 of `m1_rp2_environment_quenching_figure1.pdf` into custody, so the figure/caption (S13) becomes verifiable from snapshots.
- **MAN-ADD-3** — interior-quartile (Q2, Q3) fractions if promoted from run outputs (enables the monotonicity test, §5 N1).

### 2.4 Wording-drift hazard (flag for the reconciliation pipeline)

The artifact's own `result_bullets` say "**quenched fraction** 0.230…", while cycle-5 canon prose deliberately downgrades to "**low-sSFR emission-line fraction**" (S5) — the conservative direction. `method` = "packet-gated-paper-to-wiki-reconciliation": any wiki/proposal surface that seeds text from `result_bullets` verbatim will carry the stronger "quenched" wording and drift from canon. Same class of hazard as RCA's verbatim-carry rule, but for *terms* rather than numerals; worth an explicit carry rule for bullet-seeded prose.

---

## 3. Physics synthesis — what the numbers do and do not establish

Tags: **[DATA]** = DATA-SUPPORTED (artifact fields or pure arithmetic on them, §1.3) · **[INTERP]** = INTERPRETATION · **[GATED-EXT]** = GATED-EXTERNAL (literature slot; no values, per protocol).

**[DATA]** Within the 60,000-galaxy emission-line denominator, the top 10th-neighbour-rank quartile has a low-sSFR fraction of 0.2304 (3,456/15,000) against 0.1807 (2,710/15,000) in the bottom quartile — a raw excess of +4.97 percentage points, bootstrap 95% interval [0.0406, 0.0591], well clear of zero. **[DATA]** The excess survives linear adjustment for log stellar mass and redshift at +3.25 ± 0.37 percentage points (≈8.8σ), so the density proxy adds quenched-fraction information beyond stellar mass in this sample — the pilot question is answered affirmatively at the association level. **[DATA]** The adjustment removes 34.7% of the raw contrast (0.0497 → 0.0325), i.e., roughly a third of the raw quartile difference is mass/redshift composition rather than a fixed-mass environment signal. **[DATA]** In relative terms the raw excess is 27.5% of the low-quartile rate — a modest, precisely measured shift, not a bimodal separation.

**[INTERP]** A positive fixed-mass density coefficient is the signature expected if an environment-linked channel — satellite quenching, ram-pressure stripping, strangulation, harassment — operates on top of internal/mass quenching; nothing in this artifact can name the channel. **[INTERP]** The attenuation pattern (raw > adjusted, both positive) is what one expects when denser regions also host more massive galaxies, so part of the raw contrast is the mass function shifting with environment, with a genuine residual environmental term at fixed mass. **[GATED-EXT]** This separable mass-plus-environment structure is qualitatively the framework of Peng et al. (2010) and the SDSS satellite-quenching results of Wetzel et al. (2013) — already in the cycle-5 bibliography as missing-observable pointers (FLG:75); any *quantitative* comparison value must first pass the EXT-slot registration protocol of `INTRODUCTION_LITERATURE_REFERENCE.md` (network — needs separate Duho approval) and be added to the manifest.

What the artifact does **not** establish:

**[DATA]** No satellite/central decomposition, halo masses, morphology, or multi-redshift selection functions exist in this artifact — its own `full_proposal_requires` lists exactly these as missing, and the proposal title ("Separating internal and environmental quenching…") remains untested by the pilot. **[DATA]** The environment metric is an ordinal projected-neighbour rank inside a selection-limited sample — per canon prose with no velocity window (S10) — and the 55-arcsec fiber-collision limit biases it in dense regions, so no physical density, halo density, or overdensity value can be read off. **[DATA]** The denominator is the four-line S/N≥3 emission-line cache: emission-weak passive galaxies are excluded before the environment split, so 0.230/0.181 are *conditional* low-sSFR incidences within emission-line galaxies, not population quenched fractions, and their high−low difference need not equal the population environmental quenched-fraction excess. **[INTERP]** The two known distortions plausibly push the same way — fiber collisions compress rank contrast in dense regions, and the S/N cut removes passive (likely denser-region) galaxies preferentially — which would make +3.2 pp an underestimate, but neither effect is quantified here, so "lower bound" remains a hypothesis, not a result. **[INTERP]** Because the rank is computed in projected separation across the whole 0.02<z<0.12 slice, a fixed rank corresponds to different physical scales at different redshifts; the LPM's linear-in-z term only partially absorbs this scale mixing. **[DATA]** Causality, timescales, and quenching-channel identification are out of scope by construction (`interpretation_guard`; FLG:74's negative-scope sentence is the flagship-side mirror of the same guard).

---

## 4. Confounders and alternative explanations

Each item: what it could do to the +3.2 pp coefficient, and whether it is **addressable with the current artifact (how)** or **requires new run/data (GATED)**.

1. **Emission-line selection of the denominator.** The S/N cut removes passive systems; if removal probability correlates with density (dense regions redder/weaker-lined), the conditional fractions understate — or in pathological cases distort — the population environmental signal. *Current artifact:* only the qualitative direction argument above; the artifact carries no parent-sample counts. **Requires new run (GATED — DB/parent-catalog query of S/N pass rates vs density).**
2. **Fiber collisions (55 arcsec).** Missing close neighbours in dense regions compresses high-density ranks; quartile assignment blurs, likely diluting the contrast (direction plausible, unproven). *Current artifact:* prose caveat only (S11/S14). **Requires new run (GATED — nearest-neighbour redshift assignment or angular-correlation correction, per SUP:93's cited SDSS methodology).**
3. **Aperture + SFR indicator.** "Low-sSFR" uses the catalog aperture-extrapolated central-fiber sSFR proxy; if bulge-dominated galaxies concentrate in dense regions (morphology–density relation — GATED-EXT pointer), central-fiber classification could label bulgy star-formers as quenched preferentially in dense regions, mimicking environmental quenching. Structural proxies were *not retained* in the 60,000-row cache (FLG:22/25). **Requires new run (GATED — re-query structural columns, then control/match on them).**
4. **Mass/redshift adjustment adequacy.** The LPM is linear in log M★ and z; residual confounding survives if the quenched probability is non-linear in mass (it is, generically) and the quartile mass distributions differ strongly. *Current artifact:* partially addressable — the raw-vs-adjusted pair itself quantifies gross composition (34.7% attenuation, §1.3), bounding how much adjustment matters at first order. Functional-form robustness (mass-binned contrasts, matching, logistic link) **requires new run (GATED — needs per-galaxy rows in `source_sample`, which live in the runs tree).**
5. **Environment-metric choice.** k=10 projected rank with no Δv window is one point in metric space; fixed-aperture counts, different k, Δv-windowed neighbours, or group-catalog environments could give different contrasts (interloper dilution currently pushes the measured contrast down if the signal is real). **Requires new run (GATED — runner for metric variants; external group catalog for the catalog variant).**
6. **Redshift-dependent physical scale of the rank.** Same angular-rank ≠ same physical environment across 0.02<z<0.12. *Current artifact:* the LPM's z term acknowledges but cannot resolve it. **Requires new run (GATED — z-binned quartile contrasts).**
7. **Interior-quartile behaviour unknown.** Only Q1 and Q4 are in the artifact; a non-monotonic Q2/Q3 pattern would point to selection/tiling artifacts rather than a smooth environmental trend. The quartile curve apparently exists as the run figure (`figure_pdf`) but is outside every pinned snapshot. **GATED, but cheap: custody promotion of existing run outputs (MAN-ADD-3) — no new computation, still Duho's call since it touches the runs tree.**

---

## 5. Falsifiable predictions and next analyses (dependency-ordered)

Everything below touching runner, network, DB, or external catalogs is **GATED for Duho**; nothing here was executed by this lane.

**N0 — custody promotion (GATED: runs-tree read; no new compute).** Pin MAN-ADD-1 (metric definition), MAN-ADD-2 (figure hash), MAN-ADD-3 (Q2/Q3 fractions) from existing run outputs into the snapshot/manifest. Unblocks P1 verification offline.
**N1 — quartile-resolved contrast (GATED: runner).** Emit Q1–Q4 fractions with SEs. **P1 (falsifiable):** fractions increase monotonically Q1→Q4; a Q4-only jump or non-monotonic interior falsifies the smooth-trend reading and implicates tiling/selection artifacts.
**N2 — velocity-windowed metric (GATED: runner).** Recompute the rank with |Δv| ≲ 1000 km/s within the slice. **P2:** the fixed-mass coefficient persists and likely strengthens (interloper removal); collapse toward 0 falsifies the physical-association reading (projection artifact).
**N3 — fiber-collision correction (GATED: runner).** Nearest-neighbour redshift assignment / angular-correlation correction at 55 arcsec. **P3:** corrected excess ≥ 3.2 pp; a corrected value consistent with 0 would attribute the signal to tiling geometry.
**N4 — group-catalog join (GATED: external catalog + runner; depends on N2/N3 being sane).** Yang-style groups → central/satellite labels + halo masses. **P4:** the excess concentrates in satellites; the central-only coefficient at fixed M★ is consistent with 0 (or much smaller). **P5:** the satellite excess grows with halo mass at fixed M★. Either failing breaks the standard satellite-quenching interpretation for this sample.
**N5 — structural controls (GATED: DB re-query).** Add concentration/fracDeV/σ to the cache; re-fit with structure controlled. **P6:** the density coefficient stays positive though attenuated; vanishing entirely would mean the "environment" signal is morphology-mediated in this denominator (confounder 3 wins).
**N6 — selection-function audit (GATED: DB/parent catalog).** Measure four-line S/N pass rate vs density in the parent sample. **P7:** pass rate anticorrelates with density, and reweighting *raises* the measured excess (tests the "3.2 pp is a floor" hypothesis, §3).
**N7 — external quantitative comparison (GATED: network + manifest change).** Fill EXT-style slots (per `INTRODUCTION_LITERATURE_REFERENCE.md` §L-2 protocol) with published satellite quenched-fraction excesses (candidate anchors already in the bibliography: wetzel2013, peng2010) only after verification + manifest registration.

---

## Stretch note — cycle-6/7 drift status for this topic (from pinned RCA, not a fresh diff)

`RCA_NUMERIC_DRIFT.md` mechanically counted all 105 manifest entries across cycles 5→6→7 and enumerated *every* changed entry: D1 (flagship CI string, 4 locations), D2 (m3_p3 table cell 2.830→2.831, cycle 7), D3 (m3_p3 span rewrite, cycle 6). None touch m1_rp2/environment entries. **Inference (grade B): all environment-quenching numerals (SUP-ENV-*, SUP-ROW-039/059, SUP-15000, SUP-NEIGHBOR-ORD) carried unchanged into cycles 6 and 7.** A direct grep of the cycle-6/7 snapshots was not performed within the cap; treat this as RCA-derived, not independently re-diffed.

## Bottom line

The m1_rp2 artifact cleanly supports one association-level statement — in this selection-limited emission-line cache, galaxies in the densest projected-neighbour quartile are ~3.2 ± 0.4 pp more likely to be low-sSFR at fixed stellar mass and redshift than those in the least dense quartile — and the cycle-5 canon prose states exactly that, with every numeral either direct (A) or a verified nearest-rounding (B), zero unsupported claims (X), and deliberately conservative wording. It does **not** measure physical density, satellite quenching, halo trends, or causation; the flagship correctly carries no environment numbers at all. The highest-leverage next steps are the three GATED custody promotions (N0) and the quartile/Δv/fiber-collision robustness runs (N1–N3), which together convert a single-contrast pilot into a falsifiable environmental-trend measurement without any new survey data.
