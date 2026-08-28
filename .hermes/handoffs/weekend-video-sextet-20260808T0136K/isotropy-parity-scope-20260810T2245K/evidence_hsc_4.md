# URL: https://arxiv.org/pdf/2410.18884

# Symmetry in Hyper Suprime-Cam galaxy spin directions

[http://orcid.org/0000-0002-0986-314X](http://orcid.org/0000-0002-0986-314X) Richard Stiskalek 1 andHarry Desmond [http://orcid.org/0000-0003-0685-9791](http://orcid.org/0000-0003-0685-9791) 2

1 2
Richard Stiskalek \[Image: Im1\] andHarry Desmond \[Image: Im1\]

1 _Astrophysics, University of Oxford, Denys Wilkinson Building, Keble Road, Oxford, OX1 3RH, UK_

2 _Institute of Cosmology & Gravitation, University of Portsmouth, Dennis Sciama Building, Portsmouth, PO1 3FX, UK_

## ABSTRACT

We perform a Bayesian analysis of anisotropy in binary galaxy spin directions in the Hyper-Suprime
Cam Data Release 3 catalogue, in response to a recent claim that it exhibits a dipole (Shamir2024).
We find no significant evidence for anisotropy, or for a direction-independent spin probability that
differs from 0.5. These results are unchanged allowing for a quadrupole or simply searching for a
fixed anisotropy between any two hemispheres, and the Bayes factor indicates decisive evidence for
the isotropic model. Our principled method contrasts with the statistic employed byShamir(2024),
which lacks a strong theoretical foundation. Our code is available at ©.

_Keywords:_ Galaxies (573) — Large-scale structure of the universe (902) — Bayesian statistics (1900)
— Astrostatistics (1882)

## 1\. INTRODUCTION

The Universe is thought to be homogeneous and isotropic on large scales, in accordance with the cosmological
principle. However, several observations such as the cosmic microwave background anomalies, bulk flows, and discrepancies between the cosmic microwave background and distant matter rest frames, point to possible anisotropies
(e.g.,Watkins et al.2023;Secrest et al.2022). There have been claims for anisotropy in the directions of galaxy spins,
forming a dipole axis that would violate large-scale anisotropy (e.g.,Longo2011;McAdam & Shamir2023). Most
recently,Shamir(2024) claims a more than 3 _σ_ detection of such a dipole in spins derived from Hyper Suprime-Cam
Data Release 3 (HSC DR3;Aihara et al.2022).Shamir(2024) also claims a monopole in spin probability that is inconsistent with 0.5, with galaxies rotating opposite to the Milky Way (as seen from Earth) significantly more common
than those rotating in the same direction.

The claims of anisotropy prior toShamir(2024) were recently revisited byPatel & Desmond(2024) who found no
significant evidence for a dipole or a monopole differing from 0.5 in any dataset publicly available at that time. This
was shown through both a standard Bayesian and frequentist analysis. The discrepancy with previous analyses was
found to be the poorly motivated statistics that they employed. Here we adapt the framework ofPatel & Desmondto
the new HSC data to show that this also does not indicate an anomalous monopole, dipole or quadrupole.

## 2\. METHODOLOGY

arXiv:2410.18884v3 \[astro-ph.GA\] 7 Nov 2024We take the HSC DR3 data which matches that used byShamir(2024). We assume that these spin assignments are
correct; a direction-dependent bias in the assignment would be much more likely to introduce a spurious dipole than
spuriously remove a true one. The catalogue is illustrated in the left panel of Figure1. We follow the methodology
th
ofPatel & Desmond. We denote the spin direction of the _i_ galaxy relative to the Milky Way as _s_ i, which can be
either Z-wise or S-wise. The likelihood of Z-wise spin is

$$
i^{\\mathrm{t h}}
$$

$$
s\_{i}.
$$

$$
\\mathcal{L}(s\_{i}\|M,D,\\hat{d},Q,\\hat{q} _{1},\\hat{q}_{2})=M+D\\left(\\hat{d}\\cdot\\hat{\\mathbf{n}} _{i}\\right)+Q\\left(\\hat{q}_{1}\\cdot\\hat{\\mathbf{n}} _{i}\ \\hat{q}_{2}\\cdot\\hat{\\mathbf{n}} _{i}-\\frac{1}{3}\\hat{q}_{1}\\cdot\\hat{q}\_{2}\\right)
$$

(1)

Corresponding author: Richard Stiskalek, Harry Desmond
[richard.stiskalek@physics.ox.ac.uk](mailto:richard.stiskalek@physics.ox.ac.uk), [harry.desmond@port.ac.uk](mailto:harry.desmond@port.ac.uk)

* * *

2

where _M_ is the monopole, _D_ the dipole magnitude and _d_ ˆ is a unit vector pointing in the direction of the dipole. _Q_ is
the strength of a possible quadrupole with unit axes _q_ ˆ₁ and _q_ ˆ₂. _n_ ˆiis the unit vector in the direction of the galaxy.
We use uniform priors on _M_, _D_ and _Q_ and on the area element of all unit vectors. The likelihood of S-wise spin is
Q
1\*−L\*, and we assume that all galaxies are independent such that the dataset likelihood isi _L_ i. Isotropy corresponds
to _D_ = 0 and _Q_ = 0, and an overall balance between Z-wise and S-wise spins corresponds to _M_ = 0\*.\*5.

$$
\\hat{d}
$$

$$
\\hat{q}\_{1}
$$

$$
\\hat{q} _{2}.\ hat n{{}}_{i}
$$

$$
M,,D
$$

$$
Q
$$

$$
1-\\mathcal{L}
$$

$$
D=0
$$

$$
\\mathbb{Z}
$$

$$
\\prod\_{i}\\mathcal{L}\_{i}
$$

$$
M=0.5
$$

We upgrade the code ofPatel & Desmondto JAX¹, sampling the posterior using the No U-Turns Sampler (Hoffman
& Gelman2011) method of Hamiltonian Monte Carlo algorithm (HMC) implemented in NumPyro (Phan et al.2019).
−3
We remove burn-in and use sufficient steps for the Gelman–Rubin statistic to be 1 to within 10 (Gelman & Rubin
1992).

$$
\\mathbf{J A X^{1}}
$$

$$
10^{-3}
$$

## 3\. RESULTS AND DISCUSSION

We first allow a monopole and dipole, showing the posterior in the right panel of Figure1. We find that _M_ is
consistent with 0\*. _5, indicating no preference for one spin direction over the other, and that D is consistent with 0 to_
_within 2_ σ\*, indicating no significant dipole. That _M ≈_ 0\*. _5 is unsurprising given that the average spin in the sample is_
_0.499, and that D ≈ 0 is unsurprising given the poor sky coverage of the HSC data. This makes the constraints on D_
_a few times weaker than those of the other datasets studied inPatel & Desmond. We then run the monopole–dipole–_
_quadrupole inference, finding the same results and that Q is consistent with 0. FollowingShamir(2024) we also try_
_splitting the data into the redshift ranges 0 < z < 0.1 and 0.1 < z < 0.2, finding near-identical results in both cases._
_We also investigate the “hemisphere anisotropy” model ofPatel & Desmondwhich neglects the cos θ dependence of_
_the dipole, finding the anisotropy parameter A to be consistent with 0 within 2_ σ\*.

$$
M\\approx0.5
$$

$$
D\\approx0
$$

$$
0<z<0.1
$$

$$
0.1<z<0.2
$$

Finally, we compute the Bayes factor describing the relative probability of the monopole–only and monopole–dipole
models, i.e. the preference for adding a dipole. As the Bayesian evidence is prior-dependent we try two ranges for
the uniform prior on _D_: 0 to 0\*. _1 and 0 to 0_. _5 (both fully enclosing the posterior in all cases). We use the harmonic_
_package (Polanska et al.2024) to compute it directly from the HMC chain. We find log₁₀ evidence ratios in favour_
_of the monopole-only model of 5.71 and 4.61 for the looser and tighter D priors, respectively. Even in the latter case_
_this corresponds to a Bayes factor of 40_,\*738 in favour of the monopole-only model, which is “decisive” on the Jeffreys’
scale.

$$
\\mathrm{l o g}\_{10}
$$

We conclude that there is no evidence for an anisotropy of any kind in the spin directions of the HSC DR3 dataset,
just as there is not in any other. That the opposite is found inShamir(2024) is attributable to the use of an off- _χ²_
statistic which relies on assumptions that may not be fully justified, as detailed in Sec. 4.3 ofPatel & Desmond.

$$
\[-\\chi^{2}\
$$\
\
## DATA AVAILABILITY\
\
Our analysis code is available at © and Zenodo (Desmond & Patel2024). The HSC DR3 data is available at\
[https://people.cs.ksu.edu/](https://people.cs.ksu.edu/) ∼lshamir/data/asymmetry hsc/.\
\
## ACKNOWLEDGEMENTS\
\
We thank Dhruva Patel for contributions to the paper on which our analysis is based. RS acknowledges financial\
support from STFC Grant No. ST/X508664/1 and the Snell Exhibition of Balliol College, Oxford. HD is supported\
by a Royal Society University Research Fellowship (grant no. 211046). For the purpose of open access, we have applied\
a Creative Commons Attribution (CC BY) licence to any Author Accepted Manuscript version arising.\
\
## REFERENCES\
\
Aihara, H., AlSayyad, Y., Ando, M., et al. 2022, PASJ, 74,\
247, doi:10.1093/pasj/psab122\
Desmond, H., & Patel, D. 2024,\
harrydesmond/GalaxySpinAnisotropy:\
GalaxySpinAnisotropy v1.0, 1.0, Zenodo,\
doi:10.5281/zenodo.14036930\
\
Gelman, A., & Rubin, D. B. 1992, Statistical Science, 7,\
457 , doi:10.1214/ss/1177011136\
Hoffman, M. D., & Gelman, A. 2011, arXiv e-prints,\
arXiv:1111.4246, doi:10.48550/arXiv.1111.4246\
Longo, M. J. 2011, Physics Letters B, 699, 224,\
doi:10.1016/j.physletb.2011.04.008\
McAdam, D., & Shamir, L. 2023, Advances in Astronomy,\
2023, 1, doi:10.1155/2023/4114004\
\
1 [https://jax.readthedocs.io/en/latest/](https://jax.readthedocs.io/en/latest/)\
\
* * *\
\
3\
\
Figure 1. _Left:_ Sky distribution of the HSC DR3 galaxies in equatorial Mollweide projection, with galaxies spinning S-wise in\
blue and Z-wise in red. _Right:_ Corner plot from the monopole-plus-dipole inference, indicating a dipole magnitude _D_ consistent\
with 0 and a monopole _M_ consistent with 0.5.\
\
## doi:10.1093/mnras/stae2158 [http://doi.org/10.1093/mnras/stae2158](http://doi.org/10.1093/mnras/stae2158)\
\
Patel, D., & Desmond, H. 2024, _M_ NRAS, 534, 1553,\
doi:10.1093/mnras/stae2158\
Phan, D., Pradhan, N., & Jankowiak, M. 2019, arXiv\
e-prints, arXiv:1912.11554,\
doi:10.48550/arXiv.1912.11554\
Polanska, A., Price, M. A., Piras, D., Spurio Mancini, A., &\
McEwen, J. D. 2024, arXiv e-prints, arXiv:2405.05969,\
doi:10.48550/arXiv.2405.05969\
\
## doi:10.3847/2041-8213/ac88c0 [http://doi.org/10.3847/2041-8213/ac88c0](http://doi.org/10.3847/2041-8213/ac88c0)\
\
Secrest, N. J., von Hausegger, S., Rameez, M., Mohayaee,\
R., & Sarkar, S. 2022, ApJL, 937, L31,\
doi:10.3847/2041-8213/ac88c0\
Shamir, L. 2024, arXiv e-prints, arXiv:2410.15269.\
[https://arxiv.org/abs/2410.15269](https://arxiv.org/abs/2410.15269)\
Watkins, R., Allen, T., Bradford, C. J., et al. 2023,\
MNRAS, 524, 1885, doi:10.1093/mnras/stad1984\
\
## doi:10.48550/arXiv.1912.11554 [http://doi.org/10.48550/arXiv.1912.11554](http://doi.org/10.48550/arXiv.1912.11554)\
\
## [https://arxiv.org/abs/2410.15269](https://arxiv.org/abs/2410.15269) [https://arxiv.org/abs/2410.15269](https://arxiv.org/abs/2410.15269)\
\
## doi:10.48550/arXiv.2405.05969 [http://doi.org/10.48550/arXiv.2405.05969](http://doi.org/10.48550/arXiv.2405.05969)