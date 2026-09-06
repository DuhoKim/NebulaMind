ACCESS_SHA=cd126c26b4a4218e2572999f15a07a909ee1bd45a83b3a3e99f51b1be7cd21ff
SEAT=codex
ROUND2_RESIDUALS=PARTLY
NEW_DEFECTS=3
STAGED_TESTS=PASS
READY_FOR_PRINCIPAL=NO

Bounded round 3, independent review of revision 3, UNADOPTED. The specific seedless, missing-symbol, orphan-claim, input-id, batch-2-chain, ownership and extra-seal negatives now fail as intended. Closure is nevertheless incomplete: some machine promises still fail open, omission vocabulary remains outside the clause, and the candidate still prints the old control count. This report adopts, freezes and installs nothing; only staged tests and reviewer probes were executed. No gate, C0 or seat-packet contents were opened. Historical run/feasibility statements below are assessed as qualified descriptions of the supplied record, not independently observed production runs.

| Round 2 residual | Judgment | Own command/probe and observed output |
|---|---|---|
| T6: seedless selection | REPAIRED | P07: removed seed, emptied audited/sample ids and zeroed k; exit 1, `C6_SELECTION: selection carries no 64-hex seed; nothing to recompute against`, `C6_AUDIT_SAMPLE=FAIL`, `study_files=CENSUS_AUDIT_FAILED`. Honest baseline P05 passes with one audited claim. A different malformed-seed defect is N2 below. |
| T8: re-filed import under another reason code | PARTLY | P02 rejects CHOSEN/ORIG_CHOICE_STATED with external value line: `such a record must be IMPORTED with ORIG_CITATION`; exit 1, `C3_NO_SUBSTITUTION=FAIL`. P03 (candidate argument omitted) and P04 (provided candidate file lacks the claim) both exit 0, `C3_NO_SUBSTITUTION=PASS`. Thus the advertised EVERY PRINTED claim binding is incomplete; N1. |
| T8: no line carries symbol and numeral | REPAIRED | P01: value 17 exists, symbol zeta does not; exit 1, `no line of source.txt carries both zeta and 17`, `C3_NO_SUBSTITUTION=FAIL`. Positive q/17 baseline passes. |
| T8: designated-locator disclosure | REPAIRED | P00 prints `DESIGNATED_LOCATOR_DISCLOSURE=FOUND`. P06 uses a borrower explicitly designating the second source line; exit 1, `external value line 2 is not the first line of source.txt carrying both q and 17 (that is line 1)`. This matches the disclosed deterministic substitution; no ruling on A versus B is made. |
| T2: join orphan claim and input-id form | REPAIRED | P11: `ledger record borrow.txt#q names claim borrow.txt#missing, not an included candidate of this batch`; P12: `input_id local_q does not begin with its claim's file followed by #`; each exit 1, `JOIN=FAIL`. Honest two-batch baseline P10: exit 0, `JOIN=PASS`. |
| T11: predecessor chain, sealed ownership, extra seals | PARTLY | P13 broken batch-2 predecessor, P14 substituted batch-2 owned file, P15 extra batch-3 seal each exit 1 with the corresponding sole diagnostic and `JOIN=FAIL`. P16 gives batch 1 a non-null fictitious predecessor and consistently binds batch 2 to it: exit 0, `JOIN=PASS`. Complete chain validation still lacks the root condition; N3. |
| T3: result vocabulary and study_files | PARTLY | P05: both excluded with DATE versus REFERENCE_NUMBER now gives `result=MATCH`, both kind fields retained, `study_files=none`, PASS. P08: auditor-only excluded passage gives `result=OMISSION_AUDIT_EXCLUDED_ABSENT_FROM_SEALED`, FAIL, `study_files=CENSUS_AUDIT_FAILED`. Study-level filing is repaired; the omission result is still outside the promised `MATCH / OMISSION / AUDIT_INCLUSION_DISPUTED` vocabulary. |
| T13: pin paths, printed counts, collision control | PARTLY | Required lane-relative shasum check: all 7 OK before and after. Own AST tally in `probes.py`: `OWN_AST_PROBE_CALLS=36`, `ID_COLLISION_PROBE=True`; kit prints 36 and 102/102. P17 independently rejects duplicated candidate id, exit 1, `candidate_id collision across batches: borrow.txt#c`, `JOIN=FAIL`. P00: `CANDIDATE_PRINTED_CONTROLS_84=True`, `BATCH_PRINTED_CONTROLS_102=True`. Candidate's 84/84 remains stale; README and batch document correctly say 102. |
| T12: sixteen sentence replacements | PARTLY | P00 independently matches all sixteen requested entries against current files: fourteen ACCURATE, Codex 1 and 4 INACCURATE. All are quoted below; overlapping Codex/Kimi requests map to the same merged sentences. Presence is not accuracy. |
| T7: custody floor wording | REPAIRED | P00: `CUSTODY_FLOOR=FOUND; HANDOUT_READS_SEALED_CANDIDATES=True; HANDOUT_FIELDS=claim_id/source_file/source_line`. Own stage-ordered audit passes and its handout contains exactly those fields. The text assigns WHAT to seals and WHEN to dispatch/release records and admits prior exposure/shared error. This is a correctly stated limit, not a test that custody actually occurred. |

New executable defects (three distinct counterexamples; N1/N3 also limit the related residual-row judgments, not additional counts):

N1 — The universal PRINTED claiming-file check still fails open. Own borrower says “We take q from source, specifically its second line.” Its candidate is `borrow.txt#c`; external source line 1 says “We choose q = 17.” Re-file the record CHOSEN/ORIG_CHOICE_STATED, quoting that external choice sentence. P02 rejects with the normal candidate file, but the same ledger passes P03 without the optional candidate argument and P04 with an empty candidate file. Code only enters the general binding guard when `candidates` is supplied, and only rejects a cross-file record when `cf0 is not None`. Missing claim binding is enforced separately only in the ORIG_CITATION branch. This refutes “For EVERY PRINTED record validate first binds the claim.” An honest batch join catches the orphan variant; that later protection does not make standalone validate's stated invariant true. Counterexample files: `d1_refiled.json`, `empty_candidates.json`, `src/`, all under W.

N2 — compare validates seed length but not the seed alphabet. With an honest one-claim selection generated from 64 lowercase a characters, changing only `seed_hex` to 64 uppercase A characters gives P09a PASS, while `audit select` rejects that same uppercase seed in P09b (`seed must be 64 lowercase hexadecimal characters`). Replacing it with 64 g characters gives P09c exit 1 with `ValueError: invalid literal for int() with base 16`; no C6_AUDIT artefact, study_files or C6 failure token is emitted. Thus absent-seed rejection is repaired, but compare's seed contract differs from select's and malformed input can abort failure reporting. Uppercase preserves the numeric seed and does not demonstrate a changed sample; the demonstrated faults are acceptance inconsistency and missing structured failure output. Counterexample files: `audit/uppercase_selection.json`, `audit/nonhex_selection.json`.

N3 — join never validates the chain's root predecessor. Starting with honestly sealed own batches, set seal 1's `predecessor_seal_sha256` to 64 f characters and recompute seal 2's predecessor digest over that altered first seal. Leave partition, ownership and all artefact digests intact. P16 reports `JOIN=PASS`; the first seal now purports to have a predecessor absent from the partition. The check runs only for k>1. This is a bounded structural validation gap in the promised complete chain, not evidence of actual custody tampering or a demonstration that valid ownership/denominator counts changed. Counterexample: `batch_root_chain/mutated_seals.json` with the associated own batch files.

Commands and evidence:

First command executed, exactly:
```
shasum -a 256 /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md
```
Exit 0; full digest is line 1. From the supplied lane working directory, executed before and after testing:
```
shasum -a 256 -c r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256
```
Both exit 0:
```
r3c2_staged_d1d7/r3c2_ledger_tools_STAGED.py: OK
r3c2_staged_d1d7/r3c2_batch_tools_STAGED.py: OK
r3c2_staged_d1d7/r3c2_staged_tests.py: OK
r3c2_staged_d1d7/README_STAGED_UNADOPTED.md: OK
r3c2_staged_d1d7/partition_12_of_89.json: OK
r3c2_staged_d1d7/partition_12_of_89.txt: OK
r3c2_staged_d1d7/C6_COUNTEREXAMPLE_EXHIBIT.txt: OK
```
Executed exactly:
```
cd r3c2_staged_d1d7 && /usr/bin/python3 -E r3c2_staged_tests.py
```
Exit 0; last three lines:
```
deletion_probes=36
controls=102 passed=102 failed=0
STAGED_TESTS=PASS
```
The mandated kit run regenerates its own `_ctl/` and exhibit; the pinned exhibit still verifies. I made no edits to candidate, batch document or staged implementation. Independent probe inputs are newly authored under `r3c2_staged_d1d7/_review3_codex/`; none are copied from kit fixtures or prior reviewers.

Executed from the lane:
```
/usr/bin/python3 -E r3c2_staged_d1d7/_review3_codex/probes.py
/usr/bin/python3 -E r3c2_staged_d1d7/_review3_codex/text_probes.py
```
Both exit 0. The first creates fresh synthetic inputs and runs each staged command with subprocess; full actual command lines and unabridged stdout/stderr are in `_review3_codex/commands_output.txt`; structured results are in `results.json`. The second checks replacement text, custody disclosure, actual handout fields, and pinned workload figures. Probe-call counting uses Python AST Call nodes whose function name is `probe`, excluding its definition, comments and string mentions.

For compact command notation below, W is the absolute `_review3_codex` directory under the supplied working directory; L and B are the absolute `r3c2_ledger_tools_STAGED.py` and `r3c2_batch_tools_STAGED.py` paths in its parent. These substitutions abbreviate paths only; commands and arguments are those actually executed. P00 is the text_probes.py invocation above.

P01:
```
/usr/bin/python3 -E $L validate $W/d1_no_symbol.json $W/src $W/d1_candidates.json
```

P02:
```
/usr/bin/python3 -E $L validate $W/d1_refiled.json $W/src $W/d1_candidates.json
```

P03:
```
/usr/bin/python3 -E $L validate $W/d1_refiled.json $W/src
```

P04:
```
/usr/bin/python3 -E $L validate $W/d1_refiled.json $W/src $W/empty_candidates.json
```

P05:
```
/usr/bin/python3 -E $L audit compare $W/audit/s1.txt $W/audit/ac.json $W/audit/ax.json $W/audit/sc.json $W/audit/sx.json $W/audit/sl.json $W/audit/sel.json $W/audit/s2.txt $W/audit/rd.json $W/audit/audit_compare.json
```

P06:
```
/usr/bin/python3 -E $L validate $W/d1_designated_second.json $W/src $W/d1_candidates.json
```

P07:
```
/usr/bin/python3 -E $L audit compare $W/audit/s1.txt $W/audit/ac.json $W/audit/ax.json $W/audit/sc.json $W/audit/sx.json $W/audit/sl.json $W/audit/seedless_selection.json $W/audit/s2.txt $W/audit/rd.json $W/audit/seedless.json
```

P08:
```
/usr/bin/python3 -E $L audit compare $W/omission/s1.txt $W/omission/ac.json $W/omission/ax.json $W/omission/sc.json $W/omission/sx.json $W/omission/sl.json $W/omission/sel.json $W/omission/s2.txt $W/omission/rd.json $W/omission/omission_compare.json
```

P09a:
```
/usr/bin/python3 -E $L audit compare $W/audit/s1.txt $W/audit/ac.json $W/audit/ax.json $W/audit/sc.json $W/audit/sx.json $W/audit/sl.json $W/audit/uppercase_selection.json $W/audit/s2.txt $W/audit/rd.json $W/audit/uppercase_seed.json
```

P09b:
```
/usr/bin/python3 -E $L audit select $W/audit/sc.json AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA $W/audit/s1.txt $W/audit/rejected_selection.json
```

P09c:
```
/usr/bin/python3 -E $L audit compare $W/audit/s1.txt $W/audit/ac.json $W/audit/ax.json $W/audit/sc.json $W/audit/sx.json $W/audit/sl.json $W/audit/nonhex_selection.json $W/audit/s2.txt $W/audit/rd.json $W/audit/nonhex_seed.json
```

P10:
```
/usr/bin/python3 -E $B join $W/partition.json $W/batch_positive $W/batch_positive/seals.json $W/src/R3C2_CORPUS_MANIFEST.md $W/batch_positive/joined_
```

P11:
```
/usr/bin/python3 -E $B join $W/partition.json $W/batch_orphan $W/batch_orphan/seals.json $W/src/R3C2_CORPUS_MANIFEST.md $W/batch_orphan/joined_
```

P12:
```
/usr/bin/python3 -E $B join $W/partition.json $W/batch_input_form $W/batch_input_form/seals.json $W/src/R3C2_CORPUS_MANIFEST.md $W/batch_input_form/joined_
```

P13:
```
/usr/bin/python3 -E $B join $W/partition.json $W/batch_chain $W/batch_chain/mutated_seals.json $W/src/R3C2_CORPUS_MANIFEST.md $W/batch_chain/joined_
```

P14:
```
/usr/bin/python3 -E $B join $W/partition.json $W/batch_ownership $W/batch_ownership/mutated_seals.json $W/src/R3C2_CORPUS_MANIFEST.md $W/batch_ownership/joined_
```

P15:
```
/usr/bin/python3 -E $B join $W/partition.json $W/batch_extra $W/batch_extra/mutated_seals.json $W/src/R3C2_CORPUS_MANIFEST.md $W/batch_extra/joined_
```

P16:
```
/usr/bin/python3 -E $B join $W/partition.json $W/batch_root_chain $W/batch_root_chain/mutated_seals.json $W/src/R3C2_CORPUS_MANIFEST.md $W/batch_root_chain/joined_
```

P17:
```
/usr/bin/python3 -E $B join $W/partition.json $W/batch_collision $W/batch_collision/seals.json $W/src/R3C2_CORPUS_MANIFEST.md $W/batch_collision/joined_
```

Sixteen replacement entries, quoted as they now stand (line wrapping normalized; C = candidate, B = batch preparation). Kimi F6/F7 overlap Codex 8/13/14, so sixteen review entries do not imply sixteen distinct resulting sentences.

Codex 1 (C) — INACCURATE

> The reconciliation (`R3C2_CANDIDATE_REVIEW_RECONCILIATION_20260906.md`) lists the intended repairs by topic; revision 2 implemented many of them and this revision 3 implements the round-2 residuals (a seedless selection bypass, an import re-filed under another reason code, a symbol floor that failed open, join not checking orphan claims, input-id form or the predecessor chain, pin-sheet path form, counts, and the sentence replacements both reviewers required). Remaining limits are custody matters the clauses state as such.

Overclaims closure: printed counts and output vocabulary remain wrong; executable gaps are not solely custody.

Codex 2 (C) — ACCURATE

> For eligible imports the intended status, origin and value agree; the evidence records differ (which file and line `origin_evidence` names), and wording A needs the same explicit eligibility and locator rules before equivalence beyond these examples can be claimed.

Accurately limits equivalence; A remains unstaged.

Codex 3 (C) — ACCURATE

> Whether the quotation cites THAT value is seat judgement; the second seat and C6 may detect an error, but can share it, and C6 re-classifies inputs only for selected claims.

Accurate semantic and sampling limits.

Codex 4 (C) — INACCURATE

> Revision 2 added controls for these cases; round 2 found a seedless-selection bypass (a selection without a seed skipped recomputation and a zero-claim audit passed) and a vocabulary gap, repaired in revision 3 with their controls; census and seal authenticity also depend on custody.

Seedless case repaired; vocabulary only partly repaired: omission result strings still differ.

Codex 5 (C) — ACCURATE

> `CENSUS_COMPLETE` and `CENSUS_PARTIAL` then require a run record supporting enumeration before ledger exposure and re-derivation commitment before release, in addition to the repaired machine checks.

Accurate conditional run-record requirement, not evidence that a run occurred.

Codex 6 (C) — ACCURATE

> A PASS accompanied by satisfactory dispatch and release evidence supports the intended independent enumeration and blind re-derivation; shared error and prior exposure remain possible; it is bounded evidence, not proof of corpus completeness.

Accurately qualified.

Codex 7 (C) — ACCURATE

> **D7 in code** (`audit seal-enumeration | select | handout | seal-rederivation | compare`): implements the clause's stages; the exposure chronology itself is custody, verified by the dispatch and release record, not by these commands (`handout` reads the sealed candidates and therefore runs only in the custodian's hands).

Accurate as a description of stages and custody; does not establish full output-schema conformance.

Codex 8 (B) — ACCURATE

> Batch 1 is light but not the lightest (batches 9 and 11 are smaller on both measures); a light first batch confirms less about capacity than a heavy one would — a heavier first batch is the stronger pilot, at a higher risk of the failure it is testing for.

Merged with Kimi F6; pinned table confirms both smaller batches. Pilot comparison is a workload rationale, not a measured success probability.

Codex 9 (B) — ACCURATE

> The pinned partition implementation deterministically computes these bytes from this manifest and 12; identical serialization and implementation are required for byte equality (kimi recomputed it byte-identical with the pinned code).

Correct reproducibility qualification; Kimi attribution matches its prior report.

Codex 10 (B) — ACCURATE

> Whole-text ownership preserves a claim's local context; cross-batch imports are not blocked by withheld evidence if each dispatch supplies and verifies all manifest texts as required — a dispatch check recording the availability and byte verification of all 89 texts per session is part of the run plan, since final ownership coverage alone does not verify earlier reference access, and neither coverage nor join verifies the lookup logs.

Correct conditional access and logging limits.

Codex 11 (B) — ACCURATE

> The comparison code is unchanged; sections 1 and 3 require equivalent evidence access and global identifiers; dispatch checks and the repaired join must verify their implementation.

Accurate in context: batching uses the same audit comparator; not a claim that D7 code never changed between revisions.

Codex 12 (B) — ACCURATE

> Per-claim outcomes and classes use the operative rules explicitly accepted for this run, including any accepted D1/D2 changes, over the validated joined files.

Correctly names conditional operative rules instead of asserting V23 identity.

Codex 13 (B) — ACCURATE

> It is the difference between a census that could not run (one observed failure) and one that might — whether it can run is what batch 1 is designed to test.

Merged with Kimi F7; limits inference to the recorded failure and proposed test.

Codex 14 (B) — ACCURATE

> (Blocks a first run on the evidence of the limb-B death finding: the unbatched seat died; whether this batching is the remedy is what batch 1 tests; the principal may choose another workable execution design.)

No universal impossibility or exclusive-remedy claim remains.

Kimi F6 (B) — ACCURATE

> Batch 1 is light but not the lightest (batches 9 and 11 are smaller on both measures); a light first batch confirms less about capacity than a heavy one would — a heavier first batch is the stronger pilot, at a higher risk of the failure it is testing for.

Same merged replacement as Codex 8.

Kimi F7 (B) — ACCURATE

> It is the difference between a census that could not run (one observed failure) and one that might — whether it can run is what batch 1 is designed to test.

Same merged replacement as Codex 13; its second requested sentence is quoted under Codex 14.

Custody floor, directly quoted:

> the enumerated predicates held over the sealed files; it is bounded by the custodian's dispatch and release record (the seals fix WHAT was committed, the dispatch record — inventoried and access-proven like the seats' — fixes WHEN, relative to release) and by shared reader error; prior exposure cannot be excluded — the same floor C4 states for the seats.

P00 additionally confirms pinned batch 1 = 278483 bytes / 4030 nonblank lines, batch 9 = 198317 / 3799, batch 11 = 197654 / 3321. It confirms all sixteen quoted entries exist, and only the two closure claims remain inaccurate on this bounded review's evidence.

READY_FOR_PRINCIPAL=NO means the requested repaired-object condition is not met. These residuals are listed for Duho in this last bounded round; no further round, implementation change, adoption or scope expansion is proposed. D1 wording, D7 strength and batching remain the principal's choices.
