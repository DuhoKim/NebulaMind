# V44 whole-document referee — GPT56

## Verdict

**NOT CLEAR.** The dispatched bytes match the required SHA-256. The V43 same-run rerun deletion remains complete, the V42 `KIMI-V11 F7` citation is correct, the V43 transition now appears in the proper successor draft with V43's digest, the class inventory is 16/8, and the misconduct antecedents remain at `Any`. But the principal V44 repair still does not produce a single-valued Row-J outcome: the normative Stage-C clauses continue to send any Stage-C failure to `INCONCLUSIVE-BY-POWER`, while §5 assigns numerical Stage-C failures to residual `INCONCLUSIVE-BY-COMPUTATION`, and §11's “after the power guard” order makes the latter route unreachable rather than residual. A second stale sentence in §11 still calls the already-settled BS-3g completeness semantics open.

## Findings

### 1. HIGH / REPAIR-REQUIRED — the purported residual computation route is still claimed by POWER and is made unreachable by its implementation order

**Sections / lines.** §4 line 476; §5 lines 491–498; §6.1 Row J line 564; §7.1 line 744; §11 line 921.

V44 changes §5's labels, but not the branch that created the collision. Section 5 lines 491–492 now say that a pre-unblinding non-finite or degenerate Stage-C permutation/statistic/protocol computation emits `INCONCLUSIVE-BY-COMPUTATION`, residual to POWER and CALIBRATION. Row J line 564 still says **“Any locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER`”**; §4 line 476 likewise states without a numerical-failure carve-out, **“FAIL → INCONCLUSIVE-BY-POWER.”** A non-finite or degenerate Stage-C permutation is both the numerical event §5 assigns to COMPUTATION and a Stage-C failure the normative Row-J branch assigns to POWER.

The new §11 item does not enforce residuality. It requires COMPUTATION to be evaluated **after** the power and calibration guards. The calibration-first part is sound, but the universal power branch already claims every Stage-C failure. If the power guard sees the numerical failure, it emits POWER before COMPUTATION is reached; if numerical failure prevents a valid power result, the text supplies no ordered branch that converts that exception before interpreting PASS/FAIL. The claimed residual Stage-C route is therefore either double-valued in prose or unreachable in the prescribed implementation. Section 5 line 496 and §7.1 line 744 additionally summarize all pre-unblinding numerical failures as routing to COMPUTATION, contradicting the new exclusions for calibration and power rather than curing them.

The repair must define one ordered partition, not a fallback label: invalid calibration aggregates → CALIBRATION; Stage-C numerical invalidity detected before interpreting the power result → COMPUTATION; valid finite ordinary Stage-C failure → POWER; PASS alone → BS-5f. Row J, §4, §5, §7.1, and §11 must all state that same partition.

### 2. MEDIUM / REPAIR-REQUIRED — §11 still describes the principal-settled BS-3g completeness semantics as open

**Sections / lines.** §7 BS-3g row line 719; §11 line 920; `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` lines 3–18 and 67–71.

The repaired §7 row is accurate: the principal selected the executable joint-counterfactual path, holding observed `p` fixed is rejected, withdrawal to a limitation is rejected, and the only open issue is the modelling map from γ to the counterfactual accepted-sign vector and calibration. The referenced sidecar confirms exactly that: the joint path is built, ships no mapping, and refuses to run without one.

Section 11 was not re-derived. Line 920 still says the receipt content depends on **“the completeness semantics still open in `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`.”** The completeness semantics are not open; the γ-to-sign/calibration mapping is. Because §11 is the code-side inventory for the future receipt producer and verifier, this stale wording can reopen principal-rejected options or leave the item underspecified for the wrong reason.

Replace only that status statement: the joint-counterfactual completeness semantics are settled, while the receipt fields cannot be fully specified until the separately open γ-to-sign/calibration mapping is preregistered. Do not choose the mapping in this repair.

## Targeted attacks that held

- **Subject identity held.** SHA-256 was recomputed before the draft was read: `4faa2564ba093ae4eccbd3f868f62782833b2a09c56ec8282945b5fd46d65aa2`, exact match.
- **The same-run rerun deletion held.** Searches found no surviving Stage-C retry permission, seed schedule, retry-attempt log, attempt cap, or same-run re-execution allowance. Remaining rerun language concerns Stage P, Branch A, fixtures, or historical explanation. The operator's recourse is a new run under a new preregistration.
- **The V42 citation repair held.** `PREREG_TEXT_V11_KIMI.md` F7 says the exact-null Stage P is not implemented in the file §0 pins; KIMI F4 is the access/custody finding. `KIMI-V11 F7` supports the cited Stage-P passage.
- **The V43 self-transition repair held.** V44 carries the historical V42→V43 row with V43's real digest; V44 does not write a V43→V44 row in-band. `prereg_trace.py --check` reports 43 transitions and 0 problems; its three-control self-test reports 0 failures.
- **Misconduct phases held.** Forbidden acts, protocol deviation, and digest deviation remain `Any` in both §5 and registry rows `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION`. Only numerical non-finite/degenerate failures are post-unblinding VOID antecedents.
- **Inventory held.** `prereg_counts.py` independently returns 16 class-P and 8 class-E rows, with prose matched. The 15/8 occurrence is the historical V36→V37 transition.
- **BS-3g receiptability is not falsely claimed complete.** Section 6.1 now includes BS-3g in the exhaustive non-χ-bearing slot-receipt list, and §11 admits that no schema entry, producer, or independent verifier yet exists. The edge is still not receiptable and BS-6 remains blocked. Finding 2 is the stale description of *which substantive question* remains open, not a demand to fabricate a receipt schema before the mapping is preregistered.
- **Named checker posture held.** VOID registry: 54 antecedents, 20 row names, digest `a4d1d745b2ed33bc0e01dd39b845f88daffdc542d2bdd98d5e122ab7dd443d37`; self-test 6 controls, 0 failures. Lint exits 0 with 96 legacy advisories and 0 blocking findings; lint self-test 8 controls, 0 failures. Per the principal's option-D ruling, the 96 advisories are not reported as unresolved work.

## Evidence ledger and custody

Read as content: `gates/BRIEF_V44_REVIEW.md` first; all 922 lines of V44 only after digest verification; the exact V43→V44 diff; both V43 whole-review reports; `gates/PREREG_TEXT_V11_KIMI.md`; `gates/FINDINGS_MAP.md`; `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`; the relevant `successor_ref_v9.py` Stage-C/power and production-runner code; and the count, trace, VOID-registry, and lint checker sources. A targeted search later surfaced the current CODEX V44 report; it independently concurs on the same two defects, but it was not used as proof for either finding.

Executed read-only: subject SHA-256; exact V43→V44 byte diff; searches over rerun/retry/attempt language, outcome classifications, open-question language, class counts, VOID phases, and universal negatives; `prereg_counts.py`; `prereg_trace.py --check` and self-test; `void_registry.py` normal and self-test; `prereg_lint.py` normal and self-test; and scoped repository status.

I did not run Stage P or Stage C, unblind, fill a slot, alter frozen code, modify the draft, or intentionally modify any file outside this report. Pre-existing repository state and the concurrently produced CODEX report were left untouched.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V44
VERDICT: NOT CLEAR
COUNT: 2
F1 | HIGH | REPAIR-REQUIRED | §4 line 476; §5 lines 491–498; §6.1 Row J line 564; §7.1 line 744; §11 line 921 | Row J still assigns numerical Stage-C failures to POWER, while §5 assigns them to residual COMPUTATION and §11 evaluates COMPUTATION only after the claiming power guard.
F2 | MEDIUM | REPAIR-REQUIRED | §7 line 719; §11 line 920 | Section 11 still calls BS-3g completeness semantics open although the joint-counterfactual path is settled and only the γ-to-sign/calibration mapping remains open.
<!-- END FINDINGS-BLOCK -->