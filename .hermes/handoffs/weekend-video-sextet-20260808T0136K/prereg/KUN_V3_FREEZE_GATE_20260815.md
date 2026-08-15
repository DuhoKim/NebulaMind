# Kun v3 preregistration freeze gate — 2026-08-15 KST

## Verdict

**HOLD_V3_FREEZE_FOR_GZ_DECALS_RATIONALE_REPAIR.**

The v3 candidate is structurally close, and the PC-1 amendment is applied in the right place, but I
would not freeze these exact bytes. The corrected Galaxy Zoo DECaLS rationale still contains one
overstrong sentence that turns a sourced "primarily includes" selection statement into an every-parent
guarantee.

Blocking sentence, in `LANA_PC1_INPUT_AMENDMENT_20260815.md` §2(c):

> "Every parent therefore has secure r-band flux by construction, whereas g flux for the reddest
> spirals is not guaranteed at equal S/N — a color-dependent sensitivity subpopulation g would create
> and r avoids."

The first clause is too strong as written. The local Walmsley source says NSA **primarily** includes
galaxies brighter than `m_r = 17.77`, and explicitly notes fainter exceptions in deeper areas or spare
fibres. That source supports an r-limited tendency and a strong r-band rationale; it does not support
"Every parent" by itself. The study's own frozen cuts do support r-band positivity/brightness for the
selected study parent (`flux_r > 0`, `dered_mag_r < 17.7`), so this is repairable without changing the
science decision.

Exact repair that would clear this blocker:

> "For the study's selected parent, r is directly constrained by the frozen `flux_r > 0` and
> `dered_mag_r < 17.7` cuts. Walmsley et al. 2022 separately supports that the GZ DECaLS NSA parent is
> primarily r-limited (`m_r = 17.77`), while noting exceptions; the r-band guarantee here therefore
> rests on our frozen study cuts, not on a claim that every GZ DECaLS source is r-limited."

Apply the same repair to the incorporated v3 §6 summary if needed, so the freeze candidate does not
summarize the rationale more strongly than the amendment.

## Exact Artifacts Checked

Hashes and mode recomputed from disk:

| Artifact | SHA-256 / mode |
|---|---|
| `_tmp_KUN_V3_FREEZE_GATE_BRIEF.md` | `210b2c33b0a6d77d8b7bfc15dae3cf278ddea7a90e8441bd98bf1da951dca6f8` |
| `PREREG_LONGO_AMPLITUDE_TEST_20260815_V3_CANDIDATE.md` | `8ba037ec79f641baa9c78b4956c1155218d87229e6bd5c4f738cb4e8672afd05` |
| `LANA_PC1_INPUT_AMENDMENT_20260815.md` Rev 2 | `16a4a6019a90e4c90d690c0b058bdd1e5a8ef51deb17d9012da9df274f2696e1` |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md` | `62dad44dd92acf2781d2c8cf25161f7f344e3fe6f7fec35b7e04308bd1539c12`, mode `444` |

The frozen 08-15 v2 file is intact and read-only. I did not freeze, fetch, run, commit, push, publish,
or accept anything.

## GZ DECaLS Correction

The original wrong claim that GZ DECaLS classification imagery was "r-dominated" is gone as a live
claim. It now appears only in the open correction record, where the document says it was wrong and
that volunteer images were `grz` composites. That part is good.

The replacement source is partly right:

- local Walmsley evidence supports NSA selection as primarily `m_r = 17.77` with `z <= 0.15` and
  Petrosian radius criteria;
- the same source explicitly records exceptions below the nominal `m_r = 17.77` limit;
- the project's own frozen photometric cuts independently require positive r-band flux and
  dereddened `r < 17.7`.

So the band decision survives, but the wording must make the support chain precise. Do not let
"primarily includes" become "every parent" in a frozen public record.

## Other Gate Checks

The rest of the v3 candidate is acceptable subject to the single blocker above:

- PC-1 is amended to `bands=r`, `size=128`, single 128x128 float32 input, delivered raster consumed
  whole.
- The old `bands=grz` / `size=256` text appears only as the defect being superseded or in quoted
  historical context.
- IC-1...IC-7 cover band/plane, units, background, invalid pixels, scaling, float32/layout, and
  mirror point. The open invalid-fraction cap and scaling constants are named as binding slots filled
  on synthetics only before sky access.
- The R1-R5 / retention / calibration rerun is stated as a binding prerequisite to sky access.
- Tori's successor route binding, local-path PC-3/PC-4 re-gate if needed, and the prohibition on
  executing the old `nm_acquire_cutouts.py` route are binding prerequisites, not casual notes.
- BS-1 still FAILED as written; F-10, BS-11, HC-1H, HC-7, STOP, K-1...K-14, and the canonical null
  boundary carry forward.
- K-8 is untripped: the candidate states no real-sky statistic, chirality label, sky estimand,
  unblinding, or science cutout exists.
- The candidate correctly says it fixes the input contract, not the delivery route; acquisition is
  still unresolved pending the operator/near-data route decision.

## Final Ruling

Something does block freezing v3: the repaired GZ DECaLS rationale still overstates the selection
source as an every-parent r-band guarantee. Fix that sentence and any incorporated summary that
inherits it; then return the new hash for a tight re-gate. Execution remains held regardless.
