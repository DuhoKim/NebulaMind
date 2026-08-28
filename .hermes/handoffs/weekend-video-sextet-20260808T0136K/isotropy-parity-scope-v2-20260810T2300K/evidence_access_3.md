URL: https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3

[Skip to content](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#content)

- [Persistent Problems Since PDR1/2](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#hsc-link-0)
- [Over-estimated CModel fluxes](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#hsc-link-1)
- [FGCM zero-point non-uniformity](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#hsc-link-2)
- [r/i vs r2/i2 filter differences](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#hsc-link-3)
- [Missing data in DEEP2-F3](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#hsc-link-4)
- [Catastrophic flux calibration failures](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#hsc-link-5)
- [Pixel flags in UltraDeep fields](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#hsc-link-6)
- [Processing failure in UD-SXDS : ADDED ON 14. Dec. 2021](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/#hsc-link-7)

This page summarizes known problems in our data. Please carefully go over the page before you use
our data for your science. There may be problems that have gone unnoticed and if you discover
a new problem, please [let us know](mailto:hsc_pdr@hsc-software.mtk.nao.ac.jp).
We will continue to improve the pipeline to mitigate these problems for future data releases.

## Persistent Problems Since PDR1/2

While we have put efforts in improving the data processing pipeline, there are issues persisting from our previous releases, some of which are fundamentally difficult problems.

- One such fundamental problem is the over-shredding of nearby galaxies. For instance, star-forming regions and arms of a spiral galaxy can be deblended into separate pieces. It is difficult to distinguish multiple galaxies blended with each other from a single galaxy with structure.
- Another fundamental difficulty with the deblending is that it occasionally fails to cleanly deblend sources in crowded regions such as the dense core of galaxy clusters.  There is no easy solution to this problem. There is a [multi-color deblender,](https://ui.adsabs.harvard.edu/abs/2018A%26C....24..129M/abstract) which we do not use in this release, and we hope it will help.  We also note that the pipeline is not optimized for very crowded fields such as star clusters or dwarf galaxies around the Milky Way Galaxy. The user should carefully check the images and catalogs in crowded regions before using them.
- The NB387 data should also be used with caution because this is a rather difficult filter to calibrate. We infer NB387 magnitudes by applying color-terms to the PS1 gr photometry when we calibrate its zero-point. We use the stellar library from Pickles (1998) to derive the color-terms. Most of the stars in this library are close to solar metallicity, but the stars that we use for calibration are faint halo stars, which are likely to have subsolar metallicities.The NB387 filter is quite sensitive to the metallicity of stars and the PS1 gr photometry does not fully capture the metallicity variation. As we have reported on [the known issue page for PDR2](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems-2/), the photometric zero-point can be off as much as 0.45 mag. This is from a comparison with SDSS spectroscopic stars and is still a tentative number. Further investigations are needed.
- There are artifacts left in the coadd images. Most obvious artifacts are optical ghosts around bright stars. We do make an attempt to remove them, but we are not always successful, especially in regions where only a few visits have been taken. Also, our algorithm cannot remove artifacts if they stay at similar positions on the sky. This is often the case in the D/UD fields, where the dithers are relatively small (several arcmin) and optical ghosts stay at similar positions. An additional algorithm would be needed to fully eliminate them.

## Over-estimated CModel fluxes

We perform CModel photometry in our measurements (Section 4.9.9 of [Bosch et al. 2018](https://ui.adsabs.harvard.edu/abs/2018PASJ...70S...5B/abstract)). This is for galaxy photometry and is expected to deliver good colors of extended sources.  In PDR2, there was a population of apparently faint objects with large CModel fluxes. Visual inspections of those objects on the coadds indicate that their CModel fluxes are likely over-estimated.  We suspect that the over-estimated fluxes are at least partly due to the global sky subtraction applied in PDR2; it preserves wings of bright objects and it could contaminate the outer parts of nearby objects’ footprints. It could also be due to the deblender; HSC images are very deep and the deblender often faces a difficult problem of deblending multiple sources simultaneously (especially when the extended wings are preserved), and the deblender may leave residual fluxes in crowded regions, which then contaminate the outskirts of nearby objects. As CModel is relatively sensitive to fluxes in the outer parts, the flux can be over-estimated.

To further explore this, we show in the figure below a small piece of the UD-COSMOS field.  The ellipses illustrate inferred object sizes from CModel, and as can be seen, most objects have ellipses with reasonable sizes.  However, there are ellipses that appear much too large given the visual sizes of objects. They are indicated as the red ellipses and they are the problematic objects with over-estimated fluxes.

![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/08/cmodel_ellipse-1024x707.png)

Let us be quantitative about these objects. A way to identify them is to compare the fixed-aperture (e.g., 2 arcsec) photometry and CModel photometry because the fixed-aperture photometry is insensitive to fluxes in the outer parts of footprints and is thus relatively robust against flux contamination from nearby sources.  The figures below makes this comparison in D/UD.  The figures are for the i-band, but the same trends can be seen in all the filters.  In PDR1, there is a reasonable agreement between the two photometric measurements.  In contrast, in PDR2, there are many objects around 25-26th magnitudes with large magnitude differences. At this faint level, most sources are compact and the aperture photometry should be a reasonable proxy for total flux. Thus, CModel is likely too bright by ~3 magnitudes or more for many of these sources.

The fraction of objects with a magnitude difference of more than 1~mag and detected at S/N>5 is about 6% in D/UD and 5% in Wide.  In this release (PDR3), the number of such objects is significantly reduced as shown in the right panel and the fraction decreases to 3% and 2% in D/UD and Wide, respectively.  Care must be taken when comparing these numbers, but it is clear that PDR3 is better behaved than PDR2.  The fraction is only 0.5% in PDR1 UD, although the data were rather shallow at that time.  We note that these numbers should be regarded as rough numbers because we apply only a minimal set of flag cuts here: only primary objects with no CModel/aperture measurement failure.

We encourage the user to check the consistency between CModel and aperture photometry for faint sources.  If the user is interested in relatively faint sources (e.g., >~22 mag), the PSF-matched aperture photometry (convolvedflux) is more reliable; it is fixed-aperture photometry performed on images smoothed to a common seeing size across bands and is a robust measure of colors. It does not capture the total flux, but it is fairly robust against deblending effects and residual flux in the outskirts.

![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/08/mag_comp_pdr1.png)

![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/08/mag_comp_pdr2.png)

![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/08/mag_comp_pdr3.png)

Magnitude differences in i-band between 2 arcsec aperture and CModel as a function of the 2 arcsec aperture magnitude in three data releases, PDR1, PDR2, and PDR3 from left to right. Objects with aperture photometry with S/N>5 in UD (PDR1) and D/UD (PDR2 and 3) are plotted. For comparison, 50,000 objects are randomly chosen and plotted in each panel.

## FGCM zero-point non-uniformity

There is an issue with the photometric zero-point introduced by the local sky subtraction performed internally in FGCM. This has been mitigated by the stellar sequence regression and we encourage the user to apply the zero-point offsets.  Note that these offsets have not been applied to the photometry in the database (it is as quoted by the pipeline). The user can apply these correction by joining the magnitude offset tables: join `pdr3_{dud,wide}.stellar_sequence_offsets` with `skymap_id`.  The magnitude offset is estimated for each patch (not for each object) and the user needs to use `skymap_id` to join tables.

## r/i vs r2/i2 filter differences

The r and i band filters have radial dependence in their transmissions, and we have replaced them with r2 and i2 filters with better uniformity.  The old and new filters are similar, but not identical, and they introduce spatially varying response function in the survey.  To account for it, we use the effective response function to translate the r and i band photometry into fiducial r2 and i2 photometry.  The estimated offsets have not been applied to the photometry in the database (it is as quoted by the pipeline). The user can apply the correction by joining the magnitude offset table, `pdr3_{dud,wide}.mag_corr`.  The correction is estimated for each object.  So, you want to join tables using object\_id.  We failed to estimate the correction for a very small fraction of objects and the correction is not available for objects observed in a single filter by definition.  Always do `left join`.

## Missing data in DEEP2-F3

Due to a processing error, seven i-band visits (31.5 min in total) are excluded from tract=9463 (DEEP2-F3) from the coaddition stage and the tract has i2-band data only.  The coadd is thus shallower than it should be by ~0.2 mag. This will be fixed in our next release.

## Catastrophic flux calibration failures

The joint flux calibration is performed using FGCM, but a tiny fraction of the CCD images have incorrect calibrations applied due to bad outlier rejection (25 CCD images out of 2,822,678 CCD images used for Wide). We identify these CCDs as an image with a strong spatial gradient in the flux calibration, with at least one pixel having an inverted flux (i.e., the calibration applied to that pixel is negative).  There are probably more CCDs that are less problematic but still bad.  This problem is visible particularly in warps because these are the images that are flux-calibrated by FGCM.  The warps are then added together to generate coadds. We have visually inspected the potentially affected coadds, but we see no obvious artifact. It may be that the artifact rejection algorithm rejected those problematic warps during the coaddition. It is unlikely that the coadd images as well as catalogs are significantly affected, but warps are affected. We provide a list of problematic images below.

#### [List of affected CCDs](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/\#1628783902677-78a2edd8-6868)

|     |     |     |
| --- | --- | --- |
| Filter | Visit | CCD |
| HSC-G | 103020 | 065 |
| HSC-G | 126312 | 011 |
| HSC-G | 183672 | 014 |
| HSC-G | 183914 | 053 |
| HSC-G | 193802 | 017 |
| HSC-R | 11392 | 084 |
| HSC-R | 23912 | 024 |
| HSC-R | 23918 | 081 |
| HSC-R | 23924 | 078 |
| HSC-R2 | 105194 | 086 |
| HSC-R2 | 105228 | 050 |
| HSC-R2 | 203718 | 039 |
| HSC-R2 | 203766 | 000 |
| HSC-R2 | 96740 | 067 |
| HSC-I2 | 101534 | 067 |
| HSC-I2 | 177594 | 095 |
| HSC-I2 | 177630 | 072 |
| HSC-I2 | 177672 | 086 |
| HSC-Y | 00442 | 091 |
| HSC-Y | 00458 | 049 |
| HSC-Y | 00464 | 093 |
| HSC-Y | 00468 | 084 |
| HSC-Y | 135836 | 021 |
| HSC-Y | 27032 | 032 |
| HSC-Y | 27042 | 008 |

## Pixel flags in UltraDeep fields

A flag, `pixelflags_crcenter` is set for an object if a cosmic ray is detected within 3 pixels from the center of that object in any of the individual visits going into the coadd.  In the CCD processing, cosmic rays are identified and interpolated, but because interpolation does not normally work well at object centers, we recommend excluding objects with this flag set to select objects with clean photometry in the Wide area.

However, doing so can be problematic in the UD fields, which include 100 or more visits, any one of which could be affected by a cosmic ray, giving a substantial chance of the object being excluded. The figure below illustrates the effect. The figure shows the number of objects in the COSMOS field, on a grid of 0.05 deg, after excluding objects with  `pixelflags_crcenter` applied. The number density in the UD region is only 2/3 that in the surrounding D pointings, even though the UD data are considerably deeper.  The figure is for the $i$-band, but the other filters show exactly the same trend.  If we do not apply the flag cut, the UD region shows a considerably larger source density than the Deep pointings, as expected. We therefore suggest not to apply the cosmic ray and interpolated pixel flags in D/UD, where there is a large number of visits and effects of cosmic rays are minor on coadds.

[![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/08/cosmos_nobj-500x428.png)](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/08/cosmos_nobj.png)

Number of detected objects on a 0.05 deg grid after rejecting objects with the cosmic ray pixel flag set in the D/UD-COSMOS field. The color-coding shows the number of objects. Recall the central pointing is the UD pointing and the surrounding 4 pointings are D pointings.

## Processing failure in UD-SXDS : ADDED ON 14. Dec. 2021

It was recently pointed out by a public user that there is a sharp edge in the depth map of UD-SXDS.  It is most evident in the y-band ( [link to the plot](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/qa/figs/full/dud_sxds_depth.png)), but other filters are affected as well.  The problematic filter + tract are

|     |     |
| --- | --- |
| Filter | Tract |
| g-band | 8766, 9463 |
| i-band | 8524, 9463 |
| y-band | 8523, 8765 |

We hope to reprocess these tracts and make an incremental release.  The timeline is TBD.

**Note added on 29 August 2022**: we have reprocessed these tracts.  See [this pag](https://hsc-release.mtk.nao.ac.jp/doc/index.php/pdr3-d-ud-reprocessing/) e for details.

![](<Base64-Image-Removed>)

[Previous image](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/)[Next image](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/)
