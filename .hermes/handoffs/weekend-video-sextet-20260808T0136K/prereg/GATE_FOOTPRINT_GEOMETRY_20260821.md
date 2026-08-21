HOLD_FOOTPRINT_GEOMETRY_FINDING

# Adversarial gate — Hwao footprint-geometry finding

## Verdict

The central population-mismatch allegation survives: the BS-1 receipt measured 832,393 dered Cut-6 objects over BRICKID 1…662174, while the position file now provisioned for measurement contains 208,407 dered Cut-5 study-parent rows from BRICKID 1..121000. My independent all-row geometry reproduces Hwao's moments and the two stated response coefficients.

I nevertheless HOLD the finding as written rather than PASS it. Its statement that F-3 is “not affected” is true only for permutation-test calibration under exchangeability; the footprint changes permutation power through var(cos theta). Its 0.0286 example meets the amplitude centre but does not by itself meet all REPRODUCED-LONGO predicates. Most importantly, the 208,407 rows are the pre-classifier Cut-5 parent, whereas F-1 is defined over accepted galaxies; the exact final coefficients cannot be asserted until the accepted-position subset exists. These limits do not refute the mismatch or the current-parent arithmetic.

## 1. Independent all-row recomputation

Input: `_positions_20260820/positions_parent_20260820.csv`, independently hashed as `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`.

Method: one CSV pass over every row; no sampling. For each equatorial position I evaluated

`c = sin(dec) sin(dec0) + cos(dec) cos(dec0) cos(ra-ra0)`

at `(ra0,dec0)=(216.984434295527,+32.060611193471)` degrees, then used population moments `mean(c)`, `mean(c^2)`, and `mean(c^2)-mean(c)^2`. Summation used `math.fsum`.

- CSV data rows: `208407`
- usable rows: `208407`
- blank required-field rows: `0`
- distinct `ls_id`: `208407`
- `mean(cos theta) = -0.646430488136329` → six decimals: `-0.646430`
- `mean(cos^2 theta) = 0.475857013390269` → six decimals: `0.475857`
- `var(cos theta) = 0.057984637398096` → six decimals: `0.057985`
- `min(cos theta) = -0.991828178939370` → six decimals: `-0.991828`
- `max(cos theta) = +0.318139878629485` → six decimals: `+0.318140`

Comparison to the finding: `n`, both means, and the population variance match its printed values to six decimals. The finding prints the range only to four decimals (`[-0.9918,+0.3181]`), so a six-decimal match cannot be tested from its text; my extrema agree with it at the precision it prints.

The current object-level value is below BS-1's `0.15` threshold. Even applying the variance receipt's conservative `+0.0124` bracket gives `0.057984637398096 + 0.0124 = 0.070384637398096 < 0.15`.

## 2. Population mismatch, verified by quotation

### Population measured by the footprint receipt

`TORI_FOOTPRINT_VARIANCE_RECEIPT.md` says:

> line 16: `- frozen population: 832,393 dered Cut-6 objects;`
>
> lines 33–37: `- partition coverage: 67/67;` / `- BRICKID keyspace: 1…662174, disjoint and exhaustive;` / `- aggregate rows returned: 270,577 per-brick count rows;` / `- summed grouped population: 832,393;` / `- frozen population match: TRUE;`
>
> line 90: `- accepted-sample variance claimed: NO — this receipt is for the frozen dered Cut-6 population;`

### Population in the current study-parent positions

`TORI_PARENT_ROW_COUNT_20260812.md` says:

> lines 36–38: `- Contiguous completed BRICKID range: 1..121000 of documented key range 1..662174.` / `- Catalogue partition-key coverage: 121,000/662,174 = 18.273143%.` / `- Not yet covered: BRICKID 121001..662174.`
>
> line 62: `| Cut 5 dered parent | dered Cut 4 + shape_r>1.5 | 208,407 | STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND |`

The later position-provisioning receipt makes the current scope explicit:

> `_positions_20260820/POSITIONS_RECEIPT_20260820.md`, line 35: `### Frozen R1 study-parent chain, BRICKID 1..121000`
>
> line 44: `| Cut 5 dered study parent | 208,407 | 208,407 | MATCH |`
>
> lines 165–173: the successful study-parent query binds `WHERE t.brickid BETWEEN 1 AND 121000` and ends at `t.shape_r > 1.5`.

These are not the same population: they differ in count, BRICKID keyspace, and cut level (full-keyspace Cut-6 versus R1 Cut-5). The finding does not collapse.

## 3. Arithmetic of the three consequences

Let `c=cos theta`, `D_hat = mean(s*c)`, and F-1's `A_hat=3*D_hat`. Under the model stated in the brief, `E[s|c]=M+A*c`, linearity gives

`E[A_hat] = 3*M*mean(c) + 3*A*mean(c^2)`.

This formula is correct for the fixed current positions.

### Consequence 1 — normalisation

For the 208,407-row parent:

- dipole response coefficient: `3*mean(c^2) = 1.427571040170807`, i.e. `1.4276`;
- inflation relative to a coefficient of one: `42.7571%`;
- an amplitude producing `A_hat=0.0408` when `M=0` is `0.0408/1.427571040170807 = 0.028580013779993`, i.e. `0.0286`.

Hwao's `1.4276` and “43%” arithmetic are right for this parent. For the footprint receipt's brick-centre moment, `3*0.457107680481017 = 1.371323041443051`, so the factor-three issue is not created by the R1 cap.

However, “landing dead centre in REPRODUCED-LONGO” is too strong. `A=0.0286`, `M=0` centres the amplitude predicate near 0.0408; F-6 additionally requires permutation `p<0.001`, Longo's sign, attenuation correction, and the stated uncertainty band. The example alone proves only the amplitude-centre statement.

### Consequence 2 — monopole leakage

For the current parent:

- monopole coefficient: `3*mean(c) = -1.939291464408987`, i.e. `-1.939`;
- `M=0.01`, `A=0` gives `E[A_hat] = -0.019392914644090`.

For the footprint receipt, the coefficient is `3*(-0.109116141652194) = -0.327348424956582`. The absolute coefficient ratio is `5.924242539631`, so “six times worse” is a fair rounding. F-2 reporting the monopole does not subtract or orthogonalise it from F-1's frozen raw estimator.

### Consequence 3 — positive-pole coverage

The all-row extrema are `[-0.991828178939370,+0.318139878629485]`. The parent reaches very near the negative pole but never approaches the positive pole. This geometric consequence survives.

### Scope limit on all exact coefficients

F-1 says it is evaluated “over accepted galaxies.” The 208,407-row file is the Cut-5 study parent before classifier acceptance. `LANA_VARIANCE_APPROACH_AUDIT.md` lines 85–88 explicitly warns that none of its tiers licenses accepted-sample variance because abstention can re-tilt the weights. Therefore `1.427571` and `-1.939291` are exact for the current parent, not yet proven exact for the eventual F-1 accepted subset. This is a material reason for HOLD, not a refutation of the present population mismatch.

## 4. Four required refutation attacks

### (a) Non-full-sky F-1 normalisation receipt — ATTACK FAILED

I found no receipt that re-derived `A_hat=3*D_hat` for a non-full-sky footprint. The frozen preregistration line 131 names only an unpinned shorthand, “unbiasedness receipt: spike, injected 0.0400 → recovered 0.0402”; the exact phrase/value search found repetitions in prereg copies, not a separate non-full-footprint receipt.

The actual referenced source, `spike/sim_power.py`, is decisive:

> lines 5–9: `# Uniform points on sphere` and `costheta = np.random.uniform(-1, 1, N)`
>
> lines 96–106: `test_unbiasedness`, `# On a sphere, mean(cos^2) = 1/3`, `expected_D = A / 3.0`, and `Implied A (3*D)`.

So the spike uses a uniform full sphere and assumes `mean(cos^2)=1/3`; it does not validate the non-full-sky normalisation. `LANA_VARIANCE_APPROACH_AUDIT.md` lines 28–30 independently states the general result `E[D_hat]=A*mean(cos^2)`, which supports rather than refutes the finding.

### (b) Longo's published A absorbs the needed normalisation — ATTACK FAILED

The primary paper, Longo 2011, arXiv:1104.2815, says:

> “The 15158 points were then fitted to an a cos gamma dependence.”
>
> “The a cos gamma fit for the actual handedness assignments gave a = -0.0408 with an uncertainty sigma_a = +/-0.011.”

Thus Longo's number is the fitted coefficient of the model `s ≈ a*cos(gamma)` on his positions. For an unweighted through-origin fit that coefficient is `sum(s*c)/sum(c^2) = D_hat/mean(c^2)`; the sample's second moment is in the fit denominator. Nothing in the paper defines Longo's `a` as the raw moment multiplied by three. His fit therefore does not make `3*D_hat` correct on a different footprint whose `mean(c^2)` is 0.475857.

### (c) BRICKID 121001..662174 was always intended to land — PARTIAL HISTORICAL FACT, NOT A REFUTATION

`TORI_FULL_KEYSPACE_SWEEP_20260813.md` line 9 confirms that a later aggregate sweep had `New one-pass scope: BRICKID 121001…662174`, and lines 24–27 close the exact full-keyspace aggregate count. Therefore it would be wrong to say the remaining keyspace was never counted or never contemplated.

But that later aggregate sweep did not change the current position deliverable. The 2026-08-20 provisioning receipt deliberately calls BRICKID 1..121000 the “Frozen R1 study-parent chain” and exports exactly its 208,407 Cut-5 rows. The current CSV is not documented as a provisional prefix awaiting automatic append. Historical intent to count full-keyspace aggregates does not erase the population mismatch for the current measured parent. If a different final position population is later authorized, this gate's coefficients do not automatically transfer to it.

### (d) F-3 permutation null unaffected — PARTIAL REFUTATION OF WORDING; CALIBRATION SURVIVES

A label permutation preserves the sign multiset and therefore preserves `mean(s)` exactly. For fixed signs `s` and positions `c`, the exact permutation moments are

`E_perm[D_perm] = mean(s)*mean(c)`

and

`Var_perm(D_perm) = Var_pop(s)*Var_pop(c)/(N-1)`.

So the null distribution is centred on the monopole-leakage offset. It does not give every permutation the identical leakage; it preserves that offset in expectation. Under the null hypothesis that labels are exchangeable over positions, including a constant global monopole, the conditional randomisation p-value remains calibrated. In that limited sense Hwao is right.

But under a dipole alternative,

`E[D_obs - E_perm(D_perm)] = A*(mean(c^2)-mean(c)^2) = A*Var(c)`.

The current `Var(c)=0.057985` therefore directly reduces the separation from the permutation null and changes F-3's power. A spatially varying selection effect would also violate exchangeability and would not be rescued merely by preserving the global sign count. Accordingly, “F-3 is unaffected” and “damage is confined to F-6's amplitude comparisons” are too broad. The p-value procedure remains valid under exchangeability; its power is affected.

## 5. F-6 decision-region effects

- **REPRODUCED-LONGO:** affected. The absolute-amplitude band can be entered by a smaller true dipole or by monopole leakage/cancellation, but the separate `p<0.001` and sign predicates still bind. The low `Var(c)` also reduces permutation power, so an amplitude-centred example is not automatically REPRODUCED-LONGO.
- **REJECTED-AT-LONGO-AMPLITUDE:** affected. The frozen condition uses `|A_hat_c|` and `sigma_ours` against 0.0408. Inflation or monopole leakage can block rejection; opposite-signed leakage can cancel a true dipole and make rejection easier. Its separate `p>0.05` predicate is also power-sensitive.
- **INCONCLUSIVE:** affected as the exhaustive residual region whenever either of the above memberships changes.
- **INCONCLUSIVE-BY-POWER:** potentially affected before unblinding. The cited spike/power source generates a uniform sphere and uses the `1/3` geometry. The actual permutation leverage is `Var(c)`, so the claimed full-sky power calculation does not establish the same power on this parent. I did not compute or propose a replacement gate.

The same footprint issue also reaches F-4/F-7 quantities: F-4 freezes `sigma_D=sqrt(1/(3N))`, while the fixed-footprint uncentred sign variance uses `mean(c^2)/N` and the permutation-conditioned variance uses `Var(s)*Var(c)/(N-1)`. Therefore the finding's statement that damage is confined only to F-6 amplitude comparisons omits uncertainty/floor and pre-unblinding-power consequences.

## 6. Evidence and boundaries

Read in full: the named finding, frozen preregistration, footprint receipt, parent row-count receipt, full-keyspace sweep, position CSV, position receipt, position gate, `LANA_VARIANCE_APPROACH_AUDIT.md`, `LANA_BS5_LONGO_SIGN_20260814.md`, and `spike/sim_power.py`. Primary-source check: Longo 2011 arXiv abstract and PDF at `https://arxiv.org/abs/1104.2815` and `https://arxiv.org/pdf/1104.2815`.

Independent source hashes were recomputed for all six named gate inputs. No file under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened; no chi value or aggregate was computed. Geometry used positions only. No preregistration input was edited, chmodded, or replaced. No estimator change or remedy is proposed here.
