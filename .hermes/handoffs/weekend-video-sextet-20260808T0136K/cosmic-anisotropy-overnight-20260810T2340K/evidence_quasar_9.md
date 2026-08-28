URL: https://arxiv.org/html/2311.14938v2

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2311.14938v2 \[astro-ph.CO\] 15 Aug 2024

# The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis

Report issue for preceding element

Vasudev Mittal,1,2∗
Oliver T. Oayda,2∗
and Geraint F. Lewis2

∗Joint first author

1Department of Physical Sciences, IISER Mohali, Knowledge City, Sector 81, SAS Nagar, Manauli PO 140306, Punjab, India

2Sydney Institute for Astronomy, School of Physics A28, The University of Sydney, NSW 2006, Australia

E-mail: vasudeviiser@gmail.comE-mail: ooay3125@uni.sydney.edu.au

Report issue for preceding element

(Accepted 2023 November 24. Received 2023 November 15; in original form 2023 October 17)

###### Abstract

Report issue for preceding element

We present a Bayesian analysis of the Quaia sample of 1.3 million quasars as a test of the cosmological principle.
This principle postulates that the universe is homogeneous and isotropic on sufficiently large scales, forming the basis of prevailing cosmological models.
However, recent analyses of quasar samples have found a matter dipole inconsistent with the inferred kinematic dipole of the Cosmic Microwave Background (CMB), representing a tension with the expectations of the cosmological principle.
Here, we explore various hypotheses for the distribution of quasars in Quaia, finding that the sample is influenced by selection effects with significant contamination near the galactic plane.
After excising these regions, we find significant evidence that the Quaia quasar dipole is consistent with the CMB dipole, both in terms of the expected amplitude and direction.
This result is in conflict with recent analyses, lending support to the cosmological principle and the interpretation that the observed dipole is due to our local departure from the Hubble flow.

Report issue for preceding element

###### keywords:

Report issue for preceding element
quasars: general – cosmology: observations – cosmology: theory – large-scale structure of Universe

††pubyear: 2023††pagerange: The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis– [A](https://arxiv.org/html/2311.14938v2#A1 "Appendix A Bayes Factors for Tested Hypotheses ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis")

## 1 Introduction

Report issue for preceding element

A critical assumption in the contemporary cosmological framework is that the universe is homogeneous and isotropic at the largest scales (Harrison, [2000](https://arxiv.org/html/2311.14938v2#bib.bib20 "")).
This is the cosmological principle, and it is for example taken as a starting point by the Friedmann-Lemaître-Robertson-Walker (FLRW) metric of spacetime and the Friedmann equations describing cosmic evolution.
Homogeneity and isotropy were initially raised to the level of an a priori principle by Milne ( [1935](https://arxiv.org/html/2311.14938v2#bib.bib29 "")) – but the question as to whether there is an a posteriori basis remains.
If such a basis cannot be found, then we must critically re-examine the support for prevailing cosmological models.

Report issue for preceding element

The cosmological principle tacitly assumes the existence of a set of fundamental observers which reside in the ‘cosmic rest frame’ where the universe is maximally isotropic.
This is supported by the fact that the ‘cosmic microwave background’ (CMB) is remarkably smooth with temperature anisotropies of order Δ⁢T/T≈10−5Δ𝑇𝑇superscript105\\Delta T/T\\approx 10^{-5}roman\_Δ italic\_T / italic\_T ≈ 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT.
However, imprinted on these underlying small-scale fluctuations is a dipole anisotropy of order Δ⁢T/T≈10−3Δ𝑇𝑇superscript103\\Delta T/T\\approx 10^{-3}roman\_Δ italic\_T / italic\_T ≈ 10 start\_POSTSUPERSCRIPT - 3 end\_POSTSUPERSCRIPT.
This is conventionally explained by the Earth’s peculiar motion through the universe with a speed of 369.82±0.11⁢km⁢s−1plus-or-minus369.820.11kmsuperscripts1369.82\\pm 0.11\\,\\text{km}\\,\\text{s}^{-1}369.82 ± 0.11 km s start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT towards (l,b)=(264⁢.∘⁢021,48⁢.∘⁢253)𝑙𝑏264superscript.02148superscript.253(l,b)=(264\\hbox to0.0pt{.\\hss}^{\\circ}021,48\\hbox to0.0pt{.\\hss}^{\\circ}253)( italic\_l , italic\_b ) = ( 264 . start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT 021 , 48 . start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT 253 ) in galactic coordinates (Planck Collaboration et al., [2020](https://arxiv.org/html/2311.14938v2#bib.bib32 "")), which we denote as 𝐯CMBsubscript𝐯CMB\\mathbf{v}\_{\\text{CMB}}bold\_v start\_POSTSUBSCRIPT CMB end\_POSTSUBSCRIPT for future reference.
If this explanation (the kinematic interpretation of the CMB) is correct, then other cosmological probes using all-sky surveys should show a similar anisotropy.
Critically, distributions of matter at sufficiently large distances – namely where local clustering effects are negligible – should exhibit a dipole anisotropy, which we call the ‘cosmic dipole’ or the ‘matter dipole’.
If the cosmological principle is an accurate description of the universe, then the peculiar velocity inferred from this dipole should correspond with 𝐯CMBsubscript𝐯CMB\\mathbf{v}\_{\\text{CMB}}bold\_v start\_POSTSUBSCRIPT CMB end\_POSTSUBSCRIPT.

Report issue for preceding element

This matter anisotropy is observed, but there is no clear consensus on whether it is consistent with the cosmological principle or not.
However, the general trend is that the matter dipole studies – specifically with radio galaxies and quasars – find a dipole that aligns with the CMB dipole in direction, but is larger in magnitude (Peebles, [2022](https://arxiv.org/html/2311.14938v2#bib.bib31 ""); Kumar Aluri et al., [2023](https://arxiv.org/html/2311.14938v2#bib.bib26 "")).
This ‘dipole anisotropy problem’ thus represents an outstanding problem amongst cosmological probes.
Insofar that a consensus on this issue has not been reached, independent studies of matter dipoles with new catalogues of sources are key in further understanding the nature of this anomaly; for example, does it represents a shortcoming of our scientific understanding or an as of yet unresolved systematic issue?

Report issue for preceding element

With this in mind, in this work we present an analysis of the recently-released Quaia quasar catalogue (Storey-Fisher et al., [2023](https://arxiv.org/html/2311.14938v2#bib.bib46 "")).
At the highest magnitude limit, this catalogue contains 1 295 50212955021\\,295\\,5021 295 502 sources.
We examine the anisotropy in angular distribution of these quasars over the sky, applying a Bayesian framework to compare the inferred dipole to that of the CMB.
The structure of this paper is as follows.
In Section [2](https://arxiv.org/html/2311.14938v2#S2 "2 Background: Number count dipole ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis"), we present the background theory and an overview of the instant state of the literature, including current observations of the cosmic dipole and an assessment of their consistency with the cosmological principle.
The data under consideration in this study – the Quaia quasar catalogue – is presented in Section [3](https://arxiv.org/html/2311.14938v2#S3 "3 Quaia catalogue ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis"), and our approach to analysing the sample is examined in Section [4](https://arxiv.org/html/2311.14938v2#S4 "4 Approach ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis").
The results are presented in Section [5](https://arxiv.org/html/2311.14938v2#S5 "5 Results ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis").
We discuss our results and present our conclusions in Section [6](https://arxiv.org/html/2311.14938v2#S6 "6 Discussion & Conclusions ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis").

Report issue for preceding element

## 2 Background: Number count dipole

Report issue for preceding element

The cosmological principle’s key assumption of homogeneity and isotropy can, and has been, tested.
One critical family of tests involves probing the distribution of matter in the Earth’s frame of reference; these are the ‘matter dipole’ studies.
If we assume the principle to be an accurate description of the universe, then the CMB’s temperature dipole is interpreted to arise solely from the Earth’s peculiar motion.
Moreover, the dipole-removed frame is the frame of ‘cosmic rest’ where the universe is perceived as maximally isotropic and homogeneous.
Insofar that the Earth’s peculiar velocity imprints a Doppler shift on observed sources like radio galaxies, we should be able to recover the magnitude and direction of this motion from the dipole in matter distributions over the sky.
Framed in this way, measuring the consistency between the CMB-inferred and matter-inferred velocities is the linchpin of the matter dipole studies.

Report issue for preceding element

To see this, consider an observer moving with velocity v≪cmuch-less-than𝑣𝑐v\\ll citalic\_v ≪ italic\_c with respect to distant sources which are isotropic and homogeneous in their own rest frame.
As suggested in Ellis & Baldwin ( [1984](https://arxiv.org/html/2311.14938v2#bib.bib13 "")), if within the observer’s passband the sources have a spectral energy distribution with a power law dependence on frequency described by S∝ν−αproportional-to𝑆superscript𝜈𝛼S\\propto\\nu^{-\\alpha}italic\_S ∝ italic\_ν start\_POSTSUPERSCRIPT - italic\_α end\_POSTSUPERSCRIPT, and the apparent flux density has a cumulative power law distribution N(>S)∝S−xproportional-toannotated𝑁absent𝑆superscript𝑆𝑥N(>S)\\propto S^{-x}italic\_N ( > italic\_S ) ∝ italic\_S start\_POSTSUPERSCRIPT - italic\_x end\_POSTSUPERSCRIPT, then Doppler boosting and relativistic aberration will induce a dipole anisotropy in the distribution of sources in the observer’s frame.
The isotropic frame of reference will be boosted by an amplitude

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒟=\[2+x⁢(1+α)\]⁢vc.𝒟delimited-\[\]2𝑥1𝛼𝑣𝑐{\\bf\\mathcal{D}}=\[2+x(1+\\alpha)\]\\frac{v}{c}.caligraphic\_D = \[ 2 + italic\_x ( 1 + italic\_α ) \] divide start\_ARG italic\_v end\_ARG start\_ARG italic\_c end\_ARG . |  | (1) |

This is the famous ‘kinematic dipole’, and Ellis & Baldwin ( [1984](https://arxiv.org/html/2311.14938v2#bib.bib13 "")) made the rough estimate that a minimum of O⁢(105)𝑂superscript105O(10^{5})italic\_O ( 10 start\_POSTSUPERSCRIPT 5 end\_POSTSUPERSCRIPT ) sources would be needed to discern this dipole.
The implicit assumption here is that the observer should survey the sky until a flux density above which there is no directional bias in the completeness of the survey.
Additionally, x𝑥xitalic\_x and α𝛼\\alphaitalic\_α are assumed to not be redshift-dependent, although there has been some suggestion that this simplification should be revisited (see e.g. Dalang & Bonvin, [2022](https://arxiv.org/html/2311.14938v2#bib.bib10 "")).
Further, local inhomogeneities introduce a clustering dipole, so for a genuine measurement of the cosmic dipole a significant fraction of the sources need to be at high redshifts (z≈1𝑧1z\\approx 1italic\_z ≈ 1; Tiwari & Nusser, [2016](https://arxiv.org/html/2311.14938v2#bib.bib48 "")).
From equation ( [1](https://arxiv.org/html/2311.14938v2#S2.E1 "In 2 Background: Number count dipole ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis")), the net dipole anisotropy for a patch of sky in the direction 𝐧^^𝐧\\bf\\hat{n}over^ start\_ARG bold\_n end\_ARG will be

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | Δ⁢NN=𝐃⋅𝐧^=\[2+x⁢(1+α)\]⁢𝐯c⋅𝐧^.Δ𝑁𝑁⋅𝐃^𝐧⋅delimited-\[\]2𝑥1𝛼𝐯𝑐^𝐧\\frac{\\Delta N}{N}={\\bf D}\\cdot{\\bf\\hat{n}}=\[2+x(1+\\alpha)\]\\frac{\\bf v}{c}%<br>\\cdot{\\bf\\hat{n}}.divide start\_ARG roman\_Δ italic\_N end\_ARG start\_ARG italic\_N end\_ARG = bold\_D ⋅ over^ start\_ARG bold\_n end\_ARG = \[ 2 + italic\_x ( 1 + italic\_α ) \] divide start\_ARG bold\_v end\_ARG start\_ARG italic\_c end\_ARG ⋅ over^ start\_ARG bold\_n end\_ARG . |  | (2) |

Various all-sky surveys of radio sources have been used to trace out this dipole over the sky, and thus probe the cosmological principle.
We note that Kumar Aluri et al. ( [2023](https://arxiv.org/html/2311.14938v2#bib.bib26 "")) deals with the genealogy of these tests in greater detail, but none the less we recount some of the salient results here.

Report issue for preceding element

Blake & Wall ( [2002](https://arxiv.org/html/2311.14938v2#bib.bib5 "")) initially found support for a kinematic dipole aligned with the CMB and possessing the expected amplitude.
However, the immediate state of the literature is equivocal as to whether or not the matter dipole is consistent with the CMB dipole.
Many studies (see e.g. Singal, [2011](https://arxiv.org/html/2311.14938v2#bib.bib37 ""); Colin et al., [2017](https://arxiv.org/html/2311.14938v2#bib.bib7 ""); Bengaly et al., [2018](https://arxiv.org/html/2311.14938v2#bib.bib4 ""); Singal, [2019](https://arxiv.org/html/2311.14938v2#bib.bib38 ""); Siewert et al., [2021](https://arxiv.org/html/2311.14938v2#bib.bib36 ""); Singal, [2023](https://arxiv.org/html/2311.14938v2#bib.bib41 ""); Wagenveld et al., [2023](https://arxiv.org/html/2311.14938v2#bib.bib50 "")) have reported dipole amplitudes that are in excess of the CMB expectation, while the inferred dipole directions generally align with the CMB dipole (although notably Darling ( [2022](https://arxiv.org/html/2311.14938v2#bib.bib12 "")) and Cheng et al. ( [2023](https://arxiv.org/html/2311.14938v2#bib.bib6 "")) find consistency with the CMB dipole for their chosen radio catalogues).
We point out that in the foregoing works and amongst others, authors discussed the appropriate choice of dipole estimator at length, including whether or not certain estimators incur a bias that must be accounted for.
To our knowledge, tests instead formulated in the language of Bayesian statistics have been used less extensively, which we discuss below.

Report issue for preceding element

Turning away from the radio galaxy studies, Secrest et al. ( [2021](https://arxiv.org/html/2311.14938v2#bib.bib34 "")) showcased that the Ellis & Baldwin ( [1984](https://arxiv.org/html/2311.14938v2#bib.bib13 "")) method can be used to study the matter dipole in quasar samples.
This study, taken together with the joint radio galaxy and quasar analysis in Secrest et al. ( [2022](https://arxiv.org/html/2311.14938v2#bib.bib35 "")), is perhaps one of the more significant challenges to the cosmological principle.
Therein, the authors studied the dipole in the distribution of quasars from CatWISE2020 (Marocco et al., [2021](https://arxiv.org/html/2311.14938v2#bib.bib28 "")) using a least squares estimator, finding that the amplitude was at least twice as large as expected (at a 4.9σ𝜎\\sigmaitalic\_σ level of statistical significance).
A similar conclusion with the same sample was reached in Kothari et al. ( [2022](https://arxiv.org/html/2311.14938v2#bib.bib25 "")).
Separately, Singal ( [2021](https://arxiv.org/html/2311.14938v2#bib.bib39 "")) used a sample of 0.28 million quasars and also found a dipole magnitude in excess of the CMB expectation, although the sample size there was about 5 times smaller than that of Secrest et al. ( [2021](https://arxiv.org/html/2311.14938v2#bib.bib34 "")).

Report issue for preceding element

As we touched on earlier, these analyses used frequentist statistics, and the results are sensitive to the estimator chosen.
However, a Bayesian analysis of CatWISE2020 was performed by Dam et al. ( [2023](https://arxiv.org/html/2311.14938v2#bib.bib11 "")), in which Secrest et al. ( [2021](https://arxiv.org/html/2311.14938v2#bib.bib34 ""))’s result of an anomalously large dipole was confirmed at a statistical significance of 5.7⁢σ5.7𝜎5.7\\sigma5.7 italic\_σ.
Taken together, these results lend evidence to the proposition that the quasar dipole is in tension with the kinematic dipole inferred from the CMB.

Report issue for preceding element

On the basis of the foregoing, the literature interrogating the matter dipole is by no means unanimous.
That being said, these works do not represent an exhaustive survey of what is possible; a suite of other probes have been formulated, many of which are accounted for in Kumar Aluri et al. ( [2023](https://arxiv.org/html/2311.14938v2#bib.bib26 "")).
Some of these include tests with Type Ia SNe (see e.g. Horstmann et al., [2022](https://arxiv.org/html/2311.14938v2#bib.bib21 ""); Singal, [2022](https://arxiv.org/html/2311.14938v2#bib.bib40 ""); Sorrenti et al., [2022](https://arxiv.org/html/2311.14938v2#bib.bib44 "")), analyses of bulk flows (see e.g. Watkins et al., [2023](https://arxiv.org/html/2311.14938v2#bib.bib51 "")) and direct probes of the FLRW metric with tests of spatial curvature (see e.g. Zhou & Li, [2020](https://arxiv.org/html/2311.14938v2#bib.bib54 "")).
Recently, Oayda & Lewis ( [2023](https://arxiv.org/html/2311.14938v2#bib.bib30 "")) proposed a novel test involving a dipole in time dilation, as sources with intrinsic time-scales are time dilated along the direction of the Earth’s motion.

Report issue for preceding element

Returning to quasars, if there is an outstanding tension between the dipole inferred from quasars and that expected from the CMB, then closer scrutiny is warranted.
Since the cosmological principle is a foundational assumption in the prevailing cosmological paradigm (Harrison, [2000](https://arxiv.org/html/2311.14938v2#bib.bib20 "")), a challenge to it cannot be easily overlooked.
In this work, we present another analysis of the dipole in quasar distributions.
We tested the recently-released Quaia catalogue (Storey-Fisher et al., [2023](https://arxiv.org/html/2311.14938v2#bib.bib46 "")), employing Bayesian inference to understand which model is best supported by the sample and whether the inferred dipole is consistent with that of the CMB.

Report issue for preceding element

## 3 Quaia catalogue

Report issue for preceding element

The Quaia catalogue (Storey-Fisher et al., [2023](https://arxiv.org/html/2311.14938v2#bib.bib46 "")) is principally taken from quasars observed by the Gaia satellite (Gaia Collaboration et al., [2016](https://arxiv.org/html/2311.14938v2#bib.bib15 "")), which were released in Gaia DR3 (Gaia Collaboration et al., [2023a](https://arxiv.org/html/2311.14938v2#bib.bib16 ""), [b](https://arxiv.org/html/2311.14938v2#bib.bib17 "")).
The full sample of DR3 quasar candidates totals to 6 649 16266491626\\,649\\,1626 649 162 sources, which was the starting point for the authors.

Report issue for preceding element

In constructing their catalogue, they first imposed that all Gaia quasars have a measurement of photometric magnitude in the G𝐺Gitalic\_G, B⁢P𝐵𝑃BPitalic\_B italic\_P and R⁢P𝑅𝑃RPitalic\_R italic\_P bands.
Additionally, the authors cross-matched each of the quasar candidates with those from the Wide-field Infrared Survey Explorer(WISE; Wright et al., [2010](https://arxiv.org/html/2311.14938v2#bib.bib53 "")), using the unWISE reprocessing to also provide photometric information in the W⁢1𝑊1W1italic\_W 1 and W⁢2𝑊2W2italic\_W 2 infrared bands.
To decontaminate their sample, the authors imposed proper motion cuts, since quasars are anticipated to be sources well within the background, and a number of colour magnitude cuts.
They finally applied a G<20.5𝐺20.5G<20.5italic\_G < 20.5 magnitude cut, the result of which constitutes their primary catalogue: the ‘Quaia high’ catalogue.
Another cut of G<20.0𝐺20.0G<20.0italic\_G < 20.0 created the ‘Quaia low’ catalogue, since the authors noted that deeper magnitudes sacrificed purity and measurement precision.

Report issue for preceding element

One other issue is outstanding: selection effects.
To mitigate these, the authors created a selection function to account for how some sources are preferentially observed at different locations on the sky due to dust extinction, stellar density and the peculiarities of Gaia’s scanning pattern.
This information is encoded in four maps: a dust extinction map; a stellar distribution map; a separate Large Magellanic Cloud and Small Magellanic Cloud stellar map; and, a map encoding Gaia’s scanning law and source crowding.
This data is passed to a Gaussian process, producing a probability map: the selection function.
The selection function describes how likely it is for sources to be included in the final catalogue depending on where they are on the sky.
In other words, regions which are less dense on the basis of systematics like dust extinction will be associated with a lower probability, and regions which do not suffer from these effects have a probability closer to 1.

Report issue for preceding element

A visualisation of the raw Quaia low and Quaia high catalogues with number count densities can be seen in the top row of Fig. [1](https://arxiv.org/html/2311.14938v2#S3.F1 "Figure 1 ‣ 3 Quaia catalogue ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis").

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2311.14938v2/x1.png)

![Refer to caption](https://arxiv.org/html/2311.14938v2/x2.png)

![Refer to caption](https://arxiv.org/html/2311.14938v2/x3.png)

![Refer to caption](https://arxiv.org/html/2311.14938v2/x4.png)

![Refer to caption](https://arxiv.org/html/2311.14938v2/x5.png)

![Refer to caption](https://arxiv.org/html/2311.14938v2/x6.png)

Figure 1: Visualisation of the salient features of the two Quaia catalogues in galactic coordinates, with Quaia low in the left column and Quaia high in the right column. Top row: Raw catalogue prior to any additional masking or processing. Note that the catalogue already has an absence of sources near the galactic plane, shown in grey, primarily due to dust absorption. Middle row: The selection function provided for both the Quaia catalogues, with the colour scale indicating the probability of source detection associated with each pixel due to factors like dust extinction. Bottom row: Both catalogues have been smoothed via a sliding average over a 1 steradian scale after scaling according to the selection function. Deviations in source density along the galactic plane can be seen, with an over-density at the galactic centre and an under-density at mid galactic longitudes. The solid and dashed lines indicate the 40∘superscript4040^{\\circ}40 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT and 30∗superscript3030^{\*}30 start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT galactic plane masks respectively.Report issue for preceding element

These maps, as well as subsequent ones, are displayed in galactic coordinates.
We show the selection function provided by the Quaia authors for both catalogues in the middle row of Fig. [1](https://arxiv.org/html/2311.14938v2#S3.F1 "Figure 1 ‣ 3 Quaia catalogue ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis").
By visual inspection, dust extinction appears to dominate the map, which explains the dearth of sources near the galactic plane in the raw catalogue.
Finally, we show smoothed maps in the bottom row of Fig. [1](https://arxiv.org/html/2311.14938v2#S3.F1 "Figure 1 ‣ 3 Quaia catalogue ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis") for Quaia low and Quaia high.
To generate the smoothed map, we first scaled the catalogue according to the selection function such that the i𝑖iitalic\_i-th pixel with number of sources Nisubscript𝑁𝑖N\_{i}italic\_N start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT (see Section [4.1.1](https://arxiv.org/html/2311.14938v2#S4.SS1.SSS1 "4.1.1 Binning ‣ 4.1 Catalogue processing ‣ 4 Approach ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis") for information on how sources are binned) is scaled by 1/si1subscript𝑠𝑖1/s\_{i}1 / italic\_s start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT, where sisubscript𝑠𝑖s\_{i}italic\_s start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT is the value of the selection function at that pixel.
We then implemented a sliding average; for each pixel, we selected pixels within 1 steradian and computed the mean density.
These maps give a visual cue of a source over-density near the galactic centre, as well as under-densities near mid galactic longitudes along the galactic plane.
Superimposed on the maps are two masks we chose to use, which are explained in more detail in Section [4.1.2](https://arxiv.org/html/2311.14938v2#S4.SS1.SSS2 "4.1.2 Masking ‣ 4.1 Catalogue processing ‣ 4 Approach ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis").

Report issue for preceding element

## 4 Approach

Report issue for preceding element

### 4.1 Catalogue processing

Report issue for preceding element

#### 4.1.1 Binning

Report issue for preceding element

In order to prepare the catalogue for analysis, the sky was divided into equal-area pixels using the the pixelisation regime of HEALPix111 [https://healpix.sourceforge.io/](https://healpix.sourceforge.io/ "")(Górski et al., [2005](https://arxiv.org/html/2311.14938v2#bib.bib18 ""); Zonca et al., [2019](https://arxiv.org/html/2311.14938v2#bib.bib55 "")) as incorporated in the Python package healpy.
Nside=64subscript𝑁side64N\_{\\text{side}}=64italic\_N start\_POSTSUBSCRIPT side end\_POSTSUBSCRIPT = 64 – generating a total of 49 1524915249\\,15249 152 pixels – was chosen, since the selection maps created by the Quaia authors are given at this resolution.
The choice of Nsidesubscript𝑁sideN\_{\\text{side}}italic\_N start\_POSTSUBSCRIPT side end\_POSTSUBSCRIPT depends upon the fact that for number count analysis, the uncertainty in number counts for each pixel due to shot noise should not be greater than the mean number count for the catalogue.
We then summed the number of sources within each pixel using their recorded positions in right ascension and declination.
This gives a means by which changes in the source density can be discerned as a function of sky position.

Report issue for preceding element

#### 4.1.2 Masking

Report issue for preceding element

Storey-Fisher et al. ( [2023](https://arxiv.org/html/2311.14938v2#bib.bib46 "")) noted that the selection function is potentially poorly-modelled in the vicinity of the galactic plane.
In making this judgment, they computed the fractional residuals between a synthetic catalogue generated by randomly sampling over a sphere according to the selection function and the actual Quaia catalogue.
Around the edge of the plane, the random synthetic catalogue over-predicts the data; additionally, near the galactic centre, the random catalogue seems to under-predict the data.
We note that in the bottom row of Fig. [1](https://arxiv.org/html/2311.14938v2#S3.F1 "Figure 1 ‣ 3 Quaia catalogue ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis"), which shows our smoothed map of the Quaia low and Quaia high samples, there indeed appears to be an over-density near (l,b)≈(0∘,30∘)𝑙𝑏superscript0superscript30(l,b)\\approx(0^{\\circ},30^{\\circ})( italic\_l , italic\_b ) ≈ ( 0 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT , 30 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT ) as well as under-densities along the galactic plane from about l=120∘𝑙superscript120l=120^{\\circ}italic\_l = 120 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT to l=240∘𝑙superscript240l=240^{\\circ}italic\_l = 240 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT.
This is in line with the proposition made by the Quaia authors.
For example, if the galactic centre is under-predicted by the selection function, then si<s~isubscript𝑠𝑖subscript~𝑠𝑖s\_{i}<\\tilde{s}\_{i}italic\_s start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT < over~ start\_ARG italic\_s end\_ARG start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT where s~isubscript~𝑠𝑖\\tilde{s}\_{i}over~ start\_ARG italic\_s end\_ARG start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT is some true value of the selection function.
Thus, in our smoothed maps which originate from scaled number counts, the i𝑖iitalic\_i-th pixel has a number count Ni/si>Ni/s~isubscript𝑁𝑖subscript𝑠𝑖subscript𝑁𝑖subscript~𝑠𝑖N\_{i}/s\_{i}>N\_{i}/\\tilde{s}\_{i}italic\_N start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT / italic\_s start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT > italic\_N start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT / over~ start\_ARG italic\_s end\_ARG start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT, manifesting as an over-density.

Report issue for preceding element

In order to address this issue, we chose to mask the galactic plane with a series of increasingly conservative masks, as the Quaia authors suspected may be necessary at Section 4.5 in Storey-Fisher et al. ( [2023](https://arxiv.org/html/2311.14938v2#bib.bib46 "")).
To be explicit, we examined the effect of \|b\|<10∘𝑏superscript10\|b\|<10^{\\circ}\| italic\_b \| < 10 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT, 20∘superscript2020^{\\circ}20 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT, 30∘superscript3030^{\\circ}30 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT and 40∘superscript4040^{\\circ}40 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT galactic plane masks on the recovered signal in conjunction with an unmasked catalogue.
The 30∘superscript3030^{\\circ}30 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT mask curtains much of the problematic regions, but it is still possible that at the edge of the mask the issues at the galactic plane seep into the masked sample.
Accordingly, in addition to testing with a 40∘superscript4040^{\\circ}40 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT mask, we implemented a circular mask centred on (l∘,b∘)=(0,0)superscript𝑙superscript𝑏00(l^{\\circ},b^{\\circ})=(0,0)( italic\_l start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT , italic\_b start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT ) = ( 0 , 0 ) and subtending a solid angle of 4⁢sr4sr4\\,\\text{sr}4 sr in concert with the 30∘superscript3030^{\\circ}30 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT galactic plane mask.
We denote this as a 30∗superscript3030^{\*}30 start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT mask for future reference.
The 40∘superscript4040^{\\circ}40 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT mask is represented by the solid black line overlaid on the bottom row of Fig. [1](https://arxiv.org/html/2311.14938v2#S3.F1 "Figure 1 ‣ 3 Quaia catalogue ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis"), and the 30∗superscript3030^{\*}30 start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT mask is represented by the dashed black line.

Report issue for preceding element

### 4.2 Dipole amplitude expectation

Report issue for preceding element

Since we are ultimately testing the kinematic interpretation of the CMB, we will need to compare the expected dipole amplitude given CMB-inferred motion and the actual recovered dipole from the Quaia sample.
Conventionally, this amounts to using equation ( [1](https://arxiv.org/html/2311.14938v2#S2.E1 "In 2 Background: Number count dipole ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis")) with v=vCMB≈369⁢km s−1𝑣subscript𝑣CMB369superscriptkm s1v=v\_{\\text{CMB}}\\approx 369\\,\\text{km\\,s}^{-1}italic\_v = italic\_v start\_POSTSUBSCRIPT CMB end\_POSTSUBSCRIPT ≈ 369 km s start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT.
This also means that x𝑥xitalic\_x and α𝛼\\alphaitalic\_α must be ascertained from the sample of galactic sources.
Here, we instead use the actual source counts themselves – rather than their proxy x𝑥xitalic\_x – and take the distribution of α𝛼\\alphaitalic\_α to find a distribution of dipole amplitudes 𝒟𝒟\\mathcal{D}caligraphic\_D given v𝑣vitalic\_v.
This approach is detailed below.

Report issue for preceding element

#### 4.2.1 Spectral index

Report issue for preceding element

As mentioned earlier, we assume that the i𝑖iitalic\_i-th Quaia source follows a flux power law such that Sν∝ν−αiproportional-tosubscript𝑆𝜈superscript𝜈subscript𝛼𝑖S\_{\\nu}\\propto\\nu^{-\\alpha\_{i}}italic\_S start\_POSTSUBSCRIPT italic\_ν end\_POSTSUBSCRIPT ∝ italic\_ν start\_POSTSUPERSCRIPT - italic\_α start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT.
To find the spectral index αisubscript𝛼𝑖\\alpha\_{i}italic\_α start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT, we compute the colour magnitude mG−B⁢Psubscript𝑚𝐺𝐵𝑃m\_{G-BP}italic\_m start\_POSTSUBSCRIPT italic\_G - italic\_B italic\_P end\_POSTSUBSCRIPT.
Since Gaia magnitudes are measured in the Vega system, we use the zero points (ZP) and mean wavelengths of the G𝐺Gitalic\_G and B⁢P𝐵𝑃BPitalic\_B italic\_P bands, as provided in (Riello et al., [2021](https://arxiv.org/html/2311.14938v2#bib.bib33 "")), to determine αisubscript𝛼𝑖\\alpha\_{i}italic\_α start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT.
Namely,

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | mν=−2.5⁢log10⁡Sν+ZPsubscript𝑚𝜈2.5subscript10subscript𝑆𝜈ZPm\_{\\nu}=-2.5\\log\_{10}S\_{\\nu}+\\text{ZP}italic\_m start\_POSTSUBSCRIPT italic\_ν end\_POSTSUBSCRIPT = - 2.5 roman\_log start\_POSTSUBSCRIPT 10 end\_POSTSUBSCRIPT italic\_S start\_POSTSUBSCRIPT italic\_ν end\_POSTSUBSCRIPT + ZP |  | (3) |

such that

Report issue for preceding element

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  | mG−B⁢Psubscript𝑚𝐺𝐵𝑃\\displaystyle m\_{G-BP}italic\_m start\_POSTSUBSCRIPT italic\_G - italic\_B italic\_P end\_POSTSUBSCRIPT | =2.5⁢(log10⁡SB⁢P−log10⁡SG)+ZPG−ZPB⁢Pabsent2.5subscript10subscript𝑆𝐵𝑃subscript10subscript𝑆𝐺subscriptZP𝐺subscriptZP𝐵𝑃\\displaystyle=2.5(\\log\_{10}S\_{BP}-\\log\_{10}S\_{G})+\\text{ZP}\_{G}-\\text{ZP}\_{BP}= 2.5 ( roman\_log start\_POSTSUBSCRIPT 10 end\_POSTSUBSCRIPT italic\_S start\_POSTSUBSCRIPT italic\_B italic\_P end\_POSTSUBSCRIPT - roman\_log start\_POSTSUBSCRIPT 10 end\_POSTSUBSCRIPT italic\_S start\_POSTSUBSCRIPT italic\_G end\_POSTSUBSCRIPT ) + ZP start\_POSTSUBSCRIPT italic\_G end\_POSTSUBSCRIPT - ZP start\_POSTSUBSCRIPT italic\_B italic\_P end\_POSTSUBSCRIPT |  | (4) |
|  | ⟹αiabsentsubscript𝛼𝑖\\displaystyle\\implies\\alpha\_{i}⟹ italic\_α start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT | =k−mG−B⁢P2.5⁢log10⁡(νB⁢P/νG)absent𝑘subscript𝑚𝐺𝐵𝑃2.5subscript10subscript𝜈𝐵𝑃subscript𝜈𝐺\\displaystyle=\\frac{k-m\_{G-BP}}{2.5\\log\_{10}(\\nu\_{BP}/\\nu\_{G})}= divide start\_ARG italic\_k - italic\_m start\_POSTSUBSCRIPT italic\_G - italic\_B italic\_P end\_POSTSUBSCRIPT end\_ARG start\_ARG 2.5 roman\_log start\_POSTSUBSCRIPT 10 end\_POSTSUBSCRIPT ( italic\_ν start\_POSTSUBSCRIPT italic\_B italic\_P end\_POSTSUBSCRIPT / italic\_ν start\_POSTSUBSCRIPT italic\_G end\_POSTSUBSCRIPT ) end\_ARG |  | (5) |

where k𝑘kitalic\_k is ZPG−ZPB⁢PsubscriptZP𝐺subscriptZP𝐵𝑃\\text{ZP}\_{G}-\\text{ZP}\_{BP}ZP start\_POSTSUBSCRIPT italic\_G end\_POSTSUBSCRIPT - ZP start\_POSTSUBSCRIPT italic\_B italic\_P end\_POSTSUBSCRIPT and in the last line we used the assumption that Sν∝ν−αiproportional-tosubscript𝑆𝜈superscript𝜈subscript𝛼𝑖S\_{\\nu}\\propto\\nu^{-\\alpha\_{i}}italic\_S start\_POSTSUBSCRIPT italic\_ν end\_POSTSUBSCRIPT ∝ italic\_ν start\_POSTSUPERSCRIPT - italic\_α start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT.
Equation ( [5](https://arxiv.org/html/2311.14938v2#S4.E5 "In 4.2.1 Spectral index ‣ 4.2 Dipole amplitude expectation ‣ 4 Approach ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis")) yields a distribution of spectral indices for Quaia low and Quaia high, which we show in Fig. [2](https://arxiv.org/html/2311.14938v2#S4.F2 "Figure 2 ‣ 4.2.1 Spectral index ‣ 4.2 Dipole amplitude expectation ‣ 4 Approach ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis").

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2311.14938v2/x7.png)Figure 2: Distribution of spectral indices α𝛼\\alphaitalic\_α in the Quaia low and Quaia high samples computed from mG−B⁢Psubscript𝑚𝐺𝐵𝑃m\_{G-BP}italic\_m start\_POSTSUBSCRIPT italic\_G - italic\_B italic\_P end\_POSTSUBSCRIPT. Blue and orange are used to denote Quaia low and Quaia high respectively. The mean spectral indices α¯¯𝛼\\bar{\\alpha}over¯ start\_ARG italic\_α end\_ARG for each catalogue are indicated by the vertical lines.Report issue for preceding element

The mean value of α𝛼\\alphaitalic\_α is labelled there only for illustrative purposes; what is important, in our analysis, is the distribution itself.

Report issue for preceding element

#### 4.2.2 Source number counts

Report issue for preceding element

To find the distribution of fluxes in the Quaia sample, we first convert the G𝐺Gitalic\_G magnitude into a Gaia flux using the zero points mentioned above.
This yields Gaia fluxes in units of photoelectronss−1superscripts1\\,\\text{s}^{-1}s start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT, though we note that these fluxes can also be found by matching each Quaia source with its entry in DR3 by using each entry’s Gaia DR3 source identifier.

[... middle omitted — see footer ...]

| M4subscript𝑀4M\_{4}italic\_M start\_POSTSUBSCRIPT 4 end\_POSTSUBSCRIPT (Kinematic Direction) | 32.519 14732.51914732.519\\,14732.519 147 | 43.213 93343.21393343.213\\,93343.213 933 | 43.596 22943.59622943.596\\,22943.596 229 | 29.243 38429.24338429.243\\,38429.243 384 | 21.417 60221.41760221.417\\,60221.417 602\\cellcolorblack!10 | 16.346 72316.34672316.346\\,72316.346 723 |
| M5subscript𝑀5M\_{5}italic\_M start\_POSTSUBSCRIPT 5 end\_POSTSUBSCRIPT (Kinematic Velocity) | 98.306 56098.30656098.306\\,56098.306 560 | 88.593 32988.59332988.593\\,32988.593 329 | 57.663 70957.66370957.663\\,70957.663 709 | 31.606 55231.60655231.606\\,55231.606 552 | 21.013 92121.01392121.013\\,92121.013 921 | 16.615 12816.61512816.615\\,12816.615 128 |
| M6subscript𝑀6M\_{6}italic\_M start\_POSTSUBSCRIPT 6 end\_POSTSUBSCRIPT (Kinematic Dipole) | 30.195 95330.19595330.195\\,95330.195 953 | 35.724 36835.72436835.724\\,36835.724 368 | 34.653 69234.65369234.653\\,69234.653 692 | 26.172 29226.17229226.172\\,29226.172 292 | 20.359 35720.35935720.359\\,35720.359 357 | 17.371 70917.37170917.371\\,70917.371 709 |
| 175.003 049175.003049175.003\\,049175.003 049\\cellcolorblack!10 |  |  |  |  |  |  |
| 130.598289\\cellcolorblack!10 | 57.706 86057.70686057.706\\,86057.706 860\\cellcolorblack!10 | 18.877 40018.87740018.877\\,40018.877 400\\cellcolorblack!10 | 0.229 1650.2291650.229\\,1650.229 165 | 14.474 10214.47410214.474\\,10214.474 102 |  |  |
| M3subscript𝑀3M\_{3}italic\_M start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT (Quadrupole) | 44.300 00044.30000044.300\\,00044.300 000 | 21.100 00021.10000021.100\\,00021.100 000 | 10.200 00010.20000010.200\\,00010.200 000 | 6.200 0006.2000006.200\\,0006.200 000 | 0.500 0000.5000000.500\\,0000.500 000 | 11.974 10211.97410211.974\\,10211.974 102 |
| M4subscript𝑀4M\_{4}italic\_M start\_POSTSUBSCRIPT 4 end\_POSTSUBSCRIPT (Kinematic Direction) | 23.418 57223.41857223.418\\,57223.418 572 | 30.460 79430.46079430.460\\,79430.460 794 | 24.045 10724.04510724.045\\,10724.045 107 | 12.776 03012.77603012.776\\,03012.776 030 | 5.750 9785.7509785.750\\,9785.750 978 | 13.213 19913.21319913.213\\,19913.213 199 |
| M5subscript𝑀5M\_{5}italic\_M start\_POSTSUBSCRIPT 5 end\_POSTSUBSCRIPT (Kinematic Velocity) | 50.369 72350.36972350.369\\,72350.369 723 | 45.749 31345.74931345.749\\,31345.749 313 | 28.687 37228.68737228.687\\,37228.687 372 | 13.996 62513.99662513.996\\,62513.996 625 | 7.429 8027.4298027.429\\,8027.429 802 | 11.769 30011.76930011.769\\,30011.769 300 |
| M6subscript𝑀6M\_{6}italic\_M start\_POSTSUBSCRIPT 6 end\_POSTSUBSCRIPT (Kinematic Dipole) | 23.352 70923.35270923.352\\,70923.352 709 | 26.983 82226.98382226.983\\,82226.983 822 | 22.901 71222.90171222.901\\,71222.901 712 | 15.494 46815.49446815.494\\,46815.494 468 | 10.001 54410.00154410.001\\,54410.001 544\\cellcolorblack!10 | 14.638 96814.63896814.638\\,96814.638 968\\cellcolorblack!10 |

Table 3: Table of Bayes Factors for different hypotheses and galactic masks using the Quaia low catalogue with the point-by-point analysis. Here, 30∗ represents the combination of a 30∘superscript3030^{\\circ}30 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT mask and a 4⁢sr4sr4\\,\\text{sr}4 sr circular mask centered at the (l∘,b∘)=(0,0)superscript𝑙superscript𝑏00(l^{\\circ},b^{\\circ})=(0,0)( italic\_l start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT , italic\_b start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT ) = ( 0 , 0 ). The highlighted cell represents the model with the highest Bayes factor, indicating it has the strongest level of support.
Report issue for preceding element

Hypothesis   Galactic mask angle b∘superscript𝑏b^{\\circ}italic\_b start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT001010101020202020303030304040404030303030\*

M0subscript𝑀0M\_{0}italic\_M start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT (Null)0.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 000M1subscript𝑀1M\_{1}italic\_M start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT (Dipole)131.400 000131.400000131.400\\,000131.400 000109.900 000109.900000109.900\\,000109.900 00049.900 00049.90000049.900\\,00049.900 00014.500 00014.50000014.500\\,00014.500 0003.500 0003.5000003.500\\,0003.500 00011.700 00011.70000011.700\\,00011.700 000M2subscript𝑀2M\_{2}italic\_M start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT (Double Dipole)175.613 985175.613985175.613\\,985175.613 985\\cellcolorblack!10132.002 973132.002973132.002\\,973132.002 973\\cellcolorblack!1058.892 64458.89264458.892\\,64458.892 644\\cellcolorblack!1019.991 74819.99174819.991\\,74819.991 748\\cellcolorblack!101.447 5811.4475811.447\\,5811.447 58115.200 00015.20000015.200\\,00015.200 000\\cellcolorblack!10
M3subscript𝑀3M\_{3}italic\_M start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT (Quadrupole)45.500 00045.50000045.500\\,00045.500 00022.100 00022.10000022.100\\,00022.100 00011.200 00011.20000011.200\\,00011.200 0007.400 0007.4000007.400\\,0007.400 0001.600 0001.6000001.600\\,0001.600 00013.100 00013.10000013.100\\,00013.100 000M4subscript𝑀4M\_{4}italic\_M start\_POSTSUBSCRIPT 4 end\_POSTSUBSCRIPT (Kinematic Direction)23.783 90923.78390923.783\\,90923.783 90930.697 84430.69784430.697\\,84430.697 84424.453 27524.45327524.453\\,27524.453 27512.941 54612.94154612.941\\,54612.941 5466.114 1796.1141796.114\\,1796.114 17913.426 08313.42608313.426\\,08313.426 083M5subscript𝑀5M\_{5}italic\_M start\_POSTSUBSCRIPT 5 end\_POSTSUBSCRIPT (Kinematic Velocity)50.924 24350.92424350.924\\,24350.924 24346.379 54446.37954446.379\\,54446.379 54429.469 39429.46939429.469\\,39429.469 39414.076 14714.07614714.076\\,14714.076 1477.909 0937.9090937.909\\,0937.909 09312.071 23312.07123312.071\\,23312.071 233M6subscript𝑀6M\_{6}italic\_M start\_POSTSUBSCRIPT 6 end\_POSTSUBSCRIPT (Kinematic Dipole)23.725 72723.72572723.725\\,72723.725 72727.498 68227.49868227.498\\,68227.498 68223.584 60723.58460723.584\\,60723.584 60715.966 43415.96643415.966\\,43415.966 43410.524 38210.52438210.524\\,38210.524 382\\cellcolorblack!1015.197 63815.19763815.197\\,63815.197 638\\cellcolorblack!10

Report issue for preceding element

Table 4: As for Table [3](https://arxiv.org/html/2311.14938v2#A1.T3 "Table 3 ‣ Appendix A Bayes Factors for Tested Hypotheses ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis") but with the Poisson statistics.

Table 5: As for Table [3](https://arxiv.org/html/2311.14938v2#A1.T3 "Table 3 ‣ Appendix A Bayes Factors for Tested Hypotheses ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis") but with Quaia high.Report issue for preceding element

Hypothesis   Galactic mask angle b∘superscript𝑏b^{\\circ}italic\_b start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT001010101020202020303030304040404030303030\*

M0subscript𝑀0M\_{0}italic\_M start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT (Null)0.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 000M1subscript𝑀1M\_{1}italic\_M start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT (Dipole)375.900 000375.900000375.900\\,000375.900 000308.500 000308.500000308.500\\,000308.500 000146.400 000146.400000146.400\\,000146.400 00049.600 00049.60000049.600\\,00049.600 000\\cellcolorblack!1021.000 00021.00000021.000\\,00021.000 00018.618 20118.61820118.618\\,20118.618 201\\cellcolorblack!10
M2subscript𝑀2M\_{2}italic\_M start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT (Double Dipole)426.827 565426.827565426.827\\,565426.827 565\\cellcolorblack!10329.175 231329.175231329.175\\,231329.175 231\\cellcolorblack!10156.449 248156.449248156.449\\,248156.449 248\\cellcolorblack!1049.618 61549.61861549.618\\,61549.618 615\\cellcolorblack!1020.283 19820.28319820.283\\,19820.283 19816.323 11016.32311016.323\\,11016.323 110M3subscript𝑀3M\_{3}italic\_M start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT (Quadrupole)64.400 00064.40000064.400\\,00064.400 00027.500 00027.50000027.500\\,00027.500 00010.200 00010.20000010.200\\,00010.200 0001.600 0001.6000001.600\\,0001.600 0000.000 0000.0000000.000\\,0000.000 0006.818 2016.8182016.818\\,2016.818 201M4subscript𝑀4M\_{4}italic\_M start\_POSTSUBSCRIPT 4 end\_POSTSUBSCRIPT (Kinematic Direction)32.569 92932.56992932.569\\,92932.569 92943.173 85343.17385343.173\\,85343.173 85343.572 66143.57266143.572\\,66143.572 66129.150 86729.15086729.150\\,86729.150 86721.325 63021.32563021.325\\,63021.325 630\\cellcolorblack!1016.010 93816.01093816.010\\,93816.010 938M5subscript𝑀5M\_{5}italic\_M start\_POSTSUBSCRIPT 5 end\_POSTSUBSCRIPT (Kinematic Velocity)98.654 16498.65416498.654\\,16498.654 16488.895 46188.89546188.895\\,46188.895 46157.955 08457.95508457.955\\,08457.955 08431.386 00731.38600731.386\\,00731.386 00721.076 58921.07658921.076\\,58921.076 58916.837 08216.83708216.837\\,08216.837 082M6subscript𝑀6M\_{6}italic\_M start\_POSTSUBSCRIPT 6 end\_POSTSUBSCRIPT (Kinematic Dipole)30.336 51730.33651730.336\\,51730.336 51735.703 67735.70367735.703\\,67735.703 67734.850 18034.85018034.850\\,18034.850 18026.080 76926.08076926.080\\,76926.080 76920.397 99220.39799220.397\\,99220.397 99217.443 67417.44367417.443\\,67417.443 674

Report issue for preceding element

Table 6: As for Table [3](https://arxiv.org/html/2311.14938v2#A1.T3 "Table 3 ‣ Appendix A Bayes Factors for Tested Hypotheses ‣ The Cosmic Dipole in the Quaia Sample of Quasars: A Bayesian Analysis") but with Quaia high and the Poisson statistics.Report issue for preceding element

Hypothesis   Galactic mask angle b∘superscript𝑏b^{\\circ}italic\_b start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT001010101020202020303030304040404030303030\*

M0subscript𝑀0M\_{0}italic\_M start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT (Null)0.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 0000.000 0000.0000000.000\\,0000.000 000M1subscript𝑀1M\_{1}italic\_M start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT (Dipole)376.000 000376.000000376.000\\,000376.000 000308.100 000308.100000308.100\\,000308.100 000146.500 000146.500000146.500\\,000146.500 00049.300 00049.30000049.300\\,00049.300 00021.200 00021.20000021.200\\,00021.200 00018.778 62018.77862018.778\\,62018.778 620\\cellcolorblack!10
M2subscript𝑀2M\_{2}italic\_M start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT (Double Dipole)426.791 312426.791312426.791\\,312426.791 312\\cellcolorblack!10328.539 441328.539441328.539\\,441328.539 441\\cellcolorblack!10155.837 352155.837352155.837\\,352155.837 352\\cellcolorblack!1050.917 74850.91774850.917\\,74850.917 748\\cellcolorblack!1020.201 34520.20134520.201\\,34520.201 34516.176 39316.17639316.176\\,39316.176 393M3subscript𝑀3M\_{3}italic\_M start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT (Quadrupole)64.400 00064.40000064.400\\,00064.400 00027.700 00027.70000027.700\\,00027.700 00010.200 00010.20000010.200\\,00010.200 0002.300 0002.3000002.300\\,0002.300 0000.200 0000.2000000.200\\,0000.200 0007.178 6207.1786207.178\\,6207.178 620M4subscript𝑀4M\_{4}italic\_M start\_POSTSUBSCRIPT 4 end\_POSTSUBSCRIPT (Kinematic Direction)32.519 14732.51914732.519\\,14732.519 14743.213 93343.21393343.213\\,93343.213 93343.596 22943.59622943.596\\,22943.596 22929.243 38429.24338429.243\\,38429.243 38421.417 60221.41760221.417\\,60221.417 602\\cellcolorblack!1016.346 72316.34672316.346\\,72316.346 723M5subscript𝑀5M\_{5}italic\_M start\_POSTSUBSCRIPT 5 end\_POSTSUBSCRIPT (Kinematic Velocity)98.306 56098.30656098.306\\,56098.306 56088.593 32988.59332988.593\\,32988.593 32957.663 70957.66370957.663\\,70957.663 70931.606 55231.60655231.606\\,55231.606 55221.013 92121.01392121.013\\,92121.013 92116.615 12816.61512816.615\\,12816.615 128M6subscript𝑀6M\_{6}italic\_M start\_POSTSUBSCRIPT 6 end\_POSTSUBSCRIPT (Kinematic Dipole)30.195 95330.19595330.195\\,95330.195 95335.724 36835.72436835.724\\,36835.724 36834.653 69234.65369234.653\\,69234.653 69226.172 29226.17229226.172\\,29226.172 29220.359 35720.35935720.359\\,35720.359 35717.371 70917.37170917.371\\,70917.371 709

Report issue for preceding element

Report issue for preceding element

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)

──────── [TRUNCATED] ────────
Showing 37,197 chars (head) + 12,398 chars (tail) of 172,454 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-06b0eda53c.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-06b0eda53c.md" offset=311 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
