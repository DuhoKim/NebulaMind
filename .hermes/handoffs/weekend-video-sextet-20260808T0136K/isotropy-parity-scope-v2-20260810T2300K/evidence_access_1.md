URL: https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3

[Skip to content](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/#content)

HSC-SSP PDR3 includes over 600 square degrees of multi-band data at the nominal survey depth.  See the figures below for the survey footprints.  The blue and green areas show the Wide and Deep+UltraDeep layers, respectively.  The darker blue regions are covered in more filters (max. 5).

[![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/07/pdr3_0h-500x165.png)](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/07/pdr3_0h-1024x338.png)

[![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/07/pdr3_12h-500x165.png)](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/07/pdr3_12h-1024x338.png)

[![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/07/pdr3_north-500x165.png)](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/07/pdr3_north-1024x338.png)

[![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/07/pdr3_table-500x161.png)](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/07/pdr3_table-1024x330.png)

The table gives a quick overview of the quality of our data.  The depths are given as 5 sigma limiting magnitudes for point sources.  Area is the area covered in at least 1 exposure in each filter.

### NEW : Reprocessed Deep/UltraDeep Data

**Incremental Release 3:** As described in the [known issue page](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/), several tracts in the D/UD layer suffered from processing failures and some of the good exposures were not included in the final coadds, which resulted in shallower depths in those tracts. We have reprocessed the entire D/UD layer and the deeper data are now available. See the following page for details.

[Reprocessed D/UD data](https://hsc-release.mtk.nao.ac.jp/doc/index.php/pdr3-d-ud-reprocessing/ "PDR3 D/UD reprocessing")

## Data Retrieval

The data can be retrieved in multiple ways.  The simplest way to retrieve catalog data is to use the database.  We have online/offline SQL tools.  For image data, most users will find hscMap, an online image browser, very useful.  For binary files, we have a data search tool as well as image cutout tool.  All these tools are summarized in [the Data Access page](https://hsc-release.mtk.nao.ac.jp/doc/index.php/data-access__pdr3/).  In order to access the data, you first have to [sign up for an account](https://hsc-release.mtk.nao.ac.jp/datasearch/new_user/new).  Before you use our data products, we strongly recommend you to go over [the data release paper](https://www2.nao.ac.jp/~masayuki/upload/hsc_pdr3_submitted.pdf) and [the Known Problems page](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/).  If you use the HSC data in your publication, please [acknowledge us](https://hsc-release.mtk.nao.ac.jp/doc/index.php/acknowledging-hsc__pdr3/).  This site serves only the processed data.  Raw data can be retrieved from [SMOKA](http://smoka.nao.ac.jp/).

### Data Quality

We have performed a number of validation tests for our data products.  A complete set of the plots can be found here.

[Quality Assurance Plots](https://hsc-release.mtk.nao.ac.jp/doc/index.php/quality-assurance-plots__pdr3/ "Quality Assurance Plots (PDR3)")

[Stellar Sequence](https://hsc-release.mtk.nao.ac.jp/doc/index.php/stellar-sequence__pdr3/ "Stellar Sequence (PDR3)")

[Star/Galaxy Separation](https://hsc-release.mtk.nao.ac.jp/doc/index.php/star-galaxy-separation__pdr3/ "Star/Galaxy Separation (PDR3)")

## Known Problems

Although our data are of high quality, there are several known problems.  We have a dedicated page to summarize them.  Please check out the page before you use our data for your science.

[Dedicated Page for Known Problems](https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3/ "Known Problems (PDR3)")

## Pipeline Products

[![](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/08/pdr3_processing-339x500.png)](https://hsc-release.mtk.nao.ac.jp/doc/wp-content/uploads/2021/08/pdr3_processing-694x1024.png)

The figure summarizes some of the most important pipeline outputs from each processing stage.  All the files are available for download.  However, detailed shape measurements (HSM shapes) and deblended images (heavy footprints) are withheld from the release.  The files shown in red are new files in PDR3.

- [Single-frame](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/#1487734079285-f2c1b712-1aca)
- [Joint calibration](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/#1487734079450-14e2c80d-3e95)
- [Coadd](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/#1487734685047-f0027323-1de9)
- [Multi-band](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/#1487734439066-365ea063-ef9e)

#### [Single-frame](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/\#1487734079285-f2c1b712-1aca)

**ICSRC:** Catalog of bright sources detected and measured on a CCD, and used in astrometric and photometric calibration. (FITS BINTABLE)

**SRC:** Catalog of sources detected and measured on a CCD, output from the final stage of the single frame processing. See CALSRC, too. (FITS BINTABLE)

**SRCMATCH:** Source catalog (SRC) cross-matched with the external reference (PS1) sources. Identification numbers and separation angles in cross-matching are recorded for the external sources. (FITS BINTABLE)

**SRCMATCHFULL:** Another form of SRCMATCH, in which coordinates and fluxes of the external sources are explicitly listed (de-normalized) rather than listing the identification numbers only. (FITS BINTABLE)

**CORR:** CCD image with calibrated coordinates and magnitude zeropoint from the single frame processing. See CALEXP, too. (Muliti-extension FITS IMAGE + BINTABLE)

**BKGD:** Sky background model subtracted from a CCD image. (Multi-extension FITS IMAGE)

**skyCorr:** Residual pattern to be subtracted from a CORR image to get the global sky subtraction applied. (Multi-extension FITS IMAGE)

#### [Joint calibration](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/\#1487734079450-14e2c80d-3e95)

The following files are from the joint calibration process.  They are not inteded to be used by the user, but we provide them for completeness.

**jointcal\_wcs:**

**atmosphere:**

**fgcm\_photoCalib:**

#### [Coadd](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/\#1487734685047-f0027323-1de9)

**det:** List of source positions and footprints detected on a coadd patch. (FITS BINTABLE)

**det\_bkgd:** Constant background subtracted in the object detection phase.

**warp:** Image of a single visit (CORR) transformed onto a destination tangential plane in a tract. (Multi-extension FITS IMAGE + BINTABLE)

**psfMatchedWarp:** warp image convolved to a common seeing (Multi-extension FITS IMAGE + BINTABLE).

**calexp:** Coadd image **with the local sky subtraction applied** (Multi-extension FITS IMAGE + BINTABLE).

**$(patch)\_nImage:** Image representing a number of visits contributed to each pixel in coaddition. (Multi-extension FITS Image)

**$(patch):** Coadd image **with the global sky subtraction applied** (Multi-extension FITS IMAGE + BINTABLE).

The photometric zero-point of the coadd images is 27.0 mag. However, this is not accurate at a few percent level because aperture corrections, which account for missing light from the aperture used for the photometric calibration, cannot be applied at the image level.

#### [Multi-band](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/\#1487734439066-365ea063-ef9e)

**mergeDet:** Merged list of source positions and footprints from all filters in a coadd patch. (FITS BINTABLE)

**meas:** Single-band source catalog measured on each of sources in a coadd image listed in mergeDet. Peak positions and shapes of sources are determined in a band being measured. (FITS BINTABLE)

**srcMatch:** Single-band source catalog (meas) cross-matched with the external reference (PS1) sources. (FITS BINTABLE)

**src** **MatchFull:** Another form of srcMatch.  Coordinates and fluxes of the external sources are explicitly listed (de-normalized) in the same manner as in SRCMATCHFULL. (FITS BINTABLE)

**ref:** List of source positions and shapes determined by merging results of the single-band measurements (meas) in a coadd. Reference catalog used for the final forced measurement. (FITS BINTABLE)

**forced\_src:** Source catalog from a multi-band measurement, which is performed on each of sources listed in the ref catalog. Positions and shapes are held fixed in the reference band in the measurements. Final catalog from the forced photometry. (FITS BINTABLE)

## Additional Products

In addition to the pipeline products, we also provide a collection of public spectroscopic redshifts, random points, and the bright star masks in our database.  Photometric redshifts are not yet available and will be released in the future.

[Bright Star Masks](https://hsc-release.mtk.nao.ac.jp/doc/index.php/bright-star-masks__pdr3/ "Bright Star Masks (PDR3)")

Objects around bright stars likely have bad photometry (and many of them can even be fake sources).  These objects are flagged during the processing.  There are masks for different types of features defined for each band separately.

[Random Points](https://hsc-release.mtk.nao.ac.jp/doc/index.php/random-points__pdr3/ "Random Points (PDR3)")

For clustering analysis, a set of random points across the survey area will be useful.  Such a collection of random points can be found in the database.

[Passive Spiral Catalog](https://hsc-release.mtk.nao.ac.jp/doc/index.php/passive_spiral_galaxy_catalog__pdr3/ "Passive Spiral Galaxy Catalog (PDR3)")

Incremental Release 1: Passive spirals are known to be a special class of spiral galaxies and a large statistical sample is available from Shimakawa et al. 2022.

[Density Map Catalog](https://hsc-release.mtk.nao.ac.jp/doc/index.php/density-map-catalog__pdr3/ "Passive Spiral Galaxy Catalog (PDR3)")

Incremental Release 2: Galaxy density map has been updated for PDR3 using the methodology described in Shimakawa et al. 2021.

[Public Spectroscopic Redshifts](https://hsc-release.mtk.nao.ac.jp/doc/index.php/catalog-of-spectroscopic-redshifts__pdr3/ "Catalog of Spectroscopic Redshifts (PDR3)")

Partly for the purpose of photo-z calibrations, we have collected public spectroscopic redshifts from the literature and the collection is matched to the HSC objects by position.  Each spectroscopic survey has its own flagging scheme to indicate the redshift confidence and we have a homogenized flag for each object for easy selection of objects with reliable redshifts. _It is important to emphasize that users should acknowledge the original data source(s) when using this table._

[Photometric Redshifts](https://hsc-release.mtk.nao.ac.jp/doc/index.php/photometric-redshifts__pdr3/ "Photometric Redshifts (PDR3)")

Incremental Release 3: long-awaited photo-z’s are now available!

[CAMIRA Cluster Catalog](https://hsc-release.mtk.nao.ac.jp/doc/index.php/camira-cluster-catalog__pdr3/ "Photometric Redshifts (PDR2)")

Incremental Release 1: A cluster catalog based on CAMIRA, a multi-color red sequence cluster finder, is now available for PDR3.

## COSMOS Wide-depth stacks

The COSMOS field is one of the key extragalactic fields and is a valuable calibration field.  Using subsample of the UltraDeep COSMOS data, we have generated three sets of Wide-depth stacks at 25, 50, and 75th percentile seeing for each band in the Wide layer.  These sets will be useful for various systematic tests for the Wide layer.

[COSMOS wide-depth stacks](https://hsc-release.mtk.nao.ac.jp/doc/index.php/cosmos-wide-depth-stacks__pdr3/ "COSMOS Wide-Depth Stacks (PDR3)")

## Weak-lensing data products

We have not yet made a weak-lensing data release as part of PDR3.  The page below is a summary page of our weak-lensing products.  Currently, only those based on the S16A internal release are available (which were released as part of PDR2).

[Summary page of our weak-lensing products](https://hsc-release.mtk.nao.ac.jp/doc/index.php/weak-lensing-results-and-data-products/ "Weak-lensing results and data products")

## Tracts and Patches

The figures below show the coverage in each field in each filter. The large squares are tracts (approx. 1.7deg wide) and each tract is broken into 9×9 patches, each of which is 4200 pixels on a side. There is an overlap of 1 arcmin between the two adjacent tracts. Patches have an overlap of 200 pixels (~34 arcsec).

#### Deep/Udeep

| Field Name | HSC-G | HSC-R | HSC-I | HSC-Z | HSC-Y | NB0387 | NB0816 | NB0921 | NB1010 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COSMOS | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_HSC-G.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_HSC-G.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_HSC-R.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_HSC-R.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_HSC-I.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_HSC-I.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_HSC-Z.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_HSC-Z.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_HSC-Y.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_HSC-Y.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_NB0387.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_NB0387.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_NB0816.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_NB0816.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_NB0921.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_NB0921.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_COSMOS_NB1010.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_COSMOS_NB1010.png) |
| DEEP2-3 | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_HSC-G.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_HSC-G.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_HSC-R.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_HSC-R.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_HSC-I.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_HSC-I.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_HSC-Z.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_HSC-Z.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_HSC-Y.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_HSC-Y.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_NB0387.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_NB0387.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_NB0816.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_NB0816.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_NB0921.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_NB0921.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_DEEP2-3_NB1010.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_DEEP2-3_NB1010.png) |
| ELAIS-N1 | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_HSC-G.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_HSC-G.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_HSC-R.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_HSC-R.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_HSC-I.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_HSC-I.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_HSC-Z.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_HSC-Z.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_HSC-Y.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_HSC-Y.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_NB0387.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_NB0387.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_NB0816.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_NB0816.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_NB0921.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_NB0921.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_ELAIS-N1_NB1010.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_ELAIS-N1_NB1010.png) |
| SXDS+XMM-LSS | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_HSC-G.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_HSC-G.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_HSC-R.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_HSC-R.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_HSC-I.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_HSC-I.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_HSC-Z.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_HSC-Z.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_HSC-Y.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_HSC-Y.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_NB0387.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_NB0387.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_NB0816.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_NB0816.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_NB0921.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_NB0921.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_DUD_XMM-LSS_NB1010.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_DUD_XMM-LSS_NB1010.png) |

#### Wide

| Field Name | HSC-G | HSC-R | HSC-I | HSC-Z | HSC-Y |
| --- | --- | --- | --- | --- | --- |
| AEGIS | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_AEGIS_HSC-G.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_AEGIS_HSC-G.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_AEGIS_HSC-R.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_AEGIS_HSC-R.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_AEGIS_HSC-I.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_AEGIS_HSC-I.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_AEGIS_HSC-Z.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_AEGIS_HSC-Z.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_AEGIS_HSC-Y.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_AEGIS_HSC-Y.png) |
| Autumn | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_autumn_HSC-G.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_autumn_HSC-G.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_autumn_HSC-R.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_autumn_HSC-R.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_autumn_HSC-I.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_autumn_HSC-I.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_autumn_HSC-Z.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_autumn_HSC-Z.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_autumn_HSC-Y.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_autumn_HSC-Y.png) |
| HECTOMAP | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_hectomap_HSC-G.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_hectomap_HSC-G.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_hectomap_HSC-R.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_hectomap_HSC-R.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_hectomap_HSC-I.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_hectomap_HSC-I.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_hectomap_HSC-Z.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_hectomap_HSC-Z.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_hectomap_HSC-Y.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_hectomap_HSC-Y.png) |
| Spring | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_spring_HSC-G.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_spring_HSC-G.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_spring_HSC-R.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_spring_HSC-R.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_spring_HSC-I.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_spring_HSC-I.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_spring_HSC-Z.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_spring_HSC-Z.png) | [![](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/thumb/tracts_patches_W_spring_HSC-Y.png)](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/full/tracts_patches_W_spring_HSC-Y.png) |

The files below give the exact celestial coordinates of each tract and patch.

- Deep/Udeep
  - [COSMOS](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/info/tracts_patches_DUD-COSMOS.txt)
  - [DEEP2-3](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/info/tracts_patches_DUD-DEEP2-3.txt)
  - [ELAIS-N1](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/info/tracts_patches_DUD-ELAIS-N1.txt)
  - [SXDS+XMM-LSS](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/info/tracts_patches_DUD-XMM-LSS.txt)

- Wide
  - [AEGIS](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/info/tracts_patches_W-AEGIS.txt)
  - [HECTOMAP](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/info/tracts_patches_W-hectomap.txt)
  - [Autumn](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/info/tracts_patches_W-autumn.txt)
  - [Spring](https://hsc-release.mtk.nao.ac.jp/rsrc/pdr3/tract_patches/info/tracts_patches_W-spring.txt)

![](<Base64-Image-Removed>)

[Previous image](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/)[Next image](https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3/)
