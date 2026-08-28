# Known limitations and open gates

## Worker artifact limitations

1. This packet contains static visual states, not an encoded video canary. It does not test transition timing, animated masking, pacing, compression, or encoded-frame readability.
2. No narration audio exists. The proposed 98-second timeline and approximately 122 WPM text pacing have only been checked arithmetically, not against actual Alloy delivery at speed 1.18.
3. No audio checks are possible: there is no stream, peak, loudness, clipping, or A/V duration to inspect.
4. The exact finite-Monte-Carlo 16–84% resampling spans are visually very narrow on a z=6–10 axis. They are encoded as source-exact translucent spans and printed numerically; an integrator should not enlarge them for effect or present them as total-model or observational uncertainty.
5. The static proposal demonstrates target end states, not the temporal reveal grammar between them. Hwao must decide how to reveal axes, bands, and markers without obscuring scientific evidence.
6. The proposal uses a deterministic local redraw, not the shared renderer. Integration may expose typography or layout differences that require fresh encoded QA.
7. v4 draws coarse z=0.5 grid polylines while placing crossing markers at separately computed fine-root values. The offsets are near line width but are not mathematically exact; Hwao must insert the roots into the displayed geometry or use the same continuous/interpolated curve for roots and drawing.

## Scientific limitations that must remain visible

1. This is a literature-anchored model propagation, not a survey-data study and not a new measurement.
2. Required and inferred escape-fraction distributions are conditional on frozen priors and low-redshift proxy anchors.
3. Proxy-inferred escape fraction is z-independent by construction because the same low-redshift O32 and UV-slope calibrations are transported to all grid redshifts.
4. Proxy-calibration evolution with redshift is the dominant omitted systematic and sits outside the Monte Carlo; it is not the complete inventory of unpropagated assumptions.
5. The 66/83/93% values are conditional systematic mass with Delta greater than zero at z=7/8/9, not real-world probabilities that a cosmic shortfall exists.
6. `z_c=8.045` is the 16th-percentile Delta-envelope crossing. The median Delta crossing is a different value, `z_m=6.328`.
7. `z_c=7.615` belongs to a separate no-SFRD-tail model run with one prior family removed and unpaired Monte Carlo draws. It is not a paired one-variable counterfactual, an all-assumptions worst corner, or a full envelope over unrepresented systematics.
8. The high-redshift required-fraction tail can exceed one; this says the frozen anchors would have to move, not that a physical escape fraction above one exists.
9. In the frozen v4 S05 proposal, 66/83/93% markers are placed at median-Delta y-positions even though the percentages encode fractions of draws with Delta greater than zero. Hwao must separate the probability encoding from the median-Delta coordinates during integration.
10. The required-fraction band exceeds the physical `f_esc=1` boundary at the highest redshifts, but frozen v4 does not draw that boundary. The integrated canary must show that above-one required values mean no physical escape fraction closes the budget for that model space.
11. Several audience labels retain specialist shorthand (`SFRD`, `IGM`, proxy transport, frozen anchors, conditional model mass, fiducial, and high-redshift tail). These need compact first-use expansion or plain-language replacement during integration.

## Gates still closed

- Shared renderer or plot-tool edits.
- Storyboard-of-record edits.
- Official candidate rendering.
- TTS invocation or audio-file creation.
- Public MP4 replacement.
- Upload/publication.
- Website, cockpit, database, deploy, or restart changes.
- Git add/commit/push/merge.

## Exact unblock condition

Hwao may integrate only after explicitly accepting the two semantic corrections and selecting this proposal or an equivalent source-exact representation. The integrated silent canary then requires encoded full-resolution review before any TTS request is executed.
