URL: https://arxiv.org/html/2509.14997

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2509.14997v2 \[astro-ph.CO\] 17 Nov 2025

# No evidence for local H0H\_{0} anisotropy from Tully–Fisher or supernova distances

Report issue for preceding element

Richard Stiskalek1 [Report issue for preceding element](https://orcid.org/0000-0002-0986-314X "ORCID 0000-0002-0986-314X"),
Harry Desmond2 [Report issue for preceding element](https://orcid.org/0000-0003-0685-9791 "ORCID 0000-0003-0685-9791")
and Guilhem Lavaux3 [Report issue for preceding element](https://orcid.org/0000-0003-0143-8891 "ORCID 0000-0003-0143-8891")

1Astrophysics, University of Oxford, Denys Wilkinson Building, Keble Road, Oxford, OX1 3RH, UK

2Institute of Cosmology & Gravitation, University of Portsmouth, Dennis Sciama Building, Portsmouth, PO1 3FX, UK

3CNRS & Sorbonne Université, Institut d’Astrophysique de Paris (IAP), UMR 7095, 98 bis bd Arago, F-75014 Paris, France

[richard.stiskalek@physics.ox.ac.uk](mailto:richard.stiskalek@physics.ox.ac.uk "")

Report issue for preceding element

(Accepted XXX. Received YYY; in original form ZZZ)

###### Abstract

Report issue for preceding element

Claims of local (z≲0.05z\\lesssim 0.05) anisotropy in the Hubble constant have been made based on direct distance tracers such as Tully–Fisher galaxies and Type Ia supernovae. We revisit these using the CosmicFlows-4 Tully–Fisher W1 subsample, 2MTF and SFI++ Tully–Fisher catalogues, and the Pantheon+ supernova compilation (all restricted to z<0.05z<0.05), including a dipole in either the Tully–Fisher zero-point or the standardised supernova absolute magnitude. Our forward-modelling framework jointly calibrates the distance relation, marginalises over distances, and accounts for peculiar velocities using a linear-theory reconstruction. We compare the anisotropic and isotropic model using the Bayesian evidence. In the CosmicFlows-4 sample, we infer a zero-point dipole of amplitude 0.087±0.0190.087\\pm 0.019 mag, or 4.1±0.94.1\\pm 0.9 per cent when expressed as a dipole in the Hubble parameter. This is consistent with previous estimates but at higher significance: model comparison yields odds of 877:1877\\!:\\!1 in favour of including the zero-point dipole. In Pantheon+ we infer zero-point dipole amplitude of 0.049±0.0130.049\\pm 0.013 mag, or 2.3±0.62.3\\pm 0.6 per cent when expressed as a dipole in the Hubble parameter. However, by allowing for a radially varying velocity dipole, we show that the anisotropic zero-point model captures local flow features (or possibly systematics) in the data rather than an actual linearly growing effective bulk flow caused by anisotropy in the zero-point or expansion rate. Crucially, inferring a more general bulk flow curve we find results fully consistent with expectations from the standard cosmological model.

Report issue for preceding element

###### keywords:

Report issue for preceding element
large-scale structure of the universe – galaxies: distances and redshifts – cosmology: distance scale

††pubyear: 2025††pagerange: No evidence for local H0H\_{0} anisotropy from Tully–Fisher or supernova distances– [9](https://arxiv.org/html/2509.14997v2#A2.F9 "Figure 9 ‣ Appendix B CF4 TFR W1 full posterior ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances")

## 1 Introduction

Report issue for preceding element

The cosmological principle—that the Universe is isotropic and homogeneous on sufficiently large scales—plays a foundational role in modern cosmology. Combined with the assumption of General Relativity as the theory of gravity, it leads to the Friedmann–Robertson–Walker metric which underpins the concordance model of cosmology, Λ\\Lambda-cold dark matter. It is therefore crucial to test if the cosmological principle is satisfied and hence fit for the purpose of providing such a bedrock. Recent years have seen increased scrutiny of the cosmological principle, for example in the cosmic microwave background (cosmic microwave background; CMB\_anisotropy; Sravan), Type Ia supernovae (Basheer; Hu; SN\_1; SN\_2; Sah; Conville; Krishnan; Zhai; Rahman\_2022; Cowell\_2023; Sorrenti\_2025), direct distance tracers (Watkins\_2023; Boubel\_2025), galaxy clusters (Migkas\_2021; Pandya\_2024) and distant radio galaxies, quasars and gamma ray bursts (EB\_1; EB\_2; colloquium; Luongo\_2022) (for a review, see CP\_review).
Moreover, increasing attention has been directed toward defining “expansion” in metrics beyond Friedmann–Robertson–Walker to enable model-independent tests (Maartens\_2024; Kalbouneh\_2024; Kalbouneh\_2025; Sarma\_2025).
Any evidence for anisotropy must be carefully validated before violation of so fundamental a principle as the cosmological principle can be concluded.

Report issue for preceding element

One powerful test of the cosmological principle involves examining the _local_ expansion rate H0H\_{0} in different directions, which can be achieved by using direct distance tracers such as Tully–Fisher relation galaxies and Type Ia supernovae. This is doubly important as it may also be relevant for the Hubble tension, which is derived assuming isotropic expansion (Riess\_2022; cosmoverse). Without calibration through a lower rung of the distance ladder, an anisotropy in H0H\_{0} is completely degenerate with an anisotropy in the normalisation of the TFR and the absolute magnitude of supernovae. While it is therefore not possible to assess an H0H\_{0} anisotropy directly with this method, it seems implausible that a null detection of the degenerate combination would arise from compensated anisotropies in both H0H\_{0} and the normalisation of the standardising relation.

Report issue for preceding element

In this paper, we revisit claims of anisotropy in H0H\_{0} by fully forward-modelling the Tully–Fisher relation and supernova observables at z<0.05z<0.05. Our starting point is the recent study of Boubel\_2025 (hereafter Boubel\_2025), who conclude weak evidence for anisotropy in the CosmicFlows-4 W1 Tully–Fisher relation subsample using a partial forward model. Following Boubel\_2025, we adopt the first-order deviation from isotropy in spherical harmonics, namely a dipolar modulation to the degenerate combination of the Tully–Fisher relation or supernova normalisation and H0H\_{0}. Our approach jointly calibrates the distance relation, marginalizes over distances and latent parameters describing the true values of the observables, and corrects for peculiar velocities using a linear-theory reconstruction based on Carrick\_2015 (hereafter Carrick\_2015). We generalise the analysis of Boubel\_2025 to three further independent data sets to provide a more comprehensive and robust assessment of local anisotropy, namely the 2MTF and SFI++ Tully–Fisher relation catalogues and the Pantheon+ supernova compilation (restricted to z<0.05z<0.05). We also, for the first time, explicitly investigate the impact of dust extinction on the results by investigating three qualitatively different maps with different priors on the extinction coefficients. This is potentially an important systematic because extinction is anisotropic across the sky.

Report issue for preceding element

However, we caution that although we search for a cosmological principle-violating anomaly, this is done under the assumption of the Carrick\_2015 reconstruction to account for peculiar velocities, which itself assumes the cosmological principle. In principle, the Carrick\_2015 reconstruction could already contain part of a cosmological dipole, which would then be subtracted in our analysis. Nevertheless, the bulk flow in Carrick\_2015 shows no significant deviation from Λ\\Lambda-cold dark matter (see also e.g. Boruah\_2019; VF\_olympics). Thus, the results presented here should be interpreted as a dipole in H0H\_{0} that would be superimposed on the dipole already present in the Carrick\_2015 peculiar velocity field, which is not cosmological principle-violating.
Nevertheless, we also consider the total bulk flow curve from both Carrick\_2015 and a superimposed radially varying velocity dipole to test whether the resulting flow is in tension with Λ\\Lambda-cold dark matter expectations.

Report issue for preceding element

The remainder of this paper is structured as follows. In [Section˜2](https://arxiv.org/html/2509.14997v2#S2 "2 Data ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"), we describe the data sets used in our analysis, including the CosmicFlows-4 Tully–Fisher relation sample, the 2MTF sample, the SFI++ catalogue, and the Pantheon+ supernova compilation. In [Section˜3](https://arxiv.org/html/2509.14997v2#S3 "3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"), we present our methodology, including the forward-modelling framework, the peculiar velocity modelling scheme, the Bayesian evidence calculation and the mock data procedure. [Section˜4](https://arxiv.org/html/2509.14997v2#S4 "4 Results ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances") presents the results on both mock and observed data, while [Section˜5](https://arxiv.org/html/2509.14997v2#S5 "5 Discussion and Conclusion ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances") presents further comparison with Boubel\_2025, discusses the more general ramifications of our results, and concludes. Appendix [A](https://arxiv.org/html/2509.14997v2#A1 "Appendix A Flow model of S25 ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances") describes the flow model in full, and Appendix [B](https://arxiv.org/html/2509.14997v2#A2 "Appendix B CF4 TFR W1 full posterior ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances") shows the complete posterior distribution for the CosmicFlows-4 W1 Tully–Fisher relation inference.

Report issue for preceding element

All logarithms are base-10 unless otherwise stated. We use the notation 𝒩​(x;μ,σ)\\mathcal{N}(x;\\mu,\\sigma) to denote a one-dimensional normal distribution with mean μ\\mu and standard deviation σ\\sigma, evaluated at xx; in higher dimensions μ\\mu is a vector and σ\\sigma is replaced by a covariance matrix. We define h≡H0/(100​km​s−1​Mpc−1)h\\equiv H\_{0}/\\left(100~\\mathrm{km}\\,\\mathrm{s}^{-1}\\,\\mathrm{Mpc}^{-1}\\right), where H0H\_{0} is the Hubble constant.

Report issue for preceding element

## 2 Data

Report issue for preceding element

To test the hypothesis of a dipole in the zero-point calibration of redshift-independent distance indicators, or, equivalently, in the Hubble constant, we analyse multiple low-redshift catalogues. Our primary data set is the Tully–Fisher relation subsample of the CosmicFlows-4 catalogue (CosmicFlows-4; Tully\_2023), restricted to photometry in the all-sky W1 band. In addition, we consider two other all-sky Tully–Fisher relation samples: 2MTF (Masters\_2008; Hong\_2019) and the SFI++ catalogue (Springob\_2007). We also analyse the Pantheon+ compilation of Type Ia supernova (Scolnic\_2022), along with its reanalysis by Lane\_2024.

Report issue for preceding element

Since any large-scale dipole in the zero-point is degenerate with the local peculiar velocity field, we account for peculiar velocities using the linear reconstruction of Carrick\_2015. This choice, widely adopted in the literature (e.g. Boruah\_2019; Said\_2020; Carr\_2022; Boubel\_2024\_H0; Boubel\_2025), allows for direct comparison with recent studies, particularly Boubel\_2025, and facilitates consistent treatment of large-scale flows across all samples.

Report issue for preceding element

### 2.1 Tully–Fisher samples

Report issue for preceding element

Our first method for obtaining redshift-independent distance estimates is the Tully–Fisher relation (Tully–Fisher relation; Tully\_1977), which relates a spiral galaxy’s rotational velocity to its absolute magnitude MM. Given an observed apparent magnitude, this relation yields a distance modulus and thereby a peculiar velocity, since the observed redshift is a function of the distance and peculiar velocity. The linewidth parameter η\\eta is defined as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | η≡log⁡Wkm​s−1−2.5,\\eta\\equiv\\log\\frac{W}{\\mathrm{km}\\,\\mathrm{s}^{-1}}-2.5, |  | (1) |

where WW is the observed width of a galaxy’s spectral line (typically HI), serving as a proxy for its rotational velocity. Throughout, we refer to η\\eta simply as the galaxy linewidth. We adopt the following quadratic form of the Tully–Fisher relation:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | M​(η)={aTFR+bTFR​η+cTFR​η2if​η>0aTFR+bTFR​ηotherwiseM(\\eta)=\\begin{cases}a\_{\\rm TFR}+b\_{\\rm TFR}\\eta+c\_{\\rm TFR}\\eta^{2}&\\mathrm{if}~\\eta>0\\\<br>a\_{\\rm TFR}+b\_{\\rm TFR}\\eta&\\mathrm{otherwise}\\end{cases} |  | (2) |

where aTFRa\_{\\rm TFR} and bTFRb\_{\\rm TFR} are the zero-point and slope, respectively, and cTFRc\_{\\rm TFR} models the curvature of the relation for high-linewidth (i.e. high-mass) galaxies.

Report issue for preceding element

#### 2.1.1 CosmicFlows-4 TFR sample

Report issue for preceding element

We use the CosmicFlows-4 Tully–Fisher relation catalogue, a subset of the broader CosmicFlows-4 compilation (Tully\_2023), consisting of 97929792 galaxies with zCMB≲0.05z\_{\\rm CMB}\\lesssim 0.05 and no strict apparent magnitude limit (Kourkchi\_2020B; Kourkchi\_2020A). Our analysis uses photometry exclusively in the all-sky Wide-field Infrared Survey Explorer W1 band (same as Boubel\_2025), with additional selection criteria applied. We require η>−0.3\\eta>-0.3 (to eliminate dwarf and low-mass galaxies, which may follow a different Tully–Fisher relation or have a higher scatter), Galactic latitude \|b\|>7.5∘\|b\|>7.5^{\\circ} to exclude the Galactic Zone of Avoidance, and a photometric quality flag of 55 (“best”). After these cuts, the final W1 sample contains 32463246 galaxies. The highest photometric quality requirement excludes ∼\\sim13001300 galaxies from the W1 subsample, while the Galactic latitude cut removes only 44 galaxies from the final sample. The Zone of Avoidance is typically defined as \|b\|<5∘\|b\|<5^{\\circ} (e.g. Staveley-Smith\_1998), making our choice relatively conservative. In contrast, Boubel\_2025 do not apply either cut. Since the publicly released CosmicFlows-4 catalogue does not provide magnitude uncertainties, we adopt a conservative fiducial uncertainty of 0.05​mag0.05~\\mathrm{mag}, following Kourkchi\_2019. However, this uncertainty is subdominant to the intrinsic scatter in the Tully–Fisher relation, which is approximately 0.35​mag0.35~\\mathrm{mag} (see [Fig.˜2](https://arxiv.org/html/2509.14997v2#S4.F2 "In 4.1 CosmicFlows-4 TFR W1 dipole ‣ 4 Results ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances") or [Fig.˜9](https://arxiv.org/html/2509.14997v2#A2.F9 "In Appendix B CF4 TFR W1 full posterior ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances")). Moreover, unlike Boubel\_2025, who impose a lower redshift cut of c​zCMB>3000​km​s−1cz\_{\\rm CMB}>3000~\\mathrm{km}\\,\\mathrm{s}^{-1}, we do not apply a lower redshift limit in our main analysis, but discuss its impact in [Section˜5](https://arxiv.org/html/2509.14997v2#S5 "5 Discussion and Conclusion ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances").

Report issue for preceding element

#### 2.1.2 2MTF sample

Report issue for preceding element

Next, we consider the 2MASS Tully–Fisher Survey (2MTF), an all-sky sample of 2,062 spiral galaxies with Tully–Fisher relation measurements extending to redshifts of zCMB≲0.03z\_{\\mathrm{CMB}}\\lesssim 0.03(Masters\_2008; Hong\_2019). The survey is selected in the KK band with an apparent magnitude limit of K<11.25K<11.25. We use the version of the catalogue compiled by Boruah\_2019, which removes duplicates from the SFI++ sample, includes only KK-band photometry, and applies a quality cut on linewidths, retaining only galaxies with −0.1<η<0.2-0.1<\\eta<0.2. These cuts leave 12471247 galaxies.

Report issue for preceding element

#### 2.1.3 SFI++ TFR sample

Report issue for preceding element

We also consider the SFI++ catalogue, an all-sky sample comprising galaxies and groups with TFR measurements extending to redshifts of zCMB≲0.05z\_{\\mathrm{CMB}}\\lesssim 0.05(Masters\_2006; Springob\_2007). Unlike 2MTF, the survey does not impose a strict apparent magnitude limit, and photometry is provided in the II band. In this work, we use the galaxy-only version of the catalogue compiled by Boruah\_2019, who apply quality cuts to select galaxies within the 2M++ footprint, impose a lower linewidth threshold to exclude low-mass galaxies, and use an iterative procedure to reject Tully–Fisher relation outliers. While Boruah\_2019 also impose a strict upper linewidth selection to ensure linearity of the TFR, we relax this constraint and allow for Tully–Fisher relation curvature, resulting in a final sample of 20102010 galaxies.

Report issue for preceding element

### 2.2 Pantheon+ supernovae sample

Report issue for preceding element

Type Ia supernovae are widely used as standardisable candles in cosmology. The SALT2 model standardises their light curve (SALT2), yielding a standardised apparent magnitude via the Tripp formula (Tripp\_1998):

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | mstandard=mobs+𝒜​x1−ℬ​c,m\_{\\rm standard}=m\_{\\rm obs}+\\mathcal{A}x\_{1}-\\mathcal{B}c, |  | (3) |

where mobsm\_{\\rm obs} is the observed supernova apparent magnitude, x1x\_{1} characterises the light curve stretch, and cc the colour. The global parameters 𝒜\\mathcal{A} and ℬ\\mathcal{B} quantify the standardisation with respect to stretch and colour, respectively. Combined with the absolute magnitude MSNM\_{\\rm SN}, the standardised magnitude mstandardm\_{\\rm standard} defines the distance modulus.

Report issue for preceding element

The Pantheon+ data set is a compilation of 17011701 spectroscopically confirmed Type Ia supernovae spanning redshifts from z∼0.001z\\sim 0.001 to ∼2.3\\sim 2.3(Scolnic\_2022; Brout\_2022; Peterson\_2022; Carr\_2022). For consistency with our peculiar velocity modelling and to match the redshift range of the CosmicFlows-4 sample, we restrict the data to zCMB≤0.05z\_{\\rm CMB}\\leq 0.05, yielding a subset of 525525 supernovae. Pantheon+ combines the original Pantheon sample (Scolnic\_2018) with updated low- and high-redshift supernovae, incorporating improved photometric calibration, light-curve standardisation, and systematic uncertainty modelling. Distance moduli are derived using the SALT2 light-curve fitter and corrected for selection effects via the BEAMS with Bias Corrections (BBC) method (Kessler\_2017), which introduces an additive bias correction term in [Eq.˜3](https://arxiv.org/html/2509.14997v2#S2.E3 "In 2.2 Pantheon+ supernovae sample ‣ 2 Data ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"). We use such bias-corrected apparent magnitudes mcorrm\_{\\rm corr} from the Pantheon+ sample, which include a fiducial Tripp calibration. We therefore sample only MSNM\_{\\rm SN}, not the light curve stretch and colour coefficients of the Tripp calibration.

Report issue for preceding element

Uncertainties in the distance moduli (or equivalently, bias-corrected apparent magnitude), including both statistical and systematic contributions, are encoded in a covariance matrix that incorporates uncertainty in the Tripp parameters 𝒜\\mathcal{A} and ℬ\\mathcal{B}, held fixed at fiducial values. The Pantheon+ data release therefore provides a set of standardised, bias-corrected apparent magnitudes and an associated covariance matrix, with the only global parameter varied in our analysis being MSNM\_{\\rm SN}, which is inferred jointly with the flow model.

Report issue for preceding element

#### 2.2.1 Lane et al. reanalysis

Report issue for preceding element

A reanalysis of the Pantheon+ data was presented by Lane\_2024, who constructed a supernova covariance matrix designed to minimise dependence on the assumed cosmology and peculiar velocities. Unlike the standard Pantheon+ covariance matrix and bias-corrected apparent magnitudes, which assume a fiducial cosmology and Tripp parameters, the Lane\_2024 covariance matrix does not include any contribution from the Tripp parametrisation. This enables simultaneous inference of the Tripp coefficients, with the standardised apparent magnitudes expressed as in [Eq.˜3](https://arxiv.org/html/2509.14997v2#S2.E3 "In 2.2 Pantheon+ supernovae sample ‣ 2 Data ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"), and no further bias corrections. We treat this as a variant of the Pantheon+ data, denoted “Pantheon+Lane” henceforth.

Report issue for preceding element

### 2.3 Peculiar velocity data

Report issue for preceding element

In Carrick\_2015, the luminosity-weighted density field is reconstructed from the redshift-space positions of galaxies in the 2M++ catalogue using the iterative method of Yahil\_1991. 2M++ is a whole-sky redshift compilation of 6916069160 galaxies (Lavaux\_2011), derived from 2MASS photometry (Skrutskie\_2006) and redshifts from 2MRS (Huchra\_2012), 6dF (Jones\_2009), and Sloan Digital Sky Survey DR7 (Abazajian\_2009). Apparent magnitudes are corrected for Galactic extinction, kk-corrections, evolution, and surface brightness dimming. The catalogue is magnitude-limited to K<11.5K<11.5 in the 2MRS region and K<12.5K<12.5 in the 6dF and Sloan Digital Sky Survey regions.

Report issue for preceding element

The velocity field is derived from the galaxy density field using linear theory and must be scaled to match peculiar velocities via a parameter β⋆\\beta^{\\star}, which we treat as a free parameter of the model. The field is generated on a 2563256^{3} grid with a box size of 400​h−1​Mpc400~h^{-1}\\,\\mathrm{Mpc}, assuming Ωm=0.3\\Omega\_{\\rm m}=0.3. β⋆\\beta^{\\star} is defined as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | β⋆≡f​σ8,NLσ8b,\\beta^{\\star}\\equiv\\frac{f\\sigma\_{8,\\mathrm{NL}}}{\\sigma\_{8}^{b}}, |  | (4) |

where ff is the dimensionless growth rate, with f≈Ωm0.55f\\approx\\Omega\_{\\mathrm{m}}^{0.55} in Λ\\LambdaCDM (Bouchet\_1995; Wang\_1998). The terms σ8b\\sigma\_{8}^{b} and σ8,NL\\sigma\_{8,\\mathrm{NL}} represent the fluctuation amplitude in the biased galaxy field and in the non-linear matter field, respectively. The value of σ8g\\sigma\_{8}^{g} in 2M++ was measured as 0.98±0.070.98\\pm 0.07(westover) and 0.99±0.040.99\\pm 0.04(Carrick\_2015). Carrick\_2015, combined with peculiar velocity samples, has been extensively used to constrain the growth of structure and the S8S\_{8} parameter (e.g. Boruah\_2019; Said\_2020; Boubel\_2024; VF\_olympics).

Report issue for preceding element

## 3 Methodology

Report issue for preceding element

We adopt a forward modelling framework, predicting the observables from the model parameters and comparing them to the observed values through a likelihood function. This has the advantage that it exploits all the information in the data (as no summary statistics are used), and makes it straightforward to model systematics and other effects that impact the observed quantities. It also lends itself naturally to a Bayesian inference by determining the probability distributions of the parameters implied by the observational data.

Report issue for preceding element

In particular our method jointly calibrates the Tully–Fisher relation relation (or supernovae) with the galaxy bias and the peculiar velocity field, following the methodology developed in VF\_olympics. While Boubel\_2025 also largely adopts a forward-modelling approach, one key step does not fall within that framework: by querying peculiar velocity in redshift space, they use the observed redshift to assign peculiar velocity to a galaxy, approximately updating the fiducial velocity field calibration of Carrick\_2015, and then use that to estimate the cosmological redshift. That is a backward-modelling step (going from the redshift observation to a model parameter, the cosmological redshift or analogously distance) that introduces complications in triple-valued zones where a single observed redshift can map to multiple line-of-sight distances (StraussWillick\_1995). We instead model the observed redshift directly by querying the peculiar velocity field in real space. Here, we provide a brief summary of the model; a more detailed explanation is given in [Appendix˜A](https://arxiv.org/html/2509.14997v2#A1 "Appendix A Flow model of S25 ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"), with further discussion in VF\_olympics.

Report issue for preceding element

### 3.1 Tully–Fisher model

Report issue for preceding element

Each galaxy is described by its observed redshift, apparent magnitude, and linewidth, with which we infer the distance. The velocity field is modelled as a combination of a reconstructed internal flow, scaled by a parameter β⋆\\beta^{\\star}, and an external flow 𝑽ext\\bm{V}\_{\\rm ext}. In the absence of a velocity field model, the flow reduces to a constant 𝑽ext\\bm{V}\_{\\rm ext} term. We also include a Gaussian dispersion parameter σv\\sigma\_{v} to account for small-scale velocities not captured by the reconstruction.

Report issue for preceding element

The distances and true linewidths of each galaxy are latent model parameters over which we marginalise. The true linewidths are drawn from an inferred Gaussian distribution (MNR) and compared to the observations through a likelihood function. Via the Tully–Fisher relation, the true linewidths determine the absolute magnitudes, which, combined with the distances, yield predictions of the apparent magnitudes to be compared with the data. Likewise, the true model distances, together with the peculiar velocity model, provide predictions of the observed redshifts for comparison with the measurements. The forward model accounts for both homogeneous and inhomogeneous Malmquist bias. The homogeneous case is an assumption that sources are uniformly distributed in volume, yielding a distance prior p​(r)∝r2p(r)\\propto r^{2} in the absence of selection effects. The inhomogeneous Malmquist bias is set by the density field of Carrick\_2015 and modelled as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | n​(r)=1+b1​δ​(r),n(r)=1+b\_{1}\\delta(r), |  | (5) |

where δ​(r)\\delta(r) is the density contrast at the galaxy’s position. To ensure non-negative values, n​(r)n(r) is clipped from below at zero. We adopt this linear bias model to be consistent with the reconstruction of Carrick\_2015, which uses linear theory to relate the galaxy density field, effectively smoothed over scales of 4​h−1​Mpc4~h^{-1}\\,\\mathrm{Mpc}, to a peculiar velocity field. We treat b1b\_{1} as a model parameter and infer it with a wide uniform prior.

Report issue for preceding element

In general, Tully–Fisher relation samples are subject to a complex selection function combining HI flux, linewidth, optical magnitude, and possibly redshift selection. Following the empirical approach of Lavaux\_Virbius, we model the prior distribution of galaxy distances as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | π​(r∣𝜽)=n​(r,𝜽)​f​(r,𝜽)∫dr′​n​(r′,𝜽)​f​(r′,𝜽),\\pi(r\\mid\\bm{\\theta})=\\frac{n(r,\\,\\bm{\\theta})\\,f(r,\\,\\bm{\\theta})}{\\int\\mathrm{d}r^{\\prime}\\,n(r^{\\prime},\\,\\bm{\\theta})\\,f(r^{\\prime},\\,\\bm{\\theta})}, |  | (6) |

where n​(r,𝜽)n(r,\\,\\bm{\\theta}) accounts for the inhomogeneous Malmquist bias through the large-scale density field, 𝜽\\bm{\\theta} collectively denotes the model parameters, and

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | f​(r,𝜽)=rp​exp⁡\[−(rR)q\].f(r,\\,\\bm{\\theta})=r^{p}\\exp\\!\\left\[-\\left(\\frac{r}{R}\\right)^{q}\\right\]. |  | (7) |

Here pp, qq, and RR are free parameters: p≈2p\\approx 2 recovers the homogeneous Malmquist bias, RR sets the characteristic scale of sample incompleteness, and qq controls how sharply the completeness falls off. The normalisation in [Eq.˜6](https://arxiv.org/html/2509.14997v2#S3.E6 "In 3.1 Tully–Fisher model ‣ 3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances") is computed explicitly since it depends on 𝜽\\bm{\\theta}. This treatment remains phenomenological, approximating the selection rather than modelling it directly. A rigorous forward modelling of the survey selection, which requires knowledge of the selection function, is presented in Kelly\_2008 and we recently applied it to H0H\_{0} inference in CH0.

Report issue for preceding element

We extend the Tully–Fisher relation zero-point aTFRa\_{\\rm TFR} by introducing a dipole, such that

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | aTFR→aTFR+𝚫ZP⋅𝒓^,a\_{\\rm TFR}\\rightarrow a\_{\\rm TFR}+\\bm{\\Delta}\_{\\mathrm{ZP}}\\cdot\\hat{\\bm{r}}, |  | (8) |

where 𝚫ZP\\bm{\\Delta}\_{\\mathrm{ZP}} is the zero-point dipole vector and 𝒓^\\hat{\\bm{r}} is the unit vector in the direction of each galaxy. The dipole amplitude is denoted ΔZP\\Delta\_{\\rm ZP}, with direction specified in Galactic coordinates as (ℓΔZP,bΔZP)(\\ell\_{\\Delta\_{\\rm ZP}},\\,b\_{\\Delta\_{\\rm ZP}}). The zero-point aTFRa\_{\\rm TFR} is perfectly degenerate with the Hubble constant H0H\_{0}, since the distance modulus depends on the logarithm of the luminosity distance. This leads to a degenerate parameter combination aTFR+5​log⁡ha\_{\\rm TFR}+5\\log h, where h≡H0/(100​km​s−1​Mpc−1)h\\equiv H\_{0}/(100~\\mathrm{km}\\,\\mathrm{s}^{-1}\\,\\mathrm{Mpc}^{-1}). Following VF\_olympics and similar works, we express distances in units of h−1​Mpch^{-1}\\,\\mathrm{Mpc}, rendering the analysis independent of hh and constraining only the degenerate combination.

Report issue for preceding element

As explored by Boubel\_2025, one may allow for a dipole in this degenerate parameter across the sky. Provided sufficient sky coverage, such a dipole can be constrained. This introduces four possible interpretations:

Report issue for preceding element

1. 1.


An anisotropic zero-point with isotropic H0H\_{0};

Report issue for preceding element

2. 2.


An isotropic zero-point with an anisotropic H0H\_{0};

Report issue for preceding element

3. 3.


A combination of both aforementioned effects;

Report issue for preceding element

4. 4.


Spurious H0H\_{0} anisotropy arising from flows not captured by Carrick\_2015.

Report issue for preceding element


Boubel\_2025 found no evidence for significant spatial variation in linewidths within the CosmicFlows-4 W1 subsample, by comparing the linewidth distribution of sources in the northern and southern hemispheres of the ALFALFA survey (Haynes\_2018). Moreover, the use of WISE photometry minimises systematic variation in magnitude calibration across the sky. Based on these considerations, they interpreted their measured dipole in aTFR+5​log⁡ha\_{\\rm TFR}+5\\log h as a potential signature of anisotropy in H0H\_{0}. Assuming the dipole in aTFR+5​log⁡ha\_{\\rm TFR}+5\\log h arises from a dipole in H0H\_{0}, the corresponding fractional variation in the Hubble constant is given by

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | Δ​H0/H0=10ΔZP/5−1,\\Delta H\_{0}/H\_{0}=10^{\\Delta\_{\\rm ZP}/5}-1, |  | (9) |

where ΔZP\\Delta\_{\\rm ZP} is the magnitude of the dipole in the degenerate combination aTFR+5​log⁡ha\_{\\rm TFR}+5\\log h and H0H\_{0} is the monopole term of the Hubble constant.

Report issue for preceding element

As a second extension, we introduce a radial dependence of 𝑽ext\\bm{V}\_{\\rm ext} to test for potential signatures of H0H\_{0} anisotropy. We uniformly sample the magnitude and sky direction of 𝑽ext\\bm{V}\_{\\rm ext} at NknotsN\_{\\rm knots} radial distance knots (set to 0, 20, 40, 60, 800,\\,20,\\,40,\\,60,\\,80 and 100​h−1​Mpc100~h^{-1}\\,\\mathrm{Mpc} for CosmicFlows-4), and apply cubic interpolation of its Cartesian components to evaluate 𝑽ext\\bm{V}\_{\\rm ext} at each galaxy position. This procedure allows for a smoothly varying 𝑽ext\\bm{V}\_{\\rm ext}. Since a dipole in H0H\_{0} would imply a linearly increasing 𝑽ext\\bm{V}\_{\\rm ext} with distance, this extension serves as a consistency check of the inferred 𝚫ZP\\bm{\\Delta}\_{\\rm ZP} dipole. It also lets us infer the radial dependence of the bulk flow more generally.

Report issue for preceding element

### 3.2 Pantheon+ supernova model

Report issue for preceding element

To model the Pantheon+ data, we adopt an approach analogous to that used for the Tully–Fisher relation, with the primary difference being that the predicted apparent magnitude is a function of the supernova properties. The Pantheon+ sample accounts for both statistical and systematic uncertainties, encapsulated in a covariance matrix for the apparent magnitudes. These uncertainties arise from the Tripp standardisation, photometric calibration, and the heterogeneity of the contributing surveys. While the full covariance matrix provided in the Pantheon+ release includes contributions from peculiar velocities, our model accounts for these explicitly. We therefore use a reduced version of the covariance matrix with the peculiar velocity terms removed, as provided to us by Anthony Carr (private communication).

Report issue for preceding element

As before, galaxy distances are sampled from the prior of [Eq.˜6](https://arxiv.org/html/2509.14997v2#S3.E6 "In 3.1 Tully–Fisher model ‣ 3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"). These are converted to distance moduli μ\\mu, which combined with MSNM\_{\\rm SN} give the predicted apparent magnitudes as mpred=μ+MSNm\_{\\rm pred}=\\mu+M\_{\\rm SN} (the Tripp parameters are calibrated to fiducial values in the Pantheon+ sample). The likelihood is then evaluated against the standardised, bias-corrected magnitudes,

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒ​(𝒎corr∣𝒎pred)=𝒩​(𝒎corr;𝒎pred,𝐂),\\mathcal{L}(\\bm{m}\_{\\rm corr}\\mid\\bm{m}\_{\\rm pred})=\\mathcal{N}(\\bm{m}\_{\\rm corr};\\bm{m}\_{\\rm pred},\\,\\mathbf{C}), |  | (10) |

where 𝒎corr\\bm{m}\_{\\rm corr} is a vector of the standardised, bias-corrected apparent magnitudes, 𝒎pred\\bm{m}\_{\\rm pred} is a vector of predicted apparent magnitudes, and 𝐂\\mathbf{C} is the reduced Pantheon+ covariance matrix. After this, the rest of the inference follows the same steps as the Tully–Fisher relation analysis. Similarly as for the Tully–Fisher relation, we extend the standardised supernova absolute magnitude to include a dipole term:

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | MSN→MSN+𝚫ZP⋅𝒓^.M\_{\\rm SN}\\rightarrow M\_{\\rm SN}+\\bm{\\Delta}\_{\\rm ZP}\\cdot\\hat{\\bm{r}}. |  | (11) |

On the other hand, when using the covariance matrix of Pantheon+ supernovae from Lane\_2024, we explicitly sample the Tripp parameters 𝒜\\mathcal{A} and ℬ\\mathcal{B} to predict the supernova apparent magnitude (see Eq. [3](https://arxiv.org/html/2509.14997v2#S2.E3 "Equation 3 ‣ 2.2 Pantheon+ supernovae sample ‣ 2 Data ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances")), since their data does not assume a fiducial Tripp standardisation or its contribution to the covariance matrix. We evaluate the likelihood in the apparent magnitudes as in Eq. 5 of Seifert\_2025, except that we explicitly sample the galaxy distances, rather than setting them deterministically from the observed redshift which is equivalent to assuming no redshift uncertainty and no peculiar velocities.

Report issue for preceding element

### 3.3 Galactic extinction

Report issue for preceding element

A potential systematic effect in inferring the dipole in the zero-point, or equivalently in the apparent magnitude, arises from the treatment of Galactic extinction. We test this on the CosmicFlows-4 subsample, for which the applied Galactic extinction corrections are available in the public data release. The reported magnitudes in a given waveband λ\\lambda are given by (see Section 2.4 of Kourkchi\_2019):

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | m¯λ=mtotalλ−Abλ−Akλ−Aaλ,\\overline{m}^{\\lambda}=m\_{\\rm total}^{\\lambda}-A\_{b}^{\\lambda}-A\_{k}^{\\lambda}-A\_{a}^{\\lambda}, |  | (12) |

where mtotalλm\_{\\rm total}^{\\lambda} is the measured total magnitude, AbλA\_{b}^{\\lambda} is the Milky Way extinction, computed as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | Abλ=Rλ​E​(B−V),A\_{b}^{\\lambda}=R\_{\\lambda}~E(B\\!-\\!V), |  | (13) |

AkλA\_{k}^{\\lambda} is the kk-correction, AaλA\_{a}^{\\lambda} is the total flux aperture correction, and E​(B−V)E(B\\!-\\!V) is the colour excess (reddening). As described by Kourkchi\_2019, the CosmicFlows-4 catalogue uses the Schlegel\_1998100​μ​m100~\\mu\\mathrm{m} cirrus maps to extract the Milky Way E​(B−V)E(B\\!-\\!V) values. For wavebands λ∈(u,g,r,i)\\lambda\\in(u,g,r,i), the extinction coefficients RλR\_{\\lambda} are taken from Schlafly\_2011, while for the infrared bands, RW1=0.186R\_{\\rm W1}=0.186 and RW2=0.123R\_{\\rm W2}=0.123, as determined by Fitzpatrick\_1999.

Report issue for preceding element

To assess potential systematics from Galactic extinction corrections, we use the dustmaps package111 [https://dustmaps.readthedocs.io/en/latest/](https://dustmaps.readthedocs.io/en/latest/ "")(dustmaps) to extract E​(B−V)E(B\\!-\\!V) values at the angular positions of CosmicFlows-4 galaxies. We adopt the extinction maps of Chiang\_2023 and Planck\_2016. The former is a dust reddening map on the plane of the sky, derived from a reanalysis of Schlafly\_2011, which in turn is based on Schlegel\_1998. It uses tomographically constrained templates from Wide-field Infrared Survey Explorer galaxy density fields to remove contamination from the cosmic infrared background (CIB). The latter map, from Planck\_2016, employs the generalized needlet internal linear combination (GNILC) method to separate Galactic dust emission from CIB anisotropies, yielding an alternative all-sky extinction estimate. We consider these approaches for modelling Galactic extinction:

Report issue for preceding element

- •


Use the E​(B−V)E(B\\!-\\!V) values from Schlegel\_1998, jointly sampling the extinction coefficient RW1R\_{\\rm W1}. We adopt a Gaussian prior on RW1R\_{\\rm W1} centred at 0.19, with either a standard deviation of 0.01, consistent with the measurement of Yuan\_2013, or a broader, more conservative prior with standard deviation 0.05.

Report issue for preceding element

- •


Use the E​(B−V)E(B\\!-\\!V) values from Chiang\_2023 or Planck\_2016, also jointly sampling RW1R\_{\\rm W1} under the same prior choices as above.

Report issue for preceding element


The other Tully–Fisher relation samples, 2MTF and SFI++, are compiled in the optical and hence may be more susceptible to dust extinction. We cannot test this explicitly as the dust corrections they used are not publicly available, but note that the very small effect between different dust models found for CF4 suggests that the effect still would not be significant. Similarly, we do not consider Galactic extinction variations in the Pantheon+ samples.

Report issue for preceding element

### 3.4 Mock data generation

Report issue for preceding element

We use mock data to estimate the sample size required for a CosmicFlows-4-like survey to yield a significant detection of a dipole of given strength. The mock catalogue is designed to replicate the CosmicFlows-4 Tully–Fisher relation subsample with W1 photometry and full-sky coverage, excluding the Galactic Zone of Avoidance. The injected parameter values, listed in [Table˜1](https://arxiv.org/html/2509.14997v2#S3.T1 "In 3.5 Inference procedure ‣ 3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"), correspond to the posterior mean from the CosmicFlows-4 inference.

Report issue for preceding element

For NN sources, we draw sky positions uniformly over the sphere, excluding a mock “Zone of Avoidance” defined by \|b\|<7.5∘\|b\|<7.5^{\\circ}. Each line of sight is then used to query the Carrick\_2015 field for the density and peculiar velocity. The radial distance rr is sampled from the prior in [Eq.˜6](https://arxiv.org/html/2509.14997v2#S3.E6 "In 3.1 Tully–Fisher model ‣ 3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"), which incorporates the linear galaxy bias of [Eq.˜5](https://arxiv.org/html/2509.14997v2#S3.E5 "In 3.1 Tully–Fisher model ‣ 3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"). At this distance we evaluate the line-of-sight peculiar velocity 𝒗​(𝒓)\\bm{v}(\\bm{r}) and compute the true redshift,

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | 1+ztrue=(1+zcosmo​(r))​(1+\[𝑽ext+β​𝒗​(𝒓)\]⋅𝒓^c),1+z\_{\\rm true}=\\big(1+z\_{\\rm cosmo}(r)\\big)\\left(1+\\frac{\\left\[\\bm{V}\_{\\rm ext}+\\beta\\bm{v}(\\bm{r})\\right\]\\cdot\\hat{\\bm{r}}}{c}\\right), |  | (14) |

where zcosmoz\_{\\rm cosmo} is the cosmological redshift at distance rr and 𝒓^\\hat{\\bm{r}} is the unit vector toward the source. The observed redshift is then drawn with scatter σv\\sigma\_{v},

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | c​zobs↩𝒩​(c​ztrue,σv),cz\_{\\rm obs}\\hookleftarrow\\mathcal{N}(cz\_{\\rm true},\\,\\sigma\_{v}), |  | (15) |

assuming the “measurement” error of zobsz\_{\\rm obs} to be subdominant to σv\\sigma\_{v}. The apparent magnitude is obtained by first sampling ηtrue\\eta\_{\\rm true} from a Gaussian hyperprior,

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ηtrue↩𝒩​(η^,wη),\\eta\_{\\rm true}\\hookleftarrow\\mathcal{N}(\\hat{\\eta},\\,w\_{\\eta}), |  | (16) |

and then the observed linewidth as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ηobs↩𝒩​(ηtrue,ση).\\eta\_{\\rm obs}\\hookleftarrow\\mathcal{N}(\\eta\_{\\rm true},\\,\\sigma\_{\\eta}). |  | (17) |

The true apparent magnitude is

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | mtrue=μ​(r)+M​(ηtrue),m\_{\\rm true}=\\mu(r)+M(\\eta\_{\\rm true}), |  | (18) |

where μ​(r)\\mu(r) is the distance modulus and M​(ηtrue)M(\\eta\_{\\rm true}) is defined in [Eq.˜2](https://arxiv.org/html/2509.14997v2#S2.E2 "In 2.1 Tully–Fisher samples ‣ 2 Data ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"). The observed magnitude is drawn as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | mobs↩𝒩​(mtrue,σm2+σint2).m\_{\\rm obs}\\hookleftarrow\\mathcal{N}\\left(m\_{\\rm true},\\,\\sqrt{\\sigma\_{m}^{2}+\\sigma\_{\\rm int}^{2}}\\right). |  | (19) |

The resulting catalogue contains observed redshifts, magnitudes, linewidths, and sky positions. An example redshift distribution compared with the CosmicFlows-4 data is shown in [Fig.˜1](https://arxiv.org/html/2509.14997v2#S3.F1 "In 3.5 Inference procedure ‣ 3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances").

Report issue for preceding element

### 3.5 Inference procedure

Report issue for preceding element

To sample the posterior distribution we use the No-U-Turn Sampler (No-U-Turn Sampler; Hoffman\_2011) method of Hamiltonian Monte Carlo as implemented in the numpyro222 [https://num.pyro.ai/en/latest/](https://num.pyro.ai/en/latest/ "") package (Phan\_2019; Bingham\_2019), ensuring a Gelman–Rubin statistic R^−1≤0.001\\hat{R}-1\\leq 0.001 for convergence (Gelman\_1992).
For each model, we run four independent chains with 10001000 warm-up steps and 20002000 sampling steps, typically yielding more than 40004000 effective samples for the dipole and other parameters.

[... middle omitted — see footer ...]


Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | 1+zCMB=(1+zcosmo)​(1+zpec),1+z\_{\\rm CMB}=\\left(1+z\_{\\rm cosmo}\\right)\\left(1+z\_{\\rm pec}\\right), |  | (23) |

where zcosmoz\_{\\rm cosmo} is the redshift due to cosmic expansion, and zpec=Vpec/cz\_{\\rm pec}=V\_{\\rm pec}/c represents the redshift contribution from the galaxy’s line-of-sight peculiar velocity, VpecV\_{\\rm pec}. In a flat Λ\\Lambda-cold dark matter universe dominated by non-relativistic matter and dark energy, the cosmological redshift, zcosmoz\_{\\rm cosmo}, is related to the comoving distance, rr, by (e.g., Hogg1999)

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | r​(zcosmo)=cH0​∫0zcosmodz′Ωm​(1+z′)3+1−Ωm,r(z\_{\\rm cosmo})=\\frac{c}{H\_{\\rm 0}}\\int\_{0}^{z\_{\\rm cosmo}}\\frac{\\differential z^{\\prime}}{\\sqrt{\\Omega\_{\\rm m}(1+z^{\\prime})^{3}+1-\\Omega\_{\\rm m}}}, |  | (24) |

where Ωm\\Omega\_{\\rm m} is the matter density parameter. The velocity field, 𝒗​(𝒓)\\bm{v}(\\bm{r}), is modelled under the single-flow approximation, so that the line-of-sight peculiar velocity is

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | Vpec=(β​𝒗​(𝒓)+𝑽ext)⋅𝒓^,V\_{\\rm pec}=\\left(\\beta\\bm{v}(\\bm{r})+\\bm{V}\_{\\rm ext}\\right)\\cdot\\hat{\\bm{r}}, |  | (25) |

where 𝒓^\\hat{\\bm{r}} is the galaxy line-of-sight unit vector, and 𝑽ext\\bm{V}\_{\\rm ext} accounts for external flows originating beyond the reconstruction volume. The parameter β⋆\\beta^{\\star} is a calibration factor to scale the velocities predicted by Carrick\_2015 and is a function of both cosmology and the galaxy bias. When assuming no underlying velocity field, we effectively set 𝒗=0\\bm{v}=0, modelling the flow solely as 𝑽ext\\bm{V}\_{\\rm ext}. A third parameter, σv\\sigma\_{v}, which we introduce later, captures small-scale velocity dispersion not accounted for by the reconstruction.

Report issue for preceding element

For each galaxy we observe the apparent magnitude mobsm\_{\\rm obs} with uncertainty σm\\sigma\_{\\rm m} and the linewidth ηobs\\eta\_{\\rm obs} with uncertainty ση\\sigma\_{\\eta} (which is a distance-independent observable). These quantities constrain the galaxy distance. In VF\_olympics we introduce two latent parameters per galaxy to be inferred: the distance rr and the true linewidth ηtrue\\eta\_{\\rm true}. The Tully–Fisher relation relates ηtrue\\eta\_{\\rm true} to the absolute magnitude MM via [Eq.˜2](https://arxiv.org/html/2509.14997v2#S2.E2 "In 2.1 Tully–Fisher samples ‣ 2 Data ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"). Converting rr to a distance modulus μ\\mu yields a predicted apparent magnitude, mpred=μ​(r)+M​(ηtrue)m\_{\\rm pred}=\\mu(r)+M(\\eta\_{\\rm true}), with the distance modulus being

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | μ=5​log⁡dLMpc+25,\\mu=5\\log\\frac{d\_{\\rm L}}{\\mathrm{Mpc}}+25, |  | (26) |

where the luminosity distance dLd\_{\\rm L} is related to the comoving distance rr by

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | dL=(1+zcosmo)​r,d\_{\\rm L}=(1+z\_{\\rm cosmo})r, |  | (27) |

assuming a flat Λ\\Lambda-cold dark matter universe.

Report issue for preceding element

We jointly infer the velocity field calibration parameters, (𝑽ext,β,σv\\bm{V}\_{\\rm ext},\\beta,\\sigma\_{v}), the distance indicator parameters, (aTFR,bTFR,cTFR,σinta\_{\\rm TFR},b\_{\\rm TFR},c\_{\\rm TFR},\\sigma\_{\\rm int}), the mean η^\\hat{\\eta} and standard deviation wηw\_{\\eta} of the ηtrue\\eta\_{\\rm true} prior, and potentially the zero-point dipole 𝚫ZP\\bm{\\Delta}\_{\\rm ZP}. Assuming independent sources, VF\_olympics formulate the likelihood of the observed redshift, magnitude, and linewidth given the distance, true linewidth, and the set of model parameters 𝜽\\bm{\\theta} as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒ(zCMB,mobs,ηobs∣𝜽,r,ηtrue)==𝒩​(c​zCMB;c​zpred,σv2+σc​zCMB2)×𝒩​(mobs;mpred,σint2+σm2)×𝒩​(ηobs;ηtrue,ση)p​(S=1∣η^,wη),\\begin{split}\\mathcal{L}(z\_{\\rm CMB},\\,m\_{\\rm obs},\\,&\\eta\_{\\rm obs}\\mid\\bm{\\theta},\\,r,\\,\\eta\_{\\rm true})=\\\<br>&=\\mathcal{N}\\left(cz\_{\\rm CMB};cz\_{\\rm pred},\\,\\sqrt{\\sigma\_{v}^{2}+\\sigma\_{cz\_{\\rm CMB}}^{2}}\\right)\\\<br>&\\times\\mathcal{N}\\left(m\_{\\rm obs};m\_{\\rm pred},\\,\\sqrt{\\sigma\_{\\rm int}^{2}+\\sigma\_{m}^{2}}\\right)\\\<br>&\\times\\frac{\\mathcal{N}(\\eta\_{\\rm obs};\\eta\_{\\rm true},\\,\\sigma\_{\\eta})}{p(S=1\\mid\\hat{\\eta},\\,w\_{\\eta})},\\end{split} |  | (28) |

where p​(S=1∣η^,wη)p(S=1\\mid\\hat{\\eta},\\,w\_{\\eta}) is the expected fraction of retained sources given a truncation in ηobs\\eta\_{\\rm obs}. Strictly speaking, p​(S=1∣η^,wη)p(S=1\\mid\\hat{\\eta},\\,w\_{\\eta}) is not part of the data likelihood. It should multiply the product of the per-sample likelihoods and the prior as \[p​(S=1∣η^,wη)\]−n\\left\[p(S=1\\mid\\hat{\\eta},\\,w\_{\\eta})\\right\]^{-n}, where nn is the number of galaxies in the sample. For notational convenience, however, we absorb it into the likelihood (see Kelly\_2008 for more details). The first term in [Eq.˜28](https://arxiv.org/html/2509.14997v2#A1.E28 "In A.1 Tully–Fisher flow model ‣ Appendix A Flow model of S25 ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances") is the likelihood of the observed redshift given the predicted value, which depends on the inferred distance and peculiar velocity, while the second term is the likelihood of the observed magnitude given the predicted apparent magnitude. Furthermore, we have that

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | p​(S=1∣η^,wη)=∬dηobs​dηtrue​p​(S=1∣ηobs)×ℒ​(ηobs∣ηtrue)​π​(ηtrue∣η^,wη),\\begin{split}p(S=1\\mid\\hat{\\eta},\\,w\_{\\eta})&=\\iint\\mathrm{d}\\eta\_{\\rm obs}\\,\\mathrm{d}\\eta\_{\\rm true}\\;p(S=1\\mid\\eta\_{\\rm obs})\\\<br>&\\quad\\times\\mathcal{L}(\\eta\_{\\rm obs}\\mid\\eta\_{\\rm true})\\,\\pi(\\eta\_{\\rm true}\\mid\\hat{\\eta},\\,w\_{\\eta}),\\end{split} |  | (29) |

where p​(S=1∣ηobs)p(S=1\\mid\\eta\_{\\rm obs}) is a binary detection indicator between ηmin\\eta\_{\\min} and ηmax\\eta\_{\\max},

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | p​(S=1∣ηobs)={1ifηmin<ηobs<ηmax,0otherwise.p(S=1\\mid\\eta\_{\\rm obs})=\\begin{cases}1&\\text{if}\\quad\\eta\_{\\min}<\\eta\_{\\rm obs}<\\eta\_{\\max},\\\\[3.0pt\]<br>0&\\text{otherwise}.\\end{cases} |  | (30) |

ℒ​(ηobs∣ηtrue)\\mathcal{L}(\\eta\_{\\rm obs}\\mid\\eta\_{\\rm true}) denotes the Gaussian likelihood of the observed given the true linewidth, and π​(ηtrue∣η^,wη)\\pi(\\eta\_{\\rm true}\\mid\\hat{\\eta},\\,w\_{\\eta}) is the Gaussian prior on the true linewidth. Given these assumptions, it can be shown that

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | p​(S=1∣ηobs)=Φ​(ηmax−η^ση2+wη2)−Φ​(ηmin−η^ση2+wη2),p(S=1\\mid\\eta\_{\\rm obs})=\\Phi\\!\\left(\\frac{\\eta\_{\\max}-\\hat{\\eta}}{\\sqrt{\\sigma\_{\\eta}^{2}+w\_{\\eta}^{2}}}\\right)-\\Phi\\!\\left(\\frac{\\eta\_{\\min}-\\hat{\\eta}}{\\sqrt{\\sigma\_{\\eta}^{2}+w\_{\\eta}^{2}}}\\right), |  | (31) |

where Φ​(x)\\Phi(x) is the cumulative density function of the standard normal distribution, defined as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | Φ​(x)=12​π​∫−∞xe−t2/2​dt.\\Phi(x)=\\frac{1}{\\sqrt{2\\pi}}\\int\_{-\\infty}^{x}e^{-t^{2}/2}\\differential t. |  | (32) |

We assume only a lower threshold in ηobs\\eta\_{\\rm obs} in CosmicFlows-4 and SFI++, while in 2MTF we impose both a lower and upper threshold. We marginalise over rr and ηtrue\\eta\_{\\rm true} as

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒ(zCMB,mobs,ηobs∣𝜽)==∬ℒ​(zCMB,mobs,ηobs∣𝜽,r,ηtrue)×π​(r∣𝜽)​π​(ηtrue∣𝜽)​d​r​d​ηtrue,\\begin{split}\\mathcal{L}(z\_{\\rm CMB},\\,&m\_{\\rm obs},\\,\\eta\_{\\rm obs}\\mid\\bm{\\theta})=\\\<br>&=\\iint\\mathcal{L}(z\_{\\rm CMB},\\,m\_{\\rm obs},\\,\\eta\_{\\rm obs}\\mid\\bm{\\theta},\\,r,\\,\\eta\_{\\rm true})\\\<br>&\\quad\\times\\pi(r\\mid\\bm{\\theta})\\,\\pi(\\eta\_{\\rm true}\\mid\\bm{\\theta})\\,\\mathrm{d}r\\,\\mathrm{d}\\eta\_{\\rm true},\\end{split} |  | (33) |

where π​(r∣𝜽)\\pi(r\\mid\\bm{\\theta}) is defined in [Eq.˜6](https://arxiv.org/html/2509.14997v2#S3.E6 "In 3.1 Tully–Fisher model ‣ 3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances").
Rather than modelling the full HI selection of the Tully–Fisher relation sample, which is the primary reason why the Tully–Fisher relation samples do not extend to higher redshifts, we follow Lavaux\_Virbius and adopt an effective treatment by setting the distance prior to [Eq.˜6](https://arxiv.org/html/2509.14997v2#S3.E6 "In 3.1 Tully–Fisher model ‣ 3 Methodology ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"), which incorporates both the homogeneous and inhomogeneous Malmquist bias. We may either sample rr and ηtrue\\eta\_{\\rm true} for each galaxy directly with an Hamiltonian Monte Carlo sampler, or marginalise over them numerically at each Markov Chain Monte Carlo step. The former is computationally faster, while the latter yields a lower-dimensional parameter space suitable for evidence computation. Because evidence values are central to this work, we adopt the latter approach and evaluate the two-dimensional integral numerically on a grid in rr and ηtrue\\eta\_{\\rm true} at each Markov Chain Monte Carlo step. We define a fixed radial distance grid ranging from 0.0010.001 to 201​h−1​Mpc201~h^{-1}\\,\\mathrm{Mpc} with a step size of 0.5​h−1​Mpc0.5~h^{-1}\\,\\mathrm{Mpc}, which is sufficient given that the Carrick\_2015 field is smoothed on scales of 4​h−1​Mpc4~h^{-1}\\,\\mathrm{Mpc}. For ηtrue\\eta\_{\\rm true}, we adopt an adaptive binning scheme. The Gaussian likelihood term ℒ​(ηobs∣ηtrue)\\mathcal{L}(\\eta\_{\\rm obs}\\mid\\eta\_{\\rm true}) determines the region of ηtrue\\eta\_{\\rm true} that carries non-negligible probability mass. Accordingly, for each source we define a grid spanning ηobs±5​ση\\eta\_{\\rm obs}\\pm 5\\sigma\_{\\eta}, discretised into 3131 equally spaced steps, and evaluate the likelihood over a 402×31402\\times 31 grid at each Markov Chain Monte Carlo iteration. We then marginalise over this two-dimensional grid using Simpson’s rule. This computation is performed on GPUs using our JAX-based implementation555 [https://github.com/jax-ml/jax](https://github.com/jax-ml/jax ""). To verify that the numerical integration does not introduce bias, we compared the results to a model in which the latent parameters ηtrue\\eta\_{\\rm true} were explicitly sampled and found the posteriors to be consistent.

Report issue for preceding element

We compute the model evidence, 𝒵\\mathcal{Z}, defined as the integral of the likelihood weighted by the prior over the parameter space,

Report issue for preceding element

|     |     |     |     |
| --- | --- | --- | --- |
|  | 𝒵≡∫d𝜽​ℒ​(D∣𝜽)​π​(𝜽),\\mathcal{Z}\\equiv\\int\\differential\\bm{\\theta}\\mathcal{L}(D\\mid\\bm{\\theta})\\pi(\\bm{\\theta}), |  | (34) |

where DD represents the data and 𝜽\\bm{\\theta} the model parameters. The ratio of evidences between two models, known as the Bayes factor, quantifies the relative statistical support for one model over another, assuming equal prior model probabilities.

Report issue for preceding element

## Appendix B CF4 TFR W1 full posterior

Report issue for preceding element

In [Fig.˜9](https://arxiv.org/html/2509.14997v2#A2.F9 "In Appendix B CF4 TFR W1 full posterior ‣ No evidence for local 𝐻₀ anisotropy from Tully–Fisher or supernova distances"), we present the posterior distribution over model parameters inferred from the CosmicFlows-4 Tully–Fisher relation W1 data, with and without a dipole in the zero-point. The parameter set includes the isotropic Tully–Fisher relation zero-point, slope, and curvature (aTFRa\_{\\rm TFR}, bTFRb\_{\\rm TFR}, cTFRc\_{\\rm TFR}); the velocity field calibration factor β⋆\\beta^{\\star}; the intrinsic Tully–Fisher relation scatter (σint\\sigma\_{\\rm int}); the redshift scatter (σv\\sigma\_{v}); the external flow parameters (VextV\_{\\rm ext}, ℓext\\ell\_{\\rm ext}, bextb\_{\\rm ext}); the zero-point dipole parameters (ΔZP\\Delta\_{\\rm ZP}, ℓΔZP\\ell\_{\\Delta\_{\\rm ZP}}, bΔZPb\_{\\Delta\_{\\rm ZP}}); the linewidth hyperprior mean and standard deviation (η^\\hat{\\eta}, wηw\_{\\eta}); and the distance prior parameters (RR, nn, pp).

Report issue for preceding element

We find a mild degeneracy between the zero-point dipole amplitude and the magnitude of the external flow: a larger external flow can compensate for a smaller zero-point dipole, and vice versa. Comparing the model with a zero-point dipole to the isotropic case, we find a slight shift in the zero-point monopole, while the posteriors for bTFRb\_{\\rm TFR}, cTFRc\_{\\rm TFR}, α\\alpha, β⋆\\beta^{\\star}, σint\\sigma\_{\\rm int}, η^\\hat{\\eta}, and wηw\_{\\eta} remain unchanged. As expected, introducing the dipole shifts the posterior on 𝑽ext\\bm{V}\_{\\rm ext}, affecting both its magnitude and Galactic latitude.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2509.14997v2/x10.png)Figure 9: Posterior distributions for the model parameters inferred from the CosmicFlows-4 Tully–Fisher relation W1 data, comparing the zero-point dipole model (red) to the isotropic model (black). Parameters shown include the Tully–Fisher relation calibration (aTFRa\_{\\rm TFR}, bTFRb\_{\\rm TFR}, cTFRc\_{\\rm TFR}), velocity field calibration factor (β⋆\\beta^{\\star}), scatter terms (σint\\sigma\_{\\rm int}, σv\\sigma\_{v}), external flow parameters (VextV\_{\\rm ext}, ℓext\\ell\_{\\rm ext}, bextb\_{\\rm ext}), linewidth hyperparameters (η^\\hat{\\eta}, wηw\_{\\eta}), distance prior hyperparameters (RR, nn, pp), and zero-point dipole parameters (ΔZP\\Delta\_{\\rm ZP}, ℓΔZP\\ell\_{\\Delta\_{\\rm ZP}}, bΔZPb\_{\\Delta\_{\\rm ZP}}). We observe a mild degeneracy between the magnitude of the zero-point dipole and the external flow, and find that introducing a dipole shifts the inferred 𝑽ext\\bm{V}\_{\\rm ext} while leaving other parameters largely unchanged. Contours denote 1​σ1\\sigma and 2​σ2\\sigma credible regions.Report issue for preceding element

Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)

──────── [TRUNCATED] ────────
Showing 44,612 chars (head) + 14,759 chars (tail) of 117,564 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-3080187a9a.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-3080187a9a.md" offset=437 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
