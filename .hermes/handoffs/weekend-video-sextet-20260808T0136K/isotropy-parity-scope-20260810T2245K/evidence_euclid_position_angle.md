# URL: https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html

### Navigation

- [index](https://euclid.esac.esa.int/dr/q1/dpdd/genindex.html "General Index")
- [next](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html "Background-Subtracted Mosaic Product") \|
- [previous](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merphotometrycookbook.html "MER Photometry Cookbook") \|
- [EUCL-EC-ICD-8-001 Data Product Description v2.0 (DM 10.0.4 - FDM 10.0.4 - EDEN 3.1\\
) documentation](https://euclid.esac.esa.int/dr/q1/dpdd/index.html) »
- [MER Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merindex.html) »
- [MER Morphology Cookbook](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html)

# MER Morphology Cookbook [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html\#mer-morphology-cookbook "Permalink to this heading")

## Introduction [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html\#introduction "Permalink to this heading")

The [MER final catalog](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#merfinalcatalog) contains a wealth of
morphological information collected for all objects and across all bands
(VIS, NIR and EXT). In this cookbook we document the various flavors of
morphological information available.

## Detection morphology [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html\#detection-morphology "Permalink to this heading")

As part of the detection process we calculate rather simple morphological
parameters. These parameters are computed from the light distribution within
the detection mosaic area (either in the VIS band
or in the NIR-stack band).

The relevant columns in the
[MER main catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-main-catalog-fits) are:

- `SEMIMAJOR_AXIS`: the semi-major axis of the ellipse describing the object
shape, in pixel units;

- `POSITION_ANGLE`: the position angle of the ellipse describing the object
shape, in degrees and using a counter-clockwise NE-SW convention;

- `ELLIPTICITY`: the ellipticity of the ellipse describing the object shape.


The information content of those columns corresponds to the parameters
`A_IMAGE`, `B_IMAGE`, `THETA_IMAGE`, as provided by SExtractor, or
`ellipse_a`, `ellipse_b`, `ellipse_theta`, as provided by
SourceXtractor++.

![../_images/morphology_cookbook_fig1.png](https://euclid.esac.esa.int/dr/q1/dpdd/_images/morphology_cookbook_fig1.png)

Fig. 32 A cutout of a VIS detection mosaic (size ~ 50’’ x 30’’) with the ellipses
associated to each detected object. [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#id1 "Permalink to this image")

## Extended CAS morphology [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html\#extended-cas-morphology "Permalink to this heading")

The parameters Concentration, Asymmetry and Clumpiness (CAS) correlate with
important modes of galaxy evolution: star formation and major merging activity.
In the MER pipeline these parameters are computed for VIS detected objects
following
[Conselice 2003](https://ui.adsabs.harvard.edu/abs/2003ApJS..147....1C) (and
references given therein). In addition, we compute
the Gini coefficient and the M20 coefficient described in
[Lotz, Primack & Madau 2004](https://ui.adsabs.harvard.edu/abs/2004AJ....128..163L).

The extended CAS values are stored in the
[MER morphology catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-morphology-catalog-fits)
in the following columns:

- `CONCENTRATION`

- `ASYMMETRY`

- `SMOOTHNESS`

- `GINI`

- `MOMENT_20`


## Zoobot morphology [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html\#zoobot-morphology "Permalink to this heading")

Zoobot is a deep learning model trained to measure detailed morphology (bars,
spiral arms, mergers, etc) using labels from
[Galaxy Zoo](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo)
citizen scientists.

The [MER final catalog](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#merfinalcatalog)
includes columns with these predictions for galaxies which are either bright
enough (VIS < 20.5 mag) or extended enough (`SEGMENTATION_AREA` \> 1200
pixels) that detailed morphology measurement makes sense. This is roughly 2% of
all MER sources.

Zoobot columns are named like _{question}\_{answer}_. For example, the column
`SMOOTH_OR_FEATURED_SMOOTH` measures the prediction for how many volunteers
would answer _“smooth”_ to the question: _“is this galaxy smooth or featured?”_

The [MER morphology catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-morphology-catalog-fits)
contains the following Zoobot columns:

- `BAR_NO`

- `BAR_STRONG`

- `BAR_WEAK`

- `BULGE_SIZE_DOMINANT`

- `BULGE_SIZE_LARGE`

- `BULGE_SIZE_MODERATE`

- `BULGE_SIZE_NONE`

- `BULGE_SIZE_SMALL`

- `CLUMP_COUNT_ANY_THRESHOLD`

- `CLUMP_COUNT_ABOVE_THRESHOLD`

- `CLUMP_COUNT_UNUSUAL_ANY_THRESHOLD`

- `CLUMP_COUNT_UNUSUAL_ABOVE_THRESHOLD`

- `DISK_EDGE_ON_NO`

- `DISK_EDGE_ON_YES`

- `EDGE_ON_BULGE_BOXY`

- `EDGE_ON_BULGE_NONE`

- `EDGE_ON_BULGE_ROUNDED`

- `LOPSIDED_NO`

- `LOPSIDED_YES`

- `HAS_SPIRAL_ARMS_NO`

- `HAS_SPIRAL_ARMS_YES`

- `HOW_ROUNDED_CIGAR_SHAPED`

- `HOW_ROUNDED_COMPLETELY`

- `HOW_ROUNDED_IN_BETWEEN`

- `MERGING_MAJOR_DISTURBANCE`

- `MERGING_MERGER`

- `MERGING_MINOR_DISTURBANCE`

- `MERGING_NONE`

- `SMOOTH_OR_FEATURED_ARTIFACT_STAR_ZOOM`

- `SMOOTH_OR_FEATURED_FEATURED_OR_DISK`

- `SMOOTH_OR_FEATURED_SMOOTH`

- `SPIRAL_ARM_COUNT_1`

- `SPIRAL_ARM_COUNT_2`

- `SPIRAL_ARM_COUNT_3`

- `SPIRAL_ARM_COUNT_4`

- `SPIRAL_ARM_COUNT_CANT_TELL`

- `SPIRAL_ARM_COUNT_MORE_THAN_4`

- `SPIRAL_WINDING_LOOSE`

- `SPIRAL_WINDING_MEDIUM`

- `SPIRAL_WINDING_TIGHT`

- `DWARF_YES`

- `DWARF_NO`

- `PECULIAR_YES`

- `PECULIAR_NO`

- `RING_YES`

- `RING_NO`

- `AGN_YES`

- `AGN_NO`

- `ETG_OR_LTG`

- `T_TYPE`

- `MAJOR_MERGER`

- `MAJOR_MERGER_UNCERTAINTY`

- `MAJOR_MERGER_STAGE`

- `MAJOR_MERGER_STAGE_PROBABILITY`

- `MAJOR_MERGER_STAGE_UNCERTAINTY`


The column values encode a posterior distribution for the answers to each
question. They are Dirichlet concentrations. The most common way to use these
is to convert them to _“the fraction of volunteers expected to select this_
_morphology answer”_ with the formula:

(8) [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#equation-morph-cookbook-equ-1 "Permalink to this equation")answersum for all answers to that question

For example, the fraction of volunteers expected to answer _“smooth”_ is:
`SMOOTH_OR_FEATURED_SMOOTH` / (`SMOOTH_OR_FEATURED_SMOOTH` +
`SMOOTH_OR_FEATURED_FEATURED_OR_DISK` +
`SMOOTH_OR_FEATURED_ARTIFACT_STAR_ZOOM`).

For more details consult the
[Zoobot github page](https://github.com/mwalmsley/zoobot) and the
[online documentation](https://zoobot.readthedocs.io/en/latest/).

## Parametric morphology [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html\#parametric-morphology "Permalink to this heading")

The MER pipeline performs a Sersic fit to all Euclid data. The actual fitting
is done with SourceXtractor++
( [Kümmel et al. 2022](https://ui.adsabs.harvard.edu/abs/2022arXiv221202428K),
[Bertin et al. 2020](https://ui.adsabs.harvard.edu/abs/2020ASPC..527..461B))
in no-detection mode. This fitting mode allows to perform model fits based
totally on positions and fitting areas provided in the program input, and is
independent of the SourceXtractor++ internal detection mechanism.

The fitting method is based on an iterative approach which takes into account
the differences in the resolution of the Euclid VIS and NIR bands. First a
Sersic model is fitted to the combined VIS and NIR (Y/J/H) data.
In a second Sersic fitting process the parameters determined on the VIS data
are used as a constant input to determine flux values on all available EXT
bands.

This fitting procedure was validated using Euclid data taken in the COSMOS
field.

![../_images/morphology_cookbook_fig2.png](https://euclid.esac.esa.int/dr/q1/dpdd/_images/morphology_cookbook_fig2.png)

Fig. 33 An illustration of the Sersic fitting result showing a cutout of the original
VIS mosaic (top), the Sersic model image (middle), and the residual image
(bottom). [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#id2 "Permalink to this image")

In order to keep the processing time in a reasonable range we implemented a
few limitations:

- A large amount of processing time is usually spent on the bright stars in the
FoV, since the fitting area, which is derived from the segmentation area, is
usually very large and thus involves a large data volume. Since these objects
are often saturated and do not promise reasonable fitting results, we have
set the fitting box to 50 x 50 pixels for all objects that, according to their
segmentation imprint, have a fitting area > 300 x 300 pixels.

- All objects that descended from the same parent object via deblending are
collected into a single fitting group, which means that the minimization of
their Sersic parameters is done together. Also in this area bright stars
usually result into a fitting group with many members since the deblending
tends to generate multiple objects along the diffraction spikes and in the
saturated core. Since this again would result in a long processing time for
one group only, we limit the number of objects in a group to 150.


The flux values from the Sersic fitting procedure for all photometric bands are
stored in the [MER main catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-main-catalog-fits)
(see the [MER photometry cookbok](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merphotometrycookbook.html#merphotometrycookbook) for more details)
with column names:

- `FLUX_<band>_SERSIC`


The [MER morphology catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-morphology-catalog-fits)
contains the parameters and qualitative results from the Sersic fits:

- `SERSIC_SERSIC_VIS_{RADIUS, AXIS_RATIO, INDEX}`

- `SERSIC_SERSIC_NIR_{RADIUS, AXIS_RATIO, INDEX}`

- `SERSIC_ANGLE`

- `SERSIC_VISNIR_{REDUCED_CHI2, ITERATIONS, FLAGS, DURATION}`

- `SERSIC_EXT_{REDUCED_CHI2, ITERATIONS, FLAGS, DURATION}`


## Point-like probability [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html\#point-like-probability "Permalink to this heading")

A simple Star-Galaxy (S/G) classifier has been historically implemented in the
MER pipeline in order to identify the point-like detected objects on which the
PSF characterization could be performed by SHE. In addition to the
`POINT_LIKE_FLAG`, a point-like probability (`POINT_LIKE_PROB`) was also
requested in the output catalog. Both values are stored in the
[MER main catalog FITS file](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html#mer-main-catalog-fits) for VIS-detected
objects. Notice that this classifier is heavily biased towards a high purity,
and thus has a low completeness.

The method is inspired from the `SPREAD_MODEL` method provided by
SExtractor which is used in
[Desai et al. 2012](https://ui.adsabs.harvard.edu/abs/2012ApJ...757...83D) and
[Sevilla-Noarbe et al. 2018](https://ui.adsabs.harvard.edu/abs/2018MNRAS.481.5451S).

Our method uses `MU_MAX` \- `MAG_AUTO` as a proxy of `SPREAD_MODEL`;
`MU_MAX` being the peak surface brightness above the background. Thus, our
estimator `MU_MAX` \- `MAG_AUTO` is related to the concentration of light
at the peak versus the total magnitude.

As shown in [Fig. 34](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#morphology-cookbook-fig3), the S/G separation is only
performed in VIS-detected objects. The current rule-of-thumb to select stars in
the MER catalog is: select very bright (even saturated) sources at VIS AB
magnitudes < 17, and to add all detections with `POINT_LIKE_PROB` \> 0.96.

Notice that `POINT_LIKE_FLAG` is defined as `POINT_LIKE_PROB` \> 0.96
AND `DET_QUALITY_FLAG` = 0, so this flag can also be used.

For a more complete selection of stars, please use in addition the color and
SED fitting information provided by PHZ.

![../_images/Point_like_proba_SG_separation.png](https://euclid.esac.esa.int/dr/q1/dpdd/_images/Point_like_proba_SG_separation.png)

Fig. 34 VIS and NIR detections in the `MU_MAX` \- `MAG_AUTO` plane for real
data from tile 102021495. Stars are prominently present in the bottom
horizontal branch. Black cross: sources identified as stars. Colors code the
probability of being a point source. [¶](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#id3 "Permalink to this image")

### [Table of Contents](https://euclid.esac.esa.int/dr/q1/dpdd/index.html)

- [MER Morphology Cookbook](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#)
  - [Introduction](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#introduction)
  - [Detection morphology](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#detection-morphology)
  - [Extended CAS morphology](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#extended-cas-morphology)
  - [Zoobot morphology](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#zoobot-morphology)
  - [Parametric morphology](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#parametric-morphology)
  - [Point-like probability](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html#point-like-probability)

#### Previous topic

[MER Photometry Cookbook](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merphotometrycookbook.html "previous chapter")

#### Next topic

[Background-Subtracted Mosaic Product](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html "next chapter")

### This Page

- [Show Source](https://euclid.esac.esa.int/dr/q1/dpdd/_sources/merdpd/mermorphologycookbook.rst.txt)

### Quick search

### Navigation

- [index](https://euclid.esac.esa.int/dr/q1/dpdd/genindex.html "General Index")
- [next](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html "Background-Subtracted Mosaic Product") \|
- [previous](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merphotometrycookbook.html "MER Photometry Cookbook") \|
- [EUCL-EC-ICD-8-001 Data Product Description v2.0 (DM 10.0.4 - FDM 10.0.4 - EDEN 3.1\\
) documentation](https://euclid.esac.esa.int/dr/q1/dpdd/index.html) »
- [MER Data Products](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/merindex.html) »
- [MER Morphology Cookbook](https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html)