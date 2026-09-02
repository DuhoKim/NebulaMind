F1=FLUX_ALPHA F2=FLUX_GAMMA

## 1. Linearised flux

I use conformal Newtonian gauge,
\[
 ds^2=a^2(\eta)\{(1+2\Psi)d\eta^2-(1-2\Phi_N)[dr^2+r^2d\Omega^2]\}.
\]
(The symbol \(\Phi_N\) is a metric potential, not the flux.) To first order,
\[
 \sqrt{-g}=a^4(1+\Psi-3\Phi_N),\qquad
 \delta\sqrt{-g}=a^4(\Psi-3\Phi_N).
\]
Let the spherically symmetric four-window be represented by a fixed background
indicator/weight \(U_\S(\eta,r)\). From Eq. (16),
\[
 \Phi(M_\S)=-\int d^4x\,U_\S\sqrt{-g}\,R^0{}_0.
\]
The mixed-index Einstein equation in the conventions of the brief is
\[
 R^\mu{}_\nu=8\pi G\left(T^\mu{}_\nu-
 \frac12\delta^\mu{}_\nu T\right)-\Lambda\delta^\mu{}_\nu.
\]
For a perfect fluid at linear order, \(T^0{}_0=\rho\) (a velocity contribution is
quadratic), while \(T=\rho-3p\). Therefore, step by step,
\[
 R^0{}_0=8\pi G\left[\rho-\frac12(\rho-3p)\right]-\Lambda
 =4\pi G(\rho+3p)-\Lambda,
\]
and, with fixed \(\Lambda\),
\[
 \delta R^0{}_0=4\pi G(\delta\rho+3\delta p).
\]
Expanding the product in the flux and subtracting the background gives
\[
 \boxed{\delta\Phi[\delta]=-
 \int d^4x\,U_\S\left\{a^4,4\pi G(\delta\rho+3\delta p)
 +a^4(\Psi-3\Phi_N)\,\bar R^0{}_0\right\}},
\]
where
\[
 \bar R^0{}_0=4\pi G(\bar\rho+3\bar p)-\Lambda.
\]
This is the requested linear functional for any spherical radial and temporal
profile \(U_\S\). Its split into density, pressure, and volume-element pieces is
gauge dependent, as expected for perturbations, but the perturbation of the
geometrically specified full flux is gauge invariant when the window/boundary is
transformed with the geometry. The displayed formula is its Newtonian-gauge
representation; fixing a coordinate window in different gauges would instead
define different functionals.

## 2. F1: one observer-centred window

Define the scalar integrand perturbation
\[
 q(\eta,r,\Omega)=4\pi G(\delta\rho+3\delta p)
 +(\Psi-3\Phi_N)\bar R^0{}_0
 =\sum_{\ell m}q_{\ell m}(\eta,r)Y_{\ell m}(\Omega).
\]
Because \(U_\S\) and the background measure have no angular dependence,
\[
 \int d\Omega\,Y_{\ell m}=\sqrt{4\pi}\,\delta_{\ell0}\delta_{m0}.
\]
Consequently
\[
 \delta\Phi=-\sqrt{4\pi}\int d\eta\,dr\,r^2a^4
 U_\S(\eta,r)q_{00}(\eta,r).
\]
Thus \(\delta\Phi=0\) is one weighted scalar constraint on the \((\ell,m)=(0,0)\)
part only. No \(\ell\geq1\) coefficient enters.

The same conclusion follows without coordinates. Let a linear spherical
functional acting on sky coefficients have the form
\(L=\sum_{\ell m}b_{\ell m}a_{\ell m}\). Under a rotation,
\(a_{\ell m}\mapsto\sum_{m'}D^{(\ell)}_{mm'}a_{\ell m'}\), whereas spherical
symmetry demands \(L\mapsto L\) for every rotation. Hence \(b_\ell\) must be an
invariant vector of the irreducible \(\ell\) representation. Such a vector exists
only for the trivial representation \(\ell=0\); therefore \(b_{\ell m}=0\) for
all \(\ell\geq1\).

It follows that this condition supplies no modification of the CMB anisotropy
coefficients and
\[
 C_\ell^{\rm F1}=C_\ell^{\rm unconstrained}\quad(\ell\geq1).
\]
In particular, with
\[
 C(\theta)=\sum_{\ell\geq2}\frac{2\ell+1}{4\pi}C_\ell
 P_\ell(\cos\theta),\qquad
 S_{1/2}=\int_{-1}^{1/2}d\mu\,[C(\arccos\mu)]^2,
\]
one has \(S_{1/2}^{\rm F1}=S_{1/2}^{\rm unconstrained}\). The classification is
therefore **FLUX_ALPHA**.

## 3. F2: the condition at every centre

Write the universal condition as
\[
 (W\star\delta)(\mathbf x)=\int d^3y\,W(\mathbf x-\mathbf y)
 \delta(\mathbf y)=0\quad\hbox{for every }\mathbf x,
\]
where \(\delta\) denotes the relevant time-projected scalar combination above.
Fourier transformation converts convolution into multiplication:
\[
 \boxed{\widetilde W(\mathbf k)\widetilde\delta(\mathbf k)=0
 \quad\hbox{for every }\mathbf k.}
\]
Hence \(\widetilde\delta(\mathbf k)\) can have support only where
\(\widetilde W(\mathbf k)=0\).

For a compactly supported spherical \(W\), \(\widetilde W(\mathbf k)=\widetilde
W(k)\). By the Paley-Wiener theorem its Fourier transform extends to an entire
analytic function (and it is not identically zero for a nonzero window). The
identity theorem for analytic functions then makes its radial zeros isolated.
In three-dimensional \(\mathbf k\)-space the zero set is therefore a discrete
union of spherical shells (possibly including an isolated origin), a set of
Lebesgue measure zero.

An ordinary continuous power spectrum compatible with the condition must vanish
off those shells. The complement is dense, so continuity also forces it to
vanish on every shell. Thus
\[
 \boxed{P(k)\equiv0}
\]
is the only compatible continuous spectrum. Nonzero distributional power
concentrated on delta-function shells is possible, but is not a continuous
spectrum and cannot give the observed smooth acoustic spectrum. F2 is therefore
**FLUX_GAMMA**, not a cutoff or suppression with a computable modified \(C_\ell\).

## 4. Mandatory top-hat check

For \(W(r)=1\) at \(r\leq R\) and zero otherwise,
\[
 \widetilde W(k)=4\pi\int_0^Rdr\,r^2\frac{\sin kr}{kr}
 =\frac{4\pi}{k^3}[\sin(kR)-kR\cos(kR)]
 =\frac{4\pi R^3}{3}\frac{3j_1(kR)}{kR}.
\]
Its positive zeros obey \(\tan x=x\), \(x=kR\). The first two are
\[
 kR=4.493409\ldots,\qquad kR=7.725252\ldots.
\]

In plain language, applying the flux rule once around us merely fixes one
spherically averaged number, so it cannot select or suppress any CMB anisotropy
multipole. Applying the same rule around every possible observer is far stronger:
it eliminates every smooth, nonzero perturbation spectrum, leaving at most
singular waves on isolated Fourier shells. Neither reading generates a physical
large-angle CMB cutoff.
