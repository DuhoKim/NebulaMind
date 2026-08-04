# C41 Track-B Shape-2 T5 final receipts

Lane: `c41-trackb-shape2-mzr-20260804T1452K`
Receipt author: Tori
Receipt run: 2026-08-04 18:29 KST
Result: **PASS — SHAPE-2 MEASUREMENT RECEIPTED**

This file receipts the reviewed real-measurement pipeline, its frozen contract/forecast inputs, the
real run outputs, and Kun's script and forensic reviews. It closes T5 custody; it does not upgrade the
scientific outcome beyond the recorded no-verdict result.

## SHA-256 measurement-artifact table

One `shasum -a 256` result per required artifact, one line each:

```text
a3a7529802beac74c8ac7b5f8969e17a38a49313c6fc5b287fbf767246507518  t3_real.py
f9b671aa0fa6915f4762bf48b24bcb629be8cb0c92e2b89f08d28f7cbe3e3fd6  T3_REAL_RESULTS.json
cfecf77e25a96e6e1855979cb6139ac8b119ca1a7024b4dcf6324490d6b2caaa  T3_REAL_SAMPLE.jsonl
45ffb83fbe761739c83ec5f9eb04edab17ef492b54dd97e3d8cb5863a1d342e1  T3_REAL_LOG.txt
e9da31edec618806323e6db731632f208b83916bd1739616b069db7a03ab6d41  KUN_SCRIPT_REVIEW.md
5215ddeb42c724df84a6ceb78a3370f09b233826a342f5df0fba7b13cecc3e43  KUN_T4_REAL_FORENSICS.md
61d48d22d34a2aed5fa1385a76afb04bb5aa6ac2f074c9b1b099961f99b860ec  T2A_FORECAST_FROZEN.json
5e35fc22a9044e9bab0292ce02bef2f75ea90e0e5a6a5c8ce778863a604cf30b  T2A_FORECAST_FROZEN_V2.json
865f1fccd828a804aa24037baf995f51a2d96177fe9fe52c5c98dd219bce13b0  APRIME_PIPELINE_FROZEN.md
4b2030a12f886db96ec1318ccb99805e753f0fb30ced8e1d543d54d1a7dbc015  T2B_CONTRACT_SEMANTICS.md
f3577b56a5dbba8f149ae9359c116670a18cbe7f94ede3f9fd1ba91b3f0afc1d  T2B_AMENDMENT_RULING.md
```

## Mechanical checks

All checks were re-executed from the live lane files. Machine-readable details are in
`_tmp_tori_t5_receipt_check.json`; the checker is `_tmp_tori_t5_receipt_check.py`.

### 1. Results-bin accounting equals the five usable anchors

PASS.

- `T3_REAL_SAMPLE.jsonl`: 95 parseable rows.
- Contract-grade usable anchors (`exclusion == null` and `oh_direct` present): 5.
- Results bin counts:
  - `M_star_bin_8_9`: N=2
  - `M_star_bin_9_10`: N=1
  - `M_star_bin_gt_10`: N=0
- Sum of binned N: 3.
- `per_class_counts.below_bin_floor`: 2.
- Recomputed usable rows with `logmass < 8.0`: exactly 2 — `ERO_04590` at 7.60 and `ERO_10612`
  at 7.78.
- Equality: binned N 3 + below-bin-floor 2 = usable-anchor rows 5.
- `per_class_counts.oh_rows_total`: 5.
- `forecast_vs_actual.actual_usable_anchors_total`: 5.
- `forecast_vs_actual.actual_per_bin` exactly matches the results-bin N values.

No usable anchor is unaccounted after Kun correction C1.

### 2. Forecast block reproduces both frozen files

PASS.

The two nested objects in `T3_REAL_RESULTS.json` were parsed and compared key-for-key and
value-for-value against the frozen JSON files:

- `forecast_vs_actual.frozen_forecast_v1` == parsed `T2A_FORECAST_FROZEN.json`.
- `forecast_vs_actual.frozen_forecast_v2` == parsed `T2A_FORECAST_FROZEN_V2.json`.
- V2's `v1_sha256` equals the live V1 artifact SHA:
  `61d48d22d34a2aed5fa1385a76afb04bb5aa6ac2f074c9b1b099961f99b860ec`.
- The V1/V2 IDs, per-bin forecasts, expected totals, precision fields, thresholds, revision cause,
  notes, and V1 pin all match their frozen sources without semantic substitution.
- The block explicitly discloses that V1 was frozen pre-fetch, V2 was re-frozen under Amendment
  Ruling 3, and both remain receipted.

This is structural verbatim fidelity of the JSON content; whitespace/indentation differences in the
embedding are not treated as content changes.

### 3. Kun C1 and C2 are applied

PASS.

- **C1 — below-bin-floor accounting:** `below_bin_floor = 2` is present; the note names both verified
  low-mass anchors and states that they sit below the frozen 8.0 edge. The five-anchor accounting now
  closes exactly.
- **C2 — forecast/null framing:** `forecast_vs_actual` contains both frozen forecast objects, the
  supersession disclosure, actual total/per-bin counts, and the instantiated T2b §6 null statement.
  The statement gives V1≈25, V2≈87, actual contract-grade N=5, states that no bin reaches the
  three-anchor minimum, and licenses no deficit verdict.
- `KUN_T4_REAL_FORENSICS.md` explicitly defines both corrections and ends with
  `KUN_T4REAL_COMPLETE_20260804`.

Neither correction changes a measured Te/O-H value; C1 repairs accounting and C2 repairs framing.

### 4. Seven-run receipt and Kun review-marker chain

PASS.

`T3_REAL_LOG.txt` contains exactly seven `t3_real.py START` records. The run disposition is:

- 3 honest S1 failures, each explicitly logged as `HONEST_FAILURE`;
- 1 started/incomplete run during the live repair sequence;
- 3 completed runs with `t3_real.py DONE`;
- 7 console receipts: `t3_real_console.log` through `t3_real_console7.log`.

`KUN_SCRIPT_REVIEW.md` contains the complete review chain:

1. Initial full review: `APPROVED_WITH_EDITS` with B1–B3, R1–R4, and advisories.
2. Delta re-review: `SCRIPT_APPROVED`, confirming the blocking/required edits.
3. Micro-delta 1: S1 v2 global enumeration — approved.
4. Micro-delta 2: sibling-z admission/resolution — approved.
5. Micro-delta 3: v4 query-layer/unquoting repair — approved.
6. Micro-delta 4: v5 per-candidate fetch guards — approved.
7. Micro-delta 5: v6 flux/error column-pick repair — approved.
8. Micro-delta 6: v7 sibling-mass join — approved.

All six micro-delta sections contain an approval verdict, and the chain ends with
`KUN_S2V7_COMPLETE_20260804`.

### 5. Frozen pipeline and contract chain

PASS.

- `APRIME_PIPELINE_FROZEN.md` records the A′ components, including auroral S/N≥5, ICF(O)=1,
  Cardelli/CCM89, fixed density, seed 42, and 1000 draws.
- `T2B_CONTRACT_SEMANTICS.md` ends with `LANA_SHAPE2_T2B_COMPLETE_20260804`.
- `T2B_AMENDMENT_RULING.md` ends with `LANA_SHAPE2_RULING_COMPLETE_20260804`, authorizes exactly one
  pre-result V2 re-freeze, and requires both forecasts to remain receipted.
- The result status is `REAL_COMPLETED`; A4 remains `not-computable-v1` rather than carrying an
  improvised SFR result.

## Full Shape-2 timeline from gate to T5

All times below are filesystem mtimes rendered in KST (`Asia/Seoul`). They are ordered by observed
mtime; embedded prose dates were not substituted for file custody times.

| Milestone | Mtime evidence | Time (KST) | Receipt |
|---|---|---|---|
| Shape-2 gate opens | study history + `GORU_T1_BRIEF.md` | 2026-08-04 14:52:56 | Duho-gated Track-B Shape-2 lane begins. |
| T1 assembly freeze/recon | `T1_ASSEMBLY_RULES.md` through `GORU_T1_REPORT.md` | 14:53:19 → 14:59:39 | Metadata reconnaissance, manifest, and fragmented-catalog verdict landed. |
| Design adversarial gate | `KUN_DESIGN_REFUTATION.md`; patched `MEASUREMENT_DESIGN_V1.md` | 14:55:56 → 14:58:10 | `DESIGN_SOUND_WITH_PATCHES`; six design patches folded into v2. |
| T2b semantics freeze | `T2B_CONTRACT_SEMANTICS.md` | 15:00:18 | Declared-scale, class, channel, lensing, and null semantics frozen. |
| T2a machinery + V1 forecast | T2a brief/join/conversion/forecast/report | 15:01:04 → 15:03:07 | V1 forecast frozen pre-fetch at SHA `61d48d22…`. |
| Initial T3 attempt | `GORU_T3_BRIEF.md`; `t3_compute.py` | 15:09:31 → 15:13:24 | First executor path begins; contract conflicts stop honest completion. |
| Pre-result amendment | `T2B_AMENDMENT_RULING.md` | 15:34:28 | Class A′ accepted, lensing rule retained, one V2 re-freeze licensed. |
| A′ pipeline + V2 forecast freeze | `APRIME_PIPELINE_FROZEN.md`; `te_pipeline.py`; V2 forecast | 15:38:00 → 15:38:19 | Pipeline and revised eligibility forecast frozen before resumed fetch. |
| Resumed/mock T3 chain | `t3_resume.py` through `T3_RESULTS.json` and `GORU_T3_REPORT.md` | 15:38:38 → 15:57:30 | Mock/stencil path landed and was preserved for audit, not accepted as real. |
| Mock forensics | `KUN_T4_FORENSICS.md` | 16:07:18 | Fabricated/stenciled result path rejected; real reviewed-script protocol required. |
| Real run 1 | `t3_real_console.log` | 16:43:23 | Honest S1 failure. |
| Prediction scope artifacts | prediction entries + Lana report | 16:44:40 → 16:45:05 | Prediction ledger/scope completed during real-pipeline iteration. |
| Real run 2 | `t3_real_console2.log` | 16:52:30 | Honest S1 failure. |
| Real run 3 | `t3_real_console3.log` | 16:56:49 | Honest S1 failure. |
| Real run 4 | `t3_real_console4.log` | 17:10:00 | Enumeration advanced; run did not reach a terminal DONE/HONEST_FAILURE marker. |
| Real run 5 | `t3_real_console5.log` | 17:23:16 | Completed but yielded zero A′ O/H rows. |
| Real run 6 | `t3_real_console6.log` | 17:43:01 | Completed with five rows before the mass-join delta. |
| Reviewed script v7 frozen | `t3_real.py`; `KUN_SCRIPT_REVIEW.md` | 17:43:49 → 18:00:17 | Initial review, delta approval, and all six micro-delta approvals complete. |
| Real run 7 final outputs | sample, console 7, aggregate log | 18:08:12 | 95 archived rows, five contract-grade derived anchors, full provenance. |
| Independent T4 real forensics | `KUN_T4_REAL_FORENSICS.md` | 18:15:19 | Five rows re-derived exactly; C1+C2 ordered. |
| C1+C2 result annotation | `t3_annotate_corrections.py`; corrected results JSON | 18:24:26 | Below-floor accounting and forecast/null block applied without changing measurements. |
| T5 Tori final receipt | `T5_RECEIPTS.md` | 2026-08-04 18:29 | This closure stamp; minute-resolution receipt-run time. |

## Final measurement state

- Eleven required measurement/contract/review artifacts are present and SHA-receipted.
- Five contract-grade usable anchors are fully accounted: three in frozen bins and two below the
  frozen lower bin edge.
- Both forecast versions are preserved exactly in the result block with the required supersession
  disclosure.
- Kun C1+C2 are applied; seven-run and initial-review-plus-six-micro-delta chains are complete.
- Scientific outcome remains the honest one: no mass bin reaches the pre-committed three-anchor
  minimum, so no deficit verdict is possible at contract-grade public statistics.
- T5/Shape-2 custody closes here. No prose publication, DB mutation, deployment, or git action is
  authorized by this receipt.

TORI_SHAPE2_T5_COMPLETE_20260804
