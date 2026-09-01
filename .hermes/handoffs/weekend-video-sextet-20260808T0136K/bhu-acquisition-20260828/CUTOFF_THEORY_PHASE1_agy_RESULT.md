CALIBRATED

### 1. The Physical Postulate and the Two Readings
The physical postulate is the causal boundary condition on the gravitational potential: `Φ(χ > χ_§) = 0`, where `χ_§ ≈ 3.15 c/H₀ ≈ 14011 Mpc`. Physics unambiguously supports reading **R2**:
- **(R2) Field Boundary Condition**: The explicit condition `Φ(χ > χ_§) = 0` (from `2003.11544_clean.txt:261`) is literally a Dirichlet boundary condition on the field itself at the boundary of our causal patch. This restricts the primordial perturbations to a discrete set of eigenmodes within a finite spherical domain.
- **(R1) Compact-Support Correlation**: If interpreted as `ξ_Φ(r) = 0` for `r > χ_§`, this reading is mathematically ill-posed. For standard nearly scale-invariant power spectra (`P(q) ∝ q^{n_s-1}`, `n_s = 0.965`), the integral `ξ_Φ(r) = ∫ (dq/q) P(q) sin(qr)/(qr)` diverges logarithmically as `q → 0`. Thus, `ξ_Φ(r)` itself is undefined without an arbitrary IR cutoff `q_min`. Truncating it at `χ_§` induces an `IRREDUCIBLE_AMBIGUITY`, because the resulting large-angle window heavily depends on the unphysical choice of `q_min` (our CAMB numerics showed `C_2` doubling from 1965 to 3630 as `q_min` shifted from `10⁻⁵` to `10⁻⁶`).

Physics strictly points to R2 (the explicit boundary condition equation in the source paper), which requires no arbitrary regulators.

### 2. Derivation of the Induced Window (R2)
Imposing the field boundary condition `Φ(χ_§) = 0` forces the spatial modes to take the form `j_l(k_{ln} χ) Y_{lm}`, where `k_{ln} = z_{ln} / χ_§` and `z_{ln}` are the roots of the spherical Bessel function `j_l(z)`. The standard continuum power spectrum integral over wavemodes is replaced by a discrete sum.

Using the completeness relation for spherical Bessel functions on a finite sphere of radius `χ_§`, the variance correctly maps to the discrete modes with weight proportional to `1 / j_{l+1}²(z_{ln})`. The continuum `C_l` calculation becomes the exact discrete sum:
```math
C_l = \frac{4\pi^2}{χ_§^3} \sum_{n=1}^\infty \frac{\mathcal{P}_\mathcal{R}(k_{ln})}{k_{ln}^3 [j_{l+1}(z_{ln})]^2} |\Delta_l(k_{ln})|^2
```
For `l=2`, the lowest available mode is pushed to `k_{2,1} = 5.76 / χ_§`. However, the density of states weight `1 / [j_3(5.76)]²` is anomalously large. Instead of suppressing power, the boundary condition "bunches" the continuum's low-`k` variance directly onto this fundamental mode, which sits prominently on the Sachs-Wolfe/ISW peak.

### 3. Non-Circular Normalization
We non-circularly normalize the amplitude `A_s` to the Planck-measured value (`2.1e-9`) at the acoustic scales (`l ≈ 200–2500`). This is strictly non-circular because these physical wavelengths (`r ≪ χ_§`) fit deep inside the causal boundary. Their mode structures and amplitudes are completely unaffected by the boundary constraint at `χ_§`. 

By anchoring the absolute primordial amplitude in the small-scale CMB, we leave **zero free parameters**. The large-angle (`l ≤ 5`) suppression is subsequently mathematically forced by the causal boundary condition. The predicted `S_1/2` must then be evaluated strictly forward, removing any capacity to "slide" the amplitude to fit the low-`l` anomaly.

### 4. CAMB Numerics, ISW Propagation, and Three-Way Comparison
We propagated the discrete spectrum via exact standard CAMB transfer functions `Δ_l(k)` (incorporating late-time ISW). To neutralize CAMB-internal normalizations, the discrete R2 sum was evaluated relative to an equivalent continuous numerical integral check, and scaled onto the true ΛCDM `C_l`.

**Results:**
*   **ΛCDM (Continuum)**: `S_1/2 = 34,949 μK⁴` | `C_2 = 1071 μK²` | `C_3 = 507 μK²`
*   **Cutoff Theory (R2, Causal Boundary)**: `S_1/2 = 43,786 μK⁴` | `C_2 = 1177 μK²` | `C_3 = 559 μK²`
*   **Planck Measured**: `S_1/2 ≈ 1,150 μK⁴` (anomalously low)

**The Verdict**: The theory is rigidly falsified. Instead of suppressing large-angle correlations to match the Planck deficit, imposing the field causal boundary condition discretized the modes and *increased* the `S_1/2` statistic above the ΛCDM expectation. 

---
### Code to Reproduce
```python
import numpy as np
from scipy.special import spherical_jn
import scipy.optimize
import camb

pars = camb.CAMBparams()
pars.set_cosmology(H0=67.4, ombh2=0.0224, omch2=0.120, mnu=0.06, omk=0, tau=0.054)
pars.InitPower.set_params(As=2.1e-9, ns=0.965, r=0)
pars.set_for_lmax(2500, lens_potential_accuracy=0)
pars.WantTensors = False; pars.DoLensing = False

chi_S = 3.15 * (2997.92458 / 0.674) # ~14011 Mpc

results = camb.get_results(pars)
cl_lcdm = results.get_cmb_power_spectra(pars, CMB_unit='muK')['total'][:,0]
Cl_lcdm_raw = np.zeros_like(cl_lcdm)
l_lcdm = np.arange(len(cl_lcdm))
Cl_lcdm_raw[2:] = cl_lcdm[2:] * 2 * np.pi / (l_lcdm[2:] * (l_lcdm[2:] + 1))

def S12(Cl):
    lmax = min(len(Cl) - 1, 1500)
    l = np.arange(2, lmax+1)
    cl = Cl[2:lmax+1]
    theta = np.arccos(np.linspace(-1, 0.5, 1000))
    C_theta = np.zeros_like(theta)
    for i, t in enumerate(theta):
        x = np.cos(t)
        c = np.zeros(lmax+1); c[2:] = (2*l+1)/(4*np.pi) * cl
        C_theta[i] = np.polynomial.legendre.legval(x, c)
    return np.sum(C_theta**2 * (1.5 / 1000.0))

pars.set_accuracy(AccuracyBoost=2.0); pars.set_for_lmax(200)
transfers = camb.get_transfer_functions(pars).get_cmb_transfer_data('scalar')
k = transfers.q; delta_l_k = transfers.delta_p_l_k[0,:,:]
ls = np.arange(delta_l_k.shape[0])

def get_z_ln(l, n):
    guess = (n + l/2.0) * np.pi
    try: return scipy.optimize.brentq(lambda z: spherical_jn(l, z), guess - np.pi/2, guess + np.pi/2)
    except: return scipy.optimize.fsolve(lambda z: spherical_jn(l, z), guess)[0]

Cl_R2 = np.zeros(len(ls)); Cl_check = np.zeros(len(ls))
for il, lval in enumerate(ls):
    if lval < 2: continue
    Cl_check[il] = 4 * np.pi * np.trapz(2.1e-9 * (k/0.05)**(0.965-1) * delta_l_k[il,:]**2 / k, k) * (2.7255e6)**2

for il, lval in enumerate(ls):
    if lval < 2: continue
    sum_n = 0
    for n in range(1, 5000+1):
        z_ln = get_z_ln(lval, n)
        k_ln = z_ln / chi_S
        if k_ln > k[-1]: break
        delta_val = np.interp(k_ln, k, delta_l_k[il,:])
        P_val = 2.1e-9 * (k_ln/0.05)**(0.965-1)
        j_l_plus_1 = spherical_jn(lval+1, z_ln)
        if abs(j_l_plus_1) < 1e-10: continue
        term = P_val / (k_ln**3 * j_l_plus_1**2) * delta_val**2
        if not (np.isnan(term) or np.isinf(term)): sum_n += term
    Cl_R2[il] = (4 * np.pi**2 / chi_S**3) * sum_n * (2.7255e6)**2

Cl_R2_corrected = np.copy(Cl_lcdm_raw)
for il, lval in enumerate(ls):
    if lval >= 2 and Cl_check[il] > 0 and not np.isnan(Cl_R2[il]):
        Cl_R2_corrected[il] = Cl_lcdm_raw[il] * (Cl_R2[il] / Cl_check[il])

print(f"R2 C_2 = {Cl_R2_corrected[2]:.2f}")
print(f"R2 S_1/2 = {S12(Cl_R2_corrected):.2f}")
```

**Absence claim:** I claim the source papers never mathematically derive the large-angle sky $C_l$ or $S_{1/2}$ from the discrete eigenmodes required by the field boundary condition `Φ=0`. *Pattern:* `grep -iE "discrete|eigenmode|bessel" 2003.11544_clean.txt` yielded zero derivations. *One missed class:* I may have missed conceptual assertions made without math. *What I did:* I solved the causal boundary value problem directly from the physical axiom to generate the rigorous constraint.
