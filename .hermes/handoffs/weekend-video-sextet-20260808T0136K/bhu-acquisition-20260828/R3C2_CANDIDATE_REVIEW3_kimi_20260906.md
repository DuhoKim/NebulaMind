ACCESS_SHA=cd126c26b4a4218e2572999f15a07a909ee1bd45a83b3a3e99f51b1be7cd21ff
SEAT=kimi
ROUND2_RESIDUALS=PARTLY
NEW_DEFECTS=2
STAGED_TESTS=PASS
READY_FOR_PRINCIPAL=YES

# R3C2 candidate REVISION 3 — bounded verification round 3, seat kimi, 2026-09-06

Independent, adversarial, bounded verification of REVISION 3 of the UNADOPTED candidate, confined to the reconciliation's
round-2 table (each row probed with my own fixtures) plus new executable defects. My first act was the access-proof
command above (line 1 is its full digest). Read: the candidate, the batch preparation, the reconciliation, the two
round-2 reports (codex F1–F7/F.1–14, kimi F1–F8), the staged code and the kit. Not opened: R3C2_GATE_*, R3C2_C0_*,
the seat packet. All my fixtures/drivers/outputs are under `r3c2_staged_d1d7/_review3_kimi/` (`run_probes.py`,
`check_sentences.py`, `work/` with `command_log.json`, 33 commands, every rc and stdout). Nothing else written, with the
one mandated exception: the required kit run recreates `_ctl/` and rewrites `C6_COUNTEREXAMPLE_EXHIBIT.txt` (README
discloses it; the pin sheet verified 7/7 OK before and again AFTER all my runs — the exhibit regenerates byte-identical).
Nothing here adopts, freezes, installs or runs anything.

## A. Pin sheet and kit, run by me

```
$ shasum -a 256 -c r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256        (from the working directory)
r3c2_staged_d1d7/r3c2_ledger_tools_STAGED.py: OK
r3c2_staged_d1d7/r3c2_batch_tools_STAGED.py: OK
r3c2_staged_d1d7/r3c2_staged_tests.py: OK
r3c2_staged_d1d7/README_STAGED_UNADOPTED.md: OK
r3c2_staged_d1d7/partition_12_of_89.json: OK
r3c2_staged_d1d7/partition_12_of_89.txt: OK
r3c2_staged_d1d7/C6_COUNTEREXAMPLE_EXHIBIT.txt: OK                 (exit 0; paths are lane-relative, as the brief requires)

$ cd r3c2_staged_d1d7 && /usr/bin/python3 -E r3c2_staged_tests.py  (exit 0) — last three lines:
exhibit written: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/r3c2_staged_d1d7/C6_COUNTEREXAMPLE_EXHIBIT.txt
controls=102 passed=102 failed=0
STAGED_TESTS=PASS                                                  (line above those: deletion_probes=36)
```

## B. The round-2 table, row by row — my own probes (never the kit's fixtures)

Driver: `_review3_kimi/run_probes.py`; full log: `_review3_kimi/work/command_log.json`. D1 fixtures: my own sources
`k3borrow.txt` (citing sentence "We adopt q = 7 from k3src (2021)." at line 3), `k3src.txt` ("For this calculation we
choose q = 7." line 4, repeated line 5), `k3nosym.txt`, `k3split.txt`, my own manifest and candidate file. D7 fixtures:
my own sealed/auditor candidate, exclusion and ledger files. Batch fixtures: my own corpus `u1..u5.txt`, my own
manifest, partition and seat directory.

| row (round-2 residual) | verdict | my probe, command and output |
|---|---|---|
| 1. T6 — a selection WITHOUT `seed_hex` skipped recomputation; a zero-claim audit PASSED. Claimed repair: compare fails a seedless selection. | REPAIRED | Staged my own honest run (`audit seal-enumeration` → `select` → `handout` → `seal-rederivation` → `compare`, all rc=0, `C6_AUDIT_SAMPLE=PASS`). Then a selection minus `seed_hex`, ids emptied, digests retained: `audit compare … sel_noseed.json …` → rc=1, `FAIL: C6_SELECTION: selection carries no 64-hex seed; nothing to recompute against`, `C6_AUDIT_SAMPLE=FAIL`. The exact rev-2 attack no longer passes. Variant, seed retained but audit emptied: rc=1, three recomputation failures (`supplied k / sampled_ids / audited_ids differs from the recomputed selection`). A zero-claim audit cannot PASS anymore (N>0 ⇒ k≥1 or a non-empty arithmetic group; N=0 with rows ⇒ zero-denominator FAIL). |
| 2. T8 — an import re-filed CHOSEN under `ORIG_CHOICE_STATED` quoting the source's line bypassed every D1 check. Claimed repair: every PRINTED record bound first; a value line in another file must be IMPORTED/ORIG_CITATION. | REPAIRED | `validate d1_refiled_chosen.json d1src d1_cands.json` → rc=1: `FAIL: k3borrow.txt#1.q: value line is in k3src.txt but claim k3borrow.txt#1 belongs to k3borrow.txt: such a record must be IMPORTED with ORIG_CITATION (submitted CHOSEN/ORIG_CHOICE_STATED)`. Variant under FITTED/ORIG_FIT_STATED → rc=1, same binding message ("whatever reason code was submitted" holds). Honest import sanity: rc=0, `C3_NO_SUBSTITUTION=PASS`. Residual limit of this binding: new defect N1 below. |
| 3. T8 — the symbol floor failed OPEN when no line carried symbol and numeral. Claimed repair: fails when no such line exists. | REPAIRED | `validate d1_nosym.json …` (numeral 7 present, symbol q nowhere in the source) → rc=1: `FAIL: … no line of k3nosym.txt carries both q and 7`. Variant `d1_split.json` (symbol on one line, numeral on another, never together) → rc=1: `no line of k3split.txt carries both q and 7`. Fails closed. |
| 4. T8 — designated-locator tie-break described; the deterministic first-line rule landed undisclosed. Claimed repair: disclosed in the candidate's D1 section. | REPAIRED | Candidate lines 29–31: "**Disclosure (kimi round 2):** the reconciliation described a designated-locator tie-break with an `ORIGIN_DISPUTED` fallback; what landed is the deterministic first-line rule — no seat discretion, no `ORIGIN_DISPUTED` case, no others-listed requirement — a stricter rule, substituted here knowingly." `ORIGIN_DISPUTED` occurs nowhere else in the candidate and zero times in both staged tools and the batch document (grep). Executed: filing the SECOND of two matching lines → rc=1, `external value line 5 is not the first line of k3src.txt carrying both q and 7 (that is line 4)` — the code is the disclosed deterministic rule, no seat discretion. |
| 5. T2 — join never checked `input_id` form or that a ledger claim names an included candidate. Claimed repair: both checked. | REPAIRED | My own corpus/partition/seals (join positive: `JOIN=PASS`, `joined: batches=2 candidates=3 …`). Orphan: ledger record naming `u1.txt#77` → rc=1, `FAIL: batch 1: ledger record u1.txt#1.a names claim u1.txt#77, not an included candidate of this batch`, `JOIN=FAIL`. Input-id: record `input_id="i1"` under claim `u1.txt#1` → rc=1, `FAIL: batch 1: input_id i1 does not begin with its claim's file followed by #`, `JOIN=FAIL`. |
| 6. T11 — join did not verify the predecessor chain or the sealed ownership fields against the partition; extra seals unnoticed. Claimed repair: all three verified. | REPAIRED | (a) batch-2 predecessor digest zeroed → rc=1, `FAIL: batch 2: predecessor chain broken (seal does not bind batch 1's seal)`. (b) batch-1 sealed `owned_files` altered → rc=1, `FAIL: batch 1: sealed ownership differs from the partition` AND `batch 2: predecessor chain broken` (the tampered record changes the recomputed predecessor — correct coupling). (c) an added seal for batch 3 → rc=1, `FAIL: seals for batches not in the partition: ['3']`. Bonus: a deleted batch-2 seal → `FAIL: batch 2: not sealed`. |
| 7. T3 — code emitted `MATCH_KIND_DIFFERS`, unnamed by the clause; `study_files` absent from the artefact. Claimed repair: code emits MATCH with both kind fields; artefact states what the study files. | REPAIRED (two limits stated) | `MATCH_KIND_DIFFERS`: zero occurrences in the staged tool (grep). Executed: sealed excludes a passage as DATE, the auditor excludes the same passage as REFERENCE_NUMBER → completeness row `{"key":["r3b.txt",1,"2020"], "result":"MATCH", "sealed_kind":"DATE", "audit_kind":"REFERENCE_NUMBER", "sealed_included":false, "audit_included":false}` — MATCH with both kind fields, not a fourth result. `study_files` executed both ways: `"none"` on my PASS artefact, `"CENSUS_AUDIT_FAILED"` on my seedless-FAIL artefact. Limits not claimed by this row and still true (round-2 codex F2's other two points): the clause's literal result token `OMISSION` is emitted as the compound `OMISSION_<direction>` forms, and per-input origin agreement is aggregated into each claim's `why` array rather than emitted as per-input MATCH/MISMATCH rows. |
| 8. T13 — pin sheet kit-relative while the brief said lane-relative; probe counts wrong; id-collision check had no control. Claimed repair: lane-relative sheet; counts from the kit's own tally; id-collision control + probe. | PARTLY | Pin sheet: lane-relative paths, verifies 7/7 OK from the working directory (section A). Counts, counted by me: `grep -c "^probe(" r3c2_staged_tests.py` = 36; `check(` calls = 62 (3 col-0 + 59 inline); manual `results.append` = 4; 36+62+4 = 102 = the kit's printed `controls=102 passed=102 failed=0`, `deletion_probes=36` — the kit's tally is true, and the batch document and README print 102/36 correctly. Id-collision: control + probe exist in the kit, and my own collision probe → rc=1, `FAIL: candidate_id collision across batches: u4.txt#1`. PARTLY because the CANDIDATE's own test-run bullet still prints the revision-2 count: `controls=84 passed=84 failed=0` (candidate line 161) beside the correct "36 deletion probes" — the stale-count family survived in one place in the revision that repaired it. |
| 9. T12 — the sixteen sentence replacements (codex F.1–14; kimi F6/F7, merged where both addressed one sentence). Claimed repair: all applied verbatim or merged. | REPAIRED (one sentence partly inaccurate) | All fourteen old forms are absent from both documents (whitespace-normalized search, count 0 each); all sixteen replacement slots landed (14 distinct sentences; kimi F6 merges onto codex F.8, kimi F7's two quotes merge onto codex F.13/F.14). Each as it now stands, with my accuracy judgement: (1) header: "The reconciliation … lists the intended repairs by topic; revision 2 implemented many of them and this revision 3 implements the round-2 residuals (a seedless selection bypass, an import re-filed under another reason code, a symbol floor that failed open, join not checking orphan claims, input-id form or the predecessor chain, pin-sheet path form, counts, and the sentence replacements both reviewers required). Remaining limits are custody matters the clauses state as such." — PARTLY INACCURATE: the "counts" residual is not fully repaired (row 8: `controls=84` survives at line 161 of this same document), so "remaining limits are custody matters" is one misprint short of true. (2) "For eligible imports the intended status, origin and value agree; the evidence records differ (which file and line `origin_evidence` names), and wording A needs the same explicit eligibility and locator rules before equivalence beyond these examples can be claimed." — accurate. (3) "Whether the quotation cites THAT value is seat judgement; the second seat and C6 may detect an error, but can share it, and C6 re-classifies inputs only for selected claims." — accurate. (4) "Revision 2 added controls for these cases; round 2 found a seedless-selection bypass (a selection without a seed skipped recomputation and a zero-claim audit passed) and a vocabulary gap, repaired in revision 3 with their controls; census and seal authenticity also depend on custody." — accurate (rows 1, 7 verify the repair half; the custody half is the stated floor). (5) "`CENSUS_COMPLETE` and `CENSUS_PARTIAL` then require a run record supporting enumeration before ledger exposure and re-derivation commitment before release, in addition to the repaired machine checks." — accurate. (6) "A PASS accompanied by satisfactory dispatch and release evidence supports the intended independent enumeration and blind re-derivation; shared error and prior exposure remain possible; it is bounded evidence, not proof of corpus completeness." — accurate. (7) "D7 in code (audit seal-enumeration \| select \| handout \| seal-rederivation \| compare): implements the clause's stages; the exposure chronology itself is custody, verified by the dispatch and release record, not by these commands (`handout` reads the sealed candidates and therefore runs only in the custodian's hands)." — accurate (stages verified in rows 1 and 7; `cmd_audit_handout(sel, sc, out)` does read the sealed candidates file, code lines 252–256). (8) batch: "Batch 1 is light but not the lightest (batches 9 and 11 are smaller on both measures); a light first batch confirms less about capacity than a heavy one would — a heavier first batch is the stronger pilot, at a higher risk of the failure it is testing for." — accurate against the document's own table (batch 1: 4030 lines/278483 bytes; batch 9: 3799/198317; batch 11: 3321/197654). (9) "The pinned partition implementation deterministically computes these bytes from this manifest and 12; identical serialization and implementation are required for byte equality (kimi recomputed it byte-identical with the pinned code)." — accurate. (10) "Whole-text ownership preserves a claim's local context; cross-batch imports are not blocked by withheld evidence if each dispatch supplies and verifies all manifest texts as required — a dispatch check recording the availability and byte verification of all 89 texts per session is part of the run plan, since final ownership coverage alone does not verify earlier reference access, and neither coverage nor join verifies the lookup logs." — accurate. (11) "The comparison code is unchanged; sections 1 and 3 require equivalent evidence access and global identifiers; dispatch checks and the repaired join must verify their implementation." — accurate. (12) "Per-claim outcomes and classes use the operative rules explicitly accepted for this run, including any accepted D1/D2 changes, over the validated joined files." — accurate. (13) "It is the difference between a census that could not run (one observed failure) and one that might — whether it can run is what batch 1 is designed to test." — accurate. (14) "(Blocks a first run on the evidence of the limb-B death finding: the unbatched seat died; whether this batching is the remedy is what batch 1 tests; the principal may choose another workable execution design.)" — accurate. |
| 10. T7 — exposure chronology is custody; `handout` runs only in custody. Claimed repair: stated in the candidate; run-plan additions for the run plan, not the clause. | REPAIRED | Candidate, "What PASS means": "the enumerated predicates held over the sealed files; it is bounded by the custodian's dispatch and release record (the seals fix WHAT was committed, the dispatch record — inventoried and access-proven like the seats' — fixes WHEN, relative to release) and by shared reader error; prior exposure cannot be excluded — the same floor C4 states for the seats." And the D7-in-code bullet: "the exposure chronology itself is custody, verified by the dispatch and release record, not by these commands (`handout` reads the sealed candidates and therefore runs only in the custodian's hands)". The code fact is true (row 9, sentence 7). The floor is stated as a limit, which is what this row's repair required. |

Whole-table judgement: PARTLY — nine rows REPAIRED, row 8 PARTLY (one stale count survives inside the candidate), and
row 9's sentence 1 inherits that inaccuracy. No claimed repair was found absent; no round-2 attack I rebuilt still passes.

## C. New executable defects (my own counterexamples; both executed against the staged code)

N1. The D1 floor's "For EVERY PRINTED record validate first binds the claim to its claiming file" has an executable
exception for claims absent from the candidate file. `cmd_validate` binds only when `claim_file.get(claim_id)` is not
None (r3c2_ledger_tools_STAGED.py:126–129); a non-import PRINTED record whose claim_id is NOT a candidate row skips the
binding and falls into the ordinary same-file path, which checks the verbatim and value at the record's own cited line
and nothing else. My counterexample: record `ghost.txt#9.q` (claim `ghost.txt#9`, not in my candidate file), origin
CHOSEN / ORIG_CHOICE_STATED, value line `k3src.txt:4` — a DIFFERENT file from any claiming paper — → rc=0,
`C3_NO_SUBSTITUTION=PASS`. Contrast: the same unknown claim filed as IMPORT fails (`claim ghost.txt#9 is not a candidate
row`) — the import branch fails closed, the non-import branch does not. So the re-filed-import repair (row 2) is
complete only for KNOWN claims; an unknown-claim CHOSEN record with a cross-file value line still passes, the same
provenance-tally corruption codex's F4 named, by a different door. Reachability: in the BATCHED flow the repaired join
backstops it (my row-5a probe: a ledger record naming a non-included claim fails `JOIN=FAIL` before the joined
validate); the UNBATCHED validate path has no such backstop (census reads candidates/exclusions only). Minor, executable,
not in any round's table. Stated for Duho, not repaired (round-3 rule).

N2. `audit compare` validates the selection's seed by type and length only, then crashes on non-hex input.
r3c2_ledger_tools_STAGED.py:270 requires `isinstance(seed,str) and len==64`; a selection carrying `seed_hex="Z"*64`
passes that check and dies at line 242 (`int(seed_hex,16)`) with an uncaught `ValueError: invalid literal for int()
with base 16` — rc=1, NO `FAIL:` line, NO `C6_AUDIT_SAMPLE` token, and NO `C6_AUDIT.json` written (the artefact is
written only after recomputation). It fails closed, but by traceback, not by the clause's "fails on any disagreement"
contract: a wrapper keyed on the artefact or the token sees an absent result rather than a FAIL, and a hand-crafted
selection is exactly the input compare exists to distrust. `cmd_audit_select` already validates hexness for its own seed
argument (line 248); compare does not. One conjunct fixes it. Minor, executable, not in any round's table. Stated for
Duho, not repaired (round-3 rule).

## What the principal rules on, with the remaining limits stated as limits

An examined object: every claimed repair in the round-2 table was probed with my own fixtures (33 logged commands), the
pin sheet verifies lane-relative before and after my runs, the kit prints `controls=102 passed=102 failed=0`,
`deletion_probes=36`, `STAGED_TESTS=PASS`, and my independent recount reproduces 102 = 62 checks + 36 probes + 4 manual
assertions. Repaired: every round-2 attack I rebuilt now fails. The remaining limits, stated as limits (here, and for
the candidate's own text where flagged): (i) one stale number inside the candidate (`controls=84`, line 161) — the T13
family, documentary only, no executable predicate affected; (ii) N1 — unknown-claim non-import records escape the D1
binding (backstopped by join in the batched flow); (iii) N2 — non-hex 64-char seed crashes compare instead of a clean
FAIL (fails closed anyway); (iv) the clause's literal `OMISSION` token is emitted as compound `OMISSION_<direction>`
forms and per-input origin agreement is aggregated in `why` arrays (round-2 codex F2 points not claimed by revision 3);
(v) the custody floor itself — PASS is bounded by the dispatch and release record, which the candidate states. Nothing
here re-litigates Duho's recorded choices (D1 wording A vs B, D7 stronger vs weaker, batching itself) and nothing
proposes new scope. Per the round-3 frame, residuals are listed for Duho, not repaired; this is the last review round
unless ordered otherwise. READY_FOR_PRINCIPAL=YES on that basis.

R3C2_CANDIDATE_REVIEW3_kimi — UNADOPTED-REVIEW
