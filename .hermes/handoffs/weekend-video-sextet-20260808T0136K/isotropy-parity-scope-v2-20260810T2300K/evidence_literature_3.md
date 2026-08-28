URL: https://arxiv.org/pdf/2011.00662

# Spin Parity of Spiral Galaxies III – Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations

1 1
Masanori Iye, Masafumi Yagi, and Hideya Fukumoto²

1National Astronomical Observatory of Japan, Osawa 2-21-1, Mitaka, Tokyo 181-8588 Japan
2The Open University of Japan, 2-11 Wakaba, Mihama-ku, Chiba 261-8586 Japan

Submitted to ApJ

## ABSTRACT

Observation has not yet determined whether the distribution of spin vectors of galaxies is truly
random. It is unclear whether is there any large-scale symmetry-breaking in the distribution of the
vorticity field in the universe. Here, we present a formulation to evaluate the dipole component Dmax
of the observed spin distribution, whose statistical significance σDcan be calibrated by the expected
amplitude for 3D random walk (random flight) simulations.

$$
\\sigma\_{D}
$$

We apply this formulation to evaluate the dipole component in the distribution of Sloan Digital Sky
Survey (SDSS) spirals. Shamir (2017a) published a catalog of spiral galaxies from the SDSS DR8,
classifying them with his pattern recognition tool into clockwise and counterclockwise (Z-spiral and
S-spirals, respectively). He found significant photometric asymmetry in their distribution. We have
confirmed that this sample provides dipole asymmetry up to a level of σD= 4.00.

$$
D\_{m a x}
$$

$$
\\sigma\_{D}=4.00
$$

However, we also found that the catalog contains a significant number of multiple entries of the
same galaxies. After removing the duplicated entries, the number of samples shrunk considerably to
45%. The actual dipole asymmetry observed for the ’cleaned’ catalog is quite modest, σD= 0.29. We
conclude that SDSS data alone does not support the presence of a large-scale symmetry-breaking in
the spin vector distribution of galaxies in the local universe. The data are compatible with a random
distribution.

$$
\\sigma\_{D}=0.29
$$

Keywords: anisotropy—catalogs—galaxies: formation—galaxies: rotation—galaxies: spiral

## 1\. INTRODUCTION

For many decades, investigation of the formation
and evolution of galaxies has been primary subject
of astrophysics. Semi-analytic simulations of structure formation in the ΛCDM model of the universe to reproduce clustering and merging of galaxarXiv:2011.00662v1 \[astro-ph.GA\] 2 Nov 2020
ies provide the current standard picture of galaxy
formation (White & Rees 1978; Steinmetz & Navarro
2002). Ferreira (2020) suggests that ultralight
dark matter may reconcile certain remaining problems which the standard models fail to explain. Recent high-spatial resolution simulations enable tracking of the formation of the spiral structure of indi-

On the other hand, there are other classical models
of galaxy formation, such as the primordial whirl scenario (von Weizsaecker 1955), the pancake shock scenario (Peebles 1969; Zeldovich 1970), and the tidal
torque scenario (White 1984). Each provides naive inference regarding the statistical distribution of the spin
vectors of galaxies.

vidual galaxies (Robertson et al. 2004; Agertz et al.
2011; Ceverino et al. 2017; Shimizu et al. 2019).

If the spin vectors of individual galaxies were produced
by splitting of large-scale primordial whirls, there would
be some remaining coherent spin alignment parallel to
the primordial whirl vectors, producing an observable
dipole anisotropy.

If the galaxies were formed mainly at the equatorial
planes of primordial collapsing pancakes, spin vectors
can mostly be expected to be parallel to the equatorial
planes, possibly producing a quadrupole anisotropy seen
from the observer located within a cluster of galaxies.

Corresponding author: Masanori Iye
[m.iye@nao.ac.jp](mailto:m.iye@nao.ac.jp)

mailto: [m.iye@nao.ac.jp](mailto:m.iye@nao.ac.jp) [m.iye@nao.ac.jp](mailto:m.iye@nao.ac.jp)

* * *

If an individual galaxy started spinning owing to the
tidal torque from a galactic cluster mass assembly, the
galaxy’s spin vector should initially be perpendicular to
the line joining the galaxy and the center of gravity of
the cluster mass assembly. Such an initial correlation
would, however, be diluted soon by orbital mixing.

Figure 1 illustrates potential anisotropy that might
be induced from different galactic formation scenarios
(Sugai & Iye 1995). While the orbital mixing and merging of galaxies could wipe out these initial spin vector anisotropy, if any, observational verification of any
symmetry-breaking in the distribution of spin vectors
would be a significant evidence.

Figure 1. Three illustrative scenarios of galaxy formation:
(a) primordial whirl, (b) pancake shock, and (c) tidal torque.
Inferred distributions of spin vectors of galaxies are shown in
top views, side views, and views for observers located inside
the cluster of galaxies (modified from a figure in Sugai & Iye
(1995)).

There were hot debates in the middle of the last century over whether the spiral structure of galaxies winds
in a trailing way or in a leading way. It has been generally believed that the spiral structure of galaxies is
in general ”trailing” rather than ”leading.” Iye et al.
(2019) found corroborative evidence from their survey
of 146 spiral galaxies that all spiral structure in these
galaxies is indeed ”trailing.” This confirmation provides
a basis for us to use the spiral winding direction projected on the sky, either S-wise spirals or Z-wise spirals,
to judge the sign of the line-of-sight component Ωdof a
galaxy’s spin vector. This determines whether the spin
vector is pointing away or toward us.

$$
\\Omega\_{d}
$$

Borchkhadze & Kogoshvili (1976) pointed out the
number dominance of ”S”spirals over ”reverse S” spirals, hereafter referred as Z-spirals in the present paper,
in the 7,563 galaxies sampled from the Abastumani catalog of Bright Galaxies. MacGillivray & Dodd (1985)
found a similar trend and a marginal dependence on
the super galactic hemisphere. Iye & Sugai (1991) and
Sugai & Iye (1995) used S/Z parity information on spiral galaxies to study the distribution of spin angular
momentum vectors in the assembly of galaxies. However the data sets available at that time were not large
enough.

$$
\ {/2}
$$

The Galaxy Zoo 1 catalog, a morphological classification of SDSS galaxies, was compiled by a public poll. It
showed a similar predominance of S spirals as previous
studies, but Hayes et al. (2017) interpreted this as being due to human selection bias rather than a human
chirality bias or physical reality.

Shamir (2017a) published tables of 82,244 clockwise (Z-spirals) and 80,272 counterclockwise (S-spirals)
galaxies by using his Ganalyzer algorithm (Shamir
2011a,b) for a dataset of 740,908 galaxies classified as
spiral galaxies from three million SDSS Data Release
8 galaxies (Kuminski & Shamir 2016). The statistics
show over-dominance of Z-spirals from a random distribution at 3.46σ. Shamir (2017b) reported finding a
significant ”photometric anisotropy” such that the mean
magnitudes of S/Z spirals behave differently depending
on their right ascension with a possible asymmetry axis
◦ ◦
at (α = 172, δ = +50) in J2000. This axis corresponds
◦ ◦
to the direction (l = 152, b = +62) near the galac-
◦
tic pole (b = +90). Note that Shamir’s catalog shows
dominance of Z-spirals instead of the S-spiral dominance
reported by previous workers.

$$
2011\\mathrm{a a,b})
$$

$$
\\mathrm{S}/\\mathrm{Z}
$$

$$
(\\alpha=172^{\\circ},\\delta=+50^{\\circ})
$$

$$
(left\ \ =\ 152^{\\circ},b\ =\ +62^{\\circ})
$$

$$
(b=+90^{\\circ})
$$

In the present paper, we develop a formulation to
analyze the dipole anisotropy of S/Z spin distribution
of galaxies and apply this formulation to reanalyze the
Shamir’s SDSS catalog.

## 2\. FORMULATION OF DIPOLE ANALYSIS

## 2.1. Dipole Component of Spin Distribution

Number statistics can be used to study the S/Z number asymmetry from equipartition. The significance
level of the number asymmetry is given by

$$
\\sigma\_{N}=\|N(S)-N(Z)\|/\\sqrt{N(S)+N(Z)}.
$$

(1)

Another option is to look for any statistically significant dipole in the spatial distribution of S/Z-spirals.

i i i i il ib id
Let Ω (l, b, d) = (Ω, Ω, Ω) be the spin vector
i
of the i-th galaxy with galactic longitude l, galactic
i i i
latitude b, and distance d. The distance d to the
galaxy can be approximated for the nearby universe by

$$
\\Omega^{i}(l^{i},b^{i},d^{i});=;(\\Omega\_{l}^{i},\\Omega\_{b}^{i},\\Omega\_{d}^{i})
$$

$$
l^{i},
$$

$$
b^{i}.
$$

$$
d^{i}
$$

$$
d^{i}
$$ i i i
d = cz /H₀, where c is the speed of light, z is the spectroscopic/photometric redshift of the i-th galaxy and H₀
is the Hubble constant.

$$
d^{i}=c z^{i}/H\_{0}
$$

$$
z ^ {i}
$$

$$
H\_{0}
$$

i
Measuring the 3D vector Ω is nontrivial, but one can
i id
easily judge the sign h of Ω. This can be done by
examining the spiral winding sense to see if it is S-wise
i i
(h = −1) or Z-wise (h = +1), since all spiral galaxies
can be assumed to be trailing (Iye et al. 2019, : Paper
I). The net effect of misidentifying S-spirals vs Z-spirals
and improbable presence of leading spiral arms would
be reduction of the dipole strength, should it exist. For
i
simplicity, hereafter we assume that all the Ω have an
id i
unit length, namely Ω = h.

$$
\\Omega^{i}
$$

$$
h^{i}
$$

$$
\\Omega\_{d}^{i}
$$

$$
\ h^{i}=-1)
$$

$$
(h^{i}=+1)
$$

$$
\\Omega^{i}
$$

$$
\\Omega\_{d}^{i}=h^{i}
$$

i
By compiling the spin parity, h = ±1, together with
the coordinates of spiral galaxies from image archives
such as SDSS, Pan-Starrs1, ESO-DR2, DES, Subaru
HSC, and others, we estimate that one can produce a
spin parity catalog of up to a million spiral galaxies in
the 3D volume within 1 Gpc of the Earth. We are developing an analysis scheme to probe any partial volume within this volume, not necessarily centered on the
Earth. This will be discussed in a forthcoming paper.
For the moment, however, we consider a local volume
centered on the Earth.

$$
h^{i}=\\pm1
$$

To analyze the spin vector distribution in terms of
spherical harmonics expansion, one can first examine on
its dipole component Y₁₀, quadrupole component Y₂₀ and
higher components.

$$
Y\_{1}^{0}
$$

$$
Y\_{2}^{0}
$$

If we define a unit vector to a fiducial pole P(lP, bP),
one can calculate the inner product

$$
\\mathbf{P}(l\_{P},b\_{P})
$$

$$
D(l\_{P},b\_{P})=\\sum\_{i=1}^{N}h^{i}\\mathbf{\\Omega}^{i}\\mathbf{P}/N=\\sum\_{i=1}^{N}h^{i}\\cos\\theta^{i}/N
$$

(2)

i
where the angle θ is the angle between the direction
of the i-th galaxy and the direction of the fiducial pole
vector P. By determining the direction of the vector P
for which the amplitude Dmax= \|D(lP, bP)\| takes the
largest value, one can derive the dipole vector Dmaxof
the observed distribution.

$$
\\theta^{i}
$$

$$
D\_{m a x}=\|\\mathbf{D}(l\_{P},b\_{P})\|
$$

$$
{\\bf D}\_{m a x}
$$

$$
D\_{m a x}
$$

In fact, Dmaxcan be obtained simply by calculating
a vector G, which is the vector sum of the unit radial
vectors pointing to the direction of the i-th galaxy muli
tiplied by the helicity h. The inner product of G with P
takes the maximum value when P is pointing in parallel
to G, and then Dmaxis ‖G/N ‖.

$$
h^{i}
$$

$$
\ {bf G G},,
$$

$$
D\_{m a x}
$$

$$
\|\\mathbf{G}/N\|
$$

## 2.2. Perfect Dipole Distribution

We assume an extreme case of perfect dipole segregation, where all S-spirals are in the northern hemisphere and all Z-spirals are in the southern hemisphere
i
as shown in Figure 2(a). The weight factor cos θ of
Equation 2 shows that the galaxies toward the dipole

$$
\\theta^{i}
$$

i
axis with small θ add to Dmaxwhile those near the
i
equator with θ ∼ π/2 reduce Dmax. It is easy to
see by integration that the expected mean amplitude
perf ect
Dmaxof all sky sampling is 0.5. Perfect but random
dipole distribution produces fluctuation around this expected mean amplitude of 0.5. Monte Carlo simulation
shows that the associated standard deviation from this
mean amplitude for perfect random dipole distributions
√
is ∼ 0.3/ N.

$$
\\theta^{i}\ \\sim\ \\pi/2
$$

$$
D\_{m a x}
$$

$$
\\theta^{i}
$$

$$
D\_{m a x}
$$

$$
D\_{m a x}^{p e r f e c t}
$$

$$
\\sim0.3/\\sqrt{N}
$$

## 2.3. Effect of Non-uniform Sky Coverage for a Perfect Dipole Distribution

Although the currently available data from imaging
surveys are growing rapidly, the data do not yet fill the
entire sky uniformly. There may be observational biases that affect evaluation of S/Z number asymmetry
and/or the evaluation of the observed dipole vector in
the S/Z distribution. Let us examine the effect of nonuniform sky coverage for the perfect dipole distribution
case mentioned in the previous subsection.

$$
\\mathrm{S}/\\mathrm{Z}
$$

When the sky sampling is limited to a certain narrow
cone direction, the dipole amplitude can take any value
in the range 0 ≤ Dmax≤ 1 depending on the direction to
the sample. The largest amplitude Dmax= 1 is obtained
when the sampling is toward the pole, θ = 0 or π, and
the lowest amplitude Dmax= 0 is observed toward the
equator θ = π/2. Therefore depending on the direction
of the biased small sky sampling, the resulting Dmaxcan
be larger or smaller than the whole sky sampling.

$$
0\\leq D\_{m amathrm}{x x}\\leq1
$$

$$
D\_{m a x}=1
$$

$$
\\pi
$$

$$
\\theta=0
$$

$$
D\_{m a x}=0
$$

$$
\\theta=\\pi/2
$$

$$
D\_{m a x}
$$

Consider a non-uniform sampling of the complete
dipole distribution covering only the northern hemisphere as shown in Figure 2(b). There would be a conspicuous number count asymmetry. However, the dipole
strength observed would be equal to that of the whole
sky sampling. If the sampling were limited to the eastern hemisphere as shown in Figure 2(c), there would be
no number asymmetry. The dipole amplitude, again,
would be equal to that of full sky sampling.

$$
2(\\mathrm{c})
$$

The number asymmetry and the dipole amplitude thus
provide complementary information to analyze large
scale symmetry-breaking in the spin distribution of
galaxy ensembles.

## 2.4. Random Flight Simulation for an Isotropic Distribution

For a uniformly randomly distributed set of N veci
tors with Ω, the resultant vector sum Dmaxwill have
an isotropic distribution with non-zero amplitude, unless the summation has incidentally completely canceled
Dmax.

$$
\\Omega^{\\mathrm{i}}
$$

$$
\\mathbf{D\_{m a x}}
$$

$$
\\mathbf{D\_{m a x}}
$$

As Dmaxcan be calculated by ‖G/N ‖, our problem is
equivalent to a well-studied mathematical problem, 3D

$$
D\_{m a x}
$$

$$
\|\\mathbf{G}/N\|
$$

* * *

Figure 2. Effect of non-uniform sky coverage on the number asymmetry and on dipole evaluation. (a) Distribution of
spiral galaxies for an extreme case of 100% dipole asymmetry. All spirals in the northern hemisphere are exclusively
S-spirals, while all spirals in the southern hemisphere are
exclusively Z-spirals. (b) If the sampling volume is limited
only to the northern hemisphere, then only S-spirals are observed, showing an extreme asymmetry in the number count.
The dipole amplitude, however, is equal to that derived for
the entire sky. (c) If the sampling volume is limited to the
eastern hemisphere, the dipole amplitude is equal to that of
the entire sky and no asymmetry is observed in the number
count.

random walk (random flight). Namely, it is equivalent to
find the distribution of distance to the final point vector
R of a particle that starts from the origin and takes N
steps of a 3D random walk. One can evaluate the mean
amplitude of Dmaxand the standard deviation around
the mean amplitude as a function of N.

$$
D\_{m a x}
$$

Chandrasekhar (1943) established that the probability
density function W (R) of the final displacement vector
R of random flights for a large N will be a 3D Gaussian
distribution.

$$
W({\\bf R})=\\frac{1}{(2\\pi N\\langle r^{2}\\rangle\_{A v}/3)^{\\frac{3}{2}}}e x p(-3\|{\\bf R}\|^{2}/2N\\langle r^{2}\\rangle\_{A v})
$$

(3)

where 〈r²〉Avis the expected mean square displacement,
which is in our case 〈r²〉Av= 1.

$$
\\langle r^{2}\\rangle\_{A v}
$$

2
The distribution of Dmax, therefore, follows the chisquared distribution for three degrees of freedom. The
distribution of Dmax, hence, follows the chi distribution¹, a square root of chi- squared distribution. The

$$
\\langle r^{2}\\rangle\_{A v}=1
$$

$$
D\_{m a x}^{2}.
$$

$$
D\_{m a x}
$$

$$
\\overline{{D}}\_{m a x}
$$

(5)

(4)

$$
\\begin{aligned}{S t d d e v=}&{{}\\sqrt{\\frac{2\[\\Gamma(3/2)\\Gamma(5/2)-\\Gamma(2)^{2}\]}{3\\Gamma(3/2)^{2}N}}=\\sqrt{\\frac{3\\pi-8}{3\\pi N}}}\ {\\sim}&{{}\\frac{0.389}{\\sqrt{N}}.}\ \\end{aligned}
$$

We can use these formulae to evaluate the statistical significance σDof the observed spin dipole strength
Dmaxin any ensemble of spiral galaxies using
√

The associated standard deviation from this expected
mean distance is given by
√

(6)

expected mean amplitude Dmaxis
√ √

## 2.5. Detectability of Dipole Component

$$
\\sigma\_{D}\\sim(D\_{m a x}\\sqrt{N}-0.921)/0.389.
$$

$$
D\_{m a x}
$$

$$
\\overline {{D}} \_ {m a x} = \\frac {\\sqrt {2} \\Gamma (2)}{\\sqrt {3 N} \\Gamma (3 / 2)} = \\frac {2 \\sqrt {2}}{\\sqrt {3 \\pi N}} \\sim \\frac {0 . 9 2 1}{\\sqrt {N}}.
$$

Consider an ensemble of galaxies where a perfect
dipole system and a uniform random system are mixed
with fractions p and 1 − p, respectively. The observed
dipole vector Dmaxwould be, on average, a vector sum
perfect
of Dmaxwith an amplitude 0.5p and a random vector
√
with an amplitude (1 − p) × 0.921/ N in an arbitrary
direction. To discern the intrinsic dipole from the random dipole with a statistical significance of s-sigma, the
following relation is required
√

$$
\\sigma\_{D}
$$

$$
1-p,
$$

$$
\\mathbf{D}{\_{a x}}
$$

$$
(1-p)\\times0.921/\\sqrt{N}
$$

The Equation 8 indicates that between one hundred
thousand or one million spirals are necessary to detect
a 3%, or 1% residual inherent dipole system at 5σ confidence level, respectively.

(8)

Real data are not always obtained uniformly. The
quantitative discussion of the non-uniform sampling of
a random distribution in the general case is not straightforward. We examine, however, the actual S/Z data of
SDSS spirals in the next section and compare the observed dipole amplitude with those expected from simulated random distributions.

(7)

This implies

## 3\. APPLICATION TO THE S/Z DISTRIBUTION OF SDSS SPIRAL GALAXIES

$$
N\\geq(\\frac{0.921(1-p)(1+s)}{0.5p})^{2}
$$

$$
0\. 5 p \\geq (s + 1) \* 0. 9 2 1 (1 - p) / \\sqrt {N}
$$

## 3.1. Reanalysis of Shamir’s Spin Catalog

1Weisstein, Eric W. ”Chi Distribution.”
From MathWorld–A Wolfram Web Resource.
[https://mathworld.wolfram.com/ChiDistribution.html](https://mathworld.wolfram.com/ChiDistribution.html)

To apply our formulation of dipole anisotropy to real
data, we studied two samples using Shamir’s catalog

* * *

2
based on SDSS photometric data (Shamir 2017a). The
first sample retains all 162,516 spirals from the original catalog. The original sample shows an S/Z
dipole signal of Dmax= 0.00489, with its axis
◦ ◦
pointing toward (l, b) = (189, +15). This axis
coincides with that reported in Shamir (2020a),
◦ ◦ ◦ ◦
(α = 88, δ = +36), which is (l = 175, b = +5) for
an SDSS sample, considering the 1σ estimation
◦
error of about 30 in both coordinates.

$$
2017\\mathrm{a})^{2}
$$

$$
\\mathbf{S}/\\mathbf{z}
$$

$$
D\_{m a x}\ =\ 0.00489
$$

$$
(l,b),=,(189^{\\circ},+15^{\\circ})
$$

$$
(\\alpha=88^{\\circ},\\delta=+36^{\\circ})
$$

$$
\\left(l=175^{\\circ},b=+5^{\\circ}\\right)
$$

$$
30^{\\circ}
$$

For calibration, we made 50,000 independent
i
Monte Carlo simulations by assigning h = ±1
randomly to the 162,516 spirals and measured
the simulation’s Dmax. The resulting Dmaxshows
an isotropic distribution with an ensemble mean
amplitude of Dmax= 0.00225 and an associated
amplitude standard deviation of σ = 0.00105, as
shown in Table 1. The observed Dmaxfrom
the original catalog, therefore, has an amplitude, that is larger than the mean amplitude by
σD= 2.52. The number dominance of Z-spirals over
S-spirals here is σN= 4.89.

$$
h^{i};=;\\pm1
$$

$$
\\mathbf{D}{\_{a x}}
$$

$$
\\mathbf{D\_{m a x}}
$$

$$
D\_{m a x},=,0.00225
$$

$$
\\sigma=0.00105
$$

$$
D\_{m a x}
$$

$$
\\sigma\_{D},=,2.52
$$

$$
\\sigma\_{N}=4.89
$$

The second sample we studied is a volume-limited
sample retaining 111,867 spirals with measured redshift
in the range 0.01 ≤ z ≤ 0.1. To avoid any possible
effect of local peculiar motions, 162 nearby spirals at
z ≤ 0.01 were removed from this volume-limited sample. This sample shows a stronger S/Z dipole signal
Dmax= 0.00773 with its axis pointing toward (l, b) =
◦ ◦
(138, −38).

$$
0.01,\\leq,z,\\leq,0.1
$$

$$
z\\leq0.01
$$

$$
\\mathrm{S}/\\mathrm{Z}
$$

$$
(l,b)=
$$

$$
D\_{m a x}=0.00773
$$

$$
(138^{\\circ},-38^{\\circ})
$$

The Dmaxvalue observed for this sample, together
with that of 50,000 simulated mock samples is shown in
Figure 3. The observed Dmaxfrom the original catalog
limited to a volume defined by redshift, therefore, has
an amplitude, that is larger than the mean amplitude
by σD= 4.00.This amplitude happens to be close to the
value 4.34σ reported in Shamir (2020a). The number
dominance for this sample is 6.36σ.

$$
D\_{m a x}
$$

$$
D\_{m a x}
$$

$$
\\sigma\_{D}=4.00.\\mathrm{I}
$$

## 3.2. Analysis of New Cleaned Catalog

Upon re-examining Shamir’s original catalog, we
found significant duplication of entries in its tables. Apparently, Shamir (2017a) used PhotoObjAll to search
the SDSS catalog. According to the Table Description
3
of DR8, the view of PhotoPrimary, instead of PhotoObjAll, should be used to avoid duplicate detections. PhotoObjAll returns every entry from the searched images
without checking for duplication of the same object.

$$
\\mathrm{D R8^{3}}
$$

Figure 3. Dipole amplitude Dmax measured in 50,000 mock
simulations and in a sample of 111,867 spirals within a volume of 0.01 ≤ z ≤ 0.1 from Shamir (2017a). The solid line
shows the mean dipole amplitude expected from the simulation and the broken line shows ±1σ deviation from the mean
amplitude. The observed dipole (red circle) for this volumelimited sample is 4.00σ away from the expected mean amplitude.

$$
D\_{m a x}
$$

$$
0.01\\leq z\\leq0.1
$$

Figure 4. Same as Figure 3 but for a ’cleaned’ sample
of 48,089 spirals, removing multiple entries in the original
catalog.

In fact, 34,198 spiral galaxies were found to have
multiple entries with their coordinates within 3 arcsec distance of each another. For instance, one of the
galaxies in his catalog, SDSS J031945.63-000437.9 (objid=1237666300555427954) at z = 0.037, has 89 separate entries. We confirmed by visual inspection that all
of them are the same galaxy.

$$
z,=,0.037
$$

A total of 106 spirals had contradicting S/Z classification among the duplicated entries. We rectified these

2 [https://data-portal.hpc.swin.edu.au/dataset/data-for-galaxyassymetry-experiment](https://data-portal.hpc.swin.edu.au/dataset/data-for-galaxyassymetry-experiment)

3 [http://skyserver.sdss.org/dr8/en/help/docs/tabledesc.asp](http://skyserver.sdss.org/dr8/en/help/docs/tabledesc.asp) contradictions by assigning a spin parity via visual inspection in some cases. In other cases, where the voting
was significantly split, we adhered to the outcome of
majority voting.

After removing the duplicated entries, the number of
spiral galaxies is reduced to 72,888, that is 45% of the
original number. The number of spirals in the volumelimited sample range 0.01 ≤ z ≤ 0.1 is 48,089 (23,819 Sspirals and 24,270 Z-spirals), 43% of the 111,867 counted
in the original catalog. The measured amplitudes for
these ’cleaned’ samples with and without the volume
limitation are summarized in Table 1.

$$
0.01\\leq z\\leq0.1
$$

The observed dipole for the entire cleaned sample
set has Dmax= 0.00535 with its axis pointing toward
◦ ◦
(l, b) = (192, +79). 50,000 random mock simulations for the cleaned sample shows a mean amplitude
Dmax= 0.00336 and a standard deviation σ = 0.00154.
Therefore, the observed dipole deviates from the expected mean strength only at a level of σD= 1.29. Number dominance of Z-spirals over S-spirals is also only at
the σN= 1.87 level.

$$
D\_{m a x},=,0.00535
$$

$$
(l,b);=;\\left(192^{\\circ},+79^{\\circ}\\right)
$$

$$
D\_{m a x}=0.00336
$$

$$
\\sigma=0.00154
$$

$$
\\sigma\_{D}=1.29
$$

$$
\\sigma\_{N}=1.87
$$

The observed dipole for the cleaned sample limited to
the redshift range 0.01 ≤ z ≤ 0.1, is Dmax= 0.00468
◦ ◦
with its axis pointing toward (l, b) = (106, +57). Results of 50,000 random mock simulations for the cleaned
sample shows a mean amplitude Dmax= 0.00414 and a
standard deviation σ = 0.00188, as shown in Figure 4.

$$
D\_{m a x},=,0.00468
$$

$$
0.01\\leq z\\leq0.1
$$

$$
(l,b)=(106^{\\circ},+57^{\\circ})
$$

$$
D\_{m a x}=0.00414
$$

$$
\\sigma=0.00188.
$$

Therefore, the observed dipole deviates from the expected mean strength only at the σD= 0.29 level. Column (13) of Table 1, obtained from Equation 6 for uniform sampling is not necessarily correct for non-uniform
sampling. However, the fact that Column (13) shows
values close to the values in column (12), obtained from
actual sampling, suggests their relevance. Finally, the
number dominance of Z-spirals over S-spirals is also only
at the σN= 2.06 level.

$$
\\sigma\_{D}=0.29
$$

$$
\\sigma\_{N}=2.06
$$

Comparison of Figures 3 and 4 clearly shows that the
apparent pseudo dipole signal observed in Figure 3 came
from massively duplicated data in the original catalog.

As a final remark, Longo (2011) made a similar analysis of his sample of 15,158 spirals with z ≤ 0.085 from
SDSS DR6. He used the terms left-handed (S-spiral
in the present paper) and right-handed (Z-spiral). He
found a dipole asymmetry by plotting the distribution
of A = (Z − S)/(Z + S). The dipole strength under his
definition was −0.0408±0.011, found with an axis point-
◦ ◦
ing at (l, b) = (52, +68.5) at 5.6σ. The relation of his
study to the current work has yet to be investigated.

$$
z\\leq0.085
$$

$$
A=\\big(Z-S\\big)/\\big(Z+S\\big)
$$

$$
(l,b)=(52^{\\circ},+68.5^{\\circ})
$$

## 4\. CONCLUSION

We present a formulation to quantify the observed
dipole amplitude Dmaxof the S/Z spin parity distri-

$$
D\_{m a x}
$$

$$
\\mathrm{S}/\\mathrm{Z}
$$

bution of spirals in an ensemble of galaxies. We show
that the statistical significance σDof this quantity can
be calibrated with that expected from 3D random flight
simulations.

$$
\\sigma\_{D}
$$

Notably, we found that the S/Z spin catalog published
by Shamir (2017a) contains a significant amount of duplicated data, which at least partly caused the increased
level of dipole asymmetry that we observed. After removing the duplicated entries from the catalog, we found
that the distribution is compatible with random distribution. We conclude that the SDSS sample of spiral
galaxies does not show large scale anisotropy in the spin
distribution of galaxies.

$$
\\mathrm{S}/\\mathrm{Z}
$$

Recently, Shamir (2020b) studied another dataset
based on spectroscopic sample to detect a significant
dipole signal. Previously Shamir (2012) also presented
that a dataset based on SDSS SpecObj shows a significant dipole signal, while the direction of the axis is different. The different results from the different datasets
will be investigated elsewhere.

The current authors are compiling a large coherent dataset of spiral winding evaluation as derived
from several modern large image datasets, including
the SDSS (Aguado et al. 2018), the Panoramic Survey
Telescope and Rapid Response System (Pan-Starrs1:
Chambers et al. 2016), the Hyper Suprime-Cam (HSC:
Miyazaki et al. 2018) of Subaru Telescope, and the
Dark Energy Survey (Abbott et al. 2018) by deep
learning algorithm. Tadaki et al. (2020) developed a
deep learning algorithm to judge S/Z winding of 76,635
spiral galaxies from the Hyper Suprime-Cam Subaru
Strategic Program Data Release 2 dataset (HSC SSP
DR2: Aihara et al. 2019) sample, with further objective to generate a galactic spin data catalog.

$$
\\mathrm{S}/\\mathrm{Z}
$$

* * *

Table 1. Observed dipole asymmetry in the spin distribution of SDSS galaxies. Column(6) is the number asymmetry significance
obs
level. Columns (7-9) shows the observed amplitude and the direction of the dipole Dmax, while Columns (10) and (11) show the
mean amplitude of Dmax from 50,000 mock simulations and the standard deviation from the mean value, respectively. Column
(12) is the observed significance level of Dmax. Column(13) is the expected significance level for an isotropic random distribution
as given by Equation 6.

$$
\\mathbf{D\_{m a x}^{o b s}}
$$

$$
D\_{m a x}
$$

$$
D\_{m a x}
$$

| (1)Sample | (2)redshift range | (3)N | (4)N(S) | (5)N(Z) | (6)$\\sigma\_{N}$ | (7)$D\_{max}^{obs}$ | (8)l | (9)b | (10)$\\overline{D}\_{max}$ | (11)stddev | (12)$\\sigma\_{D}^{obs}$ | (13)$\\sigma\_{D}^{iso}$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Original | All | 162,516 | 80,272 | 82,244 | 4.89 | 0.00489 | 189 | +15 | 0.00225 | 0.00105 | 2.52 | 2.70 |
| Original | 0.01≤z≤0.1 | 111,867 | 54,870 | 56,997 | 6.36 | 0.00773 | 138 | -38 | 0.00271 | 0.00126 | 4.00 | 4.28 |
| Cleaned | All | 72,888 | 36,191 | 36,697 | 1.87 | 0.00535 | 192 | +79 | 0.00336 | 0.00154 | 1.29 | 1.34 |
| Cleaned | 0.01≤z≤0.1 | 48,089 | 23,819 | 24,270 | 2.06 | 0.00468 | 106 | +57 | 0.00414 | 0.00188 | 0.29 | 0.27 |

$$
D\_{m a x}^{o b s}
$$

$$
(12)
$$

$$
\\overline{{D}}\_{m a x}
$$

$$
0.01\\leq z\\leq0.1
$$

$$
\\sigma\_{D}^{o b s}
$$

$$
\\sigma\_{D}^{i s o}
$$

$$
0.01\\leq z\\leq0.1
$$

## ACKNOWLEDGMENTS

$$
+57
$$

Special thanks are due to Lior Shamir who gave us useful comments to improve the present paper. We thank
the anonymous referee for helpful comments. Data analysis of this study was in part carried out on the Multiwavelength Data Analysis System operated by the Astronomy Data Center (ADC), National Astronomical
Observatory of Japan. This research has made use of
NASA’s Astrophysics Data System Bibliographic Services. Funding for SDSS-III has been provided by the
Alfred P. Sloan Foundation, the Participating Institutions, the National Science Foundation, and the U.S. Department of Energy Office of Science. The SDSS-III web
site is [http://www.sdss3.org/](http://www.sdss3.org/). SDSS-III is managed by
the Astrophysical Research Consortium for the Participating Institutions of the SDSS-III Collaboration including the University of Arizona, the Brazilian Participation Group, Brookhaven National Laboratory, Carnegie
Mellon University, University of Florida, the French
Participation Group, the German Participation Group,
Harvard University, the Instituto de Astrofisica de Canarias, the Michigan State/Notre Dame/JINA Participation Group, Johns Hopkins University, Lawrence
Berkeley National Laboratory, Max Planck Institute for
Astrophysics, Max Planck Institute for Extraterrestrial
Physics, New Mexico State University, New York University, Ohio State University, Pennsylvania State University, University of Portsmouth, Princeton University,
the Spanish Participation Group, University of Tokyo,
University of Utah, Vanderbilt University, University of
Virginia, University of Washington, and Yale University.

## REFERENCES

Abbott, T. M. C. Abdalla, F. B., Allam, S. et al. , 2018,
ApJS, 239, 18
Agertz, O., Teyssier, R. & Moore, B. 2011, MNRAS, 410,
1391.

Aguado, D. S., Aumada, R. Almeida, A.et al. , 2018, ApJS,
240, 23
Aihara, H.,, AlSayyad,Y., Ando,M. et al. 2019, PASJ, 71,
114

* * *

Borchkhadze, T. M. & Kogoshvili, N. G. 1976, A&A, 53,
431
Ceverino, D., Primack, J., Dekel, A. et al. , 2017, MNRAS,
467, 2664
Chambers, K. C., Magnier, E. A., Metcalfe, N. et al. 2016,
arXiv:1612.05560
Chandrasekhar, S. 1943, Rev. Modern Physics,15, 1
Ferreira,E.G.M., 2020, arXiv:2005.03254v1
Hayes, W. B., Davis, D., & Silva, P. 2017, MNRAS, 466,
3928
Iye, M. and Sugai, H. 1991, ApJ, 374, 112
Iye, M., Tadaki, K. and Fukumoto, H. 2019, ApJ, 886, 133
Kuminski, E. & Shamir, L. 2016, ApJS, 223, 20
Longo, M. 2011, Physics Letter B, 669, 224
MacGillivray, T. M. & Dodd, R. J. 1985, A&A, 145, 269
Miyazaki, S., Komiyama, Y., Kawanomoto, S. et al. 2018,
PASJ, 70, 1
Peebles, P. J. E., 1969, ApJ, 155, 393
Robertson, B., Yoshida, N., Springel, V. et al. 2004, ApJ,
606, 32

Shamir, L. 2011a, The Astrophysics Space Code Library,
p.ascl:1105.011
Shamir, L. 2011b, ApJ, 736, 141
Shamir, L. 2012, Phys. Let. B, 715, 25
Shamir, L. 2017a, PASA, 34, e011
Shamir, L. 2017b, PASA, 34, e044
Shamir, L. 2020a, Astron. N., 341, 324
Shamir, L. 2020b, Ap&SS, 365, 136
Shimizu I., Todoroki, K., Yajima, H. and Nagamine, K.,
2019, MNRAS, 484, 2632-2655
Steinmetz, M. & Navarro, J. F. 2002, NewA, 7,155.
Sugai, H. & Iye, M. 1995, MNRAS, 276, 327
Tadaki, K., Iye, M., Fukumoto, H., Hayashi, M., Rusu, C.
E., Shimakawa, R. and Tosaki T. 2020, MNRAS, xxx, yyy
von Weizsaecker, C. F., 1955, Zeitshrift fur Astronomie, 35,
252
White, S. & Rees, M. 1978, MNRAS, 183, 341.
White, S., 1984, ApJ, 286, 38
Zeldovich, Y. B., 1970, A&A. 5, 84
