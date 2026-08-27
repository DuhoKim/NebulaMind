# V17 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

V17 is **NOT CLEAR**. The pinned digest and 782-line identity match, five repairs hold cleanly, and the large §6.3 restoration has operative normative bodies rather than titles. But the §2.7 reason-(d) repair still did not land, the new outcome registry conflates run outcomes with per-attempt states and therefore makes its own “exactly one outcome” assertion false, and the newly inserted scalar/profile sentence omits the calibration-precedence condition enforced by both §6.3 and the pinned code. The restored §6.3 repair-trace rule is also not applied to V17 itself: §10 has no V16→V17 finding-to-change trace.

## Subject identity — verified before opening

- Required SHA-256: `1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5`.
- Independently computed before opening for `../PREREG_SUCCESSOR_DRAFT_V17_20260827.md`: `1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5`.
- Result: **MATCH**.
- `wc -l`: **782**, matching the brief.

## Numbered findings

1. **HIGH / BLOCKING — §2.7 still contains the supposedly deleted reason-(d) contract, and its replacement threshold sentence remains non-single-valued.**

   - **Section and lines:** §2.7 lines 337–375, especially lines 360–365 and 373; §7 lines 675 and 682.
   - **Evidence:** The live exclusion enumeration at lines 337–340 contains only reasons (a) and (b), with confidence deferred to Row P. Yet paragraph 5 still begins, “Reason (d) is the outcome-adjacent one” and defines its confidence/absence behavior at lines 360–365. V17 changed paragraph 7, but it now says the confidence threshold is defined as part of Row-P state (7) **“or”** the refused BS-2a design. Row P is the P8 application state; §7 line 675 makes BS-2a the pre-image DESIGN owner. Those are not alternative owners. BS-3 at line 682 is now correctly only instrument identity, so that half of V16’s conflict is repaired, but the dangling reason and the `or` contract remain.
   - **Why it fails:** Repair 3 was not applied as briefed. A pre-image frozen design must define one confidence predicate and one authority; Row P can apply that predicate but cannot be an alternative place to define it after unblinding. The live reason-(d) prose also contradicts the closed (a)–(b) pre-lock enumeration. Clause 10 therefore still leaves the confidence branch’s definition dependent on which live paragraph an operator follows.
   - **Smallest sufficient repair:** Delete paragraph 5’s reason-(d) text. Rewrite paragraph 7 to state that the refused BS-2a design is the sole pre-BS-6 owner of the confidence quantity, numeric threshold, authority, and retry/failure semantics; Row P state (7) only applies those already-frozen bytes at P8. Preserve below-threshold → `EXCLUDED-BY-CONFIDENCE` → immediate run-level `INCONCLUSIVE-BY-CALIBRATION`.

2. **HIGH / BLOCKING — the canonical registry mixes two cardinalities, so §5’s “exactly one outcome” claim and Clause 10 cannot both hold.**

   - **Section and lines:** §5 lines 458–475; Row P line 534; Clause 10 line 564.
   - **Evidence:** Line 466 says `run_production_verdict()` “emits exactly one outcome from the canonical registry.” The registry then includes three **per-attempt exclusions** at line 472 alongside run-level numeric verdicts, halts, refusals, and VOID. Row P says every absent/non-finite/low-confidence attempt receives one of those exclusion states, while any post-unblinding removal also immediately emits the run-level `INCONCLUSIVE-BY-CALIBRATION` (lines 475 and 534). One run may contain many attempts and more than one exclusion reason. Conversely, Row P’s eighth per-attempt state, accepted-finite, is not a category in the purported registry.
   - **Why it fails:** For a concrete reachable branch containing one absent and one non-finite attempt, the document requires both `EXCLUDED-BY-ABSENCE` and `EXCLUDED-BY-NONFINITE` in the terminal partition and then `INCONCLUSIVE-BY-CALIBRATION` for the run. That is not “exactly one outcome from the registry.” The registry is neither a closed run-outcome set (because it contains repeatable attempt states) nor a closed attempt-state set (because accepted-finite is omitted and run outcomes are included). This is the new double-assignment seam the V17 brief explicitly required the registry audit to attack.
   - **Smallest sufficient repair:** Split the surface into two explicitly different namespaces: (a) a complete per-attempt terminal-state registry including accepted-finite and the three exclusions, and (b) an exactly-one run-level outcome/refusal registry containing numeric verdicts, pre-statistic halts, accounting refusals, and VOID. State the deterministic projection from any per-attempt exclusion to the single run-level calibration halt, and make `run_production_verdict()`’s exactly-one assertion refer only to namespace (b).

3. **HIGH / BLOCKING — the newly added scalar/profile threshold omits the calibration gate’s precedence and assigns a profile path to records that must halt.**

   - **Section and lines:** §3 line 388; §4 line 448; §6.3 lines 585–587; pinned `ref/successor_ref_v9.py` lines 1492–1496.
   - **Evidence:** The new §3 sentence says scalar if `max_b |â_b − â| <= 0.03` and profile “otherwise,” without conditioning either path on the calibration floor. §4 says any `a_LB_b < 0.85` immediately halts before Stage C. §6.3 gives the correct ordered partition: scalar only when spread passes **and** every lower bound passes; “spread failure only” selects profile; any low bound halts. The pinned `adjudicate_path()` likewise checks the `0.85` floor first and raises `InconclusiveByCalibration`, reaching the `0.03` scalar/profile return only after that check.
   - **Why it fails:** For a reachable calibration record with spread `> 0.03` and one `a_LB_b < 0.85`, §3 says PROFILE while §4/§6.3/code say calibration halt. The requested value is present, and the rough phase is present, but the failure effect and precedence are not single-valued across the whole document. This is a Clause-10 forward double assignment introduced by the V17 repair itself.
   - **Smallest sufficient repair:** Make §3 explicitly ordered: first, any lower bound `< 0.85` emits pre-unblinding `INCONCLUSIVE-BY-CALIBRATION`; only after all bins pass does spread `<= 0.03` select scalar and spread `> 0.03` select profile. Use “spread failure only” as §6.3 already does.

4. **MEDIUM / BLOCKING — restored §6.3 requires every gated revision’s finding→change map in §10, but V17 has no V16→V17 repair trace.**

   - **Section and lines:** §6.3 lines 594–596; §10 lines 738–772, especially line 769.
   - **Evidence:** The restored operative clause says every gated revision maps finding → change in §10 and lists any untraced change separately. V17 changes the banner, §2.6, §2.7, §3, §4, §5, Row P, §6.3, and §7. Section 10 ends with a one-sentence **V15 → V16** entry; it contains no V16-review findings and no V16 → V17 mapping.
   - **Why it fails:** The restored clause body is normative, but the same assembled revision does not conform to it. This is an adjacent seam created by restoring §6.3: the rule exists but its first applicable revision is unreceipted in the section the rule names. It also hides Finding 1’s partial application and Findings 2–3’s new registry/threshold seams from the document’s own repair accounting.
   - **Smallest sufficient repair:** Add a V16 → V17 table in §10 mapping every finding from both V16 whole-review reports to the exact applied edit, marking partial/unresolved items honestly, and list any incidental V17 change separately with its hypothesis.

## Seven-repair application audit

1. **§6.3 operative bodies — HOLDS.** Seven titles now carry normative bodies. The universal post-first-real-χ change/void rule is present at lines 590–593, and Row P cites current §6.3 rather than V15.
2. **§4 / Row-J conformance — HOLDS locally.** Lines 448 and 450–454 now state the pre-Stage-C calibration halt, pre-attrition BS-5f scope, one-removal calibration consequence, and no Stage-C rerun. The §10 claim that §4 was conformed is now substantively true, although V17’s own trace is absent (Finding 4).
3. **§2.7 reason-(d) deletion — FAILS.** Paragraph 5 remains live, and paragraph 7 uses an alternative-owner `or` construction (Finding 1).
4. **§7 class-E count — HOLDS.** Direct parsing gives 14 Class-P rows and 8 Class-E rows, matching line 669. BS-2f is Class E and value-only; BS-2a and BS-2k are the two DESIGN rows.
5. **Canonical outcome/refusal registry — PRESENT BUT DOES NOT HOLD.** The list exists and §5’s old count wording was changed, but its mixed run/per-attempt namespace defeats exact-one closure (Finding 2).
6. **Three-moment chronology — HOLDS to available evidence.** The banner separates 21:48 instruction/initiation, report landings at 21:52:33 and 21:53:46, and the later final V16 byte state. Report mtimes match the two landing times; V16’s mtime is 22:47:17 and its bytes contain the schema repair. The raw 21:48 instruction remains Testimony.
7. **Two smaller overclaims — HOLDS.** Line 319 now calls the Stage-P material candidate evidence only and does not fill BS-5p. The `0.03` threshold is now stated, but its newly written precedence defect is Finding 3.

## Clause 10 audit across §§0–11 — both directions

### Forward: every branch → exactly one category

- **Held under attack:** BS-1 A/B/date fallback; exact-versus-production selection boundary; manifest pass/refusal checks; numeric p/sign/band/floor regions including equality residuals; Row-J `<0.85` versus all-bins-pass; exact 1,000-trial protocol; 961/962 boundary and self-verification failures; Row-P missing/duplicate/orphan/malformed precedence; zero versus one-or-more post-unblinding removals; disclosure only after BS-V; forbidden table acts → VOID.
- **Failed:** confidence definition remains split across stale reason-(d) and BS-2a/Row-P wording (Finding 1); the registry assigns per-attempt exclusion states and a run-level calibration halt on the same reachable branch while promising exactly one registry outcome (Finding 2); §3 assigns PROFILE to a low-bound branch that §4/§6.3/code halt (Finding 3).
- **Carried blocker, honestly disclosed:** Stage P remains dual-valued between pinned shared-null code and preferred exact-per-trial measurement; BS-5p remains blocked rather than falsely terminated as filled.

### Reverse: every category → reachable antecedent

- Numeric `REPRODUCED-LONGO`, `REJECTED-AT-LONGO-AMPLITUDE`, and residual numeric `INCONCLUSIVE` have reachable, closed predicates.
- Pre-statistic `INCONCLUSIVE-BY-CALIBRATION` and `INCONCLUSIVE-BY-POWER` have reachable lower-bound and Stage-C witnesses.
- The four accounting refusals have Row-P witnesses; VOID has table/protocol witnesses.
- Each exclusion label has a Row-P witness, but because those labels are per-attempt states rather than exactly-one run outcomes, their inclusion in the same registry invalidates the claimed reverse category contract rather than closing it. Accepted-finite is the omitted complementary attempt state.

## Threshold sweep — value, phase, failure effect

- **Calibration floor `0.85`:** value, equality side (`>=` passes), P4/P5 phase, and `<` calibration-halt effect agree in §4, §6.3 and pinned code.
- **Scalar/profile spread `0.03`:** value and equality side agree with pinned code, but §3 omits the all-bins-calibration-pass precondition and therefore misstates the failure effect/precedence (Finding 3).
- **Stage C `N_TRIALS = 1,000`, success cut `962`:** value, P5/pre-BS-L phase, protocol-deviation VOID, `<962` power halt, and complementary PASS are stated.
- **Self-verification:** any `refuted` or `nonconservative` result fails closed to power inconclusive; pinned code lines 1275–1277 agree.
- **Post-unblinding attrition:** one or more removals → calibration inconclusive; zero proceeds; no Stage-C rerun.
- **Confidence:** numeric value is permissibly absent while BS-2a is refused and BS-6 blocked, but owner/definition is not single-valued (Finding 1).
- **Production/decision:** 100,000 permutations; reproduction p `<0.001`; rejection p `>0.05`; detection multiplier `3.09`; amplitude `0.0408`; three-sigma bands. Pinned v9 constants and decision lines 1577–1584 agree, including equality falling to numeric inconclusive.
- **Planning:** retention `0.8572`, `N_eq >= 100,000`, exact mode `<=16`, and margin `1.2` agree with pinned v9 constants.
- **Other explicit thresholds:** release fallback 2026-09-05; catalog cuts; 10× Stage-P boundary audit; calibration allocation floors ≥10 per non-empty joint cell and ≥30 per live inherited stratum. Their stated phases and local failure effects are closed.

## Structural-completeness and overclaim checks

- V17 contains the same twelve major `## §0` through `## §11` headings as V16, plus the separately headed `## §2.7` block counted by the brief’s 13-section structural description. It ends on the same §11 verifier bullet. No truncation seam found.
- The draft/no-run status, unresolved Findings 1/2/2b/3, BS-2a refusal, Rows C2/E blockage, BS-6/first-image blockage, and missing implementation work remain prominent.
- The remaining overclaims are specific: the banner says the §2.7 partial edit was completed when it was not; §5 calls a mixed-cardinality list an exactly-one registry; §3 states an unconditional scalar/profile partition that the code does not execute; and §6.3 says the repair trace exists for every revision when §10 has none for V17.

## Failed attacks / credited repairs

- Tried to recover the seven bare §6.3 titles: failed; the operative bodies are restored and carry normative verbs, thresholds, and failure effects.
- Tried to recover Row P’s superseded “V15 lines 570–573” citation: failed; it now cites current §6.3.
- Tried to reopen §4’s missing calibration and post-attrition text: failed; both are present.
- Recounted §7 directly: 14 Class-P and 8 Class-E rows; the V17 count repair holds.
- Tried to recover the class-P completion overclaim beside BS-5p: failed; line 319 is appropriately narrow.
- Checked the principal equality boundaries (`a_LB_b == 0.85`, spread `==0.03`, 962/1,000, p `==0.001`, p `==0.05`): their intended sides agree with pinned code. Finding 3 concerns ordering/applicability, not the numeric value or equality side.

## Testimony and limits

- The 21:48 principal instruction/initiation is not independently receipted in the reviewed artifact set; it remains Testimony. The later report mtimes and final V16 byte state were independently checked.
- Future `verify_lock()`, `verify_unblinding_receipt()`, slot/unblinding schemas, Row-J guard implementation, mediator, C2 worker, acceptance recomputation, replay verifier and negative fixtures remain required work, not executed protection.
- I did not re-derive predecessor/real-geometry/Stage-P scientific measurements, inspect prohibited data, fetch anything, inspect secrets, or touch χ-bearing material.
- No `prereg_lint.py` was present in the authorized build tree, so “lint clean” was not independently reproduced. Structural headings, final non-empty line, and slot counts were independently parsed instead.

## Evidence ledger and custody

Content read:

- `BRIEF_V17_WHOLE_REVIEW.md` in full.
- `../PREREG_SUCCESSOR_DRAFT_V17_20260827.md` in full, only after digest verification.
- `V16_WHOLE_REVIEW_CODEX.md` and `V16_WHOLE_REVIEW_GPT56.md` in full.
- V16→V17 whole-file mechanical diff.
- Targeted pinned-code regions for constants, `adjudicate_path()`, Stage-P fail-closed returns, and numeric decision regions.

Independent checks run:

- SHA-256 and line count before opening V17.
- SHA-256 of the R15 source and both pinned §0 code files.
- V16→V17 applied-diff audit.
- Programmatic major-heading/final-line checks and direct Class-P/Class-E row counts.
- Whole-document outcome-token inventory and forward/reverse Row-P/§5 mapping.
- Whole-document threshold-token sweep and targeted comparison to pinned v9.
- R15-report and V16/V17 filesystem timestamp checks.

No source, code, draft-under-review, data artifact, gate brief, or prior report was modified. This required report is the sole write by this seat.

**NOT CLEAR**