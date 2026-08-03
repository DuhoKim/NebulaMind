# LANA BRIEF — wave2 pin adequacy gate — 20260705T1615Z

Coordinator: Hwao. Tori relays/verifies.

Read these inputs:
- Hwao direction: `.hermes/handoffs/overnight_autonomy_20260705T1615Z/HWAO_CONTINUE_OVERNIGHT_DIRECTION.md`
- Run dir: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/`
- Target rows: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/WAVE2_TARGETS.md` and `.json`
- Fetch manifest/log: `FETCH_MANIFEST.json`, `FETCH_LOG.md`
- Source text files in `docs/hwao_overnight_pinning_wave2_20260705T1615Z/source_text/`

Task:
Produce the adequacy gate report for every wave-2 target before Goru writes any pin ledger row.
Targets:
1. claim 2931 evidence 28099/28154/28161 -> `1308.5224v1` (local text copied from prior packet)
2. claim 2931 evidence 28132 -> `2605.31052v1` (local text copied from prior packet)
3. claim 2572 evidence 26088 -> `2512.16290v1` (fetched this run)
4. claim 2942 evidence 28155 -> `2604.15438` (fetched this run)
5. claim 2573 evidence 26089 -> `2401.12953` (fetched this run)

For each target, decide: `ADEQUACY_PASS`, `PASS_WITH_LIMITATION`, or `HOLD_NO_PIN`.
Include exact quote candidates where possible, but do not invent offsets if you did not compute them; Goru/Kun will handle offset verification.
Binding constraints:
- 2931 evidence stance is `none`; if passed, role must remain `neutral_context` and must never become `support`.
- 2929 `parent_replaced` rows are out of this pin ledger and routed to DB spec prep only.
- Fetched-source targets are allowed only because Tori fetched exactly three public arXiv sources and extracted text; no more fetches.
- If the quote does not actually support/refute/contextualize the claim wording, mark `HOLD_NO_PIN` and explain the safe next packet.

Scope:
- Read-only analysis and exactly one report write: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/LANA_WAVE2_ADEQUACY.md`.
- No DB, no SQL/apply/rollback, no prose/wiki/page_versions publish, no git, no deploy/restart, no extra fetches, no secrets.

Required marker:
`LANA_WAVE2_ADEQUACY_20260705T1615Z`
