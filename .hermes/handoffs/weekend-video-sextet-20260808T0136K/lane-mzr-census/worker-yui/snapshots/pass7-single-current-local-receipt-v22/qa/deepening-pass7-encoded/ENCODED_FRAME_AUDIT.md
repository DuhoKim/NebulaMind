# Encoded-frame scientific-presentation audit — isolated deepening pass 7

Audit timestamp: 2026-08-08T04:54:41+09:00

## Exact target and fresh method

- Read-only candidate: `/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4`
- Candidate SHA-256: `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`
- Scoped latest-candidate discovery used `mzr-archive-census*.mp4`: four matching aliases/versioned cuts; the 01:55 version remains latest and unchanged.
- Stream reverified: H.264 1920×1080 at 30 fps plus AAC mono 24 kHz; duration 128.4 seconds; 13,989,937 bytes.
- Fresh sampling is transition-focused rather than another integer cadence: each of the 14 pass-6 hard cuts was sampled at −0.25 s and +0.25 s (28 frames), and the midpoint of all 15 resulting holds was sampled (15 frames), for 43 fresh encoded frames.
- Boundary contact sheet: `contact_sheet_cut_boundaries_28frames.jpg`, SHA-256 `215834598ff62a28afb00b0c435b6dfec7f69e9417214abb9f1345f845617f5c`.
- Hold-midpoint contact sheet: `contact_sheet_hold_midpoints_15frames.jpg`, SHA-256 `fa9388349ff37de815769e57ae4593df7adae1996fd7fbb5f467ef7cf53af309`.
- Frame manifest: `FRAME_HASHES.json`, SHA-256 `04f0c4c1733d71b512248e3006e1d6761a0b6635b162321537f991a312be96ba`; 43/43 frames pinned.
- Full-stream video decode completed with an empty ffmpeg error log.
- `OCR_DENSITY.json` is a reproducible screen-text-density proxy, not an audio transcript or semantic verdict. `BOUNDARY_CONTINUITY.json` uses a declared scientific-anchor vocabulary as an aid; the pixel review remains the decision surface.
- Audio meaning was not inferred or audited.

## Verdict

`FAIL_FOR_SCIENTIFIC_REPRESENTATION_STATE_CONTINUITY_AND_PRIOR_BOUNDARIES`

This fresh audit does not clear, alter, or replace the failed candidate.

## Fresh pass-7 finding — cuts erase scientific state rather than hand it forward

Eleven of 14 cut pairs preserve zero declared scientific anchors in OCR. The remaining three preserve only one anchor each: `redshift` at cut 2, `157` at cut 6, and `62` at cut 7. This is not used as a standalone semantic score; it corroborates the pixels. The candidate is a sequence of full-frame resets, not one evolving evidence surface.

### Exact continuity failures

- Cut 2 at 13.767 s: the archive question resets to a literature metallicity plot. Only the word `redshift` persists; metadata-census scope, single-table topology, and not-a-measurement status do not.
- Cuts 3–4 at 25.567 and 28.067 s: the plot is replaced by a standalone `Data` divider and then by method prose. The source/evidence surface is absent during the divider, and the method does not inherit a visible retrieval topology.
- Cut 5 at 41.833 s: method prose resets to giant `157`; UCD/name channels, 178, −21, and 19/2 drop bins do not persist.
- Cut 6 at 52.467 s: giant `157` resets to the 157/62 bar. Only `157` persists; no direct 157→T2 path or 178→21→157 conservation is retained.
- Cut 7 at 61.433 s: the 157/62 bar resets to giant `62`. Only `62` persists. Its parent 157, side-check geometry, and all-157-to-T2 requirement disappear, making the strongest evidence-class/topology defect more severe at the boundary.
- Cuts 8–9 at 68.667 and 71.167 s: count context resets to a standalone `Analysis` divider and then to retrieval prose. No T1 stage or parent population is carried across.
- Cut 10 at 85.767 s: the T1 retrieval-instrument paragraph resets to T2 contract prose with zero declared anchors preserved. Without persistent stage labels, the two different control systems can be read as one result.
- Cuts 11–12 at 99.533 and 102.000 s: T2 contract prose resets to a `Discussion` divider and then to taxonomy prose. Application-not-completed/no-count status never persists into the limitation card.
- Cuts 13–14 at 118.133 and 120.633 s: taxonomy resets to `Summary`, then to a generic brand close. Characterization-not-ruling, reportable/pending, no-count/no-measurement, and single-table scope are all absent.

## Midpoint density/readability evidence

Tesseract detected more than 25 on-screen word tokens in six of 15 midpoint states. The maximum is 96 on the literature-plot state because plot labels, legend, caption, prose, and a long internal source line coexist. Other dense states include method (32), 157/62 graphic (49), retrieval prose (40), T2 prose (43), and taxonomy prose (40). The count is an OCR proxy, not a semantic metric, but it confirms that the presentation alternates between empty dividers and dense full-frame states instead of pacing related evidence through persistent layers.

## Reconfirmed blockers

All pass-2 through pass-6 blockers remain: target concepts presented as adjudicated search-axis results; false 62 evidence wording/topology; missing 178→21→157/drop-bin graphic; T1/T2 control-stage conflation; incomplete 12-decoy/3-anchor provenance; missing T2 application/no-count status; collapsed taxonomy; internal filenames as citations; generic close; and long unchanged evidence states.

## Evidence-bounded correction decision

A safe pass-7 storyboard correction is justified while leaving visual v8 pixels unchanged:

1. add an explicit cross-beat state-continuity contract; every beat must declare what scientific state enters, persists, retires, and exits;
2. prohibit full-frame scientific resets: section identity must coexist with the current evidence layer;
3. keep the 178→−21→157→T2 main spine visible from its first construction through the qualified close;
4. keep 62 attached to its 157 parent as a side check whenever 62 is visible; never isolate a giant 62;
5. persist explicit T1/T2 stage identity across the retrieval-check→contract-status handoff;
6. carry application-not-completed/no-count and not-an-MZR/single-table scope into the final state;
7. require any future exact candidate to pass cut-boundary continuity, hard-cut/evidence-state timing, and sentence/action alignment together.

This correction changes presentation state and continuity only. It introduces no new count, source claim, eligibility ruling, uncertainty, metallicity result, or MZR measurement. Static visual v8 remains a compatible overview, not proof that transition continuity was encoded.
