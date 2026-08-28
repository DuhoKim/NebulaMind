# KUN QUASAR-DIPOLE VIDEO OVERCLAIM GATE

Timestamp: 2026-08-11T16:13:47 KST

## Verdict

PASS_CLAIM_SAFETY.

Safe to show as a compressed video version of the external methods note, with one non-blocking weakness recorded below. This is not publication or Duho acceptance.

## Bound Artifact

- Candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/quasar-dipole-video-20260811T1603K/quasar-dipole-record-narrated-20260811T1608.mp4`
- SHA-256 verified on disk: `17950101f5dce1cf1c8b186b97a277a09239c51a452cefc4024a734ec4653821`
- ffprobe: 200.033333 s, H.264 1920x1080 30 fps, AAC mono 24000 Hz
- Audio decode/level sanity: stream decodes through full file; volumedetect mean -21.2 dB, max -0.7 dB
- Storyboard reviewed: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/quasar-dipole-video-20260811T1603K/storyboard_quasar_dipole.json`
- Binding brief reviewed: `reviews/LANA_VIDEO_CLAIM_BOUNDARY_QUASAR_DIPOLE_20260811.md`
- Source note SHA verified: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`

Note on spoken review: no local ASR backend is installed in this environment. I therefore gated spoken-claim content against the storyboard body text used for the 13 rendered audio segments, the preserved audio stream, and the rendered lower-third narration text sampled from the encoded MP4. I did not claim an independent phonetic transcript.

## Spoken Narration Gate

PASS.

- B1 boundary appears at the start of the narration payload and is visible in the encoded frame sampled around 0:05: "This video reports what two such measurements published, and why their disagreement cannot yet be resolved. It makes no claim about the universe itself." This satisfies the requirement that the universe/cosmological-principle boundary be early, not saved for the end.
- The selection-function fork narration is bounded: "obvious suspect" is immediately followed by "obvious is not demonstrated" and "leading stated difference - not the explanation." That does not make the selection fork the demonstrated cause.
- The data-identity narration keeps the qualification: "strongly supported to be the same release - not verified byte for byte" and "Keep that word: supported." It does not say "same data."
- The closing narration stays inside the permitted claim: "not attributable from the published record," with coupled choices, an unstated correction, and different quantities as the reasons the published record stops answering.
- The kinematic-null amplitudes 0.0048/0.0043 are not narrated; the superseded 0.0080/0.0068 pair is also absent. No numerical inference is drawn from their relation.

## On-Screen Text Gate

PASS.

Sampled encoded frames from the MP4:

- ~0:05, B1: boundary sentence is on screen and readable; no universe-is-anisotropic or cosmological-principle-fails claim.
- ~0:35, B3/verdict: "Finding: the cause is not attributable from the published record"; body says neither number can test the principle until the disagreement is explained. This is a methods-record claim, not a cosmology claim.
- ~1:05, B5 identity: heading says "Strongly supported to be the same release - not verified byte for byte"; figure marks Singal as pinned and Mittal as "no self-bound record." This preserves the external-note qualification.
- ~1:30, B6 fork: heading says "The most visible difference is not the demonstrated cause"; footer says "the leading STATED difference - not the demonstrated explanation." The visual does not convert the fork into causation by layout.
- ~1:50, B7 coupled choices: "The choices are coupled - never varied one at a time"; this prevents causal narrowing to the selection-function fork alone.
- ~3:10, close: "Not attributable from the published record - that is the result"; body includes "One catalogue - as far as the public record can establish" and the exact stopping point: coupled choices, unstated correction, different quantities.

## Specific Overclaim Checks

1. Selection-function fork as demonstrated cause: PASS. The fork is framed as the leading stated difference and obvious suspect, not the explanation. The adjacent coupled-choice card blocks the false inference that one isolated switch explains the factor-of-three gap.

2. Drift into cosmological anisotropy / cosmological principle failure / paper correctness: PASS. The early boundary sentence is present, and later text says neither number can test the principle until the disagreement is resolved. The video never says either paper is correct.

3. Data identity: PASS. The video uses "one catalogue" and "same release," but the load-bearing identity card and closing sentence carry "strongly supported" / "not verified byte for byte" / "as far as the public record can establish." I found no forbidden "same data" assertion.

4. Expected amplitudes: PASS. The video omits both the corrected 0.0048/0.0043 pair and the superseded 0.0080/0.0068 pair. There is no numerical inference from expected-amplitude ratios.

5. Closing claim: PASS. The close does not exceed section 5 of the note. It says the published record does not contain the answer and identifies what a resolving reconstruction would require.

## Weakest Thing

The weakest compression is the repeated phrase "one catalogue" in the title/card 3/closing. Standing alone, it could sound like byte-verified identity. In this encode it is non-blocking because the identity card explicitly says "strongly supported to be the same release - not verified byte for byte," and the closing carries "as far as the public record can establish." Do not remove those qualifiers in any future shorter cut.

## Replacement Wording

No blocking replacement required.
