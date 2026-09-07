# R3C2 — two-seat gate on V38 (`8095c18c…`), reconciled BY TOPIC (2026-09-07 10:44 KST)

**FILED, NOT REPAIRED.** Duho has re-set this lane's objective to the bounce investigation; Blanc's instruction of 10:17 KST is to
close this gate out, preserve every record and pin, and open NO V39 repair round. These findings keep. Nothing below is fixed.

Reports: `R3C2_GATE_V38_codex_20260907.md` (**PREREG_UNSOUND**; N1, N2, N3 non-cosmetic; NO_MASKED_STAGE=NO and
PRIOR_FINDINGS_CLOSED=NO; written 10:13, wrapper absent 10:18:55), `R3C2_GATE_V38_kimi_20260907.md` (**PREREG_UNSOUND** — its first
unsound verdict; findings 1 and 2, both non-cosmetic; NO_MASKED_STAGE=YES, PRIOR_FINDINGS_CLOSED=YES; written 10:39, pid gone
10:42:50). Access lines verified on both. Blind intact on both. Master, packet and both pin sheets re-verified unchanged after all runs.

| topic | codex | kimi | status — FILED for a later version |
|---|---|---|---|
| the alternative-branch predicate still uses raw equality, so an auditor-only permutation of a MULTI-ENTRY silent alternative's `files`/`matches` flips C6 (base exit 0, reversed exit 1) | N1 | (agrees in substance: the search-order class is the one live residual) | OPEN. codex supplies an exact replacement: compute the canonical representation before EITHER branch predicate and use it for selection and diagnostics alike. The V38 repair covered the primary branch only; the delivered exhibition's silent-alternative case has singleton inventories, so it could not expose this |
| type-blind comparison: `{"line":1}` and `{"line":true}` compare EQUAL, so a genuine evidence difference passes (Python equates 1 and True); sorting retained the distinct representations, the COMPARISON erased them | N2 | — | OPEN, and it is the failure Blanc named in advance at 09:07: canonicalisation must not hide a real difference. codex's replacement is equality of a TYPE-PRESERVING canonical JSON serialisation at merge and at both C6 predicates. Note what the kit's guards did and did not catch: duplicate, whitespace, inner-order, changed, added and deleted entries all still FAIL correctly (executed by both seats); the cross-type case was not among them |
| query-list order is an ordering that carries no meaning, is canonicalised nowhere, is not enumerated in (a)–(g), and flips the verdict on an otherwise identical ORIG_SILENT reconstruction | — | finding 1 | OPEN — the sixth instance of the ordering class, and it sits inside the sentence that says the invariant "governs any other that is found". Whether query order is meaningless is itself a design question: codex's V37 replacement expressly preserved `query`, kimi shows the audit compares searches BETWEEN agents, where run order can carry no meaning. That tension is recorded, not resolved here |
| two in-text pins name digests the delivered files do not have: `r3c2_batch_tools.py` printed 3822f12c… vs delivered e078e05c…; `r3c2_manifest.py` printed 6b6e4bce… vs delivered f3854f8b… | N3 | finding 2 | OPEN, and it is MINE: both files gained V38 completion tokens, I regenerated both pin SHEETS (seat 8/8, kit 24/24 verify against the delivered bytes) but did not update the hashes quoted inside the master, and the packet is built from the master, so the seat-facing packet asserts two false digests for files in the seat's own working directory. Exact replacements supplied by both seats |

**Where the seats disagree, recorded rather than reconciled away:** codex answered NO_MASKED_STAGE=NO and PRIOR_FINDINGS_CLOSED=NO;
kimi answered YES to both and closed every V37 finding with its own executed evidence. The substance is not in conflict — both hold
that the search-order class is not fully closed — but the tokens differ and neither is overridden here.

**What both seats independently confirmed as working:** the V37 exact-failure repair. Each attacked the judges directly and reports
that no control passed under any subversion — a real traceback, a missing completion token, a padded, reordered or dropped row, an
unpinned control (fail-closed), a SyntaxError fixture, a relocated inert probe marker, a probed tool exiting the right code for the
wrong reason, an emptied tools directory, a wrong-bytes subcase, and re-capturing the pinned table. Capture mode on the delivered
tools is a byte-identical fixed point, and an expectation-changing re-capture breaks the kit pin sheet. Cycles and missing
dependencies fail through every origin at validate, compute and C6, 7 of 7 each. The kit ran 206 controls and 65 probes clean in both
modes for both seats. Stated as what those controls assert, not as a guarantee.

**Sweep (2026-09-07 10:44 KST):** every finding label in both reports checked programmatically against the rows above — missing: none. kimi's two
findings are numbered in prose rather than labelled, and are carried as rows.
