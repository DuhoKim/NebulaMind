# Integrator request proposal — spin method-only deck

Owner of writer seat: Hwao/Fable.
Worker Yui action: evidence, visual/storyboard proposal, and QA only.

## Requested disposition

## Pass-31 latest request

Review `PASS31_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS31.json`, `COLOR_MINIMUM_SCALE_REPRESENTED_DIAGONAL_SMEAR_GUARD_PASS31.json`, and `qa/pass31_review_snapshot_v1.json` before any separately authorized integration.

Fresh pass-31 evidence applies native color, linear-light BT.709 grayscale, or each fixed packet-specific Machado severity-100 presentation transform, then Pillow LANCZOS 640×360, then a represented-pixel centered main-diagonal NW-SE width-3 box smear with offsets (−1,−1), (0,0), and (+1,+1), edge replication on both axes, uint64 accumulation, and integer round-half-up division. It reproduces 15/15 candidate cuts, 16/16 native midpoints byte-identical to pass 30, 80/80 candidate and 105/105 method pass-23 baselines pixel-exact, and all 185 diagonal-smear derivatives exactly.

Direct represented-pixel review finds candidate structural held gates at 0/16 and held-critical gates at 0/5 under every variant. Sealed-v8 badges and method/status boundaries, pass-7 exact top gates, and pass-12 exact top gates remain 7/7 in every variant. Anti-diagonal/oblique strokes, diagonal connectors/arrowheads, small glyph joins/counters, fine axes/grids, sloped markers/error-bar caps, legends, caveats, citations, provenance, and qualifiers soften first. The unchanged OCR aid passes only 1/7 in every variant, minimum 0.307692, while direct review confirms 7/7; retain the segmentation undercount and do not alter the inherited threshold.

Requested disposition: adopt the non-pixel diagonal-smear guard only. Do not make a new pixel/copy correction, mutate sealed v8, or create v9. Preserve candidate 0149 as failed evidence. The science blockers remain unchanged, and result integration, TTS, encoding, publication, shared/public writes, and Git actions remain separate approvals.

## Pass-30 latest request

Review `PASS30_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS30.json`, `COLOR_MINIMUM_SCALE_REPRESENTED_RESAMPLING_ROUNDTRIP_GUARD_PASS30.json`, and `qa/pass30_review_snapshot_v1.json` before any separately authorized integration.

Fresh pass-30 evidence applies native color, linear-light BT.709 grayscale, or each fixed packet-specific Machado severity-100 presentation transform, then Pillow LANCZOS 640×360, then represented-pixel Pillow BILINEAR 512×288 and Pillow BILINEAR restoration to 640×360. It reproduces 15/15 candidate cuts, 16/16 native midpoints byte-identical to pass 29, 80/80 candidate and 105/105 method pass-23 baselines pixel-exact, and all 185 resampling-round-trip derivatives exactly.

Direct represented-pixel review finds candidate structural held gates at 0/16 and held-critical gates at 0/5 under every variant. Sealed-v8 badges and method/status boundaries, pass-7 exact top gates, and pass-12 exact top gates remain 7/7 in every variant. One-pixel rules/connectors, small glyph counters and narrow spacing, fine axes/grids/error bars, legends, caveats, citations, provenance, and qualifiers soften first. The unchanged OCR aid passes 4/7–5/7, minimum 0.285714, while direct review confirms 7/7; retain the undercount and do not alter the inherited threshold.

Requested disposition: adopt the non-pixel resampling-round-trip guard only. Do not make a new pixel/copy correction, mutate sealed v8, or create v9. Preserve candidate 0149 as failed evidence. The science blockers remain unchanged, and result integration, TTS, encoding, publication, shared/public writes, and Git actions remain separate approvals.

## Pass-29 latest request

Review `PASS29_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS29.json`, `COLOR_MINIMUM_SCALE_REPRESENTED_VERTICAL_SMEAR_GUARD_PASS29.json`, and `qa/pass29_review_snapshot_v1.json` before any separately authorized integration.

Fresh pass-29 evidence applies native color, linear-light BT.709 grayscale, or each fixed packet-specific Machado severity-100 presentation transform, then Pillow LANCZOS 640×360, then a represented-pixel centered vertical width-3 box smear with edge replication, uint64 accumulation, and integer round-half-up division. It reproduces 15/15 candidate cuts, 16/16 native midpoints byte-identical to pass 28, 80/80 candidate and 105/105 method pass-23 baselines pixel-exact, and all 185 vertical-smear derivatives exactly.

Direct encoded-pixel review finds candidate structural held gates at 0/16 and held-critical gates at 0/5 under every variant. Sealed-v8 badges and method/status boundaries, pass-7 exact top gates, and pass-12 exact top gates remain 7/7 in every variant. Horizontal strokes, separators, grid rules, axes, error-bar caps, small legends, caveats, citations, provenance, and qualifiers soften first. The unchanged OCR aid passes 3/7–4/7, minimum 0.516129, while direct review confirms 7/7; retain the undercount and do not alter the inherited threshold.

Requested disposition: adopt the non-pixel guard only. Do not make a new pixel/copy correction, mutate sealed v8, or create v9. Preserve candidate 0149 as failed evidence. The science blockers remain unchanged, and result integration, TTS, encoding, publication, shared/public writes, and Git actions remain separate approvals.

## Pass-28 latest request

Review `PASS28_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS28.json`, and `COLOR_MINIMUM_SCALE_REPRESENTED_SMEAR_GUARD_PASS28.json` as the latest cumulative guard. Pass 28 freshly reproduced all 16 held-candidate midpoints and tested native color, linear-light BT.709 grayscale, and fixed Machado severity-100 protanopia/deuteranopia/tritanopia presentation transforms followed by LANCZOS 640×360 and a represented-pixel centered horizontal width-3 box smear. Candidate structural held gates remain 0/16 and 0/5 in held-critical scenes across every variant. Preserve the candidate as failed evidence while `video_reportable_now` is false.

Final pass-28 custody is pinned by `qa/pass28_review_snapshot_v1.json`, snapshot ID `spin-worker-yui-pass28-review-v1-20260808T153230K`. Pass 28 changes no science or sealed proof byte. It creates 80 candidate and 105 method static PNG derivatives; pass-23 baselines reproduce 80/80 and 105/105 pixel-exact, and all 185 represented-pixel smear derivatives independently recompute exactly. Sealed v8, pass 7, and pass 12 retain 7/7 directly readable exact gates or major boundaries and 7/7 complete badges under every variant. The inherited OCR aid undercounts some smeared transformed gates at its unchanged 0.80 heuristic (minimum 4/7; minimum score 0.545455), but direct encoded-pixel review confirms 7/7 in every variant. Pass 28 transparently retains that aid miss, adds a non-pixel compound directional/color guard, and requests no pixel/copy change.

## Pass-27 latest request

Review `PASS27_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS27.json`, and `COLOR_MINIMUM_SCALE_REPRESENTED_DEFOCUS_GUARD_PASS27.json` as the latest cumulative guard. Pass 27 freshly reproduced all 16 held-candidate midpoints and tested native color, linear-light BT.709 grayscale, and fixed Machado severity-100 protanopia/deuteranopia/tritanopia presentation transforms followed by LANCZOS 640×360 and represented-pixel Pillow Gaussian radius 0.5. Candidate structural held gates remain 0/16 and 0/5 in held-critical scenes across every variant. Preserve the candidate as failed evidence while `video_reportable_now` is false.

Final pass-27 custody is pinned by `qa/pass27_review_snapshot_v1.json`, snapshot ID `spin-worker-yui-pass27-review-v1-20260808T151015K`. Pass 27 changes no science or sealed proof byte. It creates 80 candidate and 105 method static PNG derivatives; pass-23 baselines reproduce 80/80 and 105/105 pixel-exact, and all 185 represented-pixel blur derivatives independently recompute exactly. Sealed v8, pass 7, and pass 12 retain 7/7 directly readable exact gates or major boundaries and 7/7 complete badges under every variant. Pass-12 mapped gate similarity remains 0.972100–0.987949 with 7/7 above threshold for every variant. Pass 27 adds a non-pixel compound sharpness/color guard and requests no pixel/copy change.

## Pass-26 latest request

Review `PASS26_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS26.json`, and `COLOR_MINIMUM_SCALE_OBSTRUCTION_GUARD_PASS26.json` as the latest cumulative guard. Pass 26 freshly reproduced all 16 held-candidate midpoints and tested native color, linear-light BT.709 grayscale, and fixed Machado severity-100 protanopia/deuteranopia/tritanopia presentation transforms followed by LANCZOS 640×360 and opaque RGB black bottom-quarter obstruction. Candidate structural held gates remain 0/16 and 0/5 in held-critical scenes across all variants. Preserve the candidate as failed evidence while `video_reportable_now` is false.

Final pass-26 custody is pinned by `qa/pass26_review_snapshot_v1.json`, snapshot ID `spin-worker-yui-pass26-review-v1-20260808T144908K`. Pass 26 changes no science or sealed proof byte. It creates 80 candidate and 105 method static PNG derivatives; pass-23 baselines reproduce 80/80 and 105/105 pixel-exact, and all 185 obstruction derivatives independently prove rows 0..269 unchanged and rows 270..359 opaque black. Sealed v8 retains 7/7 badges and major status hierarchy but loses scene-specific lower boundaries S2–S6. The existing pass-7 and pass-12 corrections retain 7/7 directly readable exact top gates and badges under every variant; mapped gate similarity is 1.000000. Pass 26 therefore confirms the existing top-gate correction, adds a non-pixel compound color/minimum-scale/obstruction guard, and requests no new pixel/copy change.

## Pass-25 latest request

Review `PASS25_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS25.json`, and `COLOR_MINIMUM_SCALE_BLACK_LIFT_GUARD_PASS25.json` as the latest cumulative guard. Pass 25 freshly reproduced all 16 held-candidate midpoints and tested native color, linear-light BT.709 grayscale, and fixed Machado severity-100 protanopia/deuteranopia/tritanopia presentation transforms followed by LANCZOS 640×360 and represented-pixel linear-light black lift20. Candidate structural held gates remain 0/16 and 0/5 in held-critical scenes across all variants. Preserve the candidate as failed evidence while `video_reportable_now` is false.

Final pass-25 custody is pinned by `qa/pass25_review_snapshot_v1.json`, snapshot ID `spin-worker-yui-pass25-review-v1-20260808T142621K`. Pass 25 changes no science or sealed proof byte. It creates 80 candidate and 105 method static PNG derivatives; pass-23 baselines reproduce 80/80 and 105/105 pixel-exact, and all 185 black-lift derivatives independently recompute exactly. Sealed v8 retains 7/7 badges and status boundaries; pass 7 and pass 12 retain 7/7 directly readable exact gates and badges. Mapped gate similarity is 1.000000 with 7/7 above threshold for every variant. Pass 25 adds a non-pixel compound contrast/color guard and requests no pixel/copy change.

Review `PASS24_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS24.json`, and `COLOR_MINIMUM_SCALE_RECOMPRESSION_GUARD_PASS24.json` as the latest cumulative guard. Pass 24 freshly reproduced all 16 held-candidate midpoints and tested native color, linear-light BT.709 grayscale, and fixed Machado severity-100 protanopia/deuteranopia/tritanopia presentation transforms followed by LANCZOS 640×360 and Pillow JPEG q60 4:2:0 decode. Candidate structural held gates remain 0/16 and 0/5 in held-critical scenes across all five variants. Preserve the candidate as failed evidence; do not use it as an integration base while `video_reportable_now` is false.

Final pass-24 custody and exact decision rule are pinned by `qa/pass24_review_snapshot_v1.json`, snapshot ID `spin-worker-yui-pass24-review-v1-20260808T140417K`. Pass 24 changes no science, sealed-v8 byte, pass-7 proof byte, or pass-12 proof byte. It creates 80 candidate and 105 method JPEG streams plus decoded PNGs; candidate pass-23 baselines reproduce 80/80 pixel-exact and method baselines 105/105. Exact JPEG bytes and decoded RGB pixels reproduce for every scene/variant. Sealed v8 retains 7/7 badges and status boundaries; pass 7 and pass 12 retain 7/7 directly readable exact gates and badges under every variant. Pass-12 tritanopia scene 2 has a disclosed OCR-aid score of 0.729730, but direct review confirms the exact gate and complete container remain readable. Pass 24 adds a non-pixel compound recompression guard and requests no pixel/copy change.

Review `PASS23_ENCODED_FRAME_AUDIT.md`, `BLOCKER_PACKET_PASS23.json`, and `MINIMUM_SCALE_COLOR_REDUNDANCY_GUARD_PASS23.json` as the latest cumulative guard. Pass 23 freshly reproduced all 16 held-candidate midpoints and tested native linear-light BT.709 grayscale plus fixed Machado severity-100 protanopia, deuteranopia, and tritanopia presentation transforms followed by full-canvas LANCZOS downscale to 640×360. Grayscale candidate headline/full/lower-support/numeric recall versus the full-color 360p reference is 0.988533/0.930353/0.732388/0.828125; structural held gates remain 0/16 across all five represented variants and 0/5 in held-critical scenes. Large result headlines, numbers, plots, bars, matrices, and conclusions remain primary. Preserve the candidate as failed evidence; do not use it as an integration base or promote result content while `video_reportable_now` is false.

Final pass-23 custody is pinned by `qa/pass23_review_snapshot_v1.json`, snapshot ID `spin-worker-yui-pass23-review-v1-20260808T133615K`. Pass 23 changes no science, sealed-v8 byte, pass-7 proof byte, or pass-12 proof byte. Across the full-color reference, grayscale, protanopia, deuteranopia, and tritanopia represented variants, sealed v8 keeps 7/7 generic held badges and 7/7 major method/status boundaries. Pass 7 and pass 12 preserve 7/7 exact top gates and 7/7 badges under every variant. Pass-12 mapped-crop similarity is 1.000000 with 7/7 above threshold in every variant, exact transform recomputation is 7/7 per variant, and no required method meaning is hue-only. Pass 23 adds the compound minimum-scale color-redundancy integration guard and requests no pixel or copy change. The transforms are reproducible presentation stresses, not clinical diagnostics.

Review sealed v8 with `CAPTION_SAFE_STORYBOARD_CORRECTION_PASS7.json`, `REDUNDANT_ENCODING_GUARD_PASS8.json`, `TITLE_SAFE_STORYBOARD_CORRECTION_PASS9.json`, `AMBIENT_CONTRAST_GUARD_PASS10.json`, `RECOMPRESSION_RESILIENCE_GUARD_PASS11.json`, `SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json`, `DIRECTIONAL_SMEAR_GUARD_PASS13.json`, `DARK_TONE_RESILIENCE_GUARD_PASS14.json`, `GEOMETRY_RESILIENCE_GUARD_PASS15.json`, `MINIMUM_SCALE_GEOMETRY_GUARD_PASS16.json`, `MINIMUM_SCALE_RECOMPRESSION_GUARD_PASS17.json`, `MINIMUM_SCALE_OBSTRUCTION_GUARD_PASS18.json`, `MINIMUM_SCALE_BLACK_LIFT_GUARD_PASS19.json`, `MINIMUM_SCALE_DEFOCUS_GUARD_PASS20.json`, `MINIMUM_SCALE_DIRECTIONAL_SMEAR_GUARD_PASS21.json`, and `MINIMUM_SCALE_DARK_TONE_GUARD_PASS22.json` as bounded, cumulative corrections and guards. Pass 22 freshly reproduced all 16 held-candidate midpoints and tested native integer-luma-preserving dark-tone floor16 followed by full-canvas LANCZOS downscale to 640×360. At the operational transform, candidate headline/full/lower-support/numeric recall is 0.894444/0.635932/0.256180/0.288889, held-critical full-text recall is 0.352031, and no held gate appears. Bright result headlines, numbers, plots, bars, matrices, and conclusions remain primary while dark grids, axes, error bars, dividers, caveats, citations, provenance, and lower support weaken first. Preserve the candidate as failed evidence; do not use it as an integration base or promote result content while `video_reportable_now` is false.

Final pass-22 custody is pinned by `qa/pass22_review_snapshot_v1.json`, snapshot ID `spin-worker-yui-pass22-review-v1-20260808T130921K`. The pass-5 exact all-209-file blocker proof remains binding. Pass 22 changes no science, sealed-v8 byte, pass-7 proof byte, or pass-12 proof byte. Under native floor16 followed by 640×360 downscale, sealed v8 keeps 7/7 generic held badges and 7/7 major method/status boundaries. The pass-7 and pass-12 proofs preserve 7/7 directly readable exact top gates and 7/7 badges. Pass-12 mean mapped-crop similarity is 0.967458 with 7/7 above the disclosed 0.80 threshold, 7/7 exact transform recomputation, and no overlap, clipping, or ambiguity. Floors 32 and 48 followed by 360p also score 7/7 in characterization, but their higher non-monotonic OCR scores do not prove semantic repair or make dark fine support acceptance-reliable. Pass 22 adds the compound native-dark-tone/minimum-scale integration guard and requests no further pixel or copy change.

## Exact requested implementation

1. Use seven graphics-first beats: method question, overlapping sample readouts, predeclared equation, archive-frame convention, bounded column-mapping probe, bias-control matrix, and full-screen status boundary.
2. Keep `RESULT HELD` persistent. Do not use a result number, result plot, character close, or URL in this diagnostic deck.
3. Keep audience citations human-readable; place absolute verification paths and hashes in the receipt only.
4. Preserve `ALTERNATIVE READOUTS · COUNTS OVERLAP · DO NOT SUM`, the subset relationship, unquantified release-flag overlap, and one A estimate per readout.
5. Preserve `CONCEPTUAL — convention map, not data`, `POSSIBILITIES SHOWN WITHOUT PROBABILITY`, and dominant `FRAME UNSTATED` on the storage-convention scene.
6. Preserve the bounded 36-object column-mapping language, code definitions, and `SCHEMATIC · 6 EXAMPLE ROWS OF 36`.
7. Preserve `PAIRED BY OBJECT ID`, the monochrome/mirror comparison questions, and `OUTCOMES WITHHELD` on the controls scene.
8. Preserve the final KNOWN / UNRESOLVED / NOT CLAIMED matrix and separate-authorization gate after both blockers resolve.
9. Do not reuse held candidate scenes 7, 9, 10, or 11. They are result-bearing encoded figures, not method graphics, and their small disclaimers do not repair their dominant assertions.
10. Use clean hard cuts between the seven v8 scenes. Keep the complete outgoing frame through its last frame, show the complete incoming frame at the cut, and keep `RESULT HELD` visible on both sides. Do not crossfade, wipe, zoom, morph, or insert blank/badge-free transition frames.
11. Treat 360p as a required representation-boundary acceptance test. Every semantic hold must remain headline-scale or use the persistent high-contrast `RESULT HELD` capsule; never rely on footer, citation, provenance, caveat, or small-axis copy to carry the gate. Require human visual review of all seven downscaled scenes because OCR misses scenes 1 and 5 at every scale despite visible badges.
12. Treat the bottom 25% as an obstruction zone. Keep the generic `RESULT HELD` capsule and place one scene-specific semantic gate line fully above that zone: S1 result locked plus both requirements; S2 overlapping readouts/do not sum; S3 label-frame interpretation held; S4 frame unstated; S5 column-check-only/storage-frame unresolved; S6 control-design-only/outcomes withheld; S7 separate authorization after both blockers resolve. Require clean, caption-15%, player-UI-25%, and 360p human review.
13. Carry no method, scope, availability, unresolved state, or authorization meaning by hue alone. Pair every branch, condition, column, rail, marker, and status with a direct label and distinct shape, line style, marker, or stable position. Keep unavailable rails both explicitly labelled and visibly blocked/dashed. Require color, linear-light grayscale, protanopia, deuteranopia, and tritanopia full-sheet review; words and border, not amber hue, must carry held gates.
14. Place every complete semantic or audience-readable element inside the inner 5% rectangle at 1920×1080: x=96..1824 and y=54..1026. This includes the full header, complete `RESULT HELD` capsule, scene-specific gate line, headlines, diagram/card borders, labels, status columns, and audience citations. The outer band is decorative-only. Specifically protect the S1 first pipeline node, S5 left source-column card, and S7 first status card/headline. Rerun symmetric 3%, symmetric/horizontal/vertical 5%, color/monochrome, obstruction, and 360p review.
15. Treat 20% uniform linear-light black lift as the operational contrast floor. Require 7/7 complete `RESULT HELD` capsules and 7/7 scene-specific gate lines to remain visually readable, with the specific lines also OCR-detectable. Do not carry any scientific qualifier, unresolved boundary, unavailable rung, or interpretation limit only in low-contrast footer, citation, axis, or tiny body copy. Treat 30% and 40% as hierarchy characterization only, not assumed viewing environments or mandatory thresholds. Rerun contrast together with title-safe, obstruction, color/monochrome, and 360p review.
16. Treat the exact Pillow JPEG q60 4:2:0 recompression/decode transform as a packet-specific operational floor. Require 7/7 complete `RESULT HELD` capsules and 7/7 scene-specific gate lines to remain visually readable, with the specific lines OCR-detectable. Do not carry a scientific boundary only in fine chroma detail, a one-pixel line, a tiny axis, citation, or footer. Treat q35 and q20 as characterization only, not named-platform or universal delivery requirements. Rerun recompression together with contrast, title-safe, obstruction, color/monochrome, and 360p review.
17. Treat exact Pillow Gaussian defocus radius 1.5 pixels at 1920×1080 as a packet-specific operational floor. Keep the exact seven pass-7 gate sentences, but strengthen their presentation in a complete title-safe box: the QA proof uses x=102..1540, y=78..121, 28-pixel bold type, one-pixel same-color text stroke, and a three-pixel border. Require 7/7 exact scene-gate lines and 7/7 complete `RESULT HELD` capsules, no overlap with header/badge/headline, and no scientific boundary carried only by small body copy, footer, citation, fine line, or low-sharpness detail. Treat radius 2.5 and 4.0 as characterization only. Rerun defocus with recompression, contrast, title-safe crop, obstruction, color/monochrome, and 360p review.
18. Treat exact centered horizontal width-7 box smear with edge replication, unsigned 64-bit sums, and integer round-half-up division at 1920×1080 as a packet-specific operational floor. Require 7/7 exact strengthened scene-gate lines, 7/7 complete `RESULT HELD` capsules, and separated header/gate/badge/headline/diagram layers. Pair arrows, borders, connectors, rails, and status columns with direct labels and stable geometry. Do not carry any required distinction or scientific boundary only through a thin vertical edge, one-pixel separator, fine axis, small label, citation, provenance footer, narrow glyph spacing, or other low-horizontal-sharpness detail. Keep widths 13 and 21 as characterization only. Rerun directional smear with defocus, recompression, contrast, title-safe crop, obstruction, color/monochrome, and 360p review.
19. Treat the exact integer-luma-preserving floor-16 dark-tone transform and full-range remap at 1920×1080 as a packet-specific operational floor. Require 7/7 exact strengthened gates, 7/7 complete `RESULT HELD` capsules, and separated header/gate/badge/headline/diagram layers. Carry no required scientific qualifier, unresolved boundary, unavailable rung, interpretation limit, branch distinction, axis, error bar, or provenance fact only through source-luma code values at or below 16, dark fill, low-luminance texture, grid, or divider. Pair required text with a surviving bright border, connector, capsule, or stable geometry channel. Keep floors 32 and 48 as characterization only. Rerun dark-tone review with directional smear, defocus, recompression, black lift, title-safe crop, obstruction, color/monochrome, and 360p review.
20. Treat centered anisotropic Pillow LANCZOS x90 and y90 resampling with black padding on the unchanged 1920×1080 canvas as a packet-specific operational pair. Require 7/7 exact strengthened gates, 7/7 complete `RESULT HELD` capsules, and separated header/gate/badge/headline/diagram layers under both transforms. Retain direct labels for branches, arrows, connectors, rails, status columns, equation terms, axes, units, values, error bars, and thresholds. Carry no required comparison, interpretation, ordering, uncertainty, branch distinction, or status boundary only through apparent slope, angle, circle/spiral aspect, bar width/length, area, spacing, proximity, line thickness, or geometric ratio. Keep x80 and y80 as characterization only. Rerun geometry with dark-tone, smear, defocus, recompression, black lift, title-safe crop, obstruction, color/monochrome, and 360p review.
21. Treat centered native x90 and y90 anisotropic Pillow LANCZOS resampling with black padding followed by full-canvas Pillow LANCZOS downscale to 640×360 as a packet-specific compound operational pair. Require 7/7 exact strengthened gates, 7/7 complete `RESULT HELD` capsules, and direct readable labels for every required axis, unit, value, error bar, threshold, branch, equation term, interpretation, uncertainty, and result-status boundary. Carry no required meaning only through tiny fine print, citation, provenance, geometry, color, or global full-frame OCR. Use exact mapped gate crops plus human review of represented output pixels. Keep x80_360p and y80_360p as characterization only. Rerun the compound pair separately from the native geometry, dark-tone, smear, defocus, recompression, black-lift, title-safe, obstruction, color/monochrome, and standalone 360p gates.
22. Treat Pillow JPEG q60 4:2:0 recompression/decode after full-canvas Pillow LANCZOS downscale to 640×360 as a packet-specific compound operational transform. Require 7/7 exact strengthened gates, 7/7 complete `RESULT HELD` capsules, and direct readable labels for every required axis, unit, value, error bar, threshold, branch, equation term, interpretation, uncertainty, and result-status boundary. Carry no required meaning only through fine chroma detail, one-pixel lines, tiny axes, small error bars, citations, provenance footers, low-contrast caveats, or global full-frame OCR. Use exact mapped gate crops plus human review of represented output pixels. Keep q35 and q20 as characterization only. Rerun this interaction separately from native q60 recompression, compound geometry, native geometry, dark-tone, smear, defocus, black-lift, title-safe, obstruction, color/monochrome, and standalone 360p gates.
23. Treat opaque bottom-15-percent and bottom-25-percent obstruction after full-canvas Pillow LANCZOS downscale to 640×360 as packet-specific compound operational transforms. Require 7/7 exact scene-specific top gates and 7/7 complete `RESULT HELD` capsules fully above the bottom quarter. A generic held badge alone is not a complete scope boundary. Carry no required qualifier, uncertainty, branch distinction, axis, unit, value, error bar, threshold, equation term, provenance fact, or interpretation limit only in the lower quarter. Prove all pixels above the mask remain byte-identical to the 360p reference, and use mapped gate crops plus human represented-pixel review. Keep bottom 35 percent as characterization only. Rerun this interaction separately from minimum-scale recompression, compound geometry, native geometry, dark-tone, smear, defocus, black-lift, title-safe, standalone obstruction, color/monochrome, and standalone 360p gates.
24. Treat represented-pixel 20% linear-light black lift after full-canvas Pillow LANCZOS downscale to 640×360 as a packet-specific compound operational transform. Require 7/7 exact scene-specific gates, 7/7 complete `RESULT HELD` capsules, and direct high-contrast labels plus complete shapes, borders, connectors, or stable geometry for every required status, qualifier, uncertainty, branch, axis, unit, value, error bar, threshold, equation term, interpretation limit, and provenance fact. Carry no required meaning only in dark fill, a low-contrast footer, tiny axis, one-pixel line, subtle grid, citation, provenance footer, or global OCR. Independently recompute the exact float64 linear-light transform from the lossless 360p baseline and use mapped gate crops plus represented-pixel human review. Keep 30% and 40% black lift as characterization only. Rerun this interaction separately from native black lift, minimum-scale obstruction, minimum-scale recompression, compound geometry, native geometry, dark-tone, smear, defocus, title-safe, standalone obstruction, color/monochrome, and standalone 360p gates.
25. Treat native-canvas Pillow Gaussian defocus radius 1.5 followed by full-canvas Pillow LANCZOS downscale to 640×360 as a packet-specific compound operational transform. Require 7/7 exact scene-specific gates, 7/7 complete `RESULT HELD` capsules, and direct high-contrast labels plus complete shapes, borders, connectors, or stable geometry for every required status, qualifier, uncertainty, branch, axis, unit, value, error bar, threshold, equation term, interpretation limit, and provenance fact. Carry no required meaning only in blur-fragile fine print, tiny axes or error bars, one-pixel lines, narrow glyph spacing, citations, provenance footers, low-contrast caveats, or global OCR. Independently recompute the exact compound transform from each native source and use mapped gate crops plus represented-pixel human review. Keep native radii 2.5 and 4.0 followed by 360p as characterization only. Rerun this interaction separately from standalone native defocus, minimum-scale black lift, minimum-scale obstruction, minimum-scale recompression, compound geometry, native geometry, dark-tone, smear, title-safe, standalone obstruction, color/monochrome, and standalone 360p gates.
26. Treat native centered horizontal width-7 box smear with edge replication, unsigned 64-bit channel sums, and integer round-half-up division followed by full-canvas Pillow LANCZOS downscale to 640×360 as a packet-specific compound operational transform. Require 7/7 directly readable exact scene-specific gates, 7/7 complete `RESULT HELD` capsules, and direct high-contrast labels plus complete shapes, borders, connectors, or stable geometry for every required status, qualifier, uncertainty, branch, axis, unit, value, error bar, threshold, equation term, interpretation limit, and provenance fact. Carry no required meaning only in thin vertical strokes, tiny axes or error bars, one-pixel connectors, narrow glyph spacing, fine legends, citations, provenance footers, low-contrast caveats, or global OCR. Independently recompute the exact compound transform from each native source and use mapped gate crops plus represented-pixel human review. Disclose mapped-crop OCR misses rather than treating the aid as a semantic oracle. Keep native widths 13 and 21 followed by 360p as characterization only. Rerun this interaction separately from standalone native smear, minimum-scale defocus, minimum-scale black lift, minimum-scale obstruction, minimum-scale recompression, compound geometry, native geometry, dark-tone, title-safe, standalone obstruction, color/monochrome, and standalone 360p gates.
27. Treat native integer-luma-preserving dark-tone floor16/full-range remap followed by full-canvas Pillow LANCZOS downscale to 640×360 as a packet-specific compound operational transform. Require 7/7 directly readable exact scene-specific gates, 7/7 complete `RESULT HELD` capsules, and direct high-contrast labels plus complete borders, capsules, connectors, markers, rails, status columns, or stable geometry for every required status, qualifier, uncertainty, branch, axis, unit, value, error bar, threshold, equation term, interpretation limit, and provenance fact. Carry no required meaning only at source-luma values at or below code value 16, in dark texture, subtle grids, fine axes/error bars, one-pixel dividers/connectors, low-contrast caveats, citations, provenance footers, or global OCR. Independently recompute the exact compound transform from each native source and use mapped gate crops plus represented-pixel human review. Keep floors 32 and 48 followed by 360p as characterization only; non-monotonic OCR is not semantic repair. Rerun this interaction separately from standalone native floor16, minimum-scale smear, minimum-scale defocus, minimum-scale black lift, minimum-scale obstruction, minimum-scale recompression, compound geometry, native geometry, title-safe, standalone obstruction, color/monochrome, and standalone 360p gates.
28. Treat native linear-light BT.709 grayscale and the fixed packet-specific Machado severity-100 protanopia, deuteranopia, and tritanopia presentation transforms followed by full-canvas Pillow LANCZOS downscale to 640×360 as a compound operational suite. Require 7/7 directly readable exact scene-specific gates, 7/7 complete `RESULT HELD` capsules, and a direct label plus at least one non-color shape, line style, marker, border, connector, stable position, pattern, or status-column channel for every required status, branch, comparison, equation term, axis, unit, value, error bar, threshold, unavailable rung, uncertainty, qualifier, provenance fact, and interpretation boundary. Hue may reinforce meaning but may not solely carry scientific category, sign, direction, threshold crossing, availability, unresolved state, result status, or authorization. Independently recompute each exact compound transform from its native source and use mapped gate crops plus represented-pixel human review. Treat the matrices as presentation stresses, not clinical diagnostics. Rerun this interaction separately from standalone color/monochrome, minimum-scale dark tone, smear, defocus, black lift, obstruction, recompression, compound geometry, native geometry, title-safe, standalone obstruction, and standalone 360p gates.
29. Treat native color or linear-light BT.709 grayscale / fixed Machado severity-100 protanopia, deuteranopia, or tritanopia presentation transformation followed by full-canvas Pillow LANCZOS 640×360 and Pillow JPEG q60 4:2:0 decode as a packet-specific compound operational suite. Require 7/7 directly readable exact gates, 7/7 complete badges, and direct labels plus compression-resilient non-color geometry for every required status and scientific distinction. Do not carry required meaning solely through hue, fine chroma edges, tiny axes/error bars, legends, caveats, citations, provenance, one-pixel rules, or global OCR. Independently recompute exact JPEG bytes and decoded RGB pixels from each matching verified 360p baseline. Disclose OCR-aid misses, but use direct represented-pixel review to decide readability. Treat matrices and q60 as reproducible packet stresses, not clinical diagnostics or universal delivery requirements.
30. Treat native color or linear-light BT.709 grayscale / fixed Machado severity-100 protanopia, deuteranopia, or tritanopia transformation followed by full-canvas Pillow LANCZOS 640×360 and represented-pixel float64 linear-light black lift20 as a packet-specific compound operational suite. Require 7/7 directly readable exact gates, 7/7 complete badges, and direct labels plus complete non-color geometry for every required status and scientific distinction. Do not carry required meaning solely through hue, dark fill, subtle texture, low-contrast support, tiny axes/error bars/legends/thresholds, one-pixel rules/connectors, caveats, citations, provenance footers, or global OCR. Independently recompute every baseline and black-lift derivative from pinned native sources and use represented-pixel human review. Treat matrices and black lift as reproducible presentation stresses, not clinical diagnostics or universal viewing requirements.
31. Treat native color or linear-light BT.709 grayscale / fixed Machado severity-100 protanopia, deuteranopia, or tritanopia transformation followed by full-canvas Pillow LANCZOS 640×360 and opaque RGB black bottom-quarter obstruction as a packet-specific compound operational suite. Require 7/7 exact scene-specific gates and 7/7 complete badges entirely above row 270, with direct labels plus complete non-color geometry. Carry no required qualifier, uncertainty, branch distinction, axis, unit, value, error bar, threshold, equation term, provenance fact, interpretation limit, or release boundary only in the lower quarter. Independently prove rows 0..269 byte-identical to the matching represented baseline and rows 270..359 exactly RGB black. Use mapped gate crops plus represented-pixel human review; the matrices and mask are presentation stresses, not clinical diagnostics or named caption/player behavior.
32. Treat native color or linear-light BT.709 grayscale / fixed Machado severity-100 protanopia, deuteranopia, or tritanopia transformation followed by full-canvas Pillow LANCZOS 640×360 and represented-pixel Pillow GaussianBlur radius 0.5 as a packet-specific compound operational suite. Require 7/7 directly readable exact scene-specific gates, 7/7 complete badges, direct labels, and complete non-color geometry. Carry no required status, qualifier, uncertainty, branch, equation term, axis, unit, value, error bar, threshold, unavailable rung, provenance fact, or interpretation boundary only through hue, blur-fragile fine print, tiny axes/error bars, one-pixel lines/connectors, narrow glyph spacing, fine legends, caveats, citations, provenance footers, subtle texture, or global OCR. Independently reproduce all 185 derivatives from pinned native sources and use represented-pixel human review. Radius 0.5 is an operational packet stress at 640×360, not a translated native-radius claim or named viewing standard.
33. Treat native color or linear-light BT.709 grayscale / fixed Machado severity-100 protanopia, deuteranopia, or tritanopia transformation followed by full-canvas Pillow LANCZOS 640×360, represented-pixel Pillow BILINEAR 512×288, and Pillow BILINEAR restoration to 640×360 as a packet-specific compound operational suite. Require 7/7 directly readable exact scene-specific gates, 7/7 complete badges, GALAXY SPIN headers, direct labels, and complete non-color geometry. Carry no required meaning only through hue, one-pixel rules/dividers/connectors, small glyph counters or narrow spacing, fine axes/grids/error bars, small units/legends, caveats, citations, provenance footers, low-contrast support, or global OCR. Independently reproduce all 185 derivatives from pinned native sources and use represented-pixel human review. The resampling round trip is a packet stress, not a named scaling, display, or delivery standard.
34. Treat native color or linear-light BT.709 grayscale / fixed Machado severity-100 protanopia, deuteranopia, or tritanopia transformation followed by full-canvas Pillow LANCZOS 640×360 and represented-pixel centered main-diagonal NW-SE width-3 box smear as a packet-specific compound operational suite. Use exact offsets (−1,−1), (0,0), and (+1,+1), edge replication on both axes, uint64 accumulation, and integer round-half-up division. Require 7/7 directly readable exact gates, 7/7 complete badges, GALAXY SPIN headers, direct labels, and complete non-color geometry. Carry no required meaning solely through hue, anti-diagonal/oblique strokes, diagonal connectors/arrowheads, small glyph joins/counters, fine axes/grids/sloped markers/error-bar caps, one-pixel geometry, legends, caveats, citations, provenance, low-contrast support, or global OCR. Independently reproduce all 185 derivatives and use represented-pixel human review. Disclose the 1/7 OCR-aid result without lowering its threshold or inventing a semantic defect.

## Shared-tool capabilities this proposal may require

If Hwao chooses to integrate, the shared renderer needs only bounded diagram primitives; no paper-specific global redesign is requested:

- rounded labelled nodes and connectors;
- equal-weight branch arrows;
- equation card;
- compact connector matrix;
- condition-by-rung matrix with an unavailable rail;
- persistent status badge;
- caption-safe scene-specific gate line above the bottom quarter;
- direct labels plus non-color shape/line/marker redundancy;
- explicit line-style, marker-shape, border, connector, stable-position, pattern, and status-column channels that survive grayscale and all fixed packet color-vision transforms at 360p;
- exact title-safe insets for complete header, badge, gate, card, and citation containers;
- operational 20% uniform-black-lift contrast acceptance for complete badges, scene-specific gates, diagram labels, and scientific qualifiers;
- packet-specific Pillow JPEG q60 4:2:0 recompression acceptance for complete badges, gates, direct labels, borders, arrows, and status columns;
- packet-specific Gaussian defocus radius-1.5 acceptance for complete badges, exact strengthened title-safe gates, direct labels, borders, arrows, and status columns;
- packet-specific centered horizontal width-7 box-smear acceptance for complete badges, exact strengthened gates, direct labels, connectors, borders, arrows, rails, and status columns;
- packet-specific integer-luma floor-16 dark-tone acceptance for complete badges, exact strengthened gates, direct labels, bright borders, connectors, rails, status columns, qualifiers, and interpretation limits;
- packet-specific centered anisotropic x90/y90 acceptance for complete badges, exact strengthened gates, direct labels, branches, arrows, axes, values, error bars, thresholds, and geometry-independent meaning;
- packet-specific centered x90_360p/y90_360p compound acceptance for complete badges, exact strengthened gates, direct 360p-readable status/axis/value/error/threshold labels, and exact-crop plus represented-pixel human review;
- packet-specific q60 4:2:0-after-640x360 compound acceptance for complete badges, exact strengthened gates, direct represented-pixel status/axis/value/error/threshold labels, and exact-crop plus human review;
- packet-specific bottom-15-percent and bottom-25-percent obstruction-after-640x360 compound acceptance for complete badges, exact top gates, lower-quarter-independent scientific/status meaning, upper-pixel identity, and represented-pixel human review;
- packet-specific 20-percent linear-light-black-lift-after-640x360 compound acceptance for complete badges, exact gates, direct high-contrast labels plus complete geometry channels, exact transform recomputation, and represented-pixel human review;
- packet-specific native-Gaussian-radius-1.5-then-640x360 compound acceptance for complete badges, exact gates, blur-resilient direct labels plus complete geometry channels, exact transform recomputation, and represented-pixel human review;
- packet-specific native-horizontal-width-7-smear-then-640x360 compound acceptance for complete badges, directly readable exact gates, directionally resilient direct labels plus complete geometry channels, exact transform recomputation, disclosed mapped-crop OCR aid results, and represented-pixel human review;
- packet-specific native-dark-tone-floor16-then-640x360 compound acceptance for complete badges, exact gates, direct high-contrast labels plus complete borders/connectors/rails/status geometry, exact transform recomputation, non-monotonic-OCR disclosure, and represented-pixel human review;
- audience citation field separate from receipt verification paths.

Worker Yui did not edit shared tools. `render_proposal_frames.py` is a lane-local static mock renderer and is not a candidate encoder.

## Audio request

None at this gate. Worker Yui did not invoke TTS. If Hwao later approves an integrated storyboard after semantic/visual review, the recorded route is Alloy through Nous at speed 1.18, invoked only by Hwao.

## Evidence

- `PASS22_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS22.json`
- `MINIMUM_SCALE_DARK_TONE_GUARD_PASS22.json`
- `qa/extract_pass22_minimum_scale_dark_tone_frames.py`
- `qa/pass22_minimum_scale_dark_tone_audit/extraction_receipt.json`
- `qa/pass22_minimum_scale_dark_tone_audit/contact_sheet_floor16_then_360p.png`
- `qa/pass22_minimum_scale_dark_tone_audit/contact_sheet_floor48_then_360p.png`
- `qa/pass22_minimum_scale_dark_tone_quantitative_audit.json`
- `qa/pass22_v8_minimum_scale_dark_tone/receipt.json`
- `qa/pass22_review_snapshot_v1.json`
- `qa/verify_pass22_packet.py`

- `PASS21_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS21.json`
- `MINIMUM_SCALE_DIRECTIONAL_SMEAR_GUARD_PASS21.json`
- `qa/extract_pass21_minimum_scale_directional_smear_frames.py`
- `qa/pass21_minimum_scale_directional_smear_audit/extraction_receipt.json`
- `qa/pass21_minimum_scale_directional_smear_audit/contact_sheet_smear_w07_then_360p.png`
- `qa/pass21_minimum_scale_directional_smear_audit/contact_sheet_smear_w21_then_360p.png`
- `qa/pass21_minimum_scale_directional_smear_quantitative_audit.json`
- `qa/pass21_v8_minimum_scale_directional_smear/receipt.json`
- `qa/pass21_review_snapshot_v1.json`
- `qa/verify_pass21_packet.py`

- `PASS20_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS20.json`
- `MINIMUM_SCALE_DEFOCUS_GUARD_PASS20.json`
- `qa/extract_pass20_minimum_scale_defocus_frames.py`
- `qa/pass20_minimum_scale_defocus_audit/extraction_receipt.json`
- `qa/pass20_minimum_scale_defocus_audit/contact_sheet_defocus_r1_50_then_360p.png`
- `qa/pass20_minimum_scale_defocus_audit/contact_sheet_defocus_r4_00_then_360p.png`
- `qa/pass20_minimum_scale_defocus_quantitative_audit.json`
- `qa/pass20_v8_minimum_scale_defocus/receipt.json`
- `qa/pass20_review_snapshot_v1.json`
- `qa/verify_pass20_packet.py`

- `PASS19_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS19.json`
- `MINIMUM_SCALE_BLACK_LIFT_GUARD_PASS19.json`
- `qa/extract_pass19_minimum_scale_black_lift_frames.py`
- `qa/pass19_minimum_scale_black_lift_audit/extraction_receipt.json`
- `qa/pass19_minimum_scale_black_lift_audit/contact_sheet_black_lift20_360p.png`
- `qa/pass19_minimum_scale_black_lift_audit/contact_sheet_black_lift40_360p.png`
- `qa/pass19_minimum_scale_black_lift_quantitative_audit.json`
- `qa/pass19_v8_minimum_scale_black_lift/receipt.json`
- `qa/pass19_review_snapshot_v1.json`
- `qa/verify_pass19_packet.py`

- `PASS18_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS18.json`
- `MINIMUM_SCALE_OBSTRUCTION_GUARD_PASS18.json`
- `qa/extract_pass18_minimum_scale_obstruction_frames.py`
- `qa/pass18_minimum_scale_obstruction_audit/extraction_receipt.json`
- `qa/pass18_minimum_scale_obstruction_audit/contact_sheet_player_ui25_360p.png`
- `qa/pass18_minimum_scale_obstruction_audit/contact_sheet_heavy35_360p.png`
- `qa/pass18_minimum_scale_obstruction_quantitative_audit.json`
- `qa/pass18_v8_minimum_scale_obstruction/receipt.json`
- `qa/pass18_review_snapshot_v1.json`
- `qa/verify_pass18_packet.py`

- `PASS17_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS17.json`
- `MINIMUM_SCALE_RECOMPRESSION_GUARD_PASS17.json`
- `qa/extract_pass17_minimum_scale_recompression_frames.py`
- `qa/pass17_minimum_scale_recompression_audit/extraction_receipt.json`
- `qa/pass17_minimum_scale_recompression_audit/contact_sheet_jpeg_q60_420_360p.png`
- `qa/pass17_minimum_scale_recompression_audit/contact_sheet_jpeg_q20_420_360p.png`
- `qa/pass17_minimum_scale_recompression_quantitative_audit.json`
- `qa/pass17_v8_minimum_scale_recompression/receipt.json`
- `qa/pass17_review_snapshot_v1.json`
- `qa/verify_pass17_packet.py`

- `PASS16_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS16.json`
- `MINIMUM_SCALE_GEOMETRY_GUARD_PASS16.json`
- `qa/extract_pass16_minimum_scale_geometry_frames.py`
- `qa/pass16_minimum_scale_geometry_audit/extraction_receipt.json`
- `qa/pass16_minimum_scale_geometry_audit/contact_sheet_x90_360p.png`
- `qa/pass16_minimum_scale_geometry_audit/contact_sheet_y90_360p.png`
- `qa/pass16_minimum_scale_geometry_quantitative_audit.json`
- `qa/pass16_v8_minimum_scale_geometry/receipt.json`
- `qa/pass16_review_snapshot_v1.json`
- `qa/verify_pass16_packet.py`

- `PASS15_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS15.json`
- `GEOMETRY_RESILIENCE_GUARD_PASS15.json`
- `qa/extract_pass15_geometry_frames.py`
- `qa/pass15_geometry_audit/extraction_receipt.json`
- `qa/pass15_geometry_audit/contact_sheet_squeeze_x90.png`
- `qa/pass15_geometry_audit/contact_sheet_squeeze_y90.png`
- `qa/pass15_geometry_quantitative_audit.json`
- `qa/pass15_v8_geometry/receipt.json`
- `qa/pass15_review_snapshot_v1.json`
- `qa/verify_pass15_packet.py`

- `PASS14_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS14.json`
- `DARK_TONE_RESILIENCE_GUARD_PASS14.json`
- `qa/extract_pass14_shadow_floor_frames.py`
- `qa/pass14_shadow_floor_audit/extraction_receipt.json`
- `qa/pass14_shadow_floor_audit/contact_sheet_clean.png`
- `qa/pass14_shadow_floor_audit/contact_sheet_shadow_floor_16.png`
- `qa/pass14_shadow_floor_audit/contact_sheet_shadow_floor_48.png`
- `qa/pass14_shadow_floor_quantitative_audit.json`
- `qa/pass14_v8_shadow_floor/receipt.json`
- `qa/pass14_review_snapshot_v1.json`
- `qa/verify_pass14_packet.py`

- `PASS13_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS13.json`
- `DIRECTIONAL_SMEAR_GUARD_PASS13.json`
- `qa/pass13_directional_smear_audit/extraction_receipt.json`
- `qa/pass13_directional_smear_audit/contact_sheet_clean.png`
- `qa/pass13_directional_smear_audit/contact_sheet_smear_w07.png`
- `qa/pass13_directional_smear_audit/contact_sheet_smear_w21.png`
- `qa/pass13_directional_smear_quantitative_audit.json`
- `qa/pass13_v8_directional_smear/receipt.json`
- `qa/pass13_review_snapshot_v1.json`
- `qa/verify_pass13_packet.py`

- `PASS12_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS12.json`
- `SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json`
- `qa/pass12_spatial_defocus_audit/extraction_receipt.json`
- `qa/pass12_spatial_defocus_audit/contact_sheet_clean.png`
- `qa/pass12_spatial_defocus_audit/contact_sheet_defocus_r1_50.png`
- `qa/pass12_spatial_defocus_audit/contact_sheet_defocus_r4_00.png`
- `qa/pass12_spatial_defocus_quantitative_audit.json`
- `qa/pass12_v8_spatial_defocus/receipt.json`
- `qa/pass12_sharpness_safe_mockup/receipt.json`
- `qa/pass12_sharpness_safe_quantitative_audit.json`
- `qa/pass12_review_snapshot_v1.json`
- `qa/verify_pass12_packet.py`

- `PASS11_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS11.json`
- `RECOMPRESSION_RESILIENCE_GUARD_PASS11.json`
- `qa/pass11_recompression_audit/extraction_receipt.json`
- `qa/pass11_recompression_audit/contact_sheet_clean.png`
- `qa/pass11_recompression_audit/contact_sheet_jpeg_q60_420.png`
- `qa/pass11_recompression_audit/contact_sheet_jpeg_q20_420.png`
- `qa/pass11_recompression_quantitative_audit.json`
- `qa/pass11_v8_recompression/receipt.json`
- `qa/pass11_review_snapshot_v1.json`
- `qa/verify_pass11_packet.py`

- `PASS23_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS23.json`
- `MINIMUM_SCALE_COLOR_REDUNDANCY_GUARD_PASS23.json`
- `qa/extract_pass23_minimum_scale_color_vision_frames.py`
- `qa/pass23_minimum_scale_color_vision_audit/extraction_receipt.json`
- `qa/pass23_minimum_scale_color_vision_quantitative_audit.json`
- `qa/build_pass23_v8_minimum_scale_color_vision.py`
- `qa/pass23_v8_minimum_scale_color_vision/receipt.json`
- `qa/audit_pass23_minimum_scale_color_vision.py`
- `qa/pass23_review_snapshot_v1.json`
- `qa/verify_pass23_packet.py`
- `SOURCE_STATUS_FREEZE.json`
- `FRAME_DIAGNOSIS.md`
- `PASS10_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS10.json`
- `AMBIENT_CONTRAST_GUARD_PASS10.json`
- `qa/pass10_ambient_contrast_audit/extraction_receipt.json`
- `qa/pass10_ambient_contrast_audit/contact_sheet_clean.png`
- `qa/pass10_ambient_contrast_audit/contact_sheet_uniform_black_lift_20pct.png`
- `qa/pass10_ambient_contrast_audit/contact_sheet_uniform_black_lift_40pct.png`
- `qa/pass10_ambient_contrast_quantitative_audit.json`
- `qa/pass10_v8_ambient_contrast/receipt.json`
- `qa/pass10_review_snapshot_v1.json`
- `qa/verify_pass10_packet.py`
- `PASS9_ENCODED_FRAME_AUDIT.md`
- `BLOCKER_PACKET_PASS9.json`
- `TITLE_SAFE_STORYBOARD_CORRECTION_PASS9.json`
- `REDUNDANT_ENCODING_GUARD_PASS8.json`
- `CAPTION_SAFE_STORYBOARD_CORRECTION_PASS7.json`
- `qa/pass9_safe_area_audit/extraction_receipt.json`
- `qa/pass9_safe_area_audit/contact_sheet_clean.png`
- `qa/pass9_safe_area_audit/contact_sheet_symmetric_crop_3pct.png`
- `qa/pass9_safe_area_audit/contact_sheet_symmetric_crop_5pct.png`
- `qa/pass9_safe_area_audit/contact_sheet_horizontal_crop_5pct.png`
- `qa/pass9_safe_area_audit/contact_sheet_vertical_crop_5pct.png`
- `qa/pass9_safe_area_quantitative_audit.json`
- `qa/pass9_v8_safe_area/receipt.json`
- `qa/pass9_review_snapshot_v1.json`
- `qa/verify_pass9_packet.py`
- `STORYBOARD_PROPOSAL.json`
- `proposal_frames/v8/contact_sheet.png`
- `STATIC_PROPOSAL_QA.md`
- `FUTURE_RESULT_FIGURE_SPEC_HELD.md`
- `qa/static_proposal_validation.json`
- `MANIFEST.sha256`

## Gates unchanged

No candidate bundle, TTS, shared-tool edit, upload, publication, website/cockpit, DB, deploy/restart, or Git action is requested or authorized by this worker packet.
