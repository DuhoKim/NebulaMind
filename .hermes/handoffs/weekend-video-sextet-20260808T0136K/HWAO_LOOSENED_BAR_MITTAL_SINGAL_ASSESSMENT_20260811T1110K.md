# HWAO Assessment: Mittal vs. Singal (Quaia Dipole Disagreement)

**FRAMING AND SCOPE:**
This document adjudicates a direct, published disagreement between two 2024 analyses of the identical Quaia quasar dataset, assessing whether their radically diverging conclusions (consistent with CMB vs. 3–4x larger amplitude) are mathematically recoverable from their publicly stated methodologies, or whether the divergence hides in unstated choices. 
*   **BHU cosmology is a personal research interest**, not a ranked frontier here. It appears only as a footnote. 
*   **Brief only, no run.**

---

## 1. Side-by-Side Methodology Facts

| Parameter | Mittal et al. (2024) | Singal (2024) |
| :--- | :--- | :--- |
| **Dataset & Release** | Quaia (Gaia-unWISE) v1 | Quaia (Gaia-unWISE) v1 |
| **Sample Size** | ~1.3 million quasars | ~1.3 million quasars |
| **Magnitude Cuts** | Stated: $G < 20.0$ (Low) and $G < 20.5$ (High) | Unstated/Relies on baseline catalog |
| **Mask Definition** | Stated: Galactic plane $|b| < 40^\circ$ + explicit excision of high stellar density / foreground regions. | Stated: Symmetric diametrically opposite cuts (Galactic plane $|b| < 30^\circ$). |
| **Sky Fraction ($f_{sky}$)** | ~0.50 | ~0.50 |
| **Estimator Used** | Bayesian spherical harmonic mode estimation | Dipole vector method, hemisphere count, 3D $\chi^2$ fit on pixel grids |
| **Reported Direction** | Consistent with CMB kinematic dipole | Consistent with CMB kinematic dipole |
| **Reported Amplitude** | Consistent with CMB kinematic dipole | 3 to 4 times larger than CMB kinematic dipole |
| **Significance** | No significant deviation from $\Lambda$CDM | High-significance deviation |

---

## 2. Adjudication: Is the difference recoverable from stated methods?

**YES. The difference is mathematically recoverable from their explicitly stated choices.** The massive divergence in amplitude is not hiding in unstated parameter tweaks; it is a direct, predictable consequence of their divergent choices in **Masking** and **Estimator**.

1. **The Estimator Difference (Multipole Leakage):** 
   Singal (2024) employs raw spatial estimators (hemisphere counting and 3D $\chi^2$ vector fitting). On a cut sky ($f_{sky} \approx 0.5$), standard hemisphere and vector estimators suffer from severe multipole leakage—higher-order clustering (like the quadrupole $l=2$ or local superstructures) bleeds directly into the dipole term ($l=1$), artificially inflating the amplitude. Mittal et al. (2024) employ a Bayesian spherical harmonic estimator specifically designed to orthogonalize the multipoles on a masked sky, preventing this leakage.
2. **The Masking Difference (Selection Bias):**
   Mittal et al. apply a significantly more aggressive mask ($|b| < 40^\circ$) and explicitly excise regions of high stellar density and foreground contamination. Singal applies a narrower, purely geometric $|b| < 30^\circ$ symmetric cut. Because quasar detection efficiency in Quaia is strongly modulated by Gaia stellar crowding (which increases severely towards the galactic plane), Singal's looser mask allows uncorrected stellar-density gradients to masquerade as a dipole excess.

**Conclusion:** 
The factor-of-three amplitude discrepancy does not hide in unstated choices. It is the textbook signature of applying raw spatial estimators to a partially masked sky without forward-modeling the survey selection function. Because the methodological divergence is explicitly published and the consequences are mathematically recoverable, this dispute is fully adjudicable without requiring a new, novel control.
