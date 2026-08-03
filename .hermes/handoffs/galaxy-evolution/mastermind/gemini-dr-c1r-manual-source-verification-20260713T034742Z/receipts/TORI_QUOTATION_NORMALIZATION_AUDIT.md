# Tori Gate B quotation-normalization audit

Kun correctly reported that 29 `source_quotation` excerpts were not whole-string matches under a simple whitespace-normalized substring test. The excerpts are mechanically truncated with leading/trailing or internal ellipses, so the entire rendered excerpt—including the ellipsis marker—is not expected to occur verbatim in PDF text.

Tori reran the check over all 73 entries using only deterministic text normalization:

1. Unicode NFKC;
2. remove soft hyphens;
3. normalize Unicode dash variants;
4. collapse whitespace;
5. remove boundary ellipsis markers and, where an internal ellipsis exists, require every non-trivial fragment to occur in at least one active evidence path.

Result:

- non-empty source excerpts: **59**;
- normalized excerpt/fragments found in active evidence: **59/59**;
- empty excerpts: **14**, exactly M018 plus the `NONE`-tier ambiguous entries M053–M056, M058, M066–M073;
- quarantined contamination path used: **0**;
- verdicts or evidence files edited: **0**.

This resolves the mechanical excerpt-representation exception without claiming that ellipsis markers are verbatim source characters. Hwao's fixed B-P5 sample still performs the independent semantic/source review.

TORI_GATE_B_QUOTATION_NORMALIZATION_AUDIT_DONE_20260713T034742Z
