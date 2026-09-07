import pathlib,json
W=pathlib.Path(__file__).resolve().parent; H=W.parent; lane=H.parent
results=json.loads((W/'results.json').read_text()); sentences=json.loads((W/'sentence_results.json').read_text())
head='''ACCESS_SHA=cd126c26b4a4218e2572999f15a07a909ee1bd45a83b3a3e99f51b1be7cd21ff
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
'''
mapping=[('P01','d1_no_symbol'),('P02','d1_refiled'),('P03','d1_refiled_no_candidates'),('P04','d1_refiled_unbound_claim'),('P05','audit_compare'),('P06','d1_designated_second'),('P07','seedless'),('P08','omission_compare'),('P09a','uppercase_seed'),('P09b','select_uppercase'),('P09c','nonhex_seed'),('P10','join_positive'),('P11','join_orphan'),('P12','join_input_form'),('P13','join_chain'),('P14','join_ownership'),('P15','join_extra'),('P16','join_root_chain'),('P17','join_collision')]
for label,key in mapping:
    cmd=results[key]['command'].replace(str(W),'$W').replace(str(H/'r3c2_ledger_tools_STAGED.py'),'$L').replace(str(H/'r3c2_batch_tools_STAGED.py'),'$B')
    head+='\n'+label+':\n```\n'+cmd+'\n```\n'
head+='\nSixteen replacement entries, quoted as they now stand (line wrapping normalized; C = candidate, B = batch preparation). Kimi F6/F7 overlap Codex 8/13/14, so sixteen review entries do not imply sixteen distinct resulting sentences.\n'
for label,doc,q,ok,why in sentences:
    head+='\n'+label+' ('+doc+') — '+('ACCURATE' if ok else 'INACCURATE')+'\n\n> '+q+'\n\n'+why+'\n'
head+='''
Custody floor, directly quoted:

> the enumerated predicates held over the sealed files; it is bounded by the custodian's dispatch and release record (the seals fix WHAT was committed, the dispatch record — inventoried and access-proven like the seats' — fixes WHEN, relative to release) and by shared reader error; prior exposure cannot be excluded — the same floor C4 states for the seats.

P00 additionally confirms pinned batch 1 = 278483 bytes / 4030 nonblank lines, batch 9 = 198317 / 3799, batch 11 = 197654 / 3321. It confirms all sixteen quoted entries exist, and only the two closure claims remain inaccurate on this bounded review's evidence.

READY_FOR_PRINCIPAL=NO means the requested repaired-object condition is not met. These residuals are listed for Duho in this last bounded round; no further round, implementation change, adoption or scope expansion is proposed. D1 wording, D7 strength and batching remain the principal's choices.
'''
report=lane/'R3C2_CANDIDATE_REVIEW3_codex_20260906.md'
report.write_text(head)
print(head)
