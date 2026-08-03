# Corrected Tori root-cause report — Gemini Deep Research C1r

Investigation ID: `dr-c1r-root-cause-20260712T163156Z`
Authoritative failed packet: `gemini-dr-revised-canary-20260712T045317Z`
Mode: offline/local-only; no browser, network, retry, account action, DB, deploy, or git write
Correction note: this report supersedes `TORI_ROOT_CAUSE.md`, whose first-pass anchor-only inspection missed Gemini source-footnote citation chips.

## Executive verdict

The run was not primarily a model citation-collapse failure. The largest immediate cause of the 54-failure result was a mismatch between Gemini's rendered citation format and our capture/validator pipeline.

Gemini rendered inline citations as `<source-footnote><sup data-turn-source-index="N">` components. The structured extractor recorded only descendant `<a href>` links. Because the source-footnote chips are not anchors, the extractor converted cited table cells, bullets, GAP lines, and Section-2 Citation cells into units with empty `links` arrays and sometimes empty text. The validator then treated those cited units as uncited or blank.

Raw HTML proves the citations existed:

- 108 source-footnote chip occurrences total
- 62 inline before the Links ledger
- 46 in the Links ledger
- 57 inline chips inside table cells
- 3 inside warning bullets
- 2 in GAP prose
- all 32 claim-bearing Section-1 cells have source chips; the one allowed empty field also carries one
- all eight Section-2 dedicated Citation cells have source chips
- all nine Section-4 `CALIBRATED`/`EMERGENT` status cells have source chips

After rebuilding an in-memory chip-aware normalized representation from the immutable HTML and mapping each source index to its ledger URL, the validator falls from 54 deterministic failures to 12. Three of those 12 are over-broad `fraction` keyword false positives. The remaining report still fails, so rejection remains correct—but for a much smaller and more specific set of reasons than the sealed headline suggested.

## Tight reproduction

Original validator replay:

`python3.11 validator/run_validator.py --body runs/c1r/body.md --structured runs/c1r/structured_capture.json --spec validator/contract_spec.json --output /tmp/c1r-repro.json`

Observed:

- overall: `FAIL`
- deterministic failures: 54
- manual-review findings: 28
- passes: 3
- finding keys reproduce the sealed result exactly; only unordered C7 set-evidence text changes order

Tests:

- Python validator suite: `37 passed in 0.09s`
- structured-capture JavaScript fixture: PASS

The green tests prove internal consistency, not coverage of Gemini's real source-footnote DOM. Existing fixtures use anchors and do not represent `source-footnote`/`data-turn-source-index` behavior.

## Corrected classification of the original 54 findings

### Forty-five are capture/validator defects or false positives

| Count | Original finding | Corrected classification |
|---:|---|---|
| 8 | C2 `EMPTY_TABLE_CELL` | Extractor defect. Every Section-2 Citation cell contains a source-footnote chip; it only appears text-empty because the chip has no anchor/text captured. |
| 1 | C2 `BAD_STRUCTURE` | Validator defect. The section order is correct. Any empty cell sets the same flag used for ordering, producing a redundant structure failure. |
| 31 | C4 Section-1 `UNCITED_CELL_CLAIM` | Extractor defect. Raw HTML shows a source chip in every affected cell. |
| 2 | C4 paragraph `UNCITED_CLAIM` | Extractor defect. The warning has a source chip; the GAP block contains two source chips and the other two GAP lines carry the allowed asserted-absence token. |
| 3 | C6 `MISSING_QUALIFIER` | Validator overreach. It triggers on qualitative uses of the word `fraction`, not only quoted numerical fractions/incidences. |
| **45** | | |

### Nine original findings survive as genuine or contract-level problems

| Count | Original finding | Corrected classification |
|---:|---|---|
| 2 | C4 Section-2 result cells | Genuine under the literal C4 rule: FLAMINGO and BAHAMAS result cells lack their own repeated source chip, even though their dedicated Citation cells are populated. The validator misses the same issue in the other six Section-2 result cells. |
| 6 | C6 `UNLABELED_COMPARISON` | Literal contract noncompliance: five Section-1 rows and one GAP unit make simulation-observation comparisons without the required comparability token. The rule is also awkward/unrealistic because calibration-target reporting naturally describes relationships to observations. |
| 1 | C7 ledger/body mismatch | Genuine at global level, but overstated by the extractor. A chip-aware map finds 25 unique inline source indices versus 37 ledger indices, leaving 12 orphan ledger sources—not all 37. |
| **9** | | |

## Chip-aware normalized replay

A throwaway in-memory replay mapped:

- each `data-turn-source-index` chip to the matching ledger URL;
- table chips to their exact row/cell;
- warning chips to their bullet units;
- GAP chips to the GAP block;
- source-chip-only Citation cells to non-empty normalized citation units.

Observed result:

- deterministic FAIL: 12
- manual review: 61
- PASS findings: 4

The 12 failures are:

- 2 C4 same-cell citation failures in Section-2 result cells
- 6 C6 unlabeled comparisons
- 3 C6 qualifier false positives
- 1 C7 orphan-ledger-set finding

Removing only the three demonstrated qualifier false positives leaves nine original-finding failures. This replay does not certify scientific correctness; it isolates the representation boundary.

## What the model actually did well

The rendered answer is materially better than the sealed 54-failure summary implied:

- exact header passed;
- all major sections and table rows were emitted;
- the final marker was exact, unique, and final;
- all Section-1 claim cells carried source chips;
- all eight Section-2 Citation cells carried source chips;
- all three warning bullets carried source chips;
- all nine claim-bearing Section-4 status cells carried source chips;
- all four GAP lines were either source-cited or carried the explicit unverified-absence token;
- the banned-word check passed.

This rules out a blanket conclusion that Gemini simply ignored claim-level citations.

## Genuine report/contract defects that remain

### 1. Section-2 citation design is redundant and the model satisfied only the dedicated column

Every Section-2 row has a populated Citation cell. However, C4 separately says a dedicated Citation cell cannot cover the claim-bearing Result cell. None of the eight Result cells repeats its own citation chip. The validator catches only two because its C4 heuristic looks for calibration keywords rather than all validation-result cells.

This is a genuine literal failure, but it also identifies a contract-design problem: the schema asks for a Citation column and then declares that column insufficient. A deterministic renderer should place/repeat resolved citations; a research model should return source IDs once per atomic validation record.

### 2. Six outside-Section-2 comparison labels are missing

Five calibration-ledger rows and one GAP block contain language matching the comparison rule without `MATCHED_SELECTIONS` or `NON_COMMENSURABLE_UNMATCHED_SELECTIONS` in the same logical unit. This is literal noncompliance.

The rule is difficult because a calibration target is naturally described as matching/reproducing an observed quantity. Typed records should distinguish `CALIBRATION_TARGET_DESCRIPTION` from a genuine validation comparison instead of using prose keyword detection.

### 3. Links ledger fails the revised bidirectional/unique format

The source-chip map is complete for source indices 1–37, but only 25 indices are used inline. Twelve ledger indices are orphaned:

`2, 5, 8, 9, 13, 16, 18, 23, 24, 29, 31, 33`

The rendered ledger also has:

- 46 rows/occurrences for 37 unique source indices/URLs;
- nine duplicate URL instances;
- blank short-name fields on the rendered ledger rows.

These are genuine C7/format defects. The original validator's URL-set extraction both missed duplicates and wrongly classified all 37 ledger URLs as orphaned because it ignored source chips.

### 4. Minor exact-token defect

The FIRE feedback-parameter cell uses `NONE_FOUND.` with punctuation rather than exact `NONE_FOUND`. The current validator misses this.

### 5. Scientific review remains unresolved

The answer still cannot be accepted as evidence without source-level checking. The eight Section-2 rows all use `MATCHED_SELECTIONS`, and all overlap cells say `No`. Uniform labels are not proof of semantic correctness. This investigation stayed offline and did not verify the papers, selections, quoted magnitudes, or source fidelity.

## Root causes, ranked

### 1. Real-DOM citation chips were outside the extractor's data model — highest confidence

`structured_capture.js:18-22` records only `element.querySelectorAll('a[href]')`. Gemini's inline citations are `source-footnote` components whose `sup` child carries `data-turn-source-index`. The URL is resolved elsewhere in the rendered answer. No source-chip fixtures existed, so the tests remained green while the live capture dropped citation associations.

This is the principal reason the validator reported 54 instead of approximately 12 finding-level failures.

### 2. The validator mixes representation, syntax, and semantics — high confidence

Examples:

- empty-cell detection doubles as structure-order failure;
- C4 relies on keyword/word-count heuristics rather than typed claim units;
- C6 treats any `fraction` word as a numerical fraction;
- C7 converts URLs to sets, hiding duplicate rows;
- C3 checks whole rows/blocks, so one uncertainty token can cover a different cell;
- warning bullets and short Section-4 statuses are not directly validated;
- multiple GAP lines can be coalesced into one block.

The fail-closed posture was correct, but the reported reasons were not sufficiently representation-aware.

### 3. The one-shot contract delegates deterministic assembly work to the research model — high confidence

The prompt asks one model response to do literature discovery, scientific classification, per-cell citation repetition, uncertainty labeling, cross-section comparison control, global ledger bijection/uniqueness, exact token formatting, and final rendering across eight simulation suites.

The model largely performed research/citation attachment but failed global assembly invariants. Those invariants belong in typed local records plus a deterministic renderer.

### 4. Some contract rules are internally awkward — high confidence

- Section 2 provides a Citation column, while C4 says that column does not cover its Result cell.
- Section 1 must describe calibration against observations, while C6 treats comparison-like wording outside Section 2 as requiring validation comparability labels.
- Full repeated URLs/source chips in every rendered claim unit are better produced mechanically than requested as model prose.

## Smallest safe remediation sequence

No live retry should occur from this investigation.

1. Fix the representation layer first:
   - capture `source-footnote` and `data-turn-source-index`;
   - resolve each index to its canonical ledger URL/source record;
   - preserve exact cell/bullet/GAP association;
   - avoid duplicate `<li>` plus nested `<p>` logical units;
   - split GAP lines into independent units.
2. Add RED fixtures copied from the real rendered DOM for source chips in:
   - ordinary table cells;
   - source-chip-only Citation cells;
   - bullets;
   - GAP lines;
   - ledger rows.
3. Repair validator logic:
   - separate order errors from empty cells;
   - enforce exact empty tokens;
   - validate typed claim units rather than keyword guesses;
   - detect duplicate ledger rows and blank short names;
   - make fraction/incidence checks numerical/typed;
   - validate uncertainty per value/cell.
4. Keep the decomposed architecture already planned:
   - one machine-readable evidence unit per simulation;
   - source IDs attached to atomic claims;
   - deterministic local renderer repeats citations and builds the ledger from actual rendered references;
   - fail closed on any unresolved or unreviewed unit.
5. Re-run offline fixtures first. Only after a chip-aware classifier covers all 54 original findings with zero unresolved rows should Hwao finalize the contract or prepare a separately approved one-simulation canary.

## Bottom line

The run failed mainly because our validator could not see Gemini's real inline citation components, not because Gemini put all evidence only in a bibliography. The report still had genuine global-contract defects—especially Section-2 repeated-citation rules, six unlabeled comparisons, and a non-bijective/duplicated ledger—so it remains rejected. The next move is to repair the capture/validator boundary and keep the planned decomposed, deterministic assembly architecture. A longer prompt or immediate retry would repeat the wrong experiment.

TORI_DR_C1R_ROOT_CAUSE_CORRECTED_DONE_20260712T163156Z
