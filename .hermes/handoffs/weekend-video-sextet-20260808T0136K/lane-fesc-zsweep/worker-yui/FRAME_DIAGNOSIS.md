# Encoded-frame diagnosis — exact current MP4

Target inspected read-only: `frontend/public/videos/fesc-zsweep-photon-budget.mp4`

SHA-256: `840ced2b52c2007bc5387fc69b49527c548daca6f6d81b3f14bc9a43b7e9b5af`

## Media facts

- 86.000 s; 1920×1080; 30 fps; H.264 High/yuv420p.
- One video stream only. There is no audio stream.
- Scene detector threshold: `gt(scene,0.02)`.
- Ten static-card states beginning at 0, 7, 15, 23, 31, 38, 46, 56, 65, and 74 seconds.
- The exact extracted contact sheet is `qa/current/contact_sheet.jpg`.
- Five safety-critical full-resolution frames are preserved under `qa/current/full_resolution_frames/`.

## Lineage finding

The exact MP4 is stale relative to the storyboard of record and current shared renderer:

- Encoded: 10 cards, 86 s, no figure, no section states, no audio.
- Storyboard of record: 16 cards, nominal 102.5 s, one literature figure, five full-screen section cards, and two character flags.
- The MP4 predates both the current storyboard and renderer hashes frozen in `SOURCE_FREEZE.json`.

This is an artifact-lineage failure and a presentation-grammar failure. The stale MP4 cannot be used to infer that the current renderer lacks figure support, but it is the exact artifact the user sees and therefore remains the correct diagnosis target.

## Timestamped observations from encoded frames

### 0–7 s — question hook

The opening asks whether reionization has enough photons, but the screen is a title plus paragraph on an almost empty navy field. It does not preview the two compared quantities, the model-only status, or the central envelope-crossing geometry.

### 7–15 s — verbal comparison only

“The shape of the question” correctly distinguishes required from inferred escape fraction, but no axes, variables, curves, envelope, or comparison design is visible. The scientific relationship is asserted rather than inspectable.

### 15–23 s — `z = 8.045`

The full-resolution 19 s frame is clean and unclipped, but it is a giant number with prose and a tiny `TREND_RESULTS.json` path. There is no Delta axis, zero line, 16th-percentile envelope edge, uncertainty band, or comparison curve.

More importantly, the wording says this is where required and inferred escape fractions “part company.” The frozen numeric source defines 8.045 as where the 16th percentile of Delta reaches zero and the 16–84% interval stops spanning zero. The median required/inferred crossing is instead `z_m = 6.328`. The frame is therefore not only non-inspectable but semantically imprecise.

### 23–31 s — trend claim without trend

“The trend is the result” is a sound narrative steer, but the screen remains a prose card. No sweep, grid points, deficit axis, uncertainty, or keyed redshift sequence appears.

### 31–38 s — `66 to 83 to 93`

The full-resolution 34.5 s frame omits percent symbols from the headline and does not key the values to `z=7`, `z=8`, and `z=9`. The body supplies only “as redshift climbs.” No plotted probability mass, zero baseline, uncertainty envelope, or monotonic sequence is visible. The tiny rendered source is a repository-relative review-loop path, not an audience citation.

The exact source supports rounded `66%`, `83%`, and `93%` at redshifts 7, 8, and 9 respectively. Those conditions must be displayed with the values.

### 38–46 s — `7.615`

The full-resolution 42 s frame is unclipped and readable, but the number is detached from the no-tail curve and its 7.602–7.631 bootstrap interval. The card calls it a least-favourable corner “where every assumption is set against the result.” The source supports only a specific `boost=none` corner in which the JWST-motivated SFRD-tail term is removed; the other frozen assumptions remain. This is a hard semantic mismatch, not merely a missing label.

### 46–56 s — status/limitation boundary

The 51 s limitation frame clearly states that the study contains no measurements, transports `z≈0.3` calibrations unchanged, and reports conditional probability mass given frozen anchors rather than the probability of a real shortfall. This is the strongest semantic boundary in the current artifact.

The text is unclipped and prominent, but it arrives after three unvisualized result cards. There is no retained plot or visual link showing which band/probability the limitation qualifies. Raw `z~0.3` notation and an internal repository path weaken the scientific presentation.

### 56–65 s — proxy-transport escape route

The card correctly names proxy transport failure as the route by which the result could fail. It is another paragraph-only hold, with no diagram distinguishing systematics propagated inside the Monte Carlo from the dominant systematic outside it.

### 65–74 s — referee arithmetic

The artifact switches from scientific evidence to process history. “Sixteen decimal places” and `MINOR` are not tied to a reproducibility table, hash, or compact result. This is secondary provenance and should not displace the central uncertainty/scenario visual in a short canary.

### 74–86 s — branded close

The closing frame says the result is a number about a model of the literature, not the sky. That status language is useful, but the frame does not preserve the finding (`z_c=8.045`), its evidence (16th-percentile edge crossing zero), its uncertainty (8.030–8.059), the no-tail comparison (7.615), or the next empirical test (high-redshift proxy transport). A URL heading is not a scientific summary.

## Current plot-asset diagnosis

The dark video plot asset is more scientific than the MP4 because it shows redshift and escape-fraction axes, required and inferred medians, and 16–84% bands. However, it places a vertical `crossing z = 8.045` line on the median-curve panel under the title “Where the two curves cross is the result.” That representation conflates:

- median-curve crossing: `z_m = 6.328`; and
- closure-envelope crossing: `z_c = 8.045`, where the 16th percentile of Delta reaches zero.

It also omits the Delta panel, keyed 66/83/93% deficit values, no-tail 16th-percentile curve, 7.615 scenario crossing, and the bootstrap bands for both crossings. It must not be reused unchanged.

## Required visual correction

Use a progressive two-panel evidence surface derived from `TREND_RESULTS.json` or the canonical manuscript figure:

1. reveal redshift and escape-fraction axes plus plain-language definitions;
2. reveal required and proxy-inferred median curves with their 16–84% bands;
3. reveal Delta and its zero line;
4. mark `z_c=8.045` where the lower envelope edge reaches zero, with 8.030–8.059 uncertainty;
5. key `66% @ z=7`, `83% @ z=8`, and `93% @ z=9` on the deficit panel;
6. compare the fiducial lower edge with the no-SFRD-tail lower edge and mark `z_c=7.615` with 7.602–7.631 uncertainty;
7. end with finding, evidence, model-only boundary, and the proxy-transport measurement needed next.

No generated or inferred geometry is needed: all plotted values are fully recoverable from the frozen source.
