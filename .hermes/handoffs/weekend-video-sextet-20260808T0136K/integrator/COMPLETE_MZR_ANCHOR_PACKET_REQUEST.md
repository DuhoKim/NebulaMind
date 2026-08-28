# REQUEST to the integrator — complete the mzr-anchor correction packet

Filed 2026-08-09 13:34 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"have the integrator complete the mzr-anchor packet."*

You are the single writer for candidate directories. This hands back work that should have been
yours: I built a candidate at Duho's instruction and left its packet incomplete.

## The candidate

`integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1300K/`
MP4 SHA-256 **`c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584`**
9,722,369 B · 219.533 s · 6,586 frames · h264 + aac mono 48 kHz

Supersedes `973daba3…` (preserved untouched), which Kun HELD for visual claim drift: the persistent
header `A metallicity offset has two explanations` presupposes the offset exists while the narration
says *"an **apparent** offset could instead be…"*. Fix: header → **`An apparent metallicity offset
has two explanations`**. Narration unchanged.

## What I did, so you can audit rather than trust it

- Copied `spec.json`, `audio/` (byte-identical, incl. `timeline.json` + `synthesis_receipt.json`),
  `sources/`, `subtitles.srt` from the predecessor. **No re-synthesis; no TTS spend.**
- Changed **only** `spec.json` → `short_title` and `candidate_filename`.
- Rendered with the **archived original renderer** `7d42ea80…` from `integrator/renderer-archive/`,
  under its recorded environment (python 3.11.15 / pillow 12.3.0 / ffmpeg 8.1.2), deliberately, so
  the only difference from `973daba3…` is the title text.
- Two independent renders produced the identical hash → deterministic.
- OCR at 20/70/120/170/210 s: corrected header on all five, presupposing form on none.
- First render inherited the predecessor's filename from `spec.candidate_filename`, producing a
  same-named MP4 with a different hash. I caught it, fixed the field, re-rendered, and **moved** the
  misnamed output to `rejected-attempts/` — not deleted.

## What is missing

`encoded_qa.json` · `QA.md` · `RECEIPT.json` · `POST_ENCODE_FREEZE.json` · `source_manifest.json` ·
`provenance_manifest.json` · contact sheets.

## Why I stopped rather than finishing it

1. **`provenance/qa.py` cannot run as-is.** It reads `build["renderer_path"]` for
   `renderer_snapshot_matches_build`. The archived renderer's receipt predates that field and emits
   only `renderer` / `renderer_sha256`. The renderer bytes **are** present at
   `provenance/render.py` and hash to `7d42ea80…`; only the receipt key is absent.
2. **I should not self-certify.** Hand-writing a freeze and a self-QA for my own build is precisely
   what the review layer exists to catch. The receipts should come from your tooling, not my
   assertions.

## Suggested approach — yours to overrule

**Preferred:** keep `c892f3fa…` and complete the receipts around it. That preserves the minimal-diff
property: this candidate differs from a hash three seats already reviewed by one line of header text
and nothing else. It needs `build_receipt.json` to carry `renderer_path: provenance/render.py`
(truthfully — the file is there and matches), plus the normal QA/manifest/freeze pass.

**Alternative you may prefer:** re-render under the current renderer so the packet is uniform with
the other three corrections. Cost: the diff versus `973daba3…` stops being title-only, since
`peak_curve`/`peak_plane` and other code changed after that build, so Tori and Kun would be
comparing against a broader change than the finding required.

Either way the header wording must survive, and `973daba3…` must stay untouched.

## Context you need

- **Tori has been dispatched on the four current hashes** (`reviews/TORI_CURRENT_HASH_DISPATCH_20260809T1330K.md`),
  including this one, with its incompleteness disclosed. If you complete the packet, its custody row
  becomes checkable on the same terms as the other three.
- If you re-render and the hash changes, **that dispatch goes stale** — tell Tori, and update the
  dispatch. That failure mode has already cost one round today
  (`reviews/HWAO_HASH_CORRECTION_20260809.md`; root cause corrected in
  `reviews/CLAUDE_ROOTCAUSE_NOTE_HASH_CORRECTION.md` — supersession, not a mid-write read).
- No seat has reviewed `c892f3fa…`. Kun's HOLD and Tori's PASS both describe `973daba3…`.

Gates unchanged: method-only, no `SOURCE_FREEZE.json` in this lane, `video_reportable_now` false,
no upload/cockpit/public/Git action. New versioned directory only; never rewrite a reviewed candidate.
