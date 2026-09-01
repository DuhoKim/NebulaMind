## 7. Discussion

The preregistration and auditing machinery deployed in this study arrested several failure modes that ordinary software development and peer review typically permit. However, this discipline imposed substantial costs and revealed the limits of cryptographic rigidity when applied to operational science. The outcomes demonstrate both the value of adversarial pre-execution verification and the necessity of aligning human resources with frozen constraints.

### 7.1 What the machinery caught

The design's formal verification caught systemic logic and custody errors before they could infect a measurement. Crucially, the audit revealed a dependency cycle in the frozen text itself: the robustness gate required a receipt whose inputs could only exist after the gate it blocked. In execution, a robustness rehearsal evaluated 5,049 = 99 x 51 cells with 0 flips, but this was explicitly conducted on fixture mask and fixture calibration only, and therefore could not discharge the frozen edge required for real labels.

Custody controls also intercepted operational defects. Two separate go-live attempts were voided by post-hoc verification before any downstream consumer could accept them. The first involved a clock-unit error against a frozen nanosecond specification. The second attempt exposed a failure in cryptographic custody: sealed materials bound a public key that could not verify its own signature. Neither error would have been caught by conventional pipeline repetition, yet the consumption barrier successfully halted both.

Furthermore, the audit exposed test fixtures that passed for incorrect reasons. A mocked boundary refusal proved the mock's behaviour rather than the operating system's constraint, and a strict-equality closure test was implemented using the wrong criterion. Review of the prose text found paraphrase-versus-quote failures, where statements claimed as verbatim quotations were instead interpretive summaries. These findings demonstrate that unverified test suites and informal prose can actively obscure pipeline defects.

### 7.2 The honest costs and rigidity

The cost of this adversarial discipline was severe, and the resulting rigidity created procedural friction. When a frozen executable's date guard directly contradicted a principal ruling, the system's immutability meant the contradiction could not be silently resolved. The ruling had to be explicitly recorded as a disclosed supersession.

Additionally, the testing apparatus itself required extensive maintenance; several fixtures were found to be defective and demanded their own iterative repair rounds. The known-debt appendix documents the scale of this effort: out of 703 findings across 84 seat-rounds, 334 findings were retained as standing pre-convention audit debt, alongside 177 repaired and 192 mapped-by-citation items.

For future teams adopting this framework, the primary operational lesson is to settle the human calibration resource before freezing a design that requires it. This study defined a minimum real-label calibration floor of 270 decisions, requiring a panel of at least 38 people at a cap of 50 to satisfy the 1,860 decisions demanded by the three-person design. By freezing a design whose calibration term it could not practically obtain, the project was forced to halt.

### 7.3 Generalisation

The methods developed here transfer readily to other measurements vulnerable to sign or orientation conventions, particularly those susceptible to analyst freedom in specifying geometry or mapping coordinates. By forcing the sign anchor and counterfactuals to be frozen and audited before any labels are read, researchers can eliminate the silent convention flips that often plague spatial analyses.

However, these benefits are specific to the measurement of handedness and similar orientation-dependent phenomena. Preregistration is not a universal remedy. It cannot substitute for physical calibration, nor can cryptographic seals repair an under-resourced operational plan. It simply ensures that the constraints, once declared, are immutably enforced, forcing a project to halt rather than publish an uncalibrated result.

SEAT: AGY
VERSION: SECTION7-V1
VERDICT: DRAFTED
COUNT: 577
