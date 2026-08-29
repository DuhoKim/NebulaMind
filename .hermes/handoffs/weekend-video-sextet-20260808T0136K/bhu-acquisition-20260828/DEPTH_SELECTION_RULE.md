# Depth-probe selection rule — fixed before it selects anything

Blanc, 2026-08-29 11:27: *"record what 'densest' means as a rule before you pick the next entries,
not after. If the selection rule for depth probes is chosen per-entry, the depth result inherits
exactly the selection-bias problem you fixed for the main sweep with the random draw."*

Correct, and it applies retroactively: **entry 36 was picked on a raw count of scientific-notation
values (21), which is confounded by paper length.** A long paper has more of everything. That pick
happened to be defensible, but the rule was implicit and chosen after looking.

## The measure

> **NUMERIC DENSITY = physical values per 1,000 words**, where a *physical value* is a number in
> scientific notation **or** a number carrying a physical unit, and **equation labels of the form
> `(N.M)` are excluded.**

Three parts, each with a reason:

1. **Per 1,000 words**, not a raw count — otherwise the measure ranks by paper length, which has
   nothing to do with whether a calibrated claim is hiding.
2. **Scientific notation or a unit** — a bare `3.5` is usually structural (a section number, an
   index, a coefficient in an algebraic identity). A number with a magnitude or a unit is a
   candidate for a physical claim.
3. **Equation labels excluded** — entry 36 contains **614** of them against 21 real values. Any
   measure that counted them would rank papers by how many equations they number, and would have
   called the most equation-heavy paper in the corpus the most numerically dense. That is the same
   defect as counting `σ` in a paper where `σ` is the equation-of-state parameter.

## Why this measure and not another

The depth probe exists to find a calibrated claim that the surface pass missed **because it sat
away from claim-language**. So the right ordering is by *how much material could hide such a
claim*, normalised for how much text there is to hide it in. Density does that; a raw count
measures the paper's size as much as its content.

**Known limitation, stated so it is not discovered later:** a paper stating exactly one calibrated
threshold in otherwise verbal prose would score near zero and be probed last. The measure ranks
*opportunity to hide*, not *probability of hiding*. It is a queue order, not a prediction.

## How it is used

The rule produces a queue. Probes run **in queue order**, top-down, skipping entries already
probed. **No entry is promoted or skipped by judgement.** If two entries tie, the lower entry
number goes first — an arbitrary tiebreak, fixed here so it is not chosen later by taste.

Ambiguities are recorded rather than resolved by preference.
