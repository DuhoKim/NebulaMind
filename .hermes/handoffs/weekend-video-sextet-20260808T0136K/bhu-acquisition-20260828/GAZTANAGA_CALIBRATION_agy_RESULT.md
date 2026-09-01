UNDETERMINED_NEEDS_SHAPE

### 1. The Exact Cutoff Prescription
The Gaztañaga Black Hole Universe (BHU) model firmly fixes the **location** of the causal horizon cutoff, but its exact mathematical **shape** (e.g., sharp vs. smooth) and the **space** it applies to ($k$-space vs. $\theta$-space) are qualitatively specified and mutually ambiguous:
- **Location fixed**: The cutoff is tied to the causal horizon. "$\chi_{\lx@sectionsign}$ corresponds to an angle $\theta = \chi_{\lx@sectionsign} / d_A \lesssim 1 \text{ rad} \simeq 60 \text{ deg}$" (`2104.00521_clean.txt`:184).
- **Angular-space description**: "Thus, we would expect to see no correlations in the CMB on angular scales $\theta > \theta_{cut} \equiv \chi_{\lx@sectionsign}/\chi_{CMB} \simeq 60$ degrees" (`2003.11544_clean.txt`:415).
- **k-space description**: "The key difference with Inflation is that in the BHU the spectrum of incoming fluctuations have a cutoff for scales larger than $\lambda > 2R$ ($k < \pi/R$)" (`2204.11608_clean.txt`:295).

The model relies on standard cosmology for the small-scale amplitude ("The Big Bounce could also help us understand... the origin for the amplitude $\delta_T \simeq 10^{-5}$" - `2204.11608_clean.txt`:339), but leaves the functional form of the suppression (the "sharp-vs-smooth choice") free.

### 2. The Derivation of $S_{1/2}$ and $C_2$
I evaluated the $S_{1/2}$ statistic and quadrupole $D_2 = 6 C_2 / 2\pi$ using CAMB with standard $\Lambda$CDM parameters, testing different interpretations of the model's cutoff.

**Calculated & Extracted Numbers**:
- **$\Lambda$CDM Expected**: $S_{1/2} \approx 34,913\,\mu\text{K}^4$, with a quadrupole of $D_2 \approx 1022\,\mu\text{K}^2$.
- **Planck Measured** (from `1906.02552v2_planck2018_isotropy_clean.txt`): $S_{1/2} = 1156.6\,\mu\text{K}^4$ (NILC; Table 11). For $\Lambda$CDM, the probability of obtaining such a low $S_{1/2}$ represents a $>99.9\%$ anomaly significance (Table 12).
- **Model Predicted** (dependent on the unsupplied shape assumption):
  1. *If we assume a sharp angular cutoff* ($C(\theta) = 0$ for $\theta > 60^\circ$, per "no correlations"): $S_{1/2} = \int_{-1}^{1/2} C(\theta)^2 d(\cos\theta)$ evaluates **exactly to $0$**, and the surviving quadrupole drops to $D_2 \approx 524\,\mu\text{K}^2$.
  2. *If we assume a sharp comoving cutoff* ($P(k) = 0$ for $k < \pi/R \approx 6/\chi_{CMB}$): Projection effects still leak power to large angles. The script yields $S_{1/2} \approx 6,905\,\mu\text{K}^4$ and $D_2 \approx 476\,\mu\text{K}^2$.
  3. *If we assume a smooth suppression* (e.g., exponential): The predicted $S_{1/2}$ is free to slide anywhere between $0$ and the $\Lambda$CDM baseline depending on the smoothness.

<details>
<summary>Python calculation code (CAMB)</summary>

```python
import numpy as np
import camb
from scipy.integrate import simpson
from scipy.special import lpn

pars = camb.CAMBparams()
pars.set_cosmology(H0=67.4, ombh2=0.0224, omch2=0.120, mnu=0.06, omk=0, tau=0.054)
pars.InitPower.set_params(As=2.1e-9, ns=0.965, r=0)
pars.set_for_lmax(2500, lens_potential_accuracy=0)
results = camb.get_results(pars)
powers = results.get_cmb_power_spectra(pars, CMB_unit='muK')
cl_TT_lcdm = powers['total'][:,0]

def get_ctheta(cl, theta_deg):
    x = np.cos(np.radians(theta_deg))
    val = 0.0
    for l in range(2, min(len(cl)-1, 1000)+1): 
        if cl[l] == 0: continue
        Cl_true = cl[l] * 2 * np.pi / (l * (l + 1))
        val += (2*l + 1) / (4 * np.pi) * Cl_true * lpn(l, x)[0][-1]
    return val

def get_S12(cl):
    xs = np.linspace(-1, 0.5, 500)
    C_th = np.array([get_ctheta(cl, t) for t in np.degrees(np.arccos(xs))])
    return simpson(C_th**2, x=xs)

chi_cmb = results.conformal_time(0) - results.tau_maxvis
print(f"LCDM S1/2 = {get_S12(cl_TT_lcdm):.2f} muK^4, D2 = {cl_TT_lcdm[2]:.2f}")

# Sharp k-space cutoff
pars_trunc = pars.copy()
ks = np.logspace(-5, 1, 10000)
Pk = np.where(ks > np.pi / (chi_cmb * np.pi / 6), 2.1e-9 * (ks / 0.05)**(0.965 - 1), 1e-30)
pars_trunc.set_initial_power_table(ks, Pk)
cl_trunc_k = camb.get_results(pars_trunc).get_cmb_power_spectra(pars_trunc, CMB_unit='muK')['total'][:,0]
print(f"Sharp k-cutoff S1/2 = {get_S12(cl_trunc_k):.2f}, D2 = {cl_trunc_k[2]:.2f}")

# Sharp theta-space cutoff
xs_th = np.linspace(-1, 1, 1000)
C_th = np.array([get_ctheta(cl_TT_lcdm, t) for t in np.degrees(np.arccos(xs_th))])
C_th[np.degrees(np.arccos(xs_th)) > 60] = 0.0
C2_true = 2 * np.pi * simpson(C_th * [lpn(2, x)[0][-1] for x in xs_th], x=xs_th)
print(f"Sharp theta-cutoff D2 = {C2_true * 6 / (2 * np.pi):.2f}")
```
</details>

### 3. The Threshold and the Verdict
- **Verdict**: `UNDETERMINED_NEEDS_SHAPE`
- **Threshold & Refutation**: Because the mathematical form of the cutoff is missing, a unified prediction for $S_{1/2}$ cannot be uniquely derived without fabricating assumptions. If the model were forced to adopt a sharp $k$-space cutoff, the predicted $S_{1/2} \approx 6,905\,\mu\text{K}^4$ would be robustly refuted by the Planck measurement ($1156\,\mu\text{K}^4$). Conversely, if forced to a strict angular cutoff, the prediction of exactly $0$ is accommodated by the data. Because the "sharp-vs-smooth" and "$k$ vs $\theta$" choices are free, the model's prediction for $S_{1/2}$ is free to slide.

### 4. Absence Claim
- **Pattern**: Searched using `grep -iE "P\(k\)|spectrum|power|shape|sharp|smooth|Heaviside|exponential|break"` across all Gaztañaga sources.
- **One missed class**: Specific mathematical equations or functional forms outlining the cutoff's behavior (e.g., $P(k) \propto 1 - e^{-k/k_c}$).
- **What I did about it**: I manually read the surrounding context in `2003.11544`, `2104.00521`, and `2204.11608`. I verified that the authors only apply qualitative descriptors ("a cutoff", "no correlations", "anomalous lack") and strictly omit any formal prescription for the cutoff's shape or the surviving power's normalization.
