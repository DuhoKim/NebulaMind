# V46 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V46 bytes match the required SHA-256, and the specific V44 collision is genuinely removed: no live clause routes a branch to `INCONCLUSIVE-BY-COMPUTATION`. But V46's replacement claim—that the existing POWER/CALIBRATION routes exhaust every pre-unblinding numerical failure—is false against both the prose and the pinned code. Row F has explicit, reachable numerical FAIL branches (degenerate calibration bins and infeasible hand-check allocation) with no named lifecycle outcome, and the deletion rationale separately miscites catalogue-quality reason (c) as the route for a non-finite instrument output even though the document expressly defers that case to post-unblinding Row P.

## Subject identity and scope

- Required SHA-256: `c5afba31f909dcda1fc573a396f884e48bb4880ac6adb119421c3e335e7a8ca3`.
- Recomputed before reading the draft: `c5afba31f909dcda1fc573a396f884e48bb4880ac6adb119421c3e335e7a8ca3` — exact match.
- The exact V45→V46 diff removes the computation outcome and its §11 producer, rewrites the §5/§7.1 rationale, and adds the historical V44→V45 row. I treated the brief's assertion that this deletion is sound as a claim to attack, not as a ruling to inherit.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the closed-row argument does not close Row F's explicit numerical failure branches

V46 §5 lines 493–494 says every pre-unblinding numerical failure already terminates through POWER, CALIBRATION, or §2.7, and argues that Row R makes the lifecycle enumeration closed. Section 6.3(10), line 602, independently requires **every branch of every row** to terminate in one stated outcome.

That proof omits Row F. Row F at §6.1 line 562 performs calibration-bin sealing and hand-check allocation at P3, before unblinding. Section 6.3 lines 612–618 says `allocate_handcheck()` can find the inherited floors infeasible and “FAIL rather than shrink,” while `calibration_bins()` “refuses degenerate bins.” The normative pinned `ref/successor_ref_v9.py` confirms these are executable failure branches:

- `calibration_bins()` lines 1359–1369 raises `RuntimeError("degenerate calibration bins ... — FAIL")` when any bin is empty.
- `allocate_handcheck()` lines 1378–1442 raises `RuntimeError(... — FAIL)` for insufficient objects, floor demand above budget, budget above availability, exhausted headroom, allocation mismatch, and floor violations.

I exercised two controls directly against the pinned bytes with bytecode writes disabled. A constant nine-object position vector produced `RuntimeError: degenerate calibration bins [9, 0, 0] — FAIL`; a one-object live stratum produced `RuntimeError: stratum 0 needs 30 labels but only 1 objects exist — FAIL`.

No clause maps either Row-F failure to a named lifecycle outcome. They are not Stage-C or `N_eq` failures, so Row J's POWER outcome does not reach them. They are not BS-8f aggregate failures, so the §5 CALIBRATION clause does not reach them. They are not Row-I missing allocated outputs. Row R closes the set of **actors/processes that may touch χ-bearing objects**; it does not turn an unassigned branch inside named Row F into an outcome. Thus deletion of the redundant computation label may be correct for Row J, but V46's stronger completeness claim and Clause 10 are not correct for the whole pre-unblinding pipeline.

Smallest sufficient repair: assign every `calibration_bins()` and `allocate_handcheck()` failure to one explicit terminal run outcome (or prove and state that these are pre-run slot-fill refusals rather than run branches, with a phase/lifecycle boundary that prevents Row F from running inside a study run). Then extend the branch-termination inventory and fixtures to cover those paths. Do not rely on Row R as a substitute for branch enumeration.

### F2 — MEDIUM / REPAIR-REQUIRED — §5 falsely routes non-finite instrument output through catalogue-quality reason (c)

V46 §5 line 493 says “a per-object non-finite instrument output [routes] through §2.7's exclusion reason (c).” Section 2.7 lines 342–345 defines reason (c) as **catalogue quality** and immediately says instrument absence/non-finiteness and confidence exclusions are deferred to post-unblinding handling. Row E line 561 repeats that instrument absence/non-finiteness is excluded from the pre-lock structural exclusion. Row P line 572 supplies the actual route: post-unblinding `EXCLUDED-BY-NONFINITE`, followed by run-level `INCONCLUSIVE-BY-CALIBRATION` because any post-unblinding removal terminates the run.

The ultimate case is therefore assigned, but not at the cited reason or phase. This matters because line 493 uses the false §2.7(c) premise as evidence that the pre-unblinding numerical route was already complete. A post-unblinding adequacy consequence cannot establish that proposition.

Smallest sufficient repair: replace the §2.7(c) claim with the actual Row-P route and stop presenting it as evidence about pre-unblinding numerical-failure completeness. Catalogue-quality reason (c) must remain separate, as §2.7 and Clause 10 require.

## Targeted attacks that held

- **V44 computation collision:** held as a deletion. Full-text search found `INCONCLUSIVE-BY-COMPUTATION` only in the historical deletion record and the historical §7.1 explanation; no operative clause routes to it and §11 no longer orders a producer.
- **V43 rerun deletion:** held. No surviving same-run Stage-C rerun permission, seed schedule, computation-attempt log, verifier, or attempt cap exists. Remaining “rerun/retry” language concerns Branch A, Stage P, BS-2a design, historical execution, or Row-P measurement attempts; Row P says no discretionary retry and no Stage-C rerun.
- **V42 KIMI citation:** held. `gates/PREREG_TEXT_V11_KIMI.md` F7 is the Stage-P finding: the exact-null Stage P is absent from the §0-pinned implementation and its receipt actually names v7 bytes. KIMI F4 is the access/custody finding.
- **BS-3g posture:** held as honest unfinished work, not as current receiptability. Section 6.1 now includes BS-3g in the closed slot-receipt class, and §11 names the required `SLOT_SCHEMA` entry, producer, and independent verifier while explicitly admitting the edge is not yet receiptable and the slot remains DESIGN/UNFILLED. This is sufficient only because BS-6 remains blocked; it does not itself produce a conforming receipt.
- **Settled BS-3g semantics:** held. Both §7 and §11 now say the executable joint-counterfactual path is settled and only the γ-to-sign/calibration mapping remains open.
- **VOID misconduct scope:** held. Section 5 keeps forbidden acts and protocol/digest deviation at any phase; registry IDs `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION` all remain `Any`. Only numerical non-finite/degenerate VOID conditions are post-unblinding.
- **Class inventory:** held. `prereg_counts.py` reports 16 Class P / 8 Class E and says prose matches. No live inventory assumes 15/8.
- **Current-transition trace:** held. `prereg_trace.py --check` reports 45 computed transitions and 0 problems.
- **VOID checker:** held at its declared strength. `void_registry.py --self-test` reports 6 controls and 0 failures; as the draft admits, this establishes name coverage, not semantic branch coverage.
- **Lint posture:** held. `prereg_lint.py` exits 0 with exactly 96 `repair-citation-legacy` advisories and 0 blocking findings; per the brief, I do not report those permanent legacy advisories as unresolved.
- **Pinned-byte checks:** held. Live SHA-256 values match the draft for `successor_ref_v9.py` (`6a9abbbd…c148`), `closure_worker_v9.py` (`28f8e1f9…5959`), `gain_gradient_estimator.py` (`e2270297…27fd`), and `verify_mu_gamma.py` (`e33d9275…6d04`).

## Evidence ledger and limits

Read as content: `gates/BRIEF_V46_REVIEW.md` first; the complete 925-line V46 draft only after digest verification; the exact V45→V46 diff; `gates/V44_WHOLE_REVIEW_CODEX.md`; `gates/PREREG_TEXT_V11_KIMI.md`; and the relevant calibration/allocation code in `ref/successor_ref_v9.py`.

Executed: subject SHA-256 before reading and again before report write; exact V45→V46 diff; full-text searches for the deleted outcome, rerun/retry/attempt language, inventory counts, open/unresolved status, and calibration/non-finite branches; live hashes for the four pinned code/checker files; `prereg_counts.py`; `prereg_trace.py --check`; `void_registry.py --self-test`; `prereg_lint.py`; and two read-only Row-F failure controls with `PYTHONDONTWRITEBYTECODE=1`.

I did not read image data, run inference, execute Stage P or Stage C, unblind, fill a slot, choose the gain mapping, alter frozen code, modify the draft, or modify any file outside this report. The report path did not exist and scoped git status was clean immediately before this write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V46
VERDICT: NOT CLEAR
COUNT: 2
F1 | HIGH | REPAIR-REQUIRED | §5 lines 493–494; §6.1 Row F line 562; §6.3 lines 612–618 and Clause 10 line 602 | Row F's executable degenerate-bin and infeasible-allocation FAIL branches have no named outcome, so Row R does not prove pre-unblinding numerical-failure completeness.
F2 | MEDIUM | REPAIR-REQUIRED | §2.7 lines 342–345; §5 line 493; §6.1 Rows E/P lines 561/572 | Section 5 falsely routes non-finite instrument output through catalogue-quality reason (c); the document actually defers it to post-unblinding Row P and CALIBRATION.
<!-- END FINDINGS-BLOCK -->