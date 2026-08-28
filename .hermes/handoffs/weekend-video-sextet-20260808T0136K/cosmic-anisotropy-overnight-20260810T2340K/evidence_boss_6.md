URL: https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/galaxy_DRX_SAMPLE_NS.html

# Data model: galaxy\_DRX\_SAMPLE\_NS

**General description:**
These files contain the Large Scale Structure galaxy redshift
catalogs, which become available after publication.

**Naming convention:**
galaxy\_DRXvY\_SAMPLE\_NS.fits.gz - DRXvY (vY is the internal version
number, used by the galaxy clustering working group) is the data
release, SAMPLE is either CMASS or LOWZ, NS is one of (North,South).
There is a corresponding mangle mask file mask/mask\_DRXvY\_SAMPLE\_NS.ply/fits to
describe the sky coverage for each sample.

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
15-300 Mbytes

**File type:**
FITS (gzipped)

**Written by products:**
Galaxy clustering working group large scale structure code (mksample).

**Column names:**

- **ra** (float64): Right Ascension
- **dec** (float64): Declination
- **run** (int32): run number (see the
   [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description)
- **rerun** (int32): rerun number (see the
   [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description)
- **camcol** (int32): camera column (see the
   [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description)
- **field** (int32): field number (see the
   [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description)
- **id** (int32): object ID within the field (see the
   [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description)
- **ichunk** (int32): chunk id which tells you the chunk number
   that the object is from. Chunks below 15 were targeted using earlier versions of photometry and/or targeting code.
- **tchunk** (int32): targeting chunk id (for example, chunk 2
   objects are targeted using tchunk=8 (main008) targeting file.
   Deprecated in DR12.
- **ipoly** (int32): Index of the containing polygon in corresponding DRXvY mask file.
- **isect** (int32): ID of the containing sector in corresponding DRXvY mask file.
- **fracpsf\[5\]** (float32): see the
   [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description)
- **expflux\[5\]** (float32): see the [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description.
- **devflux\[5\]** (float32): see the [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description.
- **psfflux\[5\]** (float32): see the [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description.
- **modelflux\[5\]** (float32): see the [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description.
- **fiber2flux\[5\]** (float32): see the [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description.
- **r\_dev\[5\]** (float32): Only available in DR12. see the [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description.
- **extinction\[5\]** (float32): see the [photoObj](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html) description.
- **imatch** (int32): 0: missed galaxies, 1: BOSS redshifts, 2: legacy redshifts, 3: fiber collided galaxies, 4: stars, 5: redshift failures.
- **z** (float32): Z\_NOQSO redshift (see the
   [spZbest description](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/RUN1D/spZbest.html))
- **weight\_fkp** (float32): FKP weight. w\_fkp as defined in Eq.
   17 of Anderson et al. 2012. Note the fiducial cosmology and choice of P0 are not uniform across data releases.
- **weight\_cp** (float32): Close pairs weight. Defined in Section 3.2 of Anderson et al. 2012. Accounts for galaxies not allocated a fiber due to fiber collisions.
- **weight\_noz** (float32): Redshift failure weight. w\_zf as defined in Anderson et al. 2012.
- **weight\_star** (float32): Stellar systematic correction
   weight. w\_sys as defined in Anderson et al. 2012 and Ross et al. 2012.
- **weight\_seeing** (float32): Seeing systematic correction
   weight. w\_seeing as defined in Anderson et al. 2013.
- **weight\_systot** (float32): Total systematic weight.
   weight\_systot = weight\_star\*weight\_seeing
- **nz** (float32): Comoving number density for the object's redshift using the fiducial cosmology. Note that the fiducial cosmology is different in DR11 and DR12.
- **comp** (float32): Sector completeness as defined in Eq. 10 of Anderson et al. 2012.
- **plate** (int32): Plate number (see the
   [spZbest description](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/RUN1D/spZbest.html))
- **mjd** (int32): Modified Julian Date of the observation (see the
   [spZbest description](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/RUN1D/spZbest.html))
- **fiberID** (int32): Fiber number on the plate (see the
   [spZbest description](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/RUN1D/spZbest.html))
- **tile\[3\]** (int32): See the [final-bossN](https://data.sdss.org/datamodel/files/BOSSTILELIST_DIR/outputs/bossN/final-bossN.html) description.
- **spectile** (int32): The tile id for this target that matches the target's entry in the [spAll](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/spAll.html) file.
- **icollided** (int32): See the [final-collated](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/bosstile-final-collated-boss2-boss32.html) description.
- **finaln** (int32): The number of the [final-bossN](https://data.sdss.org/datamodel/files/BOSSTILELIST_DIR/outputs/bossN/final-bossN.html) file from which the target information for this object was taken. Objects with the same (finaln, ingroup) fields share a collision group.
- **ingroup** (int32): See the [final-bossN](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/datamodel/files/BOSSTILELIST_DIR/outputs/bossN/final-bossN.html) description. Objects with the same (finaln, ingroup) fields share a collision group.
- **multgroup** (int32): See the [final-bossN](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/datamodel/files/BOSSTILELIST_DIR/outputs/bossN/final-bossN.html) description.
- **psf\_fwhm\[5\]** (float32): Only available in DR12. Derived at the imaging field level rather than the object-by-object level; see the [window\_flist](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/datamodel/files/PHOTO_RESOLVE/window_flist.html) description. Used to estimate **weight\_seeing**.
- **sky\_flux\[5\]** (float32): Only available in DR12. Derived at the imaging field level rather than the object-by-object level; see the [window\_flist](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/datamodel/files/PHOTO_RESOLVE/window_flist.html) description.
- **airmass** (float32): Only available in DR12. Derived at the imaging field level rather than the object-by-object level, based on ra, dec, and tai; see the [window\_flist](https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/datamodel/files/PHOTO_RESOLVE/window_flist.html) description.
- **image\_depth\[5\]** (float32): Only available in DR12. Derived from psf\_fwhm, skyflux, and airmass according to [Padmanabhan et al.](http://adsabs.harvard.edu/abs/2008ApJ...674.1217P)
- **eb\_minus\_v** (float32): Only available in DR12. Reddening value from [Schlegel, Finkbeiner, and Davis](http://adsabs.harvard.edu/abs/1998ApJ...500..525S)
.
