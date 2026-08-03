# P1 Massive-Galaxy Mechanical Audit - Cross-Review

## 1. Output Parsing & Structure
All Kun outputs (`CUMULATIVE_DENSITY_LEDGER.csv`, `SYSTEMATIC_BUDGET_LEDGER.csv`, `KUN_VERDICT.md`, `QUERY_COVERAGE.json`, `SIMULATION_COMMENSURABILITY.md`, `SOURCE_ROLE_AUDIT.md`, `RECEIPT.json`) were parsed.
- **Row Counts:** 6 cumulative density rows, 8 systematic budget rows.
- **Required Fields:** All CSV fields exist (e.g., `source_role`, `poisson_error`, `direct_count_vs_integration_status`). 
- **Internal Links:** References to `input/served-p1.pdf` and public IDs are correctly formatted.

## 2. Numeric Arithmetic & Locations
The two distinct shift quantities (0.28 dex and 0.20 dex) are mechanically sound based on the stated slope $|s|=1.58$:
- **0.28 dex:** TNG $N=15$, $n=1.11 \times 10^{-5}$ Mpc$^{-3}$ (aperture $2 \times R_{\text{half}}$). Observed $\sim 3 \times 10^{-5}$. Ratio is $\sim 2.7\times$. $\Delta \log M_* = \log_{10}(2.7) / 1.58 = 0.272 \approx 0.28$ dex. Found in: Figure 1 arrow annotation (stale).
- **0.20 dex:** TNG $N=20$, $n=1.47 \times 10^{-5}$ Mpc$^{-3}$ (all-bound total mass). Observed $\sim 3 \times 10^{-5}$. Ratio is $2.04\times$. $\Delta \log M_* = \log_{10}(2.04) / 1.58 = 0.196 \approx 0.20$ dex. Found in: Abstract, Results, Caption, Conclusion.

## 3. Cumulative-Density Row Counts
- **Explicit direct support for `n(>Mstar)`:** 0 observed rows. (The draft uses indirect differential SMF/Schechter fits).
- **Simulation predictions:** 3 rows (CD1, CD2, CD3).
- **Indirect inputs / candidates / gap rows:** 3 rows (CD4 [Weibel SMF], CD5 [Labbé candidates], CD6 [Boylan-Kolchin analytic HMF]).

## 4. Population Separation
Populations are critically mixed in the systematic budget. While candidate (Labbé) objects and analytic ceilings are tracked separately in the density ledger, the systematic budget (e.g., `SYSTEMATIC_BUDGET_LEDGER.csv`) mixes total, UV-red, and candidate populations. Central vs. Satellite fractions are unseparated.

## 5. Flags (Invented counts, invalid budgets, overstated language)
- **Invented counts:** None strictly invented, but TNG counts ($N=15, 20$) are not regenerated from catalog.
- **Invalid additive budgets:** The draft's $1.30$ dex linear sum and $0.55$ dex quadrature sum are correctly flagged by Kun as invalid or inflated because the terms strongly covary (e.g., IMF, SFH, SPS, dust-age-metallicity).
- **Ambiguous source identities:** 2025-2026 systematic sources remain unresolved.
- **Overstated status language:** "robust and IMF-independent consistency" is correctly flagged by Kun as overstated and requiring conditional, narrower language.

## 6. State Modification Check
No primary input, manuscripts, or public artifacts were modified. Kun maintained read-only isolation.
