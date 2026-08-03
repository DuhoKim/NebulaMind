# Hwao video plan — overnight report video

Source brief: `HWAO_SOURCE_BRIEF.md` (marker `OVERNIGHT_REPORT_VIDEO_SOURCE_BRIEF_20260722`)
Evidence anchors: live feed marker `GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE`, frozen at `2026-07-22T02:25:43Z` (= 2026-07-22 11:25:43 KST); canonical constructor `tools/render_ge_autopilot_dashboard_v2.py:1265-1304` (verified read-only — all stable facts below match it, including "won a 10-model citation-retrieval eval", line 1286).

Scope: plan only. No production code, cockpit, DB, site, git, or video-asset edits. This file is the sole deliverable.

## 1. Contract restate + timing

Status-update / overnight-report explainer. 73.5 s, six scenes, 1280×720 @ 24 fps → **1764 frames exactly**, all scene cuts on integer frames. Same established female astronomer presenter and female narration voice as the accepted series. Exact final narration is locked first, then drives facial animation, mix, and SRT. Deterministic Pillow + ffmpeg charts/labels over reused atmospheric footage. Local review master only.

| # | Scene | Sec | Frames | Words | wps |
|---|-------|-----|--------|-------|-----|
| 1 | Overnight outcome | 10.5 | 252 | 23 | 2.2 |
| 2 | Corpus | 13.0 | 312 | 34 | 2.6 |
| 3 | Frontier map | 12.5 | 300 | 31 | 2.5 |
| 4 | Retrieval + grounding | 12.0 | 288 | 30 | 2.5 |
| 5 | Three gates | 14.5 | 348 | 37 | 2.6 |
| 6 | Honest handoff | 11.0 | 264 | 28 | 2.5 |
| — | **Total** | **73.5** | **1764** | **183** | **2.5 (~149 wpm)** |

Pacing rule: narration audio per scene ends ≥0.7 s before its cut (breath room for the facial animation and SRT readability). If the final TTS take for any scene overruns its slot, trim the narration text — never the scene duration; the 73.5 s / 1764-frame total is fixed.

## 2. Final six-scene narration

Numbers policy: speech uses rounded forms ("over…", "nearly…", "about…") for pace; the on-screen graphic always carries the exact figure. Every sentence traces to a frozen feed fact (§4 table).

**Scene 1 — Overnight outcome (10.5 s)**
> Overnight, the autopilot built the full AI-Scientist corpus foundation — and all three quality gates. Not a paper. The foundation first, by design.

**Scene 2 — Corpus (13.0 s)**
> The foundation: over one hundred twenty thousand papers embedded — galaxies and cosmology, 2009 through 2026. The embedding model won a ten-model retrieval evaluation, and the new index is about ten times the old corpus.

**Scene 3 — Frontier map (12.5 s)**
> Fifty-seven research topics were derived from scratch, then ranked by recent citation inflow over eight point nine million citation edges. JWST high-redshift galaxy evolution is first — by a wide margin.

**Scene 4 — Retrieval + grounding (12.0 s)**
> Retrieval runs on the local corpus and deep-reads each working set in full text. The canonical layer: nearly five thousand top-cited papers, ninety-six percent in clean HTML.

**Scene 5 — Three gates (14.5 s)**
> Between an idea and a paper now stand three gates. Novelty can abort work that's already been done — and cite the prior paper. Expected value checks physical sanity, rejecting gross errors. And citation entailment catches fabricated citations.

**Scene 6 — Honest handoff (11.0 s)**
> The honest scoreboard: zero papers auto-generated — work was held until the gates existed. Next: end-to-end gated study runs. No execution phrase is armed; the system waits.

SRT: cue per sentence, ≤2 lines × ≤42 chars, timed by forced alignment against the final narration audio.

## 3. Visual hierarchy per scene

Global frame: reused atmospheric footage dimmed to ≤35 % luminance (informative-not-cosmic rule — text and charts carry the content, footage is only a dim backdrop). Presenter in the series' established position; facial animation driven by the locked narration. Color progression: backdrop stays cool throughout; the **accent/label color and a low horizon glow** ramp midnight-blue `#24406E` (S1) → dawn-gold `#E8B84B` (S6), interpolated in OKLCH to avoid muddy midpoints. Presenter is the primary element only in S1 and S6 (open/close); in S2–S5 the data graphic is primary and the presenter is secondary.

| Scene | Primary | Secondary | Tertiary |
|-------|---------|-----------|----------|
| 1 | Headline lockup: "Overnight: corpus foundation + 3 quality gates" (with presenter, open framing) | Chip: "0 papers generated — by design" | Provenance chip: "as of 2026-07-22 11:25 KST" |
| 2 | Frame-indexed counter to **120,676 papers embedded** | Scope band "astro-ph.GA + astro-ph.CO · 2009–2026"; size bar "1.24 GB ≈ 10× the old 12k corpus" | Model chip: "qwen3-embedding-4b — won 10-model citation-retrieval eval" |
| 3 | Topic map: 57-node cluster scatter from **frozen exported coordinates** (never rerun UMAP at render time — nondeterministic), JWST high-z node highlighted #1 | Ranked top-topics list, #1 emphasized, label "#1 by a wide margin" | Method chip: "UMAP → HDBSCAN → c-TF-IDF · 8.9M-edge citation graph" |
| 4 | Pipeline diagram: query → local semantic retrieval (120k) → working set → deep read (HTML-first · ar5iv) | Stat card "4,864 top-cited papers" + slim 96 % bar "clean HTML" | Chip: "fully local retrieval" |
| 5 | Three gate cards — Novelty / Expected value / Citation entailment — each lighting on its narration beat (frame-timed to the locked audio) | One-line function per card: "aborts already-done work · cites the prior paper" / "numeric targets · physical-sanity rejects gross errors" / "verifies real citations · catches fabricated ones" | Status badge: "built · wired · validated"; gate/filter iconography only — no shields or seals |
| 6 | Scoreboard: "Papers auto-generated: 0" · "Next: end-to-end gated study runs" (presenter, close framing, dawn-gold accent) | Neutral chip: "Execution phrase: NONE ARMED" | Mono provenance footer: `GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE` · "local review master — not published" |

Audio mix: narration foreground; low ambient bed ≈ −26 dB relative; no music swell; quiet resolve on S6.

## 4. Wording / caveat checks

Claim → source (frozen feed / constructor):

| Narration claim | Source fact |
|---|---|
| S1 foundation + three gates; not a paper; by design | Headline; "Zero papers were auto-generated overnight. Work was deliberately held until the gates existed." |
| S2 "over 120 thousand" (screen 120,676); galaxies+cosmology 2009–2026; won 10-model eval; ~10× | 120,676 embedded; astro-ph.GA + astro-ph.CO 2009–2026; "won a 10-model citation-retrieval eval" (line 1286); 1.24 GB ≈ 10× old 12k corpus |
| S3 57 topics from scratch; recent citation inflow; 8.9M edges; JWST high-z #1 wide margin | "57 topics derived from scratch with UMAP → HDBSCAN → c-TF-IDF"; "ranked by recent citation inflow over an 8.9-million-edge graph"; "JWST high-redshift… first by a wide margin" |
| S4 local retrieval; deep-read full text (screen: HTML-first via ar5iv); "nearly 5,000" (screen 4,864); 96 % clean HTML | "Retrieval uses the local 120k corpus and deep-reads the working set HTML-first through ar5iv"; "4,864 top-cited papers, 96% clean HTML" |
| S5 gate functions as narrated | Gate list verbatim from feed ("numeric targeting" carried by the on-screen sub-line) |
| S6 zero auto-papers; next = end-to-end gated study runs; no phrase armed | Feed lines verbatim; "Approval phrase remains NO ACTIVE EXECUTION PHRASE" |

Exclusion compliance:
- **No usage-quota / live provider-card count** and **no Flow/Veo credit count** anywhere in narration, graphics, or SRT (both confirmed changing/stale cards in the constructor).
- **Does not imply a paper was generated** — S1 and S6 state the zero explicitly.
- **Does not imply the gates guarantee truth** — verbs limited to *checks / catches / can abort / rejects*; banned phrases: "guarantees", "ensures correctness/truth", "certified"; no shield/checkmark-seal iconography.
- **Does not imply an end-to-end run already happened** — "Next: end-to-end gated study runs" is strictly future-tense.
- **Does not imply any execution phrase is armed** — stated in the negative, styled neutral (not alarm-red).
- **Does not imply publication authorization** — no CTA, no URL/QR, no upload metadata; S6 footer says "local review master — not published".

Data-honesty gate for S3: the frozen feed asserts rank order and "wide margin" but gives no inflow values. **Do not draw proportional bars with invented lengths.** Render the ranked list (text emphasis) unless the operator exports real inflow numbers from the pipeline before render; only then may bars be proportional.

Freshness guard: immediately before render, re-read the live feed **once, read-only**. If the marker is no longer `GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE` or the headline changed, STOP and re-brief — never silently update numbers into this locked narration.

## 5. Same-presenter decision

**Appropriate — reuse the established female astronomer and the same female narration voice.** Rationale: (1) series continuity — the accepted series built recognition and trust on this presenter, and a status report trades on exactly that trust; (2) the pipeline (exact-narration-driven facial animation) is already validated on her, keeping the render deterministic and cheap; (3) the domain is unchanged (galaxy-evolution autopilot), so there is no editorial reason to introduce a new face. Guardrail: in S2–S5 the presenter stays secondary to the data graphics; she anchors only the open (S1) and the close (S6).

## 6. Local-only publication boundary

- Deliverable of the production step: local review master + SRT (+ per-scene stills) under `.hermes/handoffs/overnight-report-video-20260722/render/`. Nothing outside the handoff directory.
- Explicitly **not authorized** by this plan or by a completed render: YouTube upload (not even unlisted), website/lab embedding, deployment, DB writes, git add/commit of any media, or sharing links externally.
- The only gate to any distribution is Duho reviewing the local master and giving explicit per-action approval afterward.
- Production must treat the cockpit/feed as read-only (freshness guard above) and must not modify production code or video assets belonging to the accepted series — footage is *reused*, not edited in place.

HWAO_OVERNIGHT_VIDEO_PLAN_DONE
