# C1r repair lane table

Packet: `gemini-dr-c1r-chip-validator-repair-20260713T010203Z`
Coordinator: Hwao

| Lane | Role | Allowed writes | Required ACK | Completion marker |
|---|---|---|---|---|
| Lana | Contract/capture design review | `design/LANA_DESIGN_REVIEW.md`, `design/LANA_ACK`, `design/LANA_SIGNOFF` | `LANA_C1R_REPAIR_ACK_20260713T010203Z` | `LANA_C1R_REPAIR_DESIGN_DONE_20260713T010203Z` |
| Goru | Mechanical sealed-HTML fixture/count construction | `fixtures/`, `fixtures/GORU_ACK` | `GORU_C1R_REPAIR_ACK_20260713T010203Z` | `GORU_C1R_REPAIR_FIXTURES_DONE_20260713T010203Z` |
| Kun | Custody/reproducibility and test-runner gate | `receipts/`, `tests/run_all.sh`, `receipts/KUN_ACK` | `KUN_C1R_REPAIR_ACK_20260713T010203Z` | `KUN_C1R_REPAIR_PREFLIGHT_DONE_20260713T010203Z` |
| Tori | Bounded packet integration after lane receipts | remaining packet-local implementation/test/re-adjudication files | implicit relay ACK | packet completion marker after GREEN |

All lanes: local/offline only. No writes outside this packet. No edits to the sealed packet. No live Gemini/browser/network/DB/wiki/product/deploy/restart/git/cron/public cockpit action.

C1R_REPAIR_ROLE_TABLE_LOCKED_20260713T010203Z
