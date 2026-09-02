# Reading B built and computed — blind double, reconciled

**Authority:** Duho, chat-verified via Blanc, "topic A". Program (A) on the **no-go branch**:
prove the amplitude is permanently free, or find a forced completion. **No tier moved.**

Blind double per the ruled method: codex (`READINGB_codex_RESULT.md`, `cutoffA_readingB.py`) and agy
(`READINGB_agy_RESULT.md`, `cutoffA_readingB_agy.py`), each run to completion, agy explicitly barred
from codex's files. Brief: `_PROGRAM_A2_READINGB_BRIEF.md`.

## What both seats found, independently

**Reading B does not yield a number at all.** `S₁/₂` depends on the infrared regulator and does not
converge as it is removed:

| seat | k_min range | S₁/₂ range (μK⁴) |
|---|---|---|
| codex | 10⁻³ → 10⁻⁶ × k_§ | **252,066 → 900,646** (×3.57, monotonic) |
| agy | 10⁻⁴ → 10⁻⁸ | **diverging**, 553,328 at k_min = 10⁻⁸ |

Absolute numbers differ (different grids and regulator ranges, as expected); **the mechanism and the
conclusion are identical and were reached independently.**

**The mechanism, in both seats' words and confirmed by the scaling.** For a near-scale-invariant
spectrum, `ξ(r) = ∫ dk/k Δ²(k) sinc(kr)` is **log-divergent in the IR**, and the divergent piece is
`r`-independent — an unobservable *monopole*. Multiplying by a compactly supported window `W(r)`
**converts that monopole into physical low-k power**, because `c·W̃(k)` is concentrated at
`k ≲ 2π/χ_§` — precisely the multipoles that dominate `S₁/₂`. The observed scaling is consistent with
`S₁/₂ ∝ c²` (codex's ×3.57 across three decades against a predicted ×4). **The paper supplies no
prescription for that constant, so Reading B has no unique prediction.**

## Where the two readings land — and a seat prediction refuted

`ΛCDM 34,924 · Reading A 6,897 · Reading B 2.5×10⁵–9×10⁵ · observed ~1,150`

**kimi predicted at step 2 that the two readings' minima would "straddle the observed ~1150 μK⁴".
That is refuted by computation: both land far above it.** They straddle **ΛCDM**, not the
observation — Reading A ~5× below, Reading B ~7–26× above. codex stated this correctly; agy's summary
says "opposite sides of the observed value", which its own numbers contradict (both are above 1,150).
**On that point codex is right and agy is wrong**, and it is arithmetic rather than a matter of
judgement, so it needs no ruling.

## Why this strengthens the no-go

The no-go is now specific rather than general. It is not merely "the amplitude is free" — it is that
**each candidate refinement of the paper's one perturbation sentence fails in its own identifiable
way:**

- **Reading A** yields a number, but the number is set by an unlicensed convention: `2π/χ_§` gives
  6,897, `π/χ_§` gives 14,000. The paper fixes neither.
- **Reading B** yields *no* number: its value is set by an IR regulator the theory does not specify,
  and it does not converge as the regulator is removed.
- **The two are mutually exclusive** (Paley–Wiener, computed earlier), so they cannot be averaged,
  combined, or treated as bracketing a common answer.

Together with the four-seat `READING_C` finding — that the paper licenses neither refinement — this
is a complete account of *why* the prediction cannot be calibrated, not just an assertion that it
cannot.

## The obvious objection, which is NOT yet answered

**A referee will say: just subtract the monopole.** If `ξ` is defined with its `r`-independent piece
removed (or equivalently the field's zero mode projected out, as the CMB monopole is in practice),
the divergent constant vanishes and Reading B might give a stable, finite number.

**Neither seat tested that, and I am not claiming it fails.** Both used the same construction
(`ξ_ΛCDM · W`), so their agreement does not exclude a shared error of exactly this kind. **Until a
monopole-subtracted Reading B is computed, the claim "Reading B has no prediction" is
under-tested** — the honest statement today is "Reading B's prediction is regulator-dependent under
the natural construction, and the monopole-subtracted variant has not been checked."

That check is the next step, and it is cheap.

## Status

Program (A) no-go branch: **advancing, not concluded.** No tier moved; entries 23–27 unchanged. The
paper remains HELD by Duho's standing ruling — nothing outward.
