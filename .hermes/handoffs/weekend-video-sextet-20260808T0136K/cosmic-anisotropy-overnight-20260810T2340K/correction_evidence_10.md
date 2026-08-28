URL: https://data.desi.lbl.gov/doc/organization/

[Skip to content](https://data.desi.lbl.gov/doc/organization/#data-organization)

# Data Organization [¶](https://data.desi.lbl.gov/doc/organization/\#data-organization "Permanent link")

This page describes how DESI data is organized in public releases, focusing on the structure of key data products that most users will need.

## End-user data products [¶](https://data.desi.lbl.gov/doc/organization/\#end-user-data-products "Permanent link")

The primary data products for end-users are [**redshift catalogs**](https://data.desi.lbl.gov/doc/organization/#redshift-catalogs), [**spectra**](https://data.desi.lbl.gov/doc/glossary/#spectra), coadditions ( [**coadds**](https://data.desi.lbl.gov/doc/glossary/#coadd)) of those spectra, and individual **redshifts**. These are available in two broad groups: [**HEALPixel-based**](https://data.desi.lbl.gov/doc/organization/#healpixel-based-spectra) and [**tile-based**](https://data.desi.lbl.gov/doc/organization/#tile-based-spectra) (per-tile).

For a hands-on introduction to DESI data organization and how to access files, please see the tutorial notebook:
[https://github.com/desihub/tutorials/blob/main/01\_getting\_started/03\_DataOrganization.ipynb](https://github.com/desihub/tutorials/blob/main/01_getting_started/03_DataOrganization.ipynb)

### Redshift catalogs [¶](https://data.desi.lbl.gov/doc/organization/\#redshift-catalogs "Permanent link")

Redshift and classification catalogs are combined across thousands of individual files into stacked redshift catalogs in `spectro/redux/MOUNTAIN/zcatalog/`. For DR1, `MOUNTAIN=iron` (for EDR, `MOUNTAIN=fuji`).

Multiple zcatalog versions may be released with each spectroscopic production. In general, the highest version number is the preferred catalog. DR1 uses version 1 (`v1`) catalogs, and older `v0` catalogs are deprecated. A planned future `v2` will significantly reformat the files to make them easier to work with the rapidly increasing data volumes of the DESI catalogs.

For analyses that just want the recommended “best” redshift for a given target, regardless of survey or program, we recommend using:

- **`zall-pix-iron.fits`**: (20.8GB) Combines all the HEALPix-based redshifts across all surveys and programs. The `ZCAT_PRIMARY` boolean column indicates the recommended redshift.
- **`zall-tilecumulative-iron.fits`**: (23.6GB) Provides all cumulative, tile-based redshifts across all surveys and programs.

These files can be accessed at:

```
https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits
https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-tilecumulative-iron.fits
```

Note that these are v1 catalogs, which are the preferred version for DR1.

### HEALPixel-based spectra [¶](https://data.desi.lbl.gov/doc/organization/\#healpixel-based-spectra "Permanent link")

Full-depth coadds are located under `spectro/redux/MOUNTAIN/healpix/`, and combine exposures for targets on a given HEALPixel (nside = 64; see [Górski _et al._ (2005)](https://ui.adsabs.harvard.edu/abs/2005ApJ...622..759G/abstract)), including combining data across tiles if a target was observed on multiple tiles. These are further divided by _survey_ and _program_, and stored in files based on HEALPixel group (`HPIXGROUP`) and HEALPixel number (`HEALPIX`):

```
spectro/redux/MOUNTAIN/healpix/SURVEY/PROGRAM/HPIXGROUP/HEALPIX/
```

Note

`HPIXGROUP` = floor(`HEALPIX`/100)

For example, all `SURVEY=main`, `PROGRAM=dark` data for targets in nested NSide=64 HEALPix number 31542 can be found at:

```
https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/main/dark/315/31542/
```

HEALPixel-based redshifts combine data across tiles to group data for a given HEALPixel into a single directory. Note that even in the HEALPixel case data are _not_ combined across different surveys ( [sv1](https://data.desi.lbl.gov/doc/glossary/#sv1), [sv2](https://data.desi.lbl.gov/doc/glossary/#sv2), etc.) or programs ( [bright](https://data.desi.lbl.gov/doc/glossary/#bright-program), [dark](https://data.desi.lbl.gov/doc/glossary/#dark-program), etc.).

The figure below shows a DESI [tile](https://data.desi.lbl.gov/doc/glossary/#tile), divided into 10 [petals](https://data.desi.lbl.gov/doc/glossary/#petal), and a [rosette](https://data.desi.lbl.gov/doc/glossary/#rosette) of tiles observed
during [sv3](https://data.desi.lbl.gov/doc/glossary/#sv3), color-coded by HEALPixel number (`HEALPIX`). The left-hand panel shows the sky positions of the fibers from a single tile (pointing) color-coded by `PETAL_LOC` values as labeled. The right-hand panel shows all fiber sky positions for a single rosette, obtained by observing the same area of the sky with multiple dithered tiles (figure credit: S. Juneau / DESI collaboration / NSF’s NOIRLab Astro Data Lab).

![Tile versus Healpix](https://data.desi.lbl.gov/doc/img/tile_vs_healpix.png)

### Tile-based spectra [¶](https://data.desi.lbl.gov/doc/organization/\#tile-based-spectra "Permanent link")

Per-tile spectra are located under `spectro/redux/MOUNTAIN/tiles/`, and combine data across multiple exposures of the same [tile](https://data.desi.lbl.gov/doc/glossary/#tile), but not across different tiles even if the same target was observed on multiple tiles. These are further divided into different subgroups, with some differences between EDR and DR1:

**For DR1 (`iron`), the subdirectories are:**

```
tiles/cumulative/
tiles/pernight/
```

**For EDR (`fuji`), additional subdirectories are available:**

```
tiles/1x_depth/
tiles/4x_depth/
tiles/cumulative/
tiles/lowspeed/
tiles/perexp/
tiles/pernight/
```

**cumulative** contains all data for each [tile](https://data.desi.lbl.gov/doc/glossary/#tile), coadded across exposures and nights. If the tile was observed on only a single night, this is the same as the equivalent _pernight_ group (see below).

```
tiles/cumulative/TILEID/LASTNIGHT/
```

**pernight** combines data within a night, typically from back-to-back exposures, but not _across_ nights. If the [tile](https://data.desi.lbl.gov/doc/glossary/#tile) was observed on only a single exposure on that night, this is the same as the equivalent _perexp_ group (see below).

```
tiles/pernight/TILEID/NIGHT/
```

**perexp** contains classifications and redshift fits to individual exposures (EDR only).

```
tiles/perexp/TILEID/EXPID/
```

Other custom coadds, classifications, and redshift fits available EDR include files to match the expected depth of the Main Survey (`1x_depth/`), four times the expected Main Survey depth (`4x_depth/`), and coadds that use only data from poor observing conditions (`lowspeed/`).

I’ll update the Large-Scale Structure Catalogs section with the correct URL for the Lasker paper:

## Large-Scale Structure Catalogs [¶](https://data.desi.lbl.gov/doc/organization/\#large-scale-structure-catalogs "Permanent link")

The data products produced during the creation of Large-Scale Structure (LSS) catalogs can be found under the `survey/catalogs/RELEASE/LSS/` directory, with final products associated with different versions of the catalogs within `survey/catalogs/RELEASE/LSS/MOUNTAIN/LSScats/VERSION/`.

### Directory Structure [¶](https://data.desi.lbl.gov/doc/organization/\#directory-structure "Permanent link")

- `${DESI_ROOT}/survey/catalogs/RELEASE/LSS/` hosts the LSS catalogs tagged by the spectroscopic production used (SPECPROD), named after mountains (e.g., `iron` for DR1). Normally, one SPECPROD is published per data release, maintaining consistency with the spectroscopic data processing runs described earlier.

- `${DESI_ROOT}/survey/catalogs/RELEASE/LSS/MOUNTAIN/LSScats/` contains different versions of the final clustering catalogs based on progressive improvements of the reduction pipeline. Multiple versions may exist for the same RELEASE.


### Key Components [¶](https://data.desi.lbl.gov/doc/organization/\#key-components "Permanent link")

The LSS directories contain several important components:

- **SPECPROD**: Directories named after mountains (e.g., “iron” for DR1), matching the spectroscopic production names
- **randomRANN**: Initial 18 random files with all potential assignments
- **altmtl**: Products used to calculate the pairwise inverse probability (PIP) weights with the AltMTL method ( [Lasker _et al._ 2025](https://iopscience.iop.org/article/10.1088/1475-7516/2025/01/127)).
- **tiles-{OBSCON}.fits**: List of tiles for the given release (where OBSCON is “DARK” or “BRIGHT”, corresponding to the program types)
- **collisions-{OBSCON}.fits**: List of FIBER and LOCATION positions rejected from fiber assignment

### Catalog Versions [¶](https://data.desi.lbl.gov/doc/organization/\#catalog-versions "Permanent link")

Within any data release, there may be multiple versions of these catalogs with different properties. As of DR1, these are (see Appendix B [here](https://inspirehep.net/literature/2850031)):

- [https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.2/](https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.2/)
- [https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/](https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/)

In DR1, the catalogs that include a record of alternative fiber assignment histories and completeness weights are available in directories with the `pip` suffix.
Currently for DR1 the altmtl products are not yet public.

### Usage Guidance [¶](https://data.desi.lbl.gov/doc/organization/\#usage-guidance "Permanent link")

Most users will want to use the final products designed for clustering measurements, which have `clustering` in the file name. See [Ross _et al._ (2025)](https://inspirehep.net/literature/2790563) for details about the content and production of the LSS catalogs. To determine which version you should use for your analysis, please consult DESI publications.

### Documentation and References [¶](https://data.desi.lbl.gov/doc/organization/\#documentation-and-references "Permanent link")

The full data model for DESI LSS catalogs can be found [here](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/index.html).

### Historical Note [¶](https://data.desi.lbl.gov/doc/organization/\#historical-note "Permanent link")

LSS catalogs produced before the Iron spectroscopic reductions are organized differently. Specifically, early Main Survey data (the first two months) processed through the Guadalupe spectroscopic pipeline are available as a Value-Added Catalog (VAC) at [https://data.desi.lbl.gov/public/dr1/vac/dr1/lss/guadalupe/v1.0/LSScats/](https://data.desi.lbl.gov/public/dr1/vac/dr1/lss/guadalupe/v1.0/LSScats/). These earlier catalogs follow a similar structure to the Iron-based LSS catalogs but are located in the VAC directory.

## Directory Structure Overview [¶](https://data.desi.lbl.gov/doc/organization/\#directory-structure-overview "Permanent link")

The DESI data is organized in a hierarchical directory structure. The following table summarizes the main directories and their contents:

| Directory | Description |
| --- | --- |
| `spectro/` | All spectroscopic data |
| `data/` | Raw data |
| `redux/` | Reduced data |
| `iron/` | Iron spectroscopic production |
| `tiles-iron.fits` | Unique list of tiles |
| `exposures-iron.fits` | Unique list of exposures |
| `exposures/` | Intermediate processing files per exposure |
| `healpix/` | Spectra and redshifts grouped by HEALPix |
| `tiles/` | Spectra and redshifts grouped by TILEID |
| `cumulative/` | Spectra and redshifts coadded across all nights |
| `pernight/` | Spectra and redshifts coadded within a night |
| `zcatalog/` |  |
| `v1/` | Merged redshift catalogs |
| `guadalupe/` | Like `iron/` but for the Guadalupe production |
| `survey/` | Survey operations and LSS catalog files |
| `catalogs/` |  |
| `dr1/` |  |
| `LSS/` | Large-scale structure catalogs |
| `QSO/` | QSO catalogs |
| `mocks/` | LSS mock catalogs |
| `target/` |  |
| `catalogs/` | Input target catalogs |
| `fiberassign/` | Fiber assignment catalogs for each TILEID |
| `vac/` |  |
| `dr1/` | Contributed value-added catalogs |

Please see the [DESI data model documentation](https://desidatamodel.readthedocs.io/) for more details regarding the directory and subdirectory structure listed in this table, individual file formats, and additional directories and files not listed here used by the DESI pipeline, including calibration files.

## DESI observations [¶](https://data.desi.lbl.gov/doc/organization/\#desi-observations "Permanent link")

DESI observes a “ [tile](https://data.desi.lbl.gov/doc/glossary/#tile)” of 5,000 spectra at a time. Survey tiles overlap to provide greater coverage density than could be achieved with a single pass. Most targets are observed only on a single tile, but some targets, such as
Lyman-alpha [QSO](https://data.desi.lbl.gov/doc/glossary/#qso) s (z \> 2.1) and standard stars, can be observed multiple times across multiple overlapping tiles. The [**TARGETID**](https://data.desi.lbl.gov/doc/glossary/#targetid) provides the unique identifier for which astronomical object is associated with a given spectrum or redshift.

DESI observations are split into multiple [**survey**](https://data.desi.lbl.gov/doc/glossary/#survey) phases (see [Myers _et al._ (2023)](https://ui.adsabs.harvard.edu/abs/2023AJ....165...50M/abstract) for additional details):

- **Commissioning** ( [**cmx**](https://data.desi.lbl.gov/doc/glossary/#cmx)): Provided for completeness, but does not have the same quality as subsequent data. Should only be used with caution and not for scientific analysis requiring uniform sample selection or data quality.
- **Target Selection Validation** ( [**sv1**](https://data.desi.lbl.gov/doc/glossary/#sv1)): Uses an extended target selection different from that of the One-Percent Survey ( [sv3](https://data.desi.lbl.gov/doc/glossary/#sv3)) and the [Main Survey](https://data.desi.lbl.gov/doc/glossary/#main-survey).
- **Operations Testing** ( [**sv2**](https://data.desi.lbl.gov/doc/glossary/#sv2)): Dress rehearsal observations for the One-Percent Survey ( [sv3](https://data.desi.lbl.gov/doc/glossary/#sv3)). This will be of limited interest to most users but is included for completeness.
- **One-Percent Survey** ( [**sv3**](https://data.desi.lbl.gov/doc/glossary/#sv3)): Very similar target selection as the Main Survey, and covers about 1% (~140 square degrees) of the total DESI footprint area.
- [**Special**](https://data.desi.lbl.gov/doc/glossary/#special-survey): Observations that do not fit within one of the other survey phases, e.g. custom observations of dedicated secondary programs.
- [**Main**](https://data.desi.lbl.gov/doc/glossary/#main-survey): The primary DESI science survey.

Surveys are further split by [**program**](https://data.desi.lbl.gov/doc/glossary/#program), i.e. the observing conditions under which the [tile](https://data.desi.lbl.gov/doc/glossary/#tile) was designed to be observed:

- [**dark**](https://data.desi.lbl.gov/doc/glossary/#dark-program): for observing [LRG](https://data.desi.lbl.gov/doc/glossary/#lrg), [ELG](https://data.desi.lbl.gov/doc/glossary/#elg), and [QSO](https://data.desi.lbl.gov/doc/glossary/#qso) targets
- [**bright**](https://data.desi.lbl.gov/doc/glossary/#bright-program): for observing [BGS](https://data.desi.lbl.gov/doc/glossary/#bgs) and [MWS](https://data.desi.lbl.gov/doc/glossary/#mws) targets
- [**backup**](https://data.desi.lbl.gov/doc/glossary/#backup-program): for when observing conditions are worse than [bright](https://data.desi.lbl.gov/doc/glossary/#bright-program)
- **other**: none of the above

## Spectroscopic data processing runs [¶](https://data.desi.lbl.gov/doc/organization/\#spectroscopic-data-processing-runs "Permanent link")

Production data processing runs are named alphabetically after mountains and contained under `spectro/redux/` for a given data release. In the top-level production directory, the file `MOUNTAIN/tiles-MOUNTAIN.fits` is a catalog of all DESI tiles included the production run named `MOUNTAIN`.

Note

DR1 uses `MOUNTAIN=iron` while EDR uses `MOUNTAIN=fuji`.

Tiles may be observed on multiple exposures spanning multiple nights. More detailed per-exposure information is available in the file `exposures-MOUNTAIN.fits`.

### Spectroscopic Pipeline [¶](https://data.desi.lbl.gov/doc/organization/\#spectroscopic-pipeline "Permanent link")

The spectroscopic pipeline produces wavelength and flux-calibrated spectra of observed targets. These spectra include flux variance, bit masks, and spectral resolution for each wavelength and fiber. Additionally, the pipeline generates a redshift catalog, which classifies targets spectroscopically, provides redshift estimates, uncertainty measurements, and confidence levels.

The diagram below illustrates the data flow through the spectroscopic pipeline. It outlines the key algorithms, fitting procedures, and performance metrics used during data processing.

For a detailed description of the pipeline, please see [Guy _et al._ (2023)](https://ui.adsabs.harvard.edu/abs/2023AJ....165..144G/abstract).

![Spectroscopic Pipeline Flowchart](https://data.desi.lbl.gov/doc/img/spec_pipeline.png)

## Target Catalogs [¶](https://data.desi.lbl.gov/doc/organization/\#target-catalogs "Permanent link")

Target catalogs used as input for DESI observations can be found in the `target/catalogs` directory tree. The photometric catalogs from which primary DESI targets were selected remain unchanged from the Early Data Release (EDR). Some catalogs of secondary and calibration targets have been updated between the Early Target Selection (ETS) and DR1.
