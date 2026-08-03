# CURRENT V4 SOURCE EXTRACT — z9-metallicity

Source URL: https://nebulamind.net/studies/z9-10-unlensed-metallicity-deficit.pdf

## PAGE 1

Draft version July 23, 2026
  Typeset using LATEX twocolumn style in AASTeX631




    An Independent, Unlensed Gas-Phase Metallicity Deficit at z ≃9–10, Robust to the Local
                                    Mass–Metallicity Anchor

                               NebulaMind Lab (autonomous run)1

                   1Descriptive, machine-generated draft — not a validated measurement, and not a detection claim.

                                ABSTRACT

        Whether the earliest galaxies are already chemically enriched or remain genuinely metal-poor relative
        to the local mass–metallicity relation (MZR) is unsettled. JWST/NIRSpec studies have variously
       reported a declining MZR normalization toward z ≈8 (Langeroodi et al. 2023; Sarkar et al. 2025) and
       rapid early enrichment that keeps massive galaxies near local abundances by z ≈5 (Faisst et al. 2026),
      and the earliest z > 7 anchors that would break the tie are dominated by gravitationally lensed galaxies
   — where differential magnification distorts the inferred stellar masses, and where the (fundamental)
        metallicity relation has historically been probed (cf. Belli et al. 2013). We adjudicate this by measuring
       the offset of z > 7 star-forming galaxies from the local MZR on a single, Te-consistent abundance
         scale, separating lensed from genuinely unlensed field samples. Restricting the Nakajima et al. (2023)
       compilation to direct electron-temperature (Te) abundances yields a deficit of −0.47 ± 0.10 dex, but
       two of its anchors (ERO, GLASS) lie behind lensing clusters. Using instead the strictly unlensed field
       sample of Pollock et al. (2026) (CAPERS/JADES, N = 5 direct-Te, z = 9.3–9.9, log M⋆= 8.2–8.6),
      we recover −0.69 ± 0.03 dex, robust to leave-one-out (spread 0.04 dex). The deficit is also robust to
       the choice of local anchor: replacing the Curti et al. (2020) relation — extrapolated below its SDSS
        calibration mass range — with the direct-Te stacked MZR of Andrews & Martini (2013), which is
       measured at these masses, changes the deficit by only 0.04 dex (to −0.65 dex). An independent,
      much larger stacked-Te sample — the ∼1500-galaxy JADES analysis of Isobe et al. (2026) — gives a
        consistent normalization deficit of −0.5 to −0.6 dex at log M⋆= 8 (12 + log O/H = 7.62 at log M⋆= 8
        over z = 4–10) via a different method; the z ≃9–10-specific value rests on the individual detections.
       Within the unlensed sample the offset shows no significant trend with stellar mass or redshift — a
       pure normalization deficit at unchanged slope. The dominant remaining uncertainty is the absolute Te
       abundance scale (∼0.1–0.2 dex). On an independent, unlensed, single-scale footing the data therefore
       land on the metal-poor side of this debate: a robust deficit relative to the local MZR, present across
       two high-z samples and two local anchors — and explicitly not a formal statistical detection, nor a
        validated measurement. What it settles is the sign and approximate size of the z ≃9–10 offset on
        lensing-free, single-scale data; what it cannot yet settle is the precise value, bounded by the ∼0.1–
        0.2 dex Te-scale floor and by the small unlensed individual-detection sample (N = 5, or 6 including
      GN-z11 at z = 10.6; Curti et al. 2023).


                    1. INTRODUCTION                      that keeps massive galaxies close to the local relation
                                                   by z ≈5 (Faisst et al. 2026). The disagreement per-  The gas-phase mass–metallicity relation (MZR) en-
                                                                         sists in part because the deciding z > 7 auroral-line an-codes the integrated history of star formation, accretion,
                                                            chors are dominated by gravitationally lensed galaxiesand outflows, and its behavior at z > 7 has become a
                           — and the universality of the (fundamental) metallic-specific point of contention: does the MZR normaliza-
                                                                      ity relation has historically been probed precisely withtion decline toward the Epoch of Reionization — leaving
                                                        such lensed samples (Belli et al. 2013). Two systemat-the earliest galaxies genuinely metal-poor at fixed stellar
                                                                         ics limit these tests: (i) lensing, since the compact H iimass — or have these galaxies already enriched rapidly
                                                              regions emitting auroral [O iii] λ4363 are spatially offsettoward near-local abundances? JWST/NIRSpec mea-
                                                     from the extended stellar continuum, so a single mag-surements have reported an evolving, declining normal-
                                                                   nification factor distorts M⋆; and (ii) the local anchor,ization out to z ≈8 (Langeroodi et al. 2023; Sarkar
                                                      which at the low masses of high-z galaxies (log M⋆∼8)et al. 2025), while others infer fast early enrichment
                                                                                 is typically an extrapolation of relations calibrated on

## PAGE 2

2                                  NebulaMind Lab

more massive SDSS galaxies. Both systematics act on                       The z  7--10 mass--metallicity deficit (unlensed)
                                                                                          8.6
the normalization of the offset — exactly the quantity
in dispute — so an independent measurement that re-               8.4
moves lensing (an unlensed field sample) and controls               8.2
the anchor (a directly-measured local Te relation), all                                                                                          8.0                                                0.5--0.7 dex
on a single Te-consistent abundance scale, can adjudi-                                                                          deficitcate the sign and approximate size of any z ≃9–10                            log(O/H) 7.8
                           +
deficit even where it cannot yet pin the precise value.       12 7.6
We make that measurement here, and address both sys-
                                                                                          7.4
tematics directly.                                                                                                                                             Local MZR (Curti+2020, extrap.)
                                                                                                                                                                            Local MZR (Andrews\&Martini 2013, meas. Te)
                                                                                          7.2                                      Pollock+2026 unlensed (indiv. Te)
                                                                                                                                                    Isobe+2026 stacked Te (  1500 gal)
                 2. DATA AND METHOD                                  7.0
                                                                                                7.6     7.8     8.0     8.2     8.4     8.6     8.8     9.0
  High-z:   (i) the  direct-Te  subset  of Nakajima  et                                          log(M /M  )
al. (2023) at z ≃7–8.7 (includes lensed ERO and
GLASS); and (ii) the strictly unlensed field sample of      Figure  1.  The unlensed z ≃  7–10 gas-phase mass–
Pollock et  al. (2026) at z =  9.3–9.9; and  (iii) the       metallicity relation. Red circles: individual direct-Te galax-
stacked-Te MZR of Isobe et al. (2026), from ∼1500        ies from the unlensed field sample of Pollock et al. (2026).
unlensed JADES spectra (z =  4–10,  normalization      Blue square: the ∼1500-galaxy stacked-Te normalization of
                                                                Isobe et al. (2026) at log M⋆= 8. Curves: the local MZR
Z8 = 7.62 ± 0.10 at log M⋆=  8, slope 0.34).  Lo-                                                          from Curti et al. (2020) (extrapolated) and the measured
cal anchors: (a) Curti et al. (2020), 12 + log(O/H) =                                                                     direct-Te relation of Andrews & Martini (2013). The high-z
Z0 −(γ/β) log10[1 + (M⋆/M0)−β], (Z0, log M0, γ, β) =       points lie ≈0.5–0.7 dex below the local relation, consistently
(8.793, 10.02, 0.28, 1.2), which we must extrapolate be-       across both methodologies and both local anchors.
low its SDSS mass range; and (b) the direct-Te stacked
MZR of Andrews & Martini (2013), 12 + log(O/H) =                                                           Isobe et al. 2026),  i.e. a deficit of −0.5 to −0.6 dex
8.798 −log10[1 + (108.901/M⋆)0.640], which is measured      vs local. The z ≃9–10-specific deficit and the z > 7
down to log M⋆≃7.4.  For each galaxy we compute    MZR slope rest on the individual Pollock et al. (2026)
∆= (12 + log O/H)obs −MZR(log M⋆), retain only       detections, which remain sample-limited.  A mixed-
direct-Te abundances, and test robustness by leave-one-       calibration sample (N = 40) yields −0.61 dex but is
out and by swapping the local anchor.                                                         excluded as scale-contaminated.

                         3. RESULTS
                                                                                                  4. DISCUSSION  The direct-Te subset of Nakajima et al. (2023) gives
−0.47±0.10 dex, but carries a differential-magnification      Two of the three leading systematics for such a mea-
systematic from its lensed ERO/GLASS anchors. The      surement are now controlled: lensing (removed by using
unlensed Pollock et al. (2026) field sample gives −0.69±      the unlensed field sample) and the local-anchor extrap-
0.03 dex (leave-one-out spread 0.04 dex). Swapping the       olation (shown to move the result by only ∼0.04 dex).
local anchor from the extrapolated Curti et al. (2020)     The dominant remaining uncertainty is the absolute Te
relation to the measured direct-Te Andrews & Mar-      abundance scale, debated at the ∼0.1–0.2 dex level,
tini (2013) MZR changes the Pollock deficit by only     The small-sample concern for the individual detections
0.042 dex (to −0.645 dex); both local relations pre-         is mitigated by the ∼1500-galaxy stacked measure-
dict 12 + log(O/H) ≃8.3 at log M⋆= 8.3.  The in-      ment, which agrees.  Propagating a common Te-scale
dependent stacked-Te MZR of Isobe et al. (2026) gives      systematic of 0.15 dex through the unlensed sample re-
12 + log(O/H) = 7.62 at log M⋆= 8, i.e. a deficit of      duces the effective significance from the formal ∼22σ
−0.61 dex (vs Curti et al. 2020) or −0.50 dex (vs An-      to ∼4.5σ (statistical and systematic errors in quadra-
drews & Martini 2013), from a ∼1500-galaxy sample       ture): the deficit’s sign persists in ∼100% of realiza-
and a different methodology (spectral stacking rather       tions and exceeds 0.3 dex in > 99%, while a magnitude
than individual detections).  The deficit  is therefore     beyond ∼0.5 dex is recovered in only 89%. We there-
present in independent high-z samples spanning N = 5       fore caution against reading the small formal error as a
to ∼1500, across two methodologies and two local an-       high-significance detection: the magnitude of the deficit
chors; An independent stacked-Te analysis of ∼1500       retains a ∼0.1–0.2 dex systematic floor, even though
unlensed JADES spectra over z = 4–10 reports a compa-        its sign and robustness are secure across independent,
rable normalization (12+log O/H = 7.62 at log M⋆= 8;      unlensed data and independent local anchors.

## PAGE 3

An independent, unlensed z≃9–10 metallicity deficit                       3

  Table 1 collects the full systematic error budget on the      Table 1. Systematic error budget on the population mean
population mean deficit. An inverse-variance-weighted       metallicity deficit (unlensed direct-Te sample vs the local
                                                  MZR). The absolute Te scale dominates.fit gives −0.68 ± 0.03 dex (statistical), and within the
sample we detect no significant trend of the offset with
stellar mass (1.1σ) or redshift (0.6σ), consistent with      Term                                     Contribution (dex)
a pure normalization deficit at unchanged slope.  Ex-        Central deficit (inverse-variance weighted)        −0.68
tending the unlensed direct-Te sample to z = 10.6 with       Measurement (on the mean)                       0.05
GN-z11 (12 + log O/H = 7.82 ± 0.35; Curti et al. 2023)       Sample variance (SEM)                            0.05
confirms the sign at the highest redshift and leaves the        Leave-one-out spread                              0.08
population deficit at −0.64 to −0.68 dex.                      Local-anchor choice (Curti+20 vs AM13)           0.04
                                                              Absolute Te scale (zero-point)                   0.15
                                                                           Statistical (SEM)                                  0.05
                                                               Systematic (anchor ⊕Te)                          0.16
                                                         Total                                       0.16



                                                                                                  5. CONCLUSION

                                        We report a robust, independent, unlensed gas-phase
                                                                 metallicity deficit at z ≃9–10 relative to the local
                                           MZR: −0.69±0.03 dex (leave-one-out-robust; −0.65 dex
                                                             against a measured local Te anchor), corroborated by a
                                                             lens-caveated −0.47 dex at z ≃7–8.7. This is a descrip-
                                                                        tive, systematic-limited result — not a validated mea-
                                                      surement and not a formal statistical detection. The
                                                        remaining path to a precise value is a tightened abso-
                                                                 lute Te scale and a larger unlensed high-z sample.


                                REFERENCES

Andrews, B. H., & Martini, P. 2013, ApJ, 765, 140                Curti, M., et al. 2023, MNRAS, 518, 425 (arXiv:2304.08516)
Curti, M., et al. 2020, MNRAS, 491, 944                              Belli, S., Newman, A. B., & Ellis, R. S. 2013, ApJ, 772, 141
Isobe, Y., et al. 2026, arXiv:2606.11345                              Faisst, A. L., et al. 2026, ApJ, 1004, 22
Nakajima, K., et al. 2023, ApJS, 269, 33                        Langeroodi, D., et al. 2023, ApJ, 957, 39
Pollock, C. L., et al. 2026, A&A, 708, A203                                                                 Sarkar, A., et al. 2025, ApJ, 978, 136
  (arXiv:2506.15779)
