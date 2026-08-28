# KUN_GATE_V12

Timestamp: 2026-08-13 KST

## Verdict

PASS_FOR_V12_RENDERED_VISUAL_GATE.

Bound source targets:

- `NARRATION_DRAFT_V12.md` - SHA-256 `178ffe4ada125668c8ff84bc156adee7820954591f9781adb7101aac562d80da`
- `STORYBOARD_DRAFT_V12.json` - SHA-256 `9d55257fe62c7a82d2fe32f424e896ce079393219c08aed6663b6c90c3539399`
- `V12_VISUAL_TEXT_CONTRACT.json` - SHA-256 `c91662e15de095161e84d128683dd69150c8a73b4cbb6f303dda8f79c943999c`
- `V12_SOURCE_FREEZE_RECEIPT.json` - SHA-256 `08898232927ec926b74030fc61113e813b716b9557ab5136d429366ee3c19cf3`

I also found and inspected the local encoded V12 freeze even though the dispatch text said "No audio, no render":

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v12-local-20260813T1657K.mp4`
- SHA-256 `060764c04ba095637cb484237064d501e097b1c326d7bf8b389a22292f96d9c2`
- SRT SHA-256 `8966f66a3d74c9b0e0c80c7d1aff9651bf6a5ee7267d72347f75f86d3ad7d8d5`
- VTT SHA-256 `e893244f46e9bd377defc81d4afeb37a32a211adafee776103baa32790874f13`

This pass is not upload approval, YouTube caption-serving approval, publication acceptance, or Duho acceptance.

## Text Deletion Gate

The 54 deleted viewer-facing strings did not remove a load-bearing safety condition in a way that makes the artifact unsafe.

The two most important safeguards survive:

- Card 01 retains the full boundary badge from frame zero: `A PERSONAL SIDE-QUESTION - NOT PART OF THE LAB'S RESEARCH PROGRAMME`.
- The narration still says the route closes while the idea is "not declared true or false."

Other deleted guards are carried either by narration or by deterministic visual logic:

- The removed Card 01 "IDEA NOT DECLARED TRUE OR FALSE" screen text is now carried by the spoken line and by the closed-but-not-demolished gate.
- The removed Card 05 "NO 95.4% LOWER-BOUND VALUE..." line is carried by the retained anchor plus the open-ended fade/no-terminus render rule.
- The removed Card 06 "NOT ADJUDICATED HERE" line is carried by the traveller stopping at the fork while the narration says the record and video do not decide.
- Cards 09-11 retain the non-identification logic through the footprint split, two locks, and keyholes.

I verified the V12 closed-world viewer-text contract against the storyboard, including Card 08's four repeated question marks. The contract and storyboard match when `repeat` is honored. I found zero viewer-facing personal or seat names in the V12 storyboard strings.

## Visual Claim Gate

The pictures make the intended argument rather than a stronger one.

- Card 01: the gate closes the galaxy-fog road but does not destroy it. That reads as route closure, not BHU disproof.
- Card 02: five icons diverge to different endpoints. That supports "no shared prediction" without claiming exhaustive review beyond the surveyed set.
- Card 03: dartboard/no-board/two-thrower sequence cleanly expresses missability plus identification.
- Card 04: the mass gauge is deterministic; generated imagery is limited to non-quantitative atmosphere/prop language. The quote is source-bounded and legible in the rendered frame.
- Card 05: the rendered late frame shows chart data and a continuous 95.4% fade with no lower-bound endpoint, arrow, tick, bracket, marker, or plotted value. I saw no fabricated 1.95-style precision.
- Card 06: the fork and stopped marker preserve the refusal to adjudicate.
- Card 07: unequal stacks plus a question-mark gap express qualitative difference without invented amplitude.
- Card 08: timeline plus empty slots preserve post-hoc/non-calibrated forecast logic.
- Card 09: the footprint split is generic and unlabeled. It does not name rival cosmologies or imply a specific alternative cause.
- Cards 10-11: locks and keys close/reopen the route on calibration plus uniqueness, not on truth or falsity of BHU.

## Generated Imagery

The generated-imagery boundary is adequate. The source contract forbids generated text and generated quantitative pixels. The freeze reports no generated assets used in quantitative Cards 04 or 05, and the rendered text projection audit passes the closed-world text list exactly.

The weakest thing is Card 09's footprint metaphor: it is very plain and may read as a bit cartoonish in a public science video. It is not a claim-safety blocker; in fact, being unlabeled helps avoid the prior risk of freezing uncited rival cosmology classes.

## Final Ruling

PASS on V12 claim safety, deleted-text safety, generated-boundary safety, and rendered visual-claim inspection for the exact hashes above. The next separate gates are encoded A/V quality and any YouTube/upload-specific serving checks, especially subtitle serving after upload.
