# R3C2 — reconciliation of the independent reviews of the UNADOPTED candidate (started 2026-09-06 20:27 KST)

Reviewed object: `R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md` at digest `cb78eef0f4167759a415b5381b73fd075bb5475172e5290afa24d9a1c3820cfe`,
with `R3C2_BATCH_PREPARATION_UNADOPTED_20260906.md` and the staged kit (pin sheet `r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256`).
Reviews: codex (`R3C2_CANDIDATE_REVIEW_codex_20260906.md`, access proven by the wrapper; report written 20:14 KST; exit not observed by
the lane — Blanc observed the wrapper and children alive at 20:17:11 and gone by 20:27:10; the lane read the report after its own
process check showed the wrapper absent); kimi (pending at the time of
writing; added below when it exits and its access line is verified). Nothing here adopts anything; all repairs listed are STAGED
preparation of an unadopted candidate. Findings are reconciled BY TOPIC; report numbering is the reviewer's and is not relied on.

## Codex tokens (verbatim)
CANDIDATE_D1=SOUND_WITH_REPAIRS · CANDIDATE_D7=SOUND_WITH_REPAIRS · BATCH_PREP=UNSOUND · TOOLING_MATCHES_CLAUSE=NO ·
COUNTEREXAMPLE_HANDLED=YES · IMPORTED_RULE_BREAKS_PARTITION=YES · STAGED_TESTS=PASS (kit re-run by the reviewer, 44/44; pins OK before and after).

Codex's own both-seats-omit counterexample (its synthetic `results.txt` line 2, "we report our own calculated result: the dimensionless
yield is 73", omitted by both of its seat files, present in its auditor file) → `audit_included_absent_from_sealed: [["results.txt", 2, "73"]]`,
`C6_AUDIT_SAMPLE=FAIL`; the reverse → `sealed_included_absent_from_audit_enumeration`, FAIL. Codex: "My COUNTEREXAMPLE_HANDLED=YES must
not be read as TOOLING_MATCHES_CLAUSE=YES." Agreed.

## Topic map and disposition (class: CLAUSE = candidate text; TOOL = staged code/kit; CUSTODY = dispatch/custody, not a clause; WORDING = overclaim; STALE = citation)

| # | topic | class | disposition |
|---|---|---|---|
| T1 | **Batch partition breaks §2's IMPORTED rule** — a session holding ONLY its batch's texts cannot read a named source's value line that lives in another batch; codex executed it (borrower in batch 1, source in batch 2: the same D1 record validates with both texts present and fails with only batch 1's) | CLAUSE (batch) | **ACCEPTED, the decisive finding.** Batch proposal as written is UNSOUND. Repair to stage: a batch partitions OWNERSHIP of candidate passages, not ACCESS to evidence — every session's working directory holds all 89 pinned texts plus an ownership list; the seat enumerates only its owned texts (reading load unchanged) and may look up any manifest text for §2/D1, every lookup logged; nothing becomes BLOCKED because dispatch withheld a text; coverage checks ownership exactly once. Same rule for both seats and the auditor. |
| T2 | **Join corrupts cross-batch `derived_from`** (`b2_i1` → `b1_b2_i1`, JOIN passed) and validates no graph | TOOL + CLAUSE (batch) | ACCEPTED. Repair: globally unique source-based ids preregistered (`<file>#<local>`), join does not prefix, rejects unresolved references, collisions and cycles, and the lane's `validate` runs over the joined ledger against the full manifest. |
| T3 | **`compare` narrower than the clause** — only INCLUDED passages are searched for absence; one-sided EXCLUDED candidates vanish; no per-key disposition | TOOL + CLAUSE (D7) | ACCEPTED. Repair: compare the union of all keys; emit per key both presences, both dispositions, both kinds, MATCH / OMISSION / AUDIT_INCLUSION_DISPUTED; included-omission either side fatal; one-sided excluded reported separately, NOT fatal (codex's proposed resolution, adopted explicitly in the clause and tested). |
| T4 | **Zero denominator** passes with a dispute; disputed rows lack both dispositions | TOOL | ACCEPTED. N=0 with any candidate on either side → FAIL; disputed rows carry both dispositions and the token. |
| T5 | **Auditor `census` PASS not enforced** by any audit subcommand | TOOL | ACCEPTED. `seal-enumeration` runs census over the auditor's files and refuses on FAIL; the seal records the census output digest. |
| T6 | **Selection trusted, not recomputed**; `select` needs no stage-1 seal; edited `audited_ids=[]` passed | TOOL | ACCEPTED. `select` refuses without a stage-1 seal; `compare` recomputes N, groups, k, sample and audited ids from the sealed candidates and seed and fails on any disagreement; stage-1 seal is first-write (refuses overwrite). |
| T7 | **Source-only independence is procedural**; channel classes the kit cannot close (pre-placed ledgers, reused context, premature select output, unsealed re-derivations, replaceable seal, runtime surfaces) | CUSTODY (+ TOOL for three items) | ACCEPTED as stated: the clause promises custody, code cannot prove it. Tool side staged: first-write seals, a `handout` that prints ids+file+line only, `seal-rederivation` committing the auditor's re-derivations by digest before release. Custody side: the dispatch record must list the auditor's inventory, profile, probes and release events — for the run plan, not the clause; and the candidate must say that PASS is bounded by custody. |
| T8 | **D1 code weaker than its claim** — value is a substring ("2" matches "b = 20"); `enumerable()` accepts any backticked mention or any file when the manifest is absent; no source-byte check; evidence file not bound to the claiming paper (an import re-filed CHOSEN quoting the source's choice sentence passes); empty quotation passes | TOOL + CLAUSE (D1) | ACCEPTED. Repair: numeric-token match with the symbol on the line; manifest required, exact row membership, source bytes verified against the row's sha256; `validate` takes the candidate file and binds each claim to its claiming file, evidence file must be that file, quotation non-empty; clause adds the multi-occurrence rule (the locator the borrower designates; otherwise the first line carrying symbol and numeral, the others listed; seats disagreeing → ORIGIN_DISPUTED as already defined). |
| T9 | **D1 wordings not identical in filings** (evidence bytes differ; codex: adopt the borrower-evidence wording as the single operative rule) | CLAUSE (D1) | ACCEPTED: the candidate's sentence "reaches the same filings" is replaced by "assign the same origin; their evidence records differ"; the borrower-evidence wording stays the recommendation; the choice stays Duho's. |
| T10 | **D1 consequence paragraph overstates** (import availability ≠ arithmetic success; transitive provenance visibility unpromised) | WORDING | ACCEPTED, replacements applied verbatim. |
| T11 | **Seals do not bind partition or order**; coverage does not verify source bytes; "join has no parameters" | TOOL + WORDING (batch) | ACCEPTED. Seal binds partition digest, source digests, predecessor seal, order; refuses out-of-order; coverage verifies each owned text's bytes against the manifest; wording of what seals prove reduced to what they prove. |
| T12 | **D7 / batch overclaims** ("strongest statement", "guaranteed", cost "roughly equals", drift "measured", "nothing about the claims", feasibility of 12 batches) | WORDING | ACCEPTED, replacements applied; 12 batches restated as a workload hypothesis with per-batch line/byte counts printed. |
| T13 | **Stale pins in the batch document** (cites the pre-repin tool digest and 37 controls) | STALE | ACCEPTED, corrected. |

## Kimi tokens (verbatim; access line verified by hand against the candidate digest; report written 20:26 KST; exit not observed —
Blanc observed the process alive at 20:27:10 and absent by 20:32–20:35; the lane read the report after a process check showed count 0)
CANDIDATE_D1=SOUND_WITH_REPAIRS · CANDIDATE_D7=SOUND_WITH_REPAIRS · BATCH_PREP=UNSOUND · TOOLING_MATCHES_CLAUSE=NO ·
COUNTEREXAMPLE_HANDLED=YES · IMPORTED_RULE_BREAKS_PARTITION=YES · STAGED_TESTS=PASS — identical to codex's seven.
Kimi's own counterexample (its `paperY.txt:4` numeral `17.4`, "We obtain w = 17.4 from the fit.", omitted by both of its seat files,
retained by its auditor) → `audit_included_absent_from_sealed`, FAIL; reverse → FAIL. Kimi verified the pin sheet before and after its
run, the partition byte-identical on recomputation, and the deletion probes.

## Kimi findings mapped to the topics above (their numbering is theirs)
| kimi | topic | note |
|---|---|---|
| F1 (two wordings ≠ same filings; tool implements the review's only) | T9 | accepted; the candidate now says so in its first paragraph |
| F2 (no tie-break at multiple matching lines) | T8 | accepted; first line carrying symbol and numeral, enforced |
| F3 (claiming paper not machine-bound; third-text quotation passes) | T8 | accepted; bound through the candidate file; floor stated |
| F4 (auditor census PASS not enforced) | T5 | accepted; seal is census-gated |
| F5 (re-derivations unsealed; MATCH manufacturable) | T7 (tool part) | accepted; `seal-rederivation`, first-write, checked in compare |
| F6 (excluded-only asymmetries vanish) | T3 | accepted with KIMI'S reading of the two excluded cases (stricter than codex's proposal) |
| F7 ("both sealed ledgers" vs the merged object) | T3 | accepted; the clause names the sealed (merged) ledgers |
| F8 (stage-1 seal ≠ proof of precedence; restate the C4 floor) | T7 (custody part) | accepted; the clause states what PASS means and the floor |
| F9 (IMPORTED rule breaks the partition; join ignores ledger citations) | T1, T2 | accepted; ownership-not-access; ledger evidence checked at join; full-corpus validate |
| F10 (stale pins and counts in both documents) | T13 | accepted; documents cite the pin sheet only |
| F11 ("cannot alter" → detection, not prevention) | T11 | accepted, replacement applied |
| F12 (12 batches untested; batch-1 confirmation) | T12 | accepted, replacement applied |
| F13 (audit re-derivation under batching unspecified) | T1 | accepted; stated in both documents |
| F14 (engine wording ambiguous) | T12 | accepted, replacement applied |
| F15 ("strongest statement in the design") | T12 | accepted, kimi's replacement applied |
| F16 (partition .txt unpinned) | T13 | accepted; pinned |

## Convergence
Two engines, no shared context, identical tokens; every substantive finding of one is found by the other (T1, T3, T5, T6/T7, T8, T13)
or is a sharper statement of the same topic. No finding of either was rejected. The one place the two proposed different resolutions
(one-sided EXCLUDED passages: codex "report, not fatal"; kimi "auditor-excluded-absent is fatal, sealed-excluded-absent is a dispute")
was resolved by taking the stricter reading, stated explicitly in the clause and tested both ways.

## Repairs applied (2026-09-06 20:38 KST) — all STAGED, nothing adopted
Candidate revision 2 (`R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md`), batch preparation revision 2, staged kit re-pinned
(`r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256`): `controls=84 passed=84 failed=0`, `STAGED_TESTS=PASS`, 29 deletion probes.
A second independent review round is dispatched on revision 2; its verdicts are filed beside the first when they exist.

## Round 2 (revision 2, digest `53fa3ab5…`; codex: wrapper access proven, report written 20:46 KST, lane check at 20:49 showed the wrapper absent;
kimi: report written 21:11 KST, the lane's process check printed count 0 at 21:12 while Blanc observed it alive at 21:12:10 and absent
by 21:13:40 — the lane's read followed that check; access line verified by hand)
Tokens, identical from both: CANDIDATE_D1=SOUND_WITH_REPAIRS · CANDIDATE_D7=SOUND_WITH_REPAIRS · **BATCH_PREP=SOUND_WITH_REPAIRS** ·
TOOLING_MATCHES_CLAUSE=NO · COUNTEREXAMPLE_HANDLED=YES · **IMPORTED_RULE_BREAKS_PARTITION=NO** · STAGED_TESTS=PASS.
Both re-ran the kit (84/84), rebuilt their own counterexamples, and checked T1–T13: T1, T4, T5, T9, T10 REPAIRED by both; the rest
PARTLY, for the residuals below. No finding rejected.

| topic | residual (round 2) | found by | repair in revision 3 |
|---|---|---|---|
| T6 | a selection WITHOUT `seed_hex` skipped recomputation; a zero-claim audit PASSED (executed by both) | codex F1, kimi F2 | compare fails a seedless selection; control + probe |
| T8 | an import re-filed CHOSEN under `ORIG_CHOICE_STATED` quoting the source's line bypassed every D1 check | codex F4 | for every PRINTED record the claim is bound first; a value line in another file must be IMPORTED/ORIG_CITATION; control + probe |
| T8 | the symbol floor failed OPEN when no line carried symbol and numeral | codex F5, kimi F3 | fails when no such line exists; control + probe |
| T8 | reconciliation described a designated-locator tie-break; the deterministic first-line rule landed undisclosed | kimi F8 | disclosed in the candidate's D1 section |
| T2 | join never checked `input_id` form or that a ledger claim names an included candidate | codex F6 | both checked; controls + probes |
| T11 | join did not verify the predecessor chain or the sealed ownership fields against the partition; extra seals unnoticed | codex F7 | all three verified; controls + probes |
| T3 | result vocabulary: code emitted `MATCH_KIND_DIFFERS`, unnamed by the clause; `study_files` absent from the artefact | kimi F5, codex F2 | code emits MATCH with both kind fields; artefact states what the study files |
| T13 | pin sheet regressed to kit-relative paths while the brief said lane-relative; probe counts wrong (27 not 29; "eight" checks = seven; id-collision check had no control) | codex A, kimi F1/F4 | lane-relative sheet; counts printed from the kit's own tally; id-collision control + probe |
| T12 | fourteen sentence replacements (codex) and two (kimi F6/F7) — "every accepted repair is in this revision", "caught by the second seat", "as the clause states", "Batch 1, the lightest", "a census that can run … which batch 1 will be", "no seat completes", "exactly as V23 states", "must get the same bytes", "which §1 and §3 supply" | codex F.1–14, kimi F6/F7 | all applied verbatim or merged where both addressed one sentence |
| T7 | exposure chronology is custody: the tools commit bytes, the dispatch/release record fixes WHEN; `handout` reads the sealed candidates so it runs only in custody | codex D, kimi D | stated in the candidate; run-plan additions listed (inventory + probes per dispatch, fresh auditor context, custodian-only selection, release events recorded against both commitments) — for the run plan, not the clause |

Kit after revision-3 repairs: `controls=102 passed=102 failed=0`, `deletion_probes=36`, `STAGED_TESTS=PASS` (2026-09-06 21:16 KST).

## Round 3 (bounded verification of revision 3, digest `cd126c26…`; codex report written 21:22 KST, wrapper absent at the lane's 21:25
check; kimi report written 21:39 KST, process count 0 at the lane's 21:40 check; both access lines verified)
Tokens: codex ROUND2_RESIDUALS=PARTLY, NEW_DEFECTS=3, STAGED_TESTS=PASS, READY_FOR_PRINCIPAL=NO; kimi ROUND2_RESIDUALS=PARTLY,
NEW_DEFECTS=2, STAGED_TESTS=PASS, READY_FOR_PRINCIPAL=YES. **Unique new defects: THREE** (N1 and N2 found by both; N3 by codex alone) — not five;
Blanc's 21:53 correction of his own earlier count is recorded here. The readiness split (codex NO / kimi YES) was recorded on
revision 3; whether it survives revision 4 is not settled — no readiness token exists on revision 4; Codex's targeted replay
(`.hermes/CODEX_TORI_R4_TARGETED_CLOSURE_20260906.json`) closed its own round-3 counterexamples, which is narrower than a review. Rows: every round-2 repair found PRESENT by both; PARTLY rows and new
defects, all routine and all REPAIRED in revision 4 under Blanc's 21:26 order (which withdrew the "residuals are listed, not repaired"
rule: routine, mechanical and wording residuals are repaired under preparation scope; only what changes what the census can conclude
goes to Duho — nothing in this round does):

| finding | by | class | repair in revision 4 (each with a control asserting its exact failure and a deletion probe) |
|---|---|---|---|
| N1 — the claiming-file binding ran only when a candidate file was given AND the claim was known; an unknown-claim non-import PRINTED record with a cross-file value line passed | codex N1, kimi N1 | mechanical | every PRINTED record now requires the candidate file and a known claim before anything else |
| N2 — `compare` accepted an uppercase seed `select` refuses; a non-hex seed crashed with a traceback and no artefact | codex N2, kimi N2 | mechanical | `compare` applies `select`'s contract; a FAIL token and an artefact are always written |
| N3 — join never checked that the root seal (batch 1) has no predecessor | codex N3 | mechanical | root check added |
| omission results emitted as `OMISSION_<direction>`; per-input origin agreement aggregated in `why` | codex T3, kimi (iv) | vocabulary | `result` ∈ {MATCH, OMISSION (+`direction`), AUDIT_INCLUSION_DISPUTED}; per-input rows with MATCH/MISMATCH |
| stale `controls=84` inside the candidate | both | stale count | printed from the kit's tally: `controls=111`, `deletion_probes=38` |
| codex sentence 1 and 4 inaccurate (closure overclaimed) | codex | wording | rewritten to name round 3's findings and their repair |

**Packaging defect and its fix (2026-09-06 21:53 KST).** The README was edited (revision-4 counts) AFTER the pin sheet had been generated, so the
sheet's README row failed (expected `1333de06…`). Fix chosen: the pin sheet was REGENERATED from the current bytes, not the README
restored, because the current README is the intended one (its counts are the kit's own tally) and the recorded digest was of the
superseded text; 7/7 verify from the lane directory after all document writes. Rule from here: pin last, after every document write.

Kit after revision 4: `controls=111 passed=111 failed=0`, `deletion_probes=38`, `STAGED_TESTS=PASS` (2026-09-06 21:45 KST).

**Timing errata (Blanc 21:26).** A report's write time is not its author's exit time. Every "exited HH:MM" above is now stated as a
write time plus an observed process absence (whose, when) or "exit not observed". The discipline the lane applies is unchanged: a
report is read only after a process check shows the reviewer absent; the record now says what was observed rather than a time.

**What goes to Duho from these three rounds.** Nothing new. D1 (wording B recommended; A needs the tool re-staged), D7 (stronger
recommended), the batch choice (ownership-partitioned; row-order vs line-balanced partition), the inherited-provenance "change" route —
each with its cost and the lane's recommendation, already in the candidate and batch documents. Custody limits are stated as limits,
not as decisions.

## What stays Duho's after these repairs
D1 (which wording; or the inherited-provenance change), D7 (stronger / weaker), the batch choice (now: ownership-partition, with the
T1 repair), any version fingerprint, the run word. The repairs above change the CANDIDATE and the STAGED kit only.
