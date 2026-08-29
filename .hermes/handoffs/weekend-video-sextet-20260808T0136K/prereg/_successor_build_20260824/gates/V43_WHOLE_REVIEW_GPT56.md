# V43 whole-document referee — GPT56

## Verdict

**NOT CLEAR.** The dispatched bytes match the required SHA-256, the five-step rerun allowance is gone, aggregate-calibration precedence is now explicit, the class inventory is 16/8, the misconduct conditions remain at `Any`, and `KIMI-V11 F7` is the correct Stage-P citation. But deleting the retry did not dissolve all of V40 F1: a pre-unblinding non-finite/degenerate Stage-C computation is still assigned two terminal outcomes by §5 and Row J, and no row is named as the producer of the computation outcome. Two smaller whole-document defects remain: §7 gives a stale account of the BS-3g design decision that the cited current sidecar says the principal already made, and §10 writes a current-transition row that its own contract and self-reference explanation say must not exist in-band.

## Findings

### 1. HIGH / REPAIR-REQUIRED — the terminal computation halt still collides with Row J's universal Stage-C-failure branch

**Sections / lines.** §5 lines 488–493; §6.1 Row J line 564; clause 10 line 600.

V43 line 492 assigns every pre-unblinding non-finite or degenerate `permutation, statistic or protocol` computation (other than aggregate calibration) to the terminal run outcome `INCONCLUSIVE-BY-COMPUTATION`. Stage C is a pre-unblinding permutation/statistic/protocol computation. Row J nevertheless still says **“Any locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts the run”**, explicitly gives two examples with **“including”** rather than an exhaustive restriction, says continuing after any Stage-C FAIL voids, and makes the complementary PASS branches the sole route to BS-5f.

The deletion removes the retry contradiction but not this classification contradiction. A non-finite Stage-C permutation can satisfy both rules: §5 says COMPUTATION; Row J says POWER. Nothing in Row J carves computation failures out of “Any ... FAIL,” and §5's statement that the lifecycle registry names the producing phase/process for each category is also false for COMPUTATION: Row J's emission column names only BS-5f and its failure text names POWER. The operator still has to choose the run outcome for the same event, violating clause 10's single-termination rule.

The repair is narrow: give Row J an ordered branch in which invalid calibration aggregates map to CALIBRATION, pre-unblinding Stage-C numerical failures map to COMPUTATION, ordinary finite Stage-C failure maps to POWER, and PASS alone emits BS-5f. Name Row J (or another exact process) as the authenticated producer of the computation outcome and align its VOID antecedents with that partition.

### 2. MEDIUM / REPAIR-REQUIRED — §7 describes the wrong remaining BS-3g design decision

**Section / line.** §7 BS-3g row, line 719; §11 line 920; referenced `OPEN_QUESTION_T_COMPLETENESS.md` lines 28–55 and `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` lines 3–6, 67–71.

The §7 row says the control's completeness semantics remain an open three-way fork—hold observed `p` fixed, build a joint counterfactual, or withdraw the rule—and assigns that fork to `OPEN_QUESTION_T_COMPLETENESS.md`. The current referenced evidence says otherwise. `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` records that the principal already selected option (b), a real joint-counterfactual gate, and that the remaining decision is specifically the γ-to-counterfactual-sign/calibration mapping. Section 11 itself points to that newer mapping question.

This is not a demand to resolve the deliberately open mapping. It is a document-status defect: §7, the binding slot inventory, tells a future filler that three semantics remain available after one was already ruled. Because the choice changes what BS-3g means, the stale description reopens two principal-rejected paths on the very row that is supposed to block BS-6. Replace the three-way-fork language with the settled option-(b) requirement and name only the still-open mapping contract.

### 3. LOW / REPAIR-REQUIRED — §10 contains the current transition despite its own digest and self-reference rules

**Section / lines.** §10 lines 848–854, 891, and 903.

The checker contract says the current transition is checked in the external `FINDINGS_MAP.md`, that every written in-band row carries its own result digest, and that a draft **cannot describe the transition that created it** because doing so changes its own bytes. V43 nevertheless contains a `V42 → V43` row and substitutes `(this revision)` for the required result digest. The row is exactly the construct line 903 says belongs only in the next draft.

`prereg_trace.py --check` exits 0 because its current-transition branch consults the sidecar and does not reject an extra in-band current row; that successful run therefore does not settle the prose contract. Delete the V42→V43 row from V43; keep its mapping in `FINDINGS_MAP.md`, and let V44 carry the digest-pinned historical row if V44 exists.

## Targeted attacks that held

- **Subject identity held.** SHA-256 was recomputed before reading the draft: `7b2e9a701c38c57094b23b0dcb9173985c6a986bf99de6f31af8e3200f23dfbd`, exact match.
- **The retry deletion itself held.** The V42→V43 diff removes the five-step same-run allowance, attempt log, attempt cap, and retry permission. Searches found no surviving same-run Stage-C retry clause; the remaining “rerun” occurrences concern Stage P, Branch A, fixtures, or historical explanation. Finding 1 is the surviving outcome collision, not a demand to restore retry machinery.
- **Calibration precedence held.** §5 now explicitly excludes aggregate calibration failures from COMPUTATION and routes them to CALIBRATION.
- **BS-3g's receipt-list omission is repaired at the text-accounting level.** §6.1's exhaustive non-χ-bearing `SLOT_SCHEMA` list now includes BS-3g, and §11 explicitly admits that without a schema entry, producer, and independent verifier the edge remains declared but not receiptable. I do not treat that honest unfinished implementation as a new finding. Finding 2 concerns the stale substantive design status in the binding §7 row.
- **V42 citation correction held.** `PREREG_TEXT_V11_KIMI.md` F7 states that the exact-null Stage P is not implemented in the file §0 pins; F4 is the access/custody finding. `KIMI-V11 F7` supports the passage it now cites.
- **Misconduct phases held.** §5 lines 495–496 keep forbidden acts and protocol/digest deviation at `Any`; registry rows `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION` all remain `Any`. Only numerical non-finite/degenerate antecedents are post-unblinding.
- **Inventory held.** Independent parser and `tools/prereg_counts.py` both return 16 class-P and 8 class-E rows. The only 15/8 occurrence is the historical V36→V37 transition record.
- **Named checker posture held.** Counts: 16/8, prose matched. Trace: 42 transitions, 0 reported problems. VOID registry: 54 antecedents, 20 row names, digest `a4d1d745b2ed33bc0e01dd39b845f88daffdc542d2bdd98d5e122ab7dd443d37`; self-test 6 controls, 0 failures. Lint exits 0 with 96 legacy advisories and 0 blocking; lint self-test 8 controls, 0 failures. Per the principal's option-D ruling, the 96 advisories are not findings.

## Evidence ledger and custody

Read as content: `gates/BRIEF_V43_REVIEW.md`; all 921 lines of V43; V42→V43 byte diff; `gates/V40_WHOLE_REVIEW_GPT56.md`; `gates/V40_WHOLE_REVIEW_CODEX.md`; `gates/PREREG_TEXT_V11_KIMI.md`; `gates/FINDINGS_MAP.md`; `OPEN_QUESTION_T_COMPLETENESS.md`; `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`; `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`; and the relevant current-transition logic/comments in `tools/prereg_trace.py` plus citation behavior in `tools/prereg_lint.py`.

Executed: subject SHA-256; referenced-evidence SHA-256 inventory; exact V42→V43 diff; targeted searches over rerun/retry/attempt language, class-count language, universal-negative language, misconduct phases, and referenced filenames; `prereg_counts.py`; `prereg_trace.py --check`; `void_registry.py` normal and self-test; `prereg_lint.py` normal and self-test; and repository status before the report write.

I did not read image data, run inference, execute Stage P or Stage C, unblind, fill a slot, alter frozen code, modify the draft, or modify any file outside this report. Pre-existing repository dirt was left untouched.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V43
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §5 lines 488–493; §6.1 Row J line 564; clause 10 line 600 | A pre-unblinding Stage-C numerical failure still maps to both COMPUTATION and POWER, with no named computation-outcome producer.
F2 | MEDIUM | REPAIR-REQUIRED | §7 line 719; §11 line 920 | The BS-3g row reopens a three-way semantics fork after the cited current sidecar records option (b) as settled, instead of naming only the open γ-to-sign/calibration mapping.
F3 | LOW | REPAIR-REQUIRED | §10 lines 848–854, 891, 903 | V43 writes its own V42→V43 transition with no result digest despite saying the current transition is sidecar-only and cannot appear in-band.
<!-- END FINDINGS-BLOCK -->