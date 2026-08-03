# HWAO_IMPLEMENTATION_DIRECTION — C1r chip-aware capture + validator repair (TDD, offline)

Packet: `gemini-dr-c1r-chip-validator-repair-20260713T010203Z` · Direction-only pass: Hwao edits no implementation files. Approved scope per `HWAO_BRIEF.md`; all 13 required repair behaviors are covered by the tests below. Strict RED → GREEN → refactor. Everything offline; no live/network/browser/git/DB/deploy action anywhere in this packet.

## 1. File boundaries (hard)

- **All writes under this packet root only**, in: `capture/` (structured_capture_v2.js), `validator/` (validator_v2.py, contract_spec_v2.json), `fixtures/`, `tests/`, `readjudication/`, `receipts/`, `design/`, `markers/`, lane ACKs, temp as `_tmp_*` inside this root.
- Sealed packet `gemini-dr-revised-canary-20260712T045317Z` and `dr-c1r-root-cause-20260712T163156Z` are **byte-immutable, read-only**. Byte-copies INTO `fixtures/` are allowed and must be hash-recorded. v2 code starts as copies of the sealed `structured_capture.js` / `validator.py` — never edit the originals.
- The real sealed `rendered_body.html` (sha256 `78ed129c…2bbc`) is the primary fixture. No simplified anchor-only mocks may substitute for it in any RED test.

## 2. Lane assignments (quintet; ACK per role-table before work; Hwao coordinates only)

- **Lana — design review (high reasoning), `design/LANA_DESIGN_REVIEW.md`:** exact same-cell citation semantics (a resolved same-unit chip = checkable citation; Simulation cell and dedicated Citation cell NEVER satisfy other claim-bearing cells, C1r.md:86-92); C6 comparison definition per logical cell (agreement/tension claims about results — including "Explicitly emergent"-cell claims — require the token; calibration-target register in cell 1 alone does not); C7 rule set (bidirectionality over resolved chip indices ∪ inline text URLs, duplicate rows, non-empty short names, normalization incl. `abs|html|pdf` and `article` vs `article-abstract`); numeric-fraction gate for C6 qualifiers; the preserved manual-review list. Sign-off marker `design/LANA_SIGNOFF` required before the GREEN gate.
- **Goru — mechanical fixtures + count assertions, `fixtures/`:** byte-copy sealed inputs with `GORU_FIXTURE_MANIFEST.json` (paths + sha256); derive `EXPECTED_DOM_FACTS.json` from the sealed HTML: 108 chips total (S1 40, S2 8, S3 3, S4 9, S5 2, ledger 46); 46 anchors, all in ledger, 0 inside any `<td>`; 46 chip→URL pairs, 37 unique indices (1–37), 0 inconsistent; per-S2-row Citation-cell chip indices `[27,28,10,11,15,20,30,30]` with Result cells chip-free; li+p duplicate S3 blocks; 4 GAP lines in one `<p>` with chips on GAP1(30)/GAP3(36), tokens on GAP2/GAP4; heading order. Plus one deliberately corrupted copy (same index → two URLs) for the fail-closed mapping test. Marker `fixtures/GORU_FIXTURES_DONE`.
- **Kun — reproducibility + immutability, `receipts/KUN_IMMUTABLE_INPUT_RECEIPT.md`:** pre-flight and post-phase sha256 of every sealed input vs the RUN_RECEIPT custody values; test-runner harness (pytest + node) with full-output RED/GREEN receipts; determinism check (two runs, byte-identical outputs); write-scope audit (no file outside this packet changed). Kun owns the final GREEN gate.
- **Tori — relay, packet writer, bounded integration:** implements `capture/structured_capture_v2.js` and `validator/validator_v2.py` to Lana's design against Goru's RED tests; runs the re-adjudication; writes `receipts/TORI_PACKET_RECEIPT.md` (files, hashes, safety attestation). No integration beyond this packet; dashboard checkpoint only per §6.

## 3. RED tests in execution order (`tests/`; author all before any implementation; receipt `tests/RED_RECEIPT_20260713T010203Z.txt`, marker `C1R_REPAIR_TDD_RED_20260713T010203Z`)

Phase A — custody guard (runs first and after every phase):
- **T0** sealed-input hashes == RUN_RECEIPT custody values; mismatch ⇒ STOP (§7).

Phase B — capture (against `structured_capture_v2.js`; behaviors 1–6):
- **T1** chip extraction per exact logical unit: totals and per-region counts match `EXPECTED_DOM_FACTS.json`; every S1 cell, every S2 Citation cell, all 9 S4 status cells, S3 bullets, GAP1/GAP3 carry their chips with per-cell attribution.
- **T2** deterministic index→URL map from ledger chip+anchor pairs: 46 pairs / 37 unique / 0 inconsistent on the real HTML; on the corrupted fixture the capture FAILS CLOSED (explicit error/flag, no guessing).
- **T3** citation-only cells: S2 Citation cells are non-empty citation units when the chip resolves (resolved URL recorded); unresolved chip ⇒ fail-closed flag, not silent empty.
- **T4** li+p dedup: exactly 3 S3 bullet units, no paragraph twins.
- **T5** GAP split: 4 independent GAP units with correct chip/token attribution per line.
- **T6** blank-line locator: source-line mapping monotonic and correct for pinned blocks; blank lines do not desynchronize the cursor.

Phase C — validator units (against `validator_v2.py`; behaviors 7–13):
- **T7** order/empty decoupling: empty cells + perfect order ⇒ no `BAD_STRUCTURE`; scrambled order ⇒ `BAD_STRUCTURE` with named evidence (never "set()").
- **T8** numeric gate: "cluster gas fractions" (no value) ⇒ no `MISSING_QUALIFIER`; a quoted numeric fraction/incidence without the four-qualifier syntax ⇒ FAIL; with syntax ⇒ MANUAL.
- **T9** typed C4 units: every S2 Result cell and every S4 CALIBRATED/EMERGENT cell is claim-bearing by schema (no keyword or word-count guards); uncited+chip-free ⇒ FAIL; resolved same-cell chip ⇒ MANUAL(cited-review); Simulation/dedicated-Citation cells never cover others; bullets scanned; GAP absence-token satisfies the GAP citation rule.
- **T10** per-cell comparison scan: sealed EAGLE emergent-cell text ⇒ `UNLABELED_COMPARISON` anchored (row, cell 3); sealed calibration-target cell-1 text alone ⇒ no finding; GAP1 ⇒ finding; GAP2/4 ⇒ none.
- **T11** exact sentinels: `NONE_FOUND.` ⇒ format defect; `NONE_FOUND` ⇒ pass; S4 composite `NOT_REPORTED — NONE_FOUND` enforced.
- **T12** C7: on sealed data — 12 orphan indices {2,5,8,9,13,16,18,23,24,29,31,33}; 9 duplicate rows; 46 blank short names; `abs|html|pdf` unify; 14↔29 (`article` vs `article-abstract`) flagged as near-duplicate.
- **T13** manual preservation: semantic comparability, uncertainty, citation quality, source fidelity ⇒ `MANUAL_REVIEW_REQUIRED` only, never auto-PASS/FAIL.

Phase D — integration (the residue is TESTED, not assumed):
- **T14** full offline re-adjudication of the sealed C1r artifacts via v2 capture+validator. Expected deterministic set, pinned: 8 C4 S2 Result-cell failures (rows 15–22); 6 `UNLABELED_COMPARISON` (5 S1 emergent cells + GAP1); C7 failure covering 12 orphans + 9 duplicate rows + blank short names; the `NONE_FOUND.` sentinel defect; C1/C5/C8 still PASS; and **absence** of the 41 capture-caused findings, the 3 fraction false positives, and `BAD_STRUCTURE`. Any deviation ⇒ do not weaken the test — STOP per §7 and adjudicate.
- **T15** determinism: two full runs byte-identical.

## 4. GREEN acceptance criteria (Kun gates; receipt `tests/GREEN_RECEIPT_20260713T010203Z.txt`, marker `C1R_REPAIR_TDD_GREEN_20260713T010203Z`)

All T0–T15 pass with **no weakened assertion** (any expectation change needs a logged Lana+Hwao sign-off in the receipt); sealed hashes unchanged pre/post; write-scope audit clean; `design/LANA_SIGNOFF` present; determinism green. Refactor only after GREEN, behavior-frozen (suite stays green), then Kun re-runs everything.

## 5. Re-adjudication outputs and receipts

`readjudication/structured_capture_v2.json`, `readjudication/validator_result_v2.json`, and `readjudication/RESIDUE_REPORT.md` — final findings with evidence refs (file:line / block / cell), an explicit statement that the result is **mechanical only and does not certify science or source fidelity** (those stay in the manual queue), and no retro-acceptance language: C1r remains FAIL_CLOSED. Packet completion marker (last, after all receipts): `markers/C1R_CHIP_VALIDATOR_REPAIR_DONE_20260713T010203Z`.

## 6. Dashboard checkpoint (content-only, after §5 completes)

Tori updates the private tailnet dashboard only, same bounds as `HWAO_DASHBOARD_DIRECTION.md`: card 5 "Next safe work" → status **DONE — OFFLINE REPAIR COMPLETE**, detail one line: "chip-aware capture + validator green; sealed C1r re-adjudicated: 15 genuine mechanical findings + sentinel defect; science review still manual; no live run armed." Publish marker `GE_AUTOPILOT_C1R_REPAIR_20260713T010203Z_DONE`. Public Baseline cockpit untouched; no approval phrase; no deploy/restart beyond the established bounded renderer path.

## 7. Stop conditions (fail closed, escalate to Hwao/Duho with a partial receipt)

1. Any sealed-input hash mismatch at any phase. 2. Chip→URL inconsistency on the real sealed HTML. 3. T14 residue deviates from the pinned expectation (adjudicate; never silently edit the pin). 4. Any test appears to need network/browser/live Gemini/account/quota action. 5. Any write would land outside this packet. 6. GREEN unreachable without weakening a RED assertion. 7. Goru lane approaching 40% of the Antigravity 5h window. 8. No git commit/push/merge even on success — out of scope; Duho may request separately.

HWAO_C1R_CHIP_VALIDATOR_REPAIR_DIRECTION_DONE_20260713T010203Z
