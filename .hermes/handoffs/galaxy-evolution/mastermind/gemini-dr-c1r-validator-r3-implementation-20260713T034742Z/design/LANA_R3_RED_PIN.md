# LANA_R3_RED_PIN — exact Gate A r3 RED pin (A-P1)

Packet: `gemini-dr-c1r-validator-r3-implementation-20260713T034742Z` · Lane: Lana (A-P1, high reasoning). Coordinator: Hwao.
Status: **RED pin for review. Hwao countersign REQUIRED before any implementation (A-P3).** No tests/code/verdicts written. Offline; no network/live/browser/git/DB/dashboard action.

## Diagnostic disclaimer (binding, read first)
This pin predicts a **diagnostic re-scoring of a PRE-r3 body** (the sealed C1r capture) under the proposed r3 rules. It is **mechanical only**: it does not verify whether any paper supports a claim, whether quoted science is correct, whether comparison labels are defensible, or whether uncertainty handling is faithful. Expected-new findings are legitimate artifacts of re-scoring an old body under new rules — they are **pinned, not discovered**. The sealed C1r run remains **FAIL_CLOSED**; nothing here retro-accepts it or releases any quarantine.

## Inputs of record (custody, from `receipts/KUN_INPUT_CUSTODY_RECEIPT.md`, GREEN)
- Contract: `../gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/design/CONTRACT_R3_DRAFT.md` sha256 `0ac73b70…03bd9` (§D1–D6 + standalone r3).
- Repaired v2 residue: `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/readjudication/validator_result_v2.json` sha256 `ad4d035b…3d52`; `structured_capture_v2.json` sha256 `e26819db…e3e9`; `READJUDICATION_SUMMARY.json`; `RESIDUE_REPORT.md`.
- Sealed body/HTML/spec: `prompt/C1r.md` `fffac44f…e1ef`; `runs/c1r/rendered_body.html` `78ed129c…2bbc`; `body.md` `8a130c5a…bc00`.
All pinned bytewise; any mismatch at any phase ⇒ STOP (Gate A stop condition 1).

---

## 1. Baseline v2 residue (pinned exactly from `validator_result_v2.json`)

**17 deterministic FAIL + 73 MANUAL + 4 PASS** (overall FAIL). The 17 (canonical `clause:code @ source_refs`):
- `C2:SENTINEL_FORMAT_DEFECT` @ `[table_row_7, 2]` — FIRE/FIRE-2 feedback cell `NONE_FOUND.`
- `C4:UNCITED_CELL_CLAIM` ×8 @ `[table_row_14..21, 2]` — Section-2 Result cells (TNG, EAGLE, SIMBA, FIRE, ROMULUS, ASTRID, FLAMINGO, BAHAMAS)
- `C6:UNLABELED_COMPARISON` ×6 @ `[table_row_5,3][table_row_6,3][table_row_9,3][table_row_10,3][table_row_11,3][gap_line_1]` — 5 S1 emergent (EAGLE, SIMBA, ASTRID, FLAMINGO, BAHAMAS) + GAP1
- `C6:MISSING_QUALIFIER` ×1 @ `[table_row_6, 2]` — SIMBA ~10% accretion fraction
- `C7:C7_INTEGRITY_FAILURE` ×1 @ `[]` — 12 orphans {2,5,8,9,13,16,18,23,24,29,31,33}, 9 duplicate rows, 46 blank short names, 14↔29 near-dup, 0 inline-only.

Manual 73: `C3:UNCERTAINTY_CHECK`×18, `C4:CITED_CELL_CLAIM_REVIEW`×40, `C4:CITED_CLAIM_REVIEW`×5, `C4:CITATION_QUALITY_REVIEW`×1, `C4:SOURCE_FIDELITY_REVIEW`×1, `C6:COMPARISON_LABEL_REVIEW`×8.

Capture facts used below (from `structured_capture_v2.json`, schema `NM_GEMINI_RENDERED_DOM_V2`): S1 rows = `table_row_4..11` (cols 0 sim / 1 calibration_target / 2 feedback_params / 3 emergent / 4 notes); S2 rows = `table_row_14..21`; GAP units = `gap_line_1..4` (`source_lines` 263–266, `gap_index` 1–4, **no parent-paragraph field**); ledger = 46 rows / 37 indices in `chip_index_occurrences`.

---

## 2. RED test families (order D5 → D4 → D2 → D1 → D3), exact codes/statuses

One family per D-item; each has positive (r3-shaped, passes) and negative (sealed or synthetic, fails) fixtures. Primary fixture = real sealed HTML/capture; synthetic fixtures for positive paths only. No assertion weakenable without logged Lana+Hwao sign-off.

| Family | Negative fixture ⇒ expected | Positive fixture ⇒ expected |
|---|---|---|
| **D5** one-GAP-per-paragraph | merged `<p>` holding 4 `GAP:` lines ⇒ `C2:GAP_MULTIPLE_PER_PARAGRAPH` FAIL ×1 (evidence = the 4 gap_lines' shared parent) | 4 separate `<p>`, one `GAP:` each ⇒ no D5 finding |
| **D4** ledger integrity | sealed ledger ⇒ `C7:C7_INTEGRITY_FAILURE` FAIL ×1 (12 orphan / 9 dup / 46 blank / 0 inline-only) + `C7:C7_NEAR_DUPLICATE` MANUAL ×1 (14↔29) | unique/named/index-bidirectional ledger ⇒ `C7` PASS; `abs\|html\|pdf` variants of one arXiv id ⇒ merged (unique); `article` vs `article-abstract` ⇒ `C7_NEAR_DUPLICATE` MANUAL, never auto-merge |
| **D2** numeric-fraction qualifier | SIMBA `feedback_params` "~10%" with no four-qualifier syntax ⇒ `C6:MISSING_QUALIFIER` FAIL ×1 | `TRACER=MODEL_PARAMETER; SELECTION=NOT_APPLICABLE; DENOMINATOR=<...>; REDSHIFT=NOT_APPLICABLE` ⇒ MANUAL (`SEMANTIC_QUALIFIER`), not FAIL; observational fraction w/ full real qualifiers ⇒ MANUAL; fraction/incidence word with no numeric value ⇒ no finding |
| **D1** typed comparison scope | un-prefixed S1 col-1/col-2 calibration-target-description cell ⇒ `C6:MISSING_CALIBRATION_TARGET_PREFIX` FAIL (see §4); un-tokened S1 emergent (col-3) comparison ⇒ `C6:UNLABELED_COMPARISON` FAIL | `CALIBRATION_TARGET_DESCRIPTION:`-prefixed col-1/col-2 cell ⇒ exempt, no finding; col-2 cell with no observation reference ⇒ no prefix required, no finding; emergent cell with a comparability token ⇒ MANUAL (`COMPARISON_LABEL_REVIEW`) |
| **D3** S2 citation authority | S2 row with an **empty** dedicated Citation cell ⇒ `C4:EMPTY_CITATION_CELL` FAIL (hard) | S2 row: populated/resolved Citation cell + uncited Result cell ⇒ **no** `UNCITED_CELL_CLAIM` (removed) and `C4:CITED_CELL_CLAIM_REVIEW` MANUAL ×1 (row-citation review) |

Plus **T-INT** (full sealed-capture re-adjudication vs §3 multiset), **T-DET** (two byte-identical runs), and **T-CUST** (immutable-input hashes) — unchanged discipline from the repair packet.

---

## 3. Predicted v3 finding multiset on the sealed pre-r3 capture (order-independent)

### 3a. REMOVED vs v2 (by D3)
- `C4:UNCITED_CELL_CLAIM` ×8 @ `[table_row_14..21, 2]` — the S2 Result cells now pass deterministically (their bound dedicated Citation cells hold resolved chips 27,28,10,11,15,20,30,30).

### 3b. RETAINED deterministic (unchanged code + refs)
- `C2:SENTINEL_FORMAT_DEFECT` ×1 @ `[table_row_7, 2]`
- `C6:UNLABELED_COMPARISON` ×6 @ `[tr5,3][tr6,3][tr9,3][tr10,3][tr11,3][gap_line_1]`
- `C6:MISSING_QUALIFIER` ×1 @ `[table_row_6, 2]`
- `C7:C7_INTEGRITY_FAILURE` ×1 @ `[]` (12 orphan / 9 dup / 46 blank / 0 inline-only)

### 3c. NEW deterministic (raised by r3 devices on the legacy body)
- `C6:MISSING_CALIBRATION_TARGET_PREFIX` **×9** (primary; **×8** under a negation-aware D1 detector — §4/§10 S1): col-1 `[tr4,1][tr5,1][tr6,1][tr7,1]*[tr8,1][tr9,1][tr10,1][tr11,1]` + col-2 `[tr11,2]`; `*[tr7,1]` = FIRE boundary.
- `C2:GAP_MULTIPLE_PER_PARAGRAPH` **×1** (parent paragraph of `gap_line_1..4`) — **CONDITIONAL on capture v3 adding a parent-paragraph field** (§5); count is 1-per-over-full-paragraph.

### 3d. NEW manual
- `C4:CITED_CELL_CLAIM_REVIEW` **×8** @ `[table_row_14..21, 2]` — D3 row-citation manual review (each S2 row's authoritative col-5 citation goes to cited-review; source fidelity is a later manual question, never auto-pass).
- `C7:C7_NEAR_DUPLICATE` **×1** (indices 14↔29) — D4 promotes the near-dup from v2 evidence-text to an explicit manual reconciliation flag.

### 3e. RETAINED manual
- All 73 v2 manual entries unchanged (18 C3 + 40+5+1+1 C4 + 8 C6). None is anchored to an S2 Result-cell citation, so D3 does not remove any.

### 3f. Totals (the T-INT pin)
- **Deterministic FAIL: 19** (primary) — `= 17 v2 − 8 (D3) + 9 (D1) + 1 (D5)`; **18** if the D1 detector exempts FIRE `[tr7,1]`.
- **MANUAL: 82** `= 73 + 8 (D3 row reviews) + 1 (D4 near-dup)`.
- **PASS unchanged**: C1, C5, C8, structural order.
- Overall: **FAIL** (FAIL_CLOSED).

---

## 4. D1 cell-by-cell: expected-new missing typed-prefix findings (req 3)

**Detector (must be frozen by A-P2 verbatim; fixture-scoped — any lexicon change ⇒ re-pin):** an S1 col-1 (`calibration_target`) or col-2 (`feedback_params`) cell needs the `CALIBRATION_TARGET_DESCRIPTION:` prefix iff it references an observation/observable (`observed|observation(al)|empirical|data`, or a named observable e.g. stellar/UV luminosity function, stellar-mass function, scaling relation, thermodynamic/gas-mass profile) **and** a calibrate/tune-to-target verb (`calibrat*|tuned to|targeted|match(ed)?|reproduc*|optimi[sz]e … (to|against)|emulation to match`). Un-prefixed + detector-positive ⇒ `MISSING_CALIBRATION_TARGET_PREFIX` FAIL. A `NONE_FOUND`/`NONE_FOUND.` cell is exempt (empty-field device; the sentinel case is charged once under C2). The sealed body predates the prefix, so no cell carries it.

col-1 `calibration_target` (all 8 are calibration-target descriptions):
| cell | sim | verdict |
|---|---|---|
| `[tr4,1]` | IllustrisTNG | FLAGGED ("targeted the observed galaxy stellar mass function…") |
| `[tr5,1]` | EAGLE | FLAGGED ("calibrated to reproduce the observed … stellar mass function") |
| `[tr6,1]` | SIMBA | FLAGGED ("reproducing the global galaxy stellar mass function") |
| `[tr7,1]` | FIRE/FIRE-2 | **BOUNDARY** — text is negated ("no … calibration … to match … observational properties"); FLAGGED under the negation-blind detector (primary), EXEMPT under a negation-aware one |
| `[tr8,1]` | ROMULUS | FLAGGED ("optimize … directly against a comprehensive set of redshift [observations]") |
| `[tr9,1]` | ASTRID | FLAGGED ("calibrated to … agreement with observed UV luminosity/stellar-mass functions") |
| `[tr10,1]` | FLAMINGO | FLAGGED ("calibrated … emulation to match the redshift z=0 [stellar mass function]") |
| `[tr11,1]` | BAHAMAS | FLAGGED ("calibrate the subgrid models … to reproduce the present-day galaxy [population]") |

col-2 `feedback_params`:
| cell | sim | verdict |
|---|---|---|
| `[tr4,2]` | TNG | EXEMPT — parameter description, no observation reference ("adjusted parameters governing galactic winds …") |
| `[tr5,2]` | EAGLE | EXEMPT — "subgrid routines … were varied", no observation reference |
| `[tr6,2]` | SIMBA | EXEMPT for D1 (no observation reference) — but this is the D2 `MISSING_QUALIFIER` cell (~10%) |
| `[tr7,2]` | FIRE | EXEMPT — `NONE_FOUND.` sentinel (C2 defect) |
| `[tr8,2]` | ROMULUS | EXEMPT — "optimized free parameters controlling … accretion rate", no observation reference |
| `[tr9,2]` | ASTRID | EXEMPT — "tuned the supernova feedback energy parameter to 1.0 …", parameter values, no observation reference |
| `[tr10,2]` | FLAMINGO | EXEMPT — "varied and tuned stellar feedback efficiency, kick velocity …", no observation reference |
| `[tr11,2]` | BAHAMAS | **FLAGGED** — "adjusted the stellar feedback wind velocity **to match the lower-mass end of the stellar mass function**" (observation + match) |

⇒ **9 FLAGGED** (8 col-1 + BAHAMAS `[tr11,2]`), of which FIRE `[tr7,1]` is the sole boundary (⇒ 8 if exempted). **7 col-2 exempt** (6 no-observation + 1 sentinel). The emergent-cell (col-3) comparisons are a separate mechanism → `UNLABELED_COMPARISON` (§3b), not prefix findings; no double count.

---

## 5. D5 merged-paragraph detection + capture-v3 field requirement (req 4)

Sealed provenance: `gap_line_1..4` each carry only `source_lines` (263,264,265,266) and `gap_index` (1..4). The root-cause established all four render as spans of **one** `<p data-path-to-node="11">`. **Capture v2 carries no parent-paragraph identifier**, and consecutive `source_lines` are innerText line numbers — identical whether the GAPs sit in one paragraph or four. Therefore D5 ("one GAP per paragraph") **cannot be detected from v2 capture output**.

**Determination: capture v3 REQUIRES a new field** — a parent-paragraph identity on each `gap_line` unit (recommended `parent_path` from the DOM `<p>` `data-path-to-node`, or `parent_block_id`). With it, the validator groups gap_lines by parent and emits `C2:GAP_MULTIPLE_PER_PARAGRAPH` when a parent holds >1 `GAP:` line. On the sealed body all four share one parent ⇒ **exactly 1** finding (1-per-over-full-paragraph). Without this field, the D5 count is unpinnable — A-P3 must add and populate it, or STOP.

---

## 6. D4 exact ledger output + normalization deltas (req 5)

From `chip_index_occurrences` and the 46-row ledger:
- **12 orphan indices** (in ledger, never cited inline): `2,5,8,9,13,16,18,23,24,29,31,33` ⇒ inside `C7_INTEGRITY_FAILURE`.
- **9 duplicate rows**: indices with >1 ledger occurrence `{3:2, 4:2, 8:2, 10:3, 14:2, 22:3, 26:2}` ⇒ extra rows `1+1+1+2+1+2+1 = 9`.
- **46 blank short-name fields**: every ledger row's `short_name` is `""`.
- **0 inline-only** indices.
- **Near-duplicate 14↔29 → MANUAL** `C7_NEAR_DUPLICATE`: index 14 `academic.oup.com/mnras/article/470/1/1121/3828081` vs index 29 `…/mnras/article-abstract/470/1/1121/3828081` (`article` vs `article-abstract`, same paper) — flagged, never merged.
- **Normalization deltas under r3-D4: NONE that change the above counts.** The `abs|html|pdf` extension produces zero new merges: every `arxiv.org/abs/*` ledger index is a distinct arXiv id (30,31,36,5,15,17,18,20,24,25,33,37 — no abs/html/pdf cross-variants). The only variant pair is the non-arXiv `article`/`article-abstract` (14↔29), handled as the near-dup flag. So the deterministic C7 integrity components are identical to v2; r3 only reclassifies the near-dup from evidence-text to a distinct manual flag.

---

## 7. D2 SIMBA + MODEL_PARAMETER positive fixture (req 6)

- **Sealed negative (retained):** `[table_row_6, 2]` SIMBA feedback cell quotes "~10%" accretion fraction (a numeric fraction) with no four-qualifier syntax and no `NOT_APPLICABLE`/`MODEL_PARAMETER` device ⇒ `C6:MISSING_QUALIFIER` FAIL ×1. The numeric gate keys on the quoted value, so bare "cluster gas fractions"/"fraction of SN energy" (no number) still produce no finding (the 3 v2 false positives stay removed).
- **Positive fixture (synthetic, passes):** a feedback cell "couples ~10% of available SN energy — `TRACER=MODEL_PARAMETER; SELECTION=NOT_APPLICABLE; DENOMINATOR=available SN energy; REDSHIFT=NOT_APPLICABLE`" ⇒ MANUAL (`SEMANTIC_QUALIFIER`), not FAIL. An observational fraction with full real qualifiers ⇒ MANUAL.

---

## 8. D3 removal + row-citation review + EMPTY_CITATION_CELL (req 7)

- **Removal:** the 8 `C4:UNCITED_CELL_CLAIM` @ `[tr14..21, 2]` are NOT emitted under r3 (each S2 row's authoritative dedicated Citation cell (col 5) holds a resolved chip → the row-citation gate passes deterministically).
- **Preserved row-citation manual-review:** each of the 8 S2 rows is a cited validation claim → `C4:CITED_CELL_CLAIM_REVIEW` MANUAL ×8 @ `[tr14..21, 2]` (authoritative citation = col 5). This preserves fail-closed review posture: a resolved citation is never mechanically certified; source fidelity is a later manual step. Net at this locus: 8 deterministic FAIL → 8 MANUAL (reclassified, not dropped).
- **EMPTY_CITATION_CELL hard-fail (guard intact):** if an S2 row's dedicated Citation cell is empty/missing, the r3 validator emits `C4:EMPTY_CITATION_CELL` FAIL (hard) — this is D3's preserved guard and the accepted verbatim limit of D3's relaxation. On the sealed body no S2 Citation cell is empty (all resolve), so zero `EMPTY_CITATION_CELL` here; the guard is exercised only by the negative D3 fixture (§2). Any implementation where an empty Citation cell does **not** hard-fail ⇒ immediate STOP (Gate A stop condition).

---

## 9. Integration acceptance rule (req 8)

- **T-INT canonical form:** each finding canonicalizes to the tuple `(clause, code, status, tuple(source_refs))`. The run's deterministic-FAIL set and MANUAL set are compared to §3's pinned multisets as **order-independent multisets** (sort by the tuple; compare counts). Sub-evidence inside `C7_INTEGRITY_FAILURE` (orphan/dup/blank lists) is compared as sorted sets.
- **Acceptance:** PASS iff the deterministic-FAIL multiset == §3 pin (19 primary / 18 FIRE-exempt, whichever Hwao freezes in §10) AND the MANUAL multiset count == 82 with matching `(clause,code,source_refs)` identities AND the removed-set (8 `UNCITED_CELL_CLAIM`) is absent AND C1/C5/C8/order PASS.
- **Manual entries are counted by identity, never by science:** a MANUAL finding is counted iff its `(clause, code, source_refs)` matches; the pin asserts **nothing** about whether the underlying citation/label/value is scientifically correct. "82 manual" is a review-queue size, not 82 proven errors.
- **Deviation ⇒ STOP + adjudicate (T14 pattern); never silently edit the pin or weaken an assertion.**

---

## 10. Sensitivities requiring Hwao countersign (freeze before A-P2)

- **S1 — FIRE `[tr7,1]` negation:** D1 detector negation-blind ⇒ 9 prefix findings / det total 19 (RECOMMENDED, fail-closed); negation-aware ⇒ 8 / 18. Freeze one; T-INT pin follows.
- **S2 — capture v3 parent-paragraph field:** D5 requires it (§5). Freeze the field name/source and the "1-per-over-full-paragraph" granularity (vs per-excess-line).
- **S3 — D4 near-dup custody:** pinned as +1 MANUAL `C7_NEAR_DUPLICATE` (⇒ manual 82). If Hwao prefers it as evidence-within-`C7_INTEGRITY_FAILURE` (as v2), manual = 81; freeze.
- **S4 — new code names/clauses:** `MISSING_CALIBRATION_TARGET_PREFIX` (clause C6 recommended), `GAP_MULTIPLE_PER_PARAGRAPH` (C2), `EMPTY_CITATION_CELL` (C4), `C7_NEAR_DUPLICATE` (C7). Freeze names so A-P2 asserts on them verbatim.
- **S5 — D3 +8 manual:** design-derived from "preserved row-citation manual-review behavior"; confirm the S2 row review anchors to `[row, 2]` with authoritative citation col 5.

If Hwao freezes S1=blind, S3=+1, the pinned totals are **deterministic 19 / manual 82**; otherwise adjust per the frozen choice before A-P2 authors tests.

---

## 11. Restated disclaimer + stop posture
This is a mechanical, offline, diagnostic re-scoring pin of a pre-r3 body. No science or source fidelity is certified; C1r stays FAIL_CLOSED; no retro-acceptance; no quarantine release. Any immutable-input hash mismatch, any T-INT deviation from the countersigned pin, or any D3 relaxation beyond the empty-cite hard-fail guard ⇒ STOP to Hwao/Duho with a partial receipt.

LANA_GATE_A_R3_RED_PIN_DONE_20260713T034742Z
