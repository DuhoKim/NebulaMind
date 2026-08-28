# DISPATCH — Tori: review the four CURRENT hashes

Filed 2026-08-09 13:30 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"have tori review the four current hashes."*

Hwao retains coordination and accept/hold. This conveys the instruction and the verified inputs.

## Why this dispatch exists

Your `TORI_SIBLING_ROLLOUT.md` work is thorough and its findings are **confirmed correct** — Lana
reached the counts finding independently, and your fesc/brightend HOLDs match hers from decoded
pixels. But every artifact you have reviewed has since been **superseded**. Each of your findings is
already addressed in a candidate you have not seen.

| lane | you reviewed | verdict | current candidate | what changed |
|---|---|---|---|---|
| mzr-census | `0496435a…` | HOLD (counts at ~109–130 s) | **`d6014ac0…`** | `178`/`21`/`157` removed from narration and pixels; retained as `forbidden_terms` guards; stages kept symbolic |
| fesc | `b9003831…` | HOLD (visible crossing) | **`47eb0d0b…`** | ordered/crossing curve geometry removed by renderer redesign — equal-height non-positional arms; also re-rendered for loudness |
| brightend | `9a137c61…` | HOLD (outcome-bearing mark) | **`6e0f4b09…`** | moving marker removed; `EMPTY PLANE · NO DATA POINTS`; provenance animation terminates outside the axes |
| mzr-anchor | `973daba3…` | PASS (reaffirmed) | **`c892f3fa…`** | persistent header `A metallicity offset has two explanations` → `An apparent metallicity offset has two explanations` |

## Hashes — verified against disk AND each lane's own freeze before dispatch

Per `HWAO_HASH_CORRECTION_20260809.md`, a watcher hash is not authority. Each was re-read from disk
at 13:29 KST and cross-checked against that lane's `POST_ENCODE_FREEZE.json` and `encoded_qa.json`:

| lane | SHA-256 | bytes | disk == freeze == QA |
|---|---|---|---|
| mzr-census | `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` | 9,539,823 | **yes**, QA PASS 28/28 |
| fesc | `47eb0d0b151b51667a4b29a39da74b947086c925dda7ce7e819240ffde25e42d` | 9,998,675 | **yes**, QA PASS 28/28 |
| brightend | `6e0f4b098d6c5386d08ab7fb670b8b6564e257edeac5dc1c6fec2cc6b97bc7b4` | 9,747,250 | **yes**, QA PASS 28/28 |
| mzr-anchor | `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584` | 9,722,369 | **NO — see below** |

Directories: `integrator/canaries/{mzr-census…0320K, fesc…0327K, brightend…0337K, mzr-anchor…1300K}`.

## The fourth candidate is an INCOMPLETE PACKET — disclosed, not hidden

`mzr-anchor…1300K` was built by **this seat**, not the integrator, on Duho's instruction
*"fix the title card and rebuild"*, addressing Kun's claim-drift HOLD. It is **not packet-complete**
and your custody row will legitimately differ from the other three:

**Present:** MP4, `spec.json`, `audio/` (byte-identical copy, incl. `timeline.json` and
`synthesis_receipt.json`), `sources/`, `subtitles.srt`, `numeric_guard.json`, `build_receipt.json`,
`provenance/render.py` + `render_environment.json`, `CORRECTION.json`, `PREDECESSOR.json`,
`rejected-attempts/`.

**Absent:** `encoded_qa.json`, `QA.md`, `RECEIPT.json`, `POST_ENCODE_FREEZE.json`,
`source_manifest.json`, `provenance_manifest.json`, contact sheets.

Reason: it was rendered with the **archived original renderer** `7d42ea80…` (deliberately, to keep
the diff to the title alone), whose `build_receipt.json` does not emit `renderer_path` — a field the
corrections' `provenance/qa.py` requires. I did not hand-write the missing receipts, because
fabricating a freeze and a self-QA for my own build is exactly the kind of self-certification this
review layer exists to catch.

**What I did verify:** OCR of five frames sampled across the runtime (20/70/120/170/210 s) shows the
corrected header on every one and the presupposing form on none; two independent renders produced the
identical hash, so the build is deterministic; narration is unchanged and audio was reused
byte-identically; predecessor `973daba3…` re-verified untouched.

Treat that as a claim to check, not evidence. If you judge the packet too incomplete to review, say
so and hold it — that is a legitimate outcome and the integrator can complete the packet properly.

## Your charge, unchanged

Actual encoded-frame decode and OCR, claim-boundary in pixels, source/status authority as it stands
at review time, closed gates, prior-attempt preservation, private playback.

Specifically worth your attention:

1. **mzr-census** — confirm the three counts are gone from *pixels*, not just narration; your earlier
   finding located them at ~109.25–129.75 s.
2. **fesc** — the peak is now non-positional cards. Confirm no relative height, slope, ordering or
   crossing survives; Lana ruled that a `WITHHELD` label alone is insufficient.
3. **brightend** — confirm no mark acquires an outcome-bearing location anywhere in the plane.
4. **mzr-anchor** — the header wording is the only intended change from a hash you already passed.
5. **Routes:** 8766 was retired at 02:07; 8765 currently serves the **spin** cut `c5e7deed…`, not any
   sibling. No sibling has a live route, so a playback row needs one opened first.

None of the four lanes has a `SOURCE_FREEZE.json`; all remain method-only, `video_reportable_now`
false. Independent packet, append-only, preserve disagreements. A 28/28 machine QA is not semantic
authorization — you have demonstrated that twice tonight.
