# Request to Hwao — FESC graphics-first integration

This is a review/evidence request only. Worker Yui did not edit shared tools, alter the storyboard of record, render an official candidate, invoke TTS, or touch the public MP4.

## Integrator decision requested

Please accept or reject these two source-backed corrections before rendering:

1. `z_c=8.045` must be shown as the point where the 16th percentile of `Delta = required − inferred` reaches zero and the 16–84% interval stops spanning zero. It must not be represented as the first crossing of the required and inferred median curves; that median crossing is `z_m=6.328`.
2. `z_c=7.615` must be labeled as a separate `boost=none` / no-SFRD-tail model run, with one named prior family removed and unpaired Monte Carlo draws. It must not be called a corner where every assumption is set against the result or shown as a paired one-variable counterfactual.

Until these are integrated, `video_reportable_now=false` for an official render from the current storyboard/plot.

## Exact current-storyboard conflicts

- Lines 45–48: replace “where the required and inferred escape fractions part company” with “where the 16th-percentile Delta edge reaches zero and the 16–84% interval stops spanning zero.”
- Lines 53–56: replace heading `66 to 83 to 93` with keyed percent/redshift labels and replace “probability mass” with “conditional systematic mass with Delta greater than zero.”
- Lines 61–64: replace “least-favourable corner, where every assumption is set against the result” with “separate no-SFRD-tail model run, where one prior family is removed and the Monte Carlo draws are not paired to the fiducial run.”
- Lines 21–27: the heterogeneous literature scatter is optional context, not the central evidence surface; do not imply it establishes a coherent observed trend.
- Lines 37–41, 68–72, 89–93, and 111–115: suppress full-screen section dividers in the canary.
- Lines 82–86: process/referee history is secondary provenance and should not displace the Delta/crossing evidence in a short scientific canary.
- Lines 118–123: replace the branded URL close with the finding/evidence/boundary/next-test hold in S08.

## Recommended proposal

Use:

- `STORYBOARD_PROPOSAL.json`
- `visual_proposal_v4/manifest.json`
- `visual_proposal_v4/static_states_contact_sheet.jpg`
- `qa/proposal/machine_validation.json`
- `qa/proposal/FULL_RESOLUTION_REVIEW.md`

The v1–v3 visual attempts are preserved for review history. v4 is the recommended state packet after full-resolution, finite-Monte-Carlo, model-boundary, scenario-run, and plain-language revisions.

## Requested shared-renderer behavior

1. Build one persistent two-panel evidence surface from the frozen numeric arrays.
2. Reveal axes and plain-language variable definitions before curves; expand specialist shorthand at first use.
3. Reveal required and proxy-inferred medians plus 16–84% bands, with a labeled physical `f_esc=1` boundary and an explanation that required values above one cannot be met by any physical escape fraction.
4. Reveal Delta, its zero line, median, lower edge, and full systematic envelope.
5. At `z_c=8.045`, attach the marker and vertical line to the lower Delta edge at zero; label 8.030–8.059 as finite-Monte-Carlo 16–84% resampling bounds, not observational or total-model uncertainty. Insert the frozen root into the displayed polyline, or draw the same continuous/interpolated geometry used to compute it, so the marker lies exactly on the rendered zero crossing. Apply the same rule to `z_m=6.328` and no-tail `z_c=7.615`.
6. Keep `z_m=6.328` separate and subordinate.
7. Key `66% @ z=7`, `83% @ z=8`, and `93% @ z=9`, with “conditional model mass, not real-world probability.” Do not place these percentage markers at median-Delta y-coordinates: use a dedicated probability strip/panel, or an x-keyed rail/table outside the Delta data coordinates.
8. Add the separate no-SFRD-tail run's 16th-percentile curve, `z_c=7.615`, finite-Monte-Carlo 16–84% bounds 7.602–7.631, an unpaired-draw disclosure, and a clear fiducial `z_c=8.045` comparator.
9. Retain the plot while showing propagated examples, the dominant proxy-transport omission, and an explicit `not exhaustive` model-boundary note; do not replace evidence with a paragraph card or imply a complete uncertainty inventory.
10. End on finding, evidence, boundary, and next test, with the plot still visible.

## Presentation constraints

- 1920×1080, 16:9, no presenter or face.
- Graphics/plot primary for the full canary.
- No manuscript cover, section-divider cards, or branded URL close.
- No internal repository paths in audience frames.
- Minimum encoded material text height: 24 px.
- Keep the persistent audience chip: `MODEL OUTPUT · NO NEW MEASUREMENT`.
- Keep audience provenance: `NebulaMind z-sweep model output (2026-08-04) · 40,000 draws per redshift · conditional on frozen low-z proxy anchors`.
- Do not enlarge narrow bootstrap spans or invent geometry for visibility.
- Add compact first-use glosses for `SFRD`, `IGM`, proxy transport, frozen anchors, conditional model mass, fiducial, and the high-redshift tail if those terms remain audience-visible.

## Silent-canary gate

Please render and inspect the silent visual canary before any narration work. Required evidence:

- ffprobe dimensions, fps, duration, and stream inventory;
- contact sheet covering every transition;
- full-resolution frames for S04, S05, S06, S07, and S08 equivalents;
- encoded confirmation that all axes/ticks/bands/markers/zero lines remain visible;
- no clipping, text collisions, raw paths, or value/condition separation;
- no visual implication that 66/83/93% are median-Delta y-values;
- crossing markers lie exactly on the displayed curve geometry, not only within line width;
- the `f_esc=1` physical boundary and above-one interpretation remain visible;
- first-use specialist terms are expanded or replaced with plain-language equivalents;
- independent check that 8.045 and 7.615 remain attached to the correct source geometry.

## TTS request after silent-canary PASS only

If and only if Hwao accepts the silent canary:

- provider: Nous managed TTS;
- voice: Alloy;
- speed: 1.18;
- copy: `STORYBOARD_PROPOSAL.json:/scenes/*/narration_proposal` after any integrator wording revision receives fresh scientific review;
- target delivered pacing: approximately 122 WPM over 98 seconds;
- do not change provider or voice without an explicit blocker and revised request.

After encoding narrated output, verify audio stream presence, duration, peak/loudness, clipping, A/V fit, and full-resolution transition frames. Worker Yui has not authorized upload or public replacement.
