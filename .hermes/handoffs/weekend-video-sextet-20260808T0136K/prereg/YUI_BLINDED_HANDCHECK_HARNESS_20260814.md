# YUI — blinded hand-check harness

> **SUPERSEDED 2026-08-15:** this report describes the withdrawn HC-1 A/B/J design. It is retained only as history. The accepted HC-1H implementation, receipts, operating instructions, and honest limits are under `prereg/handcheck/`, especially `YUI_HANDCHECK_HARNESS_20260814.md` and `SELFTEST.md`. Do not use this file as current authority.

Date: 2026-08-14 KST  
Status: **DELIVERED — synthetic-only build and verification PASS; no actual hand-check run**

## Verdict

The blinded HC-1…HC-5 hand-check harness is implemented under `prereg/handcheck/`.

It provides:

- secret-keyed nine-stratum sampling with the frozen 500-image / floor-40 production design;
- a 0.5 random parity assignment committed before checking;
- an encrypted sealed key that is absent from and unreachable through the checker HTTP path;
- separate independent A/B sessions;
- a disagreement-only third-checker package;
- one-keystroke classification, progress, pause, synchronous append/fsync, stale-token rejection, double-key debounce, and lossless resume;
- key opening only after all A/B/J labels and commitments are complete;
- de-mirroring, population-weighted attenuation `a`, Wilson 68% intervals, FPC delta uncertainty, exact HC-5 decisions, and separate private/public outputs;
- F-10 masking for every public stratum with support below 50.

## Principal artifacts

- Harness: `prereg/handcheck/nm_handcheck.py`
- Contract tests: `prereg/handcheck/test_nm_handcheck.py`
- Exact human/custodian commands: `prereg/handcheck/OPERATING_INSTRUCTIONS.md`
- Full 500-item synthetic self-test: `prereg/handcheck/run_synthetic_selftest.py`
- Self-test narrative: `prereg/handcheck/SELFTEST.md`
- Machine receipt: `prereg/handcheck/synthetic_selftest_receipt.json`
- Independent stdlib-only verifier: `prereg/handcheck/independent_verify.py`
- Independent machine receipt: `prereg/handcheck/independent_verification.json`

## Verification

- Compile: PASS.
- Unit/contract tests: **14/14 PASS**.
- Full 500-item production-shape synthetic protocol: **29/29 PASS**.
- Independent AST/hash/receipt verification: **33/33 PASS**.
- Synthetic parity replay: **500/500 pixel exact**.
- Independent HMAC parity re-derivation: **500/500 exact**.
- Synthetic A/B disagreements: 39; disagreement-only adjudications: 39.
- Real images, positions, survey rows, scientific objects, model inference, estimator access, network retrieval: **zero**.

The full synthetic allocation was:

`00=86, 01=43, 02=40, 10=43, 11=65, 12=54, 20=40, 21=54, 22=75`.

F-10 therefore masked public rows `01`, `02`, `10`, and `20`. Their full values remained private. The nine-row public shape was preserved.

The synthetic fixture—not a scientific result—produced:

- `a = 15386756/16979625 = 0.9061893887526963`
- `σ_a = 0.008771601462441143`
- `2a−1 = 13793887/16979625 = 0.8123787775053924`
- `σ_(2a−1) = 0.017543202924882286`
- synthetic HC-5: PASS.

Exact edge tests prove `a=0.849` is `INCONCLUSIVE-BY-POWER`; exact `0.850` passes only when all nine strata meet the floor; stratum `0.699` fails and exact `0.700` is accepted.

## Key custody and checker isolation

The sealed document includes the source mapping, sample, strata, signs, parity bits, identities, source/authority hashes, and a fresh 256-bit HMAC root key. It is encrypted using Scrypt and AES-256-GCM. Plaintext key bytes are never written.

The checker package and HTTP interface contain no source ID/path, instrument sign, `|χ|`, angular size, stratum, parity bit, key, passphrase, per-object aggregate, or peer answer. The server exposes exactly four routes: page, state, current-token asset, and answer submission. Traversal and direct-file requests return 404. The `check` command has no unseal or reduction option.

The public commitment is anchored by a separate private preparation receipt. Rewriting both public commitment files is insufficient: reduction compares them to the private anchor and fails closed. Current source and protocol-authority hashes are also rechecked.

The key cannot be read or derived through the checking HTTP capability. This is application capability separation, not a general OS sandbox: hostile checkers must receive browser-only access or distinct OS accounts/devices rather than shell access under the custodian account. The passphrase remains custodian-only.

## Statistical and release boundary

The private reduction:

1. majority-resolves A/B/J;
2. reverses the sealed presentation parity;
3. compares the original-parity human sign to the instrument sign;
4. computes nine stratum rates and Wilson 68% intervals;
5. weights by accepted-population stratum fractions;
6. computes delta uncertainty using the pinned SRS-without-replacement FPC `(N_h−n_h)/(N_h−1)`;
7. evaluates HC-5 on exact unrounded values.

The private per-object table is sorted by canonical source/object key before hashing. Public output is exactly one JSON aggregate and one CSV aggregate. Any stratum with `k<50`, including its derivative failing-stratum disclosure, is masked publicly after private HC-5 evaluation.

## Final core hashes

- Harness: `7dbcf51e3a542411316a3197131f3bc4ff6d41d2bb098adcb82bafdf1639da14`
- Tests: `a32762b912c39a9910e776662fcf3f973cdb1a7f8c533d1875bbb93bb168dacb`
- Full self-test source: `cc3c077ec613d4745ae7743cbc6e24a5b8a12e04efe361359560a07e5ef42821`
- Full self-test receipt: `1a6a82559f3c9e4c568ac8076da4d4d53c0b4a2ebd302ecaaec656ef240f01c8`
- Independent verifier: `c10ca1b5cc3f9e178e5551b4b48459f11f8fafbb0734ce4531af481f1e9aec98`
- Independent receipt: `54b5b30e4d7ffba9a3e154e0b7cd7dc4f72cbed2fbf4360673198b150f2194ae`

## Boundaries

This delivery authorizes no actual hand-check population, real-image access, HC-6 calculation, study run, acceptance, freeze, release, publication, database action, cockpit update, git commit, or push. Those remain separate gates. The harness and instructions are ready for Kun/Hwao review and later custodian-controlled use.
