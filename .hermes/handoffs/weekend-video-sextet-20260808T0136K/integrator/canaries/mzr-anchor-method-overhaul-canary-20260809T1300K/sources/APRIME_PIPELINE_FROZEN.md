# A-Prime Pipeline Freeze

## Components (per Ruling 1 requirement A'-2)
- **Te relation & atomic data**: Izotov et al. (2006) empirical relations. Atomic data from PyNeb v1.1.18.
- **Ionization-correction scheme**: ICF(O) = 1 (assumes $O/H = O^+/H^+ + O^{++}/H^+$).
- **Dust law**: Cardelli, Clayton, & Mathis (1989) $R_V = 3.1$. Balmer decrement used if $H\alpha/H\beta$ available, otherwise source-published $A_V$.
- **Electron-density treatment**: Assumed $n_e = 100 \text{ cm}^{-3}$ (typical high-z star-forming).
- **Auroral S/N floor**: $S/N \ge 5$ on the auroral line flux.
- **Uncertainty propagation**: Monte Carlo with fixed seed (`42`) and draw count (`1000`).

## Pipeline Script
Versioned as `te_pipeline.py`. No per-source tweaks allowed; consumes only source-published inputs.
