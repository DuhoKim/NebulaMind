# r3c2_staged_d1d7 — STAGED, UNADOPTED tooling for the D1 / D7 / batch candidates (V33, 2026-09-06 20:38 KST)

Nothing here is installed. Since V26 the tools here are the SAME bytes as the pinned tools (`r3c2_ledger_tools.py` sha256 bd1f4a237357f439…, and the lane, batch, manifest and builder tools),
kept under their `_STAGED` names so the kit runs against the delivered implementation; the kit is the fail-first control suite of the living draft.

- `r3c2_ledger_tools_STAGED.py` — the seat tool plus (D1, the review's wording only) the import evidence rule in `validate <ledger> <sources_dir> <candidates.json>`
  and (D7) `audit seal-enumeration | select | handout | seal-rederivation | compare`.
- `r3c2_batch_tools_STAGED.py` — lane-side `partition | seal | join | coverage` (ownership partitioned, access not; global source-based ids).
- `r3c2_staged_tests.py` — 184 controls: positives, negatives asserting the EXACT failure set, and 63 deletion probes (the check on a marked line is neutralised in a copy of the tool; the matching negative must then either PASS or, where an authoritative guard overlaps the neutralised diagnostic, still FAIL on that guard with the diagnostic line absent — a guard is never weakened to make a probe killable). Run from this directory: `/usr/bin/python3 -E r3c2_staged_tests.py`; verify the pin sheet from the LANE directory: `shasum -a 256 -c r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` (paths are lane-relative)
  → `STAGED_TESTS=PASS`. It recreates `_ctl/` and rewrites `C6_COUNTEREXAMPLE_EXHIBIT.txt` deterministically.
- `C6_COUNTEREXAMPLE_EXHIBIT.txt` — emitted completeness results: both seats omit a required passage; its reverse; the seats never enumerated a
  passage the auditor excluded; a sealed exclusion the auditor never listed; disputes at 10% and 15%.
- `partition_12_of_89.json` / `.txt` — the candidate ownership partition of the real manifest into 12 batches, with bytes and non-blank lines.
- `R3C2_STAGED_D1D7.sha256` — pins of everything above. Reviewer scratch directories `_review_*/` are the reviewers' own and are not pinned.
- `r3c2_spi_exhibition.py` — SEAT-PERMUTATION INVARIANCE exhibition: every reviewer construction under both seat orders; merged bytes and the whole audit outcome must be equal. `_v32_bytecopy/` — pinned byte copies of the V32 lane and seat tools against which the exhibition must FAIL (the fail-first record of the class found twice by codex).
