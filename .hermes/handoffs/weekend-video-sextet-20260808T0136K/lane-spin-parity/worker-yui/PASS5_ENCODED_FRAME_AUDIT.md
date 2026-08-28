# Spin worker-Yui — isolated deepening pass 5 encoded cut-boundary audit

Extraction completed: 2026-08-07T19:58:17.422409+00:00 (2026-08-08T04:58:17.422409+09:00)
Audit completed: 2026-08-08T05:00:57+09:00
Scope: exact held Hwao candidate, read-only; separate from sealed v8 static proposal.
Verdict: `FAIL_SCIENTIFIC_PRESENTATION_AND_HELD_SOURCE_GATE`

## Fresh cut-boundary extraction

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`; exact official-freeze match.
- Probe: 243.300 s; 28,637,729 bytes; H.264 1920×1080 at 30 fps; AAC mono 24 kHz.
- Fresh scene detection at threshold 0.04 again found 15 cuts and 16 scenes.
- Pass 5 independently decoded five frames around every cut: −2 frames, −1 frame, the detected cut timestamp, +1 frame, and +2 frames. Total: 75 RGB 1920×1080 PNGs.
- Exact receipt and per-frame hashes: `qa/pass5_boundary_audit/extraction_receipt.json`.
- Contact sheets: `contact_sheet_minus_2f.png`, `contact_sheet_minus_1f.png`, `contact_sheet_cut.png`, `contact_sheet_plus_1f.png`, and `contact_sheet_plus_2f.png` under `qa/pass5_boundary_audit/`.
- No candidate byte, audio, shared tool, public asset, storyboard of record, or sealed-v8 pixel was changed.

## Scientific-presentation finding at every cut

All 15 transitions are clean hard cuts. Two and one frames before each cut show the complete outgoing card. The frame decoded at the cut timestamp already shows the complete incoming card; the +1 and +2 frames remain on that incoming card. No blank frame, flash, wipe, crossfade, partial title, mixed plot, disappearing citation, or transitional disclaimer was found.

Deterministic reference classification compares each boundary frame with pass-4 stable outgoing and incoming frames. All 15 sequences are exactly `outgoing, outgoing, incoming, incoming, incoming`; every cut-timestamp frame classifies as incoming. The weakest incoming/outgoing reference separation is still 6.275656×, so no ambiguous blend is hidden by the visual contact-sheet scale. Evidence: `qa/pass5_cut_classification.json`.

This strengthens the held-candidate failure:

- The transition from scene 6 to result-bearing scene 7 reveals the complete result plot immediately at the cut.
- The transitions into scenes 9, 10, and 11 likewise reveal their complete result bars, matrix, and decomposition immediately.
- No structural `RESULT HELD`, `FRAME UNSTATED`, or separate-authorization gate appears before, during, or after those cuts.
- Small caveats and internal provenance arrive simultaneously with the dominant result visual; they never get a prior frame in which to establish the scientific boundary.
- The transition into scene 16 cleanly reveals the URL/work-in-progress close, again without a structural held boundary.

The result assertions are therefore not only persistent during scene dwell time (pass 4); they are fully present on the first incoming frame. A narration or timing change cannot repair this representation failure.

## Sealed-v8 disposition and evidence-backed transition correction

Fresh pass-5 review found `RESULT HELD` on every one of the seven sealed v8 frames, including both sides of every possible scene transition. No result plot, result value, character close, or URL exists in v8. No pixel or copy defect warrants v9.

The next safe correction is a transition contract for Hwao's integrator request, without modifying sealed bytes:

1. Use clean hard cuts between the seven static v8 scenes.
2. Keep the full outgoing frame through its last frame and show the complete incoming frame at the cut.
3. Keep `RESULT HELD` visible on both sides of every cut.
4. Do not crossfade, wipe, zoom, morph, or animate result-bearing material into the method-only deck.
5. Do not insert blank or badge-free transition frames.

This is an evidence-backed storyboard/integration guard, not render authorization. It preserves v8's exact static review while preventing transition effects from weakening its structural gate.

## Pass-5 exact blocker deepening

Pass 4 classified the six non-UTF-8 files by container and source metadata. Pass 5 now decodes and scans their content directly:

- four gzip archives were decompressed with Python `gzip.decompress`;
- two literature PDFs were text-extracted with `pdftotext`;
- decoded payload hashes and marker counts are bound in `qa/pass5_binary_content_scan.json`;
- raw source content is not reproduced in the packet;
- zero decoded binary files contain any exact T4 filename/hash or A3.8 name/hash identity marker;
- zero decoded binary files contain the exact T4+A3.8 hash pair.

The exact A3.8 absence proof no longer relies only on binary-file mtimes. Combined with pass 4's nine post-T4 UTF-8 scan, all 209 regular source files are content-covered for the exact identity markers required by the frozen review contract. This is a custody/absence finding only and does not adjudicate T4.

`KUN_FRAME_REVIEW.md` remains exactly `FRAME REVIEW: AGREES FRAME_UNSTATED`.

## Integrator-safe next action

Preserve 0149 as failed evidence. If Hwao elects to integrate the method-only proposal, start from sealed v8 and apply the hard-cut transition contract above. Do not reuse held scenes 7, 9, 10, or 11, and do not transfer their values into new cards. Result integration, narration, candidate encoding, publication, and public wiring remain separate explicit gates.
