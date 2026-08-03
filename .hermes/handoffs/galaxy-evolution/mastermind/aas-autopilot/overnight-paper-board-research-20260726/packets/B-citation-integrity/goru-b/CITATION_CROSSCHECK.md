# Citation Cross-Check

AI_DRAFT_NOT_HUMAN_GOLD

| citation_key | own_clause | own_reference_entry | own_clause_vs_own_reference | gate_supported_bool | gate_consistent_with_one_to_one | kun_action | lana_verdict | goru_one_to_one_finding |
|---|---|---|---|---|---|---|---|---|
| `Torrey2019` | `[Torrey2019] investigated the evolution of the mass-metallicity relation in IllustrisTNG` | `[Torrey2019] Torrey et al. (2019). The evolution of the mass-metallicity relation and its scatter in IllustrisTNG. bibcode 2019MNRAS.484.5587T` | MATCH | false | NO — COMPOUND-SENTENCE-CROSS-ASSIGNMENT | remove | gate-defect; split | Lana |
| `Qi2025` | `[Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50` | `[Qi2025] Qi et al. (2025). Star Formation Rates, Metallicities, and Stellar Masses on Kiloparsec Scales in TNG50. bibcode 2025ApJ...993...32Q` | MATCH | true | YES | retain | genuine; retain | both |
| `Guo2016` | `[Guo2016] studied the stellar mass-gas-phase metallicity relation at redshifts between 0.5 and 0.7` | `[Guo2016] Guo et al. (2016). Stellar Mass-Gas-phase Metallicity Relation at 0.5 <= z <= 0.7: A Power Law with Increasing Scatter toward the Low-mass Regime. bibcode 2016ApJ...822..103G` | MATCH | false | NO — COMPOUND-SENTENCE-CROSS-ASSIGNMENT | remove | gate-defect; split | Lana |
| `Garcia2023` | `[Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG` | `[Garcia2023] Garcia et al. (2023). Gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG. bibcode 2023MNRAS.519.4716G` | MATCH | true | YES | retain | genuine; retain | both |
| `Renzini2015` | `Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS by providing insights into its definition and characteristics.` | `[Renzini2015] Renzini et al. (2015). An Objective Definition for the Main Sequence of Star-forming Galaxies. bibcode 2015ApJ...801L..29R` | PARTIAL | true | YES | retain | genuine; retain | both |
| `Pearson2023` | `Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS by providing insights into its definition and characteristics.` | `[Pearson2023] Pearson et al. (2023). Influence of star-forming galaxy selection on the galaxy main sequence. bibcode 2023A&A...679A..35P` | PARTIAL | false | NO | remove | gate-defect; retain/remove | neither |

## Pearson2023 Mechanical Facts
- **Own Clause**: Pearson2023 does **not** have its own distinct per-author clause. It is a bare grouped citation sharing one predicate with Renzini2015 ("Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS...").
- **Reference Entry Topic**: The `lit_reflist` entry ("Influence of star-forming galaxy selection on the galaxy main sequence") **is** topically about the main sequence.
