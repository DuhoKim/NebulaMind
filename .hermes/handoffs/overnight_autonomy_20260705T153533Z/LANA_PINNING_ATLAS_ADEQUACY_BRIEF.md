# Lana brief — pinning atlas top-20 adequacy review

Marker: `LANA_PINNING_ATLAS_ADEQUACY_20260705T153533Z`

Read first:

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/overnight_autonomy_20260705T153533Z/HWAO_OVERNIGHT_DIRECTION.md`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/pinning_backlog_prioritized.md`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/pinning_backlog_prioritized.json`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/evidence_source_inventory.json`

Task: high-reasoning adequacy review of the top ~20 prioritized claim↔source pairs.

Scope:

- read the local atlas artifacts;
- inspect local full-text files only when the inventory says local full text is present;
- use claim text + source metadata/snippet fields in the inventory for missing-fulltext rows;
- write only `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/LANA_ADEQUACY_TOP20.md`.

Review requested:

1. For the top 20 backlog rows, classify each as one of:
   - `READY_FOR_PINNING_REVIEW` (local text present and likely enough to pin, based on metadata/row shape),
   - `NEEDS_FULL_TEXT_FETCH` (no local full text; do not fetch now),
   - `WORDING_CONTRACT_RISK` (claim wording may be overbroad or needs caveat before pinning),
   - `ALREADY_PINNED_OR_LOW_PRIORITY`.
2. Identify the first 5 rows/sources that should become tomorrow's human-readable pinning packet.
3. Identify any science/wording risks that should become a disposition/wording packet instead of a silent pin.
4. Preserve the distinction between absence of local full text and source inadequacy. Do not judge a source unsupported solely because the full text is missing overnight.

Hard excludes:

No DB queries/writes, no full-text fetching/downloading, no SQL/apply/rollback files, no writes outside the one report, no prose/wiki/page_versions publish, no git, no deploy/restart, no secrets/account/billing/GCP/API/provider changes, no unattended Gemini web/app.

Report format:

- Verdict: PASS_WITH_QUEUE or BLOCKED.
- Top-20 table with classification/reason.
- First 5 recommended pinning targets.
- Science/wording risk list.
- Safety ledger: DB writes 0; SQL/apply 0; prose/wiki 0; git/deploy/restart 0.
- Standalone final marker line: `LANA_PINNING_ATLAS_ADEQUACY_20260705T153533Z`.
