URL: https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html

- [Home](https://desidatamodel.readthedocs.io/en/latest/index.html)
- [DESI\_ROOT](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/index.html)
- [survey](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/index.html)
- [catalogs](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/index.html)
- [RELEASE](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/index.html)
- [LSS](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/index.html)
- [SPECPROD](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/index.html)
- [LSScats](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/index.html)
- [VERSION](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/index.html)
- DATA clustering catalogs
- [View page source](https://desidatamodel.readthedocs.io/en/latest/_sources/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.rst.txt)

* * *

# DATA clustering catalogs [](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html\#data-clustering-catalogs "Link to this heading")

Summary:

For each target type, LSS catalogs for the data, ready to be used for clustering measurements, are provided.

Naming Convention:

`{TARGET}_{GALCAP}_clustering.dat.fits`, where `{TARGET}` is the target: `QSO`, `ELG`, `ELG_LOPnotqso`, `LRG`, `LRG+ELG_LOPnotqso`,
for dark or `BGS_ANY`, `BGS_BRIGHT`, `BGS_BRIGHT-21.5` for bright. `{GALCAP}` is the Galactic hemisphere region `NGC` or `SGC` or the combination of both if not explicitly shown.

Regex:

`[A-Za-z0-9._+-]+_(NGC|SGC)_clustering\.dat\.fits`

File Type:

FITS, 237 MB

## Contents [](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html\#contents "Link to this heading")

| Number | EXTNAME | Type | Contents |
| --- | --- | --- | --- |
| [HDU0](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#hdu0) |  | IMAGE | Empty |
| [HDU1](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#hdu1) | LSS | BINTABLE | Catalog data |

## FITS Header Units [](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html\#fits-header-units "Link to this heading")

### HDU0 [](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html\#hdu0 "Link to this heading")

This HDU has no non-standard required keywords.

Empty HDU.

### HDU1 [](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html\#hdu1 "Link to this heading")

EXTNAME = LSS

LSS catalogs for clustering measurements

#### Required Header Keywords [](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html\#required-header-keywords "Link to this heading")

Required Header Keywords Table

| KEY | Example Value | Type | Comment |
| --- | --- | --- | --- |
| NAXIS1 | 137 | int | width of table in bytes |
| NAXIS2 | 1821322 | int | number of rows in table |
| DESIDR | dr1 | str | DESI Data Release |

#### Required Data Table Columns [](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html\#required-data-table-columns "Link to this heading")

| Name | Type | Units | Description |
| --- | --- | --- | --- |
| TARGETID | int64 |  | Unique DESI target ID |
| Z | float64 |  | Redshift measured by Redrock |
| NTILE | int64 |  | Number of tiles target was available on |
| RA | float64 | deg | Barycentric Right Ascension in ICRS |
| DEC | float64 | deg | Barycentric declination in ICRS |
| PHOTSYS | char\[1\] |  | N for the MzLS/BASS photometric system, S for DECaLS |
| FRAC\_TLOBS\_TILES | float64 |  | Fraction of targets with the same TILES value that contribute to FRACZ\_TILELOCID |
| WEIGHT\_ZFAIL | float64 |  | Should be all 1 at this point for main survey |
| WEIGHT\_RF [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float64 |  | Imaging systematics weights derived with the regressis random forest regression method |
| WEIGHT\_SN [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float64 |  | Imaging systematics weights derived with the sysnet NN regression method |
| WEIGHT\_SYS | float64 |  | Correction for fluctuations in projected density with imaging conditions, from random forrest method |
| WEIGHT | float64 |  | The combination of all weights to use |
| WEIGHT\_COMP | float64 |  | Completeness weight accounting for the local chance of being assigned a fiber |
| NX | float64 |  | Estimated mean number density given the redshift and number of overlapping tiles (NTILE) |
| WEIGHT\_FKP | float64 |  | 1/(1+NX\*P0), with P0 different for each tracer |
| WEIGHT\_RESCALED [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float64 |  | Rescaled weight when unifying different targets into a single frame |
| EFFECTIVE\_BIAS [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float64 |  | Effective bias used to weight the galaxy when unifying several tracers |
| flux\_g\_dered [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float32 | nanomaggy | (lower or uppercase) Flux in the g-band after correcting for Galactic extinction (AB system) |
| flux\_r\_dered [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float32 | nanomaggy | (lower or uppercase) Flux in the r-band after correcting for Galactic extinction (AB system) |
| flux\_z\_dered [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float32 | nanomaggy | (lower or uppercase) Flux in the z-band after correcting for Galactic extinction (AB system) |
| flux\_w1\_dered [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float32 | nanomaggy | (lower or uppercase) Flux in the WISE W1-band after correcting for Galactic extinction (AB system) |
| flux\_w2\_dered [\[1\]](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html#id10) | float32 | nanomaggy | (lower or uppercase) Flux in the WISE W2-band after correcting for Galactic extinction (AB system) |

## Notes and Examples [](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html\#notes-and-examples "Link to this heading")

Optional columns:

- `WEIGHT_RESCALED` and `EFFECTIVE_BIAS` only when unifying targets into a single frame ( _e.g._: LRG+ELG\_LOPnotqso)

- `flux_g_dered`, `flux_r_dered`, `flux_z_dered`, `flux_w1_dered`, `flux_w2_dered` only present in BGS samples


Versions**[latest](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html)**[stable](https://desidatamodel.readthedocs.io/en/stable/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html)[25.3](https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html)[24.9](https://desidatamodel.readthedocs.io/en/24.9/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html)[23.1](https://desidatamodel.readthedocs.io/en/23.1/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html)On Read the Docs[Project Home](https://app.readthedocs.org/projects/desidatamodel/?utm_source=desidatamodel&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/desidatamodel/builds/?utm_source=desidatamodel&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=desidatamodel&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=desidatamodel&utm_content=flyout)
