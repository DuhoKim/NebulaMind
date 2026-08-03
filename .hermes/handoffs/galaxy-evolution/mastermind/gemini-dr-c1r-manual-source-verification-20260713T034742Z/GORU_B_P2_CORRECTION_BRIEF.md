# Goru B-P2 custody-correction brief

A pre-B-P4 audit found one source-catalog contamination. Read:

- `sources/SUPPLEMENTAL_CONTAMINATION_CORRECTION.json`;
- corrected `sources/EVIDENCE_CATALOG.json` (V2);
- `receipts/TORI_SOURCE_ACQUISITION_RECEIPT.md` addendum;
- current `mechanical/ENTRY_SPAN_NOTES.jsonl` and `.md`.

Mechanical correction only; no verdict authority and no network.

1. Regenerate or patch both mechanical span-note files so the quarantined text path `sources/text/idx01_supplemental_arxiv_pdf_89976fa297d0.txt` and the invalid supplemental metadata for indices 1/3/4 occur nowhere in their candidate, selected, matched, or evidence paths.
2. Preserve all 73 entry IDs/order and all valid matched spans/paths. Confirm no existing `matched_path` used the quarantined file.
3. Re-run 73/73 reconciliation, path-existence checks, and index/path alignment. Cross-index paths remain allowed only for declared index29→14 duplicate custody and index32→33 same-work mapping.
4. Add a correction section to the markdown ending with `GORU_GATE_B_SPANS_CORRECTED_20260713T034742Z`.
5. Write nothing outside `mechanical/`; clean temporary files.

No verdict changes, network, browser, live run, DB, dashboard, deploy, cron, git, or publication.
