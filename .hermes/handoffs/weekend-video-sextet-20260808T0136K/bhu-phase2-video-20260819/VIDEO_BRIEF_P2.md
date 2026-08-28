# PLATOON BRIEF — Phase 2 results video ("the chain on trial, and the ceiling")

Tori (BHU coordinator), 2026-08-19 17:2x KST. Duho, verbatim: **"go ahead with the phase 2
video"** (17:1x KST, after the gated Phase 2 verdict was reported). Fourth video in the
series; upload unlisted to NebulaMind after the render gate, per the standing rule and the
three-for-three precedent (v2 explainer, theory-closure, phase-1 results).

Scope label from frame zero: BHU cosmology is Duho's personal side-interest, not a
NebulaMind research programme.

## The story (two acts + a verdict)

**Act 1 — the chain on trial.** Four published papers carry the "our universe was born
inside a black hole" bounce story. We audited them equation by equation overnight — 77
verdict rows — and the chain testifies against itself: (a) the sequel paper disavows the
original's foundation in print ("not self-consistent", "violates the cosmological
principle") — the two bounce mechanisms disagree by a factor of ~730 on how dense the
bounce is, and they cannot both be true; (b) the averaging step the whole torsion number
rests on is derived in NEITHER paper — choosing it one way or the other swings the answer
by a factor of 6; (c) the one correction notice that might fix a broken number exists in
the journal record but its content sits behind a wall no permitted host can read — so we
recomputed every quarantined number ourselves; (d) across all four papers, the parent black
hole's SPIN — the thing the whole axis story needs — appears in exactly ONE sentence, with
no equation. The inheritance story the axis question needs was never written down.

**Act 2 — the strict chain.** So we derived it ourselves, receipts at every step: the
torsion density re-derived as an honest bracket (the published number reproduces at one
edge, 2.6% in); then the piece that exists nowhere in print — a CEILING on inheritance:
demand the published bounce of a spinning parent and self-consistency caps the inherited
spin fraction at about 10⁻²⁷ (conserving it outright would overshoot causality by a factor
of 6.6×10²⁶); and a frozen-ratio theorem — lopsidedness and torsion dilute at exactly the
same rate through the bounce, so the bounce performs ZERO ironing-out: it cannot create an
axis memory and it cannot erase one; that question stays hostage to a step the papers
assert but never derive. Confrontation: our bracket clears the published BBN bound by 45
orders of magnitude — consistent, and therefore invisible; stacking every generosity, the
sky-signal ceiling lands at about 10⁻⁵ of what counting EVERY galaxy in the observable
universe could ever detect.

**Verdict to end on:** the strongest version of the inheritance story now exists on the
record — as a ceiling — and the ceiling says the route stays closed. Asked through the
published chain, the axis question answers: nothing observable. That is what taking an
idea seriously looks like — twice now.

## Authorities (all local, all gated today)

`../bhu-theory-phase2-20260819/`: PHASE2_SUMMARY.md (fastest map; sha 8fe04976…),
TRACK_A1_AUDIT.md, TRACK_A2_AUDIT.md, P2_DERIVATION_BOUNCE.md, P2_DERIVATION_INHERITANCE.md,
P2_CONFRONTATION.md + the four PASS gate files. Phase 1 lane for the ε/f_b spec context and
format precedent; ../bhu-phase1-video-20260819/ for schema/build templates. The summary's
Reading-1 conditionality sentence travels with the ceiling wherever it is stated.

## Content rules (inherited from the phase-1 video brief, all still binding)

- Accessibility bar: plain-words comparisons first; equations on screen only where they ARE
  the story — here: the fork (w = +1 vs w = −1, the two incompatible bounces), a⁻⁶ = a⁻⁶
  (the frozen ratio), and ε ≤ 10⁻²⁷ (the ceiling). Narration stays equation-free. Numbers
  as digits.
- Must-not-say: "BHU is false/impossible"; "we proved the idea wrong" (we audited one
  published chain and bounded one route); no "Smolin refuted" import. Attack the claims,
  never the author — all four papers are one author's chain, so extra care: cite arXiv ids
  / journal refs, keep it clinical, no name-mockery. The incompatibility finding is the
  PAPERS' own words — quote them as such.
- One honest caveat sentence mid-video (not the ending): the erratum's content remains
  unread (paywall) with our recomputations in its place, and the strict chain awaits
  external theorist review before any publication claim.
- Structure contract: verdict complete ≤35 s; assertion heading per panel; no divider
  cards; end on the verdict; 4–6 min; ≤730 narration words; panel 01 ≤72 words.
- Magnitude visuals honest: the ×730 fork gap, the 45-order BBN margin, the 6.6×10²⁶
  causality overshoot, and the 10⁻⁵-of-the-floor gap all use labeled ladders/steps — no
  unlabeled log compression. The "counting every galaxy" floor must be named as the
  theoretical best, not an instrument.
- The Planck-regime caveat (V1) appears where a bounce state is drawn: both bounces sit
  at/above the Planck scale treated classically.

## Chain (platoon per the reform — engine names; fresh kimi one-shot per gate; grep-only,
time-boxed gates)

1. **gpt1** (hermes profile yui) — SCRIPT.md + STORYBOARD.json (schema
   nebula-explainer-storyboard-v1 per ../bhu-phase1-video-20260819 templates) →
   GPT1_DONE.md / GPT1_P2V_COMPLETE
2. **claude-seat** (cseat1) — CLAIM_LEDGER.md: every narration/on-screen claim bound to its
   gated artifact + line; definitional pins if needed → CSEAT_DONE.md / CSEAT_P2V_COMPLETE
3. **agy** — VISUALS.md: the four-papers-one-sentence visual, the ×730 fork ladder, the ×6
   averaging swing, the walled-erratum card, the ceiling dial with the causality overshoot,
   the a⁻⁶ = a⁻⁶ frozen-ratio scale, the 45-order BBN ladder, the all-galaxies floor tiling
   → AGY_DONE.md / AGY_P2V_COMPLETE; claim-bearing additions flagged for claude-seat review
4. **kimi** — packet gate → KIMI_P2V_PACKET_GATE.md / PASS_P2V_PACKET
5. **gpt3** (hermes profile tori3, new window bhu-gpt3) — build/ (adapt
   ../bhu-phase1-video-20260819/build/; output BHU_PHASE2_RESULTS_VIDEO_LOCAL_REVIEW.mp4;
   gateway TTS; full ASR QA; freeze) → GPT3_DONE.md / GPT3_P2V_COMPLETE
6. **kimi** — render gate → KIMI_P2V_RENDER_GATE.md / PASS_P2V_RENDER
7. **Tori** — registry check (cockpit/videos/published.json) then unlisted upload to
   NebulaMind, server-verified; dashboard event; report to Duho.

Boundaries: local pipeline until upload; gateway TTS/ASR only (no Flow/Veo credits — none
authorized and none needed); writes in this lane only; never portal.nersc.gov; catalog
notes honored (gpt2 busy with Hwao's transport builder — not used; Fable cap 61% — claude-seat
gets only the ledger step).
