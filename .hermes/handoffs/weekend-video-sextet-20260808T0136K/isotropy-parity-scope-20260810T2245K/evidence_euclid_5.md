# URL: https://irsa.ipac.caltech.edu/ibe/cutouts.html

[NASA/IPAC\\
\\
Infrared\\
\\
Science\\
\\
Archive](https://irsa.ipac.caltech.edu/)

About

\|

Holdings

\|

Data Access

\|

Help

Login

# IRSA Image Server Cutouts

- [Overview](https://irsa.ipac.caltech.edu/ibe/cutouts.html#overview)
- [Quick start guide for IBE cutouts](https://irsa.ipac.caltech.edu/ibe/cutouts.html#intro)
- [Access URLs](https://irsa.ipac.caltech.edu/ibe/cutouts.html#urls)
- [Query parameters](https://irsa.ipac.caltech.edu/ibe/cutouts.html#param)
- [Submitting cutout queries](https://irsa.ipac.caltech.edu/ibe/cutouts.html#submit)
- [Getting Help](https://irsa.ipac.caltech.edu/ibe/cutouts.html#help)

### Overview

The IRSA Image Back End (IBE) can generate cutouts of FITS images in response to programmatic queries.
These queries consist of URLs that are constructed by appending a query string with cutout parameters to the access URL of a FITS image served by the IBE (full details below).
The data sets that are available through this service can be explored in the [IBE data directory tree](https://irsa.ipac.caltech.edu/ibe/data/), with the exception of SPHEREx, which can be found at [/ibe/data/spherex](https://irsa.ipac.caltech.edu/ibe/data/spherex).
Note that not all image data sets stored at IRSA are available through the IBE.
The data served [elsewhere](https://irsa.ipac.caltech.edu/applications/Cutouts/index.html) use a [different cutout service](https://irsa.ipac.caltech.edu/applications/Cutouts/docs/CutoutsProgramInterface.html).

To produce cutouts programmatically, users can either use the command line IBE cutout tool described on this page, or generate cutouts in Python.
Given the URL to a remote hosted FITS image (see the [Access URLs](https://irsa.ipac.caltech.edu/ibe/cutouts.html#urls) section), the astropy function [Cutout2D](https://docs.astropy.org/en/stable/io/fits/usage/cloud.html#using-cutout2d-with-cloud-hosted-fits-files) can be used to extract a cutout without downloading the full image.
To interactively generate and inspect cutouts, the [IRSA Viewer](https://irsa.ipac.caltech.edu/irsaviewer/) is a highly versatile tool with access to most of the imaging and catalog data sets stored at IRSA.

### Quick start guide for IBE cutouts

For files accessed via URLs containing "/ibe/data/", one can request a cutout of a FITS image (or gzipped FITS image) by simply appending a query string containing the center and size parameters to the image URL.

#### Example 1: Euclid cutout in RA and Dec

Image access URLs can be obtained as described in the [Access URLs](https://irsa.ipac.caltech.edu/ibe/cutouts.html#urls) section.
Below is an example of a FITS image URL for a Euclid MERge (MER) Near IR Spectrometer and Photometer (NISP) H-band mosaic (background-subtracted) and the corresponding background model image (note that both of these images are over 1 GB):

- [https://irsa.ipac.caltech.edu/ibe/data/euclid/q1/MER/102158277/NISP/EUC\_MER\_BGSUB-MOSAIC-NIR-H\_TILE102158277-797A7D\_20241025T122514.635323Z\_00.00.fits](https://irsa.ipac.caltech.edu/ibe/data/euclid/q1/MER/102158277/NISP/EUC_MER_BGSUB-MOSAIC-NIR-H_TILE102158277-797A7D_20241025T122514.635323Z_00.00.fits)
- [https://irsa.ipac.caltech.edu/ibe/data/euclid/q1/MER/102158277/NISP/EUC\_MER\_BGMOD-NIR-H\_TILE102158277-48F2AF\_20241025T122514.635142Z\_00.00.fits](https://irsa.ipac.caltech.edu/ibe/data/euclid/q1/MER/102158277/NISP/EUC_MER_BGMOD-NIR-H_TILE102158277-48F2AF_20241025T122514.635142Z_00.00.fits)

To obtain cutouts of these images a query string must be appended to the image URL.
The center position and the size of the cutout can be specified either in terms of pixels or angles.
Here is an example of a cutout request with the query string appended to the image URL given above:

- [https://irsa.ipac.caltech.edu/ibe/data/euclid/q1/MER/102158277/NISP/EUC\_MER\_BGSUB-MOSAIC-NIR-H\_TILE102158277-797A7D\_20241025T122514.635323Z\_00.00.fits?center=273.72107,64.58133deg&size=1arcmin](https://irsa.ipac.caltech.edu/ibe/data/euclid/q1/MER/102158277/NISP/EUC_MER_BGSUB-MOSAIC-NIR-H_TILE102158277-797A7D_20241025T122514.635323Z_00.00.fits?center=273.72107,64.58133deg&size=1arcmin)

Clicking this link (in most browsers) will download the cutout to your default downloads location.
However, you can also download cutouts with command line tools such as [wget](http://www.gnu.org/software/wget/) or [curl](http://curl.haxx.se/) as described in the [Submitting cutout queries](https://irsa.ipac.caltech.edu/ibe/cutouts.html#submit) section below.

Most cutouts are gzipped by default and will have the extension ".fits.gz".
Although many FITS file viewers can read gzipped FITS files directly, if you prefer to download uncompressed cutouts, adding gzip=false to the parameters will cause an uncompressed FITS image to be returned instead.

Note that Euclid cutouts should, in general, use the MER images, rather than the individual exposures.
Each detector in the individual exposure FITS files is stored as a separate FITS extension, which is not currently supported by the IBE cutout service.

#### Example 2: SPHEREx cutout in pixels

Cutout positions and sizes can also be specified in terms of pixels in the parent image.
In the example below a 100 x 100 pixel cutout is made from a SPHEREx image:

- [https://irsa.ipac.caltech.edu/ibe/data/spherex/qr2/level2/2025W20\_1C/l2b-v20-2025-247/1/level2\_2025W20\_1C\_0002\_2D1\_spx\_l2b-v20-2025-247.fits?center=570,900pix&size=100pix](https://irsa.ipac.caltech.edu/ibe/data/spherex/qr2/level2/2025W20_1C/l2b-v20-2025-247/1/level2_2025W20_1C_0002_2D1_spx_l2b-v20-2025-247.fits?center=570,900pix&size=100pix)

SPHEREx spectral images are stored in Multi-Extension FITS (MEF) format, with the first extension containing the primary image data, and subsequent extensions containing a variance image, the zodiacal light background, etc.
For more details, refer to Section 2.2 of the [SPHEREx Explanatory Supplement](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/SPHEREx_Expsupp_QR.pdf).
All extensions are cut out in the same way, so the cutout returned will also be a MEF file with the same number of extensions as the parent image.
Unlike cutouts from other data sets, SPHEREx cutouts will not be gzipped.

It is important to note that the axes of cutouts are always aligned with the axes of the parent image, which may not match the cardinal directions.
As the parent image in this example is a single exposure rather than a re-gridded mosaic, its orientation depends on the spacecraft orientation at the time of the exposure, and is not aligned with the typical north-up, east-left convention.
This would be the case even if the cutout was specified in terms of RA and Dec, and an angular size. Furthermore, SPHEREx images have distortion corrections in their WCS headers, so pixel scale and orientations vary across the image. These corrections are often not supported by FITS viewers.

#### Example 3: Clipped 2MASS cutouts from gzipped images

The units of the position and size parameters do not have to be the same, and there are multiple queries that will yield identical cutouts.
For example, the following two URLs will both return the same cutout from a 2MASS image (which has 1 arcsec pixels):

- [https://irsa.ipac.caltech.edu/ibe/data/twomass/allsky/allsky/000105s/s019/image/hi0190056.fits.gz?center=29,176pix&size=90arcsec](https://irsa.ipac.caltech.edu/ibe/data/twomass/allsky/allsky/000105s/s019/image/hi0190056.fits.gz?center=29,176pix&size=90arcsec)
- [https://irsa.ipac.caltech.edu/ibe/data/twomass/allsky/allsky/000105s/s019/image/hi0190056.fits.gz?center=83.9124,-43.1616deg&size=90pix](https://irsa.ipac.caltech.edu/ibe/data/twomass/allsky/allsky/000105s/s019/image/hi0190056.fits.gz?center=83.9124,-43.1616deg&size=90pix)

Note that in this case the parent image is a gzipped FITS file (with extension ".fits.gz").
The cutout service can handle either gzipped or uncompressed FITS parent images, and will return cutouts in gzipped form by default, regardless of whether the parent image is compressed or not.

If you open one of the cutouts produced by the above queries, you will notice that it is not a square, 90 x 90 pixel, image.
This is because the requested cutout extends beyond the boundaries of the parent image.
In such cases, the cutout service will still return a cutout, but it will be clipped to the portion that intersects the parent image.
An error will only be returned if the requested cutout does not intersect the parent image at all.

For the service to successfully return a cutout, the cutout center does not even need to be within the parent image, there simply needs to be non-zero overlap between the cutout area and the parent image.
To illustrate an extreme example, the URL below will return a cutout with just a single column of pixels (all NaNs as they are from the edge of the image):

- [https://irsa.ipac.caltech.edu/ibe/data/twomass/allsky/allsky/000105s/s019/image/hi0190056.fits.gz?center=-49,175pix&size=100pix](https://irsa.ipac.caltech.edu/ibe/data/twomass/allsky/allsky/000105s/s019/image/hi0190056.fits.gz?center=-49,175pix&size=100pix)

If the cutout center was moved one more pixel away from the image edge, then the request would instead return a 500 Internal Server Error, as the requested cutout would be completely outside of the parent image.

#### Example 4: WISE image and uncertainty cutouts

Some of the available data sets have accompanying uncertainty, background, or other ancillary images that match the coverage of the primary images and can be cutout in the same way.
These can usually be selected with a small systematic change to the primary image URL.
Here are two such sample URLs for a WISE W1 image and its corresponding uncertainty image:

- [https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band\_p1bm\_frm/6a/02206a/149/02206a149-w1-int-1b.fits](https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a/149/02206a149-w1-int-1b.fits)
- [https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band\_p1bm\_frm/6a/02206a/149/02206a149-w1-unc-1b.fits.gz](https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a/149/02206a149-w1-unc-1b.fits.gz)

The URLs below extract identical cutout areas from the image and the uncertainty image.
In this case, we have also chosen to override the default gzipping behavior.

- [https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band\_p1bm\_frm/6a/02206a/149/02206a149-w1-int-1b.fits?center=70,20&size=200pix&gzip=false](https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a/149/02206a149-w1-int-1b.fits?center=70,20&size=200pix&gzip=false)
- [https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band\_p1bm\_frm/6a/02206a/149/02206a149-w1-unc-1b.fits.gz?center=70,20&size=200pix&gzip=false](https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a/149/02206a149-w1-unc-1b.fits.gz?center=70,20&size=200pix&gzip=false)

### Access URLs

All cutouts requested through the IBE service must begin with an access URL that identifies the FITS image from which the cutout will be extracted.
The data sets that are available through this service can be explored in the [general IBE data directory](https://irsa.ipac.caltech.edu/ibe/data/), with the exception of SPHEREx, which can be found in a [SPHEREx-specific directory](https://irsa.ipac.caltech.edu/ibe/data/spherex).
The image access URLs can be copied from your browser after navigating to the desired image in the IBE data directory tree.
In addition, [instructions](https://irsa.ipac.caltech.edu/ibe/docs/) are available describing on how to programmatically construct access URLs for WISE, 2MASS, and PTF.

Image access URLs for almost all images hosted by IRSA can also be obtained through the [Simple Image Access v2 (SIAv2) service](https://irsa.ipac.caltech.edu/docs/program_interface/api_images.html).
In the case of moving objects, image access URLs can be obtained through the [Moving Object Search Tool (MOST)](https://irsa.ipac.caltech.edu/applications/MOST/), or its [astroquery interface](https://astroquery.readthedocs.io/en/latest/ipac/irsa/most.html), for (NEO)WISE, 2MASS, Spitzer, PTF, and ZTF images.
However, only image URLs containing "/ibe/data/" can be used to generate cutouts through this service.

Note that not all of the data stored at [/ibe/data/](https://irsa.ipac.caltech.edu/ibe/data/) is compatible with the cutout service, for example, IRAS.
Please see IRSA's [alternate cutout tool](https://irsa.ipac.caltech.edu/applications/Cutouts/docs/CutoutsProgramInterface.html) for data sets that are not compatible with the IBE cutout service.
If there is any IRSA data set that you need to create cutouts from, but cannot, then please submit a question to the [help desk](https://irsa.ipac.caltech.edu/docs/help_desk.html).

### Query parameters

Cutout requests are made by appending a query string with cutout parameters to the access URL of a FITS image served by the IBE.
The query string must begin with a question mark ( `?`), and parameters are separated from each other by ampersands ( `&`).
At a minimum, the center and size parameters must be specified.
An optional gzip parameter can also be included to control whether the cutout is returned in compressed (gzipped) form or not (default is to gzip).
The order of the parameters is not important.

Thus, the basic structure of a cutout request URL is as follows:

- <imageURL> `?` center=<value> `&` size=<value>\[ `&` gzip=<true\|false>\]

Further details on the syntax of the parameter values is provided below.

center=x,y\[units\]

The center parameter must consist of a
comma separated coordinate pair followed by an optional units
specification. If **units** is set to `px`,
`pix` or `pixels`, then **x,y** are interpreted
as the pixel space coordinates of the desired cutout center. If
**units** are angular ( `rad`, `deg`, etc...),
then **x,y** are interpreted as the J2000 right ascension
( **x**) and declination ( **y**) of the
desired cutout center. If no units are specified, degrees are assumed.
Declinations outside of \[-90, 90\] degrees are illegal; right ascensions
are range-reduced, so any value will do.


Examples:

- center=10,10deg
- center=10,10
- center=3.141,1.56rad
- center=300.5,120px

size=x\[,y\]\[units\]

The size parameter consists of one or two
(comma separated) values followed by an optional units specification.
Units can be pixels ( `px`, `pix`, `pixels`) or
angular ( `arcsec`, `arcmin`, `deg`, `rad`);
the default is degrees. The first size value ( **x**) is
taken to be the full-width of the desired cutout along the first
image axis ( `NAXIS1`), and the second ( **y**) is
taken to be the full-height along the second axis ( `NAXIS2`).
If only one size value is specified, it is used as both the full-width
and full-height. Negative sizes are illegal.


Examples:

- size=0.1
- size=200px
- size=100,200px
- size=3arcmin
- size=30,45arcsec

gzip=flag

This parameter determines whether or not the cutout is returned in
compressed (gzipped) form or not. If the parameter is omitted,
then cutouts are gzipped. Compression can also be explicitly requested
with:


- gzip=1
- gzip=on
- gzip=t\[rue\]
- gzip=y\[es\]

To download uncompressed images, pass:

- gzip=0
- gzip=off
- gzip=f\[alse\]
- gzip=n\[o\]

Parsing of unit specifications is fairly forgiving, e.g. `radians`,
`asec`, `"`, `arcminutes` and `'` are all
recognized. Malformed unit specifications and illegal sizes or coordinates
will result in an HTTP 400 Bad Request response.

**Submitting cutout queries**

Queries can be submitted by simply pasting the constructed URL into a web browser.
Most browsers will either download the cutout file directly, adopting a default filename, or may prompt the user with a "Save As" dialog box.
You can also use command-line tools such as
[wget](http://www.gnu.org/software/wget/) or
[curl](http://curl.haxx.se/) to download cutouts.
The basic syntax for both of these tools is shown below.

wget

The query URL should be passed to wget in quotes.
If this is the only parameter being passed to wget, the cutout will be saved to a local file with the same name as the last segment of the URL path (i.e., everything after the last slash), which is usually a cumbersome and unhelpful file name.
The output file name can be specified with either the `-O` or `--output-document` option in wget.


```bsh
wget -O filename "URL"
```

or equivalently:

```bsh
wget --output-document=filename "URL"
```

For example:

```bsh
wget --output-document=mycutout.fits.gz "https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a/149/02206a149-w1-int-1b.fits?center=70,20&size=200pix"
```

Care should be taken to ensure that the file name extension (e.g., `.fits` or `.fits.gz`) matches the format of the returned cutout, otherwise you may have trouble opening the file with your FITS viewer.


If instead you wish to use the default suggested file name, which will be the name of the parent image, you can make wget use this with the `--content-disposition` option.
For example:


```bsh
wget --content-disposition "https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a/149/02206a149-w1-int-1b.fits?center=70,20&size=200pix"
```

curl

The same operations can also be performed with curl.
If curl is passed only the query URL, it will attempt write the cutout to standard output, and likely fail.
Thus, for curl it is even more important to specify a local output file name with either the `-o` or `--output` option.


```bsh
curl -o filename "URL"
```

or equivalently:

```bsh
curl --output filename "URL"
```

For example:

```bsh
curl --output mycutout.fits.gz "https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a/149/02206a149-w1-int-1b.fits?center=70,20&size=200pix"
```

It is also possible to pipe curl's output directly to a file (rather than stdout):

```bsh
curl "URL" > filename
```

Again, if you wish to use the default suggested file name, you can make curl do this by using the `-O` option in conjunction with the `-J` option.


```bsh
curl -O -J "https://irsa.ipac.caltech.edu/ibe/data/wise/allsky/4band_p1bm_frm/6a/02206a/149/02206a149-w1-int-1b.fits?center=70,20&size=200pix"
```

**Getting Help**

If you've run into a problem, think you've found a bug, or simply have questions, please contact
[IRSA User Support](https://irsa.ipac.caltech.edu/docs/help_desk.html).

- [Contact](https://irsa.ipac.caltech.edu/docs/help_desk.html)
- [Privacy Policy](https://irsa.ipac.caltech.edu/privacy.html)
- [Acknowledge IRSA](https://irsa.ipac.caltech.edu/ack.html)

Search IRSA

[![Icon_ipac](https://irsa.ipac.caltech.edu/frontpage/images/icon_ipac-white-78x60.png)](http://www.ipac.caltech.edu/ "Infrared Processing and Analysis Center")[![Icon_caltech](https://irsa.ipac.caltech.edu/frontpage/images/icon_caltech-new.png)](http://www.caltech.edu/ "California Institute of Technology")[![Icon_jpl](https://irsa.ipac.caltech.edu/frontpage/images/icon_jpl-white-91x60.png)](http://www.jpl.nasa.gov/ "Jet Propulsion Laboratory")[![Icon_nasa](https://irsa.ipac.caltech.edu/frontpage/images/icon_nasa-white-59x60.png)](http://www.nasa.gov/ "National Aeronautics and Space Administration")