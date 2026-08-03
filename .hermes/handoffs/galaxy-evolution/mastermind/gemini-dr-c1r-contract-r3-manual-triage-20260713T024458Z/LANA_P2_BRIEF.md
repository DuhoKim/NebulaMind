# Lana P2 brief — classify the verified 73-entry manual queue

P1a is accepted after the standalone-contract completeness correction. P1b extraction independently passed. Read `HWAO_PLAN.md`, `HWAO_PLAN_AMENDMENT_1.md`, `triage/GORU_MANUAL_QUEUE_TABLE.json`, `design/CONTRACT_R3_DRAFT.md`, and the repaired validator result/body refs as needed.

First, align only `design/CONTRACT_R3_DRAFT.md` §9 with Amendment A3: replace the misleading statement that the eight deterministic D3 findings are triage entries. State explicitly that those eight remain outside the 73-entry manual ledger, and give the deterministic crosswalk D1↔6 unlabeled comparisons, D2↔SIMBA missing qualifier, D3↔8 S2 Result-cell failures, D4↔C7 integrity, D5↔GAP granularity history.

Then create:

- `triage/TRIAGE_LEDGER.json`
- `triage/TRIAGE_LEDGER.md`

Requirements:

1. Classify exactly M001–M073, source order, one of Hwao's five pinned lanes exactly once.
2. Do not force nonzero counts. `CONTRACT_R3_CHANGE` and/or `IGNORE_FOR_THIS_CONTRACT_TEST` may be zero. Follow Amendment A1.
3. Ties break toward a `VERIFY_*` lane. Classification is routing, not scientific adjudication.
4. Preserve verbatim: `manual_id`, `finding_ordinal`, `clause`, `code`, `status`, and `source_refs`.
5. JSON entries additionally include `lane`, a one-line `reason`, and `absorbing_d_item` (`D1`…`D6` only for `CONTRACT_R3_CHANGE`, otherwise null). Preserve `evidence_snippet` for auditability.
6. Top-level JSON includes schema marker, Goru input sha256, total, all-five-lane counts including zeros, clause:code counts, cross-map for any `CONTRACT_R3_CHANGE` entries, and explicit zero-lane objects/reasons.
7. Markdown lists all 73 entries, provides lane and clause:code arithmetic, and ends with exact `ZERO_LANE <name>: no entry fit because <reason>` lines for each zero lane.
8. “Ignore” never means accepted; any ignored entry must include one-clause residual risk. If no entry meets that definition, leave the lane zero.
9. The eight deterministic D3 findings must not appear as queue entries.
10. End Markdown with `LANA_R3_TRIAGE_CLASSIFICATION_DONE_20260713T024458Z`; JSON marker `LANA_R3_TRIAGE_LEDGER_V1`.

No source retrieval or scientific/source-fidelity conclusion. Writes only `design/CONTRACT_R3_DRAFT.md` and `triage/TRIAGE_LEDGER.*`. No live/network/browser/git/DB/dashboard/deploy/cron/account action.
