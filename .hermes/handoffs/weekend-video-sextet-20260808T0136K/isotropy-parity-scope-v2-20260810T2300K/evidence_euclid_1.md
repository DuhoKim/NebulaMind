URL: https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html

### Navigation

- [index](https://euclid.esac.esa.int/dr/q1/dpdd/genindex.html "General Index")
- [next](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html "Final Catalog Product") \|
- [previous](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html "MER Morphology Cookbook") \|
- [EUCL-EC-ICD-8-001 Data Product Description v2.0 (DM 10.0.4 - FDM 10.0.4 - EDEN 3.1\\
) documentation](https://euclid.esac.esa.int/dr/q1/dpdd/index.html) »
- [MER Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merindex.html) »
- [Background-Subtracted Mosaic Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html)

# Background-Subtracted Mosaic Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#background-subtracted-mosaic-product "Permalink to this heading")

## Data Product Name [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#data-product-name "Permalink to this heading")

DpdMerBksMosaic

## Data Product Custodian [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#data-product-custodian "Permalink to this heading")

MER

## Name of the Schema File [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#name-of-the-schema-file "Permalink to this heading")

[euc-mer-BksMosaic.xsd](https://gitlab.euclid-sgs.uk/ST-DM/ST_DataModel/-/blob/10.0.4/ST_DM_Schema/auxdir/ST_DM_Schema/dpd/mer/euc-mer-BksMosaic.xsd)

## Last Edited for DPDD Version [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#last-edited-for-dpdd-version "Permalink to this heading")

2.0

## Processing Elements Creating / Updating / Using the Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#processing-elements-creating-updating-using-the-product "Permalink to this heading")

**Creators:**

- MER\_Background

- MER\_CatalogPsfCalculation

- MER\_Compression


**Consumers:**

- MER\_Detection

- MER\_CatalogPsfCalculation

- MER\_PsfExtraction

- MER\_LowResPsfExtraction

- MER\_Kernel

- MER\_Morphology

- MER\_Photometry

- MER\_CatalogAssembly

- MER\_Compression

- MER\_MorphoFitting

- MER\_Validation


## Processing Function Using the Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#processing-function-using-the-product "Permalink to this heading")

MER, SIR, SHE

## Proposed for Inclusion in EAS/SAS [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#proposed-for-inclusion-in-eas-sas "Permalink to this heading")

This product is proposed for inclusion in the SAS: yes.

These products combine all the imaging data that overlap the
MER tiles, so they will be very useful for any scientific
studies that require image data.

## Data Product Elements [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#data-product-elements "Permalink to this heading")

Header:

object of type sys:genericHeader

Data:

object of type mer:merBksMosaic

QualityFlags:

object of type dqc:sqfDpdMerBksMosaic

Parameters:

object of type ppr:genericKeyValueParameters

## Detailed Description of the Data Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#detailed-description-of-the-data-product "Permalink to this heading")

This product is the result of applying the MER mosaicing and
MER background subtraction [Processing Element](https://euclid.esac.esa.int/dr/q1/dpdd/acronyms.html#term-Processing-Element) s to the
[VIS calibrated quad frames](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#viscalibratedquadframe), the
[NIR calibrated frames](https://euclid.esac.esa.int/dr/q1/dpdd/nirdpd/dpcards/nir_calibratedframe.html#nircalibratedframe), and the
EXT stacked frames.

MER mosaics are built using the MER tile outer spatial
footprint as a reference, and share the same field of view and pixel scale
(0.1’’ x 0.1’’) for all bands. Their size is typically 32’ x 32’ for WIDE tiles,
and 17’ x 17’ for DEEP tiles.

Before coaddition, the background models calculated in the VIS and NIR
pipelines are subtracted to the input images. The EXT stacked frames habe been
already background-subtracted and the MER pipeline just rebins them to the
target 0.1’’ x 0.1’’ pixel size. These background models are not propagated
by the MER pipeline and cannot be added again to the MER mosaics.

A second background subtraction step is applied in the MER pipeline to remove
any remaining background in the mosaiced images. The background model
calculated in this step is stored in the
[background FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-background-fits).

MER receives the Point Spread Functions (PSFs) measured by the VIS, NIR and
EXT pipelines and propagates them to the MER mosaic grid to calculate a
different PSF stamp for each individual source and band. The propagated PSF
stamps are stored in the mosaic [PSF FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-psf-fits).

The imaging and rms data have, depending on the provenience, different units
with:

- VIS in \[ADU/sec\]

- NIR in \[electrons\]

- EXT in arbitrary units


In all cases, image units can be translated to physical units using the
mosaic Zero Point and the well known formula:

(9) [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#equation-mag-ab-equ-1 "Permalink to this equation")mAB=−2.5×log10⁡(image\_value)+ZeroPoint

The main elements inside the MER background-subtracted mosaic product are:

- **Instrument**: The instrument name (VIS, NIR, DECAM) and the
telescope name (Euclid, NOAO, LSST).

- **Filter**: The filter name (e.g., VIS, NIR\_Y, NIR\_J, NIR\_H, DECAM\_g,
LSST\_u).

- **WCS**: The mosaic astrometric parameters (e.g., CTYPE1, CRVAL2, CRPIX1,
CD1\_1)

- **ZeroPoint**: The photometric reference zero point to convert the image untis
to AB-magnitudes.

- **ImgSpatialFootprint**: The mosaic spatial footprint.

- **TileIndex**: The MER tile index.

- **PatchIdList**: The sky patch ids associated to the product.

- **ObservationIdList**: List of unique IDs identifying the Euclid
observations that were used to generate the product.

- **CalblockIdList**: The calibration block ids associated to the
product.

- **CalblockVariantList**: The calibration block variants associated to the
product.

- **ProcessingMode**: The MER pipeline processing mode (e.g. WIDE, DEEP) used to
generate the product.

- **ReferenceObservationDateTime**: Reference observation date time for GAIA
proper motion correction (only applicable to Euclid observations).

- **FirstObservationDateTime**: Observation date time of the first Euclid
observation used to generate the product.

- **LastObservationDateTime**: Observation date time of the last Euclid
observation used to generate the product.

- [DataStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-image-fits): Element that links to a FITS file
containing the mosaic signal data set.

- [RmsStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-rms-fits): Element that links to a FITS file
containing the mosaic rms data set.

- [FlagStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-flag-fits): Element that links to a FITS file
containing the mosaic flag data set.

- [PsfModelStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-psf-fits): Element that links to a FITS
file containing the mosaic catalog PSF.

- [FilterTransmissionStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-filter-transmission-fits):
Element that links to a FITS file containing the mosaic average filter
transmission wavelength data set.

- [LayersStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-layers-fits): Element that links to a FITS
file containing the mosaic input layers information (only provided for the
Euclid bands).

- [BrightStarMasksStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-bright-star-masks-json): Element that links
to a json file containing the mosaic bright star spatial masks.

- [BackgroundStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-background-fits): Element that links to
a FITS file containing the subtracted background model.

- [QualityParams](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-image-quality-parameters): The mosaic image
quality parameters.

- [BackgroundQualityParams](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-background-quality-parameters): The
mosaic background quality parameters.


### Image FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#image-fits-file "Permalink to this heading")

This FITS file contains the background-subtracted mosaic image.

PRIMARY extension header keywords:

| **HDU** _PRIMARY_: header |
| --- |
|  | **Name** | **Description** | **Value** |
| Keywords | AUTHOR | Who ran the software (Swarp keyword) | string |
| BITPIX | array data type | integer |
| CD1\_1 | Linear projection matrix | double |
| CD1\_2 | Linear projection matrix | double |
| CD2\_1 | Linear projection matrix | double |
| CD2\_2 | Linear projection matrix | double |
| CENTERT1 | CENTER\_TYPE config parameter (Swarp keyword) | string |
| CENTERT2 | CENTER\_TYPE config parameter (Swarp keyword) | string |
| COMBINET | COMBINE\_TYPE config parameter for SWarp (Swarp keyword) | string |
| CRPIX1 | Reference pixel on this axis | double |
| CRPIX2 | Reference pixel on this axis | double |
| CRVAL1 | World coordinate on this axis | double |
| CRVAL2 | World coordinate on this axis | double |
| CTYPE1 | WCS projection type for this axis | string |
| CTYPE2 | WCS projection type for this axis | string |
| CUNIT1 | Axis unit | string |
| CUNIT2 | Axis unit | string |
| DATASETR | The pipeline data set release | string |
| DATE | When it was started (GMT) (Swarp keyword) | string |
| EQUINOX | Mean equinox | double |
| FILTER | The filter name | string |
| MAGZERO | AB zeropoint | double |
| NAXIS | number of array dimensions | integer |
| NAXIS1 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| NAXIS2 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| ORIGIN | Where it was done (Swarp keyword) | string |
| PIPDEFID | The pipeline definition id | string |
| PPLANID | The parent plan id | string |
| PPOID | The pipeline processing order id | string |
| PSCALET1 | PIXELSCALE\_TYPE config parameter (Swarp keyword) | string |
| PSCALET2 | PIXELSCALE\_TYPE config parameter (Swarp keyword) | string |
| PSWNAME | The pipeline software name | string |
| PSWREL | The pipeline software release | string |
| RADESYS | Astrometric system | string |
| RESAMPT1 | RESAMPLING\_TYPE config parameter (Swarp keyword) | string |
| RESAMPT2 | RESAMPLING\_TYPE config parameter (Swarp keyword) | string |
| SIMPLE | conforms to FITS standard | logical |
| SOFTAUTH | Maintainer of the software (Swarp keyword) | string |
| SOFTDATE | Release date of the software (Swarp keyword) | string |
| SOFTINST | Institute (Swarp keyword) | string |
| SOFTNAME | The software that processed those data (Swarp keyword) | string |
| SOFTVERS | Version of the software (Swarp keyword) | string |

### RMS FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#rms-fits-file "Permalink to this heading")

This FITS file contains the propagated rms associated to the mosaic. Note that
the VIS and NIR rms values contain a Poisson noise contribution that could be
significant for bright sources, while the EXT rms values currently do not
include this contribution.

PRIMARY extension header keywords:

| **HDU** _PRIMARY_: header |
| --- |
|  | **Name** | **Description** | **Value** |
| Keywords | AUTHOR | Who ran the software (Swarp keyword) | string |
| BITPIX | array data type | integer |
| CD1\_1 | Linear projection matrix | double |
| CD1\_2 | Linear projection matrix | double |
| CD2\_1 | Linear projection matrix | double |
| CD2\_2 | Linear projection matrix | double |
| CENTERT1 | CENTER\_TYPE config parameter (Swarp keyword) | string |
| CENTERT2 | CENTER\_TYPE config parameter (Swarp keyword) | string |
| COMBINET | COMBINE\_TYPE config parameter for SWarp (Swarp keyword) | string |
| CRPIX1 | Reference pixel on this axis | double |
| CRPIX2 | Reference pixel on this axis | double |
| CRVAL1 | World coordinate on this axis | double |
| CRVAL2 | World coordinate on this axis | double |
| CTYPE1 | WCS projection type for this axis | string |
| CTYPE2 | WCS projection type for this axis | string |
| CUNIT1 | Axis unit | string |
| CUNIT2 | Axis unit | string |
| DATASETR | The pipeline data set release | string |
| DATE | When it was started (GMT) (Swarp keyword) | string |
| EQUINOX | Mean equinox | double |
| FILTER | The filter name | string |
| MAGZERO | AB zeropoint | double |
| NAXIS | number of array dimensions | integer |
| NAXIS1 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| NAXIS2 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| ORIGIN | Where it was done (Swarp keyword) | string |
| PIPDEFID | The pipeline definition id | string |
| PPLANID | The parent plan id | string |
| PPOID | The pipeline processing order id | string |
| PSCALET1 | PIXELSCALE\_TYPE config parameter (Swarp keyword) | string |
| PSCALET2 | PIXELSCALE\_TYPE config parameter (Swarp keyword) | string |
| PSWNAME | The pipeline software name | string |
| PSWREL | The pipeline software release | string |
| RADESYS | Astrometric system | string |
| RESAMPT1 | RESAMPLING\_TYPE config parameter (Swarp keyword) | string |
| RESAMPT2 | RESAMPLING\_TYPE config parameter (Swarp keyword) | string |
| SIMPLE | conforms to FITS standard | logical |
| SOFTAUTH | Maintainer of the software (Swarp keyword) | string |
| SOFTDATE | Release date of the software (Swarp keyword) | string |
| SOFTINST | Institute (Swarp keyword) | string |
| SOFTNAME | The software that processed those data (Swarp keyword) | string |
| SOFTVERS | Version of the software (Swarp keyword) | string |

### Flag FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#flag-fits-file "Permalink to this heading")

MER propagates the image bit flags from their input products, and these products
can have different flag definitions. That means that the MER
image bit flag values will have a different meaning depending on the filter
assotiated to the mosaic. Read the
[VIS calibrated quad frame](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#viscalibratedquadframe),
[NIR calibrated frame](https://euclid.esac.esa.int/dr/q1/dpdd/nirdpd/dpcards/nir_calibratedframe.html#nircalibratedframe), and
EXT stacked frame product documentation for more
details about their specific image flag values.

Flags are propagated using an OR operation: it is enough that one of the input
images had the flag switched on at the mosaic pixel position, to switch on
the mosaic bit flag at that position.

PRIMARY extension header keywords:

| **HDU** _PRIMARY_: header |
| --- |
|  | **Name** | **Description** | **Value** |
| Keywords | AUTHOR | Who ran the software (Swarp keyword) | string |
| BITPIX | array data type | integer |
| CD1\_1 | Linear projection matrix | double |
| CD1\_2 | Linear projection matrix | double |
| CD2\_1 | Linear projection matrix | double |
| CD2\_2 | Linear projection matrix | double |
| CENTERT1 | CENTER\_TYPE config parameter (Swarp keyword) | string |
| CENTERT2 | CENTER\_TYPE config parameter (Swarp keyword) | string |
| COMBINET | COMBINE\_TYPE config parameter for SWarp (Swarp keyword) | string |
| CRPIX1 | Reference pixel on this axis | double |
| CRPIX2 | Reference pixel on this axis | double |
| CRVAL1 | World coordinate on this axis | double |
| CRVAL2 | World coordinate on this axis | double |
| CTYPE1 | WCS projection type for this axis | string |
| CTYPE2 | WCS projection type for this axis | string |
| CUNIT1 | Axis unit | string |
| CUNIT2 | Axis unit | string |
| DATASETR | The pipeline data set release | string |
| DATE | When it was started (GMT) (Swarp keyword) | string |
| EQUINOX | Mean equinox | double |
| EXTEND | This file may contain FITS extensions | logical |
| FILTER | The filter name | string |
| NAXIS | number of array dimensions | integer |
| NAXIS1 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| NAXIS2 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| ORIGIN | Where it was done (Swarp keyword) | string |
| PIPDEFID | The pipeline definition id | string |
| PPLANID | The parent plan id | string |
| PPOID | The pipeline processing order id | string |
| PSCALET1 | PIXELSCALE\_TYPE config parameter (Swarp keyword) | string |
| PSCALET2 | PIXELSCALE\_TYPE config parameter (Swarp keyword) | string |
| PSWNAME | The pipeline software name | string |
| PSWREL | The pipeline software release | string |
| RADESYS | Astrometric system | string |
| RESAMPT1 | RESAMPLING\_TYPE config parameter (Swarp keyword) | string |
| RESAMPT2 | RESAMPLING\_TYPE config parameter (Swarp keyword) | string |
| SIMPLE | conforms to FITS standard | logical |
| SOFTAUTH | Maintainer of the software (Swarp keyword) | string |
| SOFTDATE | Release date of the software (Swarp keyword) | string |
| SOFTINST | Institute (Swarp keyword) | string |
| SOFTNAME | The software that processed those data (Swarp keyword) | string |
| SOFTVERS | Version of the software (Swarp keyword) | string |

### PSF FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#psf-fits-file "Permalink to this heading")

This FITS file stores the propagated PSF stamps for most of the sources
in the [MER final catalog](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#merfinalcatalog).

The file consists of an image extension with all the PSF stamps distributed on a
regular grid, and a table extension with the PSF stamps coordinates (`RA`,
`Dec`), their central pixel position on the image extention (`x_center`,
`y_center`) and on the mosaic image (`x`, `y`). The stamp size in pixel
units, `STMPSIZE`, is stored in the header of the PSF image extension.

PRIMARY extension header keywords:

| **HDU** _PRIMARY_: header |
| --- |
|  | **Name** | **Description** | **Value** |
| Keywords | BITPIX | array data type | integer |
| EXTEND |  | logical |
| NAXIS | number of array dimensions | integer |
| SIMPLE | conforms to FITS standard | logical |

PSF image extension header keywords:

Stamps information table columns:

| **Catalog**: 7 columns table |
| --- |
| **Name** | **Description** | **Unit** | **Format** |
| x\_center |  | pix | FITS _D_ |
| y\_center |  | pix | FITS _D_ |
| x |  | pix | FITS _D_ |
| y |  | pix | FITS _D_ |
| RA |  | deg | FITS _D_ |
| Dec |  | deg | FITS _D_ |
| FWHM |  | arcsec | FITS _D_ |

### Filter transmission FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#filter-transmission-fits-file "Permalink to this heading")

This FITS file contains the average filter transmission wavelength for each
pixel in the mosaic.

PRIMARY extension header keywords:

| **HDU** _PRIMARY_: header |
| --- |
|  | **Name** | **Description** | **Value** |
| Keywords | AUTHOR | Who ran the software (Swarp keyword) | string |
| BITPIX | array data type | integer |
| CD1\_1 | Linear projection matrix | double |
| CD1\_2 | Linear projection matrix | double |
| CD2\_1 | Linear projection matrix | double |
| CD2\_2 | Linear projection matrix | double |
| CENTERT1 | CENTER\_TYPE config parameter (Swarp keyword) | string |
| CENTERT2 | CENTER\_TYPE config parameter (Swarp keyword) | string |
| COMBINET | COMBINE\_TYPE config parameter for SWarp (Swarp keyword) | string |
| CRPIX1 | Reference pixel on this axis | double |
| CRPIX2 | Reference pixel on this axis | double |
| CRVAL1 | World coordinate on this axis | double |
| CRVAL2 | World coordinate on this axis | double |
| CTYPE1 | WCS projection type for this axis | string |
| CTYPE2 | WCS projection type for this axis | string |
| CUNIT1 | Axis unit | string |
| CUNIT2 | Axis unit | string |
| DATASETR | The pipeline data set release | string |
| DATE | When it was started (GMT) (Swarp keyword) | string |
| EQUINOX | Mean equinox | double |
| FILTER | The filter name | string |
| NAXIS | number of array dimensions | integer |
| NAXIS1 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| NAXIS2 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| ORIGIN | Where it was done (Swarp keyword) | string |
| PIPDEFID | The pipeline definition id | string |
| PPLANID | The parent plan id | string |
| PPOID | The pipeline processing order id | string |
| PSCALET1 | PIXELSCALE\_TYPE config parameter (Swarp keyword) | string |
| PSCALET2 | PIXELSCALE\_TYPE config parameter (Swarp keyword) | string |
| PSWNAME | The pipeline software name | string |
| PSWREL | The pipeline software release | string |
| RADESYS | Astrometric system | string |
| RESAMPT1 | RESAMPLING\_TYPE config parameter (Swarp keyword) | string |
| RESAMPT2 | RESAMPLING\_TYPE config parameter (Swarp keyword) | string |
| SIMPLE | conforms to FITS standard | logical |
| SOFTAUTH | Maintainer of the software (Swarp keyword) | string |
| SOFTDATE | Release date of the software (Swarp keyword) | string |
| SOFTINST | Institute (Swarp keyword) | string |
| SOFTNAME | The software that processed those data (Swarp keyword) | string |
| SOFTVERS | Version of the software (Swarp keyword) | string |

### Layers FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#layers-fits-file "Permalink to this heading")

This FITS file stores relevant information (exposure time, observation date,
spatial footprint) about all the VIS and NIR input images that contributed to
the mosaic.

PRIMARY extension header keywords:

| **HDU** _PRIMARY_: header |
| --- |
|  | **Name** | **Description** | **Value** |
| Keywords | BITPIX | array data type | integer |
| EXTEND | This file may contain FITS extensions | logical |
| NAXIS | number of array dimensions | integer |
| SIMPLE | conforms to FITS standard | logical |

Table columns:

| **Catalog**: 8 columns table |
| --- |
| **Name** | **Description** | **Unit** | **Format** |
| CALIB\_IMAGE | Calibrated image file name | NA | FITS _80A_ |
| EXTNAME | Calibrated image extension name | NA | FITS _15A_ |
| EXPTIME | Exposure time | s | FITS _1E_ |
| POLYGON | Detector or quadrand spatial polygon | rad | FITS _8D_ |
| ALPHA | Alpha angle | NA | FITS _1E_ |
| BETA | Beta angle | NA | FITS _1E_ |
| SAA | Solar Aspect Angle | NA | FITS _1E_ |
| MJD-OBS | Instrument sequence start time in MJD | d | FITS _1E_ |

### Bright star masks json file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#bright-star-masks-json-file "Permalink to this heading")

File containing the Gaia bright star masks point (RA, Dec) coordinates.

### Background FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#background-fits-file "Permalink to this heading")

FITS file containing the background model calculated in the MER background
subtraction step.

This background has been subtracted to the mosaic
[image FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#mer-mosaic-image-fits).

PRIMARY extension header keywords:

| **HDU** _PRIMARY_: header |
| --- |
|  | **Name** | **Description** | **Value** |
| Keywords | BITPIX | array data type | integer |
| CD1\_1 | Linear projection matrix | double |
| CD1\_2 | Linear projection matrix | double |
| CD2\_1 | Linear projection matrix | double |
| CD2\_2 | Linear projection matrix | double |
| CRPIX1 | Reference pixel on this axis | double |
| CRPIX2 | Reference pixel on this axis | double |
| CRVAL1 | World coordinate on this axis | double |
| CRVAL2 | World coordinate on this axis | double |
| CTYPE1 | WCS projection type for this axis | string |
| CTYPE2 | WCS projection type for this axis | string |
| CUNIT1 | Axis unit | string |
| CUNIT2 | Axis unit | string |
| DATASETR | The pipeline data set release | string |
| EQUINOX | Mean equinox | double |
| EXTEND | This file may contain FITS extensions | logical |
| FILTER | The filter name | string |
| NAXIS | number of array dimensions | integer |
| NAXIS1 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| NAXIS2 | NUMBER OF ELEMENTS ALONG THIS AXIS | integer |
| PIPDEFID | The pipeline definition id | string |
| PPLANID | The parent plan id | string |
| PPOID | The pipeline processing order id | string |
| PSWNAME | The pipeline software name | string |
| PSWREL | The pipeline software release | string |
| RADESYS | Astrometric system | string |
| SIMPLE | conforms to FITS standard | logical |

### Image quality parameters [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#image-quality-parameters "Permalink to this heading")

The following list of quality parameters is calculated for each MER mosaic
image. Their values can be used to select an specific subset of
background-subtracted mosaics, to study global trends, or to detect potencial
problems in the MER pipeline or its input products.

| Quality parameter | Descriptiom |
| --- | --- |
| Mean | Average image level (mean of all image pixel values) |
| Median | Median image level (estimated median of all image pixel values) |
| StDev | Sample standard deviation of the image pixel values |
| Min | Minimum image pixel value |
| Max | Maximum image pixel value |
| MaskedPixelFraction | The fraction of masked pixels |
| CoverageFraction | The fraction of the image covered with data |

### Background quality parameters [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html\#background-quality-parameters "Permalink to this heading")

The following list of quality parameters is calculated for each MER
mosaic backgroun map.

| Quality parameter | Descriptiom |
| --- | --- |
| Mean | Average background level (mean of all background pixel values) |
| Median | Median background level (estimated median of all background pixel values) |
| StDev | Sample standard deviation of the background pixel values |
| Min | Minimum background pixel value |
| Max | Maximum background pixel value |

### [Table of Contents](https://euclid.esac.esa.int/dr/q1/dpdd/index.html)

- [Background-Subtracted Mosaic Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#)
  - [Data Product Name](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#data-product-name)
  - [Data Product Custodian](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#data-product-custodian)
  - [Name of the Schema File](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#name-of-the-schema-file)
  - [Last Edited for DPDD Version](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#last-edited-for-dpdd-version)
  - [Processing Elements Creating / Updating / Using the Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#processing-elements-creating-updating-using-the-product)
  - [Processing Function Using the Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#processing-function-using-the-product)
  - [Proposed for Inclusion in EAS/SAS](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#proposed-for-inclusion-in-eas-sas)
  - [Data Product Elements](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#data-product-elements)
  - [Detailed Description of the Data Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#detailed-description-of-the-data-product)
    - [Image FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#image-fits-file)
    - [RMS FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#rms-fits-file)
    - [Flag FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#flag-fits-file)
    - [PSF FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#psf-fits-file)
    - [Filter transmission FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#filter-transmission-fits-file)
    - [Layers FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#layers-fits-file)
    - [Bright star masks json file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#bright-star-masks-json-file)
    - [Background FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#background-fits-file)
    - [Image quality parameters](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#image-quality-parameters)
    - [Background quality parameters](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html#background-quality-parameters)

#### Previous topic

[MER Morphology Cookbook](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html "previous chapter")

#### Next topic

[Final Catalog Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html "next chapter")

### This Page

- [Show Source](https://euclid.esac.esa.int/dr/q1/dpdd/_sources/merdpd/dpcards/mer_bksmosaic.rst.txt)

### Quick search

### Navigation

- [index](https://euclid.esac.esa.int/dr/q1/dpdd/genindex.html "General Index")
- [next](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html "Final Catalog Product") \|
- [previous](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html "MER Morphology Cookbook") \|
- [EUCL-EC-ICD-8-001 Data Product Description v2.0 (DM 10.0.4 - FDM 10.0.4 - EDEN 3.1\\
) documentation](https://euclid.esac.esa.int/dr/q1/dpdd/index.html) »
- [MER Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merindex.html) »
- [Background-Subtracted Mosaic Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html)
