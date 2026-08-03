# Video Brief — "How the topics were picked" (in-section clip)
**For:** Yui (Flow) · **Requested by:** Duho (2026-07-17) · **Status:** ready to produce
**Purpose:** a short looping clip that sits in the **Topic tab** of lab.nebulamind.net, in the
"How the research topics were picked" panel — it replaces the native SVG diagram currently in the
`cfg-viz` slot (`frontend/src/app/lab/LabStages.tsx`). Claude Code self-hosts the MP4 and wires it in.

## Concept
An ~8-second **silent, looping** infographic clip that animates the derivation the panel describes in text:
**12,000 papers → embed → 32 clusters → ranked frontiers**. Pure data-motion, **no people, no cosmic
footage, no narration** — it plays muted-autoplay-loop under the step list, so it must read at a glance and
loop seamlessly. Legible on-screen labels via **Nano Banana Pro** (not Veo text).

## Visual system (match the Lab section exactly)
- Background `#0a0d17`; dots/ink `#9aa3b8`; accent (indigo) `#7c86ff`; accent-2 (teal) `#4ad6c4`;
  cluster tints `#7c86ff / #4ad6c4 / #e0a458 / #f47272 / #8b93c9`.
- Monospace for the four labels. Calm, precise motion; slow drift; no flares. Loop must return to frame 1.

## Beats (~8s, left-to-right flow, mirrors the on-page SVG)
| t (s) | Motion | Label (Nano Banana Pro, mono) |
|---|---|---|
| 0–2 | A tidy grid of ~30 paper-glyphs streams in from the left into a dark field | `12,000 papers` |
| 2–4 | Each paper collapses into a glowing point; points drift apart into a loose 2-D scatter | `embed → vectors` |
| 4–6 | The scatter self-organizes: points migrate into ~5 distinct colored clusters | `32 clusters` |
| 6–8 | Clusters reflow into a stack of ranked horizontal bars; the top three brighten (the frontiers) | `ranked frontiers` |
| loop | Hold ~0.3s, then dissolve back to the paper grid so it loops seamlessly | — |

## Production notes
- Model: **Omni Flash / Veo** for the dot-field motion only. The four labels are **Nano Banana Pro** frames
  composited as ingredients — never Veo-rendered text.
- Aspect **16:9**, but the action is a **wide horizontal band** (the slot is short/wide); keep the four stages
  spread left→right and the vertical center clear so it reads in a short crop.
- **Silent. Seamless loop.** No music, no VO, no subtitles/lower-thirds/logos/watermarks.
- 8s / 1x to stay on the current low cost gate. All numbers are real: `12,000` · `32`.
- Consistent with the series: same palette/typography as the methodology & pipeline explainer briefs
  (`frontier-methodology-explainer-brief.md`, `lab-pipeline-explainer-brief.md`), but no character here.

## Deliverables → hand back to Claude Code
- Primary: **MP4** (H.264, silent), 16:9, ~8s, seamless loop.
- Nice-to-have: a **WebM/VP9** copy (smaller, for browsers) + a **poster still** (frame 1, PNG).
- I self-host these in the frontend `public/` and swap them into the `cfg-viz` slot as a muted
  autoplay-loop `<video poster=…>` in place of the SVG, then redeploy. No external host (CSP-safe).

## ⚠️ Human step + current block
- Flow local-file/reference attach goes through the macOS file dialog — an agent can't drive it (Chrome
  automation is TCC-blocked). Yui needs Duho to attach the Nano Banana Pro label ingredients + enable
  "Create", then reply the trigger phrase.
- **Currently blocked:** Video-2 is `HOLD_ALL_TICKS_NO_SUBMIT` (Chrome Apple-Events control-plane failure).
  Queue this behind Video-2 / until the browser control plane recovers; it needs no account action to author.
