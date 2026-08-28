# Late pre-v4 independent-review reconciliation

Received at: `2026-08-07T17:48:24Z`

## Review lineage

Three late asynchronous batches reviewed frozen pre-v4 packets, not the recommended v4 packet. Their verdicts included paper-naive `PASS`/`MINOR`, scientific `MINOR`, and a v3-specific scientific `BLOCK` resolved by v4.

A later independent v4 paper-naive review already returned `PASS; C=none`, and the independent v4 scientific audit returned `PASS; R=none`. The pre-v4 results are nevertheless preserved and reconciled rather than discarded.

Verbatim late results are preserved at:

- `qa/proposal/archive/LATE_PAPER_NAIVE_PRE_V4.md`
- `qa/proposal/archive/LATE_SCIENTIFIC_PRE_V4.md`
- `qa/proposal/archive/LATE_COMPACT_PAPER_NAIVE_V3.json`
- `qa/proposal/archive/LATE_COMPACT_SCIENTIFIC_V3.json`
- `qa/proposal/late_review_numeric_replay.json` — worker-Yui independent reproduction of the surviving numeric/geometry findings.

## Third late compact v3 batch

The compact paper-naive v3 pass returned `PASS` on all eight questions while retaining two confusions: `SFRD`/`IGM` were undefined on screen and `proxy transport` remained jargon. These support the existing first-use terminology request.

The compact scientific v3 pass returned `BLOCK` specifically because v3 S07 looked exhaustive and v3 S04/S06/S08 used generic `bootstrap`/`ONE CHANGE` language. Both are resolved in v4: S07 says `EXAMPLES PROPAGATED`, `DOMINANT OMISSION`, and `NOT EXHAUSTIVE`; S04/S06/S08 use finite-Monte-Carlo 16–84% resampling language and separate/unpaired no-tail-run disclosure.

Therefore this late `BLOCK` applies to preserved v3 only and introduces no new v4 blocker. It does not cancel the surviving v4 representation/disclosure minors below.

## Findings resolved by v4

v4 added or strengthened:

- a first-frame definition of escape fraction;
- finite-Monte-Carlo 16–84% resampling labels instead of generic bootstrap wording;
- separate/unpaired no-tail-run disclosure;
- a non-exhaustive model-boundary rail;
- model/no-new-measurement status and the high-redshift proxy-transport next test.

The older paper-naive pass also flagged `f_esc`, `SFRD`, `IGM`, `proxy`, `proxy transport`, `frozen anchors`, `model mass`, the JWST-motivated tail, and bootstrap bounds. v4 defines escape fraction, replaces generic bootstrap language, and expands star-formation-rate density in narration. Some audience labels still rely on specialist shorthand. Hwao should add compact first-use glosses for any term retained in the encoded canary.

## Live minors that survive into v4

The v3 reviewer correctly noted that the 66/83/93% labels sit on markers whose vertical positions are the median-Delta values. Those percentages encode the fraction of Monte Carlo draws with `Delta > 0`; they are not the y-coordinate of the median-Delta curve.

The v4 rail states the correct condition and says `conditional model mass, not real-world probability`, but the marker placement is unchanged. A paper-naive viewer could still infer that the median curve itself represents probability.

Additional source-backed pre-v4 findings that remain applicable:

1. The proposal plots coarse z=0.5 grid polylines while placing crossing markers at separately computed fine roots. Interpolating the geometry actually drawn gave fiducial lower-edge `8.042556` versus marker `8.045284`, median `6.309639` versus `6.327877`, and no-tail lower-edge `7.606093` versus `7.615345`. These differences are visually near line width but make “exactly where the drawn edge touches zero” mathematically inexact.
2. The top-panel required-fraction band exceeds the physical `f_esc=1` boundary at high redshift—approximately 1.0449 at z=9.5 and 1.3747 at z=10—but v4 does not draw or explain that boundary. Values above one mean no physical escape fraction closes the budget for that model space; they are not physically admissible escape fractions.

The older scientific audit's other findings are resolved by v4: the outside-model list is labeled non-exhaustive, finite-Monte-Carlo 16–84% resampling labels are explicit, and the no-tail run is labeled separate/unpaired rather than a paired one-variable counterfactual.

Classification: `REPRESENTATION_AND_DISCLOSURE_MINOR`, not a source or numeric error.

## Integrator request

Before Hwao renders the official canary:

1. Preferred probability treatment: add a dedicated probability strip or small panel with y-axis `fraction of draws with Delta > 0`, plotting 0.66/0.83/0.93 at z=7/8/9.
2. Minimal probability treatment: keep the Delta panel but move 66/83/93% into an x-keyed rail or table outside the data coordinates, with vertical guides from z=7/8/9 and no marker on the median-Delta curve.
3. Insert each frozen crossing point into the plotted polyline or draw the same continuous/interpolated geometry used to compute the root, so the marker lies exactly on the displayed zero crossing.
4. Draw and label the physical `f_esc=1` boundary; explain that any required-fraction band above it denotes model space where no physical escape fraction closes the budget.
5. Add compact first-use glosses for specialist shorthand retained in audience-visible text.

Do not encode the percentages at median-Delta y positions.

## Final-v4 expanded confirmation

A later expanded review of the actual final v4 packet returned scientific `PASS; REQUIRED=none` after replaying the source pipeline to `4.44e-16` and confirming all core crossing, fraction, scenario, model-boundary, custody, and no-audience-path claims. Its paper-naive partner also returned `PASS` on all eight questions, with one terminology confusion: the concrete proxies and “proxy transport” remain unspecified. Exact results are preserved in `qa/proposal/archive/LATE_EXPANDED_*_V4.json`.

This confirms the core v4 science while reinforcing—not removing—the existing first-use terminology request and the independently reproduced representation/disclosure minors.

## Gate consequence

The frozen v4 scientific values, source hashes, and machine validation remain valid. The worker verdict remains:

`PASS_WITH_MINOR_INTEGRATION_REQUEST`

This worker does not create v5 or edit shared tooling because Hwao remains the sole integrator/candidate writer. Hwao's silent encoded canary must test corrected probability placement, exact root-to-curve geometry, the physical `f_esc=1` boundary, and first-use terminology before TTS.
