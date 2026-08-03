# Kun Packet B Receipt

Dispatch marker: OVERNIGHT_PAPER_BOARD_PACKET_B_KUN_BRIEF_V1

## Files Produced

| file | sha256 |
|---|---|
| packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.md | 54cf78b57b61d0a4ddb755f8a1d6f96ed53e25873a08268a775102af6f720498 |
| packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.csv | b1cec58ae9f30b1845988f40c563c50d36f9cb19475f1c53b67e0da55c436f2b |
| packets/B-citation-integrity/kun/candidates/gated-e2e-demo.corrected.md | d0bfe94ceb733710fe72393c4683ec439485ca294b845606653e56def32cb56d |
| packets/B-citation-integrity/kun/candidates/gated-halt-demo.corrected.md | 7c46256b5457058367934f6fb40db0ef58eb2e579d5ec60b0475b21a71cceb28 |
| packets/B-citation-integrity/kun/METHOD.md | fc278658bedb6e488a16dff303373310d13e7a0c879ee795892db53e2383b2e2 |

Receipt file SHA256 is not self-listed because the receipt content would change its own hash.

## Source Stability

Source hash check: PASS. `shasum -a 256 -c baseline/INPUT_SHA256.txt` returned OK for all 38 captured source files from the immutable Lab source root.

## Checked vs Unsupported Counts

| run_id | checked | unsupported | note |
|---|---:|---:|---|
| gated-e2e-demo | 4 | 2 | Checked keys: Torrey2019, Qi2025, Guo2016, Garcia2023. |
| gated-halt-demo | 2 | 1 | Checked keys: Renzini2015, Pearson2023. |
| fesc002 | 0 | 0 | `adversarial=true`; `all=[]`; no citations were checked or silently counted as supported. |

## Fix Types

| run_id | citation_key | fix |
|---|---|---|
| gated-e2e-demo | Torrey2019 | removal |
| gated-e2e-demo | Guo2016 | removal |
| gated-halt-demo | Pearson2023 | removal |

Re-attributions: none.

Removals: Torrey2019, Guo2016, Pearson2023.

## STOP Notes

None. No corrected candidate required a new unsupported number, a new citation outside the source reference list, a weakened/deleted caveat, a source-draft edit, a write outside the allowed roots, or an `expected_value` verdict of `CONTRADICTS`.

## Completion State

DONE

OVERNIGHT_PAPER_BOARD_PACKET_B_KUN_CITATIONMAP_COMPLETE_V1
