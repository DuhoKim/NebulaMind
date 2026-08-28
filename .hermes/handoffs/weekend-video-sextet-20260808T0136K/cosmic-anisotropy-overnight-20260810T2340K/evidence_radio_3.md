URL: https://arxiv.org/html/2503.02470v1

HTML conversions [sometimes display errors](https://info.dev.arxiv.org/about/accessibility_html_error_messages.html) due to content that did not convert correctly from the source. This paper uses the following packages that are not yet supported by the HTML conversion tool. Feedback on these issues are not necessary; they are known and are being worked on.

- failed: textgreek

Authors: achieve the best HTML results from your LaTeX submissions by following these [best practices](https://info.arxiv.org/help/submit_latex_best_practices.html).

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2503.02470v1 \[astro-ph.CO\] 04 Mar 2025

11institutetext: Max-Planck Institut fur Radioastronomie,
Auf dem Hügel 69,
53121 Bonn, Germany
22institutetext: Department of Physics,
University of Oxford,
Parks Road, Oxford OX1 3PU, UK
33institutetext: Fakultät für Physik,
Universität Bielefeld,
Postfach 100131,
33501 Bielefeld, Germany

# The kinematic contribution to the cosmic number count dipole

Report issue for preceding element

J.D. Wagenveld
11S. von Hausegger
22H-R. Klöckner
11D.J. Schwarz
33

Report issue for preceding element

Measurements of the number count dipole with large surveys have shown amplitudes in tension with kinematic predictions based on the observed Doppler dipole of the cosmic microwave background (CMB). These observations seem to be in direct conflict with a homogeneous and isotropic Universe as asserted by the cosmological principle, demanding further investigation into the origin of the tension. Here, we investigate whether the observed number count dipoles are consistent with being fully kinematic, regardless of boost, or if there is any residual anisotropy contributing to the total observed dipole, independent of the kinematic part. To disentangle these contributions, we aim to leverage the fact that the kinematic matter dipole expected in a given galaxy catalogue scales with observed properties of the sample, and different catalogues used in the literature therefore have different kinematic dipole expectations. We here perform joint dipole fits using the NRAO VLA Sky Survey (NVSS), the Rapid ASKAP Continuum Survey (RACS), and the AGN catalogue derived from the Wide-field Infrared Survey Explorer (CatWISE). The direction of the common dipole between these catalogues is offset from the CMB dipole direction by 23±5plus-or-minus23523\\pm 523 ± 5 degrees. Assuming a common kinematic and non-kinematic dipole component between all catalogues, we find that a large residual, non-kinematic dipole anisotropy is detected, though a common direction between the two components is disfavoured by model selection. Freeing up both amplitude and direction for this residual dipole while fixing the kinematic dipole to the CMB dipole expectation, we recover a significant residual dipole with 𝒟r⁢e⁢s⁢i⁢d=(0.81±0.14)×10−2subscript𝒟𝑟𝑒𝑠𝑖𝑑plus-or-minus0.810.14superscript102\\mathcal{D}\_{resid}=(0.81\\pm 0.14)\\times 10^{-2}caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT = ( 0.81 ± 0.14 ) × 10 start\_POSTSUPERSCRIPT - 2 end\_POSTSUPERSCRIPT, that is offset from the CMB dipole direction by 39±8plus-or-minus39839\\pm 839 ± 8 degrees. While these results cannot explain the origin of the unexpectedly large number count dipoles, they offer a rephrasing of the anomaly in terms of kinematic and non-kinematic contributions, providing evidence for the existence of the latter within the models explored here. The present work provides a valuable first test of this concept, although its scrutinising power is limited by the currently employed catalogues. Larger catalogues, especially in radio, will be needed to further lift the degeneracy between the kinematic and residual dipole components.

Report issue for preceding element

###### Key Words.:

Report issue for preceding elementlarge scale structure of the Universe –
Cosmology: observations –
Galaxies: statistics

## 1 Introduction

Report issue for preceding element

Modern cosmological models based on Friedmann-Lemaître-Robertson-Walker (FLRW) metrics, such as \\textLambda-CDM, are built on the assumptions of the cosmological principle. As such, these models require homogeneity and isotropy on the largest scales. While the cosmic microwave background (CMB) is a remarkable example of this large scale isotropy, with fluctuations around the CMB monopole being largely as small as 1 part in 105superscript10510^{5}10 start\_POSTSUPERSCRIPT 5 end\_POSTSUPERSCRIPT, the CMB dipole appears to be an exception. A hundred times larger than the smaller-scale fluctuations, the CMB dipole is conventionally considered to be the result of our movement with respect to the frame in which the CMB would have appeared isotropic, the so-called CMB rest frame. Under this interpretation, measurements of the CMB dipole translate a velocity of the Solar System with respect to the CMB of v=369.82±0.11⁢km⁢s−1𝑣plus-or-minus369.820.11kmsuperscripts1v=369.82\\pm 0.11\ \\mathrm{km\ s^{-1}}italic\_v = 369.82 ± 0.11 roman\_km roman\_s start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT(Aghanim et al., [2020](https://arxiv.org/html/2503.02470v1#bib.bib1 "")).

Report issue for preceding element

Our movement is expected to result in an apparent dipole also in the number counts of cosmologically distant sources, whose rest frame ought to agree with that of the CMB (Ellis & Baldwin, [1984](https://arxiv.org/html/2503.02470v1#bib.bib13 "")). Caused by the relativistic effects of aberration, Doppler boosting, and Doppler shifting of the observed source positions and spectra, the same physics is at play as that suspected at the root of the CMB dipole. This immediately places an expectation on the kinematic matter dipole: a dipole pointing in the same direction as the CMB dipole with an amplitude proportional to β=v/c𝛽𝑣𝑐\\beta=v/citalic\_β = italic\_v / italic\_c, where c𝑐citalic\_c is the speed of light. To measure the expected 𝒪⁢(10−3)𝒪superscript103\\mathcal{O}(10^{-3})caligraphic\_O ( 10 start\_POSTSUPERSCRIPT - 3 end\_POSTSUPERSCRIPT ) number count dipole, it was predicted that catalogues of extragalactic sources in excess of 106superscript10610^{6}10 start\_POSTSUPERSCRIPT 6 end\_POSTSUPERSCRIPT were required to reach 3⁢σ3𝜎3\\sigma3 italic\_σ statistical significance (Crawford, [2009](https://arxiv.org/html/2503.02470v1#bib.bib7 "")). The earliest statistically significant measurements were performed with a catalogue of radio sources from the National Radio Astronomy Observatory (NRAO) Very Large Array (VLA) Sky Survey (NVSS, Condon et al., [1998](https://arxiv.org/html/2503.02470v1#bib.bib6 "")), where the measured dipole consistently had a larger amplitude than expected (e.g. Blake & Wall, [2002](https://arxiv.org/html/2503.02470v1#bib.bib3 ""); Singal, [2011](https://arxiv.org/html/2503.02470v1#bib.bib50 ""); Rubart & Schwarz, [2013](https://arxiv.org/html/2503.02470v1#bib.bib44 ""); Siewert et al., [2021](https://arxiv.org/html/2503.02470v1#bib.bib49 ""); Secrest et al., [2022](https://arxiv.org/html/2503.02470v1#bib.bib46 ""); Wagenveld et al., [2023](https://arxiv.org/html/2503.02470v1#bib.bib61 "")), while being broadly consistent with the CMB dipole in terms of direction. Other radio catalogues have since been used for this measurement with varying levels of success, yielding similar results, though in absence of independent measurements at other wavelengths it was difficult to exclude common systematic effects as the cause of the dipole.

Report issue for preceding element

An important breakthrough in the credibility of these measurements was the recent addition of a measurement of the number count dipole with infrared AGN (Secrest et al., [2021](https://arxiv.org/html/2503.02470v1#bib.bib47 ""), [2022](https://arxiv.org/html/2503.02470v1#bib.bib46 ""); Dam et al., [2023](https://arxiv.org/html/2503.02470v1#bib.bib9 "")). This measurement was performed with a catalogue of sources observed by the Wide-field Infrared Survey Explorer (WISE, Wright et al., [2010](https://arxiv.org/html/2503.02470v1#bib.bib63 "")). As WISE is a space-based telescope, it is not influenced by any of the potential systematic effects that would affect ground-based radio observations. Furthermore, the sample of sources was entirely independent from NVSS and other radio catalogues. This measurement yielded a dipole amplitude that was two times larger than the kinematic expectation, with a significance of 4.9⁢σ4.9𝜎4.9\\sigma4.9 italic\_σ. With this level of significance, these measurements are in serious tension with the cosmological principle. Since then, additional measurements of the dipole with quasars selected in a composition of optical and infrared measurements (Mittal et al., [2024b](https://arxiv.org/html/2503.02470v1#bib.bib37 ""), [a](https://arxiv.org/html/2503.02470v1#bib.bib36 "")) also showed a higher amplitude than expected, although to a less significant degree, due to lower source counts. With this, an excess dipole has now been confirmed at different wavelengths, with different instruments, and in different independent source samples.

Report issue for preceding element

With such pronounced excess dipoles measured in these catalogues, the question arises whether the measured dipole is purely caused by the velocity of the observer, as is assumed in Ellis & Baldwin ( [1984](https://arxiv.org/html/2503.02470v1#bib.bib13 "")). Rather than a purely kinematic ‘EB dipole’, some other (residual) component could be contributing to the total observed dipole, that does not scale with β𝛽\\betaitalic\_β. Such a question lies at the core of studies employing a range of methods to scrutinise the kinematic dipole signals detected (and suspected) thus far. For instance, the CMB Doppler dipole is expected to be accompanied by aberration of the CMB anisotropies and though indeed corresponding measurements report consistency (Planck Collaboration et al., [2014](https://arxiv.org/html/2503.02470v1#bib.bib42 ""); Saha et al., [2021](https://arxiv.org/html/2503.02470v1#bib.bib45 ""); Ferreira & Quartin, [2021](https://arxiv.org/html/2503.02470v1#bib.bib17 "")), it has not been conclusively shown that the CMB dipole is entirely kinematic. For the number count dipole, methods to measure kinematic and non-kinematic components separately have been proposed (e.g. Nadolny et al., [2021](https://arxiv.org/html/2503.02470v1#bib.bib38 ""); Tiwari et al., [2015](https://arxiv.org/html/2503.02470v1#bib.bib52 "")), although these require a great deal more data than what is currently available. Only recently, Ferreira & Marra ( [2024](https://arxiv.org/html/2503.02470v1#bib.bib16 "")) and Tiwari et al. ( [2024](https://arxiv.org/html/2503.02470v1#bib.bib54 "")) attempted to measure the kinematic dipole directly using redshifts from Sloan Digital Sky Survey (SDSS). While there is an indication for consistency with the CMB dipole, large uncertainties remain. Separate measures of the Solar system velocity, for example with SNIa (e.g. Horstmann et al., [2022](https://arxiv.org/html/2503.02470v1#bib.bib25 "")), seem to favour consistency with the velocity obtained from the CMB dipole as well. However, an explicit separation of kinematic and non-kinematic dipoles has not been made, and these components have so far not been independently and simultaneously measured.

Report issue for preceding element

We here propose and implement an alternative method for isolating the kinematic dipole, as expected from Ellis & Baldwin ( [1984](https://arxiv.org/html/2503.02470v1#bib.bib13 "")), from a potential non-kinematic, residual dipole, by using multiple catalogues at the same time. We achieve this by utilising the dipole estimator from Wagenveld et al. ( [2023](https://arxiv.org/html/2503.02470v1#bib.bib61 "")), which is able to fit a common dipole signal from a set of catalogues. This avoids the problems that stem from attempting to combine the catalogues, due to differences in frequency, angular resolution, and flux density limit (e.g. Colin et al., [2017](https://arxiv.org/html/2503.02470v1#bib.bib4 ""); Darling, [2022](https://arxiv.org/html/2503.02470v1#bib.bib10 "")). Previously, this procedure allowed a combined dipole estimate between NVSS and the Rapid Australian Square Kilometre Array Pathfinder (ASKAP) Continuum Survey (RACS-low, Hale et al., [2021](https://arxiv.org/html/2503.02470v1#bib.bib24 "")). This measurement could be performed because the predicted (kinematic) dipole amplitude of both catalogues was the same. While true for the case of NVSS, RACS-low and other radio catalogues, this is not the case in general. For instance for CatWISE the expected dipole amplitude is nearly twice that of NVSS and RACS-low. Under certain assumptions, chief of which is that any residual non-kinematic dipole component is common between the catalogues, using catalogues with different expected kinematic dipole amplitudes allows a combined estimate to be used to separate these components.

Report issue for preceding element

In this paper, we will use the NVSS, RACS-low and CatWISE AGN catalogues and their different expected kinematic dipole amplitudes to isolate the kinematic component of the number count dipole. The paper is organised as follows. In Section [2](https://arxiv.org/html/2503.02470v1#S2 "2 The cosmic number count dipole ‣ The kinematic contribution to the cosmic number count dipole") we describe the estimators, and in Section [3](https://arxiv.org/html/2503.02470v1#S3 "3 Data ‣ The kinematic contribution to the cosmic number count dipole") we describe the data we will use to perform this measurement. The results are presented in Section [4](https://arxiv.org/html/2503.02470v1#S4 "4 Results ‣ The kinematic contribution to the cosmic number count dipole"), and discussed in Section [5](https://arxiv.org/html/2503.02470v1#S5 "5 Discussion ‣ The kinematic contribution to the cosmic number count dipole"). We conclude in Section [6](https://arxiv.org/html/2503.02470v1#S6 "6 Conclusion ‣ The kinematic contribution to the cosmic number count dipole").

Report issue for preceding element

## 2 The cosmic number count dipole

Report issue for preceding element

As a result of Doppler boost, Doppler shift and relativistic aberration induced by our velocity with respect to background sources, we see a dipole in the observed number counts of extragalactic background sources. The amplitude of this kinematic number count dipole, caused by the velocity of the observer β=v/c𝛽𝑣𝑐\\beta=v/citalic\_β = italic\_v / italic\_c, is given by (Ellis & Baldwin, [1984](https://arxiv.org/html/2503.02470v1#bib.bib13 ""))

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒟k⁢i⁢n=\[2+x⁢(1+α)\]⁢β,subscript𝒟𝑘𝑖𝑛delimited-\[\]2𝑥1𝛼𝛽\\mathcal{D}\_{kin}=\[2+x(1+\\alpha)\]\\beta,caligraphic\_D start\_POSTSUBSCRIPT italic\_k italic\_i italic\_n end\_POSTSUBSCRIPT = \[ 2 + italic\_x ( 1 + italic\_α ) \] italic\_β , |  | (1) |

and depends on the spectral index of the sources, α𝛼\\alphaitalic\_α111Here we use the spectral index convention S∝ν−αproportional-to𝑆superscript𝜈𝛼S\\propto\\nu^{-\\alpha}italic\_S ∝ italic\_ν start\_POSTSUPERSCRIPT - italic\_α end\_POSTSUPERSCRIPT., and the power law index of the flux density distribution, x𝑥xitalic\_x. These parameters in general differ per catalogue and survey, and as such the expected kinematic dipole amplitude for a given β𝛽\\betaitalic\_β can also differ. Given the fact that the measured dipole amplitude has in many cases been larger than the expected kinematic dipole amplitude, the possibility arises that the excess dipole amplitude is not kinematic, but is caused by a different phenomenon altogether. In this case (assuming that both components point in the same direction), we can hypothesise that the total dipole amplitude can be broken down as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒟=𝒟k⁢i⁢n+𝒟r⁢e⁢s⁢i⁢d,𝒟subscript𝒟𝑘𝑖𝑛subscript𝒟𝑟𝑒𝑠𝑖𝑑\\mathcal{D}=\\mathcal{D}\_{kin}+\\mathcal{D}\_{resid},caligraphic\_D = caligraphic\_D start\_POSTSUBSCRIPT italic\_k italic\_i italic\_n end\_POSTSUBSCRIPT + caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT , |  | (2) |

where 𝒟k⁢i⁢nsubscript𝒟𝑘𝑖𝑛\\mathcal{D}\_{kin}caligraphic\_D start\_POSTSUBSCRIPT italic\_k italic\_i italic\_n end\_POSTSUBSCRIPT is the Ellis & Baldwin ( [1984](https://arxiv.org/html/2503.02470v1#bib.bib13 "")) prediction from Equation [1](https://arxiv.org/html/2503.02470v1#S2.E1 "In 2 The cosmic number count dipole ‣ The kinematic contribution to the cosmic number count dipole"), and 𝒟r⁢e⁢s⁢i⁢dsubscript𝒟𝑟𝑒𝑠𝑖𝑑\\mathcal{D}\_{resid}caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT represents the contribution of a residual, non-kinematic dipole component. While the fact that the total dipole we measure is relatively close to the CMB dipole in direction indicates that any residual dipole might also point in a similar direction, it is unlikely that the separate components do point in the exact same direction. We distinguish corresponding considerations following Equation [8](https://arxiv.org/html/2503.02470v1#S2.E8 "In 2.2 Joint dipole estimation ‣ 2 The cosmic number count dipole ‣ The kinematic contribution to the cosmic number count dipole") below.

Report issue for preceding element

### 2.1 Dipole estimation

Report issue for preceding element

For dipole estimation we expand upon the existing Bayesian estimators introduced in Wagenveld et al. ( [2023](https://arxiv.org/html/2503.02470v1#bib.bib61 "")). These estimators are based on the fact that the counts-in-cells distribution of sources isotropically distributed across the sky follows a Poisson distribution

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | p⁢(n)=λn⁢e−λn!,𝑝𝑛superscript𝜆𝑛superscript𝑒𝜆𝑛p(n)=\\frac{\\lambda^{n}e^{-\\lambda}}{n!},italic\_p ( italic\_n ) = divide start\_ARG italic\_λ start\_POSTSUPERSCRIPT italic\_n end\_POSTSUPERSCRIPT italic\_e start\_POSTSUPERSCRIPT - italic\_λ end\_POSTSUPERSCRIPT end\_ARG start\_ARG italic\_n ! end\_ARG , |  | (3) |

where n𝑛nitalic\_n is the number of sources in a cell, and λ𝜆\\lambdaitalic\_λ represents the mean and variance of the distribution. The most basic Poisson estimator assumes only a dipole and monopole, which affect λ𝜆\\lambdaitalic\_λ as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | λ⁢(ℳ,d)=ℳ⁢(1+d⋅n^).𝜆ℳ@vec⁡dℳ1⋅@vec⁡d@vec⁡n^\\lambda(\\mathcal{M},\\@vec{d})=\\mathcal{M}(1+\\@vec{d}\\cdot\\@vec{\\hat{n}}).italic\_λ ( caligraphic\_M , start\_ID start\_ARG italic\_d end\_ARG end\_ID ) = caligraphic\_M ( 1 + start\_ID start\_ARG italic\_d end\_ARG end\_ID ⋅ start\_ID start\_ARG over^ start\_ARG italic\_n end\_ARG end\_ARG end\_ID ) . |  | (4) |

Here ℳℳ\\mathcal{M}caligraphic\_M represents the monopole, and d@vec⁡d\\@vec{d}start\_ID start\_ARG italic\_d end\_ARG end\_ID the dipole vector, the amplitude of which is 𝒟𝒟\\mathcal{D}caligraphic\_D. In order to estimate the dipole parameters, we maximise the likelihood given by

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒ⁢(n\|d,ℳ)=∏iλ⁢(ℳ,d)ni⁢e−λ⁢(ℳ,d)ni!,ℒconditional@vec⁡n@vec⁡dℳsubscriptproduct𝑖𝜆superscriptℳ@vec⁡dsubscript𝑛𝑖superscript𝑒𝜆ℳ@vec⁡dsubscript𝑛𝑖\\mathcal{L}(\\@vec{n}\|\\@vec{d},\\mathcal{M})=\\prod\_{i}\\frac{\\lambda(\\mathcal{M},%<br>\\@vec{d})^{n\_{i}}e^{-\\lambda(\\mathcal{M},\\@vec{d})}}{n\_{i}!},caligraphic\_L ( start\_ID start\_ARG italic\_n end\_ARG end\_ID \| start\_ID start\_ARG italic\_d end\_ARG end\_ID , caligraphic\_M ) = ∏ start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT divide start\_ARG italic\_λ ( caligraphic\_M , start\_ID start\_ARG italic\_d end\_ARG end\_ID ) start\_POSTSUPERSCRIPT italic\_n start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT italic\_e start\_POSTSUPERSCRIPT - italic\_λ ( caligraphic\_M , start\_ID start\_ARG italic\_d end\_ARG end\_ID ) end\_POSTSUPERSCRIPT end\_ARG start\_ARG italic\_n start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ! end\_ARG , |  | (5) |

over all cells i𝑖iitalic\_i. This likelihood was shown in Wagenveld et al. ( [2023](https://arxiv.org/html/2503.02470v1#bib.bib61 "")) to produce similar results as quadratic estimators, and outperforms them in the limit of low counts where the assumption of Gaussian noise no longer holds. It was also shown that this basic estimator can be extended in several ways to increase the number of usable sources for a dipole measurement while accounting for systematics. One such extension of the basic Poisson estimator was used in Wagenveld et al. ( [2024](https://arxiv.org/html/2503.02470v1#bib.bib60 "")) to fit for an additional linear relation between a specific parameter y𝑦yitalic\_y and the source density

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | λ⁢(d,ℳ,ε,y)=ℳ⁢\[1−ε⋅y\]⁢(1+d⋅n^),𝜆@vec⁡dℳ𝜀𝑦ℳdelimited-\[\]1⋅𝜀𝑦1⋅@vec⁡d^𝑛\\lambda(\\@vec{d},\\mathcal{M},\\varepsilon,y)=\\mathcal{M}\[1-\\varepsilon\\cdot y\](%<br>1+\\@vec{d}\\cdot\\hat{n}),italic\_λ ( start\_ID start\_ARG italic\_d end\_ARG end\_ID , caligraphic\_M , italic\_ε , italic\_y ) = caligraphic\_M \[ 1 - italic\_ε ⋅ italic\_y \] ( 1 + start\_ID start\_ARG italic\_d end\_ARG end\_ID ⋅ over^ start\_ARG italic\_n end\_ARG ) , |  | (6) |

where ε𝜀\\varepsilonitalic\_ε is defined as the slope of the linear relation. Below, we use this estimator to fit the observed change in source density as a function of absolute ecliptic latitude seen in CatWISE (Secrest et al., [2021](https://arxiv.org/html/2503.02470v1#bib.bib47 "")), similar to what was done in Dam et al. ( [2023](https://arxiv.org/html/2503.02470v1#bib.bib9 "")). As demonstrated in Dam et al. ( [2023](https://arxiv.org/html/2503.02470v1#bib.bib9 "")), not including the ecliptic latitude effect is heavily disfavoured by model selection, and yields an even higher dipole amplitude than if it is included.

Report issue for preceding element

### 2.2 Joint dipole estimation

Report issue for preceding element

Another extension of the basic Poisson estimator is the multi-Poisson estimator, which can take multiple catalogues and perform a joint dipole estimate. This estimator assumes a common dipole but a different monopole for each catalogue, thereby allowing the fit of a common dipole signal. The likelihood of this estimator is defined as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒ⁢(n\|d,ℳ)=∏j\[∏iλ⁢(ℳj,d)ni,j⁢e−λ⁢(ℳj,d)ni,j!\],ℒconditional@vec⁡n@vec⁡d@vec⁡ℳsubscriptproduct𝑗delimited-\[\]subscriptproduct𝑖𝜆superscriptsubscriptℳ𝑗@vec⁡dsubscript𝑛𝑖𝑗superscript𝑒𝜆subscriptℳ𝑗@vec⁡dsubscript𝑛𝑖𝑗\\mathcal{L}(\\@vec{n}\|\\@vec{d},\\@vec{\\mathcal{M}})=\\prod\_{j}\\left\[\\prod\_{i}%<br>\\frac{\\lambda(\\mathcal{M}\_{j},\\@vec{d})^{n\_{i,j}}e^{-\\lambda(\\mathcal{M}\_{j},%<br>\\@vec{d})}}{n\_{i,j}!}\\right\],caligraphic\_L ( start\_ID start\_ARG italic\_n end\_ARG end\_ID \| start\_ID start\_ARG italic\_d end\_ARG end\_ID , start\_ID start\_ARG caligraphic\_M end\_ARG end\_ID ) = ∏ start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT \[ ∏ start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT divide start\_ARG italic\_λ ( caligraphic\_M start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT , start\_ID start\_ARG italic\_d end\_ARG end\_ID ) start\_POSTSUPERSCRIPT italic\_n start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT italic\_e start\_POSTSUPERSCRIPT - italic\_λ ( caligraphic\_M start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT , start\_ID start\_ARG italic\_d end\_ARG end\_ID ) end\_POSTSUPERSCRIPT end\_ARG start\_ARG italic\_n start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT ! end\_ARG \] , |  | (7) |

taking the product over each cell i𝑖iitalic\_i in each catalogue j𝑗jitalic\_j and taking the product of all catalogues. The efficacy of this estimator is however predicated on the fact that the catalogues have the same dipole signal, whereas the amplitude of the kinematic dipole actually depends on the spectral indices and flux density distribution of the sources in the catalogue. As such, if we wish to combine catalogues with different expected kinematic dipole amplitudes, this presents an opportunity to, under certain assumptions, actually isolate the kinematic dipole from any other components contributing to the dipole, following Equation [2](https://arxiv.org/html/2503.02470v1#S2.E2 "In 2 The cosmic number count dipole ‣ The kinematic contribution to the cosmic number count dipole"). Based on this principle, we redefine the dipole vector d@vec⁡d\\@vec{d}start\_ID start\_ARG italic\_d end\_ARG end\_ID in Equation [7](https://arxiv.org/html/2503.02470v1#S2.E7 "In 2.2 Joint dipole estimation ‣ 2 The cosmic number count dipole ‣ The kinematic contribution to the cosmic number count dipole") as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | dj=\[2+xj⁢(1+αj)\]⁢β+dr⁢e⁢s⁢i⁢d,subscript@vec⁡d𝑗delimited-\[\]2subscript𝑥𝑗1subscript𝛼𝑗@vec⁡βsubscript@vec⁡d𝑟𝑒𝑠𝑖𝑑\\@vec{d}\_{j}=\[2+x\_{j}(1+\\alpha\_{j})\]\\@vec{\\beta}+\\@vec{d}\_{resid},start\_ID start\_ARG italic\_d end\_ARG end\_ID start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT = \[ 2 + italic\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT ( 1 + italic\_α start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT ) \] start\_ID start\_ARG italic\_β end\_ARG end\_ID + start\_ID start\_ARG italic\_d end\_ARG end\_ID start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT , |  | (8) |

for catalogue j𝑗jitalic\_j, where each catalogue has a different pair of x𝑥xitalic\_x and α𝛼\\alphaitalic\_α values. To get a better understanding of what model describes the data the best, we consider several different hypotheses.

Report issue for preceding element

1. (0)


The dipole consists of a single component, which is fully kinematic.

Report issue for preceding element

2. (i)


The dipole consists of two components, one kinematic and one residual, which both point in the same direction.

Report issue for preceding element

3. (ii)


The dipole consists of two components, one kinematic and one residual, which both point in different directions.

Report issue for preceding element

4. (iii)


The dipole consists of two components, one kinematic and one residual, which both point different directions. The kinematic component is fixed to what is expected from the CMB dipole in both amplitude and direction.

Report issue for preceding element


Here, hypothesis (0) is considered our “null” hypothesis, and seeks to explain the observed dipole purely by kinematics. In all other cases, we separate the kinematic contribution and residual dipole, described by β@vec⁡β\\@vec{\\beta}start\_ID start\_ARG italic\_β end\_ARG end\_ID and dr⁢e⁢s⁢i⁢dsubscript@vec⁡d𝑟𝑒𝑠𝑖𝑑\\@vec{d}\_{resid}start\_ID start\_ARG italic\_d end\_ARG end\_ID start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT, respectively. If the direction of these components is the same, Equation [8](https://arxiv.org/html/2503.02470v1#S2.E8 "In 2.2 Joint dipole estimation ‣ 2 The cosmic number count dipole ‣ The kinematic contribution to the cosmic number count dipole") simply becomes a linear equation with two unknowns, and thus requires at least two measurements with significantly different outcomes to resolve. This is of course more complicated once we associate uncertainties with these measurements. In the latter two cases, we also allow for separate directions for these two components. We stress here that the separation of dipole components as presented here assumes that different catalogues have the same dr⁢e⁢s⁢i⁢dsubscript@vec⁡d𝑟𝑒𝑠𝑖𝑑\\@vec{d}\_{resid}start\_ID start\_ARG italic\_d end\_ARG end\_ID start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT, even though the origin of this dipole component is not known. The validity of this assumption is discussed in Section [5](https://arxiv.org/html/2503.02470v1#S5 "5 Discussion ‣ The kinematic contribution to the cosmic number count dipole").

Report issue for preceding element

### 2.3 Priors

Report issue for preceding element

To avoid biasing results, we aim to make priors as uninformed as possible. For the dipole, we separately fit the right ascension and declination of the dipole direction, as well as the dipole amplitude. We do not restrict or fix any particular direction (unless explicitly mentioned), so the priors on right ascension and declination of the dipole direction are the same for both the kinematic and residual dipole. On individual catalogues we can only fit for the total dipole amplitude 𝒟𝒟\\mathcal{D}caligraphic\_D, while in the multi-Poisson estimator, we fit for both β𝛽\\betaitalic\_β and 𝒟r⁢e⁢s⁢i⁢dsubscript𝒟𝑟𝑒𝑠𝑖𝑑\\mathcal{D}\_{resid}caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT. We define these priors such that the total dipole amplitude can not exceed unity. Regardless of estimator, we estimate the monopole ℳℳ\\mathcal{M}caligraphic\_M for each catalogue separately, using as an initial estimate the mean of all cell counts n¯¯𝑛\\bar{n}over¯ start\_ARG italic\_n end\_ARG. We can summarise these general priors as follows

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | π⁢(𝒟)𝜋𝒟\\displaystyle\\pi(\\mathcal{D})italic\_π ( caligraphic\_D ) | ∼usimilar-toabsent𝑢\\displaystyle\\sim u∼ italic\_u |  |
|  | π⁢(𝒟r⁢e⁢s⁢i⁢d)𝜋subscript𝒟𝑟𝑒𝑠𝑖𝑑\\displaystyle\\pi(\\mathcal{D}\_{resid})italic\_π ( caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT ) | ∼0.5⋅usimilar-toabsent⋅0.5𝑢\\displaystyle\\sim 0.5\\cdot u∼ 0.5 ⋅ italic\_u |  |
|  | π⁢(β)𝜋𝛽\\displaystyle\\pi(\\beta)italic\_π ( italic\_β ) | ∼0.05⋅usimilar-toabsent⋅0.05𝑢\\displaystyle\\sim 0.05\\cdot u∼ 0.05 ⋅ italic\_u |  |
|  | π(R.A.)\\displaystyle\\pi(\\mathrm{R.A.})italic\_π ( roman\_R . roman\_A . ) | ∼360⋅usimilar-toabsent⋅360𝑢\\displaystyle\\sim 360\\cdot u∼ 360 ⋅ italic\_u |  |
|  | π(Dec.)\\displaystyle\\pi(\\mathrm{Dec.})italic\_π ( roman\_Dec . ) | ∼sin−1⁡\[2⁢u−1\]similar-toabsentsuperscript12𝑢1\\displaystyle\\sim\\sin^{-1}\[2u-1\]∼ roman\_sin start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT \[ 2 italic\_u - 1 \] |  |
|  | π⁢(ℳ)𝜋ℳ\\displaystyle\\pi(\\mathcal{M})italic\_π ( caligraphic\_M ) | ∼2⁢n¯⋅u.similar-toabsent⋅2¯𝑛𝑢\\displaystyle\\sim 2\\bar{n}\\cdot u.∼ 2 over¯ start\_ARG italic\_n end\_ARG ⋅ italic\_u . |  |

Here, u=𝒰⁢\[0,1\]𝑢𝒰01u=\\mathcal{U}\[0,1\]italic\_u = caligraphic\_U \[ 0 , 1 \] represents a uniform distribution between 0 and 1. For the Poisson estimator implementing a linear fit described in Equation [6](https://arxiv.org/html/2503.02470v1#S2.E6 "In 2.1 Dipole estimation ‣ 2 The cosmic number count dipole ‣ The kinematic contribution to the cosmic number count dipole"), we fit for an additional parameter ε𝜀\\varepsilonitalic\_ε. The only requirement for this parameter is that the resulting number counts should not be negative, making the prior dependent on the maximum value of y𝑦yitalic\_y, such that π⁢(ε)∼(2⁢u−1)/ym⁢a⁢xsimilar-to𝜋𝜀2𝑢1subscript𝑦𝑚𝑎𝑥\\pi(\\varepsilon)\\sim(2u-1)/y\_{max}italic\_π ( italic\_ε ) ∼ ( 2 italic\_u - 1 ) / italic\_y start\_POSTSUBSCRIPT italic\_m italic\_a italic\_x end\_POSTSUBSCRIPT.

Report issue for preceding element

All above described esimators are implemented using the Bayesian inference library bilby(Ashton et al., [2019](https://arxiv.org/html/2503.02470v1#bib.bib2 "")). Through bilby, we maximise the likelihood with MCMC sampling using emcee(Foreman-Mackey et al., [2013](https://arxiv.org/html/2503.02470v1#bib.bib18 "")). After sampling, the best-fit parameters are obtained by taking the median of the posterior distribution, with the uncertainties represented by the 16% (lower) and 84% (upper) quantiles of the distribution. The scripts where these have been implemented are available on GitHub222 [https://github.com/JonahDW/Bayesian-dipole](https://github.com/JonahDW/Bayesian-dipole "") and an immutable copy is archived in Zenodo (Wagenveld, [2025](https://arxiv.org/html/2503.02470v1#bib.bib59 "")).
For the purposes of model comparison, we use harmonic, which implements the learnt harmonic mean estimator (McEwen et al., [2021](https://arxiv.org/html/2503.02470v1#bib.bib33 "")) to compute the marginal likelihood, 𝒵𝒵\\mathcal{Z}caligraphic\_Z.

Report issue for preceding element

## 3 Data

Report issue for preceding elementTable 1: Best fit dipole estimates on the individual NVSS, RACS, and CatWISE catalogues.

| Catalogue | S0subscript𝑆0S\_{0}italic\_S start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT | N𝑁Nitalic\_N | ℳℳ\\mathcal{M}caligraphic\_M | ε𝜀\\varepsilonitalic\_ε | 𝒟𝒟\\mathcal{D}caligraphic\_D | R.A. | Dec. |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | (mJy) |  | counts/pixel | (×10−4absentsuperscript104\\times 10^{-4}× 10 start\_POSTSUPERSCRIPT - 4 end\_POSTSUPERSCRIPT) | (×10−2absentsuperscript102\\times 10^{-2}× 10 start\_POSTSUPERSCRIPT - 2 end\_POSTSUPERSCRIPT) | (deg) | (deg) |
| NVSS | 15 | 352,862 | 10.11±0.02plus-or-minus10.110.0210.11\\pm 0.0210.11 ± 0.02 | – | 1.39±0.29plus-or-minus1.390.291.39\\pm 0.291.39 ± 0.29 | 151±12plus-or-minus15112151\\pm 12151 ± 12 | −9±14plus-or-minus914-9\\pm 14\- 9 ± 14 |
| NVSSa | 15 | 351,483 | 10.07±0.02plus-or-minus10.070.0210.07\\pm 0.0210.07 ± 0.02 | – | 1.20±0.29plus-or-minus1.200.291.20\\pm 0.291.20 ± 0.29 | 152±14plus-or-minus15214152\\pm 14152 ± 14 | −10±16plus-or-minus1016-10\\pm 16\- 10 ± 16 |
| RACS-low | 15 | 442,046 | 14.20±0.02plus-or-minus14.200.0214.20\\pm 0.0214.20 ± 0.02 | – | 1.43±0.24plus-or-minus1.430.241.43\\pm 0.241.43 ± 0.24 | 190±10plus-or-minus19010190\\pm 10190 ± 10 | 3±13plus-or-minus3133\\pm 133 ± 13 |
| RACS-lowa | 15 | 440,377 | 14.15±0.02plus-or-minus14.150.0214.15\\pm 0.0214.15 ± 0.02 | – | 1.34±0.24plus-or-minus1.340.241.34\\pm 0.241.34 ± 0.24 | 194±11plus-or-minus19411194\\pm 11194 ± 11 | 8±14plus-or-minus8148\\pm 148 ± 14 |
| CatWISE | 0.078 | 1,567,586 | 68.23±0.09plus-or-minus68.230.0968.23\\pm 0.0968.23 ± 0.09 | 9.2±0.4plus-or-minus9.20.49.2\\pm 0.49.2 ± 0.4 | 1.51±0.16plus-or-minus1.510.161.51\\pm 0.161.51 ± 0.16 | 141±5plus-or-minus1415141\\pm 5141 ± 5 | −6±6plus-or-minus66-6\\pm 6\- 6 ± 6 |

333a Excluded sources matched to the 2MRS catalogue.

Report issue for preceding element

For the purposes of testing these hypotheses we want to combine several catalogues that have different expected kinematic dipole amplitudes. These catalogues should also provide reliable dipole measurements on their own, and thus be large enough to yield a significant dipole measurement individually. Furthermore, for combined measurements, we want to select catalogues that can easily be made statistically independent from each other. In a purely kinematic interpretation of the number count dipole, the dipole signal is dominated by sources near the flux density limit. As such, covering an completely independent sample of sources is not necessary for a statistically independent measurement. If however an intrinsic dipole is thought to contribute to the overall dipole, then this signal can originate from the overall observed source population. This motivates the use of the RACS-low, NVSS and CatWISE catalogues, which have all independently yielded robust and significant measurements of the number count dipole. With NVSS and RACS-low covering the northern and southern hemisphere radio populations respectively, and CatWISE covering the infrared quasar population, these catalogues see for the most part different sources. As such, they are easily made completely statistically independent by removal of shared sources, enabling joint dipole measurements to constrain the contribution of a residual dipole effect.

Report issue for preceding element


[... middle omitted — see footer ...]

Ashton, G., Hübner, M., Lasky, P. D., et al. 2019, ApJS, 241, 27

- Blake & Wall (2002)↑
Blake, C. & Wall, J. 2002, Nature, 416, 150

- Colin et al. (2017)↑
Colin, J., Mohayaee, R., Rameez, M., & Sarkar, S. 2017, MNRAS, 471, 1045

- Condon (1984)↑
Condon, J. J. 1984, ApJ, 287, 461

- Condon et al. (1998)↑
Condon, J. J., Cotton, W. D., Greisen, E. W., et al. 1998, AJ, 115, 1693

- Crawford (2009)↑
Crawford, F. 2009, ApJ, 692, 887

- Dalang & Bonvin (2022)↑
Dalang, C. & Bonvin, C. 2022, MNRAS, 512, 3895

- Dam et al. (2023)↑
Dam, L., Lewis, G. F., & Brewer, B. J. 2023, MNRAS, 525, 231

- Darling (2022)↑
Darling, J. 2022, ApJ, 931, L14

- Domènech et al. (2022)↑
Domènech, G., Mohayaee, R., Patil, S. P., & Sarkar, S. 2022, J. Cosmology Astropart. Phys., 2022,
019

- Duchesne et al. (2023)↑
Duchesne, S. W., Thomson, A. J. M., Pritchard, J., et al. 2023, PASA, 40,
e034

- Ellis & Baldwin (1984)↑
Ellis, G. F. R. & Baldwin, J. E. 1984, MNRAS, 206, 377

- Erickcek et al. (2008)↑
Erickcek, A. L., Carroll, S. M., & Kamionkowski, M. 2008, Phys. Rev. D, 78, 083012

- Erickcek et al. (2009)↑
Erickcek, A. L., Hirata, C. M., & Kamionkowski, M. 2009, Phys. Rev. D, 80, 083507

- Ferreira & Marra (2024)↑
Ferreira, P. d. S. & Marra, V. 2024, J. Cosmology Astropart. Phys., 2024, 077

- Ferreira & Quartin (2021)↑
Ferreira, P. d. S. & Quartin, M. 2021, Phys. Rev. Lett., 127, 101301

- Foreman-Mackey et al. (2013)↑
Foreman-Mackey, D., Hogg, D. W., Lang, D., & Goodman, J. 2013, PASP, 125,
306

- Gibelyou & Huterer (2012)↑
Gibelyou, C. & Huterer, D. 2012, MNRAS, 427, 1994

- Górski et al. (2005)↑
Górski, K. M., Hivon, E., Banday, A. J., et al. 2005, ApJ, 622, 759

- Grishchuk & Zeldovich (1978)↑
Grishchuk, L. P. & Zeldovich, Ia. B. 1978, Sov. Ast., 22, 125

- Guandalin et al. (2023)↑
Guandalin, C., Piat, J., Clarkson, C., & Maartens, R. 2023, ApJ, 953, 144

- Gunn (1988)↑
Gunn, J. E. 1988, 4, 344

- Hale et al. (2021)↑
Hale, C. L., McConnell, D., Thomson, A. J. M., et al. 2021, PASA, 38, e058

- Horstmann et al. (2022)↑
Horstmann, N., Pietschke, Y., & Schwarz, D. J. 2022, A&A, 668, A34

- Huchra et al. (2012)↑
Huchra, J. P., Macri, L. M., Masters, K. L., et al. 2012, ApJS, 199, 26

- kumar Aluri et al. (2023)↑
kumar Aluri, P., Cea, P., Chingangbam, P., et al. 2023, Classical and Quantum
Gravity, 40, 094001

- Lacasa et al. (2024)↑
Lacasa, F., Bonvin, C., Dalang, C., & Durrer, R. 2024, J. Cosmology Astropart. Phys., 2024, 045

- Lacy et al. (2020)↑
Lacy, M., Baum, S. A., Chandler, C. J., et al. 2020, PASP, 132, 035001

- Langlois & Piran (1996)↑
Langlois, D. & Piran, T. 1996, Phys. Rev. D, 53, 2908

- Marocco et al. (2021)↑
Marocco, F., Eisenhardt, P. R. M., Fowler, J. W., et al. 2021, ApJS, 253, 8

- McConnell et al. (2020)↑
McConnell, D., Hale, C. L., Lenc, E., et al. 2020, PASA, 37

- McEwen et al. (2021)↑
McEwen, J. D., Wallis, C. G. R., Price, M. A., & Spurio Mancini, A. 2021,
arXiv e-prints, arXiv:2111.12720

- Migkas et al. (2021)↑
Migkas, K., Pacaud, F., Schellenberger, G., et al. 2021, A&A, 649, A151

- Migkas & Reiprich (2018)↑
Migkas, K. & Reiprich, T. H. 2018, A&A, 611, A50

- Mittal et al. (2024a)↑
Mittal, V., Oayda, O. T., & Lewis, G. F. 2024a, MNRAS, 530, 4763

- Mittal et al. (2024b)↑
Mittal, V., Oayda, O. T., & Lewis, G. F. 2024b, MNRAS, 527, 8497

- Nadolny et al. (2021)↑
Nadolny, T., Durrer, R., Kunz, M., & Padmanabhan, H. 2021, J. Cosmology Astropart. Phys., 2021, 009

- Oayda et al. (2025)↑
Oayda, O. T., Mittal, V., & Lewis, G. F. 2025, MNRAS, 537, 1

- Oayda et al. (2024)↑
Oayda, O. T., Mittal, V., Lewis, G. F., & Murphy, T. 2024, MNRAS, 531, 4545

- Peebles (2022)↑
Peebles, P. J. E. 2022, Annals of Physics, 447, 169159

- Planck Collaboration et al. (2014)↑
Planck Collaboration, Aghanim, N., Armitage-Caplan, C., et al. 2014,
A&A, 571, A27

- Rameez et al. (2018)↑
Rameez, M., Mohayaee, R., Sarkar, S., & Colin, J. 2018, MNRAS, 477, 1772

- Rubart & Schwarz (2013)↑
Rubart, M. & Schwarz, D. J. 2013, A&A, 555, 1

- Saha et al. (2021)↑
Saha, S., Shaikh, S., Mukherjee, S., Souradeep, T., & Wandelt, B. D. 2021,
J. Cosmology Astropart. Phys., 2021, 072

- Secrest et al. (2022)↑
Secrest, N. J., von Hausegger, S., Rameez, M., Mohayaee, R., & Sarkar, S.
2022, ApJ, 937, L31

- Secrest et al. (2021)↑
Secrest, N. J., von Hausegger, S., Rameez, M., et al. 2021, ApJ, 908, L51

- Siewert et al. (2020)↑
Siewert, T. M., Hale, C., Bhardwaj, N., et al. 2020, A&A, 643, A100

- Siewert et al. (2021)↑
Siewert, T. M., Schmidt-Rubart, M., & Schwarz, D. J. 2021, A&A, 653, A9

- Singal (2011)↑
Singal, A. K. 2011, ApJ, 742, L23

- Taylor (2005)↑
Taylor, M. B. 2005, 347, 29

- Tiwari et al. (2015)↑
Tiwari, P., Kothari, R., Naskar, A., Nadkarni-Ghosh, S., & Jain, P. 2015,
Astroparticle Physics, 61, 1

- Tiwari & Nusser (2016)↑
Tiwari, P. & Nusser, A. 2016, J. Cosmology Astropart. Phys., 2016, 062

- Tiwari et al. (2024)↑
Tiwari, P., Schwarz, D. J., Zhao, G.-B., et al. 2024, ApJ, 975, 279

- Turner (1991)↑
Turner, M. S. 1991, Phys. Rev. D, 44, 3737

- Turner (1992)↑
Turner, M. S. 1992, General Relativity and Gravitation, 24, 1

- von Hausegger (2024)↑
von Hausegger, S. 2024, MNRAS, 535, L49

- von Hausegger & Dalang (2024)↑
von Hausegger, S. & Dalang, C. 2024, arXiv e-prints, arXiv:2412.13162

- Wagenveld (2025)↑
Wagenveld, J. 2025, JonahDW/Bayesian-dipole: Third Release, Zenodo

- Wagenveld et al. (2024)↑
Wagenveld, J. D., Klöckner, H. R., Gupta, N., et al. 2024, A&A, 690,
A163

- Wagenveld et al. (2023)↑
Wagenveld, J. D., Klöckner, H.-R., & Schwarz, D. J. 2023, A&A, 675, A72

- Watkins et al. (2023)↑
Watkins, R., Allen, T., Bradford, C. J., et al. 2023, MNRAS, 524, 1885

- Wright et al. (2010)↑
Wright, E. L., Eisenhardt, P. R., Mainzer, A. K., et al. 2010, AJ, 140, 1868

- Zonca et al. (2019)↑
Zonca, A., Singer, L. P., Lenz, D., et al. 2019, Journal of Open Source
Software, 4, 1298


## Appendix A Additional combined dipole estimates

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2503.02470v1/extracted/6251055/Figures/NVSS-WISE_beta_dipole.png)

![Refer to caption](https://arxiv.org/html/2503.02470v1/extracted/6251055/Figures/RACS-WISE_beta_dipole.png)

Figure 3: Posterior distributions of β𝛽\\betaitalic\_β and 𝒟r⁢e⁢s⁢i⁢dsubscript𝒟𝑟𝑒𝑠𝑖𝑑\\mathcal{D}\_{resid}caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT from the combined estimate using NVSS and CatWISE (upper panel), and RACS-low and CatWISE (lower panel). The 1-,2-, and 3-σ𝜎\\sigmaitalic\_σ uncertainties are indicated by the black contours. The dotted line indicates the maximum posterior values for these parameters. The canonical CMB velocity of β=1.23×10−3𝛽1.23superscript103\\beta=1.23\\times 10^{-3}italic\_β = 1.23 × 10 start\_POSTSUPERSCRIPT - 3 end\_POSTSUPERSCRIPT is indicated by the dotted red line, the red dot indicating the kinematic dipole expected in the standard cosmology, assuming a negligible structure dipole (𝒟r⁢e⁢s⁢i⁢d≈0subscript𝒟𝑟𝑒𝑠𝑖𝑑0\\mathcal{D}\_{resid}\\approx 0caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT ≈ 0)Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2503.02470v1/extracted/6251055/Figures/High_flux_beta_dipole.png)

![Refer to caption](https://arxiv.org/html/2503.02470v1/extracted/6251055/Figures/High_z_beta_dipole.png)

Figure 4: Posterior distributions of β𝛽\\betaitalic\_β and 𝒟r⁢e⁢s⁢i⁢dsubscript𝒟𝑟𝑒𝑠𝑖𝑑\\mathcal{D}\_{resid}caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT from the combined estimate using NVSS, RACS-low, and CatWISE. In the upper panel, higher flux density cuts are applied, with 20 mJy for NVSS and RACS-low, and 0.09 mJy (W1 ¡ 16.4) for CatWISE. In the lower panel, sources with z<0.1𝑧0.1z<0.1italic\_z < 0.1 in 2MRS have been removed from all catalogues. The 1-,2-, and 3-σ𝜎\\sigmaitalic\_σ uncertainties are indicated by the black contours. The dotted line indicates the maximum posterior values for these parameters. The canonical CMB velocity of β=1.23×10−3𝛽1.23superscript103\\beta=1.23\\times 10^{-3}italic\_β = 1.23 × 10 start\_POSTSUPERSCRIPT - 3 end\_POSTSUPERSCRIPT is indicated by the dotted red line, the red dot indicating the kinematic dipole expected in the standard cosmology, assuming a negligible structure dipole (𝒟r⁢e⁢s⁢i⁢d≈0subscript𝒟𝑟𝑒𝑠𝑖𝑑0\\mathcal{D}\_{resid}\\approx 0caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT ≈ 0)Report issue for preceding elementTable 3: Best fit dipole estimates for different data combinations and cuts. Where catalogues are combined only hypothesis (i) is tested, with results shown in Figures [3](https://arxiv.org/html/2503.02470v1#A1.F3 "Figure 3 ‣ Appendix A Additional combined dipole estimates ‣ The kinematic contribution to the cosmic number count dipole") and [4](https://arxiv.org/html/2503.02470v1#A1.F4 "Figure 4 ‣ Appendix A Additional combined dipole estimates ‣ The kinematic contribution to the cosmic number count dipole").

| Catalogue(s) | S0subscript𝑆0S\_{0}italic\_S start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT | N𝑁Nitalic\_N | ℳℳ\\mathcal{M}caligraphic\_M | 𝒟𝒟\\mathcal{D}caligraphic\_D | R.A. | Dec. |
|  | (mJy) |  | counts/pixel | (×10−2absentsuperscript102\\times 10^{-2}× 10 start\_POSTSUPERSCRIPT - 2 end\_POSTSUPERSCRIPT) | (deg) | (deg) |
| NVSS | 20 | 272,977 | 7.87±0.02plus-or-minus7.870.027.87\\pm 0.027.87 ± 0.02 | 1.60±0.34plus-or-minus1.600.341.60\\pm 0.341.60 ± 0.34 | 150±13plus-or-minus15013150\\pm 13150 ± 13 | −25±14plus-or-minus2514-25\\pm 14\- 25 ± 14 |
| RACS-low | 20 | 346,092 | 11.14±0.02plus-or-minus11.140.0211.14\\pm 0.0211.14 ± 0.02 | 1.68±0.27plus-or-minus1.680.271.68\\pm 0.271.68 ± 0.27 | 191±10plus-or-minus19110191\\pm 10191 ± 10 | 9±13plus-or-minus9139\\pm 139 ± 13 |
| CatWISE | 0.09 | 1,216,501 | 52.49±0.05plus-or-minus52.490.0552.49\\pm 0.0552.49 ± 0.05 | 1.56±0.19plus-or-minus1.560.191.56\\pm 0.191.56 ± 0.19 | 141±6plus-or-minus1416141\\pm 6141 ± 6 | −6±7plus-or-minus67-6\\pm 7\- 6 ± 7 |
| NVSSa | 15 | 349,439 | 10.02±0.02plus-or-minus10.020.0210.02\\pm 0.0210.02 ± 0.02 | 1.17±0.30plus-or-minus1.170.301.17\\pm 0.301.17 ± 0.30 | 149±14plus-or-minus14914149\\pm 14149 ± 14 | −9±17plus-or-minus917-9\\pm 17\- 9 ± 17 |
| RACS-lowa | 15 | 438,085 | 14.07±0.02plus-or-minus14.070.0214.07\\pm 0.0214.07 ± 0.02 | 1.25±0.24plus-or-minus1.250.241.25\\pm 0.241.25 ± 0.24 | 194±12plus-or-minus19412194\\pm 12194 ± 12 | 5±15plus-or-minus5155\\pm 155 ± 15 |
|  |  |  | β𝛽\\betaitalic\_β | 𝒟r⁢e⁢s⁢i⁢dsubscript𝒟𝑟𝑒𝑠𝑖𝑑\\mathcal{D}\_{resid}caligraphic\_D start\_POSTSUBSCRIPT italic\_r italic\_e italic\_s italic\_i italic\_d end\_POSTSUBSCRIPT |  |  |
|  |  |  | (×10−3absentsuperscript103\\times 10^{-3}× 10 start\_POSTSUPERSCRIPT - 3 end\_POSTSUPERSCRIPT) | (×10−2absentsuperscript102\\times 10^{-2}× 10 start\_POSTSUPERSCRIPT - 2 end\_POSTSUPERSCRIPT) |  |  |
| NVSS CatWISE | 15 0.078 | 1,884,811 | <1.85absent1.85<1.85< 1.85 | 0.98±0.50plus-or-minus0.980.500.98\\pm 0.500.98 ± 0.50 | 144±6plus-or-minus1446144\\pm 6144 ± 6 | −11±6plus-or-minus116-11\\pm 6\- 11 ± 6 |
| RACS-low CatWISE | 15 0.078 | 1,973,705 | 1.23−1.03+0.87subscriptsuperscript1.230.871.031.23^{+0.87}\_{-1.03}1.23 start\_POSTSUPERSCRIPT + 0.87 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT - 1.03 end\_POSTSUBSCRIPT | 0.62−0.44+0.57subscriptsuperscript0.620.570.440.62^{+0.57}\_{-0.44}0.62 start\_POSTSUPERSCRIPT + 0.57 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT - 0.44 end\_POSTSUBSCRIPT | 152±6plus-or-minus1526152\\pm 6152 ± 6 | −10±6plus-or-minus106-10\\pm 6\- 10 ± 6 |
| NVSS RACS-low CatWISE | 20 20 0.09 | 1,579,687 | <0.90absent0.90<0.90< 0.90 | 1.47−0.44+0.20superscriptsubscript1.470.440.201.47\_{-0.44}^{+0.20}1.47 start\_POSTSUBSCRIPT - 0.44 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT + 0.20 end\_POSTSUPERSCRIPT | 144±5plus-or-minus1445144\\pm 5144 ± 5 | −8±6plus-or-minus86-8\\pm 6\- 8 ± 6 |
| NVSS RACS-low CatWISEa | 15 15 0.078 | 2,032,858 | 1.06±0.93plus-or-minus1.060.931.06\\pm 0.931.06 ± 0.93 | 0.84±0.50plus-or-minus0.840.500.84\\pm 0.500.84 ± 0.50 | 145±5plus-or-minus1455145\\pm 5145 ± 5 | −9±6plus-or-minus96-9\\pm 6\- 9 ± 6 |

666a Excluded sources matched to the 2MRS catalogue at z<0.1𝑧0.1z<0.1italic\_z < 0.1.

Report issue for preceding element

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)

──────── [TRUNCATED] ────────
Showing 36,221 chars (head) + 12,485 chars (tail) of 108,358 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-fd490cc9fb.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-fd490cc9fb.md" offset=240 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
