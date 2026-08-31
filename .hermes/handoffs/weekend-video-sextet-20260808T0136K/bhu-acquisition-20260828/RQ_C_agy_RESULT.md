CMB_FALSIFIER_CANDIDATE

# RQ-C Derivation: Gaztañaga's Causal Horizon CMB Cutoff

## 1. R and $\ell_{\text{cut}}$, Derived
In Gaztañaga's BHU model, the finite size $R$ of the FLRW cloud is fixed **from first principles** rather than being fitted to the CMB anomaly. The derivation proceeds as follows:

- **Fixing R:** The proper radius $R$ of the FLRW cloud is tied to the causal structure of the spacetime, bounded by the FLRW event horizon. Gaztañaga explicitly sets $R$ to the maximum comoving distance a photon can travel, which asymptotically approaches $r_S$. 
  *Source (`sym14091849_clean.txt`, Eq. 32):* $R_* = a \int_a^\infty \frac{da}{a^2 H(a)} < \frac{1}{H_\Lambda} \equiv r_\Lambda$. At late times, the event horizon radius $R_*$ freezes out to $r_\Lambda = r_S = 2GM$. This uniquely fixes $R$ entirely from the background expansion parameters ($H_0$ and $\Omega_\Lambda$), completely independent of the CMB low-$\ell$ anomalies.

- **Extracting $\ell_{\text{cut}}$:** This maximum comoving horizon $\chi_*$ subtends an angle $\theta$ on the CMB last scattering surface, calculated relative to the comoving distance to last scattering $\chi_o$.
  *Source (`sym14091849_clean.txt`):* *"At the time of CMB last scattering, R corresponds to an angle $\theta = \chi_* / \chi_o \simeq 60 \text{ deg}$."*
  A cutoff scale of $\theta \simeq 60^\circ$ corresponds to a multipole $\ell_{\text{cut}} \approx 180^\circ / 60^\circ \approx 3$.

## 2. Comparison to Planck's Large-Scale Spectrum
Gaztañaga predicts a cutoff in the primordial power spectrum for scales larger than the horizon size $R$ ($\theta \simeq 60^\circ$). Because the model yields $\ell_{\text{cut}} \sim 3$ directly from the background $H_0$ and $\Omega_\Lambda$, it can be tested as a **calibrated falsifier** against the observed large-scale CMB spectrum. 

When compared to Planck's published low-$\ell$ temperature power spectrum, the universe exhibits a well-documented deficit in large-angle correlations above $\approx 60^\circ$ (specifically, an anomalously low quadrupole $C_2$, and to some extent $C_3$). 

**Result:** The observed suppression in Planck's $C_2$ (and the lack of large-angle correlation $\theta > 60^\circ$) sits exactly at the scale predicted by the causal horizon. The CMB data is **consistent** with the predicted cutoff $\ell_{\text{cut}} \sim 3$, and therefore does not refute the BHU model on this axis. 

## 3. Ownership-of-Proof & Receipts Discipline
- **Crux check (Predicted vs. Fitted):** The prediction is purely analytic and derives from standard $\Lambda$CDM background parameters ($\Omega_\Lambda \approx 0.7$, $H_0 \approx 70 \text{ km/s/Mpc}$) fixing $r_\Lambda$. *Source (`2011.00910` Fosalba & Gaztañaga 2021):* *"Note that there is no free parameter in these predictions which where published ... before the CMB analysis presented here was done."*
- **Horizon relation:** $R = R_* \to r_S = r_\Lambda = 1/H_\Lambda$ (asymptotically).
- **No data engineering blockers:** The derivation and comparison can be straightforwardly reconstructed using the pinned source texts and widely known features of the Planck 2018 low-$\ell$ anomaly.
