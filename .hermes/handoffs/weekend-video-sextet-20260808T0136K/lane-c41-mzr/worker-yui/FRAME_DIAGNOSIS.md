# C41 MZR encoded-frame diagnosis

Authority: Hwao weekend order. This is paper-lane QA only; it is not an integration or publication decision.

## Exact artifact inspected

- Current MP4 SHA-256: `02a26fa3449dd5dfc070b21988430ec51bd8d69d40adcc883a4ff2cba7831ed8`
- Probe: 1920×1080, H.264, 30 fps, 81.000 s, no audio stream.
- Scene-change times: 9, 18, 26, 33, 41, 50, 60, and 69 seconds, yielding nine observed scene states.
- Current source storyboard: 16 cards, 107.5 s of duration floors.
- Verdict: `FAIL_AS_CURRENT_CANDIDATE__ARTIFACT_LINEAGE_AND_REPRESENTATION_BOUNDARY`.

The encoded MP4 does not match the current storyboard lineage. Its nine text-only states omit the source storyboard’s figure and section cards.

## Frame-level findings

### Opening and motivation

The opening question and the direct-temperature-anchor motivation are understandable. No full-frame clipping was seen. The body paragraphs are readable at full resolution but too visually static to carry a scientific evidence story alone.

### 79 → redshift/join → reachability

The `79 tables` heading correctly attaches the unit `tables` to 79. The subordinate sentence contains the redshift/join count 23, but it does not promote 23 to its own `candidate tables` visual state.

The same sentence says that `8 were reachable at run time`. Frozen run evidence instead says:

- 23 candidate tables were redshift-joinable;
- 11 tables were fetched at run time;
- those 11 tables belonged to 8 catalogs;
- 12 candidate tables were unreachable.

The current wording visually makes 8 look like a table count. This is a material unit ambiguity, not merely a styling preference.

### 95 rows

The 29.5-second frame leads with a giant unqualified `95`. `Rows` appears only in body prose. A viewer scanning the metric hierarchy can conflate this with the preceding table count. The required fix is a primary `95 z > 3 ROWS` unit chip plus an explicit `TABLES → ROWS` bridge.

### 5 anchors

The 37-second frame likewise leads with an unqualified `5`. `Contract-grade direct-temperature anchors` appears only below it. The required fix is a primary `5 CONTRACT-GRADE ANCHORS` unit chip plus an explicit `ROWS → ANCHORS` bridge.

### Row-accounting evidence

No encoded frame shows how 95 rows close to five anchors. The same-unit accounting is available and exact:

- 64 below the λ4363 signal-to-noise floor;
- 12 without Hβ;
- 6 missing required λ4363 or λ5007 flux;
- 8 temperature failures;
- 5 contract-grade survivors.

Because all five categories have the unit `rows`, a proportional 95-cell or 95-row accounting visual is truthful here.

### Mass-bin null

The 45.5-second frame states the null only as prose. It does not show axes, bin counts, the pre-committed shared minimum, or the below-floor pool.

The reportable visual is:

- x-axis: stellar-mass bin, `log10(M*/M_sun)`;
- y-axis: contract-grade anchors, `N`;
- actual bars: 2, 1, 0;
- one shared dashed threshold: `N = 3 anchors per bin`;
- separate side pool: `+2 anchors below the frozen log10(M*/M_sun) = 8 floor`, explicitly not a fourth bin.

The existing source bins PNG is insufficient because its y-maximum is below three and it omits the N=3 decision threshold. Panel a of the paper figure is also unsafe for a short video because five metallicity points against the local AM13 curve can visually imply a calibrated high-z relation or deficit that the paper does not license.

### Citations and provenance

The current MP4 renders internal filenames such as `ANCHOR_GAP_PAPER.tex` and `T3_REAL_RESULTS.json`. Those are useful verification paths but are not audience citations.

Display citations should use author/year/journal or the public paper title/URL. Internal paths and hashes remain in `EVIDENCE_FREEZE.json` and QA manifests only.

### Final boundary

The closing non-claim is conceptually correct: this study does not establish whether local diagnostics survive at high redshift, and a null about archive supply is not a statement about galaxies. The proposed final frame strengthens it to:

`ARCHIVE CENSUS — NOT A GALAXY RELATION`

and explicitly excludes a calibrated high-z relation, a deficit verdict, sky absence, and an FMR result.

## Proposal-only iteration receipt

The first proposal-still contact sheet was preserved at `proposals/stills-v1/`. It exposed two presentation defects:

1. pipeline title collision with the proposal badge;
2. mass-bin y-axis overlap and unsupported subscript/solar glyphs.

The second pass at `proposals/stills-v2/` corrects both. Full-resolution inspection found no remaining material clipping or overlap. The four stills are evidence-backed visual proposals only; they are not an official candidate bundle.
