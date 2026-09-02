# Phase (b) result — like-for-like cut-sky comparison, blind-doubled

**Prereg followed end to end; controls C1/C2 passed before this table existed; percentiles only,
per prereg §5. Interpretation returns to Duho. No tier moved.**

## The two independent implementations agree

Mine (n=2,000/row, seeds 100k–500k) vs codex's blind rebuild from the prereg alone (n=500/row,
seeds 731021–731025; barred from every file of my implementation, and dispatched BEFORE my
production numbers existed):

| quantity | mine | codex blind | consistent? |
|---|---|---|---|
| f_sky (Nside 64, >0.9) | 0.7515 | 0.75146 | exact |
| observed cut-sky S₁/₂ | **1,223.3** | **1,217.4** | 0.5% |
| P(S ≤ obs \| ΛCDM) | 0.15% | 0.20% | within MC error |
| P(S ≤ obs \| A 2π/χ_§) | **2.75%** | **2.20%** | within MC error |
| P(S ≤ obs \| A π/χ_§) | 0.40% | 0.80% | within MC error |
| P(S ≤ obs \| B spliced) | 1.10% | 1.60% | within MC error |
| P(S ≤ obs \| B no-splice) | 0.65% | 0.60% | within MC error |

Medians agree row-by-row within the (large, skew-driven) median MC error; every percentile pair is
within binomial error at its n. **No adjudication needed — the blind double passes.**

## The licensed statement (C3 wording: percentiles, never verdicts)

On the masked sky, with one estimator applied identically to Planck SMICA and to every simulation:

> The observed sky sits at the **0.15–0.2 percentile under ΛCDM**. Under the causal-cutoff
> refinements it sits at **0.4–2.8%** depending on the (paper-unfixed) reading and convention —
> the most favourable row being Reading A at `2π/χ_§` (~2.2–2.8%). **Every refinement leaves the
> observed correlation deficit at or below the ~3% level; the best improvement over ΛCDM is
> roughly 15×.**

ΛCDM itself is reported as unlikely-but-possible (the reductio control's wording), and the same
grammar applies to every row. Whether ~3% "explains" the anomaly is not a question this table
answers; it is Duho's, and it bears on entries 23–27 — **nothing moved.**

## Note for the record

This like-for-like result lands numerically close to the earlier full-sky p-value shift
(0.1% → ~3.3%) whose *method* was refuted (C1/C2 gates). The numbers survived the correction;
the licence did not exist until now. The distinction matters: what was refuted was comparing
full-sky theory to a cut-sky number — this table compares cut-sky to cut-sky with passed controls,
a pre-registration, two dated pre-data amendments, and a blind double.
