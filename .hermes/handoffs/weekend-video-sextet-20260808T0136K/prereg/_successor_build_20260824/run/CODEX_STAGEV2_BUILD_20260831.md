# CODEX staging-v2 build receipt v3 — 2026-09-01

Repaired all five findings from `AGY_STAGEV2_VERIFY2_20260901.md` in place.
All changes and executions stayed under `run/`; `--go-live` was not run.

## Per-finding repairs and fixtures

1. R1 allowed-root boundary: the boundary test now labels and runs both an
   allowed-root probe using a genuine sibling outside all three stores and a
   retained lexical traversal probe. The former returns
   `REFUSED-RAW-STORE-PATH`; the latter returns the distinct
   `REFUSED-STORE-PATH-TRAVERSAL`. Dedicated allowed-root fixture: green.
2. R2 resolved containment: `mediator_read` resolves the allowed store root
   and joined target, then requires `resolved_target.relative_to(resolved_root)`
   to succeed. The lexical absolute/`..` checks remain fast paths, while
   resolved containment is authoritative. A fixture creates an in-store
   symlink to a temporary outside file, verifies refusal, and removes both the
   symlink and temporary directory. Dedicated symlink fixture: green.
3. R3 fail-closed archive pin: `archive_identity` now refuses
   `REFUSED-SCHEMA-NONCONFORMING` when v9's
   `PINNED_PARENT_RECEIPTS_SHA256` is absent. A temporary v9 copy with that
   assignment removed is refused. Dedicated missing-pin fixture: green.
4. R4 v9 assignment semantics: `v9_literal` collects all direct module-level
   assignments and returns the last, matching runtime semantics for the v9
   constants. Its comment records that those constants are module-top-level
   by inspection and nested scopes are outside this parser's scope. A
   two-assignment temporary file returns the second value. Dedicated
   last-assignment fixture: green.
5. R5 commitment closure at the seal: `STAGED_manifest.json` now includes
   `../OPERATION_SET_COMMIT_20260831.md` with SHA-256
   `aa4b65bcc00668dac8f8d255b0965b66a05882fec86203ed7878627d7a6ba4ed`.
   `verify_staged`, and therefore the `--go-live` preflight, refuses a later
   mutation. The internal tokens-versus-stated-digest check remains. A fixture
   mutates the commitment file, verifies drift refusal, and restores it.
   Dedicated commitment-drift fixture: green.

Pre-staging custody of `OPERATION_SET_COMMIT_20260831.md` is git history plus
the pushed adjudication record. This is the honest custody scope; cryptographic
closure begins at this staged manifest seal, not before it.

## Green runs

- `python3 bs2k_stage_v2.py`: 17/17 green.
- `python3 boundary_test.py`: 16/16 green: 3 mode, 3 traversal, 3 allowed-root,
  3 mediated-read, 3 named owner-raw-read residual, and 1 symlink-escape
  fixture.
- `_test_r2_r3.py`: green.
- `tamper_test.py`: both archive and X2 tamper probes refused staged drift.
- `verify_staged()`: green across all 7 manifest entries.
- `python3 -m py_compile bs2k_stage_v2.py boundary_test.py`: green.
- `git diff --check` on the repaired and staged files: green.

## Final digests

- `bs2k_stage_v2.py`: `f74b5a70879fa4a9c9067f7246d1453f980693c2fb6e0b5d6fc30c0093a4efcf`
- `boundary_test.py`: `8b4d5a0a9a38dde75b2498f014cf3b590662477fce0075f8f51aca9319e4188e`
- `OPERATION_SET_COMMIT_20260831.md`: `aa4b65bcc00668dac8f8d255b0965b66a05882fec86203ed7878627d7a6ba4ed`
- `STAGED_manifest.json`: `8a3167d2a89f37fd4ccb1fc36fbcfa8df7e375397708bb9229c811402465c84f`
- `STAGED_seal_state.json`: `44c8a6f4bc830c8ff7ea84c559bda333f804986c8e3ba93404462b76e1cf7471`
- `STAGED_RowA_receipt.json`: `e0665f997db2c4e61f6eb6988298577c3c3dc7e21b5d9b80011a2b6e53aaca31`
- `chain/STAGED_epoch1_opening.json`: `672ee937eec09ec44b8c3b00108a3a961f93cf043fbc3fe5acfd2ce5d778ba30`
- `constants.json`: `8ead9fb7f5b07377522ca459b025a53a1c9804ee6495e9bf0f15369f3783a0c8`
- `mediator/mediator.json`: `d81b9b62329e00605d2ca897b59d2e5e7df1ef6b244466088f0e29275ba45fd5`
- `rosters.json`: `270abb7735f8f69816c4d718230cb1fc6f90d1eeec920271b4bb7ce1e745dde8`

## Residuals

Mode 0700 remains a same-machine POSIX boundary against other users only;
the filesystem owner and root can bypass it. The fixture names successful
owner raw reads as that residual. Private-file removal cannot guarantee
erasure from copy-on-write storage, snapshots, or device firmware. Nested v9
scopes remain intentionally outside the literal parser because the relevant
v9 constants are direct module-level assignments by inspection.

SEAT: CODEX
VERSION: STAGEV2-V3
VERDICT: BUILT-GREEN
COUNT: 17
