# Goru P1b brief — deterministic manual-queue extraction

P0 is OPEN: lane ACKs exist and Kun custody is GREEN.

Source, read-only:
`../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/readjudication/validator_result_v2.json`

Create only:

- `triage/GORU_MANUAL_QUEUE_TABLE.json`
- `triage/GORU_MANUAL_QUEUE_TABLE.md`

Requirements:

1. Select findings whose `status` is exactly `MANUAL_REVIEW_REQUIRED`, preserving source order.
2. There must be exactly 73 entries. If not, stop and write no done marker.
3. Assign stable `manual_id` values `M001`…`M073` and preserve the 1-based original `finding_ordinal` from the complete findings array.
4. JSON entry fields: `manual_id`, `finding_ordinal`, `clause`, `code`, `status`, `source_refs` (verbatim JSON), `evidence` (verbatim), and deterministic `evidence_snippet` (first 240 Unicode characters of evidence; if evidence is not a string, compact JSON serialization then first 240 characters).
5. JSON top level: schema marker, source relative path, source sha256, total, exact clause:code counts, and entries.
6. Markdown table must list every entry with manual ID, finding ordinal, clause, code, source_refs, and escaped one-line snippet, followed by exact clause:code arithmetic summing to 73.
7. Do not classify, interpret, verify sources, or invent fields.
8. JSON marker: `GORU_MANUAL_QUEUE_EXTRACT_V1`; Markdown final marker: `GORU_R3_TRIAGE_EXTRACTION_DONE_20260713T024458Z`.
9. Remove any `_tmp_*` file before completion.

Write boundary: `triage/GORU_*` and temporary in-packet `_tmp_*` only. Standing Antigravity cap ≤40% of the 5h window. No network/browser/git/DB/dashboard/deploy/cron/account/secret action.
