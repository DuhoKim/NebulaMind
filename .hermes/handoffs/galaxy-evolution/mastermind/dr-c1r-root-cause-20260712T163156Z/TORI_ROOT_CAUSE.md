# SUPERSEDED DRAFT — do not use for the final verdict

This first-pass draft counted only `<a href>` anchors and therefore missed Gemini's inline
`<source-footnote><sup data-turn-source-index>` citation chips. Raw-HTML inspection corrected that
interpretation. Use `TORI_ROOT_CAUSE_CORRECTED.md` in this directory instead. This draft is retained
only as an audit trail of the corrected investigation step.

# Tori root-cause report — Gemini Deep Research C1r (superseded)

Investigation ID: `dr-c1r-root-cause-20260712T163156Z`
Authoritative failed packet: `gemini-dr-revised-canary-20260712T045317Z`
Mode: offline/local-only; no browser, network, retry, account action, DB, deploy, or git write

## Executive verdict

The Deep Research service did not crash, time out, truncate, or lose the report during capture. It completed the requested research-shaped answer, emitted the required header/sections/final marker, and produced a large source ledger. It failed at the harder task: satisfying a globally cross-linked evidence contract in one pass.

The dominant failure was citation placement. Gemini collected 46 links (37 unique URLs) but placed every rendered anchor in the final Links ledger and zero anchors inside the claim-bearing table cells, bullets, or GAP units. Section 2 also left all eight dedicated Citation cells blank. This is a genuine rendered-output defect, not an `innerText` or structured-capture loss.

The sealed headline of 54 failures is reproducible, but it is not 54 independent root causes. Forty-five of the 54 validator failures collapse to the single citation/empty-citation problem plus one redundant validator umbrella finding. The remaining nine are C6 comparison/qualifier findings; six reflect literal but awkward cross-section contract rules, while three are over-broad validator triggers on the word `fraction` rather than actual quoted numerical fractions.

## Tight reproduction

Command:

`python3.11 validator/run_validator.py --body runs/c1r/body.md --structured runs/c1r/structured_capture.json --spec validator/contract_spec.json --output /tmp/c1r-repro.json`

Observed:

- exit code: 1
- overall: `FAIL`
- deterministic failures: 54
- manual-review findings: 28
- passes: 3
- finding keys match the sealed result; only unordered Python-set text in the C7 evidence string changes order between runs

Validator tests:

`PYTHONWARNINGS=ignore PYTHONPATH=. backend/.venv/bin/python -m pytest tests -q`

Observed: `37 passed in 0.09s`.

Structured-capture JavaScript fixture: PASS.

## Reconciliation of the 54 counted failures

| Count | Validator class | Root-cause interpretation |
|---:|---|---|
| 35 | C4 uncited claim/cell | Genuine missing same-unit citations, but repeated manifestations of one citation-locality failure. |
| 8 | C2 empty table cell | All eight are the Section-2 Citation column, left blank. Genuine. |
| 1 | C7 missing from body | Same citation-locality failure viewed as global set mismatch: body URL set is empty while ledger URL set has 37 unique URLs. |
| 1 | C2 `BAD_STRUCTURE` | Redundant/incorrect umbrella count. Section headings exist in the correct order; the validator reuses its order flag for any empty cell, so the eight blank Citation cells force a separate `BAD_STRUCTURE` finding. |
| 6 | C6 unlabeled comparison | Five Section-1 rows and one GAP block match the validator's comparison heuristic without a comparability token. Literal noncompliance, but the Section-1 calibration task naturally requires discussion of targeted observations and makes this rule difficult to apply cleanly. |
| 3 | C6 missing qualifier | Validator overreach: it triggers on any occurrence of `fraction`/`incidence`, including qualitative phrases such as “fraction of available Type II Supernovae energy” and “cluster gas fractions,” even when no numerical fraction/incidence is quoted. |
| **54** | | |

Counterfactual replay on immutable inputs, modifying only an in-memory copy of the structured representation:

- baseline: 54 FAIL / 28 manual / 3 pass
- after restoring citation/unit anchoring and filling the eight Citation cells: 9 FAIL / 63 manual / 5 pass
- after also adding the literal C6 tokens to the nine flagged blocks: 0 FAIL; `MANUAL_REVIEW_REQUIRED`

This does not claim the counterfactual answer is scientifically correct. It isolates what drove the deterministic failure count.

## Ranked root causes

### 1. Citation locality collapsed into an end-of-report bibliography — high confidence

Evidence:

- `rendered_body.html` contains 46 `<a href>` anchors.
- All 46 have a paragraph ancestor in the Links ledger.
- Zero have a `td` or `li` ancestor.
- `structured_capture.json` reports 46 block links in `paragraph_43`, zero cell links, and zero non-ledger inline URLs.
- Section 2 has eight rows and eight empty Citation cells.
- The Links ledger has 46 rows/anchors but only 37 unique exact URLs, with nine duplicate URL instances.

The prompt repeatedly required every claim-bearing cell/bullet to carry its own checkable citation or `UNCITED_NOT_USABLE`. Gemini instead generated prose first and pooled sources at the end. This violated C4 and made bidirectional C7 impossible.

This was not capture loss. The original rendered HTML itself has no anchors in the tables or bullets.

### 2. The single request combined literature discovery, scientific adjudication, formatting, and global integrity checks — high confidence as a reliability cause

Measured request/output shape:

- prompt: 1,395 words, 151 lines
- output: 2,837 words, 317 physical `innerText` lines
- eight named simulation suites
- eight binding clauses
- nine silent preflight checks
- 40 Section-1 data cells
- 48 Section-2 data cells
- 48 Section-4 data cells
- 46 ledger anchors

The output passed the simple/local constraints: exact header, banned-word scan, and final marker. It also produced all major sections and rows. It failed global relational constraints: citation-to-cell binding, empty-citation prevention, bidirectional URL equality, uniqueness, and some cross-section comparison labeling.

That pattern is evidence of practical one-pass constraint overload, not token truncation. The output was complete and ended with the exact marker.

### 3. C6 mixes a difficult literal rule with over-broad heuristics — high confidence

The prompt prohibits simulation-observation comparisons outside Section 2 unless the same logical unit carries a comparability token. Five Section-1 rows discuss calibration against observed quantities using words such as `reproduce`, so they violate the literal rule. However, calibration-target reporting naturally describes the relationship to observations, and the validator scans the whole row rather than the individual cell. The contract and checker therefore create avoidable friction.

The three qualifier failures are not reliable model defects. The implementation tests for the words `fraction` or `incidence`, not for a quoted numerical fraction/incidence. A minimal local probe confirms that “The model tunes a fraction of available energy” produces `MISSING_QUALIFIER`.

### 4. Validator coverage is incomplete and partly double-counts — high confidence

The validator correctly proves the run must fail, but the number 54 should not be treated as 54 independent defects.

Confirmed validator issues:

- Any empty cell sets the same flag used for section ordering, producing redundant `BAD_STRUCTURE`.
- URL sets erase duplicate ledger rows, so nine duplicate instances are missed despite the uniqueness contract.
- A bare Section-4 `EMERGENT` or `CALIBRATED` cell without a citation is not caught by C4.
- Uncited warning bullets are not checked directly; nested `<li><p>` capture happened to expose one duplicate paragraph to the paragraph-only rule.
- `NONE_FOUND.` passes C2 even though the contract requires exact `NONE_FOUND`.
- C3 is row/block-level: one uncertainty token can mask a bare quantity in a different cell.
- C6's `fraction` keyword trigger creates the three likely false positives.
- Multiple GAP lines captured in one paragraph can share a token incorrectly; two of four GAP lines lacked either a citation or the required asserted-absence token, but C2 did not report them separately.
- The validator misses several genuine citation defects: all three warning bullets, nine Section-4 `EMERGENT`/`CALIBRATED` status cells, and most Section-2 result cells unless they happen to contain calibration keywords.
- The ledger format requires a short name, but all 46 rendered rows begin with an empty short-name field; this is not validated.

Therefore the true contract noncompliance is broader than the 54 findings, even though several of the 54 are duplicate or heuristic counts.

### 5. Scientific acceptance was still unresolved — high confidence

The deterministic validator produced 28 manual-review findings:

- 13 uncertainty/source-value checks
- 8 Section-2 comparability-label checks
- 5 duplicate comparison-label reviews on a subset of those rows
- 2 fraction/qualifier semantic checks

All eight Section-2 rows use `MATCHED_SELECTIONS`, and every overlap column says `No`. Without source-level verification, those uniform judgments cannot be accepted. This investigation did not use the network and does not certify any scientific claim or citation.

## Capture/representation verdict

The dual-capture design worked for the decisive question.

- Headings and table cell boundaries are present in `structured_capture.json`.
- MathJax remains fragmented in immutable `innerText`, but the structured DOM preserves logical table cells.
- The final marker is present exactly once and final.
- The rendered HTML confirms that inline citation anchors were absent, not dropped by the capture adapter.

There are still capture-modeling weaknesses: nested list `<li><p>` content is represented twice, while four GAP lines are coalesced into one paragraph block. Those affect counting and validator coverage, but they do not explain the missing inline links.

## Smallest safe remediation sequence

No live retry should occur from this investigation.

1. Repair the offline validator first with RED tests for:
   - independent section order vs empty-cell findings;
   - exact `NONE_FOUND` tokens;
   - bullet citations;
   - Section-4 status citations;
   - per-GAP-line validation;
   - ledger short names and duplicate rows;
   - per-cell/value uncertainty checks;
   - numeric fraction/incidence detection instead of keyword-only detection.
2. Replace the one-shot eight-suite report with one independently validated evidence unit per simulation. Each unit should bind every claim directly to a source identifier and source position before cross-simulation assembly.
3. Make the cross-simulation tables and Links ledger deterministic local assembler outputs, not model-authored global set-equality work.
4. Run the repaired validator against immutable failed and clean fixtures, then an offline eight-unit end-to-end fixture.
5. Only after those offline gates pass may Hwao prepare a separate, still-unarmed one-simulation canary for explicit user approval.

## Bottom line

The run failed mainly because Gemini separated evidence from claims: it produced a bibliography rather than claim-level evidence bindings. The strict validator was right to reject the report. However, `54` is an inflated/overlapping symptom count, not 54 independent causes, and the validator itself needs repair before it can guide another run. The correct architectural response is decomposition plus deterministic local assembly—not a longer prompt or immediate retry.

TORI_DR_C1R_ROOT_CAUSE_DONE_20260712T163156Z
