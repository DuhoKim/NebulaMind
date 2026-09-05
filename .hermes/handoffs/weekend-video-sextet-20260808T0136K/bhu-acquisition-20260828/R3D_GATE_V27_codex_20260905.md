ACCESS_SHA=3e5b6979930535e5cb09c8eb6d3f6f3c7fefd47c6df8697cf2d384124c753234
GATE=PREREG_SOUND_WITH_REPAIRS

1. OUTCOME CLASSES

Sound. The filing classes are exhaustive and mutually exclusive under the document's procedural decision rule: class 3 is exclusively the limb-A exit; classes 1, 2, and 4 exhaust limb B through the partition of admissible readings into P, Z, and I; and classes 5 and 6 cover source/procedure/split blockage and persistent control failure in the stated order. Although the physical predicate underlying class 3 entails the no-floor consequence used in class 4, no run can file both because limb A stops before the limb-B partition. I could construct neither a result fitting two fileable classes nor a terminal result fitting none.

An inconclusive scientific result is genuinely reachable. Concrete example: the completion-free reading permits M approaching zero, while an admissible one-completion reading yields a 10 kg positive floor. Then P and Z are both non-empty, so class 2, DYM_FLOOR_UNDERDETERMINED, files. Non-scientific inconclusive states are also reachable through class 5 (for example, a manifest digest mismatch) and class 6 (a reached control failing again on its prescribed rerun).

2. CONTROLS

Defect. C5 has printed-command evidence, but it has no frozen expected interpreter digest or expected version values and no explicit PASS/FAIL comparison. Thus the purported pin can be passed by a seat's unexplained classification of its own output; printing a digest is not the same as pinning identity.

Verbatim sentence: "- **C5 — harness, LIVE.** Execute and print the three commands of §9. This control emits `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN` from the run actually executed; the token is a result to be recorded, not a claim this document makes about itself."

Exact replacement: "- **C5 — harness, LIVE.** Execute and print the three commands of §9. The frozen expected outputs are `/usr/bin/python3 --version` = `Python 3.9.6`, `/usr/bin/python3 -c \"import sympy; print(sympy.__version__)\"` = `1.14.0`, and `shasum -a 256 /usr/bin/python3` digest = `b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9`. `C5_HARNESS_PINNED=PASS` exactly when all three commands exit 0 and their printed values equal these frozen values; otherwise it is `FAIL`. It is `NOT_RUN` only when explicitly unreached under §9. The three captured outputs, exit codes, and comparisons are the required artefact; a claimed pass without them fails. This control emits exactly `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN` from the run actually executed; the token is a result to be recorded, not a claim this document makes about itself."

All other controls are sound on the requested criteria. C0, C1, C2, C3, C4, and C5b require printed exhibitions, digests, ledgers, captured output/algebra, or complete path tables rather than assertions. Every control has an exact `PASS|FAIL|NOT_RUN` code in §9. Early blocking and explicitly unreached limbs assign later controls `NOT_RUN`; reached C3 exit 2 is expressly treated as failure and rerun once. The literal C3 script-hash command, literal C3 invocation, and all three literal C5 commands are executable as written. I executed them; all exited 0. The C3 script digest matched its declared pin. The C5 defect is not shell executability but the missing frozen comparison rule.

C3 deletion-probe execution, explicitly:

(a) Yes. I executed the literal command printed in §5 exactly as printed.

(b) Working directory: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828`

(c) Exit code: `0`

Exact stdout:

```text
target            : M
retained (all)    : ['eq_src', 'inj_ok']
DELETED (pinned)  : ['eq_src']
injected relations: [('inj_ok', 'Eq(r0, 2*G*M/c**2)')]
§2b constants     : ['hbar', 'c', 'G']
with everything   : c**2*r0/(2*G)   (indeterminate: free in ['r0'])
pinned DELETED    : c**2*r0/(2*G)   (indeterminate: free in ['r0'])
VERDICT: no unique floor without the source-pinned equations -> not circular
C3_DELETION_PROBE=PASS
```

3. CIRCULARITY

Sound. The lane-authored pattern is forbidden from the census, inclusion/exclusion decisions, completion ledger, limb choice, and scientific-class selection. It enters only after a positive-floor class has independently filed, through C6. The census accounts for every nonblank line, separately lists every displayed or numbered equation, restricts exclusions to fixed reason codes evidenced by source text, and treats disagreement or missing evidence as UNRESOLVED and blocking. A contrary mass/core/horizon relation cannot quietly disappear without either breaking the line reconciliation/equation list or generating an inspectable exclusion row. C3 then independently tests whether an injected relation alone sustains a unique determinate floor.

4. THE FALSIFIER

C6 can return FAIL in 4 declared terminal outcome classes: DYM_FLOOR_DERIVED and DYM_FLOOR_UNDERDETERMINED directly; DYM_SOURCE_BLOCKED after an engaged condition-3 UNDECIDED result; and R3D_NO_CLASS after an engaged C6 is followed by a persistent control failure. It is initially engaged from 2 classes.

Condition 1: PASS is reachable with a filed floor of 10 kg. Substantive FAIL is not reachable on any valid scientific-class path because positive-floor membership requires a mass; the document correctly labels this ENTAILED. Its integrity-check FAIL input is a malformed filing that calls the dimensionless ratio M/m_P the floor. Condition 1 is the one condition that cannot fail on any valid path.

Condition 2: PASS is reachable with M_floor = 3 sqrt(hbar c/G), with 3 derived by a manifest-source equation and hbar, c, G from §2b. FAIL is reachable with M_floor = alpha sqrt(hbar c/G), where alpha terminates in an unsupported choice rather than a manifest equation or §2b.

Condition 3: PASS is reachable with M_floor = 3 sqrt(hbar c/G), which has no non-§2b free symbol. FAIL is reachable with M_floor = alpha sqrt(hbar c/G), with alpha free.

Condition 4: PASS is reachable when every held-constant quantity has a deriving passage in the C2 artefact; concretely, M_floor = 3 sqrt(hbar c/G) with no additional held-fixed model parameter. FAIL is reachable for M_floor = alpha sqrt(hbar c/G) when alpha is held at 3 by choice and no manifest passage derives its constancy.

Condition 5: PASS is reachable with the point floor 1.0e15 kg, which overlaps none of the three numerical comparator intervals. FAIL is reachable with 2.0e11 kg, which overlaps the Hawking-evaporation interval [1.729e11, 5.190e11] kg. Additional declared FAIL directions are 2.176434e-8 kg for the Planck interval and 5.0e30 kg for the stellar-collapse interval.

5. RE-RUN GUARD

Sound. The design explicitly forbids assuming K6 repeats and leaves DYM_FLOOR_DERIVED reachable. Concrete positive case: the completion-free relations yield the non-empty allowed mass set [10 kg, infinity), and every admissible reading yields that same infimum; then P is non-empty and unanimous while Z and I are empty, so class 1 files.

6. FAIRNESS

Sound. Every operative negative scientific finding uses "unreproduced from the stated inputs": limb A and class 3 use that wording for the relation; class 4 uses it for the positive floor; and the inconsistent-input branch uses it for a consistent solution and positive lower bound. The word "error" is not used as an operative scientific verdict.

7. STALL

Sound. Every symbolic operation has a 120-second cap and a bounded second fallback; failure of that fallback routes to DYM_SOURCE_BLOCKED. Source/proposition failures, control failures, and seat disagreements all have explicit terminal routing. The split rule covers differing classes, C6 results, floor values/formulas, and class-4 families; an unresolved three-way split files DYM_SOURCE_BLOCKED. No terminal path is left without a fileable class.

R3D_V27_GATE_COMPLETE
