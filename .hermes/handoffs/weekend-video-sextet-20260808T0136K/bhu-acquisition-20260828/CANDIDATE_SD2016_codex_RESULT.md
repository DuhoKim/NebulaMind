UNDETERMINED_NEEDS_DERIVED_TORSION_SPECTRUM

## 1. The chain

The background chain is partly derived and partly assumed.

- ECSK spin-fluid equations give the effective density and pressure, \(\tilde\epsilon=\epsilon-\alpha n_f^2\) and \(\tilde p=p-\alpha n_f^2\) (paper lines 80–87), and the closed-FLRW Friedmann equation (99–109). The radiation/spin-fluid inputs are \(g_b=28\), \(g_f=90\), and the assumption of a closed, homogeneous, isotropic universe (88–98).
- Particle production is not derived from QFT in Riemann–Cartan spacetime: the paper says it “should be derived” there, but assumes \(K=\beta(\kappa\tilde\epsilon)^2\) following earlier work (116–130). This assumption plus the Friedmann equations yields the temperature/scale-factor relation (paper Eq. 7, lines 195–216), the bound \(\beta<\beta_{cr}\), and \(\beta_{cr}=1/929.0915\) for Standard Model particles (212–218).
- For chosen initial data, Eqs. 3–4 are solved numerically for \(a(t),H(t),T(t)\) (259–286). The benchmark is \(\beta=1/929.25\), \(a_0=10^{-27}\) m, and \(T_0=0.99T_{max}\) (262–275); it gives about 60 e-folds and an approximately constant \(H\) until \(1.33\times10^{-42}\) s (275–286).
- The Ellis–Madsen construction is then an equation-level reconstruction of a *different*, canonical scalar-field system with the same background: Eqs. 10–11 map \(a,H,\dot H\) to \(V(t)\) and \(\dot\phi^2(t)\) (307–326), integration gives \(\phi(t)\) and hence \(V(\phi)\) (336–340), and Eqs. 12–15 define its slow-roll parameters (321–340). Eqs. 16–18 then assign the usual single-field slow-roll \(n_s,r,\alpha_s\) (343–354).

That last assignment is not a computation of perturbations in the torsion universe. The paper acknowledges the gap unusually clearly: it says the required calculation is of “quantized perturbations of the torsion field,” defers that calculation to a future publication, and instead constructs a scalar potential with the same scale-factor dynamics so standard scalar-field fluctuations can be used (283–306). It also emphasizes that there is no fundamental scalar and calls reconstruction a mathematical technique for calculating \(n_s\) and \(r\) (73–93). Equal homogeneous background histories do not by themselves imply equal quadratic actions, vacuum states, sound speeds, scalar/tensor normalizations, or evolution through the bounce. Justification would require deriving and quantizing the gauge-invariant scalar, vector, and tensor perturbations of the ECSK spin fluid plus particle-production sector, specifying initial conditions/vacuum and matching through the bounce, and demonstrating that their power spectra reduce to those of the reconstructed canonical scalar.

## 2. Inputs and freedom

- **Particle production:** \(K=\beta(\kappa\tilde\epsilon)^2\) is assumed; \(\beta\) is a dimensionless free coefficient that the authors say ultimately should come from quantum gravity (116–130, 436–441). Expansion requires \(0<\beta<\beta_{cr}\); values slightly below critical yield near-exponential but finite expansion, while \(\beta\ge\beta_{cr}\) is eternal (218–255). The benchmark ratio is \((1/929.25)/(1/929.0915)=929.0915/929.25=0.9998294\), giving about 60 e-folds. The conclusion reports about 60–150 e-folds depending on \(\beta\) (444–456), but the text/captions do not print a numerical \(\beta\) interval for “more than 60” or for Planck consistency; Figs. 8–11 encode the scan graphically (397–420).
- **Relativistic content:** \(g_b=28\), \(g_f=90\), so \(g_*=g_b+(7/8)g_f=106.75\); the particle-production continuity equation separately uses \(g_{n1}=9\) (88–96, 112–129). These are fixed Standard Model choices, not scanned.
- **Bounce data:** \(a_0=10^{-27}\) m is motivated by an electron Cartan radius; \(T_0=0.99T_{max}\), with dynamics said insensitive to the exact \(T_0\) when it is near \(T_{max}\) (259–273). The abstract’s “minimal dependence” is borne out only as a numerical sensitivity statement: Figs. 8–11 vary \(a_0,\beta\); the authors report little change with \(a_0\), but sensitivity to \(\beta\) (397–433). It is not independence from all bounce physics.
- **Reference epoch:** numerical time is set to \(t=0\) at the last/Big Bounce (247–252, 275–282). Observables are evaluated \(N\) e-folds before the end of the reconstructed inflationary phase.
- **Horizon exit:** \(N\) is not predicted. The paper notes the conventional 50–60 range, a literature lower limit of 18, and adopts the broad scan \(18\le N\le60\), promising model-specific bounds later (356–368). For the initial-condition scan it fixes \(N=20\) (397–411).

The outputs therefore are functions of both the free \(\beta\) and the uncalibrated horizon-exit choice \(N\), not definite predictions. At the displayed benchmark, \(n_s\approx0.96\) for \(N\approx20\)–25, but \(n_s\approx0.99\) for \(N=50\)–60 (369–380): this is a wide, observationally consequential band, not a narrow number. Across the \(a_0,\beta\) scan at \(N=20\), the paper prints \(r\simeq0.01\)–0.03 and \(\alpha_s<0\) with \(|\alpha_s|=O(10^{-3}\!-
10^{-4})\), and states that \(n_s,r,\alpha_s\) depend mainly on \(\beta\) (408–433). Table I’s printed 0.965 is a value of \(\beta/\beta_{cr}\) giving three bounces—not \(n_s\) (228–238).

## 3. Numbers versus Planck 2018

Planck 2018 gives \(n_s=0.9649\pm0.0042\) (68%, base power-law spectrum; Planck lines 1818–1831). Thus:

- At \(N\sim20\)–25, the paper’s \(n_s\approx0.96\) differs by \(-0.0049\), or \(1.17\sigma\): LIVE.
- At \(N=50\)–60, \(n_s\approx0.99\) differs by \(+0.0251\), or \(5.98\sigma\): FIRED for that part of its stated \(N\)-range under the base Planck comparison.
- The scanned \(r\approx0.01\)–0.03 is below Planck 2018’s combined \(r_{0.002}<0.058\) (95%; Planck lines 3118–3134), hence numerically LIVE. This is only an approximate comparison because the paper quotes/plots \(r\) against a \(k=0.05\,\mathrm{Mpc}^{-1}\) bound (381–390), whereas the pinned Planck limit is at \(0.002\,\mathrm{Mpc}^{-1}\), and the paper supplies no torsion tensor tilt for a pivot conversion.
- The paper’s \(\alpha_s\sim-10^{-3}\) to \(-10^{-4}\) is consistent with Planck’s \(dn_s/d\ln k=-0.0045\pm0.0067\): the differences are 0.0035–0.0044, only 0.52–0.66\(\sigma\) (paper 389–394, 424–430; Planck lines 3038–3074).

So the *borrowed reconstructed-scalar numbers* are LIVE for the low-\(N\) region and FIRED by \(n_s\) for the conventional 50–60 region. The ECSK model’s own perturbation prediction remains unscorable because neither \(N\) nor the torsion-universe spectra are derived.

## 4. Warrant

The ECSK-plus-particle-production mechanism produces the nonsingular/accelerating background; it does not, in this paper, produce the advertised CMB falsifier. The numerical \(n_s,r,\alpha_s\) are borrowed from a canonical inflaton chosen to reproduce only that background (paper lines 283–326). A lane-owned threshold cannot repair this: the missing item is a **NUMBER-generating derivation**—the torsion universe’s scalar and tensor spectra and their transfer—not merely a threshold against which an existing mechanism-owned number can be calibrated. The lane may report conditional scalar-surrogate arithmetic, but may not promote it into an ECSK prediction.

## 5. Tier proposal

**UNDETERMINED_NEEDS_DERIVED_TORSION_SPECTRUM.** This is stronger and more precise than CANDIDATE_PROSPECT: the paper gives a concrete background and an explicit surrogate calculation, but the claimed falsifier lacks mechanism ownership. It is not CANDIDATE_CALIBRATED_FALSIFIER because no calibration can supply the absent torsion perturbation spectrum; not CANDIDATE_QUALITATIVE_DIRECTIONAL because even the red tilt is established only for the reconstructed scalar; and not CANDIDATE_CONSISTENCY_ONLY because background equivalence does not test perturbative consistency. Conditional standing of the surrogate is LIVE around \(N\sim20\)–25 and FIRED around \(N=50\)–60, with \(r\) and running individually LIVE, but standing for the torsion universe itself is unscorable.

In plain language: the paper convincingly shows that a narrowly chosen particle-production rate can make the torsion-bounce background expand like inflation, then finds an ordinary scalar-field model that expands the same way. It calculates the scalar model’s CMB numbers, not the torsion universe’s. Some of those proxy numbers still fit Planck 2018, while the usual 50–60-e-fold choice gives a scalar tilt about six standard deviations too high. Until the actual torsion perturbations are derived and carried through the bounce, these are useful diagnostics but not a falsifiable prediction of the proposed mechanism.
