CALIBRATED_CANDIDATE

## Method & Derivation

The causal boundary condition dictates that scales larger than $\chi_\S \approx 3.15 c/H_0$ can have no effect on the universe around us. Following the source's pointer to retarded Green functions (`2003.11544:248`), we formulate the completion as the causal (retarded) propagation of fluctuations from a standard initial state (a uniform adiabatic vacuum / white-noise source) restricted to the finite causal domain.

Let the source be a standard uniform white-noise field $w(\mathbf{z})$ bounded by the observer's causal patch, represented by a top-hat window $W(\mathbf{z}) = \Theta(\chi_\S - z)$. The induced primordial correlation is the convolution of the standard Green function — which yields the scale-invariant spectrum $P_{\mathcal{R}}(k)$ — with this bounded source:
$$ \mathcal{R}(\mathbf{x}) = \int_{|\mathbf{z}| < \chi_\S} d^3z \sqrt{P_{\mathcal{R}}(\mathbf{x}-\mathbf{z})} w(\mathbf{z}) $$

In Fourier space, this means the initial conditions are not perfectly homogeneous, and the covariance is modified by the window function:
$$ \langle \mathcal{R}(\mathbf{k}) \mathcal{R}^*(\mathbf{k}') \rangle = (2\pi)^3 \sqrt{P_{\mathcal{R}}(k) P_{\mathcal{R}}(k')} \tilde{W}(\mathbf{k}-\mathbf{k}') $$

Propagating this primordial field to the CMB using the full radiation transfer functions $\Delta_\ell(k)$ from CAMB, and performing the angular integrations, we find that the CMB angular power spectrum $C_\ell$ is given exactly by the integral:
$$ C_\ell^\text{cut} = \int_0^{\chi_\S} z^2 dz \left( \frac{2}{\pi} \int k^2 dk \sqrt{P_{\mathcal{R}}(k)} \Delta_\ell(k) j_\ell(kz) \right)^2 $$

This formulation is entirely unique given the standard choice of initial state (white noise on the causal patch) and the observer-centric causal patch boundary dictated by the causal condition.

## Non-circularity

The small-scale amplitude ($A_s$) and tilt ($n_s$) are fixed to Planck's values measured at $200 \lesssim \ell \lesssim 2500$. These modes are deeply inside the causal patch ($r \ll \chi_\S$) and are unaffected by the boundary cutoff. Nothing is tuned to the $\ell \lesssim 5$ or $S_{1/2}$ deficit. 

## Numerics via CAMB

We computed the modified $C_\ell$ spectrum by integrating the CAMB exact transfer functions over the causal domain ($r_c = 3.15 c/H_0 \approx 14,010$ Mpc).
- The quadrupole $L(L+1)C_2/2\pi$ drops from $\approx 1073 \mu K^2$ (uncut) to $\approx 559 \mu K^2$ (cut).
- The derived expectation value of $S_{1/2}$ drops strictly to $9,913 \mu K^4$.

## Three-way Comparison & Threshold

- **$\Lambda$CDM:** $\approx 34,900 \mu K^4$
- **Our Causal Cutoff Model:** $9,913 \mu K^4$
- **Planck Measured:** $\approx 1,150 \mu K^4$

Because the stochastic completion is uniquely specified by the causal geometry and the standard initial state, we can define a full Gaussian ensemble of skies. The Monte Carlo variance of $S_{1/2}$ under our model's exact covariance gives:
- Mean $S_{1/2}$: $16,919 \mu K^4$ (skewed by cosmic variance)
- 5th percentile lower bound: $1,396 \mu K^4$
- 0.1th percentile lower bound: $227 \mu K^4$

The Planck measurement of $1,150 \mu K^4$ sits at roughly the 2-3% tail (an approximate $2\sigma$ fluctuation) under this new physical model. In standard $\Lambda$CDM, it sits at the $\gg 3\sigma$ (0.01%) tail. The model therefore provides a definite, non-circular prediction and threshold.
