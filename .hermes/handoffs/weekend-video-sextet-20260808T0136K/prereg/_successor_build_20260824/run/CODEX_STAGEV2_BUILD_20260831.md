# CODEX staging-v2 build receipt — 2026-08-31

Built `run/bs2k_stage_v2.py` and `run/boundary_test.py` from the staging-v2
repair contract without importing v1.  The stage now derives the predecessor
archive identity from v9's pinned receipt path and both frozen digests; covers
exactly the main, committee, and predecessor-archive store roots; installs the
three roots at mode 0700; generates and XOR-splits both machine private keys;
removes the unsplit private files; binds both public keys and signer identities
in the mediator and seal provisioning materials; derives canonical Option-A
reviewer and holder rosters from P0's public key; recomputes and binds X2; and
emits the exact five-field seal and exact four-field staged opening schemas.

Duho's keypair requirement is discharged by
`P0_FREEZE_SIGNATURE_20260831.md`; no new Duho key or signature was generated.
Row L's holder designation is discharged by the ruled label "Option A
(principal alone)".  Go-live remains a separate explicit path.  It rechecks
the complete staged manifest before writing anything live, then writes a fresh
epoch-1 opening, authenticates the Row-A seal digest under the enumerator key
with namespace `nmpr-rowa`, and emits the go-live receipt.  `--go-live` was not
run.

The staging command passed 10/10 fixtures.  These cover mediator success and
raw-path refusal, share recombination and corrupted-share refusal, both exact
schemas including missing/extra rejection, roster ordering determinism and
digest sensitivity, X2 recomputation, and staged-byte drift refusal.
`boundary_test.py` separately passed 6/6 store-direction assertions: three raw
path refusals and three mediator successes.

Staged digests from the final green run:

- `STAGED_RowA_receipt.json`: `999f08b505337c4202987381a1038874dedfe620411621d4ac3d7e538eb6c43a`
- `STAGED_seal_state.json`: `074b0b8421c35a1163c0f90b9aa3bd0a5e343f60ba6299ecd4383e6c9eef2425`
- `chain/STAGED_epoch1_opening.json`: `c4aeb5aa2dc41db901f2c5bf1ceb9e58f8ed6a59eec7859465045add79c88abf`
- `constants.json`: `8ead9fb7f5b07377522ca459b025a53a1c9804ee6495e9bf0f15369f3783a0c8`
- `mediator/mediator.json`: `d81b9b62329e00605d2ca897b59d2e5e7df1ef6b244466088f0e29275ba45fd5`
- `rosters.json`: `270abb7735f8f69816c4d718230cb1fc6f90d1eeec920271b4bb7ce1e745dde8`
- `STAGED_manifest.json`: `e96c94a42eedf0170ccd9026b5c7ecee220a717ddbcb88fbac18925735cdc54b`

Disclosed residuals: this is the contract's single-user POSIX boundary, not a
separate security principal.  Directory mode 0700 plus the tested mediator
capability path denies the modeled outside process, but the filesystem owner
or root can bypass POSIX modes.  Private-file removal overwrites, fsyncs, and
unlinks the unsplit pathname; copy-on-write storage, snapshots, or device
firmware can retain historical physical blocks.  Private shares and temporary
recombination material remain confined to the gitignored `run/bs2k/escrow/`.

SEAT: CODEX
VERSION: STAGEV2-V1
VERDICT: BUILT-GREEN
COUNT: 10
