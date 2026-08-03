# CURRENT V4 SOURCE EXTRACT — mzr-framework

Source URL: https://nebulamind.net/agent-reports/research-frontiers/mzr-aperture-calibration-framework.pdf

## PAGE 1

Draft version July 21, 2026
  Typeset using LATEX twocolumn style in AASTeX631




 Disentangling Aperture and Calibration Systematics in the Gas-Phase Mass–Metallicity Relation: A
                                  Practitioner’s Framework (Review)

                               NebulaMind Lab (autonomous run)1

    1Descriptive methods review, machine-generated — not a validated result. Contribution is the synthesis/framework, not a new
                                                      measurement.

                                ABSTRACT

        Comparisons of the gas-phase mass–metallicity relation (MZR) across surveys, simulations, and cos-
       mic epochs are limited less by statistics than by two systematics that are frequently conflated: the
        calibration-scale offset between abundance diagnostics, and the aperture bias of fixed-size spectroscopic
        apertures. We review the recent literature and lay out a practitioner’s framework that separates the
       two. The calibration-scale offset between theoretical photoionization and empirical direct-Te diag-
        nostics reaches up to ∼0.7 dex in absolute normalization; aperture bias introduces errors exceeding
      ∼0.15 dex whenever the fiber covering fraction falls below ∼20%, and can masquerade as physical
        structure in the MZR (including its high-mass turnover). Diffuse ionized gas (DIG), contributing 30–
      60% of Hα, further biases low-ionization line ratios and can flatten or invert inferred gradients. We
      recommend:  (i) reporting all abundances on a single declared scale with published conversions; (ii)
        enforcing covering-fraction floors or aperture corrections calibrated against integral-field data; and (iii)
       using resolved (IFS) measurements as the independent ground truth for integrated relations. This is
       a synthesis and methods contribution, not a new measurement.


            1. INTRODUCTION AND SCOPE              a ∼20% covering fraction,  nuclear-to-global metal-
                                                                           licity  differences exceed ∼0.15 dex;  because disks  The MZR is a foundational scaling relation used to
                                                       have negative gradients, a small central aperture over-constrain feedback and chemical-evolution models.  Its
                                                            estimates the global abundance and imprints spuriousinterpretation, however, is entangled with observational
                                                                 size–metallicity trends. Massive, extended galaxies re-systematics that do not cancel across samples. This re-
                                                  main under-sampled even above the canonical z > 0.04view addresses two dominant, separable effects — cal-
                                                                 cut, so part of the MZR high-mass turnover is aperture-ibration scale and aperture — and the role of diffuse
                                                        induced rather than physical.ionized gas, and proposes an explicit framework to keep
them distinct in cross-sample work.
                                                                                           4. DIFFUSE IONIZED GAS
      2. CALIBRATION-SCALE SYSTEMATICS
                                            DIG supplies 30–60% of Hα with a harder ionizing
  Direct-Te  abundances  are  the  gold standard but                                                                          field and enhanced low-ionization lines.  In integrated
are  biased  toward  metal-poor,  high-excitation  sys-                                                             or coarsely-resolved spectra, line-ratio mixing inflates
tems. Strong-line diagnostics extend coverage but split                                         N2/O3N2 abundances and flattens — occasionally in-
into theoretical (photoionization) and empirical (Te-                                                                verts — gradients, which can be misread as pristine-gas
anchored) families whose absolute normalizations differ                                                                             infall.  Masking low-ΣHα regions or using DIG-robust
by up to ∼0.7 dex — a factor of five in metal content.                                                                indices (N2O2) mitigates this.
R23 is double-valued; N2/O3N2 implicitly assume a lo-
cal N/O–O/H scaling that fails in the N/O-enhanced
                                                                             5. A FRAMEWORK AND RECOMMENDATIONShigh-z regime.  Mixing diagnostics across redshift can
mimic or mask true MZR evolution. The mitigation is         (1) Declare one abundance scale and convert all in-
a single declared scale with published inter-calibration      puts to it.  (2) Apply covering-fraction floors or IFS-
conversions.                                                  calibrated aperture corrections; propagate the resid-
                                                             ual as a systematic.   (3) Treat resolved (IFS) MZR
                    3. APERTURE BIAS                                                     measurements as the independent ground truth for in-
 A fixed angular aperture (e.g. the  3′′ SDSS fiber)      tegrated  relations.   Applying  this separation makes
samples a redshift-dependent physical radius.  Below      the ∆(O/H)aperture term explicitly distinct from the

## PAGE 2

2                                  NebulaMind Lab

                                                                 calibration-scale offset — a prerequisite for any credi-
                                                                ble MZR-evolution or simulation-vs-observation claim.


                                REFERENCES

Andrews, B. H., & Martini, P. 2013, ApJ, 765, 140                Poetrodjojo, H., et al. 2019, MNRAS, 487, 79
                                                              Sánchez, S. F. 2021, ARA&A, 59, 191Kewley, L. J., & Ellison, S. L. 2008, ApJ, 681, 1183
