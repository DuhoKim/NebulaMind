# G2 — V4 NARRATION REWRITES (mandatory scenes from G1)

Coordinator: Hwao · Written: 2026-07-23 ~14:45 KST (05:45Z) · Lane-only receipt.
Every number is anchored to `sources-v4/<key>.md` lines (the G0 current freeze). Card grammar (2–3 cards) and ~35–45-word scene budgets preserved so durations stay near V3. These texts are the V4 batch inputs for the three changed papers; z9-metallicity has its own full spec (`V4_Z9_CANARY_SPEC.json`); mzr-framework needs no rewrite (identical freeze).

## massive-abundance (scenes 3–6 SUPERSEDED → rewritten)

**[3] THE RAW GAP | Observed counts are about twice the simulation** — anchors `:28-30`, `:77-84`
N: "At redshift five, observations report about three times ten to the minus five massive galaxies per cubic megaparsec. On a like-for-like total-mass footing, IllustrisTNG gives one point four seven times ten to the minus five — a raw factor of about two."
C: `3×10⁻⁵`=observed per Mpc³ (Weibel) ; `1.47×10⁻⁵`=TNG, total-mass matched ; `≈2.04×`=raw excess (0.31 dex)

**[4] WHY MASS MATTERS | A small shift crosses a steep cutoff** — anchors `:31-32`, `:85-88`, `:95-96`
N: "The high-mass tail is steep — the count falls with slope near minus one point six. So a downward stellar-mass shift of only about zero point two dex, dividing masses by roughly one point six, erases the entire redshift-five excess."
C: `−1.58`=local log-slope of the tail ; `0.20 dex`=required mass shift ; `÷1.6`=what 0.20 dex means

**[5] THE ERROR BUDGET | A committed budget replaces the loose one-dex claim** — anchors `:32-35`, `:77-84`
N: "Earlier drafts leaned on a loose one-dex mass-error budget. This version commits: independent systematics add to zero point four six to zero point five five dex. The required zero point two dex shift is roughly forty percent of that budget — comfortably covered."
C: `0.46–0.55 dex`=committed quadrature budget ; `≈0.4×`=required shift vs budget ; `±0.10 dex`=Poisson floor, IMF-independent

**[6] THE EARLIER CANDIDATES | The redshift 7–9 excess is NOT covered** — anchors `:44-45`, `:101`
N: "At redshifts seven to nine, photometric candidates sit about thirteen point six times high — one point one three dex. Erasing that needs a zero point seven two dex shift, which exceeds the committed budget. Their masses are also spectroscopically unconfirmed. This tension stays open."
C: `≈13.6×`=apparent excess (1.13 dex) ; `0.72 dex`=required shift ; `EXCEEDS 0.46–0.55`=not covered by the budget
Semantic note (Lana): this flips V3's conclusion for z 7–9 from "uncertain masses could cover it" to "not covered; grouped with the quiescent residual as unresolved" — the video must not soften this.

## scaling-relations (scenes 4–5 REFRAMED → rewritten; 6+8 strengthened)

**[4] STAR FORMATION, AS MEASURED | Big offsets — but selection is in the frame** — anchors `:26-33`, `:63-65`, `:132-133`
N: "As measured, early galaxies sit far above the local star-forming sequence: zero point seven seven dex at redshift three point five, one point nine four dex at redshift six point seven. But these samples were selected by emission-line flux — and that selection itself inflates the offset."
C: `+0.77 → +1.94 dex`=as-measured elevation ; `Hβ-FLUX SELECTED`=selection forward-modeled ; `INFLATION`=selection raises detected offsets

**[5] WHAT SURVIVES SELECTION | No claim below z≈6; the z>6 residual stands** — anchors `:31-33`, `:160-165`
N: "Modeling that selection, the de-biased elevation below redshift six can reach zero — pure selection cannot be excluded, so the paper claims no star-formation evolution there. What survives is the redshift-above-six residual, about one point three to one point five dex, in a forty-six-galaxy bin."
C: `≤0 dex`=possible de-biased elevation below z≈6 ; `NO CLAIM z<6`=the paper's own boundary ; `~1.3–1.5 dex`=surviving z>6 residual (n=46)

**[6] strengthen (recommended, drafted)** — anchors `:160-162`, `:190-191`: append to existing scene-6 narration: "The paper calls this metallicity deficit the more robust of its two signals — emission-line selection does not manufacture it." (cards unchanged: −0.43/−0.37/−0.40 dex confirmed)

**[8] extend (recommended, drafted)** — anchors `:74-75`: append: "Using the older Tremonti-scale anchor, about zero point two four dex high, would by itself have overstated the deficit by roughly zero point one dex."

## tng-validation (scene 5 REFINED → rewritten)

**[5] STAR FORMATION | Correcting the start reveals over-growth** — anchors `:29-30`, `:88`
N: "A raw comparison can look reassuring because TNG starts low. After removing that starting residual, TNG's internal main-sequence growth reaches one point three to one point six dex from redshift four to six. Observed galaxies rise only zero point eight to one point zero dex — an over-evolution gap of zero point four to zero point five dex."
C: `+1.3 to +1.6 dex`=TNG internal growth ; `+0.8 to +1.0 dex`=observed elevation ; `+0.41/+0.49 dex`=gap at z≈4.7/5.4
Semantic note (Lana): this also repairs the V3 narration-vs-card inconsistency (narration said 0.9–1.0; card said +0.8–1.0; current freeze says ∼+0.8–1.0).

## Not rewritten

- z9-metallicity: G1 verdict all-CONFIRMED; full V4 spec in `V4_Z9_CANARY_SPEC.json` (this lane).
- mzr-framework: PDF hash identical to V3 freeze; V3 text stands; V4 changes only its visuals (procedure diagram, no cover page) at batch time.

HWAO_V4_G2_NARRATION_REWRITES_COMPLETE
