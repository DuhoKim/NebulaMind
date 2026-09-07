# INPUT CONTRACT FOR THE TRIMMED SELECTION PATH — owner decisions (2026-09-07 10:59 KST)
The bounded selection author STOPPED rather than guess on two gaps in my brief, which is the correct behaviour and is recorded as such (`_tmp_v35_selection_REPORT.md`). Both are mine to decide; here they are.

**1. Every pinned input is passed with its expected digest, and a mismatch refuses.** Signature:
`select(eligible_ids_path, eligible_sha256, exclusion_path, exclusion_sha256, failed_set_path, failed_sha256, seed_hex, sizes=(400,200,2000), floors=(380,190,1900))`
Each file's sha256 is recomputed on read and compared with the value passed in; any mismatch, absence or malformation RAISES. No default digests, no "verify if supplied" — the caller states what it expects or the call refuses.

**2. Eligibility is an INPUT, not something the selection path re-derives.** The trimmed path consumes a pinned ELIGIBLE-ID FILE (one GZ1_OBJID per line, ascending, no duplicates) produced by the existing documented renderability procedure — the survey-bricks half-open brick test and the no-r registry stay exactly where they are and are NOT reimplemented here.
Why this is the right simplification, not a loss: eligibility stays explicit and checkable (a file anyone can diff, with a digest in the manifest), its derivation keeps its existing provenance, the selection path has one job, and the run path no longer depends on the large catalogue inputs that the review sandbox could not even stage (the three suites that could not run at V33). What the reader gives up: the eligibility file's correctness is established by the procedure that made it, not re-proved at selection time — so **the eligibility file and its digest must be in the amendment's input manifest and fixed before the seed round is named**.

CONSEQUENCE FOR THE AMENDMENT (`AGREEMENT_RUN_AMENDMENT_A1_20260907.md`, drafted before this decision): its eligibility clause currently derives renderability inline from the survey-bricks table. It must instead name the eligibility FILE + digest as a pinned input, with the derivation cited as its provenance. That is a bounded follow-up edit, not a re-draft.

The amendment author's eight open questions stand as open questions for the independent review — none is answered by guessing here.

## 3. THE THIRD INPUT'S FORMAT, decided from the files themselves (2026-09-07 11:20 KST)
The selection author asked whether the exclusion and failed-set files share the eligible-id file's one-ID-per-line format. Checked against the real artefacts rather than assumed:
- **Exclusion**: `_optionA_dev/corpus_identity/dryrun_identities_to_exclude_20260905.txt` — 2,644 lines, ONE GZ1_OBJID PER LINE, sha256 `77b29eafe18e02d4dee621a6e748e8f698381c6e23098e7db2db190aee270c95` (recomputed here, equal to V15's pin). The author's assumption HOLDS.
- **Failed set**: it does NOT. It lives in `VALIDATION_SELECTION_V29_20260905.csv`, a CSV with a header and columns `GZ1_OBJID,RA,DEC,G,DR9N_BRICK`.
DECISION, for uniformity with the eligibility decision: **all three selection inputs are pinned one-ID-per-line files.** The failed-set input is a file DERIVED from that CSV (its `GZ1_OBJID` column, ascending, deduplicated); the CSV is cited as its provenance and BOTH digests go in the manifest. `select_sample.py` therefore needs no change — it already reads three ID files — but the derivation step must exist, be recorded, and run before the manifest is fixed.
What the reader loses: the failed-set membership is established by the derivation from the CSV rather than re-checked at selection time — so the derived file, its digest and the CSV's digest must all be fixed BEFORE the seed round is named, exactly as for eligibility.
