Read-only referee pass completed. I did not edit files.

**Integrity / Reproducibility Blockers**
- Custody is present: `provenance/REAL_DATA_SOURCE_CUSTODY.json` inventories the 60,000-row cache, 8,146-pair file, topic JSONs, hashes, and active manuscript hashes.
- I did not find a mock/synthetic-data integrity violation in the candidate text. Numeric invariants are preserved: 60,000 galaxies, 8,146 pairs, median offset `-1.309` dex, CI `[-1.334,-1.283]`, class counts `39,553 / 12,234 / 8,146 / 67`.
- Reproducibility remains blocked for journal level: both manuscripts state the package lacks executable analysis scripts and frozen command recipes. A custody manifest is not enough to regenerate results.
- The public parent count `249,917` and `24.0%` cache coverage are correctly caveated as context, but they still need SQL/query receipts before journal integration.

**Journal-Quality Blockers**
- Flagship is still too short and underdeveloped for a main journal article: audit reports about 3,193 words, 110-word abstract, one table, no displayed equations, and no explicit quantitative comparison to prior work.
- Supplement is useful as an atlas, but reads like a compact internal checklist. It needs stronger per-entry reproducibility tables: artifact, JSON field names, exact measured value, selection denominator, and missing-observable boundary.
- Compile is not journal-clean: audit reports `overfull=21`, `underfull=19`; logs show severe overfull boxes in data-availability/hash paragraphs and a stuck float warning in the supplement.
- Many bibliography entries still contain `source identifier unverified / do not integrate`, including core SDSS/BPT/catalog references. Those must be verified or removed before submission.

**Concrete Section-Level Improvements**
- Flagship `Abstract`: expand to AAS-style 200-350 words with selection, matching, result, limitations, and reproducibility status.
- Flagship `Data and shared selection`: add a selection-flow table and a formal matching definition/equation; include query receipt paths for the `249,917` parent if retained.
- Flagship `Matched-control result`: add at least two real-data-derived tables: balance diagnostics and denominator/class-count table.
- Flagship `Interpretation`: add quantitative prior-work comparison, but only with verified identifiers.
- Supplement `Provenance map`: add field-level mapping from each quoted number to the inventoried JSON key or CSV column.
- Supplement `Atlas notes`: split long paragraphs, move repeated caveats to shared limitations, and add one compact “Measured / Not measured / Required follow-up” table per topic.
- Both bibliographies: replace unverified references with DOI/ADS/arXiv identifiers or mark them explicitly as “unverified / do not integrate” and do not cite them in submission text.

**Literature Identifier Requirements**
Examples needing verification before integration include SDSS DR17, Baldwin 1981, Brinchmann 2004, Kewley 2001/2006, York 2000, Fabian 2012, Heckman & Best 2014, Peng 2010, Wetzel 2013, Schaye 2015. Current manuscript labels them “unverified / do not integrate,” which is acceptable for review but not for journal submission.

JOURNAL_LEVEL_PASS: NO