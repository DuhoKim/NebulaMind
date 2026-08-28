HARNESS_UNSOUND_A12_ZERO_COUNT_INVALIDATES_STRONGEST_TIER_VERDICT
FALSE_PASS_POSSIBLE:  YES
CLASSIFIER_SOUND:     NO

# Dispositive failure

`a12_entry8_indistinguishable.py`, check **“COUNTED: the paper contains no scientific-notation value and no numeric magnitude threshold anywhere in its text”**, is already false on the pinned input while reporting PASS.

The two patterns return `len(sci) == 0` and `len(ineq) == 0`, but the source contains, among other numeric inequalities, `0≤r<∞`, `0<ξ≪r_g`, `0<ξ≪1`, and `r_S0>r_g`. The regex only recognizes scientific notation in two very particular renderings and inequalities beginning with `≳`, `≲`, or `>` followed by a scientific-notation value. It does not recognize ordinary `<`, `≤`, `>`, `≪`, integers, decimals, percentages, equation values, or most LaTeXML/ar5iv renderings.

This is load-bearing: a12 turns that zero into “there is no candidate number,” “not one scientific-notation value in the whole text,” and the “strongest available sense” tier verdict. The count cannot support those statements. The underlying CONSISTENCY-ONLY tier may still be right, but this harness did not establish the advertised stronger verdict.

# Classifier audit

The classifier is not sound.

- Its advertised `1/1/19/7/24 over 52` is not the current battery. Running it now reports 55 checks: `1/1/19/9/25`. The three a12 checks were evidently added without refreshing the self-audit.
- It mistakes source-derived string flags for COMPUTED. For example, a12's `ind` is assigned from `"..." in T`, but `chk(..., ind)` is classified COMPUTED because expansion carries the name `T` without carrying the membership operation. The same defect affects bare booleans such as a10's `hedge_rough`, `hedge_assum`, and `observed`, and several a7 flags.
- Conversely, binding-map unions are path- and order-insensitive. Reassigning a name preserves every old dependency, and a function is marked data-driven if any name anywhere in its body touches a data-hint identifier. This can turn a constant final value into a source-driven one.
- The lone TAUTOLOGY (`a1`'s `ok_all`) is a third control-flow artefact: the classifier sees the initializer and AugAssign dependencies but does not model the conditional assignments `ok_all = False`.
- `DATA_HINTS` is identifier spelling, not provenance. Any unrelated variable named `T`, `A`, `G`, `N`, etc. is treated as source data; source variables with other names require a lucky transitive path to a recognized call.
- `string_test` is inferred from source-text substrings and a short call-name list, not AST semantics. It misses expanded membership tests and methods such as `count`, while `len` is treated as generic data evidence. The resulting STRING/MIXED/COMPUTED totals are not reliable.

# The five renamed checks

Only the a8 rename is fully honest. It says exactly that this particular regex did not match and names major classes it misses.

The other four are substantially cosmetic:

- `a6`, **“QUOTED ... contains no time-varying Lambda/r_S statement”**: `drift` only detects `time-varying|evolving` immediately before `Λ|Lambda|r_S`. It misses “r_S changes with time,” “Lambda depends on a/t,” “a variable horizon,” reversed word order, equations, and figures. The caveat is in the detail, but the check name still asserts corpus-wide absence.
- `a9`, **“QUOTED ... fixes lambda from the observed Lambda ... direction of inference”**: three disconnected presence tests do not establish that `λ=...` is fixed *from the observed* Lambda or that the threshold is downstream of it. `from_obs` merely matches “This small value results from the small cosmological constant.”
- `a10`, **“QUOTED ... FROM the lack ... and no forward uncertainty ... anywhere”**: the reverse-direction quotation is reachable, but `fwd_err` is one narrow theta glyph/spacing regex. It misses prose uncertainties, asymmetric errors, intervals, tables, figures, `\pm` renderings, and other theta encodings. “Anywhere” remains an overclaim.
- `a10`, **“QUOTED ... evaluates it at the measured Omega_Lambda -- direction ...”**: `chain` and `from_ol` only show an equation and an evaluation phrase somewhere. They do not test “measured,” connect the clauses, or exclude the anomaly as an input. The rename labels evidence as quotation while the name/detail still state the adjudicated conclusion.

# 29 additional defective checks

These exclude the five above and exclude a3's already-confessed truncation failure.

## a1

1. **“every target produced a file with its own arXiv id in the header region”** authenticates only an ID string. A different paper or arbitrary payload with `[ID]` injected into its first 4096 bytes passes.
2. **“all six ranked targets accounted for”** is `len(results) == 6`. The loop appends a row on fetch failure, so six total failures still pass this check.

## a2 (the survived-finding lane)

3. **“Table 1 reproduces the text's '63'”** never reads Table 1 or the printed 63. `W0=0.0062` and 63 are both hard-coded; an empty or different source passes.
4. **“the paper's two printed upper bounds are the SAME number”** is only hard-coded `f10≈10`. It never tests either printed bound.
5. **“both '63 Hz' and '10 Hz' ... in the pinned text”** allows `63` anywhere, `Hz` anywhere, and `10 Hz` elsewhere. It does not require `63 Hz`, much less that both are bounds on the same quantity.
6. **“so omega in this paper is ANGULAR”** tests only an external Schwarzschild control assembled from hard-coded constants. It never tests the paper's definition/convention for omega. A different paper passes.
7. **“top of the paper's own mass range ... outside the LISA band it claims”** hard-codes the mass range, LISA band, and mode coefficient. It does not verify that this paper states any of them.
8. **“pre-authorises the escape from any null result”** matches only the isolated phrase `not amplitude-wise sensitive enough`; it does not bind that phrase to a null result or establish the universal “any” consequence.
9. **“no rate-ESTIMATE construct ... anywhere”** passes on an empty/truncated/different paper. It also misses `/yr`, `yr−1`, `s−1`, “annually,” “per unit time,” “one event every...,” “detection count,” “volumetric rate,” `Mpc−3`, and rates given only in tables/figures. Calling the automated claim narrow does not make it complete over “anywhere.”

## a4 (browser-reassembled sources)

10. **“both papers reassembled from overlapping captures”** means only that two splice attempts returned non-None. Neither the captures nor the emitted header authenticate publisher identity/content; a different overlapping document can pass.
11. **“every landmark from START, MIDDLE and END ... present”** does not establish completeness between landmarks, correct order, uniqueness, or correct paper identity. A source can lose arbitrary blocks and pass.
12. **“each file recovers >=95% ...”** explicitly permits a 5% truncation and compares against a browser-reported character count whose normalization/furniture basis is not checked. Corruption compensated by duplication also passes.
13. **“the seams did not duplicate text”** counts one tail boilerplate sentence. Duplication at either actual seam, or anywhere before that boilerplate, passes. This is particularly source-sensitive because citation markers already differ between captures and the normalized fallback's index mapping is not provenance-preserving after citation removal.

## a5 (the other survived-finding lane)

14. **“two stated central values ... inconsistent”** never parses either stated value. `6e22` and `11` are constants, so an empty/different source passes.
15. **“three peak positions the paper names ...”** tests only identities at hard-coded Delta values 0 and 2 (not even Delta 1). It never verifies Equation 11, the named peaks, or the quoted span.
16. **“observed Lambda ... every modal location the paper names, on its own tau_O”** is wholly source-independent: tau=13, modes, H0, Omega_Lambda, and labels are constants. It passes unchanged on an empty or different paper. This is the check closest to the survived substantive finding.

## a6

17. **“pinned third-party fit puts w0 within ~2 sigma”** accepts any four regex-shaped negative decimals anywhere in the file; it does not authenticate rows as w0, the dataset, confidence convention, or even a table. Four unrelated matching numbers in a different paper pass.

## a7

18. **“makes no observational prediction”** is `predicts == 0` for four narrow English templates. It misses “we forecast,” “should observe,” “signature,” “testable,” “measurement,” equations/tables/figures, and paraphrases. Truncation or a different theorem paper passes. The count of five obstruction words also does not establish the semantics of the tier definition.
19. **“load-bearing junction ... degenerate and non-comoving ... falls outside Theorem 1”** finds three phrases anywhere across two papers. It does not identify which junction is load-bearing, connect “is not always constant” to chi-star/the junction, or verify that the same boundary is the theorem's subject.
20. **“concedes a past singularity, so it never claims completeness”** tests presence of a past-singularity phrase, not absence of a completeness claim. “Never claims” is not entailed by the predicate, and the two claims could coexist in different senses or regions.
21. **“texts do NOT name the same technical ingredient”** defines “same ingredient” as only three literal phrases. Synonyms, equations, stress-energy descriptions, or an unnamed equivalent component all pass the negative test.

## a8

22. **“reports a 3.1 sigma preference ... from DESI+CMB”** merely requires any `3.1 sigma` and `dynamical dark energy` anywhere in an authenticated title-level document. The number need not modify that result or dataset combination.
23. **“significance is combination-dependent, spanning ...”** collects every sigma value in the full paper and compares extrema. Values for unrelated parameters/tests can create the span; no dataset/result association is tested.

## a9

24. **“explicit numeric threshold”** uses `C >[^.]*`; it does not require a number at all. “C > x” or a corrupted tail passes.
25. **“analyses all three curvature cases and commits to none”** tests one closed-universe sentence plus one unrestricted-flat/open phrase. It neither counts/identifies all cases nor tests the absence of a commitment about our Universe.
26. **“C is NOT a free model parameter ... observable ... conserved ... theory-determined scale”** tests only “representing the product...” plus an `x_eq` token. None of free/not-free, observable, conserved, or theory-determined normalization is established.

## a12

27. **“no scientific-notation value and no numeric magnitude threshold anywhere”** is the dispositive false PASS above.
28. **“paper's own conclusion is modal”** counts three phrase templates over the entire file, not the conclusion. The current four hits include abstract material and an unrelated speculative sentence. A different paper with two “may be” occurrences passes.

## Cross-cutting wrong-input defect

29. None of a2, a5, a6, a7, a9, a10, or a12 pins an expected digest or robust bibliographic identity before its substantive checks. Several print a digest, but do not compare it. Presence-heavy scripts can therefore pass on a different paper sharing a few phrases; hard-coded a5 passes with no relevant paper content at all.

# Counts/absence coverage summary

- `a2 rate_hits == 0`: misses the rate forms listed in defect 9, plus image-only/table-only rates; truncation is indistinguishable from absence.
- `a7 predicts == 0`: misses synonyms and non-prose predictions listed in defect 18.
- `a8 has_threshold is None`: honestly caveated, but additionally misses confidence levels/credible intervals, p-values, odds, likelihood ratios, and thresholds separated by more than 60 characters or with the number before the rejection verb.
- `a10 not fwd_err`: misses essentially every uncertainty representation except one narrow glyph form.
- `a12 sci == 0 and ineq == 0`: misses ordinary inequalities and almost all numeric formats; demonstrably false on the current source.
- `a12 mays >= 2`: measures whole-document phrase frequency, not conclusion modality, and duplicate/reassembled text can inflate it.

# Bottom line

False PASS is not merely possible; it occurs on the current a12 input. Empty/truncated or different-paper false passes are also possible in a1, a2, a5, a7, a9, a10, and a12. The five renames mostly relabel evidence without upgrading the predicates. The classifier misses exactly this because it classifies dependency form, imperfectly, and cannot compare a check name with what its predicate proves.
