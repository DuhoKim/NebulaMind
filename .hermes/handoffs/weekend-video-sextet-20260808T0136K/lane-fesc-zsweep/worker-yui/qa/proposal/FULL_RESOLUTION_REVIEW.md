# Full-resolution visual review — static proposal only

## Scope

- v1 contact sheet and critical 1920×1080 states were inspected after rendering.
- v1 is preserved under `visual_proposal/`; it is not accepted.
- v2 is preserved under `visual_proposal_v2/`; it fixed the first layout defects.
- v3 is preserved under `visual_proposal_v3/`; it sharpened the S05 conditional-shortfall wording.
- v4 is preserved under `visual_proposal_v4/`; it is the recommended review proposal.
- No MP4, audio, official candidate, or shared-tool mutation was produced.

## v1 disposition: FAIL — targeted revision required

The scientific sequence was coherent, plot-primary, and free of internal audience paths. S04 correctly attached `z_c=8.045` to the lower Delta envelope edge at zero and kept `z_m=6.328` separate. S05 keyed 66%, 83%, and 93% to redshifts 7, 8, and 9. S07 preserved the evidence plot while marking the outside-Monte-Carlo proxy-transport limitation. S08 retained finding, evidence, boundary, and next test.

Two visual issues required revision:

1. S04 right-rail heading “Keep two crossings separate” clipped at the right edge.
2. S06 showed the fiducial and no-tail vertical lines but did not label both crossings explicitly enough for a single-state read.

## v2/v3 disposition: superseded after adversarial disclosure review

The v2/v3 geometry and layout passed, but an independent adversarial source audit identified non-blocking disclosure debt: generic `bootstrap` labels, an inside/outside rail that could be mistaken for a complete inventory, and `ONE CHANGE` language that could imply paired Monte Carlo draws. v4 corrects those issues without changing any scientific geometry.

## v4 disposition: PASS_FOR_INTEGRATOR_REVIEW

### Contact-sheet progression

The eight states now read as a single progressive argument:

1. question plus evidence preview;
2. required versus proxy-inferred curves and bands;
3. Delta definition, envelope, and zero line;
4. closure-envelope geometry and distinct median crossing;
5. keyed conditional shortfall fractions;
6. exact one-prior no-tail scenario comparison;
7. inside-versus-outside-model boundary;
8. held scientific summary.

There are no face/presenter states, manuscript covers, section-divider cards, URL end cards, or full-screen prose-only cards. The same two-panel evidence surface persists, so state changes correspond to reasoning progress rather than arbitrary motion.

Late scientific addendum: `MINOR`. The top-panel required-fraction band exceeds physical `f_esc=1` at the highest redshifts, but v4 does not draw that boundary or explain that above-one required values mean no physical escape fraction can close the budget for that model space.

### S04 — closure crossing

PASS.

- Right-rail heading is fully visible after shortening to “Two different crossings.”
- The green `z_c=8.045` line and marker are attached to the lower Delta envelope edge at the zero line.
- The 8.030–8.059 interval is explicitly labeled `finite-MC 16–84%` in the rail so it cannot be mistaken for observational confidence or total model uncertainty.
- A separate grey dotted line and rail entry identify median crossing `z_m=6.328` as not the headline criterion.
- Top-panel median curves are not marked as crossing at 8.045.
- Axes, ticks, zero line, band, median, lower edge, legend, and audience provenance are present.
- No clipping or curve-covering text was found. The bootstrap interval is too narrow to be visually wide at this scale, but it is encoded as a translucent vertical span and stated numerically.

Late scientific addendum: `MINOR`. The displayed curve uses coarse z=0.5 grid segments while markers use separately computed fine roots. Insert the frozen roots into the displayed polylines or use the same continuous/interpolated curve for drawing and root finding so each marker lies mathematically on the rendered zero crossing.

### S05 — keyed probabilities

PASS.

- `66%`, `83%`, and `93%` are each attached to visible markers at `z=7`, `z=8`, and `z=9` on the Delta panel and repeated in the rail.
- Each is stated as the conditional mass with `Delta > 0`; the rail says “conditional model mass, not real-world probability.”
- Percentage labels do not collide with each other, curves, axes, or the rail.
- The top comparison and bottom uncertainty surface remain complete and readable.

Late paper-naive addendum: `MINOR`. The numeric keys and conditions are correct, but the percentage markers sit at median-Delta y-positions. Because the percentages encode fractions of draws with Delta greater than zero, Hwao should use a dedicated probability strip/panel or move them to an x-keyed rail/table outside the Delta data coordinates.

### S06 — separate no-tail scenario run

PASS after v4 disclosure revision.

- Heading and rail say `Separate no-tail run`.
- `ONE PRIOR FAMILY` states exactly that the JWST-motivated SFRD tail is removed and the draws are unpaired.
- White dotted 16th-percentile curve and white vertical crossing are labeled `no-tail 7.615`.
- Green fiducial crossing is labeled `fiducial 8.045`.
- Rail repeats both values and labels 7.602–7.631 as finite-Monte-Carlo 16–84% resampling bounds.
- Direction is explicit: the earlier no-tail crossing means closure gets harder.
- No all-assumptions or worst-corner language remains.
- Full-resolution labels are legible and do not overlap the legend, curves, axes, or each other.

### S07 — model boundary

PASS.

- Persistent chip says “MODEL OUTPUT · NO NEW MEASUREMENT.”
- Rail labels propagated terms as examples rather than a complete inventory.
- Proxy transportability is labeled the dominant omission; a separate `NOT EXHAUSTIVE` row says other structural assumptions remain unpropagated.
- `no survey measurement in this study` is prominent.
- The evidence plot remains visible and complete.
- The rail is categorical status design, not quantitative geometry; it does not invent values.
- No clipping or collision was found.

### S08 — scientific close

PASS.

- Finding: closure envelope leaves zero at `z_c=8.045`.
- Evidence: lower Delta edge crosses zero; finite-Monte-Carlo 16–84% bounds are 8.030–8.059.
- Boundary: frozen low-redshift anchors; no new measurement.
- Next test: measure proxy transport at high redshift.
- The final frame retains the complete top comparison and bottom Delta evidence surface rather than replacing it with branding.
- No clipping, overlap, or internal provenance path was found.

## Remaining integration checks

These static states are not an encoded-video pass. If Hwao chooses to integrate them, the official candidate still needs:

- temporal reveal verification rather than simple hard cuts between full states;
- encoded 1920×1080 frame inspection at every transition and safety-critical value;
- narration-fit checks against actual Alloy audio at speed 1.18;
- audio-stream, peak, loudness, and A/V-duration checks;
- a fresh contact sheet and first/middle/last review from the encoded candidate;
- confirmation that shared renderer labels reproduce the v4 crossing, resampling, scenario-run, and model-boundary semantics exactly.
