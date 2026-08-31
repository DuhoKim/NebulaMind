# STAGING-V2 REPAIR CONTRACT — 2026-08-31 22:55 KST (Hwao's judgment; codex builds)

The build target is `run/bs2k_stage_v2.py` (+ `run/boundary_test.py`), repairing
every RUNOPEN-V1 finding against the FROZEN clauses — read them, quote them in
docstrings, derive from them. v1 (`run/bs2k_stage.py`) is the corrected-away
state; do not import from it.

## Per-finding requirements

- **F1 — the three frozen stores + enforced mediation.** The mediator covers
  exactly: the MAIN SEALED store, the COMMITTEE SEALED store, and the
  PREDECESSOR ARCHIVE brought under it. Derive the predecessor archive's
  concrete identity FROM the frozen bytes (v9's `PINNED_PARENT_RECEIPTS_REL`
  and §2's pins), never a hand answer. Enforcement: POSIX modes on the store
  roots (0700 mediator-owned directories; raw paths unreadable outside the
  mediator user/process model — state the model honestly for a single-user
  machine: the boundary is directory modes + the boundary test, and the
  residual (root/owner can bypass POSIX) is NAMED in the receipt, not hidden).
  `boundary_test.py` must PROVE the boundary fires: a direct read attempt on
  each store root outside the mediator path fails; the mediator path succeeds;
  both directions receipted.
- **F2 — split keys, bound public halves.** Each machine keypair (enumerator,
  sealed interface) is generated, then its private half SPLIT (2-way XOR
  shares, both shares inside `run/bs2k/escrow/`, the recombination function in
  the staging script and fixtured), the unsplit private file securely removed.
  BOTH public keys + signer identities are BOUND into the seal object and
  `mediator.json` (not stdout). Duho's signing keypair clause is DISCHARGED BY
  P0 (his ceremony generated it; the P0 artifact binds the public half) — say
  so with the artifact reference, generate nothing for him.
- **F3 — no principal signature.** The seal state is RECORDED by non-content
  metadata operation: the staging emits the canonical seal-state body plus its
  sha256 as the Row-A receipt, authenticated at go-live under the ENUMERATOR
  key (a machine signature, ssh-keygen -Y sign, namespace nmpr-rowa) — no Duho
  act anywhere. Row L's "designates holders at BS-2k" is discharged BY
  REFERENCE to the constants-and-rosters ruling (quote the option label).
- **F4 — exact seal-state schema.** Fields exactly: archive identity (the
  UNIQUE predecessor-archive identity from F1's derivation), seal
  identifier/version, holder-roster digest (over the F6 canonical encoding),
  checkpoint predecessor digest (the P0 signing digest d1be4a3b…), and
  MONOTONIC EVENT/EPOCH DATA (boot_epoch=1, the provisioning monotonic reading
  quantized to g=1ms, taken at emission). Nothing else at top level; the
  constants/mediator/X2/pubkey digests ride INSIDE a named provisioning-
  materials sub-body so the canonical five-field schema stays exact.
- **F5 — exact opening schema.** The staged epoch-1 opening carries EXACTLY
  `(boot_epoch, monotonic_reading, predecessor_epoch, gap_declaration)` —
  bounded decimal integers (predecessor_epoch = 0, the reserved pre-first
  value; gap_declaration = the empty declaration), nothing else. It appends at
  go-live as Row B's first act, reading taken then.
- **F6 — canonical rosters.** `(kind, roster_entries)` with kind literals
  (reviewer-roster / holder-roster), entries COUNT-PREFIXED and
  IDENTITY-SORTED `(identity, pubkey)` pairs, canonical length-prefixed
  encoding (the void-registry `canonical()` style: `len:value` per field),
  digest over the canonical bytes. Duho's pubkey from the P0 artifact.
- **F7 — X2 inside the seal.** The operation-set commitment
  (`run/OPERATION_SET_COMMIT_20260831.md`): its six tokens, canonical encoding
  `6:ARCHIVE-METADATA-READ,…`, set digest
  `c520596b6233d2d6…` (recompute, don't paste), and the commitment file's
  sha256 — all inside the provisioning-materials sub-body.
- **F8/F9 — sequence.** The script STAGES and verifies; go-live is a separate
  explicit `--go-live` entry that (1) re-verifies every staged digest, (2)
  appends the epoch-1 opening with a fresh reading, (3) emits the Row-A seal
  receipt under the enumerator key, (4) prints the go-live receipt. It must
  REFUSE `--go-live` if any staged artifact drifted (recompute-and-compare).

## Fixtures (in-script, direct exits, exact refusal codes)
Boundary both directions; share-recombination round-trip + a corrupted-share
refusal; seal-body schema exactness (missing/extra field refused); opening
schema exactness; roster canonical-encoding determinism + digest sensitivity;
X2 digest recomputation matching the commitment file; --go-live drift refusal
(tamper one staged byte → refuse). Print `staging-v2 fixtures: N/N green`.

## Non-negotiables
No key bytes in stdout or git (escrow/ is gitignored — keep everything secret
under it). No χ, no imagery, no catalog reads tonight — staging touches its own
artifacts only. Every frozen quote in the docstring cites its clause. macOS:
no `timeout` command; BSD userland.
