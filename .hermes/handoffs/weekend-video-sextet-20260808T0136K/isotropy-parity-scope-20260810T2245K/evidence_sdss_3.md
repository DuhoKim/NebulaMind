# URL: https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/frames/RERUN/RUN/CAMCOL/frame.html

# Data model: frame

General Description
The calibrated, sky-subtracted corrected frame plus associated
calibration meta-data. The units of the images are in
[nanomaggies](http://www.sdss.org/dr13/help/glossary/#nanomaggie).
It is kept compressed under "bzip2", which we
have found is the most efficient compressor of this format. In
addition, there is a lossy compression applied to the floating point
values (which retains accuracy at the 0.1 percent level). The IDL
routine "read\_frame.pro" in photoop will back out the calibration and
sky-subtraction from this file if necessary, in steps explained
below. Also explained below is how to calculate the noise in the
image.
Naming Convention`frame-[ugriz]-[0-9]{6}-[1-6]-[0-9]{4}\.fits\.bz2`, where
`[ugriz]` is the filter, `[0-9]{6}` is a zero-padded six-digit
number containing the run number, `[1-6]` is the camera column ('camcol') and
`[0-9]{4}` is the zero-padded, four-digit frame sequence number.Approximate Size3 MbytesFile TypeFITSRead by ProductssasWritten by Productssas

## HDU0: the corrected frame, what is normally in the "fpC" files

The "image", a 2048x1489 array of floating point values, the
calibrated and sky-subtracted version of the fpC "corrected frame"
files produced by photo. Units are in
[nanomaggies](http://www.sdss.org/dr13/help/glossary/#nanomaggie).

The header has additional WCS information. These have been altered
from the fpC versions to correct for any offsets from the astrom
solutions found in the asTrans files.

The image itself has had the FLOATCOMPRESS algorithm
(see the [idlutils](http://www.sdss.org/dr13/software/idlutils/) package)
applied to it, keeping 10 significant binary digits. This approach guarantees that the
precision is kept strictly within 0.1 percent per pixel, and allows a very efficient
compression using bzip2. No special scaling or adjustment need be
applied to the values when read in.

## HDU1: the flat-field and calibration vector

The "calibvec", a 2048-element array of "float32" values,
encompassing the flat-field correction to apply, multiplied by the
calibration. Translates the counts in the original image into
[nanomaggies](http://www.sdss.org/dr13/help/glossary/#nanomaggie).

The calibrations have ALREADY been applied to the HDU0, so this
calibration vector is only to be used to _decalibrate_ an image
back into counts.

## HDU2: the sky image

The "sky", an approximately 256x192 array of "float32" values
(there are some variations around the y-size of the array), with
information about how to interpolate it to the full image size. These
sky values are determined from the global sky fits across the run (not
photo).

There are cases at the end of runs where the y-size
of `ALLSKY` is less than 186, which requires one to
extrapolate off the end of the `ALLSKY` image in the
y-direction when using `XINTERP`
and `YINTERP`. This extrapolation should be a constant
extrapolation (not linear).

The sky values have ALREADY been subtracted from HDU0, so this
sky estimate is only to be used to return an image to its (near)
original set of values.

| Name | Type | Comment |
| --- | --- | --- |
| ALLSKY | float32\[256,ny\] | the binned sky values, in units of counts |
| XINTERP | float32\[2048\] | X pixel-values to interpolate "allsky" into to produce a full image of the sky (bilinear interpolation is fine) |
| YINTERP | float32\[1489\] | Y pixel-values to interpolate "allsky" into to produce a full image of the sky (bilinear interpolation is fine) |

Required Columns

## HDU3: the asTrans structure

Detailed astrometric information for the field. Basically the
asTrans structure as found in the [asTrans](https://data.sdss.org/datamodel/files/PHOTO_REDUX/RERUN/RUN/astrom/asTrans.html)
files.

| Name | Type | Comment |
| --- | --- | --- |
| RUN | int32 | Run number |
| RERUN | char\[3\] | Photometric reduction version |
| CAMCOL | int32 | Column in the imaging camera. |
| FILTER | char\[1\] | Filter (u, g, r, i, or z). |
| NODE | float64 | RA of great circle's asending node. (degrees) |
| INCL | float64 | RA of great circle's asending node. (degrees) |
| NAXIS | int32\[2\] | The dimensions of the image the astrometry is based on. Usually 2048x1489, but could be different in principle for binned runs. |
| FIELD | int32 | Field sequence number within the run. |
| A | float64 | A coefficient. |
| B | float64 | B coefficient. |
| C | float64 | C coefficient. |
| D | float64 | D coefficient. |
| E | float64 | E coefficient. |
| F | float64 | F coefficient. |
| DROW0 | float64 | Zero-order row distortion coefficient. |
| DROW1 | float64 | First-order row distortion coefficient. |
| DROW2 | float64 | Second-order row distortion coefficient. |
| DROW3 | float64 | Third-order row distortion coefficient. |
| DCOL0 | float64 | Zero-order column distortion coefficient. |
| DCOL1 | float64 | First-order column distortion coefficient. |
| DCOL2 | float64 | Second-order column distortion coefficient. |
| DCOL3 | float64 | Third-order column distortion coefficient. |
| CSROW | float64 | Slope in row DCR correction for blue objects. |
| CSCOL | float64 | Slope in column DCR correction for blue objects. |
| CCROW | float64 | Constant row DCR correction for red objects. |
| CCCOL | float64 | Constant column DCR correction for red objects. |
| RICUT | float64 | r'-i' cutoff between blue and red objects. |
| MJD | float64 | MJD(TAI) when row 0 was read. |
| AIRMASS | float64 | Airmass for star at frame center (mid exposure) |
| MUERR | float32 | Error in transformation in mu |
| NUERR | float32 | Error in transformation in nu |

Required Columns

## Example of use, and calculating errors

As a guide to how to successfully read in and interpret this file, we
reproduce here code from "read\_frame.pro" in the photoop IDL
product:

```
;; 0. find filename of the frame file
framename = (sdss_name('frame', run, camcol, field, $
                       filter=filternum(filter), rerun=rerun))[0]+'.bz2'

;; 1. read in the FITS image from HDU0; the resulting image will be
;;    sky-subtracted as well as calibrated in nanomaggies/pixel
img= mrdfits(framename,0,hdr)
nrowc= (size(img,/dim))[1]

;; 2. read in sky, and interpolate to full image size; this returns a
;;    sky image the same size as the frame image, in units of counts
sky= mrdfits(framename,2)
simg= interpolate(sky.allsky, sky.xinterp, sky.yinterp, /grid)

;; 3. read in calibration, and expand to full image size; this returns
;;    a calibration image the same size as the frame image, in units of
;;    nanomaggies per count
calib= mrdfits(framename,1)
cimg= calib#replicate(1.,nrowc)
```

Steps (0) and (1) just read in the "image". Step (2) reads in the
sky HDU, and bilinearly interpolates "allsky" onto a 2048x1489 sized array
at the points on the grid defined by "xinterp" and "yinterp". Step (3)
reads in the 2048-element vector defined the
calibration-times-flat-field for each row, and expands it to a
full-sized image.

If you have performed the above calculations, you can return the
image to very close to the state it was in when input into the
photometric pipeline, as follows:

```
dn= img/cimg+simg
```

These `dn` values are in the same units as the "data
numbers" stored by the raw data files that come off the instrument.
They are related to the detected number `nelec` of
photo-electrons by:

```
nelec= dn*gain
```

The number of photo-electrons is the quantity that is statistically
Poisson distributed. In addition, there are additional sources of
noise from the read-noise and the noise in the dark current, which
we will lump together here as the "dark variance." Thus, to
calculate per-pixel uncertainties, you need the `gain`
and `darkVariance` for the field in question. The
`darkVariance` comes from the read noise and the noise in
the dark current. In fact, these
are nearly fixed as a function of [`camcol`](http://www.sdss.org/dr13/help/glossary/#camcol) and filter (see
the table below). You can retrieve the values from the
`field` table in CAS (or the [`photoField`](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/photoField.html)
file). With those values in hand the following yields the errors in
DN:

```
dn_err= sqrt(dn/gain+darkVariance)
```

Statistical errors in the sky values are completely negligible.
Finally, to get those errors into
[nanomaggies](http://www.sdss.org/dr13/help/glossary/#nanomaggie),
you simply
apply back the calibration:

```
img_err= dn_err*cimg
```

Finally, there are some areas of the image which are part of bleed
trails, bad columns, and the like. If you require to track those in
your analysis (e.g. weight them at zero) then you need to use the [fpM](https://data.sdss.org/datamodel/files/PHOTO_REDUX/RERUN/RUN/objcs/CAMCOL/fpM.html)
files. Those files are in a special format, best read using the [stand-alone\\
atlas reader software](http://www.sdss.org/dr13/imaging/images/#atlas). Use the utility called
`read_mask`.

The gain and dark variance values are given below as a function of
camcol and filter. In some cases the configuration was changed during
the survey, and those cases are noted below. In detail, some chips had
two amplifiers, and in those cases the values below are an
intermediate value.

| `camcol` | u | g | r | i | z |
| --- | --- | --- | --- | --- | --- |
| 1 | 1.62 | 3.32 | 4.71 | 5.165 | 4.745 |
| 2 | 1.595 (for `run` < 1100)<br>1.825 (for `run` \> 1100) | 3.855 | 4.6 | 6.565 | 5.155 |
| 3 | 1.59 | 3.845 | 4.72 | 4.86 | 4.885 |
| 4 | 1.6 | 3.995 | 4.76 | 4.885 | 4.775 |
| 5 | 1.47 | 4.05 | 4.725 | 4.64 | 3.48 |
| 6 | 2.17 | 4.035 | 4.895 | 4.76 | 4.69 |

Gain of each CCD

| `camcol` | u | g | r | i | z |
| --- | --- | --- | --- | --- | --- |
| 1 | 9.61 | 15.6025 | 1.8225 | 7.84 | 0.81 |
| 2 | 12.6025 | 1.44 | 1.00 | 5.76 (for `run` < 1500)<br>6.25(for `run` \> 1500) | 1.0 |
| 3 | 8.7025 | 1.3225 | 1.3225 | 4.6225 | 1.0 |
| 4 | 12.6025 | 1.96 | 1.3225 | 6.25 (for `run` < 1500)<br>7.5625(for `run` \> 1500) | 9.61 (for `run` < 1500)<br>12.6025(for `run` \> 1500) |
| 5 | 9.3025 | 1.1025 | 0.81 | 7.84 | 1.8225 (for `run` < 1500)<br>2.1025(for `run` \> 1500) |
| 6 | 7.0225 | 1.8225 | 0.9025 | 5.0625 | 1.21 |

Dark variance of each CCD