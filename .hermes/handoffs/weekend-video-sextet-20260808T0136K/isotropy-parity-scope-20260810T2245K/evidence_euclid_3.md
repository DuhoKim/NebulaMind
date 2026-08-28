# URL: https://zenodo.org/records/15027787

[Skip to main](https://zenodo.org/records/15027787#main)

Published March 19, 2025
\| Version 0.0.3

[Dataset](https://zenodo.org/search?q=&f=resource_type%3Adataset)
Open


# Euclid Quick Data Release (Q1): First visual morphology catalogue

### Authors/Creators

- [Walmsley, Mike\\
(Contact person)1, 2](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Walmsley,+Mike%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0002-6408-4181 "Walmsley, Mike's ORCID profile")
- [Huertas-Company, Marc3](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Huertas-Company,+Marc%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0002-1416-8483 "Huertas-Company, Marc's ORCID profile")
- [Quilley, Louis4](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Quilley,+Louis%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0009-0008-8375-8605 "Quilley, Louis's ORCID profile")
- [Masters, Karen5](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Masters,+Karen%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-0846-9578 "Masters, Karen's ORCID profile")
- [Kruk, Sandor6](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Kruk,+Sandor%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0001-8010-8879 "Kruk, Sandor's ORCID profile")
- [Kristin, Remmelgas7](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Kristin,+Remmelgas%22)
- [Popp, Jürgen Joseph8](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Popp,+J%C3%BCrgen+Joseph%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0002-3724-1727 "Popp, Jürgen Joseph's ORCID profile")
- [Romelli, Erik9](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22Romelli,+Erik%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-3069-9222 "Romelli, Erik's ORCID profile")
- [O'Ryan, David7](https://zenodo.org/search?q=metadata.creators.person_or_org.name:%22O%27Ryan,+David%22) [![ORCID icon](https://zenodo.org/static/images/orcid.svg)](https://orcid.org/0000-0003-1217-4617 "O'Ryan, David's ORCID profile")

- 1.






[![ROR icon](https://zenodo.org/static/images/ror-icon.svg)](https://ror.org/03dbr7087 "University of Toronto's ROR profile")



University of Toronto

- 2.






[![ROR icon](https://zenodo.org/static/images/ror-icon.svg)](https://ror.org/027m9bs27 "University of Manchester's ROR profile")



University of Manchester

- 3.






[![ROR icon](https://zenodo.org/static/images/ror-icon.svg)](https://ror.org/0220k9r37 "Université Paris Descartes's ROR profile")



Université Paris Descartes

- 4.






[![ROR icon](https://zenodo.org/static/images/ror-icon.svg)](https://ror.org/03j307b25 "Observatoire de Lyon's ROR profile")



Observatoire de Lyon

- 5.






[![EDMO icon](https://zenodo.org/static/images/edmo-icon.svg)](https://edmo.seadatanet.org/report/3553 "Haverford College's EDMO profile")



Haverford College

- 6.






[![ROR icon](https://zenodo.org/static/images/ror-icon.svg)](https://ror.org/00kw1sm04 "European Space Astronomy Centre's ROR profile")



European Space Astronomy Centre

- 7.






[![EDMO icon](https://zenodo.org/static/images/edmo-icon.svg)](https://edmo.seadatanet.org/report/2391 "European Space Agency's EDMO profile")



European Space Agency

- 8.






[![ROR icon](https://zenodo.org/static/images/ror-icon.svg)](https://ror.org/05mzfcs16 "The Open University's ROR profile")



The Open University

- 9.






[![ROR icon](https://zenodo.org/static/images/ror-icon.svg)](https://ror.org/02n742c10 "University of Trieste's ROR profile")



University of Trieste


### Contributors

- [The Euclid Consortium](https://zenodo.org/search?q=metadata.contributors.person_or_org.name:%22The+Euclid+Consortium%22)
- [Galaxy Zoo](https://zenodo.org/search?q=metadata.contributors.person_or_org.name:%22Galaxy+Zoo%22)

## Description

_Image to be added after embargo lifts on 19th_

Contents

1. Catalogue
1. List of ID columns and morphology columns
2. List of morphology questions and answers available
3. List of additional columns copied from MER (flux, ellipticity, area, etc.)
2. Images

Full documentation is available [here](https://docs.google.com/document/d/1l0iEfB3h978RLSf_ujPlfMJClkmH-5ePPweUwqpXCqs/edit?usp=sharing). Below is a summary.

## 1\. Catalogue

The morphology catalogue covers galaxies which are either bright or extended. Specifically, it includes galaxies matching one of the following criteria:

- segmentation area > 700 pixels, or...
- VIS < 20.5 AND segmentation area > 200 pixels

The measurements were made by [Zoobot](https://github.com/mwalmsley/zoobot) foundation models, finetuned on Euclid galaxies using the responses of [Galaxy Zoo volunteers](https://www.galaxyzoo.org/).

Our models were trained using galaxies from the selection cuts above _but with the first option requiring 1200 pixels_. Therefore, galaxies between 700 and 1200 pixels in area are may have less reliable measurements.

The catalogue file is morphology\_catalogue (.parquet or .csv, the contents are identical). It includes the following columns:

|     |     |
| --- | --- |
| release\_name | Always Q1\_R1, for now |
| tile\_index | Euclid tile index i.e. which MER tile hosts this galaxy |
| **object\_id** | Euclid object id i.e. the **MER catalogue identifier** for this galaxy |
| segmentation\_map\_id | Alternative Euclid identifier. The first 9 digits are the tile index, the other digits match the internal segmentation id of the source. |
| **right\_ascension** | in degrees, from the MER catalogue |
| **declination** | in degrees, from the MER catalogue |
| **{question}\_{answer}\_fraction** | e.g. smooth-or-featured\_smooth\_fraction. The fraction of volunteers expected to give this answer to this morphology question. **Probably the morphology columns you want.** |
| {question}\_{answer}\_dirichlet | e.g. smooth-or-featured\_smooth\_dirichlet. The concentration for a Dirichlet distribution (useful for uncertainties). See the paper. |
| **warning\_galaxy\_fails\_training\_cuts** | **Marks galaxies between 700px and 1200px, where performance may be lower. See above.** |
| cutout\_width\_arcsec | Width (and height) of cutout in arcseconds |

The following questions and answers are available.

|     |     |     |
| --- | --- | --- |
| Question | Answer | Notes |
| smooth-or-featured | smooth | May include face-on lenticulars, which are better identified with e.g. Sersic indices |
| how-rounded | round |  |
| how-rounded | in-between |  |
| how-rounded | cigar-shaped |  |
| smooth-or-featured | featured-or-disk | The question branch most commonly used by researchers |
| disk-edge-on | yes |  |
| edge-on-bulge | boxy |  |
| edge-on-bulge | none |  |
| edge-on-bulge | rounded |  |
| disk-edge-on | no |  |
| has-spiral-arms | yes |  |
| spiral-winding | tight |  |
| spiral-winding | medium |  |
| spiral-winding | loose |  |
| spiral-arm-count | 1 |  |
| spiral-arm-count | 2 |  |
| spiral-arm-count | 3 |  |
| spiral-arm-count | 4 |  |
| spiral-arm-count | more-than-4 | Often overlaps with cant-tell |
| spiral-arm-count | cant-tell | Often overlaps with more-than-4 |
| has-spiral-arms | no |  |
| bar | strong | Bar strength is a mix of length and width |
| bar | weak |  |
| bar | no |  |
| bulge-size | dominant |  |
| bulge-size | large |  |
| bulge-size | moderate |  |
| bulge-size | small |  |
| bulge-size | none |  |
| smooth-or-featured | problem |  |
| problem | star |  |
| problem | zoom | i.e. bad zoom, a cutout which is too wide |
| problem | artifact |  |
| artifact | satellite |  |
| artifact | scattered |  |
| artifact | diffraction |  |
| artifact | ray |  |
| artifact | saturation |  |
| artifact | other |  |
| artifact | ghost | Dichrotic ghosts |
| merging | none |  |
| merging | minor\_disturbance |  |
| merging | major\_disturbance | Primarily obvious tidal tails and similar features |
| merging | merger | Primarily "dramatic" ongoing mergers |
| clumps | yes | Not recommended; we are building clump-specific models |
| clumps | no | Not recommended; we are building clump-specific models |

For convenience, we have also copied over some useful MER catalogue columns. The schema for the full MER catalogue is [here](http://st-dm.pages.euclid-sgs.uk/data-product-doc/dmq1/merdpd/dpcards/mer_finalcatalog.html#main-catalog-fits-file). Additionally, Euclid also makes available many other tables with e.g. photometric redshifts, estimated masses, etc. These are documented [here](http://st-dm.pages.euclid-sgs.uk/data-product-doc/dmq1/). All fluxes are in micro-janskies (uJy).

|     |     |
| --- | --- |
| **segmentation\_area** | **Number of pixels included in SourceExtractor++ mask of galaxy (0.1 arcsec/pixel).** |
| flux\_segmentation | Total VIS flux inside the segmentation mask above. |
| mag\_segmentation | As above, converted to magnitude. \`\`\`mag = -2.5\*log10(flux\[muJy\])+23.9\`\`\`. Not technically in MER catalogue. |
| flux\_detection\_total | VIS flux measured within a Kron aperture in the detection image. FLUX\_AUTO in SourceExtractor. |
| flux\_vis\_1fwhm\_aper | VIS flux within an aperture of radius 1 FWHM. |
| mumax\_minus\_mag | A star/galaxy diagnostic. The morphology catalogue uses the recommended filter MUMAX\_MINUS\_MAG>=-2.6 to reject stars. |
| mu\_max | Peak surface brightness above the background in the detection band (directly from SExtractor) |
| ellipticity | A parametrization of how stretched an object is in the detection band (VIS, here), computed from the minor and major axes of the object itself (directly from SExtractor). \[I assume this is the major/minor axis ratio\] |
| kron\_radius | Major semi-axis (in pixels) of the elliptical aperture used for total (Kron) aperture photometry on the detection image |

2\. Images

We are sharing the original cutout images as shown to Galaxy Zoo volunteers. The images are named like {tile\_index}\_{object\_id}.jpg, where the negative sign ('-') in object id is replaced with 'NEG' to avoid path issues. You can construct the file paths from the morphology catalogue. For example:

df\['file\_loc'\] = df\['tile\_index'\].astype(str) + '\_' + df\['object\_id'\].astype(str).str.replace('-', 'NEG') + '\_.jpg'

Each ZIP has images of every galaxy. There are three ZIP files, one for each image processing version. Volunteers were shown all three versions. The model predictions are made using the first version (the colour composite).

**Fig 3 in the Q1 visual morphology paper shows an example galaxy in all three versions.**

The VIS+Y images are composites with VIS in the blue channel and Y in the red channel (and the median of VIS and Y in the green channel, but this isn't visible). They use an arcinsh stretch, with the stretch designed to balance the contribution from each band.

The VIS only images are black-and-white, and also use an arcsinh stretch.

The VIS LSB images use a more complicated stretch to highlight LSB features. _This is not included yet on Zenodo._

Full details of the image processing are in the Q1 visual morphology paper.

## Files

### morphology\_catalogue.csv

Preview

### Cannot preview file

Sorry, we are unfortunately not able to preview this file.

### Files (8.6 GB)

| Name | Size |  |
| --- | --- | --- |
| [cutouts\_jpg\_gz\_arcsinh\_vis\_only.tar](https://zenodo.org/records/15027787/files/cutouts_jpg_gz_arcsinh_vis_only.tar?download=1)<br>md5:1acad78f1e9883e765beff508233894d | 3.7 GB | [Download](https://zenodo.org/records/15027787/files/cutouts_jpg_gz_arcsinh_vis_only.tar?download=1) |
| [cutouts\_jpg\_gz\_arcsinh\_vis\_y.tar](https://zenodo.org/records/15027787/files/cutouts_jpg_gz_arcsinh_vis_y.tar?download=1)<br>md5:4cec21cfb799c1861ea9701bed5a8980 | 3.8 GB | [Download](https://zenodo.org/records/15027787/files/cutouts_jpg_gz_arcsinh_vis_y.tar?download=1) |
| [morphology\_catalogue.csv](https://zenodo.org/records/15027787/files/morphology_catalogue.csv?download=1)<br>md5:652e4546c63085c37539a9e9664f64e2 | 601.4 MB | [Preview](https://zenodo.org/records/15027787/preview/morphology_catalogue.csv?include_deleted=0) [Download](https://zenodo.org/records/15027787/files/morphology_catalogue.csv?download=1) |
| [morphology\_catalogue.parquet](https://zenodo.org/records/15027787/files/morphology_catalogue.parquet?download=1)<br>md5:79e7880d5989e05ec23205782c30025a | 97.3 MB | [Download](https://zenodo.org/records/15027787/files/morphology_catalogue.parquet?download=1) |
| [representations\_pca\_100.parquet](https://zenodo.org/records/15027787/files/representations_pca_100.parquet?download=1)<br>md5:d007c08ccb52450d542eca13591118bf | 337.8 MB | [Download](https://zenodo.org/records/15027787/files/representations_pca_100.parquet?download=1) |
| [representations\_pca\_40.parquet](https://zenodo.org/records/15027787/files/representations_pca_40.parquet?download=1)<br>md5:a43e3edfe6df3ef0ad9bd10da67d3dae | 138.6 MB | [Download](https://zenodo.org/records/15027787/files/representations_pca_40.parquet?download=1) |

## Additional details

2025-03-19

Initial public release

[Python](https://zenodo.org/search?q=custom_fields.code%5C:programmingLanguage:%22Python%22)

Citations [Citations help page](https://support.zenodo.org/help/en-gb/25-citations)

literature (0)

dataset (0)

software (0)

unknown (0)

Citations to this version

Search citations

Search

|
|

_No citations found_

Jump up


This site uses cookies. Find out more on [how we use cookies](https://about.zenodo.org/cookie-policy)

Accept all cookiesAccept only essential cookies