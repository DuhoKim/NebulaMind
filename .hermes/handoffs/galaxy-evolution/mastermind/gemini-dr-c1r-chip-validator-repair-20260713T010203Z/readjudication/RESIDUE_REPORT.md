# Offline re-adjudication residue report

Packet: `gemini-dr-c1r-chip-validator-repair-20260713T010203Z`
Input: byte-copied, hash-checked sealed C1r rendered HTML and body text
Result: **FAIL_CLOSED remains in force**

## What changed

The v2 capture now reads Gemini's native citation chips (`data-turn-source-index`) in the exact cell, bullet, or GAP line where they appear. It pairs the 46 Links-ledger chips with 46 anchors, resolves 37 source indices, rejects conflicting index→URL mappings, removes nested `li`/`p` duplicates, and splits the merged Gaps paragraph into four independent logical units.

The v2 validator now judges typed logical units rather than row-wide link aggregates or keyword/word-count heuristics. It keeps Section-2 Result cells separate from the dedicated Citation cells, scans comparisons per cell, applies the fraction/incidence qualifier rule only when a numeric value is quoted, and evaluates ledger bidirectionality from chip indices.

## Verified capture facts

- Native citation chips: 108 total.
- Region counts: Section 1 = 40; Section 2 = 8; Section 3 = 3; Section 4 = 9; Section 5 = 2; Links ledger = 46.
- Links-ledger pairs: 46 rows, 37 unique indices, zero conflicts in the real sealed HTML.
- Literal anchors: 46, all in the Links ledger; zero inside table cells.
- Section-2 Citation-cell chip indices: 27, 28, 10, 11, 15, 20, 30, 30.
- Four GAP units: GAP1→chip 30; GAP2→absence token; GAP3→chip 36; GAP4→absence token.
- The deliberately corrupted fixture fails closed with index 10 mapped to two different URLs.

## Deterministic mechanical residue

The amended, Hwao-adjudicated and Lana-countersigned T14 result is **17 mechanical FAIL findings**:

1. C2 — one exact-sentinel defect:
   - FIRE/FIRE-2 feedback-parameter cell uses `NONE_FOUND.` instead of exact `NONE_FOUND`.

2. C4 — eight same-cell citation failures:
   - All eight Section-2 Result cells are uncited in their own cells.
   - Their dedicated Citation cells contain valid, resolved chips, but the contract explicitly says those chips do not satisfy the Result cells.
   - Affected rows: IllustrisTNG, EAGLE, SIMBA, FIRE/FIRE-2, ROMULUS, ASTRID, FLAMINGO, and BAHAMAS.

3. C6 — six unlabeled comparisons:
   - Five Section-1 emergent cells: EAGLE, SIMBA, ASTRID, FLAMINGO, and BAHAMAS.
   - GAP1.

4. C6 — one missing four-qualifier declaration:
   - SIMBA's feedback-parameter cell quotes an approximately 10% accretion fraction without `TRACER`, `SELECTION`, `DENOMINATOR`, and `REDSHIFT`, or the contract's `NOT_APPLICABLE` device.
   - This defect was masked in the sealed run by row-level granularity and surfaced at cell granularity, parallel to the six previously missed C4 comparison/result defects.

5. C7 — one ledger-integrity clause failure containing:
   - 12 orphan ledger indices: 2, 5, 8, 9, 13, 16, 18, 23, 24, 29, 31, 33.
   - 9 duplicate ledger rows.
   - 46 blank short-name fields.
   - One near-duplicate source pair: indices 14 and 29.
   - Zero inline-only indices.

C1, C5, C8, and structural order pass mechanically.

## Artifact findings removed

The repaired pipeline no longer emits the previously identified representation/validator artifacts:

- 8 false `EMPTY_TABLE_CELL` findings on citation-chip-only cells.
- 31 false Section-1 `UNCITED_CELL_CLAIM` findings.
- 2 false duplicate-paragraph `UNCITED_CLAIM` findings.
- 3 bare-word fraction/incidence `MISSING_QUALIFIER` false positives.
- The coupled `BAD_STRUCTURE` finding with `set()` evidence.

The new SIMBA approximately-10% finding is a different, genuinely numeric contract violation; it is not one of those three removed bare-word false positives.

## Manual-review boundary

The validator emitted 73 manual-review entries for citation-supported claims, uncertainty tokens, comparability labels, numeric qualifier semantics, citation quality, and source fidelity. This count is a review queue, not 73 proven scientific errors.

This re-adjudication is **mechanical only**. It does not verify whether any paper supports a claim, whether the quoted science is correct, whether comparison labels are scientifically defensible, or whether uncertainty handling is faithful to the sources. It does not certify science or source fidelity.

## Governance result

This report does not retroactively accept the C1r report and does not authorize reuse as evidence. The sealed report remains **FAIL_CLOSED**. There was no new Gemini run, browser action, network call, DB/wiki/product write, publication, deploy, restart, git action, or public-cockpit change.

TORI_C1R_READJUDICATION_RESIDUE_DONE_20260713T010203Z
