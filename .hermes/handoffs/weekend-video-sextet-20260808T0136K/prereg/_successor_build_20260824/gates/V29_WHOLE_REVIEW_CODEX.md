# V29 WHOLE-DOCUMENT RE-REVIEW — CODEX

## Verdict

**CLEAR.** I re-refereed the same V29 document bytes rather than inferring from the first-round result. The subject's independently recomputed SHA-256 exactly matches the supplied pin and the digest recorded in my first-round review. No V30 subject exists. The only first-round CODEX blocker was against `tools/prereg_lint.py`, not against the document; the repaired linter now demonstrates all six executed checks, its required self-test passes, and the trace check passes. Re-reading the document, Clause 10 in both directions, its threshold/phase/effect neighbours, and the standing-state disclosures found no remaining document objection. CLEAR means only that V29 is an internally honest preregistration draft of an unfinished programme; it does not authorize the study, image acquisition, or any blocked execution.

## Digest first — same-byte comparison

Subject: `../PREREG_SUCCESSOR_DRAFT_V29_20260827.md`

- supplied SHA-256: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- independently recomputed SHA-256: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- comparison: **MATCH — exact 64-hex equality over the named current bytes**
- first-round CODEX review's independently recomputed SHA-256: the same `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- same-byte conclusion: **this is the same V29 document previously reviewed, not a repaired document revision**
- V30 search: no `PREREG_SUCCESSOR_DRAFT_V30*` file exists in the successor-build directory

## Required tool runs

All three required commands were run from the assigned `gates` directory.

### 1. `prereg_lint.py`

Command:

```text
python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V29_20260827.md --gates .
```

Return: exit code **0**; stdout exactly:

```text
prereg lint — PREREG_SUCCESSOR_DRAFT_V29_20260827.md
  §7 data rows: 23 (15 class P, 8 class E) — 22 carry a BS- identifier
  no inconsistencies found (all 6 checks demonstrated they can fail)
```

The live coverage comparison also returned `UNCONTROLLED=<none>` and `COVERAGE=6/6`. `CHECKS_RUN` contains the six checks executed by `main()`, and `CONTROLS` now contains all six, including `check_repair_citations` via `_mut_repair_citations`.

### 2. `prereg_lint.py --self-test`

Command:

```text
python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V29_20260827.md --gates . --self-test
```

Return: exit code **0**; stdout exactly:

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

This directly closes the prior tool objection: the repair-citation check now proves it can fire, every executed check has a control, and the regression assertion exits clean only with six firing controls and no uncontrolled check.

### 3. `prereg_trace.py --check`

Command:

```text
python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py .. --check ../PREREG_SUCCESSOR_DRAFT_V29_20260827.md
```

Return: exit code **0**; stdout exactly:

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V29_20260827.md
  28 computed transition(s); 0 problem(s)
```

## Numbered findings

**None.** There is no remaining blocking or non-blocking objection to the document, so there is no failing severity, section/line, rationale, or document repair to prescribe.

## Independent document attacks that held

1. **Subject-identity attack — held.** The current V29 bytes match the dispatch pin and the first-round subject digest exactly. The document was not silently changed to obtain this verdict.

2. **Unfinished-programme honesty attack — held.** The document does not present a CLEAR text gate as authorization to proceed. It says the draft is not in force (lines 53–59), keeps BS-2a DESIGN/UNFILLED, keeps BS-2v DESIGN/UNRESOLVED, states that Rows C2 and E cannot run, keeps BS-6 and the first image byte blocked (lines 559–580, 666–692), and leaves required implementations explicitly unresolved (§5 and §11).

3. **Clause 10 forward-termination attack — held.** The lifecycle table retains named phases, prerequisites, emissions, and failure effects. Row I halts a missing/non-finite allocated output before BS-8f; Row J halts calibration failure as `INCONCLUSIVE-BY-CALIBRATION` and Stage-C threshold or self-verification failure as `INCONCLUSIVE-BY-POWER`; Row P gives a closed precedence order for missing, duplicate, orphan, malformed, absent, non-finite, low-confidence, and accepted-finite states. Any post-unblinding removal deterministically yields calibration-inconclusive, with no Stage-C rerun.

4. **Clause 10 reverse-reachability attack — held as an honest open block.** Clause 10 does not falsely claim executable reverse closure. Line 580 states that `VOID` reverse reachability is unresolved, Clause 10 is not executable, and BS-6 plus the first image byte remain blocked until a pinned producer/conversion handles every enumerated antecedent. BS-2v remains a DESIGN/UNRESOLVED class-P prerequisite, and §7.1 retains the stable antecedent registry. That is a correct preregistration of blocked work, not a claim that the work is complete.

5. **Catalogue-quality threshold/phase/effect sweep — held.** The thresholds remain exactly `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, and `nobs_r >= 3` (lines 372–378 and 690). They are pre-BS-2f catalogue-quality exclusions into the 49,211-row sealed mask, not post-unblinding Row-P removals. Line 378 remains explicit that conditional independence from handedness given position is not established. Moving a threshold after inference/first real χ remains a VOID condition.

6. **Calibration boundary sweep — held.** `a_LB_b < 0.85` terminates pre-unblinding as `INCONCLUSIVE-BY-CALIBRATION`; the complement `a_LB_b >= 0.85` is required before Stage C. Spread `<= 0.03` selects the scalar path and spread `> 0.03` selects the profile path rather than a failure. Aggregate non-finite/degenerate handling remains separated from Row I's missing-allocated-output halt.

7. **Power boundary sweep — held.** Stage P/Stage C use 1,000 trials and the exact `x >= 962` pass boundary, with 961 failing. I independently recomputed the one-sided 95% Clopper–Pearson lower bounds: 961 gives `0.949365993205` (fail) and 962 gives `0.950487129744` (pass). The 995/1,000 Stage-P result remains prominently `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`; BS-5p remains unfillable pending rerun on that mask. Stage-C failure and `N_eq < 100,000` halt pre-statistic as power-inconclusive.

8. **Numeric-verdict neighbour sweep — held.** `REPRODUCED-LONGO` keeps strict p `< 0.001`, Longo's sign, the three-sigma band, and the evaluated detection floor. `REJECTED-AT-LONGO-AMPLITUDE` keeps strict p `> 0.05` and strict upper bound `< 0.0408`; all other numeric outcomes are `INCONCLUSIVE`. No equality boundary is left to operator judgement.

9. **Trace-scope attack — held.** §10 retains the four disjoint cases: historic V1→V15 exemption; predecessor transitions checked in-band; the current transition checked in `gates/FINDINGS_MAP.md`; later transitions out of scope. The live trace check computes 28 transitions and reports zero problems. No V30 was created to manufacture a content delta.

10. **Prior-blocker classification attack — held.** My first-round report explicitly found no prose blocker in Clause 10 or its neighbours and prescribed only a linter repair: add the repair-citation mutator/control and a regression assertion. V29 itself makes no claim about linter coverage. The repaired tool now satisfies that separate request, so the former tool defect does not remain an objection to these unchanged document bytes.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or authorize any image byte, run Stage P, execute inference, unblind anything, modify the subject, or mutate git.
- Survey provenance, scientific-source authenticity, the measured 49,211/`N_eq` values, and the historical assertion that no image byte has been fetched remain **Testimony** in this pass. I verified document identity, internal phase/value/effect consistency, threshold boundaries, standing-state disclosures, and checker behavior.
- The repository already contained unrelated modified/untracked state when inspected. I did not treat that pre-existing state as evidence for or against the document. This report is my only durable write.

## Evidence ledger

Content read: `BRIEF_V29_REREVIEW.md`; the complete pinned V29 document; the first-round CODEX and GPT56 V29 reports; `tools/prereg_lint.py`; `tools/prereg_trace.py`; and `gates/FINDINGS_MAP.md`.

Independent executions: exact V29 SHA-256; search for a V30 subject; required lint; required lint self-test; required trace check; programmatic `CHECKS_RUN` versus `CONTROLS` comparison; one-sided 95% Clopper–Pearson lower-bound recomputation at 961 and 962 successes; targeted rereads of §5, §6.1 Clauses 1–10, §6.3, §7/§7.1, §10, §11, threshold neighbours, and standing-state lines.

**CLEAR**