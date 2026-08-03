# High-redshift abundance-matching and simulation–observation audit

Use this checklist when reviewing claims that a simulation under-produces rare JWST galaxies or that an inferred stellar-to-halo efficiency evolves with redshift.

## 1. Identify the compared population statistic

- An individual catalogue object does **not** have a cumulative number density. `n(>M*)` belongs to a selection-corrected stellar-mass function in a defined redshift bin.
- Never assign every observed object the same `n` and then summarize the resulting object-by-object efficiencies. At fixed redshift this gives all objects essentially the same halo denominator, so the inferred efficiency distribution merely restates the selected stellar-mass distribution.
- For a fixed-number-density comparison, invert the observed and simulated cumulative GSMFs separately to obtain one `M*(n,z)` from each.
- For a rare single object, use its actual survey volume and extreme-value or cumulative stellar-mass-density statistics. Do not infer impossibility from an arbitrary abundance assigned to that object.
- If a conditional fixed-`n` mapping yields `M*/(fb Mh) > 1`, the result shows only that the chosen tuple of stellar mass, assigned rank, HMF, cosmology, and zero-scatter assumptions is internally inconsistent with the physical ceiling. It does **not** by itself show that the photometric mass is overestimated. The tension could instead come from the assigned `n`, selection/completeness, scatter, duty cycle, IMF/aperture conventions, redshift uncertainty, or the HMF/mass definition. Replace “hence likely overestimated” with an explicit list of unresolved alternatives unless an independent mass reanalysis supports that diagnosis.
- A number density is meaningless unless accompanied by the stellar-mass threshold or bin, redshift interval, completeness/selection definition, and uncertainty treatment.

## 2. Prefer direct commensurable comparisons

Recommended order:

1. Match redshift bins and cosmology/unit conventions.
2. Harmonize IMF, living-star/remnant conventions, and stellar-mass aperture.
3. Compare binned GSMFs directly.
4. Compare cumulative `n(>M*)` at common thresholds.
5. Only then invert at selected `n` values.

Do not substitute a mass–redshift scatter plot of individual observed galaxies for an abundance comparison.

## 3. Distinguish physical efficiency from an abundance-matching proxy

`M*/(fb Mh)` is an integrated stellar-to-halo baryon-conversion fraction, not an instantaneous star-formation efficiency.

If `M*` is taken from a simulated GSMF quantile but `Mh` comes from an analytic HMF quantile, call the result an **effective deterministic abundance-matching conversion factor**. It is not the efficiency physically achieved by individual simulated haloes.

For a physical simulation claim:

- match central galaxies to their native parent haloes;
- use an explicitly defined native halo mass such as `M200c`;
- report the median and scatter of `M*/(fb M200c)`;
- analyze gas supply, SFR, winds, black holes, and feedback diagnostics before attributing a population discrepancy to a mechanism.

Check host accounting: a distinct-host spherical-overdensity HMF cannot be matched one-to-one to a galaxy catalogue containing both centrals and satellites unless subhaloes/occupancy are modeled consistently.

## 4. Forward-model scatter, occupancy, and selection

At the steep high-mass tail, require a model of the form

`phi_obs(Mobs) = integral dMh [dn/dMh] f_duty(Mh,z) integral dMtrue p(Mtrue|Mh,z) p(Mobs|Mtrue,z) S(Mobs,z)`.

Keep these effects separate because their directions differ:

- intrinsic scatter in `M*|Mh` promotes numerous moderate haloes into the selected high-mass tail;
- duty cycle or incomplete occupation changes the halo abundance corresponding to an observed galaxy abundance;
- SED mass errors cause Eddington bias in the observed high-mass tail;
- incompleteness and contamination alter the abundance in potentially opposite directions.

Minimum sensitivity grid: zero, 0.2, and 0.3 dex intrinsic scatter; at least one sub-unity duty-cycle case; full joint redshift–mass posteriors; and the published selection/completeness function.

A uniform stellar-mass shift is not an adequate robustness test when errors, AGN contamination, and Eddington bias vary with mass, redshift, or SED class.

## 5. Match simulated and SED-derived stellar masses

Particle masses inside a variable 3D aperture, all bound stellar mass, fixed physical-aperture mass, and SED-inferred total mass are different observables.

Bracket at least:

- the simulation's canonical galaxy aperture;
- all bound stellar mass;
- one or more fixed physical apertures relevant to the observations.

Report how the GSMF and fixed-abundance masses change. The strongest test is mock photometry passed through the same detection and SED-fitting pipeline as the observations.

## 6. Treat volume errors as more than Poisson noise

A count of order 10–20 objects still has roughly 20–30% Poisson uncertainty. This alone does not establish a redshift trend of similar fractional size.

Also account for:

- halo bias and realization-to-realization sample variance;
- missing modes larger than a periodic simulation box;
- order-statistic uncertainty in fixed-abundance masses;
- observational pencil-beam cosmic variance;
- covariance between redshift bins and cumulative thresholds.

Internal subvolume jackknifes cannot recover modes larger than the parent box. Use a larger box or multiple realizations plus an analytic `b^2 sigma_V^2` estimate. A larger, lower-resolution simulation also requires a resolution-convergence comparison.

## 7. Audit the HMF as a model, not a software output

Record:

- HMF fitting function;
- calibration redshift and mass ranges;
- cosmology;
- spherical-overdensity or FoF mass definition;
- distinct-halo versus subhalo accounting;
- software and version;
- integration range and units.

Tool citations establish implementation, not validity. Many classic HMF fits are extrapolated when used at `z > 4`; bracket them with a high-redshift calibration and propagate the resulting host-mass/efficiency spread. Ensure the analytic mass definition matches the native simulation halo mass.

## 8. Source-role verification

For every cited paper, record whether it supplies:

- candidate objects;
- a binned GSMF or cumulative density;
- a survey-volume extreme-object test;
- an HMF calibration;
- software only;
- an AGN/SED-systematics constraint;
- a simulation prediction.

Do not transfer a number from one role into another. In particular, do not use an early candidate sample as a generic abundance anchor, describe a cumulative baryon-ceiling test as ordinary abundance matching, or quote a density without the threshold used to derive it.

## 9. Minimum defensible claim language

Until the preceding checks are passed, prefer:

- “suggestive deficit relative to the face-value observed GSMF”;
- “effective abundance-matching conversion factor”;
- “not yet shown to be robust to volume and mass-calibration systematics.”

Avoid “the data demand,” “the trend is robust,” “the simulation’s achieved efficiency,” or a specific feedback attribution without propagated uncertainties and native-halo diagnostics.

## Core literature families

Use exact identities appropriate to the case, including:

- abundance-matching scatter and galaxy–halo connection: Behroozi, Conroy & Wechsler (2010); Wechsler & Tinker (2018);
- maximum-mass and extreme-value tests: Behroozi & Silk (2018); Lovell et al. (2023); Boylan-Kolchin (2023);
- cosmic variance: Trenti & Stiavelli (2008); Moster et al. (2011);
- high-redshift HMF calibration: Yung et al. (2024) or a later validated successor;
- aperture sensitivity in the relevant simulation suite;
- observational GSMF papers that explicitly propagate mass posteriors, completeness, cosmic variance, and Eddington bias.
