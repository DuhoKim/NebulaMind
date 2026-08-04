# T2a Conversion Tables & Machinery

## 1. Mass-Convention Conversions (IMF/SED)
To homogenize stellar masses ($M_*$) across diverse catalogs to a single Chabrier (2003) IMF:
- **Salpeter to Chabrier**: $\log(M_{*,\text{Chabrier}}) = \log(M_{*,\text{Salpeter}}) - 0.24$
- **Kroupa to Chabrier**: Treated as equivalent ($\Delta \log M_* \approx 0$).
- SED fitting assumptions (e.g., Prospector vs. FAST) introduce systematic scatter. An explicit $+0.15$ dex systematic uncertainty is added to the stellar mass error budget for cross-survey mass homogenization if derived using different SPS codes.

## 2. Te-Scale Relations
For Class C (strong-line) objects, they must be converted to the $T_e$-anchored scale.
- **Conversion Equation**: Adopted from empirical $T_e$-strong line recalibrations (e.g., Sanders+ 2024 or equivalent high-z anchor derivations) explicitly declared per survey.
- **0.24 dex Te-vs-strong-line O/H class**: All Class C objects converted via strong-line diagnostics inherit a mandatory $\pm 0.24$ dex scale uncertainty term added in quadrature to their statistical error.
- **0.15 dex per-anchor Te-scale class**: All Class A (direct $T_e$) objects inherit a $\pm 0.15$ dex scale uncertainty term.

## 3. UV-vs-Optical Channel Separation (F3)
- **Channels**: 
  - Optical: $[OIII] \lambda 5007 / \lambda 4363$, $[NII]$
  - UV: $OIII] \lambda 1666$, $CIII]$
- **Cross-Channel Systematic**: Per §4.2, any comparison mixing UV and optical derivations must include a $\pm 1.4$ dex systematic term for N/O or C/O ratios, and a conservatively bounded offset term for O/H unless a specific empirical cross-calibration is cited. If absent, channels strictly do not mix.

## 4. Lensing-Inheritance Fields (F1)
- For the $10^{5.7} M_\odot$ low-mass lensed samples (e.g., GLASS/UNCOVER), the catalog must declare magnification $\mu$.
- **Propagation**: $\sigma_{\log M_*}^2 = \sigma_{\text{phot}}^2 + \sigma_{\log \mu}^2$.
- Objects without declared $\mu$ and $\sigma_\mu$ are flagged as `cluster-line-of-sight` and excluded from the main MZR.
