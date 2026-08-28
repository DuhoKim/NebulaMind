URL: https://arxiv.org/pdf/2206.04227

# Probing Parity-Violation with the Four-Point Correlation Function of BOSS Galaxies

1, 2,
Oliver H. E. Philcox

<sup>1</sup>
*Department of Astrophysical Sciences, Princeton University,*

*Princeton, NJ 08540, USA*

<sup>2</sup>
*School of Natural Sciences, Institute for Advanced Study, 1 Einstein Drive,*
*Princeton, NJ 08540, USA*

Parity-violating physics in the early Universe can leave detectable traces in late-time observables.
Whilst vector- and tensor-type parity-violation can be observed in the *B*-modes of the cosmic microwave background, scalar-type signatures are visible only in the four-point correlation function
(4PCF) and beyond. This work presents a blind test for parity-violation in the 4PCF of the BOSS
1
CMASS sample, considering galaxy separations in the range [20*;*<sup>1</sup>60]*h* Mpc. The parity-odd 4PCF
contains no contributions from standard CDM physics and can be eciently measured using recently developed estimators. Data are analyzed using both a non-parametric rank test (comparing
2
the BOSS 4PCFs to those of realistic simulations) and a compressed analysis, with the former
avoiding the assumption of a Gaussian likelihood. These nd similar results, with the rank test giving a detection probability of 99*:* 6% (2*:* 9). This provides signicant evidence for parity-violation,
either from cosmological sources or systematics. We perform a number of systematic tests: although
these do not reveal any observational artefacts, we cannot exclude the possibility that our detection
is caused by the simulations not faithfully representing the statistical properties of the BOSS data.
Our measurements can be used to constrain physical models of parity-violation. As an example, we
consider a coupling between the inaton and a *U*(1) gauge eld and place bounds on the latter’s
energy density, which are several orders of magnitude stronger than those previously reported. Upcoming probes such as DESI and Euclid will reveal whether our detection of parity-violation is due
to new physics, and strengthen the bounds on a variety of models.

$$
\chi^{2}
$$

## I. INTRODUCTION

A detection of parity-violation in cosmological observables would be a smoking gun for physics beyond the standard
model, and could provide crucial insights into the nature of dark matter, dark energy, and ination. In the conventional
paradigm, all cosmological correlators are symmetric under the parity operator P, since gravity (along with all other
standard model interactions except the weak force [1]), is P-invariant. Despite this, a number of theoretical arguments
suggest that parity-violating interactions *should* occur in the early Universe, most notably to source baryogenesis.
Creation of the current baryon asymmetry requires a process which violates charge and parity conservation [2,3]; a
possible route is via leptogenesis, which, if sourced by gravity, must be parity-violating [e.g.,4{8].

Additional sources of parity-violation include inationary interactions between multiple elds, such as via the
Chern-Simons term [e.g.,9{14], generation of primordial magnetic elds [e.g.,15{17], vector perturbations generated
by cosmic strings or defects [e.g.,18{20], reheating [e.g.,21,22], Chern-Simons modied general relativity [11], and
inationary particle exchange [23,24], all of which leave distinctive imprints on late-time observables [e.g.,9]. Potential
evidence for such models was recently provided by [25], which found a 2*:* 4 hint (updated to 3*:* 6 in [26]) of parityviolation in the cosmic microwave background (hereafter CMB). Whilst some argue that this eect may be caused
by interstellar dust emission [27] (though see [28,29]), it has nevertheless provided a resurgence of interest in these
theories.

To constrain such phenomena, we require observables that are parity-sensitive. Common choices are vector and
tensor quantities, such as *B* modes of the CMB [e.g.,30], or those of galaxy ellipticities [e.g.,31]. These satisfy
arXiv:2206.04227v3  [astro-ph.CO]  15 Mar 2023
P[*B*] = *B*, and can be combined in two-point correlators (e.g., *TB* and *EB* for the CMB, or *EB* for weak lensing).
Barring contamination by systematics, the observables should have no contribution from standard CDM physics, but
can be sourced by eects such as birefringence (whereupon the plane of the photon polarization is coherently rotated
between the surface of last scattering and the observer, as in [25]), gravitational wave chirality [e.g.,9,32{35], and
multi-eld ination [7,23,36]. Information is not limited to the two-point function however; higher-order correlators
such as *TTB* can give additional constraining power on eects such as birefringence [37].

When constructing observables from scalar elds (such as the galaxy density or CMB temperature), obtaining a
parity-sensitive quantity is more dicult. As an example, the isotropic galaxy two-point correlation function (hereafter

ohep2@cantab.ac.uk

---

2

FIG. 1. Cartoon of the galaxy four-point correlation functions (4PCFs) considered in this work. In the left panel, we show the
4PCF, (*r₁; r₂; r₃*), which depends on the separation vectors of three secondary galaxies from a given primary. The right panel
shows the parity-inverted 4PCF, P [ (*r₁; r₂; r₃*)], which corresponds to replacing *ri* with *ri*. Unlike for the 2PCF and 3PCF,
the two congurations cannot be related by a rotation. The parity-even 4PCF is a sum of the two geometries (which have the
same side-lengths and relative angles), whilst the parity-odd 4PCF is a dierence. In this work, the 4PCF is given as a function
of three lengths (*r₁*, *r₂*, and *r₃*) and three internal angles (xing the angle of the *ri* vectors with the respect to the primary
galaxy). The latter are represented by their harmonic-space momenta, *‘*1, *‘*2 and *‘*3, with odd-parity 4PCFs corresponding to
odd *‘*1 + *‘*2 + *‘*3. Assuming standard CDM physics, the two correlators shown in the gure should be equivalent, thus the
expectation value of the parity-odd 4PCF is zero.

$$
\zeta(r_{1},r_{2},r_{3})
$$

$$
\mathbb{P}[\zeta({r}_{1},{r}_{2},{r}_{3})right\dot{}_{.}
$$

$$
r_{i}
$$

$$
(r_{1},\,r_{2},
$$

$$
r_{3})
$$

$$
r_{i}
$$

$$
\ell_{1},\:\ell_{2}
$$

$$
\ell_{3}.
$$

$$
\ell_{1}+\ell_{2}+\ell_{3}
$$

2PCF) is insensitive to parity, since the action of P is equivalent to a rotation, under which the statistic is invariant. In
three-dimensions, the isotropic *N*-point correlation functions (NPCFs) are parity-sensitive only if *N >* 3; this applies
also to the CMB, since the intrinsic uctuations are the projection of a three-dimensional quantity. The simplest
statistic with which to probe scalar parity-violation is thus the 4PCF, as pointed out in [23,38,39]. A cartoon of this
1
is shown in Fig.1.

$$
\mathbb{P}
$$

Whilst a number of works have considered the 4PCF of the CMB [e.g.,44,45] including its parity-odd contributions
[38,46] (though only theoretically), the large scale structure (LSS) equivalent has been rarely explored. Given the
inux of spectroscopic data expected in the next decade from DESI [47], Euclid [48], and Rubin [49], galaxy surveys
seem to be a natural arena in which to hunt for parity-violating interactions, allowing constraints to exceed the CMB
cosmic variance limit. Historically, use of the higher-point galaxy correlation functions has been hampered by the
computational resources required for their estimation; navely, the 4PCF requires *O*(*N*<sup>g4</sup>) operations to compute from
*N*<sub>g</sub>galaxies. Recent works have signicantly improved upon this [50,51], with the algorithm of [51] requiring only
*O*(*N*<sup>g2</sup>) operations. This allows the 4PCF of current galaxy surveys to be computed in 30 CPU-hours. The approach
proceeds by rst projecting the correlation function into a suitable angular basis [52]; thence, the integrals decouple
and the 4PCF may be computed by summing over pairs of galaxies. This naturally generalizes to higher-dimensions,
as well as to anisotropic correlators [53]. As rst pointed out in [52] there is a natural separation of the parity-even
and parity-odd isotropic basis functions. The even-parity component can be used to place constraints on gravitational
non-Gaussianity from a hitherto unexplored statistic [54]. The use of the parity-odd basis to measure parity violation
in the galaxy four-point correlation was rst proposed in [39] and is carried out in this work (see also [23]).

$$
\mathcal{O}(N_{\mathrm{g}}^{4})
$$

$$
N_{\mathrm{g}}
$$

$$
\mathcal{O}(N_{\mathrm{g}}^{2})
$$

There are two main ways in which parity-violation can be probed using the galaxy 4PCF. Firstly, one may place
constraints on the amplitudes of specic physical models given their associated theoretical predictions. This is an
approach oft-used in the analysis of CMB 3- and 4-point functions, for example in non-Gaussianity studies, which
typically exploit separability of the underlying theoretical templates for signicant computational gain [e.g.,55]. This
approach was also suggested in [23,46,56], and allows for targeted constraints on specic models of early-Universe
particle exchange, via a search for their specic isotropy-violating signatures. An alternative method would be to rst
measure the *full* galaxy 4PCF in some set of bins, then perform a blind test, looking for the signatures of *any* physical
model (and systematic eects). This approach is possible since the parity-odd 4PCF receives no contribution in CDM,
including from general relativistic and baryonic eects. Given the multitude of possible models for parity-violation,
we will principally adopt the second strategy in this work, though we demonstrate also the rst, by placing constraints
on a specic model involving Chern-Simons terms in the inationary Lagrangian. Analysis using the galaxy 4PCF
comes with its complexities, however. In particular, the high-dimensionality of the statistic prohibits conventional

$$
f u l l
$$

<sup>1</sup>Large scale structure correlators are sensitive also to redshift-space distortions [40,41], giving dependence of the statistic on line-of-sight
velocities [42]. This enables vector-type parity-violation to be probed in the 3PCF [43], though it requires careful modelling of galaxy
velocities.

---

3

2
mock-based-analyses. To alleviate this, we include a data-compression step, facilitated using a theoretical model
of the 4PCF covariance [57], which dramatically reduces the number of bins without introducing bias. It is not
guaranteed that the 4PCF likelihood be Gaussian however (see AppendixAand [58,59]); to provide a fully robust,
yet conservative, test for parity-violation, we make use of a likelihood-free inference technique, involving a suite of
realistic simulations. We caution that such blind tests are naturally subject to systematic uncertainties, some of which
will be explored in this work. The results below represent the rst constraints on scalar parity-violation from LSS
data.

$$
\chi^{2}.
$$

The remainder of this work is structured as follows. In §II, we present the parity-odd 4PCF estimator, including the
corrections necessary to account for non-uniform survey geometry, before we discuss the data and covariance matrices
in §III. Analysis methods are considered in §IV, with the corresponding constraints on parity-violation presented in
§V. In §VI, we include a number of systematic checks and a brief discussion of potential biases in the approach. §VII
discusses parity-breaking phenomena including the presentation of an inationary model for the parity-odd 4PCF,
based on a Chern-Simons coupling, whose amplitude is then bounded using the BOSS data. We conclude in §VIII,
with AppendicesAandBdiscussing the impacts of likelihood non-Gaussianity and sketching the derivation of the
2
Chern-Simons 4PCF template. Jupyter notebooks containing our analysis pipeline can be found on GitHub.

*Note on Blinding*: To limit conrmation bias, the BOSS data were sent to an external collaborator (M. Konig)
after computation, and not revealed until the analysis pipeline was constructed and tested. The initial draft of the
paper was also written before unblinding (encompassing all sections except §VIand AppendixA), with the BOSS
data replaced by that from a single mock dataset.

## II. MEASURING THE PARITY-ODD 4PCF

3
We begin by outlining our estimator for the parity-odd 4PCF, which is implemented in the public encore code.
Further details of the formalism can be found in [51] (for the general NPCF estimator and encore), [52] (for the basis
functions), [54] (for the parity-even 4PCF), [39] (for an overview of the parity-odd 4PCF) and [53] (for extensions
beyond at 3D space).

## A. Isotropic Basis Functions

Given a (scalar) density eld (*r*), the 4PCF is dened as

$$
\delta(r)
$$

$$
\boxed{\zeta(\boldsymbol{r}_{1},\boldsymbol{r}_{2},\boldsymbol{r}_{3})\equiv\left<\delta(\boldsymbol{s})\delta(\boldsymbol{s}+\boldsymbol{r}_{1})\delta(\boldsymbol{s}+\boldsymbol{r}_{2})\delta(\boldsymbol{s}+\boldsymbol{r}_{3})\right>,}
$$

(1)

where *hi* represents a statistical average over realizations of. A cartoon of this parametrization is shown in Fig.1.
By statistical homogeneity, the 4PCF is independent of the absolute coordinate *s*.

$$
\langle\cdots\rangle
$$

As demonstrated in [51,53], a complete angular basis for the isotropic *N*-point correlation functions is given by the
4
isotropic basis functions of (*N* 1) coordinates dened in [52] (see also the TriPoSH formalism; [60]). For *N* = 4,
the basis functions are
X

$$
(N-1)
$$

$$
N=4.
$$

$$
\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}(\hat{{r}}_{1},\hat{{r}}_{2},\hat{{r}}_{3})\equiv(-1)^{\ell_{1}+\ell_{2}+\ell_{3}}\sum_{m_{1}m_{2}m_{3}}\left(\begin{matrix}{\ell_{1}}&{\ell_{2}}&{\ell_{3}}\\ {m_{1}}&{m_{2}}&{m_{3}}\\ \end{matrix}\right)Y_{\ell_{1}m_{1}}(\hat{{r}}_{1})Y_{\ell_{2}m_{2}}(\hat{{r}}_{2})Y_{\ell_{3}m_{3}}(\hat{{r}}_{3}),
$$

(2)

where *Y*<sub>‘m</sub>(*r*^) is a spherical harmonic, the 3 2 matrix is a Wigner 3-*j* symbol, and the *m*<sub>i</sub>summations run over
integer *m*<sub>i</sub>*2* [ *‘*<sub>i</sub>*;‘*<sub>i</sub>]. Such functions arise from the theory of angular momentum addition, and are specied by
three non-negative integers *f‘*<sub>1</sub>*;‘*<sub>2</sub>*;‘*<sub>3</sub>*g*, encoding the relative orientation of *r*^<sub>1</sub>*; r*^<sub>2</sub>, and *r*^<sub>3</sub>. Due to the 3-*j* symbol, the
integers must obey the triangle condition *j‘*<sub>1</sub>*‘*<sub>2</sub>*j ‘*<sub>3</sub>*‘*<sub>1</sub>+ *‘*<sub>2</sub>, and we additionally enforce *‘*<sub>i</sub>*‘*<sub>max</sub>. In practice,
we restrict to relatively low *‘*<sub>max</sub>, which gives an angular resolution of<sub>min</sub>2*=‘*<sub>max</sub>for the internal angles of the
4PCF tetrahedron. The basis functions have the following properties under parity and conjugation transformations
(for parity operator P):

$$
Y_{\ell m}(\hat{r})
$$

$$
3\times2
$$

$$
3-j
$$

$$
m_{i}
$$

$$
m_{i}\,\in\,[-\ell_{i},\ell_{i}]
$$

$$
\{\ell_{1},\ell_{2},\ell_{3}\}
$$

$$
\hat{r}_{1},\hat{r}_{2}
$$

$$
\hat{r}_{3}
$$

$$
|\ell_{1}-\ell_{2}|\leq\ell_{3}\leq\ell_{1}+\ell_{2}
$$

$$
3-j
$$

$$
\ell_{\mathrm{m a x}}
$$

$$
\ell_{i}\leq\ell_{\operatorname*{m a x}}
$$

$$
\theta_{\mathrm{m i n}}\approx2\pi/\ell_{\mathrm{m a x}}
$$

$$
\mathbb{P}\left[\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}(\hat{\mathbf{r}}_{1},\hat{\mathbf{r}}_{2},\hat{\mathbf{r}}_{3})\right]=(-1)^{\ell_{1}+\ell_{2}+\ell_{3}}\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}(\hat{\mathbf{r}}_{1},\hat{\mathbf{r}}_{2},\hat{\mathbf{r}}_{3}),\qquad\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}^{*}(\hat{\mathbf{r}}_{1},\hat{\mathbf{r}}_{2},\hat{\mathbf{r}}_{3})=(-1)^{\ell_{1}+\ell_{2}+\ell_{3}}\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}(\hat{\mathbf{r}}_{1},\hat{\mathbf{r}}_{2},\hat{\mathbf{r}}_{3}),
$$

(3)

<sup>2</sup>Available atgithub.com/oliverphilcox/Parity-Odd-4PCF.

<sup>3</sup>Available atgithub.com/oliverphilcox/encore.

<sup>4</sup>The approach naturally extends to *anisotropic* correlators [53], though we do not consider them in this work.

---

4

implying that the basis is parity-odd and pure imaginary if *‘*<sub>1</sub>+ *‘*<sub>2</sub>+ *‘*<sub>3</sub>is odd, and parity-even and real else.
Furthermore, (2) is invariant under joint rotations of all three separation vectors, *i.e. fr₁; r₂; r₃g!fRr₁;Rr₂;Rr₃g*,
for arbitrary rotation matrix *R*.

$$
\ell_{1}+\ell_{2}+\ell_{3}
$$

$$
\left\{r_{1},r_{2},r_{3}\right\}\rightarrow\left\{R r_{1},R r_{2},R r_{3}\right\}
$$

The isotropic part of the galaxy 4PCF can be decomposed into the basis of (2):
X

$$
\zeta_{\operatorname{i s o}}({r r}_{1},{r}_{2},{r}_{3})=\sum_{\ell_{1}\ell_{2}\ell_{3}}\zeta_{\ell_{1}\ell_{2}\ell_{3}}({r}_{1},{r}_{2},_{{3}})\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}(\hat{{r}}_{1},\hat{{r}}_{2},\hat{{r}}_{3}),
$$

(4)

5
where the coecients<sup>‘</sup><sup>1</sup> <sup>‘</sup><sup>2</sup> <sup>‘</sup><sup>3</sup>(hereafter denoted ‘multiplets’) can be obtained via the orthonormality of *P*<sup>‘</sup><sup>1</sup> <sup>‘</sup><sup>2</sup> <sub>‘</sub><sub>3</sub>. Given
the transformation properties of (3), we nd a natural split of<sub>iso</sub>into parity-even and parity-odd parts:
X

$$
\zeta_{\ell_{1}\ell_{2}\ell_{3}}
$$

$$
\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}\cdot^{5}
$$

$$
\zeta_{\mathrm{i s o}}
$$

$$
\begin{aligned}{\zeta_{+}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})}&{{}=\sum_{\ell_{1}+\ell_{2}+\ell_{3}=\operatorname{e v e n}}\zeta_{\ell_{1}\ell_{2}\ell_{3}}(_{{1}},{r{}}_{2},{_{3}})\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}(\hat{r}_{1},\hat{r}_{2},\hat{r}_{3}),}\\ {\zeta_{-}(\mathbf{r}_{1},\mathbf{r}_{2},\mathbf{r}_{3})}&{{}=\sum_{\ell_{1}+\ell_{2}+\ell_{3}=\operatorname{o d d}}\zeta_{\ell_{1}\ell_{2}\ell_{3}}({r}_{1},{r}_{2},{r}_{3})\mathcal{P}_{\ell_{1}\ell_{2}\ell_{3}}(\hat{r}_{1},\hat{r}_{2},\hat{r}_{3}).}\\ \end{aligned}
$$

(5)

These satisfy P [ (*r₁; r₂; r₃*)] = (*r₁; r₂; r₃*), and may be related to the sum and dierence of the two panels in
Fig.1. In this work, we restrict to odd *‘*<sub>1</sub>+ *‘*<sub>2</sub>+ *‘*<sub>3</sub>, and thus consider the (purely imaginary) parity-odd 4PCF.

$$
\mathbb{P}\big[\zeta_{\pm}(r_{1},r_{2},r_{3})\big]=\pm\big(\zeta_{\pm}(r_{1},r_{2},r_{3})
$$

$$
\ell_{1}+\ell_{2}+\ell_{3}
$$

## B. 4PCF Estimator

Invoking the ergodic principle, we may estimate the full 4PCF as an integral over four density elds,
Z

$$
\hat {\zeta} \left(\boldsymbol {r} _ {1}, \boldsymbol {r} _ {2}, \boldsymbol {r} _ {3}\right) \equiv \frac {1}{V} \int d \boldsymbol {s} \delta (\boldsymbol {s}) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {1}\right) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {2}\right) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {3}\right),
$$

(6)

where *V* is the integration volume. This is unbiased, *i.e.* it has expectation E[ ^] =. Since the basis functions of (2)
are orthonormal [52], (6) can be used to construct an estimator for the 4PCF basis coecients:
Z

$$
i.e.
$$

$$
\mathbb{E}[\hat{\zeta}]=\zeta.
$$

$$
\begin{array}{l} \hat {\zeta} _ {\ell_ {1} \ell_ {2} \ell_ {3}} \left(r _ {1}, r _ {2}, r _ {3}\right) = \int d \hat {\boldsymbol {r}} _ {1} d \hat {\boldsymbol {r}} _ {2} d \hat {\boldsymbol {r}} _ {3} \mathcal {P} _ {\ell_ {1} \ell_ {2} \ell_ {3}} ^ {*} \left(\hat {\boldsymbol {r}} _ {1}, \hat {\boldsymbol {r}} _ {2}, \hat {\boldsymbol {r}} _ {3}\right) \hat {\zeta} \left(\boldsymbol {r} _ {1}, \boldsymbol {r} _ {2}, \boldsymbol {r} _ {3}\right) \\ = \frac {1}{V} \sum_ {m _ {1} m _ {2} m _ {3}} \left( \begin{array}{c c c} \ell_ {1} & \ell_ {2} & \ell_ {3} \\ m _ {1} & m _ {2} & m _ {3} \end{array} \right) \\ \times \int d \boldsymbol {s} d \hat {\boldsymbol {r}} _ {1} d \hat {\boldsymbol {r}} _ {2} d \hat {\boldsymbol {r}} _ {3} \delta (\boldsymbol {s}) \delta (\boldsymbol {s} + \boldsymbol {r} _ {1}) \delta (\boldsymbol {s} + \boldsymbol {r} _ {2}) \delta (\boldsymbol {s} + \boldsymbol {r} _ {3}) Y _ {\ell_ {1} m _ {1}} \left(\hat {\boldsymbol {r}} _ {1}\right) Y _ {\ell_ {2} m _ {2}} \left(\hat {\boldsymbol {r}} _ {2}\right) Y _ {\ell_ {3} m _ {3}} \left(\hat {\boldsymbol {r}} _ {3}\right), \\ \end{array}
$$

)(7)

using the conjugate properties of (3). Dening the harmonic coecients
~~Z~~

$$
\boxed{a_{\ell m}(s;r)\equiv\int d\hat{r}\:\delta(s+r)Y_{\ell m}(\hat{r}),}
$$

(8)

this is separable in *r*^<sub>i</sub>:

$$
\hat{r}_{i}
$$

$$
\boxed{\dot{\zeta}_{\ell_{1}\ell_{2}\ell_{3}}(r_{1},r_{2},r_{3})=\sum_{m_{1}m_{2}m_{3}}\left(\begin{matrix}{\ell_{1}}&{\ell_{2}}&{\ell_{3}}\\ {m_{1}}&{m_{2}}&{m_{3}}\\ \end{matrix}\right)\int\frac{d s}{V}\delta(\mathfrak{s})a_{\ell_{1}m_{1}}(\mathfrak{s};r_{1})a_{\ell_{2}m_{2}}(\mathfrak{s};r_{2})a_{\ell_{3}m_{3}}(\mathfrak{s};r_{3}).}
$$

(9)

For a discrete density eld dened by *N*<sub>g</sub>particles at positions *fx*<sub>i</sub>*g* with weights *w*<sub>i</sub>, the estimator can be written as
a sum:

$$
N_{\mathrm{g}}
$$

$$
\left\{x_{i}\right\}
$$

$$
w_{i}.
$$

(10)

$$
\begin{aligned}{a_{\ell m}(\mathbf{x}_{i};r)}&{{}\equiv\sum_{j=1}^{N_{\theta}}w_{j}Y\_{\ell m}(\widehat{\mathbf{x}_{j}-\mathbf{x}_{i}})\delta_{\operatorname{D}}(r-|\mathbf{x}_{j}-\mathbf{x}_{i}|),}\\ {\hat{\zeta}_{\ell_{1}\ell_{2}\ell_{3}}(r_{1},r_{2},r_{3})}&{{}=\sum_{i=1}^{N_{\theta}}\sum_{m_{1}m_{2}m_{3}}\left(\begin{matrix}{\ell_{1}}&{\ell_{2}}&{\ell_{3}}\\ {m_{1}}&{m_{2}}&\ m{matrix_{{3}}}\\ \end{matrix}\right)w_{i}\:a_{\ell_{1}m_{1}}(\mathbf{x}_{i};r_{1})a_{\ell_{2}m_{2}}(\mathbf{x}_{i};r_{2})a_{\ell_{3}m_{3}}(\mathbf{x}_{i};r_{3}),}\\ \end{aligned}
$$

<sup>5</sup>Since the anisotropic basis functions are orthogonal to those of (2), the decomposition in (4) holds regardless of whether the full statistic
is isotropic.

---

5

where the Dirac delta,<sub>D</sub>, ensures that we count only secondary particles, *j*, separated from the primary, *i*, by a
distance *r*. Since we must compute *a*<sub>‘m</sub>at the location of each primary particle, the estimator requires a sum over
pairs of particles, and thus has complexity *O*(*N*<sup>g2</sup>); in practice, the scaling is closer to linear, as the *m*<sub>i</sub>summation
is rate limiting for large *‘*<sub>max</sub>[51]. By replacing the Dirac function in (10) by a binning function of nite width, the
estimator extends to bin-averaged 4PCF estimates; we refer the reader to [51,54] for details. We further note that
the 4PCF contains also a ‘disconnected’ piece sourced by two copies of the 2PCF. Whilst this can be subtracted at
the estimator level directly [54], it does not contribute to parity-odd multiplets, and will thus be ignored henceforth.

$$
\delta_{\mathrm{D}}
$$

$$
a_{\ell m}
$$

$$
j,
$$

$$
r\,
$$

$$
\mathcal{O}(N_{\mathrm{g}}^{2})
$$

$$
m_{i}
$$

$$
\ell_{\mathrm{m a x}}
$$

## C. Edge-Correction

Finally, estimator (9) must be modied to account for the non-uniform survey geometry. For this purpose, we rst
dene the 4PCF using the generalized Landy-Szalay form [51,61,62]

$$
\hat{\zeta}(r_{1},r_{2},r_{3})\equiv\frac{\mathcal{N}(r_{1},r_{2},r_{3})}{\mathcal{R}(r_{1},r_{2},r_{3})},
$$

(11)

where *N* and *R* are the 4PCF estimates obtained from ‘data-minus-random’ and random catalogs respectively, both
of which are modulated by the survey window function. Following some algebra, the *edge-corrected* 4PCF multiplets
are given by
X

$$
\mathcal{R}
$$

(12)

$$
\zeta_{\ell_{1}\ell_{2}\ell_{3}}(r_{1},r_{2},r_{3})=\sum_{\ell_{1}^{\prime}\ell_{2}^{\prime}\ell_{3}^{\prime}}\left[M^{-1}\right]_{\ell_{1}\ell_{2}\ell_{3}}^{\ell_{1}^{\prime}\ell_{2}^{\prime}\ell_{3}^{\prime}}\left(r_{1},r_{2},r_{3}\right)\frac{\mathcal{N}_{\ell_{1}^{\prime}\ell_{2}^{\prime}\ell_{3}^{\prime}}(r_{1},r_{2},r_{3})}{\mathcal{R}_{000}(r_{1},r_{2},r_{3})},
$$

dening the coupling matrix

$$
\begin{array}{l} M _ {\ell_ {1} \ell_ {2} \ell_ {3}} ^ {\ell_ {1} ^ {\prime} \ell_ {2} ^ {\prime} \ell_ {3} ^ {\prime}} \left(r _ {1}, r _ {2}, r _ {3}\right) = \frac {(- 1) ^ {\ell_ {1} ^ {\prime} + \ell_ {2} ^ {\prime} + \ell_ {3} ^ {\prime}}}{(4 \pi) ^ {3 / 2}} \sum_ {L _ {1} L _ {2} L _ {3}} \frac {\mathcal {R} _ {L _ {1} L _ {2} L _ {3}} \left(r _ {1}, r _ {2}, r _ {3}\right)}{\mathcal {R} _ {0 0 0} \left(r _ {1}, r _ {2}, r _ {3}\right)} \left[ \prod_ {i = 1} ^ {3} \sqrt {(2 \ell_ {i} + 1) (2 L _ {i} + 1) \left(2 \ell_ {i} ^ {\prime} + 1\right)} \right] \left\{ \begin{array}{l l l} \ell_ {1} & L _ {1} & \ell_ {1} ^ {\prime} \\ \ell_ {2} & L _ {2} & \ell_ {2} ^ {\prime} \\ \ell_ {3} & L _ {3} & \ell_ {3} ^ {\prime} \end{array} \right\} \\ \times \left( \begin{array}{c c c} \ell_ {1} & L _ {1} & \ell_ {1} ^ {\prime} \\ 0 & 0 & 0 \end{array} \right) \left( \begin{array}{c c c} \ell_ {2} & L _ {2} & \ell_ {2} ^ {\prime} \\ 0 & 0 & 0 \end{array} \right) \left( \begin{array}{c c c} \ell_ {3} & L _ {3} & \ell_ {3} ^ {\prime} \\ 0 & 0 & 0 \end{array} \right), \\ \end{array}
$$

(13)
;

with the curly brackets indicating a Wigner 9-*j* symbol. This allows us to ‘undo’ the eects of non-uniform survey
6
geometry by measuring the 4PCF multiplets of the random eld *R*. Note that there are two manners in which an
7
parity-odd can be sourced: parity-odd *N* and parity-even *R*, or parity-odd *R* and parity-even *N*. For this reason,
it is imperative to restrict to parity-odd multipets only *after* performing edge-correction.

$$
9-j
$$

$$
\ {\mathcal R}^{6}
$$

$$
\mathcal{N}
$$

$$
{\mathfrak R},
$$

$$
{\mathcal{N}}.{}^{7}
$$

$$
\mathcal{R}
$$

## III. DATA

## A. Data and Simulations

Our dataset comprises galaxies from the twelfth data-release (DR12) [64] of the Baryon Oscillation Spectroscopic
Survey (BOSS), part of SDSS-III [65,66]. The survey contains two samples, CMASS and LOWZ, of which we use
the former. This contains 587 071 (216 041) galaxies in the Northern (Southern) galactic cap (hereafter denoted NGC
8
and SGC), across a redshift range *z 2* [0*:* 43*;* 0*:* 7] and an eective redshift of ze= 0: 57. We use a ducial cosmology
P
*f*<sub>m</sub>= 0*:* 31*;*<sub>b</sub>*h²* = 0*:* 022*;h* = 0*:* 676*;*<sub>8</sub>= 0*:* 8*;n*<sub>s</sub>= 0*:* 96*; m* = 0*:* 06 eV*g* to convert angles and redshifts to
Cartesian coordinates [cf.54,67], and assign galaxy weights according to

$$
z\in[0.4{\dot{3}},{\dot{0}}.7]
$$

$$
z_{\mathrm{e f f}}=0.57.^{8}
$$

$$
\{\Omega_{m}\:=\:0.31,\Omega_{b}h^{2}\:=\:0.022,h\:=\:0.676,\sigma_{8}\:=\:0.8,n_{s}\:=\:0.96,\sum_m m_{\nu}\:=\:0.06\operatorname{e V}\}
$$

$$
w_{\mathrm{t o t}}=\big(w_{\mathrm{r f}}+w_{\mathrm{f c}}-1\big)w_{\mathrm{s y s}}w_{\mathrm{f k p}}.
$$

(14)

Here *w*<sub>rf</sub>, *w*<sub>fc</sub>, and *w*<sub>sys</sub>correspond to redshift-failure, ber-collision, and systematic weights respectively, with *w*<sub>fkp</sub>=
1 4 3
[1 + *n*(*z*)*P₀*] being the well-known FKP weight [68] for background number density *n*(*z*) and *P₀* = 10 *h* Mpc³.
To model the survey geometry, we use the BOSS random catalogs, containing 50 more randoms than galaxies.

$$
w_{\mathrm{r f}},\,w_{\mathrm{f c}};
$$

$$
w_{\mathrm{s y s}}
$$

$$
w_{\mathrm{f k p}}=
$$

$$
[1+n(z)P_{0}]^{-1}
$$

$$
P_{0}=10^{4}h^{-3}\mathrm{M{c}}^{3}
$$

$$
n(z)
$$

<sup>6</sup>Note that this does not remove any geometry eects that couple to the *anisotropic* 4PCF, nor those coupling to the 4PCF multiplets
with *‘*<sub>i</sub>*> L*, assuming an initial *‘*<sub>max</sub> of *L*. The former eect is expected to be small (and usually ignored for the 3PCF [e.g.,63]),
and the latter is ameliorated by discarding all multiplets containing *‘*<sub>i</sub>= *L* after edge-correction, justied by noting that the coupling
matrix, *M*, is close to tridiagonal.

$$
\ell_{i}\,>\,L,
$$

$$
L.
$$

$$
\ell_{i}=L
$$

<sup>7</sup>This occurs since the product of 3-*j* symbols in the coupling matrix is zero unless *‘* + *‘* + *‘* + *‘*<sup>0</sup>+ *‘*<sup>0</sup>+ *‘*<sup>0</sup>+ *L* + *L* + *L* is even.
1 2 3 1 2 3 1 2 3
<sup>8</sup>Data are publicly available atdata.sdss.org/sas/dr12/boss/lss/.

$$
\ell_{1}+\ell_{2}+\ell_{3}+\ell_{1}^{\prime}+\ell_{2}^{\prime}+\ell_{3}^{\prime}+L_{1}+L_{2}+L_{3}
$$

---

6

We additionally make use of a suite of *N*<sub>mocks</sub>= 2048 ‘MultiDark-Patchy’ (hereafter Patchy) simulations [69,70].
These are computed using an approximate gravity solver and calibrated to an *N*-body simulation, with halo occupation
parameters adjusted such that the mocks well reproduce the BOSS two- and three-point statistics. These share the
CMASS survey geometry and are assigned weights via

$$
N_{\mathrm{m o c k s}}=2048\ mathrm~~mathrmmathrm{M M l t i D}
$$

$$
w_{\mathrm{t o t}}=w_{\mathrm{v e t0}}w_{\mathrm{f c}}w_{\mathrm{f k p}},
$$

(15)

including the veto weight *w*veto. The mocks are generated with the parameter set *f*m= 0*:* 3071*;*b*h²* = 0*:* 02205*;h* =
P
0*:* 6777*;*<sub>8</sub>= 0*:* 8288*;n*<sub>s</sub>= 0*:* 96*; m* = 0 eV*g* and coordinates are converted using the BOSS ducial cosmology.

$$
w_{\mathrm{v e t o}}
$$

$$
\left\{\Omega_ {m} = 0. 3 0 7 1, \Omega_ {b} h ^ {2} = 0. 0 2 2 0 5, h = \right.
$$

$$
0.6777,\sigma_{8}=0.8288,n_{s}=0.96,\sum m_{\nu}=0\,\mathrm{e V}\}
$$

## B. 4PCF Estimates

One of the main drawbacks with higher-order NPCFs is their dimensionality. To characterize the 4PCF, we must
specify three multiplet indices (*‘*<sub>1</sub>*;‘*<sub>2</sub>*;‘*<sub>3</sub>) and three radial bins (*r₁;r₂;r₃*), which can lead to a statistic with a large
number of (highly correlated) elements [51]. For this reason, we adopt a relatively coarse radial binning scheme using
1 1
*N*<sub>r</sub>= 10 linearly spaced radial bins in [20*;*<sup>1</sup>60]*h* Mpc, giving *r* = <sup>1</sup>4*h* Mpc. Furthermore, we enforce *r₂ > r₁*+*r*
and *r₃ > r₂* + *r*, to ensure that the the separation between any two galaxies in the 4PCF tetrahedron is at least *r*
(cf. Fig.1). This removes modes from the non-linear region; these are dicult to model and can be strongly aected
by baryonic physics. For the angular binning, we x *‘*<sub>max</sub>= 5, leading to a total of 56 radial bins and 111 multiplets
(both parity-odd and parity-even), hence 6 216 elements in the full 4PCF statistic. In the analysis of §IV, we use only
the 23 multiplets with odd *‘*<sub>1</sub>+ *‘*<sub>2</sub>+ *‘*<sub>3</sub>and *‘*<sub>i</sub>4, giving a total of *N* = 1288 elements; the rest are required for
edge-correction (§II C).

$$
(\ell_{1},\ell_{2},\ell_{3})
$$

$$
(r_{1},r_{2},r_{3})
$$

$$
N_{r}=10
$$

$$
\dot{160}|h^{-1}\mathrm{M p c}
$$

$$
r_{2}>r_{1}\!+\!\Delta r
$$

$$
\Delta r=14h^{-1}\mathrm{M p c}
$$

$$
r_{3}>r_{2}+\Delta r.
$$

$$
\Delta r
$$

$$
\ell_{\mathrm{m a x}}=5
$$

$$
\ell_{1}+\ell_{2}+\ell_{3}
$$

$$
\ell_{i}\leq4
$$

$$
N_{\zeta}=1288
$$

Computation of the 4PCF multiplets,<sup>‘</sup><sup>1</sup> <sup>‘</sup><sup>2</sup> <sup>‘</sup><sup>3</sup>(*r₁*;r₂;r₃), is performed using the encore code [51]. We separately
measure the contributions from a random catalog and a set of 32 ‘data-minus-random’ catalogs, each with 1*:* 5 the
galaxy density; the latter are averaged to form the *N* quantities entering the edge-correction equation (11), whilst
9
the former give *R*. Using (12), the quantities are then combined to form the edge-corrected 4PCF multipoles.

$$
\zeta_{\ell_{1}\ell_{2}\ell_{3}}(r_{1},r_{2},r_{3})
$$

$$
\mathcal{R}.^{9}
$$

3 5
For samples with similar number densities to BOSS, the runtime of encore scales as *N*<sup>g</sup>*N*<sup>r</sup>(*‘*<sup>max</sup>+ 1) [<sup>5</sup>1], with
computation dominated by the *m*<sub>i</sub>summations of (10) rather than estimation of the harmonic coecients *a*<sub>‘m</sub>(which
2
scales as *N*<sub>g2</sub>(1+*‘*<sub>max</sub>), albeit with a more modest prefactor). In practice, we parallelize computation using OpenMP,
with each NGC (SGC) each simulation requiring 32 (6) CPU-hours to analyze on a modern 16-core Intel processor,
including edge-correction. In total, analysis of the BOSS data and 2048 Patchy mocks required 80k CPU-hours.
This is comparable to the computational costs of the 2PCF analysis in Ref. [73], and is facilitated by the ecient
nature of the encore algorithm. We display a selection of the measured 4PCF multiplets in Fig.2.

$$
N_{\mathrm{g}}N_{r}^{3}(\ell_{\mathrm{m a x}}+1)^{5}\,[5]
$$

$$
m_{i}
$$

$$
a _ {\ell m}
$$

$$
N_{\mathrm{g}}^{2}(1\!+\!\ell_{\mathrm{m a x}})^{2}
$$

$$
\sim\!32\,(6)
$$

## C. Covariance Matrices

The Patchy mocks described in §III Acan be used to form a sample covariance of the 4PCF statistic in the
standard manner:

$$
\begin{aligned}{\hat{\mathcal{C}}_{\ell_{1}\ell_{2}\ell_{3};\ell_{1}^{\prime}\ell_{2}^{\prime}\ell_{3}^{\prime}}(r_{1},r_{2},r_{3};r_{1}^{\prime},r_{2}^{\prime},r_{3}^{\prime})=\frac{1}{N_{\mathrm{m o c k s}}-1}\sum_{i=1}^{N_{\mathrm{{m o c k s}}}}\Big(\zeta_{\ell_{1}\ell_{2}\ell_{3}}^{(i)}(r_{1},r_{2},r_{3})-\bar{\zeta}_{\ell_{1}\ell_{2}\ell_{3}}^r{_(11}r_{2},r_{3})\Big)}\\ {\times\ (\zeta_{\ell_{1}^ell{prime}ell_{2}^{\prime}}^{(i)}(r_{1}^{\prime},r_{2}^{\prime},r_{3}^{\prime})-\bar{\zeta}_{\ell_{1}\ell_{2}^{\prime}\ell_{3}^{\prime}}(r_{1}^{\prime},r_{2}^{\prime})r_{3}^{\prime})\ ,}\\ \end{aligned}
$$

(16)

(<sup>i</sup><sup>)</sup>
where represents the *i*-th 4PCF estimate (in the NGC or SGC region), and is the average over *N*<sub>mocks</sub>realizations.
Since the number of 4PCF bins exceeds the number of Patchy mocks, this is not invertible, making it dicult to
2
perform traditional-based analyses. For this reason, we supplement the sample covariance with the analytic
covariance described in [57]. Essentially, this computes:
Z

$$
\zeta^{(i)}
$$

$$
\bar{\zeta}
$$

$$
N_{\mathrm{m o c k s}}
$$

$$
\chi^{2}.
$$

$$
\begin{array}{l} \operatorname {C o v} \left(\boldsymbol {r} _ {1}, \boldsymbol {r} _ {2}, \boldsymbol {r} _ {3}; \boldsymbol {r} _ {1} ^ {\prime}, \boldsymbol {r} _ {2} ^ {\prime}, \boldsymbol {r} _ {3} ^ {\prime}\right) = \int \frac {d \boldsymbol {s}}{V} \frac {d \boldsymbol {s} ^ {\prime}}{V} \left\langle \delta (\boldsymbol {s}) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {1}\right) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {2}\right) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {3}\right) \delta \left(\boldsymbol {s} ^ {\prime}\right) \delta \left(\boldsymbol {s} ^ {\prime} + \boldsymbol {r} _ {1} ^ {\prime}\right) \delta \left(\boldsymbol {s} ^ {\prime} + \boldsymbol {r} _ {2} ^ {\prime}\right) \delta \left(\boldsymbol {s} ^ {\prime} + \boldsymbol {r} _ {3} ^ {\prime}\right) \right\rangle \tag {17} \\ - \int \frac {d \boldsymbol {s}}{V} \left\langle \delta (\boldsymbol {s}) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {1}\right) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {2}\right) \delta \left(\boldsymbol {s} + \boldsymbol {r} _ {3}\right) \right\rangle \int \frac {d \boldsymbol {s} ^ {\prime}}{V} \left\langle \delta \left(\boldsymbol {s} ^ {\prime}\right) \delta \left(\boldsymbol {s} ^ {\prime} + \boldsymbol {r} _ {1} ^ {\prime}\right) \delta \left(\boldsymbol {s} ^ {\prime} + \boldsymbol {r} _ {2} ^ {\prime}\right) \delta \left(\boldsymbol {s} ^ {\prime} + \boldsymbol {r} _ {3} ^ {\prime}\right) \right\rangle , \\ \end{array}
$$

(17)

<sup>9</sup>If the algorithm’s runtime scales as *N*, this partitioning minimizes the Poisson error at xed computational cost [71,72]. In our case,
g2
the scaling is closer to linear, thus the total work is roughly independent of the partition size.

$$
N_{\mathrm{g}}^{2}
$$

---

7

( 1, 1

( 1, 2

( 2, 3

( 4, 4

FIG. 2. Measurements of the parity-odd 4PCF from the BOSS CMASS galaxy sample, alongside those from 2048 Patchy
simulations. The NGC (SGC) results are shown in blue (red) bands, with the BOSS data shown as error-bars, using the
Patchy variances. Results are displayed for a selection of *f‘*1*;‘*2*;‘*3*g* multiplets (which specify the internal angles of the galaxy
tetrahedron, as in Fig.1), whose values are indicated by the title of each subgure. In total, 23 parity-odd multiplets are
included in the analysis of §V. The horizontal axis species the radial bin combinations, *fr₁;r₂;r₃g*, with the central values of
*r₁*, *r₂* and *r₃* in each bin shown in the top panel. These correspond to the distances of the secondary, tertiary, and quaternary
galaxies from the primary in Fig.1. For visibility, the 4PCF measurements are rescaled by a factor *ir₁r₂r₃*. As expected, the
Patchy measurements show no signs of parity-violation. Given the high correlation between neighboring bins, it is dicult to
visually assess whether the BOSS dataset contains signatures of parity-violation; this is quantied in Figs.4&5.

$$
\{\ell_{1},\ell_{2},\ell_{3}\}
$$

$$
r_{1}
$$

$$
\{r_{1},r_{2},r_{3}\}
$$

$$
r_{3}
$$

$$
-i\,r_{1}r_{2}r_{3}
$$

---

8

where the statistical expectations can be expanded using Wick’s theorem to yield products of four 2PCFs. The covariance is then projected into the angular basis of §II Aand simplied. The approach makes a number of assumptions:

• Isotropy: The 2PCF (*r*) *h* (*s*) (*s* + *r*)*i* is assumed to be a function only of *jrj*. This neglects redshift-space
distortions, which have a non-trivial impact on the isotropic 4PCF covariance.

$$
\xi(\boldsymbol{r})\equiv\langle\delta(\boldsymbol{s})\delta(\boldsymbol{s}+\boldsymbol{r})\rangle
$$

• Gaussianity: The expectations entering (17) strictly contain additional contributions from higher-order correlators such as the 3PCF.

• Survey Geometry: Whilst the 4PCF is edge-corrected (§II C), the same is not true for the covariance. The
latter inherits non-trivial dependence on the survey geometry [e.g.,74,75], which cannot be simply captured by
modifying the survey volume or shot-noise [57].

For these reasons, we do *not* expect the analytic models of [57] to accurately predict the true covariance of BOSS. It is
a relatively close approximation of matrix structure however, and will thus be used as a proxy covariance to facilitate
the analysis techniques described in §IV. We construct the covariance using the same radial binning parameters as in
§III A, restricting to odd *‘*<sup>1</sup>+ *‘*<sup>2</sup>+ *‘*<sup>3</sup>. Following the prescription of [74] (but generalized to higher dimensions), we
3 3 3 3
use an eective volume of 1*:* 90*h* Gpc³ (0*:* 77*h* Gpc³) and shot-noise *P*<sub>shot</sub>= 3130*h* Mpc³ (<sub>3</sub>160*h* Mpc³) for the
NGC (SGC) subsample. The input 2PCFs are taken from a t to the BOSS CMASS power spectrum, modelled using
the Eective Field Theory of Large Scale Structure [76], as implemented in class-pt [77].

$$
\ell_{1}+\ell_{2}+\ell_{3}
$$

$$
1.90h^{-3}G p c^{3}((0.77h^{-3}G p c^{3})
$$

$$
\dot{\dot{P_{\mathrm{s{o t t}}}}}=\dot{3}130h^{-3}\mathrm{M p c^{3}}\ (3\dot{1}60h^{-3}\mathrm{M p c^{3}})
$$

Fig.3compares the analytic and sample covariances for the NGC region, with the latter estimated from (16) using
p
2048 Patchy mocks. Considering the correlation matrices (Fig.3a, dened as R<sub>ij</sub>C<sub>ij</sub>*=* C<sub>ii</sub>C<sub>jj</sub>for covariance
C<sub>ij</sub>), we nd good agreement between the two, indicating that the Gaussian theory model well reproduces the matrix
structure. However, the diagonal elements (Fig.3b) of the analytic covariance are roughly a factor of two less than
those of the sample covariance. This is likely to arise from the non-trivial survey geometry of the BOSS CMASS
10
region [57] and prohibits direct use of the analytic covariance as a model for the 4PCF statistics.

$$
\mathsf{R}_{i j}\,\equiv\,\mathsf{C}_{i j}/\sqrt{\mathsf{C}_{i i}\mathsf{C}_{j j}}
$$

$$
\mathsf{C}_{i j})
$$

## IV. ANALYSIS METHODS

Below, we discuss two techniques that will be used to search for a signature of parity-violation in §V: (1) a nonparametric rank test, which does not require the likelihood to be Gaussian, and (2) data compression followed by
2
a mock-based-analysis. Both approaches make use of the smooth (but inaccurate) covariance matrix model of
§III Cto overcome the diculties associated with the high-dimensionality of the 4PCF. To avoid conrmation bias,
the pipeline implementing these techniques¹¹ was constructed before the BOSS data were unblinded.

$$
\S\ mathrm V V:(1)
$$

$$
\chi^{2}.
$$

## A. Non-Parametric Rank Test

Non-parametric tests provide a powerful way to analyze data when the underlying likelihood is not known. Here, we
consider a *rank test*, examining the null hypothesis of zero parity-odd 4PCF. To implement this, we rst dene a test
statistic, computed on both the data and a set of mocks. These simulations are required to obey the null hypothesis
(*i.e.* be parity-invariant) and have realistic noise properties. The test statistic measured from data is then compared
to the empirical distribution obtained from the mocks, allowing construction of a detection signicance. For example,
if the data statistic exceeds that of 95% of the mocks, we may reject the null hypothesis at 95% CL. The principal
advantage of this approach is that it does not require a theoretical PDF for the test statistic, *i.e.* we do not have to
assume the 4PCF to be a draw from some multivariate Gaussian. Indeed, the observed 4PCF does *not* appear to be
Gaussian; this is explored in AppendixA. A limitation of such rank tests is that one cannot claim a detection at high
signicance; rather the maximal condence level is (1 1*=N*<sup>mocks</sup>).

$$
\left(1-1/N_{\mathrm{m o c k s}}\right)
$$

2
Below, we will use the following test statistic, dubbed the *pseudo*-:
h i h i

$$
\tilde{\chi}^{2}\equiv\left[{\zeta}^{T}\tilde{\mathsf{C}}^{-1}{\zeta}\right]_{\operatorname{N G C}}+\left[{\zeta}^{T}\tilde{\mathsf{C}}^{-1}{\zeta}\right]_{\operatorname{S G C}},
$$

(18)

where is the set of measured parity-odd 4PCF multipoles (treated as a *N*-dimensional vector), and C~ is the
theoretical covariance matrix (§III C). If C~ is equal to the sample covariance (in the limit of innite mocks), (18) reduces

$$
N_{\zeta}mathrm{{\ d i m e n s i o n a l}}
$$

$$
\tilde{C}
$$

<sup>10</sup>Note that this discrepancy is *not* fully resolved by rescaling the theory covariance by a constant factor.

<sup>11</sup>Available atgithub.com/oliverphilcox/Parity-Odd-4PCF.

---

(a) Correlation Matrices

(b) Covariance Diagonal

FIG. 3. Comparison of the sample and analytic covariance matrices for the parity-odd 4PCF of the BOSS CMASS NGC region.
The former are estimated using (16), whilst the latter use the approach of [57], which does not include redshift-space distortions,
non-Gaussianity, or the eects of survey geometry. Fig.3acompares the correlation matrices (dened as the covariance matrices
normalized by their diagonals); we see similar structure in both cases. The rows and columns represent the indices of the 4PCF,
collapsed into one dimension, with each submatrix (indicated by the dotted lines) showing a dierent multiplet *f‘*1*;‘*2*;‘*3*g*, as
labelled in green. Elements within a submatrix are ordered in increasing radii *r₁;r₂;r₃*. We include only the rst six multiplets
here; 23 are used in the analysis of §V&VII C. Fig.3bshows the corresponding diagonal elements of the covariance. Notably,
the analytic covariance is an underestimate by a factor close to two; we expect this to arise primarily due to the non-uniform
survey geometry of the CMASS region [57].

$$
\{\ell_{1},\ell_{2},\ell_{3}\}
$$

$$
r_{1},r_{2},r_{3}
$$

2
to the usual statistic, given a ducial model of zero parity-odd 4PCF and assuming the NGC and SGC regions to
be independent. Whilst the covariances are not quite equal in practice (Fig.3), we expect (18) to produce a close-to-
2
optimal weighting for the data, particularly if the likelihood is close to Gaussian. Furthermore, since the pseudostatistic does not subtract o a mean, the rank test will naturally account for any spurious parity-odd contributions
that are present in both Patchy and BOSS. These might arise from imperfections in the edge-correction routine or
2
lightcone projection eects. To perform the test, we simply compute ~ for BOSS and each of the *N*<sub>mocks</sub>= 2048
Patchy simulations (§III A), before assigning a detection signicance from the empirical Patchy PDF.

$$
\chi^{2}
$$

$$
\chi^{2}
$$

$$
N_{\mathrm{m o c k s}}=2048
$$

$$
\tilde{\boldsymbol{\chi}}^{2}
$$

## B. Compressed Gaussian Analysis

A common trick when dealing with high-dimensional statistics is to apply some form of data compression [e.g.,
78{81]. In general, this proceeds by projecting the data onto some (small) set of basis vectors, thus greatly reducing the dimensionality. When performing parameter inference, basis vectors are usually chosen to preserve the Fisher
information matrix [e.g.,78,80] or the log-likelihood [81]. Since our primary goal in this work is to search for signatures
of parity-violation in a model-agnostic fashion, we adopt a somewhat dierent compression scheme, following [54,79].

Here, we project the 4PCF onto a basis given by the eigenvectors of the theoretical covariance matrix (§III C).
Explicitly, we dene the projected statistic
T

$$
\boldsymbol{v}\equiv\mathsf{U}^{T}\boldsymbol{\zeta},
$$

(19)

~ = UU*T*

[... middle omitted — see footer ...]

*Lett.* 78 (1997) 2054[astro-ph/9609169].
[31]R. G. Crittenden, P. Natarajan, U.-L. Pen and T. Theuns, *Discriminating Weak Lensing from Intrinsic Spin*
*Correlations Using the Curl-Gradient Decomposition*,ApJ 568 (2002) 20[astro-ph/0012336].
[32]S. M. Carroll, G. B. Field and R. Jackiw, *Limits on a Lorentz- and parity-violating modication of electrodynamics*,
*Phys. Rev. D* 41 (1990) 1231.
[33]V. Gluscevic and M. Kamionkowski, *Testing parity-violating mechanisms with cosmic microwave background*
*experiments*, *Phys. Rev. D* 81 (2010) 123529[1002.1308].
[34]R. R. Caldwell and C. Devulder, *Axion gauge eld ination and gravitational leptogenesis: A lower bound on B modes*
*from the matter-antimatter asymmetry of the Universe*, *Phys. Rev. D* 97 (2018) 023532[1706.03765].
[35]K. W. Masui, U.-L. Pen and N. Turok, *Two- and Three-Dimensional Probes of Parity in Primordial Gravity Waves*,
*Phys. Rev. Lett.* 118 (2017) 221301[1702.06552].
[36]F. Schmidt, N. E. Chisari and C. Dvorkin, *Imprint of ination on galaxy shape correlations*,JCAP 2015 (2015) 032
[1506.02671].
[37]M. Kamionkowski and T. Souradeep, *Odd-parity cosmic microwave background bispectrum*, *Phys. Rev. D* 83 (2011)
027301[1010.4304].
[38]M. Shiraishi, *Parity violation in the CMB trispectrum from the scalar sector*, *Phys. Rev. D* 94 (2016) 083503
[1608.00368].
[39]R. N. Cahn, Z. Slepian and J. Hou, *A Test for Cosmological Parity Violation Using the 3D Distribution of Galaxies*,
*arXiv e-prints* (2021) arXiv:2110.12004 [2110.12004].
[40]N. Kaiser, *Clustering in real space and in redshift space*,MNRAS 227 (1987) 1.
[41]A. J. S. Hamilton, *Linear Redshift Distortions: a Review*, in *The Evolving Universe*, D. Hamilton, ed., vol. 231 of
*Astrophysics and Space Science Library*, p. 185, Jan., 1998, astro-ph/9708102,DOI.
[42]C. Bonvin, R. Durrer, N. Khosravi, M. Kunz and I. Sawicki, *Redshift-space distortions from vector perturbations*,JCAP
2018 (2018) 028[1712.00052].
[43]D. Jeong and F. Schmidt, *The Odd-Parity Galaxy Bispectrum*, *arXiv e-prints* (2019) arXiv:1906.05198 [1906.05198].
[44]D. Munshi, A. Heavens, A. Cooray, J. Smidt, P. Coles and P. Serra, *New optimized estimators for the primordial*
*trispectrum*,MNRAS 412 (2011) 1993[0910.3693].
[45]K. M. Smith, L. Senatore and M. Zaldarriaga, *Optimal analysis of the CMB trispectrum*, *arXiv e-prints* (2015)
arXiv:1502.00635 [1502.00635].
[46]L. Dai, D. Jeong and M. Kamionkowski, *Seeking ination fossils in the cosmic microwave background*, *Phys. Rev. D* 87
(2013) 103006[1302.1868].
[47]DESI Collaboration, A. Aghamousa, J. Aguilar, S. Ahlen, S. Alam, L. E. Allen et al., *The DESI Experiment Part I:*
*Science,Targeting, and Survey Design*, *arXiv e-prints* (2016) arXiv:1611.00036 [1611.00036].
[48]R. Laureijs, J. Amiaux, S. Arduini, J. L. Augueres, J. Brinchmann, R. Cole et al., *Euclid Denition Study Report*, *arXiv*
*e-prints* (2011) arXiv:1110.3193 [1110.3193].
[49]LSST Science Collaboration, P. A. Abell, J. Allison, S. F. Anderson, J. R. Andrew, J. R. P. Angel et al., *Lsst science*

## https://doi.org/10.1103/PhysRevD.41.1231 Phys. Rev. D 41 (1990) 1231.

[1506.02671]. https://arxiv.org/abs/1506.02671

[1608.00368]. https://arxiv.org/abs/1608.00368

## arXiv:1502.00635 [1502.00635]. https://arxiv.org/abs/1502.00635

## e-prints (2011) arXiv:1110.3193 [1110.3193]. https://arxiv.org/abs/1110.3193

---

29

[50]C. G. Sabiu, B. Hoyle, J. Kim and X.-D. Li, *Graph Database Solution for Higher-order Spatial Statistics in the Era of*
*Big Data*,ApJS 242 (2019) 29[1901.00296].
[51]O. H. E. Philcox, Z. Slepian, J. Hou, C. Warner, R. N. Cahn and D. J. Eisenstein, *ENCORE: Estimating Galaxy*
*N -point Correlation Functions in O*(*N*<sup>g2</sup>) *Time*, *arXiv e-prints* (2021) arXiv:2105.08722 [2105.08722].
[52]R. N. Cahn and Z. Slepian, *Isotropic N-Point Basis Functions and Their Properties*, *arXiv e-prints* (2020)
arXiv:2010.14418 [2010.14418].
[53]O. H. E. Philcox and Z. Slepian, *Ecient Computation of N -point Correlation Functions in D Dimensions*, *arXiv*
*e-prints* (2021) arXiv:2106.10278 [2106.10278].
[54]O. H. E. Philcox, J. Hou and Z. Slepian, \A First Detection of the Connected 4-Point Correlation Function of Galaxies
using the BOSS CMASS Sample." in prep.
[55]M. Liguori, E. Sefusatti, J. R. Fergusson and E. P. S. Shellard, *Primordial Non-Gaussianity and Bispectrum*
*Measurements in the Cosmic Microwave Background and Large-Scale Structure*, *Advances in Astronomy* 2010 (2010)
980523[1001.4707].
[56]E. Dimastrogiovanni, M. Fasiello, D. Jeong and M. Kamionkowski, *Inationary tensor fossils in large-scale structure*,
JCAP 2014 (2014) 050[1407.8204].
[57]J. Hou, R. Cahn, O. Philcox and Z. Slepian, \Analytic Gaussian Covariance Matrices for Galaxy *N*-Point Correlation
Functions." in prep.
[58]T. L. Smith and M. Kamionkowski, *Probability distribution for non-Gaussianity estimators constructed from the CMB*
*trispectrum*, *Phys. Rev. D* 86 (2012) 063009[1203.6654].
[59]C. Hahn, F. Beutler, M. Sinha, A. Berlind, S. Ho and D. W. Hogg, *Likelihood non-Gaussianity in large-scale structure*
*analyses*,MNRAS 485 (2019) 2956[1803.06348].
[60]D. A. Varshalovich, A. N. Moskalev and V. K. Khersonskii, *Quantum Theory of Angular Momentum*. 1988,
10.1142/0270.
[61]S. D. Landy and A. S. Szalay, *Bias and Variance of Angular Correlation Functions*,ApJ 412 (1993) 64.
[62]I. Szapudi and A. S. Szalay, *A New Class of Estimators for the N-Point Correlations*,ApJ 494 (1998) L41.
[63]Z. Slepian, D. J. Eisenstein, J. R. Brownstein, C.-H. Chuang, H. Gil-Marn, S. Ho et al., *Detection of baryon acoustic*
*oscillation features in the large-scale three-point correlation function of SDSS BOSS DR12 CMASS galaxies*,MNRAS
469 (2017) 1738[1607.06097].
[64]S. Alam, F. D. Albareti, C. Allende Prieto, F. Anders, S. F. Anderson, T. Anderton et al., *The Eleventh and Twelfth*
*Data Releases of the Sloan Digital Sky Survey: Final Data from SDSS-III*,ApJS 219 (2015) 12[1501.00963].
[65]D. J. Eisenstein, D. H. Weinberg, E. Agol, H. Aihara, C. Allende Prieto, S. F. Anderson et al., *SDSS-III: Massive*
*Spectroscopic Surveys of the Distant Universe, the Milky Way, and Extra-Solar Planetary Systems*,AJ 142 (2011) 72
[1101.1529].
[66]K. S. Dawson, D. J. Schlegel, C. P. Ahn, S. F. Anderson, E. Aubourg, S. Bailey et al., *The Baryon Oscillation*
*Spectroscopic Survey of SDSS-III*,AJ 145 (2013) 10[1208.0022].
[67]F. Beutler, H.-J. Seo, S. Saito, C.-H. Chuang, A. J. Cuesta, D. J. Eisenstein et al., *The clustering of galaxies in the*
*completed SDSS-III Baryon Oscillation Spectroscopic Survey: anisotropic galaxy clustering in Fourier space*,MNRAS
466 (2017) 2242[1607.03150].
[68]H. A. Feldman, N. Kaiser and J. A. Peacock, *Power-Spectrum Analysis of Three-dimensional Redshift Surveys*,ApJ 426
(1994) 23[astro-ph/9304022].
[69]F.-S. Kitaura, S. Rodrguez-Torres, C.-H. Chuang, C. Zhao, F. Prada, H. Gil-Marn et al., *The clustering of galaxies in*
*the SDSS-III Baryon Oscillation Spectroscopic Survey: mock galaxy catalogues for the BOSS Final Data Release*,
MNRAS 456 (2016) 4156[1509.06400].
[70]S. A. Rodrguez-Torres, C.-H. Chuang, F. Prada, H. Guo, A. Klypin, P. Behroozi et al., *The clustering of galaxies in the*
*SDSS-III Baryon Oscillation Spectroscopic Survey: modelling the clustering and halo occupation distribution of BOSS*
*CMASS galaxies in the Final Data Release*,MNRAS 460 (2016) 1173[1509.06404].
[71]Z. Slepian and D. J. Eisenstein, *Computing the three-point correlation function of galaxies in O(N2) time ^*,MNRAS 454
(2015) 4142[1506.02040].
[72]F. Sosa Nu~nez and G. Niz, *On the fast random sampling and other properties of the three point correlation function in*
*galaxy surveys*,JCAP 2020 (2020) 021[2006.05434].
[73]M. Vargas-Maga~na, S. Ho, A. J. Cuesta, R. O’Connell, A. J. Ross, D. J. Eisenstein et al., *The clustering of galaxies in*
*the completed SDSS-III Baryon Oscillation Spectroscopic Survey: theoretical systematics and Baryon Acoustic*
*Oscillations in the galaxy correlation function*,MNRAS 477 (2018) 1153[1610.03506].
[74]D. Wadekar and R. Scoccimarro, *Galaxy power spectrum multipoles covariance in perturbation theory*, *Phys. Rev. D* 102
(2020) 123517[1910.02914].
[75]O. H. E. Philcox and D. J. Eisenstein, *Estimating covariance matrices for two- and three-point correlation function*
*moments in Arbitrary Survey Geometries*,MNRAS 490 (2019) 5931[1910.04764].
[76]M. M. Ivanov, M. Simonovic and M. Zaldarriaga, *Cosmological parameters from the BOSS galaxy power spectrum*,
JCAP 2020 (2020) 042[1909.05277].
[77]A. Chudaykin, M. M. Ivanov, O. H. E. Philcox and M. Simonovic, *Nonlinear perturbation theory extension of the*
*Boltzmann code CLASS*, *Phys. Rev. D* 102 (2020) 063533[2004.10607].
[78]A. F. Heavens, R. Jimenez and O. Lahav, *Massive lossless data compression and multiple parameter estimation from*

[1101.1529]. https://arxiv.org/abs/1101.1529

*book, version 2.0*, 2009.

## arXiv:2010.14418 [2010.14418]. https://arxiv.org/abs/2010.14418
## e-prints (2021) arXiv:2106.10278 [2106.10278]. https://arxiv.org/abs/2106.10278

## https://doi.org/10.1142/0270 10.1142/0270.

---

30

[79]R. Scoccimarro, *The Bispectrum: From Theory to Observations*,ApJ 544 (2000) 597[astro-ph/0004086].
[80]J. Alsing and B. Wandelt, *Generalized massive optimal data compression*,MNRAS 476 (2018) L60[1712.00012].
[81]O. H. E. Philcox, M. M. Ivanov, M. Zaldarriaga, M. Simonovic and M. Schmittfull, *Fewer mocks and less noise:*
*Reducing the dimensionality of cosmological observables with subspace projections*, *Phys. Rev. D* 103 (2021) 043508
[2009.03311].
[82]J. Wishart and M. S. Bartlett, *The generalised product moment distribution in a normal system*, *Proceedings of the*
*Cambridge Philosophical Society* 29 (1933) 260.
[83]J. Hartlap, P. Simon and P. Schneider, *Why your model parameter condences might be too optimistic. Unbiased*
*estimation of the inverse covariance matrix*,A&A 464 (2007) 399[astro-ph/0608064].
[84]E. Sellentin and A. F. Heavens, *Parameter inference with estimated covariance matrices*,MNRAS 456 (2016) L132
[1511.05969].
[85]C. Eckart and G. Young, *The approximation of one matrix by another of lower rank*, *Psychometrika* 1 (1936) 211.
[86]O. H. E. Philcox, J. Hou and Z. Slepian, *A First Detection of the Connected 4-Point Correlation Function of Galaxies*
*Using the BOSS CMASS Sample*, *arXiv e-prints* (2021) arXiv:2108.01670 [2108.01670].
[87]S. Alam, M. Ata, S. Bailey, F. Beutler, D. Bizyaev, J. A. Blazek et al., *The clustering of galaxies in the completed*
*SDSS-III Baryon Oscillation Spectroscopic Survey: cosmological analysis of the DR12 galaxy sample*,MNRAS 470
(2017) 2617[1607.03155].
[88]O. H. E. Philcox and M. M. Ivanov, *The BOSS DR12 Full-Shape Cosmology: CDM Constraints from the Large-Scale*
*Galaxy Power Spectrum and Bispectrum Monopole*, *arXiv e-prints* (2021) arXiv:2112.04515 [2112.04515].
[89]N. Arkani-Hamed, P. Creminelli, S. Mukohyama and M. Zaldarriaga, *Ghost ination*, *JCAP* 04 (2004) 001
[hep-th/0312100].
[90]K. Freese, J. A. Frieman and A. V. Olinto, *Natural ination with pseudo Nambu-Goldstone bosons*, *Phys. Rev. Lett.* 65
(1990) 3233.
[91]S. Alexander, A. Marciano and D. Spergel, *Chern-Simons ination and baryogenesis*,JCAP 2013 (2013) 046.
[92]S. Hannestad, *What is the lowest possible reheating temperature?*, *Phys. Rev. D* 70 (2004) 043506[astro-ph/0403291].
[93]C. Caprini and L. Sorbo, *Adding helicity to inationary magnetogenesis*,JCAP 2014 (2014) 056[1407.2809].
[94]B. Ratra, *Cosmological \Seed" Magnetic Field from Ination*,ApJ 391 (1992) L1.
[95]M. Shiraishi, E. Komatsu and M. Peloso, *Signatures of anisotropic sources in the trispectrum of the cosmic microwave*
*background*,JCAP 2014 (2014) 027[1312.5221].
[96]L. Ackerman, S. M. Carroll and M. B. Wise, *Imprints of a primordial preferred direction on the microwave background*,
*Phys. Rev. D* 75 (2007) 083502[astro-ph/0701357].
[97]M. Shiraishi, E. Komatsu, M. Peloso and N. Barnaby, *Signatures of anisotropic sources in the squeezed-limit bispectrum*
*of the cosmic microwave background*,JCAP 2013 (2013) 002[1302.3056].
[98]Planck Collaboration, Y. Akrami, F. Arroja, M. Ashdown, J. Aumont, C. Baccigalupi et al., *Planck 2018 results. IX.*
*Constraints on primordial non-Gaussianity*,A&A 641 (2020) A9[1905.05697].
[99]S. Endlich, A. Nicolis and J. Wang, *Solid ination*,JCAP 2013 (2013) 011[1210.0569].
[100]G. Franciolini, A. Kehagias, A. Riotto and M. Shiraishi, *Detecting higher spin elds through statistical anisotropy in the*
*CMB bispectrum*, *Phys. Rev. D* 98 (2018) 043533[1803.03814].
[101]P. Campeti, O. Ozsoy, I. Obata and M. Shiraishi, *New constraints on axion-gauge eld dynamics during ination from*
*Planck and BICEP/Keck data sets*, 2203.03401.
[102]J. Maldacena, *Non-gaussian features of primordial uctuations in single eld inationary models*, *Journal of High*
*Energy Physics* 2003 (2003) 013[astro-ph/0210603].
[103]E. Dimastrogiovanni, M. Fasiello and L. Pinol, *Primordial Stochastic Gravitational Wave Background Anisotropies:*
*in-in Formalization and Applications*, 2203.17192.
[104]E. Dimastrogiovanni, M. Fasiello and M. Kamionkowski, *Imprints of Massive Primordial Fields on Large-Scale*
*Structure*, *JCAP* 02 (2016) 017[1504.05993].
[105]P. Creminelli and M. Zaldarriaga, *Single eld consistency relation for the 3-point function*, *JCAP* 10 (2004) 006
[astro-ph/0407059].
[106]D. Bertolini, K. Schutz, M. P. Solon and K. M. Zurek, *The trispectrum in the Eective Field Theory of Large Scale*
*Structure*,JCAP 2016 (2016) 052[1604.01770].
[107]Planck Collaboration, Y. Akrami, F. Arroja, M. Ashdown, J. Aumont, C. Baccigalupi et al., *Planck 2018 results. X.*
*Constraints on ination*,A&A 641 (2020) A10[1807.06211].
[108]L. Sorbo, *Parity violation in the Cosmic Microwave Background from a pseudoscalar inaton*,JCAP 2011 (2011) 003
[1101.1525].
[109]G. Arfken, H. Weber and F. Harris, *Mathematical Methods for Physicists: A Comprehensive Guide*. Elsevier Science,
2013.
[110]NIST, *NIST Digital Library of Mathematical Functions*. DLMF.
[111]O. H. E. Philcox and Z. Slepian, *An exact integral-to-sum relation for products of Bessel functions*, *Proceedings of the*
*Royal Society of London Series A* 477 (2021) 20210376[2104.10169].
[112]O. H. E. Philcox and D. J. Eisenstein, *Computing the small-scale galaxy power spectrum and bispectrum in conguration*
*space*,MNRAS 492 (2020) 1214[1912.01010].

## Planck and BICEP/Keck data sets , 2203.03401. https://arxiv.org/abs/2203.03401

[astro-ph/0407059]. https://arxiv.org/abs/astro-ph/0407059

[1101.1525]. https://arxiv.org/abs/1101.1525

*galaxy spectra*,MNRAS 317 (2000) 965[astro-ph/9911102].

[2009.03311]. https://arxiv.org/abs/2009.03311

[1511.05969]. https://arxiv.org/abs/1511.05969

[hep-th/0312100]. https://arxiv.org/abs/hep-th/0312100
## https://doi.org/10.1103/PhysRevLett.65.3233 (1990) 3233.

──────── [TRUNCATED] ────────
Showing 44,975 chars (head) + 14,909 chars (tail) of 162,415 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-570c6305b9.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/arxiv.org-570c6305b9.md" offset=1070 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────
