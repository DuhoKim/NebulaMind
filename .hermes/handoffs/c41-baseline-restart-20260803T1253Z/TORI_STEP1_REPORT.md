# Tori C41 Step-1 execution report

Lane: `c41-baseline-restart-20260803T1253Z`
Protocol: `C41_STEP1_V1`
Authorized gate: Duho, 2026-08-03, `APPROVE C41 STEP 1`
Final verified run: 2026-08-03 13:14:31 UTC / 22:14:31 KST

## Work completed

- Verified the frozen question at mode 0444 and the required SHA-256
  `9ac5ca1f6321e2808eec3b9c2d38b8e616e0a9d774f4f277469c38fadbf789e1`.
- Verified all required local input files before relying on them.
- Inspected field schemas and aggregate distributions without emitting or inspecting individual
  candidate records/titles.
- Authored `STEP1_CORPUS_PROTOCOL.md` before title-level selection.
- Authored executable, stdlib-only `step1_filter.py`; mode is 0755. It streams the 420 MB base
  JSONL, reads no network/DB/model service, and writes atomically only in this lane.
- Executed the filter and generated the included set, grouped excluded set, and checksum manifest.
- Ran independent structural, partition, rank-order, scope-clause, cap, checksum, static-import,
  and synthetic decoy validations.

## Input and selection counts

- Base C41 labels / metadata found: 1,296 / 1,296.
- Delta C41 labels / metadata found: 21 / 21.
- Combined universe: 1,317.
- Eligible before review/calibration/capacity handling: 833.
- Included: 180 (ceiling met, not exceeded).
- Excluded: 1,137.
- Included origins: 179 base; 1 delta.
- Included source classes: 179 peer-reviewed primary; 1 arXiv preprint.
- Included calibration anchors: 8 (cap 8).
- Included reviews: 0 (cap 24 did not fire).

Overlapping included-axis coverage:

- Formation efficiency: 166.
- Chemical enrichment: 100.
- Ionizing output: 92.

Included contested-priority distribution:

- Priority 4, direct measurement in a `contested` dispersion quantity: 58.
- Priority 3, direct measurement in a `mild` dispersion quantity: 10.
- Priority 2, strict disagreement lexicon: 97.
- Priority 1, relevant dispersion-quantity lexicon: 15.
- Priority 0: 0.

## Exclusion counts by named rule class

| Rule class | Count |
|---|---:|
| `DUPLICATE_IDENTITY` | 0 |
| `MALFORMED_REQUIRED_METADATA` | 0 |
| `UNSUPPORTED_SOURCE_CLASS` | 0 |
| `LRD_AGN_OUTSIDE_THREE_AXES` | 41 |
| `INSTRUMENT_OUTSIDE_SELECTION_LIMITS` | 5 |
| `NAMED_TOPIC_OUTSIDE_THREE_AXES` | 7 |
| `NO_THREE_AXIS_SIGNAL` | 151 |
| `NO_HIGH_Z_SIGNAL` | 280 |
| `REVIEW_CLASS_CAP` | 0 |
| `CALIBRATION_ANCHOR_CAP` | 75 |
| `CAPACITY_BELOW_TOP_180` | 578 |
| **Total** | **1,137** |

Every source record has exactly one final disposition. The grouped JSON publishes each rule's full
text and its excluded records; there is no unnamed or manual exclusion.

## Runtime and determinism

- Final output-generating verified runtime: 3.787252 seconds.
- A second run on unchanged inputs was byte-identical for both selection JSON files and the SHA
  manifest.
- `SELECTION_SHAS.txt` verification:
  - `SELECTION_INCLUDED.json`: `4a0ba6e7ae1ad7b8249c68ddd0c73ccf81a1ba05c94ffac03febb012589e961f`
  - `SELECTION_EXCLUDED.json`: `1496765f3fd1450363465dbed0b1788c499b1687396f96d4015ef3019aa3acc4`
- `shasum -a 256 -c SELECTION_SHAS.txt`: both files `OK`.

## Validation results

Independent validation returned `PASS` with zero errors:

- JSON parse and exact 1,317-record partition;
- ranks exactly 1–180 and deterministic published sort order;
- unique included identities and correct duplicate-rule handling;
- all included records have either a high-z signal or the named calibration-anchor exception;
- every included LRD/AGN record has a strong three-axis signal;
- every included instrument-core record has both an axis and a selection-limit exception;
- review and calibration-anchor caps respected;
- all three frozen axes represented;
- SHA manifest has exactly two standard, valid lines;
- Python source compiles, imports stdlib only, and has no network, subprocess, DB, or git module;
- seven synthetic decoys passed: relevant high-z paper survives; irrelevant high-citation paper gets
  a named exclusion; LRD nature-only is excluded while LRD ionizing-axis survives; instrument-only
  is excluded while completeness-bearing instrument metadata survives; named out-topic is excluded.

## Anomalies and diagnostics

Input anomalies: none. There were no malformed JSON rows, label/metadata mismatches, missing required
metadata, duplicate identities, or unsupported source classes.

Selection diagnostic, preserved without hand correction: nine records were mechanically flagged as
the review source class across the universe, but none entered the top 180. Their exclusions were one
LRD-boundary, one no-axis, one no-high-z, one calibration-anchor-cap, and five capacity exclusions.
The protocol specifies a review cap and small review ranking bonus, not a manual review quota, so the
result was left unchanged for Kun's adversarial review.

Delta diagnostic, also preserved without hand correction: one of 21 delta records entered; the other
20 received named rule dispositions (2 calibration-anchor-cap, 9 capacity, 3 LRD-boundary, 2 named
out-topic, 2 no-high-z, 2 no-axis).

One bundled shell verification invocation surfaced a wrapper exit status of 1 after printing a
successful filter summary; the filter was immediately rerun directly and explicitly returned
`FILTER_EXIT=0`. Subsequent deterministic execution, SHA checks, syntax validation, and independent
JSON validation all passed. No output was accepted solely from the anomalous wrapper invocation.

No `_tmp_*` files or Python cache directories remain in the lane.

## Deliverables

- `STEP1_CORPUS_PROTOCOL.md`
- `step1_filter.py`
- `SELECTION_INCLUDED.json`
- `SELECTION_EXCLUDED.json`
- `SELECTION_SHAS.txt`
- `TORI_STEP1_REPORT.md`

Safety boundary held: no network, DB/SQL, model/Deep Research/credits, product/wiki/live,
deploy/restart, or git-write action occurred; all writes remained in the authorized lane.

TORI_STEP1_COMPLETE_20260803

## PATCH — Kun `SEALED_WITH_PATCHES`

- F1 disclosure: The calibration-anchor cap ranks anchors against each other rather than against the
  whole pool, so seven priority-2-signal anchors were capped out while lower-ranked non-anchors
  remained in the sealed 180.
- N1 fidelity correction: Protocol rule 9 now states that the review-cap counter counts only reviews
  already included, matching `step1_filter.py`.
- Sealed selection preserved: `step1_filter.py`, both selection JSONs, and `SELECTION_SHAS.txt` were
  not modified.

TORI_STEP1_PATCHED_20260803
