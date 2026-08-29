# V49 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** V49's new class rule does not cover the failure universe that its own implementation item enumerates: the prose promises to terminate any qualifying computation failure, while §11 inventories only explicit `raise` statements, and the pinned reference demonstrably produces an implicit `OverflowError` outside that inventory under finite inputs not excluded by any documented function contract. The rule's caller/run boundary is also internally non-single-valued at `_finite`, and the advertised 31–79 class range is a heuristic candidate partition rather than a verified range after precedence removes VOID and other specific outcomes. Separately, the long-carried Row-L signing contradiction remains live: two signatures the lifecycle requires still satisfy the row's own unqualified void condition.

## Identity and machine checks

- Recomputed subject SHA-256 before reading: `d8a9501e0653dd84ca554e26aaacd4de87d4efb34cb6ef6266285757b96ce2bc` — exact match.
- Recomputed §0 pins: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- `prereg_counts.py`: 16 Class P / 8 Class E; prose matches.
- `prereg_trace.py --check ... --self-test`: real subject clean; 48 transitions; all three scope controls fire.
- `void_registry.py --self-test`: 54 antecedents; six controls; zero failures. This is name coverage, not semantic coverage, as V49 correctly discloses.
- `prereg_lint.py`: exit 0; 96 advisory legacy citations and 0 blocking. Per the brief, those advisories are not findings here.
- Independent Python-AST recount of the pinned reference: 112 `ast.Raise` statements, one of which is a bare re-raise at reference line 776; therefore 111 sites that instantiate an exception, exactly three typed to named inconclusive outcomes. The draft's 111/3 count holds under that disclosed convention.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §6.1 Row L and Clauses 3/6, V49 lines 577, 592–603: the required signing path still voids itself

Row L requires Duho to produce three signed objects: the freeze signature, the BS-L detached signature, and the canonical opening authorization. Its unqualified void condition is still “signing anything but the canonical lock digest.” Clause 6 requires a signed opening-authorization body/envelope, and Clause 3 requires the separate freeze signature in BS-L's manifest. Thus the required P0 freeze signature and P7 opening-authorization signature are both signatures of something other than the BS-L canonical lock digest and satisfy Row L's own VOID condition.

This is not an inferred omission. V49's preamble itself carries “§6.1 Row L's signing path voids itself” at line 31, and the current row still has the bytes that caused CODEX-V24 F1. The brief's deliberately-unrepaired list exempts only the gain mapping and `require_authorization`; it does not exempt this contradiction. The current `VOID-6.1L-WRONG-SIGNATURE` row at line 804 also remains P7-only and therefore cannot accurately represent the distinct P0/P6/P7 acts.

Smallest sufficient repair: phase-index the rule and antecedents—P0 authenticates only the canonical freeze body, P6 signs only the canonical BS-L body digest, and P7 authenticates only the canonical opening-authorization body—so each required act has a distinct permitted body and a correctly phased failure ID.

### F2 — HIGH / REPAIR-REQUIRED — §5 lines 494–498 and §11 line 934 versus `ref/successor_ref_v9.py` lines 1500–1503 and 1533–1539: the “any computation” rule is narrower in its implementation and non-single-valued at helper boundaries

V49's condition promises that **any computation** in the pinned reference that can fail under its calling contract and admissible data terminates in a named outcome. Section 11 then defines the implementation universe as “every raise site” and sizes it from 111 explicit exception-instantiating statements. That universe is not closed over computation failures.

I executed the pinned `sigma_ours_scalar()` directly with `(sigma_beta=1e200, beta=1.0, a_star=0.85, sigma_a=1.0)`. All four arguments are finite, `a_star` satisfies the document's calibration floor, and neither §3 nor the function documents an upper bound. `_finite()` accepts every input and `q > 0`; Python then raises an implicit `OverflowError: (34, 'Result too large')` at the arithmetic on reference line 1538. There is no `raise` statement at that failure site, so a per-`raise`-site classification of the advertised 111 cannot classify or convert it. The same occurred with `(1e308, 0.0, 0.85, 0.0)`.

The caller/run wording is independently ambiguous at the exact helper V49 names as genuinely unterminated. `_finite(*vals)` tests a property of its arguments “as supplied,” which line 496's first sentence calls a caller error; but `_decide_from()` supplies values it computed from the run, which line 496's second sentence/test and line 498 call a run outcome. A helper boundary therefore changes the classification without changing the failed value. The “documented contract” cannot resolve this because `_finite` and `sigma_ours_scalar` document no magnitude/admissibility contract in the pinned bytes.

This is a concrete unenumerated failure, not a request to list the 48 unread explicit sites. The class rule can remain general, but §11 must cover implicit operation/library exceptions as well as syntactic `raise` statements, and it must classify by the provenance of the failed value across helper boundaries. Alternatively, exact admissibility bounds and a top-level conversion/refusal policy must make the demonstrated inputs caller-invalid before claiming the universe is closed.

### F3 — MEDIUM / REPAIR-REQUIRED — §5 line 497 and `OPEN_QUESTION_PRE_UNBLINDING_NUMERICAL_ROUTES.md` lines 311–349: the 31–79 “class” range is not established after precedence

The arithmetic 29 + 31 + 48 = 108 correctly closes the 108 untyped explicit sites, but it does not establish that 31–79 sites belong to `INCONCLUSIVE-BY-NUMERICAL-FAILURE`. The new outcome's condition excludes failures already claimed by a more specific outcome. The referenced open-question file's post-ruling pass identifies a third material class—approximately 25 digest/protocol/integrity failures governed by VOID—and explicitly says the partitions changed across heuristics and are “indicative, not measurements.” No per-site classification ledger on disk supports the asserted lower bound.

A “reachable run-time failure” is not automatically a member of the new numerical outcome: planner-digest mismatch, manifest non-closure, parent-receipt inconsistency, and similar executable failures can be run-time in the ordinary sense while precedence assigns them to `VOID-5-DIGEST-DEVIATION` or `VOID-5-PROTOCOL-DEVIATION`. V49's general precedence sentence is broad enough to preserve VOID, so this does not make the outcome unreachable; it makes the stated extent unsupported. Until the sites are read and specific outcomes subtracted, 31–79 is a candidate-failure range, not the new code's class range.

Smallest sufficient repair: relabel 31–79 as the heuristic range of untyped candidate run-time sites, with no claimed lower bound on the default numerical outcome, or publish the promised per-site ledger and compute the class range only after removing caller errors and all more-specific outcomes.

## Failed attacks / repairs that held

1. **BS-3g receiptability attack held as honest incompleteness.** V49 line 549 adds BS-3g to the closed non-χ-bearing receipt-class list, line 730 keeps the slot DESIGN/UNFILLED and blocked on the one open γ mapping, and §11 line 937 explicitly says the edge is not yet receiptable and requires a `SLOT_SCHEMA` entry, producer, and independent verifier. Naming rather than specifying that item is insufficient to fill the slot now, but V49 does not claim otherwise; BS-6 remains blocked.
2. **V42 citation correction held.** `gates/PREREG_TEXT_V11_KIMI.md` F7, lines 224–241, is the Stage-P finding: the exact Stage-P receipt ran against v7, exact Stage P is not implemented in the §0-pinned v9 file, and the benign v7→v9 transfer still does not fill BS-5p. V49's `KIMI-V11 F7` citation supports the claim. KIMI F4 is the §6.1 access finding and would be wrong here.
3. **Rerun-deletion attack held.** Searches for rerun/retry language found the historical Stage-P measurement reruns, Branch-A fixture reruns, and BS-2a retry semantics, not a revived retry after a terminal study-run outcome. Row P says “No discretionary retry”; §5 line 504 accurately records that the five-step study rerun was deleted and no seed schedule, attempt log, verifier, cap, or extra slot remains.
4. **VOID misconduct phase attack held.** V49 lines 506–507 preserve forbidden acts and protocol/digest deviations at any phase; registry lines 765–767 independently say `Any`. Only numerical non-finite/degenerate antecedents remain post-unblinding.
5. **Inventory attack held.** The §7 parser independently returns 16/8, V49 line 715 states 16/8, and the transition record accurately records 15/8 → 16/8 when BS-3g was added. Historical fold-record quotations of twelve/fourteen are explicitly scoped to V15 and are not current inventory claims.
6. **New-code reachability attack otherwise held.** The condition's “more specific outcome governs” clause makes the default numerical code reachable on a qualifying unclaimed failure and silent on specific POWER/CALIBRATION/MISSING-OUTPUT failures. The defect is the non-closed failure universe and boundary above, not the same ordering dead branch that killed `INCONCLUSIVE-BY-COMPUTATION`.

## Evidence and limits

Read content: `BRIEF_V49_REVIEW.md`; all 938 lines of V49; V48→V49 byte diff; `ref/successor_ref_v9.py` around serialization, calibration, decision, and production paths; `PREREG_TEXT_V11_KIMI.md`; `OPEN_QUESTION_PRE_UNBLINDING_NUMERICAL_ROUTES.md`; `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`; `FINDINGS_MAP.md`; and CODEX V24/V40/V43/V44/V46 reports as needed for cited provenance. Ran SHA-256 checks, lint/count/trace/VOID checkers and self-tests, exact text searches, an AST raise inventory, and direct execution of the scalar uncertainty function. I did not read real χ data, fetch external data, run scientific measurements, or modify the draft/reference/checker bytes. The repository was already broadly dirty; this seat wrote only this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V49
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §6.1 Row L, lines 577 and 592–603 | Required freeze/opening signatures still satisfy Row L's unqualified wrong-signature VOID rule.
F2 | HIGH | REPAIR-REQUIRED | §5 lines 494–498; §11 line 934 | The any-computation rule inventories only explicit raise sites and gives conflicting classifications across helper boundaries.
F3 | MEDIUM | REPAIR-REQUIRED | §5 line 497 | The 31–79 numerical-class range is a heuristic candidate partition that does not subtract more-specific VOID/outcome sites.
<!-- END FINDINGS-BLOCK -->