# CYCLE_33_ACTUAL_RESEARCH_RESPONSE

## What changed
- Updated the flagship morphology/aperture caveat in [`flagship_rp1/aastex/rp1_flagship_polished.tex`](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_33_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L67) to keep the central-velocity-dispersion discussion tied to an existing citation set, adding `\citep{piotrowska2022}`.
- Tightened the supplement maintenance-heating boundary in [`supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_SPRINT_CONTINUATION_20260709T141106Z/candidates/cycle_33_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L77) by adding one sentence that explicitly frames optical BPT selection as a radiative-mode tracer and requires nondetection modelling before any mechanical-duty-cycle inference.
- Added the missing bibliography entries in the supplement for `cidfernandes2011`, `stasinska2008`, `stasinska2015`, and `tacconi2018` so the TeX file remains compile-safe against the citations already used in the manuscript body.

## What was refused
- No new quantitative claims were added.
- No sample sizes, offsets, fractions, confidence intervals, or other numeric invariants were changed.
- No mock, synthetic, placeholder, or toy data were introduced.
- No new physical results were asserted for morphology, gas depletion, maintenance heating, or environment; absent observables remain explicitly framed as future real-data requirements.

## Why these edits only
- The review reports identified a compile-risk bibliography gap in the supplement and recommended safer wording that keeps the manuscript strictly association-only.
- The existing numeric and selection-bound claims already match the local real-data inventory, so the safe action was prose clarification plus bibliography completion, not result expansion.
