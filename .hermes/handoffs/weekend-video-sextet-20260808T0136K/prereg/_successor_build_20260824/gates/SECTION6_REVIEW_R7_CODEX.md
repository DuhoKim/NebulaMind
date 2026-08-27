# CODEX referee report — proposed replacement §6, seventh pass R7

## Verdict

**NOT CLEAR.** R7 fixes the concrete silent-inner-join hole and gives Row I a fail-closed pre-BS-8f consequence, but Row P still names rather than defines its terminal-state and revalidation contract. A gate cannot decide from this prose what the absent/non-finite states are, what exact join outcomes produce them, what “calibration applicability” means, or which locked adequacy conditions permit versus refuse the verdict. R7 also states a BS-5f rule that its own ordering cannot enforce: current V15 §4 permits BS-5f to PASS on the pre-attrition BS-2f mask, while Row P only conditionally refuses later. Blocking finding: 1.

## Numbered findings

### 1. BLOCKING — Row P closes silent loss in principle but does not supply an evaluable terminal-state/revalidation rule

**Row / clause at issue.** Row P (line 52); Row J (line 46); Part 2 items 2–3 (lines 101–102); Part 5 defect 4 (line 129); current V15 §4 Stage C (lines 421–425).

**Why it fails.** The new exact-parent join, ban on silent inner-join loss, precedence before confidence, ban on discretionary retry, and widening from confidence removals to every removal are substantive repairs. They eliminate R6b's written permission for an absent row simply to disappear.

The decisive outputs remain undefined, however. “A named deterministic terminal state” and “explicit deterministic terminal states” do not actually name an enum or define the mapping from join evidence to each state. The draft does not say how zero, duplicate, extra, malformed, absent, or non-finite records are distinguished; which fixed join keys and attempt-set digest govern; whether more than one measurement for a parent is an unconditional refusal; or what artifact authenticates the resulting exact-parent accounting. “Calibration applicability,” the “pinned protocol,” and “any locked adequacy condition” likewise have no enumerated predicates or pass/fail relation in R7 or current V15. In particular, the text does not decide whether removal of a hand-check allocation member forces `INCONCLUSIVE-BY-CALIBRATION`, permits a frozen recalculation, or merely reruns power. A gate therefore cannot evaluate the promised consequence without supplying policy after unblinding.

The BS-5f sentence is also false as written under route (b). Current V15 §4 defines Stage C before unblinding on the sealed BS-2f accepted-position mask. R7 deliberately leaves reason-(c) rows in that mask. BS-5f can therefore certify that mask even when a row later proves unusable. Row P does not prevent that certification; it re-evaluates later and refuses only **if** an undefined adequacy condition no longer holds. If recomputation passes, the verdict proceeds. Thus Row J's “BS-5f may not certify” and Part 5's claim that such certification cannot occur “without triggering refusal” overstate the actual conditional revalidation rule.

**Smallest sufficient repair.** Without inventing the separate BS-2a schemas, make the route-(b) prose decidable: (1) name the closed post-unblinding states and define their precedence from an exact set-equality join against one pinned attempt-set identity; (2) make zero/duplicate/extra/malformed records, absence, non-finiteness, low confidence, and accepted-finite outcomes each produce one fixed consequence, with no retry; (3) enumerate the locked calibration and power predicates and state exactly which failure emits `INCONCLUSIVE-BY-CALIBRATION` or `INCONCLUSIVE-BY-POWER`; and (4) replace the impossible BS-5f claim with the honest rule that BS-5f certifies only the locked BS-2f population and cannot license a verdict after any final-mask change unless the pinned post-unblinding revalidation passes. If the intended rule is unconditional refusal after any unusable row, say that instead of the current conditional rule.

### 2. LOW — Part 5 understates a refusal already credited by both R6b referees

**Row / clause at issue.** Part 5 defect 1 (line 125), read with Row E (line 41), Row C2 (line 39), and the R6b failed attacks.

**Why it fails.** Marking the checksum/bit-channel machinery and the promise-not-boundary finding UNRESOLVED is honest, not evasive. A future-work list is not a repair receipt, and items 2, 2b, and 3 now say so correctly. But defect 1's title is the old impossibility that C2 cannot produce Row D's future execution facts before D. R7 continues the already-credited refusal: C2 no longer emits completion/finiteness, Row E excludes reason (c), and both R6b referees recorded that future-execution-status attack as failed. Calling that refusal itself UNRESOLVED conflates a settled route choice with the separate unresolved BS-2a channel/boundary mechanism.

**Smallest sufficient repair.** Split the disposition: record the impossible pre-inference execution-status assignment as **RESOLVED BY REFUSAL** (or equivalent), while keeping the replacement BS-2a schemas, verifier, attestation, mediator transition, and fixture oracles explicitly **UNRESOLVED**. This is a candor/precision repair, not a reason to clear finding 1 above.

## Row I cost and route choice

Row I now has a determinate pre-unblinding consequence: if any allocated object lacks a usable finite output, the run halts before BS-8f. Therefore no BS-8f, BS-5f, BS-L, unblinding, or statistic follows. This closes the calibration-formability branch fail-closed.

The observable halt discloses an aggregate data-completeness fact — at least one allocated output was absent or non-finite — not a handedness value or direction. I cannot verify from prose alone that missingness/non-finiteness is statistically independent of handedness or morphology; that is Testimony, not a proved property. Within the scoped route-(b) choice, fail-closed is the safer trade. The alternative “usable sealed subset” was not already available: it would need a new frozen subset-selection, calibration-validity, minimum-coverage, and allocation consequence contract, and could otherwise create a post-allocation researcher degree of freedom. R7 was right not to improvise that design.

## Preservation and failed attacks

1. **Subject pin held.** R7 sha256 is `ecccedde495a88377497057a4334c676f651f559fc0a7b2635a78dca8a990f30`, exactly matching the brief.
2. **Mechanical R6b→R7 scope held.** All twenty actor/process rows A–S (including C2) remain present. Only Rows I, J, and P changed in Part 1's table. All nine clause bodies are byte-identical between R6b and R7; their individual lengths, hence their average length, are identical.
3. **Protected properties held.** Clause 1 retains the universal access ban; Rows G→H→I plus Clause 5 retain the authorized committee path; Clause 3 and Rows J/N/O/P retain BS-5f → BS-L → unblinding → BS-7f → BS-V.
4. **§6.2 fidelity held.** The reconstituted §6.2 is whitespace-normalized identical to R5.
5. **§6.3 fidelity held.** R7 restores the same seven R5 bullet clauses. The only substantive textual difference in that subsection is removal of the heading's editorial parenthetical “(carried unchanged),” not a new conduct rule.
6. **Unresolved-status honesty mostly held.** Part 5 no longer presents the BS-2a schema/verifier/attestation/fixture work as repaired. Finding 2 above identifies only the overbroad treatment of the already-settled refusal itself.
7. **Silent-inner-join attack now fails at the prose level.** Row P expressly forbids silent loss and makes every absence/non-finiteness/confidence removal trigger revalidation. Finding 1 is that the resulting terminal states and decision predicates remain unnamed/undefined, not that silent loss is still permitted.

## Testimony and limits

I did not inspect `/Users/duhokim/NebulaMindData/`, any image, cutout, χ value, sealed-store payload, predecessor-archive content, credential, key, live access log, runtime attestation, or future implementation. I fetched nothing. I did not verify historical archive access, present store mediation, committee conduct, statistical independence of missingness from handedness, or the behavior of any future exact-parent join/revalidation code. Assertions about those future mechanisms are contract analysis or stated repair requirements, not observations of running code.

## Evidence ledger

- Read `BRIEF_SECTION6_REVIEW_R7.md`, `BRIEF_DRAFT_SECTION6_R7.md`, `SECTION6_DRAFT_AGY_R7.md`, `SECTION6_DRAFT_AGY_R6B.md`, `SECTION6_DRAFT_AGY_R5.md`, `SECTION6_REVIEW_R6B_CODEX.md`, and `SECTION6_REVIEW_R6B_GPT56.md` as text.
- Read current `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` §2.7, §4, and §5 around acceptance states, Stage C, complete-sample guards, and verdict outcomes.
- Ran `shasum -a 256 SECTION6_DRAFT_AGY_R7.md`; it matched the brief.
- Ran `git diff --no-index -- SECTION6_DRAFT_AGY_R6B.md SECTION6_DRAFT_AGY_R7.md` and mechanically parsed row and clause inventories. The table has twenty rows in both drafts; changed rows are I, J, and P; changed clause bodies are none.
- Mechanically compared R5/R7 §6.2 and §6.3. §6.2 matches after whitespace normalization; §6.3 carries the same seven bullets, with only the editorial heading parenthetical removed.
- Searched R7 and current V15 for definitions of the asserted terminal states, calibration applicability, and locked adequacy conditions. R7 contains the assertions; no defining contract was found in current V15.
- Ran no fetch, data-directory read, scientific computation, sealed-store operation, preregistration edit, or write other than this report.

**NOT CLEAR**