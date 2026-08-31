# P0 FREEZE-SIGNATURE CEREMONY PACKET — staged 2026-08-31

**In plain words.** Everything is staged so your ceremony is short. The freeze
package is 30 files; their digests are COMPUTED into the manifest
beside this packet, and the one number you sign is the sha256 of that manifest.
You CHECK, never trust: every command below you run yourself, on your own
environment, with the OS tool.

**The signing digest (recompute it yourself before signing):**

    d1be4a3b61975c79f75d6bfafa75e117f69ae86e00dc81ea139a4884f62dc72a

## The ceremony — four steps

1. **Recompute the manifest digest yourself:**

       cd /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824
       shasum -a 256 -c P0_PACKAGE_MANIFEST_20260831.txt
       shasum -a 256 P0_PACKAGE_MANIFEST_20260831.txt

   The first command must print OK for every one of the 30 files;
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
