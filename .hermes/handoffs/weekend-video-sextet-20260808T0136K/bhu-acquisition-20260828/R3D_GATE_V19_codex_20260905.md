ACCESS_SHA=28a97c1a0522d6476cee6897470d272f8f7cd92ccfae332bc0132caa2fd02b54
GATE=PREREG_SOUND_WITH_REPAIRS

1. OUTCOME CLASSES

SOUND. The six declared terminal classes are exhaustive and mutually exclusive under the operative routing rule. Class 3 is exclusively the limb-A exit; classes 1, 2, and 4 are exclusively limb-B results and partition that limb through the disjoint sets P, Z, and I; class 5 covers unread, mismatched, unresolved, or undecidable source-dependent states; and class 6 is available only after class 5 has been ruled out and a required control has failed persistently under the seat rule.

Concrete witnesses are available for every class: (1) a completion-free allowed set M >= 10 kg, with every admissible reading yielding the same infimum; (2) a completion-free reading yielding M >= 10 kg and another admissible reading yielding M >= 20 kg, or permitting M -> 0; (3) a completed census from which neither a size-mass relation nor any mass bound is reproduced, causing the limb-A exit; (4) a printed relation admitting every M > 0, hence masses approaching zero; (5) a manifest digest mismatch or an UNRESOLVED required proposition; and (6) readable, resolved sources followed by the same required control failing on both permitted attempts. No witness fits two classes once the limb and terminal-state routing rules are applied, and none is homeless.

An inconclusive scientific result is genuinely reachable as class 2, for example when two admissible readings yield different positive floors. The two non-scientific waiting states are also reachable.

2. CONTROLS

REPAIR REQUIRED. C0, C1, C2, C3, C4, C5, C5b, and C6 each name an exact PASS/FAIL/NOT_RUN code. Their pass claims require printed artefacts rather than assertion: an exhibition table, computed identities, the complete census and completion ledger, captured deletion-probe output, benchmark algebra and premises, live command output, a complete path table, and the per-condition C6 artefacts. Section 9 explicitly assigns NOT_RUN to later controls never engaged after an earlier terminal block and preserves actual results for controls already engaged. Limb A separately gives the reached/unreached dispositions.

The three literal C5 commands are executable as printed; I executed each successfully. The literal C3 invocation is not executable according to its stated interface: shell syntax treats `<relations.json>` as stdin redirection and passes no `relations.json` positional argument, whereas the sentence says the JSON is supplied to the script by that invocation.

Verbatim sentence: “The probe is the committed script `r3d_c3_deletion_probe.py`, invoked as `python3 r3d_c3_deletion_probe.py <relations.json>` — the JSON carries `target`, `symbols`, the §2b `constants` list, and one record per relation with `id`, `origin` (`SOURCE_PINNED` or `INJECTED`) and `expr`.”

Defect: the angle brackets have shell semantics, so the printed command redirects stdin from a file and does not pass the filename as an argument. A seat executing it literally does not execute the promised positional-file interface.

Exact replacement: “The probe is the committed script `r3d_c3_deletion_probe.py`, invoked as `python3 r3d_c3_deletion_probe.py relations.json` — the JSON file `relations.json` carries `target`, `symbols`, the §2b `constants` list, and one record per relation with `id`, `origin` (`SOURCE_PINNED` or `INJECTED`) and `expr`.”

3. CIRCULARITY

SOUND. The lane pattern is barred from inclusion, exclusion, and outcome selection and enters only after a positive-floor class has been selected independently. The census accounts for every non-blank source line, separately enumerates every numbered or displayed equation, requires verbatim locators for every disposition, restricts exclusions to declared reason codes demonstrated by source text, and turns disagreement into UNRESOLVED rather than absence. A contrary printed relation therefore cannot be quietly omitted without breaking the line reconciliation or equation list. C2 also forces every considered premise or relation into the printed ledger. C3 tests whether an injected relation alone survives deletion of the source-pinned equations. No replacement.

4. THE FALSIFIER

C6 can return FAIL in 4 of the 6 declared terminal outcome classes. It is initially engaged in classes 1 and 2; an engaged FAIL can remain with either class, travel to class 5 if condition 3 is UNDECIDED after fallback, or travel to class 6 after a persistent required-control failure. This distinguishes initial engagement (2 classes) from the terminal classes in which FAIL can be recorded (4 classes).

Condition 1 can PASS: file a floor of 10 kg. It can FAIL only as a filing-integrity rejection: file the dimensionless ratio 2 as the purported floor. It cannot fail on any valid scientific path because membership in either positive-floor class already requires a mass; it is substantively ENTAILED.

Condition 2 can PASS: file M_min = sqrt(hbar*c/G), with every constant terminating in §2b. It can FAIL: file M_min = A*sqrt(hbar*c/G), where A = 2 is introduced merely by choice and has no manifest or §2b terminus.

Condition 3 can PASS: file M_min = sqrt(hbar*c/G), which contains no non-§2b free symbol after substitution. It can FAIL: file M_min = lambda*sqrt(hbar*c/G), with lambda algebraically independent and unfixed.

Condition 4 can PASS: hold only G, hbar, and c constant, each supplied by §2b, with any construction-specific fixity supported by a reproduced manifest passage. It can FAIL: obtain the floor only by holding an otherwise free core density rho_0 constant without a manifest derivation of that constancy.

Condition 5 can PASS: file the point floor 1.0e15 kg, which overlaps none of the three finite comparator intervals. It can FAIL: file 2.1764343e-8 kg (Planck comparator), 2.0e11 kg (Hawking comparator), or 5.0e30 kg (stellar-collapse comparator); each overlaps its named interval.

Thus conditions 2, 3, 4, and 5 each have both valid substantive PASS and FAIL paths. Condition 1 has a valid PASS but no valid substantive FAIL path; its only FAIL input is a malformed filing, as the document expressly discloses. No replacement.

5. RE-RUN GUARD

SOUND. Section 6 expressly prohibits assuming that K6 repeats, and class 1 is genuinely reachable from a completion-free non-empty allowed mass set having a unique positive infimum with all admissible readings agreeing. No replacement.

6. FAIRNESS

SOUND. Every operative negative scientific clause uses “unreproduced from the stated inputs”: the limb-A exit and class 3 use it for the missing relation or bound; class 4 uses it for a positive floor and, in the inconsistent case, for a consistent solution and positive lower bound. “DYM_NO_*” strings are class identifiers, not assertions of source error. Blocking and control-failure clauses are non-scientific procedural states. No replacement.

7. STALL

SOUND. Each symbolic operation has a 120-second cap and a second bounded fallback; an absent, timed-out, unparsable, or non-decisive fallback files class 5. Persistent control failure after class 5 is ruled out files class 6. Seat disagreement invokes the third seat, and all-three disagreement or inability to decide files class 5. Early blocks explicitly mark later, unengaged controls NOT_RUN. C0 failure prevents freeze rather than beginning a run. Once a run begins, no terminal path lacks a fileable declared class. No replacement.

R3D_V19_GATE_COMPLETE
