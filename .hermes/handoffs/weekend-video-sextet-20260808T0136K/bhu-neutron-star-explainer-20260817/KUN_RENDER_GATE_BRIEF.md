# GATE REQUEST — rendered explainer video

Write your verdict to `bhu-neutron-star-explainer-20260817/KUN_RENDER_GATE_20260818.md`, first line
the verdict.

## Pinned

    video      build/BHU_NEUTRON_STAR_EXPLAINER_LOCAL_REVIEW.mp4
               SHA-256 e5d6fae9436e6f66ac5825802236f4f6cba095c1e9b6676b46bc55d1bc160e18
               1920x1080@30, 334.100 s, 11.1 MB, h264/aac + embedded captions
    report     build/BUILD_REPORT.md   ·   freeze  build/FREEZE.json
    gated text SCRIPT.md  ·  ledger CLAIM_LEDGER.md  ·  your PASS_EXPLAINER_PACKET

## What is already claimed, and needs checking rather than accepting

Yui reports `PASS_EXACT_ASR_WORD_DIFF`, `PASS_EXACT_HEADING_PROJECTION_AND_ENCODED_PIXELS`,
`PASS_EXACT_ENCODED_CAPTION_PAYLOADS`. Re-derive what you can rather than reading her report:
the video is on disk, the script is on disk, and the captions are embedded in the container.

## Decide

1. **Does the rendered artifact say what the gated script says?** A video and a script are different
   objects. Verify the ASR diff independently if you can — mispronunciation, truncation, or a
   dropped line would all pass a source-level check and fail a viewer.
2. **Do the on-screen headings match the script's assertion headings exactly?** She claims this was
   verified in encoded pixels. A card is a claim; a mistyped card is a false claim that outlives
   every caveat in the packet.
3. **The four refused claims** — does the video, in narration, captions, or any on-screen text,
   anywhere say the black-hole-universe idea is falsified, that Smolin's hypothesis is refuted, that
   *we* measured or discovered anything, or cite the 2.35-solar-mass star as supporting evidence?
   My own caption scan found none; check the cards too, which I did not read pixel by pixel.
4. **Panel 03's uncertainty rendering — check this one carefully, because I got it wrong.** I
   instructed that the 2.08 ± 0.07 error bar should visibly dip below the 2.00 line. That would have
   been false: at 68.3% the interval is about [2.01, 2.15] and sits above 2.00, which is exactly why
   the measurement clears at the quoted level. Yui instead drew the 68.3% interval above the line
   with a soft 95.4% halo crossing it. Confirm what is actually rendered is the true picture — clears
   at the quoted level, fails at the strict one — and not my version.
5. **Is it still local-only?** No upload, no visibility change, no credits, nothing published. The
   freeze status should read local review, not release.

## Constraints

Review only. Do not upload, publish, change visibility, or spend credits. Do not touch
`portal.nersc.gov` — the checksum harvest resumes at 12:00 KST. Gating this authorizes review, not
release; publishing remains Duho's separate decision and unlisted-only even then.

## Return

    PASS_RENDERED_EXPLAINER
    HOLD_<SHORT_REASON_IN_CAPS>

If the rendered video overstates anywhere the script does not, hold it. This is the last check before
something leaves the machine.
