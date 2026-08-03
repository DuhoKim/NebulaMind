# Video Brief — "NebulaMind Lab: a machine that reads a whole field"
**For:** Yui (Flow) · **Requested by:** Duho (2026-07-17) · **Status:** ready to produce
**Purpose:** the hero explainer embedded on **lab.nebulamind.net** (the Lab site). Broader than the
[frontier-methodology brief](./frontier-methodology-explainer-brief.md) — that one is *just* the derivation;
this one walks the **whole pipeline**: map → topic/data/research/paper → run → AASTeX → review-revise.

## Concept
A ~60s informative explainer of the full NebulaMind Lab pipeline, for the Lab landing page. **Informative,
not cosmic** (Duho's standing note): on-screen infographics carry the message; any cosmic footage is a dim
backdrop only. Styled to the Lab's own palette so it feels native embedded on the page.

## Visual system (match the Lab site exactly)
- Background `#0a0d17`; panels `#111524`; ink `#e8ecf5`; muted `#9aa3b8`; hairlines `#242a3d`.
- Accent (indigo) `#7c86ff`; accent-2 (teal) `#4ad6c4`. Gradient headline = indigo→teal.
- Type: clean sans for headings; **monospace for all data/labels** (counts, scores, arrows) — reads as "instrument readout."
- Motion: calm, precise, technical. No lens flares. Arrows and counters animate; the dot-field drifts slowly.

## Narration script (lock the same VO voice as the methodology video, for series consistency; ~60s)
1. "NebulaMind Lab is an autonomous galaxy-evolution researcher."
2. "It begins by reading the field — twelve thousand refereed papers from NASA ADS."
3. "Every abstract becomes a vector; clustering sorts the field into thirty-two topics, with no human labeling."
4. "Overlay two hundred seventy-eight open debates from the review literature, and rank by where open questions concentrate — and how fast a topic is growing."
5. "The unsettled frontiers rise to the top: simulations versus physics, the JWST high-redshift frontier, cosmic chemical evolution."
6. "For each, the Lab runs a real study on public data — SDSS, JWST, and IllustrisTNG."
7. "It drafts an AASTeX paper, then hardens it against an automated referee that reviews and revises until the science holds."
8. "The idea — turning a body of papers into knowledge — is adopted from Astro-Note AI, by Suk Kim."
9. "A machine that reads a whole field, and works its open questions. NebulaMind Lab."

## Storyboard (10 beats · legible text via **Nano Banana Pro**, NOT Veo text)
| Beat | ~sec | Visual | On-screen text (mono) |
|---|---|---|---|
| 1 | 0–5 | Title card; dark dot-field drifts in; gradient wordmark | **NebulaMind Lab** / "autonomous galaxy-evolution research" |
| 2 | 5–12 | Papers stream into a funnel labeled NASA ADS | `12,000 papers · astro-ph.GA · 2016–2026` |
| 3 | 12–19 | Each paper → glowing point; points drift into a 2-D cloud | `abstract → embedding` |
| 4 | 19–25 | Cloud condenses into 32 tinted clusters | `32 topics · self-organized` |
| 5 | 25–33 | Red debate-markers + "?" rain on clusters; bars rank them | `278 debates · rank = open-Q density × growth` |
| 6 | 33–40 | Top-3 frontiers light up on the ranked bars | `Simulations vs physics · JWST high-z · Chemical evolution` |
| 7 | 40–47 | Pipeline row slides in: topic → data → research → paper; data glyphs SDSS/JWST/TNG | `SDSS · JWST · IllustrisTNG` |
| 8 | 47–54 | A page assembles; arrows loop review → revise → **ACCEPT** | `AASTeX PDF · review → revise → accept` |
| 9 | 54–58 | Credit card | `method after Astro-Note AI · Suk Kim` |
| 10 | 58–62 | End card, wordmark + URL | **lab.nebulamind.net** |

## Character (optional — reuse for series consistency)
Reuse the "research cartographer" from the methodology video (lock the same reference frame as an Ingredient).
Appears only in beats 1 and 10; infographics carry 2–9. Skip entirely if we want a pure-infographic cut.

## Production notes
- Model: **Omni Flash** (Ingredients-to-Video for character consistency). All text-bearing frames (beats 1–2, 4–10)
  rendered in **Nano Banana Pro** for legible text, composited as ingredients — never rely on Veo to render text.
- Aspect **16:9** primary (web hero). Also export a **9:16** cut for social if easy.
- **Also export a 10–15s silent 16:9 loop** (beats 3→7, minimal/no text) — optional muted-autoplay hero background.
- Narration: dubbed VO, **same voice** as the methodology video (series consistency).
- All numbers are real/verified: `12,000` · `32` · `278` · `200` · frontier ranking · SDSS/JWST/TNG · AASTeX · astrosage-70b referee.

## Web embedding plan (my side, once Yui delivers the MP4)
- Preferred: **self-host** the final MP4 in the frontend `public/` and add a click-to-play (poster-framed) `<video>`
  to the Lab hero — no external host, CSP-safe. If a muted-autoplay loop is wanted, use the silent 10–15s cut.
- Alternative: **YouTube — UNLISTED only** (per standing policy) embedded via privacy-enhanced iframe, unless Duho okays public per-video.
- Hand the finished MP4 (+ optional silent loop) back to me and I'll wire it into `lab/page.tsx` and redeploy.

## ⚠️ Human step required (same as video-1 / methodology video)
Flow's local-file / reference attach goes through the macOS file dialog — an agent can't drive it (Chrome
automation is TCC-blocked on this host). Yui will need **Duho** to attach the reference frame + the Nano Banana Pro
infographic ingredients, enable "Create," then reply the trigger phrase — exactly as with the earlier videos.
