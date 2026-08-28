# URL: https://dp1.lsst.io/products/catalogs/object.html

[Skip to main content](https://dp1.lsst.io/products/catalogs/object.html#main-content)

Back to top`Ctrl` + `K`

LightDarkSystem Settings

- [GitHub](https://github.com/lsst/dp1_lsst_io)

# Object [\#](https://dp1.lsst.io/products/catalogs/object.html\#object "Link to this heading")

Measurements of objects detected in deep coadd images.

Schema: [Object table](https://sdm-schemas.lsst.io/dp1.html#Object)

## Access [\#](https://dp1.lsst.io/products/catalogs/object.html\#access "Link to this heading")

The object catalog is accessible via the TAP and Butler services.

**Recommended access service:** TAP

Note

The Object catalog has many columns, and it is recommended to retrieve only a subset of the columns [with TAP](https://dp1.lsst.io/access/adql_queries.html#products-adql-queries) or the [with the Butler](https://dp1.lsst.io/access/butler_terminology.html#products-butler-terminology).

### TAP [\#](https://dp1.lsst.io/products/catalogs/object.html\#tap "Link to this heading")

- _Citation_: **NSF-DOE Vera C. Rubin Observatory** (2025); Legacy Survey of Space and Time Data Preview 1: Object searchable catalog ![DOI Logo](https://dp1.lsst.io/_images/doi.png)[https://doi.org/10.71929/rubin/2570325](https://doi.org/10.71929/rubin/2570325) \[ [`BibTeX`](https://dp1.lsst.io/_downloads/13026eb86950831930be847a7c5bb86b/tap-Object.bib)\]

- Table name: `Object`

- Columns: 1,296

- Rows: 2,299,757


### Butler [\#](https://dp1.lsst.io/products/catalogs/object.html\#butler "Link to this heading")

- _Citation_: **NSF-DOE Vera C. Rubin Observatory** (2025); Legacy Survey of Space and Time Data Preview 1: object dataset type ![DOI Logo](https://dp1.lsst.io/_images/doi.png)[https://doi.org/10.71929/rubin/2570324](https://doi.org/10.71929/rubin/2570324) \[ [`BibTeX`](https://dp1.lsst.io/_downloads/ad51c6e2b879c5f612b78a9ae5cca4cf/butler-object.bib)\]

- [Dataset type](https://dp1.lsst.io/access/butler_terminology.html#products-butler-terminology): (‘object’, { **skymap**, **tract**}, ArrowAstropy)

- Format: Parquet

- Number of Butler datasets: 29


## Description [\#](https://dp1.lsst.io/products/catalogs/object.html\#description "Link to this heading")

An “object” is an astrophysical object at a static sky coordinate.

The object catalog contains forced measurements on the deep coadd images
at the coordinates of every object detected with signal-to-noise ratio >5
in a deep coadd image of any filter.

Measurements include PSF and extended fluxes, shapes, and sizes,
as well as processing pixel flags.
Photometry is calibrated, but not corrected for Milky Way dust extinction.

Objects are detected and deblended in each patch independently, including the “outer” patch regions that overlap.
They are then filtered down to just those whose reference-band centroid falls within the inner (non-overlapping) patch bounds when per-patch catalogs are aggregated.

### Processing [\#](https://dp1.lsst.io/products/catalogs/object.html\#processing "Link to this heading")

The object catalog is the result of [Source detection and measurement](https://dp1.lsst.io/processing/detection/index.html).

### Tutorials [\#](https://dp1.lsst.io/products/catalogs/object.html\#tutorials "Link to this heading")

See the [200-level notebook](https://dp1.lsst.io/tutorials/notebook/index.html#notebook-200) or [200-level portal](https://dp1.lsst.io/tutorials/portal/index.html#portal-200)
tutorials demonstrating how to access the object table.

On this page


[Edit on GitHub](https://github.com/lsst/dp1_lsst_io/edit/main/products/catalogs/object.rst)