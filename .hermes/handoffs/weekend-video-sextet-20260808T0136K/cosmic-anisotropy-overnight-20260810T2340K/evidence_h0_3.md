URL: https://arxiv.org/html/2412.14607

# Testing anisotropic Hubble expansion

Report issue for preceding element

Paula Boubel
Matthew Colless
Khaled Said
and Lister Staveley-Smith

Report issue for preceding element

###### Abstract

Report issue for preceding element

The cosmological principle asserting the large-scale uniformity of the Universe is a testable assumption of the standard cosmological model. We explore the constraints on anisotropic expansion provided by measuring directional variation in the Hubble constant, H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, derived from differential zeropoint measurements of the Tully-Fisher distance estimator. We fit various models for directional variation in H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT using the Tully-Fisher dataset from the all-sky Cosmicflows-4 catalog. The best-fit dipole variation has an amplitude of 0.063 ±plus-or-minus\\pm± 0.016 mag in the direction (ℓ,bℓ𝑏\\ell,broman\_ℓ , italic\_b) = (142 ±plus-or-minus\\pm± 30∘,52 ±plus-or-minus\\pm± 10∘). If this were due to anisotropic expansion it would imply a 3% variation in H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT (i.e. Δ⁢H0Δsubscript𝐻0\\Delta H\_{0}roman\_Δ italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 2.10 ±plus-or-minus\\pm± 0.53  km s-1 Mpc-1 if H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 70  km s-1 Mpc-1) with a significance of 3.9σ𝜎\\sigmaitalic\_σ. A model including this H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole is only weakly favored relative to a model with a constant H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT and a bulk motion of the volume sampled by Cosmicflows-4 consistent with the standard ΛΛ\\Lambdaroman\_ΛCDM cosmology. However, m simulations that the expected Tully-Fisher data from the WALLABY and DESI surveys should allow detection of a 1% H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole anisotropy at 5.8σ𝜎\\sigmaitalic\_σ confidence and distinguish it from the typical bulk flow predicted by ΛΛ\\Lambdaroman\_ΛCDM over the volume of these surveys.

Report issue for preceding element

## 1 Motivation

Report issue for preceding element

The cosmological principle, the assumed isotropy and homogeneity of the universe on sufficiently large scales, has been put under increasing scrutiny over the past decade. Detections of an anisotropic expansion rate would create tension with this fundamental assumption of the standard model of cosmology. Hints of anisotropic expansion have been found in the quasar data \[ [1](https://arxiv.org/html/2412.14607v2#bib.bib1 ""), [2](https://arxiv.org/html/2412.14607v2#bib.bib2 ""), [3](https://arxiv.org/html/2412.14607v2#bib.bib3 "")\] and Type Ia supernovae data \[ [4](https://arxiv.org/html/2412.14607v2#bib.bib4 ""), [5](https://arxiv.org/html/2412.14607v2#bib.bib5 ""), [6](https://arxiv.org/html/2412.14607v2#bib.bib6 ""), [7](https://arxiv.org/html/2412.14607v2#bib.bib7 ""), [8](https://arxiv.org/html/2412.14607v2#bib.bib8 ""), [9](https://arxiv.org/html/2412.14607v2#bib.bib9 "")\].

Report issue for preceding element

Ref. \[ [9](https://arxiv.org/html/2412.14607v2#bib.bib9 "")\] found that while the amplitude of the anisotropy is not statistically unlikely, its alignment with the CMB dipole is troubling, since these supernovae compilations have already been put in the CMB frame by construction. Ref. \[ [8](https://arxiv.org/html/2412.14607v2#bib.bib8 "")\] found that the direction of the H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole differed from that of the CMB dipole by 3σ𝜎\\sigmaitalic\_σ until a sufficiently high redshift cut was made, indicating that corrections for peculiar velocities may be extremely important in H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT determinations. Ref. \[ [7](https://arxiv.org/html/2412.14607v2#bib.bib7 "")\] found a positive H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT variation of order 1  km s-1 Mpc-1 in the direction of the CMB dipole, for both low- and high-redshift samples. Ref. \[ [6](https://arxiv.org/html/2412.14607v2#bib.bib6 "")\] also found higher values of H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT in the direction of the CMB dipole at 2–3σ𝜎\\sigmaitalic\_σ significance. Most recently, refs. \[ [4](https://arxiv.org/html/2412.14607v2#bib.bib4 ""), [10](https://arxiv.org/html/2412.14607v2#bib.bib10 ""), [5](https://arxiv.org/html/2412.14607v2#bib.bib5 "")\] examined the catalog of Pantheon+ Type Ia supernovae \[ [11](https://arxiv.org/html/2412.14607v2#bib.bib11 "")\] in the CMB frame and found a dipole anisotropy H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT of +2–4  km s-1 Mpc-1 in roughly the same direction as the CMB dipole. These studies hint at either a calibration problem or a possible misinterpretation of the CMB dipole in modern cosmology.

Report issue for preceding element

A study using galaxy scaling relations \[ [12](https://arxiv.org/html/2412.14607v2#bib.bib12 "")\] found an anisotropy with a dipolar form corresponding to a 9% spatial variation of H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT in the direction (ℓℓ\\ellroman\_ℓ,b𝑏bitalic\_b) = (280 ±plus-or-minus\\pm± 35∘,−--15 ±plus-or-minus\\pm± 20∘) or to a bulk flow of 900  km s-1. This direction refers to a _lower_ H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT value compared to the rest of the sky. Using simulations, they determined that the significance of this was greater than 5σ𝜎\\sigmaitalic\_σ. However, they stated that the effect of a H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole is inseparable from a bulk flow in their sample due to the low median redshift (z=0.1𝑧0.1z=0.1italic\_z = 0.1). Still, the large bulk flow required would be in tension with assumptions in standard ΛΛ\\Lambdaroman\_ΛCDM cosmology.

Report issue for preceding element

Subsequently, a similar analysis was performed by \[ [13](https://arxiv.org/html/2412.14607v2#bib.bib13 "")\] while searching for systematic biases that could explain the previous result. They found no systematics large enough and their results were consistent with \[ [12](https://arxiv.org/html/2412.14607v2#bib.bib12 "")\], finding a variation in the direction (ℓℓ\\ellroman\_ℓ,b𝑏bitalic\_b) = (295 ±plus-or-minus\\pm± 71∘,−--30 ±plus-or-minus\\pm± 71∘) with a significance of 3.6σ𝜎\\sigmaitalic\_σ. Both of these studies present strong evidence for an anisotropy of galaxy scaling relations, but the underlying cause could be either an anisotropic H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT or a large-scale bulk flow.

Report issue for preceding element

Theoretical frameworks for anisotropic expansions arising from arbitrary space-time metrics beyond the standard FLRW assumption have been studied. For example, \[ [14](https://arxiv.org/html/2412.14607v2#bib.bib14 "")\] presents a model-independent multipole expansion of cosmological luminosity distances. Using simulations of this physical framework, the parameter that appears in place of the FLRW Hubble parameter was found to be dominated by a quadrupole \[ [15](https://arxiv.org/html/2412.14607v2#bib.bib15 ""), [16](https://arxiv.org/html/2412.14607v2#bib.bib16 "")\]. The maximum quadrupole found by \[ [16](https://arxiv.org/html/2412.14607v2#bib.bib16 "")\] is typically 2% but can be as high as 5%, while \[ [15](https://arxiv.org/html/2412.14607v2#bib.bib15 "")\] found a quadrupole strength of 0.565% on average for 100 observers. These results depend on the smoothing scale of the simulations. Using the Pantheon+ catalog \[ [11](https://arxiv.org/html/2412.14607v2#bib.bib11 "")\] to constrain this quadrupole in the Hubble parameter, \[ [15](https://arxiv.org/html/2412.14607v2#bib.bib15 "")\] found a 1.96σ𝜎\\sigmaitalic\_σ quadrupole even with velocity corrections.

Report issue for preceding element

In this study, we will use the Tully-Fisher relation to investigate this recurring theme and discover whether it is possible to disentangle the effect of bulk flows from a true H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy. As with the Type Ia supernovae studies, but in contrast to the galaxy scaling relation studies, we define the ‘direction’ of the H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole to be that of its maximum value.

Report issue for preceding element

The advantage of probing H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy, as opposed to the isotropic value of H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, is that differential measurements are not subject to systematics in the absolute calibration of H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT. In fact, the presence of an H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy in the local Universe could have significant implications in the form of bias or additional sample variance for H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT measurements that do not account for this possibility, since when isotropy is assumed, sky coverage is not typically considered in determinations of H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT.

Report issue for preceding element

Although the use of the Tully-Fisher relation suffers from significant systematic errors in the determination of a H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT monopole \[ [17](https://arxiv.org/html/2412.14607v2#bib.bib17 "")\], its ability to detect H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT variations is limited only by the statistical precision of the Tully-Fisher zeropoint. At present we may not have the precision required to adequately constrain anisotropic Hubble expansions, but the bounty of new Tully-Fisher data in the next few years may make useful constraints possible in the near future. This study is a proof-of-concept demonstrating that differential Tully-Fisher zeropoint analysis will be a viable tool for detecting H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy with upcoming datasets.

Report issue for preceding element

In Section [2](https://arxiv.org/html/2412.14607v2#S2 "2 Data ‣ Testing anisotropic Hubble expansion") we describe the data used for this analysis; in Section [3](https://arxiv.org/html/2412.14607v2#S3 "3 Method ‣ Testing anisotropic Hubble expansion") we describe the model used to constrain the anisotropies and its integration into our Bayesian methodology; in Section [4](https://arxiv.org/html/2412.14607v2#S4 "4 Results ‣ Testing anisotropic Hubble expansion") we present the results for the anisotropies detected and their statistical significance compared to other models; in Section [5](https://arxiv.org/html/2412.14607v2#S5 "5 Simulations ‣ Testing anisotropic Hubble expansion") we investigate our ability to distinguish anisotropic H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT and bulk flows for current and future Tully-Fisher datasets; finally, in Section [6](https://arxiv.org/html/2412.14607v2#S6 "6 Conclusions ‣ Testing anisotropic Hubble expansion") we present the conclusions of this work.

Report issue for preceding element

## 2 Data

Report issue for preceding element![Refer to caption](https://arxiv.org/html/2412.14607v2/extracted/6165380/linewidth_source_sky.png)Figure 1: Sky distribution of H I sources with WISE magnitudes from the CF4 Tully-Fisher catalog. In blue, 1424 H I line-width measurements from ALFALFA \[ [18](https://arxiv.org/html/2412.14607v2#bib.bib18 "")\]; in green, 2979 non-ALFALFA H I line-width measurements from the ADHI catalog \[ [19](https://arxiv.org/html/2412.14607v2#bib.bib19 "")\]; in red, 1076 other sources from the Springob/Cornell H I catalog\[ [20](https://arxiv.org/html/2412.14607v2#bib.bib20 "")\] or the Pre Digital H I catalog in EDD.Report issue for preceding element

The Cosmicflows-4 (CF4) catalog \[ [21](https://arxiv.org/html/2412.14607v2#bib.bib21 "")\] is currently the largest full-sky catalog of galaxies with Tully-Fisher distances and peculiar velocities. It is derived from heterogeneous datasets and contains 10,737 galaxies with H I redshifts and line widths, together with optical or infrared photometry. Because the method of this paper relies on the identification of physical differences in the Tully-Fisher relationship in different regions of the sky, it is highly sensitive to systematic differences between sources of photometry or H I line widths. We therefore want the data to be as uniform as possible.

Report issue for preceding element

### 2.1 Photometry

Report issue for preceding element

Although i𝑖iitalic\_i-band optical photometry from the Sloan Digital Sky Survey\[SDSS; [22](https://arxiv.org/html/2412.14607v2#bib.bib22 "")\] is available for 7502 CF4 galaxies in the northern sky, we choose to use W⁢1𝑊1W1italic\_W 1-band infrared photometry from the all-sky Wide-field Infrared Satellite Explorer\[WISE; [23](https://arxiv.org/html/2412.14607v2#bib.bib23 "")\], available for 5479 CF4 galaxies, as a single source of photometry over the whole sky mitigates systematic variations.

Report issue for preceding element

### 2.2 H I line widths

Report issue for preceding element

In contrast to photometry, no homogeneous all-sky H I dataset exists. Cosmicflows-4H I line widths are therefore compiled from a variety of sources, which are converted to a standard quantity, Wmxcsuperscriptsubscript𝑊mx𝑐W\_{\\textrm{mx}}^{c}italic\_W start\_POSTSUBSCRIPT mx end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_c end\_POSTSUPERSCRIPT\[ [24](https://arxiv.org/html/2412.14607v2#bib.bib24 "")\]. The H I data used here are taken primarily from the All Digital H I (ADHI) catalog\[ [19](https://arxiv.org/html/2412.14607v2#bib.bib19 "")\], which is mainly composed of good quality H I line widths from the ALFALFA survey \[ [18](https://arxiv.org/html/2412.14607v2#bib.bib18 "")\]. Sources not covered by the ALFALFA survey have H I line widths from the Springob/Cornell H I catalog\[ [20](https://arxiv.org/html/2412.14607v2#bib.bib20 "")\] or the Pre Digital H I catalog on EDD111http://edd.ifa.hawaii.edu; ‘Pre Digital HI’, both containing measurements from a variety of large single-dish radio telescopes. The sky distributions of these various sources of H I line widths are shown in Figure [1](https://arxiv.org/html/2412.14607v2#S2.F1 "Figure 1 ‣ 2 Data ‣ Testing anisotropic Hubble expansion").

Report issue for preceding element

Even though the WISE data are all-sky, the 1424 sources covered by ALFALFA are all in the northern sky. If our analysis only used this single source of H I data, the sky coverage would be too limited to meaningfully probe anisotropy. We therefore use the full Cosmicflows-4H I dataset and check that there are no remaining systematic differences in H I measurements between the different sources and hemispheres. In Figure [2](https://arxiv.org/html/2412.14607v2#S2.F2 "Figure 2 ‣ 2.2 H I line widths ‣ 2 Data ‣ Testing anisotropic Hubble expansion") we compare the distributions of line widths from ALFALFA, from measurements in the northern sky, and measurements in the southern sky. The median values and standard deviations of the distributions are log⁡(Wmxc)=2.45±0.18superscriptsubscript𝑊mx𝑐plus-or-minus2.450.18\\log{W\_{\\textrm{mx}}^{c}}=2.45\\pm 0.18roman\_log ( start\_ARG italic\_W start\_POSTSUBSCRIPT mx end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_c end\_POSTSUPERSCRIPT end\_ARG ) = 2.45 ± 0.18 in the north and log⁡(Wmxc)=2.46±0.17superscriptsubscript𝑊mx𝑐plus-or-minus2.460.17\\log{W\_{\\textrm{mx}}^{c}}=2.46\\pm 0.17roman\_log ( start\_ARG italic\_W start\_POSTSUBSCRIPT mx end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_c end\_POSTSUPERSCRIPT end\_ARG ) = 2.46 ± 0.17 in the south. Comparing the northern sky with the southern sky, a two-sample Kolmogorov–Smirnov (KS) test gives us a test statistic of 0.034 with a p𝑝pitalic\_p-value of 0.077, providing no evidence the distributions differ significantly. Since it is not likely that an all-sky H I dataset will exist in the near future, there will continue to be a need to ensure that north-south H I measurement methodologies are consistent. This will remain a limitation of this analysis even with future datasets. A systematic difference as small as Δ⁢log⁡(Wmxc)=0.01Δsuperscriptsubscript𝑊mx𝑐0.01\\Delta\\log{W\_{\\textrm{mx}}^{c}}=0.01roman\_Δ roman\_log ( start\_ARG italic\_W start\_POSTSUBSCRIPT mx end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_c end\_POSTSUPERSCRIPT end\_ARG ) = 0.01 corresponds roughly to a 3% effect on H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2412.14607v2/extracted/6165380/linewidths_north_vs_south.png)Figure 2: Normalized distributions of H I velocity widths from the CF4 Tully-Fisher catalog for all sources with W⁢1𝑊1W1italic\_W 1 magnitude measurements from WISE. The distribution for sources in the northern sky are shown in green, sources in the southern sky in blue, and sources with line-width measurements from ALFALFA in orange.Report issue for preceding element

## 3 Method

Report issue for preceding element

We have developed a forward-modeling methodology for simultaneously fitting the Tully-Fisher relation and peculiar velocity field in a sample of galaxies and applied it to the CF4 Tully-Fisher data \[ [25](https://arxiv.org/html/2412.14607v2#bib.bib25 "")\] (see also \[ [26](https://arxiv.org/html/2412.14607v2#bib.bib26 "")\]). The method formulates the conditional probability of observing an apparent magnitude m𝑚mitalic\_m for a galaxy as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | P⁢(m\|w,z,α,δ,θTF,θPV)=F⁢(m)⁢exp⁡\[−(m−m′)22⁢σTF2\]∫F⁢(m)⁢exp⁡\[−(m−m′)22⁢σTF2\]⁢𝑑m𝑃conditional𝑚𝑤𝑧𝛼𝛿subscript𝜃TFsubscript𝜃PV𝐹𝑚superscript𝑚superscript𝑚′22superscriptsubscript𝜎TF2𝐹𝑚superscript𝑚superscript𝑚′22superscriptsubscript𝜎TF2differential-d𝑚P(m\\,\|\\,w,z,\\alpha,\\delta,\\theta\_{\\rm TF},\\theta\_{\\rm PV})=\\frac{F(m)\\exp\\left%<br>\[-\\frac{(m-m^{\\prime})^{2}}{2\\sigma\_{\\textrm{TF}}^{2}}\\right\]}{\\int F(m)\\exp%<br>\\left\[-\\frac{(m-m^{\\prime})^{2}}{2\\sigma\_{\\textrm{TF}}^{2}}\\right\]\\,dm}italic\_P ( italic\_m \| italic\_w , italic\_z , italic\_α , italic\_δ , italic\_θ start\_POSTSUBSCRIPT roman\_TF end\_POSTSUBSCRIPT , italic\_θ start\_POSTSUBSCRIPT roman\_PV end\_POSTSUBSCRIPT ) = divide start\_ARG italic\_F ( italic\_m ) roman\_exp \[ - divide start\_ARG ( italic\_m - italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT end\_ARG start\_ARG 2 italic\_σ start\_POSTSUBSCRIPT TF end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT end\_ARG \] end\_ARG start\_ARG ∫ italic\_F ( italic\_m ) roman\_exp \[ - divide start\_ARG ( italic\_m - italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT end\_ARG start\_ARG 2 italic\_σ start\_POSTSUBSCRIPT TF end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT end\_ARG \] italic\_d italic\_m end\_ARG |  | (3.1) |

where m′superscript𝑚′m^{\\prime}italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT is the predicted apparent magnitude as a function of the observed quantities H I velocity width w𝑤witalic\_w, redshift z𝑧zitalic\_z, and position (α𝛼\\alphaitalic\_α,δ𝛿\\deltaitalic\_δ), and the parameters of the models for the Tully-Fisher relation θTFsubscript𝜃TF\\theta\_{\\rm TF}italic\_θ start\_POSTSUBSCRIPT roman\_TF end\_POSTSUBSCRIPT and the peculiar velocity field θPVsubscript𝜃PV\\theta\_{\\rm PV}italic\_θ start\_POSTSUBSCRIPT roman\_PV end\_POSTSUBSCRIPT,

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | m′⁢(w,z,α,δ,θPV,θTF)=M′⁢(w)+25+5⁢log⁡(1+z)+5⁢log⁡dC⁢(zc′).superscript𝑚′𝑤𝑧𝛼𝛿subscript𝜃PVsubscript𝜃TFsuperscript𝑀′𝑤2551𝑧5subscript𝑑𝐶superscriptsubscript𝑧𝑐′m^{\\prime}(w,z,\\alpha,\\delta,\\theta\_{\\rm PV},\\theta\_{\\rm TF})=M^{\\prime}(w)+25%<br>+5\\log(1+z)+5\\log d\_{C}(z\_{c}^{\\prime})~{}.italic\_m start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ( italic\_w , italic\_z , italic\_α , italic\_δ , italic\_θ start\_POSTSUBSCRIPT roman\_PV end\_POSTSUBSCRIPT , italic\_θ start\_POSTSUBSCRIPT roman\_TF end\_POSTSUBSCRIPT ) = italic\_M start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ( italic\_w ) + 25 + 5 roman\_log ( start\_ARG 1 + italic\_z end\_ARG ) + 5 roman\_log italic\_d start\_POSTSUBSCRIPT italic\_C end\_POSTSUBSCRIPT ( italic\_z start\_POSTSUBSCRIPT italic\_c end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) . |  | (3.2) |

This predicted apparent magnitude is given in terms of M′⁢(w)superscript𝑀′𝑤M^{\\prime}(w)italic\_M start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ( italic\_w ), the predicted absolute magnitude from the Tully-Fisher relation model for the observed H I velocity width w≡log⁡(Wmxc)−2.5𝑤superscriptsubscript𝑊mx𝑐2.5w\\equiv\\log{W\_{\\textrm{mx}}^{c}}-2.5italic\_w ≡ roman\_log ( start\_ARG italic\_W start\_POSTSUBSCRIPT mx end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_c end\_POSTSUPERSCRIPT end\_ARG ) - 2.5, and zc′subscriptsuperscript𝑧′𝑐z^{\\prime}\_{c}italic\_z start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_c end\_POSTSUBSCRIPT, the predicted co-moving redshift from the peculiar velocity model for the observed redshift and position.

Report issue for preceding element

The zeropoint of the Tully-Fisher relation and the value of h=H0/100ℎsubscript𝐻0100h=H\_{0}/100italic\_h = italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT / 100 are directly related \[ [17](https://arxiv.org/html/2412.14607v2#bib.bib17 "")\]; specifically, a shift in 5⁢log⁡h5ℎ5\\log h5 roman\_log italic\_h corresponds to a shift in M𝑀Mitalic\_M given by

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | M⁢(w,h)=M⁢(w,h=1)+5⁢log⁡h.𝑀𝑤ℎ𝑀𝑤ℎ15ℎM(w,h)=M(w,h=1)+5\\log h~{}.italic\_M ( italic\_w , italic\_h ) = italic\_M ( italic\_w , italic\_h = 1 ) + 5 roman\_log italic\_h . |  | (3.3) |

Consequently, it is not possible to use the Tully-Fisher relation on its own to determine H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT. However, it is in principle possible to detect variations in H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT using the _differential_ Tully-Fisher relation, since changes in H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT would be reflected by shifts in the Tully-Fisher zeropoint. This application does not rely on primary distance calibrations, but it does require high confidence in the spatial uniformity of the Tully-Fisher measurements, with negligible position-related systematic errors in the data.

Report issue for preceding element

Eq. [3.3](https://arxiv.org/html/2412.14607v2#S3.E3 "In 3 Method ‣ Testing anisotropic Hubble expansion") implies that a positive shift in M⁢(w)𝑀𝑤M(w)italic\_M ( italic\_w ), i.e. shifting the Tully-Fisher relation towards fainter magnitudes, corresponds to a positive shift in hℎhitalic\_h. Intuitively, fainter predicted absolute magnitudes necessitate closer inferred distances if the apparent magnitude is held fixed, and so a larger H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT is inferred for a fixed observed redshift. As a result, a positive Tully-Fisher zeropoint anisotropy corresponds to a positive H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy.

Report issue for preceding element

This paper explores the extent to which it is possible to measure H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropies using the Tully-Fisher relation using current and future datasets.

Report issue for preceding element

We can model a direction-dependent H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT by allowing the differential Tully-Fisher zeropoint to vary across the sky. In this scenario, the Tully-Fisher model \[ [25](https://arxiv.org/html/2412.14607v2#bib.bib25 "")\] for the absolute magnitude given the velocity width, M′⁢(w)superscript𝑀′𝑤M^{\\prime}(w)italic\_M start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ( italic\_w ), would have the form

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | M={a0⁢(ℓ,b)+a1⁢w(w<0)a0⁢(ℓ,b)+a1⁢w+a2⁢w2(w≥0)𝑀casessubscript𝑎0ℓ𝑏subscript𝑎1𝑤𝑤0subscript𝑎0ℓ𝑏subscript𝑎1𝑤subscript𝑎2superscript𝑤2𝑤0M=\\begin{cases}a\_{0}(\\ell,b)+a\_{1}w&(w<0)\\\<br>a\_{0}(\\ell,b)+a\_{1}w+a\_{2}w^{2}&(w\\geq 0)\\\<br>\\end{cases}italic\_M = { start\_ROW start\_CELL italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT ( roman\_ℓ , italic\_b ) + italic\_a start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT italic\_w end\_CELL start\_CELL ( italic\_w < 0 ) end\_CELL end\_ROW start\_ROW start\_CELL italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT ( roman\_ℓ , italic\_b ) + italic\_a start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT italic\_w + italic\_a start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT italic\_w start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT end\_CELL start\_CELL ( italic\_w ≥ 0 ) end\_CELL end\_ROW |  | (3.4) |

where we have allowed a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT to be a function of position on the sky, specified by ℓℓ\\ellroman\_ℓ (Galactic longitude) and b𝑏bitalic\_b (Galactic latitude). Representing the variation on the sky in terms of a series expansion, we can fit the lowest-order spherical multipoles. The monopole and dipole terms can described using four parameters (a00subscript𝑎00a\_{00}italic\_a start\_POSTSUBSCRIPT 00 end\_POSTSUBSCRIPT, a0⁢xsubscript𝑎0𝑥a\_{0x}italic\_a start\_POSTSUBSCRIPT 0 italic\_x end\_POSTSUBSCRIPT, a0⁢ysubscript𝑎0𝑦a\_{0y}italic\_a start\_POSTSUBSCRIPT 0 italic\_y end\_POSTSUBSCRIPT, a0⁢zsubscript𝑎0𝑧a\_{0z}italic\_a start\_POSTSUBSCRIPT 0 italic\_z end\_POSTSUBSCRIPT) as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | a0⁢(ℓ,b)=a00+a0~⁢(ℓ,b)=a00+a0⁢x⁢cos⁡((b))⁢cos⁡((ℓ))−a0⁢y⁢cos⁡((b))⁢sin⁡((ℓ))+a0⁢z⁢sin⁡((b))subscript𝑎0ℓ𝑏subscript𝑎00~subscript𝑎0ℓ𝑏subscript𝑎00subscript𝑎0𝑥𝑏ℓsubscript𝑎0𝑦𝑏ℓsubscript𝑎0𝑧𝑏a\_{0}(\\ell,b)=a\_{00}+\\widetilde{a\_{0}}(\\ell,b)=a\_{00}+a\_{0x}\\cos{(b)}\\cos{(%<br>\\ell)}-a\_{0y}\\cos{(b)}\\sin{(\\ell)}+a\_{0z}\\sin{(b)}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT ( roman\_ℓ , italic\_b ) = italic\_a start\_POSTSUBSCRIPT 00 end\_POSTSUBSCRIPT + over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG ( roman\_ℓ , italic\_b ) = italic\_a start\_POSTSUBSCRIPT 00 end\_POSTSUBSCRIPT + italic\_a start\_POSTSUBSCRIPT 0 italic\_x end\_POSTSUBSCRIPT roman\_cos ( start\_ARG ( italic\_b ) end\_ARG ) roman\_cos ( start\_ARG ( roman\_ℓ ) end\_ARG ) - italic\_a start\_POSTSUBSCRIPT 0 italic\_y end\_POSTSUBSCRIPT roman\_cos ( start\_ARG ( italic\_b ) end\_ARG ) roman\_sin ( start\_ARG ( roman\_ℓ ) end\_ARG ) + italic\_a start\_POSTSUBSCRIPT 0 italic\_z end\_POSTSUBSCRIPT roman\_sin ( start\_ARG ( italic\_b ) end\_ARG ) |  | (3.5) |

where the components of the dipole (a0⁢xsubscript𝑎0𝑥a\_{0x}italic\_a start\_POSTSUBSCRIPT 0 italic\_x end\_POSTSUBSCRIPT, a0⁢ysubscript𝑎0𝑦a\_{0y}italic\_a start\_POSTSUBSCRIPT 0 italic\_y end\_POSTSUBSCRIPT, a0⁢zsubscript𝑎0𝑧a\_{0z}italic\_a start\_POSTSUBSCRIPT 0 italic\_z end\_POSTSUBSCRIPT) are represented in Cartesian coordinates in the Galactic reference frame in order to have Gaussian-distributed parameters.

Report issue for preceding element

In this work, the anisotropy model will be denoted a0~⁢(ℓ,b)~subscript𝑎0ℓ𝑏\\widetilde{a\_{0}}(\\ell,b)over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG ( roman\_ℓ , italic\_b ) and will either be truncated at the dipole term, as above, or the quadrupole term, adding 5 more free parameters. Because the redshift range of the CF4 data is very limited, there is no need to include a decay factor as a function of redshift \[ [15](https://arxiv.org/html/2412.14607v2#bib.bib15 ""), [16](https://arxiv.org/html/2412.14607v2#bib.bib16 "")\], although this may be a consideration for future studies with more extensive datasets.

Report issue for preceding element

Assuming that the intrinsic Tully-Fisher relation is the same everywhere and that there are no differences in photometric calibration between different regions of the sky, variations in a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT on the sky are due to variations in H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT (parametrized as h=H0/100ℎsubscript𝐻0100h=H\_{0}/100italic\_h = italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT / 100  km s-1 Mpc-1). The deviation of the measured Tully-Fisher zeropoint from its true value is

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | M⁢(w,h⁢(α,δ))−M⁢(w,h¯)=a0~=5⁢log⁡h⁢(α,δ)−5⁢log⁡h¯=5⁢log⁡(Δ⁢h⁢(α,δ)/h¯+1),𝑀𝑤ℎ𝛼𝛿𝑀𝑤¯ℎ~subscript𝑎05ℎ𝛼𝛿5¯ℎ5Δℎ𝛼𝛿¯ℎ1M(w,h(\\alpha,\\delta))-M(w,\\bar{h})=\\widetilde{a\_{0}}=5\\log h(\\alpha,\\delta)-5%<br>\\log\\bar{h}=5\\log(\\Delta h(\\alpha,\\delta)/\\bar{h}+1),italic\_M ( italic\_w , italic\_h ( italic\_α , italic\_δ ) ) - italic\_M ( italic\_w , over¯ start\_ARG italic\_h end\_ARG ) = over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG = 5 roman\_log italic\_h ( italic\_α , italic\_δ ) - 5 roman\_log over¯ start\_ARG italic\_h end\_ARG = 5 roman\_log ( start\_ARG roman\_Δ italic\_h ( italic\_α , italic\_δ ) / over¯ start\_ARG italic\_h end\_ARG + 1 end\_ARG ) , |  | (3.6) |

where h¯¯ℎ\\bar{h}over¯ start\_ARG italic\_h end\_ARG is the mean value of hℎhitalic\_h. This leads to

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | Δ⁢H0=H0¯⁢(10a0~/5−1),Δsubscript𝐻0¯subscript𝐻0superscript10~subscript𝑎051\\Delta H\_{0}=\\overline{H\_{0}}(10^{\\widetilde{a\_{0}}/5}-1),roman\_Δ italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = over¯ start\_ARG italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG ( 10 start\_POSTSUPERSCRIPT over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG / 5 end\_POSTSUPERSCRIPT - 1 ) , |  | (3.7) |

where we have replaced hℎhitalic\_h with H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT. Thus, differences in H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT on the sky can be directly linked to the anisotropy of the Tully-Fisher zeropoint, a0~~subscript𝑎0\\widetilde{a\_{0}}over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG.

Report issue for preceding element

In general, the Tully-Fisher parameters a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, a1subscript𝑎1a\_{1}italic\_a start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT, a2subscript𝑎2a\_{2}italic\_a start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT, ϵ0subscriptitalic-ϵ0\\epsilon\_{0}italic\_ϵ start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, and ϵ1subscriptitalic-ϵ1\\epsilon\_{1}italic\_ϵ start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT (see  \[ [25](https://arxiv.org/html/2412.14607v2#bib.bib25 "")\]) are unique to the dataset, as the Tully-Fisher relation changes depending on the photometric band. However, any real H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy should result in a consistent a0~~subscript𝑎0\\widetilde{a\_{0}}over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG across datasets. We can therefore, in principle, combine datasets to achieve greater precision on constraints for the multipole terms of a0~~subscript𝑎0\\widetilde{a\_{0}}over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG, whilst allowing the other Tully-Fisher parameters to vary. This only works if there are no spatial non-uniformities within individual photometric datasets.

Report issue for preceding element

## 4 Results

Report issue for preceding element

In this work, we use the W⁢1𝑊1W1italic\_W 1-band Tully-Fisher data from CF4 because it provides uniform all-sky photometry. We apply a lower redshift limit, requiring c⁢z>3000𝑐𝑧3000cz>3000italic\_c italic\_z > 3000  km s-1, as the large relative effects of peculiar velocities at low redshifts may have a significant impact on H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT determinations. This is the same limit as was chosen in  \[ [17](https://arxiv.org/html/2412.14607v2#bib.bib17 "")\] to produce a H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT that did not vary with redshift. Higher redshift limits reduced the size of the sample while only resulting in small changes (<1⁢σabsent1𝜎<1\\sigma< 1 italic\_σ) to the amplitude of the dipole; lower redshift limits slightly increased the significance of the dipole amplitude. Because a lower redshift limit greater than or equal to 3000  km s-1 produced consistent results, this value was chosen to preserve sample size while minimizing the effects of peculiar velocities.

Report issue for preceding element

### 4.1 H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole and quadrupole

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2412.14607v2/extracted/6165380/cf4_constraints_dipole_cart.png)Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2412.14607v2/extracted/6165380/cf4_constraints_dip_quad_sph.png)Report issue for preceding element

Figure 3: Constraints from fitting a Tully-Fisher zeropoint monopole, dipole, and quadrupole to the W⁢1𝑊1W1italic\_W 1 CF4 data. Top cornerplot: best-fit monopole a00subscript𝑎00a\_{00}italic\_a start\_POSTSUBSCRIPT 00 end\_POSTSUBSCRIPT=−--19.928±plus-or-minus\\pm±0.009 mag and dipole a0~~subscript𝑎0\\widetilde{a\_{0}}over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG = (a0⁢xsubscript𝑎0𝑥a\_{0x}italic\_a start\_POSTSUBSCRIPT 0 italic\_x end\_POSTSUBSCRIPT, a0⁢ysubscript𝑎0𝑦a\_{0y}italic\_a start\_POSTSUBSCRIPT 0 italic\_y end\_POSTSUBSCRIPT, a0⁢zsubscript𝑎0𝑧a\_{0z}italic\_a start\_POSTSUBSCRIPT 0 italic\_z end\_POSTSUBSCRIPT) = (−--0.027 ±plus-or-minus\\pm± 0.015, 0.022 ±plus-or-minus\\pm± 0.015, 0.048 ±plus-or-minus\\pm± 0.014) mag. Bottom cornerplot: dipole direction is (ℓℓ\\ellroman\_ℓ,b𝑏bitalic\_b) = (142 ±plus-or-minus\\pm± 30∘,52 ±plus-or-minus\\pm± 10∘) and amplitude is \|a0~\|dipsubscript~subscript𝑎0dip\|\\widetilde{a\_{0}}\|\_{\\textrm{dip}}\| over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG \| start\_POSTSUBSCRIPT dip end\_POSTSUBSCRIPT=0.063 ±plus-or-minus\\pm± 0.016 mag; best-fit quadrupole amplitude is \|a0~\|quadsubscript~subscript𝑎0quad\|\\widetilde{a\_{0}}\|\_{\\textrm{quad}}\| over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG \| start\_POSTSUBSCRIPT quad end\_POSTSUBSCRIPT = 0.09 ±plus-or-minus\\pm± 0.08 mag.Report issue for preceding element

Figure [3](https://arxiv.org/html/2412.14607v2#S4.F3 "Figure 3 ‣ 4.1 𝐻₀ dipole and quadrupole ‣ 4 Results ‣ Testing anisotropic Hubble expansion") shows the pairwise constraints, with contours at the 68% and 95% confidence levels, from fitting an a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT monopole, dipole, and quadrupole to the CF4 W⁢1𝑊1W1italic\_W 1-band data. The dipole is measured to have a significance of 3.9σ𝜎\\sigmaitalic\_σ. Figure [4](https://arxiv.org/html/2412.14607v2#S4.F4 "Figure 4 ‣ 4.1 𝐻₀ dipole and quadrupole ‣ 4 Results ‣ Testing anisotropic Hubble expansion") is a visualization of these a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropies on the sky, converting a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT to the corresponding Δ⁢H0Δsubscript𝐻0\\Delta H\_{0}roman\_Δ italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT assuming H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 70  km s-1 Mpc-1. The top panel of Figure [3](https://arxiv.org/html/2412.14607v2#S4.F3 "Figure 3 ‣ 4.1 𝐻₀ dipole and quadrupole ‣ 4 Results ‣ Testing anisotropic Hubble expansion") shows the fitted dipole, amplitude Δ⁢H0Δsubscript𝐻0\\Delta H\_{0}roman\_Δ italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 2.10 ±plus-or-minus\\pm± 0.53  km s-1 Mpc-1 in the direction (ℓ,bℓ𝑏\\ell,broman\_ℓ , italic\_b) = (142 ±plus-or-minus\\pm± 30∘, 52 ±plus-or-minus\\pm± 10∘). The dipole direction is not aligned with the external bulk flow fitted from the same data \[ [25](https://arxiv.org/html/2412.14607v2#bib.bib25 "")\] nor with the CMB dipole determined by Planck\[ [27](https://arxiv.org/html/2412.14607v2#bib.bib27 "")\]. The dipole minimum, however, is consistent with the direction of the largest (negative) H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy found in studies using galaxy cluster scaling relations  \[ [12](https://arxiv.org/html/2412.14607v2#bib.bib12 ""), [13](https://arxiv.org/html/2412.14607v2#bib.bib13 "")\]. This minimum occurs at the antipode, (ℓ,bℓ𝑏\\ell,broman\_ℓ , italic\_b) = (322 ±plus-or-minus\\pm± 29∘, −--52 ±plus-or-minus\\pm± 12∘).

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2412.14607v2/extracted/6165380/dipole_cf4.png)

![Refer to caption](https://arxiv.org/html/2412.14607v2/extracted/6165380/quadrupole_cf4.png)

![Refer to caption](https://arxiv.org/html/2412.14607v2/extracted/6165380/dip_quad_cf4.png)

Figure 4: Mollweide projections of anisotropies in Galactic coordinates. Top: The best-fit H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole, where the direction of its +/−-- value is shown by the red/blue crosses and the 1σ𝜎\\sigmaitalic\_σ error boundary is shown by the red/blue ellipses. The amplitude is Δ⁢H0Δsubscript𝐻0\\Delta H\_{0}roman\_Δ italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 2.10 ±plus-or-minus\\pm± 0.53  km s-1 Mpc-1 if H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 70  km s-1 Mpc-1and the direction of the maximum is (ℓ,bℓ𝑏\\ell,broman\_ℓ , italic\_b) = (142 ±plus-or-minus\\pm± 30∘, 52 ±plus-or-minus\\pm± 10∘). The gray points are the W⁢1𝑊1W1italic\_W 1-band CF4 galaxies used in this fitting. The direction of the Planck CMB dipole \[ [27](https://arxiv.org/html/2412.14607v2#bib.bib27 "")\] in the heliocentric frame is shown by the green cross. The direction of the external bulk flow from outside the 2M++ volume 𝐕extsubscript𝐕ext\\mathbf{V}\_{\\textrm{ext}}bold\_V start\_POSTSUBSCRIPT ext end\_POSTSUBSCRIPT (W⁢1𝑊1W1italic\_W 1-band fit from  \[ [25](https://arxiv.org/html/2412.14607v2#bib.bib25 "")\]) is shown by the orange cross. The purple and light blue crosses and ellipses are directions of maximum H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy measured by  \[ [12](https://arxiv.org/html/2412.14607v2#bib.bib12 ""), [13](https://arxiv.org/html/2412.14607v2#bib.bib13 "")\] using galaxy scaling relations. The green line traces out the celestial equator. Middle: Best-fit H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT quadrupole with amplitude Δ⁢H0Δsubscript𝐻0\\Delta H\_{0}roman\_Δ italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 3.0 ±plus-or-minus\\pm± 2.6  km s-1 Mpc-1 if H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 70 km s-1 Mpc-1. Bottom: Sum of best-fit dipole and quadrupole.Report issue for preceding element

We also fit a combination of a dipole and a quadrupole; the quadrupole adds 5 free parameters to the model. The direction is not fixed, as it was in previous studies \[ [4](https://arxiv.org/html/2412.14607v2#bib.bib4 ""), [15](https://arxiv.org/html/2412.14607v2#bib.bib15 "")\]. The middle panel of Figure [4](https://arxiv.org/html/2412.14607v2#S4.F4 "Figure 4 ‣ 4.1 𝐻₀ dipole and quadrupole ‣ 4 Results ‣ Testing anisotropic Hubble expansion") shows the best-fitting quadrupole (only); it has an amplitude of \|a0~\|~subscript𝑎0\|\\widetilde{a\_{0}}\|\| over~ start\_ARG italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT end\_ARG \| = 0.09 ±plus-or-minus\\pm± 0.08 mag (Δ⁢H0Δsubscript𝐻0\\Delta H\_{0}roman\_Δ italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 3.0 ±plus-or-minus\\pm± 2.6  km s-1 Mpc-1 if H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT = 70  km s-1 Mpc-1). The significance of this quadrupole term is low, only 1.1σ𝜎\\sigmaitalic\_σ. The bottom panel of the figure shows the combined best-fit dipole plus quadrupole model.

Report issue for preceding element

### 4.2 Comparison with a bulk flow model

Report issue for preceding element

The presence of a residual bulk flow in the sample could be misinterpreted as an anisotropy in a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, because galaxy peculiar velocities modify their observed redshifts and so affect the predicted absolute magnitudes. As with H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, the direction of the bulk flow is in the same direction as that of the a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole maximum. This can be understood by looking at the effect of a peculiar velocity v𝑣vitalic\_v on the inferred cosmological redshift zcsubscript𝑧𝑐z\_{c}italic\_z start\_POSTSUBSCRIPT italic\_c end\_POSTSUBSCRIPT at a fixed observed redshift z𝑧zitalic\_z:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | 1+z=(1+zc)⁢(1+v/c).1𝑧1subscript𝑧𝑐1𝑣𝑐1+z=(1+z\_{c})(1+v/c).1 + italic\_z = ( 1 + italic\_z start\_POSTSUBSCRIPT italic\_c end\_POSTSUBSCRIPT ) ( 1 + italic\_v / italic\_c ) . |  | (4.1) |

A higher, positive value for v𝑣vitalic\_v reduces zcsubscript𝑧𝑐z\_{c}italic\_z start\_POSTSUBSCRIPT italic\_c end\_POSTSUBSCRIPT, resulting in a smaller inferred distance (for fixed H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT). A closer galaxy must therefore be intrinsically fainter, since its apparent magnitude is a fixed observed quantity. Thus the Tully-Fisher zeropoint is shifted to more positive values.

Report issue for preceding element

However, a bulk flow is, in principle, distinguishable from a H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT sky variation, mainly because the effect on a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT of a bulk flow depends on a galaxy’s redshift while the effect of a H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT variation does not. As a result, a bulk flow will not create a pure spatial dipole in a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT unless the redshift is fixed. Thus, redshift coverage and sky coverage are both important to being able to distinguish between them.

Report issue for preceding element

For the currently available data, the CF4 Tully-Fisher catalog, we can fit a zeropoint dipole and quadrupole, as described in the previous sections, or we can instead fit a velocity dipole, or we can try to constrain both simultaneously. To compare the fits from these models, we can compute the Bayes factor

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | B01≡P⁢(d\|M0)P⁢(d\|M1)subscript𝐵01𝑃conditional𝑑subscript𝑀0𝑃conditional𝑑subscript𝑀1B\_{01}\\equiv\\frac{P(d\|M\_{0})}{P(d\|M\_{1})}italic\_B start\_POSTSUBSCRIPT 01 end\_POSTSUBSCRIPT ≡ divide start\_ARG italic\_P ( italic\_d \| italic\_M start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT ) end\_ARG start\_ARG italic\_P ( italic\_d \| italic\_M start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT ) end\_ARG |  | (4.2) |

where B01subscript𝐵01B\_{01}italic\_B start\_POSTSUBSCRIPT 01 end\_POSTSUBSCRIPT is the posterior odds that model M0subscript𝑀0M\_{0}italic\_M start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT is true rather than model M1subscript𝑀1M\_{1}italic\_M start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT, in light of the data d𝑑ditalic\_d and assuming equal priors for both models \[ [28](https://arxiv.org/html/2412.14607v2#bib.bib28 ""), [29](https://arxiv.org/html/2412.14607v2#bib.bib29 "")\]. Here, the number of data points n𝑛nitalic\_n is much greater than the number of parameters k𝑘kitalic\_k, so we can use the approximation

Report issue for preceding element

|     |     |     |     |

[... middle omitted — see footer ...]


Report issue for preceding element

Assuming no systematic difference in the photometric calibration in different parts of the sky, the other physical effect that may cause anisotropies in a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT is an unaccounted-for velocity dipole. This complicates our analysis because a large residual bulk flow is known to exist \[ [25](https://arxiv.org/html/2412.14607v2#bib.bib25 "")\]. While the effect of a velocity dipole on a0subscript𝑎0a\_{0}italic\_a start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT is different to that of an H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole variation, the two may be difficult to distinguish with insufficient data. In this context, sample size, sky coverage, and redshift range are all important.

Report issue for preceding element

From the CF4 data, there is only weak evidence (Bayes factor 0.99) that fitting an H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole in addition to a velocity dipole is favored over a velocity dipole only. This suggests that the existing data is insufficient to constrain an H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole, and that the apparent 3% variation of H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT on the sky could plausibly be due to a residual bulk flow. With future data, however, our simulations demonstrate that this method can become a powerful tool for the detection of H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT anisotropy.

Report issue for preceding element

To generate forecasts for the potential of future datasets, we applied this method to mocks of the expected data from the combined WALLABY and DESI Tully-Fisher surveys. These much larger new surveys significantly tighten the constraints on an H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole relative to a velocity dipole. The anticipated expansion in sample size, redshift range and sky coverage increases the Bayes factor by 25–85 times. This will suffice to detect a 1% H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole anisotropy with 5.8σ𝜎\\sigmaitalic\_σ significance, a 1.2% H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT quadrupole anisotropy with 5σ𝜎\\sigmaitalic\_σ significance, and to clearly distinguish an H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT dipole from a velocity dipole of similar amplitude.

Report issue for preceding element

## Acknowledgments

Report issue for preceding element

MMC acknowledges support from a Royal Society Wolfson Visiting Fellowship at the University of Oxford (RSWVF\\R3\\223005).
KS acknowledges support from the Australian Government through the Australian Research Council Centre of Excellence for Gravitational Wave Discovery (OzGrav) through project number CE230100016.
We acknowledge use of the following analysis packages: Astropy \[ [51](https://arxiv.org/html/2412.14607v2#bib.bib51 "")\], GetDist \[ [52](https://arxiv.org/html/2412.14607v2#bib.bib52 "")\], emcee \[ [53](https://arxiv.org/html/2412.14607v2#bib.bib53 "")\], and Matplotlib \[ [54](https://arxiv.org/html/2412.14607v2#bib.bib54 "")\].

Report issue for preceding element

## References

Report issue for preceding element

- \[1\]
C. Krishnan, R. Mohayaee, E. Colgáin, M. Sheikh-Jabbari and L. Yin, _Does Hubble tension signal a breakdown in FLRW cosmology?_, [_Classical and Quantum Gravity_ 38 (2021) 184001](https://doi.org/10.1088/1361-6382/ac1a81 "").

- \[2\]
N.J. Secrest, S. von Hausegger, M. Rameez, R. Mohayaee, S. Sarkar and J. Colin, _A test of the cosmological principle with quasars_, [_ApJL_ 908 (2021) L51](https://doi.org/10.3847/2041-8213/abdd40 "").

- \[3\]
N.J. Secrest, S. von Hausegger, M. Rameez, R. Mohayaee and S. Sarkar, _A challenge to the standard cosmological model_, [_ApJL_ 937 (2022) L31](https://doi.org/10.3847/2041-8213/ac88c0 "").

- \[4\]
A. Sah, M. Rameez, S. Sarkar and C. Tsagas, _Anisotropy in Pantheon+ supernovae_, 2024.

- \[5\]
R. Mc Conville and E. Ó Colgáin, _Anisotropic distance ladder in Pantheon+ supernovae_, [_Phys. Rev. D_ 108 (2023) 123533](https://doi.org/10.1103/PhysRevD.108.123533 "").

- \[6\]
O. Luongo, M. Muccino, E.O. Colgáin, M.M. Sheikh-Jabbari and L. Yin, _Larger H0subscript𝐻0{H}\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT values in the CMB dipole direction_, [_Phys. Rev. D_ 105 (2022) 103510](https://doi.org/10.1103/PhysRevD.105.103510 "").

- \[7\]
C. Krishnan, R. Mohayaee, E.O. Colgáin, M.M. Sheikh-Jabbari and L. Yin, _Hints of FLRW breakdown from supernovae_, [_Phys. Rev. D_ 105 (2022) 063514](https://doi.org/10.1103/PhysRevD.105.063514 "").

- \[8\]
F. Sorrenti, R. Durrer and M. Kunz, _The dipole of the Pantheon+SH0ES data_, [_JCAP_ 2023 (2023) 054](https://doi.org/10.1088/1475-7516/2023/11/054 "").

- \[9\]
Z. Zhai and W.J. Percival, _Sample variance for supernovae distance measurements and the Hubble tension_, [_Phys. Rev. D_ 106 (2022) 103527](https://doi.org/10.1103/PhysRevD.106.103527 "").

- \[10\]
Hu, J. P., Wang, Y. Y., Hu, J. and Wang, F. Y., _Testing the cosmological principle with the Pantheon+ sample and the region-fitting method_, [_A&A_ 681 (2024) A88](https://doi.org/10.1051/0004-6361/202347121 "").

- \[11\]
D. Scolnic, D. Brout, A. Carr, A.G. Riess, T.M. Davis, A. Dwomoh et al., _The Pantheon+ analysis: The full data set and light-curve release_, [_ApJ_ 938 (2022) 113](https://doi.org/10.3847/1538-4357/ac8b7a "").

- \[12\]
K. Migkas, F. Pacaud, G. Schellenberger, J. Erler, N.T. Nguyen-Dang, T.H. Reiprich et al., _Cosmological implications of the anisotropy of ten galaxy cluster scaling relations_, [_A&A_ 649 (2021) A151](https://doi.org/10.1051/0004-6361/202140296 "").

- \[13\]
Pandya, A., Migkas, K., Reiprich, T. H., Stanford, A., Pacaud, F., Schellenberger, G. et al., _Examining the local Universe isotropy with galaxy cluster velocity dispersion scaling relations_, [_A&A_ 691 (2024) A355](https://doi.org/10.1051/0004-6361/202451755 "").

- \[14\]
A. Heinesen, _Multipole decomposition of the general luminosity distance Hubble law — a new framework for observational cosmology_, [_JCAP_ 2021 (2021) 008](https://doi.org/10.1088/1475-7516/2021/05/008 "").

- \[15\]
J.A. Cowell, S. Dhawan and H.J. Macpherson, _Potential signature of a quadrupolar hubble expansion in Pantheon+ supernovae_, [_MNRAS_ 526 (2023) 1482](https://doi.org/10.1093/mnras/stad2788 "").

- \[16\]
H.J. Macpherson and A. Heinesen, _Luminosity distance and anisotropic sky-sampling at low redshifts: A numerical relativity study_, [_Phys. Rev. D_ 104 (2021)](https://doi.org/10.1103/physrevd.104.023525 "").

- \[17\]
P. Boubel, M. Colless, K. Said and L. Staveley-Smith, _An improved Tully–Fisher estimate of H0subscript𝐻0H\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT_, [_MNRAS_ 533 (2024) 1550](https://doi.org/10.1093/mnras/stae1925 "").

- \[18\]
M.P. Haynes, R. Giovanelli, B. Kent, E. Adams, T. Balonek, D. Craig et al., _The Arecibo Legacy Fast ALFA Survey: The ALFALFA extragalactic H I source catalog_, [_ApJ_ 861 (2018) 49](https://doi.org/10.3847/1538-4357/aac956 "").

- \[19\]
H.M. Courtois, R.B. Tully, J.R. Fisher, N. Bonhomme, M. Zavodny and A. Barnes, _The extragalactic distance database: All digital H I profile catalog_, [_AJ_ 138 (2009) 1938](https://doi.org/10.1088/0004-6256/138/6/1938 "").

- \[20\]
C.M. Springob, M.P. Haynes, R. Giovanelli and B.R. Kent, _A digital archive of H I 21 centimeter line spectra of optically targeted galaxies_, [_ApJS_ 160 (2005) 149](https://doi.org/10.1086/431550 "").

- \[21\]
E. Kourkchi, R.B. Tully, S. Eftekharzadeh, J. Llop, H.M. Courtois, D. Guinet et al., _Cosmicflows-4: The catalog of ∼similar-to\\sim∼10,000 Tully–Fisher distances_, [_ApJ_ 902 (2020) 145](https://doi.org/10.3847/1538-4357/abb66b "").

- \[22\]
D.G. York, J. Adelman, J. John E. Anderson, S.F. Anderson, J. Annis, N.A. Bahcall et al., _The Sloan Digital Sky Survey: Technical summary_, [_AJ_ 120 (2000) 1579](https://doi.org/10.1086/301513 "").

- \[23\]
E.L. Wright, P.R.M. Eisenhardt, A.K. Mainzer, M.E. Ressler, R.M. Cutri, T. Jarrett et al., _The Wide-field Infrared Survey Explorer (WISE): Mission description and initial on-orbit performance_, [_AJ_ 140 (2010) 1868](https://doi.org/10.1088/0004-6256/140/6/1868 "").

- \[24\]
E. Kourkchi, R.B. Tully, J.D. Neill, M. Seibert, H.M. Courtois and A. Dupuy, _Global Attenuation in Spiral Galaxies in Optical and Infrared Bands_, [_ApJ_ 884 (2019) 82](https://doi.org/10.3847/1538-4357/ab4192 "") \[ [1909.01572](https://arxiv.org/abs/1909.01572 "")\].

- \[25\]
P. Boubel, M. Colless, K. Said and L. Staveley-Smith, _Large-scale motions and growth rate from forward-modelling Tully–Fisher peculiar velocities_, [_MNRAS_ 531 (2024) 84](https://doi.org/10.1093/mnras/stae1122 "").

- \[26\]
E. Kourkchi, R.B. Tully, G. Anand, H.M. Courtois, A. Dupuy, J.D. Neill et al., _Cosmicflows-4: The calibration of optical and infrared Tully–Fisher relations_, [_ApJ_ 896 (2020) 3](https://doi.org/10.3847/1538-4357/ab901c "").

- \[27\]
N. Planck Collaboration:, Aghanim, Y. Akrami, M. Ashdown, J. Aumont, C. Baccigalupi, M. Ballardini et al., _Planck 2018 results - VI. cosmological parameters_, [_A&A_ 641 (2020) A6](https://doi.org/10.1051/0004-6361/201833910 "").

- \[28\]
R. Trotta, _Bayes in the sky: Bayesian inference and model selection in cosmology_, [_Contemporary Physics_ 49 (2008) 71](https://doi.org/10.1080/00107510802066753 "").

- \[29\]
A.R. Liddle, _Statistical methods for cosmological parameter selection and estimation_, [_Annual Review of Nuclear and Particle Science_ 59 (2009) 95](https://doi.org/10.1146/annurev.nucl.010909.083706 "").

- \[30\]
G. Schwarz, _Estimating the dimension of a model_, _The annals of statistics_ (1978) 461.

- \[31\]
R.E. Kass and A.E. Raftery, _Bayes factors_, [_Journal of the American Statistical Association_ 90 (1995) 773](https://doi.org/10.1080/01621459.1995.10476572 "").

- \[32\]
H. Jeffreys, _The theory of probability_, OUP Oxford (1998).

- \[33\]
M.V. John and J. Narlikar, _Comparison of cosmological models using Bayesian theory_, [_Phys. Rev. D_ 65 (2002) 043506](https://doi.org/10.1103/PhysRevD.65.043506 "").

- \[34\]
P.S. Drell, T.J. Loredo and I. Wasserman, _Type IA supernovae, evolution, and the cosmological constant_, [_ApJ_ 530 (2000) 593](https://doi.org/10.1086/308393 "").

- \[35\]
M.I. Scrimgeour, T. Davis, C. Blake, J.B. James, G.B. Poole, L. Staveley-Smith et al., _The wigglez dark energy survey: the transition to large-scale cosmic homogeneity_, [_MNRAS_ 425 (2012) 116](https://doi.org/10.1111/j.1365-2966.2012.21402.x "").

- \[36\]
V.J. Martinez, M.-J. Pons-Borderia, R.A. Moyeed and M.J. Graham, _Searching for the scale of homogeneity_, [_MNRAS_ 298 (1998) 1212](https://doi.org/10.1046/j.1365-8711.1998.01730.x "").

- \[37\]
D. Camarena and V. Marra, _Impact of the cosmic variance on H0subscript𝐻0{H}\_{0}italic\_H start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT on cosmological analyses_, [_Phys. Rev. D_ 98 (2018) 023537](https://doi.org/10.1103/PhysRevD.98.023537 "").

- \[38\]
Z. Zhai, W.J. Percival and Z. Ding, _Effective volume of supernovae samples and sample variance_, [_Phys. Rev. D_ 109 (2024) 063519](https://doi.org/10.1103/PhysRevD.109.063519 "").

- \[39\]
R. Wojtak, A. Knebe, W.A. Watson, I.T. Iliev, S. Heß, D. Rapetti et al., _Cosmic variance of the local hubble flow in large-scale cosmological simulations_, [_MNRAS_ 438 (2013) 1805](https://doi.org/10.1093/mnras/stt2321 "").

- \[40\]
D. Camarena, V. Marra, Z. Sakr and C. Clarkson, _A void in the hubble tension? the end of the line for the hubble bubble_, [_Classical and Quantum Gravity_ 39 (2022)](https://doi.org/10.1088/1361-6382/ac8635 "").

- \[41\]
H.-Y. Wu and D. Huterer, _Sample variance in the local measurements of the hubble constant_, [_MNRAS_ 471 (2017) 4946](https://doi.org/10.1093/mnras/stx1967 "").

- \[42\]
A.M. Whitford, C. Howlett and T.M. Davis, _Evaluating bulk flow estimators for cosmicflows–4 measurements_, [_MNRAS_ 526 (2023) 3051](https://doi.org/10.1093/mnras/stad2764 "").

- \[43\]
J. Carrick, S.J. Turnbull, G. Lavaux and M.J. Hudson, _Cosmological parameters from the comparison of peculiar velocities with predictions from the 2M++ density field_, [_MNRAS_ 450 (2015) 317](https://doi.org/10.1093/mnras/stv547 "").

- \[44\]
K.M. Górski, E. Hivon, A.J. Banday, B.D. Wandelt, F.K. Hansen, M. Reinecke et al., _HEALPix: A framework for high-resolution discretization and fast analysis of data distributed on the sphere_, [_ApJ_ 622 (2005) 759](https://doi.org/10.1086/427976 "").

- \[45\]
B.S. Koribalski, L. Staveley-Smith, T. Westmeier, P. Serra, K. Spekkens, O.I. Wong et al., _WALLABY – an SKA Pathfinder HI survey_, [_ApSS_ 365 (2020)](https://doi.org/10.1007/s10509-020-03831-4 "").

- \[46\]
T. Westmeier, N. Deg, K. Spekkens, T.N. Reynolds, A.X. Shen, S. Gaudet et al., _WALLABY pilot survey: Public release of H I data for almost 600 galaxies from phase 1 of ASKAP pilot observations_, [_PASA_ 39 (2022) e058](https://doi.org/10.1017/pasa.2022.50 "").

- \[47\]
J. Kang, M. Zhu, M. Ai, H. Yu and C. Sun, _Extragalactic H I Survey with FAST: First look at the pilot survey results_, [_Research in Astronomy and Astrophysics_ 22 (2022) 065019](https://doi.org/10.1088/1674-4527/ac6796 "").

- \[48\]
C.-P. Zhang, M. Zhu, P. Jiang, C. Cheng, J. Wang, J. Wang et al., _The FAST all sky H I survey (FASHI): The first release of catalog_, [_Science China Physics, Mechanics & Astronomy_ 67 (2023)](https://doi.org/10.1007/s11433-023-2219-7 "").

- \[49\]
H.M. Courtois, K. Said, J. Mould, T.H. Jarrett, D. Pomarède, T. Westmeier et al., _WALLABY pre-pilot and pilot survey: The Tully Fisher relation in Eridanus, Hydra, Norma, and NGC4636 fields_, [_MNRAS_ 519 (2022) 4589–4607](https://doi.org/10.1093/mnras/stac3246 "").

- \[50\]
C. Saulder, C. Howlett, K.A. Douglass, K. Said, S. BenZvi, S. Ahlen et al., _Target selection for the DESI Peculiar Velocity Survey_, [_MNRAS_ 525 (2023) 1106](https://doi.org/10.1093/mnras/stad2200 "").

- \[51\]
T.P. Robitaille, E.J. Tollerud, P. Greenfield, M. Droettboom, E. Bray, T. Aldcroft et al., _Astropy: A community python package for astronomy_, _A&A_ 558 (2013) A33.

- \[52\]
A. Lewis, _Getdist: a python package for analysing monte carlo samples_, 2019.

- \[53\]
D. Foreman-Mackey, D. Hogg, D. Lang and J. Goodman, _emcee: The MCMC hammer_, _PASP_ 125 (2013) 306.

- \[54\]
J.D. Hunter, _Matplotlib: A 2D Graphics Environment_, _Comput. Sci. Eng._ 9 (2007) 90.


Report IssueReport Issue for Selection

──────── [TRUNCATED] ────────
Showing 44,997 chars (head) + 14,745 chars (tail) of 91,789 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-5f2f471ab6.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-5f2f471ab6.md" offset=249 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
