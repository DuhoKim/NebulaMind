# Kun Reproducibility Verdict — 2913/2921 Docs-First Lane

Marker: `2913_2921_DOCS_FIRST_LANE_VERDICT_20260705T143217Z`

## Verdict

PASS. The current docs-first lane is reproducible from local artifacts plus the read-only snapshot, and the next safe work is full-text pinning/source-hardening only. I found no docs-only disposition gap requiring a new disposition decision.

## What I Verified

- Read `.hermes/handoffs/2913_2921_docs_first_20260705T143217Z/VISIBLE_2913_2921_DISPOSITION_BRIEF.md`.
- Confirmed `CURRENT_STATE_READONLY_SNAPSHOT.json` reports `overall_current_state_matches_prior_execution: true`.
- Confirmed required snapshot invariants:
  - claim 2948 exists.
  - claims 2913 and 2921 are `parent_replaced`.
  - evidence 26678 and 26679 are on claim 2948.
  - evidence 26694 is on claim 2546.
  - target evidence dependency rows are `0`.
- Confirmed the new handoff lane has no `.sql`, `apply`, or rollback artifact names.
- Confirmed old decision-packet source files are locally present and hash-match the old packet manifest for:
  - `2605.31052v1_pdf_text.txt`
  - `2605.31052v1_targeted_snippets.json`
  - `2210.03747v2_pdf_text.txt`
  - `2210.03747v2_targeted_snippets.json`
  - `1308.5224v1_pdf_text.txt`
  - `1308.5224v1_targeted_snippets.json`
- Confirmed `pdf_extraction_summary.json` has nontrivial extracted text coverage for all three sources.
- Confirmed every entry in `selected_source_snippets.json` anchors back into its corresponding local extracted PDF text.

## Reproducibility Notes

The snapshot is reproducible as a fixed invariant check over the current lane JSON:

- expected claim statuses and evidence bindings are explicit in `CURRENT_STATE_READONLY_SNAPSHOT.json`;
- the prior source basis is pinned by the old decision packet manifest;
- selected snippets are reproducible from local extracted PDF text without network or database writes.

One caveat: the snapshot itself is a read-only state artifact, not a self-contained SQL transcript. Reproducing it from the live DB would require read-only SELECTs in a future verifier, but not SQL apply and not a mutation packet.

## No-SQL Full-Text Pinning Checker Shape

Recommended checker inputs:

- `CURRENT_STATE_READONLY_SNAPSHOT.json`
- `docs/galaxy_2913_2921_readonly_decision_packet_20260704T131018Z/artifacts/manifest.json`
- `source_text/*_pdf_text.txt`
- `source_text/*_targeted_snippets.json`
- `source_text/selected_source_snippets.json`
- `source_text/pdf_extraction_summary.json`

Recommended checks:

1. Validate current-state invariants from the snapshot JSON against the accepted disposition target map.
2. Validate SHA-256 for the three local full-text files and three targeted-snippet files against the old manifest.
3. Validate extraction coverage thresholds: each full-text file exists, is nonempty, and has the expected arXiv ID in `pdf_extraction_summary.json`.
4. Normalize whitespace in each selected snippet and confirm it appears in the matching local `*_pdf_text.txt`.
5. Emit a docs-only JSON/MD pinning report with source ID, file SHA, snippet query, snippet anchor status, and disposition role.
6. Refuse to create `.sql`, `apply`, rollback, migration, prose publish, or git/runtime artifacts.

## Boundary

No SQL/apply was run. No DB writes, prose/wiki/page-version writes, trust recompute, git action, restart, deploy, or rollback were performed.
