# QA summary — worker-Yui FESC pass

## Overall worker verdict

`PASS_WITH_MINOR_INTEGRATION_REQUEST` on `visual_proposal_v4`.

`BLOCKED_AS_IS` for rendering from the current storyboard/current dark plot because two semantic errors must be corrected by Hwao first.

This is not an encoded-candidate verdict. No official candidate, MP4, audio, or TTS artifact exists in this worker lane.

## Current public MP4

Verdict: `FAIL`.

Exact artifact:

- SHA-256 `840ced2b52c2007bc5387fc69b49527c548daca6f6d81b3f14bc9a43b7e9b5af`
- 86.000 s, 1920×1080, 30 fps, H.264, video-only
- ten static card states at 0/7/15/23/31/38/46/56/65/74 s

Failures:

- stale relative to the 16-card storyboard and current renderer;
- no audio despite narrated-video intent;
- no scientific figure, axes, bands, or markers;
- unkeyed `66 to 83 to 93` headline;
- `z=8.045` presented without the Delta-envelope geometry;
- `z=7.615` overdescribed as every assumption set against the result;
- tiny internal paths used as source labels;
- end frame omits finding, evidence, uncertainty, and next test.

Evidence: `FRAME_DIAGNOSIS.md`, `qa/current/contact_sheet.jpg`, `qa/current/full_resolution_frames/`.

## Source/semantic audit

Verdict: `BLOCK_AS_IS__CORRECTABLE`.

Verified from the frozen numeric source:

- fiducial closure-envelope crossing: `z_c=8.045284271240234`;
- fiducial bootstrap 16/50/84: `8.03008071899414 / 8.045955657958984 / 8.059269256591797`;
- median Delta crossing: `z_m=6.327877044677734`;
- no-SFRD-tail closure crossing: `z_c=7.615345001220703`;
- no-tail bootstrap: `7.601756134033203 / 7.61572265625 / 7.631122589111328`;
- shortfall fractions at z=7/8/9: `0.659525 / 0.833525 / 0.927475`, rendered as `66% / 83% / 93%`;
- shortfall fraction is monotone over the frozen z=6–10 grid.

Two current-storyboard/current-plot mismatches are recorded in `SOURCE_FREEZE.json` and `REQUEST_TO_INTEGRATOR.md`.

## Storyboard proposal checks

Target: `STORYBOARD_PROPOSAL.json` SHA-256 `49db67e9c565eef6c8ec0f53bf348e8ecf1f581168507ce6eb2fa24c4a44c182`.

- Eight continuous scenes over 98 seconds.
- 200 narration words after the v4 disclosure and plain-language edits.
- Delivered pacing is approximately 122 WPM; every scene is at or below 130 WPM.
- Every scene has a source anchor, visual action, allowed claim, and forbidden implication.
- No stale “two curves cross at 8.045,” “part company,” or all-assumptions wording remains.
- No internal path appears in proposed audience copy.
- No face, presenter, manuscript cover, section-divider card, or URL close is proposed.

## Static visual iterations

### v1 — fail

Preserved under `visual_proposal/`.

- S04 right-rail heading clipped.
- S06 did not label fiducial and no-tail crossing lines explicitly enough.

### v2 — pass after targeted correction

Preserved under `visual_proposal_v2/`.

- S04 heading corrected.
- S06 labels and rail explicitly distinguish no-tail `7.615` from fiducial `8.045`.

### v3 — superseded after adversarial disclosure review

Target: `visual_proposal_v3/manifest.json` SHA-256 `7ce0ad43ac03e4d4afceca2cde9834a40b15c495a8ea74bec924b3c81416ed6c`.

Contact sheet SHA-256: `9268d6ef996c20f76f5f0bac4d98e998a5575ebffb1bde9a01a6bed1ac9f79f8`.

v3 replaces the S05 wording “deficit deepens” with the source-exact “conditional shortfall rises.” Full-resolution S05 inspection found no clipping, collision, or ambiguity. An independent adversarial pass then found disclosure debt in generic bootstrap labels, an apparently complete inside/outside inventory, and paired-counterfactual implications in `ONE CHANGE` wording.

### v4 — recommended

Target: `visual_proposal_v4/manifest.json` SHA-256 `683460640960402716741303b38d833e1edece2a95806f912ba4c640f5f38622`.

Contact sheet SHA-256: `d3913812de4bf8a01c8ab9b875e1d5c2f2f4158d9200491402d4617c7d1d6fb7`.

v4 keeps the exact scientific geometry while adding a plain-language escape-fraction definition, finite-Monte-Carlo 16–84% resampling labels, separate/unpaired no-tail-run disclosure, and a `not exhaustive` model-boundary rail.

Full-resolution review status:

- S02 evidence curves: values pass; late scientific review retains a disclosure minor because the high-z required band exceeds physical `f_esc=1` without a drawn boundary;
- S04 closure values/roles: pass; late scientific review retains a geometry minor because fine-root markers are overlaid on coarse z=0.5 polylines rather than inserted into the displayed curves;
- S05 keyed values/conditions: pass; late paper-naive review retains a representation minor because percentage markers sit at median-Delta y-positions;
- S06 no-tail versus fiducial: pass;
- S07 model boundary: pass;
- S08 scientific close: pass.

Detailed evidence: `qa/proposal/FULL_RESOLUTION_REVIEW.md`.

## Machine validation

`qa/proposal/machine_validation.json` SHA-256 `47302d860f3ac5d5087a9773feeec5900c0049fd8d55da9d303019eb603ae1f7`.

Result: `21/21 PASS`.

Checks cover source hashes, timeline continuity, narration pacing, scene contracts, stale/internal audience copy, keyed values, exact crossing values, monotonicity, state count, file hashes, dimensions, proposal-only status, and absence of audio/MP4 output.

`qa/proposal/visual_state_difference.json` independently compares adjacent v4 PNGs. Every pair exceeds the 0.5% changed-pixel floor; observed changed fractions range from 2.271% to 13.128%. This establishes visually distinct evidence states, not temporal-motion quality.

`qa/proposal/OCR_REVIEW.md` records Tesseract 5.5.2 support checks on v4 S01 and S04–S08. The escape-fraction definition, critical crossing values, keyed percentages, separate/unpaired scenario wording, finite-Monte-Carlo bounds, non-exhaustive model boundary, and closing next test were recovered. This applies to source-resolution PNGs only; encoded-frame OCR remains a Hwao canary gate.

Search verification found zero `.mp4`, `.wav`, or `.mp3` files under the official worker directory.

## Independent reviews

Two isolated review passes were dispatched:

- paper-naive comprehension review of visuals plus narration only;
- adversarial scientific audit against the frozen JSON, manuscript, and canonical figure.

A compact final-v4 paper-naive pass returned `PASS` and recovered the leakage question, closure-envelope meaning of 8.045, all keyed percentages, the separate no-tail change and earlier 7.615 crossing, conditional-model status, proxy-transport limitation, and next measurement. Its ultra-compact response said `C=none`; an expanded pass on the same v4 target identified one residual confusion: the concrete proxies and “proxy transport” are unspecified. The aggregate grade is `PASS_WITH_TERMINOLOGY_CONFUSION`. Verbatim evidence and grading are in `qa/proposal/INDEPENDENT_PAPER_NAIVE_V4.md`.

The final compact and expanded source-backed adversarial passes returned `PASS` with `R=none`. They independently recovered `z_c=8.045` as the lower-Delta-16 crossing, `z_m=6.328` as the median crossing, no-tail `z_c=7.615`, and keyed 66/83/93%; confirmed separate/unpaired no-tail status and finite-Monte-Carlo/model/no-measurement/non-exhaustive disclosures; replayed the source pipeline to `4.44e-16`; and found no audience path exposure. Verbatim evidence is in `qa/proposal/INDEPENDENT_SCIENTIFIC_V4.md`.

A late asynchronous v3 paper-naive review returned `MINOR`. Most terminology findings were resolved by v4, but its observation that 66/83/93% markers sit at median-Delta y-positions still applies. That placement can imply the median curve itself encodes probability. `LATE_V3_REVIEW_RECONCILIATION.md` preserves the result and requests a dedicated probability strip/panel or an x-keyed rail/table outside Delta data coordinates. Scientific values and the 21/21 machine result are unchanged.

A second late pre-v4 batch returned paper-naive `MINOR` for undefined specialist shorthand and scientific `MINOR` despite reproducing every core number. Three scientific findings were already resolved by v4: finite-Monte-Carlo labels, non-exhaustive outside-model disclosure, and separate/unpaired no-tail status. Two representation findings survive: fine roots do not lie mathematically exactly on the coarse displayed polylines, and the required-fraction band exceeds physical `f_esc=1` without a visible boundary. Worker-Yui independently reproduced both in `qa/proposal/late_review_numeric_replay.json`. `LATE_V3_REVIEW_RECONCILIATION.md` now reconciles both late batches and carries exact Hwao requests.

A third late compact v3 batch returned paper-naive `PASS` and scientific `BLOCK`. The `BLOCK` is v3-specific: exhaustive-looking S07 boxes plus generic `bootstrap` and `ONE CHANGE` wording. v4 had already corrected all of those items, so no new v4 blocker is introduced. Its remaining paper-naive `SFRD`/`IGM`/`proxy transport` confusion reinforces the existing first-use terminology request. Exact compact results are preserved in `qa/proposal/archive/LATE_COMPACT_*_V3.json`.

## Gates not tested here

Because Hwao controls integration, this worker did not and cannot claim:

- silent encoded-canary pass;
- transition/motion pass;
- encoded typography pass;
- narration/TTS pass;
- audio loudness or clipping pass;
- A/V fit pass;
- official candidate pass;
- upload or publication readiness.
