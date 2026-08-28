URL: https://fermi.gsfc.nasa.gov/ssc/data/access/data_products.html

[Skip to main content](https://fermi.gsfc.nasa.gov/ssc/data/access/data_products.html#main-content)

FSSC: Data : Data Access : Data Products

# Fermi Data Products

This page lists the science data products created by the the LAT Instrument and Science Operation Center (LISOC) and GBM Instrument Operations Center (GIOC) and sent to the FSSC. A more complete description is given in the
[Science Data Products Interface Control Document](https://fermi.gsfc.nasa.gov/ssc/library/support/Science_DP_ICD_RevA.pdf), and details of the file formats can be found in the [Science Data Products File Format Document](https://fermi.gsfc.nasa.gov/ssc/library/support/Science_DP_FFD_RevA.pdf).

## LAT Data Products

The following data products are created by the LISOC and sent to the FSSC after each downlink from the spacecraft (6-8 per day).

| ID | Name | Description |
| --- | --- | --- |
| LS-001 | LAT Events | Large number of parameters describing a large subset of the events telemetered to the ground (many did not result from photons). |
| LS-002 | LAT photons | Selected parameters from the subset of events identified as gamma-ray photons |
| LS-005 | LAT Pointing and Livetime History | LAT orientation and mode at 30-second intervals; used to calculate exposures |
| LS-020 | LAT Pointing and Livetime History | LAT orientation and mode at 1-second intervals; used to calculate exposures |

The following data products are created periodically.

| ID | Name | Description |
| --- | --- | --- |
| LS-008 | LAT Source Catalog | Table of detected gamma-ray sources with derived information |
| LS-010 | Interstellar Emission Model | Model for diffuse gamma-ray emission from the Milky Way, input for high-level data analysis; refined using Fermi data. The Interstellar Emission Model is incorporated into the the Fermitools. However, investigators may occasionally need to obtain updates of this model from the FSSC web site. |

For more detailed information, see:

- [Event reconstruction, classification, and event classes](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/lat_data_products.html)
- [LAT data file column descriptions](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/lat_data_columns.html)
- [Gaps in LAT data coverage](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/lat_data_gaps.html)
- [LAT background models](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/BackgroundModels.html)
- [Caveats about LAT data](https://fermi.gsfc.nasa.gov/ssc/data/analysis/LAT_caveats.html)

## GBM Data Products

### GBM Daily Data Products

The following data products are created daily by the GIOC and sent to the FSSC, regardless of whether a gamma-ray burst has been detected, within 24 hours after the GIOC receives the last input data.

On 26 November 2012, the GBM flight software was updated to allow
operation in a new data-taking mode. In nominal operation mode, the GBM
is now continuously recording and sending to the ground time-tagged
events (TTE) with 2 μs precision, synchronized to GPS once per
second. This new operating mode produces continuous TTE files in
addition to the snippets currently available around a GBM trigger. The
previous 330-second window of the trigger TTE has been expanded to
include more pre-trigger background and longer coverage
post-trigger. Both trigger and continuous TTE files are provided
through the HEASARC FTP site and via the Browse interface in the GBM
Daily products. This continuous TTE mode is throttled in selected
(nominally, sun-facing) detectors at times of high solar activity to
avoid telemetry volume problems at the spacecraft and mission
operations level. During those times, the trigger TTE reverts
to the nominal 330-second window.

| ID | Name | Description |
| --- | --- | --- |
| GS-001 | CTIME (daily version) | The counts accumulated every 0.256 seconds in 8 energy channels for each of the 14 detectors. |
| GS-002 | CSPEC (daily version) | The counts accumulated every 8.192 seconds in 128<br> energy channels for each of the 14 detectors. |
| GS-003 | TTE (continuous version) | Event data for each detector with a time precise<br> to 2 microseconds, in 128 energy channels. These<br> files were replaced by the GS-013 hourly TTE files in 2012 for new triggers. The downlink schedule determined how many data files are produced each day. |

| GS-005 | GBM gain and energy resolution history | History of the detector gains and energy<br> resolutions; required for calculating Detector<br> Response Matrices (DRMs). |
| GS-006 | Fermi position and attitude history | History of Fermi's position and attitude, required for calculating DRMs. |
| GS-013 | TTE (hourly version) | Time tagged events for each detector which occurred during the hour (including up to the last 120 seconds of events from the previous hour) with a time precise to 2 microseconds, in 128 energy channels. |

CTIME and CSPEC are PHA FITS files (i.e., files with a format that is standard for spectra), and therefore users may have software that accesses these files. The GS-005 and GS-006 data products can be accessed by Fermi software.

### GBM Trigger and Burst Data Products

The following data products are created by the GIOC and sent to the
FSSC whenever a trigger has been detected, regardless of whether the
trigger resulted from a gamma-ray burst (for example, a solar flare or an
electron precipitation event may have caused the trigger). These data
products have a latency of 1 day. Any of the products may be updated
with new versions after the initial delivery.
In particular, the catalog entry files (GS-105,
GS-106, and GS-109) may be updated as trigger parameters are refined.

| ID | Name | Description |
| --- | --- | --- |
| GS-101 | CTIME (burst version) | For each detector, the counts accumulated every 0.064 s in 8 energy channels |
| GS-102 | CSPEC (burst version) | For each detector, the counts accumulated every 1.024 s in 128 energy channels. |
| GS-103 | GBM TTE (burst version) | Event data for the burst. There is one file for each detector. |
| GS-104 | GBM DRMs | 8 and 128 energy channel Detector Response<br> Matrices (DRMs) for all 14 detectors. These files may<br> not be produced for all triggers. |
| GS-105 | GBM Trigger Catalog Entry | Classification of GBM trigger with some<br> characteristics (e.g., trigger time, coordinates). This file is used to create the [GBM\<br> Trigger Catalog](http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigtrig.html). |
| GS-107 | GBM TRIGDAT | All the GBM's messages downlinked through TDRSS. These messages are the basis of the GCN Notices for the burst. |
|  | Quicklook Plots | Lightcurves and spacecraft pointing history files in GIF and PDF format. |

For triggers classified as gamma-ray bursts, the following products
may also be available. The burst and spectral catalog entry files have longer latency than
the other trigger files. The GS-109 spectral catalog entry files are only released when a new GRB catalog is published.

| ID | Name | Description |
| --- | --- | --- |
| GS-106 | GBM Burst Catalog Entry | Parameters describing the burst<br> (e.g., durations, fluences). This file is used to create [GBM\<br> Burst Catalog](http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigbrst.html). |
| GS-109 | GBM Spectral Catalog Entry | Parameters describing the burst<br> spectra (e.g., models and fits). The results are added to the [GBM\<br> Burst Catalog](http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigbrst.html). |
| GS-110 | GBM Localization File | Text file giving the right ascension and<br> declination values corresponding to the chi-squared<br> minima, 1σ, 2σ, and 3σ contours of<br> the GBM localization. A PNG plot is also provided. |
| GS-112 | GBM HEALPix Localization File | FITS File providing the full-sky localization<br> posterior and significance distributions of<br> GBM-localized GRBs stored as HEALPix arrays. These<br> files additionally contain the equatorial location of<br> the Geocenter, sun, and the equatorial pointings of<br> each GBM detector at the time of the GRB. A PNG skymap<br> is also provided. |

The Fermi software analyzes the TTE data (GS-103) using the response functions (GS-104) specific to a particular trigger.

### GBM Periodic Data Products

The following data products are created by the GIOC and sent to the FSSC from time to time.

| ID | Name | Description | Latency |
| --- | --- | --- | --- |
| GS-007 | GBM PHA Look-Up Tables | Tables of the correspondence between CTIME and CSPEC energy channels and the photopeak energy for each detector | Updated as warranted |
| GS-009 | GBM Low Level Threshold File | Records periods of non-standard Low Level Threshold (LLT) operation. See the [LLT Settings Page](https://fermi.gsfc.nasa.gov/ssc/data/access/gbm/llt_settings.html). | Updated periodically |
|  | WWLLN Lightning Maps and Data files | Maps of the lightning detections made by WWLLN and<br> text data files with the positions and times of<br> the lightning sferics on the maps. See the [TGF Catalog Page](https://fermi.gsfc.nasa.gov/ssc/data/access/gbm/tgf). | Updated periodically |

For more detailed information, see:

- [GBM Data Descriptions](https://fermi.gsfc.nasa.gov/ssc/data/access/gbm/gbm_data_products.html)
- [GBM Data Gaps](https://fermi.gsfc.nasa.gov/ssc/data/access/gbm/gbm_data_gaps.html)
- [GBM Data Caveats](https://fermi.gsfc.nasa.gov/ssc/data/analysis/GBM_caveats.html)
