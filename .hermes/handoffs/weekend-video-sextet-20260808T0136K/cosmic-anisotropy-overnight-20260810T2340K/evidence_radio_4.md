URL: https://arxiv.org/pdf/2206.05624

# A Challenge to the Standard Cosmological Model

http://orcid.org/0000-0002-4902-8077 N ATHAN J. S ECREST , 1 http://orcid.org/0000-0002-6274-1424 S EBASTIAN VON H AUSEGGER , 2 http://orcid.org/0000-0001-5023-5631 M OHAMED R AMEEZ , 3 http://orcid.org/0000-0002-5944-3995 R OYA M OHAYAEE , 2, 4 AND http://orcid.org/0000-0002-3542-858X S UBIR S ARKAR2

1 2 3 2, 4
NATHAN J. SECREST, SEBASTIAN VON HAUSEGGER, MOHAMED RAMEEZ, ROYA MOHAYAEE, AND SUBIR SARKAR2

<sup>1</sup>*U.S. Naval Observatory, 3450 Massachusetts Ave NW, Washington, DC 20392-5420, USA*
<sup>2</sup>*Rudolf Peierls Centre for Theoretical Physics, University of Oxford, Parks Road, Oxford, OX1 3PU, United Kingdom*
<sup>3</sup>*Dept. of High Energy Physics, Tata Institute of Fundamental Research, Homi Bhabha Road, Mumbai 400005, India*
<sup>4</sup>*Sorbonne Universite, CNRS, Institut d’Astrophysique de Paris, 98bis Bld Arago, Paris 75014, France ´*

## ABSTRACT

We present the first joint analysis of catalogs of radio galaxies and quasars to determine if their sky distribution
is consistent with the standard CDM model of cosmology. This model is based on the cosmological principle,
which asserts that the universe is statistically isotropic and homogeneous on large scales, so the observed dipole
anisotropy in the cosmic microwave background (CMB) must be attributed to our local peculiar motion. We
test the null hypothesis that there is a dipole anisotropy in the sky distribution of radio galaxies and quasars
consistent with the motion inferred from the CMB, as is expected for cosmologically distant sources. Our
two samples, constructed respectively from the NRAO VLA Sky Survey and the Wide-field Infrared Survey
Explorer, are systematically independent and have no shared objects. Using a completely general statistic that
accounts for correlation between the found dipole amplitude and its directional offset from the CMB dipole, the
3
null hypothesis is independently rejected by the radio galaxy and quasar samples with *p*-value of 8*:* 9 10 and
<sup>5</sup>
1*:* 2 10, respectively, corresponding to 2*:* 6 and 4*:* 4 significance. The joint significance, using sample sizeweighted *Z*-scores, is 5*:* 1. We show that the radio galaxy and quasar dipoles are consistent with each other and
find no evidence for any frequency dependence of the amplitude. The consistency of the two dipoles improves
if we boost to the CMB frame assuming its dipole to be fully kinematic, suggesting that cosmologically distant
radio galaxies and quasars may have an intrinsic anisotropy in this frame.

$$
1.2\!\times\!10^{-5}
$$

$$
8.9\times10^{-3}
$$

## 1. INTRODUCTION

The CDM cosmological model is based on the isotropic
and homogeneous Friedmann-Lemaˆıtre-Robertson-Walker
(FLRW) metric, justified by the “cosmological principle”
that the universe on large scales must appear to be the same
to all observers, independent of their location (Milne1937).
According to the standard picture of the growth of structure
through gravitational instability, the distribution of matter on
1
cosmological scales (larger than <sup>1</sup>00*h* Mpc) reflects
the linear evolution of primordial adiabatic density pertur-
5
bations of amplitude 10 seen imprinted on the cosmic
1
microwave background (CMB). The large-scale distribution
of matter must therefore share the same “cosmic rest frame”
as the CMB (also called the “CMB frame”) in which the
Friedmann-Lemaˆıtre equations hold. As observed from the
arXiv:2206.05624v2  [astro-ph.CO]  12 Aug 2022
solar system barycentric frame, however, the CMB exhibits
3
a prominent dipole anisotropy with amplitude *D* 10,
which is attributed to our peculiar velocity with respect to this
frame. This motion is routinely corrected for in, for example,
analysis of the Hubble diagram of Type Ia supernovae, and in
estimation of the CDM model parameters from CMB data.

$$
\sim\,100\,h^{-1}\ \mathrm{M p c})
$$

$$
\sim10^{-5}
$$

$$
\mathcal{D}\:\sim\:10^{-3}
$$

The cosmological principle has served well as a simplifying assumption that made quantitative cosmology possible.
The inference that the universe is dominated by a cosmolog-
2
ical constant of *O*(*H₀*), however, rests crucially on this
assumption (see, e.g.,Sarkar2008); hence it is essential to
rigorously test it. The most direct way of doing so is to check
if the distribution of matter on cosmological scales is indeed
isotropic in the CMB frame. A model-independent method
for doing this was proposed byEllis & Baldwin(1984): consider an observer moving at velocity *v c* with respect to
an isotropic distribution of distant sources. Within the observer’s instrumental passband, the sources have a power-law
spectral energy distribution of the form *S /*, and the
apparent flux density *S* of the sources within this passband
x
has a cumulative power-law distribution *N* (*> S*) */ S*. If
the observer surveys the sky down to a specific flux density
above which the completeness of the survey is unbiased with
respect to direction, then relativistic aberration and Doppler
boosting of source emission in the observer’s frame will induce a dipole anisotropy in the sky distribution of sources
with amplitude (Ellis & Baldwin1984):

$$
\mathcal{O}(H_{0}^{2})
$$

$$
v\ll c
$$

$$
S\,\propto\,\nu^{-\alpha}
$$

$$
N(>S)\propto S^{-x}
$$

Corresponding author: Nathan J. Secrest

$$
\mathcal{D}=\left[2+x(1+\alpha)\right]\beta,
$$

(1)

nathan.j.secrest.civ@us.navy.mil

## mailto: nathan.j.secrest.civ@us.navy.mil nathan.j.secrest.civ@us.navy.mil

<sup>1</sup>*H₀* 100*h* km s<sup>1</sup>Mpc<sup>1</sup>is the present expansion rate, with *h ’* 0*:* 7.

where *v=c*. This is called the kinematic dipole, and
the null hypothesis is that the direction and amplitude of the

$$
\beta\equiv\,v/c
$$

$$
^{1}\,H_{0}\equiv100\,h\,\mathrm{k m\,s^{-1}M p c^{-1}}
$$ dipole of distant matter matches the direction of the CMB
2
dipole and the velocity inferred from its amplitude.

The minimum number of sources required to perform this
5
test is of *O*(10) (Ellis & Baldwin1984), which precluded
statistically significant constraints until the advent of the
1.4 GHz NRAO VLA Sky Survey (NVSS;Condon et al.
1998). This enabled the creation of large samples of radio
galaxies down to a completeness limit of 10 mJy, yielding several estimates of the radio galaxy dipole (Blake &
Wall2002;Singal2011;Gibelyou & Huterer2012;Rubart
& Schwarz2013;Tiwari & Jain2015;Colin et al.2017). All
of these studies found the radio dipole to be over a factor of 2
larger than the kinematic expectation, albeit with modest significance ( 2 3). The anomalously large NVSS dipole
has consequently been controversial, with some authors arguing that it is due to unidentified systematics in the data (e.g.,
Gibelyou & Huterer2012) or possibly a large bias factor for
radio galaxies at low redshift (e.g.,Tiwari & Nusser2016).
Complicating matters further, the 150 MHz TIFR GMRT Sky
Survey (TGSS;Intema et al.2017) appears to exhibit an even
larger dipole (e.g.,Bengaly et al.2018), motivating a recent
claim that the anomalous radio galaxy dipole is frequency
dependent (Siewert et al.2021).

$$
\mathcal{O}(10^{5})
$$

$$
(\sim2-3\sigma)
$$

Confirmation of an anomalously large dipole of distant
matter requires using data that is systematically independent
— not sharing the same instruments, survey design, or calibration method. This was accomplished bySecrest et al.
(2021), who used quasars selected with mid-IR photometry from the Wide-field Infrared Survey Explorer (WISE;
Wright et al.2010). The unique power of WISE data
to reliably select large, nearly all-sky samples of quasars
based on photometry alone was demonstrated bySecrest
et al.(2015), and the release of the CatWISE2020 catalog
(Marocco et al.2021), which contains much deeper photometry than the previous AllWISE release, enabled the construction of a cosmology-grade quasar catalog of 1.36 million objects. These have a mean redshift of *hzi* = 1*:* 2, with 99%
having *z >* 0*:* 1, thus precluding a significant contribution
from the local clustering dipole.Secrest et al.(2021) found
that the quasar dipole amplitude and direction, while similar
to the previous results from NVSS, reject the null hypothesis
7
with much higher statistical significance (*p* = 5 10, or
4*:* 9).

$$
\langle z\rangle=1.2.
$$

$$
z\,>\,0.1
$$

$$
(p=5\times10^{-7}
$$

To date, however, the dipoles of radio galaxies and quasars
have not been jointly analyzed. There are several important
motivations to do this. First, the methodology used to determine the significance of disagreement with the expected
kinematic dipole (e.g., treatment of survey systematics and
estimation of errors) varies considerably in the literature,
so a meta-analysis of published results can be misleading.
Second, there is some overlap in the populations of radio
galaxies and quasars that introduces correlation between results, motivating an analysis that explicitly removes shared

sources. Third, a joint analysis may reveal a consistent, common amplitude and direction for the radio galaxy and quasar
dipoles, which could be an important clue for cosmology.

In this Letter, we perform the first joint analysis of the
sky distributions of distant radio galaxies and quasars, which
independently provide the strongest constraints on the kinematic dipole of distant matter. In Section2, we carefully account for survey systematics, such as declination-dependent
sensitivity differences, as well as astrophysical systematics,
such as Galactic synchrotron emission and reddening, all of
which can introduce dependencies of source density on position. We assess the overlap between the radio galaxy and
quasar populations, and account for shared sources to produce completely independent samples. In order to remain
conservative and account for correlation between dipole positions and amplitudes, we also introduce a two dimensional,
completely generalized *p*-value to assess the null hypothesis.
Our results are given in Section3, wherein we also explore
if there is a dipole shared by the radio galaxy and quasar
populations. In the Appendix, we critically address related
results published in the literature since the publication ofSecrest et al.(2021), such as a possible frequency dependence
of the anomalously large dipole (Siewert et al.2021), a considerably larger dipole found in an older catalog of active
galactic nuclei (AGNs) from WISE (Singal2021), and a recent result (Darling2022) claiming consistency between the
radio galaxy dipole and the kinematic expectation. Our conclusions are presented in Section4.

## 2. GALAXY SAMPLES

In this work, we use radio galaxies from the NVSS
and quasars selected using mid-infrared photometry from
CatWISE2020. The former is composed of radio galaxies detected in 1.4 GHz continuum imaging taken with the
Very Large Array (VLA) in New Mexico, while the latter is composed of quasars detected in 3*:* 4 m (*W*1) and
4*:* 6 m (*W*2) imaging taken with WISE, in a polar low Earth
orbit. Being ground based, position-dependent systematics present in the NVSS depend on declination. Specifically, the NVSS used the compact VLA D configuration for
10 < decl: < +78 and the hybrid DnC configuration
for 40 < decl: < 10 and decl: > +78 . The NVSS
images are composed of individual pointings mosaicked together on a hexagonal grid, following lines of right ascension, and adjusting declination spacing to account for increasing overlap at high latitude. The WISE scanning pattern, on the other hand, is aligned with the ecliptic for Sun
avoidance, scanning the sky continuously in great circles that
converge at the ecliptic poles, using a scan mirror to compensate for the telescope’s motion during integrations. The
single exposure images are mosaicked onto a grid of 18,240
predefined tiles shared across the various WISE data releases,
with CatWISE2020 being the latest.

$$
3.4\,\mu\mathrm{m}
$$

$$
-10^{\circ}<,
$$

$$
<+78^{\circ}
$$

$$
-40^{\circ}<<\mathrm{d e c l.}<-10^{\circ}
$$

$$
>+78^{\circ}
$$

While the NVSS and WISE catalogs are independent, the
systematics present in each must nonetheless be carefully addressed. This is done primarily by developing sky masks
to mitigate instrumental systematics such as source confu-

<sup>2</sup>Throughout this work, we use *v* = 369*:* 82 0*:* 11 km s<sup>1</sup>towards (*l; b*) =
(264*:* 021*;*48*:* 253) (Planck Collaboration et al.2020).

---

sion, image artifacts, and survey footprint limitations, as well
as astrophysical systematics such as diffuse Galactic synchrotron that may affect the purity and uniformity of an extragalactic source catalog. Additionally, each catalog has an effective sensitivity limit, generally set by a position-dependent
survey depth, which must be controlled for. In the following sections, we discuss the masks and flux density cuts developed for the NVSS and WISE catalogs. We use the Hierarchical Equal Area isoLatitude Pixelization (HEALPix;
3
Gorski et al. ´ 2005) scheme to bin dipole-subtracted source
density by declination, ecliptic latitude, Galactic synchrotron
emission, and other systematics of interest to ensure that the
source density of the masked catalog does not show any
trends with these systematics. Bin sizes are chosen to be
2
large enough to calculate the reduced and reduce the statistical dispersion, but small enough that any trends present
2
are not under-sampled. The reduced is defined as:

$$
\chi^{2}
$$

$$
\chi^{2}
$$

$$
\chi^{2}/\mathrm{d f}=\frac{1}{N-k}\sum_{i}^{N}\frac{(\rho_{i}-f_{i})^{2}}{\sigma_{\rho_{i}}^{2}/n_{i}}
$$

(2)

where<sub>i</sub>is the mean source density in bin *i*, *f*<sub>i</sub>is the value
of the functional fit for that bin,<sup>i</sup>is the dispersion of
within bin *i*, *n*<sub>i</sub>is the number of sky pixels in the bin, and
*k* is the number of parameters corresponding to *f*<sub>i</sub>. For example, the linear model fit with respect to ecliptic latitude
used to de-trend the WISE sample (Section2.2) has *k* = 2.
In checking the residuals of source density, is replaced by
the residuals after subtraction of the dipole and monopole, so
*f*<sub>i</sub>= 0 and *k* = 1. We find that requiring 200 pixels per bin
for *N*<sub>side</sub>= 64 is a good compromise, although our results
are not sensitive to changes in bin counts, and remain consistent if we use uniform bins and allow the number of pixels per bin to vary. We test for systematic trends in declination, ecliptic latitude, Galactic dust reddening, diffuse Galactic synchrotron emission, Galactic latitude, and supergalactic
latitude. We use thePlanck Collaboration et al.(2014) map
for dust, and the de-striped and source-subtracted version of
theHaslam et al.(1982) 408 MHz all-sky map made byRemazeilles et al.(2015) for synchrotron emission.

$$
\rho_{i}
$$

$$
i, f _ {i}
$$

$$
\sigma_{\rho_{i}}
$$

$$
n_{i}
$$

$$
\rho
$$

$$
k
$$

$$
f_{i}
$$

$$
k=2
$$

$$
\rho
$$

$$
f_{i}=0
$$

$$
k=1
$$

$$
N_{\mathrm{s i d e}}\,=\,64
$$

## 2.1. NVSS

Using the full NVSS catalog, we identify highly localized
( 1 scales) source concentrations that we use to produce a
list of circular mask regions, setting the radii to fully encompass the concentration. As expected, these regions are generally within a few degrees of the Galactic plane, although
some regions at high Galactic latitude were also identified,
which are likely image artifacts near particularly bright radio
sources such as M87. For less distinct artifact concentrations
near the Galactic center, we use the diffuse synchrotron map
and mask all pixels with a mean brightness temperature of
50 K or higher. In total, 27% of the sky was masked.

$$
1^{\circ}
$$

With the masking complete, the next step is to determine
the flux density cut. Using simulated point sources,Condon et al.(1998) determined the 100% source completeness limit of the NVSS to be 4 mJy. Using this flux density cut, however, there may still be some residual declination dependence of the catalog sensitivity, although at low
2
statistical significance ( *=*df = 1*:* 4). Cutting at 10 mJy re-
2
moves this potential systematic ( *=*df = 1*:* 1). We see no
evidence for source density dependence on any of the poten-
2
tial systematics we tested, with *=*df ranging from 0.95 to
1.3 for *E*(*B V*), Galactic synchrotron, or any of the principal latitudes (declination and ecliptic/Galactic/supergalactic
latitude). This flux cut leaves 508,144 sources in the masked
map. We show the NVSS sample in Figure1, top.

$$
(\chi^{2}/\mathrm{d f}=1.4)
$$

$$
(\chi^{2}/\mathrm{d f}\,1\ =\,1.1)
$$

$$
E(B-V)
$$

$$
\chi^{2}/\mathrm{d f}
$$

## 2.2. WISE Quasars

InSecrest et al.(2021), we developed a mid-IR quasar
sample from the CatWISE2020 catalog, which is deeper
and more uniform than the AllWISE catalog because of inclusion of data from the NEOWISE Reactivation mission
(Mainzer et al.2011,2014). This catalog was built using the
*W* 1 *W* 2 0*:* 8 cut ofStern et al.(2012) that reliably picks
AGN-dominated objects, and a flux cut of W 1 < 16: 4 mag
for uniform sensitivity across the sky. Objects below an absolute Galactic latitude of 30 were excluded because of the
drop in sky pixel density due to source confusion near the
Galactic plane. A slight inverse linear trend was also observed between ecliptic latitude and sky density, which is potentially attributable to two effects. First, deeper coverage
near the ecliptic poles increases sensitivity to faint sources
that, while excluded by our flux cut, may cause deblending
issues with brighter sources and lead to a loss of completeness. Second, shallower coverage near the ecliptic equator
may lead to AGNs slightly bluer than *W* 1 *W* 2 0*:* 8 scattering red-ward due to photometric error, increasing apparent
source density if bluer AGNs are more common, as is implied
in Figure 2 ofSecrest et al.(2021). A detailed characterization of these effects is beyond the scope of this work; for our
purposes it suffices that the ecliptic latitude trend is easy to
correct for.

$$
2011,2014)
$$

$$
W1-W2\geq0.8
$$

$$
W1<16.4
$$

$$
30^{\circ}
$$

$$
W1-W2\geq0.8
$$

We retain the *jbj* 30 Galactic plane cut used bySecrest et al.(2021), as well as the source mask, but with a
minor revision: we found that some of the sky areas masked
inSecrest et al.(2021) were either not optimally centered on
the region of interest (e.g., diffraction spikes around bright
stars), or were over-masked (i.e., with too large a radius). We
manually reevaluated every region outside the Galactic plane
cut, of which there are 48 in the updated mask. Including the
Galactic plane cut, 51% of the sky was masked. Repeating
the tests done on the NVSS sample, we find minimal unexplained variance in source density as a function of the prin-
2
cipal latitudes or Galactic foregrounds, with *=*df ranging
from 0.8 to 1.4. In performing these tests, we found that the
flux density cut used inSecrest et al.(2021) can safely be
relaxed slightly to W 1 < 16: 5 mag (S > 0: 078 mJy; see
Section 2 ofSecrest et al.2021, for how *W*1 magnitudes are
converted to flux densities).

$$
|b|\,\geq\,30^{\circ}
$$

$$
\chi^{2}/\mathrm{d f}
$$

$$
W1\,<\,16.5
$$

$$
(S\,>\,0.078
$$

<sup>3</sup>https://healpix.sourceforge.io

---

**Figure 1.** Top: Density map of the NVSS-based radio galaxy sample used in this work, in Galactic coordinates, Mollweide projection. The
right plot is the smoothed map, using a 1 rad moving average, showing the underlying dipole signal. Bottom: Corresponding maps of the
WISE-based quasar sample used in this work. The smoothed maps are only for visual purposes and were not used in our analysis.

We wish to determine the significance with which the
NVSS and WISE dipoles independently reject the null hypothesis. These catalogs must therefore not contain the same
objects. To this end, we match the full NVSS catalog to the
00
full CatWISE2020 catalog using a 40 match tolerance, chosen for completeness given the astrometric uncertainties of
00
NVSS that imply offsets of about 5 on average. We find
that 99*:* 7% of the NVSS sources have a counterpart in the full
00
CatWISE2020 catalog, with 99% of matches within 20.
Nonetheless, only 1*:* 4% of the WISE quasars are in the NVSS
sample, likely because radio-selected AGNs tend to have low
accretion rates (e.g.,Sikora et al.2007) and be hosted by
luminous elliptical galaxies, while mid-IR AGNs are bolometrically dominant, and preferentially reside in bluer, less
clustered galaxies (e.g.,Hickox et al.2009). Indeed, using a
sample of AGNs selected with the same WISE color cut we
employ here and a catalog of VLA sources from the COS-
MOS field,Stern et al.(2012) find that only 2% of WISEselected AGNs are radio-loud, consistent with what we find
here. By performing a joint analysis on radio-selected and
infrared-selected AGNs, we are therefore testing two almost
entirely different populations of objects, each with its own
host galaxy type and environment. We removed the small
fraction of the quasar sample that have counterparts in the
NVSS sample, and further removed random WISE quasars

$$
40^{\prime\prime}
$$

$$
\sim5^{\prime\prime}
$$

$$
\sim20^{\prime\prime}
$$

from regions of the sky not shared by the NVSS sample in
order to maintain uniformity. This results in a total of 1.6 million WISE quasars, shown in Figure1, bottom.

## 2.3. Testing the Null Hypothesis

InSecrest et al.(2021), we simulated the kinematic dipole
by applying relativistic aberration and Doppler boosting to
individual sources, expressed as directional vectors, which
were then converted into HEALPix maps. In this work, we
use a method of simulating the kinematic dipole directly in
sky pixel space, which is computationally much more efficient and allows a wide range of statistical tests. Our method
identifies the equal areas of the sky pixels as the differential
solid angle *d*. Then, each sky pixel *m*<sub>i</sub>has a Doppler factor
*i*:

$$
m_{i}
$$

$$
\delta_{i},
$$

$$
\delta_{i}=\gamma(1+\beta\cos\theta_{i})
$$

(3)

2 1=2
where (<sup>1</sup>), and<sub>i</sub>is the angular offset of
sky pixel *m*<sub>i</sub>from the velocity vector corresponding to the
CMB frame. The expected number count within each pixel
2
is enhanced by times the monopole *M*, which is furx(1+)
ther boosted by source brightening, which goes as.
Putting these together, the expected value of a sky pixel *m*<sub>i</sub>
modified by relativistic aberration and Doppler boosting is:

$$
\gamma\,\equiv\,(1-\,\beta^{2})^{-1/2}
$$

$$
\theta_{i}
$$

$$
m_{i}
$$

$$
\delta^{2}
$$

$$
\delta^{x(1+\alpha)}
$$

---

$$
m_{i}=\delta_{i}^{2+x(1+\alpha)}\mathcal{M}
$$

(4)

Simulated skies are created by using the non-masked sky pixels *m*<sub>i</sub>as the expectation values for random sampling from a
Poisson distribution (shot noise).

$$
m_{i}
$$

Because variance in pixel counts due to relativistic aberration and Doppler boosting occurs at the flux limit of the catalog, the value of and *x* used should be the values at this flux
limit. As has been noted for the NVSS previously (e.g.,Colin
et al.2017), a single value of the power-law index *x* is not
sufficient to describe the integral source counts, being flatter
at the faint end and becoming steeper at higher flux densities.
We fit the faint end near the flux cut, finding *x* = 0*:* 77. As
the NVSS was observed at a single frequency, we do not have
separately for each object. However, the population mean
in each pixel is the relevant quantity and this is expected to
be very near the typical synchrotron value 0*:* 75. We
tested the effect of allowing to have a dispersion of 0.4, estimated from a match to the lower-frequency SUMSS catalog
1=2
(Mauch et al.2003), with each pixel varying as 0*:* 4 *m*<sup>i</sup>.
We find that the effect of not knowing for each individual
source is negligible. For the WISE catalog we do have for
each source, with a mean value of 1.06 at the 0.078 mJy flux
density limit, and we find that *x* = 1*:* 89. For this sample we
include the small uncertainty of the ecliptic latitude correction in the null sky simulations by dividing the expectation
map by a permutation of the correction for each simulation,
with each permutation being drawn from the fit covariance
matrix of the correction. The best-fit correction is used in the
fit, maintaining fidelity to counting statistics.

$$
x=0.77
$$

$$
\alpha\,\sim\,0.75
$$

$$
0.4\,m_{i}^{-1/2}.
$$

$$
x=1.89
$$

To fit dipoles, we used a modified version of the Healpy
fit dipole function, which uses the linear algebra routines in NumPy. Our version optimizes memory usage to enable large Monte Carlo simulations to be run efficiently. The
expectation value maps generated using Equation4have fit
dipoles with amplitudes in agreement with Equation1(El-
2
lis & Baldwin1984), which predicts *D* = 0*:* 41 10 for
<sup>2</sup>
NVSS and *D* = 0*:* 73 10 for WISE. We quote formal uncertainties on dipole fit parameters by permuting the masked
maps with shot noise, propagating the uncertainties of any
additional terms such as the ecliptic latitude trend seen in
WISE.

$$
\mathtt{f i t\_d i p o l e}
$$

$$
\mathcal{D}=0.\check{41}\times10^{-2}
$$

$$
\mathcal{D}=0.73\times10^{-2}
$$

InSecrest et al.(2021), the definition of the *p*-value was
the fraction of simulated skies with dipole amplitudes exceeding the kinematic expectation and with directions within
the offset between the CMB dipole and the found quasar
dipole. This was motivated by the fact that simulated dipoles
at larger offsets are more likely to have a significant contribution from the “noise” dipole, which can increase their amplitudes. However, the amplitude and offset of simulated skies
are correlated, with higher amplitudes generally exhibiting
smaller offsets, so a found dipole with smaller amplitude but
larger offset could be equally as inconsistent with the null
hypothesis as one with larger amplitude and smaller offset.

In this work, we therefore adopt a completely general
definition of the *p*-value. Null sky simulations fill a 2-

dimensional space in dipole amplitude and offset, allowing
for an estimate of the joint probability distribution. The
found dipole exists along a contour of equal probability density, and the*p*-value is the fraction of null skies outside of this
contour. There will be a larger fraction of null skies meeting
this criterion, so the *p*-value will be larger (less significant).
Our generalized approach is therefore the most conservative.

## 3. RESULTS

We find an NVSS dipole amplitude of *D* = (1*:* 23 0*:* 25)
<sup>2</sup>
10, exceeding the kinematic expectation by a factor of
about 3, in the direction (*l;b*) = (196 13*;*+46 10 ),
45 away from the CMB dipole, with a 95% upper confidence limit (CL) positional uncertainty of 30 . Testing the
6
null hypothesis with 10 simulated skies, we find it is re-
3
jected with a *p*-value of 8*:* 9 10, or 2*:* 6 (Figure2, left).
2
For WISE, we find *D* = (1*:* 48 0*:* 16) 10, exceeding
the kinematic expectation by a factor of about 2, in the direction (*l;b*) = (238 7*;*+31 5 ), 26 away from the
CMB dipole, with a 95% CL positional uncertainty of 15 .
8
We performed 10 null sky simulations, finding a *p*-value of
<sup>5</sup>
1*:* 2 10, which corresponds to 4*:* 4 (Figure2, right). We
note that the conversion from *p*-value to is two-sided, so
that the point of highest probability density corresponds to
0.

$$
\mathcal{D}=(1.23\!0.25)\times
$$

$$
10^{-2}
$$

$$
(l,b)=\left(190^{\circ}\pm10^{\circ},+40^{\circ}\pm10^{\circ}\right)
$$

$$
45^{\circ}
$$

$$
10^{6}
$$

$$
30^{\circ}
$$

$$
8.9\times10^{-3}
$$

$$
\mathcal{D}=(1.48\pm0.16)\times10^{-2}
$$

$$
(l,b)=(23\ ^{0circ}pm^{{\circ}},+31^{\circ}\pm5^{\circ}),20^{\circ}
$$

$$
15^{\circ}
$$

$$
10^{8}
$$

$$
1.2\times10^{-5}
$$

Because each sample has its own particular mask, it is not
straightforward to combine them to determine the joint significance with which the null hypothesis is rejected. Moreover, each sample has a different expected dipole amplitude
under the null hypothesis, further complicating a single, combined test. However, the joint significance may be estimated
using the weighted *Z*-score:
P

$$
Z_{\mathrm{j o i n t}}={\frac{\sum_{i}w_{i}Z_{i}}{\sqrt{\sum_{i}w_{i}^{2}}}}
$$

(5)

where *w*<sub>i</sub>are the sample weights, in this case the square roots
of the sample sizes (0.5 million for NVSS and 1.6 million
for WISE), and *Z*<sub>i</sub>are the *Z*-scores of each sample independently, respectively 2*:* 6 and 4*:* 4. This gives *Z*<sub>joint</sub>= 5*:* 1, or
a joint significance of 5*:* 1 with which the kinematic expectation inferred from the CMB dipole in the standard cosmological model is rejected.

$$
w_{i}
$$

$$
Z_{i}
$$

$$
Z_{\mathrm{j o i n t}}=5.1
$$

We note that, unlike inSecrest et al.(2021) we have not
preserved the coupling of source fluxes and spectral indices,
instead using the relevant values at the flux density limit of
our catalog ( = 1*:* 06, *x* = 1*:* 89). Repeating our methodology on the sample fromSecrest et al.(2021) and defin-
7
ing the *p*-value in the same way, we get *p* = 3 10,
consistent with our previous result. This indicates that the
effect of any correlation between and *x*, as suggested by
Dalang & Bonvin(2022), is inconsequential for our results.
There is likewise no evidence for a significant difference in
and *x* between the hemispheres pointing towards the CMB
dipole and away from it, as would be expected in this scenario. The spectral index at the flux density limit is = 1*:* 06
for both hemispheres in WISE, with uncertainties below the

$$
(\alpha=1.06,\,x=1.89)
$$

$$
p\;=\;3\,\times\,10^{-7}
$$

---

**Figure 2.** Distribution of CMB dipole offsets and kinematic dipole amplitudes of simulated null skies for the NVSS catalog (left) and WISE
(right). Contours of equal *p*-value (scale on right y-axis), translated to equivalent are given (where the peak of the distribution corresponds to
0), with the found dipoles marked with the + symbol and their *p*-value in the legends.

given precision. The values of *x* in the towards/away hemispheres are 0.77/0.77 for NVSS, and 1.90/1.89 for WISE.
The small difference in *x* for WISE is consistent with fitting
error, and makes a negligible difference in the expected kinematic dipole amplitude.

$$
x
$$

As the dipoles in the large scale distribution of radio galaxies and of quasars independently reject the null hypothesis,
we can ask if these two dipoles are consistent with each
other and, if so, combine them to determine their common
or shared dipole. We repeated the kinematic expectation
test for a given input dipole amplitude and direction to de-
6
termine the distribution in amplitude and offset. Using 10
simulations, we find that the input dipole that is most consistent with the NVSS and WISE dipoles is their vector
2
mean: *D* = (1*:* 40 0*:* 13) 10, pointed at (*l;b*) =
(233 6*;*+34 5 ), 27 offset from the CMB dipole,
with a 14 positional uncertainty at the 95% CL. The corresponding *p*-value is 0*:* 72 for WISE and 0*:* 09 for NVSS, indicating that the NVSS and WISE dipoles are indeed consistent
with each other, albeit with some tension in the NVSS sample. If we additionally assume that the CMB dipole is fully
kinematic in origin, then the NVSS and WISE dipoles will
each have a different kinematic contribution (with amplitudes
2 2
*D* = 0*:* 41 10 and *D* = 0*:* 73 10, respectively), which
can be removed from the samples using Equation4. Doing
this and repeating the above test yields a residual common
2
dipole with amplitude *D* = (0*:* 86 0*:* 14) 10, pointing towards (*l;b*) = (217 10*;*+20 7 ), 48 from the
CMB dipole direction, with a 95% CL position uncertainty of
22 . The corresponding *p*-values are 0*:* 94 for WISE and 0*:* 30
for NVSS, improving consistency and alleviating the tension

$$
10^{6}
$$

$$
\mathcal{D}\,=\,(1.40\pm0.13)\times10^{-2}
$$

$$
(l,b)\ =\\
$$

$$
(233^{\circ}\pm6^{\circ},+34^{\circ}\pm5^{\circ}),27^{\circ}
$$

$$
14^{\circ}
$$

$$
\mathcal{D}=0.41\!\times\!10^{-2}
$$

$$
\mathcal{D}=0.73\!\times\!10^{-2}
$$

$$
\mathcal{D}=(0.86\pm0.14)\times10^{-2}
$$

$$
(l,b)=(217^{\circ}\pm10^{\circ},+20^{\circ}\pm7^{\circ}),48^{\circ}
$$

$$
22^{\circ{}}
$$

with NVSS. This tantalizing result suggests that if the solar system barycenter is indeed traveling in the direction of
1
the CMB dipole at 370 km s, then the space distribution
of cosmologically distant radio galaxies and quasars has an
intrinsic dipole anisotropy in that frame.

$$
\mathrm{s}^{-1}
$$

We reiterate that the two catalogs are completely independent of each other, not only systematically but also in terms
of the objects they contain. The dipoles of radio galaxies and
quasars are thus both larger than the kinematic expectation
from the CMB dipole, but consistent with a common dipole
which points 27 away from the direction of the CMB dipole
as observed, or 48 away if the kinematic expectation is removed. Note that, according toMurray(2022), the effect of
gravitational lensing by the structures responsible for the local bulk flow is negligible for the dipole in cosmologically
distant source counts.

Finally, since the NVSS and WISE samples were acquired
at frequencies differing by nearly 5 orders of magnitude,
their consistency disfavors any frequency dependence of the
anomalous dipole as claimed bySiewert et al.(2021). We
discuss this claim in AppendixA.1and show that it can be
attributed to known flux calibration issues in the 150 MHz
TIFR GMRT Sky Survey catalog (TGSS-ADR1Intema et al.
2017).

$$
27^{0}
$$

$$
48^{\circ}
$$

## 4. CONCLUSIONS

We have explored the dipoles in the sky distributions
of two large, independent, samples of radio galaxies and
quasars, constructed from the NVSS and WISE catalogs. Our
principal conclusions are as follows:

---

1.Using a common methodology and a completely generalized *p*-value, the large dipole anisotropies seen
in radio galaxies and quasars independently reject, at
2*:* 6 and 4*:* 4 respectively, the null hypothesis that the
dipoles arise due to Doppler boosting and relativistic
1
aberration with velocity 370 km s in the direction
of the CMB dipole. The found dipole amplitudes are
about 3 and 2 times larger than the respective kinematic expectations, and point 45 and 26 away from
the CMB dipole. The joint significance of this rejection of the cosmological principle is 5*:* 1.

$$
p^{-}
$$

$$
\mathrm{s}^{-1}
$$

$$
26^{\circ}
$$

$$
45^{\circ}
$$

2.These anomalously large dipoles are statistically consistent with a single, shared dipole of distant galaxies
2
and quasars, with amplitude *D* = (1*:* 40 0*:* 13) 10
in the direction (*l;b*) = (233 6*;*+34 5 ). We
find no evidence for a frequency dependence of the amplitude.

$$
\mathcal{D}=(1.40\pm0.13)\,\times\,10^{-2}
$$

$$
(l,b)=(233^{\circ}\pm6{{mathrm{0}}},+34^{\circ}\pm5^{\circ})
$$

3.The agreement between the radio galaxy and quasar
dipoles improves if the standard kinematic expectation is subtracted out, yielding a dipole of amplitude
2
*D* = (0*:* 86 0*:* 14) 10 in the direction (*l;b*) =
(217 10*;*+20 7 ). This may be interpreted as an
intrinsic over-density of galaxies and quasars on very
large scales, in a direction 48 away from the CMB
dipole.

$$
\mathcal{D}=(0.86\pm0.14)\times\dot{10^{-2}}
$$

$$
(l,b)=
$$

$$
(217^{\circ}{\pm}10^{\circ},+20^{\circ}{\pm}7^{\circ})
$$

$$
48^{\circ}
$$

These findings present a significant challenge to the cosmological principle and, by extension, the standard FLRW
cosmological model. A better understanding of the anomalously large dipole of radio galaxies and quasars will require
dedicated studies using data from ongoing surveys such as
the Dark Energy Spectroscopic Instrument and the forthcoming Rubin Observatory Legacy Survey of Space and Time,
as well as the Square Kilometre Array and the Euclid satel-

lite. These data will enable the matter dipole to be traced
as a function of redshift — from *z*. 0*:* 1 where it can have
a significant “clustering dipole” contribution from structure
— out to moderate *z* where the kinematic dipole due to our
local motion should prevail if the universe is indeed homogeneous and isotropic on large scales. Such tomographic studies may reveal if and how the observed anomalously large
matter dipole is linked to our local bulk flow, which is also
anomalous in extending deeper than is expected in the standard CDM model of structure formation. Measurement
of fluxes along with number counts will provide additional
means to differentiate contributions to the matter dipole (Tiwari et al.2015;Nadolny et al.2021).

$$
z\lesssim0.]
$$

We thank the anonymous referee for their helpful review of
our paper. SvH acknowledges support from the Carlsberg
Foundation. The authors additionally thank Camille Bonvin, Enzo Branchini, Jacques Colin, Charles Dalang, Jim
Peebles, Jean Souchay, and Jenny Wagner for helpful discussions. The National Radio Astronomy Observatory is a
facility of the National Science Foundation operated under
cooperative agreement by Associated Universities, Inc. This
publication makes use of data products from the Wide-field
Infrared Survey Explorer, which is a joint project of the University of California, Los Angeles, and the Jet Propulsion
Laboratory/California Institute of Technology, funded by the
National Aeronautics and Space Administration. Some of the
results in this paper have been derived using the healpy and
HEALPix package.


[... middle omitted — see footer ...]

reduces the sample size. Nonetheless, this discrepancy warrants investigation.

$$
W1\,<\,15.
$$

We first checked that the dipole estimator used inSingal
(2021) gives results consistent with ours by reproducing their
result using theSecrest et al.(2015) catalog and applying the
same cuts, 12 < W1 < 15 and jbj 15 . Because of
the small sample size (0.28 million), we used *N*<sub>side</sub>= 32,

$$
12\,<\,W1\,<\,15
$$

$$
|b|\,\geq\,15^{\circ}
$$

$$
N_{\mathrm{s i d e}}\,=\,32.
$$

---

9

which gives a monopole of 31 sources per sky pixel. We
2
find *D* = 3*:* 1 10, with a direction within 12 of that
found bySingal(2021). This offset may be attributable to
slight differences in the sample resulting from how the sky is
masked when working with sky pixels versus source vectors.

$$
\mathcal{D}\,=\,3.1\times10^{-2}
$$

$$
12^{\circ}
$$

Having obtained a consistent result, we now explore systematics in this sample. The first is the presence of stripes of
reduced sensitivity along certain ecliptic lines of longitude
evident in Figure 1 ofSingal(2021). We identify 4 stripes
at ecliptic longitudes 10 < < 14 , 238 < < 242 ,
313 < < 317 , and 342 < < 346 . Masking these,
2
the dipole amplitude drops to *D* = <sup>2</sup>*:* 6 10. We also find
that, although the sample does not exhibit the linear ecliptic latitude trend of the deeper CatWISE2020-based sample,
it does show a steep drop off in source density at the ecliptic poles beyond *j j* & 70 (Figure4, top). Making this
cut mitigates source density dependence on ecliptic latitude,
although it has a minor effect on the dipole, reducing it to
2
*D* = <sup>2</sup>*:* 5 10. Finally, there is a clear downward trend
in source density at lower Galactic latitudes in theSecrest
et al.(2015) sample (Figure4, bottom), which is likely due
to differences in the source detection algorithms employed
for producing the AllWISE and CatWISE2020 catalogs. The
latter is based on source detections from the unWISE catalog (Schlafly et al.2019) which performs better in crowded
regions such as the Galactic plane and ecliptic poles. Consequently, while a cut of *jbj >* 30 was sufficient to remove
dependence on Galactic latitude in the CatWISE2020 sam-
<sup>2</sup>
ple ( *=*df = 1*:* 2), a cut of *jbj >* 45 is required for the
2
AllWISE-based sample ( *=*df = 1*:* 8). This leaves 0.11 mil-
2
lion sources with *D* = 1*:* <sup>2</sup> 10, pointing 74 from the
CMB dipole and 85 from the CatWISE2020 dipole.

$$
10^{\circ}<\lambda<14^{\circ},238^{\circ}<\lambda<242^{\circ}
$$

$$
313^{\circ}<\lambda<317^{\circ}
$$

$$
342^{\circ}<\lambda<346^{\circ}
$$

$$
\mathcal{D}=2.6\times10^{-2}
$$

$$
|\dot{\beta}|\gtrsim70^{\circ}
$$

$$
\mathcal{D}=2.5\times10^{-2}
$$

$$
|b|>30
$$

$$
(\chi^{2}/\mathrm{d f}\:=\:1.2)
$$

$$
|b|\,>\,45
$$

$$
\mathcal{D}=1.2\times10^{-2}
$$

$$
(\chi^{2}/\mathrm{d f}\ \ dot==18.)
$$

$$
74^{\circ}
$$

$$
85^{\circ}
$$

We conclude that, once survey and source detection systematics have been accounted for, the AllWISE-based AGN
sample employed inSingal(2021) does not exhibit a significantly larger dipole than the CatWISE2020-based quasar
sample that we have used in this work, which has 15 times
as many sources. As a check, we added the de-striping mask
to the CatWISE2020 sample, but found it has a negligible
2
impact, resulting in an amplitude *D* = 1*:* 5 10 and a shift
in direction of 3 .

$$
\mathcal{D}=1.5\times10^{-2}
$$

$$
3^{\circ}
$$

## A.3. VLA Sky Survey and Rapid ASKAP Continuum Survey

Recently,Darling(2022) presented an analysis of the radio
galaxy dipole in the 3 GHz VLA Sky Survey (VLASS;Lacy
et al.2020) combined with the 0.9 GHz Rapid ASKAP Continuum Survey (RACS;McConnell et al.2020), claiming
agreement with the kinematic expectation. We examine this
result below but first note two issues.Darling(2022) determines consistency with the kinematic expectation by fitting
the dipole amplitude and direction, correcting for bias where
needed, and employs bootstrap resampling to determine uncertainties. The dipole of the joint VLASS+RACS catalog
is found to be consistent with the kinematic expectation, although it is acknowledged that their result is not inconsistent withSecrest et al.(2021) either. In the present paper,
the effect of counting statistics and masking, along with any

**Figure 4.** Top: drop in source density near ecliptic poles in the
AllWISE-based AGN catalog used bySingal(2021). Bottom: trend
with Galactic latitude. The dashed lines denote the cuts we employ
to account for these effects.

possible bias in the estimator, is fully accounted for in the
null sky simulations, so the formal significance of our results is unaffected. This is a major motivation for our approach, as opposed to attempting to determine uncertainties
and bias factors on the best-fit dipole amplitudes and directions, and working backwards to determine agreement with
the kinematic expectation (as was done inDarling2022, and
elsewhere). Moreover, combining radio catalogs made at different frequencies is inherently problematic, as for a given
flux limit a higher frequency catalog will preferentially select flat-spectrum sources, while a lower frequency catalog
will preferentially select steep-spectrum sources, so the assumption of a characteristic, aggregate spectral index in the
joint catalog may not be valid. This, and other observational
systematics that may vary between the two catalogs, is the
reason why we did not join the NVSS with other catalogs,
such as SUMSS (as was done inColin et al.2017).

Nonetheless, theDarling(2022) result deserves examination. Using the VLASS and RACS catalogs, we reproduced
their joint catalog of 711,450 sources. Taking = 0*:* 98
and *x* = 1*:* 0 as in that work, we find a dipole amplitude

---

10

2
of *D* = 0*:* 49 10, in agreement with the kinematic expectation. The direction is (*l;b*) = (284*;*43 ), offset from the
direction found byDarling(2022) using a similar estimator,
but within 15 of the CMB dipole.

$$
\mathcal{D}=0.49\times10^{-2}
$$

$$
(l,b)=(284^{\circ},43^{\circ})
$$

$$
15^{\circ}
$$

However, if the VLASS and RACS catalogs are jointly
consistent with the kinematic expectation, then they should
also be individually consistent, accounting for their source
counts and sky masks. The advantage of our methodology
is that it is straightforward to test this, by simulating skies
according to the kinematic expectation, masking them identically, and then determining how consistent the found dipole
directions and offsets are with expectations. For VLASS,
2
we find *D* = 1*:* 0 10, 80 from the CMB dipole, and
6
a *p*-value of 0.07 using 10 simulations, in tension with the
kinematic expectation. For RACS, which has larger over-

$$
\mathcal{D}\,=\,1.0\times10^{-2}
$$

$$
{\mathcal{D}}\ =
$$

all sky coverage (63% vs. 56% for VLASS), we find *D* =
2
1*:* 5 10, 4<sup>2</sup> from the CMB dipole, and a*p*-value of 0.003,
which is inconsistent with the kinematic expectation.

$$
10^{6}
$$

$$
1.5\!\\times\\!\\dot{100^{-2}},4\tilde{2^{\circ}}
$$

Thus, while the joint catalog appears to be consistent with
the kinematic interpretation of the CMB dipole, at least one
of the individual catalogs is not, and it is possible that the ostensible overall consistency with the kinematic expectation
is a coincidence of the particular distributions of sources in
each catalog. Indeed,Darling(2022) notes that, when tested
individually, the VLASS dipole points towards the south
equatorial pole ( 75 from the CMB dipole) with an ampli-
1
tude corresponding to 683 km s, while the RACS dipole
is closer in direction to the CMB dipole ( 42 ) but with an
1
amplitude corresponding to 644 km s.

$$
(\sim75^{\circ}
$$

Astropy Collaboration, Price-Whelan, A. M., Sipocz, B. M., et al. ˝
2018, AJ, 156, 123, doi:10.3847/1538-3881/aabc4f
Bengaly, C. A. P., Maartens, R., & Santos, M. G. 2018, JCAP,
2018, 031, doi:10.1088/1475-7516/2018/04/031
Blake, C., & Wall, J. 2002, Nature, 416, 150, doi:10.1038/416150a
Colin, J., Mohayaee, R., Rameez, M., & Sarkar, S. 2017, MNRAS,
471, 1045, doi:10.1093/mnras/stx1631
Condon, J. J., Cotton, W. D., Greisen, E. W., et al. 1998, AJ, 115,
1693, doi:10.1086/300337
Dalang, C., & Bonvin, C. 2022, MNRAS, 512, 3895,
doi:10.1093/mnras/stac726
Darling, J. 2022, ApJL, 931, L14, doi:10.3847/2041-8213/ac6f08
de Gasperin, F., Intema, H. T., & Frail, D. A. 2018, MNRAS, 474,
5008, doi:10.1093/mnras/stx3125
Ellis, G. F. R., & Baldwin, J. E. 1984, MNRAS, 206, 377,
doi:10.1093/mnras/206.2.377
Gibelyou, C., & Huterer, D. 2012, MNRAS, 427, 1994,
doi:10.1111/j.1365-2966.2012.22032.x
Gorski, K. M., Hivon, E., Banday, A. J., et al. 2005, ApJ, 622, 759, ´
doi:10.1086/427976
Green, G. 2018, The Journal of Open Source Software, 3, 695,
doi:10.21105/joss.00695
Haslam, C. G. T., Salter, C. J., Stoffel, H., & Wilson, W. E. 1982,
A&AS, 47, 1
Hickox, R. C., Jones, C., Forman, W. R., et al. 2009, ApJ, 696,
891, doi:10.1088/0004-637X/696/1/891
Hurley-Walker, N. 2017, arXiv e-prints, arXiv:1703.06635.
https://arxiv.org/abs/1703.06635
Intema, H. T., Jagannathan, P., Mooley, K. P., & Frail, D. A. 2017,
A&A, 598, A78, doi:10.1051/0004-6361/201628536
Lacy, M., Baum, S. A., Chandler, C. J., et al. 2020, PASP, 132,
035001, doi:10.1088/1538-3873/ab63eb

$$
\mathrm{s}^{-1}
$$

$$
(\sim42^{\circ})
$$

$$
\mathrm{s}^{-1}
$$

## REFERENCES

Astropy Collaboration, Robitaille, T. P., Tollerud, E. J., et al. 2013,
A&A, 558, A33, doi:10.1051/0004-6361/201322068

Mainzer, A., Bauer, J., Grav, T., et al. 2011, ApJ, 731, 53,
doi:10.1088/0004-637X/731/1/53
Mainzer, A., Bauer, J., Cutri, R. M., et al. 2014, ApJ, 792, 30,
doi:10.1088/0004-637X/792/1/30
Marocco, F., Eisenhardt, P. R. M., Fowler, J. W., et al. 2021, ApJS,
253, 8, doi:10.3847/1538-4365/abd805
Mauch, T., Murphy, T., Buttery, H. J., et al. 2003, MNRAS, 342,
1117, doi:10.1046/j.1365-8711.2003.06605.x
McConnell, D., Hale, C. L., Lenc, E., et al. 2020, PASA, 37, e048,
doi:10.1017/pasa.2020.41
Milne, E. A. 1937, Proc. R. Soc. Lond. Ser. A, 158, 324,
doi:10.1098/rspa.1937.0023
Murray, C. 2022, MNRAS, 510, 3098,
doi:10.1093/mnras/stab3652
Nadolny, T., Durrer, R., Kunz, M., & Padmanabhan, H. 2021,
JCAP, 2021, 009, doi:10.1088/1475-7516/2021/11/009
Planck Collaboration, Abergel, A., Ade, P. A. R., et al. 2014,
A&A, 571, A11, doi:10.1051/0004-6361/201323195
Planck Collaboration, Aghanim, N., Akrami, Y., et al. 2020, A&A,
641, A1, doi:10.1051/0004-6361/201833880
Remazeilles, M., Dickinson, C., Banday, A. J., Bigot-Sazy, M. A.,
& Ghosh, T. 2015, MNRAS, 451, 4311,
doi:10.1093/mnras/stv1274
Rubart, M., & Schwarz, D. J. 2013, A&A, 555, A117,
doi:10.1051/0004-6361/201321215
Sarkar, S. 2008, General Relativity and Gravitation, 40, 269,
doi:10.1007/s10714-007-0547-7
Schlafly, E. F., Meisner, A. M., & Green, G. M. 2019, ApJS, 240,
30, doi:10.3847/1538-4365/aafbea
Secrest, N. J., Dudik, R. P., Dorland, B. N., et al. 2015, ApJS, 221,
12, doi:10.1088/0067-0049/221/1/12
Secrest, N. J., von Hausegger, S., Rameez, M., et al. 2021, ApJL,
908, L51, doi:10.3847/2041-8213/abdd40

---

11

Siewert, T. M., Schmidt-Rubart, M., & Schwarz, D. J. 2021, A&A,
653, A9, doi:10.1051/0004-6361/202039840
Sikora, M., Stawarz, Ł., & Lasota, J.-P. 2007, ApJ, 658, 815,
doi:10.1086/511972
Singal, A. K. 2011, ApJL, 742, L23,
doi:10.1088/2041-8205/742/2/L23
—. 2021, Universe, 7, 107, doi:10.3390/universe7040107
Stern, D., Assef, R. J., Benford, D. J., et al. 2012, ApJ, 753, 30,
doi:10.1088/0004-637X/753/1/30
Taylor, M. B. 2005, in Astronomical Society of the Pacific
Conference Series, Vol. 347, Astronomical Data Analysis
Software and Systems XIV, ed. P. Shopbell, M. Britton, &
R. Ebert, 29
Tiwari, P. 2019, Research in Astronomy and Astrophysics, 19, 096,
doi:10.1088/1674-4527/19/7/96

Tiwari, P., Ghosh, S., & Jain, P. 2019, ApJ, 887, 175,
doi:10.3847/1538-4357/ab54c8
Tiwari, P., & Jain, P. 2015, MNRAS, 447, 2658,
doi:10.1093/mnras/stu2535
Tiwari, P., Kothari, R., Naskar, A., Nadkarni-Ghosh, S., & Jain, P.
2015, Astroparticle Physics, 61, 1,
doi:10.1016/j.astropartphys.2014.06.004
Tiwari, P., & Nusser, A. 2016, JCAP, 2016, 062,
doi:10.1088/1475-7516/2016/03/062
Virtanen, P., Gommers, R., Oliphant, T. E., et al. 2020, Nature
Methods, 17, 261, doi:10.1038/s41592-019-0686-2
Wright, E. L., Eisenhardt, P. R. M., Mainzer, A. K., et al. 2010, AJ,
140, 1868, doi:10.1088/0004-6256/140/6/1868
Zonca, A., Singer, L., Lenz, D., et al. 2019, The Journal of Open
Source Software, 4, 1298, doi:10.21105/joss.01298

──────── [TRUNCATED] ────────
Showing 37,488 chars (head) + 12,469 chars (tail) of 56,280 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-43556b0dad.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-43556b0dad.md" offset=1029 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
