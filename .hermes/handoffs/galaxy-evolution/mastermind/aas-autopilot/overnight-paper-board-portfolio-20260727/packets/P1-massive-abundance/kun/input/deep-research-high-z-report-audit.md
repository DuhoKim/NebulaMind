# Auditing Deep Research reports on high-redshift stellar masses and abundances

Use this when an external report claims to summarize JWST stellar-mass systematics, cumulative galaxy abundances, or comparisons to a named simulation suite.

## Closed verdict structure

Grade these separately; a mechanically valid citation list can still be scientifically unusable.

1. **Query coverage:** does the report answer every requested part with the requested statistic?
2. **Statistic identity:** are differential SMFs, Schechter parameters, cumulative number density, cumulative stellar-mass density, halo density, and extreme-value ceilings kept distinct?
3. **Population commensurability:** are total, star-forming, quiescent, central, satellite, and UV-selected populations not mixed in one trend/table?
4. **Simulation commensurability:** are IMF, stellar-mass aperture, bound/all-star convention, cosmology, redshift bins, and selection matched?
5. **Primary-source support:** does each load-bearing number occur in the cited primary source with the same scope and interpretation?
6. **Source identity/version:** do identifiers resolve to the same paper, and are published/final values used instead of superseded preprint tables?
7. **Claim strength:** does the conclusion remain inside what the quantitative comparison actually established?

Return `PASS`, `PARTIAL`, or `FAIL` for each dimension and an overall drafting disposition with report line references.

## Version-current number gate

When the request says **published**:

- Do not accept a pinned arXiv `v1` table merely because the paper later appeared in a journal.
- Compare every load-bearing table against the latest arXiv version or journal version. Record changed thresholds, fixed/free parameters, bin definitions, and numerical revisions.
- A value can be faithfully copied from v1 yet still fail the published-evidence gate.
- Treat a source-index link to an old version as an identity/version defect, not merely a cosmetic link choice.

A useful audit tactic for arXiv papers is to inspect the TeX source in memory and search exact numerical strings. This often reveals fixed parameters, table notes, or later-version changes that HTML extraction obscures. Do not persist source archives unless authorized.

## Cumulative-density gate

A table of Schechter parameters is **not** a table of `n(>M*)`.

For every cumulative number density require:

- redshift interval;
- explicit stellar-mass threshold;
- population/selection definition;
- IMF and mass/aperture convention;
- completeness and contamination treatment;
- Eddington/scatter treatment;
- Poisson plus cosmic/sample-variance uncertainty;
- direct count versus integration/extrapolation label.

Never combine in one apparent evolutionary sequence:

- quiescent and total populations;
- mass bins and `>M*` thresholds;
- galaxy and halo number densities;
- empirical counts and theoretical ceiling/extreme-value curves;
- different thresholds at different redshifts without an explicit conversion.

If the report cites an extreme-value or baryon-ceiling paper for an “empirical cumulative density,” grade the row as a source-role failure.

## Systematic-budget gate

A list of maximum shifts from unrelated samples is not a consensus error budget and cannot be added naively.

For each systematic record:

- sample redshift and mass range;
- direction and magnitude of the shift;
- whether the result concerns individual masses, an SMF, or stellar-mass density;
- whether it is a standard cross-literature conversion or an exploratory alternative model;
- covariance with other terms.

Do not generalize a low-mass outshining result, a `z>9` IMF experiment, or a massive-galaxy MIRI test to all `z=4–6` galaxies. Preserve conclusions that a large individual-object effect had little population-level impact.

## Named-simulation gate

For a report framed “versus IllustrisTNG” or another named suite, generic ΛCDM/HMF abundance matching does not count as a simulation comparison.

Require the report to state the simulation’s actual stellar-mass definition and IMF and to compare the requested stellar-mass statistic. For the IllustrisTNG JWST-prediction paper by Vogelsberger et al. (arXiv:1904.07238), the relevant conventions include gravitationally bound particles/cells, a fixed 30 physical-kpc aperture, and a Chabrier IMF. Its cumulative UV-luminosity result is not a cumulative stellar-mass result.

Keep these estimands separate:

- native simulated `M*/(fb Mhalo)`;
- deterministic abundance-matching conversion factors from an analytic HMF;
- instantaneous star-formation efficiency;
- UV luminosity-function agreement.

A source about one cannot support a claim about another.

## Source-index reconciliation

Run two ledgers:

1. **Mechanical:** inline IDs, anchors, targets, missing entries.
2. **Scientific:** authoritative identity, version, source role, and claim support.

Also count distinct cited sources versus index entries. A heading such as “used sources” is false if most entries are uncited. Duplicates and ResearchGate/thesis/profile routes should be reported separately from missing anchors; they may resolve mechanically while failing primary-source provenance.

Pay special attention when the correct paper is present in the index but unused while an adjacent claim cites another source. This is strong evidence of citation drift.

## Minimum correction language

Until the above gates pass, replace categorical synthesis such as “resolved,” “precisely aligned,” or “the simulation achieves” with scoped language:

- “supported for this sample and mass range”;
- “an effective abundance-matching conversion factor”;
- “not yet compared at matched IMF, aperture, selection, and cumulative threshold”;
- “the cited source concerns UV luminosity rather than stellar-mass abundance.”
