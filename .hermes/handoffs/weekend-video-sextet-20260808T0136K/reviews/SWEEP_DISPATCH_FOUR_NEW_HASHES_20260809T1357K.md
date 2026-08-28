# DISPATCH — Goru, Kun, Tori: the four CURRENT hashes (post title-fix)

Filed 2026-08-09 13:57 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"have goru, kun and tori review the four new hashes."*

Hwao retains coordination and accept/hold. Lana has already passed all four (`LANA_OVERHAUL.md`,
13:51 KST). This dispatch is for the three remaining domains.

## The four hashes — verified disk == freeze == QA at 13:56 KST

Per `HWAO_HASH_CORRECTION_20260809.md`, a watcher hash is not authority. Each was re-read from disk
and cross-checked against that lane's own `POST_ENCODE_FREEZE.json` and `encoded_qa.json`:

| lane | directory | SHA-256 | bytes | three-way |
|---|---|---|---|---|
| mzr-census | `…canary-20260809T0320K` | `d6014ac09636b106a197a9868c8f3a720c29b2015417c295849279a704e1061b` | 9,539,823 | **match**, QA PASS 28/28 |
| fesc | `…canary-20260809T1345K` | `acfb7fee70d5a131d4a44e8962cfe3fe3cd22104bf9cf8fa00bbbd6c2c00cbc0` | 10,056,847 | **match**, QA PASS 28/28 |
| brightend | `…canary-20260809T1345K` | `c772e6435af2298b3eac0eb772f406730c2240430a318a7f2268858f1b37cdb8` | 9,812,969 | **match**, QA PASS 28/28 |
| mzr-anchor | `…canary-20260809T1300K` | `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584` | 9,722,369 | **freeze and QA ABSENT — see below** |

## What changed since your last packets, per lane

Two separate fixes landed, in two waves. **Neither touched narration; no lane was re-synthesized.**

| lane | wave 1 — geometry/counts (overnight) | wave 2 — persistent title (13:45) |
|---|---|---|
| mzr-census | counts `178`/`21`/`157` removed, retained as `forbidden_terms` guards | none needed — its title is a thesis, not a presupposition |
| fesc | crossing curve geometry removed by renderer redesign (equal-height non-positional cards) | `A photon-budget mismatch has two explanations` → **`An apparent …`** |
| brightend | plotted marker removed; `EMPTY PLANE · NO DATA POINTS` | `An archival gap has two explanations` → **`An apparent …`** |
| mzr-anchor | n/a | `A metallicity offset has two explanations` → **`An apparent …`** |

Wave 2 originates from Kun's mzr-anchor claim-drift HOLD, which Duho ordered fixed and Lana then
generalised across the portfolio: a persistent header that presupposes the phenomenon while the
narration says "apparent" asserts what the voice withholds. Each wave-2 change is `short_title` only.

**Important for scoping your re-run:** `TORI_SIBLING_HWAO_FIX_REREVIEW.md` (13:48) passed
`47eb0d0b…` and `6e0f4b09…`. Those are the **pre-title-fix** fesc and brightend hashes, now
superseded by the two above. The geometry you cleared is unchanged; the delta is one header line.

## The mzr-anchor candidate is an INCOMPLETE PACKET — disclosed

`…1300K` was built by **this seat**, not the integrator, on Duho's instruction. Missing:
`encoded_qa.json`, `QA.md`, `RECEIPT.json`, `POST_ENCODE_FREEZE.json`, `source_manifest.json`,
`provenance_manifest.json`, contact sheets. It was rendered with the **archived original renderer**
`7d42ea80…` (deliberately, to keep the diff to the title alone), whose build receipt omits
`renderer_path`, a field `provenance/qa.py` requires. The integrator has been asked to complete it
(`integrator/COMPLETE_MZR_ANCHOR_PACKET_REQUEST.md`) and had not done so at dispatch time.

I did not hand-write the missing receipts: self-certifying my own build is what this review layer
exists to catch. **If you judge it too incomplete to review, hold it — that is a legitimate outcome.**

The two wave-2 candidates I built (`acfb7fee…`, `c772e643…`) **are** complete: rendered with the
shared renderer `71953059…` and passed through `qa.py`, so they carry the full receipt set.

## Per seat

**GORU** — mechanical timeline, state uniqueness, units/labels/citations, graphics share. Confirm the
wave-2 title change did not disturb state counts, section durations or graphics share; and that
mzr-census still shows zero renderer-supplied digits.

**KUN** — audio/sync/reproducibility. Audio is byte-identical to each predecessor (no re-synthesis),
so wpm and A/V deltas should be unchanged; verify rather than assume. Reproducibility: `acfb7fee…`
and `c772e643…` carry candidate-local `provenance/` snapshots; `c892f3fa…` carries only
`provenance/render.py` + `render_environment.json`, and its receipt lacks `renderer_path`.

**TORI** — actual encoded frames, claim boundary in pixels, source/status authority, closed gates,
prior-attempt preservation, playback. Your 1,389-frame sweep covered the geometry; the four hashes
above need the persistent chrome checked at full resolution on the new bytes.

## Standing constraints

No lane has a `SOURCE_FREEZE.json`; all four remain method-only, `video_reportable_now` false. Every
predecessor and rejected attempt is preserved; no frozen candidate was mutated. Routes: 8766 retired
at 02:07; 8765 currently serves the **spin** cut `c5e7deed…`, so no sibling has a live route and a
playback row needs one opened first.

Independent packets, append-only, preserve disagreements. A 28/28 machine QA is not semantic
authorization — the last two rounds proved that twice.

## Seat availability at dispatch, recorded honestly

| seat | pane | state |
|---|---|---|
| Goru | `%33` (`goru-agy`, Gemini 3.1 Pro) | idle at prompt — **note: session restarted 13:01, pane was `%3`** |
| Kun | `%25` (`kun-codex-overhaul`, gpt-5.5) | idle at prompt |
| Tori | `%23` (`tori-overhaul`, gpt-5.6-sol) | idle at prompt |
| integrator | `%24` (`yui-overhaul-integrator`) | idle — mzr-anchor packet request outstanding |

Dispatched by file. Nothing was pasted into any pane.
