URL: https://www.sdss4.org/dr17/spectro/lss/

- [Datasets](https://www.sdss4.org/dr17/data_access/)
- [Imaging Data](https://www.sdss4.org/dr17/imaging/)
- [Optical\\
\\
SpectraeBOSS, SPIDERS, TDSS, BOSS, SEGUE, SDSS-I/II](https://www.sdss4.org/dr17/spectro/)
- [APOGEE\\
\\
IR Spectra](https://www.sdss4.org/dr17/irspec/)
- [MaStar\\
\\
Library](https://www.sdss4.org/dr17/mastar/)
- [MaNGA\\
\\
IFU Spectra](https://www.sdss4.org/dr17/manga/)
- [Algorithms](https://www.sdss4.org/dr17/algorithms/)
- [Help](https://www.sdss4.org/dr17/help/)
- [Tutorials](https://www.sdss4.org/dr17/tutorials/)

# Large-Scale Structure

[Table of Contents](https://www.sdss4.org/dr17/spectro/lss/#toc-body)

- Large-Scale Structure

  - Large-scale structure catalogues
  - eBOSS

    - DR16
    - DR14

  - BOSS

    - Mock Galaxy Catalogs
    - LSS catalog creation code \[mksample\]

## Large-scale structure catalogues

The Large-Scale Structure (LSS) catalogs combine the list of cosmological tracer targets (typically galaxies or QSOs) with the results of the spectroscopic data reduction to create data and random catalogs that allow the user to estimate the cosmological tracer density fluctuations at any point within the survey footprint.  Weights are assigned to tracers to account for observational imperfections such as a failure of the spectroscopic pipeline to obtain a redshift, fiber collisions that preclude simultaneously assigning spectroscopic fibers to targets closer than 62'', and non-cosmological fluctuations imprinted the target catalog, such as the correlation between targets and stellar density described in  [Ross et al. 2011](http://adsabs.harvard.edu/abs/2011MNRAS.417.1350R),  [Ho et al. 2012](http://adsabs.harvard.edu/abs/2012ApJ...761...14H),  [Ross et al. 2012](http://adsabs.harvard.edu/abs/2012MNRAS.424..564R).  The random catalogs are designed to randomly sample the survey footprint with a density proportional to the map of the survey completeness.  Pairs of data and random catalogues are generated for samples with distinct selection functions.

This page describes the LSS catalogues for eBOSS and BOSS.  In eBOSS, we generate three independent LSS catalogues. These are Luminous Red Galaxies (LRGs; described in [Bautista et al. 2017](http://adsabs.harvard.edu/abs/2017arXiv171208064B)) with redshifts between 0.6 and 1, quasars (QSOs; described in [Ata et al. 2018](http://adsabs.harvard.edu/abs/2018MNRAS.473.4773A)) with redshifts between 0.8 and 2.2, and Emission Line Galaxies (ELGs; described in [Raichoor et al. 2020](https://ui.adsabs.harvard.edu/abs/2020arXiv200709007R/abstract)) with redshifts between 0.6 and 1.1.

In BOSS, LSS catalogues were generated for the LOWZ and CMASS samples separately. The LOWZ target class captures objects primarily at z < 0.4, while the CMASS class selects objects at 0.4 < z < 0.8. With DR12 a combined sample catalogue was provided, where these two samples are optimally combined (details in [Reid et al. 2016](http://adsabs.harvard.edu/abs/2016MNRAS.455.1553R)).

Finally, in all cases we generate catalogs in the north galactic cap and south galactic cap separately, for the reasons detailed in [Ross et al. 2011](http://adsabs.harvard.edu/abs/2011MNRAS.417.1350R), [Ho et al. 2012](http://adsabs.harvard.edu/abs/2012ApJ...761...14H), [Ross et al. 2012](http://adsabs.harvard.edu/abs/2012MNRAS.424..564R).

## eBOSS

### DR16

The DR16 eBOSS LSS catalogs for LRGs, QSOs, and ELGs are available [on the SAS](https://data.sdss.org/sas/dr16/eboss/lss/catalogs/DR16/). Catalogs are also generated that combine BOSS CMASS at redshifts greater than 0.6 with the eBOSS LRGs. This sample is denoted LRGpCMASS and is a superset of the highest redshift sample from the BOSS clustering catalogs. We recommend that this new eBOSS+BOSS catalog be used in place of the z>0.6 bin from BOSS.

Some details are different than previous releases and the information is split between more files than before.

Files with names like eBOSS\_samp\_full\_ALLdata-vDR16.fits, where samp can be LRG, QSO, or ELG contain the information on all targets that remain after masks are applied. All of the photometric information used in target selection is included, as is all of the information on eBOSS observations and redshift determination.

Files named like eBOSS\_samp\_clustering\_\* contain the data and random files meant to be used for clustering calculations, one pair each for each hemisphere. LRGpCMASS is an additional available samp, as described above. The included columns are paired down to only those required for clustering measurements and an ID column allowing a match to the full file. These include the angular position, the redshift, and any weights required to match the selection functions of the data and random catalogs.

Files that have \_rec in the name have gone through the BAO reconstruction process. There is one each for the data and random files and they should be used together for any clustering measurements.

Data model files follow the same naming format and are available [here](https://data.sdss.org/datamodel/files/EBOSS_LSS/catalogs/DR16).

Full details on the DR16 LSS catalogs are available in [Ross et al. 2020](https://ui.adsabs.harvard.edu/abs/2020arXiv200709000R/abstract) with additional details on the ELGs available in [Raichoor et al. 2020](https://ui.adsabs.harvard.edu/abs/2020arXiv200709007R/abstract).

### DR14

The DR14 eBOSS LSS catalogues for LRGs and QSOs remain available [on the SAS](https://data.sdss.org/sas/dr16/eboss/lss/catalogs/DR14/).

- Data files are described in [data\_DR14\_QSO\_NS](https://data.sdss.org/datamodel/files/EBOSS_LSS/catalogs/DR14/data_DR14_QSO_NS.html) and [data\_DR14\_LRG\_NS](https://data.sdss.org/datamodel/files/EBOSS_LSS/catalogs/DR14/data_DR14_LRG_NS.html)
- Random files are described in [random\_DR14\_QSO\_NS](https://data.sdss.org/datamodel/files/EBOSS_LSS/catalogs/DR14/random_DR14_QSO_NS.html) and [random\_DR14\_LRG\_NS](https://data.sdss.org/datamodel/files/EBOSS_LSS/catalogs/DR14/random_DR14_LRG_NS.html).
- Mask files are described in [mask\_DRX\_SAMPLE\_NS](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/mask_DRX_SAMPLE_NS.html)

X stands for the DR number, and NS corresponds to the galactic cap.

The description of the QSO LSS catalogues is given in Sections 2 and 3 of [Ata et al. 2018](http://adsabs.harvard.edu/abs/2018MNRAS.473.4773A), and the description of the QSO LRG catalogues is detailed in [Bautista et al. 2017](http://adsabs.harvard.edu/abs/2017arXiv171208064B).

## BOSS

To work directly with the catalogs used in BOSS analyses, download the following files directly from the SAS for [DR10](https://data.sdss.org/sas/dr10/boss/lss/), [DR11](https://data.sdss.org/sas/dr11/boss/lss/), and [DR12](https://data.sdss.org/sas/dr12/boss/lss/). Note that the DR12 catalogues are the final BOSS catalogues. The contents of each relevant file is described by a data model:

- Data files are described in [galaxy\_DRX\_SAMPLE\_NS](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/galaxy_DRX_SAMPLE_NS.html)
- Random files are described in [randomN\_DRX\_SAMPLE\_NS](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/randomN_DRX_SAMPLE_NS.html)

where X, SAMPLE, and NS can change depending on the data release, the sample and the galactic cap.

### Mock Galaxy Catalogs

We created a set of mock galaxy catalogs with the same survey footprint as the BOSS survey.  We use these to validate our methodology and estimate the covariance matrix associated with our observables, which is necessary to compute the uncertainty on any derived quantity from our galaxy catalogs, such as the BAO scale.  We used two different methodologies, QPM and PATCHY, both described in [Alam et al. 2017](http://adsabs.harvard.edu/abs/2017MNRAS.470.2617A).  Galaxy and random catalogs are available for each set of mocks and described by a data model: [mock\_galaxy\_DRX\_SAMPLE\_NS\_QPM\_IDNUMBER.fits.gz](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/dr11_qpm_mocks/mock_galaxy_DRX_SAMPLE_NS_QPM_IDNUMBER.html) The data model for QPM and PATCHY mocks is the same.

More information on the PATCHY mock galaxy catalog is available from [its description page](http://www.skiesanduniverses.org/page/page-3/page-15/page-9/) on the Skies and Universes website.

### LSS catalog creation code \[mksample\]

The code used by the BOSS galaxy clustering working group to produce the DR10, DR11, and DR12 catalogs is called mksample and is available to download on the SAS.  The DR10 and DR11 catalogs were produced using the same algorithm but with different input files.  The DR12 catalogs were produced with an updated version of mksample.  For details of the DR10/DR11 algorithms, consult [Anderson et al. 2014](http://adsabs.harvard.edu/abs/2014MNRAS.441...24A).  The DR12 catalogs and updated mksample are described in [Reid et al. 2016](http://adsabs.harvard.edu/abs/2016MNRAS.455.1553R).  The code can be used to create new sets of random catalogs or to generate new catalogs for a subsample of galaxies in the CMASS or LOWZ target classes. The necessary input files and algorithms are described in more detail in the [tutorial](https://www.sdss4.org/dr17/tutorials/lss_galaxy/).
