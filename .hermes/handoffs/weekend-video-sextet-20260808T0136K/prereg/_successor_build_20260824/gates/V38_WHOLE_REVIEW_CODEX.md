# V38 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V38 bytes match the brief's SHA-256, the V11 wording does support `Post-first-real-χ`, and the new BS-3g row creates the intended document-level edge to BS-6. But the 15/8 → 16/8 change left the DESIGN-slot inventory stale, and the VOID registry still claims semantic completeness while assigning the two generic §5 failure IDs a phase narrower than §5. The cited authority/provenance bytes also do not say what V38 says they say. These are document defects, not implementation complaints; BS-6 remains blocked.

## Subject identity

- Required SHA-256: `b5776d287a22cff71fe34d1ee1dbe937f1af61d51ad70530f378668cbfe1ec56`.
- Recomputed before reading: `b5776d287a22cff71fe34d1ee1dbe937f1af61d51ad70530f378668cbfe1ec56` — exact match.
- V36 and V37 recomputed as `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177` and `62dd8a7525c399126477573d55a952f1ed2f147d16f8bfbb12aa89a295821c42`, matching the brief.

## Findings

### 1. MEDIUM — REPAIR REQUIRED — the new DESIGN slot is absent from the document's DESIGN inventory

V38 §7 line 701 says, “On today's count: **BS-2a, BS-2k, and the BS-2v VOID converter are DESIGN slots.**” The table itself has four DESIGN rows: BS-2a (line 707), BS-2k (708), BS-2v (709), and newly added **BS-3g** (716). An independent parser over the §7 rows returned exactly those four. `prereg_counts.py` correctly reports 16 class P / 8 class E, but it checks class counts, not this DESIGN subtype inventory, so its clean result does not settle the sentence.

This is the direct old-inventory casualty of the 15/8 → 16/8 move. Repair line 701 to include BS-3g (and preferably compute/check this subtype inventory rather than hand-maintain it).

### 2. HIGH — REPAIR REQUIRED — §7.1 still overclaims semantic completeness; the generic §5 phases are narrower than §5

V38 §5 line 493 declares VOID for “permutation/statistic/protocol non-finite/degenerate failures” without a post-unblinding qualifier. Yet §7.1 assigns both `VOID-5-NONFINITE` and `VOID-5-DEGENERATE` the phase **`Post-unblinding`** (lines 752–753). That excludes a non-finite or degenerate failure produced under the frozen protocol before unblinding—for example during the P5 pre-unblinding Stage-C process named at line 561. `VOID-6.1J-DEVIATION` cannot silently repair this: a failure returned by the pinned protocol is not necessarily a deviation from it, and V37's own rationale says these disjuncts require separate antecedents rather than undeclared aliases.

This defeats line 737's unqualified claim that the registry supplies exact phases for **every** VOID antecedent required by §5 and §6. Line 739 accurately disclaims the checker's semantic power, but it does not retract line 737's document-level completeness claim. The executed checker returned 54 antecedents / 20 row names / digest `a4d1d745b2ed33bc0e01dd39b845f88daffdc542d2bdd98d5e122ab7dd443d37`; that is NAME closure only and cannot see this phase undercoverage.

Repair by aligning the two generic §5 rows' phases with §5 (or narrowing §5 explicitly and accounting separately for every earlier protocol failure). Until then the registry must not be represented or pinned as semantically complete.

### 3. MEDIUM — REPAIR REQUIRED — the cited file does not record the claimed principal decision

V38 §7.1 line 741 says option A is “recorded in `DECISIONS_FOR_DUHO.md` decision 1.” The cited file says in its first five lines that it is **“a plain-language index, not a source”** and that the open-question files hold the evidence. Its decision-1 section (lines 19–38) presents an unresolved ask and the lane's recommendation; it contains no principal answer or option-A authorization. `LANE_STATE_20260829.md` line 57 and `gates/FINDINGS_MAP.md` line 30 later assert that Blanc relayed a 09:20 decision, and the review brief repeats that testimony, but the file V38 actually cites does not record it.

The principal decision may be real; the cited evidence does not settle it. Cite the actual immutable relay/authorization record, or label the claim as relayed testimony rather than attributing it to `DECISIONS_FOR_DUHO.md`.

### 4. LOW — REPAIR REQUIRED — the phase conclusion holds, but its “authorship record” citation overstates what the cited bytes establish

The substantive instant survives attack. V11 lines 267–268 say the freedom is exercised “after image inference exists,” and V11 lines 293–294 tie the threshold VOID trigger to “after inference exists.” In the current lifecycle, Row D writes real χ-bearing measurement receipts at P2 (V38 line 555), while unblinding is P7 (line 545); thus the first produced real χ precedes unblinding. `Post-first-real-χ` is the defensible recovered instant.

But V38 line 743 misattributes the quoted pre-lock disclosure clause to **§6.2**; the phrase “before the primary lock” is at §6 line 527, while §6.2 begins at line 599. Also, `git show -s 4d99d1d93` names the commit author as **Duho Kim**, and the commit adds the entire V11 file; that record proves the clause entered in those bytes, not the separate assertion “authored by this lane.” The wording settles the phase without these overclaims. Repair the section citation and distinguish textual inference from unverified lane-authorship attribution.

## Attacks that held

- **BS-3g dependency edge:** held at document-contract level. BS-3g is class P, explicitly blocks BS-6, and the draft requires every class-P slot to be receipted before freeze. It remains DESIGN/UNFILLED and does not authorize imaging.
- **§2.7 instant:** held substantively as `Post-first-real-χ`, for the V11 wording and P2→P7 lifecycle reason above. The earlier post-unblinding reading confused production/existence with later reading.
- **Class totals:** `tools/prereg_counts.py` returned 16 P / 8 E and prose-matched totals. The finding is the stale DESIGN subtype list, not the class total.
- **V36→V37 and V37→V38 deltas:** exact diffs match the announced changed regions. `tools/prereg_trace.py <lane> --check <V38>` returned 37 transitions / 0 problems.
- **Frozen code pins:** live SHA-256 values match V38 for `successor_ref_v9.py` (`6a9abbb…`), `closure_worker_v9.py` (`28f8e1f9…`), `bs2a_quality_gate.py` (`dfbd63d1…`), `gain_gradient_estimator.py` (`e2270297…`), and `verify_mu_gamma.py` (`e33d9275…`).
- **Authorization-limit disclosure:** held. Directly calling frozen `require_authorization()` with `BRIEF_V38_REVIEW.md` and that file's caller-computed digest returned success, confirming it is only a caller-path/caller-digest integrity check. I did not treat this known, deliberately unbuilt guard as a new blocker.
- **Known lint posture:** `prereg_lint.py` exited 1 with exactly the quarantined `repair-citations-advisory`; I assigned it no evidentiary weight.

## Evidence ledger and limits

Read: the complete V38 draft; V11 §2.7; full V36→V37 and V37→V38 diffs; `BRIEF_V38_REVIEW.md`; `DECISIONS_FOR_DUHO.md`; `LANE_STATE_20260829.md`; `OPEN_QUESTION_VOID_2.7_PHASE.md`; `FINDINGS_MAP.md`; both V36 whole-review reports; both VOID-gate reports; and the relevant frozen-code function.

Executed: SHA-256 checks; class-count, VOID-registry, lint, and trace checkers; independent DESIGN-row extraction; exact git metadata/diff inspection; frozen-pin hashing; and the bounded `require_authorization()` probe described above.

I did not read `/Users/duhokim/NebulaMindData/`, inspect or fetch image bytes, run inference, execute Stage P/C, unblind, fill a slot, modify frozen v9, or modify the draft. Pre-existing repository dirt outside this report was left untouched. The only intended write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V38
VERDICT: NOT CLEAR
COUNT: 4
F1 | MEDIUM | REPAIR-REQUIRED | §7 line 701 | The DESIGN-slot inventory omits newly added DESIGN slot BS-3g.
F2 | HIGH | REPAIR-REQUIRED | §5 line 493; §7.1 lines 737, 752–753 | Generic non-finite/degenerate VOID rows are Post-unblinding despite an unqualified §5 trigger, defeating semantic completeness.
F3 | MEDIUM | REPAIR-REQUIRED | §7.1 line 741 | DECISIONS_FOR_DUHO.md is an unresolved index, not the claimed record of principal option A.
F4 | LOW | REPAIR-REQUIRED | §7.1 line 743 | The phase is substantively sound, but §6.2 is mis-cited and commit metadata does not prove lane authorship.
<!-- END FINDINGS-BLOCK -->