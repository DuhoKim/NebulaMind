HOLD_FOOTPRINT_GEOMETRY_REV2

# Fresh adversarial re-gate — footprint-geometry finding, Revision 2

## Verdict

Revision 2 is not refuted. The central population mismatch survives; all three requested repairs are faithful in substance; the exact permutation-variance formula is correct under the population-variance convention; and every headline full-sphere number through the 36,253 figure recomputes.

I nevertheless HOLD Revision 2 as written. Consequence 4 contains two unqualified claims that do not survive attack: (1) the `18,127` row at 50% acceptance assumes proportional/geometry-neutral retention, although Revision 2 itself says acceptance can re-tilt the footprint; actual 50% subsets of these positions span very different leverage, and (2) a merely spatially varying selection function does not necessarily violate exchangeability—only a position-dependent sign/handedness mechanism, or another mechanism that makes labels nonexchangeable conditional on the accepted positions, does. The main 36,253 conclusion survives both defects and is stronger than Revision 2 explains: total centred leverage of any accepted subset cannot exceed that of the full parent.

A separate qualification also binds the power language. `spike/sim_power.py` uses a two-sided normal p-value, whereas frozen F-3 is one-sided at Longo's sign. Sidedness changes the critical value and absolute power but not the geometric leverage ratio. Section 5 has a literal-contract reading under which its formally frozen power check can still pass by applying the pinned uniform-sphere logic at realized `N` and `a`; such a pass would not establish power on this footprint. Revision 2's narrower statement—existing uniform-sphere work does not establish actual-footprint power—is correct.

## 1. Repair fidelity against the prior gate

### Repair 1 — the `A = 0.0286` example: FAITHFUL

Revision 1 said that the example would land “dead centre in REPRODUCED-LONGO.” The prior gate ruled that it centres only the amplitude predicate because permutation `p < 0.001`, Longo's sign, attenuation, and the uncertainty-band condition bind independently (`GATE_FOOTPRINT_GEOMETRY_20260821.md`, lines 73–83).

Revision 2 now says exactly that the example “centres the amplitude predicate” and “does not establish a REPRODUCED-LONGO verdict” (`HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`, lines 42–45). This neither undershoots nor materially overshoots the ruling. The amplitude arithmetic also remains correct:

- `3 * 0.4758570133902695 = 1.4275710401708085`;
- `0.0408 / 1.4275710401708085 = 0.028580013779993`.

### Repair 2 — F-3 was not wholly unaffected: FAITHFUL, WITH NEW DEFECTS IN THE EXPANSION

Revision 1 said the p-value remained valid and “the damage is confined to F-6's amplitude comparisons.” The prior gate ruled instead:

- calibration survives under exchangeability;
- the footprint changes separation from the permutation null and therefore power;
- F-4, F-7, and the pre-unblinding power gate are implicated;
- spatially varying selection can be an exchangeability concern.

Revision 2 faithfully retracts the “unaffected/confined” wording, preserves the conditional calibration result, and adds the power consequence. It does not quietly reassert the old scope.

The expansion does, however, overstate two points not required by the prior ruling:

1. `18,127` at 50% acceptance is a hypothetical proportional-retention projection, not an accepted-subset fact.
2. “A spatially varying selection effect would violate [exchangeability]” is categorical. Position-only retention can vary arbitrarily while signs remain exchangeable under the null. The violation requires sign-dependent selection, spatially varying handedness misclassification, or another label-position dependence.

### Repair 3 — parent versus accepted-sample scope: FAITHFUL

The prior gate ruled that the exact coefficients were established for the 208,407-row pre-classifier Cut-5 parent, not the eventual accepted F-1 sample. Revision 2 adds that limit explicitly at lines 111–118 and accurately quotes the substance of `LANA_VARIANCE_APPROACH_AUDIT.md`, lines 85–88.

There is no undershoot: the scope section binds `1.427571`, `-1.939291`, and Consequence 4. There is no scientific overshoot in saying the population mismatch itself survives. One internal tension remains: the 50%-acceptance table row is not “exact for the current parent” unless read as a stated-but-unstated geometry-neutral projection.

### Changelog and unrelated-delta check

The two “Was:” passages reproduce Revision 1's lexical wording. They are not byte-identical excerpts because Revision 1's Markdown bold markers are omitted inside the changelog's italic quotation, but no scientific words are changed.

The direct Revision 1/Revision 2 diff shows no quiet reversal of an unrelated scientific claim. Revision 2 also deletes Revision 1's stopping-rule narrative and its four-item “What a gate should try to refute” list; these are unlogged editorial deletions, not altered scientific conclusions. The newly added receipt disclaimer, Cut-5/Cut-6 distinction, simulation-source check, and Longo fit discussion all come from the prior gate's own investigation as the changelog says.

## 2. Permutation moments from first principles

Let

- `D_perm = (1/N) * sum_i s_{pi(i)} c_i`,
- `s_bar = (1/N) * sum_i s_i`, `c_bar = (1/N) * sum_i c_i`,
- `V_s = (1/N) * sum_i (s_i-s_bar)^2`,
- `V_c = (1/N) * sum_i (c_i-c_bar)^2`,

where `pi` is a uniformly random permutation and `V_s,V_c` are population variances with denominator `N`.

Sampling the fixed signs without replacement gives, for every `i != j`,

- `E[s_{pi(i)}] = s_bar`,
- `Var(s_{pi(i)}) = V_s`,
- `Cov(s_{pi(i)},s_{pi(j)}) = -V_s/(N-1)`.

Therefore

`E_perm[D_perm] = s_bar * c_bar`.

For the variance,

`Var_perm(D_perm)`

`= (V_s/N^2) * [sum_i c_i^2 - (1/(N-1))*sum_{i!=j} c_i*c_j]`

`= (V_s/N^2) * [N*sum_i c_i^2 - (sum_i c_i)^2]/(N-1)`

`= V_s * V_c / (N-1)`.

Thus Revision 2's formula is structurally correct and exact with population variances.

If `S_s^2` and `S_c^2` instead denote conventional sample variances with denominator `N-1`, then

`Var_perm(D_perm) = ((N-1)/N^2) * S_s^2 * S_c^2`.

Writing the same formula as `S_s^2*S_c^2/(N-1)` would therefore be wrong. Revision 2 avoids that error only because its `Var` must mean population variance, as the prior gate's geometry computation did. I also brute-force enumerated all 24 permutations of a four-element example; the enumerated variance `0.13166666666666668` exactly matched both convention-correct formulas.

Under the alternative `E[s_i | c_i] = M + A*c_i`,

- `E[D_obs] = M*c_bar + A*mean(c^2)`;
- `E[E_perm(D_perm)] = E[s_bar]*c_bar = (M + A*c_bar)*c_bar`;
- their difference is `A*(mean(c^2)-c_bar^2) = A*V_c`.

Revision 2's third moment statement is therefore correct as an expectation over label generation. It is not a claim that a particular realized permutation centre equals its model expectation.

## 3. Independent numeric audit of Consequence 4

I read every one of the 208,407 position rows and recomputed `c = cos(theta)` at the supplied axis with `math.fsum`. Input SHA-256: `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`.

Recomputed parent moments:

- `N = 208407`;
- `mean(c) = -0.6464304881363294`;
- `mean(c^2) = 0.4758570133902695`;
- `V_c = 0.05798463739809634`;
- `min(c) = -0.9918281789393699`;
- `max(c) = +0.3181398786294847`.

Full-sphere comparison, using `V_full = 1/3`:

| Revision 2 quantity | independent value | ruling |
|---|---:|---|
| leverage ratio | `3*V_c = 0.1739539121942890` | `0.173954` correct |
| sensitivity ratio | `sqrt(3*V_c) = 0.4170778251049665` | `0.417078` correct |
| equal-power N multiplier | `1/(3*V_c) = 5.748649095532273` | `5.7486` correct |
| N for 100,000 full-sphere-equivalent | `574864.9095532272` | `574,865` correct |
| 208,407-parent full-sphere-equivalent | `36253.2129786752` | `36,253` correct |
| half-times-parent projection | `18126.6064893376` | `18,127` arithmetic correct, interpretation conditional |

The off-by-one refinement replaces `N` by `N-1` in noncentrality. At `N=208407` it is immaterial.

For `s in {-1,+1}`, `V_s = 1-s_bar^2 <= 1`. The exact normal-approximation noncentrality is

`lambda = A * sqrt((N-1)*V_c/V_s)`.

Revision 2's `A*sqrt(N*V_c)` is therefore the small-amplitude, `V_s approximately 1`, large-`N` figure of merit. It is the right geometric scaling, not an exact equality. At `A <= 0.0408` the omitted `V_s` correction is sub-per-mille for these model means and does not materially alter any printed ratio.

### The 36,253 conclusion is robust; the 50% row is not

Let `SSE(P) = sum_{i in P}(c_i-c_bar_P)^2 = N_P*V_P`. For any accepted subset `S` of the parent `P`,

`SSE(S) = min_a sum_{i in S}(c_i-a)^2 <= sum_{i in S}(c_i-c_bar_P)^2 <= SSE(P)`.

So no accepted subset can have more total centred geometric leverage than the full parent. The full-parent value `N*V_c = 12084.4043262251`, or `36,253.213` full-sphere galaxies, is an upper bound over every accepted subset—not merely the value at 100% acceptance. This independently validates the headline “even at 100% acceptance” argument.

By contrast, leverage is not generally linear in the acceptance fraction. Two explicit 104,203-row (approximately 50%) subsets of these same positions demonstrate the gap:

- the half farthest from the parent mean has `3*SSE = 33,623.880` full-sphere-equivalent;
- the half nearest the parent mean has `3*SSE = 2,583.468` full-sphere-equivalent;
- Revision 2's linear half projection is `18,126.606`.

No chirality value was used in these examples; they are position-only counterexamples to treating acceptance fraction alone as sufficient. The `18,127` row needs an explicit geometry-neutral/proportional-retention assumption and is unsupported as written.

## 4. Is this the right figure of merit for frozen F-3?

For a one-sided test at fixed `alpha`, the normal approximation gives

`Power approximately Phi(lambda - z_(1-alpha))`,

with `lambda = A*sqrt((N-1)*V_c/V_s)`. At frozen `alpha=0.001`, `z_(0.999)=3.090232306`. Therefore `A*sqrt(N*V_c)` is the correct leading figure of merit for F-3's fixed-axis, one-sided permutation test. Fixed sidedness changes only the critical constant, not the `N*V_c` ratio. An exact finite permutation test is not literally Gaussian, but at this `N` that distinction cannot rescue a factor `5.7486` loss of geometric leverage.

The named harness is not one-sided:

- `spike/sim_power.py`, line 43, uses `abs(D_null) >= abs(D_obs)`;
- lines 88–89 use `z = abs(D_obs)/std_D` and `p_val = 2*(1-CDF(z))`.

Frozen F-3 (`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`, lines 134–135) is explicitly one-sided at Longo's sign. The BS-8 power receipt also calls its `p=0.001` critical threshold two-tailed. This is an existing frozen-source seam, not a structural error in Revision 2's leverage ratio. For reference, the two-sided threshold is `3.290526731`, versus `3.090232306` one-sided.

Under the same normal planning model, the most favorable attenuation `a=1` gives `A_eff=0.0408`. Using the full parent gives

- `lambda = 4.486656765`;
- one-sided power approximately `0.9187066`;
- two-sided power approximately `0.8841771`.

The 95%-power noncentrality requirements are `4.735085933` one-sided and `4.935380358` two-sided. Even allowing the most favorable model variance permitted by `|A_eff|<=0.0408`, the full-parent SSE bounds the geometric noncentrality by `4.488844491`. Thus, under the same analytical approximation used by section 5, no accepted subset of this parent reaches 95% power at the Longo amplitude. This calculation is an audit of the frozen claim, not a proposed parameter, estimator, or remedy.

## 5. Which baseline is legitimate?

### Uniform full sphere: legitimate for auditing the frozen receipt

Revision 2's full-sphere baseline is the right baseline for its narrow claim about what the frozen power work actually established. `spike/sim_power.py` literally draws `costheta` uniformly on `[-1,1]`; the BS-8 receipt evaluates `A_eff/3` and `sigma_D approximately 1/sqrt(3N)`. The existing receipt therefore establishes a uniform-sphere calculation, not an actual-footprint calculation.

### Longo's footprint: necessary for a comparison to Longo's original data, but test-dependent

Longo's own footprint is not uniform. The paper states that the northern cap dominates, gives rough sky ranges, fits all 15,158 selected galaxies, and notes sparse opposite-hemisphere coverage. The paper also states that a supplementary file contains spin assignments and coordinates.

I retrieved that official Elsevier supplement:

`https://ars.els-cdn.com/content/image/1-s2.0-S0370269311003947-mmc1.txt`

SHA-256: `ddbdeaf78aa4f92dfa1241ffa8b44645f00dac60dcf2096dc20ff84755ff4f3d`.

It contains 25,561 unique 12-field rows. Applying the paper's printed cuts (`z < 0.085`; `g < 17` below `z=0.04`, otherwise `g < 17.4`; `1.6 < u-z < 3.5`) yields 15,157 rows, one fewer than the paper's 15,158. Inclusive-versus-strict boundary variants do not recover the missing row. The one-object custody discrepancy is disclosed rather than silently filled.

At the frozen axis `(216.984434295527,+32.060611193471)`, those 15,157 public rows give

- `mean(c) = 0.5858945922780232`;
- `mean(c^2) = 0.5677588025427663`;
- `Var(c) = 0.2244863292821353`.

Allowing the one missing object to have any `c` in `[-1,1]` bounds the 15,158-row variance to `[0.2244715195, 0.2246374316]`.

If one compares the frozen F-3 centred-permutation leverage on the two coordinate sets, the current parent relative to Longo's footprint has

- leverage ratio `0.25813–0.25832`;
- sensitivity ratio `0.50806–0.50825`;
- equal-power N multiplier `3.87122–3.87409`;
- 208,407 current-parent rows equivalent to about `53,795–53,835` Longo-footprint rows.

That is a different, less severe multiplier than the full-sphere `5.7486`, as the brief anticipated.

There is not one universal “Longo multiplier,” however. Longo's reported `a` comes from a through-origin `a*cos(gamma)` fit and his null randomly assigns `+1/-1` with equal probability rather than conditioning on a fixed sign count. For an unweighted through-origin fit the information is `sum(c^2)`, not the centred `sum((c-c_bar)^2)`. On that raw-fit metric, the current-parent/Longo per-object second-moment ratio is `0.838132` (sensitivity ratio `0.915496`, N multiplier about `1.19313`). Longo also optimized the axis, whereas F-3 is fixed-axis. Therefore:

- full sphere is the correct baseline for identifying the frozen harness's assumption;
- Longo's coordinates are the correct comparator for a claim of equal footprint sensitivity to Longo;
- Longo's original free-axis through-origin test is not identical to frozen F-3, so the comparison metric must be named.

Revision 2 names its metric “relative to a uniform full sphere,” so its `5.7486` is not numerically false. Its prose would be incomplete if read as a comparison to Longo's original experiment rather than to the frozen harness.

## 6. Section 5 of the preregistration: what follows and what does not

Section 5 HC-6 freezes this formal operation: inspect the pinned harness and evaluate its analytical power logic at `A_eff=(2a-1)*0.0408` and bound `N`; re-evaluate by the same method at the lower-bound hand-checked `a` before unblinding; require power at least 0.95; and require `N_accepted >= 100,000` (`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`, lines 319–329).

Two readings must be separated:

1. **Scientific-power reading.** “Power” means power of frozen F-3 on the accepted fixed positions. On this reading, the uniform-sphere BS-8 receipt does not establish the gate. The accepted positions do not yet exist, but the full-parent SSE is already an upper bound; under the same analytical approximation even `a=1` cannot reach 0.95. Revision 2's “does not establish that power here” follows.
2. **Literal frozen-algorithm reading.** “Same analytical method” means reuse the pinned harness's uniform-sphere `1/3` logic with only realized `N` and lower-bound `a` substituted. The text does not explicitly name accepted-sample `Var(c)` as an HC-6 input. On this reading, the formal gate can still report PASS if its frozen uniform-sphere calculation passes. Such a formal PASS would not establish actual-footprint power; it would expose a mismatch between the frozen procedure and the scientific property it is called upon to certify.

Revision 2 does not prove that the already frozen formal state is automatically `INCONCLUSIVE-BY-POWER`; it proves that the existing BS-8/uniform-sphere evidence is not evidence of actual-footprint 95% power. Its wording “reaches … INCONCLUSIVE-BY-POWER” is supportable as impact/risk, not as an already-issued verdict.

## 7. Integrity sweep of named sources and new claims

### `TORI_FOOTPRINT_VARIANCE_RECEIPT.md` line 90: ACCURATE

Actual line 90 is:

`- accepted-sample variance claimed: **NO** — this receipt is for the frozen dered Cut-6 population;`

Revision 2 preserves every word and only drops the source's Markdown bold markers around `NO`. The receipt also directly supports `832,393`, the brick-centre moments, full keyspace, and the binding variance rule.

### Frozen preregistration BS-1 row: ACCURATE COMPRESSED QUOTATION

The BS-1 row at line 451 says `footprint variance PASS` and gives `count-weighted var(cos theta) = 0.445201 >= 0.15 with >= 2x the 0.0124 bracket`. Revision 2's ellipsis removes “count-weighted” and the extra margin clause but does not reverse or inflate the cited proposition. The population problem comes from what the receipt bounds, not from a fabricated prereg quotation.

### `spike/sim_power.py`: DRAW/UNBIASEDNESS QUOTES ACCURATE; POWER-SIDEDNESS OMITTED

Revision 2 accurately reports:

- uniform-sphere generation (`costheta = np.random.uniform(-1,1,N)`, lines 5–9);
- the comment `On a sphere, mean(cos^2) = 1/3` and `Implied A (3*D)`, lines 96–106.

It is also true that this does not validate a restricted-footprint normalization. But its power block is two-sided, not frozen F-3's one-sided test. The omission does not change geometric scaling but is material to any absolute power statement.

### Longo 2011: QUOTES ACCURATE; FIT FORMULA IS A DERIVATION, NOT A QUOTE

The local primary-source extraction says at lines 159–171 that the complete 15,158 sample was used and “The 15158 points were then fitted to an a cos gamma dependence.” Lines 215–217 give `a=-0.0408`, `sigma_a=+/-0.011`. Revision 2 quotes these accurately.

`sum(s*c)/sum(c^2)` is the ordinary unweighted least-squares coefficient for the printed through-origin model; Longo does not print that algebraic formula verbatim or spell out a weighting equation in the quoted passage. The conclusion that a through-origin fit carries its own footprint moment in the denominator is mathematically sound under the ordinary equal-weight reading and is consistent with Longo's randomized-sign treatment. It should be recognized as a derivation rather than presented as another direct quotation.

### New/standing unsupported or overbroad wording

1. **New and blocking:** `18,127` at 50% acceptance is conditional on retention preserving the parent's geometry; acceptance fraction alone does not determine leverage.
2. **New and blocking:** “a spatially varying selection effect would violate exchangeability” lacks the necessary sign-dependence qualifier.
3. **Standing, not introduced by Revision 2:** “`E[cos^2 theta]=1/3`, i.e. a uniform full sphere” is logically too strong. A nonuniform footprint can also happen to have second moment `1/3`; uniform full sphere is sufficient, not necessary. The current footprint's measured second moment is nevertheless not `1/3`, so the normalization conclusion survives.
4. **Scope tension:** the statement that “every number in Consequence 4” is exact for the parent is compatible with the 36,253 full-parent value but not with the unqualified 50%-acceptance row.

I found no other new numerical claim that failed its named source or independent recomputation.

## 8. Failed attacks

- **Structural permutation-variance attack failed:** the formula is exact with population variances.
- **Off-by-one attack failed materially:** `N-1` is present in the exact formula; replacing `N-1` by `N` only in the large-N scaling is negligible here.
- **Headline arithmetic attack failed:** `0.173954`, `0.417078`, `5.7486`, `574,865`, and `36,253` all reproduce.
- **Accepted-subset escape attack failed against the headline:** subset SSE cannot exceed full-parent SSE, so selective acceptance cannot exceed 36,253 full-sphere-equivalent centred leverage.
- **Full-sphere-baseline attack only partly landed:** it is the wrong baseline for comparison to Longo's original footprint, but it is exactly the baseline the frozen harness used and is therefore legitimate for auditing that receipt.
- **Repair-fidelity attack failed:** all three prior rulings are represented in the repaired text; no unrelated scientific claim was silently reversed.
- **Quote-fabrication attack failed:** receipt, prereg, simulation, and Longo quotations are present in the named sources, subject to the formatting/derivation qualifications above.

## 9. Evidence ledger and boundaries

Read in full or in the relevant complete sections:

- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` — SHA-256 `a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76`;
- `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md` — `f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee`;
- `GATE_FOOTPRINT_GEOMETRY_20260821.md` — `1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1`;
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`;
- `TORI_FOOTPRINT_VARIANCE_RECEIPT.md` — `9f6955e3c625de3ed94ee06593661d1f3f8e196282572de2a989be9b082326c0`;
- `LANA_VARIANCE_APPROACH_AUDIT.md` — `04738a649b9d0533ce6070a5b8327839de7878250f092c517e950bba248b2c44`;
- `GORU_BS8_POWER_RECEIPT_20260814.md` — `b6207c7fc93ea7bfeb8045d0e635693010644633b747b298eb51b6233f014a92`;
- `../spike/sim_power.py` — `f2867dbf4f5ab8ad82d645324a525a75af38006ff03e8ee08b90589cff50b1ce`;
- local Longo 2011 primary-source text/PDF and official Elsevier supplementary data.

Mechanical work performed:

- direct unified diff of Revision 1 and Revision 2;
- all-row parent geometry recomputation with `math.fsum`;
- first-principles algebra plus exhaustive four-element permutation enumeration;
- independent full-sphere arithmetic and one-/two-sided normal-power calculations;
- official Longo supplement parsing, published-cut reconstruction, and moment calculation;
- explicit 50%-subset counterexamples;
- pre- and post-analysis SHA-256 custody checks.

Boundary statement: no path under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened or listed; no chi value, sign aggregate, or chirality statistic was computed. Inputs under `prereg/` were read-only. The only non-report artifact written was the permitted lane-local temporary `_tmp_regate_footprint_longo_mmc1.txt`. No estimator, parameter, preregistration, git state, database, process, or public artifact was changed.
