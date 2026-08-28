# Exact current encoded-frame diagnosis — C41 bright-end UVLF

Status: `FAIL_PRESENTATION / PASS_BASIC_ENCODING`

Scope: the exact frozen file `frontend/public/videos/c41-brightend-uvlf-archival-gap.mp4`, SHA-256 `1d84b8755e0baf726c86625baac6335fb9ca91f3356786b5b363976aa26c76d2`.

## Machine facts

- Duration: 83.000 s.
- Video: H.264 High, yuv420p, 1920×1080, 30 fps, DAR 16:9.
- Audio streams: 0.
- Scene cuts detected at 7, 15, 22, 30, 37, 45, 54, 63, and 71 s: 10 static cards total.
- The contact sheet and 10 full-resolution mid-scene frames are under `qa/current/`.
- No scientific figure, axis, table, search-flow diagram, catalogue geometry, or row-level evidence plane is visible in the encoded movie.

## Encoded opening

The opening is a centered title and two-line premise on a dark card. The hierarchy is readable, but the frame does not show the problem. There is no visual contrast between a published luminosity-function point and an archive record, no machine-readable field, no archive query, and no preview of the evidence plane. With no audio and seven seconds of no motion, the opening behaves like a paper cover rather than a scientific hook.

## Encoded archive-search claim

The `92 of 112` card preserves a denominator and states the UCD-only condition, but it only asserts the result. It does not show:

- the 20 name-reachable candidates;
- the 92 UCD-only candidates as a partition of 112;
- the name-pattern channel versus the `phys.magAbs` UCD channel;
- the transition from search reach to scientific eligibility.

The visible citation is the internal filename `T1_CATALOG_MANIFEST.json`, not a scholarly display citation.

## Encoded census and 176/453 claim

The current `176` card does correctly state that `176` is the `M_UV <= -20` subset of `453` rows in `10 <= z < 11.5`. This corrected qualifier is scientifically important. The frame still fails presentation because it shows no magnitude axis, redshift axis, threshold line, points, or slice boundary. It leaves viewers unable to see how the denominator and subset relate.

The evidence-plane proposal fixes this by plotting every one of the 453 frozen `{table, M_UV, z}` rows without jitter or smoothing, then highlighting the 176 rows satisfying `M_UV <= -20`.

## Encoded close

The final card says that every number came from a recorded artifact. That is bounded, but the movie has not shown those artifacts or transformed them into visible evidence. The close is another static card, not a meaningful final state. It also uses the site wordmark in place of an audience-facing source citation.

## Representation defects

1. **Static-card repetition:** all 10 scenes use the same card grammar; only text changes.
2. **No evidence geometry:** no axes, data marks, table cells, flow nodes, provenance overlays, or threshold geometry.
3. **Internal-path citations:** source lines name internal artifact filenames rather than the paper or VizieR archive in audience language.
4. **No encoded narration:** the MP4 contains no audio stream.
5. **Stale lineage:** the current MP4 has 10 cards / 83 s, while the frozen storyboard-of-record contains 16 cards / 99.5 planned seconds and one referenced figure.
6. **Referenced-figure mismatch:** `lit_uvlf_alpha.png` is a literature faint-end-slope-versus-redshift plot. It can provide UVLF context but cannot serve as central evidence for archive search reach, eligibility, the `M_UV=-20` threshold, or the `10 <= z < 11.5` census/published-LF boundary.

## Required visual replacement

Use the actual science artifacts, not decorative cards:

1. progressive name-query versus UCD partition (`20 + 92 = 112`);
2. eligibility partition (`67 + 34 + 1 + 10 = 112`), explicitly separating candidates, counted catalogues, and rows;
3. actual row-level evidence plane for `10 <= z < 11.5`;
4. visible `M_UV=-20` threshold and `176 / 453` subset/denominator;
5. a separate published-LF-roster status plane so that “unpopulated roster” cannot be mistaken for “zero galaxies”;
6. persistent raw-census boundary: no completeness correction, density inference, cosmic-variance interpretation, or cross-catalogue merging.

## Gate conclusion

The exact current MP4 is technically decodable but not publication-quality scientific presentation. It should not be promoted as a future C41 candidate. C41 is a non-canary paper lane and waits behind acceptance of the official `lane-c31-sed/worker-tori` canary. This worker lane prepared source-grounded visual/storyboard proposals only; Hwao remains the sole official candidate/shared-tool/TTS writer.
