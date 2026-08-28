SOURCE URL: https://www.sdss4.org/dr17/imaging/jpg-images-on-skyserver/
TITLE: JPEG Images on SkyServer | SDSS
ACCESSED: 2026-08-12 KST

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

# JPEG Images on SkyServer

The [Visual Tools](https://skyserver.sdss.org/public/VisualTools/) section of [Skyserver](https://skyserver.sdss.org/public/) – which includes the [**Finding Chart**](https://skyserver.sdss.org/public/VisualTools/explore/chartinfo), [**Navigate**](https://skyserver.sdss.org/public/VisualTools/navi), **[Image Lists](https://skyserver.sdss.org/public/VisualTools/list)** pages and the postage stamp image displayed on the [**Explore**](https://skyserver.sdss.org/public/VisualTools/explore/summary) page for each object – uses JPEG versions of the SDSS images that are retrieved and constructed on the fly by the [**ImgCutout**](http://skyservice.pha.jhu.edu/imgcutout) web service by querying the [**Catalog Archive Server (CAS)**](https://skyserver.sdss.org/public/support) databases for the given data release.

In order to create the base JPEG images that are then stored in multiple zoom levels (resolutions) in the CAS databases, the **FITS2JPEG converter** – a MATLAB code – reads in the g, r, i-band FITS corrected frame files from the [**Science Archive Server (SAS)**](https://data.sdss.org/sas) and performs a number of transformations on them before converting them to 3-color JPEG images (i-r-g to `R-G-B`), as described in the FITS to JPEG conversion data flow diagram shown below. Multiple “zoom levels” or resolutions are generated for each image, facilitating zooming in and out in the visual tools interface.  Images are interpolated between the preset zoom levels. The conversion is based upon an algorithm described in [Lupton _et al._ (2004)](http://adsabs.harvard.edu/abs/2004PASP..116..133L), with some modifications.

![Flowchart describing FITS to JPEG conversion.](https://www.sdss4.org/wp-content/uploads/2014/11/FITS2JPEG3.jpg) FITS to JPEG (MATLAB) conversion code that converts corrected frame FITS files from the SAS to 3-color JPEG images at various resolutions for loading into the CAS Frame table.

In the CAS database, image [frames](https://www.sdss4.org/dr17/help/glossary/#frame) are stored in the **Frame** table according to their [fieldIDs](https://www.sdss4.org/dr17/help/glossary/#fieldid) and zoom levels, along with photometry and [run, rerun, camcol parameters](https://www.sdss4.org/dr17/imaging/imaging_basics/). When a user asks for an image cutout for the given coordinates on the sky with the desired dimensions, the ImgCutout service first parses the request and figures out the scale needed to query images from the database.  Using the given coordinates and scale, a SQL function is invoked in the database that zeroes in on the frames that contain the given part of the sky.  ImgCutout then uses these frames to draw the image upon the canvas using the affine transform. Since these are the whole SDSS frames attached to each other ( _i.e._, mosaicked) and the user usually wants a piece of the total area covered by the frames, the final image displayed is trimmed to the given width and height with the requested coordinate at the center. When the user selects certain overlay options, for example to highlight Photo Objects or Spec Objects or to draw SDSS fields, a separate set of queries is run along with the original image query. These queries return a list of objects with coordinates. These co-ordinates are used to draw distinct markers for various objects on the underlying image, as requested by user.
