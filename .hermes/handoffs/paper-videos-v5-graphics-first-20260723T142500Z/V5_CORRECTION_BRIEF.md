# V5 CORRECTION BRIEF — graphics-first paper videos (post-V4 rejection)

Author: Hwao (coordinator) · Written: 2026-07-24 KST · Lane: `paper-videos-v5-graphics-first-20260723T142500Z`
Receipt-only turn: no media, YouTube, website, DB, git, runtime, or cockpit action. Public z9 V4 (`m5RpYlUj79M`) visibility is untouched and stays untouched absent a separate explicit instruction.

## 1. Verdict and standing

- **z9 V4 is a failed creative reference despite full technical QA** (deterministic 15/15, visual 10/10, hash 11/11). Duho's rejection: hand gesture visibly repeats, voice/content do not cohere, too little graphical evidence. QA measured integrity, not comprehension — V5 adds gates for the latter.
- **The other four papers must NOT be built from the V4 template.** The V4 z9 spec (`paper-videos-v4-intro-plots-20260723T120045Z/V4_Z9_CANARY_SPEC.json`) is demoted to content-reference only: its *claims, anchors, and boundary text* remain valid (they passed G1 against the current freeze); its *presentation grammar* is superseded by this brief.
- Evidence base carried forward unchanged: `V4_SOURCE_FREEZE.json` + `sources-v4/` extracts and vector figure crops (z9 Fig 1 crop sha `8d1575a7…`), `G1_AFFECTED_CLAIMS_REGISTER.md` (claim verdicts), `G2_NARRATION_REWRITES.md` (corrected numbers for massive-abundance, scaling-relations, tng-validation).

## 2. Root causes (established, not to be re-litigated)

1. **Gesture loop:** one 144-frame gesture source bounce-looped across the full ~3-minute track — a visible metronome.
2. **Static slots:** every slot is a single static layout PNG; nothing on screen moves with the narration.
3. **Fake progression:** slots 4–6 repeat the same Figure 1 crop with only text changes — three "different" evidence beats that look identical.

## 3. V5 design principles (required direction, binding)

1. **Presenter minimized:** presenter C appears only in a short intro (≤15 s) and outro (≤10 s), OR hands are removed entirely (framing above wrists / static hero pose) during science scenes. No gesture animation may loop visibly: no animation cycle may appear more than twice in the video.
2. **Graphics dominate:** 70–80% of runtime shows real plots or source-grounded graphics as the primary panel. Presenter-primary time ≤20%.
3. **One visual action per sentence:** every spoken sentence triggers exactly one on-screen action — a highlight, zoom, reveal, annotation draw, or pan — cut to that sentence's audio timing. No sentence lands on a frozen frame; no action fires without its sentence.
4. **Slower, causal narration:** 105–125 WPM delivered (am_michael retained; pacing via narration length + inter-sentence gaps, with Kokoro speed adjustment only if the voice canary demands it). Sentences short and causal ("X, so Y"; "because A, B"). Target ≤115 spoken words/minute of runtime.
5. **Figure 1 progressively read, never repeated:** the actual frozen crop is staged as a sequence of deterministic view-states — axes orientation → local benchmark curves → red points reveal → the −0.69 dex gap annotated → anchor-swap emphasis → blue stacked square — each state a scripted crop/zoom/overlay of the same sha-verified vector render. No redraw, no invented geometry; every zoom is a coordinate window on the verified image.
6. **Conceptual graphics, source-grounded, labeled:** five required conceptual diagrams — (a) oxygen clock (enrichment tracks star-formation history), (b) unlensed-vs-lensed bias (differential magnification distorting mass), (c) benchmark choice (extrapolated vs measured local anchor), (d) stacked cross-check (many faint spectra → one measurement), (e) systematic budget (Te-scale 0.1–0.2 dex vs the measured deficit). Every non-data diagram carries a visible "CONCEPTUAL — illustration, not data" label. The only numbers allowed on any graphic are freeze-anchored values (cite `sources-v4/<key>.md` line in the spec); **no invented values anywhere**.
7. **Comprehension before animation:** a voice canary (pacing) and a cold-reader comprehension check must PASS before any new facial animation is generated. The exact-audio downstream rule stands: wording/speed changes after animation invalidate it, so animation comes last.

## 4. V5 scene grammar (per paper)

| Block | Runtime share | Content |
|---|---|---|
| Intro (presenter OK) | ~8–15 s | Question hook in plain language; presenter greets; no cover page (ban carried from V4). |
| Science block (presenter-free or hands-free) | 70–80% | Alternating conceptual diagrams and progressive real-figure reads per §3.5–3.6; one visual action per sentence; claims verbatim from the G1/G2-verified set. |
| Status boundary | ~15 s | Warning-styled; verbatim boundary text ("…descriptive, not validated… not a formal statistical detection"). |
| Outro (presenter OK) | ~8–10 s | Paper URL + boundary line. |

Spec format for the V5 canary: per-sentence storyboard rows — `sentence | start-end (s) | visual action | asset + view-state | anchor line` — replacing V4's per-slot static layout list.

## 5. Acceptance matrix (all must PASS; measured, not asserted)

| # | Criterion | Measure |
|---|---|---|
| A1 | Graphics dominance | Primary-panel classification per frame: plots/graphics ≥70% of runtime; presenter-primary ≤20% |
| A2 | No gesture loop | No animation cycle recurs >2×; science scenes presenter-free or hands out of frame |
| A3 | Sentence↔action lock | count(visual actions) == count(sentences); each action starts within ±0.3 s of its sentence |
| A4 | Pace | Delivered narration 105–125 WPM measured on the final audio |
| A5 | Progressive figure read | ≥5 distinct scripted view-states of Figure 1; no two evidence sentences share an identical frame |
| A6 | Conceptual labeling | Every non-data diagram bears the visible conceptual label; zero unanchored numbers on screen (each traced to a freeze line) |
| A7 | Content integrity | Claims byte-match the G1-confirmed/G2-rewritten set; boundary text verbatim; no cover page; no invented values |
| A8 | Technical carry-over | Audio==SRT==spec; labels ≥22 px at 2560×1440; identity/voice contract fields match `selection_v3.json` (speed change only if voice canary approves); duration ≤3:30 |
| A9 | Comprehension | Cold-reader gate passed before facial animation (see V5-G2) |

## 6. Gates (exact order; local, lane-only until Duho releases more)

- **V5-G1 — voice canary (NEXT GATE):** Tori builds ≤60 s of am_michael audio for the draft z9 V5 opening at target pacing; measure WPM; Duho ear-check. No animation, no video.
- **V5-G2 — cold-reader comprehension:** a reader/listener who has not seen the paper consumes the full draft script + storyboard (or audio + still storyboard animatic) and must correctly answer: what was measured, what the main figure shows, what the result is, what it does not claim. Fail ⇒ rewrite narration, repeat.
- **V5-G3 — motion-graphics canary (no faces):** the science block for z9 only — progressive Figure-1 read + 2 conceptual diagrams timed to real audio; verifies A1/A3/A5/A6 mechanically.
- **V5-G4 — full z9 V5 local canary:** add intro/outro presenter (animation now permitted, gesture-loop ban enforced); full acceptance matrix.
- **V5-G5 — Duho watch-and-approve. Then batch decision for the other four (using G2 rewrites); publication remains a separate explicit gate.**

**Exact next gate: V5-G1 voice canary, Tori, bounded to this lane, on Duho's release.**

Stop: this brief is the only artifact of this turn.

HWAO_V5_CORRECTION_BRIEF_COMPLETE
