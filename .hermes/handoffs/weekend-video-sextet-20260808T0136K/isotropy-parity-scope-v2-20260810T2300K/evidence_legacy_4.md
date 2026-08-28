URL: https://www.legacysurvey.org/dr10/files

[Skip to main content](https://www.legacysurvey.org/dr10/files/#content)

## [Directory Structures](https://www.legacysurvey.org/dr10/files/\#toc-entry-1)

### [For Web Access](https://www.legacysurvey.org/dr10/files/\#toc-entry-2)

**Top level directory:**

[https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/)

**Top level directory for sweep catalogs:**

[https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/)

### [At NERSC (for collaborators)](https://www.legacysurvey.org/dr10/files/\#toc-entry-3)

**Top level directory:**

/global/cfs/cdirs/cosmo/data/legacysurvey/dr10/

**Top level directory for sweep catalogs:**

/global/cfs/cdirs/cosmo/data/legacysurvey/dr10/south/sweep/

## [Summary Files](https://www.legacysurvey.org/dr10/files/\#toc-entry-4)

### [survey-bricks.fits.gz](https://www.legacysurvey.org/dr10/files/\#toc-entry-5)

FITS binary table with the RA, Dec bounds of each geometrical "brick" on the sky.
This includes all bricks on the sky, not just the ones in our footprint or with
coverage in DR10. For that information, see the next file description.

| Column | Type | Description |
| --- | --- | --- |
| `BRICKNAME` | char\[8\] | Name of the brick. |
| `BRICKID` | int32 | A unique integer with 1-to-1 mapping to `brickname`. |
| `BRICKQ` | int16 | A "priority" factor used for processing. |
| `BRICKROW` | int32 | Dec row number. |
| `BRICKCOL` | int32 | Number of the brick within a Dec row. |
| `RA` | float64 | RA of the center of the brick. |
| `DEC` | float64 | Dec of the center of the brick. |
| `RA1` | float64 | Lower RA boundary. |
| `RA2` | float64 | Upper RA boundary. |
| `DEC1` | float64 | Lower Dec boundary. |
| `DEC2` | float64 | Upper Dec boundary. |

### [south/survey-bricks-dr10-south.fits.gz](https://www.legacysurvey.org/dr10/files/\#toc-entry-6)

A FITS binary table with information that summarizes the contents of each brick in DR10.

| Column | Type | Description |
| --- | --- | --- |
| `brickname` | char\[8\] | Name of the brick. |
| `ra` | float64 | RA of the center of the brick. |
| `dec` | float64 | Dec of the center of the brick. |
| `nexp_g` | int16 | Median number of exposures in the unique area (i.e. `BRICK_PRIMARY` area) of the brick in gg-band. |
| `nexp_r` | int16 | Median number of exposures in the unique area of the brick in rr-band. |
| `nexp_i` | int16 | Median number of exposures in the unique area of the brick in ii-band. |
| `nexp_z` | int16 | Median number of exposures in the unique area of the brick in zz-band. |
| `nexphist_g` | int32\[11\] | Histogram of number of pixels in the unique brick area with 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, or > 10 exposures in gg. |
| `nexphist_r` | int32\[11\] | Histogram of number of pixels in the unique brick area with 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, or > 10 exposures in rr. |
| `nexphist_i` | int32\[11\] | Histogram of number of pixels in the unique brick area with 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, or > 10 exposures in ii. |
| `nexphist_z` | int32\[11\] | Histogram of number of pixels in the unique brick area with 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, or > 10 exposures in zz. |
| `nobjs` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of all types. |
| `npsf` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of type `PSF`. See also [the larger description](https://www.legacysurvey.org/dr10/description/#morphological-classification). |
| `nsimp` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of type `SIMP` (there should be 0 such objects). |
| `nrex` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of type `REX`. See also [the larger description](https://www.legacysurvey.org/dr10/description/#morphological-classification). |
| `nexp` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of type `EXP`. See also [the larger description](https://www.legacysurvey.org/dr10/description/#morphological-classification). |
| `ndev` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of type `DEV`. See also [the larger description](https://www.legacysurvey.org/dr10/description/#morphological-classification). |
| `ncomp` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of type `COMP` (there should be 0 such objects). |
| `nser` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of type `SER`. See also [the larger description](https://www.legacysurvey.org/dr10/description/#morphological-classification). |
| `ndup` | int32 | Total number of `BRICK_PRIMARY` objects in this brick, of type `DUP`. See also [the larger description](https://www.legacysurvey.org/dr10/description/#morphological-classification). |
| `psfsize_g` | float32 | Median PSF size, in arcsec, evaluated at the `BRICK_PRIMARY` objects in this brick in gg-band. |
| `psfsize_r` | float32 | Median PSF size, in arcsec, evaluated at the `BRICK_PRIMARY` objects in this brick in rr-band. |
| `psfsize_i` | float32 | Median PSF size, in arcsec, evaluated at the `BRICK_PRIMARY` objects in this brick in ii-band. |
| `psfsize_z` | float32 | Median PSF size, in arcsec, evaluated at the `BRICK_PRIMARY` objects in this brick in zz-band. |
| `psfdepth_g` | float32 | 5-sigma PSF detection depth in gg-band (AB mag), using PsfEx PSF model. |
| `psfdepth_r` | float32 | 5-sigma PSF detection depth in rr-band (AB mag), using PsfEx PSF model. |
| `psfdepth_i` | float32 | 5-sigma PSF detection depth in ii-band (AB mag), using PsfEx PSF model. |
| `psfdepth_z` | float32 | 5-sigma PSF detection depth in zz-band (AB mag), using PsfEx PSF model. |
| `galdepth_g` | float32 | 5-sigma galaxy (0.45" round exp) detection depth in gg-band (AB) mag. |
| `galdepth_r` | float32 | 5-sigma galaxy (0.45" round exp) detection depth in rr-band (AB) mag. |
| `galdepth_i` | float32 | 5-sigma galaxy (0.45" round exp) detection depth in ii-band (AB) mag. |
| `galdepth_z` | float32 | 5-sigma galaxy (0.45" round exp) detection depth in zz-band (AB) mag. |
| `ebv` | float32 | Median [SFD98](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract) dust map E(B-V) extinction, in magnitudes, evaluated at `BRICK_PRIMARY` objects in this brick. |
| `trans_g` | float32 | Median Milky Way dust transparency in gg-band, based on `ebv`. See also `MW_TRANSMISSION_G`. |
| `trans_r` | float32 | Median Milky Way dust transparency in rr-band, based on `ebv`. See also `MW_TRANSMISSION_R`. |
| `trans_i` | float32 | Median Milky Way dust transparency in ii-band, based on `ebv`. See also `MW_TRANSMISSION_I`. |
| `trans_z` | float32 | Median Milky Way dust transparency in zz-band, based on `ebv`. See also `MW_TRANSMISSION_Z`. |
| `cosky_g` | float32 | Estimated sky level in the coadded images (stacks) in gg-band [\[1\]](https://www.legacysurvey.org/dr10/files/#footnote-1). |
| `cosky_r` | float32 | Estimated sky level in the coadded images (stacks) in rr-band. |
| `cosky_i` | float32 | Estimated sky level in the coadded images (stacks) in ii-band. |
| `cosky_z` | float32 | Estimated sky level in the coadded images (stacks) in zz-band. |
| `ext_g` | float32 | Extinction in gg-band. |
| `ext_r` | float32 | Extinction in rr-band. |
| `ext_i` | float32 | Extinction in ii-band. |
| `ext_z` | float32 | Extinction in zz-band. |
| `wise_nobs` | int16\[4\] | Number of images that contributed to WISE calculations in each filter (not profile-weighted). |
| `trans_wise` | float32\[4\] | Median Milky Way dust transparency in WISE bands, based on `ebv`. See also, e.g., `MW_TRANSMISSION_W1`. |
| `ext_w1` | float32 | Extinction in W1W1-band. |
| `ext_w2` | float32 | Extinction in W2W2-band. |
| `ext_w3` | float32 | Extinction in W3W3-band. |
| `ext_w4` | float32 | Extinction in W4W4-band. |
| `brickid` | int32 | A unique integer with 1-to-1 mapping to `brickname`. |
| `ra1` | float64 | Lower RA boundary. |
| `ra2` | float64 | Upper RA boundary. |
| `dec1` | float64 | Lower Dec boundary. |
| `dec2` | float64 | Upper Dec boundary. |
| `area` | float64 | Area of the brick in square degrees. |
| `survey_primary` | boolean | `True` for northern (southern) bricks that lie in the northern (southern) footprint of the Legacy Surveys. |
| `in_desi` | boolean | `True` if the brick is in the DESI footprint. |

Note that, for the `nexphist` rows, pixels that are masked by the NOIRLab Community Pipeline as, e.g., cosmic rays or saturation
(see, e.g. the `ALLMASK/ANYMASK` information on the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks)), do
_not_ count toward the number of exposures. More information about the morphological types and `MW_TRANSMISSION` can be found on
the [catalogs page](https://www.legacysurvey.org/dr10/catalogs).

### [survey-ccds-decam-dr10.fits.gz](https://www.legacysurvey.org/dr10/files/\#toc-entry-7)

A FITS binary table with almanac information about each individual CCD image for each camera.

This file contains information regarding the photometric and astrometric zero points for each CCD of every image that is part of the DR10 data release. Photometric zero points for each CCD are computed by identifying stars and comparing their instrumental magnitudes to color-selected stars in [the PanSTARRS "qz" catalog](https://www.legacysurvey.org/dr10/external).

The photometric zeropoints (`zpt`, `ccdzpt`, etc)
are magnitude-like numbers (e.g. 25.04), and
indicate the magnitude of a source that would contribute one count per
second to the image. For example, in an image with zeropoint of 25.04
and exposure time of 30 seconds, a source of magnitude 22.5 would
contribute
30×10((25.04−22.5)/2.5)=311.330×10((25.04−22.5)/2.5)=311.3
counts.

| Column | Type | Description |
| --- | --- | --- |
| `image_filename` | char\[65\] | Path to FITS image, _e.g._ "decam/CP/V5.2.2LS/CP20140328/c4d\_140329\_040642\_ooi\_r\_ls10.fits.fz". |
| `image_hdu` | int16 | FITS HDU number in the `image_filename` file where this image can be found. |
| `camera` | char\[X\] | The camera that took this image (X is 7 for "90prime", 6 for "mosaic" and 5 for "decam"). |
| `expnum` | int64 | Exposure number, _e.g._ 348224. |
| `plver` | char\[8\] | Community Pipeline (CP) version number. |
| `procdate` | char\[19\] | CP processing date. |
| `plprocid` | char\[7\] | Unique, time-based, CP processing hash - see the [plprocid page](https://www.legacysurvey.org/plprocid) for how to convert this to a date. |
| `ccdname` | char\[X\] | CCD name, _e.g._ "N10", "S7" for DECam (X is 4 for 90prime and mosaic CCDs, and 3 for decam). |
| `object` | char\[35\] | Name listed in the object tag from the CCD header. |
| `propid` | char\[10\] | Proposal ID of the program that took this image, eg "2014B-0404". |
| `filter` | char\[1\] | Filter used for observation, _e.g._ "gg", "rr", "ii", "zz". |
| `exptime` | float32 | Exposure time in seconds, _e.g._ 30. |
| `mjd_obs` | float64 | Date of observation in MJD (in UTC system), _e.g._ 56884.99373389. |
| `airmass` | float32 | Airmass of observation (measured at the telescope bore-sight). |
| `fwhm` | float32 | FWHM (in pixels) measured by the CP. |
| `width` | int16 | Width in pixels of this image, _e.g._ 2046. |
| `height` | int16 | Height in pixels of this image, _e.g._ 4094. |
| `ra_bore` | float64 | Telescope boresight RA of this exposure (deg). |
| `dec_bore` | float64 | Telescope boresight Dec of this exposure (deg). |
| `crpix1` | float32 | Astrometric header value: X reference pixel. |
| `crpix2` | float32 | Astrometric header value: Y reference pixel. |
| `crval1` | float64 | Astrometric header value: RA of reference pixel. |
| `crval2` | float64 | Astrometric header value: Dec of reference pixel. |
| `cd1_1` | float32 | Astrometric header value: transformation matrix. |
| `cd1_2` | float32 | Astrometric header value: transformation matrix. |
| `cd2_1` | float32 | Astrometric header value: transformation matrix. |
| `cd2_2` | float32 | Astrometric header value: transformation matrix. |
| `yshift` | boolean | (ignore; it's always `False`). |
| `ra` | float64 | Approximate RA center of this CCD (deg). |
| `dec` | float64 | Approximate Dec center of this CCD (deg). |
| `skyrms` | float32 | Sky rms for the entire image (in counts/second). |
| `sig1` | float32 | Median per-pixel error standard deviation, in nanomaggies. |
| `ccdzpt` | float32 | Zeropoint for the CCD (AB mag). |
| `zpt` | float32 | Median zero point for the entire image (median of all CCDs of the image), _e.g._ 25.0927. |
| `ccdraoff` | float32 | Median astrometric offset for the CCD <GAIA-Legacy Survey> in arcsec. |
| `ccddecoff` | float32 | Median astrometric offset for the CCD <GAIA-Legacy Survey> in arcsec. |
| `ccdskycounts` | float32 | Mean sky counts level per pixel (AVSKY divided by EXPTIME) in the CP-processed frames measured (with iterative rejection) for each CCD in the image section \[500:1500,1500:2500\]. DECam exposure data is in electrons. Mosaic and 90prime are in electrons/sec. Sky counts are normalized to maintain a mean level from the original gain-corrected ADU. |
| `ccdskysb` | float32 | Surface brightness (mag/arcsec²) for the sky background. |
| `ccdrarms` | float32 | rms in astrometric offset for the CCD <Gaia-Legacy Survey> in arcsec. |
| `ccddecrms` | float32 | rms in astrometric offset for the CCD <Gaia-Legacy Survey> in arcsec. |
| `ccdphrms` | float32 | Photometric rms for the CCD (in mag). |
| `phrms` | float32 | Median photometric rms across all CCDs in the image (in mag). |
| `ccdnastrom` | int16 | Number of stars (after sigma-clipping) used to compute astrometric correction. |
| `ccdnphotom` | int16 | Number of Gaia+PS1 stars detected with signal-to-noise ratio greater than five. |
| `ccd_cuts` | int64 | Bit mask describing CCD image quality (see the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks)). |
| `v4plus` | boolean | `True` if the Community Pipeline (CP) version number (`plver`, above) is >= 4.0.0. |

### [survey-ccds-decam-dr10.kd.fits](https://www.legacysurvey.org/dr10/files/\#toc-entry-8)

As for the **survey-ccds-decam-dr10.fits.gz** file but limited by the depth of each observation. This file
contains the CCDs actually used for the DR10 reductions. Columns are the same as for the **survey-ccds-decam-dr10.fits.gz** file.

### [ccds-annotated-decam-dr10.fits.gz](https://www.legacysurvey.org/dr10/files/\#toc-entry-9)

A version of the **survey-ccds-decam-dr10.fits.gz** file with additional information
gathered during calibration pre-processing before running the Tractor reductions.

Includes all of the columns in the **survey-ccds-decam-dr10.fits.gz** file plus the columns
listed below.

| Column | Type | Description |
| --- | --- | --- |
| `annotated` | boolean | `True` unless there is an error when computing the "annotated" quantities in this row of the file |
| `good_region` | int16\[4\] | If only a subset of the CCD images was used, this array of x0,x1,y0,y1 values gives the coordinates that were used, \[x0,x1), \[y0,y1). -1 for no cut (most CCDs) |\
| `ra0` | float64 | RA coordinate of pixel (1,1)...Note that the [ordering of the CCD corners is detailed here](https://www.legacysurvey.org/ccdordering) |\
| `dec0` | float64 | Dec coordinate of pixel (1,1) |\
| `ra1` | float64 | RA coordinate of pixel (1,H) |\
| `dec1` | float64 | Dec coordinate of pixel (1,H) |\
| `ra2` | float64 | RA coordinate of pixel (W,H) |\
| `dec2` | float64 | Dec coordinate of pixel (W,H) |\
| `ra3` | float64 | RA coordinate of pixel (W,1) |\
| `dec3` | float64 | Dec coordinate of pixel (W,1) |\
| `dra` | float32 | Maximum distance from RA,Dec center to the edge midpoints, in RA |\
| `ddec` | float32 | Maximum distance from RA,Dec center to the edge midpoints, in Dec |\
| `ra_center` | float64 | RA coordinate of CCD center |\
| `dec_center` | float64 | Dec coordinate of CCD center |\
| `meansky` | float32 | Our (Tractor) pipeline (not the CP) estimate of the sky level, average over the image, in nanomaggies |\
| `stdsky` | float32 | Standard deviation of our sky level, in nanomaggies |\
| `maxsky` | float32 | Max of our sky level, in nanomaggies |\
| `minsky` | float32 | Min of our sky level, in nanomaggies |\
| `pixscale_mean` | float32 | Pixel scale (via sqrt of area of a 10x10 pixel patch evaluated in a 5x5 grid across the image), in arcsec/pixel. |\
| `pixscale_std` | float32 | Standard deviation of pixel scale |\
| `pixscale_max` | float32 | Max of pixel scale |\
| `pixscale_min` | float32 | Min of pixel scale |\
| `psfnorm_mean` | float32 | PSF norm = 1/sqrt of N\_eff = sqrt(sum(psf\_i²)) for normalized PSF pixels i; mean of the PSF model evaluated on a 5x5 grid of points across the image. Point-source detection standard deviation is `sig1 / psfnorm`. |\
| `psfnorm_std` | float32 | Standard deviation of PSF norm |\
| `galnorm_mean` | float32 | Norm of the PSF model convolved by a 0.45" exponential galaxy. |\
| `galnorm_std` | float32 | Standard deviation of galaxy norm. |\
| `psf_mx2` | float32 | PSF model second moment in x (pixels²) |\
| `psf_my2` | float32 | PSF model second moment in y (pixels²) |\
| `psf_mxy` | float32 | PSF model second moment in x-y (pixels²) |\
| `psf_a` | float32 | PSF model major axis (pixels) |\
| `psf_b` | float32 | PSF model minor axis (pixels) |\
| `psf_theta` | float32 | PSF position angle (deg) |\
| `psf_ell` | float32 | PSF ellipticity 1 - minor/major |\
| `humidity` | float32 | Percent humidity outside |\
| `outtemp` | float32 | Outside temperate (degrees C). |\
| `tileid` | int32 | tile number, 0 for data from programs other than [MzLS](https://www.legacysurvey.org/mzls) or [DECaLS](https://www.legacysurvey.org/decamls) |\
| `tilepass` | uint8 | tile pass number, 1, 2 or 3, if this was an [MzLS](https://www.legacysurvey.org/mzls) or [DECaLS](https://www.legacysurvey.org/decamls) observation, or 0 for data from other programs. Set by the observers (the meaning of `tilepass` is on the [status page](https://www.legacysurvey.org/status)) |\
| `tileebv` | float32 | Mean [SFD98](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract) E(B-V) extinction in the tile, 0 for data from programs other than [BASS](https://www.legacysurvey.org/bass), [MzLS](https://www.legacysurvey.org/mzls) or [DECaLS](https://www.legacysurvey.org/decamls) |\
| `ebv` | float32 | [SFD98](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract) E(B-V) extinction for CCD center |\
| `decam_extinction` | float32\[6\] | Extinction for optical filters ugrizYugrizY |\
| `wise_extinction` | float32\[4\] | Extinction for WISE bands W1,W2,W3,W4 |\
| `psfdepth` | float32 | 5-sigma PSF detection depth in AB mag, using PsfEx PSF model |\
| `galdepth` | float32 | 5-sigma galaxy (0.45" round exp) detection depth in AB mag |\
| `gausspsfdepth` | float32 | 5-sigma PSF detection depth in AB mag, using Gaussian PSF approximation (using `seeing` value) |\
| `gaussgaldepth` | float32 | 5-sigma galaxy detection depth in AB mag, using Gaussian PSF approximation |\
\
### [south/dr10-south-depth.fits.gz](https://www.legacysurvey.org/dr10/files/\#toc-entry-10)\
\
A concatenation of the depth histograms for each brick, from the\
`coadd/*/*/*-depth.fits` tables. HDU1 contains histograms that describe the\
number of pixels in each brick with a 5-sigma AB depth in the given magnitude\
bin. HDU2 contains the bin edges of the histograms.\
\
- HDU1\
\
\
| Column | Type | Description |\
| --- | --- | --- |\
| `counts_ptsrc_g` | int32\[50\] | Histogram of pixels for point source depth in gg band |\
| `counts_gal_g` | int32\[50\] | Histogram of pixels for canonical galaxy depth in gg band |\
| `counts_ptsrc_r` | int32\[50\] | Histogram of pixels for point source depth in rr band |\
| `counts_gal_r` | int32\[50\] | Histogram of pixels for canonical galaxy depth in rr band |\
| `counts_ptsrc_i` | int32\[50\] | Histogram of pixels for point source depth in ii band |\
| `counts_gal_i` | int32\[50\] | Histogram of pixels for canonical galaxy depth in ii band |\
| `counts_ptsrc_z` | int32\[50\] | Histogram of pixels for point source depth in zz band |\
| `counts_gal_z` | int32\[50\] | Histogram of pixels for canonical galaxy depth in zz band |\
| `brickname` | char\[8\] | Name of the brick |\
\
- HDU2\
\
\
| Column | Type | Description |\
| --- | --- | --- |\
| `depthlo` | float32 | Lower bin edge for each histogram in HDU1 (5-sigma AB depth) |\
| `depthhi` | float32 | Upper bin edge for each histogram in HDU1 (5-sigma AB depth) |\
\
### [south/dr10-south-depth-summary.fits.gz](https://www.legacysurvey.org/dr10/files/\#toc-entry-11)\
\
A summary of the depth histogram for DR10. FITS table with the following columns:\
\
| Column | Type | Description |\
| --- | --- | --- |\
| `depthlo` | float32 | Lower limit of the depth bin |\
| `depthhi` | float32 | Upper limit of the depth bin |\
| `counts_ptsrc_g` | int64 | Number of pixels in histogram for point source depth in gg band |\
| `counts_gal_g` | int64 | Number of pixels in histogram for canonical galaxy depth in gg band |\
| `counts_ptsrc_r` | int64 | Number of pixels in histogram for point source depth in rr band |\
| `counts_gal_r` | int64 | Number of pixels in histogram for canonical galaxy depth in rr band |\
| `counts_ptsrc_i` | int64 | Number of pixels in histogram for point source depth in ii band |\
| `counts_gal_i` | int64 | Number of pixels in histogram for canonical galaxy depth in ii band |\
| `counts_ptsrc_z` | int64 | Number of pixels in histogram for point source depth in zz band |\
| `counts_gal_z` | int64 | Number of pixels in histogram for canonical galaxy depth in zz band |\
\
The depth histogram runs from magnitude of 20.1 to 24.9 in steps of\
0.1 mag. The first and last bins are "catch-all" bins: 0 to 20.1 and\
24.9 to 100, respectively. The histograms count the number of pixels\
in each brick's unique area with the given depth. These numbers can\
be turned into values in square degrees using the brick pixel area of\
0.262 arcseconds square. These depth estimates take into account the\
small-scale masking (cosmic rays, edges, saturated pixels) and\
detailed PSF model.\
\
## [Random Catalogs (`randoms/*`)](https://www.legacysurvey.org/dr10/files/\#toc-entry-12)\
\
### [randoms-1-\*.fits](https://www.legacysurvey.org/dr10/files/\#toc-entry-13)\
\
Twenty files of random points sampled across the CCDs that comprise the geometry of DR10 (see [Myers et al. 2023](https://ui.adsabs.harvard.edu/abs/2023AJ....165...50M/abstract)). Random locations\
were generated across the footprint at a density of 2,500 per square degree and meta-information\
about the survey was extracted from pixels at each random location from files in the `coadd` directory (see below, e.g.\
`coadd/*/*/*-depth-<filter>.fits.fz`, `coadd/*/*/*-galdepth-<filter>.fits.fz`,\
`coadd/*/*/*-nexp-<filter>.fits.fz`, `coadd/*/*/*-maskbits.fits.fz`,\
`coadd/*/*/*-invvar-<filter>.fits.fz`). The order of the points within each file is also random\
(meaning that randomness is retained if just the first N rows of the file are read). Each file contains the following columns:\
\
| Column | Type | Description |\
| --- | --- | --- |\
| `RELEASE` | int16 | Integer denoting the camera and filter set used, which will be unique for a given processing run of the data ( [RELEASE is documented here](https://www.legacysurvey.org/release)) |\
| `BRICKID` | int32 | A unique Brick ID (in the range \[1, 662174\]) |\
| `BRICKNAME` | char\[8\] | Name of the brick |\
| `BRICK_OBJID` | int32 | Random catalog object number enumerated by increasing `RA` within each brick; a unique identifier hash is `RELEASE,BRICKID,BRICK_OBJID` |\
| `RA` | float64 | Right ascension at equinox J2000 |\
| `DEC` | float64 | Declination at equinox J2000 |\
| `NOBS_G` | int16 | Number of images that contribute to the central pixel in the gg filter for this location (not profile-weighted) |\
| `NOBS_R` | int16 | Number of images that contribute to the central pixel in the rr filter for this location (not profile-weighted) |\
| `NOBS_I` | int16 | Number of images that contribute to the central pixel in the ii filter for this location (not profile-weighted) |\
| `NOBS_Z` | int16 | Number of images that contribute to the central pixel in the zz filter for this location (not profile-weighted) |\
| `PSFDEPTH_G` | float32 | For a 5σ5σ point source detection limit in gg, 5/(√PSFDEPTH\_G)5/(PSFDEPTH\_G) gives flux in nanomaggies and −2.5\[log10(5/(√PSFDEPTH\_G))−9\]−2.5\[log10⁡(5/(PSFDEPTH\_G))−9\] gives corresponding magnitude |\
| `PSFDEPTH_R` | float32 | For a 5σ5σ point source detection limit in rr, 5/(√PSFDEPTH\_R)5/(PSFDEPTH\_R) gives flux in nanomaggies and −2.5\[log10(5/(√PSFDEPTH\_R))−9\]−2.5\[log10⁡(5/(PSFDEPTH\_R))−9\] gives corresponding magnitude |\
| `PSFDEPTH_I` | float32 | For a 5σ5σ point source detection limit in ii, 5/(√PSFDEPTH\_I)5/(PSFDEPTH\_I) gives flux in nanomaggies and −2.5\[log10(5/(√PSFDEPTH\_I))−9\]−2.5\[log10⁡(5/(PSFDEPTH\_I))−9\] gives corresponding magnitude |\
| `PSFDEPTH_Z` | float32 | For a 5σ5σ point source detection limit in zz, 5/(√PSFDEPTH\_Z)5/(PSFDEPTH\_Z) gives flux in nanomaggies and −2.5\[log10(5/(√PSFDEPTH\_Z))−9\]−2.5\[log10⁡(5/(PSFDEPTH\_Z))−9\] gives corresponding magnitude |\
| `GALDEPTH_G` | float32 | As for `PSFDEPTH_G` but for a galaxy (0.45" exp, round) detection sensitivity |\
| `GALDEPTH_R` | float32 | As for `PSFDEPTH_R` but for a galaxy (0.45" exp, round) detection sensitivity |\
| `GALDEPTH_I` | float32 | As for `PSFDEPTH_I` but for a galaxy (0.45" exp, round) detection sensitivity |\
| `GALDEPTH_Z` | float32 | As for `PSFDEPTH_Z` but for a galaxy (0.45" exp, round) detection sensitivity |\
| `PSFDEPTH_W1` | float32 | As for `PSFDEPTH_G` (and also on the AB system) but for WISE W1 |\
| `PSFDEPTH_W2` | float32 | As for `PSFDEPTH_G` (and also on the AB system) but for WISE W2 |\
| `PSFSIZE_G` | float32 | Weighted average PSF FWHM in arcsec in the gg band |\
| `PSFSIZE_R` | float32 | Weighted average PSF FWHM in arcsec in the rr band |\
| `PSFSIZE_I` | float32 | Weighted average PSF FWHM in arcsec in the ii band |\
| `PSFSIZE_Z` | float32 | Weighted average PSF FWHM in arcsec in the zz band |\
| `APFLUX_G` | float32 | Total flux in nanomaggies extracted in a 0.75 arcsec radius in the gg band at this location |\
| `APFLUX_R` | float32 | Total flux in nanomaggies extracted in a 0.75 arcsec radius in the rr band at this location |\
| `APFLUX_I` | float32 | Total flux in nanomaggies extracted in a 0.75 arcsec radius in the ii band at this location |\
| `APFLUX_Z` | float32 | Total flux in nanomaggies extracted in a 0.75 arcsec radius in the zz band at this location |\
| `APFLUX_IVAR_G` | float32 | Inverse variance of `APFLUX_G` |\
| `APFLUX_IVAR_R` | float32 | Inverse variance of `APFLUX_R` |\
| `APFLUX_IVAR_I` | float32 | Inverse variance of `APFLUX_I` |\
| `APFLUX_IVAR_Z` | float32 | Inverse variance of `APFLUX_Z` |\
| `MASKBITS` | int32 | Bitwise mask for optical data in the `coadd/*/*/*maskbits*` maps (see the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks)) |\
| `WISEMASK_W1` | uint8 | Bitwise mask for WISE W1 data in the `coadd/*/*/*maskbits*` maps (see the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks)) |\
| `WISEMASK_W2` | uint8 | Bitwise mask for WISE W2 data in the `coadd/*/*/*maskbits*` maps (see the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks)) |\
| `EBV` | float32 | Galactic extinction E(B-V) reddening from [SFD98](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract) |\
| `PHOTSYS` | char\[1\] | 'N' for an [MzLS](https://www.legacysurvey.org/mzls)/ [BASS](https://www.legacysurvey.org/bass) location, 'S' for a [DECaLS](https://www.legacysurvey.org/decamls) (or DECam) location |\
| `HPXPIXEL` | int64 | [HEALPixel](https://healpy.readthedocs.io/en/latest/) containing this location at NSIDE=64 in the NESTED scheme |\
| `TARGETID` | int64 | See the [DESI data model](https://desidatamodel.readthedocs.io/en/latest/DESI_SURVEYOPS/mtl/main/dark/mtl-dark-hp-HPX.html) (added to facilitate running randoms through the [DESI fiberassign code](https://github.com/desihub/fiberassign)) |\
| `DESI_TARGET` | int64 | See the [DESI data model](https://desidatamodel.readthedocs.io/en/latest/DESI_SURVEYOPS/mtl/main/dark/mtl-dark-hp-HPX.html); set to 4, appropriate to a QSO, the highest-priority DESI dark-time target (added to facilitate running randoms through the [DESI fiberassign code](https://github.com/desihub/fiberassign)) |\
| `BGS_TARGET` | int64 | See the [DESI data model](https://desidatamodel.readthedocs.io/en/latest/DESI_SURVEYOPS/mtl/main/dark/mtl-dark-hp-HPX.html); set to zero (added to facilitate running randoms through the [DESI fiberassign code](https://github.com/desihub/fiberassign)) |\
| `MWS_TARGET` | int64 | See the [DESI data model](https://desidatamodel.readthedocs.io/en/latest/DESI_SURVEYOPS/mtl/main/dark/mtl-dark-hp-HPX.html); set to zero (added to facilitate running randoms through the [DESI fiberassign code](https://github.com/desihub/fiberassign)) |\
| `SUBPRIORITY` | int64 | See the [DESI data model](https://desidatamodel.readthedocs.io/en/latest/DESI_SURVEYOPS/mtl/main/dark/mtl-dark-hp-HPX.html) (added to facilitate running randoms through the [DESI fiberassign code](https://github.com/desihub/fiberassign)) |\
| `OBSCONDITIONS` | int32 | See the [DESI data model](https://desidatamodel.readthedocs.io/en/latest/DESI_SURVEYOPS/mtl/main/dark/mtl-dark-hp-HPX.html); set to 1023, which corresponds to all possible observing conditions (added to facilitate running randoms through the [DESI fiberassign code](https://github.com/desihub/fiberassign)) |\

[... middle omitted — see footer ...]

| `gaia_astrometric_excess_noise` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) astrometric excess noise |\
| `gaia_astrometric_excess_noise_sig` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) astrometric excess noise uncertainty |\
| `gaia_duplicated_source` | boolean |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) duplicated source flag |\
| `gaia_phot_bp_rp_excess_factor` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) BP/RP excess factor |\
| `gaia_astrometric_sigma5d_max` | float32 | mas | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) longest semi-major axis of the 5-d error ellipsoid |\
| `gaia_astrometric_params_solved` | uint8 |  | Which astrometric parameters were estimated for a [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) source |\
| `gaia_ipd_frac_multi_peak` | int8 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) percent of successful windows from the Image Parameters Determination code with more than one peak |\
| `gaia_ipd_gof_harmonic_amplitude` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) amplitude of the Image Parameters Determination code goodness-of-fit versus the position angle of a scan |\
| `gaia_ruwe` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) renormalized unit weight error |\
\
## [Image Stacks (`south/coadd/*`)](https://www.legacysurvey.org/dr10/files/\#toc-entry-34)\
\
Image stacks are on tangent-plane (WCS TAN) projections, 3600 × 3600 pixels, at 0.262 arcseconds per pixel.\
\
- <AAA>/<brick>/legacysurvey-<brick>-blobmodel-<filter>.fits.fz\
\
The Tractor's model prediction of the images, similar to `<AAA>/<brick>/legacysurvey-<brick>-model-<filter>.fits.fz`, below,\
except that the models are clipped to the blobs within which they are measured. In other words, the models used to derive the\
maps in these files are not extrapolated beyond the pixels in the blobs that are used to fit the models.\
\
- <AAA>/<brick>/legacysurvey-<brick>-ccds.fits\
\
FITS binary table with the list of CCD images that were used in this brick.\
Contains the same columns as **survey-ccds-decam-dr10.fits.gz**, and also contains\
the additional columns listed below.\
\
\
\
\
| Column | Type | Description |\
| --- | --- | --- |\
| `ccd_x0` | int16 | Minimum x image coordinate overlapping this brick |\
| `ccd_y0` | int16 | Minimum y image coordinate overlapping this brick |\
| `ccd_x1` | int16 | Maximum x image coordinate overlapping this brick |\
| `ccd_y1` | int16 | Maximum y image coordinate overlapping this brick |\
| `brick_x0` | int16 | Minimum x brick image coordinate overlapped by this image |\
| `brick_x1` | int16 | Maximum x brick image coordinate overlapped by this image |\
| `brick_y0` | int16 | Minimum y brick image coordinate overlapped by this image |\
| `brick_y1` | int16 | Maximum y brick image coordinate overlapped by this image |\
| `psfnorm` | float32 | Same as `psfnorm` in the _ccds-annotated-_ file |\
| `galnorm` | float32 | Same as `galnorm` in the _ccds-annotated-_ file |\
| `skyver` | char\[8\] | Git version of the sky calibration code |\
| `psfver` | char\[21\] | Git version of the PSF calibration code |\
| `skyplver` | char\[7\] | Community Pipeline (CP) version of the input to sky calibration |\
| `psfplver` | char\[7\] | CP version of the input to PSF calibration |\
| `co_sky` | float32 |  |\
\
\
- <AAA>/<brick>/legacysurvey-<brick>-chi2-<filter>.fits.fz\
\
Stacked χ² image, which is approximately the summed χ² values from the single-epoch images.\
\
- <AAA>/<brick>/legacysurvey-<brick>-depth-<filter>.fits.fz\
\
Stacked depth map in units of the point-source flux inverse-variance at each pixel.\
\
\
\
  - The 5σ point-source depth can be computed as 5/(√depth\_ivar)5/(depth\_ivar) .\
\
\
- <AAA>/<brick>/legacysurvey-<brick>-galdepth-<filter>.fits.fz\
\
Stacked depth map in units of the canonical galaxy flux inverse-variance at each pixel.\
The canonical galaxy is an exponential profile with effective radius 0.45" and round shape.\
\
\
\
  - The 5σ galaxy depth can be computed as 5/(√galdepth\_ivar)5/(galdepth\_ivar) .\
\
\
- <AAA>/<brick>/legacysurvey-<brick>-image-<filter>.fits.fz\
\
Stacked image centered on a brick location covering 0.25° × 0.25°. The primary HDU contains the coadded image (inverse-variance weighted coadd), in\
units of nanomaggies per pixel.\
\
\
\
  - NOTE: These are not the images used by Tractor, which operates on the\
    single-epoch images.\
\
  - NOTE: These images are resampled using Lanczos-3 resampling.\
\
  - NOTE: Images in WISE bands are on the Vega system, all other flux-related quantities\
    in DR10 are reported on the AB system. The [description](https://www.legacysurvey.org/dr10/description/#photometry) page lists\
    the Vega-to-AB conversions [recommended by the WISE team](http://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html#conv2ab).\
\
\
- <AAA>/<brick>/legacysurvey-<brick>-invvar-<filter>.fits.fz\
\
Inverse variance image corresponding to the legacysurvey-<brick>-image-<filter>.fits.fz file based on the sum of the\
inverse-variances of the individual input images in units of 1/(nanomaggies)² per pixel.\
\
\
\
  - NOTE: These are not the inverse variance maps used by Tractor, which operates\
    on the single-epoch images.\
\
  - NOTE: Images in WISE bands are on the Vega system, all other flux-related quantities\
    in DR10 are reported on the AB system. The [description](https://www.legacysurvey.org/dr10/description/#photometry) page lists\
    the Vega-to-AB conversions [recommended by the WISE team](http://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html#conv2ab).\
\
\
- <AAA>/<brick>/legacysurvey-<brick>-maskbits.fits.fz\
\
Bitmask of possible problems with pixels in this brick.\
\
\
\
  - HDU1: The optical bitmasks, corresponding to `MASKBITS` on the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks).\
\
  - HDU2: The WISE W1 bitmasks, corresponding to `WISEMASK_W1` on the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks).\
\
  - HDU3: The WISE W2 bitmasks, corresponding to `WISEMASK_W2` on the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks).\
\
\
- <AAA>/<brick>/legacysurvey-<brick>-model-<filter>.fits.fz\
\
Stacked model image centered on a brick location covering 0.25° × 0.25°.\
\
\
\
  - The Tractor's idea of what the coadded images should look like; the Tractor's model prediction.\
\
  - NOTE: Images in WISE bands are on the Vega system, all other flux-related quantities\
    in DR10 are reported on the AB system. The [description](https://www.legacysurvey.org/dr10/description/#photometry) page lists\
    the Vega-to-AB conversions [recommended by the WISE team](http://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html#conv2ab).\
\
\
- <AAA>/<brick>/legacysurvey-<brick>-nexp-<filter>.fits.fz\
\
Number of good (unmasked) exposures contributing to each pixel of the stacked images.\
\
- <AAA>/<brick>/legacysurvey-<brick>-psfsize-<filter>.fits.fz\
\
[Weighted average PSF FWHM](https://github.com/legacysurvey/legacypipe/blob/ddb05a39b739917d0b03b0cdfd5afccf907a0c7f/py/legacypipe/coadds.py#L466) in arcsec at each pixel of the stacked images.\
\
- <AAA>/<brick>/legacysurvey-<brick>-blobmodel.jpg\
\
JPEG image of the Tractor's model images, where the model fits have been clipped to\
the blobs within which the models are measured. Uses the g,r,i,zg,r,i,z filters as the colors.\
\
- <AAA>/<brick>/legacysurvey-<brick>-image.jpg\
\
JPEG image of the calibrated image using the g,r,i,zg,r,i,z filters as the colors.\
\
- <AAA>/<brick>/legacysurvey-<brick>-model.jpg\
\
JPEG image of the Tractor's model image using the g,r,i,zg,r,i,z filters as the colors.\
\
- <AAA>/<brick>/legacysurvey-<brick>-resid.jpg\
\
JPEG image of the residual image (data minus model) using the g,r,i,zg,r,i,z filters as\
the colors.\
\
- <AAA>/<brick>/legacysurvey-<brick>-wise.jpg\
\
JPEG image of the calibrated image using the WISE filters as the colors.\
\
- <AAA>/<brick>/legacysurvey-<brick>-wisemodel.jpg\
\
JPEG image of the model image using the WISE filters as the colors.\
\
- <AAA>/<brick>/legacysurvey-<brick>-wiseresid.jpg\
\
JPEG image of the residual image (data minus model) using the WISE filters as the colors.\
\
\
## [Other Files](https://www.legacysurvey.org/dr10/files/\#toc-entry-35)\
\
Much additional information is available as part of the [DESI](https://desi.lbl.gov/) Legacy Imaging Surveys Data Releases, including, in separate directories,\
statistics of the Tractor fits (`south/metrics`),\
code outputs from the fitting processes (`south/logs`) and additional files\
detailing the calibrations (`calib`).\
We don't expect that most users will need a description of these files, but [contact](https://www.legacysurvey.org/contact) us if you require more information.\
\
## [Raw Data](https://www.legacysurvey.org/dr10/files/\#toc-entry-36)\
\
See the [raw data page](https://www.legacysurvey.org/rawdata).\
\
**Footnotes**

──────── [TRUNCATED] ────────
Showing 29,726 chars (head) + 9,841 chars (tail) of 92,373 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/www.legacysurvey.org-78ea6c3bf2.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/www.legacysurvey.org-78ea6c3bf2.md" offset=357 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
