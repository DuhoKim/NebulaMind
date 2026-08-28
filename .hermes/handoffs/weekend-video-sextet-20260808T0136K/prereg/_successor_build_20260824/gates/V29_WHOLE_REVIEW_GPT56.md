# V29 WHOLE-DOCUMENT RE-REVIEW — GPT56

## Verdict

**CLEAR.** I find no remaining objection to the document. This is a clear preregistration draft for an unfinished and currently blocked programme, not authorization to proceed. The text continues to state the unresolved designs, non-applicable Stage-P result, unfilled slots, non-executable Clause 10 reverse reachability, and first-image-byte block rather than presenting them as completed work.

## Exact subject comparison

I recomputed SHA-256 over the current bytes of `../PREREG_SUCCESSOR_DRAFT_V29_20260827.md`:

- supplied SHA-256: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- recomputed SHA-256: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- comparison: **MATCH**, exact 64-hex equality

That is the same digest I recorded for the V29 bytes in my first-round report. No V30 subject was substituted; this re-review concerns the same V29 bytes.

## Required tool executions

### 1. `prereg_lint.py`

Command, from the assigned `gates` directory:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V29_20260827.md --gates .`

Return: exit **0**.

```text
prereg lint — PREREG_SUCCESSOR_DRAFT_V29_20260827.md
  §7 data rows: 23 (15 class P, 8 class E) — 22 carry a BS- identifier
  no inconsistencies found (all 6 checks demonstrated they can fail)
```

### 2. `prereg_lint.py --self-test`

Command:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V29_20260827.md --gates . --self-test`

Return: exit **0**.

```text
prereg lint self-test — PREREG_SUCCESSOR_DRAFT_V29_20260827.md
  OK   check_repair_citations: control fires
  OK   check_prose_counts: control fires
  OK   check_class_agreement: control fires
  OK   check_lock_identity: control fires
  OK   check_list_numbering: control fires
  OK   check_slots_exist: control fires
  self-test: 6 controls, 0 failure(s)
```

### 3. `prereg_trace.py --check`

Command:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py .. --check ../PREREG_SUCCESSOR_DRAFT_V29_20260827.md`

Return: exit **0**.

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V29_20260827.md
  28 computed transition(s); 0 problem(s)
```

## Numbered findings

No blocking or non-blocking document findings remain. There is therefore no failing document section or smallest sufficient document repair to prescribe.

## Failed attacks and held boundaries

1. **Subject-substitution attack — failed.** The current V29 bytes match the dispatched digest exactly and match the digest recorded in my first-round V29 review.

2. **Clause 10 forward-termination attack — failed.** The §6.1 rows retain named phases, prerequisites, emissions, and failure effects. Row I halts on missing allocated output; Row J halts calibration failure as `INCONCLUSIVE-BY-CALIBRATION` and Stage-C failure as `INCONCLUSIVE-BY-POWER`; Row P retains the closed precedence order for missing, duplicate, orphan, malformed, absent, non-finite, low-confidence, and accepted-finite states. A post-unblinding removal has the fixed calibration-inconclusive consequence and does not trigger a Stage-C rerun.

3. **Clause 10 reverse-reachability attack — failed as a document objection.** Clause 10 does not falsely claim executable closure. It explicitly says `VOID` reverse reachability is unresolved, Clause 10 is not executable, and BS-6 plus the first image byte remain blocked until a pinned producer/conversion handles every enumerated antecedent. BS-2v remains DESIGN/UNRESOLVED. This is an honest unresolved programme dependency, not an unterminated promise hidden by the prose.

4. **Catalogue-quality threshold and neighbour attack — failed.** The document consistently keeps `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, and `nobs_r >= 3` as absolute catalogue-quality exclusions applied before BS-2f. Their ordinary effect is exclusion into the 49,211-row sealed mask, distinct from post-unblinding instrument-confidence handling. Moving a threshold after first real χ is separately a `VOID` antecedent. Line 378 still states that outcome-blind chronology is established while independence from handedness conditional on position is **not established** and must be preregistered as a check or stated as an assumption with risk.

5. **Calibration boundary and neighbour attack — failed.** Any `a_LB_b < 0.85` halts pre-unblinding as `INCONCLUSIVE-BY-CALIBRATION`; the complementary `a_LB_b >= 0.85` condition permits Stage C. Spread `<= 0.03` selects the scalar path and spread-only failure `> 0.03` selects the profile path rather than a failure outcome. Aggregate non-finite/degenerate handling remains separately named.

6. **Power boundary and stale-result attack — failed.** The frozen rule remains 1,000 trials with one-sided 95% Clopper–Pearson lower bound at least 0.95, exactly `x >= 962` successes; 961 fails. Stage-C threshold or self-verification failure and `N_eq < 100,000` halt before a real statistic as power-inconclusive. The 995/1,000 Stage-P result remains prominently `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`, and BS-5p remains unfillable pending rerun on that mask.

7. **Numeric-decision neighbour attack — failed.** `REPRODUCED-LONGO` retains strict p `< 0.001`, the required sign, the three-sigma amplitude band, and the evaluated detection floor. `REJECTED-AT-LONGO-AMPLITUDE` retains strict p `> 0.05` and strict amplitude upper bound `< 0.0408`. Other numeric results remain `INCONCLUSIVE`.

8. **Unfinished-programme overclaim attack — failed.** The document still says BS-2a is DESIGN/UNFILLED; one of fifteen class-P slots is filled; BS-2v and findings 1, 2, 2b, and 3 are unresolved; Rows C2 and E cannot run; BS-5p is unfillable pending rerun; BS-6 and the first image byte remain blocked. CLEAR therefore means the document honestly preregisters an unfinished programme, not that execution is permitted.

9. **Prior tooling blocker — no document repair required.** The previous CODEX blocker identified missing negative-control coverage in `tools/prereg_lint.py`, not a claim made by V29. The current normal lint run reports all six checks controlled, the explicit self-test reports all six controls firing with zero failures, and the trace check reports zero problems. The document bytes required no version bump for that tool-only repair.

## Testimony and limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or authorize an image byte, execute inference, run Stage P, unblind anything, or modify the V29 subject.
- Survey provenance, scientific-source authenticity, measured population values, and the historical assertion that no image byte has been fetched remain **Testimony** in this pass. I verified the exact subject identity, reread the document, attacked Clause 10 in both directions, swept the operative thresholds and neighbouring consequences, and executed the three required checks myself.
- The only durable write by this seat is this report.

**CLEAR**