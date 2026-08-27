# §6 R12 REFEREE REPORT — GPT56

Subject: `SECTION6_DRAFT_AGY_R12.md`
Brief: `BRIEF_SECTION6_REVIEW_R12.md`

## Verdict

No blocking finding. R12 seats the protocol-deviation check in Row J before Stage-C execution and BS-5f issuance, binds the successful verification into BS-5f, exhausts the lawful Stage-C PASS/FAIL partition, and leaves no Stage-C FAIL branch in post-unblinding Row P. The remainder is genuinely the expressly blocked BS-2a mechanism: BS-2a remains REFUSED/UNFILLED, Rows C2 and E cannot run, BS-6 and the first image byte remain blocked, and Findings 1, 2, 2b, and 3 remain unresolved.

## Digest verification — performed before opening the subject

- Pinned digest read from `runner_s6r12_round.log`: `6339d940842fecad772034eb942600444afbf495a6da392aff6dec5e21d79dd7`.
- Independently computed SHA-256 of `SECTION6_DRAFT_AGY_R12.md`: `6339d940842fecad772034eb942600444afbf495a6da392aff6dec5e21d79dd7`.
- Result: **MATCH**. The bytes refereed are the pinned bytes.

## Numbered findings

None.

## Clause 10 audit in both directions

I treated ordinary emissions/refusals, named run-level outcomes, and VOID conditions as distinct consequences and checked both (i) every branch has one consequence and (ii) every stated consequence has a structural witness. Downstream success-path reachability is necessarily conditional on a future accepted BS-2a; the current REFUSED/UNFILLED BS-2a intentionally blocks C2, E, BS-6, and all later execution and is not counted as an orphan.

| Row | Forward termination check | Reverse reachability check | Result |
|---|---|---|---|
| A | Conforming provisioning emits BS-2k; each listed forbidden custody/read condition voids. | Provisioning witnesses BS-2k; each listed breach can witness VOID. | Complete |
| B | Authorized touches append one event; premature D touch is refused and logged; delivery/logging failures void. | Authorized touch, refused premature D touch, and listed mediator breaches witness each stated consequence. | Complete |
| C | Authorized production emits the sealed completion receipt; export/view breaches void. | Production and each forbidden export/view supply witnesses. | Complete |
| C2 | Once a replacement BS-2a exists, conforming verification emits projections plus exact-parent completion; classifier/schema/attestation breaches void. | The current BS-2a refusal blocks execution by design; each post-repair emission/breach remains structurally reachable. | Complete, blocked |
| D | Authenticated post-C2 inference emits sealed measurements; external χ emission voids. | Normal and breach witnesses exist, conditional on C2. | Complete, blocked |
| E | Complete projection set yields ledger plus realised partition; out-of-schema reads void. | Both branches are structurally reachable, conditional on replacement BS-2a and completed inference. | Complete, blocked |
| F | Conforming inputs yield sealed boundaries/allocation; χ-bearing input voids. | Normal and breach witnesses exist. | Complete |
| G | Allocated-sample interface use yields member co-signatures; role/view/export/log violations void. | Normal committee use and every listed violation witness the stated consequences. | Complete |
| H | Conforming ingestion yields the sealed label-set receipt; alternate persistence/schema/export paths void. | Normal and breach witnesses exist. | Complete |
| I | Missing/non-finite allocated output fails and halts before BS-8f; otherwise computation emits BS-8f; failure to halt or forbidden output/schema behavior voids. | Missing/non-finite and complete-finite samples witness the two ordinary branches; listed violations witness VOID. | Complete |
| J | Protocol/count/digest deviation terminates VOID before execution/BS-5f; any lawful locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts; only PASS emits BS-5f and proceeds toward BS-L. | A protocol deviation witnesses VOID; `<962` or self-verification failure witnesses `INCONCLUSIVE-BY-POWER`; a clean result with `succ >= 962` witnesses PASS/BS-5f. No consequence is orphaned. | Complete |
| K | Proper custody has no emission; any pre-unblinding holder read voids. | No-touch custody and a forbidden read witness the two states. | Complete |
| L | Authorized freeze/lock/opening signatures emit their stated artifacts; early access/opening or wrong-body signature voids. | Each ceremony step and each listed breach has a witness. | Complete |
| M | Authorized non-χ receipt work emits assigned slot receipts; pre-unblinding χ access voids. | Normal and breach witnesses exist. | Complete |
| N | Conforming ceremony emits BS-L; incomplete/unsigned/mis-signed lock voids. | Conforming and malformed ceremonies witness both consequences. | Complete |
| O | Passing lock plus canonical one-use authorization emits the unblinding receipt; early/replayed/out-of-destination operation voids. | Authorized opening and each listed breach witness the consequences. | Complete |
| P | Exact-parent precedence assigns every attempt exactly one state; missing/duplicate/orphan/malformed cases refuse under their named `INCONCLUSIVE-BY-*` outcomes; absence/non-finite/low-confidence are terminal per-attempt exclusions and any resulting removal deterministically yields `INCONCLUSIVE-BY-CALIBRATION`; no-removal then branches on the fixed `a_LB_b < 0.85` test; the complementary adequate branch emits the adequacy receipt, then BS-7f and BS-V. A Stage-C FAIL is not reintroduced. | Each record-state label is constructible; any removal witnesses calibration inconclusiveness; a no-removal low-accuracy case witnesses the second calibration branch; a no-removal adequate case witnesses the verdict path. Silent loss/retry/pre-unblinding execution witness VOID. | Complete |
| Q | Metadata-only checking emits the seal-state receipt; content read voids. | Normal metadata check and forbidden content read witness both. | Complete |
| R | Any otherwise-unlisted pre-unblinding χ access voids; no access has no emission. | The default breach supplies the VOID witness. | Complete |
| S | BS-V-authorized P9 export yields publication; earlier export voids. | Authorized and premature exports witness both outcomes. | Complete |

### Stage-C partition re-derived from the source

I read `../ref/successor_ref_v9.py` lines 1275–1276 directly:

- if `refuted or nonconservative`, the function returns `passed=False` regardless of the success count;
- otherwise line 1277 returns `succ >= CP_PASS_X` when `n_trials == N_TRIALS`.

Lines 77–78 set `N_TRIALS = 1_000` and `CP_PASS_X = 962`. Because Row J first requires exactly 1,000 trials and the frozen implementation/protocol digest, the lawful result space is exhausted by:

1. `refuted` or `nonconservative` → FAIL;
2. neither self-verification defect and `succ < 962` → FAIL;
3. neither self-verification defect and `succ >= 962` → PASS.

The separate pre-run deviation branch handles a count/digest mismatch as VOID. Thus FAIL and VOID neither overlap nor leave a gap, and PASS is the sole route to BS-5f → BS-L → unblinding. Row P correctly binds the already-verified PASS and does not branch on an unreachable FAIL.

## Row J seating and binding

Row J says the runner **must verify** exactly `N_TRIALS = 1_000` and the frozen Stage-C implementation/protocol digest **before running or issuing BS-5f**. The same sentence says BS-5f binds that verification. The VOID column names any trial-protocol or frozen-implementation deviation. This is an executable ordering constraint at Row J, not a post-BS-5f description.

## Whole-document consistency and numeric sweep

- `N_TRIALS = 1_000`: source line 77; R12 uses 1,000 consistently in Row J, Part 3 C2, and Part 5 item 17.
- `CP_PASS_X = 962`: source line 78; R12 consistently uses `<962` as FAIL and the complementary `>=962` as PASS.
- Self-verification fail-close: source lines 1275–1276; Row J, Part 3 C2, and Part 5 item 17 all include both `refuted` and `nonconservative`.
- Calibration floor `0.85`: source line 81 and V15 lines 566–567; Row P, Part 2 item 4, and Part 3 C2 agree.
- Archive count `208,405`: V15 lines 35–36 and 546–547; R12's scope and §6.2 agree.
- Part 5 items 8 and 16 now describe the actual Row J mechanism: ordinary Stage-C PASS/FAIL is pre-unblinding, deviations are VOID before an acceptable BS-5f, and Row P inherits PASS rather than rerunning or reconsidering Stage C.

## Testimony

- Part 5 item 16's parenthetical — “The frozen code at lines 1275-1276 admits no lawful state where the count differs without a breach” — is supportable only as a statement about **Row J plus the code**, not about lines 1275–1276 alone. The function accepts an `n_trials` argument and line 1277 handles a nonstandard count by returning `None`; Row J is what makes such a count a protocol breach before execution. This is a non-blocking attribution imprecision because the normative Row J rule is explicit and correctly ordered.

## Evidence ledger

Content read:

- `BRIEF_SECTION6_REVIEW_R12.md`
- `runner_s6r12_round.log`
- `SECTION6_DRAFT_AGY_R12.md`
- `../ref/successor_ref_v9.py` lines 70–85, 1210–1279, including direct inspection of 1275–1276
- `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` lines 564–575 and the located `208,405` passages
- R11→R12 unified diff, used only to verify the R12 repair surface against the current R12 brief

Commands/checks executed:

- `shasum -a 256 SECTION6_DRAFT_AGY_R12.md` — matched the pinned digest.
- Numeric-token occurrence sweep over R12 — no competing value for 1,000, 962, 0.85, or 208,405 found.
- R11→R12 diff — confirmed the Row J repair and Part 3/Part 5 conforming edits.

Deliberately not inspected or performed:

- `/Users/duhokim/NebulaMindData/` was not read.
- No network fetch was made.
- No source, preregistration draft, code, gate, or process was modified; only this required report was written.

**CLEAR**