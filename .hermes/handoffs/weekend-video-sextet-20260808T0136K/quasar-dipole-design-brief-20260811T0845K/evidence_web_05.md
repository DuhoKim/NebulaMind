By using this website, you agree that EDP Sciences may store web audience measurement cookies and, on some pages, cookies from social networks. [More information and setup](https://www.aanda.org/component/cookie_policy/)

YesNo

Free Access

| Issue |  | A&A<br> <br>**Volume** 555, July 2013 |
|  |
|  |
| Article Number |  | A117 |
| Number of page(s) |  | 13 |
| Section |  | Cosmology (including clusters of galaxies) |
| DOI |  | [https://doi.org/10.1051/0004-6361/201321215](https://doi.org/10.1051/0004-6361/201321215) |
| Published online |  | 10 July 2013 |

A&A 555, A117 (2013)

## Cosmic radio dipole from NVSS and WENSS

M. Rubart and D. J. Schwarz

+


Fakultät für Physik, Universität Bielefeld,
Postfach 100131,
33501
Bielefeld,
Germany




e-mail:
[matthiasr@physik.uni-bielefeld.de](mailto:matthiasr@physik.uni-bielefeld.de) This email address is being protected from spambots. You need JavaScript enabled to view it.
; [dschwarz@physik.uni-bielefeld.de](mailto:dschwarz@physik.uni-bielefeld.de) This email address is being protected from spambots. You need JavaScript enabled to view it.


Received:
1
February
2013


Accepted:
30
May
2013


Abstract

We use linear estimators to determine the magnitude and direction of the cosmic radio
dipole from the NRAO VLA Sky Survey (NVSS) and the Westerbork Northern Sky Survey (WENSS).
We show that special attention has to be given to the issues of bias due to shot noise,
incomplete sky coverage and masking of the Milky Way. We compare several different
estimators and show that conflicting claims in the literature can be attributed to the use
of different estimators. We find that the NVSS and WENSS estimates of the cosmic radio
dipole are consistent with each other and with the direction of the cosmic microwave
background (CMB) dipole. We find from the NVSS a dipole amplitude of
(1.8 ± 0.6) × 10-2 in direction
(RA,dec) = (154° ± 19°, −2° ± 19°).
This amplitude exceeds the one expected from the CMB by a factor of about 4 and is
inconsistent with the assumption of a pure kinetic origin of the radio dipole at 99.6%
CL.

Key words: radio continuum: galaxies / large-scale structure of Universe

_© ESO, 2013_

## 1\. Introduction

The assumed isotropy and homogeneity of the Universe at large scales is fundamental to
modern cosmology. The isotropy is best seen in the cosmic microwave background (CMB)
radiation and holds at the per cent level. The most prominent anisotropy of the CMB
temperature is a dipole signal of
Δ _T_/ _T_ ≈ 10-3. It is
commonly assumed that this dipole is largely caused by the motion of the Solar system
through the Universe ( [Stewart & Sciama 1967](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R23)).
This interpretation seems to be fully consistent with the concordance model of cosmology.

However, the observation of the microwave sky is not enough to tell the difference between
a motion induced CMB dipole and dipole contributions form other physical phenomena, i.e.
![Mathematical equation: \begin{equation} \boldsymbol{d}_{\rm cmb} = \boldsymbol{d}_{\rm motion} + \boldsymbol{d}_{\rm primordial} + \boldsymbol{d}_{\rm ISW} + \boldsymbol{d}_{\rm foregrounds} + \boldsymbol{d}_{\rm noise}. \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq6.png)

```
\begin{equation} \boldsymbol{d}_{\rm cmb} = \boldsymbol{d}_{\rm motion} + \boldsymbol{d}_{\rm primordial} + \boldsymbol{d}_{\rm ISW} + \boldsymbol{d}_{\rm foregrounds} + \boldsymbol{d}_{\rm noise}. \end{equation}
```

(1)In our notation a
dipole vector **_d_** modulates the isotropic sky by a factor
![Mathematical equation: \hbox{$(1+\boldsymbol{d} \cdot \boldsymbol{\hat{r}})$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq8.png)

```
\hbox{$(1+\boldsymbol{d} \cdot \boldsymbol{\hat{r}})$}
```

,
with ![Mathematical equation: \hbox{$\boldsymbol{\hat{r}}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq9.png)

```
\hbox{$\boldsymbol{\hat{r}}$}
```

denoting the position on the sky.

Usually it is assumed that the primordial and the integrated Sachs-Wolfe (ISW) contribution
to the CMB dipole are negligibly small and that foregrounds (the Milky Way) are under
control. Within the concordance model we expect a primordial contribution of
_d_ primordial ≈ 2 × 10-5. The ISW contribution could
be as large as 10-4 from the gravitational potentials induced by local 100 Mpc
sized structures, without being in conflict with the concordance model ( [Rakic et al. 2006](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R18); [Francis & Peacock 2010](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R10)). The noise term can be ignored due to excellent
statistics of full sky observations. Thus the measured
**_d_** cmb is directly used to infer the velocity of
the Solar system w.r.t. the CMB to be _v_ = 369 ± 0.9 km s-1
( [Hinshaw et al. 2009](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R14)). It is used in many
cosmological studies done in the CMB rest frame, e.g. supernova Hubble diagrams or
measurements of large scale bulk flows.

The effects of motion are not limited to the CMB, but should actually be detectable at any
frequency. In order to test the hypothesis
**_d_** cmb = **_d_** motion,
it would be very interesting to measure the dipole of another cosmic probe, such as that
obtained by radio point source catalogues. In this case one expects to find
![Mathematical equation: \begin{equation} \boldsymbol{d}_{\rm radio} = \boldsymbol{d}_{\rm motion} + \boldsymbol{d}_{\rm structure} + \boldsymbol{d}_{\rm foregrounds} + \boldsymbol{d}_{\rm noise}. \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq15.png)

```
\begin{equation} \boldsymbol{d}_{\rm radio} = \boldsymbol{d}_{\rm motion} + \boldsymbol{d}_{\rm structure} + \boldsymbol{d}_{\rm foregrounds} + \boldsymbol{d}_{\rm noise}. \end{equation}
```

(2)Besides the signal from
our proper motion, we expect a signal from structure in the Universe and we expect a random
dipole from Poisson noise. The dipole from structure is expected to dominate any catalogue
limited to redshift _z_ ≪ 1\. Thus we are interested in surveys with a mean
redshift of order unity and a large enough sky coverage to be sensitive to the dipole. This
makes radio catalogues the preferred probe to look at. Within the concordance model, the
dipole signal induced by the large scale structure is then a subdominant contribution, as it
is for the CMB. If we had a large enough catalogue, we could compare
**_d_** radio to
**_d_** cmb. Any statistically significant deviation
would be exciting, while finding a match would put the concordance model on firmer grounds.

A first attempt to measure the radio dipole was performed by [Baleisis et al. (1998)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R1) using a combination of the Green Bank 1987 and the
Parkes-MIT-NRAO catalogues. [Blake & Wall\\
(2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3), [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22) and [Gibelyou & Huterer (2012)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R12) attempted to determine
the dipole vector in the NRAO VLA Sky Survey (NVSS), with different conclusions. [Blake & Wall (2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3) found a result that is in
agreement with a purely kinetic origin of the cosmic radio dipole, but this was challenged
by [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22), who finds a dipole amplitude four
times larger than expected, but strangely enough pointing in a direction consistent with the
CMB dipole. The analysis of [Gibelyou & Huterer\\
(2012)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R12) finds both a different direction and an amplitude six times as large as the
expected one. While [Blake & Wall (2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3) used a
quadratic estimator, [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22) and [Gibelyou & Huterer (2012)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R12) used different linear
estimators to find the dipole direction.

The purpose of this work is to discuss the use of linear estimators of the cosmic radio
dipole and apply several versions of them on the NVSS ( [Condon\\
et al. 2002](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R4)) and the Westerbork Northern Sky Survey (WENSS; [Rengelink et al. 1997](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R19)). We resolve the conflicts in the literature and
extend the analysis to other linear estimators.

The NVSS survey covers about 10.3 sr of the sky and contains about 2 × 105
sources per steradian. For this survey the Very Large Array (VLA) in New Mexico (USA) has
been used measuring at a frequency of 1.4 GHz. The survey includes over 80 per cent of the
sky, missing only areas with declination
_δ_ < −40°. The lower flux limit lies
at 2.5 mJy for the 5 _σ_ detection of point sources. The NVSS was conducted by
means of two different configurations of the VLA above and below
_δ_ = −10°.

The Westerbork Synthesis Radio Telescope in the Netherlands was operated at a frequency of
325 MHz to record the WENSS survey covering about 2.9 sr of the nothern sky and containing
about 2.3 × 105 sources in total. This survey is made up of a main catalogue for
_δ_ ∈ (28°,76°) and a polar
catalogue for _δ_ > 72°. The
5 _σ_ detection limit for this survey is 18 mJy.

To analyse these surveys, we focus on linear estimators in this work. We do so for two
reasons. Firstly, recent controversial results used linear estimators for the dipole
direction ( [Singal 2011](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22); [Gibelyou & Huterer 2012](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R12)) and in one work also for the dipole
amplitudes ( [Singal 2011](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22)). Secondly, linear estimators
are conceptually simpler. However, it is not expected that they are optimal (unbiased and
minimal variance). The linear estimators used in our analysis are asymptotically unbiased
and their variance can be easily understood by analytic calculations and by Monte Carlo
simulations.

The paper is organized as follows: first we discuss the expected kinetic radio dipole. In
Sect. [3](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#S5) we outline previous estimates of the radio
dipole. Linear estimators for full sky surveys are investigated in Sect. [4](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#S6), followed by a detailed analysis of the effects of
incomplete sky coverage and masking in the next section. In Sect. [6](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#S13) we discuss the expected dipole amplitude from a flux based estimator.
Our estimate of the radio dipole can be found in Sect. [7](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#S15) and is followed by a comparison with previous results. We conclude in Sect.
[9](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#S21).

## 2\. Kinetic radio dipole

### 2.1. Doppler shift and aberration

[Ellis & Baldwin (1984)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R8) predicted the
kinetic contribution to the cosmic radio dipole for an isotropic and homogeneous
cosmology. At redshift of order unity and beyond, we expect this kinetic contribution to
be the dominant one.

The spectrum of a radio source is assumed to be described by a power law, ![Mathematical equation: \begin{equation} \label{fluxpowerlaw} S(f) \propto f^{-\alpha}, \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq32.png)

```
\begin{equation} \label{fluxpowerlaw} S(f) \propto f^{-\alpha}, \end{equation}
```

(3)where
_S_ denotes the flux and _f_ the frequency. Each radio
source can be described by an individual spectral index _α_. For simplicity
we assumed a mean value of _α_ for all radio sources in the catalogue.

The number of observed radio sources per steradian depends on the lower flux limit and
can be approximated by a power law ![Mathematical equation: \begin{equation} \label{numbercountpowerlaw} \frac{{\rm d}N}{{\rm d}\Omega}({>}S) \propto S^{-x} . \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq36.png)

```
\begin{equation} \label{numbercountpowerlaw} \frac{{\rm d}N}{{\rm d}\Omega}({>}S) \propto S^{-x} . \end{equation}
```

(4)The value of
_x_ can be different for each survey. Typically _x_ is
assumed to be about one.

Two effects have to be taken into account. The emitted radio frequency
_f_ rest is observed at the Doppler shifted frequency
_f_ obs. The magnitude of this change depends on the angle
_θ_ between the direction to the source and the direction of our motion,
with velocity _v_. Observed and rest frame frequencies are related by
![Mathematical equation: \begin{equation} f_\mathrm{obs} = f_\mathrm{rest} \delta(v,\theta) , \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq42.png)

```
\begin{equation} f_\mathrm{obs} = f_\mathrm{rest} \delta(v,\theta) , \end{equation}
```

(5)where _δ_
is given by ![Mathematical equation: \begin{equation} \label{deltaexact} \delta(v,\theta) = \frac{1+\frac{v}{c} \cos(\theta)}{\sqrt{1-(\frac{v}{c})^2}} \cdot \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq44.png)

```
\begin{equation} \label{deltaexact} \delta(v,\theta) = \frac{1+\frac{v}{c} \cos(\theta)}{\sqrt{1-(\frac{v}{c})^2}} \cdot \end{equation}
```

(6)Thus the observed flux
changes due to our motion, since it depends on the frequency ![Mathematical equation: \begin{equation} \label{fluxchange} S_{\mathrm{obs}}(f_{\mathrm{obs}}) \propto \delta f_{\mathrm{rest}}^{-\alpha} \propto \delta^{1+\alpha} f_{\mathrm{obs}}^{-\alpha} \propto S_{\mathrm{rest}} (f_{\rm obs}) \delta^{1+\alpha}. \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq45.png)

```
\begin{equation} \label{fluxchange} S_{\mathrm{obs}}(f_{\mathrm{obs}}) \propto \delta f_{\mathrm{rest}}^{-\alpha} \propto \delta^{1+\alpha} f_{\mathrm{obs}}^{-\alpha} \propto S_{\mathrm{rest}} (f_{\rm obs}) \delta^{1+\alpha}. \end{equation}
```

(7)The first factor of
_δ_ is due to the fact that the energy of an observed photon is enhanced
due to the Doppler effect.

Thus, the Doppler effect will change the number of observed sources above a given flux
limit like ![Mathematical equation: \begin{equation} \left(\frac{{\rm d}N}{{\rm d}\Omega}\right)_\mathrm{obs}=\left(\frac{{\rm d}N}{{\rm d}\Omega}\right)_\mathrm{rest} \delta^{x(1+\alpha)}. \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq46.png)

```
\begin{equation} \left(\frac{{\rm d}N}{{\rm d}\Omega}\right)_\mathrm{obs}=\left(\frac{{\rm d}N}{{\rm d}\Omega}\right)_\mathrm{rest} \delta^{x(1+\alpha)}. \end{equation}
```

(8)Since the velocity
of light is finite, aberration will also modify the number counts. The position of each
source is changed towards the direction of motion. The new angle
_θ_′ (observed from Earth) between the position of the source
and the direction of motion is given by ![Mathematical equation: \begin{equation} \label{thetaprime} \tan{\theta^\prime} = \frac{\sin{\theta}\sqrt{1-\frac{v^2}{c^2}}}{\frac{v}{c}+\cos{\theta}} \cdot \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq48.png)

```
\begin{equation} \label{thetaprime} \tan{\theta^\prime} = \frac{\sin{\theta}\sqrt{1-\frac{v^2}{c^2}}}{\frac{v}{c}+\cos{\theta}} \cdot \end{equation}
```

(9)Therefore, at first order
in _v_/ _c_, _d_ Ω
transforms like ![Mathematical equation: \begin{equation} {\rm d} \Omega^\prime = {\rm d} \Omega \left(1-2\frac{v}{c} \cos{\theta}\right) + O\left( \left(\frac{v}{c}\right)^2\right) \cdot \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq51.png)

```
\begin{equation} {\rm d} \Omega^\prime = {\rm d} \Omega \left(1-2\frac{v}{c} \cos{\theta}\right) + O\left( \left(\frac{v}{c}\right)^2\right) \cdot \end{equation}
```

(10)This can be combined with
the Doppler effect to give the observed number density. After approximating
_δ_( _v,θ_) to first order in
![Mathematical equation: \hbox{$\dfrac{v}{c}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq53.png)

```
\hbox{$\dfrac{v}{c}$}
```

, the
result becomes ![Mathematical equation: \begin{equation} \label{numbercountapprox} \frac{{\rm d}N}{{\rm d}\Omega}_{\mathrm{obs}} = \left(\frac{{\rm d}N}{{\rm d}\Omega}\right)_{\mathrm{rest}} \left[1+[2+x(1+\alpha)] \left(\frac{v}{c}\right) \cos(\theta)\right] . \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq54.png)

```
\begin{equation} \label{numbercountapprox} \frac{{\rm d}N}{{\rm d}\Omega}_{\mathrm{obs}} = \left(\frac{{\rm d}N}{{\rm d}\Omega}\right)_{\mathrm{rest}} \left[1+[2+x(1+\alpha)] \left(\frac{v}{c}\right) \cos(\theta)\right] . \end{equation}
```

(11)The amplitude of
the kinetic radio dipole is then given by ![Mathematical equation: \begin{equation} \label{amplitudedefinition} d = [2+x(1+\alpha) ] \left(\frac{v}{c}\right)\cdot \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq55.png)

```
\begin{equation} \label{amplitudedefinition} d = [2+x(1+\alpha) ] \left(\frac{v}{c}\right)\cdot \end{equation}
```

(12)The kinetic radio
dipole points towards the direction of our peculiar motion, which in an isotropic and
homogeneous Universe must also agree with the direction defined by the CMB dipole.

### 2.2. Expected kinetic radio dipole

The measured CMB dipole is Δ _T_ = 3.355 ± 0.008 mK in the direction
( _l,b_) = (263.99° ± 0.14°,48.26° ± 0.03°)
( [Hinshaw et al. 2009](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R14)). In equatorial coordinates
(epoch J2000) its direction reads (RA, Dec)
= (168°,−7°). Compared to the CMB temperature
of _T_ 0 = 2.725 ± 0.001 K ( [Fixsen\\
& Mather 2002](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R9)). this corresponds to a relative fluctuation of
Δ _T_/ _T_ = (1.231 ± 0.003) × 10-3
and thus the velocity of the Solar system has been inferred from the CMB dipole to be
_v_ = 369.0 ± 0.9 km s-1 ( [Hinshaw et al. 2009](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R14)).

To find the expected amplitude of the kinetic radio dipole, we also need estimates for
_x_ and _α_. The typically assumed values are
_x_ = 1 and _α_ = 0.75, which gives together with
_v_ = 370 km s-1 a radio dipole amplitude of
_d_ = 0.46 × 10-2. However, we can improve on that as
_x_ can be measured with help of the radio survey. Therefore we need to
plot _N_(> _S_) against
_S_ like in Fig. [1](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F1).

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 1 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig1_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F1.html) | [Fig. 1](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F1.html) <br>Number counts of the NVSS and WENSS surveys. A function<br>_f_( _S_) ∝ _S_ − _x_<br>is fitted to both data sets in the range of<br>25 mJy < _S_ < 200 mJy.<br>Resulting values of _x_ are 1.10 ± 0.02 for the NVSS survey and<br>0.80 ± 0.02 for the WENSS survey. |

For the purpose of this work we find _x_ NVSS = 1.10 ± 0.02 and
_x_ WENSS = 0.80 ± 0.02. The mean spectral index cannot be
inferred from the catalogues, as they provide data at a single frequency band only. We
thus stick to _α_ = 0.75, but include in the dipole error an uncertainty of
Δ _α_ = 0.25 ( [Garn et al. 2008](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R11)).
This results in the expectations:

![Mathematical equation: \begin{eqnarray} &&d_{\rm NVSS}^{\rm exp} = (0.48 \pm 0.04) \times 10^{-2}, \\[3mm] &&d_{\rm WENSS}^{\rm exp} = (0.42 \pm 0.03) \times 10^{-2}. \end{eqnarray}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq78.png)

```
\begin{eqnarray} &&d_{\rm NVSS}^{\rm exp} = (0.48 \pm 0.04) \times 10^{-2}, \\[3mm] &&d_{\rm WENSS}^{\rm exp} = (0.42 \pm 0.03) \times 10^{-2}. \end{eqnarray}
```

The error is dominated by the uncertainty in the spectral index.

## 3\. Previous results

The first measurement of the radio dipole using the NVSS catalogue was performed by [Blake & Wall (2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3). In order to remove corruption
by local structure, all sources within 15° vicinity of the Galactic disk have
been removed. Additionally the clustering dipole contribution was reduced by ignoring
sources within 30′′ of nearby known galaxies. The spherical harmonic coefficients
![Mathematical equation: \hbox{$a_{lm}^{\mathrm{obs}}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq81.png)

```
\hbox{$a_{lm}^{\mathrm{obs}}$}
```

from the
remaining NVSS catalogue have been determined up to _l_ = 3\. A model for a
dipole distribution with an isotropic background has been constructed
( _a_ 00 and _a_ 10). Due to masking,
this dipole distribution also influences higher multipoles. After applying the same mask as
for the NVSS catalogue, one finds ![Mathematical equation: \hbox{$a_{lm}^{\mathrm{model}}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq85.png)

```
\hbox{$a_{lm}^{\mathrm{model}}$}
```

up to
_l_ = 3\. A quadratic estimator (chi square) was used to compare the model
with the observed coefficients.

The resulting best-fit dipoles can be seen in Table [1](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#T1). The results of [Blake & Wall\\
(2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3) indicate a higher radio dipole than expected, however without statistical
significance.

[Table 1](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/T1.html)

Best-fit dipole parameters from [Blake & Wall\\
(2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3).

[Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22) used a linear estimator, originally
proposed by [Crawford (2009)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R6), ![Mathematical equation: \begin{equation} \label{Nsum} \boldsymbol{R}_{\mathrm{3D}} = \sum \boldsymbol{\hat r}_i , \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq100.png)

```
\begin{equation} \label{Nsum} \boldsymbol{R}_{\mathrm{3D}} = \sum \boldsymbol{\hat r}_i , \end{equation}
```

(15)and a variation of it,
which we discuss below. For a large number of sources the isotropic background will clear
away. The remaining vector **_R_** 3D will point towards
the main anisotropy in the distribution of number density over the sky. To get the correct
dipole amplitude _d_ one has to normalize this estimator depending on the
number of sources. In Singal’s analysis sources within 10° of the Galactic plane
have been removed. In order to avoid directional bias (see the more detailed discussion
below), he reestablished a north-south symmetry of the NVSS by cutting all sources with
dec > 40°. The results of [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22) are shown in Table [2](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#T2). The errors of the directional measurements are quite small here. This is an
effect of an unexpectedly large amplitude, which simplifies the measurement. While the
direction agrees with the one found by [Blake & Wall\\
(2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3), the dipole amplitude seems to be a factor of about four higher than
expected from the CMB dipole and twice as big as found by [Blake & Wall (2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3).

Masking the supergalactic plane in order to reduce the contribution of local structure did
not resolve the discrepancy. Since unknown clustering further away from the super Galactic
plane could also have contributed to the measurement, a second test was performed. A
clustering contribution to the dipole would not give a signal proportional to
cos _θ_. On the other hand, the difference in number counts of areas that
are opposite to each other should decrease with cos _θ_ (where
_θ_ is the angle between an area and the measured dipole direction), if the
measured dipole is due to our velocity. Singal was able to fit such a behaviour to the data.
Therefore he concludes that the radio dipole amplitude is not due to local clustering.

[Table 2](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/T2.html)

Dipole direction and amplitude from the number count estimator ( [15](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#FD14)) from [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22).

[Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22) also used a linear estimator for the
distribution of flux over the sky. This estimator is similar to the number density estimator
( [15](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#FD14)), but weights each radio source by its
flux _S_ _i_, ![Mathematical equation: \begin{equation} \label{Ssum} \boldsymbol{R}_{\mathrm{flux}} = \sum S_i \boldsymbol{\hat r}_i . \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq141.png)

```
\begin{equation} \label{Ssum} \boldsymbol{R}_{\mathrm{flux}} = \sum S_i \boldsymbol{\hat r}_i . \end{equation}
```

(16)Like
**_R_** 3D, this estimator finds the main anisotropy
and the amplitude needs to be normalized. The brightest sources
( _S_ > 1000 mJy) are removed, because they would
dominate **_R_** flux otherwise. Results of this estimator
are shown in Table [3](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#T3). The estimated directions are in
agreement with the results of [Blake & Wall\\
(2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3) and the number count estimator results of [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22). However, the normalized dipole amplitudes _d_ are
even higher than those of the number count estimator
**_R_** 3D. In Sect. [6](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#S13) we resolve this conflict.

[Table 3](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/T3.html)

Dipole direction and amplitude from the flux weighted number count estimator ( [16](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#FD15)) from [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22).

Most recently, [Gibelyou & Huterer (2012)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R12)
measured a dipole amplitude ( _d_ = 2.7 ± 0.5) × 10-2 towards (RA,
Dec) = (117 ± 20°,6 ± 14°) from the NVSS. This
direction is inconsistent with the studies mentioned above and the dipole amplitude is a
factor of five larger than expected. The authors used separate estimators for the direction
and the amplitude. Their direction estimate is based on a linear estimator, originally
proposed by [Hirata (2009)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R15), ![Mathematical equation: \begin{equation} \label{Gibelyouesti} \boldsymbol{R}_{\mathrm{3DM}}=\sum_i^{N_{\rm D}}\hat{r}_i - \frac{N_{\rm D}}{N_{\rm R}} \sum_j^{N_{\rm R}} \hat{r}_j . \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq174.png)

```
\begin{equation} \label{Gibelyouesti} \boldsymbol{R}_{\mathrm{3DM}}=\sum_i^{N_{\rm D}}\hat{r}_i - \frac{N_{\rm D}}{N_{\rm R}} \sum_j^{N_{\rm R}} \hat{r}_j . \end{equation}
```

(17)This
three-dimensional estimator (3DM) is intended to be unbiased for arbitrary survey geometries
and arbitrary masking. The idea is to achieve that with help of the second sum, which goes
over _N_ R randomly distributed points, subject to the same
masking. Therefore, the authors include all sources of the NVSS survey, except for those
within 10° of the Galactic plane. Below we show that this estimator has a
direction bias, which depends on the real dipole anisotropy.

We summarize, there is no agreement on the amplitude and direction of the cosmic radio
dipole so far.

## 4\. Linear estimators for a full sky

Let us first show that the estimator ( [15](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#FD14))
provides an unbiased estimate of the dipole direction.

Starting from the distribution of the number of radio sources per solid angle ( [11](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#FD11)), as seen by a moving observer in an
otherwise isotropic Universe, the probability to find a given radio source within a solid
angle dΩ of position ![Mathematical equation: \hbox{$\boldsymbol{\hat r}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq177.png)

```
\hbox{$\boldsymbol{\hat r}$}
```

is given by ![Mathematical equation: \begin{equation} \label{density2} p(\boldsymbol{\hat{r}}) {\rm d} \Omega = \frac{1}{4\pi} (1 + \boldsymbol{\hat r} \cdot \boldsymbol{d}) {\rm d}\Omega, \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq178.png)

```
\begin{equation} \label{density2} p(\boldsymbol{\hat{r}}) {\rm d} \Omega = \frac{1}{4\pi} (1 + \boldsymbol{\hat r} \cdot \boldsymbol{d}) {\rm d}\Omega, \end{equation}
```

(18)where
**_d_** denotes the dipole vector.

To study the bias of an estimator, we calculate its expectation value with respect to an
ensemble average. We do so below by means of Monte Carlo studies. For analytic
considerations, for large _N_ we replace the ensemble average by a spatial
average, i.e. ![Mathematical equation: \begin{equation} \langle 1 \rangle = \int \prod_{i=1}^N {\rm d} \Omega_i p(\boldsymbol{\hat r}_i) 1 = 1, \label{measure} \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq179.png)

```
\begin{equation} \langle 1 \rangle = \int \prod_{i=1}^N {\rm d} \Omega_i p(\boldsymbol{\hat r}_i) 1 = 1, \label{measure} \end{equation}
```

(19)thus we assume
ergodicity. Note that the average is a linear operator.

Now the expectation value of Crawford’s estimator can be evaluated for large
_N_, ![Mathematical equation: \begin{equation} \langle \boldsymbol{R}_{\mathrm{3D}} \rangle = \langle \sum_{i=1}^N \hat{r}_i \rangle = \sum_{i=1}^N \langle \hat{r}_i \rangle = \frac{N}{4 \pi}\int \mathrm{d} \Omega\, (1 + \hat{r} \cdot \boldsymbol{d})\, \hat{r} . \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq180.png)

```
\begin{equation} \langle \boldsymbol{R}_{\mathrm{3D}} \rangle = \langle \sum_{i=1}^N \hat{r}_i \rangle = \sum_{i=1}^N \langle \hat{r}_i \rangle = \frac{N}{4 \pi}\int \mathrm{d} \Omega\, (1 + \hat{r} \cdot \boldsymbol{d})\, \hat{r} . \end{equation}
```

(20)This calculation holds for
independent, identically distributed positions ![Mathematical equation: \hbox{$\hat{r}_i$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq181.png)

```
\hbox{$\hat{r}_i$}
```

,
thus without clustering effects. Only the second term survives the integration and thus the
expected dipole estimator is ![Mathematical equation: \begin{equation} \label{expectCrawford} \langle \boldsymbol{R}_{\mathrm{3D}} \rangle =\frac{1}{3} N \boldsymbol{ d}. \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq182.png)

```
\begin{equation} \label{expectCrawford} \langle \boldsymbol{R}_{\mathrm{3D}} \rangle =\frac{1}{3} N \boldsymbol{ d}. \end{equation}
```

(21)Naively, one could now
estimate the dipole signal by ![Mathematical equation: \hbox{$\boldsymbol{d}_{\mathrm{3D}} \equiv \frac{3}{N} \boldsymbol{R}_\mathrm{3D} $}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq183.png)

```
\hbox{$\boldsymbol{d}_{\mathrm{3D}} \equiv \frac{3}{N} \boldsymbol{R}_\mathrm{3D} $}
```

.

We conclude that **_d_** 3D provides us with an unbiased
estimate of the dipole direction ![Mathematical equation: \hbox{$\boldsymbol{\hat d}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq185.png)

```
\hbox{$\boldsymbol{\hat d}$}
```

for a full sky sample. However the estimated dipole amplitude
\| **_d_** 3D \| is biased.

To understand the origin of this bias let us first consider ![Mathematical equation: \begin{equation} \label{dCsquare} \langle \boldsymbol{d}^2_{\rm{3D}}\rangle = \left(1 - \frac{1}{N} \right) d^2 + \frac 9 N > d^2. \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq187.png)

```
\begin{equation} \label{dCsquare} \langle \boldsymbol{d}^2_{\rm{3D}}\rangle = \left(1 - \frac{1}{N} \right) d^2 + \frac 9 N > d^2. \end{equation}
```

(22)The inequality holds for
large _N_ and _d_ < 3 (in case of
large dipole amplitudes \[![Mathematical equation: \hbox{$d= {\cal O}(1)$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq189.png)\
\
```\
\hbox{$d= {\cal O}(1)$}\
```\
\
\]
our ansatz ( [19](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#FD18)) should also take many-point
correlations into account). Thus ![Mathematical equation: \hbox{$\boldsymbol{d}^2_{\rm{3D}}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq190.png)

```
\hbox{$\boldsymbol{d}^2_{\rm{3D}}$}
```

is definitely
biased towards higher amplitudes. However, to prove that
\| **_d_** 3D \| is biased, we would need to calculate
⟨\| **_d_** 3D \|⟩. We do this by means of the random
walk/flight method.

### 4.1. Random flight

Adding up vectors for each point of a survey corresponds to a random walk with unit step
size. To be more precise this is a random flight, since the problem is three dimensional.
Even for a vanishing dipole, such a random flight is unlikely to return to the origin
after _N_ steps. This describes the noise of any realisation of an
isotropic distribution of _N_ sources.

Following [Crawford (2009)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R6), we determine the
distance _r_ from the origin after _N_ steps from the
probability density of a random flight process ![Mathematical equation: \begin{equation} \label{Result3DFlight} \check{P}_N(r) \mathrm{d}r= \left[ \frac{54}{\pi N^3}\right]^{1/2} r^2 \exp\left( -\frac{3 r^2}{2N} \right) \mathrm{d}r. \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq193.png)

```
\begin{equation} \label{Result3DFlight} \check{P}_N(r) \mathrm{d}r= \left[ \frac{54}{\pi N^3}\right]^{1/2} r^2 \exp\left( -\frac{3 r^2}{2N} \right) \mathrm{d}r. \end{equation}
```

(23)The probability of
measuring a dipole signal of an amplitude bigger than _R_ in a random
flight is ![Mathematical equation: \begin{equation} P_N(R>R_{pCL})= \int_{R_{pCL}}^\infty \mathrm{d} r \check{P}_N(r)=1 - pCL . \end{equation}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq195.png)

```
\begin{equation} P_N(R>R_{pCL})= \int_{R_{pCL}}^\infty \mathrm{d} r \check{P}_N(r)=1 - pCL . \end{equation}
```

(24)A confidence level
_pCL_ can be choosen, leading to errorbars for a measured dipole vector
_R_ 3D ± _R_ _pCL_. To
estimate the directional uncertainties of this method, [Crawford (2009)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R6) made the following argument: at a given confidence level the
random flight corresponds to a step of length up to
_R_ _pCL_. Adding
_R_ _pCL_ perpendicular to the measured dipole
**_R_** 3D allows us to estimate the maximal offset
in direction. Using trigonometry, one can relate
_R_ _pCL_ to the directional uncertainties

[... middle omitted — see footer ...]


[Table 5](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/T5.html)

Dipole right ascension and amplitude
_d_ sin _θ_ d from NVSS.

[In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#T5)

[Table 6](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/T6.html)

Masking correction _k_ for WENSS with CG mask and a dipole with
RA = 120°.

[In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#T6)

[Table 7](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/T7.html)

Dipole estimate from WENSS based on 2D estimator using peak flux values for all
sources with _δ_ > 30°, except
those in the Galactic and counter Galactic planes (CG mask).

[In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#T7)

[Table 8](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/T8.html)

Comparison of results.

[In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#T8)

## All Figures

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 1 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig1_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F1.html) | [Fig. 1](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F1.html) <br>Number counts of the NVSS and WENSS surveys. A function<br>_f_( _S_) ∝ _S_ − _x_<br>is fitted to both data sets in the range of<br>25 mJy < _S_ < 200 mJy.<br>Resulting values of _x_ are 1.10 ± 0.02 for the NVSS survey and<br>0.80 ± 0.02 for the WENSS survey. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F1) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 2 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig2_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F2.html) | [Fig. 2](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F2.html) <br>Ampliude bias of the full sky estimator _d_ 3D. Data<br>represent mean and empirical variance of 1000 simulations for each<br>_N_. A function ![Mathematical equation: \hbox{$d_{\rm{obs}}(N) = \sqrt{D^2 + 9 A^2/N}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq203.png)<br>```<br>\hbox{$d_{\rm{obs}}(N) = \sqrt{D^2 + 9 A^2/N}$}<br>```<br> is fitted to the simulated data, with best-fit values<br> _A_ = 0.908 ± 0.002 _,D_ = (0.451 ± 0.001) × 10-2.<br> The expected dipole amplitude ( _d_ = 0.0046) is indicated by the<br> horizontal line. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F2) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 3 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig3_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F3.html) | [Fig. 3](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F3.html) <br>Ampliude bias for the estimator _d_ 2D on a hemisphere.<br>Data represent mean and empirical variance of 1000 simulations for each N. A<br>function ![Mathematical equation: \hbox{$d_{\rm{obs}}(N) = \sqrt{D^2 + 9 A^2/N}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq203.png)<br>```<br>\hbox{$d_{\rm{obs}}(N) = \sqrt{D^2 + 9 A^2/N}$}<br>```<br> is fitted to the simulated data, with best fit values<br> _A_ = 0.712 ± 0.003 and<br> _D_ = (0.444 ± 0.002) × 10-2. The dipole amplitude<br> (0.0046) is indicated by the horizontal line, the dipole vector is assumed to lie in<br> the equatorial plane (sin _ϑ_ d = 1). |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F3) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 4 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig4_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F4.html) | [Fig. 4](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F4.html) <br>Amplitude bias of the 3-dimensional estimator for the masked NVSS geometry of [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22). Data represent mean and empirical<br>variance of 1000 simulations for each _N_. A function<br>![Mathematical equation: \hbox{$d_{\rm{obs}}(N) = \sqrt{(KD)^2 + 9 A^2/N}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq268.png)<br>```<br>\hbox{$d_{\rm{obs}}(N) = \sqrt{(KD)^2 + 9 A^2/N}$}<br>```<br> is fitted to the simulated data, with best-fit values<br> _A_ = 0.883 ± 0.006,<br> _KD_ = (0.642 ± 0.005) × 10-2 and<br> _A_ = 0.847 ± 0.016,<br> _KD_ = (1.59 ± 0.008) × 10-2 for the expected kinetic<br> radio dipole and the radio dipole measured by [Blake\<br> & Wall (2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3), respectively. The simulated dipole amplitudes,<br> without masking, are indicated by the horizontal lines. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F4) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 5 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig5_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F5.html) | [Fig. 5](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F5.html) <br>Amplitude bias of the 2-dimensional estimator for the masked NVSS geometry of [Singal (2011)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R22). Data represent mean and empirical<br>variance of 1000 simulations for each _N_. A function<br>![Mathematical equation: \hbox{$d_{\rm{obs}}(N) = \sqrt{(KD)^2 + 9 A^2/N}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq268.png)<br>```<br>\hbox{$d_{\rm{obs}}(N) = \sqrt{(KD)^2 + 9 A^2/N}$}<br>```<br> is fitted to the simulated data, with best-fit values<br> _A_ = 0.810 ± 0.009,<br> _KD_ = (0.589 ± 0.008) × 10-2 and<br> _A_ = 0.745 ± 0.014,<br> _KD_ = (1.493 ± 0.006) × 10-2, for the expected kinetic<br> radio dipole and the dipole measured by [Blake\<br> & Wall (2002)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#R3), respectively. The simulated dipole amplitudes,<br> without masking, are indicated by the horizontal lines. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F5) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 6 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig6_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F6.html) | [Fig. 6](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F6.html) <br>Differential number counts of the NVSS catalogue,<br>_S_ min = 10 mJy, best fit values for<br>![Mathematical equation: \hbox{$f(s)=a \cdot s^{-\tilde x}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq305.png)<br>```<br>\hbox{$f(s)=a \cdot s^{-\tilde x}$}<br>```<br> with<br> 25 mJy < _S_ < 1000 mJy<br> are _a_ = 2.1 × 107 and<br> ![Mathematical equation: \hbox{$\tilde x=1.9$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq308.png)<br>```<br>\hbox{$\tilde x=1.9$}<br>```<br>. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F6) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 7 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig7_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F7.html) | [Fig. 7](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F7.html) <br>Map of the number counts in HEALPix pixels from NVSS. The pixel size corresponds<br>to _N_ side = 32\. Shown are equatorial coordinates at<br>epoch J2000. The NVSS contains data at<br>_δ_ > −40° and the Galactic<br>plane and a “counter galaxy” are masked (CG mask) in order to avoid Galactic<br>contamination and to restore point symmetry with respect to the zenith. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F7) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 8 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig8_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F8.html) | [Fig. 8](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F8.html) <br>Map of the number counts in HEALPix pixels from WENSS. The pixel size corresponds<br>to _N_ side = 32\. Shown are equatorial coordinates at<br>epoch B1950. The WENSS contains data at<br>_δ_ > 30° and the Galactic<br>plane and a “counter galaxy” are masked (CG mask) in order to avoid Galactic<br>contamination and to restore point symmetry with respect to the zenith. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F8) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 9 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig9_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F9.html) | [Fig. 9](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F9.html) <br>Differential number counts of the WENSS catalogue,<br>_S_ min = 5 mJy, best fit values for<br>![Mathematical equation: \hbox{$f(s)=a \cdot s^{-\tilde x}$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq305.png)<br>```<br>\hbox{$f(s)=a \cdot s^{-\tilde x}$}<br>```<br> with<br> 25 mJy < _S_ < 1000 mJy<br> are _a_ = 2.6 × 106 and<br> ![Mathematical equation: \hbox{$\tilde x=1.6$}](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-eq408.png)<br>```<br>\hbox{$\tilde x=1.6$}<br>```<br>. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F9) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 10 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig10_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F10.html) | [Fig. 10](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F10.html) <br>Histogram of dipole amplitudes for 100,000 simulations of the three dimensional<br>( _left_) and two dimensional ( _right_) estimator,<br>assuming the CMB expectation and a slope of _x_ = 1.1, with 185 649<br>( _left_) and 195 245 ( _right_) sources per simulation<br>and appropriate masks. The black vertical lines are the NVSS results of this work. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F10) |

|     |     |
| --- | --- |
| [![Thumbnail: Fig. 11 Refer to the following caption and surrounding text.](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13-fig11_small.jpg)](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F11.html) | [Fig. 11](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/F11.html) <br>Histogram of dipole amplitudes from 100 000 simulations for the dimensional<br>estimator, assuming the CMB expectation, a slope of _x_ = 0.8, 92,482<br>sources per simulation and the CG masking form for the WENSS catalogue. The black<br>vertical line is the WENSS result of this work. |
| [In the text](https://www.aanda.org/articles/aa/full_html/2013/07/aa21215-13/aa21215-13.html#F11) |

Current usage metrics show cumulative count of Article Views (full-text article views including HTML views, PDF and ePub downloads, according to the available data) and Abstracts Views on Vision4Press platform.

Data correspond to usage on the plateform after 2015. The current usage metrics is available 48-96 hours after online publication and is updated daily on week days.

Initial download of the metrics may take a while.

Click anywhere to hide the fullscreen overlay

──────── [TRUNCATED] ────────
Showing 37,410 chars (head) + 12,482 chars (tail) of 136,499 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/www.aanda.org-8b7ed29c47.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/www.aanda.org-8b7ed29c47.md" offset=601 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────