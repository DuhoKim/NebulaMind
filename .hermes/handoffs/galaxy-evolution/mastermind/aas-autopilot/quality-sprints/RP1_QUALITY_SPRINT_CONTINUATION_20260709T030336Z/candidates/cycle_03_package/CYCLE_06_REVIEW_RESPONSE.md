# CYCLE_06_REVIEW_RESPONSE

Changed safely in the candidate package only:

- Flagship title and shorttitle now use broad BPT wording instead of framing the result as generic AGN-host behavior.
- Flagship abstract and Section 4 now say the comparison is between broad BPT-selected galaxies and star-forming controls, preserving the same 8,146 pair result and `-1.309 dex` median offset.
- Flagship Section 2 now says "pilot analysis sample" instead of "cached analysis table" and replaces the internal cache phrasing with "marginal distribution checks between the pilot sample and the full public parent."
- Flagship Section 4 now states the sign convention explicitly as `target minus matched control`.
- Flagship interpretation now quotes the narrower-proxy reduction as `-1.309 dex` to `-0.763 dex` from Table 2, without changing the underlying numbers.
- Supplement Section 3.1 now uses US spelling for `neighbor`.
- Supplement figure captions were rewritten into human-readable atlas captions that describe the plotted denominator or proxy rather than the internal filename string.

Refused as requiring new data:

- Any change to numeric results, table values, subset counts, figure paths, or bootstrap intervals.
- Any causal-feedback, quenching, gas-depletion, or maintenance-heating claim beyond association-only or denominator/proxy wording.
- Any attempt to add morphology, aperture-matched SFRs, CO/HI, X-ray, radio, halo/group, outflow, or simulation-mock measurements not present in this package.

The TeX sources were kept compilable in place; the edit stayed inside the approved candidate root and did not touch public/live systems.
