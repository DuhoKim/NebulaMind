# Cycle 5 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_05`
Audit UTC: 2026-07-09T14:50:22Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=262871 sha256=ab1683f74cf0afd25884a5e0a50c1869e75ac21b65ad516246cef23c83f7aad7 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=550921 sha256=215444abdd59075159480870dfae5c5ee3ea45de5a44fa832c0fdb167aedf350 bad_markers=[]

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
