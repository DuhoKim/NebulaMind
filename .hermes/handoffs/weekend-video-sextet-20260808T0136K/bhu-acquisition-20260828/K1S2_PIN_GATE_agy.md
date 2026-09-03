ACCESS_SHA=54f992aebf7f9c404c2927991410960042b9706afd7273bfe985174325c01b88
ACCESS_SHA_CODEX=b2ef589acc4a569d7cb395151e60e88078845832ddd7229496d3eeb091a552b8
ACCESS_SHA_CLAUDE=55e27c2112231cb45037fa0419bf7f0369d8e1de532ff3ceb13213835af71979
PIN_GATE=PASS_WITH_REPAIRS

## MASTER PIN SHEET
* **Row 1 (COMPAS commit):** `e728869cef4fc21d22e7db6e6645a8f878ada2b2`. (Merge: Both seats identified the same commit and reported a build failure due to missing Boost/GSL/HDF5 dependencies. This is recorded as a resource fact, not a gate failure).
* **Row 2 (Remnant/cap options):** Options `--remnant-mass-prescription`, `--fryer-supernova-engine`, and `--maximum-neutron-star-mass` identified correctly. (Merge).
* **Row 3 (Cap grid):** `{1.97, 2.50, 3.50} M_sun`. (Codex). Selected because every value is strictly sentence-pinned (e.g., Ozel L1657-1659, Fryer L1041-1051, 1052-1063), whereas Claude relies in part on a figure caption.
* **Row 4 (SFH):** Madau & Dickinson 2014 eq. 15. (Merge).
* **Row 5 (C2 Test):** KS test with n=15 masses. (Claude). Claude correctly includes the slow pulsar J1141-6545, which Ozel explicitly notes is near birth mass (L720-723).
* **Row 6 (MC Size/Seeds):** 3,000,000 binaries per point, run in 3 batches. (Codex). Selected because it explicitly splits the run to compute the Monte-Carlo error from across-seed dispersion, directly satisfying the prereg requirement.
* **Row 7 (CE & Kicks):** Code defaults and the MAXWELLIAN alternative (σ=265 km/s). (Claude). Selected for accurately citing the COMPAS paper's fiducial alternative.

## Driver Settings Needed
* `--remnant-mass-prescription FRYER2012` (overrides the code's MULLERMANDEL default).
* `--fryer-supernova-engine DELAYED` (or `RAPID` for the alternative grid point).
* Adjust metallicity integration/scaling to use `Z☉ = 0.02` (the code default is `0.0142`).

## Failed Receipts
* **Codex Row 5:** Claims lines 313-320 in Ozel & Freire are "censored systems". The paper actually labels them "Non-recycled pulsars with massive WD companions" and explicitly states (L720-723) that they are likely near their birth masses. Furthermore, J1141-6545 has a precise, uncensored mass measurement of 1.27±0.01 M☉. The word "censored" does not appear in the text.

## Summary
The gate passes with repairs by synthesizing the strengths of both sheets. Codex provides the robust, entirely sentence-pinned cap grid and properly structured Monte-Carlo batches for error estimation. Claude correctly parses the observational sample by retaining a valid slow pulsar, and accurately sources the alternative kick prescription. Both correctly identify the commit and necessary option flags. The driver script must explicitly set Fryer 2012 and address the Z☉=0.02 mismatch against the code default.
