# Representation-boundary audit

The scientific claim was checked separately at four layers so source, storyboard, rendering, and encoded-artifact defects are not conflated.

## Layer 1 — frozen numeric/manuscript source

Verdict: `PASS` for the bounded claims used by the proposal.

The source distinguishes:

- median Delta crossing `z_m=6.328`;
- closure-envelope crossing `z_c=8.045`, where the 16th percentile reaches zero;
- separate, unpaired one-prior-family no-SFRD-tail run with crossing `z_c=7.615`;
- conditional shortfall fractions 66/83/93% at z=7/8/9;
- model-only/no-measurement status and proxy transport outside the Monte Carlo.

No source correction or figure-pixel change is required for these claims. The canonical manuscript figure already contains the Delta panel and both crossing semantics.

## Layer 2 — storyboard of record

Verdict: `FAIL`.

Classification: `MODEL/OUTPUT` at the storyboard layer.

- “required and inferred escape fractions part company” at 8.045 collapses the closure-envelope crossing into a generic curve-separation claim.
- “where every assumption is set against the result” at 7.615 broadens a one-prior no-tail test into an unsupported all-assumptions corner.
- 66/83/93 lacks displayed percent/redshift keys in the heading.

These are faithfully readable in the storyboard JSON; no capture loss is responsible.

## Layer 3 — current shared plot asset

Verdict: `FAIL`.

Classification: `REPRESENTATION/RENDERER`.

The plot builder places a vertical `crossing z=8.045` line on the required/inferred median-curve panel under “Where the two curves cross is the result.” The source value survives, but its scientific role does not. The representation omits the Delta panel that defines the value and therefore changes the meaning of the same number.

The plot also drops:

- median crossing `z_m=6.328`;
- Delta zero line and lower edge;
- keyed 66/83/93%;
- no-tail lower-edge curve and 7.615 crossing;
- both bootstrap ranges.

## Layer 4 — exact current MP4

Verdict: `FAIL`.

Classification: `CAPTURE/LINEAGE` plus preserved storyboard defects.

The exact encoded MP4 is older than both the current renderer and storyboard. It contains ten static cards, no figure, no audio, and tiny internal paths. It therefore cannot be used to conclude that the current renderer lacks figure support. It does, however, faithfully expose the audience artifact's current failures: no inspectable evidence geometry, unkeyed values, and unsupported 7.615 language.

The stale encoded artifact and the current storyboard are kept distinct in `FRAME_DIAGNOSIS.md`.

## Layer 5 — worker-Yui structured proposal

Verdict: `PASS`.

Classification: corrected proposal; not the storyboard of record.

`STORYBOARD_PROPOSAL.json` preserves separate semantic fields for narration, visual action, source anchors, allowed claim, forbidden implication, audience copy, and asset view state. Machine validation checks that every scene has these fields and that stale wording/internal audience paths are absent.

## Layer 6 — worker-Yui rendered static states

Verdict: `PASS_WITH_MINOR_INTEGRATION_REQUEST` on v4.

The structured proposal's values survive rendering, with late representation minors retained for integration:

- S02 preserves source values but omits the physical `f_esc=1` boundary even where the required band exceeds one;
- S04 visually separates `z_c=8.045` from `z_m=6.328`, but fine-root markers are overlaid on coarse z=0.5 polylines and therefore do not lie mathematically exactly on the displayed zero crossings;
- S05 renders correct percentages, redshift keys, and the conditional boundary, but a late paper-naive review classifies marker placement at median-Delta y-positions as a representation minor;
- S06 renders and labels separate/unpaired no-tail 7.615 versus fiducial 8.045;
- S07 preserves model-versus-measurement status and says its outside-model rail is not exhaustive;
- S08 preserves finding/evidence/boundary/next test.

v1's clipped S04 heading was a rendering/layout defect and is preserved rather than silently overwritten. v2 fixes that representation failure. v3 changes the S05 wording to the source-exact “conditional shortfall rises.” v4 adds finite-Monte-Carlo interval labels, separate/unpaired scenario status, a non-exhaustive boundary rail, and the escape-fraction definition while leaving the source geometry unchanged.

## Validator audit

No high-count external validator is involved. The local validator reports 21 checks and 21 passes. Its checks were inspected for the relevant failure modes:

- exact source hashes rather than path existence only;
- ordered continuous timeline rather than set membership;
- per-scene and total narration pacing;
- explicit stale/internal-copy blacklist;
- exact numeric-source values;
- output file hash and dimension checks;
- proposal-only/no-audio/no-MP4 state.

The validator does not claim visual clipping or semantic geometry from pixels; those remain separate full-resolution manual checks. This avoids treating a machine PASS as proof of rendered correctness.

## Custody conclusion

- Source packet: unchanged and hash-pinned.
- Storyboard of record: unchanged; blocked as-is.
- Shared renderer/plot tools: unchanged.
- Current public MP4: unchanged.
- Worker proposals: versioned v1/v2/v3/v4; failed and superseded attempts preserved.
- Integration and encoded-candidate acceptance: still owned by Hwao.
