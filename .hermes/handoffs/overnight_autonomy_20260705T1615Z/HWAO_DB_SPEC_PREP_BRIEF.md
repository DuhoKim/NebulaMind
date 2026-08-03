# HWAO BRIEF — Track B spec-only DB packet prep — 20260705T1615Z

Coordinator: Hwao/Fable. Tori relays/verifies.

Read:
- Continuation direction: `.hermes/handoffs/overnight_autonomy_20260705T1615Z/HWAO_CONTINUE_OVERNIGHT_DIRECTION.md`
- Prep target list: `docs/hwao_overnight_db_packet_prep_20260705T1615Z/DB_PACKET_PREP_TARGETS.md` and `.json`
- Atlas result: `docs/hwao_overnight_pinning_atlas_20260705T153533Z/OVERNIGHT_RESULT.md`

Task:
Draft the two NOT-executable database-cleanup specs Hwao selected. These are specs only, not packets and not SQL.

Deliverables in `docs/hwao_overnight_db_packet_prep_20260705T1615Z/`:
1. `DEDUPE_1308_5224v1_TRIPLICATE_SPEC.md`
   - exact target rows from DB_PACKET_PREP_TARGETS
   - why this is a dedupe candidate
   - required before-state checks for a future packet
   - projected after-state choices to present to user (keep/relink/retire/no-op), without deciding beyond evidence
   - review questions for Lana/Goru/Kun
2. `EVIDENCE_DISPOSITION_2929_PARENT_REPLACED_SPEC.md`
   - exact 14 target rows from DB_PACKET_PREP_TARGETS
   - why parent_replaced evidence should not stay in pinning queue
   - possible disposition routes (move to successors / retire with audit note / hold), with dependency checks required
   - required before-state checks and drift guards for a future exact packet
3. `DB_PACKET_PREP_SUMMARY.md`
   - plain-English summary, explicit `DB writes: 0`, `SQL/apply artifacts: 0`, `NO ACTIVE EXECUTION PHRASE`
   - morning gate: future supervised packet generation and exact `APPROVE EXECUTE <packet_id>` phrase only after validators/checks/lane reviews pass.

Scope:
- Markdown specs only in the prep dir. No `.sql`, no apply/rollback scripts, no executable mutation artifacts.
- No DB writes, no trust recompute execution, no prose/wiki publish, no git/deploy/restart, no secrets.

Required marker in the summary:
`DB_PACKET_PREP_DRAFTS_READY_20260705T1615Z`
