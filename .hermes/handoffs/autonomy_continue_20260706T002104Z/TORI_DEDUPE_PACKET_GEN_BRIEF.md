# TORI BRIEF — gated dedupe exact packet generation — 20260706T002104Z

Do not start until BOTH prerequisites are verified from files:
1. `docs/hwao_overnight_pinning_wave2_20260705T1615Z/KUN_WAVE2_BOUNDARY.md` contains `KUN_WAVE2_BOUNDARY_CLOSED_20260706T002104Z` and checker PASS.
2. `docs/hwao_overnight_db_packet_prep_20260705T1615Z/LANA_DISPOSITION_ROUTE_RECS.md` contains `LANA_DISPOSITION_ROUTE_RECS_20260706T002104Z` and explicitly confirms evidence 28099 as acceptable survivor for the 1308.5224v1/claim2931 dedupe.

If both pass, prepare ONE exact dedupe packet only from `docs/hwao_overnight_db_packet_prep_20260705T1615Z/DEDUPE_1308_5224v1_TRIPLICATE_SPEC.md`.

Packet dir pattern: `docs/galaxy_2931_dedupe_exact_packet_<YYYYMMDDTHHMMSSZ>/`

Required packet contents: backup JSON, exact diff JSON/CSV/Markdown, guarded apply script or SQL stored but NOT executed, rollback script/SQL stored but NOT executed, validator/checksum manifest, pre/post/rollback verification queries, drift guards for rows 28099/28154/28161, vote/dependency checks, pin cross-check that survivor is 28099, and a local-only packet id/approval phrase. Keep packet id and phrase out of public cockpit surfaces unless the user explicitly asks.

Status must be `AWAITING_EXPLICIT_EXECUTION_APPROVAL` / `PREPARED_NOT_EXECUTED`. Marker: `DEDUPE_PACKET_PREPARED_NOT_APPROVED_<ts>`.

Hard stops: no DB writes; no SQL/apply/rollback execution; no migrations; no trust recompute; no prose/wiki/page_versions publish; no deploy/restart/service/config; no git commit/push/merge/rebase/reset/cleanup.
