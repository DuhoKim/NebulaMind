# R-C single blind structural probe receipt — 2026-09-01

## Authorization and content-blind selection

Authorization, verbatim (Duho, 2026-09-01, direction #32): “Authorize a single blind structural probe”.

Rule stated before download: bytewise-lexicographically sort the newline-delimited IDs in the frozen `../_successor_build_20260824/acquire/selected_brickids_cut.txt`; select the first ID; resolve that ID to `brickname` using catalogue naming metadata only; use the first three characters of `brickname` as `<AAA>`. This is content-blind because it uses only a frozen identifier list and identifier/name metadata, never image content, image headers, file size, or science values.

Result:

- Selected brick ID: `100048`
- Resolved brick name: `0489m442`
- AAA prefix: `048`
- Full URL: `https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/048/0489m442/legacysurvey-0489m442-image-r.fits.fz`
- Evidence location: `probe/legacysurvey-0489m442-image-r.fits.fz`

The ID-to-name resolution was a metadata-only TAP result: `100048,0489m442`. Directory HTML and its checksum manifest were read as metadata. Exactly one real brick FITS file was downloaded and opened.

## Transfer and integrity

- Published SHA-256: `7c461a5f4d63547d16b552085584661fe452da50ed6013ac30bed63d6dca3486`
- Computed SHA-256: `7c461a5f4d63547d16b552085584661fe452da50ed6013ac30bed63d6dca3486`
- Integrity result: **MATCH**
- Bytes transferred reported by the HTTP client: `9,290,880`
- Local file size: `9,290,880 bytes`
- HTTP status: `200`

## Format contract

### HDU inventory

| Index | FITS storage type | Astropy logical type/name | Dimensions | BITPIX / logical dtype | Compression |
|---:|---|---|---|---|---|
| 0 | Primary HDU | `PrimaryHDU`, `PRIMARY` | no data axes (`NAXIS=0`, shape `()`) | `BITPIX=16`; no pixel array/dtype | none |
| 1 | Binary-table compressed-image extension | `CompImageHDU`, `COMPRESSED_IMAGE` | logical image `3600 × 3600`; NumPy axis order/shape `(3600, 3600)` | logical `ZBITPIX=-32` / `BITPIX=-32`, IEEE float32 (`>f4` when represented in FITS byte order) | tiled `RICE_ONE`; tiles `100 × 100`; `SUBTRACTIVE_DITHER_2`; block size 32; 4 bytes/pixel before compression |

There are exactly two HDUs. Physically, HDU 1 is a `BINTABLE` with 1,296 rows, 24 bytes per row, three fields (`COMPRESSED_DATA`, `ZSCALE`, `ZZERO`), and a 9,241,078-byte heap (`PCOUNT`). Logically it exposes one 2-D compressed float32 image. The pixel array itself was not fetched or traversed; shape and dtype were established from the HDU structural descriptors.

This image file contains no mask or inverse-variance HDU. The same brick directory listing contains separate companion files named `legacysurvey-0489m442-maskbits.fits.fz` and `legacysurvey-0489m442-invvar-r.fits.fz`; neither companion was downloaded or opened.

### Complete WCS card set (verbatim)

The complete WCS-bearing set present in the logical image header is:

```text
CTYPE1  = 'RA---TAN'           / TANgent plane                                 
CTYPE2  = 'DEC--TAN'           / TANgent plane                                 
CRVAL1  =     48.9168278529981 / Reference RA                                   
CRVAL2  =               -44.25 / Reference Dec                                 
CRPIX1  =               1800.5 / Reference x                                    
CRPIX2  =               1800.5 / Reference y                                    
CD1_1   = -7.27777777777778E-05 / CD matrix                                     
CD1_2   =                   0. / CD matrix                                      
CD2_1   =                   0. / CD matrix                                      
CD2_2   = 7.27777777777778E-05 / CD matrix                                      
EQUINOX =                2000. / WCS epoch                                      
```

No `RADESYS`, `CUNIT1`, `CUNIT2`, `LONPOLE`, `LATPOLE`, SIP, PV, or alternate-WCS cards are present. Axis angular units are therefore supplied by the FITS celestial-WCS convention rather than explicit `CUNITn` cards.

### Units (verbatim)

```text
MAGZERO =                 22.5 / Magnitude zeropoint                            
BUNIT   = 'nanomaggy'          / AB mag = 22.5 - 2.5*log10(nanomaggy)           
```

### Primary header (complete, verbatim)

```text
SIMPLE  =                    T / file does conform to FITS standard             
BITPIX  =                   16 / number of bits per data pixel                  
NAXIS   =                    0 / number of data axes                            
EXTEND  =                    T / FITS dataset may contain extensions            
COMMENT   FITS (Flexible Image Transport System) format is defined in 'Astronomy
COMMENT   and Astrophysics', volume 376, page 359; bibcode: 2001A&A...376..359H 
```

### Compressed-image extension header (complete physical header, verbatim)

Quoting the complete physical extension header ensures every card bearing on layout, compression, geometry, edges, coverage, units, and provenance is retained. Astropy's logical compressed-image view maps `ZBITPIX/ZNAXIS/ZNAXISn` to `BITPIX/NAXIS/NAXISn` and prepends `SIMPLE=T`; all non-compression cards below are preserved in that logical view.

```text
XTENSION= 'BINTABLE'           / binary table extension                         
BITPIX  =                    8 / 8-bit bytes                                    
NAXIS   =                    2 / 2-dimensional binary table                     
NAXIS1  =                   24 / width of table in bytes                        
NAXIS2  =                 1296 / number of rows in table                        
PCOUNT  =              9241078 / size of special data area                     
GCOUNT  =                    1 / one data group (required keyword)              
TFIELDS =                    3 / number of fields in each row                   
TTYPE1  = 'COMPRESSED_DATA'    / label for field   1                            
TFORM1  = '1PB(11480)'         / data format of field: variable length array    
TTYPE2  = 'ZSCALE  '           / label for field   2                            
TFORM2  = '1D      '           / data format of field: 8-byte DOUBLE            
TTYPE3  = 'ZZERO   '           / label for field   3                            
TFORM3  = '1D      '           / data format of field: 8-byte DOUBLE            
ZIMAGE  =                    T / extension contains compressed image            
ZSIMPLE =                    T / file does conform to FITS standard             
ZBITPIX =                  -32 / data type of original image                    
ZNAXIS  =                    2 / dimension of original image                    
ZNAXIS1 =                 3600 / length of original image axis                  
ZNAXIS2 =                 3600 / length of original image axis                  
ZTILE1  =                  100 / size of tiles to be compressed                 
ZTILE2  =                  100 / size of tiles to be compressed                 
ZQUANTIZ= 'SUBTRACTIVE_DITHER_2' / Pixel Quantization Algorithm                 
ZDITHER0=                 2329 / dithering offset when quantizing floats        
ZCMPTYPE= 'RICE_ONE'           / compression algorithm                         
ZNAME1  = 'BLOCKSIZE'          / compression block size                        
ZVAL1   =                   32 / pixels per block                               
ZNAME2  = 'BYTEPIX '           / bytes per pixel (1, 2, 4, or 8)                
ZVAL2   =                    4 / bytes per pixel (1, 2, 4, or 8)                
COMMENT Data product of the DESI Imaging Legacy Surveys                         
COMMENT Full documentation at http://legacysurvey.org                           
LEGPIPEV= 'DR10.0.1'           / legacypipe git version                         
LSDIR   = '/global/cfs/cdirs/cosmo/work/legacysurvey/dr10' / $LEGACY_SURVEY_DIR 
LSDR    = 'DR10    '           / Data release number                            
RUNDATE = '2022-06-29T17:23:35.879826' / runbrick.py run time                   
SURVEY  = 'DECaLS+BASS+MzLS'   / The LegacySurveys                              
SURVEYID= 'DECaLS BASS MzLS'   / Survey names                                   
DRVERSIO=                10000 / LegacySurveys Data Release number              
OBSTYPE = 'object  '           / Observation type                               
PROCTYPE= 'tile    '           / Processing type                                
NODENAME= 'nid004896'          / Machine where script was run                   
HOSTNAME= 'perlmutter'         / NERSC machine where script was run             
JOB_ID  = '2516458 '           / SLURM job id                                   
ARRAY_ID= 'none    '           / SLURM job array id                             
UNWISD1 = '/global/cfs/cdirs/cosmo/data/unwise/neo7/unwise-coadds/fulldepth'    
UNWISD2 = '/global/cfs/cdirs/cosmo/data/unwise/allwise/unwise-coadds/fulldepth' 
UNWISTD = '/global/cfs/cdirs/cosmo/work/wise/outputs/merge/neo7'                
UNWISSKY= '/global/cfs/cdirs/cosmo/data/unwise/neo7/unwise-catalog/mod'         
DEPNAM00= 'astrometry'                                                          
DEPVER00= '0.90-8-g575ad17b'                                                    
DEPNAM01= 'astropy '                                                            
DEPVER01= '5.0.4   '                                                            
DEPNAM02= 'fitsio  '                                                            
DEPVER02= '1.1.6   '                                                            
DEPNAM03= 'matplotlib'                                                          
DEPVER03= '3.5.2   '                                                            
DEPNAM04= 'mkl_fft '                                                            
DEPVER04= '1.3.1   '                                                            
DEPNAM05= 'numpy   '                                                            
DEPVER05= '1.21.2  '                                                            
DEPNAM06= 'photutils'                                                           
DEPVER06= '1.4.0   '                                                            
DEPNAM07= 'scipy   '                                                            
DEPVER07= '1.6.3   '                                                            
DEPNAM08= 'tractor '                                                            
DEPVER08= 'dr10.1  '                                                            
DEPNAM09= 'unwise_psf'                                                          
DEPVER09= 'dr10.0  '                                                            
DEPNAM10= 'LARGEGALAXIES_CAT'                                                   
DEPVER10= '/global/cfs/cdirs/cosmo/staging/largegalaxies/v3.0/SGA-ellipse-v3.0&'
CONTINUE  '.kd.fits'                                                            
DEPNAM11= 'LARGEGALAXIES_VER'                                                   
DEPVER11= 'L3      '                                                            
DEPNAM12= 'LARGEGALAXIES_PREBURN'                                               
DEPVER12=                    T                                                  
DEPNAM13= 'TYCHO2_KD'                                                           
DEPVER13= '/global/cfs/cdirs/cosmo/staging/tycho2'                              
DEPNAM14= 'GAIA_CAT'                                                            
DEPVER14= '/global/cfs/cdirs/cosmo/data/gaia/edr3/healpix'                      
DEPNAM15= 'SKY_TEMPLATE'                                                        
DEPVER15= '/global/cfs/cdirs/cosmo/work/legacysurvey/dr10/calib/sky_pattern'    
DEPNAM16= 'unwise  '                                                            
DEPVER16= '/global/cfs/cdirs/cosmo/data/unwise/neo7/unwise-coadds/fulldepth:/g&'
CONTINUE  'lobal/cfs/cdirs/cosmo/data/unwise/allwise/unwise-coadds/fulldepth'   
DEPNAM17= 'unwise_tr'                                                           
DEPVER17= '/global/cfs/cdirs/cosmo/work/wise/outputs/merge/neo7'                
DEPNAM18= 'unwise_modelsky'                                                     
DEPVER18= '/global/cfs/cdirs/cosmo/data/unwise/neo7/unwise-catalog/mod'         
CMDLINE = '/src/legacypipe/py/legacypipe/runbrick.py --brick 0489m442 --skip -&'
CONTINUE  '-skip-calibs --bands g,r,i,z --rgb-stretch 1.5 --nsatur 2 --survey-&'
CONTINUE  'dir /global/cfs/cdirs/cosmo/work/legacysurvey/dr10 --cache-dir  --o&'
CONTINUE  'utdir /pscratch/sd/j/jsnigula/dr10 --checkpoint /pscratch/sd/j/jsni&'
CONTINUE  'gula/dr10/checkpoints/048/checkpoint-0489m442.pickle --checkpoint-p&'
CONTINUE  'eriod 120 --pickle /pscratch/sd/j/jsnigula/dr10/pickles/048/runbric&'
CONTINUE  'k-%(brick)s-%%(stage)s.pickle --write-stage srcs --write-stage tims&'
CONTINUE  ' --write-stage fitblobs --release 10000 --cache-outliers --threads &'
CONTINUE  '64      '           / runbrick command-line                          
BRICK   = '0489m442'           / LegacySurveys brick RRRr[pm]DDd                
BRICKID =               100048 / LegacySurveys brick id                         
RAMIN   =     48.7427466150871 / Brick RA min (deg)                             
RAMAX   =     49.0909090909091 / Brick RA max (deg)                             
DECMIN  =              -44.375 / Brick Dec min (deg)                            
DECMAX  =              -44.125 / Brick Dec max (deg)                            
RA      = '03:15:40.039'       / Brick center RA (hms)                          
DEC     = '-44:15:00.000'      / Brick center DEC (dms)                         
CENTRA  =     48.9168278529981 / Brick center RA (deg)                          
CENTDEC =               -44.25 / Brick center Dec (deg)                         
CORN1RA =     49.1000682155857 / Brick corner RA (deg)                          
CORN1DEC=    -44.3808169095601 / Brick corner Dec (deg)                         
CORN2RA =     48.7335874904105 / Brick corner RA (deg)                          
CORN2DEC=    -44.3808169095601 / Brick corner Dec (deg)                         
CORN3RA =     48.7344017054984 / Brick corner RA (deg)                          
CORN3DEC=    -44.1188914770497 / Brick corner Dec (deg)                         
CORN4RA =     49.0992540004978 / Brick corner RA (deg)                          
CORN4DEC=    -44.1188914770497 / Brick corner Dec (deg)                         
BRICK_G =                    T / Does band g touch this brick?                  
CAMS_G  = 'decam   '           / Cameras contributing band g                    
BRICK_R =                    T / Does band r touch this brick?                  
CAMS_R  = 'decam   '           / Cameras contributing band r                    
BRICK_I =                    T / Does band i touch this brick?                  
CAMS_I  = 'decam   '           / Cameras contributing band i                    
BRICK_Z =                    T / Does band z touch this brick?                  
CAMS_Z  = 'decam   '           / Cameras contributing band z                    
BANDS   = 'griz    '           / Bands touching this brick                      
NBANDS  =                    4 / Number of bands in this catalog                
BAND0   = 'g       '           / Band name in this catalog                      
BAND1   = 'r       '           / Band name in this catalog                      
BAND2   = 'i       '           / Band name in this catalog                      
BAND3   = 'z       '           / Band name in this catalog                      
VER_TIMS= 'DR10.0.1'                                                            
VER_REFS= 'DR10.0.1'                                                            
VER_OUTL= 'DR10.0.1'                                                            
OUTLIER =                    T                                                  
VER_HALO= 'DR10.0.1'                                                            
VER_SRCS= 'DR10.0.1'                                                            
VER_FITB= 'DR10.0.1'                                                            
GALFRPSF=                    T                                                  
LESSMASK=                    F                                                  
COMMENT DCHISQ array model names                                                
DCHISQ_0= 'PSF     '                                                            
DCHISQ_1= 'REX     '                                                            
DCHISQ_2= 'DEV     '                                                            
DCHISQ_3= 'EXP     '                                                            
DCHISQ_4= 'SER     '                                                            
VER_COAD= 'DR10.0.1'                                                            
CTYPE1  = 'RA---TAN'           / TANgent plane                                 
CTYPE2  = 'DEC--TAN'           / TANgent plane                                 
CRVAL1  =     48.9168278529981 / Reference RA                                   
CRVAL2  =               -44.25 / Reference Dec                                 
CRPIX1  =               1800.5 / Reference x                                    
CRPIX2  =               1800.5 / Reference y                                    
CD1_1   = -7.27777777777778E-05 / CD matrix                                     
CD1_2   =                   0. / CD matrix                                      
CD2_1   =                   0. / CD matrix                                      
CD2_2   = 7.27777777777778E-05 / CD matrix                                      
EQUINOX =                2000. / WCS epoch                                      
OBSERVAT= 'CTIO    '           / Observatory name                               
TELESCOP= 'CTIO 4.0-m telescope' / Telescope  name                              
OBS-LAT =            -30.16606 / Latitude (deg)                                 
OBS-LONG=             70.81489 / Longitude (deg)                                
OBS-ELEV=                2215. / Elevation (m)                                  
INSTRUME= 'DECam   '           / Instrument name                                
FILTER  = 'r DECam SDSS c0002 6415.0 1480.0' / Filter name                      
FILTERX = 'r       '           / Filter short name                              
MJD_MIN =     56629.2538482926 / Earliest MJD in coadd (TAI)                    
MJD_MAX =     58782.1704295507 / Latest MJD in coadd (TAI)                      
MJD_MEAN=     58528.4961694089 / Mean MJD in coadd (TAI)                        
DATEOBS1= '2013-12-03T06:04:57.492' / DATE-OBS for the first image in the stack 
DATEOBS2= '2019-10-26T04:04:48.113' / DATE-OBS for the last  image in the stack 
DATEOBS = '2019-02-14T11:53:52.037' / Mean DATE-OBS for the stack (UTC)         
IMTYPE  = 'image   '           / LegacySurveys image type                       
PRODTYPE= 'image   '           / NOAO image type                                
MAGZERO =                 22.5 / Magnitude zeropoint                            
BUNIT   = 'nanomaggy'          / AB mag = 22.5 - 2.5*log10(nanomaggy)           
COSKY_R = -6.29309506621212E-05 / Sky level estimated (+subtracted) from coadd  
```

## What this pins

### BS-9 input function

The input contract for this DR10 south r-band brick class is: open a two-HDU FITS tile-compressed file; treat HDU 0 as an empty primary HDU; read the logical image from HDU 1; expect a 2-D `(3600, 3600)` float32 array in NumPy `(y, x)` order; retain nanomaggy units; and construct sky/pixel transforms from a two-axis `RA---TAN`/`DEC--TAN` WCS expressed with a CD matrix. Code must not assume the science image is in the primary HDU, mistake the physical binary table dimensions for image dimensions, or assume an uncompressed image.

This one-file probe pins the observed contract for the probed file, not universal invariance across every brick. A production input function should still validate HDU count/type, logical shape/dtype, WCS cards, units, and compression descriptors for every subsequently authorized input and fail closed on divergence.

### R-B geometry decision

The brick's pixel grid is square, 3,600 pixels per axis, with a diagonal CD matrix. The absolute scale from either diagonal CD term is `0.0000727777777777778 deg/pixel = 0.262 arcsec/pixel`; therefore the full grid spans `943.2 arcsec = 15.72 arcmin` per tangent-plane axis. The reference sky coordinate is at FITS pixel `(1800.5, 1800.5)`, the geometric center between the four central pixels. Increasing x decreases tangent-plane RA, increasing y increases Dec, and both cross-terms are zero: the native grid is axis-aligned with north up and east to the left under the usual display convention, with no additional in-plane rotation encoded.

Consequences for cutouts:

- Center on the requested sky coordinate by applying this header WCS and preserve subpixel centers; do not center by catalogue RA/Dec arithmetic alone.
- Convert an angular side length to pixels using 0.262 arcsec/pixel, then predeclare the integer-size and half-pixel rounding convention. Even-sized cutouts require an explicit convention because the brick WCS reference lies at a half-integer FITS coordinate.
- A native-orientation cutout needs no resampling rotation. Any different orientation is a deliberate resampling choice, not implied by this brick.
- Check the complete requested footprint against the `3600 × 3600` pixel domain and/or the header footprint (`RAMIN/RAMAX`, `DECMIN/DECMAX`, `CORN*`). The header establishes geometric bounds but not valid-data coverage within them.
- Coverage/quality at an object position cannot be decided from this image header alone. That requires separately authorized access to the companion inverse-variance and/or mask product and a predeclared rule.

## Read / not-read declaration

Read:

- The frozen selected-brick ID list sufficiently to apply the predeclared lexicographic rule.
- Catalogue identifier/name metadata for the selected ID only.
- The NERSC directory HTML and published checksum-manifest line for the selected image filename.
- Exactly one real brick file: its bytes for transfer, SHA-256, FITS HDU enumeration, complete headers, physical compression descriptors, logical array shape, and dtype implied by `BITPIX/ZBITPIX`.
- Header-stated geometry, edge/footprint, band-presence, units, and provenance metadata.
- The directory-level presence/names of the separate `maskbits` and r-band `invvar` companion products; neither file's bytes or headers were read.

Not read or done:

- No science pixel values were inspected, printed, compared, interpreted, iterated, sampled, or used in a calculation.
- No pixel statistics of any kind were computed: no minimum, maximum, mean, standard deviation, sum, count-by-value, histogram, percentile, quantile, or analogous reduction.
- No plots of pixel data, thumbnails, image renders, or visual inspection were produced.
- No instrument inference was performed. Instrument-related text above is quoted header metadata only.
- No chi or handedness measurement was read or computed.
- No comparison of pixel values across regions was performed.
- No source detection, segmentation, classification, or photometry was performed.
- No mask or inverse-variance pixel values were read; no companion FITS was downloaded or opened.
- No second brick file was downloaded, opened, or probed.

## Questions still open under this authorization

- Whether every selected DR10 south brick has exactly the same HDU count, shape, dtype, compression parameters, WCS representation, and `BUNIT`; one brick cannot establish population-wide invariance.
- Which pixels have valid exposure/coverage, zero inverse variance, masking, saturation, artifacts, or other quality conditions.
- What exact edge-padding or exclusion behavior BS-9 should use when a requested cutout crosses the logical image boundary or valid-coverage boundary.
- Whether the nominal header footprint and actual valid-data footprint differ, and by how much.
- Whether quantized tiled decompression has implementation-specific numerical behavior relevant to later science processing.
- What cutout angular size, integer-pixel parity, rounding convention, interpolation kernel, and padding value R-B should choose; the grid constrains these choices but does not select them.
- Whether a future workflow should consume mask/inverse-variance companions and, if so, their format contracts and the acceptance predicate. Answering this requires new authorization.
- Any question requiring pixel values, statistics, plots, regional comparisons, source detection, instrument inference, chi, or science interpretation.

SEAT: CODEX
VERSION: RC-PROBE-V1
VERDICT: PROBED
COUNT: 1
