URL: https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html

# CatWISE Catalog Definitions

#### Overview

The CatWISE2020 Catalog contains positions and brightnesses for 1,890,715,640 sources selected from combined WISE and NEOWISE all-sky survey data collected from 2010 to 2018 at 3.4 and 4.6 microns (W1 and W2).
The CatWISE Preliminary Catalog contains positions and brightnesses for 900,849,014 sources collected from 2010 to 2016.
CatWISE adapts AllWISE software to measure the sources in co-added images created from six month subsets of these data, each representing one coverage of the inertial sky, or epoch. The catalog includes the measured motion of sources in
12 epochs over the 8 year span of the data for CatWISE2020, and in 8 epochs
over the 6 year span of the data for the Preliminary Catalog (note this
[table](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/CatWISE2020_Table1_20201012.tbl) provides corrections for
a small systematic astrometric error in CatWISE2020, typically 30 mas in position and 10 mas per year in motion, as discussed in section 3.3 of [Marocco et al. (2020)](https://iopscience.iop.org/article/10.3847/1538-4365/abd805)).
The [detection list](https://faun.rc.fas.harvard.edu/unwise/neo5/) for CatWISE2020 relies on "crowdsource" software and comes from an updated version of the 10-epoch unWISE catalog
( [Schlafly et al. 2019](https://ui.adsabs.harvard.edu/abs/2019ApJS..240...30S/abstract)), while the Preliminary Catalog used
"MDET" software (the detection software used for AllWISE;
[Marsh and Jarrett 2012](https://ui.adsabs.harvard.edu/abs/2012PASA...29..269M/abstract)) to generate the detection list.
The crowdsource software is much better at recovering source detections in high-density regions such as the Galactic plane.

Sources were measured in unWISE coadded images that divide the sky into 18,240 tiles using the
WISE Atlas tile footprint. Catalog sources are required to be from the tile where that source is
furthest from the tile edge, and to have both SNR ≥ 5 and no
identified artifacts (i.e. a "0" in the corresponding "ab\_flags" character)
in the same band, which can be either W1 or W2. The 167,831,546 CatWISE Preliminary sources and 341,799,385 CatWISE2020 sources that fail to meet these criteria are provided
in the corresponding CatWISE Reject Table.
There are 185 columns in the CatWISE2020 Catalog
on IRSA, with brief descriptions provided in the table below. The CatWISE Reject Tables
include an additional column ("P") indicating whether the source meets the requirement to be
furthest from its tile edge.
The CatWISE2020 Catalog contains three columns not shown in the CatWISE Preliminary Catalog: 'glon' and 'glat' which were omitted because they were not computed correctly, and 'unwise\_objid' to facilitate cross-matching with the detection list.
Additional information about most of the columns is given in section II.1.a of the [AllWISE Explanatory Supplement](https://wise2.ipac.caltech.edu/docs/release/allwise/expsup/sec2_1a.html) with CatWISE differences described in Table A1 of [Eisenhardt et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020ApJS..247...69E/abstract).

If you use CatWISE data, please cite
[Eisenhardt et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020ApJS..247...69E/abstract),
which provides details on CatWISE and the Preliminary Catalog.
[Marocco et al. (2020)](https://iopscience.iop.org/article/10.3847/1538-4365/abd805) describes updates for
the CatWISE2020 Catalog. For more information, see
the [CatWISE2020 README](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/CatWISE2020README_IRSA.txt), the [CatWISE Preliminary README](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/PrelimREADMEIRSA.txt), or the [CatWISE Project](https://catwise.github.io/) web page.

| Name | Intype | Units | Description |
| --- | --- | --- | --- |
| source\_name | char | -- | source hexagesimal designation |
| source\_id | int | -- | tile name + processing code + wphot index |
| ra | double | deg | right ascension (J2000); (note [uncorrected systematic](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/CatWISE2020_Table1_20201012.tbl) in CatWISE2020) |
| dec | double | deg | declination (J2000); (note [uncorrected systematic](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/CatWISE2020_Table1_20201012.tbl) in CatWISE2020) |
| sigra | real | arcsec | uncertainty in RA |
| sigdec | real | arcsec | uncertainty in DEC |
| sigradec | real | arcsec | cross-term of RA and Dec uncertainties |
| wx | real | pix | x pixel value |
| wy | real | pix | y pixel value |
| w1sky | real | 'dn' | frame sky background value, band 1 |
| w1sigsk | real | 'dn' | frame sky background value uncertainty, band 1 |
| w1conf | real | 'dn' | frame sky confusion based on the uncertainty images, band 1 |
| w2sky | real | 'dn' | frame sky background value, band 2 |
| w2sigsk | real | 'dn' | frame sky background value uncertainty, band 2 |
| w2conf | real | 'dn' | frame sky confusion based on the uncertainty images, band 2 |
| w1snr | real | -- | instrumental profile-fit photometry S/N ratio, band 1 |
| w2snr | real | -- | instrumental profile-fit photometry S/N ratio, band 2 |
| w1flux | real | 'dn' | profile-fit photometry raw flux, band 1 |
| w1sigflux | real | 'dn' | profile-fit photometry raw flux uncertainty, band 2 |
| w2flux | real | 'dn' | profile-fit photometry raw flux, band 2 |
| w2sigflux | real | 'dn' | profile-fit photometry raw flux uncertainty, band 2 |
| w1mpro | real | mag | instrumental profile-fit photometry magnitude, band 1 |
| w1sigmpro | real | mag | instrumental profile-fit photometry flux uncertainty in mag units, band 1 |
| w1rchi2 | real | -- | instrumental profile-fit photometry reduced chi^2, band 1 |
| w2mpro | real | mag | instrumental profile-fit photometry magnitude, band 2 |
| w2sigmpro | real | mag | instrumental profile-fit photometry flux uncertainty in mag units, band 2 |
| w2rchi2 | real | -- | instrumental profile-fit photometry reduced chi^2, band 2 |
| rchi2 | real | -- | instrumental profile-fit photometry reduced chi squared, total |
| nb | int | -- | number of blend components used in each fit |
| na | int | -- | number of actively deblended components |
| w1Sat | real | -- | fraction of pixels affected by saturation, band 1 |
| w2Sat | real | -- | fraction of pixels affected by saturation, band 2 |
| w1mag | real | mag | instrumental standard aperture (8.25") mag w/ aperture correction applied, band 1 |
| w1sigm | real | mag | instrumental standard aperture mag uncertainty, band 1 |
| w1flg | int | - | instrumental standard aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w1Cov | real | -- | mean coverage depth, band 1 |
| w2mag | real | mag | instrumental standard aperture (8.25") mag w/ aperture correction applied, band 2 |
| w2sigm | real | mag | instrumental standard aperture mag uncertainty, band 2 |
| w2flg | int | - | instrumental standard aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w2Cov | real | -- | mean coverage depth, band 2 |
| w1mag\_1 | real | mag | aperture 1 (5.50") instrumental aperture mag, band 1 |
| w1sigm\_1 | real | mag | aperture 1 instrumental aperture mag uncertainty, band 1 |
| w1flg\_1 | int | - | aperture 1 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w2mag\_1 | real | mag | aperture 1 (5.50") instrumental aperture mag, band 2 |
| w2sigm\_1 | real | mag | aperture 1 instrumental aperture mag uncertainty, band 2 |
| w2flg\_1 | int | - | aperture 1 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w1mag\_2 | real | mag | aperture 2 (8.25") instrumental aperture mag, band 1 |
| w1sigm\_2 | real | mag | aperture 2 instrumental aperture mag uncertainty, band 1 |
| w1flg\_2 | int | - | aperture 2 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w2mag\_2 | real | mag | aperture 2 (8.25") instrumental aperture mag, band 2 |
| w2sigm\_2 | real | mag | aperture 2 instrumental aperture mag uncertainty, band 2 |
| w2flg\_2 | int | - | aperture 2 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w1mag\_3 | real | mag | aperture 3 (11.00") instrumental aperture mag, band 1 |
| w1sigm\_3 | real | mag | aperture 3 instrumental aperture mag uncertainty, band 1 |
| w1flg\_3 | int | - | aperture 3 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w2mag\_3 | real | mag | aperture 3 (11.00") instrumental aperture mag, band 2 |
| w2sigm\_3 | real | mag | aperture 3 instrumental aperture mag uncertainty, band 2 |
| w2flg\_3 | int | - | aperture 3 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w1mag\_4 | real | mag | aperture 4 (13.75") instrumental aperture mag, band 1 |
| w1sigm\_4 | real | mag | aperture 4 instrumental aperture mag uncertainty, band 1 |
| w1flg\_4 | int | - | aperture 4 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w2mag\_4 | real | mag | aperture 4 (13.75") instrumental aperture mag, band 2 |
| w2sigm\_4 | real | mag | aperture 4 instrumental aperture mag uncertainty, band 2 |
| w2flg\_4 | int | - | aperture 4 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w1mag\_5 | real | mag | aperture 5 (16.50") instrumental aperture mag, band 1 |
| w1sigm\_5 | real | mag | aperture 5 instrumental aperture mag uncertainty, band 1 |
| w1flg\_5 | int | - | aperture 5 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w2mag\_5 | real | mag | aperture 5 (16.50") instrumental aperture mag, band 2 |
| w2sigm\_5 | real | mag | aperture 5 instrumental aperture mag uncertainty, band 2 |
| w2flg\_5 | int | - | aperture 5 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w1mag\_6 | real | mag | aperture 6 (19.25") instrumental aperture mag, band 1 |
| w1sigm\_6 | real | mag | aperture 6 instrumental aperture mag uncertainty, band 1 |
| w1flg\_6 | int | - | aperture 6 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w2mag\_6 | real | mag | aperture 6 (19.25") instrumental aperture mag, band 2 |
| w2sigm\_6 | real | mag | aperture 6 instrumental aperture mag uncertainty, band 2 |
| w2flg\_6 | int | - | aperture 6 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w1mag\_7 | real | mag | aperture 7 (22.00") instrumental aperture mag, band 1 |
| w1sigm\_7 | real | mag | aperture 7 instrumental aperture mag uncertainty, band 1 |
| w1flg\_7 | int | - | aperture 7 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w2mag\_7 | real | mag | aperture 7 (22.00") instrumental aperture mag, band 2 |
| w2sigm\_7 | real | mag | aperture 7 instrumental aperture mag uncertainty, band 2 |
| w2flg\_7 | int | - | aperture 7 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w1mag\_8 | real | mag | aperture 8 (24.75") instrumental aperture mag, band 1 |
| w1sigm\_8 | real | mag | aperture 8 instrumental aperture mag uncertainty, band 1 |
| w1flg\_8 | int | - | aperture 8 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 1 |
| w2mag\_8 | real | mag | aperture 8 (24.75") instrumental aperture mag, band 2 |
| w2sigm\_8 | real | mag | aperture 8 instrumental aperture mag uncertainty, band 2 |
| w2flg\_8 | int | - | aperture 8 instrumental aperture [flag](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#apflag), band 2 |
| w1NM | int | - | number of profile-fit flux measurements for source with SNR >= 3, band 1 |
| w1M | int | - | number of profile-fit flux measurements for source, band 1 |
| w1magP | real | mag | profile-fit repeatability mag -- inverse-variance weighted mean mag, band 1 |
| w1sigP1 | real | mag | standard deviation of population of profile-fit repeatability mag, band 1 |
| w1sigP2 | real | mag | standard deviation of the mean of profile-fit repeatability mag, band 1 |
| w1k | real | - | Stetson K variability index, band 1 |
| w1Ndf | int | - | number degrees of freedom in variability chi^2, band 1 |
| w1mLQ | real | - | -ln(Q), where Q = 1 - P(chi^2), band 1 |
| w1mJDmin | double | d | minimum modified Julian Date of frame extractions, band 1 |
| w1mJDmax | double | d | maximum modified Julian Date of frame extractions, band 1 |
| w1mJDmean | double | d | mean modified Julian Date of frame extractions, band 1 |
| w2NM | int | - | number of profile-fit flux measurements for source with SNR >= 3, band 2 |
| w2M | int | - | number of profile-fit flux measurements for source, band 2 |
| w2magP | real | mag | profile-fit repeatability mag -- inverse-variance weighted mean mag, band 2 |
| w2sigP1 | real | mag | standard deviation of population of profile-fit repeatability mag, band 2 |
| w2sigP2 | real | mag | standard deviation of the mean of profile-fit repeatability mag, band 2 |
| w2k | real | - | Stetson K variability index, band 2 |
| w2Ndf | int | - | number degrees of freedom in variability chi^2, band 2 |
| w2mLQ | real | - | -ln(Q), where Q = 1 - P(chi^2), band 2 |
| w2mJDmin | double | d | minimum modified Julian Date of frame extractions, band 2 |
| w2mJDmax | double | d | maximum modified Julian Date of frame extractions, band 2 |
| w2mJDmean | double | d | mean modified Julian Date of frame extractions, band 2 |
| rho12 | int | % | band 1 - band 2 correlation coefficient |
| q12 | int | % | -log10(1 - P(rho12)), given no real correlation |
| nIters | int | - | number of chi-square minimization iterations |
| nSteps | int | - | number of steps in all iterations |
| mdetID | int | - | source ID in mdet list |
| p1 | real | arcsec | distance in ra from the mdet position to the wphot template-fit position |
| p2 | real | arcsec | distance in dec from the mdet position to the wphot template-fit position |
| MeanObsMJD | double | d | mean observation epoch |
| ra\_pm | double | deg | Right ascension from psf model incl. motion at epoch MJD=56700.0 (2014.118) for Preliminary Catalog and MJD=57170 (2015.405) for CatWISE2020 |
| dec\_pm | double | deg | Declination from psf model incl. motion at epoch MJD=56700.0 (2014.118) for Preliminary Catalog and MJD=57170 (2015.405) for CatWISE2020 |
| sigra\_pm | real | arcsec | One-sigma uncertainty in RA from psf model incl. motion |
| sigdec\_pm | real | arcsec | One-sigma uncertainty in DEC from psf model incl. motion |
| sigradec\_pm | real | arcsec | The co-sigma of the equatorial position uncertainties from psf model incl motion |
| PMRA | real | arcsec/yr | Apparent motion in RA; (note [uncorrected systematic](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/CatWISE2020_Table1_20201012.tbl) in CatWISE2020) |
| PMDec | real | arcsec/yr | Apparent motion in Dec; (note [uncorrected systematic](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/CatWISE2020_Table1_20201012.tbl) in CatWISE2020) |
| sigPMRA | real | arcsec/yr | Uncertainty in the RA motion estimate |
| sigPMDec | real | arcsec/yr | Uncertainty in the Dec motion estimate |
| w1snr\_pm | real | -- | S/N ratio of the W1 profile-fit photometry including motion |
| w2snr\_pm | real | -- | S/N ratio of the W2 profile-fit photometry including motion |
| w1flux\_pm | real | 'dn' | Raw flux W1 profile-fit photometry including motion |
| w1sigflux\_pm | real | 'dn' | Raw flux uncertainty W1 profile-fit photometry including motion |
| w2flux\_pm | real | 'dn' | Raw flux W2 profile-fit photometry including motion |
| w2sigflux\_pm | real | 'dn' | Raw flux uncertainty W2 profile-fit photometry including motion |
| w1mpro\_pm | real | mag | W1 magnitude from profile-fit photometry including motion |
| w1sigmpro\_pm | real | mag | W1 flux uncertainty in mag units from profile-fit photometry including motion |
| w1rchi2\_pm | real | -- | Reduced chi^2 of the W1 profile-fit photometry measurement including motion est |
| w2mpro\_pm | real | mag | W2 magnitude from profile-fit photometry including motion |
| w2sigmpro\_pm | real | mag | W2 flux uncertainty in mag units from profile-fit photometry including motion |
| w2rchi2\_pm | real | -- | Reduced chi^2 of the W2 profile-fit photometry measurement including motion est |
| rchi2\_pm | real | -- | Combined Reduced chi^2 in all bands for the psf photometry includes src motion |
| pmcode | char | - | Motion estimate quality code: the format is ABCCC, where A is the number of components in the passive blend group (including the primary) before any are removed or added, B is "Y" or "N" to indicate "Yes" or "No" that a secondary blend component replaced the primary, and CCC is the distance in hundredths of an arcsec between the PM position solution for the mean observation epoch and the stationary solution |
| nIters\_pm | int | - | number of chi-square minimization iterations |
| nSteps\_pm | int | - | number of steps in all iterations |
| dist\_ad | real | arcsec | radial distance between source positions in ascending and descending scans |
| dw1mag | real | mag | difference in w1mpro between ascending and descending scans |
| rch2w1 | real | - | chi-square for dw1mag (1 degree of freedom) |
| dw2mag | real | mag | difference in w2mpro between ascending and descending scans |
| rch2w2 | real | - | chi-square for dw2mag (1 degree of freedom) |
| elon\_avg | double | deg | average ecliptic longitude |
| elonSig | real | arcsec | uncertainty in elon\_avg |
| elat\_avg | double | deg | average ecliptic latitude |
| elatSig | real | arcsec | uncertainty in elat\_avg |
| Delon | real | arcsec | descending scan - ascending scan ecliptic longitude difference ( [notes](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#delonnotes)) |
| DelonSig | real | arcsec | one-sigma uncertainty in Delon |
| Delat | real | arcsec | descending scan - ascending scan ecliptic longitude difference |
| DelatSig | real | arcsec | one-sigma uncertainty in Delat |
| DelonSNR | real | - | abs(Delon)/DelonSig |
| DelatSNR | real | - | abs(Delat)/DelatSig |
| chi2pmra | real | - | chi-square for PMRA difference (1 degree of freedom) |
| chi2pmdec | real | - | chi-square for PMDec difference (1 degree of freedom) |
| ka | int | - | astrometry usage code:

|     |     |
| --- | --- |
| 0 | neither the ascending nor the descending scan provided a solution |
| 1 | only the ascending scan provided a solution |
| 2 | only the descending scan provided a solution |
| 3 | both scans provided solutions which were combined in the relevant way | |
| k1 | int | - | W1 photometry usage code:

|     |     |
| --- | --- |
| 0 | neither the ascending nor the descending scan provided a solution |
| 1 | only the ascending scan provided a solution |
| 2 | only the descending scan provided a solution |
| 3 | both scans provided solutions which were combined in the relevant way | |
| k2 | int | - | W2 photometry usage code:

|     |     |
| --- | --- |
| 0 | neither the ascending nor the descending scan provided a solution |
| 1 | only the ascending scan provided a solution |
| 2 | only the descending scan provided a solution |
| 3 | both scans provided solutions which were combined in the relevant way | |
| km | int | - | proper motion usage code:

|     |     |
| --- | --- |
| 0 | neither the ascending nor the descending scan provided a solution |
| 1 | only the ascending scan provided a solution |
| 2 | only the descending scan provided a solution |
| 3 | both scans provided solutions which were combined in the relevant way | |
| par\_pm | real | arcsec | parallax from PM desc-asce elon ( [notes](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#delonnotes)) |
| par\_pmSig | real | arcsec | one-sigma uncertainty in par\_pm |
| par\_stat | real | arcsec | parallax estimate from stationary solution ( [notes](https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html#delonnotes)) |
| par\_sigma | real | arcsec | one-sigma uncertainty in par\_stat |
| dist\_cc | double | arcsec | distance between CatWISE and AllWISE source |
| cc\_flags | char |  | worst case 4 character cc\_flag from AllWISE (See Table A1 in [Eisenhardt et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020ApJS..247...69E/abstract)) |
| w1cc\_map | int |  | worst case w1cc\_map from AllWISE (See Table A1 in [Eisenhardt et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020ApJS..247...69E/abstract)) |
| w1cc\_map\_str | char |  | worst case w1cc\_map\_str from AllWISE (See Table A1 in [Eisenhardt et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020ApJS..247...69E/abstract)) |
| w2cc\_map | int |  | worst case w2cc\_map from AllWISE (See Table A1 in [Eisenhardt et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020ApJS..247...69E/abstract)) |
| w2cc\_map\_str | char |  | worst case w2cc\_map\_str from AllWISE (See Table A1 in [Eisenhardt et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020ApJS..247...69E/abstract)) |
| n\_aw | int |  | number of sources within 2.75" in AllWISE |
| ab\_flags | char |  | unWISE artifact bitmask contamination flags |
| w1ab\_map | int |  | unWISE artifact bitmask contamination map for W1 |
| w1ab\_map\_str | char |  | unWISE artifact bitmask contamination string for W1 |
| w2ab\_map | int |  | unWISE artifact bitmask contamination map for W2 |
| w2ab\_map\_str | char |  | unWISE artifact bitmask contamination string for W2 |
| glon | double | deg | Galactic longitude (only present in CatWISE 2020) |
| glat | double | deg | Galactic latitude (only present in CatWISE 2020) |

| elon | double | deg | Ecliptic longitude |
| elat | double | deg | Ecliptic latitude |
| unwise\_objid | char |  | UnWISE Object ID (only present in CatWISE 2020) |
| P | int | - | Flag to indicate if source measurement is from primary tile (only present in Reject Tables) |

**Standard aperture measurement quality flag**: This flag
indicates if one or more image pixels in the measurement aperture for this
band is confused with nearby objects, is contaminated by saturated
or otherwise ususable pixels, or is an upper limit. The flag value
is the integer sum of any of following values which correspond to
different conditions.

| value | condition |
| --- | --- |
| 0 | nominal -- no contamination |
| 1 | source confusion -- another source falls within the measurement aperture |
| 2 | bad or fatal pixels: presence of bad pixels in the measurement aperture (bit 2 or 18 set) |
| 4 | non-zero bit flag tripped (other than 2 or 18) |
| 8 | corruption -- all pixels are flagged as unusable, or the aperture flux is<br> negative; in the former case, the aperture magnitude is NULL; in the<br> latter case, the aperture magnitude is a 95% confidence upper limit |
| 16 | saturation -- here are one or more saturated pixels in the measurement aperture |
| 32 | upper limit -- the magnitude is a 95% confidence upper limit |

**Notes about Delon, par\_pm, and par\_stat:**

1. Delon is defined as (descending ecliptic longitude - ascending ecliptic longitude)cos(ecliptic latitude) - (bias term) in order to have the proper sign for parallax, which is approximately Delon/2.
2. The bias term is 0.045 arcsec for CatWISE2020 and 0.090 arcsec for the Preliminary Catalog, and is also applied when calculating par\_pm and par\_stat. The bias term corrects for residual PSF errors that manifest themselves in ascending-descending differences.
3. Delon ignores the different effective observation epochs of ascending and descending scans. The par\_pm column is computed by first using the motion estimate to translate the motion-solution positions to the standard epoch (MJD 57170 for CatWISE2020 and MJD 56700 for the Preliminary Catalog). The two ecliptic longitudes are then subtracted, the bias term is applied, and the result is divided by 2 to estimate the parallax. The par\_stat column is computed by using the motion estimate to move the ascending stationary-solution position from the ascending effective observation epoch to that of the descending solution, then dividing the bias-corrected ecliptic longitude difference by 2.
4. Delon will be null unless ka = 3; par\_pm will be null unless km = 3; par\_stat will be null unless ka = 3 AND km > 0 AND all W?mJDmin/max/mean values are non-null in both ascending and descending solutions.

- [Contact](https://irsa.ipac.caltech.edu/docs/help_desk.html)
- [Privacy Policy](https://irsa.ipac.caltech.edu/privacy.html)
- [Acknowledge IRSA](https://irsa.ipac.caltech.edu/ack.html)

Search IRSA

[![Icon_ipac](https://irsa.ipac.caltech.edu/frontpage/images/icon_ipac-white-78x60.png)](http://www.ipac.caltech.edu/ "Infrared Processing and Analysis Center")[![Icon_caltech](https://irsa.ipac.caltech.edu/frontpage/images/icon_caltech-new.png)](http://www.caltech.edu/ "California Institute of Technology")[![Icon_jpl](https://irsa.ipac.caltech.edu/frontpage/images/icon_jpl-white-91x60.png)](http://www.jpl.nasa.gov/ "Jet Propulsion Laboratory")[![Icon_nasa](https://irsa.ipac.caltech.edu/frontpage/images/icon_nasa-white-59x60.png)](http://www.nasa.gov/ "National Aeronautics and Space Administration")
