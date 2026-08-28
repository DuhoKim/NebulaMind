URL: https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html

### Navigation

- [index](https://euclid.esac.esa.int/dr/q1/dpdd/genindex.html "General Index")
- [next](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_segmentationmap.html "Segmentation Map Product") \|
- [previous](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html "Background-Subtracted Mosaic Product") \|
- [EUCL-EC-ICD-8-001 Data Product Description v2.0 (DM 10.0.4 - FDM 10.0.4 - EDEN 3.1\\
) documentation](https://euclid.esac.esa.int/dr/q1/dpdd/index.html) »
- [MER Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merindex.html) »
- [Final Catalog Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html)

# Final Catalog Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#final-catalog-product "Permalink to this heading")

## Data Product Name [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#data-product-name "Permalink to this heading")

DpdMerFinalCatalog

## Data Product Custodian [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#data-product-custodian "Permalink to this heading")

MER

## Name of the Schema File [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#name-of-the-schema-file "Permalink to this heading")

[euc-mer-FinalCatalog.xsd](https://gitlab.euclid-sgs.uk/ST-DM/ST_DataModel/-/blob/10.0.4/ST_DM_Schema/auxdir/ST_DM_Schema/dpd/mer/euc-mer-FinalCatalog.xsd)

## Last Edited for DPDD Version [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#last-edited-for-dpdd-version "Permalink to this heading")

2.0

## Processing Elements Creating / Updating / Using the Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#processing-elements-creating-updating-using-the-product "Permalink to this heading")

**Creators:**

- MER\_CatalogAssembly

- MER\_Compression

- MER\_MorphoFitting


**Consumers:**

- MER\_QuickAnalysis

- MER\_Compression

- MER\_MorphoFitting

- MER\_Validation


## Processing Function Using the Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#processing-function-using-the-product "Permalink to this heading")

MER, SIR, PHZ, SHE, LE3

## Proposed for Inclusion in EAS/SAS [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#proposed-for-inclusion-in-eas-sas "Permalink to this heading")

This product is proposed for inclusion in the SAS: yes.

This is the main catalog produced by MER. It contains photometric and
morphological information for all detected sources.

## Data Product Elements [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#data-product-elements "Permalink to this heading")

Header:

object of type sys:genericHeader

Data:

object of type mer:merFinalCatalog

QualityFlags:

object of type dqc:sqfDpdMerFinalCatalog

Parameters:

object of type ppr:genericKeyValueParameters

## Detailed Description of the Data Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#detailed-description-of-the-data-product "Permalink to this heading")

Final merged catalog with photometric and morphological information. It contains
object positions, total fluxes, colors and some object characterization
parameters. This product is an output from the MER catalog assembly
[Processing Element](https://euclid.esac.esa.int/dr/q1/dpdd/acronyms.html#term-Processing-Element), and is used by the PHZ, SIR, SHE and LE3
[Processing Function](https://euclid.esac.esa.int/dr/q1/dpdd/acronyms.html#term-Processing-Function) s.

The catalog information is stored in several FITS files. The source coordinates
and the main photometry measurements are stored in the
[main catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-main-catalog-fits) inside the DataStorage
element. Morphological parameters are stored in the
[morphology catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-morphology-catalog-fits)
inside the MorphologyCatalogStorage element. Some DEEP regions could
contain imaging data from additional EXT filters. In those cases the additional
EXT photometry measurements are stored in the
[deep-field photomety catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-deep-catalog-fits) inside the
DeepFieldPhotometryCatalogStorage element.

Specific information about the various MER photometric and morphological
measurements and their usage can be found in the
[MER photometry cookbook](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merphotometrycookbook.html#merphotometrycookbook) and the
[MER morphology cookbook](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#mermorphologycookbook).

Euclid sources can be uniquely identified by their `OBJECT_ID`. This id is
a signed integer that combines the source right ascension (RA) and declination
(Dec) coordinates using the following equation:

(10) [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#equation-object-id-equ "Permalink to this equation")OBJECT\_ID=sign(Dec)×(int(RA×107)×109+int(abs(Dec)×107))

One can see that sources with negative declination have negative `OBJECT_ID`
values. In addition to that, it is very likely that the same source will have
different `OBJECT_ID` values in different Euclid data releases, because it
has been detected at a slightly different spatial position due to changes
in the pipeline.

MER products coverage is based on MER tiles. The MER final
catalog contains only sources within the MER tile core area, ensuring that there
are no duplicates between adjacent tiles. The tile index associated to a given
source in the catalog can be retrieved in two different ways:

- Reading the `TILE_INDEX` header keyword from
[main catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-main-catalog-fits).

- From the `SEGMENTATION_MAP_ID` column value, via the following equation:

(11) [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#equation-tile-index-equ "Permalink to this equation")TILE\_INDEX=floor(SEGMENTATION\_MAP\_ID106)


The main elements inside the MER final catalog product are:

- **SpatialCoverage**: The catalog spatial coverage.

- **SpectralCoverage**: The catalog spectral coverage with a list of the filters
that were used to produce the catalog (e.g., VIS, NIR\_Y, NIR\_J, NIR\_H,
DECAM\_g, LSST\_g).

- **TileIndex**: The MER tile index.

- **PatchIdList**: The sky patch ids associated to the product.

- **ObservationIdList**: List of unique IDs identifying the Euclid
observations that were used to generate the product.

- **CalblockIdList**: The calibration block ids associated to the product.

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

- [DataStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-main-catalog-fits): Element that links to a FITS file
containing the main catalog data set.

- [MorphologyCatalogStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-morphology-catalog-fits): Element that
links to a FITS file containing the morphology catalog data set.

- [CutoutsCatalogStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-cutouts-catalog-fits): Element that links to
a FITS file containing the source cutouts catalog data set.

- [DeepFieldPhotometryCatalogStorage](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-deep-catalog-fits):
Element that links to a FITS file containing the source DEEP field photometry
catalog data set. This catalog is only produced for DEEP observations.

- [QualityParams](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-catalog-quality-parameters): The catalog quality
parameters.


### Main catalog FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#main-catalog-fits-file "Permalink to this heading")

FITS table storing the official Euclid source ID, i.e. the `OBJECT_ID`, the
source coordinates, quality flags and all the information related to the
photometry measurements.

Table columns:

| **Catalog**: 469 columns table |
| --- |
| **Name** | **Description** | **Unit** | **Format** |
| OBJECT\_ID | Euclid unique source identifier | NA | FITS _K_ |
| RIGHT\_ASCENSION | Source barycenter RA coordinate (SExtractor ALPHA\_J2000) decimal degrees | deg | FITS _D_ |
| DECLINATION | Source barycenter DEC coordinate (SExtractor DELTA\_J2000) decimal degrees | deg | FITS _D_ |
| RIGHT\_ASCENSION\_PSF\_FITTING | Source RA coordinate derived by the PSF-fitting photometry method | deg | FITS _D_ |
| DECLINATION\_PSF\_FITTING | Source DEC coordinate derived by the PSF-fitting photometry method | deg | FITS _D_ |
| SEGMENTATION\_MAP\_ID | Source ID in the associated segmentation map | NA | FITS _K_ |
| VIS\_DET | Flag to indicate if the source is detected in the VIS mosaic (1) or is only detected in the NIR mosaic (0) | NA | FITS _I_ |
| FLUX\_VIS\_1FWHM\_APER | VIS band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_VIS\_2FWHM\_APER | VIS band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_VIS\_3FWHM\_APER | VIS band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_VIS\_4FWHM\_APER | VIS band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Y\_1FWHM\_APER | NIR Y band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Y\_2FWHM\_APER | NIR Y band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Y\_3FWHM\_APER | NIR Y band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Y\_4FWHM\_APER | NIR Y band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_J\_1FWHM\_APER | NIR J band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_J\_2FWHM\_APER | NIR J band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_J\_3FWHM\_APER | NIR J band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_J\_4FWHM\_APER | NIR J band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_H\_1FWHM\_APER | NIR H band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_H\_2FWHM\_APER | NIR H band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_H\_3FWHM\_APER | NIR H band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_H\_4FWHM\_APER | NIR H band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_NIR\_STACK\_1FWHM\_APER | NIR stack band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_NIR\_STACK\_2FWHM\_APER | NIR stack band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_NIR\_STACK\_3FWHM\_APER | NIR stack band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_NIR\_STACK\_4FWHM\_APER | NIR stack band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_DECAM\_1FWHM\_APER | Uext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_DECAM\_2FWHM\_APER | Uext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_DECAM\_3FWHM\_APER | Uext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_DECAM\_4FWHM\_APER | Uext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_DECAM\_1FWHM\_APER | Gext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_DECAM\_2FWHM\_APER | Gext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_DECAM\_3FWHM\_APER | Gext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_DECAM\_4FWHM\_APER | Gext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_DECAM\_1FWHM\_APER | Rext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_DECAM\_2FWHM\_APER | Rext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_DECAM\_3FWHM\_APER | Rext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_DECAM\_4FWHM\_APER | Rext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_DECAM\_1FWHM\_APER | Iext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_DECAM\_2FWHM\_APER | Iext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_DECAM\_3FWHM\_APER | Iext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_DECAM\_4FWHM\_APER | Iext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_DECAM\_1FWHM\_APER | Zext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_DECAM\_2FWHM\_APER | Zext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_DECAM\_3FWHM\_APER | Zext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_DECAM\_4FWHM\_APER | Zext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_LSST\_1FWHM\_APER | Uext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_LSST\_2FWHM\_APER | Uext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_LSST\_3FWHM\_APER | Uext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_LSST\_4FWHM\_APER | Uext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_LSST\_1FWHM\_APER | Gext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_LSST\_2FWHM\_APER | Gext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_LSST\_3FWHM\_APER | Gext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_LSST\_4FWHM\_APER | Gext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_LSST\_1FWHM\_APER | Rext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_LSST\_2FWHM\_APER | Rext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_LSST\_3FWHM\_APER | Rext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_LSST\_4FWHM\_APER | Rext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_LSST\_1FWHM\_APER | Iext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_LSST\_2FWHM\_APER | Iext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_LSST\_3FWHM\_APER | Iext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_LSST\_4FWHM\_APER | Iext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_LSST\_1FWHM\_APER | Zext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_LSST\_2FWHM\_APER | Zext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_LSST\_3FWHM\_APER | Zext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_LSST\_4FWHM\_APER | Zext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_MEGACAM\_1FWHM\_APER | Uext Megacam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_MEGACAM\_2FWHM\_APER | Uext Megacam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_MEGACAM\_3FWHM\_APER | Uext Megacam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_U\_EXT\_MEGACAM\_4FWHM\_APER | Uext Megacam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_MEGACAM\_1FWHM\_APER | Rext Megacam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_MEGACAM\_2FWHM\_APER | Rext Megacam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_MEGACAM\_3FWHM\_APER | Rext Megacam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_R\_EXT\_MEGACAM\_4FWHM\_APER | Rext Megacam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_JPCAM\_1FWHM\_APER | Gext JPCAM band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_JPCAM\_2FWHM\_APER | Gext JPCAM band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_JPCAM\_3FWHM\_APER | Gext JPCAM band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_JPCAM\_4FWHM\_APER | Gext JPCAM band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_PANSTARRS\_1FWHM\_APER | Iext PS band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_PANSTARRS\_2FWHM\_APER | Iext PS band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_PANSTARRS\_3FWHM\_APER | Iext PS band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_I\_EXT\_PANSTARRS\_4FWHM\_APER | Iext PS band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_PANSTARRS\_1FWHM\_APER | Zext PS band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_PANSTARRS\_2FWHM\_APER | Zext PS band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_PANSTARRS\_3FWHM\_APER | Zext PS band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_PANSTARRS\_4FWHM\_APER | Zext PS band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_HSC\_1FWHM\_APER | Gext HSC band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_HSC\_2FWHM\_APER | Gext HSC band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_HSC\_3FWHM\_APER | Gext HSC band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_G\_EXT\_HSC\_4FWHM\_APER | Gext HSC band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_HSC\_1FWHM\_APER | Zext HSC band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_HSC\_2FWHM\_APER | Zext HSC band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_HSC\_3FWHM\_APER | Zext HSC band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_HSC\_4FWHM\_APER | Zext HSC band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUXERR\_VIS\_1FWHM\_APER | VIS band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_VIS\_2FWHM\_APER | VIS band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_VIS\_3FWHM\_APER | VIS band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_VIS\_4FWHM\_APER | VIS band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Y\_1FWHM\_APER | NIR Y band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Y\_2FWHM\_APER | NIR Y band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Y\_3FWHM\_APER | NIR Y band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Y\_4FWHM\_APER | NIR Y band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_J\_1FWHM\_APER | NIR J band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_J\_2FWHM\_APER | NIR J band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_J\_3FWHM\_APER | NIR J band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_J\_4FWHM\_APER | NIR J band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_H\_1FWHM\_APER | NIR H band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_H\_2FWHM\_APER | NIR H band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_H\_3FWHM\_APER | NIR H band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_H\_4FWHM\_APER | NIR H band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_NIR\_STACK\_1FWHM\_APER | NIR stack band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_NIR\_STACK\_2FWHM\_APER | NIR stack band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_NIR\_STACK\_3FWHM\_APER | NIR stack band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_NIR\_STACK\_4FWHM\_APER | NIR stack band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_DECAM\_1FWHM\_APER | Uext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_DECAM\_2FWHM\_APER | Uext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_DECAM\_3FWHM\_APER | Uext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_DECAM\_4FWHM\_APER | Uext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_DECAM\_1FWHM\_APER | Gext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_DECAM\_2FWHM\_APER | Gext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_DECAM\_3FWHM\_APER | Gext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_DECAM\_4FWHM\_APER | Gext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_DECAM\_1FWHM\_APER | Rext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_DECAM\_2FWHM\_APER | Rext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_DECAM\_3FWHM\_APER | Rext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_DECAM\_4FWHM\_APER | Rext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_DECAM\_1FWHM\_APER | Iext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_DECAM\_2FWHM\_APER | Iext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_DECAM\_3FWHM\_APER | Iext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_DECAM\_4FWHM\_APER | Iext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_DECAM\_1FWHM\_APER | Zext DECam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_DECAM\_2FWHM\_APER | Zext DECam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_DECAM\_3FWHM\_APER | Zext DECam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_DECAM\_4FWHM\_APER | Zext DECam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_LSST\_1FWHM\_APER | Uext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_LSST\_2FWHM\_APER | Uext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_LSST\_3FWHM\_APER | Uext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_LSST\_4FWHM\_APER | Uext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_LSST\_1FWHM\_APER | Gext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_LSST\_2FWHM\_APER | Gext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_LSST\_3FWHM\_APER | Gext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_LSST\_4FWHM\_APER | Gext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_LSST\_1FWHM\_APER | Rext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_LSST\_2FWHM\_APER | Rext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_LSST\_3FWHM\_APER | Rext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_LSST\_4FWHM\_APER | Rext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_LSST\_1FWHM\_APER | Iext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_LSST\_2FWHM\_APER | Iext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_LSST\_3FWHM\_APER | Iext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_LSST\_4FWHM\_APER | Iext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_LSST\_1FWHM\_APER | Zext LSST band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_LSST\_2FWHM\_APER | Zext LSST band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_LSST\_3FWHM\_APER | Zext LSST band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_LSST\_4FWHM\_APER | Zext LSST band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_MEGACAM\_1FWHM\_APER | Uext Megacam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_MEGACAM\_2FWHM\_APER | Uext Megacam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_MEGACAM\_3FWHM\_APER | Uext Megacam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_MEGACAM\_4FWHM\_APER | Uext Megacam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_MEGACAM\_1FWHM\_APER | Rext Megacam band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_MEGACAM\_2FWHM\_APER | Rext Megacam band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_MEGACAM\_3FWHM\_APER | Rext Megacam band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_MEGACAM\_4FWHM\_APER | Rext Megacam band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_JPCAM\_1FWHM\_APER | Gext JPCAM band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_JPCAM\_2FWHM\_APER | Gext JPCAM band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_JPCAM\_3FWHM\_APER | Gext JPCAM band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_JPCAM\_4FWHM\_APER | Gext JPCAM band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_PANSTARRS\_1FWHM\_APER | Iext PS band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_PANSTARRS\_2FWHM\_APER | Iext PS band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_PANSTARRS\_3FWHM\_APER | Iext PS band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_PANSTARRS\_4FWHM\_APER | Iext PS band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_PANSTARRS\_1FWHM\_APER | Zext PS band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_PANSTARRS\_2FWHM\_APER | Zext PS band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_PANSTARRS\_3FWHM\_APER | Zext PS band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_PANSTARRS\_4FWHM\_APER | Zext PS band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_HSC\_1FWHM\_APER | Gext HSC band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_HSC\_2FWHM\_APER | Gext HSC band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_HSC\_3FWHM\_APER | Gext HSC band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_HSC\_4FWHM\_APER | Gext HSC band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_HSC\_1FWHM\_APER | Zext HSC band source aperture photometry flux (1 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_HSC\_2FWHM\_APER | Zext HSC band source aperture photometry flux (2 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_HSC\_3FWHM\_APER | Zext HSC band source aperture photometry flux (3 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_HSC\_4FWHM\_APER | Zext HSC band source aperture photometry flux (4 FWHM diameter) on PSF-matched images error | uJy | FITS _E_ |
| FLUX\_Y\_TEMPLFIT | NIR Y band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_J\_TEMPLFIT | NIR J band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_H\_TEMPLFIT | NIR H band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_U\_EXT\_DECAM\_TEMPLFIT | Uext DECam band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_G\_EXT\_DECAM\_TEMPLFIT | Gext DECam band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_R\_EXT\_DECAM\_TEMPLFIT | Rext DECam band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_I\_EXT\_DECAM\_TEMPLFIT | Iext DECam band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_DECAM\_TEMPLFIT | Zext DECam band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_U\_EXT\_LSST\_TEMPLFIT | Uext LSST band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_G\_EXT\_LSST\_TEMPLFIT | Gext LSST band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_R\_EXT\_LSST\_TEMPLFIT | Rext LSST band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_I\_EXT\_LSST\_TEMPLFIT | Iext LSST band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_LSST\_TEMPLFIT | Zext LSST band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_U\_EXT\_MEGACAM\_TEMPLFIT | Uext Megacam band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_R\_EXT\_MEGACAM\_TEMPLFIT | Rext Megacam band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_G\_EXT\_JPCAM\_TEMPLFIT | Gext JPCAM band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_I\_EXT\_PANSTARRS\_TEMPLFIT | Iext PS band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_PANSTARRS\_TEMPLFIT | Zext PS band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_G\_EXT\_HSC\_TEMPLFIT | Gext HSC band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_HSC\_TEMPLFIT | Zext HSC band source template fitting flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_Y\_TEMPLFIT | NIR Y band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_J\_TEMPLFIT | NIR J band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_H\_TEMPLFIT | NIR H band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_DECAM\_TEMPLFIT | Uext DECam band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_DECAM\_TEMPLFIT | Gext DECam band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_DECAM\_TEMPLFIT | Rext DECam band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_DECAM\_TEMPLFIT | Iext DECam band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_DECAM\_TEMPLFIT | Zext DECam band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_LSST\_TEMPLFIT | Uext LSST band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_LSST\_TEMPLFIT | Gext LSST band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_LSST\_TEMPLFIT | Rext LSST band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_LSST\_TEMPLFIT | Iext LSST band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_LSST\_TEMPLFIT | Zext LSST band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_MEGACAM\_TEMPLFIT | Uext Megacam band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_MEGACAM\_TEMPLFIT | Rext Megacam band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_JPCAM\_TEMPLFIT | Gext JPCAM band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_PANSTARRS\_TEMPLFIT | Iext PS band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_PANSTARRS\_TEMPLFIT | Zext PS band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_HSC\_TEMPLFIT | Gext HSC band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_HSC\_TEMPLFIT | Zext HSC band source template fitting flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_Y\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to NIR Y band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_J\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to NIR J band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_H\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to NIR H band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_U\_EXT\_DECAM\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Uext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_G\_EXT\_DECAM\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Gext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_R\_EXT\_DECAM\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Rext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_I\_EXT\_DECAM\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Iext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_Z\_EXT\_DECAM\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Zext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_U\_EXT\_LSST\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Uext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_G\_EXT\_LSST\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Gext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_R\_EXT\_LSST\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Rext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_I\_EXT\_LSST\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Iext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_Z\_EXT\_LSST\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Zext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_U\_EXT\_MEGACAM\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Uext Megacam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_R\_EXT\_MEGACAM\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Rext Megacam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_G\_EXT\_JPCAM\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Gext JPCAM band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_I\_EXT\_PANSTARRS\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Iext PS band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_Z\_EXT\_PANSTARRS\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Zext PS band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_G\_EXT\_HSC\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Gext HSC band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_TO\_Z\_EXT\_HSC\_TEMPLFIT | VIS band source flux on a VIS image PSF-matched to Zext HSC band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_Y\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to NIR Y band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_J\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to NIR J bandr (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_H\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to NIR H band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_U\_EXT\_DECAM\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Uext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_G\_EXT\_DECAM\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Gext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_R\_EXT\_DECAM\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Rext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_I\_EXT\_DECAM\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Iext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_Z\_EXT\_DECAM\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Zext DECam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_U\_EXT\_LSST\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Uext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_G\_EXT\_LSST\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Gext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_R\_EXT\_LSST\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Rext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_I\_EXT\_LSST\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Iext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_Z\_EXT\_LSST\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Zext LSST band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_U\_EXT\_MEGACAM\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Uext Megacam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_R\_EXT\_MEGACAM\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Rext Megacam band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_G\_EXT\_JPCAM\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Gext JPCAM band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_I\_EXT\_PANSTARRS\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Iext PS band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_Z\_EXT\_PANSTARRS\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Zext PS band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_G\_EXT\_HSC\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Gext HSC band (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_TO\_Z\_EXT\_HSC\_TEMPLFIT | VIS band source flux error on a VIS image PSF-matched to Zext HSC band (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_VIS\_PSF | VIS band source PSF-fitting photometry flux (TPHOT measurement) | uJy | FITS _E_ |
| FLUXERR\_VIS\_PSF | VIS band source PSF-fitting photometry flux error (TPHOT measurement) | uJy | FITS _E_ |
| FLUX\_SEGMENTATION | VIS or NIR stack band source segmented area flux | uJy | FITS _E_ |
| FLUXERR\_SEGMENTATION | VIS or NIR stack band source total flux (Kron aperture) | uJy | FITS _E_ |
| FLUX\_DETECTION\_TOTAL | VIS or NIR stack band source total flux error (Kron aperture) | uJy | FITS _E_ |
| FLUXERR\_DETECTION\_TOTAL | VIS or NIR stack band source segmented area flux | uJy | FITS _E_ |
| FLUX\_VIS\_SERSIC | VIS band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_Y\_SERSIC | NIR Y band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_J\_SERSIC | NIR J band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_H\_SERSIC | NIR H band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_U\_EXT\_DECAM\_SERSIC | Uext DECam band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_G\_EXT\_DECAM\_SERSIC | Gext DECam band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_R\_EXT\_DECAM\_SERSIC | Rext DECam band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_I\_EXT\_DECAM\_SERSIC | Iext DECam band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_DECAM\_SERSIC | Zext DECam band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_U\_EXT\_LSST\_SERSIC | Uext LSST band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_G\_EXT\_LSST\_SERSIC | Gext LSST band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_R\_EXT\_LSST\_SERSIC | Rext LSST band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_I\_EXT\_LSST\_SERSIC | Iext LSST band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_LSST\_SERSIC | Zext LSST band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_U\_EXT\_MEGACAM\_SERSIC | Uext Megacam band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_R\_EXT\_MEGACAM\_SERSIC | Rext Megacam band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_G\_EXT\_JPCAM\_SERSIC | Gext JPCAM band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_I\_EXT\_PANSTARRS\_SERSIC | Iext PS band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_PANSTARRS\_SERSIC | Zext PS band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_G\_EXT\_HSC\_SERSIC | Gext HSC band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_HSC\_SERSIC | Zext HSC band source flux from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_VIS\_SERSIC | VIS band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Y\_SERSIC | NIR Y band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_J\_SERSIC | NIR J band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_H\_SERSIC | NIR H band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_DECAM\_SERSIC | Uext DECam band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_DECAM\_SERSIC | Gext DECam band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_DECAM\_SERSIC | Rext DECam band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_DECAM\_SERSIC | Iext DECam band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_DECAM\_SERSIC | Zext DECam band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_LSST\_SERSIC | Uext LSST band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_LSST\_SERSIC | Gext LSST band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_LSST\_SERSIC | Rext LSST band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_LSST\_SERSIC | Iext LSST band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_LSST\_SERSIC | Zext LSST band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_MEGACAM\_SERSIC | Uext Megacam band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_MEGACAM\_SERSIC | Rext Megacam band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_JPCAM\_SERSIC | Gext JPCAM band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_PANSTARRS\_SERSIC | Iext PS band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_PANSTARRS\_SERSIC | Zext PS band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_HSC\_SERSIC | Gext HSC band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_HSC\_SERSIC | Zext HSC band source flux error from the Sersic fit | uJy | FITS _E_ |
| FLUX\_VIS\_DISK\_SERSIC | VIS band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_Y\_DISK\_SERSIC | NIR Y band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_J\_DISK\_SERSIC | NIR J band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_H\_DISK\_SERSIC | NIR H band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_U\_EXT\_DECAM\_DISK\_SERSIC | Uext DECam band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_G\_EXT\_DECAM\_DISK\_SERSIC | Gext DECam band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_R\_EXT\_DECAM\_DISK\_SERSIC | Rext DECam band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_I\_EXT\_DECAM\_DISK\_SERSIC | Iext DECam band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_DECAM\_DISK\_SERSIC | Zext DECam band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_U\_EXT\_LSST\_DISK\_SERSIC | Uext LSST band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_G\_EXT\_LSST\_DISK\_SERSIC | Gext LSST band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_R\_EXT\_LSST\_DISK\_SERSIC | Rext LSST band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_I\_EXT\_LSST\_DISK\_SERSIC | Iext LSST band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_LSST\_DISK\_SERSIC | Zext LSST band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_U\_EXT\_MEGACAM\_DISK\_SERSIC | Uext Megacam band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_R\_EXT\_MEGACAM\_DISK\_SERSIC | Rext Megacam band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_G\_EXT\_JPCAM\_DISK\_SERSIC | Gext JPCAM band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_I\_EXT\_PANSTARRS\_DISK\_SERSIC | Iext PS band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_PANSTARRS\_DISK\_SERSIC | Zext PS band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_G\_EXT\_HSC\_DISK\_SERSIC | Gext HSC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_Z\_EXT\_HSC\_DISK\_SERSIC | Zext HSC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_VIS\_DISK\_SERSIC | VIS band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Y\_DISK\_SERSIC | NIR Y band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_J\_DISK\_SERSIC | NIR J band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_H\_DISK\_SERSIC | NIR H band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_DECAM\_DISK\_SERSIC | Uext DECam band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_DECAM\_DISK\_SERSIC | Gext DECam band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_DECAM\_DISK\_SERSIC | Rext DECam band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_DECAM\_DISK\_SERSIC | Iext DECam band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_DECAM\_DISK\_SERSIC | Zext DECam band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_LSST\_DISK\_SERSIC | Uext LSST band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_LSST\_DISK\_SERSIC | Gext LSST band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_LSST\_DISK\_SERSIC | Rext LSST band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_LSST\_DISK\_SERSIC | Iext LSST band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_LSST\_DISK\_SERSIC | Zext LSST band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_U\_EXT\_MEGACAM\_DISK\_SERSIC | Uext Megacam band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_MEGACAM\_DISK\_SERSIC | Rext Megacam band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_JPCAM\_DISK\_SERSIC | Gext JPCAM band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_PANSTARRS\_DISK\_SERSIC | Iext PS band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_PANSTARRS\_DISK\_SERSIC | Zext PS band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_G\_EXT\_HSC\_DISK\_SERSIC | Gext HSC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Z\_EXT\_HSC\_DISK\_SERSIC | Zext HSC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| SERSIC\_FRACT\_VIS\_DISK\_SERSIC | VIS band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_Y\_DISK\_SERSIC | NIR Y band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_J\_DISK\_SERSIC | NIR J band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_H\_DISK\_SERSIC | NIR H band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_U\_EXT\_DECAM\_DISK\_SERSIC | Uext DECam band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_G\_EXT\_DECAM\_DISK\_SERSIC | Gext DECam band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_R\_EXT\_DECAM\_DISK\_SERSIC | Rext DECam band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_I\_EXT\_DECAM\_DISK\_SERSIC | Iext DECam band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_Z\_EXT\_DECAM\_DISK\_SERSIC | Zext DECam band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_U\_EXT\_LSST\_DISK\_SERSIC | Uext LSST band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_G\_EXT\_LSST\_DISK\_SERSIC | Gext LSST band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_R\_EXT\_LSST\_DISK\_SERSIC | Rext LSST band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_I\_EXT\_LSST\_DISK\_SERSIC | Iext LSST band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_Z\_EXT\_LSST\_DISK\_SERSIC | Zext LSST band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_U\_EXT\_MEGACAM\_DISK\_SERSIC | Uext Megacam band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_R\_EXT\_MEGACAM\_DISK\_SERSIC | Rext Megacam band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_G\_EXT\_JPCAM\_DISK\_SERSIC | Gext JPCAM band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_I\_EXT\_PANSTARRS\_DISK\_SERSIC | Iext PS band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_Z\_EXT\_PANSTARRS\_DISK\_SERSIC | Zext PS band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_G\_EXT\_HSC\_DISK\_SERSIC | Gext HSC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_Z\_EXT\_HSC\_DISK\_SERSIC | Zext HSC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_VIS\_DISK\_SERSIC\_ERR | VIS band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_Y\_DISK\_SERSIC\_ERR | NIR Y band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_J\_DISK\_SERSIC\_ERR | NIR J band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_H\_DISK\_SERSIC\_ERR | NIR H band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_U\_EXT\_DECAM\_DISK\_SERSIC\_ERR | Uext DECam band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_G\_EXT\_DECAM\_DISK\_SERSIC\_ERR | Gext DECam band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_R\_EXT\_DECAM\_DISK\_SERSIC\_ERR | Rext DECam band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_I\_EXT\_DECAM\_DISK\_SERSIC\_ERR | Iext DECam band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_Z\_EXT\_DECAM\_DISK\_SERSIC\_ERR | Zext DECam band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_U\_EXT\_LSST\_DISK\_SERSIC\_ERR | Uext LSST band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_G\_EXT\_LSST\_DISK\_SERSIC\_ERR | Gext LSST band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_R\_EXT\_LSST\_DISK\_SERSIC\_ERR | Rext LSST band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_I\_EXT\_LSST\_DISK\_SERSIC\_ERR | Iext LSST band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_Z\_EXT\_LSST\_DISK\_SERSIC\_ERR | Zext LSST band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_U\_EXT\_MEGACAM\_DISK\_SERSIC\_ERR | Uext Megacam band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_R\_EXT\_MEGACAM\_DISK\_SERSIC\_ERR | Rext Megacam band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_G\_EXT\_JPCAM\_DISK\_SERSIC\_ERR | Gext JPCAM band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_I\_EXT\_PANSTARRS\_DISK\_SERSIC\_ERR | Iext PS band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_Z\_EXT\_PANSTARRS\_DISK\_SERSIC\_ERR | Zext PS band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_G\_EXT\_HSC\_DISK\_SERSIC\_ERR | Gext HSC band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_Z\_EXT\_HSC\_DISK\_SERSIC\_ERR | Zext HSC band Sersic fraction error | NA | FITS _E_ |
| FLAG\_VIS | Objects flag keeping track of the flagged pixels in the VIS flag image | NA | FITS _J_ |
| FLAG\_Y | Objects flag keeping track of the flagged pixels in the NIR Y flag image | NA | FITS _J_ |
| FLAG\_J | Objects flag keeping track of the flagged pixels in the NIR J flag image | NA | FITS _J_ |
| FLAG\_H | Objects flag keeping track of the flagged pixels in the NIR H flag image | NA | FITS _J_ |
| FLAG\_NIR\_STACK | Objects flag keeping track of the flagged pixels in the NIR stack flag image | NA | FITS _J_ |
| FLAG\_U\_EXT\_DECAM | Objects flag keeping track of the flagged pixels in the UextDECam flag image | NA | FITS _J_ |
| FLAG\_G\_EXT\_DECAM | Objects flag keeping track of the flagged pixels in the GextDECam flag image | NA | FITS _J_ |
| FLAG\_R\_EXT\_DECAM | Objects flag keeping track of the flagged pixels in the RextDECam flag image | NA | FITS _J_ |
| FLAG\_I\_EXT\_DECAM | Objects flag keeping track of the flagged pixels in the IextDECam flag image | NA | FITS _J_ |
| FLAG\_Z\_EXT\_DECAM | Objects flag keeping track of the flagged pixels in the ZextDECam flag image | NA | FITS _J_ |
| FLAG\_U\_EXT\_LSST | Objects flag keeping track of the flagged pixels in the Uext LSST flag image | NA | FITS _J_ |
| FLAG\_G\_EXT\_LSST | Objects flag keeping track of the flagged pixels in the Gext LSST flag image | NA | FITS _J_ |
| FLAG\_R\_EXT\_LSST | Objects flag keeping track of the flagged pixels in the Rext LSST flag image | NA | FITS _J_ |
| FLAG\_I\_EXT\_LSST | Objects flag keeping track of the flagged pixels in the Iext LSST flag image | NA | FITS _J_ |
| FLAG\_Z\_EXT\_LSST | Objects flag keeping track of the flagged pixels in the Zext LSST flag image | NA | FITS _J_ |
| FLAG\_U\_EXT\_MEGACAM | Objects flag keeping track of the flagged pixels in the Uext Megacam flag image | NA | FITS _J_ |
| FLAG\_R\_EXT\_MEGACAM | Objects flag keeping track of the flagged pixels in the Rext Megacam flag image | NA | FITS _J_ |
| FLAG\_G\_EXT\_JPCAM | Objects flag keeping track of the flagged pixels in the Gext JPCAM flag image | NA | FITS _J_ |
| FLAG\_I\_EXT\_PANSTARRS | Objects flag keeping track of the flagged pixels in the Iext PS flag image | NA | FITS _J_ |
| FLAG\_Z\_EXT\_PANSTARRS | Objects flag keeping track of the flagged pixels in the Zext PS flag image | NA | FITS _J_ |
| FLAG\_G\_EXT\_HSC | Objects flag keeping track of the flagged pixels in the Gext HSC flag image | NA | FITS _J_ |
| FLAG\_Z\_EXT\_HSC | Objects flag keeping track of the flagged pixels in the Zext HSC flag image | NA | FITS _J_ |
| AVG\_TRANS\_WAVE\_VIS | Average filter transmission curve wavelength for the VIS band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_Y | Average filter transmission curve wavelength for the NIR Y band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_J | Average filter transmission curve wavelength for the NIR J band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_H | Average filter transmission curve wavelength for the NIR H band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_U\_EXT\_DECAM | Average filter transmission curve wavelength for the DECam U band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_G\_EXT\_DECAM | Average filter transmission curve wavelength for the DECam G band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_R\_EXT\_DECAM | Average filter transmission curve wavelength for the DECam R band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_I\_EXT\_DECAM | Average filter transmission curve wavelength for the DECam I band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_Z\_EXT\_DECAM | Average filter transmission curve wavelength for the DECam Z band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_U\_EXT\_LSST | Average filter transmission curve wavelength for the LSST U band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_G\_EXT\_LSST | Average filter transmission curve wavelength for the LSST G band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_R\_EXT\_LSST | Average filter transmission curve wavelength for the LSST R band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_I\_EXT\_LSST | Average filter transmission curve wavelength for the LSST I band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_Z\_EXT\_LSST | Average filter transmission curve wavelength for the LSST Z band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_U\_EXT\_MEGACAM | Average filter transmission curve wavelength for the Megacam U band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_R\_EXT\_MEGACAM | Average filter transmission curve wavelength for the Megacam R band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_G\_EXT\_JPCAM | Average filter transmission curve wavelength for the JPCAM G band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_I\_EXT\_PANSTARRS | Average filter transmission curve wavelength for the PS I band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_Z\_EXT\_PANSTARRS | Average filter transmission curve wavelength for the PS Z band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_G\_EXT\_HSC | Average filter transmission curve wavelength for the HSC G band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_Z\_EXT\_HSC | Average filter transmission curve wavelength for the HSC Z band | Angstrom | FITS _E_ |
| DEBLENDED\_FLAG | Flag marking if the object was originally blended with another one | NA | FITS _I_ |
| PARENT\_ID | ID of the parent sources of a deblended object | NA | FITS _K_ |
| PARENT\_VISNIR | ID of the parent sources of a deblended object | NA | FITS _K_ |
| BLENDED\_PROB | Probability that the source is blended with another source | NA | FITS _E_ |
| SHE\_FLAG | Flags for objects SHE might want to remove (eg. bright stars) | NA | FITS _I_ |
| VARIABLE\_FLAG | Object variability flag | NA | FITS _I_ |
| BINARY\_FLAG | Flag for potentially binary stars | NA | FITS _I_ |
| POINT\_LIKE\_FLAG | Point-like flag : flag set to 1 for VIS detections with (DET\_QUALITY\_FLAG==0) AND (POINT\_LIKE\_PROBA>threshold), otherwise set to NaN | NA | FITS _I_ |
| POINT\_LIKE\_PROB | Probability between 0 and 1 that the source is point-like (the estimation uses a “star probability cube” defined in the MDB). Value is set to NaN for NIR-only objects (use MUMAX\_MINUS\_MAG for NIR-only objcts) | NA | FITS _E_ |
| EXTENDED\_FLAG | Extended source flag | NA | FITS _I_ |
| EXTENDED\_PROB | Probability between 0 and 1 that the source is extended | NA | FITS _E_ |
| SPURIOUS\_FLAG | Spurious source flag | NA | FITS _I_ |
| SPURIOUS\_PROB | Probability between 0 and 1 that the source is spurious | NA | FITS _E_ |
| MAG\_STARGAL\_SEP | Magnitude used to compute POINT\_LIKE\_PROB | mag | FITS _E_ |
| DET\_QUALITY\_FLAG | Detection step flags that could indicate the possible corruption of the MAG\_STARGAL\_SEP values | NA | FITS _I_ |
| MU\_MAX | Peak surface brightness above the background in the detection band (directly from SExtractor) | mag/arcsec2 | FITS _E_ |
| MUMAX\_MINUS\_MAG | The difference between MU\_MAX and MAG\_STARGAL\_SEP, valid even for NIR-only sources | mag/arcsec2 | FITS _E_ |
| SEGMENTATION\_AREA | Isophotal area of the source above the analysis threshold (SExtractor ISOAREA\_IMAGE) | pix | FITS _J_ |
| SEMIMAJOR\_AXIS | Semi-major axis of the source (from Asterism) | pix | FITS _E_ |
| SEMIMAJOR\_AXIS\_ERR | Semi-major axis error | pix | FITS _E_ |
| POSITION\_ANGLE | Position angle (CCW/x) of the source (SExtractor THETA\_IMAGE) range: -90 up to [\|](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#id1) 90 decimal degrees | deg | FITS _E_ |
| POSITION\_ANGLE\_ERR | Position angle error | deg | FITS _E_ |
| ELLIPTICITY | A parametrization of how stretched an object is in the detection band, computed from the minor and major axes of the object itself (directly from SExtractor) | NA | FITS _E_ |
| ELLIPTICITY\_ERR | Ellipticity error | NA | FITS _E_ |
| KRON\_RADIUS | Major semi-axis (in pixels) of the elliptical aperture used for total (Kron) aperture photometry on the detection image | pix | FITS _E_ |
| KRON\_RADIUS\_ERR | Error on the major semi-axis (in pixels) of the elliptical aperture used for total (Kron) aperture photometry on the detection image | pix | FITS _E_ |
| FWHM | FWHM (in arcsec) used in a-phot to compute colors. A-phot fluxes are computed within apertures that are multiples (1, 2, 3, 4 times) of this FWHM | arcsec | FITS _E_ |
| GAL\_EBV | Estimated galactic E(B-V) at the source centroid according to the reference Planck map | mag | FITS _E_ |
| GAL\_EBV\_ERR | Error on galactic E(B-V) according to the reference Planck map | mag | FITS _E_ |
| GAIA\_ID | The associated GAIA source id | NA | FITS _K_ |
| GAIA\_MATCH\_QUALITY | The quality of the GAIA match | NA | FITS _E_ |

### Morphology catalog FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#morphology-catalog-fits-file "Permalink to this heading")

FITS table storing all the morphological measurements performend in the MER
piepline. Each source in this table shares the `OBJECT_ID` with the rest of
the MER catalogs.

Table columns:

| **Catalog**: 104 columns table |
| --- |
| **Name** | **Description** | **Unit** | **Format** |
| OBJECT\_ID | Euclid unique source identifier | NA | FITS _K_ |
| CONCENTRATION | This parameter, simply referred to as the concentration, is defined as the logarithm of the ratio between circular radii containing 80% and 20% of the total flux | NA | FITS _E_ |
| CONCENTRATION\_ERR | Concentratrion error | NA | FITS _E_ |
| ASYMMETRY | The asymmetry quantifies the degree to which the galaxy flux is rotationally symmetric. It is obtained by subtracting from the original image, the flipped galaxy (rotated by 180deg) | NA | FITS _E_ |
| ASYMMETRY\_ERR | Asymmetry error | NA | FITS _E_ |
| SMOOTHNESS | The smoothness quantifies the degree of small-scale structure of the galaxy. The image is smoothed with a box of width 0.25 rp and then subtracted from the original image | NA | FITS _E_ |
| SMOOTHNESS\_ERR | Smoothness error | NA | FITS _E_ |
| GINI | It is a statistic parameter based on the Lorentz curve that presents the cumulative distribution function of galaxy’s pixel i values | NA | FITS _E_ |
| GINI\_ERR | GINI error | NA | FITS _E_ |
| MOMENT\_20 | It is defined as a normalized second-order moment of the 20% brightest pixels of the galaxy. This parameter can trace the spatial distribution of any bright core, bar, spiral arm, and off-centre star cluster | NA | FITS _E_ |
| MOMENT\_20\_ERR | Moment of light error | NA | FITS _E_ |
| SERSIC\_VISNIR\_REDUCED\_CHI2 | Chi-square value from the VISNIR fit | NA | FITS _E_ |
| SERSIC\_VISNIR\_ITERATIONS | Number of iterations from the VISNIR fit | NA | FITS _J_ |
| SERSIC\_VISNIR\_FLAGS | Flags from the VISNIR fit | NA | FITS _K_ |
| SERSIC\_VISNIR\_DURATION | Duration of the VISNIR fit | s | FITS _E_ |
| SERSIC\_SERSIC\_VIS\_RADIUS | The VIS Sersic radius | arcsec | FITS _E_ |
| SERSIC\_SERSIC\_VIS\_RADIUS\_ERR | Error of the the VIS Sersic radius | arcsec | FITS _E_ |
| SERSIC\_SERSIC\_VIS\_AXIS\_RATIO | VIS Axis ratio of the Sersic | NA | FITS _E_ |
| SERSIC\_SERSIC\_VIS\_AXIS\_RATIO\_ERR | Error of the VIS axis ratio | NA | FITS _E_ |
| SERSIC\_SERSIC\_VIS\_INDEX | VIS Sersic index | NA | FITS _E_ |
| SERSIC\_SERSIC\_VIS\_INDEX\_ERR | Error of the VIS Sersic index | NA | FITS _E_ |
| SERSIC\_SERSIC\_NIR\_RADIUS | The NIR Sersic radius | arcsec | FITS _E_ |
| SERSIC\_SERSIC\_NIR\_RADIUS\_ERR | Error of the the NIR Sersic radius | arcsec | FITS _E_ |
| SERSIC\_SERSIC\_NIR\_AXIS\_RATIO | NIR Axis ratio of the Sersic | NA | FITS _E_ |
| SERSIC\_SERSIC\_NIR\_AXIS\_RATIO\_ERR | Error of the NIR axis ratio | NA | FITS _E_ |
| SERSIC\_SERSIC\_NIR\_INDEX | NIR Sersic index | NA | FITS _E_ |
| SERSIC\_SERSIC\_NIR\_INDEX\_ERR | Error of the NIR Sersic index | NA | FITS _E_ |
| SERSIC\_ANGLE | Position angle of the VISNIR Sersic | deg | FITS _E_ |
| SERSIC\_ANGLE\_ERR | Position angle error of the VISNIR Sersic | deg | FITS _E_ |
| SERSIC\_EXT\_REDUCED\_CHI2 | Chi-square value from the EXT fit | NA | FITS _E_ |
| SERSIC\_EXT\_ITERATIONS | Number of iterations from the EXT fit | NA | FITS _J_ |
| SERSIC\_EXT\_FLAGS | Flags from the EXT fit | NA | FITS _K_ |
| SERSIC\_EXT\_DURATION | Duration of the EXT fit | s | FITS _E_ |
| DISK\_SERSIC\_REDUCED\_CHI2 | Chi-square value from the fit | NA | FITS _E_ |
| DISK\_SERSIC\_ITERATIONS | Number of iterations from the fit | NA | FITS _J_ |
| DISK\_SERSIC\_FLAGS | Flags from the fit | NA | FITS _K_ |
| DISK\_SERSIC\_DURATION | Duration of the fit | s | FITS _E_ |
| DISK\_SERSIC\_SERSIC\_RADIUS | The Sersic radius | arcsec | FITS _E_ |
| DISK\_SERSIC\_SERSIC\_RADIUS\_ERR | Error of the Sersic radius | arcsec | FITS _E_ |
| DISK\_SERSIC\_SERSIC\_AXIS\_RATIO | Axis ratio of the Sersic | NA | FITS _E_ |
| DISK\_SERSIC\_SERSIC\_AXIS\_RATIO\_ERR | Error of the sersic axis ratio | NA | FITS _E_ |
| DISK\_SERSIC\_SERSIC\_INDEX | Sersic index | NA | FITS _E_ |
| DISK\_SERSIC\_SERSIC\_INDEX\_ERR | Error of the Sersic index | NA | FITS _E_ |
| DISK\_SERSIC\_DISK\_RADIUS | Disk radius of the fit | arcsec | FITS _E_ |
| DISK\_SERSIC\_DISK\_RADIUS\_ERR | Error of the disk radius | arcsec | FITS _E_ |
| DISK\_SERSIC\_DISK\_AXIS\_RATIO | Axis ratio of the disk | NA | FITS _E_ |
| DISK\_SERSIC\_DISK\_AXIS\_RATIO\_ERR | Error of the disk axis ratio | NA | FITS _E_ |
| DISK\_SERSIC\_ANGLE | Position angle of Disk\|Sersic | deg | FITS _E_ |
| DISK\_SERSIC\_ANGLE\_ERR | Position angle error of tDisk\|Sersic | deg | FITS _E_ |
| BAR\_NO | Dirichlet param. of question ‘Does the galaxy have a bar, and if so, how strong?’ Having response ‘No bar’ | NA | FITS _E_ |
| BAR\_STRONG | Dirichlet param. of question ‘Does the galaxy have a bar, and if so, how strong?’ having response ‘Strong’ | NA | FITS _E_ |
| BAR\_WEAK | Dirichlet param. of question ‘Does the galaxy have a bar, and if so, how strong?’ having response ‘Weak’ | NA | FITS _E_ |
| BULGE\_SIZE\_DOMINANT | Dirichlet param. of question ‘Does the galaxy have a bulge, and if so, how visually obvious?’ having response ‘Dominant’ | NA | FITS _E_ |
| BULGE\_SIZE\_LARGE | Dirichlet param. of question ‘Does the galaxy have a bulge, and if so, how visually obvious?’ having response ‘Large’ | NA | FITS _E_ |
| BULGE\_SIZE\_MODERATE | Dirichlet param. of question ‘Does the galaxy have a bulge, and if so, how visually obvious?’ having response ‘Moderate’ | NA | FITS _E_ |
| BULGE\_SIZE\_NONE | Dirichlet param. of question ‘Does the galaxy have a bulge, and if so, how visually obvious?’ having response ‘None’ | NA | FITS _E_ |
| BULGE\_SIZE\_SMALL | Dirichlet param. of question ‘Does the galaxy have a bulge, and if so, how visually obvious?’ having response ‘Small’ | NA | FITS _E_ |
| CLUMP\_COUNT\_ANY\_THRESHOLD | Number of clumps detected before applying confidence threshold | NA | FITS _I_ |
| CLUMP\_COUNT\_ABOVE\_THRESHOLD | Number of clumps detected after applying confidence threshold | NA | FITS _I_ |
| CLUMP\_COUNT\_UNUSUAL\_ANY\_THRESHOLD | Number of ‘unusual’ (e.g. color, shape) clumps detected before applying confidence threshold | NA | FITS _I_ |
| CLUMP\_COUNT\_UNUSUAL\_ABOVE\_THRESHOLD | Number of ‘unusual’ (e.g. color, shape) clumps detected after applying confidence threshold | NA | FITS _I_ |
| DISK\_EDGE\_ON\_NO | Dirichlet param. of question ‘Does the galaxy appear to be an edge-on-disk?’ having response ‘Not edge-on-disk’ | NA | FITS _E_ |
| DISK\_EDGE\_ON\_YES | Dirichlet param. of question ‘Does the galaxy appear to be an edge-on-disk?’ having response ‘Yes, edge-on-disk’ | NA | FITS _E_ |
| EDGE\_ON\_BULGE\_BOXY | Dirichlet param. of question ‘What shape is the bulge in the edge-on disk’ having response ‘Boxy’ | NA | FITS _E_ |
| EDGE\_ON\_BULGE\_NONE | Dirichlet param. of question ‘What shape is the bulge in the edge-on disk’ having response ‘No bulge’ | NA | FITS _E_ |
| EDGE\_ON\_BULGE\_ROUNDED | Dirichlet param. of question ‘What shape is the bulge in the edge-on disk’ having response ‘Rounded’ | NA | FITS _E_ |
| LOPSIDED\_NO | Dirichlet param. of question ‘Is the galaxy lopsided?’ having response ‘No’ | NA | FITS _E_ |
| LOPSIDED\_YES | Dirichlet param. of question ‘Is the galaxy lopsided?’ having response ‘Yes’ | NA | FITS _E_ |
| HAS\_SPIRAL\_ARMS\_NO | Dirichlet param. of question ‘Does the galaxy have spiral arms?’ having response ‘No’ | NA | FITS _E_ |
| HAS\_SPIRAL\_ARMS\_YES | Dirichlet param. of question ‘Does the galaxy have spiral arms?’ having response ‘Yes’ | NA | FITS _E_ |
| HOW\_ROUNDED\_CIGAR\_SHAPED | Dirichlet param. of question ‘Given the galaxy is visually smooth, how round is it?’ having response ‘Cigar-shaped’ | NA | FITS _E_ |
| HOW\_ROUNDED\_COMPLETELY | Dirichlet param. of question ‘Given the galaxy is visually smooth, how round is it?’ having response ‘Completely’ | NA | FITS _E_ |
| HOW\_ROUNDED\_IN\_BETWEEN | Dirichlet param. of question ‘Given the galaxy is visually smooth, how round is it?’ having response ‘In-between’ | NA | FITS _E_ |
| MERGING\_MAJOR\_DISTURBANCE | Dirichlet param of question ‘Is the galaxy visually disturbed or merging?’ having response ‘Major disturbance’ | NA | FITS _E_ |
| MERGING\_MERGER | Dirichlet param of question ‘Is the galaxy visually disturbed or merging?’ having response ‘Merger’ | NA | FITS _E_ |
| MERGING\_MINOR\_DISTURBANCE | Dirichlet param of question ‘Is the galaxy visually disturbed or merging?’ having response ‘Minor disturbance’ | NA | FITS _E_ |
| MERGING\_NONE | Dirichlet param of question ‘Is the galaxy visually disturbed or merging?’ having response ‘None (no)’ | NA | FITS _E_ |
| SMOOTH\_OR\_FEATURED\_ARTIFACT\_STAR\_ZOOM | Dirichlet param. of question ‘Is the galaxy smooth, featured/disk, or an artifact?’ having response ‘Artifact, Star, or Bad Zoom’ | NA | FITS _E_ |
| SMOOTH\_OR\_FEATURED\_FEATURED\_OR\_DISK | Dirichlet param. of question ‘Is the galaxy smooth, featured/disk, or an artifact?’ having response ‘Featured or Disk’ | NA | FITS _E_ |
| SMOOTH\_OR\_FEATURED\_SMOOTH | Dirichlet param. of question ‘Is the galaxy smooth, featured/disk, or an artifact?’ having response ‘Smooth’ | NA | FITS _E_ |
| SPIRAL\_ARM\_COUNT\_1 | Dirichlet param. of question ‘Given the galaxy has spiral arms, how many?’ having response ‘1’ | NA | FITS _E_ |
| SPIRAL\_ARM\_COUNT\_2 | Dirichlet param. of question ‘Given the galaxy has spiral arms, how many?’ having response ‘2’ | NA | FITS _E_ |
| SPIRAL\_ARM\_COUNT\_3 | Dirichlet param. of question ‘Given the galaxy has spiral arms, how many?’ having response ‘3’ | NA | FITS _E_ |
| SPIRAL\_ARM\_COUNT\_4 | Dirichlet param. of question ‘Given the galaxy has spiral arms, how many?’ having response ‘4’ | NA | FITS _E_ |
| SPIRAL\_ARM\_COUNT\_CANT\_TELL | Dirichlet param. of question ‘Given the galaxy has spiral arms, how many?’ having response ‘Can’t tell’ | NA | FITS _E_ |
| SPIRAL\_ARM\_COUNT\_MORE\_THAN\_4 | Dirichlet param. of question ‘Given the galaxy has spiral arms, how many?’ having response ‘More than 4’ | NA | FITS _E_ |
| SPIRAL\_WINDING\_LOOSE | Dirichlet param. of question ‘Given the galaxy has spiral arms, how tightly wound are they?’ having response ‘Loose’ | NA | FITS _E_ |
| SPIRAL\_WINDING\_MEDIUM | Dirichlet param. of question ‘Given the galaxy has spiral arms, how tightly wound are they?’ having response ‘Medium’ | NA | FITS _E_ |
| SPIRAL\_WINDING\_TIGHT | Dirichlet param. of question ‘Given the galaxy has spiral arms, how tightly wound are they?’ having response ‘Tight’ | NA | FITS _E_ |
| DWARF\_YES | Dirichlet param. of question identifying dwarf galaxies (visually, like a ‘smudge’) having response ‘Yes’ | NA | FITS _E_ |
| DWARF\_NO | Dirichlet param. of question identifying dwarf galaxies (visually, like a ‘smudge’) having response ‘No’ | NA | FITS _E_ |
| PECULIAR\_YES | Dirichlet param. of question identifying peculiar galaxies (visually, highly disturbed or otherwise unusual, without companion) having response ‘Yes’ | NA | FITS _E_ |
| PECULIAR\_NO | Dirichlet param. of question identifying peculiar galaxies (visually, highly disturbed or otherwise unusual, without companion) having response ‘No’ | NA | FITS _E_ |
| RING\_YES | Dirichlet param. of question ‘Does the galaxy have a ring’ (intended to include pseudo-ring) having response ‘Yes’ | NA | FITS _E_ |
| RING\_NO | Dirichlet param. of question ‘Does the galaxy have a ring’ (intended to include pseudo-ring) having response ‘No’ | NA | FITS _E_ |
| AGN\_YES | Dirichlet param. of question asking if the galaxy has a central PSF-like (very) bright spot, for positive response | NA | FITS _E_ |
| AGN\_NO | Dirichlet param. of question asking if the galaxy has a central PSF-like (very) bright spot, for negative response | NA | FITS _E_ |
| ETG\_OR\_LTG | Binary classification between early and late types, from Dominguez Sanchez\|2022 | NA | FITS _E_ |
| T\_TYPE | T-Type regression model, from Dominguez Sanchez\|2022 | NA | FITS _E_ |
| MAJOR\_MERGER | The probability of the galaxy classified as a major merger | NA | FITS _E_ |
| MAJOR\_MERGER\_UNCERTAINTY | Uncertainty on the probability of the major merger classification | NA | FITS _E_ |
| MAJOR\_MERGER\_STAGE | The most likely merger stage of the major merger | NA | FITS _I_ |
| MAJOR\_MERGER\_STAGE\_PROBABILITY | The probability of the most likely merger stage | NA | FITS _E_ |
| MAJOR\_MERGER\_STAGE\_UNCERTAINTY | Uncertainty on the probability of the most likely merger stage | NA | FITS _E_ |

### Cutouts catalog FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#cutouts-catalog-fits-file "Permalink to this heading")

FITS table containing information on the corners of the source cutouts. Each
source in this table shares the `OBJECT_ID` with the rest of the MER catalogs.

Table columns:

| **Catalog**: 25 columns table |
| --- |
| **Name** | **Description** | **Unit** | **Format** |
| OBJECT\_ID | Euclid unique source identifier | NA | FITS _K_ |
| RIGHT\_ASCENSION | Source barycenter RA coordinate (SExtractor ALPHA\_J2000) decimal degrees | deg | FITS _D_ |
| DECLINATION | Source barycenter DEC coordinate (SExtractor DELTA\_J2000) decimal degrees | deg | FITS _D_ |
| CORNER\_0\_RA | Right ascension of the lower-right cutout corner | deg | FITS _D_ |
| CORNER\_0\_DEC | Declination of the lower-right cutout corner | deg | FITS _D_ |
| CORNER\_1\_RA | Right ascension of the lower-left cutout corner | deg | FITS _D_ |
| CORNER\_1\_DEC | Declination of the lower-left cutout corner | deg | FITS _D_ |
| CORNER\_2\_RA | Right ascension of the upper-left cutout corner | deg | FITS _D_ |
| CORNER\_2\_DEC | Declination of the upper-left cutout corner | deg | FITS _D_ |
| CORNER\_3\_RA | Right ascension of the upper-right cutout corner | deg | FITS _D_ |
| CORNER\_3\_DEC | Declination of the upper-right cutout corner | deg | FITS _D_ |
| DBL\_CORNER\_0\_RA | Right ascension of the lower-right deblending corner | deg | FITS _D_ |
| DBL\_CORNER\_0\_DEC | Declination of the lower-right deblending corner | deg | FITS _D_ |
| DBL\_CORNER\_1\_RA | Right ascension of the lower-left deblending corner | deg | FITS _D_ |
| DBL\_CORNER\_1\_DEC | Declination of the lower-left deblending corner | deg | FITS _D_ |
| DBL\_CORNER\_2\_RA | Right ascension of the upper-left deblending corner | deg | FITS _D_ |
| DBL\_CORNER\_2\_DEC | Declination of the upper-left deblending corner | deg | FITS _D_ |
| DBL\_CORNER\_3\_RA | Right ascension of the upper-right deblending corner | deg | FITS _D_ |
| DBL\_CORNER\_3\_DEC | Declination of the upper-right deblending corner | deg | FITS _D_ |
| SEMIMAJOR\_AXIS | Semi-major axis of the source (from Asterism) | deg | FITS _D_ |
| SEMIMINOR\_AXIS | Semi-minor axis of the source (from Asterism) | deg | FITS _D_ |
| POSITION\_ANGLE | Position angle (CCW/x) of the source (SExtractor THETA\_IMAGE) range: -90 up to [\|](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#id3) 90 decimal degrees | deg | FITS _D_ |
| PARENT\_ID | ID of the parent sources of a deblended object | NA | FITS _K_ |
| PARENT\_VISNIR | ID of the parent sources of a deblended object | NA | FITS _K_ |
| FLUX\_DETECTION\_TOTAL | VIS or NIR stack band source total flux error (Kron aperture) | uJy | FITS _E_ |

### DEEP field photometry catalog FITS file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#deep-field-photometry-catalog-fits-file "Permalink to this heading")

FITS table storing photometry measurements related to EXT input images present
only in the DEEP survey. Each source in this table shares the `OBJECT_ID` with
the rest of the MER catalogs.

Table columns:

| **Catalog**: 713 columns table |
| --- |
| **Name** | **Description** | **Unit** | **Format** |
| OBJECT\_ID | Euclid unique source identifier | NA | FITS _K_ |
| FLUX\_IA427\_EXT\_SUBARU\_1FWHM\_APER | IA427 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA427\_EXT\_SUBARU\_2FWHM\_APER | IA427 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA427\_EXT\_SUBARU\_3FWHM\_APER | IA427 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA427\_EXT\_SUBARU\_4FWHM\_APER | IA427 ext SUBARU band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA445\_EXT\_SUBARU\_1FWHM\_APER | IA445 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA445\_EXT\_SUBARU\_2FWHM\_APER | IA445 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA445\_EXT\_SUBARU\_3FWHM\_APER | IA445 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA445\_EXT\_SUBARU\_4FWHM\_APER | IA445 ext SUBARU band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA464\_EXT\_SUBARU\_1FWHM\_APER | IA464 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA464\_EXT\_SUBARU\_2FWHM\_APER | IA464 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA464\_EXT\_SUBARU\_3FWHM\_APER | IA464 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA464\_EXT\_SUBARU\_4FWHM\_APER | IA464 ext SUBARU band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA484\_EXT\_SUBARU\_1FWHM\_APER | IA484 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA484\_EXT\_SUBARU\_2FWHM\_APER | IA484 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA484\_EXT\_SUBARU\_3FWHM\_APER | IA484 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA484\_EXT\_SUBARU\_4FWHM\_APER | IA484 ext SUBARU band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA505\_EXT\_SUBARU\_1FWHM\_APER | IA505 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA505\_EXT\_SUBARU\_2FWHM\_APER | IA505 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA505\_EXT\_SUBARU\_3FWHM\_APER | IA505 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA505\_EXT\_SUBARU\_4FWHM\_APER | IA505 ext SUBARU band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA527\_EXT\_SUBARU\_1FWHM\_APER | IA527 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA527\_EXT\_SUBARU\_2FWHM\_APER | IA527 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA527\_EXT\_SUBARU\_3FWHM\_APER | IA527 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA527\_EXT\_SUBARU\_4FWHM\_APER | IA527 ext SUBARU band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA550\_EXT\_SUBARU\_1FWHM\_APER | IA550 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA550\_EXT\_SUBARU\_2FWHM\_APER | IA550 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA550\_EXT\_SUBARU\_3FWHM\_APER | IA550 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA550\_EXT\_SUBARU\_4FWHM\_APER | IA550 ext SUBARU band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA574\_EXT\_SUBARU\_1FWHM\_APER | IA574 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA574\_EXT\_SUBARU\_2FWHM\_APER | IA574 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA574\_EXT\_SUBARU\_3FWHM\_APER | IA574 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA574\_EXT\_SUBARU\_4FWHM\_APER | IA574 ext SUBARU band source aperture photometry flux (4 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA598\_EXT\_SUBARU\_1FWHM\_APER | IA598 ext SUBARU band source aperture photometry flux (1 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA598\_EXT\_SUBARU\_2FWHM\_APER | IA598 ext SUBARU band source aperture photometry flux (2 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |
| FLUX\_IA598\_EXT\_SUBARU\_3FWHM\_APER | IA598 ext SUBARU band source aperture photometry flux (3 FWHM diameter) on PSF-matched images | uJy | FITS _E_ |

[... middle omitted — see footer ...]

| FLUX\_IA624\_EXT\_SUBARU\_DISK\_SERSIC | IA624ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_IA651\_EXT\_SUBARU\_DISK\_SERSIC | IA651ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_IA679\_EXT\_SUBARU\_DISK\_SERSIC | IA679ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_IA709\_EXT\_SUBARU\_DISK\_SERSIC | IA709ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_IA738\_EXT\_SUBARU\_DISK\_SERSIC | IA738ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_IA767\_EXT\_SUBARU\_DISK\_SERSIC | IA767ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_IA797\_EXT\_SUBARU\_DISK\_SERSIC | IA797ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_IA827\_EXT\_SUBARU\_DISK\_SERSIC | IA827ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_IA856\_EXT\_SUBARU\_DISK\_SERSIC | IA856ext SUBARU band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_USTAR\_EXT\_MEGACAM\_DISK\_SERSIC | USTARext MEGACAM band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_UPRIME\_EXT\_MEGACAM\_DISK\_SERSIC | UPRIMEext MEGACAM band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_R\_EXT\_HSC\_DISK\_SERSIC | Rext HSC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_R2\_EXT\_HSC\_DISK\_SERSIC | R2ext HSC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_I\_EXT\_HSC\_DISK\_SERSIC | Iext HSC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_I2\_EXT\_HSC\_DISK\_SERSIC | I2ext HSC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_Y\_EXT\_HSC\_DISK\_SERSIC | Yext HSC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_H\_EXT\_VISTA\_DISK\_SERSIC | Hext VISTA band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_J\_EXT\_VISTA\_DISK\_SERSIC | Jext VISTA band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_Y\_EXT\_VISTA\_DISK\_SERSIC | Yext VISTA band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_KS\_EXT\_VISTA\_DISK\_SERSIC | KSext VISTA band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_J\_EXT\_UKIRT\_DISK\_SERSIC | Jext UKIRT band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_H\_EXT\_UKIRT\_DISK\_SERSIC | Hext UKIRT band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_K\_EXT\_UKIRT\_DISK\_SERSIC | Kext UKIRT band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_CH1\_EXT\_IRAC\_DISK\_SERSIC | CH1ext IRAC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_CH2\_EXT\_IRAC\_DISK\_SERSIC | CH2ext IRAC band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_FUV\_EXT\_GALEX\_DISK\_SERSIC | FUVext GALEX band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUX\_NUV\_EXT\_GALEX\_DISK\_SERSIC | NUVext GALEX band source flux from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA427\_EXT\_SUBARU\_DISK\_SERSIC | IA427ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA445\_EXT\_SUBARU\_DISK\_SERSIC | IA445ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA464\_EXT\_SUBARU\_DISK\_SERSIC | IA464ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA484\_EXT\_SUBARU\_DISK\_SERSIC | IA484ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA505\_EXT\_SUBARU\_DISK\_SERSIC | IA505ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA527\_EXT\_SUBARU\_DISK\_SERSIC | IA527ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA550\_EXT\_SUBARU\_DISK\_SERSIC | IA550ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA574\_EXT\_SUBARU\_DISK\_SERSIC | IA574ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA598\_EXT\_SUBARU\_DISK\_SERSIC | IA598ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA624\_EXT\_SUBARU\_DISK\_SERSIC | IA624ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA651\_EXT\_SUBARU\_DISK\_SERSIC | IA651ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA679\_EXT\_SUBARU\_DISK\_SERSIC | IA679ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA709\_EXT\_SUBARU\_DISK\_SERSIC | IA709ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA738\_EXT\_SUBARU\_DISK\_SERSIC | IA738ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA767\_EXT\_SUBARU\_DISK\_SERSIC | IA767ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA797\_EXT\_SUBARU\_DISK\_SERSIC | IA797ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA827\_EXT\_SUBARU\_DISK\_SERSIC | IA827ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_IA856\_EXT\_SUBARU\_DISK\_SERSIC | IA856ext SUBARU band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_USTAR\_EXT\_MEGACAM\_DISK\_SERSIC | USTARext MEGACAM band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_UPRIME\_EXT\_MEGACAM\_DISK\_SERSIC | UPRIMEext MEGACAM band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_R\_EXT\_HSC\_DISK\_SERSIC | Rext HSC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_R2\_EXT\_HSC\_DISK\_SERSIC | R2ext HSC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_I\_EXT\_HSC\_DISK\_SERSIC | Iext HSC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_I2\_EXT\_HSC\_DISK\_SERSIC | I2ext HSC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Y\_EXT\_HSC\_DISK\_SERSIC | Yext HSC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_H\_EXT\_VISTA\_DISK\_SERSIC | Hext VISTA band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_J\_EXT\_VISTA\_DISK\_SERSIC | Jext VISTA band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_Y\_EXT\_VISTA\_DISK\_SERSIC | Yext VISTA band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_KS\_EXT\_VISTA\_DISK\_SERSIC | KSext VISTA band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_J\_EXT\_UKIRT\_DISK\_SERSIC | Jext UKIRT band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_H\_EXT\_UKIRT\_DISK\_SERSIC | Hext UKIRT band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_K\_EXT\_UKIRT\_DISK\_SERSIC | Kext UKIRT band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_CH1\_EXT\_IRAC\_DISK\_SERSIC | CH1ext IRAC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_CH2\_EXT\_IRAC\_DISK\_SERSIC | CH2ext IRAC band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_FUV\_EXT\_GALEX\_DISK\_SERSIC | FUVext GALEX band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| FLUXERR\_NUV\_EXT\_GALEX\_DISK\_SERSIC | NUVext GALEX band source flux error from the Disk\|Sersic fit | uJy | FITS _E_ |
| SERSIC\_FRACT\_IA427\_EXT\_SUBARU\_DISK\_SERSIC | IA427ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA445\_EXT\_SUBARU\_DISK\_SERSIC | IA445ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA464\_EXT\_SUBARU\_DISK\_SERSIC | IA464ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA484\_EXT\_SUBARU\_DISK\_SERSIC | IA484ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA505\_EXT\_SUBARU\_DISK\_SERSIC | IA505ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA527\_EXT\_SUBARU\_DISK\_SERSIC | IA527ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA550\_EXT\_SUBARU\_DISK\_SERSIC | IA550ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA574\_EXT\_SUBARU\_DISK\_SERSIC | IA574ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA598\_EXT\_SUBARU\_DISK\_SERSIC | IA598ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA624\_EXT\_SUBARU\_DISK\_SERSIC | IA624ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA651\_EXT\_SUBARU\_DISK\_SERSIC | IA651ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA679\_EXT\_SUBARU\_DISK\_SERSIC | IA679ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA709\_EXT\_SUBARU\_DISK\_SERSIC | IA709ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA738\_EXT\_SUBARU\_DISK\_SERSIC | IA738ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA767\_EXT\_SUBARU\_DISK\_SERSIC | IA767ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA797\_EXT\_SUBARU\_DISK\_SERSIC | IA797ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA827\_EXT\_SUBARU\_DISK\_SERSIC | IA827ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA856\_EXT\_SUBARU\_DISK\_SERSIC | IA856ext SUBARU band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_USTAR\_EXT\_MEGACAM\_DISK\_SERSIC | USTARext MEGACAM band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_UPRIME\_EXT\_MEGACAM\_DISK\_SERSIC | UPRIMEext MEGACAM band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_R\_EXT\_HSC\_DISK\_SERSIC | Rext HSC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_R2\_EXT\_HSC\_DISK\_SERSIC | R2ext HSC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_I\_EXT\_HSC\_DISK\_SERSIC | Iext HSC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_I2\_EXT\_HSC\_DISK\_SERSIC | I2ext HSC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_Y\_EXT\_HSC\_DISK\_SERSIC | Yext HSC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_H\_EXT\_VISTA\_DISK\_SERSIC | Hext VISTA band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_J\_EXT\_VISTA\_DISK\_SERSIC | Jext VISTA band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_Y\_EXT\_VISTA\_DISK\_SERSIC | Yext VISTA band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_KS\_EXT\_VISTA\_DISK\_SERSIC | KSext VISTA band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_J\_EXT\_UKIRT\_DISK\_SERSIC | Jext UKIRT band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_H\_EXT\_UKIRT\_DISK\_SERSIC | Hext UKIRT band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_K\_EXT\_UKIRT\_DISK\_SERSIC | Kext UKIRT band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_CH1\_EXT\_IRAC\_DISK\_SERSIC | CH1ext IRAC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_CH2\_EXT\_IRAC\_DISK\_SERSIC | CH2ext IRAC band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_FUV\_EXT\_GALEX\_DISK\_SERSIC | FUVext GALEX band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_NUV\_EXT\_GALEX\_DISK\_SERSIC | NUVext GALEX band Sersic fraction | NA | FITS _E_ |
| SERSIC\_FRACT\_IA427\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA427ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA445\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA445ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA464\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA464ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA484\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA484ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA505\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA505ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA527\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA527ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA550\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA550ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA574\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA574ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA598\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA598ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA624\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA624ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA651\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA651ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA679\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA679ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA709\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA709ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA738\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA738ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA767\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA767ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA797\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA797ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA827\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA827ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_IA856\_EXT\_SUBARU\_DISK\_SERSIC\_ERR | IA856ext SUBARU band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_USTAR\_EXT\_MEGACAM\_DISK\_SERSIC\_ERR | USTARext MEGACAM band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_UPRIME\_EXT\_MEGACAM\_DISK\_SERSIC\_ERR | UPRIMEext MEGACAM band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_R\_EXT\_HSC\_DISK\_SERSIC\_ERR | Rext HSC band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_R2\_EXT\_HSC\_DISK\_SERSIC\_ERR | R2ext HSC band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_I\_EXT\_HSC\_DISK\_SERSIC\_ERR | Iext HSC band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_I2\_EXT\_HSC\_DISK\_SERSIC\_ERR | I2ext HSC band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_Y\_EXT\_HSC\_DISK\_SERSIC\_ERR | Yext HSC band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_H\_EXT\_VISTA\_DISK\_SERSIC\_ERR | Hext VISTA band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_J\_EXT\_VISTA\_DISK\_SERSIC\_ERR | Jext VISTA band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_Y\_EXT\_VISTA\_DISK\_SERSIC\_ERR | Yext VISTA band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_KS\_EXT\_VISTA\_DISK\_SERSIC\_ERR | KSext VISTA band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_J\_EXT\_UKIRT\_DISK\_SERSIC\_ERR | Jext UKIRT band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_H\_EXT\_UKIRT\_DISK\_SERSIC\_ERR | Hext UKIRT band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_K\_EXT\_UKIRT\_DISK\_SERSIC\_ERR | Kext UKIRT band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_CH1\_EXT\_IRAC\_DISK\_SERSIC\_ERR | CH1ext IRAC band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_CH2\_EXT\_IRAC\_DISK\_SERSIC\_ERR | CH2ext IRAC band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_FUV\_EXT\_GALEX\_DISK\_SERSIC\_ERR | FUVext GALEX band Sersic fraction error | NA | FITS _E_ |
| SERSIC\_FRACT\_NUV\_EXT\_GALEX\_DISK\_SERSIC\_ERR | NUVext GALEX band Sersic fraction error | NA | FITS _E_ |
| FLAG\_IA427\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA427ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA445\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA445ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA464\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA464ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA484\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA484ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA505\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA505ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA527\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA527ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA550\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA550ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA574\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA574ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA598\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA598ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA624\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA624ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA651\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA651ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA679\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA679ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA709\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA709ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA738\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA738ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA767\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA767ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA797\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA797ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA827\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA827ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_IA856\_EXT\_SUBARU | Objects flag keeping track of the flagged pixels in the IA856ext SUBARU flag image | NA | FITS _J_ |
| FLAG\_USTAR\_EXT\_MEGACAM | Objects flag keeping track of the flagged pixels in the USTARext MEGACAM flag image | NA | FITS _J_ |
| FLAG\_UPRIME\_EXT\_MEGACAM | Objects flag keeping track of the flagged pixels in the UPRIMEext MEGACAM flag image | NA | FITS _J_ |
| FLAG\_R\_EXT\_HSC | Objects flag keeping track of the flagged pixels in the Rext HSC flag image | NA | FITS _J_ |
| FLAG\_R2\_EXT\_HSC | Objects flag keeping track of the flagged pixels in the R2ext HSC flag image | NA | FITS _J_ |
| FLAG\_I\_EXT\_HSC | Objects flag keeping track of the flagged pixels in the Iext HSC flag image | NA | FITS _J_ |
| FLAG\_I2\_EXT\_HSC | Objects flag keeping track of the flagged pixels in the I2ext HSC flag image | NA | FITS _J_ |
| FLAG\_Y\_EXT\_HSC | Objects flag keeping track of the flagged pixels in the Yext HSC flag image | NA | FITS _J_ |
| FLAG\_H\_EXT\_VISTA | Objects flag keeping track of the flagged pixels in the Hext VISTA flag image | NA | FITS _J_ |
| FLAG\_J\_EXT\_VISTA | Objects flag keeping track of the flagged pixels in the Jext VISTA flag image | NA | FITS _J_ |
| FLAG\_Y\_EXT\_VISTA | Objects flag keeping track of the flagged pixels in the Yext VISTA flag image | NA | FITS _J_ |
| FLAG\_KS\_EXT\_VISTA | Objects flag keeping track of the flagged pixels in the KSext VISTA flag image | NA | FITS _J_ |
| FLAG\_J\_EXT\_UKIRT | Objects flag keeping track of the flagged pixels in the Jext UKIRT flag image | NA | FITS _J_ |
| FLAG\_H\_EXT\_UKIRT | Objects flag keeping track of the flagged pixels in the Hext UKIRT flag image | NA | FITS _J_ |
| FLAG\_K\_EXT\_UKIRT | Objects flag keeping track of the flagged pixels in the Kext UKIRT flag image | NA | FITS _J_ |
| FLAG\_CH1\_EXT\_IRAC | Objects flag keeping track of the flagged pixels in the CH1ext IRAC flag image | NA | FITS _J_ |
| FLAG\_CH2\_EXT\_IRAC | Objects flag keeping track of the flagged pixels in the CH2ext IRAC flag image | NA | FITS _J_ |
| FLAG\_FUV\_EXT\_GALEX | Objects flag keeping track of the flagged pixels in the FUVext GALEX flag image | NA | FITS _J_ |
| FLAG\_NUV\_EXT\_GALEX | Objects flag keeping track of the flagged pixels in the NUVext GALEX flag image | NA | FITS _J_ |
| AVG\_TRANS\_WAVE\_IA427\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA427 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA445\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA445 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA464\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA464 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA484\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA484 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA505\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA505 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA527\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA527 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA550\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA550 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA574\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA574 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA598\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA598 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA624\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA624 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA651\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA651 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA679\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA679 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA709\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA709 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA738\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA738 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA767\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA767 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA797\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA797 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA827\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA827 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_IA856\_EXT\_SUBARU | Average filter transmission curve wavelength for the SUBARU IA856 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_USTAR\_EXT\_MEGACAM | Average filter transmission curve wavelength for the MEGACAM USTAR band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_UPRIME\_EXT\_MEGACAM | Average filter transmission curve wavelength for the MEGACAM UPRIME band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_R\_EXT\_HSC | Average filter transmission curve wavelength for the HSC R band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_R2\_EXT\_HSC | Average filter transmission curve wavelength for the HSC R2 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_I\_EXT\_HSC | Average filter transmission curve wavelength for the HSC I band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_I2\_EXT\_HSC | Average filter transmission curve wavelength for the HSC I2 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_Y\_EXT\_HSC | Average filter transmission curve wavelength for the HSC Y band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_H\_EXT\_VISTA | Average filter transmission curve wavelength for the VISTA H band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_J\_EXT\_VISTA | Average filter transmission curve wavelength for the VISTA J band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_Y\_EXT\_VISTA | Average filter transmission curve wavelength for the VISTA Y band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_KS\_EXT\_VISTA | Average filter transmission curve wavelength for the VISTA KS band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_J\_EXT\_UKIRT | Average filter transmission curve wavelength for the UKIRT J band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_H\_EXT\_UKIRT | Average filter transmission curve wavelength for the UKIRT H band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_K\_EXT\_UKIRT | Average filter transmission curve wavelength for the UKIRT K band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_CH1\_EXT\_IRAC | Average filter transmission curve wavelength for the IRAC CH1 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_CH2\_EXT\_IRAC | Average filter transmission curve wavelength for the IRAC CH2 band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_FUV\_EXT\_GALEX | Average filter transmission curve wavelength for the GALEX FUV band | Angstrom | FITS _E_ |
| AVG\_TRANS\_WAVE\_NUV\_EXT\_GALEX | Average filter transmission curve wavelength for the GALEX NUV band | Angstrom | FITS _E_ |

### Catalog quality parameters [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html\#catalog-quality-parameters "Permalink to this heading")

The following list of quality parameters is calculated for each MER final
catalog. Their values can be used to select an specific subset of
catalogs, to study global trends, or to detect potencial problems in the MER
pipeline or its input products.

| Quality parameter | Descriptiom |
| --- | --- |
| ObjectCount | Total number of objects in the catalog |
| ObjectDensity | The number of objects per mosaic pixel (the total number of objects in the catalog divided by the total number of pixels in the mosaic) |
| PointLikeFraction | The fraction of point-like objects |
| MinFluxVIS | Minimum flux value (uJy) in the VIS band |
| MaxFluxVIS | Maximum flux value (uJy) in the VIS band |
| MedianFluxVIS | Median flux value (uJy) in the VIS band |
| MinFluxErrVIS | Minimum flux error (uJy) in the VIS band |
| MaxFluxErrVIS | Maximum flux error (uJy) in the VIS band |
| MedianFluxErrVIS | Median flux error (uJy) in the VIS band |
| NoFluxFractionVIS | Fraction of objects without a flux detection in the VIS band |
| SatObjectFractionVIS | Fraction of saturated objects in the VIS band |
| MinFluxNIRJ | Minimum flux value (uJy) in the NIR J band |
| MaxFluxNIRJ | Maximum flux value (uJy) in the NIR J band |
| MedianFluxNIRJ | Median flux value (uJy) in the NIR J band |
| MinFluxErrNIRJ | Minimum flux error (uJy) in the NIR J band |
| MaxFluxErrNIRJ | Maximum flux error (uJy) in the NIR J band |
| MedianFluxErrNIRJ | Median flux error (uJy) in the NIR J band |
| NoFluxFractionNIRJ | Fraction of objects without a flux detection in the NIR J band |
| SatObjectFractionNIRJ | Fraction of saturated objects in the NIR J band |
| CoverageFraction | The fraction of the tile covered by the catalog |
| NirOnlyFraction | The fraction of sources that are detected only in the NIR stack |

### [Table of Contents](https://euclid.esac.esa.int/dr/q1/dpdd/index.html)

- [Final Catalog Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#)
  - [Data Product Name](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#data-product-name)
  - [Data Product Custodian](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#data-product-custodian)
  - [Name of the Schema File](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#name-of-the-schema-file)
  - [Last Edited for DPDD Version](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#last-edited-for-dpdd-version)
  - [Processing Elements Creating / Updating / Using the Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#processing-elements-creating-updating-using-the-product)
  - [Processing Function Using the Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#processing-function-using-the-product)
  - [Proposed for Inclusion in EAS/SAS](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#proposed-for-inclusion-in-eas-sas)
  - [Data Product Elements](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#data-product-elements)
  - [Detailed Description of the Data Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#detailed-description-of-the-data-product)
    - [Main catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#main-catalog-fits-file)
    - [Morphology catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#morphology-catalog-fits-file)
    - [Cutouts catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#cutouts-catalog-fits-file)
    - [DEEP field photometry catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#deep-field-photometry-catalog-fits-file)
    - [Catalog quality parameters](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#catalog-quality-parameters)

#### Previous topic

[Background-Subtracted Mosaic Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html "previous chapter")

#### Next topic

[Segmentation Map Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_segmentationmap.html "next chapter")

### This Page

- [Show Source](https://euclid.esac.esa.int/dr/q1/dpdd/_sources/merdpd/dpcards/mer_finalcatalog.rst.txt)

### Quick search

### Navigation

- [index](https://euclid.esac.esa.int/dr/q1/dpdd/genindex.html "General Index")
- [next](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_segmentationmap.html "Segmentation Map Product") \|
- [previous](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html "Background-Subtracted Mosaic Product") \|
- [EUCL-EC-ICD-8-001 Data Product Description v2.0 (DM 10.0.4 - FDM 10.0.4 - EDEN 3.1\\
) documentation](https://euclid.esac.esa.int/dr/q1/dpdd/index.html) »
- [MER Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merindex.html) »
- [Final Catalog Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html)

──────── [TRUNCATED] ────────
Showing 89,914 chars (head) + 29,988 chars (tail) of 187,495 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/euclid.esac.esa.int-51cce7e0ba.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/euclid.esac.esa.int-51cce7e0ba.md" offset=858 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
