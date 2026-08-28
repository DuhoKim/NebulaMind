# V21 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** V21 correctly repairs V20's false present-tense runner-guard sentence and now states that `VOID` reverse reachability is unresolved. It also adds a textual `VOID converter → BS-6` edge. However, the adjacent §7 inventory was not updated: the table now contains 15 class-P rows and three DESIGN rows while line 672 still asserts 14 and names only two DESIGN slots. More importantly, the new `VOID` row has no producer, schema, code symbol, gate, or mechanically closed fixture-coverage contract, so the phrase “branch-complete fixtures” cannot make an incomplete fixture set fail. The dependency is present as prose but is not yet an enforceable gate. The unresolved implementation inventory in §5 also still compresses three explicitly unimplemented guards into the undefined word “accounting” rather than naming them.

V21 can legitimately be an honest unfinished programme, but this revision is not yet a correct preregistration draft because it contains a mechanically false slot inventory and does not specify a receiptably enforceable form of its newly added pre-BS-6 dependency.

## 1. Subject identity — verified before opening

I first compared the live bytes of `../PREREG_SUCCESSOR_DRAFT_V21_20260827.md` with the brief's expected SHA-256 `8386d5f0b3cdc8ed4161545dbcf2f8e4898c9c68942ddfc117b3103ef6ea10e5`. `shasum -a 256` returned exactly:

`8386d5f0b3cdc8ed4161545dbcf2f8e4898c9c68942ddfc117b3103ef6ea10e5  ../PREREG_SUCCESSOR_DRAFT_V21_20260827.md`

Result: **MATCH**. I opened V21 only after that comparison.

I separately compared the live reference-code bytes with §0's pins. `successor_ref_v9.py` returned `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` returned `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`. Both are exact matches.

The V20 comparison pin in V21's banner also held: live V20 returned `607df3dd5b022a299162dac501b9c5766dda87bac8b3ba1cea11a105efa00261`.

## 2. Numbered findings

### Finding 1 — HIGH / BLOCKING — §7 lines 664–680 and §10 line 814: the new dependency row makes the adjacent count, DESIGN inventory, and lint assertion false

**What I compared.** I parsed the markdown rows between “Class P — freeze prerequisites” and “Class E — execution gates,” excluding the header/separator. V20 returned 14 class-P rows. V21 returned 15, because line 680 adds the `VOID` converter. The same parse returned three rows explicitly classified DESIGN: BS-2a, BS-2k, and the `VOID` converter.

**Why it fails.** Line 672 still says:

- “BS-2a and BS-2k are DESIGN slots”;
- “One of fourteen class-P slots is filled”; and
- “the prose count equals the parsed table count and the DESIGN inventory matches the VALUE/DESIGN classification.”

All three claims became false in the sentence immediately above the changed table region. The correct count is 15, one filled; the DESIGN inventory has three entries. This is exactly the adjacent-sentence defect the brief required this pass to attack.

The defect also weakens §10 line 814's claim that the change “made it a pre-BS-6 dependency in §7.” A literal `blocks | BS-6` edge exists, but the surrounding class-P inventory and asserted lint invariant no longer describe the graph that was actually written.

**Smallest sufficient repair.** Change line 672 to name BS-2a, BS-2k, and the `VOID` converter as DESIGN slots; change 14 to 15; rerun the parser/linter and record the returned count. Keep one of 15 filled (BS-2m).

### Finding 2 — HIGH / BLOCKING — §6.1 Clause 10 line 567, §7 line 680, §11 line 833: the `VOID` dependency is textual but not gate-enforceable, and “branch-complete fixtures” cannot fail an incomplete set

**What held.** V21 now says directly that `VOID` reverse reachability is unresolved, Clause 10 is not executable, and BS-6/first image byte remain blocked. Section 7 line 680 adds a class-P DESIGN row whose `blocks` cell is BS-6. Section 11 line 833 repeats that this is a pre-BS-6 dependency. Thus the dependency is no longer absent from the prose graph.

**Why it still fails.** The newly added row has producer `—`, code symbol `—`, no schema, no receipt fields, no gate identity, and no completion/verification rule. Section 11 merely requires a converter and “branch-complete fixtures.” Neither location defines:

1. the finite canonical manifest of void antecedents/branches to be covered;
2. a stable branch identifier or expected branch count;
3. a fixture-to-branch coverage record;
4. set equality between expected and exercised branches; or
5. the failure effect when one branch is absent from the fixtures.

“Every enumerated void antecedent” does not supply that closure. Section 5 line 472 gives three broad classes, while the §6.1 table contains many distinct row-level void conditions and §6.3 adds the post-first-real-χ mutation rule. A fixture author can omit a row-level branch and still call the remaining fixtures “branch-complete”; the document gives the gate no mechanical oracle by which to reject that claim.

This answers the brief's narrow question: **the pre-BS-6 dependency is stated and linked, but not actually enforceable as a gate.** It blocks forever as an unfilled prose DESIGN row, yet does not define how a future implementation becomes validly filled. That is safe by immobility, not a receiptable prerequisite contract.

**Smallest sufficient repair.** Give the converter DESIGN slot a canonical antecedent-manifest schema, stable IDs for every §5/§6 void branch, a named producer-of-record for the future gated revision, a code/contract digest slot, and a fixture coverage receipt requiring exact set equality between manifest IDs and exercised IDs. Specify that missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate and leaves BS-6 blocked.

### Finding 3 — MEDIUM / BLOCKING — §5 lines 462–474: the extended unresolved list still omits the exact final-mask/ledger/adequacy guards declared unimplemented immediately above it

**What I compared.** V21 line 462 declares five required-but-unimplemented runner capabilities: (1) BS-L verification, (2) authenticated one-use unblinding-receipt verification, (3) exact final-mask binding, (4) post-unblinding ledger recomputation, and (5) refusal when the adequacy tree emits `INCONCLUSIVE`. Line 474 adds only the first two by name. It retains the generic word “accounting,” plus “post-unblinding calibration return,” but neither phrase specifies the final-mask digest binding, the ledger recomputation, or the mandatory adequacy-tree pre-statistic refusal.

The source comparison confirms that these are real missing guards rather than wording nits. The AST of pinned `run_production_verdict()` lines 1591–1625 returned arguments `mask`, `cal`, `authorization_path`, `authorization_sha256`, `n_receipts`, `n_parent`, and `stage_c_receipt`; its call set contains the existing environment/authorization/sample/sealed-mask checks, `adjudicate_path`, `perm_record`, and `_decide_from`, but no lock, unblinding, final-mask, ledger, or adequacy verifier. Whole-source counts returned zero for `verify_lock`, `unblind`, and `BS-L`.

The repair is honest at line 462, so this is not V20's old false capability claim. The remaining problem is the brief's requested completeness check: the nearby “Unresolved required implementation” inventory is not exact enough to preserve all of line 462's required guards.

**Smallest sufficient repair.** After the two newly named verification items at line 474, explicitly add: exact final-mask binding verification; post-unblinding ledger recomputation; and adequacy-tree `INCONCLUSIVE` refusal before any statistic. If “accounting” is intended to include them, replace it with these exact terms rather than relying on an undefined umbrella.

## 3. Changed-line and neighbour audit

I compared V20 and V21 with `difflib.SequenceMatcher(autojunk=False)`. It returned 9 non-equal hunks, 7 old changed lines and 18 new changed lines: **25 total changed lines**, matching the brief. I read at least four context lines on both sides of every hunk.

Results by hunk:

1. Banner/title and V20 pin: accurate; the live V20 hash matched.
2. §5 guard sentence: correctly changed from false present tense to required-but-unimplemented.
3. §5 unresolved list: the two named additions are true, but Finding 3 applies.
4. Clause 10: correctly states unresolved reverse reachability and non-executability.
5. §7 new row: adds the intended textual block, but the immediately preceding inventory is now false (Finding 1), and the row is not fillably enforceable (Finding 2).
6. V19→V20 trace repair: accurately narrows “producer” to validator/authenticated outcome wording.
7. V20→V21 trace insertion: byte-accurate about what text was added; its substantive enforcement claim is limited by Findings 1–2.
8. §11 insertion: accurately lists future work, but its fixture contract is under-specified (Finding 2).
9. No unrelated body change was found.

A targeted sweep of §5 and §11 found no surviving V20-style assertion that the new lock/unblinding guards are already implemented. Section 5 now labels them unimplemented, and §11 uses future imperative language. The remaining inventory problem is Finding 3, not a present-tense implementation claim.

## 4. Clause 10 audit across §§0–11, both directions

I read row branch → lifecycle outcome and lifecycle outcome → named branch/phase.

- Numeric outcomes reverse-resolve to `_decide_from` at P8.
- `INCONCLUSIVE-BY-POWER` reverse-resolves to Row J and the production runner's Stage-C and `N_eq` guards.
- Calibration, Row-I, accounting, and per-attempt outcomes are explicitly identified as required but unimplemented; the prose maps their intended phases and consequences.
- `VOID` forward antecedents are named in §5, the row-level “what voids the run” cells, Clause 5, and §6.3's post-first-real-χ mutation rule.
- V21 now expressly says `VOID` reverse reachability is unresolved and Clause 10 is not executable. This is the intended honest state.
- Reverse executable reachability remains absent in pinned source: whole-source search returned zero `VOID` occurrences. V21 does not conceal that absence.

The Clause-10 status sentence is therefore honest. The failure is narrower: the future gate contract does not define a branch-coverage oracle capable of closing that admitted state.

## 5. Threshold audit — value, phase, and failure effect

The threshold-bearing branches held under comparison with the pinned source and the prose lifecycle:

- Selection floor: `N_eq = 3·L_ret ≥ 100,000`; in production, source lines 1613–1616 use `< NEQ_MIN` as the failure branch and return `INCONCLUSIVE-BY-POWER` before the statistic. Equality passes.
- Numeric reproduction at P8: `p < 0.001`, Longo sign, `|Â_L−0.0408| ≤ 3σ_comb`, and `Â_L ≥ 3.09·σ_ours(a_LB)` → `REPRODUCED-LONGO`.
- Numeric rejection at P8: `p > 0.05` and `|Â_L|+3σ_ours < 0.0408` → `REJECTED-AT-LONGO-AMPLITUDE`; complement → numeric `INCONCLUSIVE`.
- Calibration at P5: any `a_LB_b < 0.85` halts pre-unblinding with the required `INCONCLUSIVE-BY-CALIBRATION`; only the complement reaches spread selection. Spread `≤ 0.03` selects scalar, `> 0.03` profile; profile is not failure. The conversion remains disclosed as unimplemented.
- Stage P/C: exactly 1,000 trials; at least 962 successes passes. Fewer than 962, or `refuted`/`nonconservative`, fails closed; at Stage C the required effect is `INCONCLUSIVE-BY-POWER` before BS-L.
- Monte Carlo: production `n_perm = 100,000`; Stage-P exact measurement uses 20,000 per trial and reports its `5.00e-05` resolution floor as a lower bound rather than a measured smaller value.
- Row I missing/non-finite allocated output halts before BS-8f with `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`.
- Row P at P8 maps zero/duplicate/orphan/malformed to the four accounting outcomes. Any absent/non-finite/low-confidence removal maps to run-level `INCONCLUSIVE-BY-CALIBRATION`, with no Stage-C rerun.
- Confidence threshold value remains deliberately unfilled in refused BS-2a; the document binds its phase before any image byte and voids a post-inference change.

I found no new threshold inversion, equality gap, phase ambiguity, or unstated failure effect beyond the non-executable conversions already disclosed and Findings 2–3.

## 6. §10 repair-trace audit — all five adjacent entries

I compared each adjacent version with `difflib.SequenceMatcher(autojunk=False)` and inspected the returned hunks.

1. **V16→V17:** 14 hunks; 27 old and 60 new changed lines. The trace accurately describes the §6.3 bodies/Row-P citation, §4 calibration additions, Class E 7→8 change while Class P remained 14, evidence narrowing, 0.03 addition, and partial repairs.
2. **V17→V18:** 13 hunks; 15 old and 35 new changed lines. The trace accurately describes sole BS-2a threshold ownership, reason-(d) removal, calibration-before-spread precedence, registry split/Row-I abort, chronology repair, and trace insertion.
3. **V18→V19:** 8 hunks; 11 old and 19 new changed lines. The trace accurately describes the lifecycle producer rewrite, narrowed runner claim, non-finite split, and earlier trace repairs.
4. **V19→V20:** 8 hunks; 7 old and 19 new changed lines. The corrected V21 row accurately says the changed §5/§11 wording names a required aggregate validator and authenticated outcome, not an implemented producer.
5. **V20→V21:** 9 hunks; 7 old and 18 new changed lines, 25 total. The trace accurately lists the bytes added. Its statement that §7 “made” an enforceable pre-BS-6 dependency is only syntactically true: the row points to BS-6, but Findings 1–2 show the surrounding inventory is false and no fill/coverage gate is specified.

Thus the first four trace entries are accurate after V21's correction. The fifth is an accurate change log but overstates the operational completeness of the §7 dependency.

## 7. Failed attacks / points that held

- **Digest attack failed:** V21, V20, and both §0 code pins matched their claimed hashes.
- **Changed-line-count attack failed:** the independent V20→V21 comparison returned exactly 25 total changed lines under the same non-equal-line convention used by the brief.
- **Runner-return attack failed:** source lines 1591–1625 return only two direct `INCONCLUSIVE-BY-POWER` branches plus `_decide_from`; helper lines 1561–1588 assign exactly `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, and `INCONCLUSIVE`. V21 line 474's narrow return-value sentence is true.
- **Guard-honesty attack failed:** V21 no longer claims lock/unblinding/final-mask/adequacy guards are implemented.
- **Clause-10 disclosure attack failed:** V21 plainly states that `VOID` reverse reachability is unresolved and Clause 10 is not executable.
- **Second-reason attack failed at the prose-graph level:** BS-6 is now blocked for a separately named `VOID` reason in addition to BS-2a.
- **Trace-E attack failed:** V21 correctly repairs the V19→V20 aggregate-validation wording.
- **Threshold attack failed:** no new value/direction/phase mismatch was found.

## 8. Testimony / unverified assertions

I did not independently reconstruct fold timestamps, historical authorization, prior verdict timestamps, Longo source quotations, real-geometry measurements, Stage-P measurement outputs, closure reproduction counts, or fixture transcript claims. They remain **Testimony** for this review.

I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, execute a real-data run, inspect secrets, mutate the draft or reference code, or perform any git mutation.

## 9. Evidence ledger and constraints

Content read: `BRIEF_V21_WHOLE_REVIEW.md`; all 833 lines of V21; the full V20 comparison region and all of §10/§11; pinned `successor_ref_v9.py` lines 1540–1639; prior V20 reports as historical inputs-to-attack, not ground truth. Mechanical comparisons: SHA-256 for V19/V20/V21 and both §0 code files; complete V20→V21 diff with neighbours; AST signature/call/return extraction for `run_production_verdict()` and `_decide_from()`; source occurrence counts; parsed §7 P/E row counts for V16–V21; and five adjacent-version line comparisons for §10.

Only this required report file was written. No network, data fetch, source-document edit, code edit, git write, or access to `/Users/duhokim/NebulaMindData/` occurred.

**NOT CLEAR**