# GORU PACKET B RECEIPT

## Files Produced (SHA-256)
* `CITATION_CROSSCHECK.csv`: 956648906be1c165a3772a4541c9087c7f5caa7d98a53c7d534653b80be1694c
* `CITATION_CROSSCHECK.md`: 275639b2d8d92b8b6ab8e25577015f5725f9ad5007391e4ca9aa35d5db763c19
* `CANDIDATE_DIFF_VERIFICATION.md`: 3ed85fa371c2ec3b1e79ef59257afd14ded6421983803db5b5b146f1b4419301

## Per-Run Concordance Verdict
* **`gated-e2e-demo`**: The mechanical one-to-one evidence definitively supports **Lana's split**. Kun's removal candidate discarded verbatim matching clauses that fully supported their respective citations (Torrey2019, Guo2016). The gate's unsupported verdicts were compound-sentence cross-assignment artifacts.
* **`gated-halt-demo`**: The mechanical one-to-one evidence definitively supports **neither** Kun's removal nor Lana's split (as there is no distinct clause to split). Pearson2023 is a bare grouped citation. Lana correctly identified this as a judgment call rather than a clean split.

## Split/Removal Verification Results & Discrepancies
* **Lana Split (`gated-e2e-demo.split.md`)**: VERIFIED. The only changes made were connective replacements (`, while ` → `. ` and `, and ` → `. `). All 4 citations appear isolated, and all 5 reference entries are retained verbatim.
* **Kun Removal (`gated-halt-demo.corrected.md`)**: VERIFIED. Only the `[Pearson2023]` citation was removed, and local grammar adjusted to singular. No other content changed.
* **Kun Removal (`gated-e2e-demo.corrected.md`)**: **DISCREPANCY**. While it successfully removed exactly the Torrey2019 and Guo2016 clauses from the introduction, it also silently removed `[LaraLopez2013]` from the Reference List. This violates the instruction that no other content should be changed. The removal also discarded valid anchors whose own-clause content matched their own reference entries.

## Pearson2023 Mechanical Facts
- **Own Clause**: Pearson2023 does **not** have its own distinct per-author clause. It is a bare grouped citation sharing one predicate with Renzini2015 ("Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS...").
- **Reference Entry Topic**: The `lit_reflist` entry ("Influence of star-forming galaxy selection on the galaxy main sequence") **is** topically about the main sequence.

## Completion State
DONE

OVERNIGHT_PAPER_BOARD_PACKET_B_GORU_CROSSCHECK_COMPLETE_V1
