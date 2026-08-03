# LANA BRIEF — 2929 disposition route recommendations + 2931 survivor check — 20260706T002104Z

Coordinator: Hwao/Fable. Tori is relay/verifier. Scope: read-only source/artifact review plus this one report write.

Inputs:
- Disposition spec: `docs/hwao_overnight_db_packet_prep_20260705T1615Z/EVIDENCE_DISPOSITION_2929_PARENT_REPLACED_SPEC.md`
- Dedupe spec: `docs/hwao_overnight_db_packet_prep_20260705T1615Z/DEDUPE_1308_5224v1_TRIPLICATE_SPEC.md`
- Wave2 adequacy: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/LANA_WAVE2_ADEQUACY.md`
- Wave2 pin ledger: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/PINS_WAVE2.jsonl`
- Fetched source text now available for 2604.15438: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/source_text/2604.15438_pdf_text.txt`

2929 rows needing recommendation (from spec):
- 28110 — 0901.1880 — no votes
- 28114, 28118 — 1203.2926v2 — no votes — duplicate group x2
- 28082 — 1507.06366v1 — no votes
- 28133 — 2009.11175v1 — no votes
- 28127, 28139, 28143 — 2403.17145v1 — no votes — duplicate group x3
- 28070 — 2512.05584v2 — no votes
- 28076, 28080, 28083, 28084 — 2512.21927v1 — no votes — Perseus-Arm superbubble group x4; topical fit to z~2 AGN quenching is doubtful
- 28060 — 2604.15438 — one community vote — strongest candidate move to successor 2942 if source text supports the narrower successor wording

Task:
1. Write `docs/hwao_overnight_db_packet_prep_20260705T1615Z/LANA_DISPOSITION_ROUTE_RECS.md`.
2. For each of the 14 rows, recommend one route: `S_move_to_successor`, `R_retire_with_audit`, or `H_hold_historical_marker`, with successor claim id if S, and a short reason.
3. Specifically confirm or reject `28060 -> 2942` using the fetched `2604.15438` text.
4. Specifically give a relevance verdict for the `2512.21927v1` Perseus-Arm x4 group using available artifacts/metadata only. Do not fetch new text; if availability is insufficient, say `H_hold_pending_source_check` rather than inventing.
5. Confirm 2931 dedupe survivor: compare wave2 ledger/use of evidence 28099 with 28154/28161 as represented in `WAVE2_TARGETS.json`/spec. Say whether 28099 is acceptable survivor for future dedupe, and whether merge-notes vs keep-one needs later review.
6. State DB ripeness: disposition packet is recommendations only / not executable; dedupe can proceed only to exact packet prep after Kun boundary + survivor confirmation; execution requires exact `APPROVE EXECUTE <packet_id>` later.

Locks: no DB writes; no SQL/apply/rollback generation; no product/wiki/prose publish; no deploy/restart; no git write; no extra fetching.

Required marker: `LANA_DISPOSITION_ROUTE_RECS_20260706T002104Z`
