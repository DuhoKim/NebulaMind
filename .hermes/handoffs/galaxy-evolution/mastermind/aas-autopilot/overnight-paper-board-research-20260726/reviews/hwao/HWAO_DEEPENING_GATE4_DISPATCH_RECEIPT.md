# Hwao — Deepening Gate 4 Dispatch Receipt

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_DEEPENING_GATE4_DISPATCH_RECEIPT_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Authored by Hwao/Fable at Deepening Gate 4 (machine-authored coordination artifact; not human gold). No memory/config written this gate. No source / current-Lab / PDF-replacement / public / DB / wiki / git / cron / browser / account / deploy / PAYG byte changed.

## Inputs read this gate (read-only)
- `reviews/kun/KUN_C2_V2_AUDIT_RECEIPT.md` + `packets/C-candidate-build/kun-c2-v2-audit/C2_V2_CONTRACT_AUDIT.md` — nine-item **PASS**.
- `publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT.md` + `publication/goru-v2-new-run-map/NEW_RUN_TARGET_MAP.md` — self-reported `DONE`, **route-invalid**.
- `publication/TORI_C2_V2_ROUTE_VALIDATION.md` — `V2_AUDIT_PASS__GORU_NEW_RUN_MAP_FAIL_INVALID_ROUTE_ID`.
- `backend/app/routers/lab_runner.py` — route validators (`get_run` l.183, `get_artifact` l.196), `list_runs` visibility (l.157–161), `create_run` id convention (l.134).

## Final acceptance issued (`HWAO_C2_V2_FINAL_ACCEPTANCE.md`)
- **V2 candidate mechanics = FINAL-ACCEPTED** on Kun's independent nine-item PASS (hashes; V1→V2 diff limited to F1–F4 + header; rendered PDF strings with old overclaim + "reproducible" absent; references; split; caveats; figure byte-identity; compile rc=0; receipt concordance). V2 frozen (`bb77d38d`/`ac59ac60`/`ed83a825`); V1 + source frozen.
- **Publication remains BLOCKED:** Goru's first map used the invalid hyphenated id `gated-e2e-demo-c2-v2` (`rid.isalnum()` False → `400`); its `DONE` is not publish evidence. Corrected legal id **`c2v2e2e0726a`** (isalnum True, len 12, ABSENT — independently rechecked). First map + receipt preserved unchanged.

## Lane dispatched this gate (Tori will dispatch; Hwao does not self-start lanes)
1. **New-run mapping REPAIR — `publication/GORU_C2_V2_NEW_RUN_MAPPING_REPAIR_BRIEF.md`** (Goru, **Antigravity/Gemini**, READ-ONLY, create-only path).
   - Re-map against legal id `c2v2e2e0726a` grounded in `lab_runner.py` route validators + `list_runs` visibility; verify ABSENT `c2v2e2e0726a.json` + `c2v2e2e0726a/`; verify `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` is source-code-valid; record manifest requirements (top-level `id`/`status`/`created_utc`/`spec`; non-empty `result.summary`; `result.figure_url`/`result.pdf_url`; omit optional review fields unless backed by real artifacts); require the four visible labels in `result.summary`.
   - **Preserve the failed first map + receipt unchanged.** No live HTTP / browser / public / current-Lab / source writes; no `lab-runs` create.
   - Versioned write root `publication/goru-v2-new-run-map-v2/`; versioned receipt `publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT_V2.md`; marker `OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_V2_COMPLETE_V1`.

Active helper lanes: one (Goru mapping repair). The Kun V2 audit lane is complete.

## Preservation & public status
All writes this gate are NEW files under the approved output root (the final acceptance, the repair brief, this receipt) plus one empty versioned lane dir. All prior files preserved — V1 + V2 candidates frozen; the failed first Goru map + receipt preserved; no `lab-runs` artifact touched; the invalid hyphenated id was never created. **Public status: `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.** Promotion still requires the corrected route-valid mapping, then the exact publish packet + `APPROVE PUBLISH <packet_id>` — create-only to the new run id, never overwriting the baseline input.

## Status
This gate: **DONE** — V2 final acceptance (mechanics) + publication-blocked determination + route-repair mapping brief + this dispatch receipt written under the approved output root; markers/roots verified; V1, V2, source, the failed first map, and all prior files preserved. Handing to Tori for visible dispatch of the Goru mapping repair.

`OVERNIGHT_PAPER_BOARD_HWAO_DEEPENING_GATE4_DISPATCH_RECEIPT_V1`
