# KUN BRIEF — wave2 reproducibility and boundary checker — 20260705T1615Z

Coordinator: Hwao. Tori relays/verifies.

Read:
- Hwao direction: `.hermes/handoffs/overnight_autonomy_20260705T1615Z/HWAO_CONTINUE_OVERNIGHT_DIRECTION.md`
- Lana gate: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/LANA_WAVE2_ADEQUACY.md`
- Goru final repaired ledger: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/PINS_WAVE2.jsonl`
- Goru final repaired counts: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/GORU_WAVE2_COUNTS.md`
- Tori independent validation: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/TORI_WAVE2_PIN_LEDGER_VALIDATION.json`
- DB spec-only prep dir: `docs/hwao_overnight_db_packet_prep_20260705T1615Z/`

Important context:
- Goru's initial ledger had invalid/truncated spans, then Goru repaired it. The invalid files are intentionally preserved as `.invalid_initial_goru` evidence; do not treat them as active pins.
- Active/final files are `PINS_WAVE2.jsonl` and `GORU_WAVE2_COUNTS.md`.

Task:
Create a deterministic checker and boundary report.

Deliverables:
1. `docs/hwao_overnight_pinning_wave2_20260705T1615Z/pinning_wave2_checker.py`
   - Parse `PINS_WAVE2.jsonl`.
   - Verify exactly 5 active pin rows with evidence IDs `[28099, 28132, 26088, 28155, 26089]`.
   - Verify no claim_id 2929.
   - Verify each source text sha256 matches.
   - Verify each quote exactly equals text[`char_start`:`char_end`] and is found in the source file.
   - Verify quote length >= 120 chars.
   - Verify required marker phrases per row:
     - 28099: `two-step quenching process`, `interplay between the inner structure`
     - 28132: `central role of BH growth`, `AGN feedback and environment`
     - 26088: `halo mass is the domi-`, `previous claims regarding the dominant role`
     - 28155: `Not all AGNs exhibit every component`, `regulate star formation`
     - 26089: `black hole mass to best predict quiescence`, `halo mass`
   - Sweep both new dirs for forbidden executable artifacts: `.sql`, `*apply*`, `*rollback*`, migrations. The `.invalid_initial_goru` backups are allowed and should not count as active pins.
   - Print JSON with status PASS/FAIL and errors.
2. Run the checker and save stdout to `CHECKER_RESULT.md` (include JSON block).
3. Write `KUN_WAVE2_BOUNDARY.md` with verdict, checker output, no-mutation boundary, invalid-initial-Goru caveat, and next safe handoff.

Scope:
- Read local files and write only the three deliverables above.
- No DB writes, no SQL/apply/rollback execution or creation, no prose/wiki/page_versions publish, no git commit/push/merge, no deploy/restart, no extra fetches, no secrets.

Required marker in boundary report:
`KUN_WAVE2_BOUNDARY_20260705T1615Z`
