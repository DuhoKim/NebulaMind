NEW_FALSIFIER_CANDIDATE

# RQ-B Derivation: Popławski Torsion-Bounce Transfer Function

## 1. Assembled Field Equations
Popławski defines the interior of the collapsing parent black hole as a closed FLRW universe ($k=1$), undergoing a bounce due to the Einstein-Cartan spin-torsion coupling.
From Entry 11 (`1410.3881`, Eqs. 10 and 11), the torsion-modified Friedmann equations are:
$$ \frac{\dot{a}^2}{c^2} + k = \frac{1}{3}\kappa(\epsilon - \alpha n_f^2)a^2 $$
$$ \frac{\dot{a}^2 + 2a\ddot{a}}{c^2} + k = -\kappa(p - \alpha n_f^2)a^2 $$
where $\epsilon$ is the standard energy density, and $\alpha n_f^2 \propto a^{-6}$ is the negative, repulsive effective energy density introduced by the spin-torsion coupling of the fermions. This yields an effective density $\rho_{\text{eff}} = \epsilon - \alpha n_f^2$ and effective pressure $p_{\text{eff}} = \epsilon/3 - \alpha n_f^2$.

## 2. Derivation of the Transfer Function $T(k)$
Let the input parent perturbation (from the collapsing star) be parameterized by the uniform-density curvature perturbation $\zeta_{\text{in}}(k)$. 
- **Pre-bounce collapse:** The parent star forms an event horizon at $a_i \sim 2GM/c^2$, entering a closed contracting FLRW phase. Super-horizon modes ($k \ll aH$) remain conserved or grow logarithmically.
- **Bounce matching:** The spin fluid behaves dynamically like a negative stiff-matter fluid ($w_{\text{eff}} \to 1$ near the bounce, $\rho_{\text{eff}} \to 0$). Because the effective pressure $p_{\text{eff}}$ is uniquely defined by the fermion number density $n_f$ (meaning the non-adiabatic pressure perturbation $\delta p_{\text{nad}} = 0$), the super-horizon curvature perturbation $\zeta$ is strictly conserved across the bounce. The growing mode of the contracting phase matches onto the constant mode of the expanding phase without divergence. Thus, the transfer function across the bounce is $T(k) = \zeta_{\text{out}}(k) / \zeta_{\text{in}}(k) \approx 1$.
- **Post-bounce expansion:** The daughter universe undergoes a torsion-dominated accelerated expansion phase.

## 3. Amplitude Verdict (Finite Signature Survives)
A **finite, parent-dependent signature survives** to observable scales because the torsion bounce *fails to provide enough inflationary e-folds to dilute the classical parent input.*
Popławski explicitly calculates the extent of this accelerated phase. In Entry 9 (`1007.0587`), he states that during the accelerating period ($\ddot{a}>0$), the universe expands only by a factor of $\sqrt{2}$. In Entry 11 (`1410.3881`), with particle production included, the expansion is larger ($\sim 10^{10}$), but this is still only $\sim 23$ e-folds. 

Because $N_{\text{torsion}} \ll 60$, the classical, super-horizon inhomogeneities of the parent star (e.g., its rotation, density gradients, or multipole moments) are **not** stretched beyond the observable horizon. They remain well within the causal patch of the daughter universe CMB. Therefore, the transfer function $T(k) \approx 1$ yields a finite, measurable amplitude at observable scales (such as a preferred axis, bulk flow, or low-$\ell$ anomalies on the CMB), serving as a new falsifier candidate for the model.
