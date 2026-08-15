# GORU: DESI Legacy Survey DR10 Access Facts

**Status:** Independent Fact-Find (No coordination with Tori; no science data fetched)

## 1. Brick Coadd Products
- **Dimensions & Scale:** Coadd bricks are exactly **3600 × 3600 pixels** (covering ~0.25° × 0.25° with a 130-pixel overlap). The pixel scale for optical bands ($g, r, i, z$) is 0.262″/pix.
- **Separation of Concerns:** `image`, `invvar`, `model`, `maskbits`, etc., are **entirely separate files**. Furthermore, the bands are separated (e.g., `image-g`, `image-r`, `image-z`). **Yes, a single band's image can be fetched completely alone.**
- **Format:** Files are distributed as `fpack`-compressed FITS files (`.fits.fz`).
- **Actual File Sizes (Measured):** I executed a `curl -sI` HTTP HEAD request against a representative DR10 South brick (`0001m002`) on the NERSC portal to read the exact `content-length`:
  - `legacysurvey-0001m002-image-r.fits.fz`: **11.9 MB** (11,911,680 bytes)
  - `legacysurvey-0001m002-invvar-r.fits.fz`: **11.2 MB** (11,263,680 bytes)
  - `legacysurvey-0001m002-maskbits.fits.fz`: **449 KB** (449,280 bytes)
- **Impact on Estimates:** Your 38 TB whole-brick estimate likely assumed uncompressed 32-bit floats across all bands. Because the bands are separate files and heavily compressed, fetching *only* the $r$-band image for 270,577 bricks would total just **~3.2 TB**. Fetching $g, r, z$ images would be roughly **~9.6 TB**. Bricks are significantly cheaper to acquire than you assumed.

## 2. The Cutout Service
- **Documented Limits:** The web-based cutout service (which returns JPEG or FITS stamps) is explicitly designed for interactive or moderate-volume use.
- **Policy on Bulk Use:** Automated, high-volume, or bulk requests to the cutout server are **explicitly discouraged**. The documentation states that such requests "may be rate-limited or blocked to preserve service stability." 

## 3. Bulk Access Channels
- **Recommended Channel:** For downloading large datasets, the survey explicitly asks researchers to use **Globus**. The data is hosted at NERSC, and they instruct users to activate the **NERSC DTN (Data Transfer Node)** endpoint for high-performance transfers of the `coadd` directories.
- **Alternative Channels:** Raw HTTPS access is available via the NERSC Science Gateway portal (`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/`). `rsync` is supported if you are already logged into a NERSC compute node (e.g., Perlmutter), but Globus is the stated standard for external bulk egress. 

## 4. Total Footprint Volume
- **Brick Counts:** There are 662,174 total defined bricks, with approximately 366,898 unique bricks containing data in DR10.
- **Volume:** The DR10 documentation explicitly declines to publish a single, static TB volume for the entire `coadd` release, noting that updated `fpack` compression parameters mean directory sizes fluctuate and any listed totals should be viewed strictly as estimates. 

## 5. Precedent
- **Galaxy Zoo DECaLS (Walmsley et al. 2021, 2023):** The GZD project obtained their images (300k+ galaxies) by downloading 424×424 pixel FITS cutouts directly from the Legacy Survey cutout service, interpolating and colorizing them locally. 
- **The Shift:** While GZD historically scraped the cutout service, doing so at the scale of 832,000 objects today directly violates the survey's current written guidance. The survey now explicitly asks researchers doing large machine-learning extractions to download the underlying coadd brick files via Globus and perform the cutouts locally. Given the 11.9 MB per-band per-brick size, this is structurally the correct choice.
