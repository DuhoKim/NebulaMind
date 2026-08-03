# Canonical Recommendation

AI_DRAFT_NOT_HUMAN_GOLD

Marker: OVERNIGHT_PAPER_BOARD_PACKET_A_KUN_CANONICAL_RECOMMENDATION_V1

This is Kun's recommendation only. Hwao makes the canonical decision after the required independent Packet A inputs exist.

## Recommendation

Use `gated-e2e-demo` as the canonical representative for the TNG+SDSS z=0 gas-phase MZR analysis, not `d8de519cb9c9`.

For Packet C, build the TNG+SDSS candidate from `gated-e2e-demo` rather than directly from `d8de519cb9c9`, with the condition that Packet B citation corrections and the O/H-scale caveat remain explicit.

## Rationale

`d8de519cb9c9` and `gated-e2e-demo` carry the same core result summary: TNG100 `23,722` galaxies plus SDSS `120,000` galaxies, same `mass-metallicity` method, same `tng, sdss` data-source set, and the same TNG solar-scaled O/H wording. However, `d8de519cb9c9` is figure/summary-only and records that the full AASTeX draft is queued. `gated-e2e-demo` is the drafted, reviewed, gated build of that same core analysis.

`gated-e2e-demo` is not publication-ready as-is because its citation gate reports `2 unsupported of 4 checked`, but that is an identified and bounded citation-integrity repair rather than a reason to prefer the less complete `d8de519cb9c9` source. Packet B already isolates candidate removals for the unsupported citations.

## Redundant / Noncanonical Runs

| run_id | recommendation |
|---|---|
| `d8de519cb9c9` | Redundant as the canonical TNG+SDSS representative once `gated-e2e-demo` is available; preserve as the figure/summary precursor and provenance sibling. |
| `2958462772b2` | Noncanonical for TNG+SDSS MZR; retain as SDSS-only 120,000-galaxy context or comparator. |
| `e2f3b038f8dd` | Noncanonical for TNG+SDSS MZR and not interchangeable with `2958462772b2`; retain as a separate SDSS 80,000-galaxy MZR-family output with explicit O/H values and a method/topic label mismatch. |

## Open Reconciliation Gaps

- Common O/H scale: SDSS calibration is absent across the four runs. TNG is stated as `SF-weighted gas metallicity -> O/H (solar-scaled)` in the TNG+SDSS runs, but no common TNG-vs-SDSS O/H calibration is established. Do not apply a dex offset from these captured fields.
- SDSS sample mismatch: SDSS `120,000` appears in `2958462772b2`, `d8de519cb9c9`, and `gated-e2e-demo`; SDSS `80,000` appears in `e2f3b038f8dd`.
- `e2f3b038f8dd` label mismatch: method/topic labels point to scaling-relation/main-sequence, but the result is an MZR with explicit O/H values.
- Citation integrity: `gated-e2e-demo` requires citation repair before being used as a clean candidate source.

## Assumptions

- Documentary traceability is judged from captured run JSON, draft TEX, histories, artifacts, baseline manifest, and approved cross-reference notes only.
- The identical summary string between `d8de519cb9c9` and `gated-e2e-demo` is sufficient to treat them as the same core TNG+SDSS analysis lineage for recommendation purposes, even though no explicit parent-run link is recorded.
- Hwao may still choose a different canonical target if Goru's repaired v2 matrix adds material provenance not present at the time of this Kun audit.

