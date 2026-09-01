# BHU sweep — BATCH 1 reconciliation (Tori, 2026-09-01)

Entries [27,36,40,41,45,46,49,52,53,55,56,57], blind-double codex + agy, Duho-authorized (RELAY ~16:12).
Brief: `ENTRY_SWEEP_BATCH1_BRIEF_20260901.md`. Seat files: `ENTRY_SWEEP_BATCH1_{codex,agy}_RESULT.md`.

## Verdict table

| entry | codex | agy | source ok both? | reconciliation |
|---|---|---|---|---|
| 27 | TOO_WEAK→DIRECTIONAL | TOO_WEAK→CALIBRATED | yes | **both say too weak** → Duho (recommend DIRECTIONAL, matches 25/26 q3) |
| 36 | CONFIRMED | CONFIRMED | yes | **agree — tier holds** |
| 46 | CONFIRMED | CONFIRMED | yes | **agree — tier holds** |
| 49 | CONFIRMED | CONFIRMED | yes | **agree — tier holds** |
| 40 | CONFIRMED | TOO_WEAK→DIRECTIONAL | yes | **split (closure criterion)** → Duho |
| 41 | CONFIRMED | TOO_WEAK→DIRECTIONAL | yes | **split (closure criterion)** → Duho |
| 52 | CONFIRMED | TOO_WEAK→DIRECTIONAL | yes | **split (closure criterion)** → Duho |
| 45 | TOO_WEAK→DIRECTIONAL | CONFIRMED | yes | **split (white-hole Hawking flux observability)** → Duho |
| 53 | CONFIRMED (1906.11824) | wrong source (read 1410.3881 = entry 11) | **NO** | agy invalid → reliable re-read pending |
| 55 | CONFIRMED (2007.06664) | hallucinated identity | **NO** | agy invalid → reliable re-read pending |
| 56 | CONFIRMED (gaztanaga_mass_mnras.pdf) | hallucinated identity | **NO** | agy invalid → reliable re-read pending |
| 57 | CONFIRMED (smoller_temple_1997) | hallucinated identity | **NO** | agy invalid → reliable re-read pending |

## Settled this batch (both seats CONFIRMED, correct sources, substantive) — TIER UNCHANGED

- **36** Smoller–Temple 2000: derived distances normalize to observed H0/T0, indexed by unmeasured R*; no independent observable. codex `smoller_temple_2000:3139-3665`, agy `:115`.
- **46** Fullana/Alfonso-Faus: 10¹²² is internal Planck-unit numerology, no threshold. Both on `1111.1017`.
- **49** Blau–Guendelman–Guth 1987: closed universe "indistinguishable by local measurements from flat FRW" (agy quote); critical masses are internal bubble-trajectory scales, lab energy expressly inaccessible. Both on `blau_guendelman_guth_1987`.

Bibliography annotations for these three deferred (batched, per the no-per-entry-Fable discipline) — recorded here.

## Returns to Duho (tier-adjacent / split) — see OPEN_QUESTIONS

- **27** — both seats: CONSISTENCY-ONLY is too weak. It is the SAME causal-horizon CMB cutoff (θ≈60°, measured Θ_H=66±9°) as entries 25/26, which Duho ruled QUALITATIVE-DIRECTIONAL in q3. codex→directional (no amplitude), agy→calibrated (over-reach, same as RQ-C: no C_ℓ amplitude → not calibrated). Clean precedent.
- **40, 41, 52** — split driven by ONE criterion: does a model whose interior is a **closed / positive-curvature (Ω_k<0)** universe make a QUALITATIVE-DIRECTIONAL prediction (agy), or is closure an *assumed* ansatz not mapped to an observable → CONSISTENCY-ONLY (codex)? Corpus-wide call; note entry **54** is already tiered DIRECTIONAL for predicting Ω_k<0, and the DESI curvature watch tracks exactly this.
- **45** — genuine split: codex says the white-hole/horizon mode-matching predicts an exterior Hawking-flux departure (observation-facing → directional); agy says the paper concedes it "may not be directly relevant to observable Universe" → CONSISTENCY-ONLY. One-paper substantive disagreement.

## Operational finding (for the register / next batches)

The 12-entry batch **overloaded agy's single `--print` turn**: reliable for the first 8 entries, then read the wrong source (53) and hallucinated paper identities (55/56/57). codex (agentic `exec`) handled all 12 cleanly. **Next batches: cap agy at ~5 entries**, or route the long tail to codex + kimi. 53/55/56/57 need a reliable second read (small agy batch or kimi) — deferred until after Duho rules the closure criterion, since that ruling may bear on them.

## Sweep status

Batch 1 done. **Sweep PAUSED pending Duho's closure-criterion ruling** — continuing to batch 2 before that would just generate more of the same unresolvable split. 3 confirmed, 1 precedented tier-adjacent (27), 4 splits (40/41/45/52), 4 pending reliable re-read (53/55/56/57).
