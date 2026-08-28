URL: https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/randomN_DRX_SAMPLE_NS.html

# Data model: randomsN\_DR12vX\_SAMPLE\_NS

**General description:**
This file contains the Large Scale Structure random points,
(roughly 50 times the number of points in the respective
galaxy\_DR12vX\_SAMPLE\_NS file).

**Naming convention:**
randomN-DRXvY-SAMPLE-NS.fits.gz -
N enumerates the random catalog version (1 or 2 in DR10, 0 or 1 in DR11/DR12),
DRXvY (vY is the internal version
number, used by the galaxy clustering working group) is the data
release, SAMPLE is the corresponding galaxy catalog sample, NS is one of (North,South),
N in randomN format is used if there are more than one set of randoms per catalog.

In DR12 sample classes LOWZE2, LOWZE3, CMASSLOWZ, CMASSLOWZE2, CMASSLOWZE3, and
CMASSLOWZTOT were added. LOWZE2 and LOWZE3 correspond to early targeting
algorithms for LOWZ-like galaxies. We also generate sample catalogs that
combine CMASS and LOWZ, LOWZE2, or LOWZE3 into a single sample. CMASSLOWZTOT
combines CMASSLOWZE2, CMASSLOWZE3, and CMASSLOWZ catalogs, using each only in
the region where they were targeted.

By default catalogs containing LOWZE2 or LOWZE3 selection also include chunks 7 and
higher, even though targeting was the final LOWZ algorithm for those higher chunks.
File names are appended with '\_trimmed' if the catalog has been trimmed to its original
target footprint (chunk 2 for LOWZE2, chunks 3 through 6 for LOWZE3).

**Approximate size:**
100-2000 Mbytes

**File type:**
FITS

**Written by products:**
Galaxy clustering working group large scale structure DR12vX code
(mksample).

**Required header keywords:**

- **COMMENT** (string): description of area and which
   acceptance mask file goes with this file.

**Required column names:**

- **ra** (float64): Right Ascension
- **dec** (float64): Declination
- **z** (float32): redshift obtained by randomly drawing from the observed galaxy redshifts.
- **zindx** (int32): Only available in DR12. Index in galaxy\_DRX\_SAMPLE\_NS.fits.gz of galaxy from which random redshift was obtained..
- **ipoly** (int32): Index of the containing polygon in corresponding DRXvY mask file.
- **isect** (int32): ID of the containing sector in corresponding DRXvY mask file.
- **weight\_fkp** (float32): FKP weight. w\_fkp as defined in Eq.
   17 of Anderson et al. 2012. Note the fiducial cosmology and choice of P0 are not uniform across data releases.
- **nz** (float32): Comoving number density for the object's redshift using the fiducial cosmology. Note that the fiducial cosmology is different in DR11 and DR12.
- **psf\_fwhm\[5\]** (float32): Only available in DR12. Derived at the imaging field level rather than the object-by-object level; see the [window\_flist](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/datamodel/files/PHOTO_RESOLVE/window_flist.html) description.
- **sky\_flux\[5\]** (float32): Only available in DR12. Derived at the imaging field level rather than the object-by-object level; see the [window\_flist](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/datamodel/files/PHOTO_RESOLVE/window_flist.html) description.
- **airmass** (float32): Only available in DR12. Derived at the imaging field level rather than the object-by-object level, based on ra, dec, and tai; see the [window\_flist](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/datamodel/files/PHOTO_RESOLVE/window_flist.html) description.
- **image\_depth\[5\]** (float32): Only available in DR12. Derived from psf\_fwhm, skyflux, and airmass according to [Padmanabhan et al.](http://adsabs.harvard.edu/abs/2008ApJ...674.1217P)
- **eb\_minus\_v** (float32): Only available in DR12. Reddening value from [Schlegel, Finkbeiner, and Davis](http://adsabs.harvard.edu/abs/1998ApJ...500..525S)
.
