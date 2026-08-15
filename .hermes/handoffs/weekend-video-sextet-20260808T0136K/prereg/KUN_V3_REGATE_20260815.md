# Kun v3 preregistration re-gate — 2026-08-15 KST

## Verdict

**PASS_V3_FREEZE_CLEAR_ON_EXACT_HASH.**

The GZ DECaLS rationale repair is applied in both required places and the two cuts it now relies on
are genuinely frozen. Nothing blocks freezing v3 on the exact candidate hash
`b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`.

This pass does not authorize image acquisition, a sky run, publication, commit, push, or acceptance.

## Exact Artifacts Checked

Hashes and mode recomputed from disk:

| Artifact | SHA-256 / mode |
|---|---|
| `_tmp_KUN_V3_REGATE_BRIEF.md` | `0ee2caa7af60de48f7b626981ceb2d5c64569839a78b1ae886bcb2eedc74187e` |
| `PREREG_LONGO_AMPLITUDE_TEST_20260815_V3_CANDIDATE.md` | `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7` |
| `LANA_PC1_INPUT_AMENDMENT_20260815.md` Rev 3 | `519ab5ba33c5e9d670b5654fb41f6941293c5d969c5515fb0284ebe8d52d70fb` |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md` | `62dad44dd92acf2781d2c8cf25161f7f344e3fe6f7fec35b7e04308bd1539c12`, mode `444` |

The frozen 08-15 v2 file remains untouched and read-only.

## GZ DECaLS Repair

The blocker is discharged. The live amendment §2(c) now says the study parent guarantees r flux
through the frozen study cuts, while Walmsley et al. 2022 supplies only separate support that the
GZ DECaLS NSA parent is primarily r-limited and has exceptions. The incorporated v3 §6 summary says
the same thing and does not summarize it more strongly.

The withdrawn sentence "Every parent therefore has secure r-band flux by construction..." survives
only in the Revision 3 changelog as the wording that was replaced. That is legitimate history, not a
live claim.

## Frozen Cut Verification

Lana's claim that the two cuts were re-verified is real:

- `flux_r > 0` appears in the frozen Cut-2 chain in `TORI_BS1_CLOSURE_PACKET.md` and in the
  build-only selector's `FROZEN_SELECTION_STAGES`.
- `dered_mag_r < 17.7` appears in the frozen Cut-4 dered branch in `TORI_BS1_CLOSURE_PACKET.md`,
  in the executed parent-row receipts, and in `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`, where it is
  cross-checked against the frozen Cut-6 definition.

So the repair no longer inherits the old source defect. The r-band guarantee rests on frozen study
selection, not on an overread of GZ DECaLS imagery or parent selection.

## Drift Check

No new drift found in the areas I previously passed:

- parity argument and one-band band decision remain bounded: colour affects sensitivity/power, not a
  separate chirality-sign channel;
- PC-1 is amended to `bands=r`, `size=128`, single-band float32 input;
- IC-1...IC-7 remain present with open constants as pre-sky binding slots;
- Tori successor route binding, Yui input-function/R1-R5 rerun, conditional PC-3/PC-4 local-path
  re-gate, and the old `nm_acquire_cutouts.py` execution prohibition remain binding prerequisites;
- BS-1 still FAILED as written;
- F-10, BS-11, HC-1H, HC-7, STOP, K-1...K-14, canonical boundary sentence, and supersession chain
  remain intact;
- K-8 remains untripped;
- the document still says this fixes the input contract, not the delivery route.

## Final Ruling

Nothing blocks freezing v3 on these bytes. Freeze may proceed only as a document freeze; all real
image access remains held until the successor route binding and input-function rerun receipts are
separately produced and gated.
