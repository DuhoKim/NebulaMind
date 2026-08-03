# Duplication Analysis

AI_DRAFT_NOT_HUMAN_GOLD

Marker: OVERNIGHT_PAPER_BOARD_PACKET_A_KUN_DUPLICATION_ANALYSIS_V1

Classification vocabulary: `exact-duplicate`, `superset-subset`, `near-duplicate-different-sample`, `distinct`.

No pair is an `exact-duplicate` because every pair differs in at least one of artifacts, gates, data sources, method/topic labels, sample size, or draft/review state.

## Pairwise Classifications

| run pair | classification | basis |
|---|---|---|
| `d8de519cb9c9` vs `gated-e2e-demo` | `superset-subset` | The `result.summary` strings are identical: TNG100 `23,722` plus SDSS `120,000`, same `mass-metallicity` method, same `tng, sdss` data-source set, and same `result.png` artifact name. `d8de519cb9c9` has figure/summary/history only and says the full draft is queued; `gated-e2e-demo` adds draft PDF/TEX, review loop, novelty/expected-value/citation gates, literature references, and a compiled manuscript. |
| `2958462772b2` vs `d8de519cb9c9` | `superset-subset` | Both use `method=mass-metallicity` and SDSS `120,000`. `2958462772b2` is SDSS-only drafted/reviewed; `d8de519cb9c9` adds TNG100 `23,722` and a TNG solar-scaled O/H statement but lacks a draft/review. The relationship is partial-content subset/superset, not artifact supersession. |
| `2958462772b2` vs `gated-e2e-demo` | `superset-subset` | Both use `method=mass-metallicity` and SDSS `120,000`; both have draft/PDF/review artifacts. `gated-e2e-demo` adds TNG100 `23,722`, gates, lit references, and TNG solar-scaled O/H wording. `2958462772b2` is SDSS-only and lacks gates/literature references. |
| `2958462772b2` vs `e2f3b038f8dd` | `near-duplicate-different-sample` | Both are SDSS-only MZR-family outputs, but `2958462772b2` uses `method=mass-metallicity`, topic `cosmic-chemical-evolution`, SDSS `120,000`, and has draft/PDF/review artifacts. `e2f3b038f8dd` reports an MZR from SDSS `80,000` star-forming galaxies with explicit `12+log(O/H)` values and only `mzr.png`/history; its method/topic labels differ. |
| `d8de519cb9c9` vs `e2f3b038f8dd` | `near-duplicate-different-sample` | Both are MZR-family and include SDSS, but `d8de519cb9c9` is TNG+SDSS with SDSS `120,000` and TNG `23,722`, while `e2f3b038f8dd` is SDSS-only `80,000` with explicit O/H ordinate values. Methods/labels and artifacts differ. |
| `e2f3b038f8dd` vs `gated-e2e-demo` | `near-duplicate-different-sample` | Both are MZR-family and include SDSS, but `gated-e2e-demo` is TNG+SDSS with SDSS `120,000`, TNG `23,722`, draft/review/gates, and no explicit O/H point values; `e2f3b038f8dd` is SDSS-only `80,000` with explicit `12+log(O/H)` values and no draft/gates. |

## Redundancy Notes

- `d8de519cb9c9` is redundant as a standalone build input if the goal is to represent the already-gated TNG+SDSS MZR analysis, because `gated-e2e-demo` carries the same summary and adds the draft/review/gate layer.
- `2958462772b2` is not a duplicate of the TNG+SDSS runs; it is a narrower SDSS-only 120,000-galaxy MZR run.
- `e2f3b038f8dd` is not a duplicate of `2958462772b2`; it is a different SDSS sample size and has explicit O/H values but weaker label/provenance alignment.

