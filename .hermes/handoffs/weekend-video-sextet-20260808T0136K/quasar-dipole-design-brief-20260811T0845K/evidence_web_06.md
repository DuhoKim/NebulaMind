|     |     |     |
| --- | --- | --- |
| [Search in\<br>\<br>Xamin](https://heasarc.gsfc.nasa.gov/xamin/?table=nvss) or [Browse](https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dnvss&Action=More+Options)... | # NVSS - NRAO VLA Sky Survey Catalog | [HEASARC\<br>\<br>Archive](https://heasarc.gsfc.nasa.gov/docs/archive.html) |

* * *

## Overview

This table contains the National Radio Astronomy Observatory (NRAO) Very
Large Array (VLA) Sky Survey, the so-called NVSS Catalog. The NVSS Catalog
covers the sky north of the J2000.0 Declination of -40 degrees (82% of the
celestial sphere) at 1.4 GHz. The principal data products of the NVSS were
(1) a set of 2326 4 degree by 4 degree continuum "cubes" with three planes
containing Stokes I, Q, and U images, plus (2) a catalog of almost 2 million
discrete sources stronger than a flux density S of about 2.5 mJy. The images
all have 45 arcsecond FWHM angular resolution and nearly uniform sensitivity.
Their rms brightness fluctuations are approximately 0.45 mJy/beam = 0.14 K
(Stokes I) and approximately 0.29 mJy/beam = 0.09 K (Stokes Q and U). The rms
uncertainties in right ascension and declination vary from <= ~1 arcsecond
for the 400,000 sources stronger than 15 mJy to 7 arcseconds at the survey
limit. The NVSS was made as a service to the astronomical community. All data
products, user software, and updates were released via the World-Wide Web as
soon as they were produced and verified. For more complete information on the
NVSS, please refer to the NVSS website at [http://www.cv.nrao.edu/nvss/](http://www.cv.nrao.edu/nvss/)

* * *

### Catalog Bibcode

[1998AJ....115.1693C](https://ui.adsabs.harvard.edu/abs/1998AJ%2E%2E%2E%2E115%2E1693C)

* * *

### References

```
1.4GHz NRAO VLA Sky Survey (NVSS)
   Condon J.J., Cotton W.D., Greisen E.W., Yin Q.F., Perley R.A., Taylor G.B.
   and Broderick J.J.
   <Astron. J. 115, 1693 (1998)>

The NRAO VLA Sky Survey (NVSS)
   http://www.cv.nrao.edu/nvss/
```

* * *

### Provenance

This table was created by the HEASARC in October 2002 based on the file
[ftp://ftp.cv.nrao.edu/nvss/CATALOG/NVSSCatalog.text.gz](ftp://ftp.cv.nrao.edu/nvss/CATALOG/NVSSCatalog.text.gz) provided by the NVSS
Catalog's authors. It was updated by the HEASARC in June 2009 to fix a
problem with the original ingest in which the leading digit of some flux
fields was lost.

* * *

### Data Products

The NVSS project at NRAO maintains an FTP archive of the (u,v) data and
images from which the source catalog was constructed. These files are
available as remote data products linked to the entries in the HEASARC
implementation of the NVSS source catalog. Clicking on a data product link
for a given source will fetch the (u,v) and/or image data for the field in
which the selected source was found. The large (4 degree X 4 degree) maps and
their associated multisource (u,v) data sets are stored by NRAO as binary
files in FITS format. The naming conventions of these files are as follows.
Each map is named after the J2000 right ascension and declination of its
center, and the first letter specifies the polarization plane(s). For
example, C2230P84.gz is the map cube with Stokes I, Q, and U planes centered
on right ascension = 22h 30m, declination = +84 deg. I0224M32.gz contains
only the total-intensity plane centered on right ascension 02h 24m,
declination -32 deg. The corresponding total intensity map file is
I2230P84.gz, and the corresponding multisource (u,v) data file is called
J0224-32.MS. The compressed map cubes are about 1.7 megabytes in size, and
the total-intensity maps are smaller (about 0.7 megabytes) for faster access
by users not interested in linear polarization. Please note that not every
NVSS survey field will have a corresponding multisource (u,v) data file.

* * *

### Parameters

**Name**

The NVSS Catalog designation of the form NVSS JHHMMSS+DDMMSS, using the
standard IAU nomenclature prescription, where NVSS is the catalog acronym, J
specifies the coordinate equinox (either "J" for J2000.0 or "B" for B1950.0),
HHMMSS are the hours, minutes, and truncated (not rounded) seconds of right
ascension, + or - is the sign of the declination, and DDMMSS are the degrees,
arcminutes, and truncated (not rounded) arcseconds of declination. Thus, the
NVSS source at equinox J2000.0 coordinates of 00h 00m 00.24s, = -20d 04'
49.1" is called NVSS J000000-200449. There are four cases where there are
pairs of sources which are so close together that their names would be
identical according to this schema (see below), and the HEASARC has added
suffixes of 'a' (for the source with the smaller RA) and 'b' (for the source
with the larger RA) in such cases in order to differentate them.


```
  |Name                |RA (J2000)|Dec (J2000)
  |                    | degrees  |  degrees
  |NVSS J093731-102001a|144.381833|-10.333833
  |NVSS J093731-102001b|144.383000|-10.333750
  |NVSS J133156-121336a|202.986708|-12.226750
  |NVSS J133156-121336b|202.987167|-12.226667
  |NVSS J160612+000027a|241.552917|  0.007611
  |NVSS J160612+000027b|241.553625|  0.007639
  |NVSS J215552+380029a|328.967375| 38.008111
  |NVSS J215552+380029b|328.968792| 38.008139
```

**RA**

The Right Ascension of the centroid of the fitted radio source in the
selected equinox and for the epoch of observation 1995 +/- 2. This was given
in equinox J2000 and with a precision of 0.01 seconds of time in the original
table.

**Dec**

The Declination of the centroid of the fitted radio source in the selected
equinox and for the epoch of observation 1995 +/- 2. This was given in
equinox J2000 and with a precision of 0.1 arcseconds in the original table.

**LII**

The Galactic Longitude of the centroid of the fitted radio source.

**BII**

The Galactic Latitude of the centroid of the fitted radio source.

**RA\_Error**

The rms uncertainty in the Right Ascension, in seconds of time.

**Dec\_Error**

The rms uncertainty in the Declination, in arcseconds.

**Flux\_20\_cm**

The integrated 1.4-GHz flux density of the radio source, in milliJanskies
(mJy).

**Flux\_20\_cm\_Error**

The rms uncertainty in the 1.4-GHz flux density of the radio source, in
milliJanskies (mJy).

**Limit\_Major\_Axis**

A limit flag parameter for the fitted major axis of the radio source which is
set to '<' if it is not significantly resolved.

**Major\_Axis**

The fitted (deconvolved) major axis of the radio source, in arcseconds.

**Major\_Axis\_Error**

The rms uncertainty in the fitted major axis of the radio source, in
arcseconds.

**Limit\_Minor\_Axis**

A limit flag parameter for the fitted minor axis of the radio source which is
set to '<' if it is not significantly resolved.

**Minor\_Axis**

The fitted (deconvolved) minor axis of the radio source, in arcseconds.

**Minor\_Axis\_Error**

The rms uncertainty in the fitted minor axis of the radio source, in
arcseconds.

**Position\_Angle**

The position angle of the fitted major axis of the radio source, in degrees.

**Position\_Angle\_Error**

The rms uncertainty in the position angle of the fitted major axis of the
radio source, in degrees.

**Residual\_Code**

A code flag parameter for the residuals to the fit to the radio source which
is set to 'P' if the peak flux density residual was high, or 'S' if the
integrated flux density of the residual was high, and is otherwise left blank.
Non-blank values of this parameter are typically indicative of complex source
structure.

**Residual\_Flux**

In cases where the value of the residual\_code parameter is non-blank, this
parameter gives the peak residual, in units of mJy/beam.

**Pol\_Flux**

The integrated linearly polarized flux density (sqrt{Q2 \+ U2}) of the radio
source, in milliJanskies (mJy). A bias correction has been subtracted from the
measured value which can sometimes cause (unphysical) negative values.
A complete discussion of this issue is given in Section 5.2.6 of the NVSS
paper by Condon et al. (1998, AJ, 115, 1693).

**Pol\_Flux\_Error**

The rms uncertainty in the integrated linearly polarized flux density, in
milliJanskies (mJy).

**Pol\_Angle**

The position angle of the "E" vector of the linear polarization on the sky,
if the source was detected (1 sigma) in linear polarization, in degrees.

**Pol\_Angle\_Error**

The rms uncertainty in the linear polarization angle, in degrees.

**Field\_Name**

The name of the original survey image field from which the component was
derived.

**X\_Pixel**

The X position (in the RA direction) of the pixel where the radio source was
located in the original survey image field.

**Y\_Pixel**

The Y position (in the Declination direction) of the pixel where the radio
source was located in the original survey image field.

* * *

### Contact Person

Questions regarding the NVSS database table can be addressed to the
[HEASARC Help Desk](https://heasarc.gsfc.nasa.gov/cgi-bin/Feedback?selected=heasarc).

* * *

_Page Author:_ [Browse Software Development Team](https://heasarc.gsfc.nasa.gov/cgi-bin/Feedback?selected=w3browse)

_Last Modified:_ Monday, 16-Sep-2024 17:32:27 EDT

* * *

```

```