# Hwao brief — C1r chip-aware capture + validator repair

User approval: "go ahead with the next step"

Interpreted approved scope: execute the previously stated next safe step offline:
1. build chip-aware capture in a NEW repair packet;
2. add TDD fixtures for the real Gemini `source-footnote` DOM and known validator defects;
3. correct capture/validator behavior;
4. re-adjudicate the immutable sealed C1r artifacts offline;
5. produce receipts and a dashboard completion update.

Repair packet root:
`gemini-dr-c1r-chip-validator-repair-20260713T010203Z`

Authoritative read-only inputs:
- sealed packet `gemini-dr-revised-canary-20260712T045317Z`
- `runs/c1r/rendered_body.html`
- `runs/c1r/body.md`
- `runs/c1r/structured_capture.json`
- `runs/c1r/validator_result.json`
- `prompt/C1r.md`
- `validator/structured_capture.js`
- `validator/validator.py`
- `validator/tests/`
- root-cause reports in `dr-c1r-root-cause-20260712T163156Z`

Hard constraints:
- sealed packet remains byte-immutable; no edits under it;
- strict RED → GREEN → refactor;
- new code/tests/fixtures/results only under the new repair packet;
- use real sealed HTML as pinned fixture or byte-copy input, not a simplified anchor-only mock;
- no live Gemini/browser/computer-use/network/account/quota action;
- no DB/wiki/product writes, deploy/restart, git commit/push/merge, cron, public Baseline change, or external submission;
- no live retry or retro-acceptance;
- re-adjudication remains mechanical/offline and does not certify science/source fidelity.

Required workstreams for Hwao to direct:
- Lana: high-reasoning contract/capture design review, especially exact same-cell semantics and C6/C7 rules.
- Goru: mechanical DOM/source-index/URL-map fixtures and count assertions.
- Kun: reproducibility/test runner and immutable-input verification.
- Tori: relay, packet writer, test/receipt verifier, bounded integration only as Hwao directs.

Required repair behaviors:
1. Capture native `source-footnote` / `sup[data-turn-source-index]` per exact logical cell, bullet, and GAP unit.
2. Recover deterministic source-index→URL mapping from ledger chip+anchor pairs; fail closed on inconsistent or unresolved mappings.
3. Treat citation-only cells as non-empty when the chip resolves.
4. Avoid duplicate `li` + nested `p` logical blocks.
5. Split GAP lines into independent logical units.
6. Fix blank-line source locator behavior.
7. Separate section-order failures from empty-cell failures.
8. Require numerical/quoted fraction or incidence before four-qualifier enforcement.
9. Validate C4 on typed claim-bearing cells/units, including every Section-2 Result cell and Section-4 status cell.
10. Validate comparisons per logical cell/unit.
11. Enforce exact empty sentinels.
12. Enforce C7 orphan sources, duplicate rows, non-empty short names, and URL normalization variants.
13. Preserve manual review for semantic comparability, uncertainty, citation quality, and source fidelity.

Expected offline re-adjudication residue, to test rather than assume:
- 8 Section-2 Result-cell citation-locality failures;
- 6 unlabeled comparison failures;
- C7 failure for 12 orphan source indices, plus duplicate rows and blank short names;
- exact `NONE_FOUND.` token defect;
- semantic/source checks held for manual review;
- prior 41 capture failures, 3 fraction false positives, and `BAD_STRUCTURE` artifact removed.

Please write a concise implementation directive to:
`HWAO_IMPLEMENTATION_DIRECTION.md`
ending exactly:
`HWAO_C1R_CHIP_VALIDATOR_REPAIR_DIRECTION_DONE_20260713T010203Z`

It must specify lane assignments, file boundaries, RED tests in execution order, GREEN acceptance criteria, expected receipts/markers, dashboard checkpoint direction, and stop conditions. Do not edit implementation files yourself in this direction-only pass.
