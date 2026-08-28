URL: https://arxiv.org/html/2405.09762v2

HTML conversions [sometimes display errors](https://info.dev.arxiv.org/about/accessibility_html_error_messages.html) due to content that did not convert correctly from the source. This paper uses the following packages that are not yet supported by the HTML conversion tool. Feedback on these issues are not necessary; they are known and are being worked on.

- failed: extdash
- failed: changes

Authors: achieve the best HTML results from your LaTeX submissions by following these [best practices](https://info.arxiv.org/help/submit_latex_best_practices.html).

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2405.09762v2 \[astro-ph.CO\] 19 Jan 2025

# Reassessment of the dipole in the distribution of quasars on the sky

Report issue for preceding element

Arefe Abghari,11footnotetext: Corresponding author.Emory F. Bunn
Lukas T. Hergt
Boris Li
Douglas Scott
Raelyn M. Sullivan
Dingchen Wei

Report issue for preceding element

###### Abstract

Report issue for preceding element

We investigate recent claims by Secrest et al. of an anomalously large amplitude of the dipole in the distribution of CatWISE-selected quasars on the sky. Two main issues indicate that the systematic uncertainties in the derived quasar-density dipole are underestimated. Firstly, the spatial distribution of the quasars is not a pure dipole, possessing low-order multipoles of comparable size to the dipole. These multipoles are unexpected and presumably caused by unknown systematic effects; we cannot be confident that the dipole amplitude is not also affected by the same systematics until the origin of these fluctuations is understood. Secondly, the 50 percent sky cut associated with the quasar catalogue strongly couples the multipoles, meaning that the power estimate at ℓ=1ℓ1\\ell=1roman\_ℓ = 1 contains significant contributions from ℓ>1ℓ1\\ell>1roman\_ℓ > 1. In particular, the dominant quadrupole mode in the Galactic mask strongly couples the dipole with the octupole, leading to a large uncertainty in the dipole amplitude. Together these issues mean that the dipole in the quasar catalogue has an uncertainty large enough that consistency with the cosmic microwave background (CMB) dipole cannot be ruled out. More generally, current data sets are insufficiently clean to robustly measure the quasar dipole and future studies will require samples that are larger (preferably covering more of the sky) and free of systematic effects to make strong claims regarding their consistency with the CMB dipole.

Report issue for preceding element

## 1 Introduction

Report issue for preceding element

The cosmological principle is the assumption that, on large enough scales, the Universe is homogeneous and isotropic. One consequence of this principle is that there should be no preferred direction or location in the Universe. The cosmological principle imposes symmetries that greatly simplifies to the Friedmann–Lemaître–Robertson–Walker (FLRW) metric (for a historical discussion see, e.g., Section 2 of Peebles’ book \[ [1](https://arxiv.org/html/2405.09762v2#bib.bib1 "")\]). According to this picture, the dipole of the cosmic microwave background (CMB) is solely caused by the motion of the Earth relative to the ‘rest frame’ of the CMB, in which the sky is expected to be statistically isotropic. The temperature gradient caused by this movement is expressed as Δ⁢T/T=(v/c)⁢cos⁡θΔ𝑇𝑇𝑣𝑐𝜃\\Delta T/T=(v/c)\\cos\\thetaroman\_Δ italic\_T / italic\_T = ( italic\_v / italic\_c ) roman\_cos italic\_θ\[ [2](https://arxiv.org/html/2405.09762v2#bib.bib2 "")\], where θ𝜃\\thetaitalic\_θ is the angle from the direction of the motion. The most recent measurement of the speed of the Solar System with respect to the CMB rest frame comes from the Planck satellite and is v=369.82⁢(11)kms−1𝑣timesuncertain369.8211timeskilometersecond1v=$369.82(11)\\text{\\,}\\mathrm{km}\\text{\\,}{\\mathrm{s}}^{-1}$italic\_v = start\_ARG start\_ARG 369.82 end\_ARG start\_ARG ( 11 ) end\_ARG end\_ARG start\_ARG times end\_ARG start\_ARG start\_ARG roman\_km end\_ARG start\_ARG times end\_ARG start\_ARG power start\_ARG roman\_s end\_ARG start\_ARG - 1 end\_ARG end\_ARG end\_ARG in the direction l=264.021⁢°±0.011⁢°,b=48.253⁢°±0.005⁢°formulae-sequence𝑙plus-or-minus264.021°0.011°𝑏plus-or-minus48.253°0.005°l=$$\\pm$$,b=$$\\pm$$italic\_l = 264.021 ⁢ ° ± 0.011 ⁢ ° , italic\_b = 48.253 ⁢ ° ± 0.005 ⁢ ° in Galactic coordinates \[ [3](https://arxiv.org/html/2405.09762v2#bib.bib3 ""), [4](https://arxiv.org/html/2405.09762v2#bib.bib4 "")\]. [Figure1](https://arxiv.org/html/2405.09762v2#S1.F1 "In 1 Introduction ‣ Reassessment of the dipole in the distribution of quasars on the sky") shows a map from Planck that contains the Solar dipole; i.e., the strong ℓ=1ℓ1\\ell=1roman\_ℓ = 1 mode is very obvious. This is what a high signal-to-noise dipole looks like when it dominates over other multipoles and when the map does not require a large Galactic mask; this is in contrast to the quasar dipole that we discuss in the rest of the paper.

Report issue for preceding element

In addition to measuring the ℓ=1ℓ1\\ell=1roman\_ℓ = 1 multipole of the CMB, there are several other ways to measure our cosmic motion, including the following: aberration and anisotropy modulation effects in the CMB \[e.g. [5](https://arxiv.org/html/2405.09762v2#bib.bib5 ""), [6](https://arxiv.org/html/2405.09762v2#bib.bib6 ""), [7](https://arxiv.org/html/2405.09762v2#bib.bib7 "")\]; determining the dipole in the peculiar velocity field of distant objects \[ [8](https://arxiv.org/html/2405.09762v2#bib.bib8 ""), [9](https://arxiv.org/html/2405.09762v2#bib.bib9 "")\]; or summing the effect of large-scale structure on our local acceleration \[e.g., [10](https://arxiv.org/html/2405.09762v2#bib.bib10 "")\]. If any of these tests of our motion gave results that did not match the CMB dipole velocity, then that would point to the existence of a large-scale non-adiabatic mode \[ [11](https://arxiv.org/html/2405.09762v2#bib.bib11 ""), [12](https://arxiv.org/html/2405.09762v2#bib.bib12 ""), [13](https://arxiv.org/html/2405.09762v2#bib.bib13 "")\] or some more fundamental breakdown of physics near the Hubble scale. This motivates work comparing different observables that depend on our velocity.

Report issue for preceding element

Another way to measure our cosmological motion is to use the anisotropy of object counts or brightness using distant cosmological objects such as galaxies, quasars, or radio sources. This was first discussed by Ellis and Baldwin \[ [14](https://arxiv.org/html/2405.09762v2#bib.bib14 "")\]. The dipole anisotropy of object counts across the sky is predicted to be (to order v/c𝑣𝑐v/citalic\_v / italic\_c)

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | δ⁢N/N=\[2+x⁢(1+α)\]⁢(v/c)⁢cos⁡(θ)≡D⁢cos⁡(θ),𝛿𝑁𝑁delimited-\[\]2𝑥1𝛼𝑣𝑐𝜃𝐷𝜃\\delta N/N=\[2+x(1+\\alpha)\](v/c)\\cos(\\theta)\\equiv D\\cos(\\theta),italic\_δ italic\_N / italic\_N = \[ 2 + italic\_x ( 1 + italic\_α ) \] ( italic\_v / italic\_c ) roman\_cos ( italic\_θ ) ≡ italic\_D roman\_cos ( italic\_θ ) , |  | (1.1) |

where α𝛼\\alphaitalic\_α is the spectral index of the typical spectrum of an object (assuming that the sources have power-law spectra S∝ν−αproportional-to𝑆superscript𝜈𝛼S\\propto\\nu^{-\\alpha}italic\_S ∝ italic\_ν start\_POSTSUPERSCRIPT - italic\_α end\_POSTSUPERSCRIPT), and x𝑥xitalic\_x is the slope of the cumulative number count as a function of limiting flux density, N(>S)∝S−xproportional-toannotated𝑁absent𝑆superscript𝑆𝑥N(>S)\\propto S^{-x}italic\_N ( > italic\_S ) ∝ italic\_S start\_POSTSUPERSCRIPT - italic\_x end\_POSTSUPERSCRIPT. The amplitude of the dipole in this equation is denoted by D𝐷Ditalic\_D.

Report issue for preceding element

There is a long history of attempts to measure the dipole of distant sources at a range of wavelengths \[ [15](https://arxiv.org/html/2405.09762v2#bib.bib15 ""), [16](https://arxiv.org/html/2405.09762v2#bib.bib16 ""), [17](https://arxiv.org/html/2405.09762v2#bib.bib17 ""), [18](https://arxiv.org/html/2405.09762v2#bib.bib18 ""), [19](https://arxiv.org/html/2405.09762v2#bib.bib19 "")\]. Among the studies done using radio or quasar catalogues, some have found that the dipole amplitude and direction align with the CMB dipole \[ [20](https://arxiv.org/html/2405.09762v2#bib.bib20 ""), [21](https://arxiv.org/html/2405.09762v2#bib.bib21 ""), [22](https://arxiv.org/html/2405.09762v2#bib.bib22 ""), [23](https://arxiv.org/html/2405.09762v2#bib.bib23 ""), [24](https://arxiv.org/html/2405.09762v2#bib.bib24 ""), [25](https://arxiv.org/html/2405.09762v2#bib.bib25 ""), [26](https://arxiv.org/html/2405.09762v2#bib.bib26 ""), [27](https://arxiv.org/html/2405.09762v2#bib.bib27 "")\]. On the other hand, some studies have indicated a rough agreement with the CMB dipole direction, but have reported a higher than expected dipole amplitude \[ [28](https://arxiv.org/html/2405.09762v2#bib.bib28 ""), [29](https://arxiv.org/html/2405.09762v2#bib.bib29 ""), [30](https://arxiv.org/html/2405.09762v2#bib.bib30 ""), [31](https://arxiv.org/html/2405.09762v2#bib.bib31 ""), [32](https://arxiv.org/html/2405.09762v2#bib.bib32 ""), [33](https://arxiv.org/html/2405.09762v2#bib.bib33 ""), [34](https://arxiv.org/html/2405.09762v2#bib.bib34 "")\]. A common theme in all these studies has been the difficulty in controlling systematic effects; thus, various analysis approaches have been used in these papers.

Report issue for preceding element

In a recent study, Secrest et al. \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 ""), [36](https://arxiv.org/html/2405.09762v2#bib.bib36 "")\] used the CatWISE catalogue \[ [37](https://arxiv.org/html/2405.09762v2#bib.bib37 "")\] from the Wide-Field Infrared Survey Explorer (WISE) \[ [38](https://arxiv.org/html/2405.09762v2#bib.bib38 "")\] to estimate the dipole in the distribution of quasars. They found that the amplitude of the quasar dipole appeared to be significantly larger than that expected from the CMB dipole, with a difference estimated to be at the 4.9⁢σ4.9𝜎4.9\\,\\sigma4.9 italic\_σ level (for a normal distribution, one-sided). This has led to speculation in the literature of an unexpected contribution to the quasar dipole from large-scale structure \[ [39](https://arxiv.org/html/2405.09762v2#bib.bib39 ""), [18](https://arxiv.org/html/2405.09762v2#bib.bib18 ""), [40](https://arxiv.org/html/2405.09762v2#bib.bib40 "")\]; or for an intrinsic contribution to the CMB dipole \[ [41](https://arxiv.org/html/2405.09762v2#bib.bib41 ""), [42](https://arxiv.org/html/2405.09762v2#bib.bib42 ""), [43](https://arxiv.org/html/2405.09762v2#bib.bib43 "")\]; or even more radically that the cosmological principle might be violated \[ [44](https://arxiv.org/html/2405.09762v2#bib.bib44 ""), [45](https://arxiv.org/html/2405.09762v2#bib.bib45 ""), [46](https://arxiv.org/html/2405.09762v2#bib.bib46 "")\].

Report issue for preceding element

Several studies have explored potential sources of error in dipole estimations \[ [47](https://arxiv.org/html/2405.09762v2#bib.bib47 "")\]. As an example, Dalang et al. \[ [48](https://arxiv.org/html/2405.09762v2#bib.bib48 "")\] and Guandalin et al. \[ [49](https://arxiv.org/html/2405.09762v2#bib.bib49 "")\] specifically examined the influence of spectral index variations with redshift on the estimate of the quasar dipole.
In this paper, we investigate other sources of bias and uncertainty in the quasar dipole estimation. Specifically, we find (in [section2](https://arxiv.org/html/2405.09762v2#S2 "2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky")) that the quasar density in the sky appears to be affected by systematic effects that cause non-uniformities or anisotropies on large angular scales. The cause of these anisotropies is unknown, but since they cause fluctuations on large angular scales, one must assume that they affect the dipole, and hence comparison of the source dipole with the CMB dipole is not straightforward. Through a simple data split, we demonstrate that the data are most likely contaminated by non-quasar objects. In addition, we find (in [section3](https://arxiv.org/html/2405.09762v2#S3 "3 Masking and high-order moments ‣ Reassessment of the dipole in the distribution of quasars on the sky")) that the applied masking significantly impacts the dipole estimator used by Secrest et al \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 "")\]. Since higher-order multipoles leak into the lower-order multipoles when the map is strongly masked, this can dramatically affect the accuracy of the dipole moment estimation. We calculate the impact of higher multipoles on the dipole and assess the bias that this can introduce to this particular dipole estimator. We demonstrate that with these systematic effects in the data, the p𝑝pitalic\_p-value associated with the measurement of the aforementioned dipole magnitude will be notably reduced, approximately to the 2⁢σ2𝜎2\\,\\sigma2 italic\_σ significance level. We find (in [section4](https://arxiv.org/html/2405.09762v2#S4 "4 Estimating the quasar map power spectrum ‣ Reassessment of the dipole in the distribution of quasars on the sky")) that failure to account for masking in the analysis could lead to a biased estimation of the dipole amplitude and direction, and certainly an underestimate of the uncertainties. We attempt to estimate the quasar map dipole and its uncertainty using a correlation-function method, finding a lower value, and with a much larger uncertainty, than others have claimed using the same data. We also explore other methods for estimating the effect of the systematics mentioned and attempt to provide a more realistic error budget to the estimated dipole.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2405.09762v2/x1.png)Figure 1: All-sky CMB map from Planck with the monopole subtracted. We specifically show the Public Release 4 data \[ [50](https://arxiv.org/html/2405.09762v2#bib.bib50 "")\], employing the Commander component-separation method. A mask covering 22%times22percent22\\text{\\,}\\mathrm{\\char 37\\relax}start\_ARG 22 end\_ARG start\_ARG times end\_ARG start\_ARG % end\_ARG of the sky has been applied (fsky=78%subscript𝑓skytimes78percentf\_{\\mathrm{sky}}=$78\\text{\\,}\\mathrm{\\char 37\\relax}$italic\_f start\_POSTSUBSCRIPT roman\_sky end\_POSTSUBSCRIPT = start\_ARG 78 end\_ARG start\_ARG times end\_ARG start\_ARG % end\_ARG), which removes much less of the sky than is needed for the quasar map analysis. Even though underlying anisotropies and Galactic contamination have not been removed here, the dipole signal is much stronger than higher-order multipoles and dominates the image.
Report issue for preceding element

## 2 The quasar sample

Report issue for preceding element

### 2.1 Selecting quasars from WISE

Report issue for preceding element

CatWISE\[ [37](https://arxiv.org/html/2405.09762v2#bib.bib37 "")\] is a comprehensive catalogue of sources selected from WISE \[ [38](https://arxiv.org/html/2405.09762v2#bib.bib38 "")\] data. WISE was a space mission that conducted an all-sky survey in four infrared bands, detecting a wide range of celestial objects, dominated by stars, but also including millions of extragalactic objects. CatWISE selected sources specifically from the W1 (3.4µ⁢mtimes3.4micrometer3.4\\text{\\,}\\mathrm{\\SIUnitSymbolMicro m}start\_ARG 3.4 end\_ARG start\_ARG times end\_ARG start\_ARG roman\_µ roman\_m end\_ARG) and W2 (4.6µ⁢mtimes4.6micrometer4.6\\text{\\,}\\mathrm{\\SIUnitSymbolMicro m}start\_ARG 4.6 end\_ARG start\_ARG times end\_ARG start\_ARG roman\_µ roman\_m end\_ARG) bands of WISE.
Secrest et. al. \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 ""), [36](https://arxiv.org/html/2405.09762v2#bib.bib36 "")\] used a cut on those bands to select a sample of objects with a high probability of being quasars.

Report issue for preceding element

We have followed the selection method described by Secrest et al. \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 "")\], which involves a single CatWISE colour cut, W1−W2≥0.8W1W20.8\\mathrm{W1}-\\mathrm{W2}\\geq 0.8W1 - W2 ≥ 0.8, to obtain a sample of quasar candidates. For this sample, we found average values of α=1.26𝛼1.26\\alpha=1.26italic\_α = 1.26 and x=1.7𝑥1.7x=1.7italic\_x = 1.7. We made a correction using a Galactic extinction map to select quasars uniformly over the sky.
Nevertheless, due to the high stellar density near the Galactic plane, a 30°times30degree30\\text{\\,}\\mathrm{\\SIUnitSymbolDegree}start\_ARG 30 end\_ARG start\_ARG times end\_ARG start\_ARG ° end\_ARG cut is applied to mitigate confusion, as described in Secrest et al.\[ [36](https://arxiv.org/html/2405.09762v2#bib.bib36 "")\].
Additionally, we exclude certain nearby sources, resulting in the removal of 52.6%times52.6percent52.6\\text{\\,}\\mathrm{\\char 37\\relax}start\_ARG 52.6 end\_ARG start\_ARG times end\_ARG start\_ARG % end\_ARG of the sky. The mask can be seen in grey in [figure2](https://arxiv.org/html/2405.09762v2#S2.F2 "In 2.1 Selecting quasars from WISE ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky"). Once these steps are followed we end up with a catalogue of 1 355 35213553521\\,355\\,3521 355 352 probable quasars, matching the number selected by Secrest et al \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 "")\]. The number of quasars per unit of solid angle can then be calculated. To do so we explicitly create a map
using HEALPix222 [http://healpix.sourceforge.net](http://healpix.sourceforge.net/ "")\[ [51](https://arxiv.org/html/2405.09762v2#bib.bib51 "")\], with Nside=64subscript𝑁side64N\_{\\mathrm{side}}=64italic\_N start\_POSTSUBSCRIPT roman\_side end\_POSTSUBSCRIPT = 64. In [figure2](https://arxiv.org/html/2405.09762v2#S2.F2 "In 2.1 Selecting quasars from WISE ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky") we present areal density plots, with the left-hand panel showing the overall density, while the right-hand panel has been smoothed with a top-hat filter of area 1steradiantimes1steradian1\\text{\\,}\\mathrm{steradian}start\_ARG 1 end\_ARG start\_ARG times end\_ARG start\_ARG roman\_steradian end\_ARG and the colour scale has been set to emphasise variations relative to the average density.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2405.09762v2/x2.png)

![Refer to caption](https://arxiv.org/html/2405.09762v2/x3.png)

Figure 2: Left: density map of quasars selected from CatWISE, with the masked region shown in grey.
Right: same map smoothed with a top-hat filter of area 1steradiantimes1steradian1\\text{\\,}\\mathrm{steradian}start\_ARG 1 end\_ARG start\_ARG times end\_ARG start\_ARG roman\_steradian end\_ARG and with the colour scale chosen to show the contrast relative to the average density. The white colour represents the average of the map.
Report issue for preceding element

Looking at [figure2](https://arxiv.org/html/2405.09762v2#S2.F2 "In 2.1 Selecting quasars from WISE ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky") we note firstly that the quasar distribution on the sky is far from a pure dipole, with more complicated structure being quite apparent. The highest-density direction is _not_ opposite the lowest-density direction; moreover, the map does not show a monotonic gradient over the sky. This realisation leads to an extra correction for the quasar density in the Secrest et al. analysis \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 "")\], which we describe in more detail in the next section. This map also shows structures on smaller scales; since this structure cannot be due to our motion, then it is presumably due to a combination of Poisson fluctuations (see [section3.2](https://arxiv.org/html/2405.09762v2#S3.SS2 "3.2 Simulating mask-induced effects ‣ 3 Masking and high-order moments ‣ Reassessment of the dipole in the distribution of quasars on the sky")) in the quasar density and selection effects in the CatWISE data or the creation of the quasar catalogue. We will further investigate this below.

Report issue for preceding element

### 2.2 Ecliptic gradient

Report issue for preceding element

One important step in the data processing described by Secrest et al. \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 ""), [36](https://arxiv.org/html/2405.09762v2#bib.bib36 "")\], is the correction for a gradient in ecliptic latitude. This effectively changes the quasar magnitude cut as a function of ecliptic latitude.
We have confirmed that this gradient exists and that it is certainly significant (see the right panel of [figure3](https://arxiv.org/html/2405.09762v2#S2.F3 "In 2.2 Ecliptic gradient ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky"), which we will discuss in more detail in [section2.3](https://arxiv.org/html/2405.09762v2#S2.SS3 "2.3 Stellar contamination ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky")). Given the scanning pattern of WISE shown in [figure3](https://arxiv.org/html/2405.09762v2#S2.F3 "In 2.2 Ecliptic gradient ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky"), combined with the applied colour cut and potential source confusion, thorough simulations of all of those effects would be necessary to determine if this observed gradient is expected. For now, the origin of this gradient is unexplained, but
nevertheless, in [figure4](https://arxiv.org/html/2405.09762v2#S2.F4 "In 2.2 Ecliptic gradient ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky") we show the smoothed quasar-density map after performing this correction.

Report issue for preceding element

One other implicit choice made here (seen from [figure4](https://arxiv.org/html/2405.09762v2#S2.F4 "In 2.2 Ecliptic gradient ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky")) is that the correction for
ecliptic gradient (as carried out by Secrest et al. \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 "")\]) adds a substantial number of quasars. Before the correction the total is 1 355 35213553521\\,355\\,3521 355 352, and afterwards it is 1 424 51714245171\\,424\\,5171 424 517. Even if the ecliptic gradient were well understood, it seems unclear that adding quasars is the right way to make this correction, since it changes the monopole of the quasar-density field, complicating the interpretation of the results.Moreover, since the origin of the ecliptic gradient is unexplained, and it can affect the dipole estimate, it is unclear whether removing the gradient is the right thing to do. We tested the effect of subtracting various ecliptic gradients and found that reasonable choices can change the amplitude of the dipole by around 10 % and also shift the direction. While the ecliptic gradient does not dominate the uncertainty in the final dipole result (but see the estimates in [section4.2](https://arxiv.org/html/2405.09762v2#S4.SS2 "4.2 Applying a power spectrum estimator ‣ 4 Estimating the quasar map power spectrum ‣ Reassessment of the dipole in the distribution of quasars on the sky")), it is evidence for the presence of systematic effects (presumably caused by the quasar selection process) that are not yet understood, and would have to be fully explained before having confidence in the large-scale properties of the quasar density map.
Regardless, we apply the same ecliptic gradient correction as in Secrest et al. for all subsequent analyses.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2405.09762v2/x4.png)

![Refer to caption](https://arxiv.org/html/2405.09762v2/x5.png)

Figure 3: Left: Coverage across the whole sky in the WISE W1 band; this is a measure of the number of exposures that go into each pixel. There is considerably more coverage, and hence deeper data, in the regions around the ecliptic poles.
Right: Quasar density as a function of ecliptic latitude for faint and bright quasars. For the bright half of the quasars, the gradient is almost zero and is about 5 times smaller than for the faint half of the quasars; both of these subsamples give ecliptic gradients that are unusual compared with the gradients for randomly chosen halves of the sample, as indicated by the grey bands, representing the 68 % and 95 % confidence intervals. This suggests that the quasar data set might be contaminated by stars.
Report issue for preceding element![Refer to caption](https://arxiv.org/html/2405.09762v2/x6.png)Figure 4: Map of CatWISE quasar density _after_ the correction for ecliptic gradient. This map has been smoothed the same way as [figure2](https://arxiv.org/html/2405.09762v2#S2.F2 "In 2.1 Selecting quasars from WISE ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky"). This map looks quite different from the original map shown in [figure2](https://arxiv.org/html/2405.09762v2#S2.F2 "In 2.1 Selecting quasars from WISE ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky"). The number of quasars per pixel is higher because in the process of removing the ecliptic gradient, a number of quasars is added to the map. The white colour here represents the average of the map. There certainly appears to be a dipole in this second map, although it is also clear that there is other (higher-multipole) structure.Report issue for preceding element

### 2.3 Stellar contamination

Report issue for preceding element

The selection method described in [section2.1](https://arxiv.org/html/2405.09762v2#S2.SS1 "2.1 Selecting quasars from WISE ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky"), and the corrections to the ecliptic gradient discussed in [section2.2](https://arxiv.org/html/2405.09762v2#S2.SS2 "2.2 Ecliptic gradient ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky"), suggest that the quasar sample may be contaminated by stars. Because there is already a large mask applied to the data to remove the worst of this contamination in the Galactic plane, we should also check that outside of the Galactic plane we have a nearly uncontaminated sample.
To test whether the dipole result obtained in Secrest et al. \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 "")\] could be attributed to selection effects in constructing the quasar sample, we performed a simple test. We divided the quasar sample into two equal subsets based on their brightness in the W1 band (the cut-off magnitude between them is 15.92), and estimated the dipole, using the estimator used in the original study, for these two subsets. In order to determine how significant the bright-versus-faint split results are, we also randomly divided the data into half-size subsamples and analysed those results, which are shown in [figures3](https://arxiv.org/html/2405.09762v2#S2.F3 "In 2.2 Ecliptic gradient ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky") and [5](https://arxiv.org/html/2405.09762v2#S2.F5 "Figure 5 ‣ 2.3 Stellar contamination ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky").

Report issue for preceding element

The results for the dipole direction and amplitude are presented in [figure5](https://arxiv.org/html/2405.09762v2#S2.F5 "In 2.3 Stellar contamination ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky"). For the brighter subsample, the dipole is 9.5∘superscript9.59.5^{\\circ}9.5 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT away from the CMB dipole, while for the faint quasars, it is 44.5∘superscript44.544.5^{\\circ}44.5 start\_POSTSUPERSCRIPT ∘ end\_POSTSUPERSCRIPT away. As can be seen, the directions are significantly different from the random cuts in the data (and the size of the shift in direction between the bright and faint halves is seen in less than 1 % of random splits). Additionally, the dipole magnitude of the brighter quasars is slightly closer to the CMB dipole.
These findings suggest that a selection effect, such as stellar contamination within the quasar sample, affects the extracted dipole. We expect that the brighter quasar candidates are more likely to be quasars, with less contamination from the much larger number of faint stars. In a similar vein, we also tested different mask sizes and found that the dipole direction and amplitude changed substantially, depending on how much of the plane of the Milky Way is removed, again suggesting contamination of the quasar sample by stars.

Report issue for preceding element

Additionally, as part of the data analysis procedure, we calculated the ecliptic gradient for both sub-samples, as shown in the right panel of LABEL:{fig:CoverageEclipticGradient}. The ecliptic gradient for the bright quasars is significantly smaller than for the faint quasars and is essentially negligible. The ecliptic gradients of the bright and faint subsamples are more extreme compared to randomly-selected subsamples, further indicating that there is some problem with the large-scale properties of the quasar-candidate sample.
In [section2.2](https://arxiv.org/html/2405.09762v2#S2.SS2 "2.2 Ecliptic gradient ‣ 2 The quasar sample ‣ Reassessment of the dipole in the distribution of quasars on the sky") we discussed how the ecliptic gradient of the whole quasar sample has a surprising sign, indicating that it is a systematic effect of some sort. Checking how the ecliptic gradient changes with quasar brightness further suggests that this is caused by stellar contamination, and not related to the scanning strategy at all. Until this large-scale selection effect is better understood, we cannot be confident about any analysis of the real large-angle distribution of the quasars. In future analyses, there may be an opportunity to conduct a comprehensive examination independently on various bright and faint cuts. However, the current sample of quasar candidates is already too limited in number to support such an analysis.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2405.09762v2/x7.png)Figure 5: Dipole for the brighter and fainter halves of the quasar sample. Both the direction and the magnitude of the brighter subsample align better with the CMB dipole, compared with the fainter subsample. This suggests that the full sample is contaminated in some way.Report issue for preceding element

## 3 Masking and high-order moments

Report issue for preceding element

### 3.1 How mask-coupling can bias the dipole

Report issue for preceding element

We now turn to the second major issue with the existing quasar sample, which comes from the difficulty of estimating the dipole when a large mask is applied to the sky. For the CMB dipole estimate, the mask covers a relatively small fraction of the sky and the ℓ=1ℓ1\\ell=1roman\_ℓ = 1 mode is much larger than any other multipole. As we will see, things are much more challenging with the quasars.

Report issue for preceding element

The estimator employed by Secrest et al. \[ [35](https://arxiv.org/html/2405.09762v2#bib.bib35 ""), [36](https://arxiv.org/html/2405.09762v2#bib.bib36 "")\] in their studies is based on a linear regression method. It essentially involves finding the best-fit values for the coefficients of a monopole plus dipole template, by minimizing

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ∑p\[np−(a^00⁢Y00+a^10⁢Y10+a^11⁢Y11)\]2.subscript𝑝superscriptdelimited-\[\]subscript𝑛𝑝subscript^𝑎00subscript𝑌00subscript^𝑎10subscript𝑌10subscript^𝑎11subscript𝑌112\\sum\_{p}\\left\[n\_{p}-\\left(\\hat{a}\_{00}Y\_{00}+\\hat{a}\_{10}Y\_{10}+\\hat{a}\_{11}Y\_%<br>{11}\\right)\\right\]^{2}.∑ start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT \[ italic\_n start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT - ( over^ start\_ARG italic\_a end\_ARG start\_POSTSUBSCRIPT 00 end\_POSTSUBSCRIPT italic\_Y start\_POSTSUBSCRIPT 00 end\_POSTSUBSCRIPT + over^ start\_ARG italic\_a end\_ARG start\_POSTSUBSCRIPT 10 end\_POSTSUBSCRIPT italic\_Y start\_POSTSUBSCRIPT 10 end\_POSTSUBSCRIPT + over^ start\_ARG italic\_a end\_ARG start\_POSTSUBSCRIPT 11 end\_POSTSUBSCRIPT italic\_Y start\_POSTSUBSCRIPT 11 end\_POSTSUBSCRIPT ) \] start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT . |  | (3.1) |

Here npsubscript𝑛𝑝n\_{p}italic\_n start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT is the number of quasars in each pixel, Yℓ⁢msubscript𝑌ℓ𝑚Y\_{\\ell m}italic\_Y start\_POSTSUBSCRIPT roman\_ℓ italic\_m end\_POSTSUBSCRIPT are spherical harmonics and aℓ⁢msubscript𝑎ℓ𝑚a\_{\\ell m}italic\_a start\_POSTSUBSCRIPT roman\_ℓ italic\_m end\_POSTSUBSCRIPT are the coefficients in complex number form. Here a^^𝑎\\hat{a}over^ start\_ARG italic\_a end\_ARG denotes the fitted values and a𝑎aitalic\_a represents the true values. With the fitted values for a^ℓ⁢msubscript^𝑎ℓ𝑚\\hat{a}\_{\\ell m}over^ start\_ARG italic\_a end\_ARG start\_POSTSUBSCRIPT roman\_ℓ italic\_m end\_POSTSUBSCRIPT we can subsequently calculate the power spectrum333Note that we define Cℓsubscript𝐶ℓC\_{\\ell}italic\_C start\_POSTSUBSCRIPT roman\_ℓ end\_POSTSUBSCRIPT to be the power spectrum of a particular sky map, not an ensemble-average quantity, as is common elsewhere in the CMB literature. and the dipole magnitude according to

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | Cℓ≡12⁢ℓ+1⁢∑m\|a^ℓ⁢m\|2;subscript𝐶ℓ12ℓ1subscript𝑚superscriptsubscript^𝑎ℓ𝑚2C\_{\\ell}\\equiv\\frac{1}{2\\ell+1}\\sum\_{m}\|\\hat{a}\_{\\ell m}\|^{2};italic\_C start\_POSTSUBSCRIPT roman\_ℓ end\_POSTSUBSCRIPT ≡ divide start\_ARG 1 end\_ARG start\_ARG 2 roman\_ℓ + 1 end\_ARG ∑ start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT \| over^ start\_ARG italic\_a end\_ARG start\_POSTSUBSCRIPT roman\_ℓ italic\_m end\_POSTSUBSCRIPT \| start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT ; |  | (3.2) |

and

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | D=3⁢C1C0.𝐷3subscript𝐶1subscript𝐶0D=3\\;\\sqrt{\\dfrac{C\_{1}}{C\_{0}}}.italic\_D = 3 square-root start\_ARG divide start\_ARG italic\_C start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT end\_ARG start\_ARG italic\_C start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG end\_ARG . |  | (3.3) |

It is important to remember that D𝐷Ditalic\_D is defined relative to the average density of quasars on the sky (see [eq.1.1](https://arxiv.org/html/2405.09762v2#S1.E1 "In 1 Introduction ‣ Reassessment of the dipole in the distribution of quasars on the sky")), and hence we need to divide C1subscript𝐶1C\_{1}italic\_C start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT by the monopole in the quasar map, C0subscript𝐶0C\_{0}italic\_C start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, in order to interpret the amplitude of the dipole.

Report issue for preceding element

The method we describe above is the same as that used in the healpy444 [https://healpy.readthedocs.io](https://healpy.readthedocs.io/ "")fit\_dipole function, operating under the assumption that the map is a pure dipole plus independent Gaussian noise. However, as discussed earlier, this assumption is not valid here, since there are clearly other multipole moments in the quasar-density map.

Report issue for preceding element

In general, if a regression model fails to account for variables correlated with the existing coefficients, the estimator becomes biased. Due to the substantial masking of the sky, the orthogonality of the spherical harmonic coefficients is compromised, leading to coupling between higher multipoles and dipole coefficients, as detailed in [appendixA](https://arxiv.org/html/2405.09762v2#A1 "Appendix A Masking and multipole mixing ‣ Reassessment of the dipole in the distribution of quasars on the sky"). The coupling matrix 𝐌𝐌\\mathbf{M}bold\_M depends on the size and shape of the mask. The coupling matrix corresponding to the mask used in this study is depicted in [figure6](https://arxiv.org/html/2405.09762v2#S3.F6 "In 3.1 How mask-coupling can bias the dipole ‣ 3 Masking and high-order moments ‣ Reassessment of the dipole in the distribution of quasars on the sky"), showing a checkerboard pattern. Knowing the coupling between the coefficients one can show that the bias introduced by higher multipoles is given by

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |

[... middle omitted — see footer ...]


- \[39\]↑
K.K. Das, K. Sankharva and P. Jain, _Explaining excess dipole in NVSS data using superhorizon perturbation_, [_JCAP_ 2021 (2021) 035](https://doi.org/10.1088/1475-7516/2021/07/035 "") \[ [2101.11016](https://arxiv.org/abs/2101.11016 "")\].

- \[40\]↑
A.M. Whitford, C. Howlett and T.M. Davis, _Evaluating bulk flow estimators for cosmicflows–4 measurements_, [_Monthly Notices of the Royal Astronomical Society_ 526 (2023) 3051–3071](https://doi.org/10.1093/mnras/stad2764 "").

- \[41\]↑
A.R. King and G.F.R. Ellis, _Tilted homogeneous cosmological models_, [_Communications in Mathematical Physics_ 31 (1973) 209](https://doi.org/10.1007/BF01646266 "").

- \[42\]↑
R.A. Matzner, _On observations of the cosmic radiation background_, [_ApJ_ 241 (1980) 851](https://doi.org/10.1086/158397 "").

- \[43\]↑
E. Ebrahimian, C. Krishnan, R. Mondol and M.M. Sheikh-Jabbari, _Towards a realistic dipole cosmology: the dipole ΛΛ\\Lambdaroman\_ΛCDM model_, [_Classical and Quantum Gravity_ 41 (2024) 145007](https://doi.org/10.1088/1361-6382/ad550d "") \[ [2305.16177](https://arxiv.org/abs/2305.16177 "")\].

- \[44\]↑
A. Allahyari, E. Ebrahimian, R. Mondol and M.M. Sheikh-Jabbari, _Big Bang in Dipole Cosmology_, 7, 2023.

- \[45\]↑
C. Krishnan, R. Mondol and M.M. Sheikh-Jabbari, _A tilt instability in the cosmological principle_, [_Eur. Phys. J. C_ 83 (2023) 874](https://doi.org/10.1140/epjc/s10052-023-12048-y "") \[ [2211.08093](https://arxiv.org/abs/2211.08093 "")\].

- \[46\]↑
A. Constantin, T.R. Harvey, S. von Hausegger and A. Lukas, _Spatially homogeneous universes with late-time anisotropy_, [_Classical and Quantum Gravity_ 40 (2023) 245015](https://doi.org/10.1088/1361-6382/ad0b36 "") \[ [2212.03234](https://arxiv.org/abs/2212.03234 "")\].

- \[47\]↑
Y.-T. Cheng, T.-C. Chang and A. Lidz, _Is the Radio Source Dipole from NVSS Consistent with the CMB and ΛΛ\\Lambdaroman\_ΛCDM?_, [_arXiv e-prints_ (2023) arXiv:2309.02490](https://doi.org/10.48550/arXiv.2309.02490 "") \[ [2309.02490](https://arxiv.org/abs/2309.02490 "")\].

- \[48\]↑
C. Dalang and C. Bonvin, _On the kinematic cosmic dipole tension_, [_Mon. Not. Roy. Astron. Soc._ 512 (2022) 3895](https://doi.org/10.1093/mnras/stac726 "") \[ [2111.03616](https://arxiv.org/abs/2111.03616 "")\].

- \[49\]↑
C. Guandalin, J. Piat, C. Clarkson and R. Maartens, _Theoretical Systematics in Testing the Cosmological Principle with the Kinematic Quasar Dipole_, [_ApJ_ 953 (2023) 144](https://doi.org/10.3847/1538-4357/acdf46 "") \[ [2212.04925](https://arxiv.org/abs/2212.04925 "")\].

- \[50\]↑
Planck Collaboration Int. LVII, _Planck intermediate results. LVII. NPIPE: Joint Planck LFI and HFI data processing_, [_A&A_ 643 (2020) 42](https://doi.org/10.1051/0004-6361/202038073 "") \[ [2007.04997](https://arxiv.org/abs/2007.04997 "")\].

- \[51\]↑
K.M. Górski, E. Hivon, A.J. Banday, B.D. Wandelt, F.K. Hansen, M. Reinecke et al., _HEALPix: A Framework for High-Resolution Discretization and Fast Analysis of Data Distributed on the Sphere_, [_ApJ_ 622 (2005) 759](https://doi.org/10.1086/427976 "") \[ [astro-ph/0409513](https://arxiv.org/abs/astro-ph/0409513 "")\].

- \[52\]↑
A. Moss, D. Scott, J.P. Zibin and R. Battye, _Tilted physics: A cosmologically dipole-modulated sky_, [_Phys. Rev. D_ 84 (2011) 023014](https://doi.org/10.1103/PhysRevD.84.023014 "") \[ [1011.2990](https://arxiv.org/abs/1011.2990 "")\].

- \[53\]↑
E. Bunn, Y. Hoffman and J. Silk, _The Effects of Incomplete Sky Coverage on the Analysis of Large Angular Scale Microwave Background Anisotropy_, [_ApJ_ 425 (1994) 359](https://doi.org/10.1086/173991 "").

- \[54\]↑
Y. Hoffman and E. Ribak, _Constrained Realizations of Gaussian Fields: A Simple Algorithm_, [_ApJ_ 380 (1991) L5](https://doi.org/10.1086/186160 "").

- \[55\]↑
H.K. Eriksen, I.J. O’Dwyer, J.B. Jewell, B.D. Wandelt, D.L. Larson, K.M. Górski et al., _Power Spectrum Estimation from High-Resolution Maps by Gibbs Sampling_, [_ApJS_ 155 (2004) 227](https://doi.org/10.1086/425219 "") \[ [astro-ph/0407028](https://arxiv.org/abs/astro-ph/0407028 "")\].

- \[56\]↑
M. Tegmark, _How to measure CMB power spectra without losing information_, [_Phys. Rev. D_ 55 (1997) 5895](https://doi.org/10.1103/PhysRevD.55.5895 "") \[ [astro-ph/9611174](https://arxiv.org/abs/astro-ph/9611174 "")\].

- \[57\]↑
M. Tegmark and A. de Oliveira-Costa, _How to measure cmb polarization power spectra without losing information_, [_Physical Review D_ 64 (2001)](https://doi.org/10.1103/physrevd.64.063001 "").

- \[58\]↑
B.D. Wandelt, E. Hivon and K.M. Górski, _Cosmic microwave background anisotropy power spectrum statistics for high precision cosmology_, [_Phys. Rev. D_ 64 (2001) 083003](https://doi.org/10.1103/PhysRevD.64.083003 "") \[ [astro-ph/0008111](https://arxiv.org/abs/astro-ph/0008111 "")\].

- \[59\]↑
E. Hivon, K.M. Górski, C.B. Netterfield, B.P. Crill, S. Prunet and F. Hansen, _Master of the cosmic microwave background anisotropy power spectrum: A fast method for statistical analysis of large and complex cosmic microwave background data sets_, [_The Astrophysical Journal_ 567 (2002) 2–17](https://doi.org/10.1086/338126 "") \[ [astro-ph/0105302](https://arxiv.org/abs/astro-ph/0105302 "")\].

- \[60\]↑
I. Szapudi, S. Prunet, D. Pogosyan, A.S. Szalay and J.R. Bond, _Fast Cosmic Microwave Background Analyses via Correlation Functions_, [_ApJ_ 548 (2001) L115](https://doi.org/10.1086/319105 "").

- \[61\]↑
G. Chon, A. Challinor, S. Prunet, E. Hivon and I. Szapudi, _Fast estimation of polarization power spectra using correlation functions_, [_MNRAS_ 350 (2004) 914](https://doi.org/10.1111/j.1365-2966.2004.07737.x "") \[ [astro-ph/0303414](https://arxiv.org/abs/astro-ph/0303414 "")\].

- \[62\]↑
W. Handley, _anesthetic: nested sampling visualisation_, [_The Journal of Open Source Software_ 4 (2019) 1414](https://doi.org/10.21105/joss.01414 "").

- \[63\]↑
L. Dam, G.F. Lewis and B.J. Brewer, _Testing the Cosmological Principle with CatWISE Quasars: A Bayesian Analysis of the Number-Count Dipole_, [_arXiv e-prints_ (2022) arXiv:2212.07733](https://doi.org/10.48550/arXiv.2212.07733 "") \[ [2212.07733](https://arxiv.org/abs/2212.07733 "")\].

- \[64\]↑
A.K. Singal, _Resolution of the incongruency of dipole asymmetries within various large radio surveys - implications for the Cosmological Principle_, [_MNRAS_ 528 (2024) 5679](https://doi.org/10.1093/mnras/stae414 "") \[ [2312.12785](https://arxiv.org/abs/2312.12785 "")\].

- \[65\]↑
V. Mittal, O.T. Oayda and G.F. Lewis, _The cosmic dipole in the Quaia sample of quasars: a Bayesian analysis_, [_MNRAS_ 527 (2024) 8497](https://doi.org/10.1093/mnras/stad3706 "") \[ [2311.14938](https://arxiv.org/abs/2311.14938 "")\].

- \[66\]↑
K. Storey-Fisher, D.W. Hogg, H.-W. Rix, A.-C. Eilers, G. Fabbian, M. Blanton et al., _Quaia, the Gaia-unWISE Quasar Catalog: An All-Sky Spectroscopic Quasar Sample_, [_arXiv e-prints_ (2023) arXiv:2306.17749](https://doi.org/10.48550/arXiv.2306.17749 "") \[ [2306.17749](https://arxiv.org/abs/2306.17749 "")\].


## Appendix A Masking and multipole mixing

Report issue for preceding element

Here we investigate how masking causes leakage from other multipoles into the dipole, making dipole estimation challenging. We follow the derivation from Ref. \[ [58](https://arxiv.org/html/2405.09762v2#bib.bib58 "")\]. Decomposition into different spherical harmonic modes is a useful technique for analysing the temperature anisotropies in the CMB, or indeed any all-sky data set. A spin-zero field can be decomposed into spherical harmonic coefficients as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | T⁢(θ,ϕ)=∑ℓ,maℓ⁢m⁢Yℓ⁢m⁢(θ,ϕ).𝑇𝜃italic-ϕsubscriptℓ𝑚subscript𝑎ℓ𝑚subscript𝑌ℓ𝑚𝜃italic-ϕT(\\theta,\\phi)=\\sum\_{\\ell,m}a\_{\\ell m}Y\_{\\ell m}(\\theta,\\phi).italic\_T ( italic\_θ , italic\_ϕ ) = ∑ start\_POSTSUBSCRIPT roman\_ℓ , italic\_m end\_POSTSUBSCRIPT italic\_a start\_POSTSUBSCRIPT roman\_ℓ italic\_m end\_POSTSUBSCRIPT italic\_Y start\_POSTSUBSCRIPT roman\_ℓ italic\_m end\_POSTSUBSCRIPT ( italic\_θ , italic\_ϕ ) . |  | (A.1) |

We assume that the sky has been observed only over a region 𝒪𝒪\\mathcal{O}caligraphic\_O through the application of a mask.

Report issue for preceding element

The coefficients in the spherical harmonic expansion recovered from such an incomplete observing region are

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | a^l′⁢m′=∫𝒪𝑑Ω⁢Yl′⁢m′∗⁢(θ,ϕ)⁢T⁢(θ,ϕ)=∑l⁢mal⁢m⁢∫𝒪𝑑Ω⁢Yl′⁢m′∗⁢(θ,ϕ)⁢Yl⁢m⁢(θ,ϕ).subscript^𝑎superscript𝑙′superscript𝑚′subscript𝒪differential-dΩsuperscriptsubscript𝑌superscript𝑙′superscript𝑚′𝜃italic-ϕ𝑇𝜃italic-ϕsubscript𝑙𝑚subscript𝑎𝑙𝑚subscript𝒪differential-dΩsuperscriptsubscript𝑌superscript𝑙′superscript𝑚′𝜃italic-ϕsubscript𝑌𝑙𝑚𝜃italic-ϕ\\hat{a}\_{l^{\\prime}m^{\\prime}}=\\int\_{\\mathcal{O}}d\\Omega Y\_{l^{\\prime}m^{%<br>\\prime}}^{\*}(\\theta,\\phi)T(\\theta,\\phi)=\\sum\_{lm}a\_{lm}\\int\_{\\mathcal{O}}d%<br>\\Omega Y\_{l^{\\prime}m^{\\prime}}^{\*}(\\theta,\\phi)Y\_{lm}(\\theta,\\phi).over^ start\_ARG italic\_a end\_ARG start\_POSTSUBSCRIPT italic\_l start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT = ∫ start\_POSTSUBSCRIPT caligraphic\_O end\_POSTSUBSCRIPT italic\_d roman\_Ω italic\_Y start\_POSTSUBSCRIPT italic\_l start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT ( italic\_θ , italic\_ϕ ) italic\_T ( italic\_θ , italic\_ϕ ) = ∑ start\_POSTSUBSCRIPT italic\_l italic\_m end\_POSTSUBSCRIPT italic\_a start\_POSTSUBSCRIPT italic\_l italic\_m end\_POSTSUBSCRIPT ∫ start\_POSTSUBSCRIPT caligraphic\_O end\_POSTSUBSCRIPT italic\_d roman\_Ω italic\_Y start\_POSTSUBSCRIPT italic\_l start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT ( italic\_θ , italic\_ϕ ) italic\_Y start\_POSTSUBSCRIPT italic\_l italic\_m end\_POSTSUBSCRIPT ( italic\_θ , italic\_ϕ ) . |  | (A.2) |

The notation ∫𝒪subscript𝒪\\int\_{\\mathcal{O}}∫ start\_POSTSUBSCRIPT caligraphic\_O end\_POSTSUBSCRIPT denotes integration over the observed region. Note that the usual orthogonality property of the Yℓ⁢m⁢(θ,ϕ)subscript𝑌ℓ𝑚𝜃italic-ϕY\_{\\ell m}(\\theta,\\phi)italic\_Y start\_POSTSUBSCRIPT roman\_ℓ italic\_m end\_POSTSUBSCRIPT ( italic\_θ , italic\_ϕ ) does not hold any longer because we are not integrating over all solid angles. This becomes clearer if we define the geometric coupling matrix

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | Ml′⁢m′⁢l⁢m≡∫𝒪𝑑Ω⁢Yl′⁢m′∗⁢(θ,ϕ)⁢Yl⁢m⁢(θ,ϕ).subscript𝑀superscript𝑙′superscript𝑚′𝑙𝑚subscript𝒪differential-dΩsuperscriptsubscript𝑌superscript𝑙′superscript𝑚′𝜃italic-ϕsubscript𝑌𝑙𝑚𝜃italic-ϕM\_{l^{\\prime}m^{\\prime}lm}\\equiv\\int\_{\\mathcal{O}}d\\Omega Y\_{l^{\\prime}m^{%<br>\\prime}}^{\*}(\\theta,\\phi)Y\_{lm}(\\theta,\\phi).italic\_M start\_POSTSUBSCRIPT italic\_l start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT italic\_l italic\_m end\_POSTSUBSCRIPT ≡ ∫ start\_POSTSUBSCRIPT caligraphic\_O end\_POSTSUBSCRIPT italic\_d roman\_Ω italic\_Y start\_POSTSUBSCRIPT italic\_l start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT ( italic\_θ , italic\_ϕ ) italic\_Y start\_POSTSUBSCRIPT italic\_l italic\_m end\_POSTSUBSCRIPT ( italic\_θ , italic\_ϕ ) . |  | (A.3) |

This coupling matrix depends solely on the shape of the mask. For the mask used in this study, we have calculated and shown the matrix in [figure6](https://arxiv.org/html/2405.09762v2#S3.F6 "In 3.1 How mask-coupling can bias the dipole ‣ 3 Masking and high-order moments ‣ Reassessment of the dipole in the distribution of quasars on the sky").

Report issue for preceding element

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)

──────── [TRUNCATED] ────────
Showing 36,806 chars (head) + 12,175 chars (tail) of 95,810 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-57cf1bb655.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-57cf1bb655.md" offset=200 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
