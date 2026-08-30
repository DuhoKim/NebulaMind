SOURCE_OVERSTATES_ACT_DESI_TIER_UNCHANGED

# CGATE B59 verdict

I independently checked the pinned artifacts and their hashes. The three abstract captures match the brief's pinned SHA-256 prefixes (`4a0a05ab49d6`, `1c1f4b85f53b`, and `6c4cc64c37f7`), and I checked the full pinned DESI DR2 clean text (`cf72282ab92c...`). I did not consult the other gate seat.

## 1. ACT DR6

The gloss is not a fair summary of the cited ACT paper. ACT's abstract says both that the spectra are well fit by ΛCDM and, expressly, that the authors find “no departure from spatial flatness.” It also reports no evidence for the excess lensing that motivates the closed-Planck interpretation. A posterior in Fig. 9 may have a slightly negative central value while remaining compatible with zero, but elevating that visual displacement into “ACT ... suggest[s] a slight preference for positive curvature” suppresses the authors' stated inference. At best this is a cherry-picked description of a posterior center, not ACT's result; as written in a sequence of allegedly same-direction observational hints, it is misleading.

## 2. DESI

The DESI gloss is also not fair.

- DESI 2024 VI's abstract says DESI BAO alone are consistent with standard flat ΛCDM.
- DESI DR2 says that *most* of the paper assumes `Ω_K = 0`, but it does not only fit a fixed-flat baseline. It explicitly defines an extended `ΛCDM+Ω_K` fit and states: “We also allow for spatial curvature to vary ... and we do not find a significant preference for a non-flat ΛCDM model.” Thus the prior CGATE B14 testimony that the analysis simply “assumes Ω_K = 0” was directionally useful but too categorical and must be narrowed.
- More decisively, DR2 Table 5 does not even have a closed-curvature central trend. With the paper's convention (closed/positive spatial curvature means `Ω_K < 0`), DESI alone gives `10^3 Ω_K = 25 ± 41`, while DESI+CMB gives `10^3 Ω_K = 2.3 ± 1.1`. Both central values are on the `Ω_K > 0` (open), not `Ω_K < 0` (closed), side. The authors nevertheless decline to claim significant non-flatness.

Therefore “latest DESI data echo this trend” and “hinting at a mild preference for positive curvature” reverse the sign of the displayed DR2 central constraints and conflict with the paper's conclusion.

## 3. Di Valentino et al. 2020

This citation is accurate as an attribution to Di Valentino, Melchiorri, and Silk's analysis. Their abstract explicitly says the Planck CMB spectra prefer positive curvature at more than 99% confidence and argues that closure can explain the anomalous lensing amplitude. That supports the source paper's claim that this particular analysis argues closed.

The attribution must remain bounded: it is Di Valentino et al.'s interpretation of Planck spectra, not a license to describe the later ACT and DESI conclusions as confirming the same trend. It also does not erase the already-pinned Planck combined-data resolution toward flatness.

## 4. Record handling and tier

The present “seat's testimony, not verified here” language should now be upgraded to a primary-source-bound clarification. A precise replacement is:

> Di Valentino et al. 2020 genuinely argue for closed curvature from Planck spectra. ACT DR6 instead concludes that it finds no departure from spatial flatness. DESI 2024 VI is consistent with flat ΛCDM, and DESI DR2's explicit curvature extension finds no significant non-flat preference; its reported central `Ω_K` values are on the open, not closed, side. The entry 54 source therefore overstates ACT and DESI as same-direction support.

This is a citation-accuracy clarification, not a tier correction. Entry 54's `QUALITATIVE-DIRECTIONAL` tier rests on its own conditional prediction `Ω_k < 0`, not on whether the cited contemporary measurements favor that sign. Tier **UNCHANGED**.

## Predicate note: are the abstracts sufficient?

The ACT abstract is sufficient to rule on the fairness of the source's characterization because it contains the authors' explicit curvature conclusion. Full ACT text/Fig. 9 would be needed only to reconstruct exactly which posterior displacement the source cherry-picked; it is not needed to decide whether “ACT suggests” fairly states the paper's conclusion. The DESI 2024 abstract is sufficient for that release's headline, but not for the claim that DESI merely fixed flatness; the full DR2 text was necessary and changes that detail. The Di Valentino abstract is sufficient because the disputed proposition is stated explicitly in it.
