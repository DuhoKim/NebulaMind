# V52 whole-document review — GPT56

**Verdict: NOT CLEAR.** I verified the subject SHA-256 before reading it. The new `UNREACHABLE-BY-CONSTRUCTION` example does not satisfy its own per-site promotion rule, the draft retains a raise inventory it already disproves, and the supporting raise-site artifact does not provide the call-site/path classification §11 correctly requires.

## Findings

### F1 — HIGH — the live `UNREACHABLE-BY-CONSTRUCTION` promotion fails its own evidence contract

**Draft §5, lines 497–503; pinned source lines 1378–1442; `OPEN_QUESTION_PRE_UNBLINDING_NUMERICAL_ROUTES.md` lines 268–295; `ref/RAISE_SITE_CLASSIFICATION.md` lines 101–109.** Lines 498–501 require evidence to be named per site and require a structural promotion to state the specific preceding condition that provably subsumes that site. Line 502 then promotes five `allocate_handcheck` guards as the live `(iii)` example, but names neither the five source sites nor a specific predecessor for each. It substitutes the function docstring’s general statement that feasibility is “DECIDED before allocating.” The underlying 60,000-table record identifies the five not reached as source lines 1401, 1411, 1435, 1437, and 1439. Line 1401 is itself an intended feasibility decision (`total_need > budget`), not a later guard subsumed by a preceding feasibility decision. With the explicit function argument `budget=200` and a contract-shaped 3×9 table of 100s, the pinned function reaches it exactly and raises `inherited floors need 270 labels, budget 200 — FAIL`. If production’s frozen `budget=500` is meant to make this site unreachable, the required structural evidence is the separate numerical bound `total_need <= 9 × max(30, 3 × 10) = 270 < 500`, not the claimed preceding guard.

The classification record supplies no missing promotion: it marks all eight allocation raises `NUMERICAL`, has no `UNREACHABLE-BY-CONSTRUCTION` class, and attaches no harness or structural predecessor to any row. Thus V52 calls five guards promoted by evidence when the named record does not promote them and one of the five does not satisfy the stated structural route. This is load-bearing because line 503’s safe-falsification clause applies only after a guard has been validly marked. Repair requires a per-site record naming the harness/count and the actual proof predecessor (or frozen-constant proof) for each promoted site; line 1401 must not be described as subsumed by an earlier feasibility guard.

### F2 — MEDIUM — the current draft still contains the raise inventory V50’s own AST recount superseded

**Draft §5 line 504 and §11 line 944; pinned source; `ref/RAISE_SITE_CLASSIFICATION.md` lines 9–16.** The first half of line 504 correctly reports the live AST inventory: 112 nodes, including 39 `ManifestClosureError` and one bare re-raise. The same paragraph then retains the old V49 partition — 29 caller guards, 31 reachable run-time failures, 48 unread — despite the supporting table saying every node has been read and reporting 20 CALLER, 61 INTEGRITY, 22 NUMERICAL, 3 NUMERICAL-PLANNING, 3 TYPED-OUTCOME, and 3 WRAPPER. Section 11 is worse: line 944 again says the pinned source carries **111** raise sites and that, apart from three typed outcomes, the rest are `RuntimeError`/`ValueError`. Independent AST enumeration returned exactly 112: 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `InconclusiveByCalibration`, 1 `ValueError`, and 1 bare re-raise.

These are current assertions about the pinned bytes, not historical quotations. They also sit inside the implementation inventory a future applier is told to execute, so the stale 111/type statement can omit the bare propagation site and the entire closure-exception class again. Replace the stale partition with the current table’s status (including any unresolved/soft rows), and remove or correct §11’s 111/`RuntimeError`-or-`ValueError` sentence.

### F3 — MEDIUM — the supporting artifact classifies raise statements, not the failure paths/call sites the draft says are the unit of classification

**Draft §11 line 944; `ref/gen_raise_classification.py` lines 18–35; `ref/RAISE_SITE_CLASSIFICATION.md` lines 94–120; pinned source lines 1199–1209 and 1446–1468.** Section 11 correctly says classification must attach to every failure path and call site, because the same helper raise can have different admissibility contracts at different callers. The generator does the opposite: it walks `ast.Raise` nodes once, assigns each source line to one hard-coded class, and never enumerates callers or paths. The table therefore cannot establish the implementation obligation it is presented as supporting.

The four rows it flags as “soft” demonstrate the consequence. `inject_signs` line 1209 tests the supplied argument `a` after shape expansion; `accuracy_from_handcheck` lines 1462, 1464, and 1468 test supplied `n_counts`, `agree_counts`, and `epsilon_hat`. Under §5’s literal argument-as-supplied boundary these are caller/admissibility checks. Under particular production callers they may instead be unreachable because Stage P passes the frozen 0.85 and Stage C is supposed to follow the calibration guard. They are not established as one unconditional `NUMERICAL` class at the raise node. The source’s in-file `inject_signs` paths pass `A_FLOOR` or `1.0`, reinforcing why caller context matters. Generate the required call graph/path rows and classify each against that caller’s documented contract; a one-row-per-raise table may remain an inventory, but must not stand in for the required classification.

## Attacks that held

- Subject identity held: SHA-256 `a825e5d2045721c44703558156f0532e9d09dc22ca0f9e08fa5031b6831dd2e4` matched before reading.
- Row L’s exemption is narrow and complete on the row’s own acts: the P0 freeze signature and P7 canonical opening authorization are the two non-lock-digest signatures it mandates; the BS-L detached signature is over the canonical lock digest. I found no third mandated Row-L signature and no category-wide exemption.
- The class rule is written as a general condition rather than a closed site list, includes every phase, and gives specific outcomes plus all §7.1 VOID antecedents precedence. Its conversion remains openly unimplemented and BS-6 remains blocked.
- The falsification sentence does name `INCONCLUSIVE-BY-NUMERICAL-FAILURE` as the default route if a genuinely numerical guard is wrongly marked unreachable; F1 concerns failure to earn the marking, not absence of that default sentence.
- V43’s computational rerun allowance is gone. Remaining rerun/retry language concerns Stage-P design execution, Branch-A refixturing, BS-2a failure semantics, historical explanation, or explicit no-rerun rules; I found no retry after a terminal run outcome.
- `KIMI-V11 F7` is the Stage-P/code-subject finding: the report says the exact Stage P is not implemented in the §0-pinned file and identifies the v7 receipt subject. The V42 citation correction is accurate.
- The misconduct VOID antecedents remain at `Any`: `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION`. Numerical non-finite/degenerate antecedents remain post-unblinding.
- `BS-3g` is now in the closed non-χ slot-receipt list and has a `blocks BS-6` edge. The document also accurately admits that no schema, producer, or independent verifier yet makes that edge receiptable and keeps the slot DESIGN/UNFILLED; I did not turn that disclosed blocked state into a separate finding.
- `tools/prereg_counts.py` returned 16 class P / 8 class E with prose agreement. `tools/prereg_trace.py --check --self-test` returned 51 transitions and 0 problems. `tools/void_registry.py --self-test` returned 6 controls and 0 failures.
- `tools/prereg_lint.py` exited 0 with 0 blocking findings. It emitted **97** advisory legacy-citation findings, not the brief’s asserted 96; that discrepancy is in the dispatch claim, not a blocking defect established in the draft.

## Evidence and limits

I read all 948 lines of the subject; inspected the V11 KIMI report, the pinned reference, the raise-site table and generator, the numerical-routes note, and the V49 GPT56 report; independently enumerated the AST raise types; exercised the line-1401 allocation branch; and ran the four named checker families. I did not modify the draft, reference code, tools, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V52
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §5 lines 497–503; ref lines 1378–1442 | The live UNREACHABLE promotion names no per-site proof, and one of its five guards is the feasibility decision itself rather than a later guard subsumed by it.
F2 | MEDIUM | REPAIR-REQUIRED | §5 line 504; §11 line 944 | Current prose retains stale 29/31/48-unread and 111/RuntimeError-or-ValueError inventories that contradict the 112-node pinned source and supporting table.
F3 | MEDIUM | REPAIR-REQUIRED | §11 line 944; ref classification/generator | The supporting artifact classifies one row per raise statement, not the per-call-site failure paths the draft correctly requires, producing context-insensitive soft classifications.
<!-- END FINDINGS-BLOCK -->