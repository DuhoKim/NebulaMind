# HWAO_R3_RED_PIN_COUNTERSIGN — Gate A A-P1 pin frozen

Ref: `design/LANA_R3_RED_PIN.md` (`LANA_GATE_A_R3_RED_PIN_DONE_20260713T034742Z`) · Countersign only; no tests, no code, no live action. With this file the pin is FROZEN: A-P2 authors RED tests against it verbatim; any T-INT deviation or lexicon change ⇒ STOP + re-pin (T14 pattern), never a silent edit.

## 1. Sensitivity freezes S1–S5

- **S1 — FROZEN: negation-blind D1 detector ⇒ 9 `MISSING_CALIBRATION_TARGET_PREFIX` findings; deterministic total 19.** Rationale: fail-closed and deterministic — negation-aware parsing is exactly the fragile semantic keying this program has been eliminating; and prefixing a negated statement is semantically acceptable because the FIRE cell still *describes calibration-target status* (its absence). FIRE `[tr7,1]` is therefore FLAGGED; the boundary is recorded, and a future r3-native body may legitimately prefix a no-tuning statement.
- **S2 — FROZEN: capture v3 adds `parent_path`** on every `gap_line` unit (value = the DOM `data-path-to-node` of the nearest block-level `<p>` ancestor; may be populated on other unit types harmlessly). **Granularity = 1 finding per over-full paragraph** (not per excess line): the paragraph is the defective unit per the r3-D5 wording, and per-excess-line would double-charge one defect against the one-defect-one-finding invariant. If A-P3 cannot populate `parent_path`, STOP (per §5 of the pin).
- **S3 — FROZEN: near-duplicate as a distinct MANUAL finding `C7:C7_NEAR_DUPLICATE` ×1 (14↔29) ⇒ MANUAL total 82.** Faithful to r3-D4's "flagged for manual reconciliation"; evidence-text burial reproduces v2's under-visibility.
- **S4 — FROZEN code names and clauses, verbatim for A-P2 assertions:** `C6:MISSING_CALIBRATION_TARGET_PREFIX` · `C2:GAP_MULTIPLE_PER_PARAGRAPH` · `C4:EMPTY_CITATION_CELL` · `C7:C7_NEAR_DUPLICATE`. Clause homes as recommended (prefix under C6 — it is the D1 comparison-scope typing device; GAP granularity under C2 structure; empty-cite under C4; near-dup under C7).
- **S5 — CONFIRMED: D3 emits `C4:CITED_CELL_CLAIM_REVIEW` MANUAL ×8 anchored `[table_row_14..21, 2]`** (the claim-bearing Result cell is the review locus) with the authoritative citation read from col 5. Correct posture: a resolved citation is never mechanically certified; the 8 findings reclassify FAIL→MANUAL at the same locus, they do not vanish.

## 2. Frozen T-INT total multisets (order-independent; canonical tuple `(clause, code, status, tuple(source_refs))`)

**Deterministic FAIL — exactly 19:**
| Code | Count | source_refs |
|---|---:|---|
| `C2:SENTINEL_FORMAT_DEFECT` | 1 | `[table_row_7, 2]` |
| `C2:GAP_MULTIPLE_PER_PARAGRAPH` | 1 | parent `parent_path` of `gap_line_1..4` (single shared `<p>`) |
| `C6:UNLABELED_COMPARISON` | 6 | `[tr5,3] [tr6,3] [tr9,3] [tr10,3] [tr11,3] [gap_line_1]` |
| `C6:MISSING_QUALIFIER` | 1 | `[table_row_6, 2]` |
| `C6:MISSING_CALIBRATION_TARGET_PREFIX` | 9 | col-1 `[tr4,1][tr5,1][tr6,1][tr7,1][tr8,1][tr9,1][tr10,1][tr11,1]` + col-2 `[tr11,2]` |
| `C7:C7_INTEGRITY_FAILURE` | 1 | `[]` — sub-evidence as sorted sets: orphans `{2,5,8,9,13,16,18,23,24,29,31,33}`, 9 duplicate rows (extras over `{3:2,4:2,8:2,10:3,14:2,22:3,26:2}`), 46 blank short names, 0 inline-only |
Sum: 1+1+6+1+9+1 = **19**.

**MANUAL — exactly 82:** the 73 retained v2 entries (18 `C3:UNCERTAINTY_CHECK` + 40 `C4:CITED_CELL_CLAIM_REVIEW` + 5 `C4:CITED_CLAIM_REVIEW` + 1 `C4:CITATION_QUALITY_REVIEW` + 1 `C4:SOURCE_FIDELITY_REVIEW` + 8 `C6:COMPARISON_LABEL_REVIEW`) **+ 8** new `C4:CITED_CELL_CLAIM_REVIEW` @ `[tr14..21, 2]` (D3 row reviews; class total becomes 48) **+ 1** `C7:C7_NEAR_DUPLICATE` (14↔29). Sum: 73+8+1 = **82**.

**REMOVED — must be absent:** `C4:UNCITED_CELL_CLAIM` ×8 @ `[table_row_14..21, 2]`.
**PASS unchanged:** C1, C5, C8, structural order. **Overall: FAIL** (diagnostic re-scoring; C1r stays FAIL_CLOSED).
**On the sealed body `C4:EMPTY_CITATION_CELL` count = 0** (all 8 S2 Citation cells hold resolved chips); the code is exercised only by the negative D3 fixture, and an implementation where an empty Citation cell does not hard-fail is an immediate STOP.

## 3. Additional countersigned items

- **Field name/granularity (S2) restated as the binding capture-v3 schema delta:** `gap_line.parent_path` (string, required for gap_line units), plus no other schema changes without re-pin.
- **D1 detector lexicon** (§4 of the pin) is frozen verbatim and fixture-scoped; any extension is a logged re-pin, never silent. `NONE_FOUND`/`NONE_FOUND.` cells are prefix-exempt (the sentinel defect is charged once under C2 — no double count).
- **D4 normalization deltas = none** (§6): accepted — the `abs|html|pdf` extension yields zero new merges on the sealed ledger; 14↔29 is the sole variant pair and is the S3 manual flag.
- **T-INT acceptance rule** (§9) accepted verbatim, including: manual entries counted by identity never by science; multiset comparison; sub-evidence as sorted sets; deviation ⇒ STOP + adjudicate.
- **Diagnostic disclaimer** (§0/§11) accepted and binding on every artifact A-P2..A-P5 produce: mechanical only, no science/source-fidelity certification, no retro-acceptance, no quarantine release.

## 4. Effect

A-P1 is complete. A-P2 (Goru RED authoring, Kun runner) may be relayed by Tori against this frozen pin: expected totals **19 deterministic / 82 manual / C1-C5-C8-order PASS / overall FAIL**, with the exact multisets of §2. A-P3 implementation order D5 → D4 → D2 → D1 → D3 stands. All Gate A stop conditions remain in force.

HWAO_GATE_A_RED_PIN_COUNTERSIGN_DONE_20260713T034742Z
