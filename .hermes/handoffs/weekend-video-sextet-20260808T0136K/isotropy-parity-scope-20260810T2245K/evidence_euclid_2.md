# URL: https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html

### Navigation

- [index](https://euclid.esac.esa.int/dr/q1/dpdd/genindex.html "General Index")
- [next](https://euclid.esac.esa.int/dr/q1/dpdd/nirdpd/nirindex.html "NIR Data Products") \|
- [previous](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedframecatalog.html "Vis Calibrated Catalogue Product") \|
- [EUCL-EC-ICD-8-001 Data Product Description v2.0 (DM 10.0.4 - FDM 10.0.4 - EDEN 3.1\\
) documentation](https://euclid.esac.esa.int/dr/q1/dpdd/index.html) »
- [VIS Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/visindex.html) »
- [Vis Calibrated Quad Frame Product](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html)

# Vis Calibrated Quad Frame Product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#vis-calibrated-quad-frame-product "Permalink to this heading")

## Data product name [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#data-product-name "Permalink to this heading")

DpdVisCalibratedQuadFrame

## Data product custodian [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#data-product-custodian "Permalink to this heading")

VIS

## Name of the Schema file [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#name-of-the-schema-file "Permalink to this heading")

[euc-vis-CalibratedQuadFrame.xsd](https://gitlab.euclid-sgs.uk/ST-DM/ST_DataModel/-/blob/10.0.4/ST_DM_Schema/auxdir/ST_DM_Schema/dpd/vis/euc-vis-CalibratedQuadFrame.xsd)

## Last Edited for DPDD Version [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#last-edited-for-dpdd-version "Permalink to this heading")

2.0

## Processing Element(s) creating/using the data product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#processing-element-s-creating-using-the-data-product "Permalink to this heading")

VIS\_science\_xml\_out

## Processing function using the data product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#processing-function-using-the-data-product "Permalink to this heading")

SHE and MER processing functions.

## Proposed for inclusion in EAS/SAS [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#proposed-for-inclusion-in-eas-sas "Permalink to this heading")

Yes

## Data product elements [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#data-product-elements "Permalink to this heading")

Header:

object of type sys:genericHeader

Data:

object of type vis:visCalibratedQuadFrame

QualityFlags:

object of type dqc:sqfDpdCalibratedFrame

Parameters:

object of type ppr:genericKeyValueParameters

## Detailed description of the data product [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#detailed-description-of-the-data-product "Permalink to this heading")

The VIS processing function provides a CalibratedQuadFrame product consisting of 3 FITS files per exposure:
a **calibrated VIS individual exposure**, and the corresponding **Background map** and **Weight MAP**.

A PSF file is also provided. This corresponds to the PSF part of the VisPSFModel.

In all products, pixels are delivered at the native pixel scale and all extensions have the same pixel scale and size.
Pixel data is in 32-bit floating point format.

The unit of the pixel is ADU for all product.
To convert the image to electrons you need to multiply it by the GAIN, which is expressed in e-/ADU.

To convert the image into mJy, you need to use

mAB=−2.5log10⁡(ADU)+Zp+2.5log10⁡(texp)SmJy=1023.9−mAB2.5

Some exposures cannot be used for scientific purposes, or can only be used with certain precautions. These include exposures affected by, stray light, X-rays or guidance errors.
For selected useful data, some metrics are included in the **.xml** file that follows each FITS file. See the VisAnalysisResults for how to interpret these metrics.

### Changes introduced by the PF version [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#changes-introduced-by-the-pf-version "Permalink to this heading")

#### PF 14.0 [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#pf-14-0 "Permalink to this heading")

- This data product is added in replacement of DpdVisCalibratedFrame.

- Flags definition changes.

- Contents of VIS Noise map updated.

- Invalidate quadrants which contain too many cosmic rays.

- Add PSF statistics and quality plots.


#### PF 15.0 [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#pf-15-0 "Permalink to this heading")

- Flags definition changes.

- Quadrants containing too many cosmic rays are not invalidated.

- New FITS keyword COSMICPC containing the percentage of COSMIC flagged pixels in extension.

- Astrometry: if pointing reconstruction fails, use commanded pointing instead of crashing, set PTG\_RECD to false and DpdVisCalibratedQuadFrame.Header.AutomatedValidationStatus set to INVALID.


#### PF 17.0 [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#pf-17-0 "Permalink to this heading")

- No major change in this product.


### Calibrated VIS individual exposure [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#calibrated-vis-individual-exposure "Permalink to this heading")

The calibrated VIS individual exposure is a multi-extension FITS file containing 3 extensions per quadrant, one for pixel data,
one for the associated RMS map and one for the associated Flagmap, making 432 extensions for the full 144 quadrants which constitutes an exposure.

Each extension contains the keyword **EXTNAME**, which is **<detector id>.SCI**, **<detector id>.RMS** or **<detector id>.FLG** for Science, RMS map and Flagmap respectively.
The “detector id” describes the extension following the scheme given in the VIS FPA ICD (EUCL-SAP-ICD-6-001).

#### SCI extension [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#sci-extension "Permalink to this heading")

The SCI extension contains calibrated pixel data for each of the VIS instrument quadrants.
The individual images contain both an astrometric and photometric solution written in the FITS header.

No flux scaling is applied, but the results of the photometric solution computed by VIS are written in the FITS header keywords.

The images are not background subtracted but a background map is provided as a FITS file with the same pixel size as the individual images.

The astrometric solution is described as a PV projection.
Images are not resampled and are delivered at the native VIS pixel scale (which of course means that the optical distortion of the instrument is still present).
WCSFITS is used to compute the astrometric solution. It uses a DpdVisDistortionModel of the FPA to compute the astrometric solution (pointing and position angle).
The pointing position is the centre of rotation of the FOV and is defined as the centre of the VIS FPA.

![../../_images/CCD_numbering1.png](https://euclid.esac.esa.int/dr/q1/dpdd/_images/CCD_numbering1.png)

Fig. 11 : CCD numbering and location at detector plane level (Front view) from VIS FPA ICD (EUCL-SAP-ICD-6-001) issue 2.5 2014/20/10 [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#id3 "Permalink to this image")

#### RMS extension [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#rms-extension "Permalink to this heading")

The RMS map contains the noise at each pixel in the corresponding Science image, expressed as the absolute standard deviation and are the ones to use for photometry.
It is calculated from the quadratic sum of the signal plus the readout noise.

Please note that the RMS map is not flagged/masked, it contains the invalid pixels values.

This RMS map has undergone several improvements along the different versions of the PF, which are summarised below.

**PF-13.0**

RMS maps are generated directly from the output image using the BACKGROUND\_RMS SExtractor checkimage (Bertin & Arnouts 1996).
These maps are generated by calculating the standard deviation of pixels in a sliding window on the input images, after object removal.

Note that these RMS maps only include the noise contribution from the background, and do not contain a contribution from the Poisson noise of each individual source.

**PF-14.0 and after**

The RMS map now contains the quadratic sum of the signal (background+objects in the science image) and the readout noise.

#### FLG extension [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#flg-extension "Permalink to this heading")

The Flagmap data format is defined in the [data model](http://euclid.esac.esa.int/svn/EC/SGS/ST/4-2-05-DM/schema/trunk/dictionary/bas/msk/)
and presented in VisFlagMap in a human readable format.

#### Data Header [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#data-header "Permalink to this heading")

| Primary Header |
| --- |
| SIMPLE | File does conform to FITS standard |
| BITPIX | Number of bits per data pixel |
| NAXIS | Number of data axes |
| FITS\_DEF | FITS definition name |
| EXTEND | FITS dataset may contain extensions |
| FITS\_DEF | FITS definition name |
| FITS\_VER | FITS definition version |
| TIMESYS | Time scale of the time-related keywords |
| PLAN\_ID | 32-bit SOC Operation ID |
| BUNIT | Pixel data unit, e.g. ‘electrons’ or ‘adu’ |
| OBASW | On board application software version: version. |
| DATE | UT date when this file was created |
| SOFTVERS | Version of the simulator or version of the LE1 |
| EXPTIME | Commanded integration time in seconds, e.g. 565.0 |
| IMG\_CAT | Data product category: SCIENCE, CALIB, TECHNICA |
| IMG\_T1 | values in {BIAS, DARK, FLAT, LINEARITY, CHARGE\_INJ |
| IMG\_T2 | values in {LAMP, SKY, DOME, OTHER…} from SEQU |
| OBSMODE | Observation Mode (WIDE, DEEP, CALIBRATION) |
| OBSTYPE | DP technique (IMAGE, SPECTROIMAGE) |
| INSTRUME | VIS instrument |
| TELESCOP | Telescope name: EUCLID |
| OBT\_STA1 | Integer, number of seconds of OBT (START\_TIME) |
| OBT\_STA2 | Integer, number of milliseconds of OBT (START\_TIME) |
| DATE-OBS | UTC Date of observation (start), e.g. ‘2014-03-15T09:30:09.313’ |
| MJD-OBS | Inst. seq. start time in MJD |
| FIELDID | Field Id |
| OBS\_ID | OSS\_obsid |
| DITHOBS | OSS\_inObsId |
| PTGID | OSS\_pointingID |
| EXPNUM | Exposure Id in dither |
| TOTEXP | Total number of Exposures in the specific Point |
| INSTRMOD | VIS intrument mode: Science or Manual |
| COMPALGO | Science TM compression mode: NoCompression, Co |
| COMPPARA | Science TM compression parameters: pixels/block |
| RA | OSS\_attEqLon |
| DEC | OSS\_attEqLat |
| PA | OSS\_attEqPosAngle |
| EQUINOX | Standard FK5 (years), e.g. 2000. |
| SEQID | VIS sequences as defined in EUCL-IFS-ICD-6-002 |
| DATE-END | Inst. seq. end time in UTC |
| OBT\_END1 | Integer, number of seconds of OBT (VIS sequence) |
| OBT\_END2 | Integer, number of milliseconds of OBT (VIS seq) |
| NOMCHAIN | VDGT2771 |
| VSTART | Index of first readout line (starting at 0) |
| VEND | Index of last readout line + 1 |
| ROECFGID | ROE configuration table ID |
| RSUSINID | Table version of RSU SINE table used in the RSU |
| RSUFRID | Table version of RSU FREQ table used in the RSU |
| RSUSFRID | Table version of RSU short FREQ table used in t |
| RSUCFSTA | Shutter unit configuration status: CLOSED\_LOOP, |
| TP\_STAT | Trap pumping status: off, parallel, serial, mul |
| CUSTATUS | Calibration unit status: On or Off |
| CI\_STAT | Charge injection status: On or Off |
| IDLTIME | Time (s) between end of shutter opening or end |
| OBT\_STA | OBT at start time |
| DATE-ENH | UTC of LE1 Enhancement |
| AUX\_VERS | LE1 Enh. (AUX) Processor name & version |
| ELAT | OSS\_attEclipLat |
| ELONG | OSS\_attEclipLon |
| POS | OSS\_attEclipPosAngle |
| ALPHA | OSS\_alpha |
| BETA | OSS\_beta |
| SAA | OSS\_saa |
| PATCH\_ID | OSS\_obsPatchId |
| FOV\_LAT1 | OSS\_fovLat1 |
| FOV\_LAT2 | OSS\_fovLat2 |
| FOV\_LAT3 | OSS\_fovLat3 |
| FOV\_LAT4 | OSS\_fovLat4 |
| FOV\_LON1 | OSS\_fovLon1 |
| FOV\_LON2 | OSS\_fovLon2 |
| FOV\_LON3 | OSS\_fovLon3 |
| FOV\_LON4 | OSS\_fovLon4 |
| VS1T2043 | VS1T2043 |
| VS1T2050 | VS1T2050 |
| VS1T2020 | VS1T2020 |
| VS1T2021 | VS1T2021 |
| VS1T2028 | VS1T2028 |
| VS1T2029 | VS1T2029 |
| VS1T2036 | VS1T2036 |
| VS1T2037 | VS1T2037 |
| VS2T2043 | VS2T2043 |
| VS2T2050 | VS2T2050 |
| VS2T2020 | VS2T2020 |
| VS2T2021 | VS2T2021 |
| VS2T2028 | VS2T2028 |
| VS2T2029 | VS2T2029 |
| VS2T2036 | VS2T2036 |
| VS2T2037 | VS2T2037 |
| VS3T2043 | VS3T2043 |
| VS3T2050 | VS3T2050 |
| VS3T2020 | VS3T2020 |
| VS3T2021 | VS3T2021 |
| VS3T2028 | VS3T2028 |
| VS3T2029 | VS3T2029 |
| VS3T2036 | VS3T2036 |
| VS3T2037 | VS3T2037 |
| VS4T2043 | VS4T2043 |
| VS4T2050 | VS4T2050 |
| VS4T2020 | VS4T2020 |
| VS4T2021 | VS4T2021 |
| VS4T2028 | VS4T2028 |
| VS4T2029 | VS4T2029 |
| VS4T2036 | VS4T2036 |
| VS4T2037 | VS4T2037 |
| VS5T2043 | VS5T2043 |
| VS5T2050 | VS5T2050 |
| VS5T2020 | VS5T2020 |
| VS5T2021 | VS5T2021 |
| VS5T2028 | VS5T2028 |
| VS5T2029 | VS5T2029 |
| VS5T2036 | VS5T2036 |
| VS5T2037 | VS5T2037 |
| VS6T2043 | VS6T2043 |
| VS6T2050 | VS6T2050 |
| VS6T2020 | VS6T2020 |
| VS6T2021 | VS6T2021 |
| VS6T2028 | VS6T2028 |
| VS6T2029 | VS6T2029 |
| VS6T2036 | VS6T2036 |
| VS6T2037 | VS6T2037 |
| VS7T2043 | VS7T2043 |
| VS7T2050 | VS7T2050 |
| VS7T2020 | VS7T2020 |
| VS7T2021 | VS7T2021 |
| VS7T2028 | VS7T2028 |
| VS7T2029 | VS7T2029 |
| VS7T2036 | VS7T2036 |
| VS7T2037 | VS7T2037 |
| VS8T2043 | VS8T2043 |
| VS8T2050 | VS8T2050 |
| VS8T2020 | VS8T2020 |
| VS8T2021 | VS8T2021 |
| VS8T2028 | VS8T2028 |
| VS8T2029 | VS8T2029 |
| VS8T2036 | VS8T2036 |
| VS8T2037 | VS8T2037 |
| VS9T2043 | VS9T2043 |
| VS9T2050 | VS9T2050 |
| VS9T2020 | VS9T2020 |
| VS9T2021 | VS9T2021 |
| VS9T2028 | VS9T2028 |
| VS9T2029 | VS9T2029 |
| VS9T2036 | VS9T2036 |
| VS9T2037 | VS9T2037 |
| VSAT2043 | VSAT2043 |
| VSAT2050 | VSAT2050 |
| VSAT2020 | VSAT2020 |
| VSAT2021 | VSAT2021 |
| VSAT2028 | VSAT2028 |
| VSAT2029 | VSAT2029 |
| VSAT2036 | VSAT2036 |
| VSAT2037 | VSAT2037 |
| VSBT2043 | VSBT2043 |
| VSBT2050 | VSBT2050 |
| VSBT2020 | VSBT2020 |
| VSBT2021 | VSBT2021 |
| VSBT2028 | VSBT2028 |
| VSBT2029 | VSBT2029 |
| VSBT2036 | VSBT2036 |
| VSBT2037 | VSBT2037 |
| VSCT2043 | VSCT2043 |
| VSCT2050 | VSCT2050 |
| VSCT2020 | VSCT2020 |
| VSCT2021 | VSCT2021 |
| VSCT2028 | VSCT2028 |
| VSCT2029 | VSCT2029 |
| VSCT2036 | VSCT2036 |
| VSCT2037 | VSCT2037 |
| POS\_X | OEM\_x |
| POS\_Y | OEM\_y |
| POS\_Z | OEM\_z |
| VEL\_X | OEM\_vx |
| VEL\_Y | OEM\_vy |
| VEL\_Z | OEM\_vz |
| CALBLKID | OSS\_obsType |
| CALBLKVR | OSS\_variant |
| DATASETR | PPO DataSetRelease |
| N\_CCD | Number of CCD |
| BIASSEC | Offset area relative to readout, 1-based |
| MAGZEROP | zero-point |
| PHOT\_ERR | self calibration photometric error |
| PHOTIRMS | self calibration mag dispersion RMS |
| APERCORR | self calibration aperture correction MAG\_50pix - MAG\_13pix |
| APCORRMS | self calibration aperture correction rms error |

| Extension Header For CalibratedFrame |
| --- |
| XTENSION | IMAGE extension |
| BITPIX | Number of bits per data pixel |
| NAXIS | Number of data axes |
| NAXIS1 | Length of data axis 1 |
| NAXIS2 | Length of data axis 2 |
| PCOUNT | Required keyword; must = 0 |
| GCOUNT | Required keyword; must = 1 |
| EXTNAME | Format: CCD row-CCD column.quadrant id, e.g. 2.3-H |
| DETID | CCD-ID field from science TM (0-35) |
| CCDID | e.g. Detector ID, e.g. ‘0-0’, ‘1-1’ … ‘6-6’ |
| ROEID | ROE ID: 1-12 |
| ROECTV | ROE configuration table version |
| BUNIT | Pixel data unit, e.g. ‘electrons’ or ‘adu’ |
| PRESCANX | number of serial prescan pixels, e.g 51 |
| OVRSCANX | number of serial overscan pixels, e.g 29 |
| OVRSCANY | number of parallel overscan pixels, e.g 20 |
| EXPDUR1 | Nominal/Short, nominal with CI, Flat: duration |
| EXPDUR2 | Nominal/Short, nominal with CI, Flat: duration |
| CRVAL1 | Right ascension at ref pixel |
| CRVAL2 | Declination at ref pixel |
| CRPIX1 | Reference pixel x coordinate |
| CRPIX2 | Reference pixel y coordinate |
| CD1\_1 | Translation matrix element |
| CD1\_2 | Translation matrix element |
| CD2\_1 | Translation matrix element |
| CD2\_2 | Translation matrix element |
| CTYPE1 | Coordinamte 1 type |
| CTYPE2 | Coordinamte 2 type |
| CUNIT1 | Physical units of CRVAL1 |
| CUNIT2 | Physical units of CRVAL2 |
| WCSAXES | Number of coordinate axes |
| CMPRTSCI | Quadrant image compression ratio obtained on-board |
| GAIN | Maximum equivalent gain (e-/ADU) |
| RDNOISE | Read out Noise |
| RA | Commanded FPA pointing right ascension (deg) |
| DEC | Commanded FPA pointing declination (deg) |
| PA | Commanded FPA pointing position angle (deg) |
| EXPTIME | Commanded integration time in seconds, e.g. 565.0 |
| SATLEVEL | Pixel saturation level in e- |
| SATURATE | Pixel saturation level in ADU |
| BIAS\_TOP | bias\_cfg\[“main\_bias\_line\_end”\] |
| BIAS\_BTM | bias\_cfg\[“main\_bias\_line\_start”\] |
| BIAS\_LFT | bias\_cfg\[“main\_bias\_col\_start”\] |
| BIAS\_RGT | bias\_cfg\[“main\_bias\_col\_end”\] |
| GAINCORR | ref\_gain/cal\_gain |
| LSFCORR | True if the LargeScaleFlat corection was applied |
| COSMICPC | percent of COSMIC flagged pixels in extension |
| STDCRMS |  |
| NUMBRMS |  |
| AVGRESID | VIS mean residual |
| PV1\_1 |  |
| PV2\_1 |  |
| PV1\_2 |  |
| PV2\_2 |  |
| PV1\_4 |  |
| PV2\_4 |  |
| PV1\_5 |  |
| PV2\_5 |  |
| PV1\_6 |  |
| PV2\_6 |  |
| PV1\_7 |  |
| PV2\_7 |  |
| PV1\_8 |  |
| PV2\_8 |  |
| PV1\_9 |  |
| PV2\_9 |  |
| PV1\_10 |  |
| PV2\_10 |  |
| RA\_COMM | commanding pointing RA |
| DEC\_COMM | commanding pointing DEC |
| PA\_COMM | commanding position angle |
| REFCAT | reference star catalogue file |
| FPAMODEL | fpa model file |
| MAGZEROP | zero-point |
| PHOT\_ERR | self calibration photometric error |
| PHOTIRMS | self calibration mag dispersion RMS |
| APERCORR | self calibration aperture correction MAG\_50pix - MAG\_13pix |
| APCORRMS | self calibration aperture correction rms error |
| FLXSCALE | Flux scaling for stacked exposure |

### Weight Map [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#weight-map "Permalink to this heading")

When combining multiple dithered exposures from separate detectors with gaps it becomes important to assign a “confidence” to each detector pixel so that overlapping exposures can be
combined and the noise level at each pixel can be correctly estimated.
When combining individual exposures into stacks, this is the product to use as a weight map.

Internally, the VIS processing function uses relative “weight maps”, which are defined as wj∝1σj2,
where σj is the standard deviation (or “RMS”) of the jth pixel.

At the end it corresponds to the small scale flat (PRNU) with all pixels having the invalid flag set to 0. This corresponds only to the background, not the object.

#### Data Header [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#id1 "Permalink to this heading")

| Primary Header for Weight Map |
| --- |
| SIMPLE | conforms to FITS standard |
| BITPIX | array data type |
| NAXIS | number of array dimensions |
| EXTEND |  |

| Extension Header for Weight Map |
| --- |
| XTENSION | Image extension |
| BITPIX | array data type |
| NAXIS | number of array dimensions |
| NAXIS1 |  |
| NAXIS2 |  |
| PCOUNT | Number of parameters |
| GCOUNT | Number of groups |
| EXTNAME |  |
| CCDID |  |
| WCSAXES |  |
| CTYPE1 | Coordinamte 1 type |
| CTYPE2 | Coordinamte 2 type |
| CUNIT1 | Physical units of CRVAL1 |
| CUNIT2 | Physical units of CRVAL2 |
| CRPIX1 |  |
| CRPIX2 |  |
| CD1\_1 |  |
| CD1\_2 |  |
| CD2\_1 |  |
| CD2\_2 |  |
| CRVAL1 |  |
| CRVAL2 |  |
| STDCRMS |  |
| NUMBRMS |  |
| AVGRESID |  |
| PV1\_1 |  |
| PV2\_1 |  |
| PV1\_2 |  |
| PV2\_2 |  |
| PV1\_4 |  |
| PV2\_4 |  |
| PV1\_5 |  |
| PV2\_5 |  |
| PV1\_6 |  |
| PV2\_6 |  |
| PV1\_7 |  |
| PV2\_7 |  |
| PV1\_8 |  |
| PV2\_8 |  |
| PV1\_9 |  |
| PV2\_9 |  |
| PV1\_10 |  |
| PV2\_10 |  |
| RA\_COMM | commanding pointing RA |
| DEC\_COMM | commanding pointing DEC |
| PA\_COMM | commanding position angle |
| RA | reconstructed pointing RA |
| DEC | reconstructed pointing DEC |
| PA | reconstructed position angle |
| REFCAT | reference star catalogue file |
| FPAMODEL | fpa model file |

### Background Map [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#background-map "Permalink to this heading")

The background map delivered is calculated using NoiseChisel.

In PF V15.0.4 the background calculation changes, using NoiseChisel instead of SExtractor background check image.

NoiseChisel seems to capture the straylight very well.

As NoiseChisel is more sensitive to cosmic we have implemented some fall-back in case of crash.
The type of background calculation can be found in the VisAnalysisResults associated with these different values:

- NC1 : NoiseChisel methode 1

- NC2 : NoiseChisel methode 2

- HISTMODE : Mod of the image

- SExtractor : SourceExtractor background


#### Data Header [¶](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html\#id2 "Permalink to this heading")

| Primary Header for Background Map |
| --- |
| SIMPLE | This is a FITS file |
| BITPIX |  |
| NAXIS |  |
| EXTEND | This file may contain FITS extensions |
| NEXTEND | Number of extensions |
| MAGZEROP | zero-point |
| PHOT\_ERR | self calibration photometric error |
| PHOTIRMS | self calibration mag dispersion RMS |
| APERCORR | self calibration aperture correction MAG\_50pix - MAG\_13pix |
| APCORRMS | self calibration aperture correction rms error |
| EXPTIME | Commanded integration time in seconds, e.g. 565.0 |

| Extension Header for Background Map |
| --- |
| XTENSION | Image extension |
| BITPIX | array data type |
| NAXIS | number of array dimensions |
| NAXIS1 |  |
| NAXIS2 |  |
| PCOUNT | Number of parameters |
| GCOUNT | Number of groups |
| EXTNAME |  |
| DETID | CCD-ID field from science TM (0-35) |
| CCDID | Detector ID, e.g. ‘0-0’, ‘1-1’ … ‘6-6’ |
| ROEID | ROE ID: 1-12 |
| ROECTV | ROE configuration table version |
| BUNIT | Pixel data unit, e.g. ‘electrons’ or ‘adu’ |
| PRESCANX | Number of serial prescan pixels, e.g 51 |
| OVRSCANX | Number of serial overscan pixels, e.g 29 |
| OVRSCANY | Number of parallel overscan pixels, e.g 20 |
| EXPDUR1 | Nominal/Short, nominal with CI, Flat: duration |
| EXPDUR2 | Nominal/Short, nominal with CI, Flat: duration |
| CRVAL1 |  |
| CRVAL2 |  |
| CRPIX1 |  |
| CRPIX2 |  |
| CD1\_1 |  |
| CD1\_2 |  |
| CD2\_1 |  |
| CD2\_2 |  |
| CTYPE1 | Coordinamte 1 type |
| CTYPE2 | Coordinamte 2 type |
| CUNIT1 | Physical units of CRVAL1 |
| CUNIT2 | Physical units of CRVAL2 |
| WCSAXES |  |
| CMPRTSCI | Quadrant image compression ratio obtained on-board |
| GAIN |  |
| RDNOISE |  |
| RA | reconstructed pointing RA |
| DEC | reconstructed pointing DEC |
| PA | reconstructed position angle |
| EXPTIME | Commanded integration time in seconds, e.g. 565.0 |
| SATLEVEL | pixel saturation level in e- |
| SATURATE | pixel saturation level in ADU |
| BIAS\_TOP |  |
| BIAS\_BTM |  |
| BIAS\_LFT |  |
| BIAS\_RGT |  |
| GAINCORR | ref\_gain/cal\_gain |
| BIASLVLE |  |
| BIASRONE |  |
| BIASLVLF |  |
| BIASRONF |  |
| BIASLVLG |  |
| BIASRONG |  |
| BIASLVLH |  |
| BIASRONH |  |
| LSFCORR |  |
| COSMICPC | percent of COSMIC flagged pixels in extension |
| STDCRMS |  |
| NUMBRMS |  |
| AVGRESID |  |
| PV1\_1 |  |
| PV2\_1 |  |
| PV1\_2 |  |
| PV2\_2 |  |
| PV1\_4 |  |
| PV2\_4 |  |
| PV1\_5 |  |
| PV2\_5 |  |
| PV1\_6 |  |
| PV2\_6 |  |
| PV1\_7 |  |
| PV2\_7 |  |
| PV1\_8 |  |
| PV2\_8 |  |
| PV1\_9 |  |
| PV2\_9 |  |
| PV1\_10 |  |
| PV2\_10 |  |
| RA\_COMM | Commanding pointing RA |
| DEC\_COMM | Commanding pointing DEC |
| PA\_COMM | Commanding position angle |
| REFCAT | reference star catalogue file |
| FPAMODEL |  |
| MAGZEROP | zero-point |
| PHOT\_ERR | self calibration photometric error |
| PHOTIRMS | self calibration mag dispersion RMS |
| APERCORR | self calibration aperture correction MAG\_50pix - MAG\_13pix |
| APCORRMS | self calibration aperture correction rms error |
| FLXSCALE | Flux scaling for stacked exposure |
| CCD\_RA | CCD center right ascension |
| CCD\_DEC | CCD center declination |
| BKG\_MED | CCD bkg median value in MJY/sr |
| BKG\_MAD | CCD bkg median absolute deviation in MJy/sr |

### [Table of Contents](https://euclid.esac.esa.int/dr/q1/dpdd/index.html)

- [Vis Calibrated Quad Frame Product](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#)
  - [Data product name](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#data-product-name)
  - [Data product custodian](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#data-product-custodian)
  - [Name of the Schema file](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#name-of-the-schema-file)
  - [Last Edited for DPDD Version](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#last-edited-for-dpdd-version)
  - [Processing Element(s) creating/using the data product](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#processing-element-s-creating-using-the-data-product)
  - [Processing function using the data product](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#processing-function-using-the-data-product)
  - [Proposed for inclusion in EAS/SAS](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#proposed-for-inclusion-in-eas-sas)
  - [Data product elements](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#data-product-elements)
  - [Detailed description of the data product](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#detailed-description-of-the-data-product)
    - [Changes introduced by the PF version](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#changes-introduced-by-the-pf-version)
      - [PF 14.0](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#pf-14-0)
      - [PF 15.0](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#pf-15-0)
      - [PF 17.0](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#pf-17-0)
    - [Calibrated VIS individual exposure](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#calibrated-vis-individual-exposure)
      - [SCI extension](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#sci-extension)
      - [RMS extension](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#rms-extension)
      - [FLG extension](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#flg-extension)
      - [Data Header](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#data-header)
    - [Weight Map](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#weight-map)
      - [Data Header](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#id1)
    - [Background Map](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#background-map)
      - [Data Header](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html#id2)

#### Previous topic

[Vis Calibrated Catalogue Product](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedframecatalog.html "previous chapter")

#### Next topic

[NIR Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/nirdpd/nirindex.html "next chapter")

### This Page

- [Show Source](https://euclid.esac.esa.int/dr/q1/dpdd/_sources/visdpd/dpcards/vis_calibratedquadframe.rst.txt)

### Quick search

### Navigation

- [index](https://euclid.esac.esa.int/dr/q1/dpdd/genindex.html "General Index")
- [next](https://euclid.esac.esa.int/dr/q1/dpdd/nirdpd/nirindex.html "NIR Data Products") \|
- [previous](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedframecatalog.html "Vis Calibrated Catalogue Product") \|
- [EUCL-EC-ICD-8-001 Data Product Description v2.0 (DM 10.0.4 - FDM 10.0.4 - EDEN 3.1\\
) documentation](https://euclid.esac.esa.int/dr/q1/dpdd/index.html) »
- [VIS Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/visindex.html) »
- [Vis Calibrated Quad Frame Product](https://euclid.esac.esa.int/dr/q1/dpdd/visdpd/dpcards/vis_calibratedquadframe.html)