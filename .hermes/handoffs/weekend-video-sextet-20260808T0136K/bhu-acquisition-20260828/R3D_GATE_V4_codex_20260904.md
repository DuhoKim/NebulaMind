ACCESS_SHA=19843627fd6b3ce7aaa808eebe50c202c41d3d3ac8586d8b69445ac0aa3c6bd6
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES

Defect. The prompt calls these six classes, but §4 declares seven. More importantly, classes 6 and 7 can overlap: an unread source both files `DYM_SOURCE_BLOCKED` under C1/C2 and can make a required control fail twice, satisfying the first sentence of class 7. Precedence appears only inside class 7 and is narrower than the overlap because it says “whenever unread or unresolved evidence caused the failure,” while class 6 says merely that a source “cannot be read.” Quote: “`R3D_NO_CLASS` — after applying `DYM_SOURCE_BLOCKED` and the seat-split rule of §9, a required control still fails after two attempts **in any seat**.” Exact replacement: “**R3D_NO_CLASS** — only after ruling out `DYM_SOURCE_BLOCKED`: if no evidence is unread or unresolved and, after applying the seat-split rule of §9, a required control still fails after two attempts in any seat, file `R3D_NO_CLASS`; otherwise file `DYM_SOURCE_BLOCKED`.”

The scientific classes 1–5 are otherwise mutually exclusive under their stated completion, zero-limit, and precedence tests. Inconclusive outcomes are genuinely reachable through `DYM_SOURCE_BLOCKED` and `R3D_NO_CLASS` once the overlap above is repaired.

2. CONTROLS

Sound. C1–C6 and C5b each have an exact code; C1–C4 require printed artefacts rather than a claimed pass, C5/C5b require live output/path output, and C6 specifies artefacts. The global §9 rule records every unreached control as `NOT_RUN`. No replacement.

3. CIRCULARITY

Defect. The literal-string census cannot establish the promised universe of “every equation or sentence”: a relation written only with symbols such as `r_0`, `r_g`, `rho_0`, or `m(r)` (or with an unlisted synonym such as “energy density” or “gravitational radius”) can contain none of the eleven literal strings. Both seats may quietly omit it, and it will appear in neither the search output nor an `EXCLUDED` row. Quote: “For each manifest source the seat **prints the complete output of a literal, case-insensitive string search** of that source's extracted text for each of these eleven terms — `core`, `scale`, `density`, `mass`, `mass function`, `radius`, `horizon`, `matching`, `surface`, `regular`, `de Sitter` — and **every hit appears either as its own census row, or is cited inside a `DUPLICATE` row naming the row that covers it.**” Exact replacement: “For each manifest source the seat prints the complete extracted text with stable line numbers and assigns every nonblank line exactly one census disposition: its own included or excluded row, or a `DUPLICATE` row naming the covering row; equations and their defining/context lines are treated as one explicitly bounded block, so every source line is accounted for even when it contains only symbols or an unlisted synonym.”

Thus the lane-authored pattern is verbally barred, but the enumeration mechanism still permits a shared omission that can steer limb selection and outcome selection toward the pattern. The repair again overclaims supplied exhaustiveness while supplying only a keyword search.

4. THE FALSIFIER

Defect. Conditions 2 and 4 are not decidable without consulting documents outside this preregistration: condition 2 requires a full citation chain into source equations, and condition 4 requires a source line for every fixed quantity. The procedures are also not bounded by a maximum chain depth or a rule for an unavailable citation. Quote: “build the citation chain for each constant to its origin”. Exact replacement: “Using only the verbatim source passages reproduced in the frozen C2 artefact, trace each constant through at most the relations in those passages; PASS only if every trace terminates in a reproduced source equation or a §2b constant, and otherwise FAIL.” Quote: “list each quantity held constant and locate its derivation”. Exact replacement: “List every quantity held constant in the frozen derivation and, using only the verbatim source passages reproduced in the C2 artefact, identify its deriving passage; PASS only if every row has such a passage, and otherwise FAIL.”

Defect. Condition 3 says to “attempt” recovery but supplies no finite operation set or decision algorithm, so failure to recover is not a bounded proof. Quote: “replace **every** parameter by a free symbol and attempt to recover the printed number”. Exact replacement: “Replace every non-§2b parameter by an algebraically independent symbol, simplify the final expression once with the pinned SymPy version under the §9 120-second cap, and PASS exactly when the simplified expression contains none of those symbols; on timeout execute the specified fallback, and if it does not decide this proposition, file the applicable non-scientific class.”

Defect. That replacement also exposes a polarity error in the existing condition: a parameter-free prediction should permit recovery of the number with no parameter chosen, whereas the present pass criterion requires recovery to fail. Quote: “recovery **fails** with no parameter chosen”. Exact replacement: “the printed number is recovered with no non-§2b parameter chosen”.

Defect. Condition 5 cannot be executed consistently with the binding manifest. Two comparator sources are outside §2a, and one is falsely labelled as being in it. Reading either triggers `DYM_SOURCE_BLOCKED`, while not reading it defeats the mandated provenance/comparison. Quote: “`2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt` (manifest §2a)”. Exact replacement: “value and provenance passage reproduced in this frozen document; no external comparator artefact is read”. Quote: “entry 31's bar, `NS_MASS_WATCH_PREREG_20260902.md`”. Exact replacement: “value and provenance passage reproduced in this frozen document; no external comparator artefact is read”. The actual provenance passages must be supplied here; merely inserting these replacement labels without those passages would defer content again.

Defect. The comparator set is not complete enough to justify the universal phrase “any standard model”: it lists three mass scales and a ΛCDM null, without a closed rule defining the eligible standard-model set. The tolerance is asserted from the total span and is not tied to measurement uncertainty or a falsification criterion; one decade can arbitrarily turn a nonidentical prediction into a “shared” number. Quote: “agreement within one order of magnitude on a scale that spans about sixty.” Exact replacement: “For this preregistration, condition 5 quantifies only over the three finite numerical comparator hypotheses enumerated in this table; equality means overlap of frozen, explicitly supplied prediction intervals, and the table supplies each interval and its derivation.” Until those intervals and derivations are actually written into this document, content is still deferred rather than supplied.

5. RE-RUN GUARD

Sound. The design expressly forbids assuming K6 repeats, and class 1 is reachable before C6; C6 tests rather than preconditions `DYM_FLOOR_DERIVED`. No replacement.

6. FAIRNESS

Defect. The mandated wording is not held everywhere: terminal class names assert `NO_SIZE_MASS_RELATION` and `NO_POSITIVE_FLOOR`, and class 4 instructs the report to state a contradiction rather than consistently framing it as unreproduced. Quote: “**DYM_NO_SIZE_MASS_RELATION**”. Exact replacement: “**DYM_SIZE_MASS_RELATION_UNREPRODUCED**”. Quote: “**DYM_NO_POSITIVE_FLOOR**”. Exact replacement: “**DYM_POSITIVE_FLOOR_UNREPRODUCED**”. Quote: “file here and report the contradiction.” Exact replacement: “file here and report that mutually consistent relations, and therefore a positive floor, were unreproduced from the stated inputs, then print the encountered contradiction.” All references to the old codes must be mechanically updated.

7. STALL

Defect. The fallback table is present, but its first row names “bracketed bisection” while specifying `mpmath.findroot`, which is not a guaranteed bracket-preserving bisection procedure; therefore it can fail without deciding even when a bracket exists. Quote: “bracketed bisection on sign changes (`mpmath.findroot`)”. Exact replacement: “bracket-preserving bisection on each detected sign-change interval (`scipy.optimize.bisect`, with its version and executable identity printed by C5)”.

The document nevertheless assigns a fileable state to timeouts, fallback failures, and all enumerated seat disagreements. Subject to the class-6/class-7 overlap in finding 1, there is no terminal path with literally no named class.

Additional round-specific judgment: the source manifest is byte-binding for the four study sources and bars alternative artefacts, but C6 itself violates that manifest through two comparator citations. The five breaker rules are not self-contained or fully bounded (conditions 2–4), and condition 3 has reversed logic. The comparator set is neither closed against the condition's universal wording nor supported by defensible uncertainty-based tolerances. The census does not distinguish an omitted symbol-only or synonym-only relation from one never surfaced; only surfaced keyword hits are distinguishable from excluded rows. Accordingly, V4 again defers essential provenance, interval, and exhaustiveness content instead of supplying it.

R3D_V4_GATE_COMPLETE
