# P0 Board and Advisory-Score Representation Diff

## Frontier card

Current supported copy:

> TNG over-evolves the star-forming main sequence — a discrepancy that de-biasing the emission-line selection only widens (a conservative lower bound), and that is robust to the +0.13 dex mass-basis fix.

Disposition: **KEEP**. It states only the surviving SFMS result and does not assert MZR consistency.

Current dead metadata:

`review: "/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft_review_loop.md"`

Disposition: **REMOVE**. Fresh public verification returned 404 and no review artifact exists. The P0 card correctly has no `verdict`; no verdict will be added.

The `updated` timestamp remains unchanged in this preparation packet. A later applied/regenerated artifact must set its final timestamp only after successful compile and representation review.

## Advisory merit notes

| Evaluator | Current defect | Proposed correction |
|---|---|---|
| DR | Credits Te-scale matching and says chemistry is consistent once scales match | Credit the SFMS differencing/selection result; state MZR is suggestive on unmatched scales and not a consistency claim. |
| Hwao | Focuses on the reproducible SFMS failure | KEEP. |
| Tori | Says a naive test invented a “spurious chemical failure,” which can be read as dismissing the entire MZR state | Narrow to the spurious factor-three-to-four naive comparison; preserve the face-value factor-two result as suggestive. |
| Kun | Says the method unmasks the chemical failure as an abundance-scale artifact | Replace with unmatched-scale, suggestive MZR wording. |
| Goru | Says an uncorrected aperture-vs-SED mismatch still holds the result back | Replace with the actual standing caveats: unresolved observed-median provenance and no source-reproducible selection-envelope data/code. |

Scores are unchanged. This packet corrects reasons, not numerical merit values.

## Preserved representations

- `galaxy-evolution-tng-validation-draft_history.json` remains immutable historical intent.
- The public Paper Board audit report remains an audit of the pre-correction served identity.
- Figure assets remain unchanged because the selected repair aligns prose to the existing unmatched-scale figure state.
