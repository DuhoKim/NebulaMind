# V43 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V43 bytes match the required SHA-256. The five-step rerun allowance itself is gone: I found no surviving computation-attempt cap, seed schedule, attempt log, or permission to re-execute Stage C inside the same run. But the deletion does not finish the one-outcome repair. A pre-unblinding non-finite/degenerate Stage-C computation still satisfies the new `INCONCLUSIVE-BY-COMPUTATION` rule while Row J still assigns **any** locked Stage-C FAIL to `INCONCLUSIVE-BY-POWER`; the normative runner implements only the latter and the code-side inventory does not name the former. Separately, the BS-3g row still describes an older three-way completeness fork as awaiting the principal even though the cited current question records that option (b) was already selected and only the sign-vector mapping remains open.

## Subject identity

- Required SHA-256: `7b2e9a701c38c57094b23b0dcb9173985c6a986bf99de6f31af8e3200f23dfbd`.
- Recomputed before reading the draft: `7b2e9a701c38c57094b23b0dcb9173985c6a986bf99de6f31af8e3200f23dfbd` — exact match.
- The V42→V43 byte diff changes the title, §5's computation procedure, §7.1's description of that procedure, and §10's current-transition row. It removes all five rerun steps rather than editing them in place.

## Findings

### 1. HIGH — REPAIR REQUIRED — the terminal computation route still overlaps Row J's terminal power route and has no named implementation path

Section 5 says the lifecycle registry emits exactly one outcome per run (line 488). It assigns any pre-unblinding permutation/statistic/protocol computation returning non-finite or degenerate to `INCONCLUSIVE-BY-COMPUTATION` (line 492), except for the now-explicit calibration precedence. That terminal rule does remove the old same-run continuation defect.

The Row-J branch was not changed. Row J still says **“Any locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts the run”**, with continuation after a Stage-C FAIL itself voiding the run (line 564); §4 also states the unqualified `FAIL → INCONCLUSIVE-BY-POWER` rule (line 476). A non-finite or degenerate Stage-C permutation/statistic/protocol computation is not excluded from those universal FAIL clauses. The examples in Row J—fewer than 962 successes and a refuted/nonconservative self-check—are introduced by “explicitly including,” not by an exhaustive “only,” so they do not carve the computation failure out. V43 therefore still assigns two terminal run outcomes to the same reachable pre-unblinding event. Deleting the retry resolves continuation but not classification.

The executable seam confirms rather than arbitrates the conflict. Line 498 candidly says the normative `run_production_verdict()` returns only numeric outcomes and its two `INCONCLUSIVE-BY-POWER` branches. Its “Unresolved required implementation” list names the calibration guard, Row-I emission, per-attempt adequacy emission and VOID conversion, but not a producer/conversion for `INCONCLUSIVE-BY-COMPUTATION`; §11 likewise has no computation-outcome implementation item or fixture. Thus “the specific code governs” cannot currently choose this overlap, and the planned atomic code revision can satisfy every named §11 item while still omitting the new terminal route.

Repair requires an explicit ordered Row-J branch: pre-unblinding numerical non-finite/degenerate failure (outside calibration) must be excluded from ordinary Stage-C POWER FAIL, emit only `INCONCLUSIVE-BY-COMPUTATION`, and halt. Name its producer/conversion, receipt fields, implementation work, and negative fixtures in §11 so the one-outcome claim is executable rather than prose-only.

### 2. LOW — REPAIR REQUIRED — the BS-3g row cites a superseded open fork instead of the current unresolved mapping

The BS-3g row says the control remains UNFILLED because its completeness semantics are still a three-way choice—hold observed `p` fixed, freeze a joint counterfactual, or withdraw the gate—and that “the choice is with the principal,” citing `OPEN_QUESTION_T_COMPLETENESS.md` (line 719).

The newer cited evidence says otherwise. `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` lines 3–6 records that the principal already ruled the control a real gate and selected option (b), and lines 8–19 says `gain_counterfactual_path.py` now carries a supplied sign vector through the real joint `(A,p)` machinery but refuses to run without a frozen mapping. Its lines 67–71 identify that mapping—not the old option-(a)/(b)/(c) fork—as the current blocker. Section 11 line 920 points to this newer file, so V43 contradicts itself about what remains undecided.

This does not authorize choosing the mapping and does not weaken the BS-6 block, but it makes the prerequisite inventory inaccurate. Repair only the status: option (b) is selected; the joint path exists and refuses without a mapping; the mapping remains with the principal; BS-3g remains DESIGN/UNFILLED and blocks BS-6.

## Targeted attacks that held

- **Rerun deletion:** held except for Finding 1's surviving outcome-classification seam. Full-text searches found no remaining same-run permission, attempt cap, computation-attempt schema, attempt log, or random-address schedule. The remaining “retry” in §2.7 concerns BS-2a instrument/acceptance semantics; “per-attempt” in §5 concerns Row-P measurement attempts; Stage-P reruns concern the still-unfilled planning gate. None reopens V40's Stage-C computation rerun.
- **BS-3g closed-list propagation:** held. Independent parsing found all 16 Class-P IDs, including BS-3g, in §6.1's exhaustive slot-receipt list. Section 11 now explicitly requires a BS-3g `SLOT_SCHEMA` entry, producer, and independent verifier. The current edge is still expressly not receiptable because those are not specified or built, but the document labels the slot DESIGN/UNFILLED, blocks BS-6, and says exactly that at line 920; this is honest unfinished work rather than a separate hidden bypass. Finding 2 concerns the stale description of what must be designed.
- **V42 citation correction:** held. `PREREG_TEXT_V11_KIMI.md` F7 is the Stage-P finding: it quotes the exact-null harness as not implemented in the §0-pinned file and then establishes that the receipt actually names v7 rather than v9. That supports the passage's code/prose split. F4 is the access/custody finding and would not support it.
- **VOID misconduct phases:** held. Section 5 lines 495–496 keep forbidden acts and protocol/digest deviation at `Any`; §7.1 rows `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION` also remain `Any`. Only numerical non-finite/degenerate failures are `Post-unblinding` there.
- **Counts:** held. `tools/prereg_counts.py` reports 16 Class P / 8 Class E and says the prose matches. No live inventory sentence assumes 15/8.
- **Named checkers:** held. `prereg_trace.py --check` reports 42 transitions / 0 problems; `void_registry.py --self-test` reports 6 controls / 0 failures; `prereg_lint.py` exits 0 with 96 `repair-citation-legacy` advisories and 0 blocking findings. I did not convert the permanent option-D legacy advisories into findings.
- **Pinned bytes spot-check:** held. Live hashes match the draft for `successor_ref_v9.py` (`6a9abbbd…c148`), `closure_worker_v9.py` (`28f8e1f9…5959`), `gain_gradient_estimator.py` (`e2270297…27fd`), and `verify_mu_gamma.py` (`e33d9275…6d04`).

## Evidence ledger and limits

Read as content: `gates/BRIEF_V43_REVIEW.md` first; the complete 921-line V43 draft only after hash verification; exact V42→V43 diff; both V40 whole-review reports; `gates/PREREG_TEXT_V11_KIMI.md` F7; `OPEN_QUESTION_T_COMPLETENESS.md`; `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`; relevant `successor_ref_v9.py` outcome/RNG behavior; and the four checker sources.

Executed: SHA-256 verification; exact V42→V43 diff; full-text searches for rerun/retry/attempt/outcome language and universal negatives; independent Class-P-to-§6.1 receipt-list set comparison; live hashes for the named reference/gain files; `prereg_counts.py`; `prereg_trace.py --check`; `void_registry.py --self-test`; `prereg_lint.py --gates`; and repository status before the report write.

I did not read image data, run inference, execute Stage P/C, unblind, fill a slot, choose the gain mapping, alter frozen code, modify the draft, or modify any file outside this report. The repository had extensive pre-existing unrelated modifications and untracked files; `gates/V43_WHOLE_REVIEW_GPT56.md` was already present and was not read. The only intended write from this seat is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V43
VERDICT: NOT CLEAR
COUNT: 2
F1 | HIGH | REPAIR-REQUIRED | §5 lines 488–498; §6.1 Row J line 564; §11 lines 910–921 | The terminal computation route still overlaps Row J's terminal POWER-FAIL route and has no named implementation path.
F2 | LOW | REPAIR-REQUIRED | §7 line 719; §11 line 920 | BS-3g still presents the superseded three-way completeness fork although the principal selected the joint path and only its sign-vector mapping remains open.
<!-- END FINDINGS-BLOCK -->