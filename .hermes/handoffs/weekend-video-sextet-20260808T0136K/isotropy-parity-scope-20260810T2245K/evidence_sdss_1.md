# URL: https://www.sdss4.org/dr17/imaging/images/

- [Datasets](https://www.sdss4.org/dr17/data_access/)
- [Imaging Data](https://www.sdss4.org/dr17/imaging/)
- [Optical\\
\\
SpectraeBOSS, SPIDERS, TDSS, BOSS, SEGUE, SDSS-I/II](https://www.sdss4.org/dr17/spectro/)
- [APOGEE\\
\\
IR Spectra](https://www.sdss4.org/dr17/irspec/)
- [MaStar\\
\\
Library](https://www.sdss4.org/dr17/mastar/)
- [MaNGA\\
\\
IFU Spectra](https://www.sdss4.org/dr17/manga/)
- [Algorithms](https://www.sdss4.org/dr17/algorithms/)
- [Help](https://www.sdss4.org/dr17/help/)
- [Tutorials](https://www.sdss4.org/dr17/tutorials/)

# Imaging Data Files

[Table of Contents](https://www.sdss4.org/dr17/imaging/images/#toc-body)

- Imaging Data Files

  - Getting and Using Images
  - Corrected Frames
  - Mosaics
  - Atlas Images

    - Description
    - Stand-alone reader
    - Developer Comments
    - Linking the atlas code to scripting languages

  - PSF Data

    - Description
    - Generic Code to Reconstruct the PSF
    - Stand-alone Code

## Getting and Using Images

The [Catalog Archive Server](https://skyserver.sdss.org/) provides an flexible interface to JPG images for finding charts, cutouts for object lists, and point-and-click navigation. See its documentation (or just browse the list of tools on that site) to learn how to use it. The [data access](https://www.sdss4.org/dr17/data_access/) page links to various query forms on CAS to get images by coordinates, or to search for objects from the imaging and spectroscopic catalogs by redshift, object magnitude, color etc., and to retrieve the corresponding data from the SAS.

The [Science Archive Server](https://data.sdss.org/sas/) provides two versions of the FITS images, which can be used for quantitative analysis:

- [corrected frames for each field and band](https://www.sdss4.org/dr17/imaging/images/#corr) (sky-subtracted, calibrated)
- [atlas images for each object](https://www.sdss4.org/dr17/imaging/images/#atlas) (sky-subtracted, but uncalibrated)

The atlas images correspond to what the imaging catalog actually measured its parameters from.

To use the images, it is useful to know the point-spread function (PSF). The SDSS `photo` software has estimated the PSF from the images, and this information is described in the [PSF section](https://www.sdss4.org/dr17/imaging/images/#psf) below.

Convenient tools for searching for images of interest are available on SAS as well (by [run](https://www.sdss4.org/dr17/help/glossary/#run), [camcol](https://www.sdss4.org/dr17/help/glossary/#camcol), [field](https://www.sdss4.org/dr17/help/glossary/#field), or by RA and Dec). Additionally, the SAS is able to produce and return an arbitrary FITS mosaic using the corrected frames.

[Back to Top](https://www.sdss4.org/dr17/imaging/images/#)

## Corrected Frames

The Science Archive Server provides the survey images, called 'corrected frames', as 'frames-\*.fits.bz2' files. See the [frame datamodel](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/frames/RERUN/RUN/CAMCOL/frame.html), which explains the format in detail. These images are calibrated in [nanomaggies](https://www.sdss4.org/dr17/help/glossary/#nanomaggie) per pixel, and have had a sky-subtraction applied. The information about the calibration and sky-subtraction is provided, and can thus be backed-out if necessary.

The SAS provides an [image search tool](http://dr12.sdss3.org/fields/), using RUN, CAMCOL, FIELD or RA, DEC, that returns these corrected frames. When searching for RA and DEC, SAS will return the field which is 'primary' at that location according to the [resolve](https://www.sdss4.org/dr17/algorithms/resolve/) algorithm.

The [sky-subtraction is described in the algorithms page](https://www.sdss4.org/dr17/algorithms/sky/#global). The 'global' method used for creating these images is different from, and far less aggressive than, that applied by the photometric pipeline. The effective smoothing length for the sky background used in these images is around 2 field widths, or 20 arcmin, as opposed to about 2 arcmin for the photometric pipeline.

The image headers have WCS headers that have been corrected to align correctly with the final astrometric solution, but without the polynomial distortion terms. In case the full astrometric solution is desired, it is included as an HDU in the file. The [astrometry algorithms page](https://www.sdss4.org/dr17/algorithms/astrometry/) describes how to use the astrometric calibration information.

The images have a very slightly lossy compression applied, and are subsequently very efficiently losslessly compressed with bzip2. The lossy compression results in a relative loss of precision strictly limited to be less than 0.1% in each pixel, which amounts to a standard deviation of about 0.06%. This precision is far less than the fractional noise already present in the images; since the lossy compression is applied after sky subtraction, this statement about the fractional noise is very safe. As [Price-Whelan & Hogg (2010)](http://adsabs.harvard.edu/abs/2010PASP..122..207P) discuss, the lossy compression thus will have no scientific impact even on stacked images.

It is possible to calculate the noise in the images from the images themselves, using information about their dark variance and gain values. The method for doing so is described in the [frame datamodel](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/frames/RERUN/RUN/CAMCOL/frame.html).

In DR13, these files have not had the new calibration applied, which means they will differ from the imaging catalogs at the level of about a percent.

[Back to Top](https://www.sdss4.org/dr17/imaging/images/#)

## Mosaics

The SAS provides a [mosaic tool](http://dr12.sdss3.org/mosaics/) to stitch together corrected frames to form coherent images over larger patches of the sky. These mosaics are created using the [SWarp](https://www.astromatic.net/software/swarp) utility. The resulting images are calibrated and sky-subtracted just as the corrected frames themselves are. Only the minimal number of 'primary' fields necessary are used for each mosaic.

Currently, mosaics are only provided at the native pixel resolution (0.396 arcsec) and with a position angle of zero (north-up).

In DR13, these files have not had the new calibration applied, which means they will differ from the imaging catalogs at the level of about a percent.

[Back to Top](https://www.sdss4.org/dr17/imaging/images/#)

## Atlas Images

### Description

The `photo` software cuts out a patch of each corrected frame around each object in order to perform its measurements. There is a set of [`fpAtlas*.fits`](https://data.sdss.org/datamodel/files/PHOTO_REDUX/RERUN/RUN/objcs/CAMCOL/fpAtlas.html) files, containing the 'postage-stamp' images for individual objects from the [photometric object lists](https://www.sdss4.org/dr17/imaging/catalogs/). These images are 'deblended', so that those atlas images corresponding to child objects contain only the flux that `photo` decided was part of that object. Atlas images corresponding to parent objects obviously contain all the flux of the children. Note that these images have been sky-subtracted using the [photo sky-subtraction method](https://www.sdss4.org/dr17/algorithms/sky/#photo).

These 'atlas images' are in a binary heap format that is not easily readable by normal humans; think soft encryption. Also, most standard FITS readers will not decode them, or if they do they will appear as a string of integers rather than an actual image raster.

Note that the atlas images once read in need to be calibrated as described below. Additionally, because they are uncalibrated products, they exist in a separate directory tree from the `photoObj` files, as described in their [data model page](https://data.sdss.org/datamodel/files/PHOTO_REDUX/RERUN/RUN/objcs/CAMCOL/fpAtlas.html).

### Stand-alone reader

We have created a standalone code that serves to both read them and as a template library for inclusion in other codes. The code is available as: [readAtlasImages-v5\_4\_11.tar.gz](https://www.sdss4.org/wp-content/uploads/2014/10/readAtlasImages-v5_4_11.tar.gz), and can be compiled as follows on Unix:

1. `% make clean`
2. `% make`

If you are on a big-endian machine, remove `-DSDSS_LITTLE_ENDIAN` from `CFLAGS` in the Makefile. Note that most PCs and Macs that are Intel-based are little-endian, so there is no need to change the Makefile.

If you are using Mac OS 10.6, Snow Leopard, you may encounter an error when compiling. If you see error messages that look like this:

```
cc -o read_atlas_image main.o  -L. -latlas  -lm
Undefined symbols:
"_phRegionSetFromAtlasImage", referenced from:
_main in main.o
"_shRegNew", referenced from:
_main in main.o
...
```

Then you should do

```
export LDFLAGS=libatlas.a
```

if you use bash, or

```
setenv LDFLAGS libatlas.a
```

if you use tcsh. Then do `make clean; make`.

To investigate how to use the stand-alone reader, it is helpful to read the help string:

```
% read_atlas_image -h
Usage: read_atlas_image [options] input-file row output-file
Your options are:
-?      This message
-b #    Set background level to #
-c #    Use color # (0..ncolor-1; default 0)
-h      This message
-i      Print an ID string and exit
-v      Turn up verbosity (repeat flag for more chatter)
```

If one wanted to read the r-band atlas image of an object with id=432 in run 752, rerun 20, camcol 3, field 177, one would say:

```
% read_atlas_image -c 2 fpAtlas-000752-3-0177.fit 432  myAtlasImage.fits
```

where filters u,g,r,i,z are referred to here as color #s 0,1,2,3,4 respectively. The background level is an artificial offset added to all pixels. The SDSS convention is 1000.

The pixel values in the output images are given in counts, not calibrated quantities. To convert to [nanomaggies](https://www.sdss4.org/dr17/help/glossary/#nanomaggie), one would use the [nmgypercount](https://www.sdss4.org/dr17/help/glossary/#nmgypercount) value of the object in question, available in the [photoObj file or CAS table](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/CAMCOL/photoObj.html).

The standalone programs read\_mask (reads fpM files) and read\_PSF (reads psField files, see [below](https://www.sdss4.org/dr17/imaging/images/#psf)) are similar; all three are built by the same 'make' command.

### Developer Comments

Although the `read_atlas_image` executable is perfectly functional, many users prefer to link into custom built executables that need to process atlas image data. The code is easily reused for this purpose.

If you look at the code you'll see that it actually manipulates a type called an ATLAS\_IMAGE. This contains a field called a master\_mask that contains inter alia the bounding box of the atlas image (\[rc\]{min,max}) in the r band, and offsets to that band (d{row,col}).

### Linking the atlas code to scripting languages

Example IDL code that links directly to modified versions of the atlas reader can be found in the `photoop` product distributed with the [SDSS software](https://www.sdss4.org/dr17/software/) (see `pro/atlas/sdss_atlas_image.pro` and associated C code) as well as [`SDSSIDL`](http://github.com/esheldon/sdssidl) (see `pro/sdss/read_atlas.pro` and associated C code).

The atlas images can also be used to reconstruct entire frames. See for example the `photoop` routine `pro/atlas/fpbin_to_frame.pro` and the [`SDSSIDL`](http://github.com/esheldon/sdssidl) routine `pro/sdss/sdss_recframe.pro` and associated C code.

[Back to Top](https://www.sdss4.org/dr17/imaging/images/#)

## PSF Data

### Description

Add information about two-Gaussian and composite PSF from psField file, as well as clarify units (pixels). Also move all references to old read\_psf to point to this page.

The `photo` software fits a PSF as a function of position for every SDSS field. General metadata on the PSF is stored in the [photoField](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/photoField.html) file on SAS, which is equivalent to the `field` table in CAS. Specifically, the `psf_width` parameter reports the average FWHM of a double Gaussian fit to the PSF. In addition, this file reports the parameters of that fit, as the data model describes.

The effective number of pixels neff is defined as inverse of the sum of the squares of the normalized 2-Gaussian PSF, over all pixels. Then psfWidth in pixels is:

𝑝⁢𝑠⁢𝑓⁡𝑊⁢𝑖⁢𝑑⁢𝑡⁢ℎ=√8⁢ln⁡24⁢𝜋⁢√𝑛e⁢f⁡f

and the published values are converted to arcseconds. The actual FWHM of the 2-Gaussian PSF is typically around 0.85 times the `psfWidth` value.

The [photoField](https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/RERUN/RUN/photoField.html) files contains information about the form of the azimuthally symmetric 2-Gaussian PSF. As described in the data model, this includes the sigma for each Gaussian and the ratio ("b") of the smaller width Gaussian to the larger width Gaussian at the origin. They also contain information about an extended model for the PSF which includes a power-law outer component as well as two inner components. The form of this model is as follows:

P⁢S⁢F=exp⁡(−12⁢(𝑟/𝜎1)2)+𝑏⁢exp⁡−(12⁢(𝑟/𝜎2)2)+𝑝0⁢(1+1𝛽⁢(𝑟𝜎𝑝)2)−𝛽/2

The [psField](https://data.sdss.org/datamodel/files/PHOTO_REDUX/RERUN/RUN/objcs/CAMCOL/psField.html) files additionally contain more detailed metadata about the PSF for a given field, in particular the relevant quantities necessary to reconstruct the full PSF at any position in each frame. This PSF will be in the form of a 2D image, whose center is the center of the PSF kernel, with a pixel scale equal the native pixel scale of the SDSS images for the relevant field (very close to 0.396 arcsec per pixel).

### Generic Code to Reconstruct the PSF

The PSF reconstruction can be performed without any specialized tools. For example, to read the PSF info from a psField file for the r band, read extension 3 using your favorite FITS reader. Examples in IDL and Python:

IDL`IDL> pstruct = mrdfits(psfield_file, 3)`Python`>>> pstruct = pyfits.getdata(psfield_file, ext=3)`

(recall u,g,r,i,z == 0,1,2,3,4, which means these bands can be found in extensions 1,2,3,4,5).

The resulting structure can then be used to reconstruct the image. The following IDL code, taken from the [`SDSSIDL`](http://github.com/esheldon/sdssidl) routine `pro/sdss/sdss_psfrec.pro`, demonstrates the algorithm to reconstruct the PSF at location (row,col) in the field. The code would be quite similar in Python with NumPy.

```
nrow_b=(pstruct.nrow_b)[0]
ncol_b=(pstruct.ncol_b)[0]
;assumes they are the same for each eigen
;so only use the 0 one
rnrow=(pstruct.rnrow)[0]
rncol=(pstruct.rncol)[0]

nb=nrow_b*ncol_b
coeffs=fltarr(nb)
ecoeff=fltarr(3)
cmat=pstruct.c

rcs=0.001
for i=0l, nb-1 do coeffs[i]=(row*rcs)^(i mod nrow_b) * (col*rcs)^(i/nrow_b)

for j=0,2 do begin
for i=0l, nb-1 do begin
ecoeff[j]=ecoeff[j]+cmat(i/nrow_b,i mod nrow_b,j)*coeffs[i]
endfor
endfor
psf = (pstruct.rrows)[*,0]*ecoeff[0]+$
(pstruct.rrows)[*,1]*ecoeff[1]+$
(pstruct.rrows)[*,2]*ecoeff[2]
```

The above code can be easily rewritten in other programming languages. For example, the following function allows to reconstruct the PSF in Python.

```
from astropy.io import fits
import numpy as np

def reconstructPSF(psFieldFilename, filter, row, col):

    filterIdx = 'ugriz'.index(filter) + 1
    psField = fits.open(psFieldFilename)
    pStruct = psField[filterIdx].data

    nrow_b = pStruct['nrow_b'][0]
    ncol_b = pStruct['ncol_b'][0]

    rnrow = pStruct['rnrow'][0]
    rncol = pStruct['rncol'][0]

    nb = nrow_b * ncol_b
    coeffs = np.zeros(nb.size, float)
    ecoeff = np.zeros(3, float)
    cmat = pStruct['c']

    rcs = 0.001
    for ii in range(0, nb.size):
        coeffs[ii] = (row * rcs)**(ii % nrow_b) * (col * rcs)**(ii / nrow_b)

    for jj in range(0, 3):
        for ii in range(0, nb.size):
            ecoeff[jj] = ecoeff[jj] + cmat[int(ii / nrow_b), ii % nrow_b, jj] * coeffs[ii]

    psf = pStruct['rrows'][0] * ecoeff[0] + \
        pStruct['rrows'][1] * ecoeff[1] + \
        pStruct['rrows'][2] * ecoeff[2]

    psf = np.reshape(psf, (rnrow, rncol))
    # psf = psf[10:40, 10:40]  # Trim non-zero regions.

    return psf
```

### Stand-alone Code

The atlas image reading code discussed [above](https://www.sdss4.org/dr17/imaging/images/#atlas) also includes a stand-alone piece of software to read in the PSF:

```
% read_PSF -h
Usage: read_PSF [options] input-file hdu output-file
Your options are:
-?      This message
-h      This message
-i      Print an ID string and exit
-v      Turn up verbosity (repeat flag for more chatter)
```

To reconstruct the z PSF ( _i.e._ the 5th HDU) at the position (row, col) = (500, 600) from run 1336, column 2, field 51 you'd say:

```
%  read_PSF psField-001336-2-0051.fit 5 500.0 600.0 foo.fit
```

The desired PSF would appear as an unsigned short FITS file in foo.fit; the background level is set to the standard 'soft bias' of 1000. If you want a floating point image, change a line in the read\_PSF.c; look for

```
        /* create a float region */
```

This code can also be easily linked into larger pieces of code.

[Back to Top](https://www.sdss4.org/dr17/imaging/images/#)