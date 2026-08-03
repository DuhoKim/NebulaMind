# Goru Phase 1 worktree-classification brief

Task ID: `quartet-kun-application-20260721T114246Z-phase1`

## Authority and role

The user directed the full canonical plan to proceed. Phase 0 is complete. Hwao explicitly released Phase 1 classification under the original full-plan direction.

Goru owns the mechanical classification. Hwao ratifies, Kun spot-checks protected categories, and Tori independently verifies outputs.

## Goal

Classify every top-level entry returned by `git status --porcelain=v1` in `/Users/duhokim/NebulaMind/NebulaMind` into exactly one bucket:

- `KEEP-COMMIT`: real code, tests, canonical docs, or canonical research artifacts that require isolated review.
- `ARCHIVE`: useful receipts, reports, or snapshots that may move only after later G4a approval.
- `DELETE-CANDIDATE`: reproducible/generated debris with concrete filename/stat/reference evidence; deletion remains held behind G4b.
- `UNKNOWN`: insufficient evidence; defaults to KEEP and requires Hwao/human adjudication.

## Required fresh snapshot

Recount immediately before classifying:

- branch and short HEAD;
- ahead/behind against the locally cached `origin/main` (no fetch/network);
- modified and untracked counts using exactly `git status --porcelain=v1` so untracked directories remain collapsed;
- total status entries.

Expected starting snapshot: branch `feat/surveys-atlas-ia-p1-20260627`, HEAD `826e733`, 6 ahead / 66 behind, 20 modified + 360 untracked = 380 entries. Explain any drift and stop on unexplained drift.

Do not use expanded `-uall` counts as the 380-entry denominator. You may record an expanded leaf-file count only as separate context.

## Protected categories

These may never be classified `DELETE-CANDIDATE`:

- `.hermes/handoffs/**`
- `.hermes/plans/**`
- `.hermes/board/**`
- `docs/**` research packets
- `backend/tests/**`
- `docs/claim_ledger_contract_v1_agn_20260703T0830Z/**`
- Contract v1 validators and receipts

When one collapsed top-level status entry contains mixed protected and ordinary children, classify the collapsed entry `UNKNOWN` unless the whole entry is clearly canonical.

All 20 modified tracked code/docs paths default to `KEEP-COMMIT` as real work requiring topical review; do not imply they belong in one commit.

## Secret-adjacent rule

For every `.env*` path, including `.env.redacted-*`:

- inspect filename and filesystem metadata only (`stat`, file-vs-directory, size, mtime);
- do not open, read, hash, print, search, preview, or infer contents;
- classify `UNKNOWN` unless filename-only evidence justifies a more protective bucket;
- add it to a separate `secret-adjacent` disposition packet with G4c held.

## Evidence rules

Use filename, git status code, filesystem metadata, path family, generated-file naming, and read-only reference search where safe. Do not read file contents merely to decide cleanup. `DELETE-CANDIDATE` requires a concrete reproducibility/generated-debris reason. Ambiguity is `UNKNOWN`.

Likely filename-only candidates to evaluate include root `test_*.applescript`, `click.js`, `find_deep.js`, `wait_and_extract.py`, `tmp_build_2929_trust_packet.py`, `goru_temp_report.json`, `main.py.bak-labrunner`, renderer backups, and on-disk `test*.db` files. These are candidates, not predetermined outcomes.

## Required outputs — only these files

Write:

1. `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase1/WORKTREE_CLASSIFICATION.json`
2. `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase1/WORKTREE_CLASSIFICATION.md`

JSON requirements:

- schema/version and timestamp;
- fresh snapshot fields;
- bucket definitions;
- one entry for every top-level porcelain status entry with `status`, `path`, `bucket`, `reason`, `protected`, `evidence_basis`, and `future_gate`;
- bucket totals summing exactly to the total entry count;
- status totals reconciling exactly to modified + untracked;
- separate future disposition arrays for `archive`, `ordinary-quarantine`, `deletion-candidates`, `secret-adjacent`, `product-review`, and `research-docs-preservation`;
- safety ledger proving zero moves, deletes, stashes, commits, branches, git writes, `.env*` content reads, DB actions, runtime actions, network, or publication;
- standalone marker value `GORU_PHASE1_WORKTREE_CLASSIFICATION_COMPLETE_20260721`.

Markdown requirements:

- plain-English snapshot and bucket totals;
- table covering all entries or an explicitly complete path appendix;
- protected-category summary;
- every `DELETE-CANDIDATE` with reason and future gate;
- every `UNKNOWN` with the unresolved question;
- separate disposition packets and held gates;
- stop rules;
- standalone final marker `GORU_PHASE1_WORKTREE_CLASSIFICATION_COMPLETE_20260721`.

## Hard exclusions

- No move, rename, archive, quarantine, delete, or cleanup.
- No `git add`, commit, branch, checkout, switch, stash, reset, rebase, cherry-pick, PR, push, merge, or fetch.
- No `.env*` content access.
- No DB/SQL/migration or test execution that writes repo-local DBs.
- No runtime, deploy, restart, publication, cockpit, browser, cloud, cron, billing, or network action.
- Do not edit any product, test, board, plan, contract, or existing receipt file.
- Do not resume the old DR/CDP browser task.

Done only when both output files exist, both contain the standalone marker, totals reconcile to the fresh top-level status count, protected categories are never `DELETE-CANDIDATE`, and the safety ledger is all zero.