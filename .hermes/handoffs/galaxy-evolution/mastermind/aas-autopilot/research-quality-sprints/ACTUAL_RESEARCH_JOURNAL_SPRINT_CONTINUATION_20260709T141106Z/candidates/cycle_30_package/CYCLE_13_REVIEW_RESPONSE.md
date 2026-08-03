# Cycle 13 Review Response

## What I changed

- In [rp1_flagship_polished.tex](./flagship_rp1/aastex/rp1_flagship_polished.tex), I replaced software-style wording such as `pilot cache`, `60k-row`, and `rows` with astronomy-native sample language.
- In [rp1_flagship_polished.tex](./flagship_rp1/aastex/rp1_flagship_polished.tex), I added an explicit definition separating broad BPT selection from the stricter Seyfert-like proxy so the LINER-like exclusion is clear earlier in the paper.
- In [rp1_flagship_polished.tex](./flagship_rp1/aastex/rp1_flagship_polished.tex), I tightened the association-only and aperture-caveat language without changing any numeric results, figure paths, or claims.
- In [rp1_flagship_polished.tex](./flagship_rp1/aastex/rp1_flagship_polished.tex), I named the supplementary document by its exact title in the conclusion.
- In [supplementary_denominator_atlas.tex](./supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex), I replaced `pilot cache`, `cached rows`, and `row-level` phrasing with `pilot sample`, `galaxies`, and `galaxy-by-galaxy` wording.
- In [supplementary_denominator_atlas.tex](./supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex), I added a short intro sentence stating that the eight subsections are distinct follow-up domains bounded by the same optical selection effect.
- In [supplementary_denominator_atlas.tex](./supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex), I renamed the key section headings to avoid implying measured outflow kinematics or gas depletion: `Environment baseline` to `Relative neighbor-count baseline`, `Outflow-kinematics denominator` to `High-excitation optical AGN baseline`, and `Gas-depletion denominator` to `Low-sSFR optical denominator`.
- In [supplementary_denominator_atlas.tex](./supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex), I kept the citation-role split explicit: SDSS/BPT/catalog citations describe the current optical denominator, while radio/X-ray/CO/HI/outflow/simulation citations are future-data motivation only.

## What I did not change

- I did not change any numeric results, including `8,146` pairs, `-1.309` dex, `[-1.334,-1.283]` dex, `60,000`, `249,917`, or `24.0%`.
- I did not add any new data, any new measurements, or any new citations.
- I did not convert denominator or proxy notes into causal feedback claims.
- I did not implement morphology metrics, volume-completeness weighting, or CO/HI cross-matches because those require new external data.

## Verification

- I attempted a local TeX compile check with `latexmk`, but the tool is not installed in this environment, so I could not complete a compile verification pass here.

