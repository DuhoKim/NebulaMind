READING_C

## Deciding quotation

> “This **could result** in a non-homogeneous solution for the metric of the Universe on very large scales... smooth background across disconnected regions with an infrared cutoff in the spectrum of inhomogeneities for χ>χ§. Solutions in different regions **could be matched** as in Sanghai & Clifton 2015.”

The operative perturbation claim is tentative (“could”), and supplies neither an equation nor a definition of “cutoff.” By contrast, the paper's actual imposed condition is:

> “we will require Φ(χ>χ§)=0 in Eq.16, so that there is no flux (i.e. no effects of gravity) beyond the causal scale. This implies”

Eq. 16 defines Φ as a four-volume integral of \(R^0{}_0\), and the stated implication is Eq. 17, a constraint on \(\Lambda\) through averaged \(\rho+3p\). It is not a boundary condition on a perturbation potential or a derivation of perturbation covariance. Nothing quoted connects that flux condition mathematically to either \(P(k)=0\) below a threshold or \(\xi(r)=0\) beyond a separation.

The phrase “spectrum of inhomogeneities” weakly suggests Fourier language and hence A, but “for χ>χ§” is phrased in a distance variable and the motivating causal argument (“if there is no cause there should not be any effect”) weakly suggests real-space separation and hence B. These cues conflict. Moreover, deleting globally extended low-\(k\) Fourier modes is not itself a local no-influence condition. Since A and B are mathematically incompatible, ambiguous prose cannot select either sharp constraint.

## 2. Is Reading C correct?

Yes. It is illegitimate to extract any sharp perturbation support condition from this paper. The source offers a qualitative possible consequence, not a covariance, matching law, stochastic initial-condition model, or perturbation boundary-value problem. Its only derived condition is Eq. 17, which constrains the background \(\Lambda\) and says nothing about perturbation support or shape.

Accordingly, Program (A) cannot present an optimization under A or B as a calibrated prediction of this theory. At most it can present two additional, explicitly external formalizations and ask what each would imply. The stronger source-level conclusion is that the theory does not fix even the support of the primordial spectrum.

## 3. Is the proposed admissible class right and non-circular?

Under Reading C there is no source-licensed “chosen support condition,” so the class is refuted **as a representation of the paper**. Conditions (ii) and (iii) do not repair that foundational gap. Positivity is appropriate for a statistically homogeneous power spectrum, but statistical homogeneity and isotropy of a finite causal patch are themselves assumptions not supplied by the quoted argument.

Matching \(P_{\Lambda\mathrm{CDM}}(k)\) for \(k>k_{\rm norm}\), with all low-\(\ell\) data held out, need not be observationally circular: high-\(\ell\) data can calibrate short-scale amplitude and tilt without directly fitting \(S_{1/2}\). But it is still a strong external model assumption, not a consequence of the causal condition. It can indirectly constrain low multipoles because projection kernels are broad and low \(\ell\) receive some contribution from \(k>k_{\rm norm}\); this leakage must be quantified, and the normalization parameters and their covariance must be fixed using a genuinely disjoint likelihood. A hard equality above \(k_{\rm norm}\) is much stronger than high-\(\ell\) calibration warrants and introduces an artificial seam unless continuity/smoothness conditions are specified.

Essential missing choices include the stochastic state/covariance; homogeneity and isotropy within a patch; the observer's position relative to the boundary; geometry and boundary/matching conditions; whether translational invariance (needed for a scalar \(P(k)\)) survives; regularity and positive-definiteness; and UV/Hadamard behavior if the object is meant to arise from a physical quantum state. Transfer functions and late-time cosmological parameters must also be fixed independently of the held-out statistic.

As written, the class commits both errors in different respects: it is **too narrow** in imposing an unlicensed A-or-B support rule, exact \(\Lambda\)CDM short-scale equality, and usually implicit homogeneity/isotropy; yet, below \(k_{\rm norm}\), it is **too wide** if arbitrary nonnegative functions are allowed without regularity, covariance realizability, patch geometry, observer position, or matching dynamics. The former can manufacture a prediction; the latter can make a no-go trivial. There is no principled repair available from this source alone.

## 4. Does the choice matter?

It should not be assumed harmless. A removes low-\(k\) power, whereas a compactly supported \(\xi\) necessarily has an analytic transform and may retain substantial or even maximal power near \(k=0\). \(S_{1/2}\) is built from large-angle correlations and is especially sensitive to precisely this low-\(k\), low-\(\ell\) structure. The two feasible sets also differ globally, not by a small nuisance parameter, so there is no physical reason their minima should fall on the same side of approximately \(1150\,\mu\mathrm K^4\).

Computing both minima could be a useful robustness experiment. If both independently land on the same side after identical high-\(\ell\) calibration and all missing assumptions are exposed, that particular inequality would be robust to this ambiguity. It still would not turn either constraint into a prediction licensed by the paper. Until that calculation is done, expecting agreement would be wishful: optimization can exploit the radically different low-\(k\) freedoms, and the observed threshold is not protected by any theorem quoted here.

## Ways the formalization could make the eventual result wrong

- Treating the integrated flux \(\Phi\) as a perturbation field or Dirichlet condition.
- Converting “infrared cutoff” into a hard cutoff, and choosing \(\pi/\chi§\) rather than another scale convention, without a derivation.
- Assuming global Fourier modes and translational invariance in a finite, observer-dependent patch.
- Equating absence of causal influence with zero correlation; common initial conditions can correlate causally disconnected regions.
- Letting high-\(\ell\) normalization leak held-out low-\(\ell\) information through shared parameters or broad transfer kernels.
- Optimizing over spectra that are nonnegative but not realizable by the required geometry/state, or allowing pathological discontinuous/oscillatory spectra that no matching dynamics could produce.
- Ignoring cosmic variance, mask/estimator dependence, late-time ISW and lensing contributions, and uncertainty in \(\chi§\) when comparing with the observed \(S_{1/2}\).
- Reporting an extremum over an externally invented class as a prediction or no-go theorem of the source model.
