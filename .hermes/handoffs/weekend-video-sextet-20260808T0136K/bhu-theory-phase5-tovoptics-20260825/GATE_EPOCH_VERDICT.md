# VERDICT: NEITHER IS DETERMINED BY THE PINNED MODEL

## Ruling

The pinned geometry and junction orbit determine the exterior energy density at each crossing event,

\[
\bar\rho_s(\eta)=v(\eta)\rho_{\rm FRW}(\eta),
\]

but they do **not** determine a temperature field. Therefore neither

\[
T_s\propto \bar\rho_s^{1/4}
\]

nor

\[
\frac{d\ln T_s}{d\eta}=\frac{w}{1+w}\frac{d\ln\bar\rho_s}{d\eta}
\]

follows from the pinned material alone. The location of the dipole null is an irreducible modelling ambiguity until a thermodynamic/radiative closure is added.

This is not resolved by the fact that \(\bar r\) is timelike.

## What locus is sampled when the crossing direction varies?

Equation (3.1), together with \(A=1-N<0\) in (3.5), makes \(\bar r\) the timelike coordinate in the exterior TOV region. Because the perfect fluid is comoving with this metric and every metric/fluid scalar depends only on \(\bar r\), an exterior fluid worldline has fixed \((\bar t,\theta,\phi)\) and changing \(\bar r\), with normalized radial velocity

\[
u^{\bar r}=\pm\sqrt{N-1}.
\]

That statement does **not** identify all events having different \(\bar r\) as one fluid element. Equality of a timelike coordinate is no substitute for equality of the three labels \((\bar t,\theta,\phi)\) that identify a comoving worldline.

For one observer event, the sight lines form the observer's past light cone. Their boundary crossings form the two-dimensional cut of that null cone by the shock worldtube. For an off-centre observer, \(\eta\) varies over this cut. Distinct directions normally have distinct angular labels and hence meet distinct exterior fluid worldlines. Moreover, the shock is not a material/comoving surface: pinned equation (4.5) gives its nonzero speed relative to the FRW-side fluid, and the entropy branch has \(\sigma-u>0\). Successive events on a shock generator therefore also cannot simply be identified as the history of one fluid element.

Thus the sampled locus is a generally spacelike two-surface of events on a timelike shock worldtube, populated by a family of distinct fluid elements. It is not one exterior fluid worldline parametrized by \(\eta\).

The timelike role of \(\bar r\) still has an important but different consequence: by the TOV symmetry, all comoving exterior worldlines share the same scalar profiles \(\bar\rho(\bar r)\) and \(\bar p(\bar r)\). Geometry therefore makes a common thermal history *possible* if a common thermodynamic closure and common entropy normalization are imposed. It does not supply either one.

## Why (a) is not implied

The relation \(\bar\rho=a_{\rm rad}T^4\) is a constitutive law for equilibrium blackbody radiation. For that same component it comes with \(\bar p=\bar\rho/3\). Applying \(T\propto\bar\rho^{1/4}\) to the total exterior perfect-fluid density while independently imposing \(\bar p=w\bar\rho\) for arbitrary \(w\) is not a consequence of local anchoring; it is an additional, and generally inconsistent, identification unless \(w=1/3\).

Construction (a) can be made legitimate only by specifying a radiation component separately, for example

\[
\rho_{\rm rad}(\eta)=f_{\rm rad}(\eta)\bar\rho_s(\eta),\qquad
T_s=(\rho_{\rm rad}/a_{\rm rad})^{1/4},
\]

with the fraction \(f_{\rm rad}\) and its evolution supplied by microphysics. The pinned equations do not provide that fraction.

## Why (b) is not implied

For a simple fluid in local thermal equilibrium with vanishing chemical potential, Gibbs-Duhem gives

\[
dp=s\,dT,\qquad \rho+p=Ts.
\]

Combining these with \(p=w\rho\), constant \(w\), yields

\[
d\ln T=\frac{w}{1+w}d\ln\rho.
\]

Equivalently, an isentropic conserved-particle fluid gives this power law only after a common adiabat/composition and its normalization have been fixed. Those are thermodynamic assumptions beyond metric (3.1), field equations (3.2)-(3.4), condition (3.5), and the Rankine-Hugoniot orbit. A perfect-fluid stress tensor and a barotropic mechanical equation of state specify \(p(\rho)\), not uniquely \(T(\rho)\). Chemical potential, particle density, entropy per particle, composition, and shock entropy production remain absent.

Also, using \(\eta\) in the differential equation does not turn the sky cut into one material history. Construction (b) is valid across the sampled events only if the exterior is additionally declared to be one LTE, isentropic, constant-\(w\) fluid with the same thermodynamic normalization on all relevant comoving worldlines. TOV symmetry is compatible with that declaration, but the pinned model does not make it.

## Correct construction

Introduce and evolve a local source variable independently of the mechanical junction orbit. At minimum one must specify either:

1. a thermodynamic fundamental relation \(\bar\rho=\bar\rho(n,s)\), particle/current conservation, entropy production at the shock, composition/chemical potentials, and a normalization; or
2. a radiation distribution/source function (or a separately conserved radiation energy density) with its emission, absorption, and coupling to the exterior matter.

Then evaluate that local field at each crossing event \(x_s(\hat n)\):

\[
T_s(\hat n)=T\!\left(x_s(\hat n)\right),
\]

rather than treating the direction-dependent values of \(\eta\) as automatically belonging to one material trajectory.

With the extra assumption of one common zero-chemical-potential isentrope, the result specializes to **(b)**. With the extra assumption that the relevant energy density is equilibrium radiation, it specializes to **(a)** and simultaneously fixes that component's \(w=1/3\). For generic imposed \(w\), the pinned record selects neither.

## Consequence for the null

The existence of cancellation in both calculations is untouched. Its location is not a prediction of the pinned geometry. Quoting either \(w=0.0408\) or \(w=0.0815\) as the physical escape point would silently choose an unpinned thermal closure. The publishable result at the present gate is therefore: **the null exists, but its location is thermodynamic-model dependent and presently undetermined.**
