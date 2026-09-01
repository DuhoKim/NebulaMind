STILL_AMBIGUOUS_IR_NORMALIZATION

# Route A — maximum-entropy completion

## Result

The stated constraints do **not** define a maximum-entropy covariance. With the causal condition interpreted as compact support of the equal-time correlation, the entropy objective is unbounded under the natural (asymptotic) meaning of small-scale agreement. Under exact agreement with a power law on an open high-\(k\) interval, compact support and the measured spectrum are instead incompatible. The original flux condition is weaker still: it constrains the background causal scale but not the perturbation covariance.

Consequently Route A induces no unique primordial window \(W(k)\), and hence no Route-A values of \(C_\ell\), \(S_{1/2}\), or \(C_2\). Supplying such numbers requires an extra IR normalization/trace, reference measure, discretization, or a chosen window. None is fixed by maximum entropy plus the causal condition. Choosing any of them from the Planck low-\(\ell\) deficit would be circular.

## Causal constraint adopted

I used the strongest natural covariance reading suggested in the brief,

\[
 \xi_\Phi(r)=0\quad(r>L),\qquad
 L=\chi_{\mathsection}=3.15\,c/H_0=14019.391964\ {\rm Mpc}.
\]

This is stronger than the source's flux/boundary statement. If even this version does not close the determinant problem, the flux statement—which the brief says imposes no constraint on perturbation covariance—cannot do so.

For a statistically homogeneous isotropic field,

\[
 \xi(r)=\int_0^\infty {dk\,k^2\over2\pi^2}P(k)j_0(kr),
 \qquad
 P(k)=4\pi\int_0^L dr\,r^2\xi(r)j_0(kr).
\]

The requested window would be \(W(k)=P(k)/P_{\rm ss}(k)\), where \(P_{\rm ss}\) is fixed by the high-\(\ell\) values \(A_s=2.100549\times10^{-9}\), \(n_s=0.9649\), and \(k_*=0.05\,{\rm Mpc}^{-1}\). The constraints do not determine this ratio.

## Proof that the maximum does not exist

Assume one feasible compact-support covariance \(\xi_0\) exists under the intended asymptotic condition

\[
 {P_0(k)\over P_{\rm ss}(k)}\longrightarrow1\quad(kL\to\infty).
\]

Choose any nonzero smooth radial function \(g\in C_c^\infty(B_{L/2})\), and define its autocorrelation

\[
 q(\mathbf r)=\int d^3x\,g(\mathbf x)g(\mathbf x+\mathbf r).
\]

Then \(q(r)=0\) for \(r>L\), and it is positive definite because

\[
 Q(k)=\widetilde q(k)=|\widetilde g(k)|^2\ge0.
\]

Since \(g\) is smooth and compactly supported, \(Q(k)\) decreases faster than every inverse power. Thus, for every \(\lambda\ge0\),

\[
 \xi_\lambda=\xi_0+\lambda q,
 \qquad P_\lambda=P_0+\lambda Q
\]

is a valid covariance, has the same support bound, and has the same measured high-\(k\) asymptote. Yet on any finite regulator/grid containing a mode with \(Q_i>0\),

\[
 \log\det\Sigma_\lambda
   =\sum_i\log(P_{0,i}+\lambda Q_i)\longrightarrow+\infty.
\]

There is therefore no determinant-maximizing member and no induced window. The continuum expression adds another unresolved choice: differential entropy/log determinant depends on the mode measure and UV/volume regulator. Maximum entropy is not invariant to that missing reference measure.

If “reproduces measured \(P(k)\)” is read as **exact equality** on an open interval \(k>K\), the alternative is not uniqueness. Compact support makes the Fourier transform analytic (Paley–Wiener). Equality on an open interval fixes its analytic continuation, whereas the dimensional nearly scale-invariant spectrum \(P_{\rm ss}(k)\propto k^{n_s-4}\) is not an entire compact-support transform. Hence the exact constraint set is empty (apart from replacing the measured spectrum by a separately specified analytic approximation). Also, an analytic \(Q(k)\) cannot vanish on an open high-\(k\) interval without vanishing identically.

## CAMB calculation and non-circular normalization

CAMB 1.6.0 was run with the brief's high-\(\ell\) normalization only:

~~~python
import camb
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import eval_legendre

p = camb.CAMBparams()
p.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.1200,
                mnu=0.06, omk=0, tau=0.0544)
p.InitPower.set_params(As=2.100549e-9, ns=0.9649,
                       pivot_scalar=0.05)
p.set_for_lmax(300, lens_potential_accuracy=0)
p.DoLensing = True
p.NonLinear = camb.model.NonLinear_none
r = camb.get_results(p)  # transfer includes ordinary SW, Doppler, and ISW
cl = r.get_lensed_scalar_cls(CMB_unit='muK', raw_cl=True,
                             lmax=300)[:, 0]

x, w = leggauss(1600)
mu, wt = 0.75*x - 0.25, 0.75*w
C = sum((2*l+1)*cl[l]*eval_legendre(l, mu)/(4*np.pi)
        for l in range(2, 301))
print(np.sum(wt*C*C), cl[2])
~~~

Reproducible output for the unmodified small-scale-normalized ΛCDM reference is

\[
 S_{1/2}^{\Lambda{\rm CDM}}=34940.1404\ \mu{\rm K}^4,
 \qquad C_2^{\Lambda{\rm CDM}}=1071.0933\ \mu{\rm K}^2.
\]

This agrees with the brief's rounded ΛCDM comparison \(S_{1/2}\simeq34900\ \mu{\rm K}^4\). The Planck comparison supplied in the brief is \(S_{1/2}\simeq1150\ \mu{\rm K}^4\). Route A has no third numerical entry: \(S_{1/2}^{\rm maxent}\) and \(C_2^{\rm maxent}\) are undefined because \(W(k)\) is undefined. Running an arbitrarily selected member \(P_\lambda\) through CAMB would quantify that selection, not maximum entropy.

## Falsifiability threshold

No measured \(S_{1/2}\) threshold, and therefore no sigma-level rejection rule, exists for this underconstrained route. Its admissible covariance family is not an ensemble with a specified hyperprior; maximum entropy supplies neither an IR normalization nor probabilities over the free functions. A threshold becomes definable only after adding and fixing such information independently of low-\(\ell\) CMB data. That is a new model assumption, not a consequence of the Phase-1 Route-A constraints.

## Verdict

STILL_AMBIGUOUS_IR_NORMALIZATION: the missing input is an independently fixed IR variance/trace (together with a continuum reference measure or equivalent finite regulator). Without it, log det is unbounded; with exact high-\(k\) equality, the compact-support constraint is incompatible rather than calibrating a solution.
