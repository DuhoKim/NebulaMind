# Lana B-P3 evidence-path custody correction brief

A pre-B-P4 audit found a quarantined supplemental source path. Read:

- `sources/SUPPLEMENTAL_CONTAMINATION_CORRECTION.json`;
- corrected `sources/EVIDENCE_CATALOG.json` (V2);
- `receipts/TORI_SOURCE_ACQUISITION_RECEIPT.md` addendum;
- current `verification/VERDICTS.jsonl` and `VERDICT_LEDGER.md`.

Correct only evidence custody; do not change scientific verdicts, quotations, rationales, scope notes, IDs, order, or totals.

1. Remove `sources/text/idx01_supplemental_arxiv_pdf_89976fa297d0.txt` from every `evidence_paths` array (currently expected on M001–M004, M019–M025, M064, M065).
2. Verify each affected entry retains at least one correct source-index-aligned T2 path, except document-level entries where many correct paths remain.
3. Verify no quarantine file/metadata from the correction manifest appears anywhere in either verdict deliverable.
4. Re-run the full 73-entry schema/order/enum/quarantine/path-existence checks and preserve the exact verdict distribution.
5. Add a load-bearing ledger note describing the correction and end with both the original marker and `LANA_GATE_B_VERDICTS_CUSTODY_CORRECTED_20260713T034742Z`.
6. Write only under `verification/`; clean temporary files.

No new source reading, verdict changes, network, browser, live run, DB, dashboard, deploy, cron, git, or publication.
