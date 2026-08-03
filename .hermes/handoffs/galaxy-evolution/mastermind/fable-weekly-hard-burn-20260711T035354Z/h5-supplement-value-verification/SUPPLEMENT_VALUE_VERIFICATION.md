FABLE_HARD_BURN_H5_VALUE_VERIFICATION_20260711T035354Z

# H5 — Value-level verification of the seven remaining topic artifacts against the supplement prose snapshot

Burn `fable-weekly-hard-burn-20260711T035354Z`, lane H5. Executes rollup follow-up item 5 (P1 receipt follow-up queue #6): full value-level verification of the seven topic artifacts that P1 custody-verified but did not value-verify. Written ≈2026-07-11T04:25Z.

## TL;DR

**Zero drift. Zero unexpected absences. Zero manifest gaps.** All 138 numeric values extracted from the seven artifacts either surface in the cycle-05 supplement prose as correct nearest-roundings / exact strings (104 PASS) or are absent for an explainable, expected reason (34 ABSENT — standard errors, k/n counts behind quoted fractions, interior bins under span-only quoting). Every surfaced value is already covered by `INVARIANT_MANIFEST.json`; the **manifest add-candidate list is empty**. Three machine-flagged drift candidates were adjudicated and all three dismissed with evidence (§5). The two canon rounding anomalies P1 found (`-1.283`, `2.830`) remain the only artifact↔canon deviations in the corpus — **neither involves these seven artifacts**. Stretch: the flagship cross-references only shared denominator counts (60,000; 8,146), all correct and manifest-covered (§8).

## 1. Scope and inputs (custody chain)

The two topic artifacts P1 already value-verified (RCA §1, §3): the flagship pilot `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json` and `m3_p3_simulation_validation/analysis_results.json`. The remaining SEVEN, verified here (custody sha256 from the hash-verified `REAL_DATA_SOURCE_CUSTODY.json`, recomputed on the live originals at 04:04:22Z — all matched — then snapshotted into `sources-snapshot/` and re-verified byte-identical):

| artifact (`…/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/<slug>/analysis_results.json`) | custody sha256 (recomputed = pinned) |
|---|---|
| m1_rp2_environment_quenching | `c0421620f67f3c227955affa3f4c1876cb85f8b31874d219f2cd2e35a7f9cec0` |
| m1_rp3_maintenance_heating | `06291f82c3fbe0f7fe84f7249568882ca4fa44972bcc25a55e367ef1fdcc7e6e` |
| m2_p1_outflow_escape_recycling | `44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210` |
| m2_p2_radio_jet_environment | `4e1ff701bb5b98af4945d5adad2e543e00005e1ab3907e8fae7d15e70c93e351` |
| m2_p3_feedback_transition_mass | `204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67` |
| m3_p1_multiphase_census | `e711563011102657b6d5cab279c1b2ab7ed087dfc734e50932ad4edfe90d0683` |
| m3_p2_gas_depletion_efficiency | `42965b6f359c23b56098f5f9845561f4a4a2ba81e1e00df09fbae4acf3bcc2d9` |

Prose side: the P1 snapshot copy of the cycle-05 supplement (`supplementary_denominator_atlas.tex`, sha256 `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71`, recomputed = pinned; all line numbers below refer to this snapshot). Manifest: `INVARIANT_MANIFEST.json` (`f4eb857e…`, verified; 105 entries, 82 targeting the supplement). Cycle-05 is the manifest's own base document, so the meaningful question here is artifact→prose fidelity (did the prose round the artifacts correctly?), the exact mechanism-check P1's RCA calls for.

## 2. Method (scripted; `tools/verify_values.py` + `tools/adjudicate.py`)

1. **Extraction** — recursive walk of each artifact JSON: every int/float leaf, plus every numeral embedded in string fields (`result_bullets`, bin labels), excluding identifier/path fields (`figure_pdf`, `source_sample`, `slug`, `card_id`, `run_id`, `method`). 138 values total.
2. **Prose tokenization** — every standalone numeric token in the supplement with line numbers; LaTeX-aware (`8{,}146`, `\(-11.53\)` signs, `--` range dashes ≠ minus), identifier-guarded (tokens inside sha256 hashes, run IDs, ordinals like `10th` are excluded).
3. **Matching** — per artifact value: exact string, exact numeric, nearest-rounding at the prose token's displayed precision (Decimal HALF_UP and HALF_EVEN both accepted; no tie cases occurred), grouping variants, ×100 percent form, and |v| magnitude with verbal direction ("0.66 dex **lower**" for −0.6586).
4. **Near-miss net** — any prose token within 2 ulp of the value at the token's precision that is NOT a correct rounding → drift candidate for adjudication.
5. **Adjudication** (documented rules + explicit per-occurrence overrides in `tools/adjudicate.py`): in-section matches valid; out-of-section matches valid only for semantically unambiguous shared quantities (exact comma-grouped denominator counts; the L169 across-mass-bins span endpoints whose referent P1's RCA §2.3 established; shared mass-bin edges); bare percent-form coincidences dismissed (they turned out to be ARA&A bibliography volume numbers at L217/227/228 and S/N≥3 thresholds).
6. **Manifest cross-check** — every valid occurrence (line, surface form) tested for coverage by a manifest entry (`file` = supplement, line ∈ `lines`, surface form ⊆ `exact_string`).

Raw and adjudicated evidence: `RESULTS_RAW.json`, `RESULTS_ADJUDICATED.json` (per-value occurrence lists with line numbers, dismissal reasons, manifest entry IDs).

## 3. Summary table (core deliverable)

| artifact | values extracted | PASS | DRIFT | ABSENT (unexpected) | manifest-covered | manifest add-candidates |
|---|---:|---:|---:|---:|---:|---:|
| m1_rp2_environment_quenching | 24 | 22 | 0 | 2 (0) | 22 | 0 |
| m1_rp3_maintenance_heating | 16 | 12 | 0 | 4 (0) | 12 | 0 |
| m2_p1_outflow_escape_recycling | 12 | 11 | 0 | 1 (0) | 11 | 0 |
| m2_p2_radio_jet_environment | 16 | 10 | 0 | 6 (0) | 10 | 0 |
| m2_p3_feedback_transition_mass | 32 | 26 | 0 | 6 (0) | 26 | 0 |
| m3_p1_multiphase_census | 26 | 14 | 0 | 12 (0) | 14 | 0 |
| m3_p2_gas_depletion_efficiency | 12 | 9 | 0 | 3 (0) | 9 | 0 |
| **TOTAL** | **138** | **104** | **0** | **34 (0)** | **104** | **0** |

"Manifest-covered" = values with at least one valid occurrence covered by a manifest entry; it equals PASS in every row, i.e. **every value that surfaces in prose is already protected by the 105-entry manifest**, occurrence-for-occurrence (zero uncovered valid occurrences across all 104).

## 4. Per-artifact findings

### 4.1 m1_rp2_environment_quenching (24 values → 22 PASS / 2 ABSENT)
All headline numbers surface at L92 (its Atlas-notes subsection) as correct roundings of the raw leaves: quartile fractions `0.230` (raw 0.2304) and `0.181` (raw 0.180666…), counts `3,456`/`2,710`/`15,000` exact, bootstrap CI `[0.041, 0.059]` (raw [0.04059666…, 0.059135] — both correct 3-dp roundings), LPM coefficient `0.032` ± `0.004` (raw 0.032494…, se 0.003707… — the ±0.004 is the correct rounding of the LPM se), and the explicit ×100 restatement "3.2 percentage-point" (0.032494×100 → 3.2 ✓). `15,000`/`60,000` also correct in the Atlas-summary row L59. ABSENT (expected): the two quartile binomial SEs (0.003438…, 0.003141…) — the atlas never quotes standard errors.

### 4.2 m1_rp3_maintenance_heating (16 → 12 PASS / 4 ABSENT)
L103 + summary row L60: `9,298` and `5,695` exact; fractions `0.430` (raw 0.429877…) and `0.607` (raw 0.607374…) correct 3-dp roundings; threshold `10.8` exact (also correctly cross-referenced at L158 in the m3_p2 note). ABSENT (expected): numerators k=3,997 and k=3,459 behind the quoted fractions, and both SEs.

### 4.3 m2_p1_outflow_escape_recycling (12 → 11 PASS / 1 ABSENT)
L114 + summary row L61: `4,440` exact; fraction `0.074` exact; medians `−10.14` (raw −10.140585) and `−11.53` (raw −11.53205) correct 2-dp roundings with signs correctly parsed from LaTeX `\(-…\)`. ABSENT (expected): the binomial SE.

### 4.4 m2_p2_radio_jet_environment (16 → 10 PASS / 6 ABSENT)
L125: fractions `0.509` (raw 0.508583…) and `0.367` (raw 0.366715…), CI `[0.112, 0.170]` (raw [0.111898…, 0.170216…]) — all correct 3-dp roundings; `9,298` massive-subset denominator surfaces exactly at L60/L103 (shared with m1_rp3 — same subset, valid cross-reference). ABSENT (expected): quartile k/n (948/1,864; 1,007/2,746) and both SEs — the note carries fractions + CI only.

### 4.5 m2_p3_feedback_transition_mass (32 → 26 PASS / 6 ABSENT)
L136: threshold `0.5` exact (`transition_mass_bin_quenched_fraction_gt_0p5`), transition/peak bin `[11.0,12.5]` exact, peak incidence `0.520` (raw 0.520208…) correct. The by-mass array endpoints surface at L169 in the across-mass-bins span sentence (`0.005`–`0.729` quenched, `0.003`–`0.520` AGN) — these are the min/max of exactly these arrays (raw 0.005283…/0.729233…/0.002703…/0.520208…; referent established by P1 RCA §2.3), all correct 3-dp roundings. Mass-bin edges (8.0/9.5/10.0/10.5/11.0/12.5) match the shared binning of the simulation-vector table. ABSENT (expected): the six interior-bin fractions (e.g. agn[1]=0.013751…, agn[2]=0.077341…, agn[3]=0.260288…, quenched[1]=0.025816…, quenched[2]=0.131166…, quenched[3]=0.392541…) — prose quotes only the threshold-crossing bin, the peak, and the spans.

### 4.6 m3_p1_multiphase_census (26 → 14 PASS / 12 ABSENT)
L147 + summary row L64: census span endpoints `0.136` (BPT AGN, raw 0.135766…) and `0.418` (red+emission, raw 0.418266…), ratio `3.1` (raw 3.080775… — correct 1-dp rounding), denominators `60,000`. BPT AGN k=8,146 surfaces at L32 as the flagship matched-pairs count — numerically the same set by construction (8,146 of 8,146 matched; manifest `allowed_context` confirms). ABSENT (expected): the three interior tracer fractions (high [NII]/Hα 0.191616…, high [OIII]/Hβ 0.316983…, low-sSFR+emission 0.206833…), four tracer k counts (11,497 / 19,019 / 12,410 / 25,096), and all five SEs — the note quotes span endpoints + ratio only.

### 4.7 m3_p2_gas_depletion_efficiency (12 → 9 PASS / 3 ABSENT)
L158 + summary row L65: `6,729` exact; fraction `0.549` (raw 0.548669…) correct; median `40.061` (raw 40.06117405071403) correct 3-dp rounding; offset surfaces as "0.66 dex **lower**" (raw −0.658585… — magnitude + verbal direction, correct). ABSENT (expected): k=3,692, the SE, and the artifact bullet's own 2-dp string `40.06` — see §5.3.

## 5. Drift-candidate adjudications (all dismissed; RCA-style)

The near-miss net flagged three candidates. None survives:

### 5.1 m2_p3 `agn_fraction_by_mass[3]`=0.260288… vs L136 `0.5` — FALSE POSITIVE
L136's `0.5` is the artifact's own transition **threshold** ("first stellar-mass bin with low-sSFR fraction above 0.5"), verbatim from `transition_mass_bin_quenched_fraction_gt_0p5` and `result_bullets[0]`. The flagged bin-4 fraction is never quoted in prose; the 1-dp tolerance window (±0.2) is simply wide enough to net the threshold token. No drifted digits exist on either side.

### 5.2 m2_p3 `quenched_fraction_by_mass[3]`=0.392541… vs L136 `0.5` — FALSE POSITIVE
Same token, same reason as 5.1.

### 5.3 m3_p2 bullet string `40.06` vs L158 `40.061` — NOT DRIFT (precision choice; P1-RCA signature)
- Artifact raw leaf: `median_log_lha_denominator = 40.06117405071403`.
- Artifact's own result bullet renders it at 2 dp: `40.06` (correct nearest-rounding at 2 dp).
- Supplement L158 renders it at 3 dp: `40.061` (correct nearest-rounding at 3 dp: 40.0611… → 40.061; HALF_UP = HALF_EVEN, no tie).
- Drifted digits: none — both strings are faithful roundings of the same raw value at different precisions; direction: prose carries one more digit than the bullet; suspected mechanism: the prose writer **re-derived from the raw leaf rather than carrying the bullet string** — exactly the data-grounded-regenerator behavior P1's RCA §3 established (E1–E5). Here the re-derivation is benign (no canon string exists at 2 dp for this quantity in the supplement), but it is a live instance of the mechanism the verbatim-carry rule (RCA §5) exists to police: had the manifest pinned `40.06`, this would have been a D1-style audit failure.
- Manifest status: the L158 row is covered by a supplement manifest entry containing `40.061`; consistent. No action needed; no add-candidate.

**Confirmed DRIFT findings: 0.** For completeness, every dismissed coincidence is recorded with its reason in `RESULTS_ADJUDICATED.json` (e.g., L92 `0.004` = LPM SE vs binomial SE referent; L93 `0.02` = redshift-slice edge; L217/L227/L228 tokens = ARA&A volume numbers 51/50/52 in bibitems).

## 6. Manifest cross-check and add-candidate list

- 82 of the manifest's 105 entries target the supplement; their line set covers every line where a valid occurrence of the seven artifacts' values appears (L59–66 summary rows, L91–93, L103, L114, L125, L136, L147, L158, L169, plus the shared-count lines).
- Occurrence-level check: **all 104 surfaced values are covered; zero valid occurrences lack a manifest entry.**
- **Add-candidate list: EMPTY.** The only un-manifested tokens the sweep touched were the bibliography volume-number coincidences (correctly outside the manifest's scope). The 34 ABSENT values are not add-candidates by definition (nothing in prose to pin); if a future cycle starts quoting SEs, k/n counts, or interior bins, those additions must register in the manifest per RCA §5.3.
- Note for the GATED manifest-extension follow-up (P1 queue #3): this sweep independently re-confirms the manifest's supplement coverage is complete for the seven topics — extending the runner's audit list with the manifest would protect every one of these 104 surfaced values.

## 7. Prose-side numerals not sourced from these artifacts (informational)

The topic sections also contain numerals that do not originate in the seven artifact JSONs and were therefore out of scope: the L22 selection-context diagnostics (`249,917` parent count, `24.0%` cache coverage — manifest-covered), the L93 fiber-collision redshift window `0.02<z<0.12` (pilot selection config), and the m3_p3 simulation-vector table L176–190 (P1-verified territory). No unexplained numerals were found inside the seven topic subsections.

## 8. Stretch — flagship cross-references of the seven artifacts

Same sweep run against the flagship snapshot (`rp1_flagship_polished.tex`, `63b3920e…`, hash re-verified): of the 138 values, exactly 17 surface — every one a shared-denominator count, every one exact and manifest-covered: `60,000` (sample_rows / n for all seven topics, 11 occurrences across L13–L78) and `8,146` (≡ m3_p1's BPT AGN count = the flagship matched-pairs set, L13/36/39/57/65/74). The other 121 values are absent as expected — the flagship is the RP-1 paper and does not quote topic-specific atlas values. **Zero drift; zero unexpected cross-references.**

## 9. Follow-up queue (GATED — no action taken by this lane)

1. GATED — nothing new to gate from this sweep: no drift, no add-candidates, no canon inconsistencies found among the seven artifacts.
2. GATED (reinforces P1 queue #3/#4) — the §5.3 precision-choice instance is fresh evidence that prose phases re-derive from raw artifacts; the verbatim-carry rule + manifest handoff remain the right fix and now demonstrably cover all nine topic artifacts' surfaced values.

Evidence files: `RESULTS_RAW.json`, `RESULTS_ADJUDICATED.json`, `tools/verify_values.py`, `tools/adjudicate.py`, `sources-snapshot/` (seven hash-verified artifact copies). Custody, poll log, and safety attestation: `H5_RECEIPT.md`.

FABLE_HARD_BURN_H5_VALUE_VERIFICATION_20260711T035354Z
