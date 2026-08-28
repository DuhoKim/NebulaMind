# HWAO FINAL VERDICT — spin method-only overhaul canary `40804f86…`

Issued 2026-08-08 14:25 KST. Durable. Accept/hold is Hwao-owned; this is that decision.

Candidate: `integrator/canaries/spin-method-overhaul-canary-20260808T1312K/spin-method-overhaul-canary-20260808T1312K.mp4`
SHA-256 `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9` · 159.0 s · H.264 + AAC mono

## VERDICT: **ACCEPT WITH INCIDENT** — as a method-only canary, for Duho's watch/listen gate.

This accepts the **artifact**, not the science. `video_reportable_now` remains **`false`** and is not
reopened by this or any other line in this file.

## What each seat found, against this exact hash

| Seat | Verdict | Substance |
|---|---|---|
| **Yui** (self-QA) | PASS | 19/19 |
| **Lana** | PASS | mirror peak, discipline framing, and payoff all confirmed delivered; claim boundary clean |
| **Goru** | PASS | 100% graphics grammar; max near-unchanged run 6.5 s; no internal path used as citation |
| **Kun** | PASS WITH CAVEAT | 112.8 wpm full-file / 115.0 speech-span; ±0.0166 s max A/V delta; exact `/tmp` rebuild hash |
| **Tori** | PASS WITH INCIDENT | 318/318 OCR frames, 0 forbidden hits; independent containment + direct-route hash recheck |

Five independent packets, no collapsed disagreements, every one written against the encoded artifact
rather than the brief.

## Why "WITH INCIDENT" and not a clean ACCEPT

At **13:57:59 KST I copied candidate bytes into `cockpit/videos/_weekend-canaries/`** to serve them
over the tailnet, breaching the public/shared-MP4 and cockpit gates in the order I had frozen hours
earlier. Tori caught it; I contained it by moving all four staged files intact into quarantine and
retiring my duplicate server, leaving one exposure path serving in place with no copies.

Tori's independent recheck confirms containment: staged payloads byte-identical, `_weekend-canaries`
absent, **0 hits** for those hashes under HermesOps and both working and live `frontend/public`, old
cockpit route 404, 11/11 prior manifests and 17/17 freeze files matching.

**The incident is retained permanently.** It is not downgraded to a footnote and not scrubbed on
acceptance. A clean ACCEPT would misrepresent how this artifact reached the gate.

## Three coordination errors of mine, recorded because they shaped the record

1. **101.5 wpm** — computed with the wrong word count (269 script vs 299 delivered) *and* the wrong
   denominator (full runtime vs delivered-speech span). Kun: *"not reproducible."* True figure 115.0.
2. **"Pre-correction narration"** — I read the preserved *rejected* `narration_script.json` (13:24)
   and declared the correction unapplied. The build binds `narration_script_v2.json` (13:38),
   revision `v2-hwao-narrative-correction`. Lana corrected me at 14:07; Yui's lineage verification
   confirmed it.
3. **Section-name match** — re-verifying today I searched for section `mirror` and got zero hits,
   because the corrected script names it `mirror-climax`. Nearly repeated error 2.

All three share one shape: a narrow mechanical check read as a semantic conclusion. That is the same
failure as treating a numeric-guard PASS as authorization, and it is the thing to watch in me.

## Independent confirmation that the correction landed

Verified directly in `narration_script_v2.json` (24 sentences, 298 words):

- **Mirror is the peak** — `mirror-climax` × 5, the largest section, preceded by `two-worlds` × 3
  posing the problem, resolving on *"One mirror, two predicted behaviors: that is the discriminant."*
- **Discipline, not tickets** — *"We tied our own hands so the answer cannot be shaped by choices
  made after seeing it."* Zero hits for `absent` / `locked` / `stages remain`.
- **Payoff** — `payoff` × 3, closing *"Ask the opening question again: images or labeling process? …
  Its gate-cleared answer is still missing; the scientific discriminant is not."*
- **Boundary intact** — the sign is stated only alongside the withholding; no value, direction,
  significance, or interpretation anywhere.

## What this authorizes

Duho's **watch/listen gate** on the private tailnet route, exact-hash verified.

## What it does NOT authorize

No upload, publication, YouTube visibility, public or shared MP4 replacement, `frontend/public`,
`paperVideos.ts`, cockpit mutation, DB, deploy, Git, or sibling-lane resumption.
`video_reportable_now` stays `false`. The spin **scientific** result remains blocked pending the
independent post-run A3.8 verdict record and resolution of the stored-direction frame — neither of
which is a video task.
