# HWAO ORDER — FROZEN. Spin method-only presentation overhaul.

Issued 2026-08-08 13:02 KST against `USER_DIRECTION_OVERHAUL_20260808T1258K.md`.
**This order supersedes `METHOD_ONLY_PATTERN.md` for the spin lane and pauses all sibling video work.**

## 0. What Duho actually rejected

> still without audio, it looks almost same as before. i want you to overhaul the video leveraging
> sextet making more scientific presentation.

He watched **`spin-method-canary-20260808T0204`** and rejected **the presentation grammar itself** —
static cards with a heading and a paragraph.

Provenance corrected 2026-08-08 13:25 KST (`reviews/TORI_USER_WATCHED_ARTIFACT_CORRECTION.md`).
My first version of this order named `0648`; that was wrong. The watched file is 0204 — SHA-256
`2b1db4974f9830161015828ae44bb617345db476375204f5f079a7fd0485ccc1`, 114.0 s, 1,943,640 B,
video-only — re-verified byte-for-byte against disk by Hwao. `0648` is a **later supplemental
iteration**, admissible only as evidence that nine refinements never escaped the template.

The two share the same 11-card skeleton (0648 reworked only card 05), which is why the diagnosis
survives the correction unchanged — but a review must say which artefact it judged.
So this is not another pass on the same base. **The 11-card layout is not the starting point.**

Read that as a correction of my coordination, not of the seats: I kept authorizing refinements of a
form that was already rejected.

## 1. Immediate stops

1. **Sibling batching halts at the next safe command boundary.** `mzr-census-method-canary-20260808T1254`
   and `fesc-method-canary-20260808T1259` are **preserved as diagnostic baselines** — not deleted,
   not advanced, not shown as candidates. brightend and mzr-anchor are not started.
2. `spin-method-canary-20260808T0648` is **NOT presentation-final**. Diagnostic baseline only.
3. No sibling work resumes until the new spin canary passes Sextet review **and** Duho's
   watch/listen gate.

## 2. Audio — newly authorized, narrowly

Duho's complaint that it is "still without audio" is **explicit authorization to narrate this
method-only cut**. `lanes/spin/STATUS.json` previously read `audio_contract: silent; narration/TTS
not authorized`; that restriction is lifted **for method-only claims only**.

It does **not** touch scientific reportability. `video_reportable_now` stays `false` and
`BLOCK_SUBSTANTIVE_RESULT_RENDER` stands.

- Narrator **Alloy**, speed **1.18** unless a short exact-passage probe proves better.
- No music. **105–125 delivered wpm.**
- Sentence-aligned synthesis; **visual action boundaries derived from actual audio durations**, not
  guessed. Every substantive sentence gets a visual action starting within **±0.3 s**.
- Final MP4 must carry a **verified** audio stream, intelligible loudness, no clipping.

## 3. Banned grammar — a candidate carrying any of these is rejected on sight

- No presenter/character still.
- No giant standalone-number card.
- No paragraph/status/quote card as the dominant visual.
- **No internal filenames as audience citations.** `T1_FUNNEL.json` means nothing to a viewer;
  cite the survey and release.
- No long frozen holds with decorative zoom.
- No reuse of the 11-card layout as a base.

## 4. Required — conference-science grammar

1. Concise title + **one-sentence scientific question**.
2. **Continuously animated sample-funnel**, counts attached to labelled stages — not a number card.
3. **Progressive equation construction**: `N_CW`, `N_ACW`, numerator, denominator, sign — and
   explicitly withhold the value.
4. **Real mirroring animation**: one source image/schematic transforms, label inverts. Mark
   `CONCEPTUAL — illustration, not data` if generated.
5. **Bias-control matrix/flow**: each predeclared control and the failure mode it tests. Design
   only, **no outcomes**.
6. **Review-gate timeline/lock diagram** explaining precisely why the result is absent.
7. **Boundary slide**: what is known, what is not reportable, the exact next scientific gate.

**≥75% of runtime** source-grounded plots/diagrams/animated graphics. **≥7 materially distinct
visual states.** Progressive builds, wipes, reveals, highlights semantically aligned to narration.
**No unchanged state longer than ~8 s.**

## 5. Claim boundary — unchanged and absolute

**Allowed:** frozen source/sample funnel · symbolic asymmetry equation with **no result value** ·
handedness/mirroring convention · predeclared bias-control design · explicit unresolved-result
boundary.

**Forbidden:** T3/T4 result numbers or figures · significance · dipole/parity/cosmology ·
GRB/SN Ia/dark-energy/quasar/H0 · black-hole-universe · new DESI/Ganalyzer claims.

## 6. Sextet — dispatched independently, packets preserved before integration

| Seat | Charge | Packet |
|---|---|---|
| **Hwao/Fable** | freeze this order, stop siblings, coordinate, accept or hold the candidate | this file |
| **Lana** | scientific narrative + claim-boundary review | `reviews/LANA_OVERHAUL.md` |
| **Goru** | mechanical timeline, visual-state uniqueness, units/labels/citations | `reviews/GORU_OVERHAUL.md` |
| **Kun** | reproducibility, rendering implementation, audio/action sync, encoded-artifact checks | `reviews/KUN_OVERHAUL.md` |
| **Tori** | source-status receipt, actual-frame verification, gate enforcement, private playback | `reviews/TORI_OVERHAUL.md` |
| **Yui** | representation design + isolated candidate build | `integrator/canaries/<new>/` |

**Writer transfer, 2026-08-08 13:12 KST.** The `yui-video-integration` (Fable) seat hit its Fable 5
limit before starting this build. Its write authority is **revoked**; it is idle and read-only. The
single candidate writer is now **`yui-overhaul-integrator`** (existing `yui` Hermes profile,
non-Fable, rooted at `integrator/`). No credits were bought and no provider config changed.

**Reviews must inspect the actual prior contact sheet and MP4**, not just this brief — the rejected
grammar has to be seen to be avoided. Independent packets are preserved **before** integration; do
not collapse disagreements.

**The isolated integrator remains the only candidate writer.**

## 7. Closed gates

No upload, publication, YouTube visibility, public/shared MP4 replacement, `frontend/public/videos`,
`paperVideos.ts`, cockpit, DB/SQL, deploy/restart, **Git writes**, browser automation,
billing/provider/config, secrets, or **deletion of any prior attempt**.

Output only to a **new versioned directory** under `integrator/canaries/`.
