# V59 whole-document review — GPT56

## Verdict

**NOT CLEAR.** The dispatched V59 bytes matched the required SHA-256 before the first draft read. The central V59 repair is not a complete producer binding: §7 still names the permissive `receipt` symbol for BS-7p, while §11’s universal requirement is impossible for several §6.1 producers whose receipts are not `SLOT_SCHEMA` slots. The BS-3g non-χ claim also fails twice: the schema is not in the pinned implementation, and scalar field types do not themselves prevent an object-level value or covert object-indexed encoding. The refusal vocabulary is suspended in prose but still enforced by both the live schema language and the referenced checker. Additional defects remain in the checker pin, the unreachability evidence bar, and the raise-ledger count/boundary claims.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §0 lines 72–100; §7 line 768; §11 lines 982–986; pinned `successor_ref_v9.py` lines 208–224

The strict-constructor binding is internally incomplete and, read literally, impossible.

First, §7’s BS-7p row still names **`receipt`**, not `receipt_strict`, as its code symbol. Section 0 says the pinned code defines digest serializations and code wins over conflicting prose. Thus a named §7 producer retains an explicit normative route to the permissive v9 constructor even while §11 says every producer must use the wrapper “and through nothing else.” This is exactly the producer route the brief asked the seat to find.

Second, §11 binds **every producer named in §6.1 and §7**, but several §6.1 producers emit receipts that are not slot receipts at all: Row C’s cutout-completion receipt, Row D’s per-object measurement receipts, Row H’s label-set receipt, Row O’s unblinding receipt, and Row P’s adequacy receipt. A wrapper whose first rule is “slot must be in `SLOT_SCHEMA`” must reject those artifacts unless each receives a declared slot/schema, yet the draft intentionally treats several as separate χ-bearing receipt classes. The universal binding therefore cannot be implemented as written; narrowing it to canonical slot receipts would leave the current wording’s claimed all-producer closure false.

Live-file reproduction strengthens this: no Python file in the review tree contains `receipt_strict`; the pinned `SLOT_SCHEMA` has 18 entries; and direct `v9.receipt('BS-3g', {'per_object_chi': b'+1'})` still returns a canonical-looking envelope. This is document-level required future work, but the document has not actually eliminated every producer route to `receipt()`.

### F2 — HIGH / REPAIR-REQUIRED — §6.1 lines 574–576; §7 line 765; §11 lines 987–1026; pinned `successor_ref_v9.py` lines 190–224

BS-3g is still asserted on the non-χ side of an authenticated **pinned** schema boundary that does not exist in the pinned bytes. Section 6.1’s closed-list claim includes BS-3g as a slot receipt “under the pinned `SLOT_SCHEMA` as conformed by this revision’s code items.” The live pinned v9 schema does not contain BS-3g, and §11 is explicitly an inventory “for the next atomic revision,” not pinned implementation. The live test accepted a `per_object_chi` field for BS-3g and returned envelope/body digests.

The §7 row is honest that the estimator/verifier are “built, not bound,” the mapping is absent, γ̂ is unmeasured, and the slot is UNFILLED. That honesty does not rescue §6.1’s stronger current classification: until the schema entry, producer, independent verifier, and strict path are pinned, there is no authenticated schema under which BS-3g can safely occupy the exhaustive non-χ list. V57’s suspension makes this worse operationally because the other pre-lock log classification is also deliberately unpinned; the draft now has two controls whose prose classification outruns executable schema custody.

### F3 — MEDIUM / REPAIR-REQUIRED — §11 lines 991–1020

The claimed “property of the field list” is false. A fixed-width scalar is not incapable of carrying a per-object quantity: `gamma_hat`, `sigma_gamma`, or `gamma_bound` accepts any finite IEEE-754 double, including the χ/confidence value of one selected object; `n_perturbations` accepts any non-negative integer, including an object identifier or an object-indexed count. Fixed width prevents an array, not object-derived information or a covert object-indexed encoding.

The prose’s semantic definitions and proposed independent recomputation could constrain those channels, but that means safety depends on the producer, frozen input/sample identity, and verifier—not on the field list alone. No input-data digest, sample/mask digest, or perturbation-manifest digest appears among the nine fields, so the proposed verifier is not told by the receipt which frozen population and perturbation set it must recompute. The absence claim therefore does not survive the brief’s requested attack: the types alone do not enforce the universal negative.

### F4 — HIGH / REPAIR-REQUIRED — §6.1 lines 577–585; Row B line 601; `tools/refusal_vocabulary_check.py` lines 4–24, 46–65, 95–118

The suspension does not fully suspend. Lines 577–580 still normatively say the BS-2k refusal field carries exactly one code from the closed eight-code set and that there is no catch-all; Row B still requires every refusal to be logged. Lines 581–584 then say the derivation is withdrawn, the eight codes are not in force, and the catch-all question is reopened. That leaves the authenticated event schema with no in-force refusal enum while the mediator must log every refusal.

The referenced checker remains even less suspended. Its docstring says the exact eight-code ruling has “no escape hatch”; `CODES` hard-codes all eight, including the expressly non-surviving `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET`; and R01 rejects any replacement set. V59 happens to report only R05 because the obsolete eight strings are still present in its bytes. A from-scratch derivation that changes membership—as the principal ordered—would also receive R01 from the supposedly governing tool. A deliberately red fingerprint is not a suspension if the same checker continues enforcing the withdrawn membership and no-catch-all policy.

### F5 — MEDIUM / REPAIR-REQUIRED — §6.1 line 585; `tools/refusal_vocabulary_check.py`

The tool digest claim is false against disk. V59 says the corrected tool digest is `fd6d6d7e…`; independent SHA-256 of the referenced file is

`c2ccebbcb4730944ce1ff15ca27984feef17b39529f89656c9432b2e83c80b4c`.

The corrected code does include the `may touch` column in `keep`, so the substantive V56 fingerprint repair is present, but the draft does not pin the bytes that are actually on disk. Given that the paragraph uses the digest to identify which checker is “fixed,” this is a custody failure, not a cosmetic abbreviation issue.

### F6 — MEDIUM / REPAIR-REQUIRED — §5 lines 498–523; pinned `successor_ref_v9.py` lines 373–399

The restated unreachability evidence bar can still be satisfied literally while a guard remains reachable. Requiring a harness to vary every **argument** on the callable’s documented surface omits non-argument state: globals, filesystem objects, imported callables, process environment, mutable module state, and interaction/history.

A concrete site is `frozen_planner_digest()`: it has no arguments, but its line-395 guard fires depending on the live `_frozen_planner()` result and imported callable state. An argument-complete harness for this callable is vacuous—there are no arguments to vary—and a positive control for some broad “family” need not vary the relevant imported callable. The draft’s fallback routing is safe if a mistaken promotion later fires, but the evidentiary claim “UNREACHABLE-BY-CONSTRUCTION” would still be supportable by a harness blind to the dimension that controls reachability. The bar must require enumeration and variation/freeze justification of all reachable state dependencies, not only formal arguments.

### F7 — MEDIUM / REPAIR-REQUIRED — §5 lines 496 and 524; `ref/RAISE_SITE_CLASSIFICATION.md` lines 9–16 and 110–114; pinned reference lines 1446–1468

The draft and ledger still disagree after the sentence that says copied counts will drift was supposed to stop that defect. V59 says “The numerical class is 21”; the live generated table contains **NUMERICAL 20**, with totals CALLER 23, INTEGRITY 60, NUMERICAL 20, NUMERICAL-PLANNING 3, TYPED-OUTCOME 3, WRAPPER 3 = 112. The ledger header itself is stale too: it says soft reclassification drops NUMERICAL “from 22 to 18,” although its current table starts at 20 and marks only two rows soft.

One of those rows is not genuinely ambiguous under §5’s own boundary. `accuracy_from_handcheck(agree_counts, n_counts, epsilon_hat, sigma_epsilon)` receives `epsilon_hat` as a supplied argument; line 1468 rejects it when outside `[0, 0.5)`. This tests supplied-argument admissibility and is therefore CALLER by §5’s stated rule, just like the adjacent agreement-count check already moved to CALLER. The affirmative “numerical class is 21” is unsupported by both the live table and the document’s own boundary.

## Failed attacks / repairs that held

- Subject custody held before reading: SHA-256 was exactly `9257411511b39de6c32b8b5b52a2f4ad45dec287a9150332dadafdd6253c6105`.
- The frozen reference pin held: `successor_ref_v9.py` was exactly `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; independent AST enumeration found 112 `Raise` nodes.
- No ledger site currently holds `UNREACHABLE-BY-CONSTRUCTION`. The draft uses the term only for the ruled status, withdrawn history/evidence bar, and falsification routing; the live classification table has no such class.
- The falsification routing itself held: if a promoted guard later fires, §5 routes it to `INCONCLUSIVE-BY-NUMERICAL-FAILURE` and requires correction of the record rather than leaving the run unterminated.
- Row L’s named exemptions are narrow enough for the three signature acts the row mandates: freeze signature and opening authorization are named exceptions; the BS-L detached signature is over the canonical lock digest. I found no third mandated signature object caught by the condition.
- The V43 study-rerun deletion held. No discretionary rerun procedure, seed schedule, attempt log, cap, or rerun slot has returned; Row P still says “No discretionary retry.” References to Stage-P rerunning and BS-2a retry semantics concern pre-freeze design/execution behavior, not a retry of an `INCONCLUSIVE-BY-NUMERICAL-FAILURE` run.
- The KIMI citation repair held. V59 no longer claims KIMI-V11 F7 supports the Stage-P dual-valued conclusion; it expressly says F7 is a different disclosure finding. The source report confirms F7 concerns the v7 subject of the exact Stage-P receipt.
- The misconduct phase split held: `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION` remain `Any`; only non-finite/degenerate numerical antecedents are post-unblinding.
- Class counts held at 16 class P / 8 class E. `prereg_counts.py` matched the prose.
- `prereg_trace.py <draft-dir> --check <V59>` reported 58 transitions and 0 problems.
- `void_registry.py` reported 54 antecedents and 20 §6.1 rows with exit 0.
- `prereg_lint.py` exited 0 with exactly 96 legacy-citation advisories and 0 blocking findings; per the brief, those advisories are not reported as unresolved.
- `refusal_vocabulary_check.py` produced the designed R05 state and its self-test passed 7 controls with 0 failures. F4 concerns what else the tool continues to enforce, not whether R05 fires.

## Evidence ledger and scope

Read in content: the V59 brief; the complete V59 draft; `ref/RAISE_SITE_CLASSIFICATION.md`; the relevant `successor_ref_v9.py` schema, receipt, planner, calibration, decision, and guard regions; `tools/refusal_vocabulary_check.py`; `ANSWER_RECEIPT_UNKNOWN_SLOT_AND_V9.md`; KIMI’s V11 report; and the predecessor GPT56 V56 report for repair-state control. Executed: subject/reference/tool SHA-256 checks; direct import and unknown-slot receipt reproduction; independent `SLOT_SCHEMA` and AST/table counts; a tree-wide Python search for `receipt_strict`; prereg lint; prereg counts; the correctly invoked trace check; VOID-registry check; refusal-vocabulary check and self-test. I did not read real χ values or `/Users/duhokim/NebulaMindData/`. No draft, reference, checker, or project file was modified; the only write made by this seat is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V59
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §0 lines 72–100; §7 line 768; §11 lines 982–986 | BS-7p still names permissive receipt(), while the universal strict-constructor rule is impossible for §6.1 producers of non-slot receipts.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 574–576; §7 line 765; §11 lines 987–1026 | BS-3g is classified under a pinned authenticated non-χ schema even though it is absent from the pinned SLOT_SCHEMA and its producer/verifier are unbound.
F3 | MEDIUM | REPAIR-REQUIRED | §11 lines 991–1020 | Fixed-width scalar types do not prevent per-object or covert object-indexed values, and the nine-field schema binds no input sample or perturbation manifest.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 577–585; Row B line 601; refusal checker lines 4–24, 46–65, 95–118 | The prose suspends the eight codes, but the live schema language and checker still enforce that exact set and no-catch-all policy.
F5 | MEDIUM | REPAIR-REQUIRED | §6.1 line 585 | The claimed corrected refusal-checker digest fd6d6d7e… does not match the on-disk tool digest c2ccebbcb4730944….
F6 | MEDIUM | REPAIR-REQUIRED | §5 lines 498–523; pinned reference lines 373–399 | Varying every formal argument can miss global/imported/filesystem state that controls reachability, making the unreachability evidence bar vacuous for zero-argument guards.
F7 | MEDIUM | REPAIR-REQUIRED | §5 lines 496, 524; raise ledger lines 9–16, 110–114 | The draft says NUMERICAL 21 while the live table says 20, its header still says 22→18, and epsilon_hat’s supplied-argument guard is misclassified NUMERICAL.
<!-- END FINDINGS-BLOCK -->