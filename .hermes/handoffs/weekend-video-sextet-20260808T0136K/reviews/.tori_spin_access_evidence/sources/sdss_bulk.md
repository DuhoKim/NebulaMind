SOURCE URL: https://www.sdss4.org/dr17/data_access/bulk/
TITLE: Bulk Data Downloads | SDSS
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

# Bulk Data Downloads

[Table of Contents](https://www.sdss4.org/dr17/data_access/bulk/#toc-body)

- Bulk Data Downloads

  - Globus Online
  - APOGEE Catalog Data
  - APOGEE Spectra Per-Star Files
  - Optical Spectra Versions
  - Optical Spectra Catalog Data
  - Optical Spectra Per-Object Files
  - Optical Spectra Per-Object Lite Files
  - Spectra per-Plate Files
  - Imaging Data
  - Interferometry Data

All data can be downloaded directly from [data.sdss.org](https://data.sdss.org/sas) using the [rsync](http://rsync.samba.org/) or [wget](https://www.gnu.org/software/wget/) commands. Access is also available via [Globus Online](http://www.globus.org/). The [Data Model](https://data.sdss.org/datamodel/) page has a description of the directory structure and file formats. Note that the total SDSS data volume is > 650 TB; see [the data volume table](https://www.sdss4.org/dr17/data_access/volume/). If you need a substantial fraction of that data (>1 TB), please contact [the helpdesk](mailto:helpdesk@sdss.org) to arrange a custom data transfer. This will be faster for you and easier on our servers.

To learn how to download MaNGA data cubes, see the [MaNGA data access](https://www.sdss4.org/dr17/manga/manga-data/data-access/) page.

**NOTE**: all rsync commands on this page have `--dry-run` added to them, and all wget commands have `--spider` added to them. You have to **remove those command line arguments** for these commands **to actually download data**. Also, wget commands use the same URL as you would in a web browser, _e.g._,

```
wget --spider https://data.sdss.org/sas/dr17/eboss/spectro/redux/v5_13_2/platelist.fits
```

yet, for rsync, drop the "sas" from the URL, _e.g._,

```
rsync --dry-run -lv rsync://dtn.sdss.org/dr17/eboss/spectro/redux/v5_13_2/platelist.fits .
```

If you are having any difficulty with rsync URLs, check the notes below. The number of rsync connections is throttled but the number of wget connections is not. Thus it is recommended to use wget to initially fetch the data, and use rsync only to confirm that the data you have is correct and complete.

## Globus Online

SDSS data are also available via [Globus Online](http://www.globus.org/) using the endpoint `sdss#public` (US Mountain). For large transfers, Globus is significantly faster and more robust than using wget or rsync. Globus Online requires a separate account, but once that is set up Globus offers a "fire-and-forget" transfer that automatically optimizes transfer settings, retries any failures, and emails you when your transfer is done. The [Globus Connect](http://www.globus.org/globus-connect/) tool allows you to use globus to download data to your laptop or other computers which are not permanent Globus endpoint servers.

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## APOGEE Catalog Data

(see also the [APOGEE data access page](https://www.sdss4.org/dr17/irspec/spectro_data/), with more details on the various APOGEE spectra and data products available)

Catalogs of parameters derived from the APOGEE infrared spectra and matched are documented on the [spectra data page](https://www.sdss4.org/dr17/irspec/). These can be directly downloaded from the links on that page, or via wget commands.

For example, to download the stellar parameters and element abundance information for the entire APOGEE stellar sample:

```
wget --spider https://data.sdss.org/sas/dr17/apogee/spectro/aspcap/dr17/synspec_rev1/allStar-dr17-synspec_rev1.fits
```

To download the catalog information for each APOGEE visit spectrum:

```
wget --spider https://data.sdss.org/sas/dr17/apogee/spectro/aspcap/dr17/synspec_rev1/allVisit-dr17-synspec_rev1.fits
```

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## APOGEE Spectra Per-Star Files

The combined spectra for each star can be found in the [apStar](https://data.sdss.org/datamodel/files/APOGEE_REDUX/APRED_VERS/stars/TELESCOPE/FIELD/apStar.html) files. In the path to this file, `APRED_VERS` refers to the reduction version used to extract the spectrum for each visit.

There is a [large directory of location IDs](https://data.sdss.org/sas/dr17/apogee/spectro/redux/dr17/stars/apo25m/), each of which corresponds to a particular pointing/line of sight in the survey observed from APO (see [here](https://data.sdss.org/sas/dr17/apogee/spectro/redux/dr17/stars/lco25m/) for the same direcotry for LCO). Within each of those directories, the spectra are organized by their APOGEE ID. For example, one of these files may be downloaded as follows:

```
wget --spider https://data.sdss.org/sas/dr17/apogee/spectro/redux/dr17/stars/apo25m/000+02/apStar-dr17-2M17335483-2753043.fits
```

In this case, `APRED_VERS` is `dr17` and `APSTAR_VERS` is `stars`.

To download these spectra in bulk, you can generate a list of spectra you wish to download in a text file where each line looks like "\[LOCATIONID\]/\[FILENAME\]", for example:

```
000+02/apStar-dr17-2M17335483-2753043.fits
```

Then use wget:

```
wget --spider -nv -r -nH --cut-dirs=6 \
-i speclist.txt \
-B https://data.sdss.org/sas/dr17/apogee/spectro/redux/dr17/stars/apo25m/
```

To download all of the apStar files (about 505 GB total), it is best to use rsync:

```
rsync --dry-run -aLvz --include "[0-9][0-9][0-9][0-9]/" \
--include "apStar-*[0-9][0-9][0-9][0-9][0-9][0-9][0-9].fits" --exclude "*"\
--prune-empty-dirs --progress \
rsync://dtn.sdss.org/dr17/apogee/spectro/redux/dr17/stars/apo25m stars/apo25m
```

Note that all these examples so far have been for stars observed at Apache Point Observatory in the North. For stars observed at Las Campanas Observatory in the South, substitute **apo25m** with **lco25m**.

The majority of the stars have stellar parameters determined, with corresponding best-fit, pseudo-continuum-normalized spectra. The combined spectra for each star, along with the ASPCAP fits, can be found in the [aspcapStar](https://data.sdss.org/datamodel/files/APOGEE_ASPCAP/APRED_VERS/ASPCAP_VERS/TELESCOPE/FIELD/aspcapStar.html) files. As for `aspcapStar` files, there is a [large directory of location IDs](https://data.sdss.org/sas/dr17/apogee/spectro/aspcap/dr17/synspec_rev1/apo25m/) with the resulting files (observed from APO). For example, one of these files may be downloaded as follows:

```
wget --spider https://data.sdss.org/sas/dr17/apogee/spectro/aspcap/dr17/synspec_rev1/apo25m/000+02/aspcapStar-dr17-2M17335483-2753043.fits
```

To download these spectra in bulk, you can generate a list of spectra you wish to download in a text file where each line looks like "\[LOCATIONID\]/\[FILENAME\]", for example:

```
000+02/apo25m/aspcapStar-dr17-2M17335483-2753043.fits
```

Then use wget:

```
wget --spider -nv -r -nH --cut-dirs=6 \
-i speclist.txt \
-B https://data.sdss.org/sas/dr17/apogee/spectro/aspcap/dr17/synspec_rev1/apo25m/
```

To download all of the aspcapStar files (over 40 GB total), it is best to use rsync:

```
rsync --dry-run -aLvz --include "[0-9][0-9][0-9][0-9]/" \
--include "aspcapStar*.fits" --exclude "*"\
--prune-empty-dirs --progress \
rsync://dtn.sdss.org/dr17/apogee/spectro/aspcap/dr17/synspec_rev1/apo25m/
```

For APOGEE-2S stars observed from Las Campanas Observatory, substitute again apo25m with lco25m.

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## Optical Spectra Versions

The SDSS optical spectra are split into several versions:

- eBOSS, BOSS and SEQUELS spectra:
  - [https://data.sdss.org/sas/dr17/eboss/spectro/redux/v5\_13\_2/](https://data.sdss.org/sas/dr17/eboss/spectro/redux/v5_13_2/spectra)
- SDSS-I/-II spectra:
  - Legacy survey: [data.sdss.org/sas/dr17/sdss/spectro/redux/26/](https://data.sdss.org/sas/dr17/sdss/spectro/redux/26/spectra/)
  - SDSS stellar cluster plates: [data.sdss.org/sas/dr17/sdss/spectro/redux/103/](https://data.sdss.org/sas/dr17/sdss/spectro/redux/103/spectra/)
  - SDSS SEGUE-2 plates: [data.sdss.org/sas/dr17/sdss/spectro/redux/104/](https://data.sdss.org/sas/dr17/sdss/spectro/redux/104/spectra/)

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## Optical Spectra Catalog Data

Catalogs of parameters derived from the SDSS/BOSS/SEQUELS/eBOSS optical spectra and matched to photometric data are documented on the [optical spectra data page](https://www.sdss4.org/dr17/spectro/). These can be directly downloaded from the links on that page, or via wget commands. For example, to download the redshifts and classifications of all SDSS spectra (6.7 GB):

```
wget --spider https://data.sdss.org/sas/dr17/sdss/spectro/redux/specObj-dr17.fits
```

Or to get the associated photometric position based matches (16 GB):

```
wget --spider https://data.sdss.org/sas/dr17/sdss/spectro/redux/photoPosPlate-dr17.fits
```

The stellar parameter (SSPP) results can be downloaded similarly (1.8 GB):

```
wget --spider https://data.sdss.org/sas/dr17/sdss/sspp/ssppOut-dr12.fits
```

Note: This is unchanged since DR12, thus ssppOut-dr12.fits appears in both the dr17 and dr12 directories.

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## Optical Spectra Per-Object Files

If you want a subset of the spectra, the most convenient form may be the spec files with one file per PLATE-MJD-FIBER containing the coadded spectrum, the redshift and classification fits, spectral line fits, and optionally the individual exposures which contributed to the coadd. These are located at:

- eBOSS, BOSS and SEQUELS spectra:
  - [https://data.sdss.org/sas/dr17/eboss/spectro/redux/v5\_13\_2/spectra/full/](https://data.sdss.org/sas/dr17/eboss/spectro/redux/v5_13_2/spectra/full/)
- SDSS Legacy spectra: [data.sdss.org/sas/dr17/sdss/spectro/redux/26/spectra/](https://data.sdss.org/sas/dr17/sdss/spectro/redux/26/spectra/)
- SDSS stellar cluster plates: [data.sdss.org/sas/dr17/sdss/spectro/redux/103/spectra/](https://data.sdss.org/sas/dr17/sdss/spectro/redux/103/spectra/)
- SDSS SEGUE-2 plates: [data.sdss.org/sas/dr17/sdss/spectro/redux/104/spectra/](https://data.sdss.org/sas/dr17/sdss/spectro/redux/104/spectra/)

Beneath each of those directories, the spectra are organized by plate in the form

```
PLATE/spec-PLATE-MJD-FIBER.fits
```

_e.g._,

```
  3586/spec-3586-55181-0016.fits
3609/spec-3609-55201-0646.fits
3661/spec-3661-55614-0020.fits
...
```

To download these spectra in bulk, generate a list of spectra you wish to download in a text file of that format and then use wget:

```
  wget --spider -nv -r -nH --cut-dirs=7 \
-i speclist.txt \
-B https://data.sdss.org/sas/dr17/eboss/spectro/redux/v5_13_2/spectra/full/
```

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## Optical Spectra Per-Object Lite Files

A "lite" version of the above files are also available in the "spectra/lite/PLATE/" subdirectories. These contain the same coadd and catalog information as the full spec files, but don't include the individual exposures which contributed to the coadd. For example, to download the "lite" version of the above QSO files (~42 GB instead of ~250 GB):

```
  wget --spider -nv -r -nH --cut-dirs=8 \
-i speclist.txt \
-B https://data.sdss.org/sas/dr17/eboss/spectro/redux/v5_13_2/spectra/lite/
```

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## Spectra per-Plate Files

The spectra are also available grouped by plate, with all 640 (SDSS) or 1000 (BOSS) spectra in a single file. These are the original outputs of the spectroscopic pipeline and are itemized on the [spectro pipeline](https://www.sdss4.org/dr17/spectro/pipeline/) page, including where they are in the SAS directory structure. The primary files are:

| File | Description |
| --- | --- |
| [spPlate](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/spPlate.html) | Coadded spectra |
| [spCFrame](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/spCFrame.html) | Individual exposure spectra |
| [spZbest](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/RUN1D/spZbest.html) | Redshifts and classifications |
| [spZall](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/RUN1D/spZall.html) | Redshifts and classifications including second, third, etc. best fits |
| [spZline](https://data.sdss.org/datamodel/files/BOSS_SPECTRO_REDUX/RUN2D/PLATE4/RUN1D/spZline.html) | Spectral line fits |

To download all the spPlate files (about 344 GB total) for eBOSS, BOSS and SEQUELS:

```
  rsync --dry-run -aLvz --include "????/" --include "spPlate*.fits" \
--exclude "*" --exclude "spectra/*" \
--prune-empty-dirs --progress \
rsync://dtn.sdss.org/dr17/eboss/spectro/redux/v5_13_2/ v5_13_2/
```

Or for spPlate, spZall, spZbest, spZline:

```
  rsync --dry-run -aLvz --include "????/" \
--include "spPlate*.fits" --include "spZ*.fits" \
--exclude "*" --exclude "spectra/*" \
--prune-empty-dirs --progress \
rsync://dtn.sdss.org/dr17/eboss/spectro/redux/v5_13_2/ v5_13_2/
```

A version of the above command specific to SEGUE-2:

```
  rsync --dry-run -aLvz --include "????/" --include "spPlate*.fits" --exclude "*" \
--prune-empty-dirs --progress \
rsync://dtn.sdss.org/dr17/sdss/spectro/redux/104/segue2/ segue2/
```

This command will download the spectroscopic parameters by plate. If you need stellar parameter data, you need to use:

```
  rsync --dry-run -aLvz --include "????/" --include "output/" \
--include "param/" --include "ssppOut*.fit" \
--include "ssppOut.lineindex*.fit" --exclude "*" \
--prune-empty-dirs --progress \
rsync://dtn.sdss.org/dr17/sdss/sspp/122/ .
```

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## Imaging Data

Images and derived catalog data are described on the [imaging data](https://www.sdss4.org/dr17/imaging/) page. You can use a [SkyServer search](https://skyserver.sdss.org/public/SearchTools/) or the file [window\_flist.fits](https://data.sdss.org/sas/dr17/eboss/resolve/2013-07-29/window_flist.fits) file to identify which RERUN-RUN-CAMCOL-FIELD overlaps your region of interest. Then download the matching calibObj files (catalog data) or frame files (calibrated imaging data), _e.g._, for RERUN 301, RUN 2505, CAMCOL 3, FIELD 38, the r-band image is:

```
wget --spider https://data.sdss.org/sas/dr17/eboss/photoObj/frames/301/2505/3/frame-r-002505-3-0038.fits.bz2
```

and the associated catalog of identified galaxies for that patch of sky is:

```
wget --spider https://data.sdss.org/sas/dr17/eboss/sweeps/dr13_final/301/calibObj-002505-3-gal.fits.gz
```

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)

## Interferometry Data

The MARVELS data comprises less than 1 TB, and can simply be downloaded recursively from these directories:

- [https://data.sdss.org/sas/dr17/marvels/spectro/data](https://data.sdss.org/sas/dr17/marvels/spectro/data)
- [https://data.sdss.org/sas/dr17/marvels/spectro/redux](https://data.sdss.org/sas/dr17/marvels/spectro/redux)
- [https://data.sdss.org/sas/dr17/marvels/target](https://data.sdss.org/sas/dr17/marvels/target)

For additional assistance with MARVELS data contact [the help desk](mailto:helpdesk@sdss.org).

[Back to Top](https://www.sdss4.org/dr17/data_access/bulk/#)
