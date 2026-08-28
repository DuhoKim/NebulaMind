# V30 WHOLE-DOCUMENT REFEREE REVIEW — GPT56

## Verdict

**NOT CLEAR.** The Land null is a legitimate and useful counter-anchor, and the paragraph that reports Land's abstract does not dishonestly imply that this study expects a null. The addition nevertheless fails in two substantive places: it compares a reported monopole/relative-excess figure to Longo's dipole amplitude as though they were commensurate, and it overstates what the later McAdam–Shamir reanalysis establishes about the post-mirror residual. Independently, the required trace checker fails because V30 omits the now-in-band V28→V29 row and the current V29→V30 sidecar mapping. These are defects in this V30 document state, not authorization questions; the unfinished programme remains blocked exactly as V29 stated.

## Exact subject and predecessor comparison

I recomputed both SHA-256 digests from the current bytes:

- V30 supplied: `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`
- V30 recomputed: `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`
- V30 comparison: **MATCH**, exact 64-hex equality.
- V29 supplied: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- V29 recomputed: `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`
- V29 comparison: **MATCH**, exact 64-hex equality; this is the predecessor I cleared.

A direct unified diff shows exactly the dispatched delta: the title changes V29→V30 and six blank/content lines add three paragraphs at V30 lines 118–122. In diff terms that is eight changed lines (seven additions and one removal), with a net six-line increase. No other byte region changed.

I then reread the whole V30 document, not only the delta. The exact diff plus the whole-document read confirms that V29's scope sentence at V30 lines 131–133 and §2.7 item 7 at line 378 survive unchanged.

## Numbered findings

### 1. HIGH / BLOCKING — §1 line 120 — the “nearly four times” comparison is not a valid comparison of like quantities

**Why it fails.** The sentence says the Galaxy Zoo value is an “~15% ... handedness asymmetry,” calls Longo's tested amplitude 4%, and concludes that the former was nearly four times the latter. The numerical division `15 / 4.08 = 3.67647` is arithmetically correct but scientifically non-comparable in two independent ways.

First, McAdam & Shamir's “~15%” is a relative-count excess associated with Land's uncorrected/superclean counts, not the normalized sign asymmetry used by a dipole amplitude. Land reports superclean `(Z,S)=(6,106,7,034)`. Those bytes imply `(S−Z)/(S+Z)=0.070624`, whereas `(S−Z)/Z=0.151982`. Thus the cited “15%” and `A_LONGO=0.0408` do not even share a denominator. The document's phrase “handedness asymmetry” erases that distinction.

Second, Land's bias is a direction-independent net winding preference (a monopole/intercept), while Longo's `A·cos θ` is a direction-dependent dipole/slope. A truly constant bias is absorbed by the centred estimator's intercept; its magnitude alone is not dipole contamination. Partial footprint and low `Var(cos θ)` can make intercept and slope poorly identified, and a position-dependent classification bias can imitate a slope, so the bias is still legitimate qualitative motivation for a mirror/antisymmetry prerequisite. What does not follow is that a monopole “nearly four times” a dipole amplitude presents a correspondingly larger threat. The sentence therefore implies quantitative danger that its own metric and §1/§3 estimator do not establish.

The phrase “in the same survey family” also over-compresses the provenance: Land's Galaxy Zoo 1 sample is SDSS, while this successor is defined on the DESI Legacy Surveys branch. The tasks are closely related, but the surveys are not literally the same family without an explained meaning.

**Smallest sufficient repair.** Remove the ratio and distinguish the metrics and roles. For example: “A later reanalysis describes an approximately 15% relative excess in one uncorrected Galaxy Zoo count comparison; this is a monopole classification preference, not a quantity directly comparable to Longo's 0.0408 dipole amplitude. Its relevance is qualitative: a large handedness-dependent response in a closely related classification task makes the frozen mirror/antisymmetry check a prerequisite, while only position-dependent residual bias could imitate the tested slope.” If retaining a number, name its exact numerator, denominator, sample, and secondary-source provenance.

### 2. MEDIUM / BLOCKING — §1 line 122 — the “split” sentence tilts by overstating the post-mirror result and incompletely attributes the source

**Why it fails.** “The literature is split” is defensible, and the ordering itself is reasonably balanced: Land's null is presented first and in detail, while the later challenge is introduced with the epistemically appropriate verb “argues.” But the next phrase says the later reanalysis “argues the residual post-mirror asymmetry is real.” That is stronger than arXiv:2302.06530's treatment of that residual. The paper says the post-mirror residual is about 1.5–2%, but gives `P≈0.13` and `P≈0.21` and explicitly says those probabilities are not statistically significant; it argues that the direction and magnitude do not conflict with other reports. Its affirmative non-random/dipole results come from separate SpArcFiRe analyses of much larger selections. V30 fuses those two evidentiary grades and thereby brushes past the null in the direction favourable to this study.

The citation is also labelled “Shamir,” although arXiv:2302.06530 is authored by Darius McAdam and Lior Shamir. That incomplete attribution is especially avoidable in a paragraph whose purpose is provenance and balance.

**Smallest sufficient repair.** Write, for example: “A later reanalysis (McAdam & Shamir, arXiv:2302.06530) notes a directionally consistent but individually nonsignificant post-mirror residual (`P≈0.13–0.21`) and separately reports non-random/dipole results from SpArcFiRe analyses; it argues those results align with other methods.” “The literature is split” can remain after that qualification.

### 3. HIGH / BLOCKING — §10 lines 819–861 and `gates/FINDINGS_MAP.md` — the required trace check fails on two missing obligations

**Why it fails.** I ran the checker myself. It exited 1 and reported:

```text
prereg trace check — PREREG_SUCCESSOR_DRAFT_V30_20260827.md
  MISSING: no §10 table row for V28 → V29
  SIDECAR MISSING: V29 → V30 is the current transition and is not mapped in gates/FINDINGS_MAP.md
  29 computed transition(s); 2 problem(s)
```

This is not a stale assertion from the brief. Under V30's own checker contract, V28→V29 is now earlier than the subject and must be represented in-band in §10. The V30 table still ends at V27→V28. Separately, the current V29→V30 transition must be mapped in the external sidecar; `FINDINGS_MAP.md` contains V28→V29 but no V29→V30 entry. The fact that the delta came from a human direction does not waive the document's stated finding/change mapping discipline; it needs an honest authority/motivation mapping rather than an invented referee finding.

**Smallest sufficient repair.** Add the mechanically generated V28→V29 row to the next draft's §10 table, add an honest V29→V30 sidecar entry identifying the principal's Land-2008 motivation direction (without fabricating a finding ID), and rerun `prereg_trace.py .. --check <new-draft>` to exit 0. Because the in-band repair changes document bytes, this requires a successor draft rather than silently changing the pinned V30 subject.

## Provenance and specific brief questions

1. **Land null as motivation:** The counter-anchor paragraph itself is fair. It says Land found statistical isotropy and no significant dipole, places that null before Longo chronologically, and does not say this preregistration expects to find nothing. The failure is not null-overweighting; it is the subsequent quantitative comparison and overcompressed rebuttal.
2. **Land abstract:** arXiv:0803.3247 directly supports `~37,000`, “consistent with statistical isotropy,” “no significant dipole signal,” and the statement that prior results may be affected and explained by bias.
3. **~15% provenance label:** “as reported by a later reanalysis, not read from Land's body text” is honest as far as source tier goes, but insufficient because it omits the metric definition and then uses the value in a cross-metric ratio. McAdam & Shamir do report an approximately 15% “difference”; Land's counts show why that is a relative excess rather than normalized asymmetry.
4. **Unresolved subset size:** I searched the complete V30 bytes for `11,000`, `11000`, `91,303`, and `91303`. None appears. The only `subset` occurrence is unrelated §2.7 hypothetical prose. The deliberately unresolved Land subset-size figure therefore appears nowhere. V30's `~37,000` is Land's abstract-level full analysis sample, not the omitted bias-subset size.
5. **Scope and §2.7:** The V29→V30 diff does not touch V29's scope statement or §2.7. V30 lines 131–133 still limit the study to Longo's published amplitude and axis and explicitly exclude testing Shamir or isotropy. V30 line 378 and its continuation still mark BS-2a DESIGN/defined/UNFILLED and state that conditional independence from handedness given position is not established.

## Required tool executions

### `prereg_lint.py`

Command:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V30_20260827.md --gates .`

Exit **0**:

```text
prereg lint — PREREG_SUCCESSOR_DRAFT_V30_20260827.md
  §7 data rows: 23 (15 class P, 8 class E) — 22 carry a BS- identifier
  no inconsistencies found (all 6 checks demonstrated they can fail)
```

### `prereg_lint.py --self-test`

Command:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py ../PREREG_SUCCESSOR_DRAFT_V30_20260827.md --gates . --self-test`

Exit **0**: all six controls (`check_repair_citations`, `check_prose_counts`, `check_class_agreement`, `check_lock_identity`, `check_list_numbering`, `check_slots_exist`) reported `OK`; self-test reported 6 controls and 0 failures.

### `prereg_trace.py --check`

Command:

`python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_trace.py .. --check ../PREREG_SUCCESSOR_DRAFT_V30_20260827.md`

Exit **1**, with the two missing obligations quoted in Finding 3.

## Failed attacks and held boundaries

1. **Subject-substitution attack — failed.** Both V30 and V29 match their supplied full SHA-256 pins.
2. **Hidden-delta attack — failed.** The direct diff contains only the retitle and the six added §1 lines; no established V29 rule was silently changed.
3. **Null-expectation attack — failed.** Land is explicitly a counter-anchor, not a forecast. The text retains Longo's amplitude as the target and says it does not test isotropy or Shamir.
4. **Land-abstract quote attack — failed.** The title, authors, sample scale, null language, and bias warning match arXiv:0803.3247's abstract.
5. **Unresolved-subset-number leak attack — failed.** Neither `~11,000` nor `91,303` occurs in V30.
6. **Unfinished-programme overclaim attack — failed.** The whole-document reread confirms BS-2a remains DESIGN/UNFILLED; only one of fifteen class-P slots is filled; BS-2v and findings 1, 2, 2b and 3 remain unresolved; Rows C2 and E cannot run; the 995/1,000 Stage-P result remains `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`; BS-5p remains unfillable pending rerun; and BS-6 plus the first image byte remain blocked.
7. **Established decision-boundary attacks — failed.** The 962/1,000 power boundary, calibration lower-bound halt, post-unblinding-removal consequence, numeric verdict inequalities, and Clause-10 unresolved/execution block are unchanged from the exact V29 predecessor I cleared.

## Testimony and limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or authorize an image byte, execute inference, run Stage P, unblind anything, or modify either draft.
- Historical claims about authorization times, prior gate chronology, custody, survey measurements, and whether an image byte has ever been fetched remain **Testimony**. I verified the current draft bytes, predecessor bytes, complete textual delta, whole V30 text, named public arXiv sources, arithmetic derived from quoted Land counts, and all three required tool executions.
- The only write by this seat is this report.

**NOT CLEAR**