# FINDING — the signed §6 pipeline identity has no implementing code; the pipeline amendment must exist BEFORE any development pixel is rendered (step 3) — 2026-09-06 11:01 KST

**Shape (Blanc's binding 1):** the signed TEXT and the pinned SCRIPTS disagree. Filed, not reconciled. Steps 1–2 (beacon, identity) touch no pixel and are unaffected; **step 3 (fetch + render of the 600 development objects) is BLOCKED** until the remedy the text itself names exists.

## What the signed V15 §6 says (line 48, verbatim excerpts)
"Rejecting maskbits: {1 BRIGHT, 3 SATUR_R, 6 ALLMASK_R, 10 BAILOUT, 13 CLUSTER}. Bit 11 MEDIUM is NOT rejecting; it is carried (§8.9d) and reported per raster as a covariate. Source pixels with nexp-r == 0 are REJECTING (replaced by the §8.9c lower median and flagged), in place of the present all-or-nothing §8.12 refusal — this is a relaxation of §8.12 … bounded by §8.14a's unchanged ceiling F ≤ 819 and unchanged protected radius r_T = 23 … Fixture updated to assert the new set both ways. These rules are frozen by this rule's signature **and by the pipeline amendment's**." §10 (line 69): "one two-seat gate on this rule, one on the pipeline amendment, one on V36."

## What the pinned code does (recomputed now)
- `study_renderer/pixel_rejection.py` SHA-256 8f66bc1c61173648… (pinned by the SIGNED Tier-C V35 §8.9a): `REJECT_BITS = (1, 3, 6, 10, 11, 13)` — MEDIUM rejects. Its fixture asserts exactly that six-bit set.
- `scripts/stage2_render_validation.py`: `if (raster.nexp <= 0).any(): raise REFUSED coverage` — the all-or-nothing §8.12 refusal V15 §6 relaxes. No code anywhere rejects nexp-r == 0 pixels per pixel.
- No pipeline amendment draft exists in the lane (no file matching AMEND*/PIPELINE* beyond the V12 amendment referee files of 09-04).

## Consequence
Rendering the 600 development tensors with the pinned code would produce tensors under the Tier-C identity (MEDIUM rejecting; whole-raster refusal on any zero-exposure pixel), NOT the identity the signed V15 fixes "before any new pixel". §6 also forbids any preprocessing change after the holdout — so the identity must be right at step 3 or the attempt is spent under the wrong pipeline. Duho's own honesty constraint (18:56): the pipeline fix is a SEPARATE amendment.

## What the text prescribes as the remedy (not an improvisation)
A **pipeline amendment** to the signed Tier-C V35 under its §17.6 change machinery: (i) a new pinned module (e.g. `study_renderer/pixel_rejection_v2.py`) with REJECT_BITS = (1, 3, 6, 10, 13), MEDIUM carried and reported per raster, nexp-r == 0 pixels rejected on the source grid and flagged, replacement statistic unchanged; (ii) fixture asserting the new set both ways and the nexp rule; (iii) the render path bounded by F ≤ 819 and r_T = 23 (a zero-exposure pixel inside 23 px still refuses); (iv) amendment text; (v) **one two-seat gate** (agy + codex-cli 0.153.4/gpt-6-astra, engines stamped); (vi) **Duho's signature**. The label-blind MEDIUM perturbation study of §6 runs on the TUNING set after step 3 and is a filed disclosure, not a gate.

## Time
Step 2 cannot start before 2026-09-07T00:15Z (09:15 KST Monday). The amendment can be drafted code-first today and gated before then, so no clock is lost — IF Blanc/Duho authorise drafting it now. Nothing in the option A sequence changes; step 3 simply acquires this prerequisite, and the run-sequence file is corrected to say so.

## Not touched
No pixel, no fetch, no draw, no edit to any signed text or any pinned file. The Tier-C-pinned `pixel_rejection.py` stays byte-identical (8f66bc1c…); the amendment adds a module, it does not edit the pinned one.
