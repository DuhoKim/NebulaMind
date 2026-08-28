# V29 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V29 document bytes exactly match the supplied SHA-256. The V28→V29 document delta is confined to the title, one §10 contract paragraph, and the V27→V28 table refresh; §10 now states the four intended scopes, the full table reaches V27→V28, the corrected trace checker leaves V28 unaffected by the later V29, and both required tools exit 0. However, `prereg_lint.py`'s clean claim overstates its negative-control evidence: `check_repair_citations` is one of the six checks executed on the real document but is absent from `CONTROLS`, so that check never demonstrates on each run that it can fire and can never be reported `VACUOUS` by the new mechanism.

## Digest first — exact comparison

I computed SHA-256 over the exact current bytes of `../PREREG_SUCCESSOR_DRAFT_V29_20260827.md` and compared all 64 hexadecimal digits with the digest supplied in `BRIEF_V29_WHOLE_REVIEW.md` lines 3–5 and in the dispatch:

- supplied digest: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- independently recomputed digest: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- comparison: **MATCH — exact 64-hex equality over the named V29 Markdown file's current bytes**

## Required tool runs

From the assigned `gates` directory I ran:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V29_20260827.md --gates .`

It returned exit code **0** and exactly:

```text
prereg lint — PREREG_SUCCESSOR_DRAFT_V29_20260827.md
  §7 data rows: 23 (15 class P, 8 class E) — 22 carry a BS- identifier
  no inconsistencies found (all checks demonstrated they can fail)
```

The run printed **no `VACUOUS` line**. Finding 1 explains why that absence does not cover every check the program executes.

I also ran:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py .. --check ../PREREG_SUCCESSOR_DRAFT_V29_20260827.md`

It returned exit code **0** and exactly:

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V29_20260827.md
  28 computed transition(s); 0 problem(s)
```

The trace tool reports no `VACUOUS` status (its output has no such status); it reports zero problems.

## Numbered findings

### 1. HIGH / BLOCKING — `tools/prereg_lint.py` lines 298–304 and 324–353: the clean report claims every check demonstrated it can fail, but `check_repair_citations` has no negative control

**Evidence.** `main()` executes six consistency checks on the real document: `check_slots_exist`, `check_class_agreement`, `check_prose_counts`, `check_lock_identity`, `check_list_numbering`, and `check_repair_citations`. `CONTROLS` contains mutators for only the first five. My programmatic set comparison returned:

```text
main_checks=check_class_agreement,check_list_numbering,check_lock_identity,check_prose_counts,check_repair_citations,check_slots_exist
negative_controlled=check_class_agreement,check_list_numbering,check_lock_identity,check_prose_counts,check_slots_exist
checks_without_negative_control=check_repair_citations
```

The omitted check is not inherently incapable: appending a synthetic nonexistent repair citation and directly invoking it returned:

```text
synthetic_bad_repair_citation_finding=[('repair-citations', 'cites CODEX-V999 F1 but no PREREG_TEXT_V999_CODEX.md exists')]
```

But `run_controls()` never performs that attack. Consequently, a future regression that makes `check_repair_citations` silent will not enter `vacuous`, will not print `VACUOUS`, and will not prevent the line `no inconsistencies found (all checks demonstrated they can fail)`.

**Why it fails.** The V29 brief's tooling contract says “Each check ships a mutator,” “every check runs against its own mutated copy,” and a silent check is reported `VACUOUS`. The implemented contract covers five of six checks. The clean output therefore makes a stronger statement than the control battery proves. This is the same failure class the negative-control repair was introduced to prevent: unchecked silence presented as demonstrated capability.

**Smallest sufficient repair.** Add a `_mut_repair_citation` negative control that inserts a syntactically valid nonexistent finding citation and add `("check_repair_citations", _mut_repair_citation, "repair-citations")` to `CONTROLS`. Ensure the control uses the same gates path as the real run, and add a regression assertion that disabling or breaking `check_repair_citations` produces `VACUOUS` and exit 1.

## §10 scope, table reach, and one-paragraph delta

The V29 §10 paragraph states all four intended cases:

1. destinations earlier than the subject are in-band and checked against their own §10 row/result digest;
2. destination equal to the subject is the current transition, owned and checked in `gates/FINDINGS_MAP.md`;
3. destinations later than the subject are out of scope because they postdate it;
4. V1→V15 are exempt by the named historic rule.

The historic exemption is the explicitly stated exception to the general earlier-than-subject rule. The implementation's boundary predicates agree: `to <= 15` skips by the historic exemption, `to > subject_ver` skips as future/out of scope, `to == subject_ver` checks the sidecar, and remaining rows are checked in-band.

The §10 table contains 27 rows and ends at `V27 → V28`. I independently rebuilt the transition rows from the draft bytes, rendered complete predecessor-only rows with the findings map, and compared whole Markdown row strings:

```text
computed_total=28
expected_in_band=27
actual_in_band=27
full_row_byte_equality=True
last_actual=| V27 → V28 | `e801a18bb7c489f0` | `82cd8ac3690fb87b` | §10 (+19/−12), (preamble) (+1/−1) | no row-count change | GPT56-V27-1, GPT56-V27-2, GPT56-V27-3, CODEX-V27-1 |
```

The current V28→V29 mapping exists separately in `gates/FINDINGS_MAP.md` as `CODEX-V28-1 (current-transition scope rule)`.

The exact V28→V29 unified diff contains **10 changed minus/plus lines**, matching `runner_v29_chain.log`: one title replacement (2 diff lines), one contiguous §10 paragraph replacement (3 removed and 4 added lines), and one added V27→V28 table row. No other document bytes changed. Thus the substantive prose repair stayed one paragraph; the only other changes are the expected title and table refresh.

The V28 regression now holds in the real directory with V29 present: checking the unchanged V28 returned exit 0 with `28 computed transition(s); 0 problem(s)`. V29 itself also checks clean and therefore still requires its own V28→V29 sidecar mapping.

## Clause 10, both directions, thresholds, phases, effects, and neighbours

No new prose blocker was found in Clause 10 or its neighbours.

- **Forward termination:** Rows A–S retain their phase, prerequisite, emission, and failure-effect assignments. Row I terminates missing allocated output before BS-8f. Row J terminates a calibration lower-bound failure as `INCONCLUSIVE-BY-CALIBRATION` and Stage-C threshold/self-verification failure as `INCONCLUSIVE-BY-POWER`. Row P closes zero, duplicate, orphan, malformed, absence, non-finite, low-confidence, and accepted-finite states in precedence order; any post-unblinding removal terminates calibration-inconclusive with no Stage-C rerun.
- **Reverse reachability:** §7.1 carries the stable VOID antecedent registry, and the removed orphan `VOID-6.1C2-ATTESTATION-FAIL` remains absent. Clause 10 does not claim executable reverse closure: it states that VOID reverse reachability is unresolved, Clause 10 is not executable, and BS-6 plus the first image byte remain blocked until a pinned converter handles every enumerated antecedent.
- **Catalogue-quality thresholds and phase:** `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, and `nobs_r >= 3` remain frozen pre-BS-2f exclusions with ordinary nonfatal exclusion effect; moving a threshold after the first real χ is a VOID condition. V28 and V29 line 378 are byte-equal and still state that conditional independence with handedness given position is **not established**.
- **Calibration/path thresholds:** any `a_LB_b < 0.85` halts pre-unblinding as calibration-inconclusive; all `>= 0.85` permit Stage C. Spread `<= 0.03` selects scalar, `> 0.03` selects profile, and spread is not a failure. Aggregate non-finite/degenerate inputs are validated before the comparison and terminate calibration-inconclusive, apart from Row I's separately named missing-output halt.
- **Power thresholds and effect:** Stage P and Stage C retain 1,000 trials, one-sided 95% lower bound `>= 0.95`, the exact `x >= 962` PASS boundary (961 fails), and success p `< 0.001`. Stage P's 995/1000 remains explicitly `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK` and cannot fill BS-5p. Stage-C threshold/self-verification failure and locked-mask `N_eq < 100,000` halt pre-unblinding as power-inconclusive.
- **Numeric verdict thresholds:** `REPRODUCED-LONGO` requires p `< 0.001`, the required sign, the three-sigma amplitude band, and the evaluated detection floor. `REJECTED-AT-LONGO-AMPLITUDE` requires p `> 0.05` and strict amplitude upper bound `< 0.0408`; other numeric outcomes are `INCONCLUSIVE`.

The standing state remains explicit: BS-2v and findings 1, 2, 2b, and 3 are unresolved; Rows C2 and E cannot run; Stage P is superseded pending rerun on the 49,211 mask; BS-6 and the first image byte remain blocked; no image byte is authorized by this text.

## Failed attacks / checks that held

1. Subject-substitution attack failed: the named V29 bytes exactly match the supplied 64-hex digest.
2. Scope-boundary attack failed: all four §10 scopes are stated and the code now distinguishes historic, future, current, and in-band transitions at the intended boundaries.
3. Future-transition attack failed: with V29 present, the unchanged V28 check remains clean.
4. Current-transition attack failed: V29's V28→V29 sidecar exists and the V29 check returns zero problems.
5. Table-fidelity attack failed: all 27 complete in-band rows are byte-equal to independent regeneration, ending at V27→V28.
6. Delta-sprawl attack failed: the 10 diff lines are confined to the title, one §10 paragraph, and the one-row table refresh.
7. Five controlled lint checks demonstrated they can fire; the required lint invocation reported no inconsistency and no `VACUOUS` among those five. The sixth check's missing control is Finding 1.
8. Clause-10 termination and threshold-neighbour attacks failed: the value/phase/effect assignments and honest unresolved reverse-reachability block remain intact.
9. Held-state attacks failed: line 378 is byte-for-byte unchanged, catalogue-quality remains in the closed pre-lock vocabulary, BS-2a remains DESIGN/UNFILLED, the table remains 15 class P / 8 class E with one class-P slot filled, and the first-image block remains explicit.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`, fetch or authorize an image byte, run Stage P, execute inference, unblind anything, or mutate git.
- Survey provenance, source-data truth, the 49,211 and N_eq measurements, and scientific citation claims remain **Testimony** in this pass. I checked the pinned document bytes, exact delta, tooling behavior, internal trace reconstruction, thresholds, neighboring phase/effect rules, and closure statements.
- The synthetic repair-citation probe was performed in memory; it did not modify the subject or gates corpus. This report is the only durable write by this seat.

## Evidence ledger

Content read: `BRIEF_V29_WHOLE_REVIEW.md`; the complete pinned V29 subject across §§0–11; `tools/prereg_lint.py`; `tools/prereg_trace.py`; `runner_v29_chain.log`; `V28_WHOLE_REVIEW_CODEX.md`; and the V28→V29 entry in `gates/FINDINGS_MAP.md`. Read-only comparisons/executions: exact V29 SHA-256; exact V28→V29 unified diff and changed-line count; required V29 lint and trace invocations with exit codes; V28 future-transition regression; complete generated-row equality; line-378 byte equality; and programmatic comparison of `main()` checks against `CONTROLS`, plus an in-memory synthetic bad repair citation. An initial attempt to invoke nonexistent gate-local `../tools/` paths failed before the successful absolute-path invocations; one initial diff-count one-liner had a quoting syntax error; one first table-equality helper sliced a rendered footer incorrectly and was discarded, then replaced by row-pattern extraction that returned 27/27 byte equality. No result from a failed or malformed helper was credited.

**NOT CLEAR**