FABLE_HARD_BURN_H12_SYNTHESIS_20260711T035354Z

# H12 deep synthesis — maintenance heating (m1_rp3) + radio-jet environment (m2_p2)

Burn `fable-weekly-hard-burn-20260711T035354Z`. All inputs sha256-verified against the brief's pins before reading (see `H12_RECEIPT.md`). Line numbers refer to the hash-pinned cycle-5 snapshot files. Helper: `tools/h12_checks.py` (read-only; output reproduced in Appendix A).

## TL;DR verdict
The two artifacts are numerically consistent, share the identical massive denominator (9,298 hosts, same run, same 60k source CSV), and every prose numeric in both cycle-5 subsections is simultaneously (a) a verbatim carry of the artifact's own `result_bullets` string and (b) the exact nearest-3dp rounding of the full-precision field — so, unlike the flagship CI (`-1.283`) and sim-vector cell (`2.830`) anomalies in `RCA_NUMERIC_DRIFT.md`, **these two topics contain no latent canon/rounding inconsistency**. Jointly they *motivate* but do not *demonstrate* a single radio-mode maintenance story: A supplies the duty-cycle lever (BPT-AGN fraction 0.607 in massive low-sSFR vs implied 0.149 in massive non-low-sSFR hosts), B supplies an environment gradient (0.509 vs 0.367), and a composition model built from A alone can reproduce B's entire gradient if the massive low-sSFR share varies ≈0.48→0.78 across density quartiles — a cross-tab neither artifact provides. The prose never links the two subsections quantitatively. The joint story's causal core (anything radio) is entirely GATED follow-up.

## 1. Artifact anatomy

### 1.A m1_rp3_maintenance_heating/analysis_results.json (card `rp-3`, sha `06291f82…`)
Design in plain language: start from the shared 60,000-row SDSS DR17 emission-line analysis sample (`SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv`); cut to massive hosts log(M*/Msun) >= 10.8 (9,298 galaxies); further cut to low-sSFR by the pilot threshold (5,695; threshold value NOT stored in the artifact). Statistic: broad optical BPT-selected (AGN) fraction k/n in each subset, with plain binomial SE = sqrt(p(1-p)/n) (recomputed exact, Appendix A). No CI is stored for A. Role: optical duty-cycle *denominator* for X-ray/radio maintenance-heating follow-up — explicitly not a heating-to-cooling measurement.

Every field (units; role):
| field | value | units/role |
|---|---|---|
| card_id | `rp-3` | topic card key |
| slug | `m1_rp3_maintenance_heating` | atlas key |
| proposal_title | "Empirical duty-cycle constraints on AGN maintenance heating in massive halos" | framing |
| short_title | "Optical-AGN denominator for maintenance-heating follow-up" | framing |
| pilot_question | optical AGN fraction available as denominator among massive low-sSFR hosts | design |
| method | `packet-gated-paper-to-wiki-reconciliation` | pipeline label (see §3 tension T4) |
| run_id | `SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z` | provenance |
| source_sample | `…SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv` | parent data |
| sample_rows | 60000 (galaxies) | parent denominator |
| massive_rows | 9298 (galaxies) | massive denominator |
| massive_quenched_rows | 5695 (galaxies) | massive low-sSFR denominator |
| massive_agn_fraction | fraction 0.4298773930, k=3997, n=9298, se 0.005134069 (dimensionless) | headline stat 1 |
| massive_quenched_agn_fraction | fraction 0.6073748903, k=3459, n=5695, se 0.006470988 | headline stat 2 |
| result_bullets | 3 strings carrying `10.8`, `9,298`, `5,695`, `0.430`, `0.607` + role guard | canonical prose strings |
| interpretation_guard / full_proposal_requires | SDSS-only pilot; needs X-ray cavities/cooling L, radio jet powers, halo-selected parents, nondetection modelling | scope + GATED needs |
| figure_pdf | run-tree path `…figures/m1_rp3_maintenance_heating_figure1.pdf` | pointer (outside H12 inputs, not read) |

Derived-only quantities (not stored, implied by fields): massive low-sSFR share 5695/9298 = 0.6125; massive NON-low-sSFR AGN fraction (3997−3459)/(9298−5695) = 538/3603 = **0.1493** — the artifact's own numbers make BPT-AGN incidence ~4.1× higher in the quenched massive population.

### 1.B m2_p2_radio_jet_environment/analysis_results.json (card `p2`, sha `4e1ff701…`)
Design in plain language: same 60k parent and same 9,298 massive-host denominator; stratify by a local-density proxy into quartiles; report the BPT-AGN fraction in the high-density and low-density quartiles plus a bootstrap 95% interval on the high-minus-low difference. Quartile n's are unequal (1,864 vs 2,746) ⇒ quartile boundaries are defined on the *full* sample's density ranking, not within the massive subset (§3, C-B3). Role: environment-stratified optical denominator motivating radio/X-ray jet-coupling follow-up — explicitly not a jet-power or coupling-efficiency measurement.

| field | value | units/role |
|---|---|---|
| card_id / slug | `p2` / `m2_p2_radio_jet_environment` | keys |
| proposal_title | "Environmental dependence of radio-jet coupling efficiency in galaxy gas" | framing |
| pilot_question | does a local-density proxy modulate optical AGN fraction in massive hosts? | design |
| method | `source-first-paper-adjudication` | pipeline label (differs from A; T4) |
| run_id / source_sample / sample_rows | identical to A (60000) | shared parent |
| massive_rows | 9298 | shared massive denominator (== A) |
| high_density_massive_agn | fraction 0.5085836910, k=948, n=1864, se 0.011579320 | headline stat 1 |
| low_density_massive_agn | fraction 0.3667152221, k=1007, n=2746, se 0.009196313 | headline stat 2 |
| high_minus_low_ci | [0.1118988036, 0.1702164815] (dimensionless, bootstrap 95%) | headline interval |
| result_bullets | 3 strings carrying `0.509`, `0.367`, `[0.112, 0.170]` + role guard | canonical prose strings |
| interpretation_guard / full_proposal_requires | SDSS-only; needs radio morphology/age, cavity/shock energetics, hot-gas density, calibrated jet powers | scope + GATED needs |
| figure_pdf | run-tree path `…m2_p2_radio_jet_environment_figure1.pdf` | pointer (not read) |

Checks (Appendix A): all four fractions equal k/n exactly; all SEs are exact binomial; point diff 0.14187 sits inside the bootstrap CI, and the normal-approx CI [0.11289, 0.17085] agrees with the bootstrap [0.11190, 0.17022] to <0.001 at both ends.

## 2. Claim inventory (cycle-5 supplement `a4e3d66c…` + flagship `63b3920e…`)
Grades: **A** = numeric/string is a verbatim carry of an artifact field/result_bullet (and, where full precision exists, equals its nearest-3dp rounding — the RCA convention); **B** = derived from artifact fields, derivation shown; **C** = qualitative claim consistent with artifact fields; **X** = not supported by the artifact. Manifest = `INVARIANT_MANIFEST.json` entry id; "add-candidate" = no entry today.

### 2.A Maintenance heating (m1_rp3)
| # | claim (verbatim, supplement line) | artifact field(s) | manifest | grade |
|---|---|---|---|---|
| A1 | L40 provenance row: `Maintenance-heating denominator & …125828Z & m1_rp3…json & 06291f82…` | run_id + file identity; SHA equals my recomputed hash of artifact A | SUP-ROW-040 | A |
| A2 | L60 summary row: "…(9,298 massive; 5,695 low-sSFR)" | massive_rows, massive_quenched_rows | SUP-ROW-060; SUP-MASSIVE-N, SUP-MASSIVE-LOWSSFR-N (each ×2, L60+L103) | A |
| A3 | L103: "massive subset (log M* >= 10.8) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold" | result_bullets[0]; massive_rows; massive_quenched_rows; threshold `10.8` | SUP-MASSCUT (`10.8`, L103+L158), SUP-MASSIVE-N, SUP-MASSIVE-LOWSSFR-N | A |
| A4 | L103: "broad optical BPT-selected fraction is 0.430 in the massive subset" | result_bullets[1]; massive_agn_fraction 0.4298773930 → nearest-3dp 0.430 (deriv: 3997/9298) | SUP-BPT-FRAC-MASSIVE (note: `0.430` also a sim-vector cell L185 → occurrences_expected 2) | A (B-derivation confirms) |
| A5 | L103: "and 0.607 among massive low-sSFR objects" | massive_quenched_agn_fraction 0.6073748903 → 0.607 (3459/5695) | SUP-BPT-FRAC-MASSIVE-LOWSSFR | A |
| A6 | L103: "optical duty-cycle denominator … not a heating-to-cooling measurement" | result_bullets[2] | — (prose guard; add-candidate not needed: non-numeric) | A |
| A7 | L103: "Future physical validation requires X-ray cavity or cooling-luminosity measurements, calibrated radio jet mechanical powers, halo-selected parent catalogues, and nondetection modelling" | full_proposal_requires (near-verbatim) | — | A/C |
| A8 | L77 follow-up row "X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents" | condensed full_proposal_requires | add-candidate (table_row; Table 3 rows absent from manifest per grep) | C |
| A9 | L103: "Optical broad BPT selection primarily traces the radiative-mode denominator…" (heckmanbest2014) | no field; literature-motivated scope | — | C (consistent with guards) |

### 2.B Radio-jet environment (m2_p2)
| # | claim (verbatim, supplement line) | artifact field(s) | manifest | grade |
|---|---|---|---|---|
| B1 | L42 provenance row: `Radio-jet environment baseline & …125828Z & m2_p2…json & 4e1ff701…` | identity; SHA equals my recomputed hash of artifact B | SUP-ROW-042 | A |
| B2 | L62 summary row: "neighbor-rank-stratified broad optical BPT-selected fraction in massive hosts" | high/low_density fields exist; "neighbor-rank" naming NOT in artifact (fields say density) | SUP-ROW-062 | C |
| B3 | L125: "high-index quartile has a broad optical BPT-selected fraction of 0.509" | result_bullets[0]; 0.5085836910 → 0.509 (948/1864) | SUP-JET-HI | A |
| B4 | L125: "the low-index quartile has 0.367" | 0.3667152221 → 0.367 (1007/2746) | SUP-JET-LO | A |
| B5 | L125: "bootstrap high-minus-low interval is [0.112, 0.170]" | high_minus_low_ci [0.1118988…, 0.1702165…] → nearest-3dp [0.112, 0.170] | SUP-JET-CI (ci_interval) | A |
| B6 | L125: "does not measure radio jet power or coupling efficiency" | result_bullets[2] | — | A |
| B7 | L125: "reuses the same projected-neighbor ranking described in the relative neighbor-count baseline above" (i.e. m1_rp2's 10th-neighbor index) | NO artifact field names the density metric | add-candidate (referent invariant, RCA §5 rule 4) | **C — prose-only link; see T1** |
| B8 | L125: "Among massive hosts" (count unstated) | massive_rows 9298 (== A) | covered via SUP-MASSIVE-N at L60/L103 only | B (implicit; prose never states 9,298 here) |
| B9 | L79 follow-up row "radio morphology/age; cavity energetics; hot-gas density" | condensed full_proposal_requires | add-candidate (Table 3 row) | C |

### 2.C Flagship (both topics)
| # | claim (flagship line) | relation | grade |
|---|---|---|---|
| F1 | L19: "does not test … radio-mode maintenance heating" | matches both interpretation_guards; scope exclusion | C |
| F2 | L70: mechanistic interpretation needs supplement follow-ups (cites Supp. 5.1/5.7, not our 5.2/5.4) | consistent; note it names neighbor-rank+CO/HI, not H12 topics | C |
| F3 | L75: "integration with … radio-mode and X-ray maintenance-heating studies (best2005, fabian2012, mcnamara2007, heckmanbest2014, lamassa2013)" | motivational only; no numbers from A/B in flagship | C |

Integrity note (task 2 conclusion): every graded-A numeric above is *both* a verbatim result_bullet carry and the exact nearest-rounding of the stored full-precision value — verbatim-carry and re-derivation coincide for these topics, so the cycle-6/7 re-derivation failure mode (RCA D1/D2) cannot fire here. No X-grade claims found.

## 3. Joint synthesis — one radio-mode maintenance story?

Consistency table (values from Appendix A; line numbers = cycle-5 supplement):
| cross-check | verdict | evidence |
|---|---|---|
| Shared parent sample | AGREES | run_id, source_sample, sample_rows=60000 byte-identical across A and B |
| Shared massive denominator | AGREES | massive_rows 9298 == 9298; prose states 9,298 only in m1_rp3 (L60/L103), never in m2_p2 (L125) — artifact-backed, prose-implicit |
| B's quartile fractions vs A's overall 0.430 | AGREES (bracketing) | 0.367 < 0.430 < 0.509; implied middle-half (Q2+Q3) fraction (3997−948−1007)/(9298−1864−2746) = 2042/4688 = 0.4356 lies between the extremes ⇒ monotone-compatible |
| A internal lever | AGREES | AGN fraction 0.607 (quenched) vs implied 0.149 (non-quenched): duty-cycle concentration in quenched massive hosts |
| Composition (mediation) closure | IN TENSION (open) | B's gradient is fully reproducible from A's lever with quartile low-sSFR shares q_hi=0.784, q_lo=0.475 (overall 0.612); plausible direction (denser⇒more quenched) ⇒ B is not yet evidence of environment-modulated AGN incidence at fixed sSFR class |
| Quartile geometry | IN TENSION (informative) | massive hosts per quartile 1,864 (high) vs 2,746 (low) vs 15,000-quartile expectation 0.155×15,000≈2,325: massive hosts are UNDER-represented in the high-density quartile (12.4% vs 18.3% low) — opposite to physical clustering expectation; consistent with fiber-collision + emission-line S/N selection removing massive passive galaxies in dense fields (conditional on B7's prose-only ranking identity) |
| Prose linkage of the two topics | INDEPENDENT | m2_p2 (L124-125) links to m1_rp2's ranking, not to m1_rp3; atlas tables (L60/L62, L77/L79) juxtapose rows without any shared number; flagship mentions maintenance heating only as excluded scope (L19) and future work (L75). No number-backed sentence connects 0.607 with 0.509/0.367 anywhere in the package |
| Statistics style | AGREES | both artifacts: exact k/n fractions + exact binomial SEs; B's bootstrap CI ≈ normal-approx CI to <0.001 |

Tension list:
- **T1 (B7):** the identification of m2_p2's density proxy with the 10th-neighbor rank is prose-only; no artifact field names the metric. If the ranking ever changes upstream, L125 keeps "reuses the same ranking" with nothing machine-checkable. Add a referent invariant (RCA §5 rule 4).
- **T2:** composition confounder (row 5 above) — the joint "environment modulates the radio-mode duty cycle" reading is underdetermined by A+B; the density×sSFR×BPT cross-tab in massive hosts is the single missing table.
- **T3:** quartile under-representation of massive hosts in dense regions (row 6) is unexplained in prose; it silently shapes both B fractions.
- **T4:** the two artifacts carry different `method` labels (`packet-gated-paper-to-wiki-reconciliation` vs `source-first-paper-adjudication`) — pipeline provenance labels, not statistical methods; harmless but worth normalizing before the atlas claims a uniform method.
- **T5:** neither artifact contains any radio observable; "radio-jet"/"maintenance-heating" in both titles is motivational framing carried into section headers — the prose guards (A6, B6, F1) currently keep this honest.

Verdict: **coherent as a two-denominator scaffold, not yet a single evidenced story.** A and B agree everywhere they overlap and jointly sharpen the follow-up question, but the link between duty cycle and environment runs through an unmeasured composition term, and the radio-mode content is 100% GATED.

## 4. Confounders
Per topic; each marked addressable-with-current-artifact (how) or requires-new-run (GATED).
- **m1_rp3 / radiative- vs jet-mode selection:** BPT selects radiative-mode AGN; maintenance heating is jet-mode. Not addressable with current artifact → GATED (radio cross-match, e.g. calibrated jet powers per full_proposal_requires).
- **m1_rp3 / unstated low-sSFR threshold:** artifact stores counts but not the threshold. Addressable only by re-deriving from `analysis_sample_bpt.csv` (custody-inventoried but outside H12 inputs) → GATED run; until then A3's "pilot threshold" is definitionally opaque.
- **m1_rp3 / emission-line S/N selection:** massive passive hosts are preferentially excluded, inflating the quenched-AGN fraction's denominator relevance. Prose already caveats (L22, L68); quantification needs parent-cascade receipts → GATED.
- **m2_p2 / composition (quenching) mediation:** addressable in arithmetic with current artifacts (done here: q_hi=0.784 / q_lo=0.475 bounds); resolution needs the cross-tab → GATED run on existing CSV.
- **m2_p2 / environment metric validity:** fiber-collision-biased projected rank, no velocity window (per L93 for the sibling entry, prose-linked via B7) → physical density GATED (group catalogs, collision corrections).
- **m2_p2 / mass-density covariance inside the massive bin:** quartile mass distributions unknown; a mass gradient across quartiles would mimic an environment effect given the steep mass-AGN relation. GATED (mass-matched quartiles on existing CSV).
- **Both / stacking-free single-survey pilot:** fixed 60k specObjID cap inherits plate/sky structure (L22); both fractions are conditional denominators, not population rates. Addressable only by re-selection → GATED.

## 5. Falsifiable predictions and next analyses (dependency-ordered; all runs GATED — no runner/network/DB action taken in H12)
1. **N1 (existing CSV, first):** density-quartile × sSFR-class × BPT cross-tab in the 9,298 massive hosts. Prediction P1: if composition-driven, measured low-sSFR shares ≈0.78 (Q4) and ≈0.48 (Q1); if shares are flat ≈0.61, the AGN-fraction gradient survives at fixed sSFR class and B becomes real environment modulation. Either outcome is decisive — this is the highest-information next table.
2. **N2 (same run):** middle-quartile AGN fractions. Prediction P2: Q2+Q3 pooled fraction = 2042/4688 = 0.4356 exactly (identity), and monotone ordering Q1<Q2<Q3<Q4 if the gradient is intrinsic.
3. **N3 (needs N1):** mass-matched re-stratification of quartiles. Prediction P3: gradient shrinks but persists (>2×SE_diff≈0.030) if environmental; collapses if mass-driven.
4. **N4 (external, network — GATED):** radio cross-match (FIRST/LoTSS-class). Predictions P4: radio-AGN fraction among massive low-sSFR hosts exceeds the matched non-low-sSFR fraction; and rises with density at fixed sSFR class if jet-mode couples to environment — directly testing whether the optical 0.607 duty-cycle denominator translates to jet-mode incidence.
5. **N5 (external — GATED):** X-ray cavity/cooling-luminosity subsample per A7; falsifier: no excess cavity incidence among the 0.607 subset ⇒ optical duty cycle is a poor maintenance-heating proxy.
6. **N6 (manifest hygiene, no run):** add-candidates from §2 (B7 referent invariant; Table-3 rows A8/B9) → integrator, per RCA §5 rule 3/4.

## Appendix A — helper output (`tools/h12_checks.py`, run 2026-07-11T04:40Z)
All equality checks True; abridged key lines:
- A: 3997/9298 = 0.4298773930 → 0.430; SE exact binomial 0.005134069. 3459/5695 = 0.6073748903 → 0.607; SE 0.006470988. Implied non-low-sSFR 538/3603 = 0.1493.
- B: 948/1864 = 0.5085836910 → 0.509 (SE 0.011579320); 1007/2746 = 0.3667152221 → 0.367 (SE 0.009196313); CI [0.1118988036, 0.1702164815] → [0.112, 0.170]; diff 0.14187, normal-approx [0.11289, 0.17085].
- Cross: massive_rows equal; run_id/source_sample/sample_rows equal; middle-half 2042/4688 = 0.4356; quartile shares 0.124/0.183 vs overall 0.155; composition q_hi 0.784, q_lo 0.475 vs overall 0.612.

Stretch item (cycle-6/7 diff) not attempted — hard cap reached. Status basis for receipt: core tasks 1-5 complete.
