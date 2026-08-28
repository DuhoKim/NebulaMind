# URL: https://data.galaxyzoo.org/

A Zooniverse project


Sign up
\|
Sign in

[—](http://talk.data.galaxyzoo.org/#/profile)

—

Sign out

![](https://data.galaxyzoo.org/)

- [Galaxy Zoo](https://data.galaxyzoo.org/#section-0)  - [Full Catalog](https://data.galaxyzoo.org/#section-1)
  - [AGN Host Galaxies](https://data.galaxyzoo.org/#section-2)
  - [Overlapping Galaxy Pairs](https://data.galaxyzoo.org/#section-3)
  - [Mergers](https://data.galaxyzoo.org/#section-4)
  - [Green Peas](https://data.galaxyzoo.org/#section-5)
  - [Red Spirals](https://data.galaxyzoo.org/#section-6)
- [Galaxy Zoo 2](https://data.galaxyzoo.org/#section-7)  - [Full Catalog](https://data.galaxyzoo.org/#section-8)
  - [Images](https://data.galaxyzoo.org/#section-8)
  - [Bar Lengths](https://data.galaxyzoo.org/#section-9)
  - [Dust-Lane Spheroidal Galaxies](https://data.galaxyzoo.org/#section-10)
- [Galaxy Zoo: Hubble](https://data.galaxyzoo.org/#section-11)  - [Full Catalog](https://data.galaxyzoo.org/#section-12)
  - [Bar Fraction Evolution](https://data.galaxyzoo.org/#section-13)
- [Galaxy Zoo: CANDELS](https://data.galaxyzoo.org/#section-14)  - [Full Catalog](https://data.galaxyzoo.org/#section-15)
- [Galaxy Zoo: UKIDSS](https://data.galaxyzoo.org/#section-16)  - [Full Catalog](https://data.galaxyzoo.org/#section-17)
- [Galaxy Zoo DECaLS](https://data.galaxyzoo.org/#section-18)  - [Catalog, Images, Models](https://data.galaxyzoo.org/#section-19)
- [Galaxy Zoo DESI (8.7M)](https://data.galaxyzoo.org/#section-20)  - [Catalog, Models](https://data.galaxyzoo.org/#section-21)
- [Galaxy Zoo Euclid (Q1, 378k)](https://data.galaxyzoo.org/#section-22)  - [Catalog, Models, Representations](https://data.galaxyzoo.org/#section-23)
- [Galaxy Zoo: Cosmic Dawn](https://data.galaxyzoo.org/#section-24)  - [Catalog, Images](https://data.galaxyzoo.org/#section-25)

* * *

- [Galaxy Zoo: Mergers](https://data.galaxyzoo.org/#section-26)

* * *

- [Galaxy Builder](https://data.galaxyzoo.org/#section-27)

* * *

- [Data Visualizations](https://data.galaxyzoo.org/#section-28)

_Use the navigation bar on the left to find each data release._

# Galaxy Zoo 1 data release

The original [Galaxy Zoo](http://zoo1.galaxyzoo.org/) project ran from July 2007 until February 2009. It was replaced by [Galaxy Zoo 2](http://zoo2.galaxyzoo.org/), [Galaxy Zoo: Hubble](http://hubble.galaxyzoo.org/), and [Galaxy Zoo: CANDELS](http://www.galaxyzoo.org/). In the original Galaxy Zoo project, volunteers classified images of [Sloan Digital Sky Survey](http://www.sdss.org/) galaxies as belonging to one of six categories - elliptical, clockwise spiral, anticlockwise spiral, edge-on , star/don't know, or merger.


## Full catalog

This webpage allows anyone to download the resulting GZ classifications of nearly 900,000 galaxies in the project.


Galaxy Zoo is described in [Lintott et al. 2008, MNRAS, 389, 1179](https://adsabs.harvard.edu/abs/2008MNRAS.389.1179L) and the data release is described in [Lintott et al. 2011, 410, 166](https://adsabs.harvard.edu/abs/2011MNRAS.410..166L). Anyone making use of the data should cite at least one of these papers in any resulting publications.

|     |     |
| --- | --- |
| Table 2 |

| This table gives classifications of galaxies which have spectra included in SDSS Data Release 7. The fraction of the vote in each of the six categories is given, along with debiased votes in elliptical and spiral categories and flags identifying systems as classified as spiral, elliptical or uncertain. |
| CSV (gzipped) | [GalaxyZoo1\_DR\_table2.csv.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.csv.gz) |
| CSV (zip) | [GalaxyZoo1\_DR\_table2.csv.zip](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.csv.zip) |
| FITS | [GalaxyZoo1\_DR\_table2.fits](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.fits) |
| VOTable | [GalaxyZoo1\_DR\_table2.vot.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table2.vot.gz) |
| _Note: the provided flags in Table 2 are there for the convenience of users who do not want to get into the details too much. These are based upon a vote fraction threshold of 0.8. However, there is a complication in the debiasing (described in [Bamford et al. 2009](https://adsabs.harvard.edu/abs/2009MNRAS.393.1324B)). The classification bias depends on whether one uses the type likelihoods directly, or applies a threshold. The bias is worse if thresholds are used. We therefore applied bias corrections computed in consistent fashion. So, for the debiased type likelihoods we computed the bias correction based on the elliptical/spiral ratio using the likelihoods directly; for the type flags we debiased the raw type likelihoods using a correction based on the elliptical/spiral ratio determined after applying a 0.8 threshold, and then applied the same threshold to produce the flags. Therefore, the type flags do not correspond to simply applying a 0.8 threshold on the debiased type likelihoods, though for many galaxies these will agree._ |

|     |     |
| --- | --- |
| Table 3 |
| This table gives classifications of galaxies included in the Galaxy Zoo sample which did not have spectra available in SDSS Data Release 7. It is not possible to estimate the bias in this sample without accurate redshifts, and so only the fraction of the vote in each of the six categories is given. |
| CSV (gzipped) | [GalaxyZoo1\_DR\_table3.csv.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table3.csv.gz) |
| CSV (zip) | [GalaxyZoo1\_DR\_table3.csv.zip](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table3.csv.zip) |
| FITS | [GalaxyZoo1\_DR\_table3.fits](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table3.fits) |
| VOTable | [GalaxyZoo1\_DR\_table3.vot.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table3.vot.gz) |

|     |     |
| --- | --- |
| Table 4 |
| This table gives a series of measures of the classification confidence. |
| CSV (gzipped) | [GalaxyZoo1\_DR\_table4.csv.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table4.csv.gz) |
| CSV (zip) | [GalaxyZoo1\_DR\_table4.csv.zip](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table4.csv.zip) |
| FITS | [GalaxyZoo1\_DR\_table4.fits](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table4.fits) |
| VOTable | [GalaxyZoo1\_DR\_table4.vot.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table4.vot.gz) |

|     |     |
| --- | --- |
| Table 5 |
| This table gives the results from the bias study that introduced mirrored images. |
| CSV (gzipped) | [GalaxyZoo1\_DR\_table5.csv.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table5.csv.gz) |
| CSV (zip) | [GalaxyZoo1\_DR\_table5.csv.zip](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table5.csv.zip) |
| FITS | [GalaxyZoo1\_DR\_table5.fits](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table5.fits) |
| VOTable | [GalaxyZoo1\_DR\_table5.vot.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table5.vot.gz) |

|     |     |
| --- | --- |
| Table 6 |
| This table gives the results from the bias study that introduced monochrome images. |
| CSV (gzipped) | [GalaxyZoo1\_DR\_table6.csv.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table6.csv.gz) |
| CSV (zip) | [GalaxyZoo1\_DR\_table6.csv.zip](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table6.csv.zip) |
| FITS | [GalaxyZoo1\_DR\_table6.fits](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table6.fits) |
| VOTable | [GalaxyZoo1\_DR\_table6.vot.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table6.vot.gz) |

|     |     |
| --- | --- |
| Table 7 |
| This table gives the fraction of votes in each of the six categories, combining results from the main and bias studies. |
| CSV (gzipped) | [GalaxyZoo1\_DR\_table7.csv.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table7.csv.gz) |
| CSV (zip) | [GalaxyZoo1\_DR\_table7.csv.zip](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table7.csv.zip) |
| FITS | [GalaxyZoo1\_DR\_table7.fits](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table7.fits) |
| VOTable | [GalaxyZoo1\_DR\_table7.vot.gz](https://galaxy-zoo-1.s3.amazonaws.com/GalaxyZoo1_DR_table7.vot.gz) |

## CASjobs

These tables are also accessible via [CasJobs](http://skyserver.sdss3.org/CasJobs/). Their names are:

- Table 2: DR10.zooSpec

- Table 3: DR10.zooNoSpec

- Table 4: DR10.zooConfidence

- Table 5: DR10.zooMirrorBias

- Table 6: DR10.zooMonochrome

- Table 7: DR10.zooVotes


## AGN host galaxies

This sample is presented in the Galaxy Zoo 1 paper on AGN host galaxies ( [Schawinski et al., 2010, ApJ, 711, 284](https://adsabs.harvard.edu/abs/2010ApJ...711..284S)). It is a volume-limited sample of galaxies (0.02 < z < 0.05, Mz < –19.5 AB) with emission line classifications, stellar masses, velocity dispersions and GZ1 morphological classifications. When using this sample, please cite Schawinski et al. ( [2010](https://adsabs.harvard.edu/abs/2010ApJ...711..284S)) and Lintott et al. ( [2008](https://adsabs.harvard.edu/abs/2008MNRAS.389.1179L), [2011](https://adsabs.harvard.edu/abs/2011MNRAS.410..166L)).

Download here: [schawinski\_GZ\_2010\_catalogue.fits.gz](https://galaxy-zoo-1.s3.amazonaws.com/schawinski_GZ_2010_catalogue.fits.gz)

|     |     |
| --- | --- |

| OBJID | SDSS DR7 object ID |
| RA, DEC | RA and dec in J2000.0 |
| REDSHIFT | spectroscopic redshift from SDSS |
| GZ1\_MORPHOLOGY | Galaxy Zoo 1 morphology according to the [Land et al. (2008)](https://adsabs.harvard.edu/abs/2008MNRAS.388.1686L) "clean" criterion. This is an integer where 0 = indeterminate, 1 = early type, 3 = merger, 4 = late type |
| BPT\_CLASS | Spectroscopic classification of galaxy based on emission lines ratios in the BPT diagram. 0 = no emission lines, 1 = star-forming, 2 = composite, 3 = Seyfert and 4 = LINER. |
| U,G,R,I,Z | SDSS model magnitudes. These are extinction-corrected but not _k_-corrected. |
| SIGMA, SIGMA\_ERR | Stellar velocity dispersion (and error) measured using GANDALF |
| LOG\_MSTELLAR | log of stellar mass \[M\_sun\] |
| L\_O3 | Extinction-corrected \[OIII\] luminosity |

## Overlapping Galaxy Pairs

This section contains data from the Galaxy Zoo survey for overlapping galaxy pairs, useful for studies of dust absorption. Data is derived from the Zoo 1 and Zoo 2 periods (August 2007–April 2010), and is described in detail by [Keel et al. (PASP, 2013, 125, 923)](https://adsabs.harvard.edu/abs/2013PASP..125....2K). The catalog contains a total of 1990 galaxy pairs.

|     |     |
| --- | --- |
| Overlapping galaxy pairs |
| [Column description and format](https://data.galaxyzoo.org/overlaps.html) |
| TXT | [overlapcatalog.txt](https://data.galaxyzoo.org/data/overlapping-galaxy-pairs/overlap-catalog.txt) |
| Javascript | [Overlap candidates (sortable webpage)](https://data.galaxyzoo.org/overlap-candidates.html) |

There is a similar file of candidate pairs which were rejected for the final list because of evidence for interaction, other geometric reasons, or for having redshifts the wrong way around for dust backlighting.

|     |     |
| --- | --- |
| Rejected overlapping galaxy pairs |
| PDF | [OverlapRejects.pdf](http://astronomy.ua.edu/keel/observe/PDFcharts/OverlapRejects.pdf) |
| Javascript | [Overlap rejects (sortable webpage)](http://bama.ua.edu/~ammanning/discard.html) |

The various overlapping galaxy pair types are illustrated in Figures [2a](https://data.galaxyzoo.org/images/fig2a.png) and [2b](https://data.galaxyzoo.org/images/fig2b.png) from Keel et al. 2013. Below are PDF files containing a single page for each galaxy pair, plus finding charts, more detailed photometry and identifications, and in some cases more precise redshifts. The PDFs are also available at [http://astronomy.ua.edu/keel/observe/PDFcharts](http://astronomy.ua.edu/keel/observe/PDFcharts).

|     |     |
| --- | --- |
| [SDSSOverlaps00Final.pdf](http://astronomy.ua.edu/keel/observe/PDFcharts/SDSSOverlaps00Final.pdf) | RA: 00–10 hours |
| [SDSSOverlaps10final.pdf](http://astronomy.ua.edu/keel/observe/PDFcharts/SDSSOverlaps10final.pdf) | RA: 10–13 hours |
| [SDSSOverlaps13final.pdf](http://astronomy.ua.edu/keel/observe/PDFcharts/SDSSOverlaps13final.pdf) | RA: 13–15 hours |
| [SDSSOverlaps15final.pdf](http://astronomy.ua.edu/keel/observe/PDFcharts/SDSSOverlaps15final.pdf) | RA: 15–24 hours |

## Merging galaxies

This sample of merging galaxies is assembled from SDSS Galaxy Zoo 1 data. It is a homogenous sample of galaxies (0.005 < z < 0.1) with spectroscopy for at least one of two merging galaxies in the pair. Value-added GZ data includes the morphologies of the merging galaxies as well as the relative stage of the merger. For any use of data from this sample, please cite [Darg et al. (2010a)](https://adsabs.harvard.edu/abs/2010MNRAS.401.1043D) and [Darg et al. (2010b)](https://adsabs.harvard.edu/abs/2010MNRAS.401.1552D).

|     |     |
| --- | --- |
| Merging galaxies |
| [Column description and format](https://data.galaxyzoo.org/data/mergers/mergers_columndescription.txt) |
| CSV | [darg\_mergers.csv](https://data.galaxyzoo.org/data/mergers/darg_mergers.csv) |
| FITS | [darg\_mergers.fits](https://data.galaxyzoo.org/data/mergers/darg_mergers.fits) |

## Green peas

"Green peas" are compact galaxies with extremely high star-formation rates. Their name comes from their appearance in colour SDSS images, which is due to strong \[OIII\] λ5007 emission that appears in the _r_-band filter for large numbers of low-redshift (0.112 < z < 0.360) galaxies. Properties of the initial sample are described in [Cardamone et al. (2009)](https://adsabs.harvard.edu/abs/2009MNRAS.399.1191C). Data below is from Table 4 in Cardamone et al. (2009).

|     |     |
| --- | --- |
| Green pea galaxies |
| [Column description and format](https://data.galaxyzoo.org/data/greenpeas/peas_columndescription.txt) |
| CSV | [peas\_tbl14.csv](https://data.galaxyzoo.org/data/greenpeas/peas_tbl4.csv) |
| FITS | [peas\_tbl14.fits](https://data.galaxyzoo.org/data/greenpeas/peas_tbl4.fits) |

## Red Spirals

"Red
Spirals" are galaxies with clearly
identified spiral structure which are
optically red in
colour. Most spiral
galaxies are blue in
colour, while most
ellipticals are red,
so this sample of red
spirals is an
interesting
intermediate
population. The properties
of a sample of disky
red spirals are
described in [Masters\\
et\\
al. (2010)](https://adsabs.harvard.edu/abs/2010MNRAS.405..783M), and
compared to a match
sample of normal blue
spirals. The data
below is from Appendix
A, Tables
A1 and A2 in Masters
et al. (2010) and
gives the red and blue
spiral samples from
that work.

|     |     |
| --- | --- |
| Red Spiral galaxies |
| ASCII | [RedSpiralsA1.txt](https://data.galaxyzoo.org/data/redspirals/RedSpiralsA1.txt) |
| ASCII | [BlueSpiralsA2.txt](https://data.galaxyzoo.org/data/redspirals/BlueSpiralsA2.txt) |

# Galaxy Zoo 2

[Galaxy Zoo 2 (GZ2)](http://zoo2.galaxyzoo.org/) was the successor project to Galaxy Zoo. GZ2 extends the original Galaxy Zoo classifications for a subsample of the brightest and largest galaxies in the Legacy release, measuring more detailed morphological features. This includes galactic bars, spiral arm and pitch angle, bulges, edge-on galaxies, relative ellipticities, and many others. Two debiased Galaxy Zoo tables are provided, described in [Willett et al. (2013)](https://arxiv.org/abs/1308.3496v2) and [Hart et al. (2016)](https://mnras.oxfordjournals.org/content/461/4/3663): we strongly advise the use of the [Hart et al. (2016)](https://mnras.oxfordjournals.org/content/461/4/3663) table, as this debiases the GZ2 quetion tree most consistently.


## Full Catalog

These tables provide the GZ2 classifications for nearly 300,000 galaxies in the SDSS.


The project description and data reduction is in [Willett et al. 2013, MNRAS, 435, 2835](https://arxiv.org/abs/1308.3496v2) — please cite this paper if making any use of the GZ2 data. The table numbers below are the same as their order in the paper.

|     |     |
| --- | --- |
| Table 1 - Normal-depth sample with new debiasing method |
| Table 1 contains all galaxies that were debiased with the method described in [Hart et al. (2016)](https://mnras.oxfordjournals.org/content/461/4/3663). Galaxies with spectroscopic redshifts classified in GZ2 (from the GZ2 normal, extra and stripe82 normal depth), and apparent r-band magnitudes less than 17.0 are included (239,695 galaxies in total). Please cite [Hart et al. (2016)](https://mnras.oxfordjournals.org/content/461/4/3663) when using these classifications. |
| [Column description and format](https://gz2hart.s3.amazonaws.com/gz2_hart16.txt) |
| CSV | [https://gz2hart.s3.amazonaws.com/gz2\_hart16.csv.gz](https://gz2hart.s3.amazonaws.com/gz2_hart16.csv.gz) |
| FITS | [https://gz2hart.s3.amazonaws.com/gz2\_hart16.fits.gz](https://gz2hart.s3.amazonaws.com/gz2_hart16.fits.gz) |
| VOTable | [https://gz2hart.s3.amazonaws.com/gz2\_hart16.vot.gz](https://gz2hart.s3.amazonaws.com/gz2_hart16.vot.gz) |

|     |     |
| --- | --- |
| Table 5 - Main sample, spectroscopic redshifts |
| Table 5 gives classifications of the 243,500 galaxies in the main sample with spectroscopic redshifts. This is the primary GZ2 data release, containing the largest number of galaxies and the most reliable morphologies. |
| [Column description and format](https://data.galaxyzoo.org/data/gz2/zoo2MainSpecz.txt) |
| CSV | [zoo2MainSpecz.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2MainSpecz.csv.gz) |
| FITS | [zoo2MainSpecz.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2MainSpecz.fits.gz) |
| VOTable | [zoo2MainSpecz.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2MainSpecz.vot.gz) |

|     |     |
| --- | --- |
| Table 6 - Main sample, photometric redshifts |
| Table 6 gives classifications of the 42,462 galaxies in the main sample with photometric redshifts only. Debiased morphologies for this sample are slightly more uncertain than Table 5, since the data reduction requires a redshift to adjust the morphology for classification bias. |
| [Column description and format](https://data.galaxyzoo.org/data/gz2/zoo2MainPhotoz.txt) |
| CSV | [zoo2MainPhotoz.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2MainPhotoz.csv.gz) |
| FITS | [zoo2MainPhotoz.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2MainPhotoz.fits.gz) |
| VOTable | [zoo2MainPhotoz.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2MainPhotoz.vot.gz) |

|     |     |
| --- | --- |
| Table 7 - Stripe 82, normal-depth |
| Table 7 gives classifications of the 17,787 galaxies classified in single-depth Stripe 82 images. The magnitude limit for Stripe 82 classifications (r<17.7) is slightly deeper than the main samples. Some of these galaxies also appear in the main sample (Table 5). |
| [Column description and format](https://data.galaxyzoo.org/data/gz2/zoo2Stripe82Normal.txt) |
| CSV | [zoo2Stripe82Normal.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Normal.csv.gz) |
| FITS | [zoo2Stripe82Normal.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Normal.fits.gz) |
| VOTable | [zoo2Stripe82Normal.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Normal.vot.gz) |

|     |     |
| --- | --- |
| Table 8 - Stripe 82, coadded-depth (set 1) |
| Table 8 gives classifications of the first set of 19,765 galaxies classified in the coadded (runs 106 and 206) Stripe 82 images. Coadded images are made from combining between 47–55 individual exposures, resulting in better detection of fainter features and improved seeing. This set of images had no adjustments made to its background, which resulted in coloured background noise for some galaxies. |
| [Column description and format](https://data.galaxyzoo.org/data/gz2/zoo2Stripe82Coadd1.txt) |
| CSV | [zoo2Stripe82Coadd1.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Coadd1.csv.gz) |
| FITS | [zoo2Stripe82Coadd1.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Coadd1.fits.gz) |
| VOTable | [zoo2Stripe82Coadd1.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Coadd1.vot.gz) |

|     |     |
| --- | --- |
| Table 9 - Stripe 82, coadded-depth (set 2) |
| Table 9 gives classifications of the second set of 19,761 galaxies classified in the coadded (runs 106 and 206) Stripe 82 images. Coadded images are made from combining between 47–55 individual exposures, resulting in better detection of fainter features and improved seeing. This set of images applied a modest colour desaturation to de-emphasise background noise in the coadded data. |
| [Column description and format](https://data.galaxyzoo.org/data/gz2/zoo2Stripe82Coadd2.txt) |
| CSV | [zoo2Stripe82Coadd2.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Coadd2.csv.gz) |
| FITS | [zoo2Stripe82Coadd2.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Coadd2.fits.gz) |
| VOTable | [zoo2Stripe82Coadd2.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/zoo2Stripe82Coadd2.vot.gz) |

|     |     |
| --- | --- |
| SDSS metadata for GZ2 |
| This table provides pre-matched sets of metadata for the Galaxy Zoo 2 samples taken from DR7. This includes coordinates, photometry, size, and redshifts (where present). For science cases, we encourage users to instead use the latest measurements from the latest data release. |
| [Column description and format](https://data.galaxyzoo.org/data/gz2/gz2sample.txt) |
| CSV | [gz2sample.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/gz2sample.csv.gz) |
| FITS | [gz2sample.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/gz2sample.fits.gz) |
| VOTable | [gz2sample.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-2/gz2sample.vot.gz) |

The code used to reduce GZ2 is available on GitHub — please take a look either at its [webpage](https://willettk.github.io/galaxyzoo2/) or fork it from the [repository](https://github.com/willettk/galaxyzoo2) if you're interested in the details.


### CASjobs

The GZ2 catalog is also accessible via [CasJobs](http://skyserver.sdss3.org/CasJobs/) in Data Release 10. The table names in CasJobs are:

- Table 5: DR10.zoo2MainSpecz

- Table 6: DR10.zoo2MainPhotoz

- Table 7: DR10.zoo2Stripe82Normal

- Table 8: DR10.zoo2Stripe82Coadd1

- Table 9: DR10.zoo2Stripe82Coadd2


### SDSS Skyserver

For any object in SDSS DR10, you can access its Galaxy Zoo or Galaxy Zoo 2 classifications (if present) by using the ["Explore"](http://skyserver.sdss3.org/public/en/tools/explore/) tool. Just click the "Galaxy Zoo" link under "Imaging Summary" in the left-hand sidebar ( [example here](http://skyserver.sdss3.org/public/en/tools/explore/galaxyzoo.aspx?id=1237668296598749280&spec=2947691243863304192&apid=apogee.n.s.s3.4128.2M13102744+1826172)).



## Images

The GZ2 images are [available for download on Zenodo.](https://zenodo.org/record/3565489#.Y3vFKS-l0eY)

## Bar lengths

In conjunction with Galaxy Zoo 2, we ran a parallel project to measure lengths, widths, and angles of galactic bars using an interactive interface. See [Hoyle et al. (2011)](https://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1104.5394) for a description of the project and scientific results. The full set of results can be downloaded below.

|     |     |
| --- | --- |
| Bar lengths: Table 1 |
| CSV | [barlengths.csv](https://data.galaxyzoo.org/data/bars/hoyle_barlengths.csv) |
| FITS | [barlengths.fits](https://data.galaxyzoo.org/data/bars/hoyle_barlengths.fits) |
| VOTable | [barlengths.vot](https://data.galaxyzoo.org/data/bars/hoyle_barlengths.vot) |

## Dust-lane spheroidal galaxies

Early Galaxy Zoo 2 classifications were used to identify a sample of 362 spheroidal galaxies with prominent dust lanes (DLSGs), ranging from redshifts of z=0.01 to 0.07. Catalogues of the galaxy properties, along with multi-wavelength coverage from radio through ultraviolet, are available here.

All tables below are in ASCII format.

- [Basic information](https://data.galaxyzoo.org/data/dustlanes/Basic_Information.txt)
- [Radio-wavelength data from FIRST](https://data.galaxyzoo.org/data/dustlanes/FIRST_Radio_Survey.txt)
- [Infrared photometry from IRAS](https://data.galaxyzoo.org/data/dustlanes/IRAS_Photometry.txt)
- [Optical photometry from SDSS](https://data.galaxyzoo.org/data/dustlanes/SDSS_Photometry.txt)
- [Optical spectroscopy from SDSS](https://data.galaxyzoo.org/data/dustlanes/SDSS_Spectroscopy.txt)
- [UV photometry from GALEX](https://data.galaxyzoo.org/data/dustlanes/GALEX_photometry.txt)

Please cite the DLSG ( [Kaviraj et al. 2012](https://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1107.5306); [Shabala et al. 2012](https://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1107.5310); [Kaviraj et al. 2013](https://adsabs.harvard.edu/doi/10.1093/mnras/stt1629)) and Galaxy Zoo 2 ( [Willett et al. 2013](https://arxiv.org/abs/1308.3496v2)) publications if using this data.

# Galaxy Zoo: Hubble

[Galaxy Zoo: Hubble](http://hubble.galaxyzoo.org/) used data from the Hubble Space Telescope to classify images of distant galaxies beyond the reach of SDSS. Images for GZH were taken from the Advanced Camera for Surveys (ACS) aboard Hubble, including data from multiple Legacy surveys.

## Full catalog

The full reduction and analysis of GZ: Hubble was published in [Willett et al. (2017)](https://ui.adsabs.harvard.edu/#abs/2017MNRAS.464.4176W/abstract) (available both from [arXiv](https://arxiv.org/abs/1610.03068) or the [MNRAS journal](https://academic.oup.com/mnras/article-abstract/464/4/4176/2527878/Galaxy-Zoo-morphological-classifications-for-120?redirectedFrom=fulltext)). Please cite this paper if using any data from the project. The full data reduction pipeline and analysis codes for GZH are available as an open-source [Github repository](https://github.com/willettk/gzhubble).

|     |     |
| --- | --- |
| Table 4 - Morphological classifications for galaxies in main HST sample |
| Table 4 contains classifications of 113,705 galaxies aggregated from four _HST_ surveys: AEGIS, COSMOS, GEMS, and GOODS (5-epoch imaging only). This is the primary output of the GZH project, with calibrated and debiased morphological classifications for galaxies out to z ≲ 4. |
| [Column description and format](https://data.galaxyzoo.org/data/gzh/column_descriptions_main.tsv) |
| CSV | [gz\_hubble\_main.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_main.csv.gz) |
| FITS | [gz\_hubble\_main.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_main.fits.gz) |
| VOTable | [gz\_hubble\_main.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_main.vot.gz) |

|     |     |
| --- | --- |
| Table 5 - Morphological classifications for faded galaxies |
| Table 5 contains classifications of 3,927 galaxies from the COSMOS survey. These images were faded to very low colour saturation before classification, and tested the effects of colour gradients on morphological consistency. |
| [Column description and format](https://data.galaxyzoo.org/data/gzh/column_descriptions_faded.tsv) |
| CSV | [gz\_hubble\_faded.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_faded.csv.gz) |
| FITS | [gz\_hubble\_faded.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_faded.fits.gz) |
| VOTable | [gz\_hubble\_faded.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_faded.vot.gz) |

|     |     |
| --- | --- |
| Table 6 - Morphological classifications for recoloured galaxies |
| Table 6 contains classifications of 3,927 galaxies from the COSMOS survey. These colour composite images had the red and blue channels swapped from default settings, and tested the effects of colour perception on morphological consistency. |
| [Column description and format](https://data.galaxyzoo.org/data/gzh/column_descriptions_recoloured.tsv) |
| CSV | [gz\_hubble\_recoloured.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_recoloured.csv.gz) |
| FITS | [gz\_hubble\_recoloured.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_recoloured.fits.gz) |
| VOTable | [gz\_hubble\_recoloured.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_recoloured.vot.gz) |

|     |     |
| --- | --- |
| Table 7 - Morphological classifications for galaxies from 2-epoch GOODS imaging |
| Table 7 contains classifications of 6,144 galaxies from the GOODS-N and GOODS-S surveys. These images are shallow exposures created from 2-epoch imaging, as contrasted with the deeper 5-epoch imaging of galaxies from GOODS in Table 4. |
| [Column description and format](https://data.galaxyzoo.org/data/gzh/column_descriptions_goods_shallow.tsv) |
| CSV | [gz\_hubble\_goods\_shallow.csv.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_goods_shallow.csv.gz) |
| FITS | [gz\_hubble\_goods\_shallow.fits.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_goods_shallow.fits.gz) |
| VOTable | [gz\_hubble\_goods\_shallow.vot.gz](https://zooniverse-data.s3.amazonaws.com/galaxy-zoo-hubble/gz_hubble_goods_shallow.vot.gz) |

|     |     |
| --- | --- |
| Table 8 - Morphological classifications for single-epoch SDSS images of galaxies in Stripe 82 |
| Table 8 contains classifications of 21,522 galaxies located in SDSS Stripe 82. The images come from single-epoch observations by SDSS, but use the same decision tree and interface as the data in Tables 4-7. These images provide a low-redshift counterpart to the data from the various Hubble surveys. |
| [Column description and format](https://data.galaxyzoo.org/data/gzh/column_descriptions_sdss_single.tsv) |

[... middle omitted — see footer ...]

When tested on galaxies where the volunteers are confident, they were 99% accurate on every question.
[Code](https://github.com/mwalmsley/zoobot) and [extensive documentation](https://zoobot.readthedocs.io/) are available if you would like to extend these models or apply them to new problems.


[Walmsley et al. (2021)](https://ui.adsabs.harvard.edu/abs/10.1093%2Fmnras%2Fstab2093/abstract)
(available free from the [MNRAS journal](https://doi.org/10.1093/mnras/stab2093))
describes the project and current data release.
Please cite this paper if using any data from Galaxy Zoo DECaLS.


### Catalogue, Images, Models

The GZ DECaLS data is available via [Zenodo](https://doi.org/10.5281/zenodo.4196266). This includes:


- Morphology classifications from, typically, 5 to 40 volunteers per galaxy (see [the paper](https://doi.org/10.1093/mnras/stab2093))
- Morphology classifications from deep learning models, trained by those volunteers
- The images uploaded to Galaxy Zoo (100GB)

The DECaLS models, and code used to create them, were previously available via the [Zoobot](https://github.com/mwalmsley/zoobot) GitHub repository.
Our models have continued to advance since GZ DECaLS was published, and are now significantly more accurate at classifying galaxy morphology.
[Zoobot](https://github.com/mwalmsley/zoobot) now hosts our latest models.


# Galaxy Zoo DESI (8.7M)

Galaxy Zoo DESI includes detailed morphology measurements for 8.67 million galaxies in the DESI Legacy Imaging Surveys (DECaLS, MzLS, and BASS, plus DES).
These are automated measurements made by deep learning models trained on Galaxy Zoo volunteer votes.
Extending our morphology measurements outside of the previously-released DECaLS/SDSS intersection increases our sky coverage by a factor of 4 (5,000 to 19,000 deg$^2$) and allows for full overlap with complementary surveys including ALFALFA and MaNGA.


Our models typically predict the fraction of volunteers selecting each answer to within 5-10\\% for every answer to every GZ question.
The models are trained on newly-collected votes for DESI-LS DR8 images as well as historical votes from GZ DECaLS.
[Code](https://github.com/mwalmsley/zoobot) and [extensive documentation](https://zoobot.readthedocs.io/) are available if you would like to extend these models or apply them to new problems.


[Walmsley et al. (2023)](https://ui.adsabs.harvard.edu/abs/2023MNRAS.526.4768W/abstract)
(available free from the [MNRAS journal](https://academic.oup.com/mnras/article/526/3/4768/7283169))
describes the project and current data release.
Please cite this paper if using any data from Galaxy Zoo DESI.


### Catalogue, Models

The GZ DESI data is available via [Zenodo](https://doi.org/10.5281/zenodo.7786416).
We provide two versions of our morphology catalogue; a "friendly" version (600MB) with just the morphology measurements,
and an "advanced" version (8GB) which also includes 90% confidence intervals and a measure of question relevance.
See the [Zenodo page](https://doi.org/10.5281/zenodo.7786416) for more details.


The morphology catalogue is also available from NOIRLab's [Astro Data Lab](https://datalab.noirlab.edu/) and from [Vizier](https://vizier.cds.unistra.fr/viz-bin/VizieR).
Both services allow you to cross-match our catalogue against your own catalogues.
[Astro Data Lab](https://datalab.noirlab.edu/) also hosts data from DESI itself, allowing you to query DESI spectra and GZ DESI morphology measurements [with the same tools.](https://datalab.noirlab.edu/tools.php)

The sheer size of the images prepared for our volunteers and models (approx. 1TB) prevents us from including them in this data release.
The original data is available via the Legacy Survey FITS cutout service (select Data Release 8 for an exact replication).
We may be able to arrange sharing the prepared images on a case-by-case basis; please reach out if this is crucial to your research.


Trained model weights, and code to reproduce those models, are available via the [Zoobot](https://github.com/mwalmsley/zoobot) GitHub repository.
**Zoobot includes our latest models and is designed to be easily finetuned to new surveys and new morphology-related tasks.**

# Galaxy Zoo Euclid (Q1: 378k)

Galaxy Zoo Euclid (Q1) includes detailed morphology measurements for 378k galaxies million galaxies in Euclid Q1.
These are automated measurements made by deep learning models trained on Galaxy Zoo volunteer votes.



Our models were pretrained on all Galaxy Zoo labels to date (see ["Scaling Laws for Galaxy Images"](https://arxiv.org/abs/2404.02973)) and then finetuned on volunteer answers to pre-Q1 (OTF) Euclid images.
[Code](https://github.com/mwalmsley/zoobot) and [extensive documentation](https://zoobot.readthedocs.io/) is available if you would like to extend these models or apply them to new problems.


[Walmsley et al. (2025)](https://arxiv.org/abs/2503.15310)
describes the project and current data release.
Please cite this paper if using any data from Galaxy Zoo Euclid.


### Catalogue, Models, Representations

The GZ Euclid data is available via [Zenodo](https://doi.org/10.5281/zenodo.15002907).
This includes morphology measurements, the images (as shown to volunteers), and some common physical properties from the MER catalogues.
See the [Zenodo page](https://doi.org/10.5281/zenodo.15002907) for more details.


The morphology catalogue is also available (or will be soon) from NOIRLab's [Astro Data Lab](https://datalab.noirlab.edu/).
This service allows you to cross-match our catalogue against your own catalogues.
[Astro Data Lab](https://datalab.noirlab.edu/) also hosts data from DESI itself, allowing you to query DESI spectra and GZ Euclid morphology measurements [with the same tools.](https://datalab.noirlab.edu/tools.php)

For the first time, we are also sharing representations learned by our models. Due to the size, we share these compressed with either 40 or 100 PCA components.
The models themselves are available via [HuggingFace](https://huggingface.co/collections/mwalmsley/zoobot-encoders-65fa14ae92911b173712b874), and can be used to generate representations for new images.
Code and documentation for finetuning the models can be found in the [Zoobot](https://github.com/mwalmsley/zoobot) GitHub repository.


# Galaxy Zoo: Cosmic Dawn

Galaxy Zoo: Cosmic Dawn (GZCD) provides morphological classifications of over 41,000 galaxies across 6 square degrees of the Euclid Deep Field North (EDFN) from the Hawaii Twenty Square Degree (H20) survey, a part of the wider Cosmic Dawn survey.
This multiband Hyper Suprime-Cam (HSC) imaging featured galaxies down to apparent magnitudes of 21.5 in the HSC-i band and out to photometric redshifts of ~2.5 (or for which the photometric redshift estimation failed).
The subjects were also classified by the deep learning foundation model Zoobot, initially in an active learning cycle with volunteers before a final application to the data set.


As part of the data release, 51 new gravitational lenses in the EDFN were discovered from this iteration.
This data set provides a valuable opportunity for follow-up imaging of objects in the EDFN as well as acting as a truth set for training deep learning models for application to ground-based surveys like that of the Ultraviolet Near-Infrared Optical Northern Survey (UNIONS) collaboration and the newly operational Vera C. Rubin Observatory.


### Catalogue, Images

The GZCD data is available via [Zenodo](https://doi.org/10.5281/zenodo.17200991).
The data consists of morphological classifications made by volunteers as well as predicted classifications made by Zoobot (5.1 GB).
Also included are the subject images themselves (in PNG/JPG format), a file of metadata for each subject, and the tags assigned to the subjects by volunteers.
A Jupyter notebook is provided to give more details on the data set and examples of how to use it.
See the [Zenodo page](https://doi.org/10.5281/zenodo.17200991) for more details.


Zoobot was fine-tuned on this data set after being pretrained on all previous Galaxy Zoo labels - see the [Galaxy Zoo Euclid](https://data.galaxyzoo.org/#section-22) section above for more details - and predicts both the volunteer vote fractions and 90% confidence intervals.
The classifications are presented in a style suitable for machine learning tasks as well as a more human-readable version.
Also provided are 'friendly' versions that simplify the results to just the 'leaf fractions', i.e. vote fractions for the highest-predicted answers to each question.


# Galaxy Zoo: Mergers

See [this page](https://data.galaxyzoo.org/mergers.html) for full details and data for the separate [Galaxy Zoo: Mergers](http://mergers.galaxyzoo.org/) project.


# Galaxy Builder

[Galaxy Builder](https://www.zooniverse.org/projects/tingard/galaxy-builder/) made use of citizen science to create disc-bulge-bar-spiral photometric models of 198 spiral galaxies, selected using GZ2 and the NASA-Sloan Atlas. The project is further described in [Lingard et al. (2020)](https://arxiv.org/abs/2006.10450).

|     |     |
| --- | --- |
| Galaxy Builder main catalogue |
| [Column description and format](https://data.galaxyzoo.org/data/galaxy-builder/galaxy-builder-catalog-columns.md) |
| CSV | [galaxy-builder-catalog.csv](https://data.galaxyzoo.org/data/galaxy-builder/galaxy-builder-catalog.csv) |

# Data visualizations

For an interactive visualization of the decision trees for each of the Galaxy Zoo projects, please look at this tool created by Coleman Krawczyk (University of Portsmouth).


[Galaxy Zoo Decision Trees](https://data.galaxyzoo.org/gz_trees/gz_trees.html)

×

[Forgot your password?](https://www.zooniverse.org/password/reset) Sign in

×
This will be used when we thank contributors, for example, in talks or on posters.

If you don't want to be mentioned publicly, leave this blank.
I agree to the [privacy policy](https://www.zooniverse.org/privacy).

Sign up

──────── [TRUNCATED] ────────
Showing 29,881 chars (head) + 9,956 chars (tail) of 50,957 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/data.galaxyzoo.org-21e77be1c7.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/data.galaxyzoo.org-21e77be1c7.md" offset=418 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────