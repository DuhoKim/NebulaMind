#!/usr/bin/env python3
"""p0_ceremony_packet — stages the P0 freeze-signature ceremony so the
principal's act is short. COMPUTE-NOT-DESCRIBE: the package manifest is computed
from the bytes on disk at generation time; the signing digest is sha256 over the
canonical manifest; the principal RECOMPUTES both himself with an OS tool before
signing — the packet stages, it never asks him to trust."""
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent

PACKAGE = [
    # the frozen text and its generated appendix
    "PREREG_SUCCESSOR_DRAFT_V134_20260831.md",
    "LIFECYCLE_GUARANTEE_SPEC.md",
    "gates/KNOWN_DEBT_APPENDIX.md",
    # the frozen reference and the pinned executables
    "ref/successor_ref_v9.py",
    "ref/gain_counterfactual_path.py",
    "ref/gain_mapping_a.py",
    "gates/count_oracle_harness.py",
    "gates/replay_harness.py",
    "gates/canonical_decoder.py",
    "gates/enumeration_verifier.py",
    "gates/terminal_review_verifier.py",
    "gates/terminal_ceremony.py",
    "gates/stratum_index_producer.py",
    "gates/stratum_index_verifier.py",
    "gates/bs2f_boundary_verifier.py",
    "gates/bs2v_void_converter.py",
    # the blind commitments
    "ref/DRAW_MECHANICS_COMMIT_20260830.md",
    "ref/MAPPING_CONVENTION_COMMIT_20260831.md",
    "ref/BS2K_CONSTANTS_COMMIT_20260831.md",
    # the principal's ruling records (2026-08-30/31 set)
    "GAMMA_RATIFICATION_20260830.md",
    "TERMINAL_SIGNATURE_RULING_20260830.md",
    "MAP_WIDENING_CONFIRMATION_20260830.md",
    "EXHAUSTION_ABSTAIN_RULING_20260830.md",
    "STOPPING_RULE_RULING_20260830.md",
    "APPENDIX_FORM_FREEZE_RULING_20260831.md",
    "MAPPING_ARCHITECTURE_RULING_20260831.md",
    "MAPPING_CONFIRMATION_RULING_20260831.md",
    "BS1_EARLY_RESOLUTION_RULING_20260831.md",
    # the rehearsal receipts the pace ruling asked for
    "gates/CALIBRATION_REHEARSAL_RECEIPT_20260831.md",
    "gates/CALIBRATION_ROBUSTNESS_REHEARSAL_RECEIPT_20260831.md",
]


def main():
    rows = []
    for rel in PACKAGE:
        p = BASE / rel
        if not p.exists():
            print(f"FATAL: package member missing: {rel}")
            return 1
        rows.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {rel}")
    manifest = "\n".join(rows) + "\n"
    mpath = BASE / "P0_PACKAGE_MANIFEST_20260831.txt"
    mpath.write_text(manifest)
    digest = hashlib.sha256(manifest.encode()).hexdigest()

    packet = f"""# P0 FREEZE-SIGNATURE CEREMONY PACKET — staged 2026-08-31

**In plain words.** Everything is staged so your ceremony is short. The freeze
package is {len(PACKAGE)} files; their digests are COMPUTED into the manifest
beside this packet, and the one number you sign is the sha256 of that manifest.
You CHECK, never trust: every command below you run yourself, on your own
environment, with the OS tool.

**The signing digest (recompute it yourself before signing):**

    {digest}

## The ceremony — four steps

1. **Recompute the manifest digest yourself:**

       cd {BASE}
       shasum -a 256 -c P0_PACKAGE_MANIFEST_20260831.txt
       shasum -a 256 P0_PACKAGE_MANIFEST_20260831.txt

   The first command must print OK for every one of the {len(PACKAGE)} files;
   the second must print exactly the signing digest above. If either differs,
   STOP — nothing is signed and you surface it.

2. **Spot-check the two rehearsal receipts** (both already PASS/HELD — read
   their verdict lines): `gates/CALIBRATION_REHEARSAL_RECEIPT_20260831.md`
   (seven-stage machinery chain) and
   `gates/CALIBRATION_ROBUSTNESS_REHEARSAL_RECEIPT_20260831.md`
   (99×51, zero flips, with its honest fixture-scope language).

3. **Sign the digest with your own key tooling** (the packet holds no key and
   signs nothing): sign the 64-hex signing digest above, then record it as

       P0_FREEZE_SIGNATURE_20260831.md
       — the digest, the signature bytes (hex), your pubkey, the date.

   Your pubkey in that file simultaneously fills the reviewer and custody
   rosters per your constants-and-rosters ruling (both Option A, you alone).

4. **Say "P0 signed" through Blanc** — I fold the signature file into the
   repository, the freeze is in force, and every downstream gate verifies
   against the manifest this signature covers.

## What P0 covers and what it does not

Covers: the frozen text (V134 line: V124's text + the sanctioned slot-value
fills V125–V134), the appendix, the spec, the pinned reference and all thirteen
pinned executables, the three blind commitments, your nine ruling records, and
both rehearsal receipts. Does NOT cover (by design): run-time artifacts that do
not exist yet — the BS-1 receipt, calibration artifacts, the stratum-index
artifact (SCHEMA-PENDING, P2–P3), and every χ-bearing byte; those are produced
under the machinery this signature freezes, and their gates verify against it.

## Standing facts at staging time

- Robustness rehearsal: **HELD** — 5,049 evaluations (99 draws × 51 γ), zero
  verdict flips against each draw's own γ=0 baseline; machine-only, fixture
  data, stated so in the receipt.
- Machinery rehearsal: **PASS** — seven stages, one receipted chain.
- Battery: green fifteen-for-fifteen at every draft version through V134.
- v9 frozen at `6a9abbbd…` throughout; γ̂ unmeasured; BS-6 and the first image
  byte blocked until the run.
"""
    (BASE / "P0_CEREMONY_PACKET_20260831.md").write_text(packet)
    print(f"manifest: {len(PACKAGE)} files; signing digest: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
