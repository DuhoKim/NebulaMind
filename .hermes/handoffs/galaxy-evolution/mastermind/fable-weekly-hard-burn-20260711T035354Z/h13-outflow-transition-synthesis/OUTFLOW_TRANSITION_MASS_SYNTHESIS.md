FABLE_HARD_BURN_H13_SYNTHESIS_20260711T035354Z

# H13 deep synthesis — outflow escape/recycling (m2_p1) × feedback transition mass (m2_p3)

Burn `fable-weekly-hard-burn-20260711T035354Z` · lane h13 · written 2026-07-11T04:32Z (UTC)
All inputs hash-verified against H13_BRIEF.md pins at 2026-07-11T04:28:10Z — 9/9 MATCH (see `H13_RECEIPT.md` custody table). Snapshots only; no live-tree reads. Arithmetic checks reproducible via `tools/h13_checks.py`.

Abbreviations: **A** = `m2_p1_outflow_escape_recycling/analysis_results.json`; **B** = `m2_p3_feedback_transition_mass/analysis_results.json`; **SUP** = cycle-5 `supplementary_denominator_atlas.tex` (line numbers are that file's); **FLG** = cycle-5 `rp1_flagship_polished.tex`; **MAN** = `INVARIANT_MANIFEST.json` (105 entries); **RCA** = `RCA_NUMERIC_DRIFT.md`.

---

## 1. Artifact anatomy

### 1.1 Artifact A — m2_p1 outflow escape/recycling (sha `44b2407a…a210`, MATCH)

**Measurement design in plain language.** From the fixed 60,000-row SDSS DR17 emission-line cache (`SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv`, the same parent as the flagship), count the subset classified as *high-excitation* broad optical BPT-selected AGN candidates, report that count as a fraction of the full denominator with a binomial standard error, and compare the subset's median log sSFR against the full denominator's median. The design is a **denominator sizing exercise** for future resolved-kinematics follow-up: it deliberately measures *how many targets* an escape-vs-recycling campaign would have, not anything about escape or recycling itself. There is no kinematic, velocity, halo, or gas-phase quantity anywhere in the artifact; the artifact says so explicitly (`result_bullets[2]`, `full_proposal_requires`).

**Every field, with role and units:**

| Field | Value | Unit / dimension | Role |
|---|---|---|---|
| `card_id` | `"p1"` | — | topic card id |
| `slug` | `m2_p1_outflow_escape_recycling` | — | artifact identity |
| `run_id` | `SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z` | — | producing run (matches SUP:41 custody row) |
| `method` | `source-first-paper-adjudication` | — | pipeline method tag |
| `proposal_title` | "Escape versus recycling: the fate of AGN-driven multiphase outflows" | — | parent proposal |
| `pilot_question` | denominator-sizing question (verbatim in JSON:15) | — | scope declaration |
| `sample_rows` | 60000 | count (galaxies) | full denominator N |
| `high_excitation_agn.k` | 4440 | count (galaxies) | numerator |
| `high_excitation_agn.n` | 60000 | count (galaxies) | denominator (≡ `sample_rows`) |
| `high_excitation_agn.fraction` | 0.074 | dimensionless (proportion) | k/n |
| `high_excitation_agn.se` | 0.0010686751923136733 | dimensionless | binomial SE of the proportion |
| `median_log_sSFR_all` | −10.140585 | dex, log10(sSFR / yr⁻¹) | full-denominator median |
| `median_log_sSFR_high_excitation` | −11.53205 | dex, log10(sSFR / yr⁻¹) | subset median |
| `interpretation_guard` | SDSS-only pilot text | — | scope guard |
| `full_proposal_requires` | resolved outflow velocities, halo potentials, molecular/ionized/neutral phases, CGM recycling tracers | — | missing observables |
| `result_bullets` | 3 strings | — | canonical prose seeds |
| `figure_pdf`, `source_sample` | absolute paths | — | provenance pointers (live runs-tree paths; **not** followed, per snapshot-only directive) |
| `short_title` | "SDSS high-excitation AGN denominator for outflow escape tests" | — | display title |

**Arithmetic/unit audit (recomputed, `tools/h13_checks.py`):**
- 4440 / 60000 = **0.074 exactly** — `fraction` is exact, not rounded. ✓
- Binomial SE √(p(1−p)/n) = √(0.074·0.926/60000) = **0.00106867519231…** — matches `se` to all 16 stored digits, confirming the SE is the plain binomial proportion SE (dimensionless). ✓
- Subset-minus-all median gap: −11.53205 − (−10.140585) = **−1.391465 dex**. Not stated in the artifact but implied by SUP:114's "compared with" sentence. This is an *unmatched, subset-vs-denominator* gap — see §3 tension T1 for the conflation hazard with the flagship's matched-pair −1.309 dex.
- Dimension check: sSFR medians are in dex of yr⁻¹ (implied sSFR ≈ 7.2×10⁻¹¹ vs 2.9×10⁻¹² yr⁻¹ — both physically sensible for star-forming vs quiescent low-z galaxies). No quantity in A carries velocity (km s⁻¹), mass (M☉), or energy units. **The "outflow escape/recycling" artifact contains zero kinematic dimensions** — its entire physical content is one proportion and two sSFR medians.

### 1.2 Artifact B — m2_p3 feedback transition mass (sha `204ec46d…2b67`, MATCH)

**Measurement design in plain language.** Bin the *same* 60,000-row denominator into five stellar-mass bins (log10 M★/M☉ edges 8.0, 9.5, 10.0, 10.5, 11.0, 12.5); in each bin compute (i) the fraction classified broad-optical-BPT AGN and (ii) the fraction with low catalog sSFR ("quenched"); report the first bin where the quenched fraction exceeds 0.5, and the bin where AGN fraction peaks. The design is a **co-incidence-vs-mass diagnostic**: it locates where two optical incidence curves rise within one selection-limited denominator. It fits no threshold, carries no per-bin counts, and no uncertainties of any kind.

**Every field, with role and units:**

| Field | Value | Unit / dimension | Role |
|---|---|---|---|
| `card_id` / `slug` | `"p3"` / `m2_p3_feedback_transition_mass` | — | identity |
| `run_id` | `SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z` | — | same run as A (SUP:43 custody row) |
| `method` | `source-first-paper-adjudication` | — | pipeline tag |
| `proposal_title` | "Locating the transition from stellar-feedback to AGN-feedback regulation" | — | parent proposal |
| `pilot_question` | co-rise mass-scale question (JSON:23) | — | scope declaration |
| `sample_rows` | 60000 | count | denominator (≡ A's) |
| `mass_bin_labels` | 8.0–9.5, 9.5–10.0, 10.0–10.5, 10.5–11.0, 11.0–12.5 | dex, log10(M★/M☉) | bin edges; widths **1.5, 0.5, 0.5, 0.5, 1.5 dex — uneven** |
| `agn_fraction_by_mass` | 0.00270303…, 0.01375179…, 0.07734114…, 0.26028862…, 0.52020828… | dimensionless per bin | AGN incidence curve |
| `quenched_fraction_by_mass` | 0.00528320…, 0.02581625…, 0.13116639…, 0.39254112…, 0.72923382… | dimensionless per bin | low-sSFR incidence curve |
| `peak_agn_fraction` | 0.5202082816761716 | dimensionless | max of AGN curve |
| `peak_agn_mass_bin` | "11.0-12.5" | dex bin label | argmax bin |
| `transition_mass_bin_quenched_fraction_gt_0p5` | "11.0-12.5" | dex bin label | first bin with quenched > 0.5 |
| `interpretation_guard`, `full_proposal_requires`, `result_bullets`, `figure_pdf`, `source_sample`, `short_title` | as in A | — | guards/provenance (gas fractions, baryon deficits, halo masses, stellar-feedback observables, high-z extensions) |

**Arithmetic/unit audit (recomputed):**
- All 10 fractions ∈ [0,1]; both curves **strictly monotone increasing** across the five bins (rank correlation between the two curves = 1.0). ✓
- `peak_agn_fraction` = element 5 of `agn_fraction_by_mass` exactly; argmax = bin 5 = "11.0-12.5". ✓
- First bin with quenched > 0.5: bin 4 has 0.3925 < 0.5, bin 5 has 0.7292 > 0.5 → "11.0-12.5". Field value consistent. ✓ (Also: no bin crosses 0.5 for AGN except bin 5 — the two "transitions" land in the same bin by construction of the 0.5 threshold only for quenched; AGN merely peaks there.)
- Dimension check: "transition mass" in this artifact is a **bin label, not a measured mass** — resolution is the bin width (1.5 dex for the transition bin), it has no error bar, and no absolute masses (M☉), velocities, or energies appear anywhere. **B contains zero per-bin counts**, so binomial SEs for its 10 fractions are *not computable offline from the artifact alone* — a real gap given SUP quotes the peak to 3 decimal places (see T3).
- "Quenched" nomenclature: the JSON keys say `quenched_fraction*`; the artifact's own `result_bullets[0]` says "quenched fraction", but SUP:136 deliberately renames it "low-sSFR fraction". Prose is *stricter* than the artifact key — right direction, worth keeping deliberate (see T4).

---

## 2. Claim inventories (cycle-5 prose → artifact fields → manifest → grade)

Grading: **A** = numeric string identical to artifact value or exact arithmetic; **B** = derivable from artifact via the RCA nearest-rounding convention (derivation shown; RCA §"verbatim-carry" means these must still be *copied*, never re-derived, in future cycles); **C** = interpretive claim consistent with but not numerically backed by the artifact; **X** = unsupported/contradicted. No X grades were found.

### 2.1 Topic A — outflow escape/recycling

| # | Claim (verbatim, location) | Artifact field(s) | Manifest | Grade |
|---|---|---|---|---|
| A1 | "High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 emission-line galaxies (0.074)." — SUP:114; table row SUP:61 "…(4,440/60,000)" | `high_excitation_agn.k/.n/.fraction` | `SUP-HIEXC-N` (line 61), `SUP-HIEXC-FRAC` (line 114), `SUP-ROW-061` | **A** — 4440/60000 = 0.074 exact; strings match with `4,440` comma formatting per manifest |
| A2 | "Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator." — SUP:114 | `median_log_sSFR_high_excitation` = −11.53205; `median_log_sSFR_all` = −10.140585 | `SUP-HIEXC-SSFR`, `SUP-FULL-SSFR` | **B** — nearest 2-dp rounding: −11.53205 → **−11.53**; −10.140585 → **−10.14**. Both are clean nearest-roundings (no RCA anomaly of the −1.283/2.830 class applies to these strings) |
| A3 | "SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result." — SUP:114 | `result_bullets[2]` (near-verbatim), `full_proposal_requires`, `interpretation_guard` | (scope text; no numeric entry) | **A** (scope claim, directly artifact-seeded) |
| A4 | "The result … does not test feedback-related quenching scenarios, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling in this dataset." — FLG:19; echoed FLG:75 (outflow refs cited as *missing observables*) | consistent with A's guards (negative scope) | — | **A** (negative scope claim; nothing in A or B contradicts it) |
| A5 | Custody row: "Resolved-kinematics follow-up denominator & …PILOTS_20260708T125828Z & m2_p1…/analysis_results.json & 44b2407a…a210" — SUP:41 | artifact identity + sha | `SUP-ROW-041` | **A** — sha re-verified this session (MATCH) |
| A6 | "The follow-up ingredients are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers." — SUP:114 | `full_proposal_requires` (verbatim list) | — | **A** |

### 2.2 Topic B — feedback transition mass

| # | Claim (verbatim, location) | Artifact field(s) | Manifest | Grade |
|---|---|---|---|---|
| B1 | "The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\)" — SUP:136 | `transition_mass_bin_quenched_fraction_gt_0p5` = "11.0-12.5"; independently re-derivable: quenched[4]=0.3925<0.5, quenched[5]=0.7292>0.5 | `SUP-MASSBIN-INT`, `SUP-HALF` (threshold 0.5) | **A** — field match *and* exact re-derivation from the arrays |
| B2 | "the broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520" — SUP:136 | `peak_agn_fraction` = 0.5202082816761716; `peak_agn_mass_bin` = "11.0-12.5" | `SUP-BPT-PEAK`, `SUP-MASSBIN-DASH` | **B** — nearest 3-dp: 0.5202082817 → **0.520**; argmax bin re-derived = bin 5 ✓ |
| B3 | "that peak is consistent with a selection-function bias: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies… It must not be interpreted as a universal physical threshold." — SUP:136 | `interpretation_guard` + `result_bullets[2]` are weaker ("optical transition diagnostic; gas fractions and baryon deficits needed"); the S/N-cut *mechanism* is prose-added reasoning, not an artifact field | — | **C** — consistent and epistemically sound, but the specific bias mechanism is not artifact-backed; keep as interpretation, never promote to result |
| B4 | "Across mass bins, low-sSFR fractions span 0.005-0.729, and broad optical BPT-selected fractions span 0.003-0.520." — SUP:169 (m3_p3 sim-target subsection; **cross-topic reuse of B's arrays**) | min/max of `quenched_fraction_by_mass` → 0.00528→**0.005**, 0.72923→**0.729**; of `agn_fraction_by_mass` → 0.00270→**0.003**, 0.52021→**0.520** | `SUP-SPAN-QUENCH`, `SUP-SPAN-BPT` | **B** — aggregate (min/max) + nearest 3-dp rounding. RCA E6 flags exactly this span-recomputation class as drift-prone: future cycles must carry the strings verbatim |
| B5 | Custody row: "Stellar-mass selection diagnostic & …PILOTS_20260708T125828Z & m2_p3…/analysis_results.json & 204ec46d…2b67" — SUP:43 | artifact identity + sha | `SUP-ROW-043` | **A** — sha re-verified this session (MATCH) |
| B6 | "This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning… follow-up ingredients are gas fractions, baryon deficits, halo masses, central velocity dispersion proxies, stellar-regulation observables, and high-redshift extensions." — SUP:136 | `result_bullets[2]`, `full_proposal_requires` (prose adds "central velocity dispersion proxies \citep{piotrowska2022}" beyond the artifact's list) | — | **A** for the artifact-seeded portion; the velocity-dispersion addition is a **C**-grade methodological pointer (SUP:19 role-separation covers it) |

**RCA cross-check on this lane's numerals.** None of the topic numerals (0.074, 4,440, −11.53, −10.14, 0.520, 0.005-0.729, 0.003-0.520, [11.0,12.5]) is among the two known rounding anomalies (`FLG-CI95` −1.283; SUP:188 cell 2.830). Every graded-B string above is the *clean nearest-rounding* of its artifact value, so verbatim-carry and re-derivation currently coincide for this lane — the livelock risk RCA documents does not presently touch these entries, but the verbatim-carry rule still applies.

---

## 3. Joint synthesis — does the transition mass partition escape vs recycling?

**Center-of-mass answer: the cycle-5 prose never claims it does — and at artifact level the question is not even posable offline.** This is the lane's key structural finding:

1. **No shared mass scale exists between the two artifacts.** A contains *no mass axis at all* (its only quantities are one proportion, one SE, two sSFR medians). B contains *no kinematic or escape quantity at all*. The only mass threshold anywhere in either topic is B's "11.0-12.5" bin label, and it is quoted in SUP:136 only — SUP:114 (topic A) quotes no mass whatsoever. A partition claim ("below M★ᵗ outflows recycle, above they escape" or the reverse) would need at least one quantity carrying velocity or binding-energy dimensions on each side of the mass threshold; neither artifact has one. Dimensional bookkeeping alone shows the partition test is **not constructible** from these inputs.
2. **The prose is explicitly firewalled against the implication.** SUP:114: "SDSS does not measure escape velocity or multiphase outflow velocities here" (grade A). SUP:136: "must not be interpreted as a universal physical threshold" + selection-bias caveat. FLG:19: "does not test … outflow escape/recycling in this dataset." The two subsections never cite each other's numbers. Where a reader *might* stitch a partition narrative, cycle-5 has pre-emptively severed it. **Verdict: no over-claim exists to falsify; the joint claim is deliberately absent.**
3. **What the two artifacts *do* jointly support** (same-denominator association, not independent evidence — both consume the identical `analysis_sample_bpt.csv`, 60,000 rows, same run): A's high-excitation AGN subset sits −1.391 dex below the full-denominator median sSFR, and B shows AGN incidence and low-sSFR incidence rising together, monotonically, to a co-peak in the same top mass bin. These are two projections of one underlying association — "optically AGN-classified galaxies skew massive and low-sSFR in this selection" — viewed subset-first (A) and mass-binned (B). Internally coherent; mutually consistent; **not** mutually corroborating (shared sample, shared selection).
4. **Offline energetics sanity check:** the only physically anchored escape-relevant statement possible with zero kinematic data is dimensional (point 1). Attempting v_esc ≈ √(2GM/R) at the "transition mass" would require halo mass and radius — both listed as *missing* in the artifacts' own `full_proposal_requires`. Correctly GATED; nothing to compute.

### Consistency table

| # | Quantity / statement | Topic A side | Topic B side | Verdict |
|---|---|---|---|---|
| 1 | Denominator | n = 60000; `source_sample` = `…SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv` | identical values, identical path | **agrees** (same parent sample, same run_id) |
| 2 | AGN-class incidence | 0.074 (high-excitation subset of 60,000) | 0.0027–0.520 by mass bin (broad class; global value not recoverable — no bin counts) | **independent** — different selections (subset vs broad class), not comparable; no tension. SUP:147 (m3_p1) gives broad-class prevalence 0.136–0.418 by tracer definition; 0.074 < 0.136 is consistent with "high-excitation" being the strictest subset |
| 3 | AGN ↔ low-sSFR association | subset median sSFR 1.39 dex below denominator median | both incidence curves strictly co-monotone with mass, co-peak in top bin | **agrees** directionally (same-sample projections of one association) |
| 4 | Mass scales quoted | none — A and SUP:114 quote no mass | "11.0-12.5" (SUP:136, twice; MAN ×2 forms) | **independent** — no shared threshold exists to agree or conflict |
| 5 | Span reuse across topics | — | B's arrays' min/max = SUP:169's spans 0.005-0.729 / 0.003-0.520 (m3_p3 subsection) | **agrees** — cross-subsection numeric reuse verified exact under nearest-rounding |
| 6 | sSFR offset statistics | implied −1.391 dex (unmatched subset-vs-all, high-excitation) | — (FLG:13/74: −1.309 dex, matched pairs, broad class, CI [-1.334,-1.283]) | **in tension only if conflated** — see T1 |

### Tension list (none is a numeric contradiction; all are hazards or gaps)

- **T1 — conflation hazard, −1.391 vs −1.309 dex.** A implies a −1.391 dex unmatched subset-vs-denominator median gap (high-excitation subset); the flagship's headline is −1.309 dex from 8,146 mass-and-redshift *matched pairs* of the *broad* class. Numerically close, methodologically disjoint (different subset, different comparison design, different statistic). Neither SUP nor FLG states −1.391 explicitly — good — but any future prose that back-derives it risks presenting two "AGN sSFR deficits" that readers will average or compare. Recommendation: if −1.391 is ever surfaced, it must be introduced as "unmatched, selection-confounded, high-excitation-only" in the same sentence.
- **T2 — uneven bin widths flatter the top bin.** B's bins are 1.5 / 0.5 / 0.5 / 0.5 / 1.5 dex wide. Both "transition" statements land in the widest top bin (11.0–12.5). A wide top bin mechanically accumulates the strongly-rising tail of both curves, so "first bin > 0.5" and "peak bin" are partly artifacts of edge placement; with 0.5-dex bins the quenched-fraction crossing could land in 11.0–11.5 or later — indeterminable from stored aggregates. SUP:136's guards cover misinterpretation but do not name binning as a confounder (they name the S/N cut). Cheapest strengthening available (GATED re-run, C2 below).
- **T3 — precision without uncertainty in B.** SUP:136 quotes 0.520 to 3 dp; B stores no per-bin counts, so no SE is computable offline (contrast A, which ships k, n, and a verified binomial SE). The 3-dp quote is manifest-frozen (SUP-BPT-PEAK), so this is a *gap to close in the artifact*, not a prose edit: a re-run should emit per-bin counts (C3).
- **T4 — nomenclature split "quenched" vs "low-sSFR".** B's JSON keys say `quenched_fraction*` and its `result_bullets[0]` says "quenched fraction"; SUP:136 deliberately downgrades to "low catalog-sSFR". The prose is more careful than its own artifact. Fine as-is, but any tooling that quotes artifact keys verbatim into prose (the RCA "regenerator" failure mode) would *re-introduce* the stronger word. Verbatim-carry protects numerals only — this is the same failure class one level up, in wording.
- **T5 — bare "0.5" threshold.** MAN entry `SUP-HALF` protects the string "0.5" with match_mode numeric-context at SUP:136. A threshold this short is collision-prone under prose edits (many "0.5"s can appear). Not a current inconsistency; a manifest-robustness note for the next manifest revision.

---

## 4. Confounders

### Topic A (m2_p1)

| Confounder | Status |
|---|---|
| **Outflow tracer choice** — "high-excitation optical" is one of several optical AGN definitions; SUP:147 (m3_p1) shows broad-class prevalence swings 0.136–0.418 (ratio 3.1) by definition alone; 0.074 is stricter still | **Addressable with current artifacts (how):** state the sensitivity bracket by citing SUP:147's numbers next to 0.074; the denominator for a kinematic campaign is definition-dependent by up to ~5.6× (0.074→0.418). No new run needed for the *statement*; the per-definition target lists need a re-run (GATED) |
| **Projection / aperture** — 3″ fiber-centered classification and sSFR; no spatial decomposition; outflow vs rotation indistinguishable (SUP:114 cites exactly this) | **Requires new run (GATED):** IFU kinematics; no offline mitigation exists in A |
| **Escape-velocity assumptions** — any future escape verdict depends on halo potential model (halo mass, concentration, gas launch radius); none present | **Requires new run/data (GATED):** halo potentials via group catalogs or lensing; A correctly lists them as missing |
| **Subset-vs-all comparison design** — A2's −11.53 vs −10.14 comparison is unmatched; mass confounds it (B shows AGN skew massive; massive galaxies skew low-sSFR) | **Addressable with current artifacts (how):** cross-cite B's co-monotone curves as the reason the unmatched gap must not be read causally; quantitative matching exists only in the flagship's separate pair analysis |

### Topic B (m2_p3)

| Confounder | Status |
|---|---|
| **Mass-bin edges** — uneven widths (T2); transition-bin resolution 1.5 dex | **Requires new run (GATED):** artifact stores aggregates only, no per-galaxy masses; re-binning needs `source_sample` CSV, which is a live runs-tree path outside the H13 snapshot scope — fail-closed here |
| **Emission-line S/N≥3 selection** — removes passive massive galaxies, inflating high-mass AGN/quenched fractions among survivors (SUP:136's own caveat, grade C) | **Requires new run (GATED):** quantifying needs the parent DR17 catalog (network/DB). Offline, the caveat is already correctly worded |
| **AGN definition breadth** — B uses the broad class; the transition-bin co-peak could shift under the stricter definitions in SUP:147 | **Addressable with current artifacts (how):** prose sensitivity note via SUP:147's 0.136–0.418 bracket; per-definition mass curves need a re-run (GATED) |
| **No per-bin counts / SEs** (T3) | **Requires new run (GATED):** trivially cheap to emit (counts per bin) but artifact-side |
| **"Quenched" ≡ low catalog-sSFR proxy** — catalog sSFR is fiber/aperture-based and morphology-uncontrolled (FLG:74 states this for the flagship statistic; applies identically here) | **Addressable with current artifacts (how):** keep SUP's "low catalog-sSFR" renaming (T4); physical quenching verdicts GATED on gas fractions/baryon deficits per B's `full_proposal_requires` |

---

## 5. Falsifiable predictions & next analyses (dependency-ordered; all runner/network/DB actions GATED)

1. **[offline, prose-only — no gate]** Add a one-sentence cross-reference in each subsection (SUP:114 ↔ SUP:136) stating that no shared mass threshold links the two notes and that A carries no mass axis / B no kinematics — freezing §3's finding into the atlas so a future "regenerator" cannot stitch a partition narrative. Also pre-empt T1 with a footnote if −1.391 ever surfaces. *(Any numeric strings copied verbatim per RCA §5.)*
2. **[GATED: offline re-run against a snapshotted copy of `analysis_sample_bpt.csv`]** Re-emit B with per-bin counts + binomial SEs and 0.25-dex uniform bins from 10.5–12.5. **Prediction P1:** the quenched-fraction 0.5-crossing lands at log M★ ≥ 11.0 (i.e., the coarse bin did not hide a crossing in 10.5–11.0 — falsified if the 10.75–11.0 sub-bin already exceeds 0.5, since bin-4's aggregate 0.393 leaves room for an internal gradient). **Prediction P2:** AGN incidence in 11.0–11.5 exceeds bin-4's 0.260 (falsified → the "peak" was top-edge accumulation, T2 realized).
3. **[GATED: same re-run]** Emit B's curves for each SUP:147 tracer definition. **Prediction P3:** the co-peak bin is definition-stable (all definitions peak in the top bin) even though amplitudes swing ~3×; falsified if any definition peaks at 10.5–11.0, which would tie the "transition mass" to tracer choice rather than to the denominator.
4. **[GATED: external data — group/halo catalog crossmatch, no network from this lane]** Attach halo masses to the 4,440 high-excitation targets. **Prediction P4:** if the B-bin boundary (log M★ = 11.0) marks a genuine escape→recycling changeover, the fraction of outflow *non-escapers* (v_out < v_esc) among high-excitation AGN rises discontinuously across it; a smooth trend in v_out/v_esc across 11.0 falsifies the partition reading — which cycle-5 prose (correctly) never made.
5. **[GATED: IFU + multiphase campaign, the artifacts' own `full_proposal_requires`]** Resolved v_out per phase vs halo v_esc for the 4,440; gas fractions + baryon deficits per mass bin for B. This is the only level at which "does the transition mass partition escape vs recycling" becomes an empirical question rather than a category error on the present data.

**Stretch (cycle-6/7 supplement diff) — not executed:** remaining time inside the 04:45Z cap was reserved for receipt + marker; recorded as not-run in the receipt rather than half-done.

---
*Produced by lane h13. Only write area: `h13-outflow-transition-synthesis/`. Inputs read: the nine hash-pinned files plus nothing else; H5 subdir touched only at the two pinned artifact paths. No network, no git, no runner/DB/live-tree access.*
