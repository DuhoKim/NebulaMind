# Role table — contract r3 + 73-entry manual triage

Authority: `HWAO_PLAN.md`

| Lane | Current phase | Deliverables | Write boundary |
|---|---|---|---|
| Hwao | coordinator | plan, r3 countersign, disagreement rulings, final recommendation, final marker | packet root, `markers/` |
| Lana | P0 ACK, then P1a/P2 after P0 opens | D1–D6 r3 draft and complete classification ledger | `design/`, `triage/TRIAGE_LEDGER.*` |
| Goru | P0 ACK, then P1b after P0 opens | verbatim mechanical extraction of 73 manual entries | `triage/GORU_*`, in-packet `_tmp_*` |
| Kun | P0 custody, then P3 arithmetic | input hashes/custody and independent ledger arithmetic | `receipts/KUN_*` |
| Tori | relay/integration | ACK, ≥15-entry spot verification, packet hygiene | `receipts/TORI_*` |

No lane may change the five pinned triage categories, touch source packets, retrieve sources, or cross any hard boundary in `HWAO_PLAN.md`.

TORI_ROLE_TABLE_CONTRACT_R3_TRIAGE_20260713T024458Z
