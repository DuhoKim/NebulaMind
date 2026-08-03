# Goru Phase 4 — disposition-packet brief (no cleanup actions)

Task ID: `quartet-kun-application-20260721T114246Z-phase4-packets`

## Authority and scope

The user directed the canonical plan to proceed. Phases 0–3.2 are complete. This phase authorizes only filename/metadata census plus disposition packet writes. It does not authorize G4a, G4b, or G4c actions.

Inputs:

- `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase1/WORKTREE_CLASSIFICATION.json`
- `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase3/BRANCH_FATE_DECISION.md`
- `.hermes/plans/2026-07-21_205603-kun-report-quartet-application-plan.md`

## Hard prohibitions

- Do not move, rename, copy, archive, quarantine, delete, truncate, chmod, or touch any candidate.
- Do not run `rm`, `mv`, `git clean`, `git add`, `git commit`, checkout, worktree, stash, reset, restore, rebase, cherry-pick, PR, push, or merge.
- Do not read, preview, hash, checksum, MIME-sniff, parse, source, or otherwise access the **contents** of any `.env*` file. For the secret-adjacent path, record filename and `lstat` metadata only (type, size, mode, mtime); no SHA because hashing reads contents.
- Do not open any `.db` file. Record filename and `lstat` metadata only.
- No DB/SQL/migration, runtime, deploy, restart, network, browser, cloud, cockpit, or publication action.
- No source/product/test edits. Write only the four disposition files named below.

## Required census

### 1. G4a ordinary quarantine proposal

From Phase 1, enumerate the exact 18 `DELETE-CANDIDATE` top-level status entries. Record path, Phase 1 reason, protected flag, file type/size/mtime metadata, and the proposed future action `QUARANTINE FIRST — G4a approval required`; no move now.

Protective rules:

- `.hermes/**`, `docs/**` research/Contract packets, `backend/tests/**` source, Contract/validator/receipt artifacts, and active operational dashboard/renderer snapshots must not enter this ordinary sweep.
- Confirm 0 protected items among the 18 candidates.
- Record the 130 `ARCHIVE` and 14 operational `tools/*.bak-*` items as **retained in place / no blanket move** pending per-class review. Do not enumerate 130 large entries in markdown if JSON counts and protected-class summaries suffice.
- Proposed future G4a shape must use one timestamped quarantine directory, an exact closed-world path list, before/after counts, and rollback by restoring from quarantine. It must stop if any candidate changes identity/type/metadata before action.

### 2. G4b test DB and cache disposal proposal

Using filename and `lstat` only:

- Enumerate every repo-local filename matching `test*.db` (expected 18); do not open or hash.
- Enumerate every `.pytest_cache` directory, and count its descendant filesystem entries and total allocated/plain bytes using directory walking/stat only. Do not read file contents.
- Keep DB candidates separate from cache directories and from the 18 ordinary quarantine candidates.
- Proposed future action: quarantine where practical, verify disposable-test provenance, require separate G4b approval, then delete only after review/dwell. No action now.
- Include exact post-action verification criteria: zero repo-local `test*.db`, zero `.pytest_cache` dirs, no source/test deletion, and unchanged HEAD/branch.

### 3. G4c secret-adjacent proposal

For every status path matching `.env*` (expected exactly one), record only:

- exact path;
- status/bucket/future gate/evidence basis from Phase 1;
- `lstat` type, size, mode, mtime;
- `content_read: false`, `hash_computed: false`.

Propose a future dedicated G4c move-to-quarantine action with rollback, but do not move/delete/open/hash now. State that G4c is never bundled with ordinary cleanup.

## Required outputs

Write only:

1. `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase4/PHASE4_DISPOSITION_INDEX.json`
2. `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase4/G4A_QUARANTINE_PACKET.md`
3. `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase4/G4B_TEST_DB_CACHE_DISPOSAL_PACKET.md`
4. `.hermes/handoffs/quartet-kun-application-20260721T114246Z/phase4/G4C_SECRET_ADJACENT_PACKET.md`

The JSON must include exact candidate arrays, counts, metadata, cross-set overlap checks, protected violations, and all-zero safety counters. Markdown packets must be proposals only with prerequisites, closed-world scope, stop rules, verification, rollback, explicit future approval requirement, and final standalone markers:

- `GORU_PHASE4_G4A_PACKET_COMPLETE_20260722`
- `GORU_PHASE4_G4B_PACKET_COMPLETE_20260722`
- `GORU_PHASE4_G4C_PACKET_COMPLETE_20260722`

JSON marker: `GORU_PHASE4_DISPOSITION_INDEX_COMPLETE_20260722`.

Hard-stop and do not write outputs if the live status snapshot is not HEAD `826e733`, branch `feat/surveys-atlas-ia-p1-20260627`, 20 modified, 360 untracked, zero deleted, or if the Phase 1 entry count is not 380.
