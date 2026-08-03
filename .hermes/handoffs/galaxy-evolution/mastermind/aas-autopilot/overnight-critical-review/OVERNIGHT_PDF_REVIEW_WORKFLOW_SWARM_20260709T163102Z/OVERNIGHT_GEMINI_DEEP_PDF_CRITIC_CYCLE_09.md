# OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_09

## 1. Status
**OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_09 status: ISSUES_FOUND**

The candidates are in an excellent, highly-disciplined state regarding data claims and boundaries. However, several critical inconsistencies carried over from Cycle 8 regarding table-text mismatch, imprecise titling, and generic figure captions.

## 2. Files/Paths Inspected
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_09_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`

## 3. Ranked Findings

**Blockers (0)**
None. Real-data discipline is strict.

**Major (4)**
1. **Paper 08 Table Mismatch**: Table 1 displays the 60,000-row selection cascade but completely omits the final step subsetting to the 6,729 "massive quenched or transitioning galaxies" analyzed in the paper. The table is detached from the paper's actual sample.
2. **Paper 04 Title Terminology**: The title uses "high-excitation AGN," which conflicts with the text's "BPT-selected optical AGN." "High-excitation" risks confusion with radio-mode HERGs and should be aligned with the optical baseline focus.
3. **Paper 04 Abstract Omission**: The abstract states it "records their median sSFR" but does not supply the actual value (-11.53), omitting the paper's key measured statistic.
4. **Papers 02-09 Generic Captions**: `fig-topic.pdf` captions remain generic stubs (e.g., "The figure summarizes the cached optical result used for target definition") and lack the specific numbers/axes detailed in the text.

**Minor/Improvement (1)**
1. **Missing `\software{}` commands**: AAS journals strongly prefer a `\software{}` macro listing core packages (e.g., astropy, matplotlib) at the end of the manuscript.

## 4. Exact Feed for PDF-Writing Pilot

**Action 1: Fix Paper 08 Table 1 Selection Cascade**
*File*: `08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
*Target*: `\tablecomments{...}` in `\enddata` of Table 1.
*Replacement block*:
```tex
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
Massive quenched or transitioning subset & -- & 6,729 & -- \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. The final row defines the specific 6,729-galaxy subset used in this optical baseline.}
```

**Action 2: Fix Paper 04 Title and Abstract**
*File*: `04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
*Replacement block (Title)*:
```tex
\title{SDSS BPT-selected optical AGN denominator for outflow escape tests}
```
*Replacement block (Abstract)*:
```tex
\begin{abstract}
We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 \(\pm\) 0.001) and finds their median log sSFR is $-11.53$, providing a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
\end{abstract}
```

**Action 3: Replace Generic Figure Captions (Papers 02-09)**
*Target*: Replace `\caption{SDSS DR17 optical denominator/proxy diagnostic... The figure summarizes the cached optical result...}` in each respective file.

*Paper 02*:
```tex
\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure summarizes the equal-count density-quartile split, where the high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
```

*Paper 03*:
```tex
\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure highlights that among massive, low-sSFR objects, the BPT-AGN fraction is 0.607, providing a duty-cycle denominator for future X-ray/radio studies.}
```

*Paper 05*:
```tex
\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure demonstrates the environment-stratified target set, with the optical AGN fraction rising to 0.509 $\pm$ 0.012 in the high-density quartile of massive hosts.}
```

*Paper 06*:
```tex
\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows the high-mass tail ($\log(M_\star/M_\odot)>11.0$) where the quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520.}
```

*Paper 07*:
```tex
\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure illustrates how varying optical tracer definitions yields AGN candidate prevalence ranging from 0.136 to 0.418 within the same denominator.}
```

*Paper 08*:
```tex
\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure isolates the 6,729 massive quenched/transitioning galaxies, revealing an optical BPT AGN fraction of $0.549 \pm 0.006$.}
```

*Paper 09*:
```tex
\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure maps quenched fractions and optical AGN incidence across 15 mass-redshift cells for simulation forward-modeling.}
```

## 5. Real-Data / Source / Citation Audit
- All data claims accurately scope out missing observational modes (group/halo catalogs, escape velocities, multiphase traces) and explicitly frame current outcomes as SDSS optical denominators.
- No synthetic or mock data is injected.
- Citations appropriately delineate simulation suites and observational proxies (e.g., TNG/EAGLE vs. iMaNGA in Paper 09).

## 6. Workflow / System Notes
The current automated review-and-fix swarm is highly robust against overclaims but has struggled with localized consistency checks (e.g., ensuring a paper's abstract measurement perfectly mirrors its main text findings, and ensuring universally applied shared components—like the cascaded Table 1—are properly customized when a specific paper's methodology diverges). Enhancing the local integration script to parse and assert table/text alignment might circumvent iterative reviewer churn.

## 7. Safety Ledger
- Write operations restricted to overnight run root reports: CONFIRMED.
- No public/live frontend or static root edits: CONFIRMED.
- No database/API modifications or page publications: CONFIRMED.
- No deploy/restart executed: CONFIRMED.
- No git commits/pushes/history modifications: CONFIRMED.
- No cron/billing/OAuth modifications: CONFIRMED.
- No external manuscript submissions: CONFIRMED.
