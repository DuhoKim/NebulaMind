[Skip to main](https://zenodo.org/records/8060755#main)

Published June 29, 2023
\| Version 0.1.0

[Dataset](https://zenodo.org/search?q=&f=resource_type%3Adataset)
Open


# Quaia: The Gaia-unWISE Quasar Catalog

### Authors/Creators

- [Storey-Fisher, Kate1](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Storey-Fisher,+Kate%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0001-8764-7103 "Storey-Fisher, Kate's ORCID profile")
- [Hogg, David W.2](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Hogg,+David+W.%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-2866-9403 "Hogg, David W.'s ORCID profile")
- [Rix, Hans-Walter3](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Rix,+Hans-Walter%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-4996-9069 "Rix, Hans-Walter's ORCID profile")
- [Eilers, Anna-Christina4](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Eilers,+Anna-Christina%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-2895-6218 "Eilers, Anna-Christina's ORCID profile")
- [Fabbian, Giulio5](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Fabbian,+Giulio%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0002-3255-4695 "Fabbian, Giulio's ORCID profile")
- [Blanton, Michael1](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Blanton,+Michael%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-1641-6222 "Blanton, Michael's ORCID profile")
- [Alonso, David6](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Alonso,+David%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0001-7283-5064 "Alonso, David's ORCID profile")

- 1.



New York University

- 2.



New York University / Flatiron Institute / Max Planck Institute for Astronomy

- 3.



Max Planck Institute for Astronomy

- 4.



MIT

- 5.



Cardiff University / Flatiron Institute

- 6.



University of Oxford


## Description

Quaia is a quasar catalog constructed from the Gaia DR3 quasar candidates sample and unWISE infrared data. It is the largest-volume spectroscopic quasar catalog to date. The catalog is described in an associated publication (link coming soon).

The files included are:

- **quaia\_G20.X.fits**: The quasar catalog. Columns include the sky position, redshift estimate and uncertainty, Gaia and unWISE identifiers, Gaia and unWISE magnitudes, and proper motion values and uncertainties. The full format and column descriptions can be found in Table 2 of the paper linked above.
- **selection\_function\_NSIDE64\_G20.X.fits**: The modeled selection function for the associated catalog, in the form of a healpixel map (NSIDE=64) with a value between 0 and 1 representing the probability that a source observed in that pixel would be included in the catalog.
- **random\_G20.X\_10x.fits**: A random catalog generated with the associated selection function, having an initially Poisson sky distribution and then downsampled by the selection function map. The random has roughly 10 times the number of sources as the associated catalog.

These files are included for two versions of the catalog with different magnitude limits: the full G<20.5 catalog contains 1,295,502 sources, and the G<20.0 version contains 755,850 sources. The G<20.0 version is cleaner and has overall better redshift estimates; it is just a subset of the G<20.5 catalog with an additional magnitude cut, but the associated selection function and random catalog are different so we provide it as a separate file for ease and clarity.

A notebook showing how to read in the files and visualize them is available here: [https://github.com/kstoreyf/gaia-quasars-lss/blob/main/notebooks/2023-06-16\_data\_products.ipynb](https://github.com/kstoreyf/gaia-quasars-lss/blob/main/notebooks/2023-06-16_data_products.ipynb)

## Files

### Files (681.8 MB)

| Name | Size |  |
| --- | --- | --- |
| [quaia\_G20.0.fits](https://zenodo.org/records/8060755/files/quaia_G20.0.fits?download=1)<br>md5:42cec6519d139ac5fdcf4f891a68b5d4 | 99.8 MB | [Download](https://zenodo.org/records/8060755/files/quaia_G20.0.fits?download=1) |
| [quaia\_G20.5.fits](https://zenodo.org/records/8060755/files/quaia_G20.5.fits?download=1)<br>md5:8b816b719e8c8ccd1c0a648b53557ddd | 171.0 MB | [Download](https://zenodo.org/records/8060755/files/quaia_G20.5.fits?download=1) |
| [random\_G20.0\_10x.fits](https://zenodo.org/records/8060755/files/random_G20.0_10x.fits?download=1)<br>md5:c5d5240d8bf72dbf1d19eebee9dddf2c | 151.1 MB | [Download](https://zenodo.org/records/8060755/files/random_G20.0_10x.fits?download=1) |
| [random\_G20.5\_10x.fits](https://zenodo.org/records/8060755/files/random_G20.5_10x.fits?download=1)<br>md5:ba9f7f1428ab27cb28b13e8b4b488457 | 259.1 MB | [Download](https://zenodo.org/records/8060755/files/random_G20.5_10x.fits?download=1) |
| [selection\_function\_NSIDE64\_G20.0.fits](https://zenodo.org/records/8060755/files/selection_function_NSIDE64_G20.0.fits?download=1)<br>md5:e62df7437156763ee59210976a808e45 | 400.3 kB | [Download](https://zenodo.org/records/8060755/files/selection_function_NSIDE64_G20.0.fits?download=1) |
| [selection\_function\_NSIDE64\_G20.5.fits](https://zenodo.org/records/8060755/files/selection_function_NSIDE64_G20.5.fits?download=1)<br>md5:d327cafb2011ac4a4ceafb57e7b553f3 | 400.3 kB | [Download](https://zenodo.org/records/8060755/files/selection_function_NSIDE64_G20.5.fits?download=1) |

Citations [Citations help page](https://support.zenodo.org/help/en-gb/25-citations)

1

literature (1)

dataset (0)

software (0)

unknown (0)

Citations to this version

Search citations

Search

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  |  | 2025 | [doi](http://doi.org/10.3847/1538-4365/adf056) |  |

Page size:

10

Jump up


This site uses cookies. Find out more on [how we use cookies](https://about.zenodo.org/cookie-policy)

Accept all cookiesAccept only essential cookies