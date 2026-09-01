UNDETERMINED_NEEDS_PRIMORDIAL_AMPLITUDE_AND_UNIQUE_CUTOFF_TRANSFER

# Gaztañaga causal-horizon CMB-cutoff calibration (Codex seat)

## Bottom line

The pinned papers fix a causal **scale**, but they do not define one quantitative stochastic primordial spectrum (normalization, cutoff window, and bounce-to-curvature matching) from which a unique temperature `C_l` follows. Consequently neither `C_2` nor `S_1/2` is a model prediction. This is not repaired by importing the Planck-fitted scalar amplitude: doing so would calibrate the model with the observation it is meant to predict, contrary to the brief's non-circularity requirement.

There is also no single exact cutoff prescription across the papers. The strongest Fourier-space statement is a sharp absence of incoming modes at `k < pi/R`, while the earlier paper gives an illustrative angular-multipole suppression (`l<5`) and a verbal expectation of no correlations above about 60 degrees. A sharp Fourier cutoff does **not** imply a compact-support angular correlation function, and setting a few `C_l` to zero does **not** make `C(theta)` vanish for every `theta>60 degrees`.

## 1. What is actually pinned

### Causal/background scale

1. Gaztañaga identifies the pre-inflation causal scale with the comoving horizon at the start of inflation and says it remains fixed: `chi_section ~= eta(a_i)=d_H(t_i)` and “the scale ... is fixed before inflation in comoving coordinates” (`../bhu-reading-20260823/sources/2003.11544_clean.txt:95-113`).
2. The causal boundary condition is a vanishing gravitational flux outside causal contact, `Phi(chi>chi_section)=0`; the paper says this implies an infrared cutoff in inhomogeneities but does not give their spectral window (`2003.11544_clean.txt:241-265`).
3. Equations (20)-(24) obtain the scale by solving the light-cone average condition `rho_section=rho_Lambda` with the measured flat-background densities, giving

   `chi_section=(3.149 +/- 0.006)c/H0`, `a_section=0.933 +/- 0.006`

   (`2003.11544_clean.txt:300-343`). The last-scattering lookback distance is quoted as `chi_CMB ~= 3.145 c/H0`, and the paper maps the ratio to `theta_section ~= 60 degrees` (`2003.11544_clean.txt:405-416`). Thus the location is fixed from the assumed background/causal boundary; it is not an amplitude calculation. The same paper also reverses the argument and estimates `Omega_Lambda=0.7+/-0.1` from the observed angular cutoff, explicitly warning that ISW and lensing add large-angle correlations (`2003.11544_clean.txt:429-437`). That inverse observational estimate cannot be used in a non-circular prediction.
4. In the BHU form, the event horizon is `r_S=r_Lambda=H_Lambda^-1`, with `H_Lambda^2=H0^2 Omega_Lambda`, and the quoted mass/radius are about `5e22 M_sun` and `6e22 km` (`../bhu-reading-20260823/sources/2204.11608_clean.txt:175-188`). The later angular statement is `theta ~= 2R/d_CMB ~= 60 degrees` (`2204.11608_clean.txt:303-306`).

### Cutoff prescription: mutually non-equivalent statements

- **Fourier statement (sharp location):** “cutoff for scales larger than `lambda>2R` (`k<pi/R`)” (`2204.11608_clean.txt:292-295`). Read literally, this supplies the step location `W(k)=Theta(k-pi/R)` for the incoming spectrum. It does not supply its amplitude, tilt through the bounce, which epoch's `R(tau)` enters, or the scalar transfer/matching condition.
- **Angular statement (verbal):** “expect to see no correlations ... `theta>...~=60 degrees`” (`2003.11544_clean.txt:405-418`). The same passage/figure says the shaded comparison simulations “suppress ... multipoles `l<5`” (`2003.11544_clean.txt:402-410`); it does not say this `l<5` operation is the model's exact transfer function.
- **Smoothness statement:** the earlier paper asks for a “smooth background across disconnected regions with an infrared cutoff” (`2003.11544_clean.txt:251-253`). It does not choose a sharp versus smooth window.
- **Amplitude statement:** the review says the amplitude of gravitational-instability perturbations is *scale invariant* (`2204.11608_clean.txt:257-260`), which describes scale dependence, not normalization. It later calls the origin of `delta T ~= 10^-5` a remaining mystery (`2204.11608_clean.txt:337-340`) and says further work is needed “to estimate the perturbations” produced by the bounce (`2204.11608_clean.txt:330-337`). Another pinned review introduces an initially uniform cloud with “small random amplitude fluctuations” (`../bhu-reading-20260823/sources/sym14101984_clean.txt:93`) and says “let us further assume” similar amplitude on all scales (`sym14101984_clean.txt:520`): neither fixes the amplitude.

Therefore the papers fix neither a unique sharp/smooth window nor the normalization of surviving modes. The `k`, `l`, and real-angle descriptions cannot be substituted for one another without an extra model.

## 2. Derivation and non-identifiability proof

For scalar temperature anisotropy, a specified primordial curvature spectrum and transfer function would give

`C_l^TT = 4 pi integral d ln k P_R(k) |Delta_l^T(k)|^2`.

The literal sharp-cutoff completion would be

`P_R(k) = A (k/k0)^(n_s-1) Theta(k-k_cut)`, `k_cut=pi/R`,

and hence

`C_l(A,k_cut)=A F_l(k_cut,n_s,background,bounce matching)`.

The angular correlation and requested statistic are

`C(theta)=sum_(l=2)^infinity (2l+1) C_l P_l(cos theta)/(4 pi)`,

`S_1/2=integral_(-1)^(1/2) C(x)^2 dx = A^2 G(k_cut,n_s,background,bounce matching)`.

In particular `C_2=A F_2` and `S_1/2=A^2 G`. Since the papers leave `A` undetermined (and also leave `F_l` non-unique), every `A>=0` is compatible with the stated cutoff location: `A=0` gives `C_2=S_1/2=0`, while rescaling `A -> qA` gives `C_2 -> q C_2` and `S_1/2 -> q^2 S_1/2`. No finite amplitude or upper/lower falsification threshold follows.

The alternative hard real-space proposition `C(theta)=0` for all `theta>60 degrees`, if imposed as an additional axiom, gives exactly `S_1/2=0`. But it still does not determine `C_2`, because infinitely many full-sky spectra/correlation functions have the same zero interval; it also conflicts with the paper's warning that ISW and lensing add non-primordial correlations (`2003.11544_clean.txt:432-437`). It is therefore only a conditional idealization, not a derived observed-sky prediction.

## 3. The three requested comparisons

### (a) Gaztañaga/BHU model

- `S_1/2`: **undetermined**, with the formal family `A^2 G` above.
- harmonic quadrupole `C_2`: **undetermined**, with the formal family `A F_2` above.
- conditional, extra hard-real-space axiom only: primordial `S_1/2=0 microK^4`; no unique observed `S_1/2` after ISW/lensing and no unique `C_2`.

### (b) Planck measured

Planck defines `S_1/2` as the temperature two-point statistic integrated from 60 to 180 degrees (`../bhu-reading-20260823/sources/1906.02552v2_planck2018_isotropy_clean.txt:2267-2290`). Table 11 gives, in `microK^4`, Commander **1209.2**, NILC **1156.6**, SEVEM **1146.2**, and SMICA **1142.4** (`1906.02552v2_planck2018_isotropy_clean.txt:2416-2431`).

The pinned Planck text does **not** tabulate the measured harmonic quadrupole amplitude `C_2`. It discusses the “low observed value of the quadrupole” and its effect (`1906.02552v2_planck2018_isotropy_clean.txt:2309-2321`), but Table 15's `C_2^{XY}(180 degrees)` is a two-point correlation evaluated at the antipode, not harmonic `C_{ell=2}` (`1906.02552v2_planck2018_isotropy_clean.txt:2451-2483`, with its multipole sum at `:2954-2993`). Accordingly no harmonic Planck `C_2` number is fabricated here.

### (c) standard LambdaCDM benchmark and Planck tail fraction

Planck Table 12 reports the probability of a fiducial-LambdaCDM realization having `S_1/2` at least as large as observed as **>99.9%** for all four temperature maps (`1906.02552v2_planck2018_isotropy_clean.txt:2416-2445`). Equivalently, fewer than **0.1%** of those simulations are at or below the observed value (the finite table precision does not support a smaller exact percentage). The look-elsewhere/global probabilities are 98.8%, 98.8%, 98.8%, and 99.0% (`1906.02552v2_planck2018_isotropy_clean.txt:2451-2470`).

For a reproducible untuned reference number, I evaluated the squared **mean theoretical correlation curve** (not the Monte-Carlo median of `S_1/2`) with CAMB 1.6.0, flat six-parameter values `H0=67.4`, `ombh2=0.0224`, `omch2=0.120`, `tau=0.054`, `A_s=2.1e-9`, `n_s=0.965`, and `l<=250`:

```python
import camb, numpy as np
from scipy.special import eval_legendre
from scipy.integrate import simpson
p=camb.CAMBparams()
p.set_cosmology(H0=67.4, ombh2=.0224, omch2=.120, tau=.054)
p.InitPower.set_params(As=2.1e-9, ns=.965)
p.set_for_lmax(200)
r=camb.get_results(p)
cl=r.get_cmb_power_spectra(p,CMB_unit='muK',raw_cl=True)['total'][:,0]
x=np.linspace(-1,.5,10001)
C=sum((2*l+1)/(4*np.pi)*cl[l]*eval_legendre(l,x)
      for l in range(2,len(cl)))
print(cl[2], 6*cl[2]/(2*np.pi), simpson(C*C,x=x))
```

Output: theoretical `C_2=1070.7007 microK^2`, equivalently `D_2=l(l+1)C_l/(2pi)=1022.4438 microK^2`, and `integral[C_mean(theta)^2] dx = 34916.06 microK^4`. This is a standard-LambdaCDM mean-curve benchmark, not a BHU prediction and not Planck's simulation expectation value `E[S]` (squaring and ensemble averaging do not commute). The pinned Planck paper shows the simulation median graphically but does not tabulate it; its directly greppable expected-distribution statement is the >99.9% tail probability above.

## 4. Threshold, significance, and falsification

There is **no model-derived numerical threshold**. With free `A` and free cutoff transfer/matching, any nonnegative `S_1/2` and `C_2` can be obtained by admissible rescaling/choice of completion. Planck's measured `S_1/2` therefore neither confirms nor contradicts this cutoff model at a calculable significance. The quoted `<0.1%` is a LambdaCDM tail probability, not a BHU likelihood ratio or confirmation significance.

The conditional axiom `C(theta>60 degrees)=0` would be refuted by any statistically significant nonzero **primordial** correlation on that interval, but the papers specify neither an allowed tolerance nor the late-time ISW/lensing distribution needed to turn that into an observed-sky threshold. A calibrated falsifier requires, at minimum: (i) a predicted primordial normalization `A`; (ii) one explicit window `W(k)` including the epoch/meaning of `R`; (iii) bounce-to-adiabatic/isocurvature transfer and phase statistics; and (iv) the late-time observed-temperature transfer/covariance. Supplying these would make `F_l`, `G`, a likelihood, and a refutation threshold computable.

## 5. Absence audit

Patterns searched across all five pinned Gaztañaga papers were case-insensitive variants of `amplitude`, `normalization/normalisation`, `A_s`, `10^-5`, `scale invariant`, `power spectrum`, `P(k)`, `k<`, `cutoff`, `quadrupole`, `multipole`, and `correlation`. One easy-to-miss class was prose rather than equations: “small random amplitude fluctuations,” “let us assume,” “mystery,” and “further work ... estimate the perturbations.” Those hits were inspected, including `sym14101984_clean.txt:93,520,932` and `2204.11608_clean.txt:118,253-260,295,330-340`; none supplies a normalization or unique transfer rule. The Planck source was separately searched for `S1/2`, `quadrupole`, `C2`, and `microK^2`; the apparent `C2` table was checked and identified as an antipodal correlation rather than harmonic `C_{ell=2}`. No other seat result file was read, and no tier was changed.
