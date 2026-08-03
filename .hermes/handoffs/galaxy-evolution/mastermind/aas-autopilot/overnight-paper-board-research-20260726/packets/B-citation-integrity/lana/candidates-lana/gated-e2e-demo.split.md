# gated-e2e-demo — Split / Re-ground Candidate (Lana)

AI_DRAFT_NOT_HUMAN_GOLD

Fix type: **sentence-splitting / re-grounding** (preserves Torrey2019 and Guo2016; NO removal).

Purpose: cure the compound-sentence / key-assignment gate defect by giving each citation its own single-citation sentence, using ONLY existing passage wording and the run's existing reference list. No new source, no new citation, no new scientific claim, no weakened or deleted caveat.

## Citations addressed

| citation_key | gate verdict | Lana verdict | action |
|---|---|---|---|
| Torrey2019 | unsupported | gate-defect (compound-sentence) | split onto its own sentence (preserved) |
| Guo2016 | unsupported | gate-defect (compound-sentence) | split onto its own sentence (preserved) |
| Qi2025 | supported | confirmed supported | split onto its own sentence (preserved) |
| Garcia2023 | supported | confirmed supported | split onto its own sentence (preserved) |

## Original Introduction (verbatim from source `draft.tex`)

Recent studies have explored the relationship between galaxy properties such as mass, metallicity, and star formation rates. For instance, [Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50, while [Torrey2019] investigated the evolution of the mass-metallicity relation in IllustrisTNG. Additionally, [Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG, and [Guo2016] studied the stellar mass-gas-phase metallicity relation at redshifts between 0.5 and 0.7. These works provide valuable context for understanding the complex interplay between galaxy properties.

## Split / Re-grounded Introduction Candidate

Recent studies have explored the relationship between galaxy properties such as mass, metallicity, and star formation rates. For instance, [Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50. [Torrey2019] investigated the evolution of the mass-metallicity relation in IllustrisTNG. Additionally, [Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG. [Guo2016] studied the stellar mass-gas-phase metallicity relation at redshifts between 0.5 and 0.7. These works provide valuable context for understanding the complex interplay between galaxy properties.

## Exact edits (grammar only, zero content change)

| location | before | after |
|---|---|---|
| Qi2025 / Torrey2019 boundary | `... on kpc-scales in TNG50, while [Torrey2019] investigated ...` | `... on kpc-scales in TNG50. [Torrey2019] investigated ...` |
| Garcia2023 / Guo2016 boundary | `... in IllustrisTNG, and [Guo2016] studied ...` | `... in IllustrisTNG. [Guo2016] studied ...` |

Only the connectives `, while` and `, and` were replaced with a sentence break `. `. Every scientific token, citation, and caveat is preserved verbatim. After the split, each citation's sentence contains only that citation and its own content, so a per-sentence entailment check has no co-citation to mis-assign.

## Reference List Retained From Source Run (unchanged, all 5 entries)

[Qi2025] Qi et al. (2025). Star Formation Rates, Metallicities, and Stellar Masses on Kiloparsec Scales in TNG50. bibcode 2025ApJ...993...32Q

[Torrey2019] Torrey et al. (2019). The evolution of the mass-metallicity relation and its scatter in IllustrisTNG. bibcode 2019MNRAS.484.5587T

[Garcia2023] Garcia et al. (2023). Gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG. bibcode 2023MNRAS.519.4716G

[Guo2016] Guo et al. (2016). Stellar Mass-Gas-phase Metallicity Relation at 0.5 <= z <= 0.7: A Power Law with Increasing Scatter toward the Low-mass Regime. bibcode 2016ApJ...822..103G

[LaraLopez2013] Lara-Lopez et al. (2013). Galaxy and mass assembly (GAMA): the connection between metals, specific  SFR and hi gas in galaxies: the Z-SSFR relation.. bibcode 2013MNRAS.433L..35L
