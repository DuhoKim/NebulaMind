# V44 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V44 bytes match the required SHA-256. The V43 rerun deletion remains complete, the V42 KIMI citation is now correct, the class inventory is 16/8, the misconduct antecedents remain at `Any`, and the V43 self-transition is now a valid historical row with V43's digest. But V44's principal repair is still prose-only: it calls `INCONCLUSIVE-BY-COMPUTATION` residual while the normative Row J continues to send **any** locked Stage-C FAIL to `INCONCLUSIVE-BY-POWER`, and §11 orders the computation handler after that universal power guard. The same pre-unblinding Stage-C numerical failure can therefore still be classified as POWER, making COMPUTATION unreachable on that path, or be classified as COMPUTATION by §5. The document also leaves a stale statement in §11 that the BS-3g “completeness semantics” remain open after §7 and the cited sidecar say those semantics are settled and only the γ-to-sign/calibration mapping remains open.

## Subject identity

- Required SHA-256: `4faa2564ba093ae4eccbd3f868f62782833b2a09c56ec8282945b5fd46d65aa2`.
- Recomputed before reading the draft: `4faa2564ba093ae4eccbd3f868f62782833b2a09c56ec8282945b5fd46d65aa2` — exact match.
- The exact V43→V44 diff changes only the title, §5's computation-route prose, the BS-3g row, the V42→V43 historical digest row, and one new §11 computation-producer item.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the computation route is not residual under the normative Row-J partition

V44 §5 lines 491–492 now names Row J and the production runner as producers and says `INCONCLUSIVE-BY-COMPUTATION` fires only where neither POWER nor CALIBRATION applies. That is a declaration of precedence, not a repair of the conflicting branch. The normative lifecycle table was not changed: Row J line 564 still says **“Any locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER`”**, explicitly *including* two examples rather than restricting POWER to an exhaustive finite-failure set. Section 4 line 476 likewise retains the unqualified `FAIL → INCONCLUSIVE-BY-POWER` rule. A non-finite or degenerate Stage-C permutation/statistic/protocol computation is a locked Stage-C failure, so it remains claimed by POWER while §5 claims the same event for COMPUTATION.

The new §11 item makes the collision worse rather than resolving it: line 921 requires the computation outcome to be evaluated **after the power and calibration guards** and makes it unreachable whenever either prior guard “has fired.” Under Row J's universal power-failure clause, the power guard fires on the very Stage-C numerical failure COMPUTATION is supposed to receive. No criterion distinguishes an “ordinary finite Stage-C power failure” from a “Stage-C numerical failure” before applying the power guard. Thus V44 offers two incompatible readings: (a) obey Row J and return POWER first, making COMPUTATION unreachable for Stage-C numerical failures; or (b) obey §5 and carve those failures out of “Any locked Stage-C FAIL,” a carve-out the normative row never states.

The implementation inventory also remains internally incomplete. Line 498 says the current runner returns only numeric outcomes and two POWER branches and then presents an **“Unresolved required implementation”** list that still omits the COMPUTATION producer. The pinned runner confirms this: `successor_ref_v9.py` lines 1610–1620 returns POWER for a failed Stage-C receipt or low `N_eq`, then raises `RuntimeError` when `perm_record()` throws; it emits no COMPUTATION outcome. Section 11 now names future work, but §5's own exact unresolved-inventory sentence and the normative Row J do not carry it.

Smallest sufficient repair: rewrite Row J and §4 as an ordered, exhaustive partition—invalid calibration aggregate → CALIBRATION; pre-unblinding non-finite/degenerate Stage-C computation → COMPUTATION; ordinary finite Stage-C threshold/self-verification failure → POWER; complementary PASS → BS-5f. Then say the computation check is applied before the ordinary POWER classification (while still after calibration validation), add it to line 498's unresolved inventory, and require negative fixtures proving each event reaches exactly one code.

### F2 — MEDIUM / REPAIR-REQUIRED — §11 still describes the settled BS-3g semantics as open

The repaired BS-3g row at line 719 accurately records the principal's ruling: the executable joint-counterfactual path is selected, holding observed `p` fixed is rejected, withdrawal to a stated limitation is rejected, and **one thing only** remains open—the γ-to-counterfactual-sign-vector and calibration mapping. This matches `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`: lines 3–6 record the real-gate ruling, lines 10–18 describe the built joint path and refusal without a mapping, and lines 67–71 identify the mapping as the remaining blocker. Inspection of `ref/gain_counterfactual_path.py` confirms `evaluate_at(..., mapping=None)` raises `MappingNotFrozen` and that the supplied sign vector is passed through `perm_record()` jointly with calibration and the decision helper.

Section 11 line 920 was not re-derived. It still says the BS-3g receipt's content depends on **“the completeness semantics still open in `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`.”** That is false under the repaired row and the referenced file: the completeness semantics are settled; the modelling mapping is open. Because §11 is the code-side inventory a future revision is to implement, this stale wording can reopen the principal-rejected completeness fork or leave the receipt item deliberately unspecified for the wrong reason.

Repair line 920 to say that the joint-counterfactual completeness semantics are settled and that the receipt content cannot be specified until the separately open γ-to-sign/calibration mapping is preregistered. Do not choose that mapping in this repair.

## Targeted attacks that held

- **Rerun deletion:** held. Full-text searches found no surviving same-run Stage-C rerun permission, attempt cap, seed schedule, or computation-attempt log. Remaining rerun/retry language concerns Branch A, Stage P, BS-2a design, historical measurements, or Row-P measurement attempts. Row P expressly says no discretionary retry and no Stage-C rerun.
- **V42 citation correction:** held. `gates/PREREG_TEXT_V11_KIMI.md` F7 is the Stage-P finding: it states that the exact-null Stage P is not implemented in the §0-pinned file and additionally verifies that the receipt's subject is v7 rather than v9. KIMI F4 is the access/custody finding and would not support this passage.
- **BS-3g closed-list receiptability posture:** held apart from F2's stale status wording. Section 6.1's exhaustive non-χ-bearing slot list includes BS-3g. Section 11 names a `SLOT_SCHEMA` entry, producer, and independent verifier and candidly states that the `blocks BS-6` edge is not yet receiptable. The slot remains DESIGN/UNFILLED and blocks BS-6.
- **V43 historical transition repair:** held. V44 contains `V42 → V43` with V43's real digest `7b2e9a701c38c570`; it contains no V43→V44 row. `prereg_trace.py --check` reports 43 transitions and 0 problems.
- **VOID misconduct phases:** held. Section 5 keeps forbidden acts and protocol/digest deviation at any phase; registry rows `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION` are all `Any`. Only numerical non-finite/degenerate conditions are post-unblinding in the VOID registry. `void_registry.py --self-test` reports 6 controls and 0 failures.
- **Class inventory:** held. `prereg_counts.py` independently reports 16 Class P / 8 Class E and says the prose matches. No live inventory sentence assumes 15/8.
- **Lint posture:** held. `prereg_lint.py` exits 0 with exactly 96 `repair-citation-legacy` advisories and 0 blocking findings. Per the brief's option-D instruction, none is reported as unresolved.
- **Pinned-byte spot checks:** held. Live SHA-256 values match the draft for `successor_ref_v9.py` (`6a9abbbd…c148`), `closure_worker_v9.py` (`28f8e1f9…5959`), `gain_gradient_estimator.py` (`e2270297…27fd`), and `verify_mu_gamma.py` (`e33d9275…6d04`).

## Evidence ledger and limits

Read as content: `gates/BRIEF_V44_REVIEW.md` first; the complete 922-line V44 draft only after hash verification; exact V43→V44 diff; both V43 whole-review reports; `gates/PREREG_TEXT_V11_KIMI.md`; `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`; relevant `successor_ref_v9.py` and `gain_counterfactual_path.py` code; and checker output relevant to counts, trace, VOID coverage, and citation lint.

Executed: subject SHA-256; exact V43→V44 diff; full-text searches for rerun/retry/attempt, open-question, and computation-outcome language; live hashes for the named reference/gain files; `prereg_counts.py`; `prereg_trace.py --check`; `void_registry.py` and its self-test; `prereg_lint.py`; and scoped repository status before writing this report.

I did not read image data, run inference, execute Stage P or Stage C, unblind, fill any slot, choose the gain mapping, alter frozen code, modify the draft, or modify any file outside this report. The report path was clean before this write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V44
VERDICT: NOT CLEAR
COUNT: 2
F1 | HIGH | REPAIR-REQUIRED | §4 line 476; §5 lines 491–498; §6.1 Row J line 564; §11 line 921 | COMPUTATION is still claimed by Row J's universal POWER-failure branch, and evaluating it after that guard makes the purported residual route unreachable on Stage-C numerical failures.
F2 | MEDIUM | REPAIR-REQUIRED | §7 line 719; §11 line 920 | Section 11 still calls BS-3g completeness semantics open although the principal settled the joint path and only the γ-to-sign/calibration mapping remains open.
<!-- END FINDINGS-BLOCK -->