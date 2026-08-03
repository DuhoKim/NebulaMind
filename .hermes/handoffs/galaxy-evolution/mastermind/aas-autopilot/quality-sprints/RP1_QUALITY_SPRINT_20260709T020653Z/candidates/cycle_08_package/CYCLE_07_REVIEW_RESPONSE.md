# CYCLE_07_REVIEW_RESPONSE

Changed safely in the candidate package only:

- Flagship abstract now states the result is based on a capped `60k`-row pilot cache, not a random sample, and adds the stricter Seyfert-like reduction to `-0.763 dex`.
- Flagship Section 1 now lists the key missing observables up front: morphology/aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxies, gas mass, environment, and time-domain or duty-cycle modelling.
- Flagship Section 2 now explains the cap as a sequential `specObjID` pilot-query limit and standardizes the cache wording as a `60k-row pilot cache`.
- Flagship table caption and interpretation now keep the association-only boundary explicit while retaining the same `8,146` pairs, `-1.309 dex` median offset, and bootstrap interval.
- Supplement abstract now ends with an explicit atlas caveat: it provides observational baselines only and cannot confirm or refute feedback models without the missing observables.
- Supplement Section 3.1 now explains that the 10th-neighbor density proxy is a local rank within the emission-line-selected cache, not a substitute for central/satellite labels or a volume-complete halo-density measurement.
- Supplement Section 3.8 now states that simulation mocks must be passed through the same optical S/N and fiber-aperture selection function before any validation comparison is considered valid.

Refused as requiring new data:

- Any change to numeric results, table values, bootstrap intervals, counts, or figure paths.
- Any causal-feedback, quenching, gas-depletion, maintenance-heating, or outflow claim beyond association-only or denominator/proxy wording.
- Any attempt to add morphology, aperture-matched SFRs, CO/HI, X-ray, radio, halo/group, outflow, or simulation-mock measurements that are not present in this package.

The edits stayed inside the approved candidate root and did not touch public/live systems.
