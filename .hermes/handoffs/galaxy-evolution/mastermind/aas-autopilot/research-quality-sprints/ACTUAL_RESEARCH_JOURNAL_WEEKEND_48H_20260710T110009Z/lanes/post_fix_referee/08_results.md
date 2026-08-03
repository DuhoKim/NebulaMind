Read-only referee report. I inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json` first, then the flagship, supplement, and cycle audit. I did not edit files.

**Integrity Blockers**
- Numeric invariant mismatch remains: `CYCLE_08_results_AUDIT.json` says the required missing invariant is `[-1.334,-1.283]`, while the flagship repeatedly reports `[-1.334,-1.282]` in the abstract, table, figure caption, and conclusion: `flagship_rp1/aastex/rp1_flagship_polished.tex:13`, `:57`, `:65`, `:74`; audit lines `CYCLE_08_results_AUDIT.json:57-70`. This must be resolved against the real retained artifact before journal submission.
- Provenance is present, not absent: custody inventories 13 real CSV/JSON artifacts, including the 60,000-row analysis cache and 8,146-row matched-pair file, with hashes and no copied source data: `provenance/REAL_DATA_SOURCE_CUSTODY.json:15-47`, `:176-178`. The audit reports `custody_valid: true` and `new_result_without_provenance: false`: `CYCLE_08_results_AUDIT.json:87-93`.

**Journal-Quality Blockers**
- The flagship is still too thin for a flagship journal article: audit reports about 2,804 words, 110-word abstract, zero displayed equations, one table, and no explicit quantitative comparison to prior work: `CYCLE_08_results_AUDIT.json:61-75`, `:95-103`.
- The supplement is closer, but still below the stated target at about 3,570 words and should not pass while the audit flags it: `CYCLE_08_results_AUDIT.json:74`, `:101`.
- Compile succeeds but is not warning-clean: 12 overfull and 9 underfull boxes remain: `CYCLE_08_results_AUDIT.json:3-9`, `:50-53`, `:103`.
- Workflow/safety prose remains in the manuscript body/data availability, especially “No mock, synthetic, fake, placeholder, or toy data…” in the flagship and supplement: `flagship_rp1/aastex/rp1_flagship_polished.tex:78`, `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:158`, `:208`. That belongs in provenance/audit material, not the journal text.

**Boundary Assessment**
RP-1 association-only wording is mostly preserved. The flagship repeatedly states that the result is fiber-centered, morphology-uncontrolled, selection-limited, and not causal: `flagship_rp1/aastex/rp1_flagship_polished.tex:18-28`, `:69-75`. The supplement also correctly treats radio, X-ray, CO/HI, IFU, environment, and simulation material as missing observables rather than measured results: `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:21-28`, `:71-85`, `:204-205`.

**Required Section-Level Improvements**
- Flagship abstract: expand to a journal-ready structured abstract with denominator, selection, matching rule, exact invariant, uncertainty method, and the morphology/aperture caveat.
- Flagship data/methods: add at least two displayed equations defining BPT demarcations or standardized matching distance and the paired offset statistic.
- Flagship results: add real-data-derived tables for class counts, matching-balance diagnostics, and pair-offset summary; do not invent sensitivity analyses unless retained artifacts exist.
- Flagship interpretation: add an explicit quantitative prior-work comparison. Suitable source-identified anchors already in the bibliography include Schawinski et al. 2010, ApJ 711, 284, DOI `10.1088/0004-637X/711/1/284`; Bluck et al. 2014, MNRAS 441, 599, DOI `10.1093/mnras/stu504`; Piotrowska et al. 2022, MNRAS 512, 1052, DOI `10.1093/mnras/stac532`; Cid Fernandes et al. 2011, MNRAS 413, 1687, DOI `10.1111/j.1365-2966.2011.18244.x`; Belfiore et al. 2016, MNRAS 461, 3111, DOI `10.1093/mnras/stw1234`.
- Supplement: convert the atlas from terse note blocks into a more explicit appendix-style product: for each of the eight entries, include source artifact, measured optical baseline, exact missing observable, non-interpretation boundary, and future join path.
- Supplement references: keep adding identifiers for currently partial citations. Examples needing completion include Baldwin et al. 1981 PASP 93, 5; Brinchmann et al. 2004 MNRAS 351, 1151; Fabian 2012 ARA&A 50, 455; Wetzel et al. 2013 MNRAS 432, 336. If identifiers are not verified locally, mark them “unverified / do not integrate” until checked.

JOURNAL_LEVEL_PASS: NO