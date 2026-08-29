# V54 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** The V53 promotions are genuinely withdrawn from both the draft and the raise-site ledger, and the fallback makes a future mistaken unreachability classification routing-safe. But the restated promotion rule still permits measurement-only non-observation to establish `UNREACHABLE-BY-CONSTRUCTION` without exhaustive coverage or a structural proof. The reconciled 22-row numerical ledger also contains a caller-admissibility check classified as numerical despite §5's explicit boundary, and V54 states a new 80,000-execution result for which no runnable harness or receipt is present in the referenced build.

## Findings

### F1 — MEDIUM / REPAIR-REQUIRED — §5 lines 498–523

The restated evidence bar remains insufficient for the status it awards. Type (i) still permits an execution count by itself to promote a guard that the draft defines as one that “cannot fire at all.” Lines 518–522 now require a harness to vary every documented argument and include a family-level positive control, but neither requirement establishes coverage of each argument's domain or of interactions. A generator can literally vary both `cell_counts` and `budget`, keep `budget` only in a high range where L1401 does not fire, and include sparse cases that fire L1403 as the positive control. It would satisfy (a) and (c) while the already-demonstrated admissible `budget=200` counterexample remains outside its support. The rule would nevertheless allow measurement-only promotion under (i).

This is the absence-clause failure in rule form: “every argument varied” is not “every reachable state covered.” The line-523 fallback safely routes a falsely promoted guard to `INCONCLUSIVE-BY-NUMERICAL-FAILURE`, so this is not an unterminated-run finding. It is a false-record finding: a status named `BY-CONSTRUCTION` can still be earned by non-exhaustive sampling alone. Require either an exhaustive finite-domain argument with coverage closure or a per-site structural proof; otherwise name the status as measured non-observation rather than construction.

### F2 — MEDIUM / REPAIR-REQUIRED — §5 lines 496 and 524; `ref/RAISE_SITE_CLASSIFICATION.md` lines 111–113; pinned reference lines 1457–1468

The ledger's selected `NUMERICAL 22` classification does not consistently apply §5's caller boundary. The clearest counterexample is pinned-reference L1464, `agreement count outside [0, n]`. `accuracy_from_handcheck(agree_counts, n_counts, ...)` receives both arrays as arguments, and this guard checks their supplied cross-field admissibility. With admissible count data an agreement count cannot be negative or exceed its total. This is the same caller-input class as L1460's shape/emptiness check, which the ledger correctly marks `CALLER`; it is not a numerical failure computed from admissible data.

The ledger marks L1464 `NUMERICAL | soft`, and its header says all four soft rows might instead be caller errors, making the numerical subtotal 18. That caveat does not reconcile the current classification: §5 simultaneously says every site is classified, none is unassigned, and the numerical class is 22. At least L1464 fails the stated boundary as written. Reclassify it as `CALLER` (and resolve the other soft rows individually) before presenting one completed inventory. This finding is at the acknowledged raise-statement unit; it does not re-derive the separately parked per-call-site/call-graph finding.

### F3 — LOW / ADVISORY — §5 lines 513–517; `OPEN_QUESTION_V53_RESIDUE.md` lines 48–51

V54 states that L1411/L1435/L1437/L1439 did not fire across a new 80,000-execution rerun with `budget` varied. The only other on-disk occurrences are the review brief and `OPEN_QUESTION_V53_RESIDUE.md`, both of which repeat the result. No generator, seed/addressing record, exact input distribution, per-site counts, runnable harness, or output receipt is present in the referenced build, and the regenerated raise ledger records only classifications.

Because all promotions are withdrawn, this unsupported measurement no longer determines a live classification and is therefore advisory rather than a blocker. But “their measurement survives” is still a quantitative evidence claim in the preregistration. Either add a pinned reproducible harness/receipt or reduce the sentence to the verified fact needed for the withdrawal: no site currently meets the promotion bar.

## Failed attacks / repairs that held

1. **Withdrawal is complete.** The draft says no site currently holds `UNREACHABLE-BY-CONSTRUCTION`, and `ref/RAISE_SITE_CLASSIFICATION.md` contains zero such classifications. All eight `allocate_handcheck` raises are back in `NUMERICAL`.
2. **The falsification route is named.** If a future guard marked unreachable fires, §5 sends it to `INCONCLUSIVE-BY-NUMERICAL-FAILURE` and requires correction of the record. F1 concerns promotion truth, not routing safety.
3. **The class rule is general in prose.** It is stated as a condition rather than a closed list and gives specific outcomes and every VOID antecedent precedence. Its conversion remains openly unimplemented, so the draft does not falsely claim executable completeness.
4. **BS-3g is honestly not receiptable yet.** It is on the closed non-χ list and blocks BS-6, while §11 explicitly records the absent `SLOT_SCHEMA` entry, producer, verifier, and still-open gain-to-sign mapping. This disclosed DESIGN/UNFILLED state is not a new finding.
5. **Row L is narrow enough for its three named acts at the text level.** The freeze signature and canonical opening authorization are exempt; the BS-L detached signature is already over the canonical lock digest. The separately referred freeze-signature-definition and P7-only antecedent issues were not re-numbered.
6. **The V43 rerun deletion holds.** No discretionary retry, attempt log, seed schedule, attempt cap, or extra run slot has returned. Remaining retry/rerun language is design work, historical record, or an explicit no-rerun rule.
7. **The V42 citation correction holds.** `gates/PREREG_TEXT_V11_KIMI.md` F7 is the Stage-P finding that exact Stage P is absent from the §0-pinned file; F4 is the custody/access finding.
8. **VOID misconduct scope holds.** Forbidden acts and protocol/digest deviations remain `Any` in §5 and in `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION`. Only numerical non-finite/degenerate conditions are post-unblinding.
9. **Counts and trace hold.** Independent AST enumeration gives 112 raises with the stated exception-type breakdown. `prereg_counts.py` gives 16 Class P / 8 Class E; `prereg_trace.py --check` gives 53 transitions / 0 problems; `void_registry.py --self-test` gives six controls / 0 failures.
10. **Lint is nonblocking.** It exits 0. It emits 97 legacy advisories rather than the brief's 96; as in V53, that is a dispatch-count mismatch, not an unresolved citation defect under option D.

## Evidence and limits

I read `BRIEF_V54_REVIEW.md` first, then verified the subject SHA-256 exactly before reading the subject. I read all 970 subject lines, both V53 whole-review reports, the V11 KIMI report, the complete raise-site ledger, the relevant frozen reference functions, `OPEN_QUESTION_V53_RESIDUE.md`, and the named checker sources. I recomputed the §0 source pins, independently counted the AST raises, ran the four read-only checker paths, compared V53→V54, and searched the build for the asserted 80,000-run evidence. I did not read real χ data or modify the draft, reference, tools, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V54
VERDICT: NOT CLEAR
COUNT: 3
F1 | MEDIUM | REPAIR-REQUIRED | §5 lines 498–523 | The evidence bar still lets non-exhaustive measurement-only sampling establish a status defined as impossible by construction.
F2 | MEDIUM | REPAIR-REQUIRED | §5 lines 496, 524; raise ledger lines 111–113 | L1464 tests supplied count admissibility but is classified NUMERICAL, so the reconciled 22-row inventory violates its own caller boundary.
F3 | LOW | ADVISORY | §5 lines 513–517 | The asserted 80,000-execution rerun has no pinned runnable harness, generator, per-site count record, or receipt in the referenced build.
<!-- END FINDINGS-BLOCK -->