# BS-2a Design — Version 2

This document responds to the `BRIEF_BS2A_DESIGN_V2.md` instructions, evaluating whether the acceptance rule requires a post-cutout quality cut, and whether upstream catalogue quantities can protect statistical power without destroying the frozen sample.

## 1. Does acceptance still need a post-cutout quality cut at all?

**No, the deletions resolved the parity-violation problem.**
With §2.7's reason (d) (the confidence threshold `|χ_net(x)| > τ`) deleted and reason (c) refused, the surviving acceptance predicates are purely integrity-based (e.g., cutout present, correct frozen tensor shape). An integrity-only acceptance rule excludes nothing based on the measured quantity (handedness). Because it no longer touches the classifier's output, it cannot inject a parity-breaking selection bias. Therefore, from an independence perspective, BS-2a is resolved by these deletions, and a post-cutout quality cut is not needed.

## 2. Upstream cuts to recover power

Accepting objects based on integrity alone introduces an honest risk: the cutout might be present and correctly shaped, but have such poor signal-to-noise or seeing that its handedness is unmeasurable. Accepting these objects dilutes accuracy $a$, which reduces the study's power.

To protect power without post-cutout measurement bias, we can filter on quality quantities evaluated upstream, before the first image byte is fetched. I verified the `ls_dr10.tractor_s` schema in `_tori_parent_row_count_evidence/schema_result.csv`. The valid candidate columns are:
- `flux_ivar_r`: Inverse variance of r-band flux (signal-to-noise proxy).
- `psfsize_r`: Median PSF size in arcsec (seeing proxy).
- `nobs_r`: Number of r-band exposures.
*(Note: `fracflux_r`, `fracmasked_r`, and `fracin_r` are not present in the DR10 tractor schema and cannot be used.)*

## 3. Parity-evenness by computation

Any upstream catalogue quantity is evaluated temporally before the cutout exists, making it structurally independent of handedness. Let $M$ be the mirror operation that reflects the spatial coordinates of the image, which flips the measured handedness.
The proposed candidate quantities are derived from scalar exposure counts or rotationally averaged profile properties. They are invariant under spatial reflection:
- $M(\text{flux\_ivar\_r}) = \text{flux\_ivar\_r}$
- $M(\text{psfsize\_r}) = \text{psfsize\_r}$
- $M(\text{nobs\_r}) = \text{nobs\_r}$

For non-invariant components like `shape_e2` (where $M(\text{shape\_e2}) = -\text{shape\_e2}$), the invariant combination is already used: the sum of squares `shape_e1^2 + shape_e2^2`. However, for the IVAR candidates above, the raw columns are themselves invariant.

**Fixture Specification:**
A test gate must instantiate a valid cutout `img` and its mirror reflection `M(img)`. The gate must assert that the upstream quality metadata fetched for both images are strictly equal:
`assert metadata(img).flux_ivar_r == metadata(M(img)).flux_ivar_r`
`assert metadata(img).psfsize_r == metadata(M(img)).psfsize_r`
This guarantees the quantity is entirely blind to image chirality.

## 4. Pricing the cost

The sample is currently frozen at 65,060 objects (plan digest `aaeaa9f3...`), and the closure, geometry, and Stage-P power receipts were computed exactly on this population (as established in `TORI_PARENT_ROW_COUNT_20260812.md`). 
Applying any new upstream quality filter (e.g., `flux_ivar_r > min_threshold`) will remove objects from this frozen sample. **Any additional filter changes N and immediately invalidates all existing receipts.**
Because adding the cut fundamentally alters the sample, we have no guarantee that the specific leverage geometry—specifically the two-ended distribution with $\text{Var}(\cos\theta) = 0.756$—survives the cut. If we apply the cut, we destroy the exact geometry that justifies the successor build, and re-establishing it would require discarding the frozen sample, fetching a new population, and recalculating all receipts from scratch.

## 5. Conclusion: The answer is no

**The answer is no.**
There is no admissible upstream quantity that protects power without destroying the frozen sample. While adding an upstream cut on `flux_ivar_r` or `psfsize_r` would be parity-even and protect accuracy $a$, applying it changes N = 65,060 and destroys the leverage geometry $\text{Var}(\cos\theta) = 0.756$. 
This is an argued refusal. We cannot implement an upstream quality cut to protect power without invalidating the frozen receipts. The study must either proceed with integrity-only acceptance (accepting the dilution of power), or halt, because the current sample constraint prevents mitigating the loss of power safely.
