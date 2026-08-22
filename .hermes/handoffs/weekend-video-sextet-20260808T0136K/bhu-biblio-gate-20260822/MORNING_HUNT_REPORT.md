# Overnight hunt, round 2 — morning report (2026-08-23)

Duho's order: search again overnight, all resources, hourly supervision. Done. **Both new phases
returned findings; nothing has been integrated — every candidate below awaits Crossref verification
and your call.**

## Pipeline health (the hourly-watch summary)

Harvest ran clean in 384s. One incident: the kimi gate hit HTTP 429 (Moonshot overloaded) at 23:52,
was retried once after a 10-minute backoff per the pace-gently rule, and succeeded. No other
failures. 10 of 103 harvest queries failed on a real bug worth keeping: **DOIs containing
parentheses break the URL-encoding path** — those seeds got no citation walk, a recorded blind spot.

## Phase 1 — the channels no previous hunt used

103 queries across 5 hosts (author sweeps, citation-graph walks via OpenAlex + Semantic Scholar,
and OpenAlex/Crossref as fresh search hosts): **2,028 records, 308 new on-topic after diffing
against the 40.** Deliberately noise-heavy — the citation walk finds relevance regardless of title,
at the cost of pulling in fringe. The top 70 (W1/W2) went to triage.

## Phase 2 — kimi's triage of the 70 (second family, `HOLD_K2_MEMORY_OMISSIONS`, 242 lines)

| class | n |
|---|---|
| BASE — published physics, on-claim | **4** |
| SUPPORT | 10 |
| APPENDIX-CONTEXT (incl. the Shamir empirical line, already ruled A7) | 17 |
| FRINGE — venue named as the reason each time | 20 |
| NOT-BHU | ~19 |

Its top base candidates include: a PRD 102 (2020) de Sitter-universe-inside-a-Schwarzschild-BH
construction, Gaztañaga's MNRAS "The mass of our observable Universe" (completing branch 6), an
ApJ 2019 "Big Bounce and Closed Universe from Spin and Torsion", and a CQG 2019 independent
Einstein–Cartan bounce analysis.

## Phase 3 — the recall attack, and why two families were worth it

**Kimi's memory returned 11 published items in NEITHER the bibliography NOR the harvest — none of
which Codex's recall found.** Codex found 4; kimi found 11 different ones. The non-overlap is the
finding: neither family's memory is complete, and each samples the literature differently.

The headline cluster is a **probable missing branch: the false-vacuum / laboratory child-universe
lineage** — Farhi & Guth 1987 (PLB 183), Farhi–Guth–Guven, Blau–Guendelman–Guth (PRD), and
Sato–Kodama–Sasaki–Maeda's multi-production of universes. That is the "can a universe be *made*
inside a collapse" programme, sibling to branch 4 and in nobody's list. Also recalled: a further
Smoller–Temple extension, a Popławski PLB 690, Zhang's black-hole-universe series
(memory-uncertain), a Smolin book chapter, and Longo's dipole detection paper itself.

Kimi applied the discipline unprompted: every recall item is marked UNVERIFIED-AT-GATE, memory-
confident ≠ verified, and each needs the Crossref protocol before touching the base layer.

## Decisions waiting on you

1. **"integrate round 2"** — I verify the ~15 strongest (kimi's 4+top-10 base picks, plus the
   confident recalls) via Crossref and seat what passes, likely creating branch 11 (false-vacuum
   child universes). A morning's work.
2. The 20 fringe rows get recorded as excluded-with-venue-reasons, mirroring the appendix pattern.
3. The unread debt grows with every integration — reading remains the real outstanding work.

No completeness claim: two engines' memories and five hosts' indexes were sampled, each boundary
stated in its own verdict.
