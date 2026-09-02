AUDIT_FLAG_MEMBERSHIP

## 1. The setup and the derivation

The paper starts from the maximally extended, eternal Schwarzschild geometry, not from a model of our observed cosmology. It identifies the white-hole quadrant as a Kantowski–Sachs spacetime with spatial topology \(\mathbb R\times S^2\): the past singularity is at \(r=0\), the past horizon at \(r=2GM\), and the metric is rewritten with two anisotropic scale factors \(a(\tau)\) and \(r(\tau)\) (lines 95–98, 113–142). Near the singularity the metric has Kasner exponents \((-1/3,2/3,2/3)\), so one direction contracts and the two-sphere expands (lines 192–219).

The scalar calculation itself is mostly derived in the paper. For a real, massless, test scalar with negligible backreaction (lines 247–251), the authors perform a spherical-harmonic reduction, derive the canonical action and mode equation, and identify the Regge–Wheeler effective potential (lines 253–299). They then Fourier-decompose the extended direction and derive the reduced equation (lines 318–325). Near \(r=0\), this becomes a Bessel/Hankel equation with solution coefficients \(C_1(\omega),C_2(\omega)\) (lines 331–345); canonical quantization yields \(|C_2|^2-|C_1|^2=\pi/4\) in that normalization (lines 369–383).

The horizon Bogoliubov calculation is explicit rather than merely cited: the paper defines the \(a\)- and \(b\)-mode bases (lines 444–453, 475–498), evaluates the Fourier/contour integrals (lines 519–551), obtains \(|\alpha|^2=e^{2\pi\tilde\omega/\kappa}|\beta|^2\), and hence the Planck occupation factor (lines 553–565, 616–643). Appendix A independently reproduces the transformation by the Klein–Gordon inner product (lines 857–899). Prior literature is cited for the Regge–Wheeler equation and standard Hawking/QFT machinery (lines 287–310, 315–316, 861–869), but the coefficients used here are worked out.

The weak point is the propagation approximation, not the algebra of the near-horizon Bogoliubov factor. The full mode equation cannot be solved analytically; the authors say the near-singularity Hankel solution is only “qualitatively valid” over the whole interval despite unspecified intermediate-region modifications (lines 331–347). They drop the \(\ell(\ell+1)\) term and effectively set \(\ell=0\) on asymptotic dominance grounds (lines 312–313), then neglect the exterior Regge–Wheeler barrier for sufficiently high frequency (lines 426–430, 608–610, 649–650). The paper itself concedes that realistic scattering was omitted, expects the result only for high-frequency modes, and says the general spectrum acquires a greybody factor (lines 852–853). Backreaction is assumed negligible, not tested (lines 247–251). The claim that the result “will be easily extended” to other spins is asserted at lines 247–250; a spin-dependent potential is written at lines 301–310, but no full electromagnetic or tensor calculation is carried through. A massive test field is not analyzed.

There is also a normalization-presentation blemish: Section 3 gives the vacuum choice \(C_2=\sqrt\pi/2\) (lines 375–386), whereas Section 5 calls \(C_1=0,C_2=1\) the vacuum choice (lines 755–760). The later spectrum evidently uses rescaled coefficients satisfying the unit normalization implicit in Eq. (92), but that rescaling is not explained in the prose. This does not reverse the sign of the added term, but it weakens confidence in its quoted absolute normalization.

## 2. The result and what fixes it

For the chosen vacuum initial condition, the exterior observer obtains

\[
n_{\tilde\omega}=\frac{1}{e^{2\pi\tilde\omega/\kappa}-1},\qquad
T_H=\frac{\kappa}{2\pi}=\frac{1}{8\pi GM},
\]

as derived at lines 627–647. For the general non-vacuum state, the derived occupation spectrum is

\[
n_{\tilde\omega}=\frac{1}{e^{2\pi\tilde\omega/\kappa}-1}
+|C_1(\tilde\omega)|^2\coth\!\left(\frac{\pi\tilde\omega}{\kappa}\right),
\]

with the equivalent form involving both \(|C_2|^2\) and \(|C_1|^2\) at lines 819–830; the summary repeats the additive departure at lines 846–850.

Conditional on the setup, its sign is fixed: the correction is nonnegative because it is \(|C_1|^2\) times a positive \(\coth\) for positive frequency. Its existence and magnitude are not fixed by geometry. \(C_1(\omega)\) is an arbitrary, frequency-dependent initial-state choice subject only to normalization; \(C_1=0\) restores the exact Planck spectrum (lines 375–383, 755–774, 827–830). Thus geometry fixes the thermal kernel and the positive sign conditional on a non-vacuum occupation, while the vacuum state fixes whether any departure exists and its size. The reported formula is for a massless test field, effectively the s-wave/high-frequency regime; angular-mode scattering and greybody factors modify the received spectrum (lines 247–250, 312–313, 649–650, 852–853).

## 3. Does this describe our universe?

The sentences bearing directly on that question point away from such a claim:

- The abstract says the white-hole interior is “like an anisotropic cosmological background” and that its past singularity “play[s] the role of a big bang singularity,” immediately specifying that the calculation is in “an eternal Schwarzschild manifold” (line 19). These are analogy and coordinate/causal-role statements, not an identification with our universe.
- The introduction says a black-hole interior is “like a cosmological background” and reviews separate proposals replacing black-hole interiors by de Sitter space (lines 25–31). It then says the white-hole past singularity “behaves as the onset of big bang singularity” and calls the perturbation question natural by analogy with FLRW structure formation (lines 33–38).
- Most decisively: “the WHs are not stable and have disappeared in early universe so the current analysis may not be directly relevant to observable Universe.” The authors then state what they actually assume: “we treat WH as part of an eternal BH manifold which exists along with BH as required by the time reversal symmetry of general relativity,” and characterize the exercise as a nontrivial example of QFT in curved backgrounds (lines 40–42).
- The global-geometry section repeats: “the WH is unstable and may not exist in current observable Universe”; in their treatment it exists only as “an integral part of the full manifold” of an eternal black hole (lines 95–98).
- The perturbations are explicitly generated at the white-hole past singularity and propagate across its past horizon to exterior future null infinity; the complete Cauchy data also include modes from left and right past null infinity (lines 109–111, 315–316). That global scattering construction is an eternal Schwarzschild manifold, not a one-universe origin model.
- The FLRW comparison is expressly analogical: the authors say their interpretation is “quite similar” to primordial fluctuations and “represent[s] an anisotropic cosmological background” (lines 327–351). The summary again says the white-hole singularity is “like a big bang singularity” (lines 832–835).
- The paper even calls the second exterior region of the Kruskal extension the “other universe” in quotation marks (lines 651–657), reinforcing that “universe” here is standard extended-Schwarzschild terminology rather than a claim about our observed universe.

Accordingly, “plays the role of a big bang” is no more than a geometric analogy: a past spacelike singular boundary in an anisotropic interior. The paper nowhere claims that our Big Bang is this singularity, that our universe is inside a black hole, or that observations of our universe test the construction.

## 4. Base-layer membership (report only)

On the stated corpus definition, this paper does not make or test the identification “our universe is the inside of a black hole.” Its object is instead quantum-field propagation from the white-hole quadrant of an eternal Schwarzschild manifold to an exterior observer (lines 19, 33–42, 95–110, 315–316). Its own phrases are “like an anisotropic cosmological background,” “may not be directly relevant to observable Universe,” and “a non-trivial example of quantum field theory in curved backgrounds” (lines 19, 40–42). The explicit subject is a white hole, not our universe, and the measured observable is Hawking flux at Schwarzschild future null infinity, not a cosmological observable.

I therefore flag it as family-adjacent white-hole QFT and recommend that Duho adjudicate removal from the base layer or relocation to support/context. Per the brief, this is a membership report, not a membership decision, and it does not itself change the tier.

## 5. Tier consequence

**CONSISTENCY-ONLY holds.** The paper derives a directional, nonnegative excess over Planck form only after an arbitrary non-vacuum initial state is chosen. Because \(C_1(\omega)\) is free and \(C_1=0\) yields no excess, neither the departure's presence nor magnitude is a geometry-only prediction (lines 381–383, 755–774, 827–830). The calculation supplies no calibrated observational target, uncertainty model, source population, detector mapping, or exclusion threshold. Its high-frequency/s-wave and no-scattering approximations further prevent promotion (lines 426–430, 649–650, 852–853).

A null observation cannot contradict the model: it is compatible with the vacuum choice \(C_1=0\), with frequency-dependent choices making the excess arbitrarily small, with greybody/scattering effects, and—by the authors' own statements—with white holes being unstable or absent from the observable universe (lines 40–42, 95–98, 827–830, 852–853). Hence it is not QUALITATIVE-DIRECTIONAL in the corpus sense, because the sign is conditional rather than an unavoidable prediction for our universe; it is not a PROSPECT because no concrete observational program is developed; and it is not a CALIBRATED-FALSIFIER because no null can exclude the free-state construction.

In plain language: the paper does a recognizable Hawking-radiation calculation in the white-hole half of an eternal Schwarzschild spacetime, and a deliberately excited initial state adds a positive, state-dependent excess to the thermal spectrum. But that excess is optional, its size is freely chosen, realistic propagation is simplified, and the authors explicitly say the setup may not apply to the observable universe. Most importantly for this corpus, the paper never says that our universe is inside a black hole; it treats the white-hole interior as cosmology-like. The consistency-only tier therefore survives, while the paper's base-layer membership should be decided by Duho.
