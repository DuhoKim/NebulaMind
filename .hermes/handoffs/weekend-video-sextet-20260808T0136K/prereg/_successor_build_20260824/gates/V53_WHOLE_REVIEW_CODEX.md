# V53 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** V53 repairs the arithmetic inventory in §5 and names the five promoted raise sites, but the central live example still does not satisfy the rule it is supposed to demonstrate. One site labelled unreachable is directly reachable through the pinned function's documented integer `budget` argument, the claimed measurement harness is not reproducibly specified or present in the referenced files, and the four construction claims cite a general docstring rather than the per-site preceding conditions the promotion rule requires. The V52 inventory repair also missed a live stale “48 unread” instruction in §11, and the Row-L exemption is broader than its wording admits because “the freeze signature” has no canonical signed body or verifier in this draft.

## Identity and machine checks

- I read `gates/BRIEF_V53_REVIEW.md` first.
- Before reading the subject, I recomputed SHA-256 as `cc4e289578b129e403c07c78749bc6064a23385e0ec261c0dacd2a35cd010eba`, an exact match.
- `tools/prereg_counts.py`: 16 Class P / 8 Class E; prose matches the table.
- `tools/prereg_trace.py --check`: 52 transitions, 0 problems; its three self-test controls all fired.
- `tools/void_registry.py`: 54 antecedents and registry digest `a4d1d745b2ed33bc0e01dd39b845f88daffdc542d2bdd98d5e122ab7dd443d37`; six controls, 0 failures.
- `tools/prereg_lint.py`: exit 0, 0 blocking. It emitted 97 legacy-citation advisories, not the brief's stated 96. Per the principal's option-D ruling these are advisory and are not numbered findings.
- Independent AST/table reconciliation confirms 112 `Raise` nodes and the current table counts: CALLER 20, INTEGRITY 61, NUMERICAL 17, NUMERICAL-PLANNING 3, TYPED-OUTCOME 3, UNREACHABLE-BY-CONSTRUCTION 4, UNREACHABLE-MEASURED-ONLY 1, WRAPPER 3.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §5 lines 497–506; pinned reference lines 1378–1403

L1401 does not meet §5's definition of an unreachable guard. The status is introduced for a guard that “cannot fire at all,” but the pinned function exposes `budget` as an ordinary integer argument and neither its signature nor docstring restricts that argument to `HC_REAL_LABELS = 500`. Executing the frozen bytes with a contract-shaped 3×9 table of 100s and `budget=200` reaches L1401 exactly and raises:

`RuntimeError: inherited floors need 270 labels, budget 200 — FAIL`

The other positive-control failures are not needed for this counterexample. Calling the site `UNREACHABLE-MEASURED-ONLY` because 60,000 executions happened to use frozen production constants changes the scope from the function's calling contract to one selected caller without saying so. That conflicts with §5's own boundary test (“could this raise fire while every argument satisfies the documented contract?”) and with §11's still-correct requirement to classify per call site. Either the function contract must make `budget=500` mandatory for the classified production path and the record must be path-scoped, or L1401 is reachable and must remain a numerical failure. Measurement-only non-observation cannot override a concrete admissible firing.

### F2 — MEDIUM / REPAIR-REQUIRED — §5 lines 498–505; `ref/RAISE_SITE_CLASSIFICATION.md` lines 5, 103–110

Even setting F1's counterexample aside and reading the promotions as production-only, the five sites still lack the evidence record §5 requires. Evidence type (i) promises a reproducible stated harness and input generator. V53 gives only an aggregate description (“60,000 generated cell-count tables,” nine unnamed density scales, dead strata/bins injected) with no script or receipt, no exact density values, no generator/distribution, no seed/addressing, and no per-site execution counts. A content search of the referenced build finds the 60,000 claim only in V53/its brief and later prose about the repair, not a runnable harness or output artifact. The ledger table records only class labels.

The four type-(iii) promotions also do not name the “specific earlier condition” required by line 500. They collectively cite the function docstring's assertion that feasibility is decided before allocation, but the source-level reasons differ: L1411 depends on `total_need <= budget` plus exact completion of each stratum lift; L1435 depends on `budget <= cc.sum()` plus preserved per-cell headroom; L1437 depends on the `left` loop reaching zero; and L1439 depends on every increment being bounded by cell headroom. A general docstring slogan is not a per-site structural argument and does not prove those distinct invariants. V53 names the sites, but the repair remains assertion-level rather than the named reproducible/structural evidence its own rule demands.

### F3 — MEDIUM / REPAIR-REQUIRED — §5 line 507; §11 line 948

The V52 inventory repair is incomplete. Section 5 now says the corpus “has since been read in full,” every site is classified, and none is unassigned. The current 112-row ledger agrees. But the live implementation inventory in §11 still says **“48 sites are currently unread and the class is reported as a range until they are.”** That is not historical quotation; it directs the next atomic revision and directly contradicts the current state.

The brief says the 29/31/48-unread inventories were withdrawn, not merely superseded. Leaving the 48-unread instruction in §11 means the answered finding survives exactly where an implementer is told what work remains. Remove the stale sentence and replace it with the current state while retaining the separately parked per-call-site/call-graph obligation.

### F4 — MEDIUM / REPAIR-REQUIRED — §6.1 Row L line 587; clauses 3(b–c) and 6; §11 lines 940–946

The Row-L exemption is not as narrow as claimed because one of its two named objects is undefined at the payload level. The opening authorization is safe in this respect: clause 6 enumerates its canonical body and signature envelope and names a verifier. The BS-L signature is likewise over an exact canonical body digest. By contrast, the draft only says Duho “signs the freeze” and later binds “Duho's freeze signature” into BS-L. It defines no canonical freeze-signature body, document digest/version, envelope fields, or verifier, and §11 adds no such schema.

Therefore “the freeze signature” is a label, not a closed object identity. A signature over arbitrary or stale bytes can be called the freeze signature and falls within the named exemption from `signing anything but the canonical lock digest`; `verify_lock()` is required to bind the bytes it is handed but is not required to prove what those freeze-signature bytes authenticate. The repair correctly needed an exception for the actual P0 freeze act, but it exempted an untyped category instance. Define and authenticate the exact freeze-signature object (including the V53/final preregistration digest and completeness manifest it signs), then exempt only a conforming instance.

## Failed attacks / repairs that held

1. **§5 and the ledger's current row counts hold.** Recounting the table gives 17 current `NUMERICAL` rows and five separately promoted rows; the draft's 17 (or 13 if the four soft rows move to CALLER) matches the row-level artifact. F3 concerns the stale §11 status, not this recount.
2. **The falsification route is named.** If a legitimately marked unreachable guard fires, §5 sends it to `INCONCLUSIVE-BY-NUMERICAL-FAILURE` and requires correction of the classification record. F1/F2 concern whether the sites earned the marking.
3. **BS-3g is honestly not receiptable yet.** It is in the closed non-χ receipt class and has a `blocks BS-6` edge, while §11 explicitly admits the missing schema, producer, verifier, and gain-to-sign mapping. The slot remains DESIGN/UNFILLED and BS-6 remains blocked; I did not turn disclosed incompleteness into a finding.
4. **The V43 rerun deletion holds.** No discretionary retry after a terminal run outcome, attempt log, attempt cap, seed schedule, or extra slot has returned. Remaining “rerun” language concerns pre-run design/fixture work or explicitly says no Stage-C rerun.
5. **The V42 citation correction holds.** `gates/PREREG_TEXT_V11_KIMI.md` F7 is the Stage-P finding and states that exact Stage P is not implemented in the §0-pinned file; F4 is the unrelated access/custody finding.
6. **VOID misconduct scope holds.** Forbidden acts and protocol/digest deviations remain phase `Any`; only numerical non-finite/degenerate conditions are restricted to post-unblinding.
7. **The parked call-site and Row-L-phase findings remain parked rather than renumbered here.** I confirmed the raise ledger is per syntactic raise rather than per caller/path and that `VOID-6.1L-WRONG-SIGNATURE` remains P7-only, but the brief explicitly refers both matters and says not to re-derive them.
8. **Class inventory holds at 16/8.** Nothing in operative prose assumes 15/8; the historical transition correctly records 15/8 → 16/8 when BS-3g was added.

## Evidence and limits

I read all 952 lines of V53, both V52 whole-document reports, the V11 KIMI report, the complete raise-site classification and generator, the relevant pinned reference functions and callers, the current §7/§7.1/§11 tables, and the named checker sources needed to run them safely. I ran only read-only checkers with bytecode writes disabled, independently exercised L1401, and searched for the claimed harness and freeze-signature contract. I did not read real χ data, modify the draft/reference/tools, or write outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V53
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §5 lines 497–506; ref lines 1378–1403 | L1401 is directly reachable through the pinned function's unrestricted integer budget argument, so non-observation under one frozen-caller harness cannot mark it unreachable.
F2 | MEDIUM | REPAIR-REQUIRED | §5 lines 498–505; raise ledger lines 103–110 | The five promotions still lack the reproducible harness record and per-site structural conditions required by their own evidence rule.
F3 | MEDIUM | REPAIR-REQUIRED | §5 line 507; §11 line 948 | Section 11 still says 48 sites are unread although §5 and the complete ledger say every one of 112 nodes has been classified.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 Row L line 587; clauses 3 and 6 | The exemption for “the freeze signature” is broad because no canonical freeze-signature body or verifier defines which signed bytes qualify.
<!-- END FINDINGS-BLOCK -->