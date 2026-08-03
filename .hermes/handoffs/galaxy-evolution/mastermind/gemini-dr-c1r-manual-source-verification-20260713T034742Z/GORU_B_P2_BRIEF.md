# Goru B-P2 brief — mechanical evidence spans

B-P1 persisted source acquisition is complete. Read:

- coordination `HWAO_PARALLEL_PLAN.md` and `ROLE_TABLE.md`;
- Gate B `sources/ROUTE_MAP.json`, `sources/EVIDENCE_CATALOG.json`, `sources/FETCH_LOG.jsonl`;
- Gate B `receipts/TORI_SOURCE_ACQUISITION_RECEIPT.md` and `TORI_NETWORK_VARIANCE_NOTE.md`;
- immutable triage ledger and structured capture referenced by the custody receipt.

Write only:

- `mechanical/ENTRY_SPAN_NOTES.jsonl` — exactly 73 JSON objects, one per `M001`–`M073` in order;
- `mechanical/ENTRY_SPAN_NOTES.md` — arithmetic and concise table.

For each entry record:

- manual_id, lane, code, source_refs, source_indices;
- exact claim/evidence snippet from route map;
- candidate persisted evidence path(s) actually inspected;
- exact matching/supportive or contradictory source span(s), with page number for PDF text when recoverable or a stable local text locator;
- evidence tier from the catalog;
- `mechanical_span_status` from exactly: `SPAN_FOUND`, `PARTIAL_SPAN_FOUND`, `NO_SPAN_FOUND`, `NO_BOUND_SOURCE`;
- any source-resolution or scope note.

Rules:

- Mechanical spans only; do not issue B1 verdicts.
- Do not infer scientific equivalence or comparability.
- Do not use the disclosed web-search result as evidence.
- No network use. Read only the persisted source store.
- No writes outside Gate B `mechanical/`.
- Exactly 73 entries; no duplication/omission; include lane × span-status arithmetic.
- End the markdown with `GORU_GATE_B_MECHANICAL_SPANS_DONE_20260713T034742Z`.

If an item requires semantic judgment, record the literal source passage and leave judgment to Lana. If no source is bound (`M018`), use `NO_BOUND_SOURCE`.
