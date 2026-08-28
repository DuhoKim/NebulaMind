# KUN QUASAR-DIPOLE VIDEO V2 CLAIM-SAFETY RE-GATE

Timestamp: 2026-08-11 KST

## Verdict

PASS_CLAIM_SAFETY.

Safe to show as a claim-safe cut of v1. This is not publication or Duho acceptance.

Claim-safety judgment call: retaining Lana's spoken closing over a heading-only verdict card is correct. It preserves the mandated closing boundary in audio while satisfying the structural screen requirement. It does not create a trailing-qualifier problem because the final visible heading already contains the key scope limiter: "from the published record." The audio expands the verdict; it does not rescue an unsafe visual claim.

## Bound Artifact

- Candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/quasar-dipole-video-20260811T1603K/quasar-dipole-record-v2-narrated-20260811T1809.mp4`
- SHA-256 verified on disk: `1fff1fb6806733ceb15f56143a92c9254772f4598f32f28dc1fb7cf1af6736cc`
- Size observed: 4,243,215 bytes
- ffprobe: 186.033333 s, H.264 1920x1080 30 fps, AAC mono 24000 Hz
- Audio decode/level sanity: full-file mean -21.0 dB, max -0.7 dB; final 160-184.8 s segment mean -20.9 dB, max -2.0 dB
- Prior v1 pass: `reviews/KUN_QUASAR_DIPOLE_VIDEO_OVERCLAIM_GATE_20260811T1613K.md`
- v1 SHA preserved in candidate dir: `17950101f5dce1cf1c8b186b97a277a09239c51a452cefc4024a734ec4653821`

Note on spoken review: no local ASR backend is installed. I gated spoken-claim content against the storyboard/audio-track structure, the encoded audio stream presence, and the rendered lower-third text where present. The final closing has no lower-third body in v2, so I verified its audio segment exists and remains over the final heading, but I do not claim an independent ASR transcript.

## What Changed From V1

Diffing `storyboard_quasar_dipole.json` to `storyboard_quasar_dipole_v2.json` shows only:

1. slug changed to `quasar-dipole-record-v2`;
2. the 14 s caveat/claim figure card was deleted;
3. final card body text was removed, leaving the same final heading.

The final card heading remains: `Not attributable from the published record - that is the result`.

## Deleted Caveat Card Audit

The deleted v1 card displayed the full permitted claim:

- from the published record;
- strongly supported same Quaia v0.1.0 release, Mittal not byte-self-binding;
- cannot be attributed to one isolated analysis choice;
- choices are coupled;
- order-unity correction is unstated;
- two estimate different quantities.

Those qualifications survive in v2:

- ~0:05 encoded frame: B1 says the video reports what the measurements published and why disagreement cannot yet be resolved; "It makes no claim about the universe itself."
- ~0:35 verdict card: "Finding: the cause is not attributable from the published record."
- ~1:05 identity card: "Strongly supported to be the same release - not verified byte for byte" appears in the heading, figure banner, and lower-third narration text; the figure still marks Mittal as "no self-bound record."
- ~1:30 selection-fork card: "The most visible difference is not the demonstrated cause"; lower-third says the fork remains "the leading stated difference - not the explanation."
- ~1:50-2:20 reason cards: coupled choices, unstated order-unity correction, and different quantities are each retained before the ending.
- ~2:45-3:05 final card: heading-only verdict retains "from the published record."

Therefore deletion removed a redundant all-in-one caveat card, not the only occurrence of any load-bearing qualification.

## Overclaim Checks

1. **Selection-function fork as demonstrated cause:** PASS. V2 retains the "not the demonstrated cause" heading and the "obvious suspect / not demonstrated / leading stated difference - not the explanation" language.

2. **Cosmological overclaim:** PASS. The early boundary remains visible at ~0:05 and states no claim about the universe itself. V2 does not assert anisotropy, cosmological-principle failure, parity violation, or correctness of either paper.

3. **Data identity:** PASS. V2 retains "strongly supported to be the same release - not verified byte for byte." The natural "one catalogue" compression remains bounded by that card and by the final "from the published record" heading.

4. **Expected amplitudes:** PASS. The v2 storyboard contains none of `0.0048`, `0.0043`, `0.0080`, or `0.0068`; no numerical inference from those quantities is made.

5. **New ending:** PASS. The ending asserts nothing stronger than v1. The on-screen paragraph is gone; the final visual is the scoped verdict heading. Retained spoken closing is claim-safe because it repeats the record-level nature of the result rather than adding a late caveat needed to neutralize an unsafe heading.

## Weakest Thing

Same as v1: "one catalogue" remains the weakest compression. In v2 it is still non-blocking because the identity caveat survives visibly and early. Do not shorten this cut by removing the identity card or the B1 boundary.

## Non-Claim Caveat

`RECEIPT.md` says v2 audio lives in `_audio_quasar-dipole-record-v2/`, but that directory is not present in the candidate folder I inspected. This is a receipt/custody mismatch for Tori/Yui, not a claim-safety blocker, because the encoded MP4 audio stream itself exists and decodes.

## Replacement Wording

No blocking replacement required.
