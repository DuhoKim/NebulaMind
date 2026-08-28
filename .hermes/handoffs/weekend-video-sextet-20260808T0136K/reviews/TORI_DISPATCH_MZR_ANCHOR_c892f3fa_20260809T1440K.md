# DISPATCH — Tori: frame review of mzr-anchor `c892f3fa…`

Filed 2026-08-09 14:40 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"have tori review c892f3fa."*

Hwao retains coordination and accept/hold. This is the single open review its 14:36 amendment names:
board state for mzr-anchor is **HOLD pending review of `c892f3fa`** — *"not a defect finding, an
absence of review."*

## The artifact — verified three ways at 14:39 KST

| | |
|---|---|
| directory | `integrator/canaries/mzr-anchor-method-overhaul-canary-20260809T1406K/` |
| MP4 | `mzr-anchor-method-overhaul-canary-20260809T1406K.mp4` |
| SHA-256 | `c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584` |
| bytes | 9,722,369 |
| duration | 219.522 s |
| disk == freeze == encoded_qa | **True** |
| machine QA | PASS 28/28 |

Complete packet: `POST_ENCODE_FREEZE.json`, `encoded_qa.json`, `RECEIPT.json`, `source_manifest.json`,
`provenance_manifest.json`, contact sheets, candidate-local `provenance/`.

## What this candidate is, and what changed

It supersedes `973daba3…` (`0245K`), which you passed and which Kun and Lana then held on the
persistent title. **The only intended change is one line of header text:**

`A metallicity offset has two explanations` → **`An apparent metallicity offset has two explanations`**

Narration unchanged. Audio reused byte-identically. No geometry edits.

Two facts that may save you time:

1. **`1300K` and `1406K` are the same bytes.** `1300K` was this candidate mid-build and unfrozen;
   `1406K` is it frozen. Hwao's earlier exclusion of `1300K` and Lana's refusal to review it were both
   correct at the time and are now moot. Do not review `1300K`.
2. **Built twice with different renderers, byte-identical output** — once with the archived
   `7d42ea80…` and once with the shared `71953059…`. So the newer renderer's `peak_curve`/`peak_plane`
   changes do not affect this lane.

## Specifically worth your frames

Hwao's amendment is explicit that this is unreviewed, and that a text-level check is not enough:
*"zero curve icons is a text-level check, and text-level checks missed all three original findings.
It needs frames."*

1. **The fesc icon defect does not apply here on paper** — `spec.json` declares 8 icon primitives, all
   `anchor`, zero `curve`. Treat that as a claim to verify in pixels, not as evidence.
2. **The persistent header** at full resolution across the runtime — the change is the whole point of
   this candidate, and it is chrome, which is the surface that produced two of today's four findings.
3. **The peak** is the derivation chain (auroral flux → electron temperature → direct abundance →
   same-object mass → common scale). Confirm nothing in it acquires an order, location or magnitude.
4. Your usual rows: source/status authority as it stands, closed gates, prior-attempt preservation,
   private playback.

## Context

- `lanes/mzr-anchor/STATUS.json` remains `PENDING`, `SOURCE_FREEZE.json` absent. Method-only;
  `video_reportable_now` false. Absent freeze is not permission.
- `973daba3…` (`0245K`) is preserved untouched with its evidence.
- **Routes:** 8766 retired at 02:07; 8765 currently serves the **spin** cut `c5e7deed…`. No sibling has
  a live route, so a playback row needs one opened first.
- This candidate was built by **this seat**, not the integrator, on Duho's instruction. Its OCR and
  determinism claims above are mine and should be treated as claims to check.

Tori seat state at dispatch: `%23`, **idle at prompt**. Dispatched by file; nothing pasted into any pane.

Independent packet, append-only. A 28/28 machine QA is not semantic authorization.
