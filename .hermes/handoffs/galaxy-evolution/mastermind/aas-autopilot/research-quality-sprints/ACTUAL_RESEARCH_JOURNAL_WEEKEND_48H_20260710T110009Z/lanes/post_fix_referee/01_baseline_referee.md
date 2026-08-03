**Baseline Referee Verdict**

I inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json` before judging provenance. The custody receipt is present, marks `no_mock_or_synthetic_data: true`, inventories the real source artifacts with paths, hashes, byte counts, and approximate row counts, and records `source_data_copied: false` and `source_data_mutated: false`. The core RP-1 result traces to inventoried `analysis_results.json` plus `matched_agn_sf_pairs.csv`; the supplement maps all eight atlas entries to inventoried JSON artifacts.

**Integrity Blockers**

None for the core retained matched-control result. The key invariants are preserved: 60,000-galaxy cache, 8,146 matched pairs, median offset `-1.309 dex`, 95% interval `[-1.334,-1.283]`, and association-only RP-1 language.

One provenance-adjacent risk remains: the public selection cascade counts at flagship lines 41-49 and supplement lines 33-41 are explicitly described as contextual because the custody receipt does not inventory the SQL query logs. That is acceptable only if they remain context. Before journal submission, either add query receipts for `501,060`, `416,554`, `373,445`, `249,917`, `176,523`, and `91,768`, or move those rows to a clearly non-result appendix.

**Journal-Quality Blockers**

The flagship is still too short and underdeveloped for a journal-level main paper. It has the right claim boundary, but it reads like a compressed note rather than a full article. Required section-level improvements: expand Data/Selection with an explicit SQL/query provenance appendix or receipt table; expand Classification/Matching with formulas for BPT cuts and the standardized-distance metric; add a Results subsection with target/control balance diagnostics; add a Discussion subsection quantitatively comparing the `-1.309 dex` offset to prior morphology/AGN-sSFR literature without turning that comparison into a new measured result.

The supplement is better bounded but still over-compressed. Required section-level improvements: split the very long atlas paragraphs, especially lines 87-88 and 152-153, into reproducible fields: denominator, measured proxy, missing observable, bias, allowable interpretation. Add one compact table per atlas note giving numerator/denominator/proxy/artifact hash. Keep all physical interpretations explicitly downstream of missing radio/X-ray/CO/HI/IFU/group-catalog data.

The package still fails the audit’s presentation gate: abstract below target length, flagship below target length, no displayed equations, fewer than three real-data-derived flagship tables, no explicit quantitative prior-work comparison, supplement below target length, and compile warning cleanliness not met.

**Literature Integration**

Do not add unverified citations. Safe source identifiers already suitable for targeted comparison or methods context include: Baldwin et al. 1981, PASP, 93, 5, ADS `1981PASP...93....5B`; Kewley et al. 2001, ApJ, 556, 121, ADS `2001ApJ...556..121K`; Kauffmann et al. 2003, MNRAS, 346, 1055, ADS `2003MNRAS.346.1055K`; Brinchmann et al. 2004, MNRAS, 351, 1151, ADS `2004MNRAS.351.1151B`; Best et al. 2005, MNRAS, 362, 25, ADS `2005MNRAS.362...25B`; Cid Fernandes et al. 2011, MNRAS, 413, 1687, ADS `2011MNRAS.413.1687C`; Belfiore et al. 2016, MNRAS, 461, 3111, ADS `2016MNRAS.461.3111B`; Piotrowska et al. 2022, MNRAS, 512, 1052, ADS `2022MNRAS.512.1052P`.

JOURNAL_LEVEL_PASS: NO