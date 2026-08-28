URL: https://arxiv.org/pdf/2404.06617

# No evidence for anisotropy in galaxy spin directions

⋆
Dhruva Patel¹ and Harry Desmond¹*†*

<sup>1</sup>*Institute of Cosmology & Gravitation, University of Portsmouth, Dennis Sciama Building, Portsmouth, PO1 3FX, UK*

3 March 2025

## ABSTRACT

Modern cosmology rests on the *cosmological principle*, that on large enough scales the Universe is both homogeneous
and isotropic. A corollary is that galaxies’ spin vectors should be isotropically distributed on the sky. This has been
challenged by multiple authors for over a decade, with claims to have detected a statistically significant dipole pattern
of spins. We collect all publicly available datasets with spin classifications (binary Z-wise/S-wise), and analyse them
for large-angle anisotropies (*ℓ ≤* 2). We perform each inference in both a Bayesian and frequentist fashion, the former
establishing posterior probabilities on the multipole parameters and the latter calculating *p*-values for rejection of the
null hypothesis of isotropy (i.e. no power at *ℓ >* 0). All analysis indicate consistency with isotropy to within 3*σ*. We
similarly identify no evidence for a “hemisphere anisotropy” that neglects the angular dependence of the dipole. We
isolate the differences with contrary claims in the ad hoc or biased statistics that they employ. Our code is publicly
available ©.

$$
(\ell\leq2)
$$

Key words: galaxies: formation – galaxies: fundamental parameters – galaxies: statistics – large-scale structure of
Universe

## 1 INTRODUCTION

When averaged over sufficiently large scales, the Universe
is believed to be described by General Relativity and the
Friedmann–Robertson–Walker metric in which all regions of
space and all lines of sight from any observer are equivalent.
The homogeneity scale may already be reached at *∼*70 Mpc,
in agreement with concordance Λ Cold Dark Matter (ΛCDM)
cosmology (Ntelis et al.2017;Gonçalves et al.2017,2018;
Dias et al.2023). The observational evidence for isotropy is
somewhat weaker, and in fact several observations suggest
that preferred directions do exist in the Universe. These include anomalies in the Cosmic Microwave Background (CMB;
most recentlyJones et al.2023, although seeGaztañaga &
Sravan Kumar2024), non-negligible multipoles in the largescale velocity field traced by supernovae (Kalbouneh et al.
2023;Hu et al.2024), strong bulk flows extending to 100s
arXiv:2404.06617v3  [astro-ph.GA]  28 Feb 2025
of Mpc (Watkins et al.2023) and non-convergence of the
rest frames of the CMB and distant matter (Rameez et al.
2018;Migkas et al.2020;Secrest et al.2022;Dam et al.
2023;Horstmann et al.2022;Sorrenti et al.2023). For a review of the observational status of the cosmological principle,
seeAluri et al.(2023). We must assess carefully whether the
fundamental tenets of ΛCDM hold before we can settle into
an era of “precision cosmology”.

We investigate here a subset of the claims for anisotropy,
namely the putative presence of a dipole in galaxies’ spin directions when viewed from the Milky Way. This is a clean

test with few possible systematics: one uses images of lowinclination late-type galaxies to determine (e.g. from the direction of spiral arm winding) whether they are spinning towards or away from us, and then ask whether this binaryvalued field projected onto the sky has significant power in
multipoles beyond *ℓ* = 0 (the monopole). In galaxies, we
designate clockwise rotation as Z-wise and counterclockwise
rotation as S-wise. A Z-wise galaxy rotates clockwise, with
its angular momentum pointing away from us, while an Swise galaxy rotates counterclockwise, with its angular momentum vector pointing towards us. Provided the galaxies
are at cosmological distance, power should not be generated
at low *ℓ* from tidal torque-like interactions (Barnes & Efstathiou1987). If true, this finding would therefore force a
rethink of basic cosmology, and may imply that the Universe
possessed a net angular momentum in its initial conditions
(e.g.Schneider & Célérier1999;Rodrigues2008;Battisti &
Marcianò2010).

Over the past *∼*15 years (although seeMacGillivray &
Dodd1985;Iye & Sugai1991;Sugai & Iye1995for earlier
related attempts) this test has been performed with various
datasets, methods for determining spin direction and statistics for quantifying the anisotropy. Although dominated by
a few authors, most studies claim to find a significant dipole
(MacGillivray & Dodd1985;Longo2007,2011;Shamir2017,
2020a,b,c,d,2021a,b,2022a,c,d;McAdam & Shamir2023b;
Shamir2024). On the other hand,Iye & Sugai(1991),Land
et al.(2008),Hayes et al.(2017),Tadaki et al.(2020) and
Iye et al.(2021a) do not. Hence this important issue remains
controversial.

We collect all publicly available catalogues for which galaxy

<sup>⋆</sup>zx970439@ou.ac.uk

*†* harry.desmond@port.ac.uk spin directions have been estimated, a procedure called
“annotation”. We assume these are correct, and question
merely the statistics with which this data is interrogated for
anisotropy. If we find a dipole we may wonder whether the
annotation method suffers from a systematic that causes this,
but if we do not find a dipole it is highly unlikely that an existing dipole is hidden by such a systematic. Unlike almost
all previous authors we do not use *χ²* to avoid assumptions of
Gaussianity. Instead we define a likelihood for each galaxy’s
spin as a function of low-*ℓ* multipole parameters (monopole,
dipole, quadrupole) and the angle between the galaxy direction and multipole axes. We derive posterior probability
distributions on these parameters in a Bayesian analysis and
use mock data generated under the assumption of isotropy
to test that null hypothesis in a frequentist fashion.

$$
\dot{\chi}^{2}
$$

In Sec.2we describe the annotated galaxy catalogues that
we employ. In Sec.3we detail our methods, separately for
the Bayesian and frequentist approach. Sec.4presents our
results and Sec.5concludes.

## 2 OBSERVATIONAL DATA

We collate all publicly available image data that has been
used in the literature to test the isotropy of galaxy spins.
Beyond the raw data, this test requires an algorithm to calculate the spin direction of each galaxy (annotation). Any
difference in results for fixed data could arise either from the
annotation method or the statistics with which the annotated
data is tested for anisotropy. Here we accept at face value
the annotation of the utilised datasets by other authors, and
ask merely whether the statistics of the annotated datasets
provide compelling evidence for anisotropy. While the annotations themselves may of course be biased (we refer to the
relevant papers for arguments that they are unlikely to be), if
they imply isotropy it seems highly unlikely that such biases
would hide an underlying anisotropy, which one would expect
them if anything to increase.

The datasets we use are summarised in Table1. Most of the
datasets (Longo, Iye, SDSS DR7, GAN M, GAN NM and Shamir)
come from data releases 6-8 of the Sloan Digital Sky Survey
(SDSS;York et al.2000;Aihara et al.2011). PS DR1 derives
instead from the Panoramic Survey Telescope and Rapid Response System (Pan-STARRS1) data release 1 (Chambers
et al.2016). This was obtained by cross-matching galaxies with identical IDs between two Pan-STARRS datasets,
Shamir(2017) andGoddard & Shamir(2020). Thus, this
dataset is to our knowledge unique, and no isotropy analysis
has previously been conducted on it (although it was annotated inShamir2017). The SDSS datasets differ in sky coverage and galaxy density as seen in Figure1. GAN M is almost
identical to GAN NM except the galaxy images were mirrored
before being fed into the annotation algorithm, in order to
quantify the level of asymmetry in this algorithm. The quoted
sigma values in Table1were taken from the cited papers, except in the case of (Longo2011) where it was calculated from
the *p*-value quoted in the abstract of that paper assuming a
Gaussian distribution and the sigma value given for Iye was
taken from (Shamir2022b) as it is the more significant result
in the analysis of this dataset.

Various annotation methods were used.Longo(2011) employed a group of undergraduate students, referred to as

Table 1. The observational datasets we use to search for
galaxy spin anisotropy. The third column gives the significance of
anisotropy reported by the creators of each dataset, where such an
analysis was performed. M denotes (partial) mirroring of the data,
while the final column gives the annotation algorithm. In order,
the references areLongo(2011);Iye et al.(2021b);Shamir(2022b);
McAdam & Shamir(2023a,b);Shamir(2021a,2017). Note, GAN M
and GAN NM are cited from the same paper (McAdam & Shamir
2023b).

| Name | #gals | $\sigma$ | M | Annotation method |
| --- | --- | --- | --- | --- |
| Longo | 15158 | 3.16 | Yes | Human scanners |
| Iye | 72888 | 2.10 | No | GANALYZER |
| SDSS DR7 | 6103 | — | No | GANALYZER |
| GAN M | 139852 | 3.97 | Yes | SPArcFiRe,GANALYZER |
| GAN NM | 138940 | 2.33 | No | SPArcFiRe,GANALYZER |
| Shamir | 77840 | 2.56 | No | GANALYZER |
| PS DR1 | 28731 | — | No | GANALYZER |

“scanners”, to manually annotate randomly assigned redshift
slices of the data. The author states that any proclivity for
the scanners to prefer a particular spin direction was mitigated by mirroring half of the objects at random to disfavour
a particular handedness. The remaining datasets were annotated either by SpArcFiRe (“Scalable Automated Detection of Spiral Galaxy Arm Segments;Davis & Hayes2014),
an algorithm which extracts the structural features of spiral
galaxies, or Ganalyzer (“Galaxy Analyzer”), a modelling
tool for automated galaxy classification (Shamir2011). We
investigate the consistency of different annotation methods
by cross-matching galaxies with identical IDs between the
SDSS-based datasets, finding agreement in spin direction for
91.81% of galaxies matched between Longo and GAN M. As the
latter dataset is fully mirrored, this implies that the former
is also. This is corroborated by an 8.27% agreement between
Longo and GAN NM, and a 93.36% agreement between GAN NM
and SDSS DR7. The level of mirroring is however not important for our analysis, which aims simply to investigate the
statistical significance for anisotropy from a given set of spin
values.

We visualise the datasets in Fig.1by plotting the number
of galaxies per pixel under a healpix scheme with nside=
16. We see a significant overlap in area between most of the
datasets in the SDSS region. It is clearly imperative for the
statistical method used to assess anisotropy to be robust to
a highly incomplete sky coverage.

## 3 METHOD

To ensure that our results are robust to choice of
methodology—and suit the taste of the reader—we perform
both a Bayesian and frequentist analysis. Each of these relies
on a function that describes the likelihood of the data given
the model parameters. These parameters, which we denote
*θ⃗*, are (some subset of) monopole magnitude *M*, dipole magnitude *D* and unit vector direction on the sky *d⃗* = *{dα,dδ}*,
and quadrupole magnitude *Q* with corresponding unit sky
vectors *⃗q₁* = *{q₁,α,q₁,δ}* and *⃗q₂* = *{q₂,α,q₂,δ}*. These are multipoles of the on-sky probability field for spins to be Z-wise as
seen from the Milky Way: a monopole describes a directionindependent preference for a particular spin direction (most

$$
\theta_{}
$$

$$
\vec{d}=\{d_{\alpha},d_{\delta}\}
$$

$$
\vec{q}_{1}=\{q_{1,\alpha},q_{1,\delta}\}
$$

$$
\vec{q}_{2}=\{q_{2,\alpha},q_{2,\delta}\}
$$

---

Figure 1. The number of galaxies per pixel for each of the datasets we investigate. These are Mollweide projections in equatorial
π
coordinates using healpix with nside = 16, rotated to centre on (RA, Dec)= (*,*0) and RA increases towards the left.
2

likely due to a bias in the annotation method), a dipole describes a preference for Z-wise spins in one direction and Swise in the opposite, and a quadrupole describes a pattern
with two hotspots and corresponding coldspots. We work in
equatorial coordinates, where *α* denotes right ascension (RA)
and *δ* declination (Dec). We adopt the range of [0*,*2*π*) for RA
π <sup>π</sup>
and (*−,*) for Dec throughout. We denote a galaxy’s spin
2 2
value as *s*, which we assign the value 0 if the spin is S-wise
as seen from the Milky Way, and 1 if it is Z-wise. Isotropy
therefore corresponds to *D* = *Q* = 0, and an equal number
of Z-wise and S-wise spins to *M* = 0*.*5.

$$
\left(-{\textstyle{\frac{\pi}{2}}},{\textstyle{\frac{\pi}{2}}}\right)
$$

$$
D=Q=0.
$$

For galaxy *i*, the likelihood of Z-wise spin is

$$
M=0.5
$$

$$
\mathcal{L}(s_{i}|\vec{\theta})=M+D\:\vec{d}\cdot\vec{n}_{i}+Q\left(\vec{q}_{1}\cdot\vec{n}_{i}\:\vec{q}_{2}\cdot\vec{n}_{i}-\frac{1}{3}\vec{q}_{1}\cdot\vec{q}_{2}\right),
$$

(1)

$$
\vec{n}
$$

where *⃗n* is the unit vector pointing in the direction of the
galaxy. The likelihood of S-wise spin is 1 *−L*, and thus it
is properly normalised by construction provided 0 *≤L≤* 1.
We impose this by requiring 0 *≤|M |* + *|D|* + *|Q|≤* 1, but
find that this never comes into play because the best-fit *M*
values are *∼*0.5 while the best-fit *D* and *Q* values are small.
This matches the model ofLand et al.(2008). We assume
that all galaxies in a dataset are independent, so that the
likelihood of the dataset is the product of the likelihood of
its constituent galaxies. To investigate how the results are
affected by the inclusion of the *ℓ* = 0, *ℓ* = 1 and *ℓ* = 2 terms
we perform separate analyses modelling i) monopole only, ii)
dipole only at *M* = 0*.*5, iii) monopole and dipole, and iv)
monopole, dipole and quadrupole.

$$
1-\mathcal{L}.
$$

$$
0\leq\mathcal{L}\leq1
$$

$$
0\leq|M|+|D|+|Q|\leq1
$$

## 3.1 Bayesian analysis

$$
Q\geq0
$$

The goal of a Bayesian analysis is to establish posterior probabilities on the model parameters. We adopt uniform priors
on *M*, *D ≥* 0 and *Q ≥* 0, and a uniform prior on area element
for the *d⃗*, *⃗q₁* and *⃗q₂* vectors across the full sky. This corresponds to a prior uniform in the vector’s RA components
and in the sine of their Dec components. See Table 2 for a
description of the free parameters used in the analysis, and
their priors for the Bayesian analysis. We initially choose the
prior ranges in Table 2, with the intention of expanding the
ranges if necessary, but find that the posteriors are already
contained within these bounds in all cases. To expedite sampling and eliminate multimodality, we break the symmetry
between the two quadrupole vectors by requiring *q₂,α ≥ q₁,α*.

$$
M,D\geq0
$$

$$
\ vec d\\vec{q}_{1}
$$

$$
\vec{q_{2}}
$$

$$
q_{2,\alpha}\geq q_{1,\alpha}.
$$

We perform a Markov Chain Monte Carlo (MCMC) analysis with the affine-invariant sampler emcee (Foreman-Mackey
et al.2013), using 22 walkers with initial positions randomly
sampled from the prior. We calculate the autocorrelation

Table 2. Table of free parameters, descriptions and their prior
+π/2
ranges. [cos(*d*<sub>δ</sub>)] denotes a prior proportional to cos(*d*<sub>δ</sub>)
−π/2
within the range *−π/*2 *≤ d*<sub>δ</sub>*≤ π/*2. Below the horizontal line
we show the parameters (besides *M*) of the alternative hemisphere
anisotropy analysis (see final paragraph of Sec.3.1), which replace
*D*, *d*<sub>α</sub> and *d*<sub>δ</sub>*.*

$$
\left[\cos(d_{\delta})\right]_{-\pi/2}^{+\pi/2}
$$

$$
\cos(d_{\delta})
$$

$$
-pi2\\,\leq\,d_{\delta}\,\leq\,\pi/2
$$

$$
D,\,d_{\alpha}
$$

$$
d_{\delta}
$$

| Parameter | Description | Prior |
| --- | --- | --- |
| M | Monopole magnitude | U(0.3,0.7) |
| D | Dipole magnitude | U(0,0.3) |
| Q | Quadrupole magnitude | U(0,0.3) |
| $d_{\alpha}$ | Unit dipole RA component | U(0,2π) |
| $d_{\delta}$ | Unit dipole Dec component | [$\cos(d_{\delta})]_{- \pi/2}^{+ \pi/2}$ |
| $q_{1,\alpha}$ | Unit quadrupole $1^{\mathrm{st}}$ axis RA | U(0,2π) |
| $q_{1,\delta}$ | Unit quadrupole $1^{\mathrm{st}}$ axis Dec | [$\cos(q_{1,\delta})]_{- \pi/2}^{+ \pi/2}$ |
| $q_{2,\alpha}$ | Unit quadrupole $2^{\mathrm{nd}}$ axis RA | U(0,2π) |
| $q_{2,\delta}$ | Unit quadrupole $2^{\mathrm{nd}}$ axis Dec | [$\cos(q_{2,\delta})]_{- \pi/2}^{+ \pi/2}$ |
| A | Asymmetry magnitude | U(0,0.3) |
| $a_{\alpha}$ | Unit asymmetry RA component | U(0,2π) |
| $a_{\delta}$ | Unit asymmetry Dec component | [$\cos(a_{\delta})]_{- \pi/2}^{+ \pi/2}$ |

$$
d_{\alpha}
$$

$$
q_{1,\alpha}
$$

$$
d_{\delta}
$$

$$
q_{1,\delta}
$$

$$
\left[\operatorname{c o s}(d_{\delta})\right]_{-\pi/2}^{+\pi/2}
$$

$$
1^{\,\mathrm{s t}}
$$

$$
1^{\mathrm{s t}}
$$

$$
\left[\cos(q_{1,\delta})\right]_{-\pi/2}^{+\pi/2}
$$

$$
2^{\mathrm{n d}}
$$

$$
\mathcal{U}(0,2\pi)
$$

$$
2^{\mathrm{n d}}
$$

$$
q_{2,\delta}
$$

$$
\left[\cos(q_{2,\delta})\right]_{-\pi/2}^{+\pi/2}
$$

$$
a_{\alpha}
$$

$$
\left[ \cos \left(a _ {\delta}\right) \right] _ {- \pi / 2} ^ {+ \pi / 2}
$$

length for each parameter every 100 iterations, terminating
when the chain is at least 100 autocorrelation lengths in each
parameter and the change in autocorrelation length between
iterations is less than 1 per cent.

This produces corner plots describing the posteriors on
the parameters and their degeneracies. We summarise each
marginal posterior using its mode *θ*¯ and 68 per cent confidence interval, unless θ¯−2std(θ) < 0 in which case we instead
quote only the 68 per cent upper limit. The mode is calculated by emcee as the location of the bin containing the most
samples. The use of a 68% confidence interval corresponds to
1*σ* for a Gaussian distribution. For any parameter required
to be *≥* 0 by the prior, if it is consistent with 0 (estimated
by θ¯−2 std(θ) < 0) we quote an upper limit, while if it is not
we quote the mode of the distribution and 68% confidence
interval. This approach ensures that the reported values appropriately reflect the characteristics of the posterior distribution and the constraints imposed by the prior. We assess
the goodness-of-fit of each model using the Bayesian information criterion (BIC) as an approximation to the Bayesian

$$
\bar{\theta}\!-2!\mathrm{s t d}(\theta)<0
$$

$$
\geq0
$$

$$
\bar{\theta}\ -\ 2\operatorname{s t d}(\theta)<0)
$$ evidence. This is given bySchwarz(1978):

$$
\mathrm{B I C}\equiv k\ln(N)-2\ln(\hat{\mathcal{L}})
$$

(2)

where *k* is the number of free parameters, *N* the number of
data points and *L*ˆ the maximum-likelihood value. The BIC
shows whether the addition of parameters is warranted by the
data: an extra parameter must increase the maximum likelihood by at least ln(*N*)*/*2. As the absolute value is unimportant, we show only differences (∆BIC) relative to the baseline
model inferring *M* only.

$$
\hat{\mathcal{L}}
$$

Finally, we run a separate analysis with a model that investigates the preference for observing a particular spin direction in a given hemisphere, without any variation in predicted spin within the hemisphere. We dub this a “hemisphere
anisotropy” to distinguish it from a dipole. In this model, a
galaxy with unit direction *⃗n* on the sky has a likelihood of
Z-wise spin given by
(

$$
\mathcal{L}(s|\vec{\theta})=\begin{cases}{M+A}&{\mathrm{i f~}\vec{n}\cdot\vec{a}>0}\\ {M-A}&{\mathrm{{o o h e e w i s e}}}\\ \end{cases}
$$

(3)

where *⃗a* is the unit hemisphere axis, *A* is the strength of the
anisotropy and *M* is the monopole as before. The likelihood
of S-wise spin is 1*−L*, ensuring proper normalisation provided
0 *≤L≤* 1. We impose this by requiring 0 *≤|M |* + *|A|≤* 1.
We adopt uniform priors on *M* and *A ≥* 0, and a uniform
prior on area element for vector *⃗a* (see Table2). We perform
a similar Bayesian analysis for this model, running MCMC
and calculating ∆BIC relative to the same baseline model
inferring *M* only (the identical isotropic model to the dipole
analysis). This is designed to mimic the type of anisotropy
studied inShamir(2024).

$$
\vec{a}
$$

$$
1\!-\!\mathcal{L}.
$$

$$
0\leq{\mathcal{L}}\leq1
$$

$$
0\leq|M|+|A|\leq1
$$

$$
A\geq0.
$$

## 3.2 Frequentist analysis

The goal of a frequentist analysis is to calculate a *p*-value for
rejection of a null hypothesis, in this case that the Universe
is isotropic. First we calculate the maximum-likelihood values of *θ⃗* for each dataset using the Nelder–Mead algorithm
(Nelder & Mead1965;Gao & Han2012). Then, for each sample of Table1, we create 50,000 mock datasets¹ with galaxies
in the same positions as in the real data but the spins randomised. As we are interested in testing isotropy and not a
direction-independent preference for Z-wise or S-wise spins
(which is what a bias in annotation method would naturally
produce), the mock data is generated using the maximumlikelihood *M* value, *M*c, from the monopole plus dipole model,
but *D* = *Q* = 0. We refit each mock data set to calculate
the maximum-likelihood *θ⃗*, and then calculate the *p*-value
of the null hypothesis as the fraction of mock datasets with
more extreme *{M,D}* values than the real data. This is done
by binning the mock data in the *{M,D}* plane and calculating contour levels minimally enclosing fixed fractions of
the mock datasets; the contour passing through the real-data
point determines the *p*-value. In this case we do not consider
a quadrupole.Iye et al.(2021a) utilised mock data by performing 50,000 Monte Carlo simulations, randomly assigning

$$
\vec{\theta}
$$

$$
D\,=\,Q\,=\,0
$$

$$
\vec{\theta},
$$

Table 3. Table of parameter constraints when inferring *M* alone.
Limits are at 1*σ*.

| Dataset | M |
| --- | --- |
| Longo | $0.512^{+0.004}_{-0.004}$ |
| Iye | $0.503^{+0.002}_{-0.002}$ |
| SDSS DR7 | $0.501^{+0.006}_{-0.006}$ |
| GAN M | $0.505^{+0.001}_{-0.001}$ |
| GAN NM | $0.497^{+0.001}_{-0.001}$ |
| Shamir | $0.503^{+0.002}_{-0.002}$ |
| PS DR1 | $0.510^{+0.003}_{-0.003}$ |

$$
0.512_{-0.004}^{+0.004}
$$

$$
\mathrm\{I{e}
$$

$$
0.503_{-0.002}^{+0.002}
$$

$$
0.501_{-0.006}^{+0.006}
$$

$$
0.505_{-0.001}^{+0.001}
$$

$$
0.497_{-0.001}^{+0.001}
$$

$$
0.503_{-0.002}^{+0.002}
$$

$$
0.510_{-0.003}^{+0.003}
$$

spin directions to each galaxy to create a baseline distribution
of dipole amplitude for an isotropic distribution. By comparison, the observed dipole amplitude was calculated by taking
the vector sum of spin directions weighted by their positions
on the sky and a 3D random walk model was used to represent the isotropic distribution of galaxy spins, with each spin
direction considered as a step in the walk.

## 3.3 Validation

Before applying our method to the real data we validate it
on mock data to ensure that it returns unbiased parameter
values. Each mock dataset has the same number of galaxies
as Iye (72888), but we generate mock spin values and optionally randomise the positions of the galaxies on the sky.
The mock spin values are generated stochastically according
to the probabilities corresponding to some true, generating *θ⃗*.
We calculate a bias value for each parameter and each dataset
as

$$
{\mathrm{b i a s}}\equiv{\frac{(\langle\theta\rangle-{\tilde{\theta}})}{\mathrm{s t d}(\theta)}},
$$

(4)

following the Bayesian setup, where angular brackets denote
the mean and tilde the true, generating value. This may be
interpreted as a discrepancy in *σ* between the input parameter value and that recovered by the inference. We find that
the distribution of bias values in all cases follows closely the
expected standard normal distribution regardless of *θ⃗*˜ or the
positions of the galaxies on the sky. This is illustrated in Fig.2
for the case *M*˜ = 0*.*6, *D*˜ = 0*.*2, *d*˜ = *π*, *d*˜ = *−π/*4 without
α δ
randomising galaxy positions, over 300 mock datasets.

$$
\vec{\theta}
$$

$$
\tilde{M}\ {=}\ 0.6,\:\tilde{D}{=}\ 0.2,\:\tilde{d}_{\alpha}{=}\ \pi,\:\tilde{d}_{\delta}{=}\ -\pi/4
$$

Note that both of our methods account for the “lookelsewhere effect” that comes into play when testing multiple
hypotheses (in this case many possible dipole directions). In
the frequentist approach this is accounted for by calculating significance with respect to mock data that has the same
properties as the real data and has been processed identically,
while in the Bayesian approach it is accounted for by the priors, which appropriately weight the probability that an axis
should point in any particular direction.

<sup>1</sup>We find the *p*-values to converge quite slowly with number of
mock datasets, hence the large number required for near-stability
at two significant figures. The conclusion that the anisotropy is insignificant is readily apparent using fewer mock datasets, however.

---

Figure 2. Distribution of bias values (Eq.4) from MCMC analyses
of 300 mock datasets generated by *M*˜ = 0*.*6, *D*˜ = 0*.*2, *d*˜ = *π*,
<sub>α</sub>
*d*˜ = *−π/*4. The values are expected to follow a standard normal
δ
distribution, shown in dashed black.

$$
((\operatorname{E q},4)
$$

$$
\tilde{M}=0.6,\,\tilde{D}=0.2,\,\tilde{d}_{\alpha}=\pi,
$$

$$
\tilde{d}_{\delta}=-\pi/4
$$

Table 4. Table of parameter constraints when inferring *D* alone
(with *M* fixed to 0.5). ∆BIC is relative to the monopole-only
model; the positive values indicate that the inclusion of dipole
parameters is not warranted by the data.

| Dataset | D | ΔBIC |
| --- | --- | --- |
| Longo | $0.020^{+0.006}_{-0.006}$ | 14.5 |
| Iye | &lt;0.006 | 21.7 |
| SDSS DR7 | &lt;0.019 | 17.5 |
| GAN M | &lt;0.008 | 39.6 |
| GAN NM | &lt;0.005 | 24.4 |
| Shamir | &lt;0.007 | 26.2 |
| PS DR1 | $0.020^{+0.006}_{-0.006}$ | 31.7 |

$$
0.020_{-0.006}^{+0.006}
$$

$$
<0.007
$$

$$
0.020_{-0.006}^{+0.006}
$$

Table 5. Results inferring *M* and *D* simultaneously.

| Dataset | M | D | ΔBIC | p-value |
| --- | --- | --- | --- | --- |
| Longo | $0.500^{+0.027}_{-0.027}$ | &lt;0.016 | 28.9 | 0.44 |
| Iye | $0.503^{+0.002}_{-0.002}$ | &lt;0.005 | 33.6 | 0.92 |
| SDSS DR7 | $0.501^{+0.025}_{-0.028}$ | &lt;0.046 | 24.7 | 0.32 |
| GAN M | $0.505^{+0.002}_{-0.002}$ | &lt;0.006 | 35.0 | 0.29 |
| GAN NM | $0.497^{+0.002}_{-0.002}$ | &lt;0.004 | 35.5 | 0.91 |
| Shamir | $0.503^{+0.002}_{-0.002}$ | &lt;0.006 | 30.6 | 0.84 |
| PS DR1 | $0.509^{+0.003}_{-0.003}$ | $0.016^{+0.006}_{-0.007}$ | 20.2 | 0.054 |

$$
0.500_{-0.027}^{+0.027}
$$

$$
\Delta\mathbf{B I C}
$$

$$
<0.016
$$

$$
0.503_{-0.002}^{+0.002}
$$

$$
0.501_{-0.028}^{+0.025}
$$

$$
0.505_{-0.002}^{+0.002}
$$

$$
<0.005
$$

$$
<0.046
$$

$$
<0.006
$$

$$
0.497_{-0.002}^{+0.002}
$$

$$
<0.004
$$

$$
0.503_{-0.002}^{+0.002}
$$

$$
<0.006
$$

$$
0.509_{-0.003}^{+0.003}
$$

$$
0.016_{-0.007}^{+0.006}
$$

Table 6. Results inferring *M*, *D* and *Q* simultaneously.

| Dataset | M | D | Q | ΔBIC |
| --- | --- | --- | --- | --- |
| Longo | $0.499^{+0.009}_{-0.012}$ | &lt;0.023 | $0.070^{+0.025}_{-0.026}$ | 76.4 |
| Iye | $0.504^{+0.002}_{-0.002}$ | &lt;0.005 | &lt;0.009 | 87.3 |
| SDSS DR7 | $0.500^{+0.038}_{-0.039}$ | &lt;0.066 | &lt;0.090 | 67.2 |
| GAN M | $0.505^{+0.002}_{-0.003}$ | &lt;0.006 | &lt;0.010 | 94.9 |
| GAN NM | $0.497^{+0.002}_{-0.002}$ | &lt;0.004 | &lt;0.011 | 93.7 |
| Shamir | $0.503^{+0.002}_{-0.002}$ | &lt;0.006 | &lt;0.011 | 87.3 |
| PS DR1 | $0.510^{+0.004}_{-0.004}$ | $0.017^{+0.007}_{-0.007}$ | &lt;0.021 | 77.9 |

$$
0.499_{-0.012}^{+0.009}
$$

$$
<0.023
$$

$$
0.070_{-0.026}^{+0.025}
$$

$$
0.504_{-0.002}^{+0.002}
$$

$$
<0.009
$$

$$
0.500_{-0.039}^{+0.038}
$$

$$
<0.066
$$

$$
0.505_{-0.003}^{+0.002}
$$

$$
0.497_{-0.002}^{+0.002}
$$

$$
<0.006
$$

$$
0.503_{-0.002}^{+0.002}
$$

$$
<0.004
$$

$$
<0.006
$$

$$
<0.011
$$

$$
0.510_{-0.004}^{+0.004}
$$

$$
0.017_{-0.007}^{+0.007}
$$

$$
<0.021
$$

Table 7. Hemispherical anisotropy results, inferring *M* and *A* simultaneously.

| Dataset | M | A | ΔBIC |
| --- | --- | --- | --- |
| Longo | $0.494^{+0.006}_{-0.005}$ | $0.013^{+0.006}_{-0.006}$ | 28.9 |
| Iye | $0.503^{+0.002}_{-0.002}$ | &lt;0.004 | 33.6 |
| SDSS DR7 | $0.502^{+0.124}_{-0.128}$ | &lt;0.125 | 24.6 |
| GAN M | $0.505^{+0.002}_{-0.002}$ | &lt;0.003 | 35.5 |
| GAN NM | $0.497^{+0.002}_{-0.002}$ | &lt;0.002 | 34.2 |
| Shamir | $0.503^{+0.002}_{-0.002}$ | &lt;0.004 | 33.2 |
| PS DR1 | $0.510^{+0.003}_{-0.003}$ | $0.009^{+0.003}_{-0.004}$ | 30.7 |

$$
0.494_{-0.005}^{+0.006}
$$

$$
0.013_{-0.006}^{+0.006}
$$

$$
0.503_{-0.002}^{+0.002}
$$

$$
<0.004
$$

$$
0.502_{-0.128}^{+0.124}
$$

$$
<0.125
$$

$$
0.505_{-0.002}^{+0.002}
$$

$$
<0.003
$$

$$
<0.002
$$

$$
0.497_{-0.002}^{+0.002}
$$

$$
0.503_{-0.002}^{+0.002}
$$

$$
<0.004
$$

$$
0.510_{-0.003}^{+0.003}
$$

$$
0.009_{-0.004}^{+0.003}
$$

## 4 RESULTS

## 4.1 Bayesian analysis

Our results are presented in Tables3–7. We see that *M* is consistent with 0.5 within *∼*3*σ* regardless of whether or not one
infers *D* or *Q*, indicating no significant direction-independent
bias in the assignment of Z-wise versus S-wise spins. (To more
decimal places, the GAN M result is 0*.*50532 *±* 0*.*00135, a 3.9*σ*
difference from 0.5.) Such biases in annotation methods are
well documented, for example for visual assessment by citizen scientists inLand et al.(2008);Slosar et al.(2009);Hayes
et al.(2017). This may be at play to a minor degree in the
Longo, GAN M and PS DR1 datasets.

$$
0.50532\pm0.00135
$$

When inferring *D* alone, we see a detection of a dipole at
just over 3*σ* in the Longo and PS DR1 datasets, with direc-
+0.48 +0.46 +0.30
tion *dα* = 3*.*62−0<sup>.</sup>52*,d*δ= 0*.*51−0<sup>.</sup><sup>46</sup>and *d*α = 4*.*57−0<sup>.</sup>38*,d*δ=
+0*.*.29
0.74<sub>−</sub><sub>0</sub> <sub>31</sub>respectively. The remainder have *D* consistent with
0 at 2*σ*, such that we present only upper limits (and hence
there are no meaningful constraints on the dipole direction).
These constraints are fairly tight, indicating that a sizeable
dipole can be ruled out at high confidence. The positive ∆BIC
for all datasets relative to the monopole-only case indicates
a worse-fitting model. The significance of ∆BIC can be interpreted on the Jeffreys scale (Jeffreys1939), which rates
the evidence for the better-fitting model as “decisive” if the
Bayes factor (ratio of evidences) exceeds 100. Since evidence

[... middle omitted — see footer ...]

\vec{d}_{\alpha,\delta}
$$

$$
\chi^{2}
$$

$$
\alpha,\delta
$$

$$
\chi_{\alpha,\delta,\mathrm{d a t a}}^{2}
$$

$$
i^{\mathrm{t h}}
$$

$$
\chi_{\alpha,\delta,\mathrm{m o c k},i}^{2}
$$

$$
\alpha,\delta
$$

$$
\sigma_{\alpha,\delta}=\frac{|\chi_{\alpha,\delta,\mathrm{d a t a}}^{2}-\langle\chi_{\alpha,\delta,\mathrm{m o c k},i}^{2}\rangle|}{\mathrm{s t d}(\chi_{\alpha,\delta,\mathrm{m o c k},i}^{2})}
$$

(6)

where angled brackets denote a mean over the mock data
sets. Eq.5appears to be Pearson’s *χ²* statistic, in which one
replaces the squared uncertainty in the denominator of the
regular Gaussian *χ²* by the expected value, in this case (something proportional to) *d⃗ · ⃗ni*. However, the observed value is
*s*, not *s |d · ⃗n ⃗* | wh*i*ch mixes the observation with the exi i i
pectation. This effectively projects *si* onto the dipole axis,
which amounts to modelling the expected value as 1 everywhere in the hemisphere aligned with the dipole direction,
neglecting the fact that the likelihood of *s* = 1 is lower the
further one is from the dipole axis, even if the expected value
is *>* 0*.*5. Larger discrepancies from the dipole axis may contribute more to the overall chi-squared statistic. Even besides
this, we do not consider Eq.5a useful statistic because it
does not capture the sampling distribution of the observable
as do both our Bayesian and frequentist methods. Furthermore, our attempt at using this equation on theMcAdam
& Shamir(2023b) dataset did not yield the results quoted in
that paper, so we were unable to reproduce their analysis. An
attempt to reproduce the results ofLongo(2011) using Eq.5
(a shot in the dark, sinceLongo2011do not define their *χ²*
statistic) similarly failed.

$$
\chi^{2}
$$

$$
\chi^{2}
$$

$$
s_{i};
$$

$$
\vec{d}\cdot\vec{n}_{i}
$$

$$
s_{i}
$$

$$
s_{i}|\vec{d}\cdot\vec{n}_{i}|
$$

$$
s=1
$$

$$
>0.5
$$

$$
\chi^{2}
$$

## 5 CONCLUSION

We have analysed seven datasets of galaxy sky positions and
spin directions to assess the evidence for anisotropy in galaxies’ angular momenta. Four of these datasets have literature
claims of a *>*2*σ* dipole in the spin directions, with two at *>*3*σ*.
However, we find clear consistency with statistical isotropy
in all datasets using either a Bayesian or frequentist method,
both of which account for the look-elsewhere effect and account fully for parameter degeneracies. Due to the incomplete
sky coverage spherical harmonics are not orthogonal, leading
us to explore the possibility of a quadrupole as well as a dipole
and monopole, but this too is small and does not affect our
*ℓ* = 0 or *ℓ* = 1 results. The evidence for anisotropy does not
increase if the cosine dependence of the dipole is removed. We
trace the difference with literature results claiming a dipole to the unmotivated statistics that they employ, and do not
find their results to be reproducible.

In conclusion, galaxy spins exhibit large-scale isotropy in
adherence to the cosmological principle. Our work highlights
the vital importance of careful statistics in analysing fundamental properties of the Universe.

Hu J. P., Wang Y. Y., Hu J., Wang F. Y., 2024,A&A,681, A88 http://dx.doi.org/10.1051/0004-6361/202347121 https://ui.adsabs.harvard.edu/abs/2024A&A...681A..88H
Iye M., Sugai H., 1991,ApJ,374, 112 http://dx.doi.org/10.1086/170101 https://ui.adsabs.harvard.edu/abs/1991ApJ...374..112I
Iye M., Yagi M., Fukumoto H., 2021a,ApJ,907, 123 http://dx.doi.org/10.3847/1538-4357/abb3bb https://ui.adsabs.harvard.edu/abs/2021ApJ...907..123I

## DATA AVAILABILITY

The annotated galaxy catalogues are available online at the
following URLs:

*•* Longo: https://ars.els-cdn.com/content/image/1-s2.
0-S0370269311003947-mmc1.txt

Land K., et al., 2008,MNRAS,388, 1686 http://dx.doi.org/10.1111/j.1365-2966.2008.13490.x https://ui.adsabs.harvard.edu/abs/2008MNRAS.388.1686L

*•* Iye: https://people.cs.ksu.edu/~lshamir/data/iye_
et_al/

*•* SDSS DR7: https://people.cs.ksu.edu/~lshamir/data/
sdss_phot/

*•* GAN M/NM: https://people.cs.ksu.edu/~lshamir/data/
SpArcFiRe/

*•* Shamir: https://people.cs.ksu.edu/~lshamir/data/
assymdup/

Ceja M. E., Lovisari L., 2020,A&A,636, A15 http://dx.doi.org/10.1051/0004-6361/201936602 https://ui.adsabs.harvard.edu/abs/2020A&A...636A..15M

*•* PS DR1: https://people.cs.ksu.edu/~lshamir/data/
assym3/; https://figshare.com/articles/dataset/
PanSTARRS_DR1_Broad_Morphology_Catalog/12081144

Our code is available on github ©. Any other data underlying
the article will be made available on reasonable request to the
authors.

S., 2022,ApJ,937, L31 http://dx.doi.org/10.3847/2041-8213/ac88c0 https://ui.adsabs.harvard.edu/abs/2022ApJ...937L..31S
Shamir L., 2011,ApJ,736, 141 http://dx.doi.org/10.1088/0004-637X/736/2/141 https://ui.adsabs.harvard.edu/abs/2011ApJ...736..141S

## ACKNOWLEDGEMENTS

We thank Pedro Ferreira, Kazuya Koyama and Sebastian von
Hausegger for useful discussions.

Shamir L., 2020c,Astronomische Nachrichten,341, 324 http://dx.doi.org/10.1002/asna.202013745 https://ui.adsabs.harvard.edu/abs/2020AN....341..324S
Shamir L., 2020d,Ap&SS,365, 136 http://dx.doi.org/10.1007/s10509-020-03850-1 https://ui.adsabs.harvard.edu/abs/2020Ap&SS.365..136S
Shamir L., 2021a,Particles,4, 11 http://dx.doi.org/10.3390/particles4010002 https://ui.adsabs.harvard.edu/abs/2021Parti...4...11S
Shamir L., 2022a, http://dx.doi.org/10.1007/s12036-022-09809-8 ,43, 24 https://ui.adsabs.harvard.edu/abs/2022JApA...43...24S

DP was supported by a SEPnet Summer Placement at
the Institute of Cosmology and Gravitation, University of
Portsmouth. HD is supported by a Royal Society University
Research Fellowship (grant no. 211046).

This project has received funding from the European Research Council (ERC) under the European Union’s Horizon
2020 research and innovation programme (grant agreement
No 693024). For the purpose of open access, we have applied
a Creative Commons Attribution (CC BY) licence to any
Author Accepted Manuscript version arising.

Slosar A., et al., 2009,MNRAS,392, 1225 http://dx.doi.org/10.1111/j.1365-2966.2008.14127.x https://ui.adsabs.harvard.edu/abs/2009MNRAS.392.1225S
http://dx.doi.org/10.1088/1475-7516/2023/11/054 Phys.,2023, 054 https://ui.adsabs.harvard.edu/abs/2023JCAP...11..054S

## REFERENCES

Aihara H., et al., 2011,ApJS,193, 29 http://dx.doi.org/10.1088/0067-0049/193/2/29 https://ui.adsabs.harvard.edu/abs/2011ApJS..193...29A

York D. G., et al., 2000,AJ,120, 1579 http://dx.doi.org/10.1086/301513 https://ui.adsabs.harvard.edu/abs/2000AJ....120.1579Y

Barnes J., Efstathiou G., 1987,ApJ,319, 575 http://dx.doi.org/10.1086/165480 https://ui.adsabs.harvard.edu/abs/1987ApJ...319..575B

Davis D. R., Hayes W. B., 2014,ApJ,790, 87 http://dx.doi.org/10.1088/0004-637X/790/2/87 https://ui.adsabs.harvard.edu/abs/2014ApJ...790...87D

Aihara H., et al., 2011,ApJS,193, 29
Aluri P. K., et al., 2023,Class. Quant. Grav., 40, 094001
Barnes J., Efstathiou G., 1987,ApJ,319, 575
Battisti M. V., Marcianò A., 2010,Phys. Rev. D,82, 124060
Chambers K. C., et al., 2016,arXiv e-prints,p. arXiv:1612.05560
Dam L., Lewis G. F., Brewer B. J., 2023,MNRAS,525, 231
Davis D. R., Hayes W. B., 2014,ApJ,790, 87
Dias B. L., Avila F., Bernui A., 2023,MNRAS, 526, 3219
Foreman-Mackey D., Hogg D. W., Lang D., Goodman J., 2013,
PASP, 125, 306
Gao F., Han L., 2012, Computational Optimization and Applications, 51, 259
Gaztañaga E., Sravan Kumar K., 2024,J. Cosmology Astropart.
Phys.,2024, 001
Goddard H., Shamir L., 2020,ApJS,251, 28

Gonçalves R. S., Carvalho G. C., Bengaly Jr C. A. P., Carvalho
J. C., Bernui A., Alcaniz J. S., Maartens R., 2017,MNRAS,
475, L20
Gonçalves R. S., Carvalho G. C., Bengaly C. A. P., Carvalho J. C.,
Alcaniz J. S., 2018,MNRAS, 481, 5270
Hayes W. B., Davis D., Silva P., 2017,MNRAS,466, 3928
Horstmann N., Pietschke Y., Schwarz D. J., 2022,A&A,668, A34
Hu J. P., Wang Y. Y., Hu J., Wang F. Y., 2024,A&A,681, A88
Iye M., Sugai H., 1991,ApJ,374, 112
Iye M., Yagi M., Fukumoto H., 2021a,ApJ,907, 123
Iye M., Yagi M., Fukumoto H., 2021b,ApJ,907, 123
Jeffreys H., 1939, Theory of Probability. Oxford Univ. Press, Oxford
Jones J., Copi C. J., Starkman G. D., Akrami Y., 2023,arXiv
e-prints,p. arXiv:2310.12859
Kalbouneh B., Marinoni C., Bel J., 2023,Phys. Rev. D,107, 023507
Land K., et al., 2008,MNRAS,388, 1686
Longo M. J., 2007,arXiv e-prints,pp astro–ph/0703694
Longo M. J., 2011,Physics Letters B,699, 224
MacGillivray H. T., Dodd R. J., 1985, A&A,145, 269
McAdam D., Shamir L., 2023a,Symmetry,15, 1190
McAdam D., Shamir L., 2023b,Advances in Astronomy,2023, 1
Migkas K., Schellenberger G., Reiprich T. H., Pacaud F., Ramos-
Ceja M. E., Lovisari L., 2020,A&A,636, A15
Nelder J. A., Mead R., 1965, The computer journal, 7, 308
Ntelis P., et al., 2017,J. Cosmology Astropart. Phys.,2017, 019
Rameez M., Mohayaee R., Sarkar S., Colin J., 2018,MNRAS,477,
1772
Rodrigues D. C., 2008,Phys. Rev. D,77, 023534
Schneider J., Célérier M. N., 1999,A&A,348, 25
Schwarz G., 1978,The Annals of Statistics, 6, 461
Secrest N. J., von Hausegger S., Rameez M., Mohayaee R., Sarkar
S., 2022,ApJ,937, L31
Shamir L., 2011,ApJ,736, 141
Shamir L., 2017,Publ. Astron. Soc. Australia,34, e044
Shamir L., 2020a,Open Astronomy,29, 15
Shamir L., 2020b,Publ. Astron. Soc. Australia,37, e053
Shamir L., 2020c,Astronomische Nachrichten,341, 324
Shamir L., 2020d,Ap&SS,365, 136
Shamir L., 2021a,Particles,4, 11
Shamir L., 2021b,Publ. Astron. Soc. Australia,38, e037
Shamir L., 2022a,,43, 24
Shamir L., 2022b,Journal of Astrophysics and Astronomy PASJ,74, 1114
Shamir L., 2022c,MNRAS,516, 2281
Shamir L., 2022d,Advances in Astronomy,2022, 8462363
Shamir L., 2024,Publ. Astron. Soc. Australia,41, e038
Slosar A., et al., 2009,MNRAS,392, 1225
Sorrenti F., Durrer R., Kunz M., 2023,J. Cosmology Astropart.
Phys.,2023, 054
Sugai H., Iye M., 1995,MNRAS,276, 327
Tadaki K.-i., Iye M., Fukumoto H., Hayashi M., Rusu C. E., Shimakawa R., Tosaki T., 2020,MNRAS,496, 4276
Watkins R., et al., 2023,MNRAS,524, 1885
York D. G., et al., 2000,AJ,120, 1579

MNRAS 000,1–8(2024)

──────── [TRUNCATED] ────────
Showing 29,983 chars (head) + 9,998 chars (tail) of 48,393 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-90ed387770.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-90ed387770.md" offset=944 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
