URL: https://arxiv.org/pdf/2206.03625

# Measurement of Parity-Odd Modes in the Large-Scale

# 4-Point Correlation Function of SDSS BOSS DR12 CMASS and LOWZ Galaxies

1,2⋆ 1,3
Jiamin Hou, Zachary Slepian, _†_ & Robert N. Cahn³

1 _Department of Astronomy, University of Florida, Gainesville, FL 32611, USA_

2 _Max-Planck-Institut f¨ur Extraterrestische Physik, Postfach 1312, Giessenbachstr., 85748 Garching, Germany_

3 _Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA_

## ABSTRACT

A tetrahedron is the simplest shape that cannot be rotated into its mirror image in 3D. The 4-Point Correlation
Function (4PCF), which quantifies excess clustering of quartets of galaxies over random, is the lowest-order statistic
sensitive to parity violation. Each galaxy defines one vertex of the tetrahedron. Parity-odd modes of the 4PCF
probe an imbalance between tetrahedra and their mirror images. We measure these modes from the largest currently
available spectroscopic samples, the 280,067 Luminous Red Galaxies (LRGs) ofthe Baryon Oscillation Spectroscopic
Survey (BOSS)DR12 LOWZ (¯ _z_ = 0\*. _32) and the 803,112 LRGs of BOSS DR12 CMASS (¯z = 0_. _57). In LOWZ we find_
_3_. _1_ σ\\* evidence for a non-zero parity-odd 4PCF, and in CMASS we detect a parity-odd 4PCF at 7\*. _1_ σ\*. Gravitational
evolution alone does not produce this effect; parity-breaking in LSS, if cosmological in origin, must stem from the
epoch of inflation. We have explored many sources of systematic error and found none that can produce a spurious
parity-odd _signal_ sufficient to explain our result. Underestimation of the _noise_ could also lead to a spurious detection.
Our reported significances presume that the mock catalogs used to calculate the covariance sufficiently capture the
covariance of the true data. We have performed numerous tests to explore this issue. The odd-parity 4PCF opens
a new avenue for probing new forces during the epoch of inflation with 3Dlarge-scale structure; such exploration is
timely given large upcoming spectroscopic samples such as DESI and Euclid.

Key words: early Universe — large-scale structure of the Universe — cosmology: observations — galaxies: statistics
— methods: data analysis

Submission to MNRAS: June 08 2022, Received: June 11 2022, Accepted: April 01 2023

## 1 INTRODUCTION

The laws of nature respect certain symmetries; the physical processes governed by them are invariant under the corresponding
transformations. Parity transformation (P), which reverses the sign of each coordinate axis, had been thought to be such a
symmetry. Indeed, the electromagnetic and strong interactions are invariant under P. However, this symmetry is broken in the
weak interaction (Lee & Yang1956;Wu et al.1957).Sakharov(1967) showed that the matter-antimatter asymmetry of the
Universe requires that the combination CP of P and charge-conjugation (C) symmetry be broken. The currently-known CP
violation is inadequate to explain the observed matter-antimatter asymmetry. Whatever additional CP violation is responsible
arXiv:2206.03625v2 \[astro-ph.CO\] 23 Jun 2023
may involve pure P violation as well.

Most of the cosmological studies of parity invariance to date have focused on Cosmic Microwave Background (CMB) polarization (Lue et al.1999;Kamionkowski & Souradeep2011;Shiraishi et al.2011;Minami & Komatsu2020) or on gravitational
waves (Saito et al.2007;Yunes et al.2010;Jeong & Kamionkowski2012;Wang et al.2013;Zhu et al.2013;Nishizawa &
Kobayashi2018;Orlando et al.2021). A recent CMB study of parity violation reported 2\*. _4_ σ\\* evidence for cosmic birefringence
(where the two polarization states of a wave propagate differently) (Minami & Komatsu2020).Eskilt & Komatsu(2022)
refined this analysis and found 3\*. _6_ σ\\* evidence.

A number of mechanisms producing parity violation at cosmological scales have been presented in the literature. For instance,
one can add a Chern-Simons coupling to the standard cosmological paradigm at early or at late times.This term typically
describes an interaction between a pseudo-scalar field and a spin-1 field (Sorbo2011;Barnaby et al.2011; Ozsoy ¨ 2021) or a

⋆E-mail: [jiamin.hou@ufl.edu](mailto:jiamin.hou@ufl.edu) (JH)

_†_ E-mail: [zslepian@ufl.edu](mailto:zslepian@ufl.edu) (ZS)

* * *

2

Figure 1. Parity transformation applied to a tetrahedron formed by a quartet of galaxies. Each vertex represents a galaxy. Choosing one
galaxy (red dot) as our primary, the quartet is defined by the three vectors to the remaining vertices, r1, r2, and r3. For a quartet, the
subscripts are fixed by requiring that _r_ 1 _≤ r_ 2 _≤ r_ 3. When viewing the tetrahedron from the primary (red) looking down along each vector
ri, the direction in which one reads going from smallest to largest side ( _r_ 1to _r_ 3) defines a handedness, either clockwise or counterclockwise.
Here, the tetrahedron on the left, as viewed from the primary, is clockwise. Parity transformation in 3D is a reflection about a plane and
then a 180◦rotation about the vector perpendicular to that plane, and converts the clockwise tetrahedron at left to the counterclockwise
one at right. When one averages over rotations, as in this work, only the mirroring matters.

$$
\\mathbf{r} _{1},,\\mathbf{r}_{2},
$$

$$
\\mathbf{r}\_{3}.
$$

$$
r\_{1}\\leq r\_{2}\\leq r\_{3}
$$

$$
\\mathbf {r} \_ {i}
$$

$$
(r\_{1}
$$

$$
180^{\\circ}
$$

spin-2 field (Jackiw & Pi2003;Alexander & Yunes2009;Soda et al.2011;Dyda et al.2012). The pseudo-scalar field can be
axion-like and if present at late times, can play the role of dark matter or dark energy. In this case, the Chern-Simons coupling
1
can rotate the polarizations of initially linearly-polarized CMB photons. In contrast, if the axion-like field plays the role of the
inflaton, the couplingcan give rise to non-vanishing parity-odd polyspectra of the primordial curvature perturbations (Bartolo
et al.2015;Shiraishi2016). Since the curvature perturbations seed the subsequent formation of large-scale structure, the
primordial parity-odd polyspectra would produce the same in the late-time distribution of galaxies.

Recently,Cahn et al.(2023) made the novel proposal of using the galaxy 4-Point Correlation Function (4PCF) to probe
parity violation in 3D large-scale structure.Four galaxies can be taken as the vertices of a tetrahedron, the lowest-order 3D
shape that cannot be rotated into its mirror image, rendering the 4PCF sensitive to parity violation. An illustration of a galaxy
quartet and how we define parity on it, is shown in Fig.1. FollowingCahn et al.(2023), we expand the 4PCF in the isotropic
( _i.e._ rotation-averaged) basis functions ofCahn & Slepian(2020). In the standard inflationary paradigm (Albrecht & Steinhardt
1982;Linde1982,1983), we would not expect a parity-odd 4PCF.The initial density fluctuations are a Gaussian Random
Field(Bardeen1980;Starobinsky1982), which then evolves under gravity and forms galaxies at late times. Gravity, and even
the baryonic physics of galaxy formation, is parity-conserving. Hence, the detection of a parity-odd 4PCF of cosmological
origin would be evidence that parity violation was present before the known forces dominated the evolution of the matter
distribution.

We present here a measurement of the parity-odd modes of the 4PCF measured using the Baryon Oscillation Spectroscopic
Survey (BOSS;BOSS collaboration et al.2017) of Sloan Digital Sky Survey (SDSS)-III (Dawson et al.2013;Eisenstein et al.
2011).Philcox et al.2021bpresented the parity-even 4PCF measurement on the same dataset and found an 8\*. _1_ σ\\* detection
of a non-Gaussian 4PCF (expected in the standard picture of gravitationally evolved structure formation, _e.g._ Bernardeau
et al.2002). A progenitor of the algorithm and approach here used was employed to measure the 3-Point Correlation Function
(3PCF) of BOSS DR12 CMASS (Slepian et al.2017a,b,c,Sugiyama et al.2019,2021), and extended to use Fourier transforms
inSlepian & Eisenstein(2015c);Portillo et al.(2018) and to the anisotropic 3PCF inSlepian & Eisenstein(2018);Friesen
et al.(2017);Garcia & Slepian(2020). The 4PCF has been measured before in just a few works (in 2D;Fry & Peebles1978;
averaged over internal angles (Sabiu et al.2019), as well as in Fourier space and with a degree of compression (integrated
trispectrum;Gualdi & Verde2022), but never separated into parity-odd modes; the history ofN-Point Correlation Functions
(NPCFs) is reviewed inPeebles(2001).

Given that as yet no detection of parity-odd physics in large-scale structure has been made and that a number of proposed
theoretical models can produce it, in this work we pursue a model-independent analysis. Hence we lack an _a priori_ expectation
for the shape of the signal. While using such a model could strengthen any detection significance by correlating data in different

1Helical primordial gravitational waves couldin principleleave an imprint on the cross-spectrum between the _E_ and _B_ modes of CMB
polarization, or between _B_ modes and temperature fluctuations. However, these observables are suppressed by the two-dimensional nature
of the CMB (Masui et al.2017)

* * *

3

modes, it would inevitably tie our detection significance to a particular model, which we wish to avoid. In contrast to typical
analyses _e.g._ of the 2PCF for Baryon Acoustic Oscillations (BAO) or the 3PCF for BAO or galaxy biasing, in this work we
cannot identify systematic errors simply by observing departures from an expected template for the cosmological signal. We
must thus pay especial attention to systematics. We make extensive use of both mock catalogs and analytics to assess whether
any systematics can produce spurious parity-odd 4PCF modes.

$$
e.g.
$$

$$
\\mathrm{2P C F}
$$

Our fiducial cosmology here matches that adopted by BOSS (BOSS collaboration et al.2017). In particular, we take a
geometrically flat ΛCDM model with redshift-zero matter density (in units of the critical density) Ωm = 0\*. _31, baryon density_
_(in units of the critical density) Ωb= 0_. _048, Hubble constant h ≡ H₀/(100 km_/ _s_/ _Mpc) = 0_. _676, root-mean-square density_
_−1P_
_fluctuations (within 8_ h\* Mpc spheres) of _σ₈_ = 0\*. _8, scalar spectral tilt ns = 0_. _96 and sum of the neutrino massesimν,i =_
_0_.\*06 eV.

$$
\\Omega\_{\\mathrm{m}}=0.31
$$

$$
\\Omega\_{\\mathrm{b}},=,0.048
$$

$$
8mathrm h{{}}{^-1}\\mathrm{M p}
$$

$$
h\\equiv H\_{0}/(100;\\mathrm{k m}s/\\mathrm{M p c})=0.670
$$

$$
\\sigma\_{8}=0.8
$$

$$
0.06;\\mathrm{e V}
$$

$$
n\_{\\mathrm{s}}=0.96
$$

$$
\\textstyle\\sum\_{i}m\_{\\nu,i}=
$$

The present work is organized as follows. §3outlines the multiple analyses of varying complexity used to increase confidence
in our measurements. §2reviews the basis used to decompose the 4PCF. We also present a toy model to illustrate the relation
between parity and tetrahedra. §4describes the data, simulations, and covariance matrix. §5then presents two different paths
to obtaining a detection significance and their outcomes. We also present an analysis of cross-correlations between spatially
separated regions. §6outlines our systematics tests on mocks as well as analytic work. §7concludes. A number of Appendices
present details of the work.

$$
\\S7
$$

## 2 METHOD FOR 4PCF MEASUREMENT

The 4PCF estimator, indicated by a hat, is

$$
\\begin{array}{l c l}{\\hat{\\zeta}({\\bf r} _{1},{\\bf r}_{2},{\\bf r} _{3})}&{\\equiv}&{\\displaystyle\\langle\\delta({\\bf s})\\delta({\\bf s}+{\\bf r}_{1})\\delta({\\bf s}+{\\bf r} _{2})\\delta({\\bf s}+{\\bf r}_{3})\\rangle}\ {}&{=}&{\\displaystyle\\int\\frac{d{\\bf s}}{V}:\\delta({\\bf s})\\delta({\\bf s}+{\\bf r} _{1})\\delta({\\bf s}+{\\bf r}_{2})\\delta({\\bf s}+{\\bf r}\_{3}),}\ \\end{array}
$$

(1)

where angle brackets denotes an ensemble average of the density fluctuations field _δ_(s) _≡ ρ_(s) _/ρ_ ¯ _−_ 1, with _ρ_(s) the density
2
field and ¯ _ρ_ the average density. Invoking ergodicity, the ensemble average may be replaced by an integral of spatial position
s over the volume _V_. This integration results in a function that depends only on the relative separation vectors r₁, r₂, and r₃.
We also average over joint rotations of these vectors. In practice, the density fluctuation field is computed from discrete galaxy
data, appropriately weighted.

$$
\\bar{\\rho}
$$

$$
\\delta (\\mathbf {s}) \\equiv \\rho (\\mathbf {s}) / \\bar {\\rho} - 1
$$

$$
\\rho(\\mathbf{s})
$$

$$
\\mathbf{r} _{1},\\mathbf{r}_{2},
$$

$$
\\mathbf{r}{\_33}
$$

Since the 3D distribution of galaxies is assumed to be isotropic on cosmological scales (ignoring redshift-space distortions),
the isotropic basis (Cahn & Slepian2020) is an efficient means of systematically extracting cosmological information. The
isotropic basis functions required to measure an NPCF are given by products of ( _N −_ 1) spherical harmonics _Yℓm_(ˆr) combined
according to angular momentum addition. In particular, for the 4PCF ( _N_ = 4) we require the three-argument basis functions,
which are
X

$$
Y\_{\\ell m}(\\hat{\\mathbf{r}})
$$

$$
\\mathcal {P} \_ {\\ell\_ {1} \\ell\_ {2} \\ell\_ {3}} \\left(\\hat {\\mathbf {r}} \_ {1}, \\hat {\\mathbf {r}} \_ {2}, \\hat {\\mathbf {r}} \_ {3}\\right) = \\sum\_ {m \_ {1} m \_ {2} m \_ {3}} \\mathcal {C} \_ {m \_ {1} m \_ {2} m \_ {3}} ^ {\\ell\_ {1} \\ell\_ {2} \\ell\_ {3}} Y \_ {\\ell\_ {1} m \_ {1}} \\left(\\hat {\\mathbf {r}} \_ {1}\\right) Y \_ {\\ell\_ {2} m \_ {2}} \\left(\\hat {\\mathbf {r}} \_ {2}\\right) Y \_ {\\ell\_ {3} m \_ {3}} \\left(\\hat {\\mathbf {r}} \_ {3}\\right).
$$

(2)

The factorizability of these functions is important to the speed-up of the 4PCF algorithm (Philcox et al.2021a); in practice,
it enables us to compute the 4PCF as a sum over the spherical harmonic coefficients _aℓimi_ of the density field about a given
primary galaxy at s.

$$
a\_{\\ell\_{i}m\_{i}}
$$

3
Each unit vector ˆr _i_ is associated with one total angular momentum _ℓi_, with _z_-component _mi_. The key point is simply that
spherical harmonics are two-index tensors, and conventionally the total angular momentum and its _z_-component are chosen
to represent them. This point is further discussed inCahn & Slepian(2020) around their equation 2.The weight is
!

$$
\ {\\hat{\\mathbf{r}}}\_{i}
$$

$$
\\ell\_{i,1}
$$

$$
{m\_{i}.}^{3}
$$

$$
\\mathcal{C} _{m_{1}m\_{2}m\_{3}}^{\\ell\_{1}\\ell\_{2}\\ell\_{3}}\\equiv(-1)^{\\ell\_{1}+\\ell\_{2}+\\ell\_{3}}\\left(\\begin{array}{c c c}{\\ell\_{1}}&{\\ell\_{2}}&{\\ell\_{3}}\ {m\_{1}}&{m\_{2}}&{m\_{3}}\ \\end{array}\\right).
$$

(3)

The 3- _j_ symbol enforces the triangular inequality _\|ℓ₁ − ℓ₂\| ≤ ℓ₃ ≤ ℓ₁_ \+ _ℓ₂_, because the total angular momentum must be
4ˆ, a spherical harmonicℓ
zero for an isotropic function. Under the parity operator, denoted **P** _Yℓm_ transforms as (\*−\*1), so the
three-argument isotropic functions transform as
ˆ \[\
\
$$\
\|\\ell\_{1}-\\ell\_{2}\|\\leq\\ell\_{3}\\leq\\ell\_{1}+\\ell\_{2}\
$$\
\
$$\
\\mathbb{\\bar{P}}\
$$\
\
$$\
Y\_{\\ell m}\
$$\
\
$$\
(-1)^{\\ell}\
$$\
\
$$\
\\begin{array}{l c l}{\\hat{\\mathbb{P}}\\left\[\\mathcal{P} _{\\ell_{1}\\ell\_{2}\\ell\_{3}}(\\hat{\\mathbf{r}} _{1},\\hat{\\mathbf{r}}_{2},\\hat{\\mathbf{r}} _{3})\\right\]}&{\\equiv}&{\\mathcal{P}_{\\ell\_{1}\\ell\_{2}\\ell\_{3}}(-\\hat{\\mathbf{r}} _{1},-\\hat{\\mathbf{r}}_{2},-\\hat{\\mathbf{r}} _{3})}\ {}&{=}&{(-1)^{\\ell_{1}+\\ell\_{2}+\\ell\_{3}}\\mathcal{P} _{\\ell_{1}\\ell\_{2}\\ell\_{3}}(\\hat{\\mathbf{r}} _{1},\\hat{\\mathbf{r}}_{2},\\hat{\\mathbf{r}} _{3})=\\mathcal{P}_{\\ell\_{1}\\ell\_{2}\\ell\_{3}}^{\*}(\\hat{\\mathbf{r}} _{1},\\hat{\\mathbf{r}}_{2},\\hat{\\mathbf{r}}\_{3}).}\ \\end{array}\
$$\
\
(4)\
\
2The 4PCF after rotation-averaging has six degrees of freedom, so we will only require certain combinations of the arguments on the\
lefthand side of the estimator.\
\
3Given the rotational symmetry of the system, the choice of _z_-axis is arbitrary.\
\
4We recall that a 3- _j_ symbol with zeros in the bottom row demands that _ℓ_ \+ _ℓ_ \+ _ℓ_ be even, but with non-zero _m_ there is no such\
1 2 3 i\
requirement, allowing odd sums of the _ℓ_ iand hence parity-odd basis functions.\
\
$$\
3{-j}\
$$\
\
$$\
m\_{i}\
$$\
\
$$\
\\ell\_{1}+\\ell\_{2}+\\ell\_{3}\
$$\
\
$$\
\\ell\_{i}\
$$\
\
* * *\
\
4\
\
$$\
\\ell\_{1}+\\ell\_{2}+\\ell\_{3}\
$$\
\
Thus the basis functions are real if _ℓ₁_ \+ _ℓ₂_ \+ _ℓ₃_ is even and imaginary if the sum is odd.\
\
The isotropic functions also satisfy an orthonormality relation, which follows from that of the spherical harmonics. We have\
Z\
\
$$\
\\int d\\hat{\\mathbf r} _{1}d\\hat{\\mathbf r}_{2}d\\hat{\\mathbf r} _{3}:\\mathcal{P}_{\\ell\_{1}\\ell\_{2}\\ell\_{3}}(\\hat{\\mathbf r} _{1},\\hat{\\mathbf r}_{2},\\hat{\\mathbf r} _{3}):\\mathcal{P}_{\\ell\_{1}^{\\prime}\\ell\_{2}^{\\prime}\\ell\_{3}^{\\prime}}^{\*}(\\hat{\\mathbf r} _{1},\\hat{\\mathbf r}_{2},\\hat{\\mathbf r} _{3})=\\delta_{\\ell\_{1}\\ell\_{1}^{\\prime}}^{\\mathsf K{}}\\delta\_{\\ell\_{2}\\ell\_{2}^{\\prime}}^{\\mathsf{K}}\\delta\_{\\ell\_{3}\\ell\_{3}^{\\prime}}^{\\mathsf{K}}.\
$$\
\
(5)\
\
K\
The Kronecker delta _δ_ ℓℓ′iis unity when its subscripts are equal and zero otherwise.\
i\
\
$$\
\\delta\_{\\ell\_{i}\\ell\_{i}^{\\prime}}^{\\mathrm{K}}\
$$\
\
The 4PCF estimator defined in Eq. (1) can be expanded into the basis of isotropic functions (see Eq.2), where the expansion\
coefficients depend only on the _ri_ and are given by orthogonality as\
Z Z\
\
$$\
r\_{i}\
$$\
\
$$\
\\tilde{\\zeta} _{\\ell_{1}\\ell\_{2}\\ell\_{3}}({r} _{1},{r}_{2},{r} _{3})=\\int\\frac{d\\mathbf{s}}{V}:\\delta(\\mathbf{s})\\int d\\hat{\\mathbf{r}}_{1}d\\hat{\\mathbf{r}} _{2}d\\hat{\\mathbf{r}}_{3}:\\delta(\\mathbf{s}+\\mathbf{r} _{1})\\delta(\\mathbf{s}+\\mathbf{r}_{2})\\delta(\\mathbf{s}+\\mathbf{r} _{3}):{\\cal P}_{\\ell\_{1}\\ell\_{2}\\ell\_{3}}^{\*}(\\hat{\\mathbf{r}} _{1},\\hat{\\mathbf{r}}_{2},\\hat{\\mathbf{r}}\_{3}).\
$$\
\
(6)\
\
To avoid an over-complete basis, the radial arguments _ri_ are ordered as _r₁ ≤ r₂ ≤ r₃_, as further discussed inCahn & Slepian\
(2020).\
\
$$\
r\_{i}\
$$\
\
$$\
r\_{1}\\leq r\_{2}\\leq r\_{3}.\
$$\
\
To construct a density fluctuation field from the discrete galaxy counts, and also to account for the survey geometry, we\
use a generalized Landy-Szalay estimator (Landy & Szalay1993;Szapudi & Szalay1998, see alsoKerscher et al.2000) as first\
outlined for the angular momentum basis inSlepian & Eisenstein(2015b) and further developed inPhilcox et al.(2021a,b). It\
is\
N(r, r, r)\
\
$$\
\\hat{\\zeta}(\ \\mathbf{r} _{1},\\mathbf{r}_{2},\\mathbf{r} _{3})=\\frac{\\mathcal{N}(\\mathbf{r}_{1},\\mathbf{r} _{2},\\mathbf{r}_{3})}{\\mathcal{R}(\\mathbf{r} _{1},\\mathbf{r}_{2},\\mathbf{r}\_{3})},\
$$\
\
(7)\
\
4\
where _N ≡_ ( _D−R_) and _R≡ R⁴_, and these powers are shorthand for expanding by the binomial theorem and letting each _D_\
and _R_ be evaluated at a different spatial position. _D_ means a particle drawn from the “data” and _R_ means a particle drawn\
from the “random” catalog (a spatially uniform catalog cut by the survey geometry). As outlined inSlepian & Eisenstein\
(2015b), we may estimate the numerator and denominator separately ( _i.e._ compute each separately averaging over the whole\
survey). Doing so gives optimally weighted estimates of each in the shot-noise limit, as discussed inSlepian & Eisenstein2015b\
§4, equations 24-26 and surrounding text. Multiplying Eq. (7) through by _R_, expanding each side of the resulting relation in\
the isotropic basis, reducing a product of two isotropic basis functions to a sum over single ones, and finally taking an inverse\
to solve the linear system so obtained (Slepian & Eisenstein2015b;Philcox et al.2021a), we find the edge-corrected 4PCF\
estimator as\
X N(r ,r ,r)\
\
$$\
\\mathcal{N}\\equiv(D-R)^{4}\
$$\
\
$$\
\\mathcal{R}\\equiv R^{4}\
$$\
\
$$\
\\S4,\
$$\
\
$$\
{\\boldsymbol R},\
$$\
\
$$\
\\hat{\\zeta} _{\\ell_{1}\\ell\_{2}\\ell\_{3}}(r\_{1},r\_{2},r\_{3})=\\sum\_{\\ell\_{1}^{\\prime}\\ell\_{2}^{\\prime}\\ell\_{3}^{\\prime}}\\left\[\\mathbf{M}^{-1}\\right\] _{\\ell_{1}\\ell\_{2}\\ell\_{3},\\ell\_{1}^{\\prime}\\ell\_{2}^{\\prime}\\ell\_{3}^{\\prime}}\\left(r\_{1},r\_{2},r\_{3}\\right)\\frac{\\mathcal{N} _{\\ell_{1}^{\\prime}ell\_{2}^{\\prime}\\ell\_{3}^{\\prime}}(r\_{1},r\_{2},r\_{3})}{\\mathcal{R} _{000}(r_{1},r\_{2},r\_{3})}.\
$$\
\
(8)\
\
We note that there is no mixing in the radial variables; survey geometry does not change lengths. Our notation indicates a given\
−1\
element of M. This latter is the inverse of the coupling matrix M describing how survey geometry breaks the orthogonality\
of our basis functions, much as Fourier modes are orthogonal only on an infinite domain. _N_ denotes a measurement from the\
“data-minus-random” catalog, and _R₀₀₀_ is the _ℓ₁_ = _ℓ₂_ = _ℓ₃_ = 0 expansion coefficient of _R≡ R⁴_, _i.e._ the randoms’ 4PCF. _N_\
and _R_ are evaluated by replacing _δ_ in Eq. (6) with their definitions, given below Eq. (7).\
\
$$\
\\mathbf{M}^{-1}\
$$\
\
$$\
\\mathcal{N}\
$$\
\
$$\
\\mathcal{R}\_{000}\
$$\
\
$$\
\\ell\_{1}=\\ell\_{2}=\\ell\_{3}=0\
$$\
\
$$\
\\mathcal{R}\\equiv R^{4}\
$$\
\
$$\
\\delta\
$$\
\
The coupling matrix has elements\
\
$$\
\\mathbf {M} \_ {\\ell\_ {1} \\ell\_ {2} \\ell\_ {3}, \\ell\_ {1} ^ {\\prime} \\ell\_ {2} ^ {\\prime} \\ell\_ {3} ^ {\\prime}} \\left(r \_ {1}, r \_ {2}, r \_ {3}\\right) = (4 \\pi) ^ {- 3 / 2} (- 1) ^ {\\ell\_ {1} ^ {\\prime} + \\ell\_ {2} ^ {\\prime} + \\ell\_ {3} ^ {\\prime}} \\sum\_ {L \_ {1} L \_ {2} L \_ {3}} \\frac {\\mathcal {R} \_ {L \_ {1} L \_ {2} L \_ {3}} \\left(r \_ {1}, r \_ {2}, r \_ {3}\\right)}{\\mathcal {R} \_ {0 0 0} \\left(r \_ {1}, r \_ {2}, r \_ {3}\\right)} \\prod\_ {i = 1} ^ {3} D \_ {\\ell\_ {i} L \_ {i} \\ell\_ {i} ^ {\\prime}} ^ {\\mathrm {P}} \\mathcal {C} \_ {0 0 0} ^ {\\ell\_ {i} L \_ {i} \\ell\_ {i} ^ {\\prime}} \\left{ \\begin{array}{l l l} \\ell\_ {1} & L \_ {1} & \\ell\_ {1} ^ {\\prime} \ \\ell\_ {2} & L \_ {2} & \\ell\_ {2} ^ {\\prime} \ \\ell\_ {3} & L \_ {3} & \\ell\_ {3} ^ {\\prime} \\end{array} \\right},\
$$\
\
(9)\
\
with the coefficient\
\
$$\
\\mathcal{D} _{\\ell_{1}\\ell\_{2}\\ell\_{3}}^{\\mathbf{P}}=\\sqrt{(2\\ell\_{1}+\ 1)(2\\ell\_{2}+\ 1)(2\\ell\_{3}+\ 1)}\
$$\
\
- 1)(10)\
\
5\
which depends on the product of the _primary_ (hence the superscript “P”) angular momenta. The matrix in curly brackets\
ℓiLiℓ′i ′i\
in Eq. (10) is a Wigner 9- _j_ symbol. The factor _C₀₀₀_ (defined in Eq.3preceding it guarantees that _ℓi,ℓ_, and _Li_ can be\
′i\
combined to make a zero total angular momentum state. It also requires that _ℓi_ \+ _ℓ_ \+ _Li_ is even.\
\
$$\
“ \\mathrm {P} ”)\
$$\
\
$$\
^{9-j}\
$$\
\
$$\
\\mathcal{C} _{000}^{\\ell_{i}L\_{i}\\ell\_{i}^{\\prime}}\
$$\
\
$$\
\\ell\_{i},\\ell\_{i}^{\\prime}\
$$\
\
$$\
L\_{i}\
$$\
\
$$\
\\ell\_{i}+\\ell\_{i}^{\\prime}+L\_{i}\
$$\
\
Regarding the edge correction, we note that formally M is infinite, but we have found in practice truncating it at one angular\
momentum beyond that used for the physical analysis is suitable (Slepian & Eisenstein2015b,Philcox et al.2021a). In this\
6\
work we use _ℓ_ max = 4 for our analysis but work to _ℓ_ = 5 on all _ℓi_ for the edge correction. Further details regarding the\
suitability of, when performing the edge correction, truncating at an _ℓ_ one above that used for the analysis, are inSlepian\
& Eisenstein(2015b). Ultimately this suitability stems from the rough tri-diagonality of the edge-correction matrix (see their\
§4.2. and our Fig.28).\
\
$$\
\\ell\_{\\operatorname\*{m a x}}=4\
$$\
\
$$\
\\ell\_{i}\
$$\
\
$$\
\\ell,=,5\
$$\
\
5Were one to measure an NPCF for _N ≥_ 5, one would require isotropic basis functions of four arguments or more, and these basis\
functions require specification of intermediate angular momenta fixing how the primary momenta are coupled (further detailed inCahn &\
Slepian2020). The distinction between primary and intermediate angular momenta is not needed in the present work, but for consistency,\
we retain the superscript “P.”\
\
$$\
N,5,\
$$\
\
$$\
“P.”\
$$\
\
6This truncation does not induce spurious parity-odd modes; if it did, we would see them when we edge-correct our mock catalogs.\
\
* * *\
\
5\
\
## 2.1 Illustration With Toy Tetrahedra\
\
−1\
To understand the parity-odd measurement more intuitively, we study cubic boxes of side length _L_ box= 1000 _h_ Mpc with\
tetrahedra tuned to produce particular parity signals. To fill the boxes as fully as possible, yet at the same time have tetrahedra\
−1\
with a minimum side length of order 10 _h_ Mpc, which is similar to the situation in our BOSS dataset, we choose the three\
−1 −1 −1\
sides extending from the primary to be roughly _r₁ ∼_ 10 _h_ Mpc, \*r₂ ∼\*20 _h_ Mpc, and \*r₃ ∼ _30 h Mpc. We require that the_\
_−1_\
_minimum separation between primaries be twice the longest side of the tetrahedron (i.e. 60 h Mpc) in order to minimize any_\
_overlap between tetrahedra. Finally, we have Ntets ∼ 1_,\*500 tetrahedra within each cubic box. Fig.2shows an example box and\
also an example tetrahedron and its partner under parity transformation.\
\
$$\
L\_{\\mathrm{b o x}}=1000;h^{-1}\\mathrm{M p c}\
$$\
\
$$\
h^{-1}\\mathrm{M p c}\
$$\
\
$$\
r\_{1}!\\sim!10;h^{-1}\\mathrm{M p c},,r\_{2}!\\sim!20;h^{-1}\\mathrm{M p c}\
$$\
\
$$\
r\_{3}!\\sim!30~h^{-1}\\mathrm{M p c}\
$$\
\
$$\
h^{-1}\\mathrm{M p c})\
$$\
\
$$\
N\_{\\mathrm{t e t s}}\\sim1\
$$\
\
In 3D, parity transformation is equivalent to a mirror reflection across a 2D plane (which flips the sign of the coordinate\
◦\
axis perpendicular to that plane) plus a 180 rotation around this latter axis. For simplicity, in Fig.2we depict the parity\
transformation simply as a mirror reflection, since our basis, being isotropic, always averages over 3D rotations and is thus\
◦ ◦\
insensitive to a 180 rotation. Put another way, only the mirroring fundamentally alters the shape of a tetrahedron; the 180\
7\
rotation only changes its orientation in absolute space. In particular, one can imagine the mirroring as taking one side and\
“pulling it through” the tetrahedron from being on one side of the plane formed by the other two sides, to being on the other\
side of this plane.\
\
$$\
180^{\\circ}\
$$\
\
$$\
180^{\\circ}\
$$\
\
$$\
180^{\\circ}\
$$\
\
In practice, we must allow all four vertices of each tetrahedron a chance to be the primary (Philcox et al.2021a). However,\
−1 −1\
for this toy tetrahedron illustration we restricted to bins in side length (radial bins) such that 9 h Mpc < ri < 30 h Mpc for\
all _ri_ so that nearly always only one of the four vertices will satisfy the radial bins required for each tetrahedron. This means\
that the contribution to the signal will stem only from the isotropic function evaluated on unit vectors extending from a _single_\
primary; this renders it easier to understand the measured signal in this toy model.\
\
$$\
9,h^{-1}\\mathrm{M p c}<r\_{i}<30,h^{-1}\\mathrm{M p c}\
$$\
\
$$\
r\_{i}\
$$\
\
We set ˆr₁ to be along xˆ, ˆr₂ to be along yˆ, and ˆr₃ to be along zˆ. The tetrahedron is therefore clockwise at the only primary\
allowed in this toy model; our convention is presented in Fig.1. A parity transformation simply means that we interchange\
the sides, so that ˆr₂ aligns with the _x_-axis and ˆr₁ aligns with the _y_-axis, while ˆr₃ is unchanged. Again, characterization as\
“clockwise” or “counterclockwise” depends on at which vertex one sits, as discussed in Fig.1, but here is unambiguous. By\
restricting the radial bins we use, we force only one galaxy to be the primary; the other choices of primary will not lead to\
sides extending from them that fall within our chosen bins. Thus, we can ensure that the tetrahedra for this test are perfectly\
counterclockwise as viewed from the single primary allowed.\
\
$$\
\\hat{\\bf{x}},\
$$\
\
$$\
\\hat{\\mathbf{y}},\
$$\
\
$$\
\\hat{\\mathbf{r}}\_{1}\
$$\
\
$$\
\\hat{\\mathbf{r}}\_{3}\
$$\
\
$$\
\\hat{\\mathbf{r}}\_{2}\
$$\
\
$$\
\\hat{\\bf{r}}\_{1}\
$$\
\
$$\
\\hat{\\mathbf{r}}\_{3}\
$$\
\
We produce toy boxes in three configurations. The first is filled with only counterclockwise tetrahedra (enforced by the radial\
bin restriction); the second has only clockwise tetrahedra, and the third has an equal mix. To render each toy box somewhat\
◦ ◦\
more realistic, we randomly rotate each vertex by an angle _θ ∈_ \[\*− _180_, _180\] around each of the three Cartesian coordinates._\
_−1_\
_We also add random numbers ∆r₁ ∈ \[0_, _1\], ∆r₂ ∈ \[_ − _2_, _2\], and ∆r₃ ∈ \[_ − _1_,\*0\] (in _h_ Mpc) to, respectively, _r₁_, _r₂_, and _r₃_. We\
choose these ranges such that we always have r₁ < r₂ < r₃. Hence the parity of a given tetrahedron will not be flipped by\
these additions.\
\
$$\
\\theta\\in\[-180^{\\circ},180^{\\circ}\]\
$$\
\
$$\
\\Delta r\_{1}\\in\[0,1\],,\\Delta r\_{2}\\in\[-2,2\]\
$$\
\
$$\
\\Delta r\_{3}\\in\[-1,0\]\
$$\
\
$$\
r\_{1},r\_{2},\
$$\
\
$$\
h^{-1}\\mathrm{M p c})\
$$\
\
$$\
r\_{3}\
$$\
\
Fig.3shows the 4PCF of these illustrative boxes. We may approximate each tetrahedron as a sphere about the primary\
−1\
of radius roughly 20 _h_ Mpc, with volume _V_ tet, to estimate the expected 4PCF amplitude. We define _n_ as the local number\
density due to a given tetrahedron, _n_ = 1\*/V\*tet, and _n_ ¯ as the average number density in the box, _n_ ¯ = _N_ tets/L³box. We find\
_√_\
4 5 3/2\
_δ⁴_ = \[ _n/n_ ¯ _−_ 1\] _≈_ 2 _×_ 10\. The lowest-lying parity-odd isotropic basis function is _P₁₁₁_ = _−3i/_\[ 2(4π)\] ˆr₁ _·_ (ˆr₂ _×_ ˆr₃)\
(Cahn & Slepian2020). As expected, the counterclockwise-only box has a positive projection onto this function, while the\
clockwise-only box has a negative projection. The mixed box is consistent with zero projection onto _P₁₁₁_ on average. We can\
analytically predict the ratios among the 4PCF coefficients for different channels _ℓ₁,ℓ₂,ℓ₃_. We compare the mean ratios of the\
8\
measured 4PCF coefficients for several combinations to these predictions and find good agreement. This also serves as an\
additional test of our code (the code is further discussed in §4.1).\
\
$$\
20h^{-1}\\mathrm{M p c}.\
$$\
\
$$\
V\_{\\mathbf{t e t}}.\
$$\
\
$$\
\\bar{n}=N\_{\\mathrm{t e t s}}/L\_{\\mathrm{b o x}}^{3}\
$$\
\
$$\
n,=,1/V\_{\\mathrm{t e t}}\
$$\
\
$$\
\\left\\langle\\delta^{4}\\right\\rangle=\\left\[n\\big/\\bar{n}-1\\right\]^{4}\\approx2\\times10^{5}\
$$\
\
$$\
\\ell\_{1},\\ell\_{2},\\ell\_{3}\
$$\
\
$$\
\\mathcal{P}\_{111}\
$$\
\
## 2.2 Internal Cancellation\
\
For a given tetrahedron, in practice (but not in our illustrative boxes above), each of the four vertices gets a chance to serve\
as the primary about which the isotropic basis function expansion is computed. Some of these vertices will be “clockwise”,\
and some “counterclockwise”. Hence if co-added into the same channel and triple-bin there will be “internal cancellation” and\
consequent reduction of any parity-odd signal. However, if the radial bins are made fine enough then each vertex, in virtue of\
9\
the presumably unique lengths of the sides extending from it, will be accumulated to a different triple-bin. Thus finer binning\
can reduce the internal cancellation and increase the signal. This is much the same as in a configuration-space BAO search,\
\
7In general parity transformation and mirror reflection are distinct operations.\
\
8As an example, the analytically predicted ratio for angular momenta _{1,1,1}_ and _{1,3,3}_ is _ζ /ζ_ = \*− _1_.\*07, and we measure from\
111 133\
the data _ζ_ ¯ _/ζ_ ¯ = \*− _1_.\*07, with _ζ_ ¯ denoting the bin-averaging.\
111 133\
\
$$\
\\zeta\_{111}/\\zeta\_{133}=-1.07\
$$\
\
$$\
\\bar{\\zeta} _{111}/\\bar{\\zeta}_{133}=-1.07.\
$$\
\
9Save for isosceles or equilateral tetrahedra, which we exclude from our analysis in any case.\
\
* * *\
\
6\
\
Figure 2. _Left:_ A box with side length _L_ = 1000 _h_ −1Mpc filled with tetrahedra (upper left, small panel). Each of them has a _unique_\
box\
primary (black) from which the three sides with respective lengths _r ∼_ 10 _h_ −1Mpc (red), _r ∼_ 20 _h_ −1Mpc (yellow), and _r ∼_ 30 _h_ −1Mpc\
1 2 3\
(blue) extend. The larger panel on the left is a zoom-in on the full box to display the tetrahedra more clearly. _Right:_ A sketch of a “clockwise”\
tetrahedron and its “counterclockwise” mirror image. The primary is in red. Our convention on clockwise and counterclockwise is detailed\
in Fig.1. On the left, the red point is closer to us than all the others. Thus the tetrahedron on the left is clockwise, as looking down\
from the primary, we go clockwise as we move from the smallest side to the largest. On the right, the primary (in red) is behind the other\
galaxies, so looking down from it towards them will reverse the handedness. Thus the rightmost tetrahedron is counterclockwise as viewed\
from the primary.\
))\
3\
\
$$\
L\_{\\mathrm{b o x}}=1000h^{-1}\\mathrm{M p c}\
$$\
\
$$\
r\_{1}\\sim10h^{-1}\\mathrm{M p c}\
$$\
\
$$\
r\_{2}\\sim20h^{-1}\\mathrm{M p c}\
$$\
\
$$\
r\_{3}{\\sim}30h^{-1}\\mathrm{M p}\
$$\
\
Figure 3. Here we display 4PCF measurements from the illustrative toy boxes. The left and right panels each show a different channel,\
as indicated in their titles. In both panels, the “clockwise-only” box results are in blue, the “counterclockwise-only” box results are\
in brown, and the “mixed” box results are in grey. _Left_: Projection onto _P_ 111. As discussed in the main text, we expect a negative\
projection for the clockwise box and a positive projection for the counterclockwise box. The mixed will have on average zero projection.\
These expectations are borne out and indeed analytic calculation yields agreement with the measured signals. _Right_: Projection onto\
_P_ 122(ˆr1 _,_ ˆr2 _,_ ˆr3) _∝ i_ ˆr1 _·_ (ˆr2 _×_ ˆr3)(ˆr2 _·_ ˆr3). By construction the scalar triple product ˆr1 _·_ (ˆr2 _×_ ˆr3) is unity for all three of our illustrative\
boxes. The amplitudes on the righthand side are not strictly zero because there are still a small number of tetrahedra formed by connecting\
secondaries around one primary with secondaries around another. Additionally, the amplitude fluctuations divide into two envelopes at\
bin index 36. This bin index corresponds to raising the index for _r_ 1(the smallest side and the slowest-varying one).\
\
$$\
\\mathcal{P}\_{111}\
$$\
\
$$\
\\mathcal{P} _{122}(\\hat{\\mathtt{r}}_{1},\\hat{\\mathtt{r}} _{2},\\hat{\\mathtt{r}}_{3})\\propto i\\hat{\\mathtt{r}} _{1}\\cdot(\\hat{\\mathtt{r}}_{2}\\times\\hat{\\mathtt{r}} _{3})(\\hat{\\mathtt{r}}_{2}\\cdot\\hat{\\mathtt{r}}\_{3})\
$$\
\
$$\
\\hat{\\mathbf{r}} _{1}\\cdot(\\hat{\\mathbf{r}}_{2}\\times\\hat{\\mathbf{r}}\_{3})\
$$\
\
$$\
r\_{1}\
$$\
\
where fine enough bins must be chosen that the BAO feature in the 2PCF is not averaged out by all being added into a single\
bin.\
\
## 3 GUIDING PRINCIPLES FOR THE ANALYSIS\
\
(This section used to be directly after the introduction; now it has been moved here.)\
\
To isolate the potentially parity-violating component of the 4PCF, we expand the correlation function in two distinct sets\
of isotropic basis functions, one that is parity-even and one that is parity-odd. These are constructed from products of three\
\
* * *\
\
7\
\
spherical harmonics with angular-momentum indices _ℓ₁,ℓ₂,ℓ₃_. Isotropy requires that the _ℓi_ satisfy the triangular inequality. If\
the sum of the _ℓi_ is even, the product is parity-even and if the sum is odd, the product is parity-odd. In this analysis, only the\
parity-odd elements are used. Each basis element is a function of three radial distances, the length of the sides from a chosen\
vertex among the four defining a tetrahedron. In practice, the radial distances are binned.\
\
$$\
\\ell\_{1},\\ell\_{2},\\ell\_{3}\
$$\
\
$$\
\\ell\_{i}\
$$\
\
$$\
\\ell\_{i}\
$$\
\
Ideally, one would like to capture as much information as possible, using many narrow radial bins, and working to some\
high value of the _ℓi_. This would increase the difficulty of evaluating all the independent amplitudes, but in fact, the technique\
ofSlepian & Eisenstein(2015b);Philcox et al.(2021a) makes this manageable, as we discuss in §2. The real challenge is in\
determining the covariance matrix. This is especially critical when looking for parity violation, where establishing a statistically\
significant non-zero signal is the crux and hence understanding the inevitable statistical fluctuations is essential.\
\
$$\
\\ell\_{i}.\
$$\
\
A fairly modest choice of separating the radial variable into ten bins and including _ℓi_ only up to _ℓ_ max = 4 results in\
23 _×_ 120 = 2\*, _760 independent amplitudes; we also consider eighteen radial bins, which produces 816 × 120 = 18_,\*768 4PCF\
amplitudes. Determining the covariance matrix is thus a formidable challenge. In order to invert a sampling covariance matrix,\
as required for calculating _χ²_, we need at least many mocks as the dimensionality of the data vector, which is in excess of the\
2,000 available to us for BOSS.\
\
$$\
\\ell\_{i}\
$$\
\
$$\
23\\times120=2,760\
$$\
\
$$\
\\ell\_{\\mathrm{m a x}};=;4\
$$\
\
$$\
816\\times120=18,768~4\\mathrm{P C F}\
$$\
\
$$\
\\chi^{2},\
$$\
\
We have chosen three ways to obtain the covariance matrix. First, the NPCF covariance matrix can be calculated analytically\
under the assumption of a Gaussian Random Field (GRF) as shown inHou et al.(2021a). The GRF does not on average have\
any parity-violation at the _signal_ level, but it can still have non-zero fluctuations in parity-odd modes. Therefore the GRF is\
still the leading-order contribution to the _covariance_ of the parity-odd modes. This is simply the statement that a signal may\
be zero but its root-mean-square may not. We fit the analytic template covariance matrix by varying the number density and\
volume with respect to the covariance matrix derived from the mocks.\
\
With this analytic template in hand, we may (i) directly compute the _χ²_ of the data using the adjusted analytic covariance\
matrix. An alternative (ii) is to compress the data vector to reduce its dimensionality. The eigenvectors of the analytical\
covariance matrix with the smallest eigenvalues represent the linear combinations of basis functions that have the smallest\
statistical uncertainties. We then expand the measured 4PCF using just the _N_ eig best expansion functions. We may also\
determine the _N_ eig _× N_ eig covariance matrix directly from the mocks. Since _N_ eig is much less than the number of mocks this\
covariance matrix is invertible. Finally, we may (iii) use the empirical covariance matrix from the mocks directly, with no\
involvement of the analytic template at all, by considering many fewer channels than in (i) and (ii) (we lower _ℓ_ max to be\
_ℓ_ max = 2). A substantial reduction of the number of channels is required to enable inverting the empirical covariance matrix\
employed in this approach, and so we lose statistical power. We thus treat (iii) as a test rather than as giving us the main\
result of our analysis. The reliability of all three approaches above can be assessed using the mocks themselves by verifying\
that their _χ²_ (or _T²_) values match the expected distribution.\
\
$$\
\\chi^{2}\
$$\
\
$$\
N\_{\\mathrm{e i g}}\
$$\
\
$$\
N\_{\\operatorname{e i g}}\\times N\_{\\operatorname{e i g}}\
$$\
\
$$\
N\_{\\mathrm{e i g}}\
$$\
\
$$\
\\ell\_{\\mathrm{m a x}}\
$$\
\
$$\
\\ell\_{\\mathrm{m a x}}=2,\
$$\
\
$$\
\\chi^{2}\ {(\\mathrm{o r}\ T^{2})}\
$$\
\
## 4 DATASET AND COVARIANCE\
\
We use the final galaxy catalog of the Baryon Oscillation Spectroscopic Survey (BOSS), from the twelfth data release (DR12)\
of the Sloan Digital Sky Survey-III (SDSS-III). The catalog is split into the North Galactic Cap (NGC) and the South Galactic\
Cap (SGC). The catalog contains two samples, CMASS and LOWZ, which were selected via the SDSS multicolor photometry\
and cover a redshift range of 0.15 < z < 0.7. CMASS and LOWZ use similar target selection algorithms (Eisenstein et al.2001;\
Cannon et al.2006). The target selection algorithm provides samples that are mainly composed of Luminous Red Galaxies\
(LRGs). For CMASS the selection algorithm is further tuned to select massive objects uniformly in redshift (Reid et al.2016),\
11.3 −1\
which results in an approximately mass-limited sample down to a stellar mass _M ∼_ 10 _h_ M\*⊙\* (Maraston et al.2013;\
Leauthaud et al.2016;Saito et al.2016;Bundy et al.2017). The majority of CMASS is LRGs ( _∼74 percent), while the rest is_\
_late-type spirals (Masters et al.2011). LOWZ consists primarily of LRGs (Parejko et al.2013). Despite the difference in target_\
_selection, the LRGs in the two samples have similar stellar mass distribution (Maraston et al.2013). We apply a redshift cut of_\
_0.43 < z < 0.7 to CMASS, which results in a redshift tail from LOWZ at redshift 0.43 < z < 0.5. This tail (∼15% of the entire_\
_“CMASS” sample) slightly raises the purity of the CMASS sample by adding more LRGs. To ensure that the LOWZ sample_\
_as used here is independent of the CMASS one, we apply a redshift cut of 0.2 < z < 0.4 to the former. This cut produces_\
_−1_\
_a separation of about 70h_ Mpc between the lower edge of CMASS and the upper edge of LOWZ. Fig.4shows the number\
density for each sample as a function of redshift. Finally, we note that the early LOWZ target selection was not uniform due\
to the use of different iterations of the galaxy-star separation algorithm (Reid et al.2016). Therefore we do not include those\
early chunks in this analysis.\
\
$$\
0.15<z<0.7\
$$\
\
$$\
M\\sim10^{11.3},h^{-1}\\mathrm{M}\_{\\odot}\
$$\
\
$$\
0.43<z<0.7\
$$\
\
$$\
" C M A S S"\
$$\
\
$$\
0.43<z<0.5\
$$\
\
$$\
70h^{-1}\\mathrm{M p c}\
$$\
\
$$\
0.2<z<0.4\
$$\
\
## 4.1 4PCF from Data and Mocks\
\
−1\
For our main analyses, we considered tetrahedra with side lengths _r₁, r₂_ and _r₃_ from the primary ranging from 20 _h_ Mpc to\
−1 −1 −1\
160 _h_ Mpc inclusive, split into ten linearly-spaced bins, and also from 20 _h_ Mpc to 164 _h_ Mpc inclusive, split into eighteen\
\
$$\
r\_{1},\ r\_{2}\
$$\
\
$$\
r\_{3}\
$$\
\
$$\
20,h^{-1}\
$$\
\
$$\
h^{-1}\
$$\
\
$$\
20,h^{-1}\\mathrm{M p c}\
$$\
\
$$\
h^{-1}\\mathrm{M p c}\
$$\
\
* * *\
\
8\
\
Figure 4. The number density n as a function of redshift z for the two BOSS samples used in this work. The LOWZ (0.2 < z < 0.4) North\
Galactic Cap (NGC) is brown and South Galactic Cap (SGC) is orange. For CMASS (0.43 < z < 0.7), the NGC is in purple and the SGC\
is in lavender. We intentionally do not allow redshift overlap between the two samples, and the redshift gap ∆ _z_ = 0\*. _03 corresponds to a_\
_comoving radial separation of 73_ h\*−1Mpc. This separation means that the samples are fairly independent; the 2PCF _ξ_ between a point in\
LOWZ and CMASS would be of order 1% at this scale. The covariance between two “worst-case” tetrahedra, one in each sample (where\
each is very close to the respective edge), is of order _ξ_ 4. Few tetrahedra are near enough on either edge to be significantly correlated\
with those in the other slice. The plot shows that LOWZ has both a more uniform selection function and a somewhat higher average\
number density than CMASS. It also lacks the strongly decaying tail with an increasing redshift that CMASS displays. These points are\
important when assessing the possible impact of systematics on each sample and when addressing any differences between the detection\
significances in the two samples.\
\
$$\
0.2<z<0.4)\
$$\
\
$$\
(0.43<z<0.7)\
$$\
\
$$\
\\Delta z=0.03\
$$\
\
$$\
73,h^{-1}\\mathrm{M p c}\
$$\
\
$$\
\\xi^{4}\
$$\
\
linearly-spaced bins. We also explored a coarser binning (six bins), presented as a test in AppendixE. As a result, the sides of\
−1\
the tetrahedron that do not include the primary can range from zero to 320 _h_ Mpc. We expand the parity-odd 4PCF in the\
23 angular channels with _ℓi ≤_ 4 given in Cartesian form in AppendixA. For the edge corrections, we include all functions with\
_ℓi ≤_ 5, as further discussed in §2. We also compute the even-parity modes (for which we do not reproduce the basis functions\
here), as they are needed within the edge-correction, despite that our actual analysis focuses solely on the parity-odd ones.\
\
$$\
320,h^{-1}\\mathrm{M p c}\
$$\
\
$$\
\\ell\_{i}\\leq4\
$$\
\
$$\
\\ell\_{i}\\leq5\
$$\
\
$$\
\\S2\
$$\
\
To each galaxy, we apply a total weight _w_ given by\
\
$$\
\ =w\_{\\mathrm{f l k p}}w\_{\\mathrm{s y s}}\\big(w\_{\\mathrm{n o z}}+w\_{\\mathrm{c p}}-1\\big),\
$$\
\
(11)\
\
with the systematic weight _w_ sys (a combined weight for stellar density and seeing), the redshift failure weight _w_ noz, and the\
−1\
fiber collision weight _w_ cp (subscript “cp” for “close pairs”). The FKP weight (Feldman et al.1994) is _w_ fkp= \[1 + _n_( _z_) _P₀_\],\
4 −1 3\
with _P₀_ = 10 \[ _h_ Mpc\]; _n_( _z_) is the weighted number density at the given redshift. We use the public random catalog provided\

[... middle omitted — see footer ...]

panel shows just the diagonal of our test matrix; the residual is likely due to the slightly different number densities.\
\
Figure D1. Redshift-distribution dependence on imaging depth for CMASS NGC. _Left_: Normalized galaxy number counts as a function\
of redshift for _i_-band. We have split the sample into three bins in imaging depth. _Right_: Same as the left but for _r_-band. We see that the\
three bins in _i_\- and _r_-band depths have very similar _n_( _z_), implying that the imaging depth is unlikely to impact our analysis.\
\
## APPENDIX F: MAXIMUM SCALE CUT AND MINIMUM BIN SEPARATION\
\
To explore whether the use of small scales makes a difference in our analysis (as these are the scales on which the mocks may\
be most likely to imperfectly mirror the data, due to approximate treatment of non-linear structure formation), we test the\
detection significances by applying further restrictions to the radial bins. First, we force the minimum radial bin separation\
−1\
to be ∆ _r ≥_ 15 _h_ Mpc such that the results are less sensitive to small scales. Second, we vary the maximum radial bin\
−1 −1\
_r_ max = 90 _h_ Mpc and _r_ max = 130 _h_ Mpc such that we are less affected by any mismatch between mocks and data around\
the BAO position and towards larger scales (as was seen in some of the 2PCF measurements).\
\
$$\
\\Delta r,\\geq,15,,h^{-1}\
$$\
\
$$\
r\_{\\mathrm{m a x}}=90;h^{-1}\\mathrm{M{}o}\
$$\
\
$$\
r\_{\\mathrm{m a x}}=130;h^{-1}\\mathrm{M p c}\
$$\
\
The results are shown in Figs.F1andF2. In all these cases the detection significance reduces compared to the fiducial case\
(without minimum bin separation or maximum radial bin) given that the number of degrees of freedom is reduced. However, we\
still observe non-negligible detection significances for all cases. It is worth pointing out that there are in total only 35\*×\*23 = 805\
−1\
degrees of freedom when using _r_ max = 90 _h_ Mpc, which allows us to use the mock covariance directly. Despite the mismatch\
\
$$\
r\_{\\mathrm{m a x}}=90:h^{-1}\\mathrm{M p c}\
$$\
\
* * *\
\
# Hou, Slepian & Cahn\
\
CMASS SGC CMASS SGC 8 8\
\
21.44 < i-band < 21.97 21.93 < r-band < 22.46\
7 21.97 < i-band < 22.51 7 22.46 < r-band < 22.99\
\
22.51 < i-band < 23.04 22.99 < r-band < 23.52\
6 6\
\
5 5\
\
4 4\
\
3 3\
\
2 2\
\
Normalized Number of Galaxies 1 Normalized Number of Galaxies 1\
\
0 0\
\
0.45 0.50 0.55 0.60 0.65 0.70 0.45 0.50 0.55 0.60 0.65 0.70\
Redshift Redshift\
\
Figure D2. Same as Fig.D1but for CMASS SGC. Again, the _i_\- and _r_-bands have very similar _n_( _z_) for the three bins in imaging depth, implying that imaging depth does not strongly impact our analysis for SGC.\
\
C M A S S, 6 b i n s,m a x= 4 _N_ e i g = 5 0 _N_ e i g = 1 0 0\
\
0.0150\
_N_ e i g = 2 0 0 _T_ 2: s i n g l e\
\
0.025\
_T_ 2: s i n g l e _T_ 2: s i n g l e\
\
0.04 _T_ 2: j o i n t _T_ 2: j o i n t 0.0125 _T_ 2: j o i n t\
Gaussian fit\
\
0.020\
Gaussian fit Gaussian fit\
\
0.03 NS ::\
_TT_ 2 2 == 0 0. 3. 3 N S :: _TT_ 2 2 == 0 0. 3. 30.0100 N S :: _TT_ 2 2 == 10 ..37 PDF 0.02 N+S:T2PDF 0.010\
\
0.015 N+S:\
T 2PDF\
\
0.0075 N+S:\
T 2 _G_ == 00..11 _G_ == 00..10 0.0050 _G_ == 11..24\
\
0.01 0.005 0.0025\
0.00 50 100 150 200 250\
0.000 100 200 300 400 500\
0.0000 200 400 600 800 1000 1200\
_T_ 2 _T_ 2 _T_ 2 _N_ e i g = 4 0 0 Mock covariance Analytic covariance _T_ 2:: s 0.0052:: s2:: s\
\
0.006 _T_ 2j oi ni ng tl e2j oi ni ng tl e 0.0122j oi ni ng tl e\
0.005 Gaussian fit\
N : 2 = 0. 10.004 Gaussian fit N : = 0. 5 0.010 Gaussian fit N : = 0. 7\
\
0.004 S : _TT_ 2 = 0. 8 0.003 S : _GG_ = 0\. 8 0.008 S : _GG_ = 1\. 2 PDF 0.003 N+S:T2PDF 0.002 N + S : _G_ = 0PDF 0.006. 2 N + S : _G_ = 0\. 4\
_G_ == 00..45\
\
0.002 0.004\
0.001 0.001 0.002\
0.000 500 1000 1500 2000 2500 3000 3500\
0.000 1000 2000 3000 4000\
0.000 400 600 800 1000 1200 1400 1600\
_T_ 2 _T_ 2 2\
\
Figure E1. Here we show a compressed analysis (§5.1.2), and direct approaches with both the mock covariance (lower middle panel) and the analytic covariance (lower right panel) for a 4PCF with just six radial bins. This substantially reduces the number of degrees of freedom, permitting the use of the mock covariance. However, the detection significance is also degraded; we attribute this to much larger “internal cancellation” (§2.2) than in our ten- and eighteen-bin analyses.\
\
between the analytic covariance matrix and the expected _χ²_ distribution, there is no substantial difference in the detection significances.\
\
## APPENDIX G: ALL ANGULAR CHANNELS\
\
MNRAS 000, 000–000 (0000)\
\
$$\
n(z)\
$$\
\
$$\
\\chi^{2}\
$$\
\
* * *\
\
41\
\
C M A S S, 1 8 b i n s, ( _r_ mi n, _r_ max) =\
2 0 0 Mock covariance\
\
$$\
(\\Delta r\_{\\min},r\_{\\max})=(15,90)\[h^{-1}\
$$\
\
$$\
\\ell\_{amathsf m a times=4}\
$$\
\
L O W Z, 1 8 b i n s, ( _r_ mi n, _r_ max) = ( 1\
0 0 Mock covariance\
\
$$\
(\\Delta r\_{\\sf m i n},\ r\_{\\sf m a x})=(15,90),\[h^{-1};{sf M p c}\],;\\ell\_{\\sf m a x}=4\
$$\
\
## Analytic covariance e i g\
\
Figure F1. _Upper_: CMASS sample with minimum radial bin separation ∆ _r_ = 15 _h_ −1Mpc and maximum radial bin _r_ = 90 _h_ −1Mpc.\
max\
The leftmost column uses the data compression method with _N_ eig= 200\. The middle column directly uses the mock covariance. The\
rightmost column uses the analytic covariance. _Lower_: Same as the upper row but for LOWZ. In all these cases the detection significance\
is reduced relative to that in our fiducial analysis due to having fewer degrees of freedom.\
\
$$\
\\Delta r=15:h^{-1}\\mathrm{M p c}\
$$\
\
$$\
r\_{\\mathrm{m a x}}=90:h^{-1}\\mathrm{M p c}.\
$$\
\
$$\
N\_{\\mathrm{e i g}},=,200\
$$\
\
* * *\
\
42\
\
L O W Z, 1 8 b i n s, ( _r_ mi n, _r_ max) = ( 1\
_N_ = 8 0 0 Analytic covariance\
\
$$\
\[h^{-1}\
$$\
\
$$\
\\ell\_{a x}=4\
$$\
\
Figure F2. _Upper_: CMASS sample with minimum radial bin separation ∆ _r_ = 15 _h_ −1Mpc and maximum radial bin _r_ = 130 _h_ −1Mpc.\
max\
The left column uses the data compression method with _N_ eig= 200\. The right column uses the analytic covariance. _Lower_: Same as the\
upper row but for LOWZ. As in Fig.F1the detection significance is reduced compared to that in our fiducial analysis.\
\
$$\
\\Delta r=15:h^{-1}\\mathrm{M p c}\
$$\
\
$$\
r\_{\\mathrm{m a x}}=130:h^{-1}\\mathrm{M p c}.\
$$\
\
$$\
N\_{\\mathrm{e i g}}=200\
$$\
\
* * *\
\
))) _Parity-Odd 4PCF Detection_ _r r r_ ,,, _r²_ =, =, = _r²_,=, =, = _r²_,=, =, =, 1 1 1 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
\
)13 CMASS: NGC)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r_ CMASS: SGC _r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 1, 2 = 4, 3 = 4, _r₁_ 15001 = 2, 2 = 1, 3 = 2, _r₁_ 15001 = 2, 2 = 2, 3 = 1, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 2, 2 = 2, 3 = 3, _r₁_ 15001 = 2, 2 = 3, 3 = 2, _r₁_ 15001 = 2, 2 = 3, 3 = 4, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 2, 2 = 4, 3 = 3, _r₁_ 15001 = 3, 2 = 1, 3 = 3, _r₁_ 15001 = 3, 2 = 2, 3 = 2, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 3, 2 = 2, 3 = 4, _r₁_ 15001 = 3, 2 = 3, 3 = 1, _r₁_ 15001 = 3, 2 = 3, 3 = 3, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 3, 2 = 4, 3 = 2, _r₁_ 15001 = 3, 2 = 4, 3 = 4, _r₁_ 15001 = 4, 2 = 1, 3 = 4, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 4, 2 = 2, 3 = 3, _r₁_ 15001 = 4, 2 = 3, 3 = 2, _r₁_ 15001 = 4, 2 = 3, 3 = 4, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 25002500 500 _r r r²_\
)13)13 1 _r_ 1000 _r_ 1000 _r_ 1000 _r r_, 1500, 1500 1500 2 2 _r₁_ = 4, 2 = 4, 3 = 1, _r₁_ 15001 = 4, 2 = 4, 3 = 3, 15001 _r r_ ( 1000 ( 1000 3 3 1250012500 0 0 _r³ r³_ _r²_ 500 _r²_ 500 1 1 _r_ 1000 _r_ 1000 1500 1500 0 20 40 60 80 100 120 0 20 40 60 80 100 120\
Radial Bin Index Radial Bin Index\
\
Figure G1. The parity-odd 4PCF for the BOSS CMASS data, with NGC in red and SGC in blue. The plot includes all the angular channels for ten radial bins. The error bars are the rms of the Patchy mocks.\
\
MNRAS 000, 000–000 (0000)\
\
* * *\
\
# Hou, Slepian & Cahn)))\
\
_r₂ r₂ r₂_ ,,, _r_ =, = _r_,=, =, = _r_,=, =, = ,=, _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ) LOWZ: NGC)) _r¹_ 3LOWZ: SGC _r¹r_ 3 _r¹_ 3 _r r_, 4000, 4000, 4000 2 2 2 _r_ 2 = 4, 3 = 4 _r_,1 = 2, 2 = 1, 3 = 2 _r_,1 = 2, 2 = 2, 3 = 1, 40001 = 1,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 2, 3 = 3 _r_,1 = 2, 2 = 3, 3 = 2 _r_,1 = 2, 2 = 3, 3 = 4, 40001 = 2,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 4, 3 = 3 _r_,1 = 3, 2 = 1, 3 = 3 _r_,1 = 3, 2 = 2, 3 = 2, 40001 = 2,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 2, 3 = 4 _r_,1 = 3, 2 = 3, 3 = 1 _r_,1 = 3, 2 = 3, 3 = 3, 40001 = 3,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 4, 3 = 2 _r_,1 = 3, 2 = 4, 3 = 4 _r_,1 = 4, 2 = 1, 3 = 4, 40001 = 3,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 2, 3 = 3 _r_,1 = 4, 2 = 3, 3 = 2 _r_,1 = 4, 2 = 3, 3 = 4, 40001 = 4,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 )) _r¹_ 3 _r¹_ 3 _r¹_ _r₂ r₂_, 4000, 4000 4000 _r_ 2 = 4, 3 = 1 _r_,1 = 4, 2 = 4, 3 = 3, 40001 = 4,4000 _r¹ r¹_ ( ( 232000232000 1 1 0 0 _r³ r³_ _r²_ 2000 _r²_ 2000 _r¹ r¹_ 4000 4000 0 20 40 60 80 100 120 0 20 40 60 80 100 120 Radial Bin Index Radial Bin Index\
\
Figure G2. The parity-odd 4PCF for the BOSS LOWZ data including all the angular channels for ten radial bins. NGC is in brown and SGC in blue; the error bars are the rms of the Patchy mocks.\
\
MNRAS 000, 000–000 (0000)\
\
* * *\
\
))) _Parity-Odd 4PCF Detection_ _r r r_ ,,, _r²_ =, =, = 1 , _r²_ =, =, = 2 , _r²_ =, =, =, 1 1 1 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
\
)13 CMASS: NGC)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r_ CMASS: SGC _r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 1, 2 = 4, 3 = 4 , _r₁_ 15001 = 2, 2 = 1, 3 = 2 , _r₁_ 15001 = 2, 2 = 2, 3 = 1, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 2, 2 = 2, 3 = 3 , _r₁_ 15001 = 2, 2 = 3, 3 = 2 , _r₁_ 15001 = 2, 2 = 3, 3 = 4, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 2, 2 = 4, 3 = 3 , _r₁_ 15001 = 3, 2 = 1, 3 = 3 , _r₁_ 15001 = 3, 2 = 2, 3 = 2, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 3, 2 = 2, 3 = 4 , _r₁_ 15001 = 3, 2 = 3, 3 = 1 , _r₁_ 15001 = 3, 2 = 3, 3 = 3, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 3, 2 = 4, 3 = 2 , _r₁_ 15001 = 3, 2 = 4, 3 = 4 , _r₁_ 15001 = 4, 2 = 1, 3 = 4, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 250025002500 _r r r_\
)13)13)13 _r_ 1000 _r_ 1000 _r_ 1000 _r r r_, 1500, 1500, 1500 2 2 2 _r₁_ = 4, 2 = 2, 3 = 3 , _r₁_ 15001 = 4, 2 = 3, 3 = 2 , _r₁_ 15001 = 4, 2 = 3, 3 = 4, 15001 _r r r_ ( 1000 ( 1000 ( 1000 3 3 3 125001250012500 0 0 0 _r³ r³ r³_ 25002500 500 _r r r²_\
)13)13 1 _r_ 1000 _r_ 1000 _r_ 1000 _r r_, 1500, 1500 1500 2 2 _r₁_ = 4, 2 = 4, 3 = 1 , _r₁_ 15001 = 4, 2 = 4, 3 = 3, 15001 _r r_ ( 1000 ( 1000 3 3 1250012500 0 0 _r³ r³_ _r²_ 500 _r²_ 500 1 1 _r_ 1000 _r_ 1000 1500 1500 0 200 400 600 800 0 200 400 600 800\
Radial Bin Index Radial Bin Index\
\
Figure G3. The parity-odd 4PCF for the BOSS CMASS data including all the angular channels for eighteen radial bins. NGC is in red and SGC is in blue; the error bars are the rms of the Patchy mocks.\
\
MNRAS 000, 000–000 (0000)\
\
* * *\
\
# Hou, Slepian & Cahn)))\
\
_r₂ r₂ r₂_ ,,, _r_ =, = 1 , _r_ =, =, = 2 , _r_ =, =, = ,=, _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ) LOWZ: NGC)) _r¹_ 3LOWZ: SGC _r¹r_ 3 _r¹_ 3 _r r_, 4000, 4000, 4000 2 2 2 _r_ 2 = 4, 3 = 4 , _r_ 1 = 2, 2 = 1, 3 = 2 , _r_ 1 = 2, 2 = 2, 3 = 1, 40001 = 1,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 2, 3 = 3 , _r_ 1 = 2, 2 = 3, 3 = 2 , _r_ 1 = 2, 2 = 3, 3 = 4, 40001 = 2,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 4, 3 = 3 , _r_ 1 = 3, 2 = 1, 3 = 3 , _r_ 1 = 3, 2 = 2, 3 = 2, 40001 = 2,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 2, 3 = 4 , _r_ 1 = 3, 2 = 3, 3 = 1 , _r_ 1 = 3, 2 = 3, 3 = 3, 40001 = 3,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 4, 3 = 2 , _r_ 1 = 3, 2 = 4, 3 = 4 , _r_ 1 = 4, 2 = 1, 3 = 4, 40001 = 3,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 ))) _r¹_ 3 _r¹_ 3 _r¹_ 3 _r₂ r₂ r₂_, 4000, 4000, 4000 _r_ 2 = 2, 3 = 3 , _r_ 1 = 4, 2 = 3, 3 = 2 , _r_ 1 = 4, 2 = 3, 3 = 4, 40001 = 4,4000 4000 _r¹ r¹ r¹_ ( ( ( 232000232000232000 1 1 1 0 0 0 _r³ r³ r³_ _r²_ 2000 _r²_ 2000 _r²_ 2000 )) _r¹_ 3 _r¹_ 3 _r¹_ _r₂ r₂_, 4000, 4000 4000 _r_ 2 = 4, 3 = 1 , _r_ 1 = 4, 2 = 4, 3 = 3, 40001 = 4,4000 _r¹ r¹_ ( ( 232000232000 1 1 0 0 _r³ r³_ _r²_ 2000 _r²_ 2000 _r¹ r¹_ 4000 4000 0 200 400 600 800 0 200 400 600 800 Radial Bin Index Radial Bin Index\
\
Figure G4. The parity-odd 4PCF for the BOSS LOWZ data including all the angular channels for eighteen radial bins. NGC is in brown and SGC in blue; the error bars are the rms of the Patchy mocks.\
\
MNRAS 000, 000–000 (0000)

──────── [TRUNCATED] ────────
Showing 44,893 chars (head) + 14,973 chars (tail) of 207,857 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-9bb6421788.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-9bb6421788.md" offset=1097 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
