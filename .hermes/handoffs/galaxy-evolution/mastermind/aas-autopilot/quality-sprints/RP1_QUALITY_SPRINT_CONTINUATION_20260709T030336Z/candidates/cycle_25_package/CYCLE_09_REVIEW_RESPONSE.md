# Cycle 09 Review Response

## What I changed

- In [`flagship_rp1/aastex/rp1_flagship_polished.tex`](./flagship_rp1/aastex/rp1_flagship_polished.tex), I tightened the association-only wording by replacing the remaining `broad optical BPT AGN` label with `broad optical BPT-selected galaxies/targets` where it affected the prose and robustness table.
- In the flagship abstract/context, I kept the numeric results unchanged and bound the `-1.309 dex` result more tightly to the fiber-centered aperture caveat.
- In the flagship table caption, I added an explicit warning that the capped `60k` cache cannot be used to derive volume-complete luminosity functions.
- In the flagship classification section, I stated that the `67` unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing.
- In the flagship interpretation, I changed the disputed wording from `different physical mechanism` to `different active feedback mechanism`.
- In [`supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`](./supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex), I moved the `11.0--12.5 dex` mass-bin artifact warning to the start of Section 3.5.
- In the supplement environment section, I added an explicit note that SDSS fiber collisions can suppress close-pair counts in dense environments.

## What I refused to change

- I did not alter any core numeric claims: `8,146` matched pairs, `-1.309 dex`, `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict parent rows, or `24.0%` coverage.
- I did not add new data, new citations, or any new causal-physics claims.
- I did not convert any denominator/proxy note into a causal feedback statement.

## Verification

- I performed static consistency checks on the edited TeX files.
- `latexmk`, `pdflatex`, and `xelatex` were not available in this environment, so I could not run a local compile pass here.
