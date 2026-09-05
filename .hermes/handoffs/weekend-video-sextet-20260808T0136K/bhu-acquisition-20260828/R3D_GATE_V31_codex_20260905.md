ACCESS_SHA=aa3b184192503205229ea2a7428f7145741757636fe6ccd7fd0d834ebb108e62
GATE=PREREG_SOUND_WITH_REPAIRS

1. OUTCOME CLASSES

SOUND. The six declared terminal classes are exhaustive and mutually exclusive as an operational decision procedure. Limb A alone files class 3. Limb B contains at least the completion-free reading, and `P`, `Z`, and `I` partition every admissible reading; classes 1, 2, and 4 then partition Limb B. Classes 5 and 6 are downstream non-scientific terminals with an explicit priority: class 6 is considered only after class 5 is ruled out. I could construct neither a result that files two classes nor a terminal result fitting none. An inconclusive result is genuinely reachable: for example, a completion-free reading that permits masses approaching zero and an admissible completion that yields a 10 kg floor gives nonempty `P` and `Z` and files class 2, `DYM_FLOOR_UNDERDETERMINED`; unreadable or unresolved required evidence reaches class 5.

2. CONTROLS

SOUND. C0 through C6 each name an exact `PASS|FAIL|NOT_RUN` code. Each claimed pass requires a printed artefact rather than assertion alone. Early terminal blocks explicitly give later, never-engaged controls `NOT_RUN`, while engaged controls retain their actual result. Limb A and direct classes 2 and 4 state their special dispositions. The literal commands are executable as written: their interpreters and material paths are absolute, and the C3 command contains no placeholder or shell metacharacter.

C3 deletion-probe execution requested by this gate:

(a) Yes. I executed the literal command exactly as printed.

(b) Working directory: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828`.

(c) Exact stdout:

```
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

Exit code: `0`.

This execution used the `_c3_relations.json` already present at the command's absolute path; I did not create or alter that input, so this gate execution establishes literal-command executability and the result for that existing negative-control input, not a study-derived relations file.

3. CIRCULARITY

SOUND. The lane pattern is barred from inclusion, exclusion, and outcome selection and enters only after a positive-floor class is independently reached. The census accounts for every nonblank line and separately enumerates every displayed or numbered equation; exclusions require a declared code, locator, and verbatim source text, and disagreements become `UNRESOLVED` rather than absence. The completion set is closed and mechanical. A contrary printed relation cannot be quietly omitted while C2 passes: it must receive a visible disposition and appear in the equation list where applicable. C3 then tests whether an injected relation alone carries a unique floor.

4. THE FALSIFIER

`C6_BREAKER_TEST=FAIL` can be recorded in 4 of the 6 declared terminal outcome classes: classes 1 and 2, plus class 5 after condition 3 remains undecided, and class 6 after an engaged C6 is followed by persistent control failure.

- Condition 1 PASS: file a floor `M_min = 10 kg`. FAIL: file the dimensionless ratio `M/M_sun = 2` as the floor. The latter is a malformed filing, not a valid scientific-class path.
- Condition 2 PASS: `M_min = sqrt(hbar*c/G)`, with every constant in §2b. FAIL: `M_min = alpha*sqrt(hbar*c/G)` where `alpha=3` is merely chosen and has no manifest or §2b terminus.
- Condition 3 PASS: `M_min = sqrt(hbar*c/G)`. FAIL: `M_min = lambda*sqrt(hbar*c/G)` with free non-§2b symbol `lambda` surviving simplification.
- Condition 4 PASS: a floor whose held quantities are all tied to printed deriving passages, for example the completion-free `sqrt(hbar*c/G)` input above. FAIL: `M_min = sqrt(rho0)*sqrt(hbar*c/G)` with `rho0` held fixed by choice and no manifest passage deriving its fixity.
- Condition 5 PASS: the point floor `1.0e15 kg`, which overlaps none of the three finite comparator intervals. FAIL: the point floor `2.0e11 kg`, which overlaps the Hawking interval `[1.729e11, 5.190e11]`.

Condition 1 cannot substantively FAIL on any valid path: membership in either positive-floor class already requires a mass. It can reject only a malformed filing and is correctly marked `ENTAILED`.

DEFECT. Section 5a contains a stale, unscoped count immediately after correctly distinguishing initial engagement from terminal recording.

Verbatim sentence: “**Reachable: 2. `DYM_FLOOR_COMPLETION_DEPENDENT` IS A DEAD CLASS** — shown unreachable by seat exhibitions on **both V11 and V12**, for two different reasons.”

Defect: `DYM_FLOOR_COMPLETION_DEPENDENT` is not one of V31's six declared classes, and “Reachable: 2” has no stated object. In the operative falsifier subsection it can be misread as contradicting the required current answer of four declared terminal classes, even though the preceding paragraphs correctly explain that two is the number of initial engagement classes.

Exact replacement: “**The two initial-engagement classes are both reachable. `C6_BREAKER_TEST=FAIL` can ultimately be recorded in the four declared terminal classes named above; no retired class is counted.**”

5. RE-RUN GUARD

SOUND. The design expressly forbids assuming K6 repeats. The completion-free reading can yield a common positive floor with `Z` and `I` empty, so `DYM_FLOOR_DERIVED` is genuinely reachable. No replacement.

6. FAIRNESS

SOUND. Every operative negative scientific conclusion uses “unreproduced from the stated inputs,” including the renamed class tokens and the mutually inconsistent-relations clause. I found no operative use of “error” or an unqualified claim that the source contains no relation or floor. No replacement.

7. STALL

SOUND. Every bounded symbolic procedure has a timeout route; absent, timed-out, unparsable, or non-decisive fallbacks file `DYM_SOURCE_BLOCKED`. Control failures have retry and terminal routing, and seat splits have adjudication plus a terminal fallback. Every path files one declared class; there is no terminal state with no fileable class. No replacement.

R3D_V31_GATE_COMPLETE
