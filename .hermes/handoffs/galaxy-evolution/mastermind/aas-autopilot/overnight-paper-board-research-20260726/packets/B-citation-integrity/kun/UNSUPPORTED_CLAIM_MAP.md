# Unsupported-Claim / Citation Map

Marker: OVERNIGHT_PAPER_BOARD_PACKET_B_KUN_CITATIONMAP_V1

Source hash check: PASS. `shasum -a 256 -c baseline/INPUT_SHA256.txt` returned OK for all 38 captured source files.

Scope check: only `gated-e2e-demo.json`, `gated-halt-demo.json`, and `fesc002.json` contain `citation_entailment` blocks among the top-level baseline run JSON files. No `expected_value` verdict is `CONTRADICTS` in these scoped runs.

## Counts

| run_id | citation_entailment.checked | unsupported | adversarial | checked citations | not-checked references recorded |
|---|---:|---:|---|---|---|
| gated-e2e-demo | 4 | 2 | not recorded | Torrey2019, Qi2025, Guo2016, Garcia2023 | lit_reflist also includes LaraLopez2013; `lit_refs` also includes 2021ApJ...919..143H |
| gated-halt-demo | 2 | 1 | not recorded | Renzini2015, Pearson2023 | lit_reflist also includes CorchoCaballero2020, Berti2021, Leslie2016; `lit_refs` also includes 2015ApJ...801...80L |
| fesc002 | 0 | 0 | true | none | lit_reflist includes Muoz2024, Davies2021, Park2022, Duncan2015, Madau2017; `lit_refs` also includes 2020MNRAS.496.4342L |

For `fesc002`, the citation gate has `checked: 0`, `all: []`, and `unsupported: []`. Therefore no citation is checked-and-supported; all listed references are explicitly recorded here as not checked by the gate rather than silently treated as supported.

## One-to-One Gate Rows

| run_id | citation_key | sentence | gate_verdict | gate_reason | kun_adjudication |
|---|---|---|---|---|---|
| gated-e2e-demo | Torrey2019 | For instance, [Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50, while [Torrey2019] investigated the evolution of the mass-metallicit | unsupported | UNSUPPORTED<br>THE PASSAGE ONLY MENTIONS TORREY'S WORK ON THE EVOLUTION OF THE MASS-METALLICITY RELATION IN ILLUSTRISTNG, BUT DOES NOT MENTION QI2025 OR THEIR EXA | agree - gate row has `supported: false` for key Torrey2019; the stored reason says the compared passage does not cover the other citation content in the same sentence. |
| gated-e2e-demo | Qi2025 | For instance, [Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50, while [Torrey2019] investigated the evolution of the mass-metallicit | supported | SUPPORTED<br>THE PASSAGE MENTIONS QI (LIKELY "QI2025") EXAMINING STAR FORMATION RATES IN TNG50 AND ALSO MENTIONS PAUL TORREY (LIKELY RELATED TO "TORREY2019"), PROV | agree - gate row has `supported: true` for key Qi2025 and the reason explicitly matches Qi/TNG50 content. |
| gated-e2e-demo | Guo2016 | Additionally, [Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG, and [Guo2016] studied the stellar mass-gas-phase metallicity relatio | unsupported | UNSUPPORTED<br>THE PASSAGE ONLY MENTIONS GUO'S STUDY, BUT NOT GARCIA'S ANALYSIS OF GAS-PHASE METALLICITY BREAK RADII. | agree - gate row has `supported: false` for key Guo2016; the stored reason says the compared passage does not cover the other citation content in the same sentence. |
| gated-e2e-demo | Garcia2023 | Additionally, [Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG, and [Guo2016] studied the stellar mass-gas-phase metallicity relatio | supported | SUPPORTED<br>THE PASSAGE MENTIONS "GAS-PHASE METALLICITY BREAK RADII OF STAR-FORMING GALAXIES IN ILLUSTRISTNG" WHICH IS THE SAME FACT AS THE CLAIM ABOUT GARCIA'S A | agree - gate row has `supported: true` for key Garcia2023 and the reason explicitly matches gas-phase metallicity break radii in IllustrisTNG. |
| gated-halt-demo | Renzini2015 | Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS by providing insights into its definition and characteristics. | supported | SUPPORTED<br>THE PASSAGE MENTIONS RENZINI AS AN AUTHOR, WHICH MATCHES THE CLAIM THAT REFERENCES [RENZINI2015], INDICATING HIS WORK HAS CONTRIBUTED TO UNDERSTANDING | agree - gate row has `supported: true` for key Renzini2015 and the reason identifies Renzini as matching the cited work. |
| gated-halt-demo | Pearson2023 | Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS by providing insights into its definition and characteristics. | unsupported | UNSUPPORTED<br>THE PASSAGE DOES NOT MENTION PREVIOUS WORKS OR AUTHORS LIKE RENZINI2015 AND PEARSON2023. | agree - gate row has `supported: false` for key Pearson2023 and the reason says the compared passage does not mention Pearson2023. |

