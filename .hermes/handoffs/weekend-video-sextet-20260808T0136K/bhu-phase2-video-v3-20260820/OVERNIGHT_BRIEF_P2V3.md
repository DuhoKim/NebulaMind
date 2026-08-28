# OVERNIGHT BRIEF — Phase 2 explainer v3 ("actually understandable, actually beautiful")

Tori (BHU coordinator), 2026-08-20 01:23 KST. Duho, verbatim (on v2): **"still, hard to
understand, and graphic quality too low. please fix that overnight leveraging all our
resources"**. This is a rebuild, not a patch: both failures named — comprehension AND visual
quality — must be fixed at the root. v2 (2ipNowvi-qo) stays up unlisted until Duho judges v3.

## Diagnosis targets (what "hard to understand" means to fix)

The v2 script passed claim gates but reads like a compressed paper summary spoken aloud:
long sentences carrying 2-3 ideas, technical terms defined once then reused densely, numbers
arriving faster than a listener can absorb, and panels that ASSERT findings rather than BUILD
them. High-school register means: one idea per beat; an analogy BEFORE every mechanism; a
term defined every time it matters, not once; numbers given with a felt comparison and TIME
to land; questions as connective tissue ("so does the baby remember the spin? here's how we
checked"). Target ~120-135 spoken wpm, 9-11 minutes, 14-16 panels.

## Visual quality bar (what "too low" means to fix)

v2 panels are deterministic chart-style frames. v3 gets a real design system: full-bleed
1920x1080, professional typography (large display headings, generous whitespace, consistent
grid), a coherent dark cosmic palette, animated builds (elements enter as narration mentions
them, not all at once), smooth highlight cursors on the paper plots, and — the big lever —
**generated illustration art via Nano Banana Pro** (the catalog's tool for legible
infographic text and high-quality stills) as panel backdrops and concept illustrations:
the spin-twist of spacetime, the bounce as a crushed-and-rebounding ball, the black-hole
nursery, the causality speed-limit, the helium fossil record. Duho's "leveraging all our
resources" authorizes this generation spend for this task; every generated image is logged
(prompt, timestamp) in assets_v3/GENERATION_LOG.md and pinned in assets_v3/PINS_V3.sha256.
Veo/Flow video clips are NOT used (hard per-decision credit rule; static art + programmatic
animation carries the quality). Paper plots stay authoritative and attributed; generated art
NEVER depicts data — it illustrates concepts only, and carries an "illustration" chip so no
viewer mistakes it for evidence.

## Chain (overnight, watcher-driven; gates as always)

- **A1 (claude-seat): COMPREHENSION_AUDIT.md** — panel-by-panel audit of v2's SCRIPT.md
  against the register above: where a high-schooler loses the thread (jargon density,
  missing analogy, idea-per-sentence count, number pacing), with a concrete rewrite
  direction per panel + the v3 panel plan (14-16 panels incl. splits). → CSEAT_A1_DONE.md
- **A2 (agy, parallel): DESIGN_SYSTEM.md** — the full visual language (type scale, grid,
  palette, animation vocabulary, plot-walkthrough style) + per-panel art briefs with EXACT
  Nano Banana Pro prompts (style-consistent, text-in-image only where legible-large) +
  layout spec per panel. → AGY_A2_DONE.md
- **B (gpt1): SCRIPT.md + STORYBOARD.json v3** per COMPREHENSION_AUDIT + DESIGN_SYSTEM;
  narration contract: <= 1600 words, panel 01 verdict-complete <= 80 words, analogy-first
  rule enforced per panel, all v2 ledger-repaired facts carried EXACTLY (the five repaired
  wordings are frozen facts: lined-up edge; the two-clause spin sentence; 10,000-100,000x
  range; branch clause; 10,000x floor-true heading). → GPT1_B_DONE.md
- **C (Tori, in-session Chrome): generate the art** per A2's briefs via Nano Banana Pro;
  gentle pacing; log + pin every image; an auth wall is a report, not a puzzle — fallback
  if generation is unavailable: agy-specced programmatic illustrations, noted honestly.
- **D (claude-seat): CLAIM_LEDGER.md v3** — full re-ledger (narration + on-screen + art
  briefs; generated art must assert nothing beyond its illustration chip). → CSEAT_D_DONE.md
- **E (kimi): packet gate** → KIMI_P2V3_PACKET_GATE.md / PASS_P2V3_PACKET
- **F (gpt3): build** — new design system implemented; animated builds; 1080p; gateway TTS
  at a measured pace (target wpm above; insert breathing pauses at panel turns); full-mp4
  ASR QA. → GPT3_F_DONE.md / BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.mp4
- **G (kimi): render gate, BOUNDED (12-min budget, stored-ASR audit, max 6 frame pulls —
  must include 2 generated-art panels for the illustration chip + legibility)** →
  KIMI_P2V3_RENDER_GATE.md / PASS_P2V3_RENDER
- **H (Tori): registry-checked unlisted upload (bhu-phase2-results-v3), server-verify,
  events, morning report.** v2 retirement is DUHO'S call in the morning, not tonight's.

## Standing rules (all carry)

No scope disclaimer. Must-not-say list. Frozen repaired wordings above. Only the three
permitted equations on screen. Labeled band ladders, Planck markers, honest no-plots cards.
Paper figures attributed; generated art chipped "illustration". Caveat sentence mid-video,
verdict first and last. Writes in this lane; never portal.nersc.gov; wallet floor $10;
gates one-shot kimi; ASR contract-bearing residuals unacceptable.
