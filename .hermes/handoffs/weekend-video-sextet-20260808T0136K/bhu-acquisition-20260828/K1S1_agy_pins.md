ACCESS_SHA=a6bf9810198ab696c4564153dc841cc5faea9fb1a357eab1b1bff25de24fd137

# K1S1 agy Report

## Discovery and Pinning Process
1. **Planck 2018 Cosmological Parameters (Pin 1):** Found `ln(10^10 A_s) = 3.044 \pm 0.014` and `n_s = 0.9649 \pm 0.0042` directly in the provided `1807.06209_clean.txt` (Table 1 Plik column, lines 1413 and 1419).
2. **Linear-theory Scaling of $\sigma(M)$ (Pin 2):** Confirmed in `1807.06209_clean.txt` (line 1780) that the power spectrum amplitude scales proportionally with $A_s$, meaning $\sigma \propto A_s^{1/2}$.
3. **Initial Mass Function (Pin 3):** Fetched Kroupa (2001) as `astro-ph/0009005` since it was not present in the pinned corpus. It provides the standard broken power-law with slopes $\alpha_1 = 1.3 \pm 0.5$ and $\alpha_2 = 2.3 \pm 0.3$ (Line 826). The file SHA256 was recorded.
4. **Remnant Mass Relation (Pin 4):** Fetched Fryer et al. (2012) as `1110.1726` to obtain the mapping of $M_{\rm CO}$ to remnant mass, specifying a maximum neutron-star mass $M_{\rm NS,max} = 2.5 M_\odot$ (Line 1051, 1073). The file SHA256 was recorded.
5. **PBH Threshold and Abundance (Pin 5):** Fetched `1405.7023` to obtain the exact analytic expression for the Press-Schechter PBH mass fraction $\beta_{PS} = {\rm erfc}(\nu_c/\sqrt{2})$ (Line 1593) and a representative critical threshold $\Delta_c \approx 0.41$ (Line 553). The file SHA256 was recorded.
6. **Stellar Black Hole Number Density (Pin 6/C1):** Not found within the pre-pinned corpus. Marked as UNPINNED as per the rule prohibiting unpinned values without explicit curl fetching authorization for this control pin.
7. **PBH Abundance Constraint (Pin 7/C2):** Located constraints from Carr et al. 2020 (`2002.12778_clean.txt`) at the $O(1) M_\odot$ scale, referencing the $f(M)$ exclusions in Figure 18 (Line 1691).

The resulting values, citations, and metadata have been written to `K1S1_agy_pins.md` according to the provided format.
