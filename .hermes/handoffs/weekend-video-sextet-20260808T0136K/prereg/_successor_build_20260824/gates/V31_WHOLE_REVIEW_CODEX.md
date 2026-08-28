# V31 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** I independently verified the named V31 bytes, diffed the exact V30 predecessor against V31, reread all 880 lines of V31, checked the McAdam–Shamir quotations against arXiv:2302.06530 itself, and ran all four required tool commands. V31 correctly repairs the trace-custody failure and the treatment of Land's post-mirror residual. It also removes the invalid 15%-versus-4.08% ratio. One replacement claim remains blocking: line 120 now says BS-3's antisymmetry receipt measures and bounds the position-dependent bias component, but the instrument's own stated boundary says antisymmetry does not bound monopole × sensitivity-gradient coupling or upstream position-dependent systematics. The paragraph also reintroduces an unearned magnitude inference by saying only a “modest” component is needed because both quantities are percent-level despite its own denominator caveat. This verdict does not authorize any run, image acquisition, unblinding, or other blocked work.

## Digest and predecessor comparison

Subject: `../PREREG_SUCCESSOR_DRAFT_V31_20260828.md`

- supplied V31 SHA-256: `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`
- independently recomputed V31 SHA-256: `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`
- comparison: **MATCH — exact 64-hex equality over the named V31 bytes**
- supplied V30 SHA-256: `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`
- independently recomputed V30 SHA-256: `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`
- comparison: **MATCH — this is the exact V30 byte state CODEX reviewed as NOT CLEAR**

The direct unified diff contains only the dispatched delta: the V30→V31 retitle; replacements at §1 lines 120 and 122; and insertion of the V28→V29 and V29→V30 rows in §10. A `SequenceMatcher` decomposition found three contiguous non-equal regions: title replacement, the contiguous line-120/122 paragraph region, and the two-row insertion. No other byte region moved. The four substantive edits named in the brief are therefore present and exclusive.

## Numbered findings

### 1. HIGH / BLOCKING — §1 line 120 — BS-3 is credited with measuring a position-dependent bias component that its antisymmetry identity does not bound

**Why it fails.** The first half of the repair is correct: V31 distinguishes the approximately 15% relative count difference from Longo's normalized dipole amplitude; removes the ratio; identifies uniform classification preference as an intercept; and states that a centred estimator absorbs that intercept. The repair then overreaches in two linked sentences:

> “A bias that large ... needs only a modest component that tracks position along the tested axis, because the bias and the target signal are both percent-level quantities.”

> “BS-3's `antisymmetry_receipt` measures the parity-even part directly, so the position-dependent component is bounded by measurement instead of by assumption.”

The antisymmetric construction is `χ(x) = (w(x) − w(mirror(x)))/2`. Its receipt can verify exact mirror antisymmetry of the implemented instrument and cancellation of the parity-even part of `w` on a paired image. It does not measure a sky-position dependence in the survey population. The lane's own instrument description, `paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` §2.3 lines 99–108, states the opposite boundary explicitly: the identity says nothing about chirality introduced upstream of the analysis raster; it does not equalize sensitivity across the sky; “a nonzero global offset ... multiplied by a sky gradient in sensitivity, produces a spurious dipole ... which must be bounded by an explicit control, not assumed away”; and it does not launder upstream sample selection. BS-3's row in V31 §7 line 704 names instrument identity, weights, threshold, and antisymmetry identity; it does not name a position-stratified bias measurement capable of closing those boundaries.

The “modest component” rationale is also not earned by calling both quantities percent-level. The paragraph correctly says the approximately 15% and 0.0408 do not share a denominator, then uses their apparent scales to infer that only a modest projection is needed. Under the natural conversion of a 15% relative excess `(S−Z)/Z` to normalized sign asymmetry `(S−Z)/(S+Z)`, the corresponding value is about 6.98%, and a 4.08% component is about 58.5% of it—not a source-supported “modest” fraction. This calculation is illustrative, not a claim that the unresolved denominator has thereby been established; it shows why the adjective cannot be inferred without defining the metric and projection model.

The result is not that line 120 has retreated too far to motivate BS-3. The defensible motivation survives: the historical bias shows that this task can carry a large parity-label preference, so exact instrument antisymmetry is a prerequisite against the class of parity-even classifier bias it actually cancels. What fails is promotion of that receipt into a measurement bound on all position-dependent contamination.

**Smallest sufficient repair.** Keep the source quotations, denominator caveat, intercept/slope distinction, and qualitative motivation. Delete “needs only a modest component ... because ... percent-level quantities,” delete “a perfectly position-free bias is not the realistic case,” and narrow the final claim to what BS-3 proves. For example: “The historical preference motivates requiring exact mirror antisymmetry before use: BS-3 verifies that the instrument cancels parity-even score components and cannot chirality-filter through an absolute confidence threshold. It does not by itself bound upstream chirality, sky-dependent sensitivity coupling, or position-dependent sample bias; those remain governed by the document's separate controls and stated assumptions.” If the intended claim is genuinely to bound a position-dependent component, add a separately specified, pre-image, position-stratified control and receipt rather than assigning that capability to the antisymmetry identity.

## V30 blocker-by-blocker delta adjudication

1. **CODEX-V30-1 / monopole–dipole conflation: partially repaired, still blocking through the replacement overclaim.** The ratio, same-survey-family claim, and commensurability error are gone. The intercept/slope distinction is correct. Finding 1 identifies the narrower remaining defect.
2. **GPT56-V30-2 / post-mirror residual: repaired.** arXiv:2302.06530 names Darius McAdam and Lior Shamir. Its abstract contains “lower than 0.01” and “dipole axis with statistical strength of 2.33σ to 3.97σ.” Its body reports `P∼0.13` and `P∼0.21` for the mirrored-image control and says, verbatim, “These probabilities are not considered statistically significant, which can possibly result from the low number of galaxies, but the direction and magnitude of the distribution also does not conflict with the observed distribution.” V31 accurately distinguishes that nonsignificant residual from the paper's separate significant analyses and does not overcorrect by calling the residual null or conflicting.
3. **CODEX-V30-2 / trace custody: repaired.** The generated V28→V29 and V29→V30 rows are present in §10. `gates/FINDINGS_MAP.md` maps V29→V30 to `PRINCIPAL-20260828-LAND-NULL` and V30→V31 to the five named referee findings. `BRIEF_V30_REVIEW.md` lines 9–20 independently records the human direction to add the Land 2008 null; using a human-instruction identifier rather than inventing a referee finding is honest. The current V30→V31 transition is correctly absent from V31's in-band table and present in the sidecar.

## Source-quotation verification against arXiv:2302.06530

I checked the arXiv record and full body, not the brief's transcription.

- Authorship/title: **MATCH** — Darius McAdam and Lior Shamir, “Reanalysis of the spin direction distribution of Galaxy Zoo SDSS spiral galaxies.”
- Line 120, “that large difference of ∼15%”: **MATCH**, allowing arXiv HTML's duplicated math-rendering markup around `∼`.
- Line 120, “bias of the human perception or the user interface, rather than a reflection of the real distribution of spiral galaxies in the sky”: **MATCH** as a contiguous body-text fragment.
- Line 122, “lower than 0.01”: **MATCH** in the abstract.
- Line 122, “dipole axis with statistical strength of 2.33σ to 3.97σ”: **MATCH** in the abstract, normalizing duplicated HTML math markup.
- Line 122 residual quotation beginning “these probabilities are not considered statistically significant”: **MATCH** as a contiguous body-text sentence. The immediately preceding body text supplies `P∼0.13` and `P∼0.21`, as V31 states.

These checks establish quotation fidelity and the residual/significant-analysis distinction. They do not reproduce McAdam and Shamir's analyses or endorse their scientific interpretation.

## Whole-document attacks that held

1. **Whole-file standing-state honesty held.** The complete 880-line reread retains: BS-2a DESIGN/defined/UNFILLED; exactly one of fifteen class-P slots filled; BS-2v UNRESOLVED; findings 1, 2, 2b and 3 UNRESOLVED; Rows C2 and E unable to run; Stage P `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`; BS-5p unfillable pending rerun; and BS-6 plus the first image byte blocked.
2. **§1 scope preservation held.** V30 and V31 lines 131–133 are byte-identical. V31 still tests Longo's published amplitude at the fixed published axis and explicitly does not test Shamir, BHU, A≈0.02, or whether the sky is isotropic.
3. **§2.7 conditional-independence disclosure held.** V30 and V31 line 384 are byte-identical. The draft still says independence of the catalogue-quality predicate from handedness conditional on position is “not established” and requires either a preregistered check or a stated assumption with risk.
4. **Trace scope held.** V31's current transition is non-self-referentially mapped in the sidecar, later drafts are out of scope, and the self-test actively demonstrates those rules.
5. **Existing execution blocks held.** Clause 10 remains non-executable because VOID reverse reachability is unresolved; BS-6 and the first image byte remain blocked. Passing lint/trace does not authorize execution.

## Required tool runs

All four commands were run from the assigned absolute `gates` directory, using the repository tools by absolute path because the tools directory is at `/Users/duhokim/NebulaMind/NebulaMind/tools`.

1. `python3 .../tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V31_20260828.md --gates .`
   - exit 0
   - `§7 data rows: 23 (15 class P, 8 class E) — 22 carry a BS- identifier`
   - `no inconsistencies found (all 6 checks demonstrated they can fail)`
2. `python3 .../tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V31_20260828.md --gates . --self-test`
   - exit 0
   - all six controls reported `OK`; `6 controls, 0 failure(s)`
3. `python3 .../tools/prereg_trace.py .. --check ../PREREG_SUCCESSOR_DRAFT_V31_20260828.md`
   - exit 0
   - `30 computed transition(s); 0 problem(s)`
4. `python3 .../tools/prereg_trace.py .. --check ../PREREG_SUCCESSOR_DRAFT_V31_20260828.md --self-test`
   - exit 0
   - all three scope controls reported `OK`; `3 scope rules, 0 failure(s)`

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or authorize any image byte, run Stage P/C, execute inference, unblind anything, modify V30 or V31, or mutate git.
- The current document's statements that no image byte has historically been fetched or authorized, its survey-derived counts, historical authorization chronology, custody history, and implementation claims outside the required checkers remain **Testimony** in this pass.
- I verified the current textual execution blocks and unfinished-programme posture, not the historical external events they describe.
- This report is my only intended durable write.

## Evidence ledger

Content read: `BRIEF_V31_REVIEW.md`; all 880 lines of V31; exact V30 predecessor; CODEX and GPT56 V30 whole-document reports; `BRIEF_V30_REVIEW.md`; `FINDINGS_MAP.md`; `FRAMING_LEVERAGE_IS_IDENTIFIABILITY_20260828.md`; the relevant antisymmetry guarantee and boundary in `paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md`; arXiv:2302.06530 abstract and body.

Independent executions: V31 and V30 SHA-256; unified V30→V31 diff; non-equal-opcode count; byte comparisons for §1 lines 131–133 and §2.7 line 384; standing-state string checks; conversion illustrating why “modest” is not derivable; all four required lint/trace commands and self-tests.

**NOT CLEAR**