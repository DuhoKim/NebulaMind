GPT1_P2B_DONE

Blind independent P2b computation completed without reading the prohibited P2b/P2-P4 or S2/S3 materials.

Primary result (Legendre cosine dipole, sky-mean normalised):
- A1/(x_off/r_*c) = 2.28714342 before conservative source dilution.
- Passive-source/opacity envelope = 1.96856259 to 2.28714342.
- |x_off|/r_*c < 5.93557e-4 preferred; < 6.89614e-4 maximally diluted.

Verification:
- main computation reran successfully;
- Python compilation passed;
- centred-sky and source-limit assertions passed (`ALL_CHECKS_PASS`);
- interpolation thinning through stride 8 changed the coefficient by less than 2.2e-6 relative;
- no commits made; all outputs are in this directory.

See README.md for choices, derivation, caveats, and limiting checks.
