# Lana B-P3 brief — 73 source-verification verdicts

B-P1 and B-P2 are complete and Hwao has kept Gate B GREEN. Read:

- coordination `HWAO_PARALLEL_PLAN.md` and `ROLE_TABLE.md`;
- Gate B `sources/ROUTE_MAP.json`, `sources/EVIDENCE_CATALOG.json`, and persisted metadata/text store;
- `mechanical/ENTRY_SPAN_NOTES.jsonl` and `.md`;
- `receipts/TORI_SOURCE_ACQUISITION_RECEIPT.md`, `TORI_NETWORK_VARIANCE_NOTE.md`, and `HWAO_NETWORK_VARIANCE_DISPOSITION.md`;
- immutable triage ledger/capture referenced by the custody receipt.

Write only:

- `verification/VERDICTS.jsonl` — exactly 73 JSON objects, ordered `M001`–`M073`;
- `verification/VERDICT_LEDGER.md` — concise row table plus lane × verdict arithmetic and review notes.

Each JSON object must contain:

- manual_id, lane, clause, code, source_refs, source_indices;
- exactly one verdict from: `SUPPORTED`, `SUPPORTED_WITH_SCOPE_NOTE`, `NOT_SUPPORTED`, `SOURCE_UNRESOLVED`, `EVIDENCE_INSUFFICIENT_ABSTRACT_ONLY`, `AMBIGUOUS_NEEDS_EXPERT`;
- exact persisted evidence path(s), evidence tier, and an exact source quotation/span sufficient to audit the verdict;
- plain-English rationale and scope note;
- for `VERIFY_SCIENTIFIC_COMPARABILITY`, a separate `semantic_comparability_assessment` explaining whether `MATCHED_SELECTIONS` is actually established by the cited source and row claim;
- `quarantine_status: QUARANTINED_PENDING_LOCAL_CHECK` for every entry.

Binding rules:

1. Verdict authority is Lana only; Goru spans are candidates, not conclusions.
2. Doubt resolves downward. Metadata/abstract-only evidence can never yield `SUPPORTED*`; aggregators/secondary discovery pages are not evidence.
3. Do not borrow an unrelated source for `M018`; use `SOURCE_UNRESOLVED` unless a bound source exists in the immutable unit (none is routed).
4. Index 32: use index-33 persisted full text, carry the exact note `32→33 same-work bibliographic mapping; byte identity unproven`, and cap at `SUPPORTED_WITH_SCOPE_NOTE`.
5. Sources 2/8/13 remain true-tier and are confined to document-level `M064`/`M065`.
6. `M064`/`M065` are document-level quality/fidelity reviews across all 37 indices; do not pretend one fuzzy span certifies the full set.
7. The eight comparability entries `M066`–`M073` require actual semantic reasoning; pay special attention to FLAMINGO kSZ and the BAHAMAS row that share source index 30.
8. No release from quarantine, no product/DB/wiki/prose/trust mutation.
9. No network, web search, browser, login, live model, dashboard, deploy, cron, or git action; read only persisted Gate B artifacts.
10. Any entry that cannot take exactly one pinned verdict must STOP and escalate rather than invent a seventh verdict.

End markdown with `LANA_GATE_B_VERDICTS_DONE_20260713T034742Z`.
