# URL: https://arxiv.org/pdf/2309.11425

# Galaxy Zoo DESI: Detailed Morphology Measurements for 8.7M

# Galaxies in the DESI Legacy Imaging Surveys

1 ★ 2 3 1,4
Mike Walmsley , Tobias Géron , Sandor Kruk , Anna M. M. Scaife,
2 5 6 7
Chris Lintott , Karen L. Masters , James M. Dawson , Hugh Dickinson ,
8,9 10 8,9 10
Lucy Fortson, Izzy L. Garland, Kameswara Mantha, David O’Ryan,
7 10 11
Jürgen Popp , Brooke Simmons, Elisabeth M. Baeten, Christine Macmillan

1 _Jodrell Bank Centre for Astrophysics, Department of Physics & Astronomy, University of Manchester, Oxford Road, Manchester M13 9PL, UK_ 2 _Oxford Astrophysics, Department of Physics, University of Oxford, Denys Wilkinson Building, Keble Road, Oxford, OX1 3RH, UK_ 3 _European Space Agency (ESA), European Space Astronomy Centre (ESAC), Camino Bajo del Castillo s/n 28692 Villanueva de la Cañada, Madrid, Spain_ 4 _The Alan Turing Institute, 96 Euston Road, London NW1 2DB, UK_ 5 _Departments of Physics and Astronomy, Haverford College, 370 Lancaster Avenue, Haverford, Pennsylvania 19041, USA_ 6 _South African Radio Astronomy Observatory (SARAO), Black River Park North, 2 Fir St, Cape Town, South Africa, 7925_ 7 _School of Physical Sciences, The Open University, Milton Keynes, MK7 6AA, UK_ 8 _School of Physics and Astronomy, University of Minnesota, Minneapolis, Minnesota, 55455, USA_ 9 _Minnesota Institute for Astrophysics, University of Minnesota, Minneapolis, Minnesota, 55455, USA_ 10 _Department of Physics, Lancaster University, Lancaster LA1 4YB, UK_ 11 _Citizen Scientist, Zooniverse c/o University of Oxford, Keble Road, Oxford OX1 3RH, UK_

Last updated XXX; in original form XXX

## ABSTRACT

We present detailed morphology measurements for 8.67 million galaxies in the DESI Legacy
ImagingSurveys(DECaLS,MzLS,andBASS,plusDES).Theseareautomatedmeasurements
made by deep learning models trained on Galaxy Zoo volunteer votes. Our models typically
predict the fraction of volunteers selecting each answer to within 5-10% for every answer to
every GZ question. The models are trained on newly-collected votes for DESI-LS DR8 images
as well as historical votes from GZ DECaLS. We also release the newly-collected votes.
Extending our morphology measurements outside of the previously-released DECaLS/SDSS
intersection increases our sky coverage by a factor of 4 (5,000 to 19,000 deg²) and allows for
full overlap with complementary surveys including ALFALFA and MaNGA.

**Key words:** catalogues, software: data analysis, methods: statistical, galaxies: bar, galaxies:
interaction, galaxies: general

## 1 INTRODUCTION

Galaxy images reveal diverse structures such as spiral arms, bars,
bulges, and tidal features (Buta2013). The field of galaxy morpholarXiv:2309.11425v1 \[astro-ph.GA\] 20 Sep 2023ogy seeks to understand the origins of these structures. Relatedly,
these structures are thought to both influence and trace key physical
processes in galaxy evolution and so by measuring their presence
one can infer the history of those physical processes (Casteels et al.
2013;Géron et al.2023) .

Measuring the morphology of large samples of galaxies is crucial because many highly correlated variables influence both morphology and the processes they trace. Unpicking these correlations
requires large samples where one can hold these variables fixed
and still retain enough galaxies to draw statistically robust conclusions (Masters2019). One may also hope to find rare populations

of galaxies with properties that challenge our assumptions about
galaxy formation (e.g.Smethurst et al.2021;Keel et al.2022).

The scale of our morphology measurements is limited not by
our supply of telescope images but by our interpretation of those
images.Modernastronomicalobservatoriescapturedetailedimages
ofmillionsofgalaxies-asampleimpossibleforastronomerstoeven
begin to review by eye. To meet this challenge, astronomers have
developed methods to measure the detailed morphology of galaxies
through parametric and non-parametric fitting (e.g.Abraham et al.
1996;Simard et al.2002;Conselice2003;Lotz et al.2004), citizen
science (including Galaxy Zoo e.g.Lintott et al.2008;Willett et al.
2013), or machine learning (e.g.Huertas-Company et al.2008;
Banerji et al.2010;Ferrari et al.2015).

Combining deep learning with citizen science can achieve
morphology measurements with the classification detail of humans and the scale of automated systems (e.g.Dieleman et al.
2015;Domínguez Sánchez et al.2018, or seeHuertas-Company &

★Contact e-mail: [michael.walmsley@manchester.ac.uk](mailto:michael.walmsley@manchester.ac.uk)

* * *

2

Lanusse2022for a review). Galaxy Zoo DECaLS (Walmsley et al.
2022b, hereafter W+22) was the first to present a large-scale catalogue of morphology measurements for every Galaxy Zoo question
by training deep learning algorithms on citizen scientist responses.
Thiscataloguecoveredthe314,000galaxiesimagedbytheDarkEnergy Camera Legacy Survey (DECaLS) DR5 and within the SDSS
DR8 footprint.

DECaLS is part of the DESI Legacy Imaging Surveys (DESI-
LS), a set of three sister surveys designed to produce images with
similar characteristics. Here, in GZ DESI, we exploit this imaging
similarity to extend and apply the deep learning methods developed
for GZ DECaLS to all three DESI-LS surveys. We release new
automated predictions for 8.7M bright (𝑟 < 19) galaxies in DESI-
LSDR8.Fig.1showsrandomexamplegalaxiesandtheirautomated
morphology measurements.

The key benefit of our new morphology catalogue is scale.
Including MzLS and BASS, along with additional images from
DECaLS not classified in GZ DECaLS, increases our sky coverage from 5,000 deg2 to 19,000 deg2, with a proportional increase
in galaxies of all types. This increase in sample size is crucial for
investigating specific morphologies (e.g. weak bars) or controlling
for astrophysical variables (e.g. mass, star formation, environment,
etc),particularlywhenconstructingvolume-limitedsubsetsofwellresolved galaxies. Fig.2compares our coverage with various existing morphology catalogues and surveys.

$$
19{,}000,\\mathsf{d e g}^{2}
$$

Classifying morphology at this scale is made possible by combining citizen science with deep learning. Our general approach is
to train models primarily on the volunteer labels collected during
GZ DECaLS and then predict what volunteers would have said for
images from DECaLS’ sister surveys. In practice, despite the similarity of the images, making accurate predictions is non-trivial.
One key complication is label drift (Amos2008). Due to changes
in the Galaxy Zoo decision tree, website content, and other factors,
volunteer votes collected in our most recent campaign (2020-2022)
may not be equivalent to volunteer votes collected at the start of
the first Galaxy Zoo DECaLS campaign (2015). We would like to
predict what volunteers might say now, with the current decision
tree, and not what they might have said during earlier campaigns.
To benefit from the seven years of Galaxy Zoo labels collected during those earlier campaigns while still predicting what volunteers
might say now, we adapt our models to separately predict what a
typical volunteer would have answered had they voted during each
campaign.

GZ DESI includes fainter (𝑟 < 19.0 vs. 𝑟 ⪅ 17.77), smaller
(see Sec.5.3), and higher redshift (𝑧 ⪅ 0.4 vs. 𝑧 < 0.15) galaxies
thanGalaxyZooDECaLS.Wewillshowthatourpredictionsforthe
apparent morphology of these galaxies are reliable (Sec.4). However, the difficulty in imaging morphology under such constraints
causes apparent morphology to be an increasingly poor proxy for
absolute morphology (i.e. the morphology that would be observed
if the galaxy were closer). Researchers using our catalogues should
ensure their conclusions are not sensitive to this observational bias.

$$
(r < 1 9. 0 \\mathrm {v s}. r \\lesssim 1 7. 7 7)
$$

$$
(z\\lessapprox0.4;\\mathrm{v s.;z}<0.15)
$$

This paper is structured as follows. We summarise the data
available from the DESI-LS sister surveys (DECaLS, MZLS and
BASS) and our approach to selecting galaxies and constructing
images in Sec.2. We describe training our deep learning models in
Sec.3, focusing on our new approach to learn from multiple Galaxy
Zoo campaigns simultaneously (unlike in GZ DECaLS itself). We
measure and compare the accuracy of our models against other
approaches in Sec.4. Finally, we apply the trained models to all
three sister surveys and introduce our catalogues in Sec.5.

The morphology catalogues are available for download from
Zenodo, CDS/Vizier, and NOIRLab’s Astro Data Lab. See AppendixAfor further details. The code and weights for our deep
learning models are available viaGitHub.

## 2 DATA

## 2.1 Surveys

TheDarkEnergySpectroscopicInstrument(DESI)isacosmologyfocused multi-object fibre spectrograph at the 4m Mayall telescope
on Kitt Peak, USA. DESI requires images to target its spectroscopic
fibers; these are primarily provided by the DESI Legacy Surveys
(DESI-LS).

DESI-LS is composed of three individual surveys working in
concert; DECaLS, BASS, and MzLS. BASS and MzLS cover the
northern sky from Kitt Peak, USA; BASS captures _𝑔_ and _𝑟_-band
images using the Bok 2.3m telescope and MzLS captures _𝑧_-band
images with the same 4m Mayall telescope as DESI itself. We
refer to both surveys jointly as BASS/MzLS. DECaLS captures _𝑔𝑟𝑧_
images of the southern sky from the 4m Blanco telescope at Cerro
Tololo Inter-American Observatory, Chile. Together, DECaLS and
BASS/MzLSprovide14,000deg2 of _𝑔𝑟𝑧_ targetingimagesforDESI.

$$
14{,}000,\\mathsf{d e g}^{2}
$$

Also noteable is the Dark Energy Survey (DES), an imaging
survey focused on photometric redshifts. DES is not technically
part of the DESI-LS; the primary survey footprint of 𝛿 < −18 is
too far south to be observed by DESI from Kitt Peak. However,
DES is being conducted with the same instrumentation as DECaLS
(DECam on the 4m Blanco telescope), and so DES imaging is
included in the DESI-LS data releases.

$$
\\delta<-18
$$

Specifically, DESI-LS DR8 includes all 5,000 deg2 of _𝑔𝑟𝑧_
imaging taken by DECam as part of DES and released in DES
DR2.

$$
\ {\\mathfrak{l,}}00\\\mathsf{d e g}^{2}
$$

The four surveys (DECaLS, BASS/MzLS, and DES) together
cover a combined area of 19,437 deg2. Their imaging properties are
similar by design; DESI requires depths to be ‘as uniform as possible across the survey footprint’ for consistent target selection (Dey
etal.2019).Thiswassuccessfullyachieved.TheDESI-LSwebsite1
shows median coadded depths (5 _𝜎_ detection of a point source) of
approximately _𝑔_ = 24\*. _8, 𝑟 = 24_. _2, and 𝑧 = 23_. _4 for DECaLS, and_
_𝑔 = 24_. _2,𝑟 = 23_. _8,and 𝑧 = 23_. _3 forBASS/MzLS.DESDR2quotes_
_a median coadded catalogue depth for a 1′′95 diameter aperture at_
_signal-to-noise ratio = 10 of 𝑔 = 24_. _7, 𝑟 = 24_. _4, and 𝑧 = 23_.\*1\. This
unique combination of deep and wide images is ideal for large-scale
morphology classification. Consistent imaging properties allow us
to train deep learning models on volunteer classifications for a subset of images and then predict what volunteers would say for the
remainder.

$$
19,\ 37,\\mathsf{d e g}^{2}
$$

$$
g=24.8,r=24.2
$$

$$
g=24.2,r=23.8.
$$

$$
g=24.7,r=24.4
$$

AsubsetofDECaLSimagesinDESI-LSDR5werepreviously
classifiedbyGalaxyZoovolunteers.Thesevolunteerclassifications
were released as part of Galaxy Zoo DECaLS (W+22). The GZ
DECaLS volunteer classifications provide the bulk of the training
data we use in this work. We describe the GZ DECaLS subset
selection and labelling process in more detail in Sec.3.

## 2.2 Source Identification and Photometry

The DESI-LS source database (i.e. the coordinates and basic photometryofidentifiedsourcesintheDESI-LSimages)isconstructed

1 [https://www.legacysurvey.org](https://www.legacysurvey.org/)

* * *

# Galaxy Zoo DESI

**Figure 1.** DESI-LS galaxies with their GZ DESI automated morphology measurements. Percentages reflect the percentage of volunteers predicted to select

that answer. We show only galaxies where at least 15% of volunteers are expected to vote ‘Featured’ and with a redshift below 0.1, to better illustrate the detail of our morphology measurements; galaxies are otherwise randomly selected.

MNRAS,1–18(2023)

* * *

4

**Figure 2.** Sky coverage of GZ DESI (i.e. (DECaLS/BASS/MzLS/DES), GZ
\[Image: Im2\]
DECaLS (i.e. the DECaLS and SDSS intersection), and DES in DESI-LS
DR8

**Figure 3.** Photometric redshifts and estimated stellar masses of GZ DESI
galaxies. Measurements fromZou et al.2019(see AppendixE).

using the Bayesian sourcefinding tool tractor (Lang et al.2016).
We query the tractor database using the Table Access Protocol (TAP) server made available by the DESI-LS collaboration at
[https://datalab.noirlab.edu/tapto](https://datalab.noirlab.edu/tapto) select all extended2 sources with
𝑟 < 19.0. We selected this cut by visual inspection with the aim of
identifying an approximate limit beyond which galaxies rarely have
meaningful resolved visual morphology.

$$
r<19.0
$$

To remove stellar contamination, we exclude sources with an
approximate surface brightness lower than 18 mag arcsec−2, calculated as

$$
\\mu=\\mathrm{m a g} _{\\mathrm{r}}+2.5\\log_{10}\\left(\\pi r^{2}\\right),,
$$

(1)

where _𝜇_ is the surface brightness, magr the r-band magnitude
and _𝑟_ the estimated radius. The radius was estimated using:

$$
\\mu
$$

$$
r=f,r\_{\\mathrm{D e V}}+\\left(1-f\_{\\mathrm{D e v}}\\right)r\_{\\mathrm{E x p}},,
$$

(2)

where _𝑟_ DeV, _𝑓_ Devand _𝑟_ Expare photometric properties
estimated by tractor. In short, tractor models sources as a
weighted mixture of an exponential (Exp) and a De Vaucouleurs
(DeV) light profile. It reports the fraction of light attributable to
each profile ( _𝑓_ Dev, _𝑓_ Exp) and the angular half-light radius of those
profiles by band (e.g. _𝑟_ DeV, _𝑟_ Exp).

$$
r\_{\\mathrm{E x p}}
$$

$$
(f\_{\\mathrm{D e v}},f\_{\\mathrm{E x p}})
$$

Our magnitude 𝑟 < 19.0, surface brightness 𝜇 > 18 mag
arcsec−2 and non-PSF selection leads to a total of 8,956,477
sources. We download reduced flux measurements of each source
using the DESI-LS cutout service. We refer to these measurements
as native images. Native images are downloaded at telescope resolution (0.262 arcsec per pixel) with a field-of-view as similar as
possible to the field-of-view which GZ DECaLS would have used,
had the galaxy been included in GZ DECaLS. This is to make the
new images on which we make predictions as similar as possible
to the GZ DECaLS images used for training (i.e. to minimise the
distribution shift). We describe the details of this field-of-view calculation in AppendixB. The field-of-view is calculated according
to the estimated radius of the galaxy, with the aim that galaxies of
different angular size (due to e.g. greater distance) fill a consistent
portion of the image.

$$
r\\ll19.0.
$$

$$
\\mu,>,18
$$

$$
^{8,956,477}
$$

## 2.3 RGB Images

WenextconvertthenativeimagestoRGBimagessuitableforhuman
and automated classification. As with field-of-view, we minimise
distribution shift by following the same process as GZ DECaLS.

2i.e. of tractor class other than ‘PSF’

Images are resampled from arbitrary pixel dimensions at native telescope angular resolution to 424x424 pixels at arbitrary angular resolution. We repeat the same colouring process as GZ DE-
CaLS(W+22),whichtypicallyleadstoimageswithlesspronounced
colour than in e.g. GZ2 (Willett et al.2013).

Images with more than 20% of flux measurements missing in
any band are discarded. 8,733,858 (97.8% of 8,925,926) are successfully downloaded from the DESI-LS cutout service, of which
8,689,370(99.5%)havenomorethan20%missingfluxinanyband.
Our final sample is thus these 8,689,370 galaxies.

## 3 MORPHOLOGY CLASSIFICATIONS

Our goal is to provide accurate morphological classifications for
every galaxy image in DESI-LS. It is not feasible to do this with
volunteers alone. GZ DECaLS collected 7.5 million individual volunteer classifications over 4.5 active years, for an average rate of
approximately 1.7 million classifications per year. At that rate, collecting 40 classifications per DESI-LS galaxy (the standard prior
to GZ DECaLS) would take approximately 200 years. Collecting 5
classifications, the minimum used by GZ DECaLS (which prioritised volunteer effort towards galaxies most informative for training
models, W+22), would still take an impractical 25 years. We must
therefore rely on automated methods for most galaxies.

We have two sources of volunteer classifications with which
we can train models to make predictions on new DESI-LS images.
Our first source of labels is the 7.5 million GZ DECaLS classifications mentioned above. A subset of these were already used for
training GZ DECaLS models. However, changes to the Galaxy Zoo

* * *

5

websiteduringtheprojectmeanclassificationscollectedearlyinGZ
DECaLS are not necessarily equivalent to classifications collected
at the end. Sec.3.1describes our method for resolving this shift to
trainonallGZDECaLSclassifications.Oursecondsourceoflabels
is the additional volunteer classifications collected subsequently to
GZ DECaLS (DESI-LS DR8). We use the new classifications of
DESI-LS DR8 as additional training data to improve our models,
particularlyinthefaint,high- _𝑧_,low-angular-sizeregimenotcovered
by GZ DECaLS. Sec.3.2describes the collection of our additional
labels.

## 3.1 Multi-Campaign Training

GZ DECaLS is our key source of training labels, providing 70%
of our 10M volunteer classifications (76% of our 401k labelled
galaxies). Unfortunately, learning from these labels is complicated
by the fact that labels collected at the start of GZ DECaLS are
not equivalent to labels collected at the end. This phenomenon is
generally known as _label shift_ (Amos2008). Below, we describe
the context and causes of our label shift and then discuss how we
work around it to train models on all labels simultaneously.

## 3.1.1 Context and Causes of Label Shift

GZ DECaLS collected classifications over three Galaxy Zoo campaigns; GZD-1, GZD-2, and GZD-5, covering DECaLS images
first released in DESI-LS DR1, DR2, and DR5. GZD-1 and GZD-
2 ask identical questions (we will often group them as GZD-1/2).
GZD-5 adjusted those questions based on preliminary results from
GZD-1/2 and on the developing science interests of the community.
Some questions were unchanged, some had minor adjustments (e.g.
from four to five possible bulge size answers) and some were entirely reworked (e.g. to improve sensitivity to weak bars and minor
mergers). Volunteers were therefore asked different questions, with
differentpossibleanswers,forGZD-1/2vs.GZD-5galaxies-aclear
incompatibility for standard supervised training approaches.

Evenwherethequestionsandpossibleanswersareunchanged,
volunteers might systematically select from those possible answers
inslightlydifferentways.Questionswereclarifiedthoughupdatesto
the descriptive answer icons, the tutorial, and the field guide. These
had the explicit intention of slightly altering the distribution of
answers that volunteers select, in order to better match the scientific
aim of the question. Unintended changes are also possible; over
the seven years between the start of GZD-1 and the end of GZD-
5, the population of volunteers itself may have gradually shifted.
These intentional and unintentional changes mean that volunteers
selectingagivenanswertoagivenquestionshouldnotbeinterpreted
in exactly the same way.

In short, GZD-1/2 and GZD-5 asked slightly different questions and received slightly different distributions of responses. We
therefore cannot naively use the responses for GZD-1/2 and GZD-5
as interchangeable training labels.

ThemodelsusedtocreatetheGalaxyZooDECaLSautomated
catalogue side-stepped this issue by training only with responses
from the GZD-5 campaign. This strategy worked but was not optimal. Responses are roughly equally divided between GZD-1/2
(3.43M responses) and GZD-5 (3.84M responses) and so the GZ
DECaLSmodelsweretrainedusingonlyhalfoftheresponsesavailable. Previous work shows that Galaxy Zoo models perform better
where more training labels are available (Walmsley et al.2020) and
so simplifying the training process by discarding half of the labels likely reduced model performance. Further, volunteers kindly

contribute their time to labelling galaxies and so we have a responsibility to use those labels efficiently i.e. to derive as much science
value as possible. We should ideally use all the training labels available. To do so, we introduce a new multi-campaign loss function
that allows models to learn from several Galaxy Zoo campaigns
simultaneously.

## 3.1.2 Multi-Campaign Loss Function

Different Galaxy Zoo campaigns asked different questions with different possible answers and received different distributions of volunteer responses. We would like to learn from all of these responses
across campaigns, in order to maximise our training data and create
better models. To do so, we will treat predicting the responses for
each campaign as separate prediction tasks that use the same shared
representation. We provide the mathematical details below.

Consider a scenario where some Galaxy Zoo campaign A asks
question _𝑞 𝐴_ for galaxies _𝐺 𝐴_ and campaign B asks question _𝑞 𝐵_
for galaxies _𝐺 𝐵_. Assume we can encode the volunteer responses
(label) for some galaxy _𝑔_ as vectors _𝑘 𝐴_ or _𝑘 𝐵_, depending on which
campaign labelled the galaxy. For example, campaign GZD-1/2
asked volunteers if a galaxy had a bar, with possible answers ‘Yes’
or ‘No’, while campaign GZD-5 offered possible answers ‘Strong’,
‘Weak’, or ‘No’. We could encode the volunteer response as vote
countse.g. _𝑘 𝐴_ = \[3\*, _0\] if3volunteersresponded‘Yes’duringGZD-_
_1/2 or as 𝑘 𝐵 = \[2_, _1_,\*0\] if 2 volunteers responded ‘Strong’ and 1
volunteer responded ‘Weak’ during GZD-5. Note that _𝑘 𝐴_ and _𝑘 𝐵_
may be different lengths.

$$
q\_{A}
$$

$$
G\_{A}
$$

$$
G\_{B}
$$

$$
k\_{A}
$$

$$
k\_{B}.
$$

$$
k\_{A}=\[3,0\]
$$

$$
k\_{B},=,\[2,1,0\]
$$

$$
k\_{A}
$$

$$
k\_{B}
$$

One simple way to train a single model to predict answers
to both campaigns would be to write a loss function that, if the
galaxy _𝑔_ ∈ _𝐺 𝐴_, treats the model outputs as a prediction of _𝑘 𝐴_,
and vice versa for _𝐵_. A straightforward implementation would be
to concatenate _𝑘 𝐴_ and _𝑘 𝐵_ (where one would be filled with default/masked values), use a model with fixed output dimension
_𝐷_ model= _𝐷_ ( _𝑘 𝐴_)\+ _𝐷_ ( _𝑘 𝐵_), and a loss function that ignores default/masked values (and hence provides gradients that depend only
on the relevant question). Conveniently, the Dirichlet-Multinomial
loss function introduced in W+22 is just such a function.

$$
g,\\in,G\_{A},
$$

$$
k\_{A}.
$$

$$
k\_{A}
$$

$$
k\_{B}
$$

$$
D\_{\\mathrm{m o d e l}}=D(k\_{A})+D(k\_{B})
$$

For each question, the loss takes the form:

$$
\\mathcal{L}\_{q}=\\int\\mathrm{\\bf M~Muli}(\\vec{k}\|\\vec{\\rho},N)\\mathrm{Dirichlet}(\\vec{\\rho}\|\\vec{\\alpha})d\\vec{\\rho}
$$

(3)

where, for some target question _𝑞_, _𝑘_ ® is the (vector) counts
of responses (successes) of each answer, _𝑁_ is the total number of
responses (trials) to all answers, and _𝜌_ ® is the vector of probabilities
of a volunteer giving each answer. _𝜌_ ® is drawn from Dirichlet(® _𝜌_ \|® _𝛼_),
wherethemodelpredictstheDirichletconcentrations _𝛼_ ®.Intuitively,
this loss corresponds to the odds of observing _𝑘_ heads (votes for an
answer) after _𝑁_ coin flips (volunteers asked) assuming a (modelpredicted) distribution for the bias of that coin. See W+22 for an
extended description.

$$
q,\\vec{k}
$$

$$
\\vec{\\rho}
$$

$$
(\\vec{\\rho}\|\\vec{\\alpha})
$$

$$
\\vec{\\rho}
$$

Assuming answers to different questions are independent, the
loss may be applied to multiple questions via the sum
∑︁

$$
\\mathcal{L}=\\sum\_{q}\\mathcal{L} _{q}(\\vec{k_{q}},N\_{q},\\vec{f\_{q}^{w}})
$$

(4)

where,forquestion _𝑞_, _𝑁𝑞_ isthetotalnumberofvotesforallanswers,
_𝑘_ ® is the observed votes for each answer, and _𝑓_ ® is the predictions
_𝑞 𝑞𝑤_
of our deep learning model for all answers (which we interpret as
the Dirichlet _𝛼_ ® parameters in Eqn.3).

$$
N\_{q}
$$

$$
\\vec{k\_{q}}
$$

$$
f{\\vec{f}}\_{q}^{}}
$$

W+22 introduced this loss in the context of questions where

* * *

6

_some_ answersmayhave0votes.Here,weconsiderthecontextwhere
_all_ answersmayhave0votes(becausethequestionisnotaskedinthe
campaign). When all answers have 0 votes, _𝑝_( _𝑎_ = 0\|® _𝛼,𝑁_ = 0) = 1
𝜕L
for all _𝛼_ ® and hence = 0, meaning unanswered questions do not
𝜕 _𝛼_ ®
affect the training gradients. The loss naturally handles questions
with no answers. We can therefore train a single model to predict
answers to different questions in different campaigns.

$$
p\\big(a=0\\big\|\\vec{\\alpha},N=0\\big)=1
$$

$$
\\frac{\\partial\\mathcal{L}}{\\partial\\vec{\\alpha}}=0
$$

What about if the same question is asked in multiple campaigns, but volunteers give systematically different answers? Such
a scenario is likely here due to e.g. clarified instructions over the
course of GZ DECaLS (see Sec.3.1.1). Our brute-force solution is
to always consider questions as different between campaigns, even
if the question itself has not changed. We construct a multi-question
multi-campaign label vector _𝐾_ ® where _𝐾𝑖_ is the votes for answer _𝑖_
and _𝑖_ indexes all answers across all questions _across all campaigns_.
For a galaxy labelled in any single campaign, _𝐾𝑖_ is 0 for any answer _𝑎𝑖_ to any question not asked in that campaign. Every answer
is always predicted but the prediction only affects training if votes
for that answer are non-zero. Intuitively, this corresponds to having
zero recorded votes to questions not asked in that campaign. Questions in different campaigns (GZD-1/2, GZD-5, and GZD-8) are
effectivelytreatedasseparatepredictiontasksusing thesamerepresentation. With this setup, the model learns a shared representation
for predicting every answer to every question in every campaign,
even when the questions are different or the distributions of answers
have changed.

$$
K\_{i}
$$

$$
\\vec{K}
$$

$$
K\_{i}
$$

$$
\\alpha\_{i}
$$

## 3.2 New Volunteer Labels

Our multi-campaign loss allows us to jointly learn from volunteer
responses to multiple Galaxy Zoo campaigns. While the GZ DE-
CaLS models were trained only on GZD-5 responses, we can now
learn from both GZD-1/2 and GZD-5. Further, we can also run new
campaigns to collect new responses, and jointly learn from those
new responses as well.

Following the conclusion of GZD-5 (November 2020), we
asked Galaxy Zoo volunteers to label DECaLS images newly released in DESI-LS DR8. We later expanded this to include all
DESI-LSDR8images(i.e.alsoincludingMzLSandBASS).GalaxieswererandomlyselectedfromthecataloguedescribedinSec.2.2,
excluding galaxies already classified by volunteers in GZ DECaLS.
RGB images were constructed as described in Sec.2.3, except that
the field-of-view was directly set by the weighted half-light radius
_𝑓_ DeV(see Sec.2.2) rather than approximating the NSA Petrosian
radii (see AppendixB) as work on those approximations was still
ongoing at the time. The classification procedure was identical to
GZD-5 (i.e. we made no further changes to the Galaxy Zoo website itself). We refer to the campaign gathering these new labels as
GZD-8.

While the imaging quality is comparable to GZ DECaLS, the
galaxies classified are dramatically different. Recall that GZ DE-
CaLSrequiredgalaxiestobelistedintheNASA-SloanAtlas(NSA).
The NSA was derived from SDSS images and hence typically has
𝑟 ⪅ 17.77 and 𝑧 < 0.15. Removing the NSA requirement removes
this additional selection function and hence the newly-classified
DR8 galaxies (and indeed all DR8 galaxies) are generally higher
redshift, smaller, and fainter than those classified in GZ DECaLS.

$$
r\\lessapprox17.77
$$

Between Nov. 2020 and Oct. 2022, 38,949 volunteers3 made

3.2Mclassificationsof105kgalaxies.AswithGZDECaLS4,weremove as statistically unlikely the classifications of 347 users (0.9%)
who classified at least 150 galaxies and answered ‘artifact’ for a
majority of those galaxies. Unlike earlier Galaxy Zoo works, but in
keeping with Galaxy Zoo DECaLS, we do not attempt to re-weight
volunteer votes to improve consistency (‘weighted vote fractions’).
We use the new responses to DESI-LS images as additional training
data, which we anticipate will be particularly helpful for making accurate automated classifications of fainter, higher-redshift galaxies
not previously labelled.

$$
s^{4}
$$

## 3.3 Model and Training Details

Our model is a variant of EfficientNetB0 (Tan & Le2019) with the
classificationhead(i.e.thefinallayerfollowingtheglobalmaxpooling) replaced by an alternative head suitable for predicting Dirichlet
concentrations. Specifically, the final layer has 98 units, each with a
sigmoidactivationfunctionscalingtheoutputstofallbetween1and
1015\. We chose EfficientNetB0 as our base architecture to balance
performance with practicality. The EfficientNet family is designed
to achieve high accuracy relative to their fast (here, 15ms/galaxy)
inference speed. B0 is also small enough (approx. 4M parameters)
to be trainable on consumer-grade GPUs, which we consider critical to making our models useful for other astronomers. AppendixC
provides full details of constructing our training sets, defining and
training our models, and selecting our hyperparameters.

$$
\\mathbf{G P U s},
$$

## 4 MODEL PERFORMANCE RESULTS

The goal of this paper is to accurately measure visual morphology
for every well-resolved galaxy in DESI-LS (Sec.2). The scale of
DESI-LS requires that we first train models to reproduce the responses of Galaxy Zoo volunteers for a small subset of DESI-LS
galaxies, and then use those models to predict how GZ volunteers
would respond for the bulk of the galaxies. We therefore need to
carefully check that our models do indeed accurately reproduce the

[... middle omitted — see footer ...]

a tractor-estimated pixel scale within 20% of the pixel scale they would
have had if we had access to NSA Petrosian radii. They would therefore
have similar fields-of-view to GZ DECaLS galaxies, ensuring our DECaLSderived labels remain applicable.

imented with reducing the learning rate on loss plateau and found
no convincing evidence that this improved performance.

Wetrainourmodelsusing240GBNVIDIAA100GPUsavailable via IRIS13. We train using PyTorch’s ‘distributed data paral-

$$
\\mathrm{I R I S^{13}}
$$ lel’ configuration i.e. each model draws subbatches from a different
fixed data split and shares weight updates. Training time for each
model depends on the dataset chosen. Training on GZD-5 (223k
galaxies) takes approx. 6 hours while training on all campaigns
(GZD-1/2/5/8, 401k galaxies) takes approx. 10 hours.

## C0.3 Hyperparameter Search

The hyperparameters (and fundamental design) of our base model,
EfficientNetB0 (Tan & Le2019), were chosen to optimise a balance
of prediction FLOPs and test accuracy on ImageNet (Russakovsky
etal.2015).Theidealhyperparametersmayvarybytaskanddataset,
andsoitisplausiblethatbetterhyperparametersexistforourspecific
goalofpredictingGalaxyZoovolunteervotes.InthisAppendix,we
search for those better hyperparameters, and find that the published
hyperparameters are indeed close to optimal for our specific task.

It is important to avoid the possibility that our reported
performance improvements from training on all campaigns (Sec.
4) are caused by the hyperparameters of the model simply being
highly tuned to learning from all campaigns. To avoid this, we only
tune our hyperparameters using the GZD-5 campaign data.

$$
\\beta\_{0}
$$

Our hyperparameter search procedure is as follows. We first
select our hyperparameters to optimise, dividing them into architectural or augmentation hyperparameters. For our architectural parameters, we select the image size (as interpolated and input to the
network),thebatchsize,thelearningrate,thedrop-connectrate,the
(head) dropout rate, and the _𝛽_ 0momentum parameter of the Adam
optimiser. For our augmentation parameters, we select the upper
and lower bounds of the relative crop size and the upper and lower
boundsofthecroppedaspectratio.Wethenexecutearandomsearch
for each set of hyperparameters i.e. we train many models with randomised architectural or augmentation hyperparameters. We train
152 models with randomised architectural parameters and 55 models with randomised augmentation parameters, reflecting our larger
architectural search space. Random searches are robust and effective when the important hyperparameters are not previously known
Bergstra et al.(2012). We assume that the best choice of architectural parameters is independent of the best choice of augmentation
parameters, and so they can be searched separately.

When training each model, we divide GZD-5 into random
train/validation/testsplitsofsize70%/10%/20%.Wetrainthemodel
until the validation loss does not decrease for 10 epochs (early
stopping) and then record the test loss. Optimising the test loss is
appropriate because the validation loss will be biased low due to
early stopping, and because we will make no further changes to
the model design before retraining on additional campaigns and
reporting our performance.

$$
70%/10%/20%
$$

Fig.C1shows the effect of key architectural hyperparameters.
We find that larger batch sizes and larger image sizes likely improve
performance. We find that the ideal learning rate is likely close to
the conventional default of 10−3 (which we ultimately opt to use).
We find no significant evidence that the drop-connect rate, dropout
rate or _𝛽_ 0momentum affect performance on our task, and set these
to their conventional defaults (0.2, 0.5 and 0.9 respectively).

$$
10^{-3}
$$

$$
\\beta\_{0}
$$

Weultimatelyselectabatchsizeof256(512acrossbothGPUs)
and an image size of 224. We felt that the additional memory footprint of training on larger images was not a sensible trade-off. Our
goal is to create models which other researchers can easily finetune.
The image size during finetuning must match our (pre)training image size and so (pre)training on larger images would significantly
increase the memory footprint required to use our models (e.g.

**Figure C1.** Architectural hyperparameter search results for batch size
(upper), image size (middle), and learning rate (lower). Larger batch sizes
and larger images are likely helpful. The ideal learning rate is likely close
to the conventional 10−3value.

$$
10^{-3}
$$

Test loss given a hyperparameter is calculated after filtering for models
where the other hyperparameters are close to optimal i.e. after fixing batch
size to 128 or 256, and/or image size to 224 or 260. Errorbars show the
95% confidence interval on the mean test loss.

* * *

+60% for 300x300 vs. 224x224 images) We prefer to create models
which have slightly less-than-optimal performance but are practical
for other researchers to use.

For the augmentation hyperparameters, we find no significant
evidencethateitherrelativecropsizeandcroppedaspectratioaffect
test performance, and so we arbitrarily set these hyperparameters
to visually sensible values (0.7–0.8 relative crop size bounds and
0.9–1.1 cropped aspect ratio bounds).

## APPENDIX D: GZD-8 CONFUSION MATRICES

This Appendix shows the confusion matrices for each question for
a random model trained on all campaigns (GZD-1/2/5/8) making
predictions on a random 20% test subset of GZD-8.

Our models predict posteriors for the expected distribution of
possible responses. Here, for intuition only, these posteriors are
converted to discrete classifications by rounding the observed vote
fraction (label) and mean of the expected vote count posterior (prediction) to the nearest integer. The matrices then show the counts
of rounded predictions (x axis) against rounded labels (y axis).
To avoid the loss of information from rounding, we encourage researchers not to treat Galaxy Zoo classifications as discrete, and
instead to use the full vote fractions or posteriors where possible.

We define a correct classification as one where the answer
withthehighestpredictedvotefractionmatchestheanswerwiththe
highest actual volunteer vote fraction. We also apply the minimum
total votes of 34 and relevance criteria described in Sec.4.2).

Fig.D1-D2shows confusion matrices for all galaxies passing
the total votes and relevance criteria above (left) and for only those
galaxies where volunteers were confident (right), defined as the
actual volunteer vote fraction being greater than 0.8.

## APPENDIX E: CROSS-MATCHING TO EXTERNAL DATA

Galaxy morphology is one of many measurable galaxy properties.
We have cross-matched our GZ DESI morphology catalogue to
several external catalogues of other galaxy properties. We hope that
this will help reveal how morphology affects, and is affected by,
those properties.

We include data from the NASA-Sloan Atlas (NSA,Aguado
et al.2019), the OSSY Type 1 AGN catalogue (Oh et al.2015), the
AreciboLegacyFastALFASurvey(ALFALFA,Haynesetal.2018),
the MPA-JHU SDSS DR7 derived properties catalogue (Abazajian
et al.2009), and the DESI photometric redshift catalogue by (Zhou
et al.2021). Please credit the original authors of these external
catalogues when using their data.

We cross-match the quoted (optical) coordinates of sources in
eachoftheabovecatalogueswiththe tractor sourcecataloguecoordinates underlying our morphology catalogue. We match sources
within 10 arcseconds. For the rare case where multiple external
sources match a tractor source, the closest external source is
selected and any remaining sources are dropped.

We combine the redshifts from these external catalogues for
Fig.7and when selecting the low redshift subsets in our data release. We select redshifts in the following priority order: SDSS
spectroscopic redshifts from the NSA, then from OSSY, and then
the spec\_z and photo\_z columns fromZhou et al.(2021).

This paper has been typeset from a TEX/LATEX file prepared by the author.

* * *

_All Galaxies_

_High Volunteer Confidence_

**Figure D1.** Confusion matrices for each question, made on the 11,349 galaxies in the (random) GZD-8 test set with at least 34 votes. Classifications are
considered correct if the answer with the highest predicted vote fraction matches the answer with the highest actual volunteer vote fraction. For each question’s
confusion matrix, we only show galaxies where a majority of volunteers were asked that question (see main text). The right-hand matrices are additionally
filtered to only show galaxies where the volunteers were confident. This is defined as the actual volunteer vote fraction being greater than 0.8 i.e. where at least
80% of volunteers agreed on an answer.

* * *

# M. Walmsley

Strong

Weak 32 134 44 **Bar** Predicted No 14 99 Strong Weak No True

0 0 0 0 0 Dominant Large 1 7 7 1 0 0 15 89 8 **Bulge Size** Predicted Small 0 0 83 12 Moderate

None 0 0 2 5 28 Dominant Large Moderate Small None True

Strong

Weak 0 3 0

No 1 0 Strong Weak No True

0 0 0 0 0 Dominant Large 0 0 0 0 0 0 0 1 0

Small 0 0 0 0 Moderate

None 0 0 0 0 2 Dominant Large Moderate Small None True

None 169 59 77

21 23 6 1 Minor Dist. **Merging** Predicted22 8 73 4 Major Dist. Merger 107 7 11 334 None Minor Dist. Major Dist. Merger True

Boxy 0 0 0

None 0 56 8 Predicted **Edge On Bulge** 5 10 Rounded Boxy None Rounded True

Round 269 0

251 112 Predicted In Between **How Rounded** Cigar 0 117 870 Round In Between Cigar True

_All Galaxies_ **Figure D2.**

None 0 0 0

0 0 0 0 Minor Dist. 0 0 2 0 Major Dist. Merger 0 0 0 34 None Minor Dist. Major Dist. Merger True

Boxy 0 0 0

None 0 23 0

0 0 Rounded Boxy None Rounded True

Round 6 0

4 4 In Between

Cigar 0 1 467 Round In Between Cigar True

_High Volunteer Confidence_

MNRAS,1–18(2023)

Continuing Fig.D1above.

──────── [TRUNCATED] ────────
Showing 29,962 chars (head) + 9,900 chars (tail) of 94,143 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-b37eb6800f.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-b37eb6800f.md" offset=707 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────