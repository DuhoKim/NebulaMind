# Encoded-frame scientific-presentation audit — isolated deepening pass 6

Audit timestamp: 2026-08-08T04:36:18+09:00

## Exact target and method

- Read-only candidate: `/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4`
- Candidate SHA-256: `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`
- Scoped discovery used `mzr-archive-census*.mp4`; the versioned 01:55 cut and narrated alias remain byte-identical and latest for this lane. Unrelated C41 filenames containing `mzr` were excluded.
- Stream: H.264 1920×1080 at 30 fps plus AAC mono 24 kHz; duration 128.4 seconds; 13,989,937 bytes.
- Fresh sample: 32 encoded frames at `3 + 4n` seconds for `n=0..31`, completing the four offset classes after pass 3 (`4n`), pass 4 (`2+4n`), and pass 5 (`1+4n`).
- Contact sheet: `contact_sheet_32frames_offset3.jpg`, SHA-256 `08539f7b3e535cde8811352f62ec6968dfe7db7982a4c5f6b781c451932f0bd4`.
- Frame manifest: `FRAME_HASHES.json`, SHA-256 `4252d9f8b404924d4ccf67025abb5138c8adf47c20a6bb67ec348b0752eb1e3c`; 32/32 frame hashes pinned.
- Full-stream decode completed with no ffmpeg error.
- Hard-cut audit: ffmpeg `select='gt(scene,0.02)',showinfo`; log SHA-256 `ebcf356c265d784f312982a303fba9dd949efd804f1caa037268539a5bd6cf08`; results in `SCENE_HOLDS.json`.
- Audio meaning was not inferred or audited.

## Verdict

`FAIL_FOR_SCIENTIFIC_REPRESENTATION_STATIC_EVIDENCE_STATE_CAUSALITY_AND_PRIOR_BOUNDARIES`

This is a fresh audit of the unchanged failed candidate. It does not clear, replace, or modify that candidate.

## Fresh pass-6 finding — scientific claims remain long static evidence states

The hard-cut audit detects 14 cuts and 15 resulting holds. Ten holds exceed six seconds; the longest is 16.133 seconds. Subtle background motion or compression variation may occur, so these are not described as pixel-identical holds. They are unchanged **scientific evidence states**: no new metric, label, topology, comparison, or status is revealed between hard cuts.

Long content-state intervals include:

- 2.667–13.767 s: 11.100 s opening prose state;
- 13.767–25.567 s: 11.800 s literature scatter state;
- 28.067–41.833 s: 13.767 s method paragraph state;
- 41.833–52.467 s: 10.633 s giant-157 state;
- 52.467–61.433 s: 8.967 s 157/62 graphic state;
- 61.433–68.667 s: 7.233 s giant-62 state;
- 71.167–85.767 s: 14.600 s retrieval-instrument paragraph state;
- 85.767–99.533 s: 13.767 s T2-contract paragraph state;
- 102.000–118.133 s: 16.133 s contamination/limitation paragraph state;
- 120.633–128.400 s: 7.767 s generic closing state.

Separate 2.5-second section-divider holds displace evidence at 25.567–28.067 s, 68.667–71.167 s, 99.533–102.000 s, and 118.133–120.633 s.

### Pixel examples

- 3/7/11 s: the same opening text state persists. It adjudicates the three physical concepts and supplies no progressive metadata-search diagram.
- 15/19/23 s: the literature scatter persists. The plot is readable, with redshift and `12 + log(O/H)` axes and a method legend, but the page says its spread is what this census exists to measure. The archive census did not make that measurement, and the internal corpus path is not an audience citation.
- 31/35/39 s: the method remains paragraph text. No UCD/name-channel comparison or three-axis reach geometry is visible.
- 43/47/51 s: the giant `157` state persists. `178 − 21 = 157` and the `19 redshift / 2 abundance` bins are not visible as a conservation flow.
- 55/59 s: the 157/62 bar is one of only two plotted evidence states, but its legend and body call 62 “explicit gas-phase evidence.” It visually nests 62 inside 157, omits 178→21→157, and exposes an internal JSON path.
- 75/79/83 s: the retrieval check is a 14.6-second paragraph hold. `7/7`, `0/3`, `T1 RETRIEVAL-INSTRUMENT CHECK`, and `PRECISION NOT CERTIFIED` are absent as visible metrics/status.
- 87/91/95/99 s: the T2 contract is a 13.767-second paragraph hold. It shows seven rounds and twelve decoys, omits three anchors, application-not-completed, and no-eligible-table-count status, and cites `FREEZE_RECORD_T2.md`.
- 103/107/111/115 s: the longest content hold collapses symbol/meaning collisions and target-domain mismatches into “symbol Z, not the concept.” It is not a classification surface and does not say `RECORDED CHARACTERIZATION · NOT T2 RULINGS`.
- 123/127 s: the close is a generic brand/provenance hold. It does not preserve reportable-now facts, pending T2 application, no eligible-table count, no MZR measurement, single-table/crossmatch scope, or an audience-reachable count ledger.

## Reconfirmed blockers

All pass-2 through pass-5 blockers remain visible: target concepts versus search-axis reach, false 62 evidence status and topology, missing 178→21→157/drop-bin graphics, T1/T2 control-family separation, incomplete 12-decoy/3-anchor provenance, missing T2 application/no-count state, collapsed contamination taxonomy, internal receipt paths as citations, and generic closure.

## Evidence-bounded correction decision

A safe pass-6 storyboard correction is justified without changing the accepted static v8 overview pixels:

1. add an explicit scientific-presentation motion contract: no substantive evidence state may remain unchanged for more than four seconds;
2. map every substantive narration clause to a visible reveal state, with at least two reveal states per beat;
3. remove standalone section-divider holds; section identity must coexist with the evidence surface;
4. keep the final reportable/pending summary readable as a held state, but reveal its reportable and pending columns separately before the final combined hold;
5. require future encoded-candidate QA to re-run hard-cut/evidence-state timing, frame custody, and sentence/action alignment.

The correction changes presentation causality only. It adds no count, ruling, eligible-table number, metallicity/MZR measurement, source claim, or fabricated uncertainty. Static visual v8 remains an overview proposal, not proof that the motion contract was encoded.