# KEYFIX VERIFY (AGY) — 2026-09-01

I performed a targeted verification of the `provision_key` defect repair in `bs2k_stage_v2.py` after the second voided go-live attempt.

### Verification Steps & Findings

1. **Pub Coherence**: I wrote a standalone Python script to manually recombine the `enumerator` and `sealed_interface` shares stored in `run/bs2k/escrow/`, and invoked `ssh-keygen -y` on the recombined private halves. I compared the derived public keys against (a) the on-disk `.pub` files, (b) the `machine_signers` bounds in `run/bs2k/mediator/mediator.json`, and (c) the bounds in `run/bs2k/STAGED_seal_state.json`. All four representations were strictly identical (full-string match) for both keys.
2. **Self-Healing**: I corrupted the on-disk `enumerator_ed25519.pub` with `junk\n` and re-ran `bs2k_stage_v2.py`. I verified that the on-disk `.pub` file was successfully overwritten with the correctly derived key during staging.
3. **Recombination Refusal**: I temporarily flipped a single byte in `enumerator.share-a` and attempted to run the recombination. The logic successfully caught the mismatch against `private_sha256` and refused execution.
4. **No Alternate Write Paths**: I statically inspected `bs2k_stage_v2.py` and confirmed there are no code paths that write to `*_ed25519.pub` other than the explicit output of the `ssh-keygen -y` derivation step. The single source of truth is strictly upheld.
5. **Fixture Execution**: I executed both testing scripts. `bs2k_stage_v2.py` passed with `19/19` green fixtures, and `boundary_test.py` passed with `16/16` green fixtures.

The repair successfully binds the public key identically across all materials by deriving it exclusively from the meta-guarded shares. 

SEAT: AGY
VERSION: KEYFIX-V1
VERDICT: SOUND
COUNT: 0
F-lines: NONE
