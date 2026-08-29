# V46 whole-document referee — GPT56

## Verdict

**NOT CLEAR.** The dispatched V46 bytes match the required SHA-256. The V43 same-run rerun deletion is complete, `KIMI-V11 F7` is the correct Stage-P citation, the class inventory is 16/8, the three misconduct conditions remain at `Any`, and the BS-3g slot is honestly still not receiptable. But V46 has not established the replacement route on which deleting `INCONCLUSIVE-BY-COMPUTATION` depends. The §0-pinned Stage-C implementation propagates numerical exceptions instead of converting them to `INCONCLUSIVE-BY-POWER`, and §11 names no conversion/fixture that would make the new claim executable. The separate closed-enumeration proof also cites the wrong §2.7 reason for per-object non-finiteness and erases the document's actual Row-I/Row-P split.

## Findings

### 1. HIGH / REPAIR-REQUIRED — the claimed POWER route for pre-unblinding Stage-C numerical failures does not exist in the normative code or the code-side inventory

**Sections / lines.** §0 lines 72–100; §5 lines 492–494; §6.1 Row J line 566; §11 lines 912–925; `ref/successor_ref_v9.py` lines 1138–1155, 1158–1190, and 1218–1277.

V46's central repair says every Stage-C numerical failure is already terminated by `INCONCLUSIVE-BY-POWER`, making the deleted computation outcome a second claimant on a closed route. Row J's prose says any locked Stage-C FAIL emits POWER. The code bytes that §0 makes normative do not implement that conversion. `stage_power()` directly calls `reference_null_z()`, `calibrated_p()`, and `perm_record()` with no exception-to-outcome wrapper. Those functions explicitly raise on zero/non-finite denominators, degenerate signs, non-finite permutation values, malformed accuracy, and related failures. `stage_power()` returns `(successes, False, audit)` only for the two ordinary fail-closed cases at lines 1275–1277; a numerical exception propagates and emits no run outcome. No §0-pinned Row-J producer catches it, and the production runner merely consumes a caller-supplied BS-5f receipt.

Section 11 does not repair that executable gap. It requires the calibration guard and aggregate validator, but after deleting the COMPUTATION producer item it contains no Stage-C exception conversion, authenticated outcome schema, or negative fixture proving that a numerical exception becomes POWER. A future atomic revision can implement every §11 item while leaving this branch outcome-less. Row R's default-forbidden clause restricts which processes may touch χ-bearing objects; it cannot prove that an allowed function catches every exception. Thus the option-C route is still an assertion contradicted by the normative bytes, and clause 10's exactly-one-outcome promise is not met for the named failure class.

Smallest sufficient repair: either add and preregister an explicit exception-to-POWER conversion around the pinned Stage-C runner, with authenticated emission and fixtures for each numerical failure class, or retain a separately named numerical halt with an executable producer. Whichever route is chosen must be present in the §0-defined code plan; a closed actor table cannot substitute for control-flow implementation.

### 2. MEDIUM / REPAIR-REQUIRED — the closed-enumeration proof sends Row-D non-finiteness to a §2.7 reason that means catalogue quality, not instrument non-finiteness

**Sections / lines.** §2.7 lines 342–345 and 365–388; §5 lines 491–494; §6.1 Rows E, I, and P lines 561, 565, and 572; §7.1 line 746.

Section 5 says a per-object non-finite instrument output falls through “§2.7's exclusion reason (c)” and uses that as a premise of the exhaustive closed-row argument. Reason (c) is **catalogue quality**. The same §2.7 sentence explicitly says instrument absence/non-finiteness is deferred to post-unblinding handling, and Row E expressly excludes instrument absence/non-finiteness from the pre-lock structural exclusion. The actual contract is split: Row I detects missing/non-finite output only for an allocated hand-check object and emits the third pre-statistic code `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`; otherwise Row P classifies non-finiteness post-unblinding as `EXCLUDED-BY-NONFINITE`, after which any removal emits CALIBRATION.

The mistaken citation is not harmless shorthand. It is one of the three premises offered to prove that no numerical locus remains outside POWER/CALIBRATION, while §7.1 line 746 repeats a two-code exhaustive summary that omits the named Row-I code. The document's real routes can remain single-valued, but V46's argument for their closure is factually false against its own bytes. Re-derive the paragraph from the actual phase split: catalogue-quality exclusion at E, allocated-output failure at I, deferred nonallocated adequacy at P, and Stage-C handling at J. Do not call any of those §2.7(c) instrument-nonfinite handling.

## Targeted attacks that held

- **Subject identity held.** SHA-256 was recomputed before the draft was read: `c5afba31f909dcda1fc573a396f884e48bb4880ac6adb119421c3e335e7a8ca3`, exact match.
- **V43 rerun deletion held.** Searches found no surviving same-run Stage-C retry permission, seed schedule, computation-attempt log, attempt cap, or re-execution allowance. Remaining rerun/retry language concerns Stage P, BS-2a design, fixtures, Branch A, historical explanation, or Row-P measurement attempts; Row P explicitly forbids discretionary retry and Stage-C rerun.
- **Deleted-token sweep held subject to F1/F2.** The exact token `INCONCLUSIVE-BY-COMPUTATION` appears only in §5's deletion record and §7.1's historical explanation. No operative clause routes to it and §11's producer item is gone.
- **V42 citation correction held.** `gates/PREREG_TEXT_V11_KIMI.md` F7 states that the exact-null Stage P is not implemented in the file §0 pins and verifies the v7/v9 subject seam. KIMI F4 is the access/custody finding.
- **BS-3g status held.** Section 6.1 includes BS-3g in the exhaustive non-χ-bearing slot-receipt list, while §11 explicitly says no `SLOT_SCHEMA` entry, producer, or independent verifier yet exists. `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` confirms that the joint path is settled, ships no mapping, and refuses without one. The slot remains DESIGN/UNFILLED and blocks BS-6; the edge is not falsely claimed receiptable.
- **Misconduct phases held.** Forbidden acts, protocol deviation, and digest deviation remain `Any` in §5 and registry rows `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION`. Only numerical non-finite/degenerate VOID antecedents are post-unblinding.
- **Inventory held.** `prereg_counts.py` independently returns 16 class-P and 8 class-E rows with prose matched. The sole 15/8 occurrence is the historical V36→V37 transition.
- **Named checker posture held.** Trace: 45 transitions, 0 problems; trace self-test: 3 scope rules, 0 failures. VOID registry: 54 antecedents, 20 row names, digest `a4d1d745b2ed33bc0e01dd39b845f88daffdc542d2bdd98d5e122ab7dd443d37`; self-test: 6 controls, 0 failures. Lint exits 0 with 96 legacy advisories and 0 blocking findings; lint self-test: 8 controls, 0 failures. The 96 option-D legacy advisories are not findings.
- **Pinned-byte spot checks held.** Live SHA-256 values match the draft for `successor_ref_v9.py`, `closure_worker_v9.py`, `gain_gradient_estimator.py`, and `verify_mu_gamma.py`.

## Evidence ledger and custody

Read as content: `gates/BRIEF_V46_REVIEW.md` first; all 925 lines of V46 only after digest verification; the exact V45→V46 diff; both V43 and V44 whole-review reports; `gates/PREREG_TEXT_V11_KIMI.md`; `gates/FINDINGS_MAP.md`; `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`; and the relevant mask, permutation, Stage-C, and production-runner regions of `ref/successor_ref_v9.py`. A concurrently present CODEX V46 report was not read and did not bind this seat.

Executed read-only: subject and pinned-file SHA-256 checks; exact V45→V46 byte diff; targeted searches over deleted-outcome, rerun/retry/attempt, class-count, outcome-route, universal-negative, and VOID-phase language; `prereg_counts.py`; `prereg_trace.py --check` and self-test; `void_registry.py` normal and self-test; `prereg_lint.py` normal and self-test; and scoped repository status.

I did not read image data, run inference, execute Stage P or Stage C, unblind, fill a slot, choose the gain mapping, alter frozen code, modify the draft, or intentionally modify any file outside this report. Pre-existing repository state and the concurrently produced CODEX report were left untouched.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V46
VERDICT: NOT CLEAR
COUNT: 2
F1 | HIGH | REPAIR-REQUIRED | §0 lines 72–100; §5 lines 492–494; §6.1 Row J line 566; §11 lines 912–925 | The normative Stage-C code propagates numerical exceptions and §11 names no conversion, so the claimed existing POWER route that justifies deleting COMPUTATION is not executable.
F2 | MEDIUM | REPAIR-REQUIRED | §2.7 lines 342–345; §5 lines 491–494; §6.1 Rows E/I/P lines 561/565/572; §7.1 line 746 | The closure proof mislabels catalogue-quality reason (c) as instrument-nonfinite handling and omits the actual Row-I/Row-P phase split.
<!-- END FINDINGS-BLOCK -->