# Cycle 42 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_42`
Audit UTC: 2026-07-09T19:41:04Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=271580 sha256=36c0760d78b5cf1eaf0ebde5a7612c3902f24ad85c3764fb952638a5503ab3e8 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=558459 sha256=a0d9fbed03900b0e69eb930b106178b1701d9dff4cd94459368b3858f90b2c8d bad_markers=[]

## Guards
- flagship missing required phrases: []
- supplement missing required phrases: []
- flagship missing numeric invariants: []
- forbidden mock/synthetic data-use hits flagship: []
- forbidden mock/synthetic data-use hits supplement: []

Fatal failures: 0

## Real-data policy
- Never use mock, synthetic, fake, placeholder, or toy data.
- Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.
- New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.
- If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.
- Literature-only sources may motivate future work; they do not become measured NebulaMind results.
- The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied.
