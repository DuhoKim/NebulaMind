# Cycle 6 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_06`
Audit UTC: 2026-07-09T14:00:28Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=262957 sha256=df98f3c1bfd727017fd186c5849c8f0cbe2f0ebb806a56e2b840fac1491f4a05 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=551025 sha256=0d43a550d770f71ab7cfc8cd124cc9f2774e92849742606f1dcdf8175f340cd3 bad_markers=[]

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
