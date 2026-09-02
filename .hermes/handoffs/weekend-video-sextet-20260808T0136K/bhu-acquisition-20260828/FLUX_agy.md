F1=FLUX_ALPHA F2=FLUX_GAMMA

**1. Linearised Flux Functional**
Adopting the $+---$ metric signature used in the source paper (where $u^\mu u_\mu = 1$), the energy-momentum tensor is $T^\mu_\nu = (\rho+p)u^\mu u_\nu - p\delta^\mu_\nu$. Working in a standard choice like synchronous gauge, the 4-velocity time components are unperturbed at linear order ($u^0 = u_0 = 1$, thus $\delta u^0 = \delta u_0 = 0$). This yields $T^0_0 = \rho \implies \delta T^0_0 = \delta \rho$, and the trace $T = \rho - 3p \implies \delta T = \delta \rho - 3\delta p$. From the Einstein field equations, $R^0_0 = 8\pi G(T^0_0 - \frac{1}{2}T) - \Lambda$, we find the linearised Ricci component is:
$\delta R^0_0 = 8\pi G \left(\delta \rho - \frac{1}{2}(\delta \rho - 3\delta p)\right) = 4\pi G(\delta \rho + 3\delta p)$
Varying the flux functional $\Phi = -\int_M \sqrt{-g} R^0_0 d^4x$ to linear order, we obtain:
$\delta\Phi[\delta] = -\int_{M_\S} \left[ \sqrt{-\bar{g}} \left( 4\pi G(\delta \rho + 3\delta p) \right) + \delta(\sqrt{-g}) \left( 4\pi G(\bar{\rho} + 3\bar{p}) - \Lambda \right) \right] d^4x$
This explicitly demonstrates that the fluid term is $4\pi G(\delta \rho + 3\delta p)$ at linear order.

**2. Reading F1**
Under reading F1, $\delta\Phi[\delta] = 0$ provides exactly one scalar constraint centered on our observer's causal volume $M_\S$. When we decompose the spatial perturbation field around the observer into spherical harmonics $Y_{\ell m}(\hat{n})$, the angular integration over the spherically symmetric region $M_\S$ acts as a projector $\int Y_{\ell m}(\hat{n}) d\Omega = \sqrt{4\pi}\delta_{\ell 0}\delta_{m 0}$. Therefore, exactly only the $(\ell=0, m=0)$ mode enters the integral $\delta\Phi$.
Because this constraint uniquely restricts the monopole, it leaves all higher modes ($\ell \ge 1$) completely unconstrained. Consequently, the CMB angular power spectrum $C_\ell$ for $\ell \ge 1$ is exactly unchanged. Because the large-scale anomaly statistic $S_{1/2}$ depends purely on $C_\ell$ for $\ell \ge 2$, $S_{1/2}$ is also exactly unchanged.
**Symmetry argument:** The flux integral over a spherically symmetric region is a rotationally invariant linear functional (a spin-0 scalar singlet). The perturbation field decomposes into coefficients $a_{\ell m}$ that transform under the spin-$\ell$ representations of the rotation group $SO(3)$. By Schur's Lemma (or the Wigner-Eckart theorem), a rotationally invariant functional must transform trivially and therefore can only possess a non-zero overlap with the singlet representation. Mathematically, it must couple exclusively to the $\ell=0$ mode and cannot couple to the transformations of any $\ell \ge 1$ modes.

**3. Reading F2**
Under reading F2, the condition applies to all observers, forming a spatial convolution $(W \star \delta)(x) = 0$ for all $x$, where $W$ is the compactly supported window of $M_\S$. Taking the Fourier transform gives $\tilde{W}(k) \tilde{\delta}(k) = 0$ for all $k$, which implies $\tilde{\delta}(k)$ can only be non-zero at the specific wave-vectors $k$ where $\tilde{W}(k) = 0$. 
For a compactly supported spherically symmetric window, the **Paley-Wiener theorem** guarantees that its Fourier transform $\tilde{W}(k)$ is an entire analytic function. Because the zero set of a non-trivial entire function cannot have an accumulation point on the real axis, the zeros of $\tilde{W}(k)$ form an isolated set (a set of measure zero).
Since $\tilde{\delta}(k)$ is forced to vanish almost everywhere in $k$-space, no continuous power spectrum $P(k)$ is compatible with this condition, except for the trivial vacuum solution $P(k) = 0$.

**4. Classification**
- F1 solely constrains the unobservable $\ell=0$ monopole and preserves all $C_\ell$ ($\ell \ge 1$), thus it is classed as **FLUX_ALPHA**.
- F2 permits only a measure-zero set of frequencies and rejects any continuous power spectrum, thus it is classed as **FLUX_GAMMA**.

**5. Sanity Check**
For a 3D spherical top-hat window of radius $R$ (normalized such that its volume integral is 1), the Fourier transform in closed form is:
$\tilde{W}(k) = \frac{3}{(kR)^3} [\sin(kR) - kR \cos(kR)]$
The zeros are given by the transcendental equation $\tan(kR) = kR$. The first two positive zeros occur at:
$kR \approx 4.4934$
$kR \approx 7.7253$

The proposed causal flux condition fundamentally fails to provide a physical mechanism to suppress the large-scale anomalies observed in the cosmic microwave background. If we interpret the condition as applying uniquely to our own observer, its strict spherical symmetry guarantees it only adjusts the unobservable background average (the "monopole") of the universe, leaving the actual fluctuations and the $S_{1/2}$ statistic completely untouched. Conversely, if we require the condition to hold universally for all observers, it imposes a mathematically pathological constraint: because a finite spatial window cannot entirely block a continuous band of frequencies without destroying all others, enforcing this condition everywhere forces the universe to have absolutely no continuous primordial fluctuations at any scale. Neither interpretation yields the desired tailored cutoff of large-scale power.
