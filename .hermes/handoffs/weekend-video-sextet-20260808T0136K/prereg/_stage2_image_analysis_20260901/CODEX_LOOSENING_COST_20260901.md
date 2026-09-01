# Cost of the loosening path

## Bottom line

None of Duho's four capacity limits supports the frozen confirmatory calibration. Merely reducing `HC_REAL_LABELS` while retaining the allocation floors does not buy a smaller design: with nine live strata and three live calibration bins, `allocate_handcheck()` requires `9 × max(30, 3 × 10) = 270` real first-presentation decisions before controls. Because Duho's limit is **total decisions**, even the 120-decision case is infeasible before allocation under the frozen design.

Small totals can be made arithmetically feasible only by changing the coverage design itself. The least misleading capacity-backward variants below preserve the inherited approximate queue composition—500/850 real first presentations, 200/850 known-answer synthetics, and 150/850 mirrored repeats—with integer rounding. Thus controls are inside, not on top of, each total. `R_max=2` permits twice as many committed renders; it never creates another independent decision.

These variants are useful as pilots or, at the top budget, as a coarse upper-limit exercise. They do not provide a realistically powered route through the frozen per-bin `a_LB_b >= 0.85` gate at the stated operating point. Calling any of them a calibrated detection design would dress up a study that cannot support that claim.

## Two different loosenings

### A. Reduce the label budget but keep the floors

The frozen allocator's minimum for live stratum `j` is

`max(HC_MIN_PER_STRATUM, HC_MIN_PER_CELL × live_cells_j)`.

With all nine strata and all three bins live this is `max(30,10×3)=30` in every stratum, or **270 real labels**. Controls do not satisfy a real-label floor.

| Duho total-decision budget | maximum possible real decisions if every decision were real | frozen real minimum | result before allocation |
|---:|---:|---:|---|
| 30 | 30 | 270 | infeasible |
| 50 | 50 | 270 | infeasible |
| 80 | 80 | 270 | infeasible |
| 120 | 120 | 270 | infeasible |

This failure is deterministic and precedes precision, rendering, and outcome considerations. Even 270 **total** decisions would still be insufficient because known-answer controls and repeats must occupy part of the total. Keeping the inherited 200 synthetics and 150 repeats would make the floor-respecting minimum 620 decisions; preserving the entire frozen stream is 850.

### B. Loosen the floors and coverage itself

The following are the least-bad configurations at each capacity. They maximize usable cell counts while avoiding cells with only a handful of real labels. “Live” means the only population region for which calibration is claimed; omitted strata or bins cannot silently inherit the result.

| total decisions | real | synthetic controls | repeats | live strata / 9 | live bins / 3 | revised real floors needed | abandoned guarantee |
|---:|---:|---:|---:|---:|---:|---|---|
| 30 | 18 | 7 | 5 | 1 | 1 | 18 in the sole cell and stratum | no across-stratum or across-bin coverage; eight strata and two calibration bins have no calibration |
| 50 | 29 | 12 | 9 | 1 | 2 | 14 per live cell; 29 per stratum | no across-stratum coverage and one calibration bin absent |
| 80 | 47 | 19 | 14 | 1 | 3 | 15 per cell; 47 per stratum | all bins are represented, but only within one of nine strata; no morphology/quality-stratum transport guarantee |
| 120 | 71 | 28 | 21 | 2 | 3 | retain 10 per cell and 30 per stratum; allocate the 11 surplus prospectively | all bins are represented in only two of nine strata; seven-stratum coverage and the inherited population-weighted estimand are abandoned |

The 30/50 designs also require changing `N_CAL_BINS=3` for the operative estimator or defining a new estimand: v9 rejects an empty bin. The 80/120 designs can retain three output bins, but cannot retain `N_HC_STRATA=9` as a coverage claim. Selection of the one or two surviving strata must be frozen without image or χ inspection. No outcome-dependent choice or post hoc transport to omitted strata is valid.

## What survives numerically

The calculations below use exactly the v9 `accuracy_from_handcheck()` variance formula at the same realistic orientation point used in the prior arithmetic: corrected `a=0.90`, human synthetic error `epsilon=0.05`, hence raw real agreement `0.86`. For `m` synthetics, `sigma_epsilon=sqrt(.05×.95/m)`. Real labels are balanced over the live bins. The displayed lower-bound requirement is `0.85 + 1.645 sigma_ab`; values above one mean that an ordinary `a≈.90` run cannot clear the gate. Perfect observed agreement can collapse the raw-binomial term, so “not realistically clearable” is a power statement, not an algebraic impossibility for every possible dataset.

| total | `sigma_epsilon` | pooled `sigma_a` | per-live-bin `sigma_ab` | corrected point needed for `a_LB_b>=.85` | realistic clearance at `a≈.90` |
|---:|---:|---:|---:|---:|---|
| 30 | 0.0824 | 0.1167 | 0.1167 | 1.042 | no |
| 50 | 0.0629 | 0.0908 | 0.1157 | 1.040 | no |
| 80 | 0.0500 | 0.0717 | 0.1071 | 1.026 | no |
| 120 | 0.0412 | 0.0586 | 0.0873 | 0.994 | no; only near-perfect realized performance clears |

The epsilon split is consequential. Seven, 12, 19, or 28 known-answer trials are all extremely coarse estimates of a shared correction that induces covariance across bins. Moving decisions from repeats into synthetics would improve `epsilon` precision but weaken the inherited identity/self-consistency diagnostic; moving decisions from real objects into synthetics worsens already-poor per-bin sampling. There is no free reallocation at fixed total. The table uses the inherited fractions because they are the only frozen basis for a split; any optimized split would itself require a newly justified design and would not repair the missing-stratum problem.

For `A_L = beta/(2a-1)`, at `a=.90`, `A_L=1.25 beta` and first-order calibration uncertainty is

`sigma(A_L)_a = 2|beta| sigma_a/(2a-1)^2 = 3.125|beta| sigma_a`.

Equivalently, the pooled calibration alone contributes a 90% relative half-width of `1.645×2.5×sigma_a`; profile/bin use substitutes `sigma_ab` and also carries shared covariance. This excludes uncertainty in `beta`, so it is an inflation component, not the complete final error bar.

| total | pooled calibration contribution to 90% relative half-width of `A_L` | per-bin/profile contribution | comparison with inherited 500-real/200-synthetic orientation |
|---:|---:|---:|---|
| 30 | 48.0% | 48.0% | inherited: 9.1% pooled, 13.5% per bin |
| 50 | 37.4% | 47.6% | roughly 4.1× / 3.5× inherited |
| 80 | 29.5% | 44.0% | roughly 3.3× / 3.3× inherited |
| 120 | 24.1% | 35.9% | roughly 2.7× / 2.7× inherited |

If `a` approaches the floor, the denominator sensitivity worsens: relative calibration error is `2 sigma_a/(2a-1)`, so the table is already the favorable `a=.90` case. The final interval must combine this term with `beta` uncertainty and covariance; it cannot report the calibration component as the whole uncertainty.

## Claims a referee could accept

| budget | honest claim |
|---:|---|
| 30 | **Consistency/interface check only.** One stratum and one bin can test whether the task can be executed and whether gross sign agreement exists. It cannot estimate the frozen population accuracy, form a defensible corrected detection, or support a population upper limit. |
| 50 | **Stratum-local pilot only.** Two-bin behavior can reveal a large bin effect or gross failure, but the absent bin and eight absent strata prevent population calibration. Any amplitude result is exploratory and must not be called a calibrated detection or confirmatory upper limit. |
| 80 | **Three-bin, one-stratum calibration pilot.** It can test internal consistency across calibration bins in a prospectively narrowed stratum. It cannot transport to the nine-stratum accepted population, and realistic performance will fail the lower-bound gate. A null result is at most a stratum-local sensitivity statement. |
| 120 | **Coarse restricted-population upper limit or calibration feasibility result.** If the target population is prospectively redefined to the two live strata, all three bins can be represented and uncertainty propagated. Near-perfect realized calibration would be required for the frozen gate; absent that exceptional outcome, report `INCONCLUSIVE-BY-CALIBRATION`. It is not a planned calibrated-detection design for the original population. |

“Upper limit” at 120 is conditional on a predeclared two-stratum estimand, a newly validated allocator/receipt, and full propagation of calibration uncertainty. It is not permission to apply the result to the seven omitted strata. At 30–80, calling a null an original-population upper limit would overstate the sampling support.

## Break point

**Below 120 total decisions there is no standalone result worth publishing as the scientific answer.** At 80, all three bins can be kept only by collapsing to one stratum, while per-bin `sigma_a≈0.107` makes the calibration lower bound practically unattainable at `a≈.90`. The 30 and 50 cases lose bins as well as strata. They may be documented as methods pilots or feasibility failures, but they cannot answer the preregistered question.

The 120 case is itself only marginally publication-worthy as a transparent restricted-population upper limit or negative calibration result. It is **not** a breakpoint at which the original detection claim becomes defensible: its per-bin `sigma≈0.087` requires a corrected point near 0.994, and it omits seven strata. A defensible original-population calibration returns to the floor-respecting scale—at least 270 real labels plus controls, and materially more for realistic gate clearance—not to any budget in this table.

## Honest verdict

There is no defensible small-`N` design within Duho's 30–120 total-decision capacity that preserves a calibrated confirmatory answer for the frozen population. The apparent savings come from deleting population coverage and starving the shared-error estimate; they do not merely make the same estimator less precise. At 120, a narrower pilot/upper-limit study can be honestly preregistered, but that is a different estimand and a weaker paper. If the intended claim remains a calibrated detection over the inherited nine-stratum population, the loosening path is **not defensible**.

SEAT: CODEX
VERSION: LOOSEN-V1
VERDICT: NOT-DEFENSIBLE
COUNT: 4
