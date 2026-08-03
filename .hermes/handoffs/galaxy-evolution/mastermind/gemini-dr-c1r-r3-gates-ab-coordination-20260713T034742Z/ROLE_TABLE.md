# Gates A+B role table

Authority: `HWAO_PARALLEL_PLAN.md`

| Lane | Gate A | Gate B | Write boundaries |
|---|---|---|---|
| Hwao | A-P1 RED-pin countersign, final review | B-P5 sample countersign, synthesis | coordination packet and named review files only |
| Lana | A-P1 RED pin; A-P5 conformance | B-P3 verdicts | Gate A `design/` + named receipts; Gate B `verification/` + named receipts |
| Goru | A-P2 test authoring | B-P2 mechanical span notes | Gate A `tests/`/`fixtures/`; Gate B `mechanical/` |
| Kun | both P0 custody; A test execution/green audit; B ledger/network audit | same | each packet `receipts/` only |
| Tori | A-P3 implementation/integration | B-P1 GET-only retrieval/custody | Gate A code/readjudication roots; Gate B `sources/`; receipts in both |

No lane may write to sealed/repair/r3 packets. Gate C is unapproved.

ROLE_TABLE_GATES_AB_20260713T034742Z
