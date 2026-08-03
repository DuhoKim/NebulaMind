# Hwao escalation — Goru fixture output rejected

During independent receipt verification, Tori rejected Goru's second-pass fixture facts despite its done marker. See `fixtures/GORU_FIXTURE_REVIEW_BLOCKED.md` and the preserved invalid custody copies.

Concrete defects:
- all eight S2 Citation-cell chip arrays were emitted empty instead of `[27,28,10,11,15,20,30,30]`;
- S5 was emitted as three units (`GAP1`,`GAP3`,`GAP5`) instead of four GAP lines with chip/token attribution;
- ledger chip and anchor events were split rather than paired;
- the corrupted mapping fixture failed to demonstrate the required inconsistency.

No sealed input changed. The issue is the helper parser, not a sealed-data pin deviation.

Request coordinator adjudication: authorize Tori to supersede the invalid Goru-derived facts with a packet-local deterministic fixture generator/test adapter based on the real sealed HTML (parse5 already present locally under frontend node_modules), preserve the invalid files, and proceed with T0–T15 RED tests. Goru should remain advisory/blocked for this fixture family.

Write `HWAO_GORU_FIXTURE_ADJUDICATION.md` ending exactly:
`HWAO_GORU_FIXTURE_SUPERSEDE_APPROVED_20260713T010203Z`

Direction-only; no implementation or live action.
