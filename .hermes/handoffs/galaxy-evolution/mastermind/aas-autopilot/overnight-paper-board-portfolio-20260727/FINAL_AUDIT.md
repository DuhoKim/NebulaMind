# Final Independent Audit

Marker: `OVERNIGHT_PB_FINAL_AUDIT_PASS_WITH_FINDINGS_20260727`

## Result

`PASS_WITH_FINDINGS`

The approved P0/P1/P2 portfolio run completed with full receipt custody, independent source checks, cross-review, Hwao adjudication, and no public/source mutation before the dedicated publication step.

## Evidence matrix

| Gate | Result |
|---|---|
| Exact execution approval and publication target | PASS — one new public audit report only; no paper replacements |
| Hwao coordinator acceptance | PASS — `HWAO_PB_COORDINATOR_ACCEPTED_20260727` |
| Three primary lanes | PASS — P0 Lana, P1 Kun, P2 Goru markers present |
| Six no-self-review lanes | PASS — Kun/Goru for P0; Lana/Goru for P1; Kun/Lana for P2 |
| Hwao final roll-up | PASS — `HWAO_PB_FINAL_ROLLUP_COMPLETE_20260727` |
| Input manifests | PASS — all 11 lane/coordinator manifests; zero mismatches |
| Structured outputs | PASS — JSON/JSONL/CSV parse successfully |
| Frozen public identities | PASS — 12/12 conditions match; 11 byte-identical HTTP 200 artifacts plus the expected P0 review 404 |
| Protected local inputs | PASS — 26/26 hashes unchanged |
| Rendered representation | PASS_WITH_FINDINGS — P0 and P1 figures independently rendered; defects preserved rather than normalized |
| Stop files | PASS — absent through integration |
| Publication destination pre-existence | PASS — absent before preflight |
| Human validation | ZERO — automated review only |

## Decisive findings

1. P0: SFMS chain survives with caveats; matched-Te MZR consistency claim does not. Figure 2 visibly carries the unmatched −0.50 versus −0.25/factor-two state, while the abstract/conclusion assert a missing matched-scale analysis.
2. P1: all arithmetic reproduces, but source/estimand gates do not. The claimed observed cumulative density lacks an explicit primary-source cumulative row. The served page visibly contradicts itself (0.28 arrow versus 0.20 caption) and clips Table 1 references.
3. P2: `0 unsupported of 0 checked` is vacuous, not a citation pass. Positive enumerated passages are zero. Source identities need correction and the pair's lineage remains unproven.

## Validator correction

The first T1 validator resolved primary-lane manifest basenames relative to lane roots rather than lane `input/` directories, producing false missing-file rows. T2 tests lane/path, lane/input/path, then run-root/path; every manifest passes. The correction is recorded inside `VALIDATION_T2_FINAL.json`.

## Boundary ledger

- DB/wiki writes: 0
- Paper/PDF/card/Lab mutations: 0
- Cockpit changes: 0
- Service deploy/build/config/routing actions: 0
- Explicitly approved controlled frontend restarts: 1, after this audit passed and solely to activate the additive report
- Git commit/push/merge: 0
- Browser login/CAPTCHA/payment/OAuth/secret actions: 0
- Public writes before dedicated preflight: 0

Final audit author role: Tori receipt/custody verification; packet conclusions are Hwao's adjudications grounded in named lane receipts.

## Publication activation

The user separately approved one controlled launchd restart. The app, Lab, API, and clean report URL all returned HTTP 200 afterward. The standalone report was verified by direct HTTP, web extraction, browser structure, and visual rendering. No other deployment or mutation occurred.
