ACCESS_SHA=19843627fd6b3ce7aaa808eebe50c202c41d3d3ac8586d8b69445ac0aa3c6bd6
GATE=PREREG_UNSOUND

1. OUTCOME CLASSES — NOT mutually exclusive as written; "admissible completion" is never defined, and class 1 has no guard against it.

   Verbatim (class 1): "1. **DYM_FLOOR_DERIVED** — a unique positive floor follows from the printed relations with no added completion."
   Verbatim (class 2): "the printed relations admit **at least two positive but unequal floors** under admissible completions, **and no admissible completion permits masses approaching zero**."
   Verbatim (class 4): "**This class takes precedence over `DYM_FLOOR_UNDERDETERMINED`.**"

   Defect: a real result fits classes 1 and 2 simultaneously. The printed relations fix a unique completion-free positive floor F1 (class 1 satisfied in full — its condition says nothing about completions), while a named completion of a kind §2 itself lists ("order-unity coefficient", per "**No Euclidean volume, uniform interior, order-unity coefficient or GR exterior may enter silently** — each is an added completion, named and tested separately") yields F2 != F1, and no completion permits zero (class 2 satisfied in full). The only precedence rule in the document is class 4 over class 2; nothing orders 1 against 2. The same construct with a zero-permitting completion satisfies classes 1 and 4 simultaneously, again with no rule. Which class is filed then depends on whether an "order-unity coefficient" completion counts as "admissible" when the printed relations already fix the floor — and "admissible" is defined nowhere, so two obedient seats can file different classes for the same physics.

   Exact replacement for class 1's first sentence: "1. **DYM_FLOOR_DERIVED** — a unique positive floor follows from the printed relations with no added completion, **no admissible completion yields a different floor, and no admissible completion permits masses approaching zero**."
   Exact addition to §2, after the sentence ending "named and tested separately, exactly as K6 required.": "**A completion is admissible if and only if it introduces exactly one named assumption and is consistent with every printed relation of the manifest sources; a completion that contradicts a printed relation is inadmissible and may not be considered.**"

   Exhaustiveness is otherwise sound: class 5's "only under" separates it from class 1; class 4's printed-relation requirement separates it from class 3; the stated precedence separates 4 from 2; unequal-vs-same separates 2 from 5. An INCONCLUSIVE result is genuinely reachable: UNRESOLVED rows "may not be treated as absence, and forces `DYM_SOURCE_BLOCKED`", so the design can refuse a scientific verdict rather than manufacture one. That sub-point is sound.

2. CONTROLS — two defects; codes and unreached-control handling otherwise sound.

   (a) Verbatim (§9): "Transcribing expected values fails `C5_HARNESS_PINNED`."
   Defect: the anti-transcription rule is scoped to C5 only. C1's artefact is "the printed digests", and §2a prints the expected digests in the same document, so a seat can fill C1's artefact by copying the manifest values without hashing anything — passing C1 by assertion in artefact form. The design knows this failure mode and forbids it for exactly one control.
   Exact replacement: "Transcribing expected values fails `C5_HARNESS_PINNED`; **the same rule applies to C1 — a digest copied from §2a rather than computed from the file's bytes in the seat's own run fails `C1_SOURCE_IDENTITY`.**"

   (b) Verbatim (§9): "every seat executes and prints `python3 --version`, `sympy.__version__`, and `shasum -a 256 $(command -v python3)`."
   Defect: `sympy.__version__` is not a shell command; executed literally it fails with "command not found", so C5 as frozen cannot be executed as frozen — a seat must either fail C5 or silently substitute a working command, and two seats can choose differently.
   Exact replacement: "every seat executes and prints `python3 --version`, `python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`."

   Every control names an exact code (C1_SOURCE_IDENTITY, C2_COMPLETION_LEDGER, C3_DELETION_PROBE, C4_GR_BENCHMARK, C5_HARNESS_PINNED, C5B_PATH_LIST, C6_BREAKER_TEST). Unreached controls are handled: "controls recorded `NOT_RUN`, never as passes", with the underscore spelling fixed. C2, C3, C4 are artefact-bound with "a claimed pass without them fails" language. Sound on those points.

3. CIRCULARITY — the census key is blind exactly where physics relations live.

   Verbatim: "**every hit appears either as its own census row, or is cited inside a `DUPLICATE` row naming the row that covers it.**"
   Verbatim: "**A relation that was never listed is therefore mechanically distinguishable from one excluded under a reason code**"

   Defect: the eleven search terms are all English words (`core`, `scale`, `density`, `mass`, `mass function`, `radius`, `horizon`, `matching`, `surface`, `regular`, `de Sitter`). A relation printed purely in symbols — `r_0^2 = 3/Lambda`, `g_tt = 1 - (r_g/r)(1 - exp(-r^3/r_0^3))`, `m(r) = ...` — contains none of the eleven strings, produces zero hits, and never becomes a row. It is omitted by the key itself, so the omitted-vs-excluded distinction the design claims to have mechanised holds only for prose. A size–mass binding in a gravitation paper is overwhelmingly likely to appear as a bare displayed equation; both blind seats share this blind spot identically ("a shared blind spot reproduces in both" — the document's own words), and the re-runnable key reproduces it a third time. The contrary row is quietly omitted with the census passing in full.

   Exact replacement (add as a new sentence immediately after the sentence ending "naming the row that covers it.**"): "**In addition, every numbered or displayed equation in each manifest source appears as its own census row, or is cited inside a reason-coded row naming the row that covers it; the seat prints each source's equation list — by equation number, or by page/line locator for unnumbered displays — as part of the same C2 artefact, so a relation expressed only in symbols is surfaced exactly as a prose relation is.**"

   The rest of the firewall is sound: §0 and §8 are de-patterned with the bypass explicitly named; the pattern record is forbidden for inclusion, exclusion and outcome selection and enters only at C6 after DYM_FLOOR_DERIVED; DUPLICATE rows are checkable because both rows' verbatim texts are printed. The defect above is the remaining channel, and it sits precisely on the relations the study exists to find.

4. THE FALSIFIER — condition 5 is not decidable as specified; it files DYM_SOURCE_BLOCKED on every path. Condition 2 has a residual ambiguity. Conditions 1, 3, 4 are decidable.

   (a) Verbatim (§2a): "**A read outside this manifest files `DYM_SOURCE_BLOCKED`.**"
   Verbatim (§5): "**An unread comparator source files `DYM_SOURCE_BLOCKED`; **only a completed no-match table passes condition 5.**""
   Verbatim (comparator row 2): "`2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt` (manifest §2a)"
   Verbatim (comparator row 3): "entry 31's bar, `NS_MASS_WATCH_PREREG_20260902.md`"

   Defect: §2a's manifest contains exactly four files (entries 18, 19, 20, 55). The PBH file is not among them — the parenthetical "(manifest §2a)" is false — and neither is NS_MASS_WATCH_PREREG_20260902.md. So on condition 5 a seat that reads the comparator sources violates §2a and files DYM_SOURCE_BLOCKED, and a seat that does not read them triggers "An unread comparator source files DYM_SOURCE_BLOCKED". Both paths file BLOCKED; condition 5 can never pass. The decisive test is pre-disabled for the second consecutive round — V4's own stated reason for V3's failure ("the decisive test stayed pre-disabled") reproduced in new form. The repair supplied the values but deferred the binding, and the false manifest annotation asserts a binding that does not exist.

   Exact replacement for the "unread comparator source" sentence: "**The comparator values printed in this table are the frozen artefact; condition 5 is evaluated against these printed values alone. The source column is provenance only; no comparator source file is in the manifest, none may be read for this study, and none needs to be read — a completed no-match table built from the printed values passes condition 5.**"
   Exact replacement for comparator row 2's source cell: "`2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt` (provenance only; not a manifest source, not to be read)"
   Exact replacement for comparator row 3's source cell: "entry 31's bar, `NS_MASS_WATCH_PREREG_20260902.md` (provenance only; not a manifest source, not to be read)"
   (Equally acceptable: add both files to §2a with real digests. What is not acceptable is the current text, which forbids and requires the same read.)

   (b) Verbatim (condition 2, quoted text): "without that reference itself deriving it — the R3A test, run to the end of the citation chain."
   Verbatim (decision rule, row 2): "every constant terminates in a source equation or in the §2b constant list; any `we assume/choose/simplest form` terminus fails"
   Defect: "run to the end of the citation chain" invites chasing references, but every reference outside the manifest is unreadable under §2a; the decision rule never says what an external terminus does. One seat can follow the chain and file BLOCKED while another treats the external terminus as a failure — the same condition, two rulings.
   Exact replacement for row 2's pass criterion: "every constant terminates in an equation of a §2a manifest source or in the §2b constant list; **the citation chain is followed only within the manifest, and any terminus outside it, like any `we assume/choose/simplest form` terminus, fails**"

   Minor, same section: the fallback row reads "bracketed bisection on sign changes (`mpmath.findroot`)" — findroot is not a bracketing bisection solver. Executable, but mislabelled; a literal seat may fail where a forgiving one passes. Exact replacement: "bracketed root-finding on detected sign changes (bisection on each bracketing interval, or `mpmath.findroot` seeded from the bracket)".

   Conditions 1, 3, 4 are decidable as specified: dimension classification is bounded; the free-symbol probe has a bounded procedure whose timeout lands on the §9 absent-row rule (file DYM_SOURCE_BLOCKED, do not pass the control — terminal, not a stall); the fixity table is a finite list with a source line per row, and a held-constant quantity with no manifest derivation simply fails.

5. RE-RUN GUARD — sound in design, undermined in practice by finding 4(a).

   §6 states "K6's outcome may **not** be assumed to repeat" and the positive class is structurally reachable: limb B derives the floor, class 1 files it, class 5 covers the completion-dependent positive case. No text anywhere presupposes K6's underdetermined result. But note honestly: while finding 4(a) stands, the positive class's distinguishing consequence — "if it passes them, this is a counterexample to the pattern and the pattern record must be amended" — is unreachable, because C6 condition 5 files BLOCKED on every path. The design can return DYM_FLOOR_DERIVED on paper; it cannot confirm it as the opposite answer, which is the study's stated purpose.

6. FAIRNESS — sound.

   "Unreproduced from the stated inputs" is held in limb A ("report that **a size–mass relation was unreproduced from the stated inputs**"), in class 3's definition ("**was unreproduced from the stated inputs** after the frozen census of §2 was completed"), and as the standing rule in §6. Limb A's parenthetical makes the epistemic scope explicit: "the class records what this lane could not reproduce, not a claim that the branch contains no such relation." No negative finding anywhere is labelled an error. The earlier limb-A and class-3 violations named in §8 are genuinely repaired. No replacement.

7. STALL — sound.

   Every terminal path files a declared class. Symbolic timeout: 120 s cap, named fallback row, second cap, and "If the row is absent, times out, or does not decide its proposition, file `DYM_SOURCE_BLOCKED` and **do not pass the affected control**." Persistent control failure: R3D_NO_CLASS, with DYM_SOURCE_BLOCKED taking precedence whenever unread evidence caused the failure, and the one-seat-vs-two-seat asymmetry given an explicit third-seat re-run rule. Seat splits of any kind — scientific, blocked, or no-class — convene the third seat, which re-executes a blocked read once and files only on agreement; "If all three differ, or the third seat cannot decide, file `DYM_SOURCE_BLOCKED`." The claim "**Every terminal path files exactly one declared class**" is achieved. Caveat by cross-reference: the finding-1 ambiguity can manufacture a scientific-class split between two correct seats, but that split still terminates under the seat-split rule. No replacement.

ADDITIONAL — is the V4 content actually sufficient?

- Source manifest: binding for the four science sources — real digests, byte counts, content-verified identity (the entry-55 filename trap is caught and documented), the entry-18 restatement explicitly excluded, C1 enforces it, reads outside file BLOCKED. But the binding does not cover the document's own condition-5 path: the comparator table invites reads of two files outside the manifest, one of them falsely annotated as a manifest member. On that path a seat is not merely able but required to consult a different artefact — or blocked for refusing. The manifest is binding where it applies and contradicted where it matters most.

- Five breaker conditions: now stated in full, verbatim, with the pattern record's hash, and evaluable against the pinned text only. Conditions 1, 3 and 4 are decidable without leaving this document. Condition 2 is one ambiguous phrase away from decidable (finding 4b). Condition 5 is not decidable at all as written (finding 4a). So: no, not all five.

- Comparator table: the arithmetic is executable today — I verified the gaps: Planck-to-PBH 19.37 dex, PBH-to-TOV 18.99 dex, full span 38.36 dex, so the ±1.0 dex tolerance cannot cross-match any two rows and is defensible as stated; the ΛCDM null row makes the negative case explicit rather than skipped. (The rationale phrase "a scale that spans about sixty" overstates the table's actual ~38-dex span; cosmetic, but a frozen document should say thirty-eight.) The blocker is not completeness of the numbers, it is that execution is routed through unreadable sources.

- String-search census: for prose it does make an omitted relation distinguishable from an excluded one — the printed search output plus the DUPLICATE-citation rule close that hole. For symbol-only relations it does not: they never surface as hits, so their omission is invisible to the very mechanism that claims to detect omission. The largest single channel for a contrary row — a displayed equation — is outside the key.

Plainly stated: this round again deferred content in two places while supplying it elsewhere. It supplied the manifest, the constant list, the conditions, the decision rules and the fallback table — real repairs. It deferred (a) the comparator-source binding, supplying values whose provenance the manifest forbids reading while requiring them read, and (b) the equation-level enumeration, supplying a prose key and declaring exhaustiveness over a corpus whose relations are printed as equations. Findings 4(a), 3 and 1 are each independently terminal for a gate whose purpose is to let this branch return the opposite answer; finding 4(a) pre-disables the decisive test for the second round running.

R3D_V4_KIMI_COMPLETE
