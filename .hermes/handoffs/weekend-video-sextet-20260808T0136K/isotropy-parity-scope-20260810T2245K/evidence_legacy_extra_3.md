# URL: https://datalab.noirlab.edu/data/legacy-surveys

# LS (Legacy Surveys)

[Description](https://datalab.noirlab.edu/data/legacy-surveys#description) [Data Releases](https://datalab.noirlab.edu/data/legacy-surveys#data-releases) [LS DR10](https://datalab.noirlab.edu/data/legacy-surveys#ls-dr10) [LS DR9](https://datalab.noirlab.edu/data/legacy-surveys#ls-dr9) [LS DR8](https://datalab.noirlab.edu/data/legacy-surveys#ls-dr8) [Data Access](https://datalab.noirlab.edu/data/legacy-surveys#data-access) [Acknowledgments](https://datalab.noirlab.edu/data/legacy-surveys#acknowledgments)

# Legacy Imaging Surveys

## Description

The Legacy Surveys cover ∼14,000 deg² of the extragalactic sky, and yield high-quality optical, near-infrared, and infrared photometric catalogs. The sky coverage is approximately bounded by -18° < δ < +84° in celestial coordinates and \|b\| > 18° in Galactic coordinates. Resulting images, models, and catalogs will enhance current and future wide area surveys such as SDSS/BOSS/eBOSS and DESI.

The Legacy Surveys data products and database are accessible via the Astro Data Lab as described [here](https://datalab.noirlab.edu/ls/dataAccess.php). See the [Legacy Surveys team](https://legacysurvey.org/) page for a complete description of the surveys and data files.

The Legacy Surveys are a combination of the [DECam Legacy Survey (DECaLS)](https://www.legacysurvey.org/decamls) using the Dark Energy Camera on the Blanco 4m telescope, the [Mayall z-band Legacy Survey (MzLS)](https://www.legacysurvey.org/mzls) using the MOSAIC instrument on the Mayall 4m telescope, and the [Beijing-Arizona Sky Survey (BASS)](https://www.legacysurvey.org/bass) using the 90Prime instrument at the Steward Observatory Bok telescope. These are described in detail below.

The **ls\_dr10.tractor**, **ls\_dr9.tractor**, and **ls\_dr8.tractor** tables have each been crossmatched against our default reference datasets within a 1.5 arcsec radius, nearest neighbor only. These tables will appear with **x1p5** in their name in our table browser. Example: [ls\_dr10.x1p5\_\_tractor\_\_gaia\_dr3\_\_gaia\_source](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.x1p5__tractor__gaia_dr3__gaia_source).


#### Legacys Surveys at a Glance

| **Survey** | **Telescope** | **Band** | **Area** |
| --- | --- | --- | --- |
| DECaLS | Blanco | _g, r, z_ | 9500 sq. deg |
| MzLS | Mayall | _z_ | 5000 sq. deg |
| BASS | Bok | _g, r_ | 5000 sq. deg |
| AllWISE | WISE | _W1, W2, W3, W4_ | 5000 sq. deg |

[Back to Top](https://datalab.noirlab.edu/data/legacy-surveys#)

#### DECaLS

The [Dark Energy Camera Legacy Survey (DECaLS)](http://legacysurvey.org/decamls/) covers ∼9500 deg² in the _g, r, z_-bands to depths of _g_ =24.7, _r_ =23.9, _z_ =23.0. Infrared WISE data are also extracted at the location of the DECaLS sources.

**Status**: The ninth data release (DR9) includes the full footprint of DECaLS in all three optical filters ( **DR9-South**). Images from DECaLS _g, r, z_-band observations ( [NOAO survey program 2014B-0404](https://www.noao.edu/perl/abstract?2014B-0404)) are included from 9th August 2014 through 7th March 2019. DR9 also includes DECam data from a range of non-DECaLS surveys, including observations that were conducted from 1st September 2013 to 7th March 2019. A large portion of these non-DECaLS observations were taken by the [Dark Energy Survey](https://www.darkenergysurvey.org/) team. DR9 supersedes DR8 and previous DECaLS releases.

**Observing**: The observations are taken with DECam on the 4-meter Blanco telescope in three passes at each sky location, and in each filter ( _g, r, z_). "Pass 1" is observed in photometric, good-seeing conditions. "Pass 2" and "Pass 3" are observed in progressively worse conditions. This strategy was adopted to ensure a photometric solution across the full survey area. The observing time is adjusted as a function of sky brightness and transparency.

#### MzLS

The [Mayall z-band Legacy Survey (MzLS)](https://desi.lbl.gov/trac/wiki/PublicPages/MayallZbandLegacy) covers ∼5000 deg² in the _z_-band to depth of _z_ =23.0.

**Status**: The ninth data release (DR9) includes the entire MzLS footprint of ∼5300 deg² in the _z_-band. **DR9-North** contains MzLS images taken between 19th November 2015 through 12th February 2018, and supersedes DR8 and previous MzLS releases. While no new data were added between DR8 and DR9, the data processing and photometry extraction were improved.

**Observing**: The observations are taken with MOSAIC on the Mayall telescope in three passes at each sky location. "Pass 1" is observed in photometric, good-seeing conditions. "Pass 2" and "Pass 3" are observed in progressively worse conditions. This strategy was adopted to ensure a photometric solution across the full survey area. The observing time is adjusted as a function of sky brightness and transparency. Single exposures reach 5-sigma point source depth of 23.04 (pass 1), 22.95 (pass 2), and 22.85 (pass 3).

#### BASS

The [Beijing-Arizona Sky Survey (BASS)](http://batc.bao.ac.cn/BASS/doku.php) covers ∼5000 deg² in the _g, r_-bands to depths of _g_ =24.4, _r_ =23.9.

**Status**: The ninth data release (DR9) covers the full footprint of BASS (∼5000 deg²) in _g_-band and _r_-band. **DR9-North** includes BASS images taken from 12th November 2015 through 7th March 2019.

**Observing**: The observations are taken with 90Prime on the Bok telescope in three passes at each sky location, and in each filter ( _g, r_). "Pass 1" is observed in photometric, good-seeing conditions. "Pass 2" and "Pass 3" are observed in progressively worse conditions. This strategy was adopted to ensure a photometric solution across the full survey area. The observing time is adjusted as a function of sky brightness and transparency. In the _g_-band, single exposures reach 5-sigma point source depth of 23.92 (pass 1), 23.89 (pass 2), and 23.89 (pass 3). In the _r_-band, single exposures reach depths of 23.30 (pass 1), 23.30 (pass 2), and 23.18 (pass 3).

#### Joining DR9-North & DR9-South

Unique area is resolved by including the BASS and MzLS images (from **DR9-North**) if they are _both_ at Declination > 32.375° and North of the Galactic Plane. Otherwise, the DECam images (from **DR9-South**) are used. This method eliminates the overlap when combining the North and South areas into the full **DR9** footprint.

[Back to Top](https://datalab.noirlab.edu/data/legacy-surveys#)

## Data Releases

### LS DR10

The latest release from the [Dark Energy Spectroscopic Instrument (DESI) Legacy Imaging Surveys](https://www.legacysurvey.org/) team, the tenth data release (DR10) of the Legacy Surveys significantly expands its photometric observations to >20,000 square degrees, and includes entirely new imaging in the i-band, in addition to grz imaging and four infrared bands from WISE and [NEOWISE](https://wise2.ipac.caltech.edu/docs/release/neowise/). The imaging includes [DECaLS](https://www.legacysurvey.org/decamls) _g, r, z_-band observations taken with the [Dark Energy Camera](https://www.darkenergysurvey.org/the-des-project/instrument/the-camera/) (DECam), as well as imaging in the _g, r, i, z_-bands associated with other observing programs using DECam such as the [DeROSITAS](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera/DeROSITAS) survey, the [BLISS+ survey](https://arxiv.org/abs/1812.06318), and the [Dark Energy Survey](https://www.darkenergysurvey.org/) (DES).

However, imaging data of the Northern sky from [BASS](https://www.legacysurvey.org/bass) and [MzLS](https://www.legacysurvey.org/bass) were not reprocessed for DR10. For convenience, we serve both the **DR10-South** main photometry table ( _**ls\_dr10.tractor\_s**_) and a combined table comprising that table and its **DR9-North** counterpart ( _**ls\_dr9.tractor\_n**_), called simply _**ls\_dr10.tractor**_, along with corresponding combined table of aperture flux values from the **DR10-South** ( _**ls\_dr10.apflux\_s**_) with its **DR9-North** counterpart ( _**ls\_dr9.apflux\_n**_) called _**ls\_dvr10.apflux**_, and also a combined WISE light curves photometry table from **DR10-South** ( _**ls\_dr10.wise\_s**_) with its counterpart from **DR9-North** ( _**ls\_dr9.wise\_n**_), called _**ls\_dr10.wise**_. Note that the additional columns in DR10 (almost all of them related to the _i_-band) are not in DR9-North. Values for Northern sources in those columns of the combined tables have the value _-9999_.

#### LS DR10 Database Main Tables

| **Table** | **Description** |
| --- | --- |
| [apflux](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.apflux) | Combined aperture flux values of tractor objects from DR10-South combined with DR9-North (3,145,841,852 rows) |
| [apflux\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.apflux_s) | Aperture flux values of tractor objects in DR10-South (2,825,807,500 rows) |
| [tractor](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.tractor) | Main tractor photometry catalog (combined DR10-South and DR9-North); Less frequently used aperture fluxes and light-curve columns are placed in apflux and wise tables, respectively (3,145,841,852 rows) |
| [tractor\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.tractor_s) | Main tractor photometry catalog for DR10-South; Less frequently used aperture fluxes and light-curve columns are placed in apflux and wise tables, respectively (2,825,807,500 rows) |
| [wise](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.wise) | Combined WISE light-curve photometry of objects from DR10-South and DR9-North (3,145,841,852 rows) |
| [wise\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.wise_s) | WISE light-curve photometry of objects from DR10-South (2,825,807,500 rows) |

#### LS DR10 Database Auxiliary Tables

| **Table** | **Description** |
| --- | --- |
| [bricks](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.bricks) | Table with RA and Dec bounds for each geometrical brick in the survey (662,174 rows) |
| [bricks\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.bricks_s) | Table with information that summarizes the contents of each brick in DR10-South (366,912 rows) |
| [depth\_summary\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.depth_summary_s) | A summary of the depth histogram from DR10-South (50 rows) |
| [photo\_z](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.photo_z_10p1) | Photometric redshifts from Zhou et al. 2023 (trained on DESI EDR z) (2,827,055,986 rows) |
| [psc\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.psc_n) | LS DR10 North Point Source Catalog (339,015,213 rows) |
| [psc\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.psc_s) | LS DR10 South Point Source Catalog (2,807,176,359 rows) |

A sky map of the full imaging survey coverage ( **DR10-South** and **DR9-North**) is included below, color-coded by the depth in the _z_-band filter, and shown in an equatorial projection. The solid grey line traces the Galactic plane. (Figure credit: Dustin Lang).

![depth-z-ls-dr10.png](https://content.datalab.noirlab.edu/uploads/depth_z_ls_dr10_f989b9eef0.png)

[Back to Top](https://datalab.noirlab.edu/data/legacy-surveys#)

### LS DR9

The ninth data release (DR9) is the official release used to select DESI targets. It contains data over the entire footprint of the DESI survey, including data from MzLS ( _z_-band) and BASS ( _g_ & _r_ bands) surveys ( **DR9-North**), and data from DECaLS ( _g_, _r_, & _z_ bands; **DR9-South**). The footprint of DR9 covers approximately 14,800 deg² with 3 passes in all three optical filters ( _g, r, z_), and over 19,000 deg² with at least one pass in all three filters. The main changes between DR8 and DR9 consist in improvements of the data processing and catalog creation. Additionally, the unWISE images used to extract WISE forced photometry for DR9 include up to year 6 of NEOWISE Reactivation. An overview of the Legacy Surveys is available in [Dey et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019AJ....157..168D/abstract).

#### LS DR9 Database Main Tables

| **Table** | **Description** |
| --- | --- |
| [apflux](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.apflux) | Combined aperture flux values of tractor objects from DR9-South combined with DR9-North (1,969,942,678 rows) |
| [apflux\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.apflux_n) | Aperture flux values of tractor objects in DR9-North (364,277,779 rows) |
| [apflux\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.apflux_s) | Aperture flux values of tractor objects in DR9-South (1,649,627,447 rows) |
| [tractor](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.tractor) | Main tractor photometry catalog (combined DR9-South and North); Less frequently used aperture fluxes and light-curve columns are placed in apflux and wise tables, respectively (1,969,942,678 rows) |
| [tractor\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.tractor_n) | Main tractor photometry catalog for DR9-North; Less frequently used aperture fluxes and light-curve columns are placed in apflux and wise tables, respectively (364,277,779 rows) |
| [tractor\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.tractor_s) | Main tractor photometry catalog for DR9-South; Less frequently used aperture fluxes and light-curve columns are placed in apflux and wise tables, respectively (1,649,627,447 rows) |
| [wise](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.wise) | Combined WISE light-curve photometry of objects from DR9-South and DR9-North (1,969,942,678 rows) |
| [wise\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.wise_n) | WISE light-curve photometry of objects from DR9-North (364,277,779 rows) |
| [wise\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.wise_s) | WISE light-curve photometry of objects from DR9-South (1,649,627,447 rows) |

#### LS DR9 Database Auxiliary Tables

| **Table** | **Description** |
| --- | --- |
| [bailout](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.bailout) | LS DR9 sources with no corresponding LS DR10 sources (107,937 rows) |
| [bricks](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.bricks) | Table with RA and Dec bounds for each geometrical brick in the survey (662,174 rows) |
| [bricks\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.bricks_n) | Table with information that summarizes the contents of each brick in DR9-North (93,548 rows) |
| [bricks\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.bricks_s) | Table with information that summarizes the contents of each brick in DR9-South (253,658 rows) |
| [ccds\_annotated](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.ccds_annotated) | Additional information gathered during calibration pre-processing before running the Tractor reductions (6,776,431 rows) |
| [depth\_summary\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.depth_summary_n) | A summary of the depth histogram from DR9-North (50 rows) |
| [depth\_summary\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.depth_summary_s) | A summary of the depth histogram from DR9-South (50 rows) |
| [forced](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.forced) | Forced photometry results, for all CCDs that were included in the DR9 processing (29,919,191,561 rows) |
| [photo\_z](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.photo_z) | Photometric redshifts from [Zhou et al. 2021](https://ui.adsabs.harvard.edu/abs/2021MNRAS.501.3309Z/abstract) (trained on non-DESI z) (1,969,942,678 rows) |
| [photo\_z\_9p1](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.photo_z_9p1) | Photometric redshifts from [Zhou et al. 2023](https://ui.adsabs.harvard.edu/abs/2023JCAP...11..097Z/abstract) (trained on DESI EDR z) (2,013,905,226 rows) |

A sky map of the full imaging survey coverage is included below, color-coded by the depth in the _z_-band filter, and shown in an equatorial projection. The solid grey line traces the Galactic plane. (Figure credit: Dustin Lang).


![depth-z-ls-dr9.png](https://content.datalab.noirlab.edu/uploads/depth_z_ls_dr9_2a2139a4f3.png)

[Back to Top](https://datalab.noirlab.edu/data/legacy-surveys#)

### LS DR8

Data release 8 (DR8) is the eighth public data release of the Legacy Surveys. It is the sixth public data release of images and catalogs from DECaLS (DR7) comprised the fifth release of data from DECaLS) and the third release of data from BASS and MzLS (DR6 comprised the second release of data from BASS and MzLS). DR8 is the first release to include images and catalogs from all three of the Legacy Surveys in a single release. Imaging from the Legacy Surveys is first reduced through the NOIRLab Community Pipeline before being processed using the [Tractor processing tool](https://thetractor.org/doc/intro.html). DR8 also includes WISE fluxes from all imaging through year 4 of NEOWISE-Reactivation force-photometered in the unWISE maps at the locations of Legacy Surveys optical sources.

Initially, they were also crossmatched with several tables of the SDSS survey. These table start with **dr8\_<north\|south>** followed by the SDSS table they are crossmatched against (not listed in the table below).
Example: [ls\_dr8.dr8\_north\_specobj\_dr14.](https://datalab.noirlab.edu/data/%22/data-explorer?showTable=ls_dr8.dr8_north_specobj_dr14%22)

#### LS DR8 Database Main Tables

| **Table** | **Description** |
| --- | --- |
| [apflux](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.apflux_s) | Combined aperture flux values of tractor objects from DR8-South combined with DR9-North (2,320,796,062 rows) |
| [apflux\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.apflux_n) | Aperture flux values of tractor objects in DR8-North (357,868,565 rows) |
| [apflux\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.apflux_s) | Aperture flux values of tractor objects in DR8-South (1,336,361,803 rows) |
| [tractor](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.tractor) | Main tractor photometry catalog (combined DR8-South and DR8-North); Less frequently used aperture fluxes and light-curve columns are placed in apflux and wise tables, respectively (1,604,849,426 rows) |
| [tractor\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.tractor_n) | Main tractor photometry catalog for DR8-North; Less frequently used aperture fluxes and light-curve columns are placed in apflux and wise tables, respectively (357,868,565 rows) |
| [tractor\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.tractor_s) | Main tractor photometry catalog for DR8-South; Less frequently used aperture fluxes and light-curve columns are placed in apflux and wise tables, respectively (1,336,361,803 rows) |
| [wise](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.wise) | Combined WISE light-curve photometry of objects from DR8-South and DR8-North (1,160,389,715 rows) |
| [wise\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.wise_n) | WISE light-curve photometry of objects from DR8-North (357,868,565 rows) |
| [wise\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.wise_s) | WISE light-curve photometry of objects from DR8-South (1,336,361,803 rows) |

#### LS DR8 Database Auxiliary Tables

| **Table** | **Description** |
| --- | --- |
| [bricks](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.bricks) | Table with RA and Dec bounds for each geometrical brick in the survey (662,174 rows) |
| [bricks\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.bricks_n) | Table with information that summarizes the contents of each brick in DR8-North (93,610 rows) |
| [bricks\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.bricks_s) | Table with information that summarizes the contents of each brick in DR8-South (247,844 rows) |
| [ccds\_annotated](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.ccds_annotated) | Additional information gathered during calibration pre-processing before running the Tractor reductions (9,062,155 rows) |
| [depth\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.depth_n) | A concatenation of the depth histograms for each brick in DR8-South (93,610 rows) |
| [depth\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.depth_s) | A concatenation of the depth histograms for each brick in DR8-South (247,844 rows) |
| [depth\_summary\_n](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.depth__summary_n) | A summary of the depth histogram from DR8-North (50 rows) |
| [depth\_summary\_s](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.depth__summary_s) | A summary of the depth histogram from DR8-South (50 rows) |
| [forced](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.forced) | Forced photometry results, for all CCDs that were included in the DR8 processing (19,883,032,534 rows) |
| [photo\_z](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.photo_z) | Photometric redshifts (1,646,664,729 rows) |

```

```

#### LS DR8 Value-Added Catalogs

| **Table** | **Description** |
| --- | --- |
| [dr8\_north\_dr12q](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.dr8_north_dr12q) | SDSS DR12 QSO crossmatch (297,301 rows) |
| [dr8\_north\_dr14q\_v4\_4](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.dr8_north_dr14q_v4_4) | SDSS DR14\_v4.4 QSO crossmatch (526,356 rows) |
| [dr8\_north\_dr7q](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.dr8_north_dr7q) | SDSS DR7 QSO crossmatch (105,783 rows) |
| [dr8\_north\_specobj\_dr14](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.dr8_north_specobj_dr14) | SDSS DR14 spectra (4,851,200 rows) |
| [dr8\_north\_superset\_dr12q](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.dr8_north_superset_dr12q) | SDSS DR12 QSO Superset (546,856 rows) |
| [dr8\_south\_dr12q](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.dr8_south_dr12q) | SDSS DR12 QSO crossmatch (297,301 rows) |
| [dr8\_south\_dr14q\_v4\_4](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr8.dr8_south_dr14q_v4_4) | SDSS DR14\_v4.4 QSO crossmatch (526,356 rows) |

[... middle omitted — see footer ...]


**DR8:**
JPEG: [http://legacysurvey.org/viewer/jpeg-cutout/?ra=190.1086&dec=1.2005&layer=dr8&pixscale=0.27&bands=grz](http://legacysurvey.org/viewer/jpeg-cutout/?ra=190.1086&dec=1.2005&layer=dr8&pixscale=0.27&bands=grz)

FITS: [http://legacysurvey.org/viewer/fits-cutout/?ra=190.1086&dec=1.2005&layer=dr8&pixscale=0.27&bands=grz](http://legacysurvey.org/viewer/fits-cutout/?ra=190.1086&dec=1.2005&layer=dr8&pixscale=0.27&bands=grz)

where "bands" is a string such as " _grz_"," _gz_"," _g_", etc. This will merge the northern (MzLS+BASS) and equatorial (DECam) images at the Dec=32.375 line. Replacing layer=dr8 with layer=dr8-model or layer=dr8-resid will instead return cutouts for the model and residual images, respectively.

#### Jupyter Notebook Server

The [Data Lab Jupyter Notebook server](https://datalab.noirlab.edu/devbooks) (authenticated service) contains several examples of how to access and visualize the LS catalog:

- [DESI Legacy Surveys and SDSS/BOSS Large Scale Structure](https://github.com/astro-datalab/notebooks-latest/blob/master/03_ScienceExamples/LargeScaleStructure/LargeScaleStructureSdssLs.ipynb)
- [Star/Galaxy/QSO Classification in the DESI Imaging Legacy Surveys](https://github.com/astro-datalab/notebooks-latest/blob/master/03_ScienceExamples/StarGalQSOSeparation/StarGalQsoLSDR9.ipynb)
- [Locating Milky Way Analogues in Legacy Surveys Data](https://github.com/astro-datalab/notebooks-latest/blob/master/05_Contrib/ExtraGalactic/Milky_Way_Analogues_Legacy/Milky_Way_Analogues_LS_DR9.ipynb)

#### The NSF NOIRLab Astro Data Archive access

The NSF NOIRLab Astro Data Archive portal can be used to retrieve raw, and calibrated Legacy Surveys images, as well as the Tractor catalogs. Use the Search tool in the [Astro Data Archive](https://astroarchive.noirlab.edu/).

[Back to Top](https://datalab.noirlab.edu/data/legacy-surveys#)

## Acknowledgments

The Legacy Surveys consist of three individual and complementary projects: the Dark Energy Camera Legacy Survey (DECaLS; NOAO Proposal ID # 2014B-0404; PIs: David Schlegel and Arjun Dey), the Beijing-Arizona Sky Survey (BASS; NOAO Proposal ID # 2015A-0801; PIs: Zhou Xu and Xiaohui Fan), and the Mayall z-band Legacy Survey (MzLS; NOAO Proposal ID # 2016A-0453; PI: Arjun Dey). DECaLS, BASS and MzLS together include data obtained, respectively, at the Blanco telescope, Cerro Tololo Inter-American Observatory, NSF National Optical Infrared Astronomy Research Laboratory (NOIRLab); the Bok telescope, Steward Observatory, University of Arizona; and the Mayall telescope, Kitt Peak National Observatory, NOIRLab. The Legacy Surveys project is honored to be permitted to conduct astronomical research on Iolkam Du'ag (Kitt Peak), a mountain with particular significance to the Tohono O'odham Nation.

The NSF NOIRLab is operated by the Association of Universities for Research in Astronomy (AURA) under a cooperative agreement with the National Science Foundation. Database access and other data services are provided by the Astro Data Lab.

BASS is a key project of the Telescope Access Program (TAP), which has been funded by the National Astronomical Observatories of China, the Chinese Academy of Sciences (the Strategic Priority Research Program "The Emergence of Cosmological Structures" Grant # XDB09000000), and the Special Fund for Astronomy from the Ministry of Finance. The BASS is also supported by the External Cooperation Program of Chinese Academy of Sciences (Grant # 114A11KYSB20160057), and Chinese National Natural Science Foundation (Grant # 11433005).

The Legacy Surveys team makes use of data products from the Near-Earth Object Wide-field Infrared Survey Explorer (NEOWISE), which is a project of the Jet Propulsion Laboratory/California Institute of Technology. NEOWISE is funded by the National Aeronautics and Space Administration.

The Legacy Surveys imaging of the DESI footprint is supported by the Director, Office of Science, Office of High Energy Physics of the U.S. Department of Energy under Contract No. DE-AC02-05CH1123, by the National Energy Research Scientific Computing Center, a DOE Office of Science User Facility under the same contract; and by the U.S. National Science Foundation, Division of Astronomical Sciences under Contract No.AST-0950945 to NOAO.

This project used data obtained with the Dark Energy Camera (DECam), which was constructed by the Dark Energy Survey (DES) collaboration. Funding for the DES Projects has been provided by the U.S. Department of Energy, the U.S. National Science Foundation, the Ministry of Science and Education of Spain, the Science and Technology Facilities Council of the United Kingdom, the Higher Education Funding Council for England, the National Center for Supercomputing Applications at the University of Illinois at Urbana-Champaign, the Kavli Institute of Cosmological Physics at the University of Chicago, Center for Cosmology and Astro-Particle Physics at the Ohio State University, the Mitchell Institute for Fundamental Physics and Astronomy at Texas A&M University, Financiadora de Estudos e Projetos, Fundação Carlos Chagas Filho de Amparo, Financiadora de Estudos e Projetos, Fundação Carlos Chagas Filho de Amparo à Pesquisa do Estado do Rio de Janeiro, Conselho Nacional de Desenvolvimento Científico e Tecnológico and the Ministério da Ciência, Tecnologia e Inovação, the Deutsche Forschungsgemeinschaft and the Collaborating Institutions in the Dark Energy Survey. The Collaborating Institutions are Argonne National Laboratory, the University of California at Santa Cruz, the University of Cambridge, Centro de Investigaciones Enérgeticas, Medioambientales y Tecnológicas–Madrid, the University of Chicago, University College London, the DES-Brazil Consortium, the University of Edinburgh, the Eidgenössische Technische Hochschule (ETH) Zürich, Fermi National Accelerator Laboratory, the University of Illinois at Urbana-Champaign, the Institut de Ciències de l'Espai (IEEC/CSIC), the Institut de Física d'Altes Energies, Lawrence Berkeley National Laboratory, the Ludwig-Maximilians Universität München and the associated Excellence Cluster Universe, the University of Michigan, the National Optical Astronomy Observatory, the University of Nottingham, the Ohio State University, the University of Pennsylvania, the University of Portsmouth, SLAC National Accelerator Laboratory, Stanford University, the University of Sussex, and Texas A&M University.

#### Photometric Redshifts Acknowledgment

When using data from the Photometric Redshifts for the Legacy Surveys (PRLS) catalog, please include the following additional acknowledgment: The Photometric Redshifts for the Legacy Surveys (PRLS) catalog used in this paper was produced thanks to funding from the U.S. Department of Energy Office of Science, Office of High Energy Physics via grant DE-SC0007914. This applies to the following tables:

- [ls\_dr9.photo\_z](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.photo_z)
- [ls\_dr9.photo\_z\_9p1](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr9.photo_a_9p1z)
- [ls\_dr10.photo\_z](https://datalab.noirlab.edu/data-explorer?showTable=ls_dr10.photo_z)

[Back to Top](https://datalab.noirlab.edu/data/legacy-surveys#)

──────── [TRUNCATED] ────────
Showing 22,420 chars (head) + 7,240 chars (tail) of 34,596 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/datalab.noirlab.edu-c1a2a7c0ab.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/datalab.noirlab.edu-c1a2a7c0ab.md" offset=186 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────