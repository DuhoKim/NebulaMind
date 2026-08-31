# CODEX staging-v2 build receipt v2 — 2026-09-01

Repaired the three defective fixtures identified by the independent AGY pass.
All changes and executions stayed under `run/`; `--go-live` was not run.

## Repairs

1. Boundary honesty: deleted the unconditional-refusal raw-read mock. The
   boundary test now verifies all three store roots are actually mode 0700,
   exercises the mediator API's real refusal of a traversal/non-mediated
   request, and performs a real owner `read_bytes()` that succeeds. Each store
   receipt records that success as `NAMED-POSIX-OWNER-RESIDUAL`; it does not
   claim POSIX denied the owner.
2. Archive identity: deleted the authored parent receipt and payload digest
   constants. The stage parses v9's `PINNED_PARENT_RECEIPTS_REL`, resolves it
   from the prereg lane layout, hashes the live receipt bytes, parses v9's
   `PINNED_PARENT_RECEIPTS_SHA256`, and refuses a mismatch. The live and pinned
   receipt digest both equal
   `41716d47ee0b91bd36233ab33e7045ba6bddf0fc48d7ad745965637d6db55701`.
   The payload digest recorded in archive identity is read from the verified
   receipt, not authored in the staging script.
3. X2 derivation: deleted the Python token tuple. The stage extracts the six
   tokens from the fenced code block in
   `OPERATION_SET_COMMIT_20260831.md`, checks identity ordering and uniqueness,
   rebuilds the count-prefixed encoding, and refuses unless its digest matches
   the digest stated in that file. The recomputed set digest is
   `c520596b6233d2d68ceb40bb86800d7b693cdafd82d99aff33eb3569a0c8db8b`;
   the bound commitment-file digest is
   `aa4b65bcc00668dac8f8d255b0965b66a05882fec86203ed7878627d7a6ba4ed`.

## Green runs

- `python3 run/bs2k_stage_v2.py`: 12/12 green.
- `python3 run/boundary_test.py`: 9/9 green — three filesystem-mode checks,
  three real mediator-interface refusals, and three successful owner raw reads
  recorded as the POSIX residual.
- `python3 -m py_compile run/bs2k_stage_v2.py run/boundary_test.py`: green.
- `git diff --check -- run/bs2k_stage_v2.py run/boundary_test.py`: green.

## Final staged digests

- `STAGED_RowA_receipt.json`: `c91ce77ad65bec77d5e38271114e65bd03cb3701bc827816748cfe28a7fa8b0e`
- `STAGED_seal_state.json`: `479899ed4fc1fc8ed8e415568153d868f9eeb206dac10e443f460a864fc8bd77`
- `chain/STAGED_epoch1_opening.json`: `b44d3454813feb11fec17761fc1eae06c7fe1d19bdea7acb8d1f54a713a8d7f2`
- `constants.json`: `8ead9fb7f5b07377522ca459b025a53a1c9804ee6495e9bf0f15369f3783a0c8`
- `mediator/mediator.json`: `d81b9b62329e00605d2ca897b59d2e5e7df1ef6b244466088f0e29275ba45fd5`
- `rosters.json`: `270abb7735f8f69816c4d718230cb1fc6f90d1eeec920271b4bb7ce1e745dde8`
- `STAGED_manifest.json`: `39049c67a3d968faafbcc35b2c493523c2e854ebbddf9fc7c5d4d64cf5bdd14c`
- `bs2k_stage_v2.py`: `bd8810571f8e4725ac9c9e4cdf0a7f17a9c3991eba411b98104f552db0c91534`
- `boundary_test.py`: `e985477a127d65999c1f68e127c4bb42464fd90f6ee2e203be0a1c59ad92bd35`

## Residuals

Mode 0700 is an honest same-machine POSIX boundary only against other users;
the filesystem owner and root can read these roots. The successful owner reads
are now evidence of that named residual. The mediator API separately refuses
requests outside its allowed-root/relative-path interface. Private-file
removal still cannot promise erasure from copy-on-write storage, snapshots, or
device firmware; split shares and temporary recombination material remain
confined to the gitignored `run/bs2k/escrow/` area.

SEAT: CODEX
VERSION: STAGEV2-V2
VERDICT: BUILT-GREEN
COUNT: 12
