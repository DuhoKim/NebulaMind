URL: https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html

- [Home](https://desidatamodel.readthedocs.io/en/25.3/index.html)
- [DESI\_ROOT](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/index.html)
- [survey](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/index.html)
- [catalogs](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/index.html)
- [RELEASE](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/index.html)
- [LSS](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/index.html)
- [SPECPROD](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/index.html)
- [LSScats](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/index.html)
- [VERSIONpip](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/index.html)
- DATA full LSS catalogs with PIP weights
- [View page source](https://desidatamodel.readthedocs.io/en/25.3/_sources/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.rst.txt)

* * *

# DATA full LSS catalogs with PIP weights [](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html\#data-full-lss-catalogs-with-pip-weights "Link to this heading")

Summary:

LSS catalogs containing information on all targets identified as reachable by DESI fiberassign, with one entry for each. The files are split by target type and whether of not vetos for angular positions and healpix maps have been applied

Naming Convention:

`{TARGET}_full{VETO}.dat.fits`, where `{TARGET}` is the target type: `QSO`, `ELG_LOPnotqso`, `LRG`, for dark or `BGS_ANY`, `BGS_BRIGHT` for bright. `{VETO}` is `_noveto` if vetos have not been applied, blank if vetos have been applied and `_HPmapcut` if both vetos and healpix map cuts have been applied.

Regex:

`[a-zA-Z_]+\_full[a-z_]{0,7,9}.dat.fits`

File Type:

FITS, 11 GB

## Contents [](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html\#contents "Link to this heading")

| Number | EXTNAME | Type | Contents |
| --- | --- | --- | --- |
| [HDU0](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#hdu0) |  | IMAGE | Empty |
| [HDU1](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#hdu1) | LSS | BINTABLE | Catalog data |

## FITS Header Units [](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html\#fits-header-units "Link to this heading")

### HDU0 [](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html\#hdu0 "Link to this heading")

This HDU has no non-standard required keywords.

Empty HDU.

### HDU1 [](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html\#hdu1 "Link to this heading")

EXTNAME = LSS

Catalog data for the given target type; one entry per unique TARGETID with PIP weights

#### Required Header Keywords [](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html\#required-header-keywords "Link to this heading")

Required Header Keywords Table

| KEY | Example Value | Type | Comment |
| --- | --- | --- | --- |
| NAXIS1 | 838 | int | length of dimension 1 |
| NAXIS2 | 15327895 | int | length of dimension 2 |
| DESIDR | dr1 | str | DESI Data Release |

#### Required Data Table Columns [](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html\#required-data-table-columns "Link to this heading")

| Name | Type | Units | Description |
| --- | --- | --- | --- |
| TARGETID | int64 |  | Unique DESI target ID |
| MWS\_TARGET | int64 |  | Milky Way Survey targeting bits |
| SUBPRIORITY | float64 |  | Random subpriority \[0-1) to break assignment ties |\
| PRIORITY\_INIT | int64 |  | Target initial priority from target selection bitmasks and OBSCONDITIONS |\
| TARGET\_STATE | char\[30\] |  | Combination of target class and its current observational state |\
| TIMESTAMP | char\[25\] | s | UTC/ISO time at which the target state was updated |\
| LOCATION | int64 |  | Location on the focal plane PETAL\_LOC\*1000 + DEVICE\_LOC |\
| TILEID | int64 |  | Unique DESI tile ID |\
| TILELOCID | int64 |  | Is 10000\*TILEID+LOCATION |\
| LASTNIGHT | int32 |  | Final night of observation included in a series of coadds |\
| Z | float64 |  | Redshift measured by Redrock |\
| ZERR | float64 |  | Redshift error from redrock |\
| ZWARN | int64 |  | Redshift warning bitmask from Redrock |\
| CHI2 | float64 |  | Best fit chi squared |\
| COEFF | float64\[10\] |  | Redrock template coefficients |\
| NPIXELS | int64 |  | Number of unmasked pixels contributing to the Redrock fit |\
| SPECTYPE | char\[6\] |  | Spectral type of Redrock best fit template (e.g. GALAXY, QSO, STAR) |\
| SUBTYPE | char\[20\] |  | Spectral subtype |\
| NCOEFF | int64 |  | Number of Redrock template coefficients |\
| DELTACHI2 | float64 |  | chi2 difference between first- and second-best redrock template fits |\
| FIBER | int32 |  | Fiber ID on the CCDs \[0-4999\] |\
| COADD\_FIBERSTATUS | int32 |  | bitwise-AND of input FIBERSTATUS |\
| FIBERASSIGN\_X | float32 | mm | Fiberassign expected CS5 X location on focal plane |\
| FIBERASSIGN\_Y | float32 | mm | Fiberassign expected CS5 Y location on focal plane |\
| PRIORITY | int32 |  | Target current priority |\
| COADD\_NUMEXP | int16 |  | Number of exposures in coadd |\
| COADD\_EXPTIME | float32 | s | Summed exposure time for coadd |\
| COADD\_NUMNIGHT | int16 |  | Number of nights in coadd |\
| MEAN\_DELTA\_X | float32 | mm | Mean (over exposures) fiber difference requested - actual CS5 X location on focal plane |\
| RMS\_DELTA\_X | float32 | mm | RMS (over exposures) of the fiber difference between measured and requested CS5 X location on focal plane |\
| MEAN\_DELTA\_Y | float32 | mm | Mean (over exposures) fiber difference requested - actual CS5 Y location on focal plane |\
| RMS\_DELTA\_Y | float32 | mm | RMS (over exposures) of the fiber difference between measured and requested CS5 Y location on focal plane |\
| MEAN\_PSF\_TO\_FIBER\_SPECFLUX | float32 |  | Mean of input exposures fraction of light from point-like source captured by 1.5 arcsec diameter fiber given atmospheric seeing |\
| TSNR2\_ELG\_B | float32 |  | ELG B template (S/N)^2 |\
| TSNR2\_LYA\_B | float32 |  | LYA B template (S/N)^2 |\
| TSNR2\_BGS\_B | float32 |  | BGS B template (S/N)^2 |\
| TSNR2\_QSO\_B | float32 |  | QSO B template (S/N)^2 |\
| TSNR2\_LRG\_B | float32 |  | LRG B template (S/N)^2 |\
| TSNR2\_ELG\_R | float32 |  | ELG R template (S/N)^2 |\
| TSNR2\_LYA\_R | float32 |  | LYA R template (S/N)^2 |\
| TSNR2\_BGS\_R | float32 |  | BGS R template (S/N)^2 |\
| TSNR2\_QSO\_R | float32 |  | QSO R template (S/N)^2 |\
| TSNR2\_LRG\_R | float32 |  | LRG R template (S/N)^2 |\
| TSNR2\_ELG\_Z | float32 |  | ELG Z template (S/N)^2 |\
| TSNR2\_LYA\_Z | float32 |  | LYA Z template (S/N)^2 |\
| TSNR2\_BGS\_Z | float32 |  | BGS Z template (S/N)^2 |\
| TSNR2\_QSO\_Z | float32 |  | QSO Z template (S/N)^2 |\
| TSNR2\_LRG\_Z | float32 |  | LRG Z template (S/N)^2 |\
| TSNR2\_ELG | float32 |  | ELG template (S/N)^2 summed over B,R,Z |\
| TSNR2\_LYA | float32 |  | LYA template (S/N)^2 summed over B,R,Z |\
| TSNR2\_BGS | float32 |  | BGS template (S/N)^2 summed over B,R,Z |\
| TSNR2\_QSO | float32 |  | QSO template (S/N)^2 summed over B,R,Z |\
| TSNR2\_LRG | float32 |  | LRG template (S/N)^2 summed over B,R,Z |\
| ZWARN\_MTL | int64 |  | The ZWARN from the zmtl file (contains extra bits) |\
| Z\_QN | float64 |  | Redshift measured by QuasarNET using line with highest confidence |\
| Z\_QN\_CONF | float64 |  | Redshift confidence from QuasarNET |\
| IS\_QSO\_QN | int16 |  | Spectroscopic classification from QuasarNET (1 for a quasar) |\
| PRIORITY\_ASSIGNED | int32 |  | (only for data) PRIORITY of the target that was assigned to the given FIBER and TILEID (redundant with PRIORITY in the random catalogs) |\
| GOODPRI | logical |  | True/False whether the priority of what was assigned to the location was &lt;= the base priority of the given target class |\
| GOODHARDLOC | logical |  | True/False whether the fiber had good hardware |\
| LOCATION\_ASSIGNED | logical |  | True/False for assigned/unassigned for the target in question |\
| TILELOCID\_ASSIGNED | logical |  | 0/1 for unassigned/assigned for TILELOCID in question (it could have been assigned to a different target) |\
| GOODTSNR | logical |  | True/False whether the TSNR (class) value used was above the minimum threshold for the given target class |\
| NTILE | int64 |  | Number of tiles target was available on |\
| TILES | char\[36\] |  | TILEIDs of those tile, in string form separated by - |\
| TILELOCIDS | char\[111\] |  | TILELOCIDs that the target was available for, separated by - |\
| BRICKID | int32 |  | Brick ID from tractor input |\
| BRICKNAME | char\[8\] |  | Brick name from tractor input |\
| MORPHTYPE | char\[4\] |  | Imaging Surveys morphological type from Tractor |\
| RA | float64 | deg | Barycentric Right Ascension in ICRS |\
| DEC | float64 | deg | Barycentric declination in ICRS |\
| DCHISQ | float32\[5\] |  | Difference in chi-squared between Tractor model fits |\
| EBV | float32 | mag | Galactic extinction E(B-V) reddening from SFD98 |\
| FLUX\_G | float32 | nanomaggy | Flux in the Legacy Survey g-band (AB) |\
| FLUX\_R | float32 | nanomaggy | Flux in the Legacy Survey r-band (AB) |\
| FLUX\_Z | float32 | nanomaggy | Flux in the Legacy Survey z-band (AB) |\
| FLUX\_IVAR\_G | float32 | nanomaggy^-2 | Inverse variance of FLUX\_G (AB) |\
| FLUX\_IVAR\_R | float32 | nanomaggy^-2 | Inverse variance of FLUX\_R (AB) |\
| FLUX\_IVAR\_Z | float32 | nanomaggy^-2 | Inverse variance of FLUX\_Z (AB) |\
| MW\_TRANSMISSION\_G | float32 |  | Milky Way dust transmission in LS g-band |\
| MW\_TRANSMISSION\_R | float32 |  | Milky Way dust transmission in LS r-band |\
| MW\_TRANSMISSION\_Z | float32 |  | Milky Way dust transmission in LS z-band |\
| NOBS\_G | int16 |  | Number of images for central pixel in g-band |\
| NOBS\_R | int16 |  | Number of images for central pixel in r-band |\
| NOBS\_Z | int16 |  | Number of images for central pixel in z-band |\
| PSFDEPTH\_G | float32 | nanomaggy^-2 | PSF-based depth in g-band |\
| PSFDEPTH\_R | float32 | nanomaggy^-2 | PSF-based depth in r-band |\
| PSFDEPTH\_Z | float32 | nanomaggy^-2 | PSF-based depth in z-band |\
| GALDEPTH\_G | float32 | nanomaggy^-2 | Galaxy model-based depth in LS g-band |\
| GALDEPTH\_R | float32 | nanomaggy^-2 | Galaxy model-based depth in LS r-band |\
| GALDEPTH\_Z | float32 | nanomaggy^-2 | Galaxy model-based depth in LS z-band |\
| FLUX\_W1 | float32 | nanomaggy | WISE flux in W1 (AB) |\
| FLUX\_W2 | float32 | nanomaggy | WISE flux in W2 (AB) |\
| FLUX\_IVAR\_W1 | float32 | nanomaggy^-2 | Inverse variance of FLUX\_W1 (AB) |\
| FLUX\_IVAR\_W2 | float32 | nanomaggy^-2 | Inverse variance of FLUX\_W2 (AB) |\
| MW\_TRANSMISSION\_W1 | float32 |  | Milky Way dust transmission in WISE W1 |\
| MW\_TRANSMISSION\_W2 | float32 |  | Milky Way dust transmission in WISE W2 |\
| FIBERFLUX\_G | float32 | nanomaggy | Predicted g-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing |\
| FIBERFLUX\_R | float32 | nanomaggy | Predicted r-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing |\
| FIBERFLUX\_Z | float32 | nanomaggy | Predicted z-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing |\
| FIBERTOTFLUX\_G | float32 | nanomaggy | Predicted g-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing |\
| FIBERTOTFLUX\_R | float32 | nanomaggy | Predicted r-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing |\
| FIBERTOTFLUX\_Z | float32 | nanomaggy | Predicted z-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing |\
| WISEMASK\_W1 | binary |  | Bitwise mask for WISE W1 data |\
| WISEMASK\_W2 | binary |  | Bitwise mask for WISE W2 data |\
| MASKBITS | int16 |  | Bitwise mask from the imaging indicating potential issue or blending |\
| SHAPE\_R | float32 | arcsec | Half-light radius of galaxy model (greater than 0) |\
| PHOTSYS | char\[1\] |  | N for the MzLS/BASS photometric system, S for DECaLS |\
| DESI\_TARGET | int64 |  | DESI (dark time program) target selection bitmask |\
| BGS\_TARGET | int64 |  | BGS (Bright Galaxy Survey) target selection bitmask |\
| OII\_FLUX [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float32 | 10\*\*-17 erg/(s cm2) | Fitted flux for the \[OII\] doublet |\
| OII\_FLUX\_IVAR [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float32 | 10\*\*+34 (s2 cm4) / erg2 | Inverse variance of the fitted flux for the \[OII\] doublet |\
| o2c [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float64 | 10\*\*+34 (s2 cm4) / erg2 | (lower or uppercase) The criteria for assessing strength of OII emission for ELG observations |\
| Z\_RR [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float64 |  | Redshift collected from redrock file |\
| lrg\_mask [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | binary |  | (lower or upper case) Imaging mask bits relevant to LRG targets |\
| ABSMAG01\_SDSS\_G [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float32 | mag | g-corrected (to z=0.1) absolute magnitude in the SDSS g band from fastspecfit |\
| ABSMAG01\_SDSS\_R [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float32 | mag | r-corrected (to z=0.1) absolute magnitude in the SDSS r band from fastspecfit |\
| WEIGHT\_IMLIN [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float64 |  | Imaging systematics weights derived with the eBOSS linear regression method |\
| WEIGHT\_FKP [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float64 |  | 1/(1+NZ\*P0), with P0 different for each tracer |\
| WEIGHT\_RF [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float64 |  | Imaging systematics weights derived with the regressis random forest regression method |\
| WEIGHT\_SN [\[1\]](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html#id12) | float64 |  | Imaging systematics weights derived with the sysnet NN regression method |\
| COMP\_TILE | float64 |  | Assignment completeness for all targets of this type with the same value for TILES |\
| FRACZ\_TILELOCID | float64 |  | The fraction of targets of this type at this TILELOCID that received an observation (after forcing each target to a unique TILELOCID) |\
| WEIGHT\_ZFAIL | float64 |  | Should be all 1 at this point for main survey |\
| mod\_success\_rate | float64 |  | Expected spectroscopic success rate given the target and observation properties |\
| BITWEIGHTS | int64\[2\] |  | A size of two 64 bit masks that encodes which of the alternative assignment histories that the target was assigned in |\
| PROB\_OBS | float64 |  | The number alternative assignment histories that the target was assigned in divided by 128 |\
\
## Notes and Examples [](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html\#notes-and-examples "Link to this heading")\
\
These catalogs are the same as those find under VERSION, but with PIP weights in the WEIGHT column, obtained through the AltMTL pipeline.\
They use the same observing conditions and systematic maps as the version wihout PIP weights. Healpix maps found in the other directory.\
\
Versions[latest](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html)[stable](https://desidatamodel.readthedocs.io/en/stable/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html)**[25.3](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html)**[24.9](https://desidatamodel.readthedocs.io/en/24.9/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html)[23.1](https://desidatamodel.readthedocs.io/en/23.1/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/desidatamodel/?utm_source=desidatamodel&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/desidatamodel/builds/?utm_source=desidatamodel&utm_content=flyout)Search\
\
* * *\
\
[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=desidatamodel&utm_content=flyout) ― Hosted by\
[Read the Docs](https://about.readthedocs.com/?utm_source=desidatamodel&utm_content=flyout)
