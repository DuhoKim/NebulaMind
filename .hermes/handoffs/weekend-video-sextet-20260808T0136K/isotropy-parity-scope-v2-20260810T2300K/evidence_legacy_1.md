URL: https://www.legacysurvey.org/dr10/description

[Skip to main content](https://www.legacysurvey.org/dr10/description/#content)

The DESI Legacy Surveys team is producing an inference model of the extragalactic sky in the optical and
infrared. The original Legacy Surveys ( [MzLS](https://www.legacysurvey.org/mzls), [DECaLS](https://www.legacysurvey.org/decamls) and [BASS](https://www.legacysurvey.org/bass)) conducted dedicated observations
of ~14,000 square degrees of extragalactic sky visible from the northern hemisphere in three optical bands
(g,r,z), which was augmented with four infrared bands from [NEOWISE](https://wise2.ipac.caltech.edu/docs/release/neowise/).
To achieve this goal, the Legacy Surveys completed
three imaging projects on different telescopes, described in more depth at the following links:

- _The Beijing-Arizona Sky Survey_ ( [BASS](https://www.legacysurvey.org/bass))

- _The DECam Legacy Survey_ ( [DECaLS](https://www.legacysurvey.org/decamls))

- _The Mayall z-band Legacy Survey_ ( [MzLS](https://www.legacysurvey.org/mzls))


As of DR10, the Legacy Surveys inference model is being self-consistently expanded to > 20,000 square
degrees by incorporating additional DECam data from NOIRLab that includes extra optical bands (g,r,i,z):

- _Additional Public Data from NOIRLab_ ( [NOIRLab Astro Data Archive](https://noirlab.edu/public/projects/astrodataarchive/))


An overview of the Legacy Surveys is available in [Dey et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019AJ....157..168D/abstract).

## [Contents of DR10](https://www.legacysurvey.org/dr10/description/\#toc-entry-1)

Data Release 10 (DR10) is the tenth public data release of the Legacy Surveys. The dedicated observations that
comprised [DECaLS](https://www.legacysurvey.org/decamls), [BASS](https://www.legacysurvey.org/bass) and [MzLS](https://www.legacysurvey.org/mzls) are now complete. In DR10, we focus, instead, on incorporating
new imaging from DECam into the "southern" (Declination ≤ 32.375°) Legacy Surveys footprint; continuing to extend the footprint while also providing
a consistent inference model of imaging over much of the sky. Notably, DR10 of the Legacy Surveys provides
i-band observations for the first time. Imaging from the Legacy Surveys is
reduced through the [NOIRLab Community Pipeline](https://legacy.noirlab.edu/noao/staff/fvaldes/CPDocPrelim/PL201_3.html) before being processed using the [Legacypipe](https://github.com/legacysurvey/legacypipe) pipeline. DR10 also
includes [WISE](http://wise.ssl.berkeley.edu/) fluxes from all imaging through [year 7 of NEOWISE-Reactivation](https://wise2.ipac.caltech.edu/docs/release/neowise/neowise_2021_release_intro.html)
force-photometered in the [unWISE](https://ui.adsabs.harvard.edu/abs/2018RNAAS...2a...1M/abstract) maps at the locations of Legacy Surveys optical sources.

DR10 includes images from [DECaLS](https://www.legacysurvey.org/decamls) g,r,z-band observations ( [survey program 2014B-0404](https://noirlab.edu/science/observing-noirlab/approved-survey-programs)) observed between
9th August 2014 and 7th March 2019. DR10 also includes g,r,i,z-band DECam observations from a range of
non-DECaLS surveys, including observations that were conducted between 8th January 2013 and 30th August 2021. The bulk
of these additional DECam observations are from the [Dark Energy Survey](https://www.darkenergysurvey.org/) (including the full six years of the survey);
the [DELVE Survey](https://delve-survey.github.io/), and the [DeROSITA Survey](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera/DeROSITAS).
Information on the exact observations included in DR10 can be derived from
the Legacy Surveys [survey-ccds-\* files](https://www.legacysurvey.org/dr10/files/#survey-ccds-decam-dr10-fits-gz). To obtain northern observations from [BASS](https://www.legacysurvey.org/bass) and [MzLS](https://www.legacysurvey.org/mzls), see [DR9](https://www.legacysurvey.org/dr9) of the Legacy Surveys.

The table below indicates the area covered in DR10 for different numbers of passes and in different filters. These estimates
are derived from the geometry of the CCDs that contribute to the Legacy Surveys footprint, using the [random catalogs](https://www.legacysurvey.org/dr10/files/#random-catalogs-randoms) at a density of 50,000 deg-2.

| Band/Number of Passes | ≥ 1 | ≥ 2 | ≥ 3 |
| --- | --- | --- | --- |
| g-band | 21,619 deg2 | 20,241 deg2 | 17,290 deg2 |
| r-band | 20,135 deg2 | 19,108 deg2 | 16,576 deg2 |
| i-band | 17,732 deg2 | 15,862 deg2 | 13,024 deg2 |
| z-band | 20,810 deg2 | 19,548 deg2 | 16,762 deg2 |
| All bands jointly | 15,342 deg2 | 13,281 deg2 | 9,923 deg2 |

Past data releases have strictly defined the northern and southern portions of the Legacy Surveys to prevent double-counting of area
in regions covered by multiple surveys. Typically, the Legacy Surveys has defined locations at Dec ≥ 32.375° and
that are north of the Galactic Plane as "northern" for [BASS](https://www.legacysurvey.org/bass)/ [MzLS](https://www.legacysurvey.org/mzls) imaging and locations at Dec < 32.375° or that are
south of the Galactic Plane as "southern" for DECam imaging. Under this stricter definition of what constitues "southern" area, DR10 covers:

| Band/Number of Passes | ≥ 1 | ≥ 2 | ≥ 3 |
| --- | --- | --- | --- |
| g-band | 21,375 deg2 | 20,030 deg2 | 17,143 deg2 |
| r-band | 19,885 deg2 | 18,898 deg2 | 16,435 deg2 |
| i-band | 17,732 deg2 | 15,862 deg2 | 13,024 deg2 |
| z-band | 20,562 deg2 | 19,332 deg2 | 16,594 deg2 |
| All bands jointly | 15,342 deg2 | 13,281 deg2 | 9,923 deg2 |

DR10 includes a variety of pixel-level and catalog-level products, which are described in more
detail on the [files](https://www.legacysurvey.org/dr10/files) page.
The size of the DR10 data distribution is:

| Size\* | Directory | Description |
| --- | --- | --- |
| 1.5 TB | [calib/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/calib/) | Calibration files |
| 8.0 GB | [masking/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/masking/) | Files containing [external catalogs used for masking](https://www.legacysurvey.org/dr10/external/#external-catalogs-used-for-masking) |
| 676 GB | [randoms/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/randoms/) | Catalogs of random points _only_ in the official "southern" region of DR10 |
| 60 TB | [south/coadd/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/) | Coadded images ( [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd)) |
| 21 GB | [south/external/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/external/) | [Matches to other catalogs](https://www.legacysurvey.org/dr10/files/#external-match-files-south-external) (SDSS, etc.) |
| 56 GB | [south/logs/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/logs/) | Log files generated by [Tractor](https://github.com/dstndstn/tractor) processing |
| 4.9 TB | [south/metrics/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/metrics/) | Metrics and statisics of Tractor fits |
| 371 GB | [south/randoms/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/randoms/) | Catalogs of random points throughout all regions of DR10 |
| 6.4 TB | [south/sweep/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/sweep/) | Subsets of the Tractor [catalogs](https://www.legacysurvey.org/dr10/catalogs) and row-by-row matched products |
| 6.6 TB | [south/tractor/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/tractor/) | The Tractor [catalogs](https://www.legacysurvey.org/dr10/catalogs) |
| 6.6 TB | [south/tractor-i/](https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/tractor-i/) | Expanded versions of the Tractor [catalogs](https://www.legacysurvey.org/dr10/catalogs) |

\*Note that although the _contents_ of a directory should be fixed for each Data Release, the _size_ of a directory can change. This is typically due to updated file compression. So, the listed directory sizes should be viewed as (very reasonable) estimates.

For all of the DESI Legacy Imaging Surveys, coadded images and
Tractor catalogs are presented in "bricks" of approximate
size 0.25° × 0.25°. Each brick is defined in terms of a box in RA,Dec
coordinates. The [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd) use a simple tangent-plane (WCS TAN)
projection around the brick center. The projections for the g,r,i,z filters are identical, with
a pixel scale of 0.262″/pix. The projections for the four WISE filters are also identical
but with a pixel scale of 2.75″/pix.
There are 662,174 bricks spread over the sky, meaning that each brick has an average
area of 0.0623 deg2. The brick images have some overlap.

There are approximately 2.8 billion unique sources in DR10 spread over 366,898 unique bricks.

## [Obtaining Images and Raw Data](https://www.legacysurvey.org/dr10/description/\#toc-entry-2)

Images for the Legacy Surveys can be viewed directly using [the Sky viewer](https://www.legacysurvey.org/viewer)
and raw data can be obtained through [the NOIRLab portal](https://astroarchive.noirlab.edu/portal/search/#/search-form) (see also the information near
[the bottom of the files](https://www.legacysurvey.org/dr10/files/#raw-data) page). Note that the weight map images (the `oow` files) that can be retrieved either from the viewer or
portal are in the same units as 1/skyrms2 in the [survey-ccds-decam-dr10.fits.gz files](https://www.legacysurvey.org/dr10/files/#survey-ccds-decam-dr10-fits-gz).

Sections of the Legacy Surveys for DR10 can be obtained as JPEGs or FITS files using
the cutout service, for example, as follows:

JPEG: [https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10&pixscale=0.262](https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10&pixscale=0.262)

FITS: [https://www.legacysurvey.org/viewer/fits-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10&pixscale=0.262&bands=griz](https://www.legacysurvey.org/viewer/fits-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10&pixscale=0.262&bands=griz)

This will merge the northern (MzLS+BASS) and southern (DECam) images at a line corresponding to Dec=32.375°.

DR10 includes images in the (i) band, so it uses a different color mapping for JPEG images in the DECam footprint.
(The DR9-north footprint still uses the (g,r,z) color mapping.) To use only the (g,r,z) bands used in previous
data releases for the DECam data, you can set layer=ls-dr10-grz.

To request images from only the northern or southern surveys, specify dr9-north or dr10-south, for example:

JPEG ( [DECaLS](https://www.legacysurvey.org/decamls)): [https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10-south&pixscale=0.262](https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10-south&pixscale=0.262)

FITS ( [DECaLS](https://www.legacysurvey.org/decamls)): [https://www.legacysurvey.org/viewer/fits-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10-south&pixscale=0.262&bands=grz](https://www.legacysurvey.org/viewer/fits-cutout?ra=190.1086&dec=1.2005&layer=ls-dr10-south&pixscale=0.262&bands=grz)

JPEG ( [BASS](https://www.legacysurvey.org/bass)/ [MzLS](https://www.legacysurvey.org/mzls)): [https://www.legacysurvey.org/viewer/jpeg-cutout?ra=154.7709&dec=46.4537&layer=ls-dr9-north&pixscale=0.262](https://www.legacysurvey.org/viewer/jpeg-cutout?ra=154.7709&dec=46.4537&layer=ls-dr9-north&pixscale=0.262)

FITS ( [BASS](https://www.legacysurvey.org/bass)/ [MzLS](https://www.legacysurvey.org/mzls)): [https://www.legacysurvey.org/viewer/fits-cutout?ra=154.7709&dec=46.4537&layer=ls-dr9-north&pixscale=0.262&bands=grz](https://www.legacysurvey.org/viewer/fits-cutout?ra=154.7709&dec=46.4537&layer=ls-dr9-north&pixscale=0.262&bands=grz)

where "bands" is a string such as "griz","gz","g", etc.

Replacing layer=ls-dr10 (or, e.g., layer=ls-dr9-north) with layer=ls-dr10-model (layer=ls-dr9-north-model)
or layer=ls-dr10-resid (layer=ls-dr9-north-resid) will instead return cutouts for the model and residual images, respectively.

The size of the image can also be specified using width, height and size,
where size forces width and height to be equal. For example:

[https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&width=100&layer=ls-dr10&pixscale=0.262](https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&width=100&layer=ls-dr10&pixscale=0.262)

[https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&height=100&layer=ls-dr10&pixscale=0.262](https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&height=100&layer=ls-dr10&pixscale=0.262)

[https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&size=100&layer=ls-dr10&pixscale=0.262](https://www.legacysurvey.org/viewer/jpeg-cutout?ra=190.1086&dec=1.2005&size=100&layer=ls-dr10&pixscale=0.262)

It is possible to retrieve multiple cutouts from the command line using standard utilites such as [wget](https://www.gnu.org/software/wget/manual/wget.html#Overview).

The maximum size for cutouts (in number of pixels) is currently 512.
Pixscale=0.262 will return (approximately) the native pixels used by the [Tractor](https://github.com/dstndstn/tractor).

More examples are available on the [list of URL/cutout patterns that are supported by the viewer](https://www.legacysurvey.org/viewer/urls).

## [Source Detection](https://www.legacysurvey.org/dr10/description/\#toc-entry-3)

The source detection uses a PSF- and SED-matched-filter detection on
the stacked images, with a 6σ detection limit.
The [Tractor](https://github.com/dstndstn/tractor) fitting step is initialized with these positions, although
these positions can be changed during the fits and
low-S/N sources can be removed.

For source detection, each image is convolved by its PSF model,
then a weighted stack
of these is created in order to optimize the point-source detection
efficiency. Next, SED-matched combinations of the three bands are
created, for two SEDs: "flat" (a source with AB color zero), and
"red", a source with AB color g−r=1, r−z=1. Sources above 6σ
are detected in each of these two SED-matched filters, as well as independently in each band.

The locations of the peak fluxes of extracted sources are used to determine where objects
are photometered and how the initial parameters for an object are seeded. When a source is detected
in multiple bands a choice of filter must be made to seed the initial extraction.
Sources detected in other bands beyond the initial filter are only kept if they are
sufficiently separated from an object that was extracted in previous bands.
In [DR4](https://www.legacysurvey.org/dr4), [DR3](https://www.legacysurvey.org/dr3) and earlier data releases,
source detection was run first in g, then in r, z, "flat"
and finally in "red".
Starting with [DR5](https://www.legacysurvey.org/dr5), source detection
was run first in z, then in r, g, "flat"
and finally in "red". z was chosen as the "primary" detection image
to take advantage of the better PSF in that band. DR10 follows the convention of running
source detection in the redder bands first, i.e. in the order
z, i, r, g, "flat" and finally "red".

Starting with [DR7](https://www.legacysurvey.org/dr7) the criteria for deciding whether a
flux peak is a distinct source were relaxed. The minimum possible distance between
neighboring peaks was reduced from 6 pixels (about 1.5 arcseconds) to 4 pixels (about 1 arcsecond).
In addition, the "saddle" depth (dip in flux) necessary to model neighboring peaks as
distinct sources was reduced.

Starting with [DR8](https://www.legacysurvey.org/dr8), many different "foreground" objects are extracted as independent sources
in a similar fashion to how [Gaia stars were extracted in DR7](https://www.legacysurvey.org/dr7/description/#source-detection).
These include bright stars, medium-bright stars, globular clusters and [SGA (Siena Galaxy Atlas)](https://www.legacysurvey.org/sga/sga2020) large galaxies
(as detailed on the [external catalogs page](https://www.legacysurvey.org/dr10/external)). The foreground objects consist of pre-defined
geometrical masks (which are elliptical for galaxies) that are
fixed at their expected positions in the Legacy Surveys images after accounting for proper motion
and parallax in Gaia.
The reasoning behind treating bright foreground sources as special cases is that many of them
have large halos or include diffuse light that is not present in the Tractor model choices. This leads such sources
to be typically best-fit by misleading (and computationally expensive) diffuse galaxy models.

Sources that lie inside the boundary of a foreground object have `MASKBITS`
set (see the [bitmasks page](https://www.legacysurvey.org/dr10/bitmasks)). Within the mask regions for bright stars (`BRIGHT`), globular clusters (`CLUSTER`)
and [SGA](https://www.legacysurvey.org/sga/sga2020) large galaxies (`GALAXY`), sources are forced to be `TYPE=PSF`
(except for the [SGA](https://www.legacysurvey.org/sga/sga2020) large galaxies themselves). Note that sources are _not_ forced to be `TYPE=PSF` in the region of _medium_-bright stars
(i.e. if [MEDIUM is set but BRIGHT, CLUSTER, and GALAXY are not](https://www.legacysurvey.org/dr10/bitmasks)).
Mask regions are ignored in the Tractor local-sky-fitting calibration code and are superseded by fits within the mask regions themselves.
Within `BRIGHT`, `MEDIUM` and `GALAXY` mask regions (except for the [SGA](https://www.legacysurvey.org/sga/sga2020) large galaxies themselves), a per-source background sky level is fit in the mask blob for each exposure.

Starting with [DR9](https://www.legacysurvey.org/dr9), objects that appear in the [Gaia catalogs](https://www.legacysurvey.org/dr10/external) are always retained in the [Tractor catalogs](https://www.legacysurvey.org/dr10/catalogs), even if they would normally be cut by the
model-selection criteria used to detect sources. This is because Gaia sources are often so bright that they saturate in Legacy Surveys imaging.
Since such "retained" Gaia sources have no model fits, their `flux_g`, `flux_r`, `flux_i` and `flux_z` values are estimated in the [catalogs](https://www.legacysurvey.org/dr10/catalogs),
using [polynomial fits to Gaia-to-DECam](https://github.com/legacysurvey/legacypipe/blob/DR10.0.12/py/legacypipe/reference.py#L237-L267) color transformations for stars.
Transformations to [DECam](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera) are always used (i.e. even in areas of the Legacy Surveys footprint that are only covered by [BASS](https://www.legacysurvey.org/bass) and [MzLS](https://www.legacysurvey.org/mzls)).
The `flux_ivar_[griz]` values for these "retained" Gaia sources are set to zero.

## [PSF](https://www.legacysurvey.org/dr10/description/\#toc-entry-4)

The Tractor makes use of the PSF on each individual exposure. The PSF for
the individual exposures are first computed independently for each CCD
using [PSFEx](http://www.astromatic.net/software/psfex), generating spatially varying pixelized models. Note that it is possible that
`survey-*` and `*-annotated-*` [files](https://www.legacysurvey.org/dr10/files) could record information
that is missing from other files in cases where [PSFEx](http://www.astromatic.net/software/psfex) fails. This is [expected behavior](https://github.com/legacysurvey/legacypipe/issues/349).

Starting with [DR9](https://www.legacysurvey.org/dr9), a [modified, extended PSF model](https://www.legacysurvey.org/dr10/psf) is used to subtract the extended wings of bright stars from DECam images.

The configuration files for SExtractor and [PSFEx](http://www.astromatic.net/software/psfex) that were used for a given
iteration of the Legacy Surveys `legacypipe` codebase are available [on our GitHub page](https://github.com/legacysurvey/legacypipe/tree/main/py/legacypipe/config).

## [Sky Level](https://www.legacysurvey.org/dr10/description/\#toc-entry-5)

The Community Pipeline removes a sky level that includes a sky pattern, an illumination correction,
and a single, scaled fringe pattern. These steps are described on the [NOIRLab Community Pipeline](https://legacy.noirlab.edu/noao/staff/fvaldes/CPDocPrelim/PL201_3.html)
page.
These corrections are intended to make the sky level in the processed images near zero, and to remove most pattern artifacts.
A constant sky level, that is the mean of what was removed, is then added back to the image.

Additionally, a spatially varying (spline) sky model is computed and removed, by detecting and masking sources, then computing medians in
sliding 512-pixel boxes. The [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd) provided on the [files](https://www.legacysurvey.org/dr10/files) page have this sky level
removed. As noted under [Source Detection](https://www.legacysurvey.org/dr10/description/#source-detection), above, any regions (blobs) covered by foreground sources
are specially treated.

Changes in the Community Pipeline after [DR8](https://www.legacysurvey.org/dr8) (in particular the switch to using star flats from
the [Dark Energy Survey](https://www.darkenergysurvey.org/) instead of dark sky flats) created
residual sky patterns in DECam images. These patterns are expected to exist in all optical bands
with the z-band having the worst residuals. So, starting
with [DR9](https://www.legacysurvey.org/dr9), the Legacy Surveys [corrects DECam images to account for these residual sky patterns](https://www.legacysurvey.org/dr10/sky).

In addition, starting with [DR9](https://www.legacysurvey.org/dr9), a new set of fringe templates was created for DECam z-band
images, with associated per-exposure fringe scale factors. These
[fringe templates and scale factors](https://www.legacysurvey.org/dr10/fringe) replace the fringe correction applied by the Community Pipeline for
DECam imaging in the z-band.

## [Tractor Catalogs](https://www.legacysurvey.org/dr10/description/\#toc-entry-6)

The Tractor code runs within the geometrical region
of a brick to produce [catalogs](https://www.legacysurvey.org/dr10/catalogs) of extracted sources. This fitting is performed on the individual exposures
that overlap the brick, without making use of image stacks (such as the [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd) detailed on the
[files](https://www.legacysurvey.org/dr10/files) page).
This preserves the full information content of the data set in the fits,
handles masked pixels without the need for uncertain interpolation techniques,
and fits to data points without the complication of pixel covariances.

## [Morphological Classification](https://www.legacysurvey.org/dr10/description/\#toc-entry-7)

The [Tractor](https://github.com/dstndstn/tractor) fitting can allow any of the source properties or
image calibration parameters (such as the PSF) to float.
Only the source properties were allowed to float in DR10.
These are continuous properties for the object centers, fluxes,
and the shape parameters.

There is also the discrete choice of which
model type to use. In DR10, six morphological types are used. Five of these
are used in the [Tractor](https://github.com/dstndstn/tractor) fitting procedure: point sources ("PSF"),
round exponential galaxies with a variable radius ("REX"), deVaucouleurs ("DEV") profiles
(elliptical galaxies), exponential ("EXP") profiles (spiral galaxies), and Sersic ("SER") profiles.
The sixth morphological type is "DUP," which is set for Gaia sources that are coincident with, and so have been fit by, an extended source.
No optical flux is assigned to "DUP" sources, but they are retained to ensure that all Gaia sources appear in the catalogs even if
[Tractor](https://github.com/dstndstn/tractor) preferred and fit a different source based on the deeper Legacy Surveys imaging.
The total numbers of the different morphological types in DR10 are:

| Primary Objects of Type | Unique Sources |
| --- | --- |
| _All_ | 2,827,055,986 |
| `PSF` | 1,346,165,723 |
| `REX` | 1,122,579,568 |
| `EXP` | 225,321,618 |
| `DEV` | 83,968,261 |
| `SER` | 48,729,700 |
| `DUP` | 291,116 |

_Primary_ objects, here, specifically refers to sources for which `BRICK_PRIMARY==True`
(the totals are derived from the _total number_ counts in the [survey bricks summary file](https://www.legacysurvey.org/dr10/files/#south-survey-bricks-dr10-south-fits-gz)).
See [DR9](https://www.legacysurvey.org/dr9) for source counts in the northern footprint of the Legacy Surveys.

The decision to retain an object in the catalog and to re-classify it using
models more complicated than a point source is made using the penalized
changes to χ² in the image after subtracting the models for other sources.
Here, the χ² value is calculated as a sum across all optical bands
(i.e. g, r, i and z for DR10).
The "PSF" and "REX" models are computed for every source and the better of these
two is used when deciding whether to keep the source. A source is retained if its
penalized χ² is improved by 25; this corresponds to a χ²
difference of 27 (because of the penalty of 2 for the source centroid). Sources
below this threshold are removed.

The source is classified as the better of "point source (PSF)" or "round exponential
galaxy (REX)" unless the penalized χ² is improved by 9 (i.e.,
approximately a 3σ improvement) by treating it as a deVaucouleurs or
exponential profile. The classification becomes a Sersic profile
if it is both a better fit to a single profile over the point source, and
improves the penalized χ² by another 9. These choices implicitly mean
that any extended source classifications have to be at least 5.8σ detections
and that Sersic profiles must be at least 6.5σ detections.

The fluxes are not constrained to be positive-valued. This allows the fitting of
very low signal-to-noise sources without introducing biases at the faint end. It
also allows the stacking of fluxes at the catalog level.

## [Tractor Implementation Details](https://www.legacysurvey.org/dr10/description/\#toc-entry-8)

Tractor fundamentally treats the fitting as a χ² minimization
problem. The current core routine uses the sparse least squares
solver from the [SciPy](https://www.scipy.org/) package, or the open source
[Ceres solver](http://ceres-solver.org/), originally developed by Google.

The galaxy profiles (the exponential and deVaucouleurs profiles mentioned above
under [Morphological Classification](https://www.legacysurvey.org/dr10/description/#morphological-classification)) are approximated with [mixture-of-Gaussians](https://arxiv.org/abs/1210.6563)
(MoG) models and are convolved by the pixelized PSF models using a new
Fourier-space method ( [Lang 2020](https://ui.adsabs.harvard.edu/abs/2020arXiv201215797L/abstract)).
The galaxy profile approximation introduces errors in these
models typically at the level of 10−4 or smaller.
The PSF models are treated as pixel-convolved quantities,
and are evaluated at the integral pixel coordinates without integrating
any functions over the pixels.

The Tractor algorithm could be run with both the source parameters
and the calibration parameters allowed to float, at the cost of
more compute time and the necessity to use much larger blobs because
of the non-locality of the calibrations. A more practical approach
would be to iterate between fitting source parameters in brick space,
and fitting calibration parameters in exposure space.

## [Photometry](https://www.legacysurvey.org/dr10/description/\#toc-entry-9)

The flux calibration for [BASS](https://www.legacysurvey.org/bass), [MzLS](https://www.legacysurvey.org/mzls) and [DECaLS](https://www.legacysurvey.org/decamls) are on the AB natural system of the
[90Prime](https://soweb.as.arizona.edu/~tscopewiki/doku.php?id=90prime_info), [Mosaic-3](https://noirlab.edu/science/programs/kpno/retired-instruments/mosaic) and [DECam](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera) instruments, respectively.
An AB system reports the same flux in any band for a source whose spectrum is
constant in units of erg/s/cm²/Hz. A source with a spectrum of
f=10−(48.6+22.5)/2.5 erg/s/cm²/Hz
would be reported to have an integrated flux of 1 nanomaggie in any filter.
The natural system implies that no color terms have been applied to any of the photometry, meaning
that fluxes are reported as observed in the [90Prime](https://soweb.as.arizona.edu/~tscopewiki/doku.php?id=90prime_info), [Mosaic-3](https://noirlab.edu/science/programs/kpno/retired-instruments/mosaic) and [DECam](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera) filter systems.

Zero point magnitudes for the Community Pipeline reductions of the [90Prime](https://soweb.as.arizona.edu/~tscopewiki/doku.php?id=90prime_info), [Mosaic-3](https://noirlab.edu/science/programs/kpno/retired-instruments/mosaic) and [DECam](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera) images
were computed by comparing Legacy Survey PSF photometry to
[Pan-STARRS1 (PS1) PSF photometry](https://ui.adsabs.harvard.edu/abs/2016ApJ...822...66F/abstract), where the latter was modified with color terms
to place the PS1 photometry on the [90Prime](https://soweb.as.arizona.edu/~tscopewiki/doku.php?id=90prime_info), [Mosaic-3](https://noirlab.edu/science/programs/kpno/retired-instruments/mosaic) or [DECam](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera) system. The same color terms
are applied to all CCDs.
Zero points are computed separately for each CCD, but not for each amplifier.

[... middle omitted — see footer ...]

fluxes should be very close to a normal distribution. The fluxes can be negative for faint
objects, and indeed we expect many such cases for the faintest objects.

The filter curves are available for [BASS g-band](https://www.legacysurvey.org/files/bass-g.txt), [BASS r-band](https://www.legacysurvey.org/files/bass-r.txt), [MzLS z-band](https://www.legacysurvey.org/files/kpzd.txt), [MzLS z-band with corrections](https://www.legacysurvey.org/files/kpzdccdcorr3.txt),
[DECam g-band](https://www.legacysurvey.org/files/decam.g.am1p4.dat.txt), [DECam r-band](https://www.legacysurvey.org/files/decam.r.am1p4.dat.txt), [DECam i-band](https://www.legacysurvey.org/files/decam.i.am1p4.dat.txt) and [DECam z-band](https://www.legacysurvey.org/files/decam.z.am1p4.dat.txt). The curves "with corrections" include terms to correct for
the telescope, corrector, camera and atmosphere.

Starting with [DR6](https://www.legacysurvey.org/dr6), PSF photometry uses the same PSF models
(and sky background subtraction) for zeropoint-fitting as is later used in cataloging.
So, for DR10 the measured fluxes for PS1 stars should be completely self-consistent.

The WISE Level 1 images and the [unWISE](https://ui.adsabs.harvard.edu/abs/2018RNAAS...2a...1M/abstract) image stacks are on a Vega system.
We have converted these to an AB system using the [recommended conversions by the WISE team](http://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html#conv2ab). Namely,
FluxAB=FluxVega×10−(Δm/2.5)
where Δm = 2.699, 3.339, 5.174, and 6.620 mag in the W1, W2, W3 and W4 bands.
For example, a WISE W1 image should be multiplied by 10−2.699/2.5=0.083253 to
give units consistent with the Tractor catalogs. These conversion factors are recorded in the
Tractor catalog headers ("WISEAB1", etc). The result is that the optical and WISE fluxes
we provide should all be within a few percent of being on an AB system.

## [Galactic Extinction](https://www.legacysurvey.org/dr10/description/\#toc-entry-10)

The most recent values of the Galactic extinction coefficients are available on the [catalogs page](https://www.legacysurvey.org/dr10/catalogs/#galactic-extinction-coefficients).

## [Astrometry](https://www.legacysurvey.org/dr10/description/\#toc-entry-11)

Starting with [DR8](https://www.legacysurvey.org/dr8), astrometry is tied entirely to [Gaia Data Release 2](https://gaia.esac.esa.int/documentation/GDR2/index.html). Each image is calibrated to
[Gaia Data Release 2](https://gaia.esac.esa.int/documentation/GDR2/index.html), yielding an astrometric solution that is offset by the average difference between
the position of Gaia stars at an epoch of 2015.0 and the epoch of the DR10 image. Source
extraction is then fixed to the [Gaia Data Release 2](https://gaia.esac.esa.int/documentation/GDR2/index.html) system, such that positions of sources are tied to
predicted Gaia positions at the epoch of the corresponding Legacy Surveys observation.
Astrometric residuals are typically smaller than ±0.03″.

Astrometric calibration of all optical Legacy Surveys data is conducted using Gaia
astrometric positions of stars matched to Pan-STARRS1 (PS1).
The same matched objects are used for both astrometric and photometric calibration.
The [actual external PS1](https://www.legacysurvey.org/dr10/external/#pan-starrs-1-ps1) and [Gaia DR2](https://www.legacysurvey.org/dr10/external/#gaia-dr2) catalogs we used are available at NERSC.

## [Image Stacks](https://www.legacysurvey.org/dr10/description/\#toc-entry-12)

The image stacks (that are detailed on the [files](https://www.legacysurvey.org/dr10/files) page) are provided for convenience, but were not used in the [Tractor](https://github.com/dstndstn/tractor) fits.
These images overlap adjacent images by approximately 130 pixels in each direction.
These are tangent projections centered at each brick center, North up, with dimensions of 3600 × 3600
and a scale of 0.262″/pix for the g,r,i,z data and 2.75″/pix for the WISE data.
The image stacks are computed using Lanczos-3
interpolation. They have not been designed for "precision" work, although they should be
sufficient for many use cases.

## [Depths](https://www.legacysurvey.org/dr10/description/\#toc-entry-13)

The histograms below depict the median 5σ point source (AB) depths for areas with
different numbers of DECam observations in DR10:

![../../files/depth-hist-g-dr10-south.png](https://www.legacysurvey.org/files/depth-hist-g-dr10-south.png)![../../files/depth-hist-r-dr10-south.png](https://www.legacysurvey.org/files/depth-hist-r-dr10-south.png)![../../files/depth-hist-i-dr10-south.png](https://www.legacysurvey.org/files/depth-hist-i-dr10-south.png)![DR10 Depth Histograms](https://www.legacysurvey.org/files/depth-hist-z-dr10-south.png)

These can be compared to similar plots for the northern Legacy Surveys ( [BASS](https://www.legacysurvey.org/bass) and [MzLS](https://www.legacysurvey.org/mzls))
from [DR9](https://www.legacysurvey.org/dr9):

![../../files/depth-hist-g-dr9-north.png](https://www.legacysurvey.org/files/depth-hist-g-dr9-north.png)![../../files/depth-hist-r-dr9-north.png](https://www.legacysurvey.org/files/depth-hist-r-dr9-north.png)![../../files/depth-hist-z-dr9-north.png](https://www.legacysurvey.org/files/depth-hist-z-dr9-north.png)

These plots are based upon the formal errors in the Tractor catalogs for point sources. The
predicted proposed Legacy Surveys depths for 2 observations at 1.5″ seeing were
g=24.7, r=23.9, z=23.0.

## [Code Versions](https://www.legacysurvey.org/dr10/description/\#toc-entry-14)

- [LegacyPipe](https://github.com/legacysurvey/legacypipe): A range of versions; DR10.0.0, DR10.0.1, DR10.0.2, DR10.0.3, DR10.0.4, DR10.0.5, DR10.0.10 and DR10.0.12. The version used is documented in the Tractor header card `LEGPIPEV`.

- [Astrometry.net](https://github.com/dstndstn/astrometry.net): 0.90-8-g575ad17b

- [Tractor](https://github.com/dstndstn/tractor): dr10.1

- [NOIRLab Community Pipeline](https://legacy.noirlab.edu/noao/staff/fvaldes/CPDocPrelim/PL201_3.html): A mixture of versions; recorded in the [survey-ccds-\* files](https://www.legacysurvey.org/dr10/files/#survey-ccds-decam-dr10-fits-gz) as `plver`.

- [SourceExtractor](http://www.astromatic.net/software/sextractor): 2.25.3

- [PSFEx](http://www.astromatic.net/software/psfex): 3.23.0

- [Astropy](https://www.astropy.org/): 5.0.4

- [fitsio](https://github.com/esheldon/fitsio): 1.1.6

- [Matplotlib](https://matplotlib.org/): 3.5.2

- [mkl\_fft](https://pypi.org/project/mkl-fft): 1.3.1

- [NumPy](https://numpy.org/): 1.21.2

- [photutils](https://photutils.readthedocs.io/en/stable/index.html): 1.4.0

- [SciPy](https://www.scipy.org/): 1.6.3

- [unwise\_psf](https://github.com/legacysurvey/unwise_psf/blob/master/README): dr10.0


## [Glossary](https://www.legacysurvey.org/dr10/description/\#toc-entry-15)

BASS

[Beijing-Arizona Sky Survey](https://www.legacysurvey.org/bass).

BLISS+

[Blanco Imaging of the Southern Sky Survey](https://arxiv.org/abs/1812.06318).

Blob

Continguous region of pixels above a detection threshold and neighboring
pixels; Tractor is optimized within blobs.

Brick

A region bounded by lines of constant RA and DEC; reductions
are performed within bricks of size approximately 0.25° × 0.25°.

CP

Community Pipeline ( [reduction pipeline operated by NOIRLab](https://legacy.noirlab.edu/noao/staff/fvaldes/CPDocPrelim/PL201_3.html)).

DECaLS

[Dark Energy Camera Legacy Survey](https://www.legacysurvey.org/decamls).

DeROSITAS

[DECam eROSITA Survey](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera/DeROSITAS).

DR3

[DESI Legacy Surveys Imaging Data Release 3](https://www.legacysurvey.org/dr3).

DR4

[DESI Legacy Surveys Imaging Data Release 4](https://www.legacysurvey.org/dr4).

DR5

[DESI Legacy Surveys Imaging Data Release 5](https://www.legacysurvey.org/dr5).

DR6

[DESI Legacy Surveys Imaging Data Release 6](https://www.legacysurvey.org/dr6).

DR7

[DESI Legacy Surveys Imaging Data Release 7](https://www.legacysurvey.org/dr7).

DR8

[DESI Legacy Surveys Imaging Data Release 8](https://www.legacysurvey.org/dr8).

DR9

[DESI Legacy Surveys Imaging Data Release 9](https://www.legacysurvey.org/dr9).

DECam

[Dark Energy Camera](https://noirlab.edu/science/programs/ctio/instruments/Dark-Energy-Camera) on the Blanco 4-meter telescope.

maggie

Linear flux units, where an object with an AB magnitude of 0 has a
flux of 1.0 maggie. A convenient unit is the nanomaggie: a flux of 1 nanomaggie
corresponds to an AB magnitude of 22.5.

MoG

[Mixture-of-Gaussians](https://arxiv.org/abs/1210.6563) to approximate galaxy models.

MzLS

[Mayall z-band Legacy Survey](https://www.legacysurvey.org/mzls).

NOIRLab

[The NSF's National Optical-Infrared Astronomy Research Laboratory](https://www.aura-astronomy.org/centers/nsfs-oir-lab).

nanomaggie

Linear flux units, where an object with an AB magnitude of 22.5 has a flux
of 1×10−9 maggie or 1.0 nanomaggie.

PSF

Point spread function.

PSFEx

[Emmanuel Bertin's PSF fitting code](http://www.astromatic.net/software/psfex).

SDSS

[Sloan Digital Sky Survey](https://www.sdss.org/).

SDSS DR12

[Sloan Digital Sky Survey Data Release 12](https://www.sdss.org/dr12/).

SDSS DR13

[Sloan Digital Sky Survey Data Release 13](https://www.sdss.org/dr13/).

SED

Spectral energy distribution.

SGA

[Siena Galaxy Atlas](https://www.legacysurvey.org/sga/sga2020).

SourceExtractor

[Source Extractor reduction code](http://www.astromatic.net/software/sextractor).

SFD98

[Schlegel, Finkbeiner & Davis 1998 extinction maps](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract).

Tractor

[Dustin Lang's inference code](https://github.com/dstndstn/tractor).

unWISE

[New coadds](https://arxiv.org/abs/1405.0308) of the WISE imaging, [at original full resolution](http://unwise.me/).

WISE

[Wide Infrared Survey Explorer](http://wise.ssl.berkeley.edu/).

**Footnotes**

──────── [TRUNCATED] ────────
Showing 29,719 chars (head) + 9,942 chars (tail) of 41,691 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/www.legacysurvey.org-a8fc1e24e1.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/www.legacysurvey.org-a8fc1e24e1.md" offset=358 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
