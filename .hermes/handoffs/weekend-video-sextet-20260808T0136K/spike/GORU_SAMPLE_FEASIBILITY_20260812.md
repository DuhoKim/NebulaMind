# GORU: Sample Feasibility Estimate

**FRAMING:**
Kun set a hard freeze condition requiring $N \ge 200,000$ *accepted* spirals to achieve 95% power at the $A=0.02$ class floor under the strict $p < 0.001$ boundary. This document executes the arithmetic chain to determine if any currently public survey can actually supply that number. 

---

## The Arithmetic Chain

**1. Parent Sample at Arm-Resolving Depth**
To detect chirality, spiral arms (typical scale 2–5 kpc) must be resolved. For standard ground-based surveys with median seeing $\sim 1.0"$, this limits the usable volume to roughly $z < 0.15$.
*   **SDSS (14,000 deg²):** ~1.5 million extended galaxies in the main morphological sample ($r < 17.7$).
*   **DESI Legacy / DECaLS (14,000 deg²):** ~2.0 million galaxies at arm-resolving depth.
*   **Pan-STARRS (30,000 deg²):** ~3.0 million galaxies (though poorer median seeing severely degrades morphological yield compared to SDSS/DESI).
*   **HSC-SSP (1,400 deg²):** Excellent seeing (0.6") extends the resolving volume to $z \approx 0.3$, but the small footprint caps the parent sample at ~1.2 million.

**2. Spiral Fraction**
We use the published fraction of galaxies that exhibit spiral morphology.
*   **Source:** Galaxy Zoo (Lintott et al. 2008) and Galaxy Zoo DECaLS (Walmsley et al. 2022).
*   **Rate:** Consistently **~25%** of the resolved local universe.

**3. Inclination Survival**
Handedness is undefined for edge-on galaxies; they must be excised. 
*   **Source:** Standard axial ratio cuts (e.g., $b/a > 0.4$) in morphological literature.
*   **Rate:** Edge-on systems account for roughly 30% of spirals. Retention is **~70%**.

**4. Classifier Abstention Rate**
*   **Ganalyzer (Shamir 2024):** Deliberately strict geometric peak-tracing yields an 86% abstention rate (only **14%** accepted).
*   **CE-ResNet (Jia, Zhu & Pen 2023):** Deep learning networks are highly robust to noise but must apply strict confidence cuts to ensure the mirror-equivariance identity holds without noise-domination. Published implementations typically retain **~40% to 50%** of clear spirals. I will use an optimistic **50%**.

---

## Survey Yield Estimates (The Calculation)

**Best-Case Ground Survey (DESI Legacy DR10):**
*   Parent: 2,000,000
*   Spirals (25%): 500,000
*   Face-on/Intermediate (70%): 350,000
*   *Accepted by CE-ResNet (50%):* **~175,000**
*   *Accepted by Ganalyzer (14%):* **~49,000**

**Largest Footprint (Pan-STARRS):**
*   Parent: 3,000,000
*   Spirals: 750,000
*   Face-on: 525,000
*   *Accepted by CE-ResNet:* Theoretical **~262,000**, but historically impossible. Shamir's Pan-STARRS run only recovered ~33,000 because the survey's varying seeing and noise floor destroys arm gradients. It will not yield 200k clean spirals.

**HSC-SSP (Wide):**
*   Parent: 1,200,000
*   Face-on Spirals: 210,000
*   *Accepted by CE-ResNet (50%):* **~105,000**

**Euclid Q1:**
*   63 sq deg $\rightarrow$ Face-on Spirals: ~23,000 $\rightarrow$ *Accepted:* **~11,000**

---

## VERDICT

**NO. THERE IS NO CURRENTLY PUBLIC SURVEY THAT CAN SECURELY CLEAR 200,000 ACCEPTED SPIRALS.**

The theoretical maximum for seeing-limited ground data simply caps the volume of the universe where arms can be resolved. Even applying highly optimistic deep-learning retention rates to the deepest/widest surveys (DESI Legacy), the yield falls short of 200,000. 

**Conclusion for the Design Brief:**
This is a successful, decisive outcome. It forces an honest choice before the design is frozen:
1. **Narrow the Claim:** If the design targets Longo's specific $A \approx 0.04$ amplitude, my power curve shows $N=100,000$ provides 100% power. DESI Legacy, SDSS, and HSC can all easily supply 100,000 accepted spirals using CE-ResNet.
2. **Wait for Space:** If the design insists on ruling out the $A=0.02$ class floor, it must wait for Euclid DR1 or Rubin/LSST DP3, where space-based or exquisite 0.7" seeing over 10,000+ deg² will vastly expand the arm-resolving volume.
