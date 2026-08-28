URL: https://zenodo.org/records/8331338

[Skip to main](https://zenodo.org/records/8331338#main)

![](https://zenodo.org/api/communities/74ec9dfa-a359-4b7a-91cc-cfe82801f94b/logo)

Published September 1, 2023
\| Version 1.0.0

[Dataset](https://zenodo.org/communities/galaxy-zoo/records?q=&f=resource_type%3Adataset)
Open


# Galaxy Zoo DESI: Detailed Morphology Classifications for 8.7M Galaxies in the DESI Legacy Imaging Surveys

### Authors/Creators

- [Walmsley, Mike1](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Walmsley,+Mike%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0002-6408-4181 "Walmsley, Mike's ORCID profile")
- [Géron, Tobias2](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22G%C3%A9ron,+Tobias%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0002-6851-9613 "Géron, Tobias's ORCID profile")
- [Kruk, Sandor3](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Kruk,+Sandor%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0001-8010-8879 "Kruk, Sandor's ORCID profile")
- [Scaife, Anna M.M.1](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Scaife,+Anna+M.M.%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0002-5364-2301 "Scaife, Anna M.M.'s ORCID profile")
- [Lintott, Chris4](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Lintott,+Chris%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0001-5578-359X "Lintott, Chris's ORCID profile")
- [Masters, Karen5](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Masters,+Karen%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-0846-9578 "Masters, Karen's ORCID profile")
- [Dawson, James6](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Dawson,+James%22)
- [Dickinson, Hugh7](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Dickinson,+Hugh%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-0475-008X "Dickinson, Hugh's ORCID profile")
- [Fortson, Lucy8](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Fortson,+Lucy%22)
- [Garland, I. L.9](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Garland,+I.+L.%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0002-3887-6433 "Garland, I. L.'s ORCID profile")
- [Mantha, Kameswara Bharadwaj8](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Mantha,+Kameswara+Bharadwaj%22)
- [O'Ryan, David9](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22O%27Ryan,+David%22)
- [Popp, Jürgen7](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Popp,+J%C3%BCrgen%22)
- [Simmons, Brooke9](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Simmons,+Brooke%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0001-5882-3323 "Simmons, Brooke's ORCID profile")
- [Baeten, Elisabeth M L10](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Baeten,+Elisabeth+M+L%22)
- [Macmillan, Christine10](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Macmillan,+Christine%22)

- 1.



University of Manchester

- 2.



University of Oxford,

- 3.



European Space Astronomy Centre

- 4.



University of Oxford

- 5.



Haverford College

- 6.



South African Radio Astronomy Observatory (SARAO)

- 7.



The Open University

- 8.



University of Minnesota

- 9.



Lancaster University

- 10.



Zooniverse


## Description

This repository contains the data released in the paper "Galaxy Zoo DESI: Detailed Morphology Classifications for 8.7M Galaxies in the DESI Legacy Imaging Surveys" _(DOI to follow on publication)._

We release detailed morphology measurements for bright ( _r_ < 19) galaxies in the DESI Legacy Imaging Surveys footprint. These measurements estimate the presence of bars, spirals arms, ongoing mergers, and more.

\-\-\-

**GZ DESI Detailed Morphology Catalogs**

These catalogs are created by training deep learning models on Galaxy Zoo volunteer responses, to predict what volunteers might say for new galaxies. The models are available at \[www.github.com/mwalmsley/zoobot\](www.github.com/mwalmsley/zoobot). Our measurements are predicted vote fractions i.e. the fraction of volunteers expected to select a given answer for a given question.

We share two catalog versions containing the same morphology measurements but presented in different ways.

gz\_desi\_deep\_learning\_catalog\_friendly.parquet contains the morphology measurements

gz\_desi\_deep\_learning\_catalog\_advanced.parquet contains the same measurements, and additional information:

\- \_friendly includes only relevant vote fractions, defined as vote fractions to answers of questions that a majority of volunteers would have been asked. This removes predicted vote fractions for e.g. the fraction of volunteers answering "2 spiral arms" to a galaxy with no spiral arms. \_advanced includes all vote fractions and instead reports the (column "proportion\_asked"). The user must select which vote fractions they consider relevant (we suggest proportion\_asked > 0.5, which recovers the \_friendly fractions).

\- \_advanced includes columns with estimated credible intervals (error bars) around each vote fraction. These are calculated from the vote fraction posterior predicted by our models.

Finally, we separately present volunteer votes collected for 96k galaxies during the GZD-8 campaign, i.e. after the release of GZ DECaLS but before this (GZ DESI) release. These are split into the \_core and \_extended catalogs, where \_extended includes galaxies which received five or more votes for "artifact". The models above were trained on these votes as well as votes from GZ DECaLS.

\-\-\-

**External Catalog**

For convenience, we also include an additional catalog of non-morphology measurements created by other authors (external\_catalog.parquet) cross-matched to our morphology catalogs. Please credit those authors if you use this catalog (references are in the GZ DESI paper).

A particularly important external measurement is redshift. Morphology is increasingly hard to resolve at higher redshift and so **distant galaxies appear less featured**. external\_catalog.parquet includes the column "redshift", which is the SDSS spectroscopic redshift where available and a photometric redshift estimate otherwise (again, see the GZ DESI paper for references and credit). You may want to select only galaxies at lower redshifts.

\-\-\-

**Data Notes**

Parquet is a fast csv-like format which can be read with pd.read\_parquet(loc, columns=\[some columns\]). Parquet files are read column-by-column (rather than row-by-row) and so you can chose which columns to load. You can easily check which columns are available using columns=\['foo'\] and reading the error message. We suggest loading only the columns you need when working with the larger catalogs. This will require much less memory than loading every column.

We will release updates if needed via Zenodo versioning. We recommend using the latest version of this repository. You can check the version you are currently viewing on the right-hand sidebar.

Please cite the paper (DOI to follow on publication) when using the data in this repository.

\-\-\-

**History**

v0.0.1 - closed pre-release for internal review

v1.0.0 - first public release. Removed low-z pre-filtered catalogs.

## Files

### Files (9.9 GB)

| Name | Size |  |
| --- | --- | --- |
| [external\_catalog.parquet](https://zenodo.org/records/8331338/files/external_catalog.parquet?download=1)<br>md5:1d8ed3b5660487b5bae58cfee3e4cf0e | 1.6 GB | [Download](https://zenodo.org/records/8331338/files/external_catalog.parquet?download=1) |
| [gz\_desi\_deep\_learning\_catalog\_advanced.parquet](https://zenodo.org/records/8331338/files/gz_desi_deep_learning_catalog_advanced.parquet?download=1)<br>md5:5fd343b76cbb965bc19be722b4c10d99 | 7.6 GB | [Download](https://zenodo.org/records/8331338/files/gz_desi_deep_learning_catalog_advanced.parquet?download=1) |
| [gz\_desi\_deep\_learning\_catalog\_friendly.parquet](https://zenodo.org/records/8331338/files/gz_desi_deep_learning_catalog_friendly.parquet?download=1)<br>md5:114785d00c4d4f2208185bee73dd08b8 | 658.8 MB | [Download](https://zenodo.org/records/8331338/files/gz_desi_deep_learning_catalog_friendly.parquet?download=1) |
| [gz\_desi\_gzd8\_volunteer\_core\_catalog.parquet](https://zenodo.org/records/8331338/files/gz_desi_gzd8_volunteer_core_catalog.parquet?download=1)<br>md5:ba79d9d9b56bb81608fbaa4c48d4f465 | 6.4 MB | [Download](https://zenodo.org/records/8331338/files/gz_desi_gzd8_volunteer_core_catalog.parquet?download=1) |
| [gz\_desi\_gzd8\_volunteer\_extended\_catalog.parquet](https://zenodo.org/records/8331338/files/gz_desi_gzd8_volunteer_extended_catalog.parquet?download=1)<br>md5:d632e4830af7eae2e9bb0a3f88b26992 | 5.5 MB | [Download](https://zenodo.org/records/8331338/files/gz_desi_gzd8_volunteer_extended_catalog.parquet?download=1) |

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
|  |  | 2025 | [doi](http://doi.org/10.3847/1538-4365/ae0294) |  |

Page size:

10

Jump up


This site uses cookies. Find out more on [how we use cookies](https://about.zenodo.org/cookie-policy)

Accept all cookiesAccept only essential cookies
