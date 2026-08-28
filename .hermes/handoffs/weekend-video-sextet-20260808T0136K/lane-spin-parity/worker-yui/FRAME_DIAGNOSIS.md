# Encoded-frame diagnosis — spin worker Yui

Freeze: `spin-worker-yui-official-20260808T0210K`
Role: read-only visual/scientific QA adviser. No candidate, TTS, shared-tool, or storyboard-of-record write.

## Exact artifacts inspected

- Exact current public-tree MP4: SHA-256 `dfc8be91c47bf55b34c0040d1b6572b5960e31942c9a0cec1465d8bcf4f44585`, 93.0 s, H.264 video only, 1920×1080 at 30 fps. Pre-order extracted frames and contact sheet remain preserved under `lanes/spin/qa/current/`.
- Hwao's official narration-only canary: SHA-256 `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`, 243.3 s, H.264 + AAC mono, 1920×1080 at 30 fps.
- Scene detection on the exact candidate at threshold 0.04 found 15 hard cuts and 16 scenes. Evidence is in `qa/candidate_0149/cut_times.json`, full-resolution midpoint frames, and `contact_sheet_detected.png`.

## Exact current MP4

The current 93-second file is a sequence of ten static, mostly text-only cards. It contains no plot, axis, error bar, equation, table, handedness-convention schematic, or visible sample flow. Its two hero-number scenes (`667,944`, `29,053`) detach counts from denominators and relationships. Internal filenames are tiny audience-facing sources on some cards; the densest process claim, “Where the error actually was,” has no visible evidence or source and uses most of the frame as empty background. Nothing is clipped, but legibility alone does not make it a scientific presentation.

## Hwao narration-only candidate

### What materially improved

- The exact candidate is machine-valid and has one consistent Alloy track.
- Five evidence figures are now visible: sample/rung counts, asymmetry with error bars, frozen-threshold significance, paired-label matrix, and decomposition.
- The figures are much stronger than the current public-tree MP4's number cards. At full resolution, major axis labels, ticks, condition labels, and error bars are readable.

### What remains visually or semantically blocked

1. **Narration-only lineage.** Receipt says the storyboard is unchanged. Text-only scenes still occupy ten of sixteen scenes; several carry long paragraphs over large empty fields.
2. **Result status.** Frames 7, 9, 10, and 11 visually assert quarantined T3/T4 results. The crisp zero-line split and large assertion headlines dominate tiny caveat text. This is exactly the status conflict recorded in the official candidate's `QA.md`.
3. **Missing method bridge.** No scene defines `A = (N_CW − N_ACW)/(N_CW + N_ACW)`, defines ACW, or shows how a mirrored image creates two possible archive-frame interpretations.
4. **No visible hold on result figures.** The asymmetry frame includes an orange sentence saying it is not a cosmological result, but that sentence is small and below the plot. The dominant visual remains a clean split across zero. There is no `RESULT HELD` or `FRAME UNSTATED` primary label.
5. **Provenance leakage.** Figures and text cards expose internal names such as `T1_FUNNEL.json`, `T3_READING.json`, `LANA_T3_REDERIVATION.md`, and `KUN_FRAME_REVIEW.md`. Those are verification paths, not audience citations.
6. **Funnel grammar.** The strongest reusable scene is the sample/rung count figure. Its x-axis shows `SPIRAL_FLAG`, `0.80`, and `0.60` as parallel categories, but the headline “counts survive each one” and subtitle “where the sample goes at each rung” can be read as a sequential funnel. The rise from 30,412 at 0.80 to 51,157 at 0.60 demonstrates that these are alternate readouts, not successive filters. A method-only revision should say that explicitly and print exact counts on the bars.
7. **Weak close.** The final frame is only `nebulamind.net` plus process copy. It does not leave the allowed finding/evidence/boundary/next-gate matrix on screen.

## Full-resolution checks

### Frame 5 — sample/rung counts

- Major labels and ticks are readable and unclipped.
- Legend distinguishes passed, classified, and ties.
- Exact bar values are not printed; only 29,053 is present in body copy.
- `drawn from spin-parity-census-20260805T1922K/T1_FUNNEL.json` leaks an internal path.
- The plot and body have adequate clearance.
- Safe to adapt only as a method figure, with “parallel predeclared readouts” made explicit and internal provenance moved to the receipt.

### Frame 7 — asymmetry/error bars

- Equation on the y-axis, zero line, condition/rung labels, and uncertainty bars are readable at full resolution.
- No legend identifies colors; meaning is inferred from labels and body copy.
- The status fence is small, below the plot, and subordinate to the assertion headline.
- Internal verification filenames are visible.
- Because `video_reportable_now` is false, the result plot's visual hierarchy is not repairable by a smaller disclaimer. It should be absent from a method-only proposal.

## Ranked next visual grammar for Hwao

1. Replace quarantined result scenes with a full-screen method/status boundary, not a disclaimer over a result plot.
2. Show the three sample readouts as parallel branches with exact counts and scope labels.
3. Give the predeclared equation a dedicated scene with `ACW = anticlockwise` and ties excluded.
4. Add a conceptual two-branch convention diagram: labels stored as displayed versus de-mirrored; both point to `FRAME UNSTATED`.
5. Show column alignment as a connector/table (`36 probed`, `36 aligned`, `0 crossed`) while stating that this verifies the normal-leg mapping, not the mirrored storage frame.
6. Show the bias-control design: normal, monochrome, two mirror sets, 0.80/0.60 available, SPIRAL-flag unavailable for bias conditions.
7. End on `KNOWN / UNRESOLVED / NOT CLAIMED / NEXT GATE`, with no result number.

## Verdict

The Alloy canary fixes the audio route and exposes real plots, but it remains held and does not clear Duho's scientific-presentation complaint. The useful worker deliverable is a graphics-first, method-only storyboard and static frame proposal for Hwao, not another MP4 or narration pass.
