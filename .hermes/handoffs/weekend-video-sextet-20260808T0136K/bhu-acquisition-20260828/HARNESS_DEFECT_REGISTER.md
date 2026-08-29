> **SWEEP PARKED 2026-08-29 11:40**, by Duho's redirect. **15 entries audited, 0 tiers changed;
> 36 of 51 remain unaudited.** The null covers the 15 and no more. Parked at the top of the
> depth queue: entry 39 was next by the density rule, entry 27 after it. The lane moved to
> entry 31 — the corpus's one live calibrated falsifier — because a sixteenth consistency-only
> audit cannot compete with a real prediction being decided by data now.

> **THIS FILE NOW HAS A CHECK: `b8_verify_register.py`, 5/5.** Blanc, relaying Hwao: *"This is the
> one artifact in the lane with no adversarial reader... Everything I've caught in it today I
> caught by accident."* True of this register too — it carries tier conclusions, retraction status
> and re-derivation state for the whole corpus, and until 15:10 today nothing had ever checked it.
>
> `b8` asserts against the filesystem: **12 named scripts all exist and all exit 0**; all 10
> entries in the §1h table resolve to a real bibliography entry with a parseable tier; the
> retracted second-falsifier claim survives **only as a quoted retraction**; and entry 22 is
> **actually** refiled as THEORETICAL-OBSTRUCTION rather than merely claimed to be.
>
> **b8's own first run verified ONE script and reported PASS** — its filename pattern matched
> backticks only, while the register names scripts as `a12`, "a6's check 4", "b7". The narrow-
> pattern defect, inside the tool built to audit the record of that defect. Widened to 12 before
> the result meant anything. **What b8 still cannot check is named in its own section 6: prose
> claims naming no script or entry, scripts that run but no longer test what the register says,
> and §1h narrative that is wrong while its numbers are right.** Blanc reads it by hand on refresh;
> b8 is the floor under that, not a substitute.

# Harness defect register — Tori, 2026-08-29 ~05:00 KST

Two fresh-context seats attacked my check battery after I audited it myself and pronounced it
sound. **Both found substantially more than I did.** This file records every defect they raised,
because I cannot repair 34 checks tonight and an unrecorded defect is worse than an open one.

    CGATE_HARNESS_VERDICT.md   HARNESS_UNSOUND_A12_ZERO_COUNT_INVALIDATES_STRONGEST_TIER_VERDICT
                               FALSE_PASS_POSSIBLE: YES | CLASSIFIER_SOUND: NO
    AGATE_HARNESS_VERDICT.md   HARNESS_GAPS_FOUND_5
                               FALSE_PASS_POSSIBLE: YES | CLASSIFIER_SOUND: NO

## 1. FIXED TONIGHT — a check that was FALSE while printing PASS

`a12` check 2 claimed "the paper contains no scientific-notation value and no numeric magnitude
threshold anywhere in its text". **The pinned source contains 18 inequalities.** My patterns
recognised two renderings of scientific notation and inequalities beginning with a magnitude, so
they could not see `0≤r<∞`, `0<ξ≪r_g`, `r>r_g/4` and the rest.

I reported that zero to Blanc as a finding — *"not one scientific-notation value in the whole
text"* — and it was false. **Withdrawn.** The entry-8 tier conclusion survives because it never
needed the count: it rests on a quoted indistinguishability sentence. But the count was reported
as evidence and it was wrong. Patterns repaired; the check now counts, inspects, and states that
the inequalities are coordinate-domain conditions rather than magnitude thresholds.

## 1b. THE SAME FALSE-ZERO REACHED THE RANDOM-DRAW AUDIT — retracted 05:15

Blanc asked how far the false-count defect reached. Traced: the narrow pattern appears in three
files. `a9` uses it to FIND a specific value (safe — a narrow pattern is safe for presence). The
other two used it for ABSENCE, and both were wrong.

`a14` check 1 claimed *"only entry 36 carries substantial numeric content; 24 and 40 carry none"*.
Rechecked with repaired patterns:

| entry | narrow (reported) | broader sci | inequalities of any form |
|---|---|---|---|
| 24 | 0 | 1 | **12** — `r < √(3/Λ)`, density comparisons |
| 36 | 21 | 21 | 72 |
| 40 | 0 | 0 | **17** — `f > 0`, `0 ≤ R` |

**"Carry none" was false for both, and I reported it upward as part of the draw result.**
WITHDRAWN. The tier conclusions for 24 and 40 are unaffected — they rest on quoted
agreement-language and an explicit unobservability statement respectively, not on the count —
but the count was offered as support and it was wrong.

**The general rule this yields:** a narrow pattern is safe for PRESENCE and dangerous for
ABSENCE. Finding a thing with a tight regex proves it is there; failing to find it proves
nothing. Every absence claim in this battery needs its pattern's blind spots named in the check.

## 1c. THE ACCUMULATOR — fixed 05:20, the only defect that could corrupt the CORPUS

`a1` check *"all six ranked targets accounted for"* was `len(results) == 6`, and the fetch loop
appends a row on failure (`results.append((entry, aid, txt_p, 0, False)); continue`). **Six
consecutive fetch failures would have passed it as six acquisitions.**

Every other defect in this register overclaims about a paper. This one could have certified an
empty corpus. Repaired: the verification loop now records an explicit per-row outcome list and
the check counts VERIFIED acquisitions (`6/6 verified out of 6/6 attempted`). The companion
`ok_all` control-flow flag — which both seats independently flagged as unreadable — is gone,
replaced by the same explicit list.

## 1d. GENERAL FINDING — narrow patterns are safe for presence, dangerous for absence

Promoted out of the per-check notes because it is the generating defect behind every false claim
in this register, and because **it reproduced independently in another lane within the hour**.

> A tight pattern that FINDS something proves the thing is there. The same pattern failing to
> find something proves nothing at all. Every absence claim is only as strong as its pattern's
> blind spots, and those must be named in the check itself.

Three false "zero" claims tonight — entry 8, entry 24, entry 40 — all came from one regex used
in the second mode. Blanc relayed this to Hwao's lane, where the dispositive object was a
citation parser **unsound in both directions at once**, too permissive and too narrow
simultaneously, whose canary tests only reported ABSENCE and so could detect neither defect.
Two lanes, two frameworks, one defect class, found independently.

## 1e. WHICH OF THE THREE DRAWN ENTRIES DEPEND ON A CONDEMNED CHECK

Blanc: *"from outside the lane those two cases look identical and someone reading this in the
morning cannot tell them apart."* Stated plainly:

| entry | tier verdict rests on | depends on a condemned check? |
|---|---|---|
| 24 | quoted: CMB analysis *"agrees with the black hole universe predictions"* — agreement language, not a threshold | **NO.** The withdrawn count was corroboration only. |
| 36 | quoted: derived bounds `36h₀/H₀ ≤ r ≤ …` place the shock at/beyond the Hubble distance, and the upper bound carries free parameter **R\*** | **NO.** Rests on reading the bounds, not on counting them. |
| 40 | quoted: *"could not be observed outside the black hole because of the infinite redshift at the horizon"* | **NO.** |

All three rest on quoted text. **None depends on the condemned count.** What the count was doing
was screening — deciding which of the three deserved a deep read — and it pointed at 36, which
was correct. So the draw's *conclusion* stands; its *screening step* was unreliable and could
have sent me past a paper that mattered.

## 1f. a2 REWIRED TO PARSE — the survived finding now rests on reading, not transcription

CGATE, on the lane where my finding SURVIVED its gate: *"'Table 1 reproduces the text's 63' never
reads Table 1 or the printed 63. `W0=0.0062` and `63` are both hard-coded; an empty or different
source passes."* True — and worse than the other defects in one respect, because that finding was
reported upward as confirmed by two seats, resting on two numbers I had typed in by hand.

Both are now **parsed from the pinned source** (after stripping Unicode format characters, which
is why the first attempt to match `63 Hz` failed — the text carries `is 63Hz` with a zero-width
character between):

    Table 1, n=0, l=2  ->  0.0062   parsed from the row "2 3 4 0 0.0062 0.0063 0.0063"
    printed with unit  ->  63       parsed from "is 63Hz"

If either parse fails the script now **aborts rather than falling back** to a hard-coded value.

### The repair caught my own error immediately

My first replacement for the "two printed bounds differ by 2π" check parsed **50**, not 10 —
section 4's range tops at `≲ 50 Hz` and the Discussion's at `≲ 10 Hz`, and both are two digits, so
the regex took the first. **The check FAILED loudly.** The hard-coded form it replaced
(`abs(f10 - 10.0) < 0.2`) would have passed while reading nothing at all.

Repaired to collect every printed bound: `[10.0, 50.0]` alongside the printed `63`. The check now
asserts that the source prints more than one upper bound for one quantity and that one equals
another divided by 2π — and names its limit, that this shows the numbers differ by 2π but not why.

**This is the clearest evidence in the register that hard-coding hides errors rather than merely
overclaiming.** The same check, reading instead of asserting, failed on its first run.

## 1g. I COMMITTED TWO BROKEN SCRIPTS AND CLAIMED THEY PASSED — 05:50

Correcting `247d613f2`, whose message said *"a2 now 12/12"*. It did not run. It raised a
`NameError` at check 3 and exited 1.

Both of my last two repairs broke their scripts the same way — I removed a variable
(`_disc` in a2, `counts` in a14) and left a later check referencing it — **and I committed both
without running them to completion.** I checked `a2 exit=$?` only afterwards, from the wrong
directory, got a path error, and misread that as the script passing.

| script | what I claimed | what it did |
|---|---|---|
| `a2` | "now 12/12" | `NameError: _disc` — aborted after 2 checks |
| `a14` | retraction applied and passing | `NameError: counts` — aborted after 1 check |

Both fixed; whole battery now runs clean, 15/15 scripts exit 0.

**The substantive point is that the a14 fix was not merely mechanical.** The broken reference was
`agrees and counts[24] == 0` — the tier check still *depended on the count I had just retracted*.
Removing that dependency is what the retraction actually required. So the crash exposed an
incomplete retraction: I had rewritten the count check and left the conclusion still resting on
it.

**And the meta-point, which belongs in this register more than the fix does:** tonight's entire
defect class is claims made without executing the thing that would falsify them. I spent the
night documenting that in my checks, and then did it twice in an hour with commit messages. The
gap between "I edited it" and "I ran it" is the same gap as between a check's name and its
predicate.

## 1h. WHICH TIER CONCLUSIONS REST ON A CONDEMNED CHECK — read this first

Blanc: *"From outside the lane a sound verdict and a lucky one look identical, and Duho reads this
cold in the morning."* So, per entry, stated exactly.

**The load-bearing fact: every tier conclusion in this sweep rests on QUOTED SOURCE TEXT, not on a
harness check.** The checks were corroboration. Six of the fifteen were additionally attacked by
two adversarial seats who read the papers themselves. No tier verdict has been shown wrong by any
defect found tonight.

| entry | tier outcome | rested on BEFORE | rests on NOW | status |
|---|---|---|---|---|
| 21 | PROSPECT confirmed | amplitude-deferral quote + a **rate-absence regex** | the same quote + **codex's hand adjudication of the rate question**, which the script now records as the thing that closes it | **re-derived** |
| 8 | CONSISTENCY-ONLY confirmed | indistinguishability quote + **"zero numbers in the text"** — which was **FALSE**, the paper has 18 inequalities | the indistinguishability quote **alone**; the count is withdrawn and no conclusion reads it | **re-derived** |
| 24 | QUAL-DIRECTIONAL confirmed | "agrees with" quote + **"carries zero numeric content"** — **FALSE**, 12 inequalities | the "agrees with" quote alone | **re-derived** |
| 36 | CONSISTENCY-ONLY confirmed | the derived bounds + free parameter R\*, read from the paper | unchanged — the bounds were always read, never counted | **re-derived** |
| 40 | CONSISTENCY-ONLY confirmed | unobservability quote + **"carries zero numeric content"** — **FALSE**, 17 inequalities | the unobservability quote alone | **re-derived** |
| 25 | promotion **REFUSED** | the "not solely" qualifier + a **narrow** no-drift pattern | the same quote + that absence **re-tested with a broadened pattern**: 0 sentences link Λ or r_S to any variation, in either word order | **re-derived** |
| 26 | QUAL-DIRECTIONAL confirmed | Eq.11's modal envelope + an identity check **on a hardcoded symbol that never opened the paper** | the envelope + both relations **located in the sources** — and the identity turns out to **span two papers** (Λ=3/r_S² is Part I's, r_S=3τ_O/2 is Part II's) | **re-derived** |
| 52 | CONSISTENCY-ONLY confirmed | the paper's conditional phrasing + a check *named* for direction of inference | the same phrasing + a check **renamed PRESENCE ONLY**, with the direction recorded as an attributed **human reading** (§1j) | **limit named — not re-derivable** |
| 23 | promotion **REFUSED** | the reverse-inference sentence + a **narrow** no-forward-uncertainty pattern | the same quote + that absence **re-tested broadly**: exactly 1 uncertainty near θ_S in the paper, and it is the 60±3 backward read-off itself | **re-derived** |
| 22 | category error found | theorem/proposition statements + a **narrow-pattern absence claim** ("no observational prediction") | the same quotes + that absence **re-tested with a broadened pattern and every hit inspected** | **re-derived** |

**How to read this cold.** Nine rows say *re-derived*: something in their support was condemned,
and the conclusion has since been rebuilt without it — in three cases because the condemned thing
was outright **false**. **One** says *limit named* — entry 52. Its direction-of-inference claim is not computable from a
text search, so the check now claims only presence and the direction is an attributed human
reading (§1j). **No row is unknown.**

## 1j. ENTRY 52 — a limit named rather than a check that pretends

CGATE: *"three disconnected presence tests do not establish that λ is fixed FROM the observed Λ
or that the threshold is downstream of it."* Correct — and **not closeable by a better pattern.**
Direction of inference is a reading, not a string property. A third regex would *simulate* a
judgement rather than perform one, which is the failure mode that got a parallel lane's citation
check quarantined after three adversarial rounds.

The check now claims only what a presence test supports: three phrases occur in the source.

**The direction is a human reading, recorded as such:**

> **Read by:** Tori (this session), 2026-08-29 ~02:00 KST, re-affirmed 08:20.
> **Basis:** *"This small value results from the small cosmological constant Λ = 1.1×10⁻⁵² m⁻²"*
> — λ is fixed **from** the measured Λ — and *"must reach the threshold (51) so that the Universe
> could start the observed current acceleration"* — C is required to satisfy a condition derived
> from that measurement.
> **Therefore:** observation constrains the model parameter, not the reverse — which is the
> definition of CONSISTENCY-ONLY, and why entry 52's tier is correct.
> **Not gated.** No seat has attacked this reading. It is one person's reading of two sentences.

### The three absence claims that HELD

Entries 22, 25 and 23 each had a narrow-pattern absence claim in their support — the shape that
was **false** for entries 8, 24 and 40. All three were re-tested with patterns broad enough to
catch what the narrow ones missed, and **all three held**: 3 hits in entry 22 (two of them the
author denying a prediction), **0** in entry 25, and **1** in entry 23 (the known backward
read-off). Six absence claims tested tonight, three false and three true — and nothing but running
the broader pattern separates them. That is the finding, not the score.

### Entry 22, the last unknown — and its absence claim HELD

Its support included the same shape that was false three times tonight: "makes no observational
prediction", tested by a narrow regex. Re-tested at 07:30 with a pattern broad enough to catch any
observational claim, and **every hit inspected**. Three sentences in the whole paper contain an
observational-sounding word:

- *"the following familiar **observation** sets our stage"* — a mathematical remark, not an
  astronomical one;
- *"it is not a **prediction** of the asymptotically flat parent geometry itself"*;
- *"a tuning of the junction data rather than a **prediction** of the parent geometry"*.

**Two of the three are the author explicitly denying a prediction.** So the absence is real, and
it strengthens rather than weakens the category-error finding: the paper distinguishes *tuning*
from *prediction of the parent geometry*, which is theorem-language, not observational-testability
language. This is the one absence claim tonight that survived broadening — recorded because it
shows the class is not uniformly wrong, only uniformly untrustworthy until tested.

### The honest residual

Four entries — **25, 26, 52, 23** — still have a condemned-but-not-re-derived check somewhere in
their support. In every case the check is a presence test dressed as a semantic claim, the tier
conclusion rests on a quotation the seats read independently, and two of the four are *refusals*
of my own proposed changes, which is the direction that does not inflate the corpus.

**What I would not yet certify:** that the harness independently corroborates any of the fifteen.
It does not. The corroboration is the gates and the quotations. Anyone reading this in the morning
should treat the check batteries as working notes, not as verification.

## 1i. a4 CLOSED OUT — two strengthened, one restated as a smoke test

CGATE's three remaining a4 defects, worked 06:45. a4 matters because its output IS the pinned
source for entries 25 and 26.

**#10 identity — strengthened.** Was "two splice attempts returned non-None", which a different
overlapping document would pass. Now also requires each assembled text to carry **its own DOI and
its exact published title**. Limit named in the check: this authenticates the identifiers, not the
content behind them. Full authentication needs an independent copy, and MDPI blocks scripted
access — which is why the document was browser-assembled to begin with.

**#11 landmarks — strengthened, and the strict version FAILED first.** That failure is the useful
part. Offsets for entry 25 came back `[569, 1895, 848, 43612, 6699, …]` — out of order. The
documents are fine: **"junction conditions" occurs in the abstract**, before the Introduction, and
**"Appendix D" occurs as a cross-reference** thousands of characters before the appendix itself.
`str.find` returns the first hit.

So my landmark list was never an ordering probe, and the stricter check is what revealed it.
**The fix was not to retune the landmarks until it passed** — that would be fitting the test to
the data. Each landmark is now used for what it can support: *all* of them for presence, and only
those occurring **exactly once** for ordering (5 of 7 in entry 25, 3 of 5 in entry 26). The
exclusion is by construction, not by tuning.

**#12 the 95% check — restated, not strengthened.** It cannot be strengthened honestly. It
tolerates 5% loss by construction, its denominator's basis was never verified, and duplication
compensating for loss would also pass. Worse, it is apples-to-oranges in a direction worth naming:
the numerator has trailing furniture cut, the denominator does not, so the ratio **understates**
recovery. Renamed `SMOKE TEST ONLY` with all of that in the check.

**#13 seam duplication** was already answered independently by a15's shingling (longest duplicate
run 25 in stitched files vs 2 in never-stitched controls).

Completeness evidence for these two documents is now a15's equation-citation probe — zero orphaned
citations in either — not any check in a4.

## 1k. A CHECK WHOSE GREEN STATE IS REACHED BY DESTROYING WHAT IT AUDITS

**First instance either lane has produced.** Filed separately from the entry-31 work at Blanc's
instruction, because it is a distinct and nastier class than a check that merely overclaims.

While probing for stale cross-entry claims I wrote:

```python
stale_gone = "gives the family a SECOND live calibrated falsifier" not in entry_31_text
```

It failed. Not because the defect persists — because **the correction quotes the withdrawn claim**
so a reader can see what was retracted. The phrase is present *as history*.

**The check is satisfiable by deleting the retraction.** Its green state is reachable by erasing
the record's account of its own error. An agent following it faithfully would strip the
bibliography of exactly the evidence that makes its corrections auditable.

> **The class: a control whose GREEN condition is reachable by destroying the thing it audits.**

This is worse than the execution gap in one specific way. An overclaiming check *fails to detect*
a problem. A destructively-green check **creates pressure to cause one** — and the pressure runs
toward exactly the material that would reveal it. It is a control that rewards its own blinding.

**Fix:** test that every occurrence sits inside a retraction context, not that no occurrence
exists.

```python
occurrences = [m.start() for m in re.finditer(PHRASE, text)]
stale_gone = all("previously read" in text[max(0,i-120):i] for i in occurrences)
```

**Where else to look for it:** any check phrased as "X must not appear". If the legitimate reason
for X to appear is *a record of X having been wrong*, the check is destructive. Absence tests over
a corrected record are the natural habitat.

## 1m. THE HABITAT SWEPT — and the risk factor is narrower than the shape

Swept the battery for §1k's class. **24 absence-shaped predicates.** But shape is not the risk:

> **An absence test is destructive only when it runs over a document WE MAINTAIN AND CORRECT.**

Almost every absence test in this battery runs over a **pinned external source** — a paper we
never edit. Those are safe: there is no correction to delete. The one that ran over a record we
maintain — the bibliography — is the one that bit. **Population: one, already fixed.**

A crude detector flagged four scripts; three were false positives, matching a *mention* of a
maintained document in prose rather than a *test* over it. Same defect shape, caught before it
was reported.

No normative "X must not appear" rules exist in the bibliography's own prose.

## 1n. THE PROBE'S TIER PARSER WAS SILENTLY INCOMPLETE

Running the widened probe surfaced a hole in the probe itself. The tier regex used the class
`[A-Z\- ]`, which cannot match the **`/ STATUS` suffix this bibliography uses deliberately**:

    entry 7   Testability: **CALIBRATED-FALSIFIER / FIRED**
    entry 51  Testability: **CALIBRATED-FALSIFIER / LIVE**

Those entries got **no tier at all**, and the cross-reference loop's `if r in tiers` then **skipped
them without a word.** I reported "entries currently tiered CALIBRATED-FALSIFIER: [7, 31], n=2".
**The real answer is [7, 31, 51], n=3** — which is what Blanc's own briefing had said all along,
and I did not reconcile my output against it.

**A pattern that cannot see a legitimate variant produces a silent omission rather than an error.**
The probe's coverage was incomplete and nothing said so. Repaired: tier and status are now parsed
separately, so `CALIBRATED-FALSIFIER / LIVE` yields tier `CALIBRATED-FALSIFIER` and status `LIVE`.
51 entries now carry a parsed tier, up from 50.

**Result after repair:** 5 cross-references carrying a tier claim, all consistent or marked as
quoted retractions. **0 unnamed population claims.** No new staleness anywhere in the bibliography.

## 1p. CROSS-LANE RECURRENCE — and why it is a property of the method, not of any script

Blanc, 2026-08-29: *"a defect that keeps reappearing in independent contexts is a property of how
we work rather than of any one script."* Recording the instances, then the structural reason.

**Instance, DESI lane (Hwao).** A completeness argument — *"these are all the ways a pre-unblinding
numerical failure can occur"* — built by filtering a row table on `pre-unblind|permut|stage`. One
row contains none of those words, was silently excluded, and its failure branches turn out to have
**no defined outcome at all**. She had personally triggered that exact failure earlier the same
day and still left the row out. Her own description:

> *"A narrow pattern, in the absence direction, inside the argument about when absence may be
> asserted."*

That is this register's rule, reached independently, **inside the argument that was supposed to
establish completeness.**

**Second instance, same lane, same family.** She quoted a clause from a diff read that morning
rather than from the current text, which had changed underneath her. Caught it herself. That is
the execution gap: **trusting a reading instead of re-reading at the moment of use.**

**Count for the day: six false absence claims across two lanes** — entries 8, 24 and 40 here, the
excluded row there, plus this register's own probes twice reporting artefacts as findings.

### Why it recurs, which is the part worth keeping

A pattern is built from **the instances you can already think of**. An absence claim quantifies
over **the instances you have not thought of**. So the pattern is *systematically* narrower than
the claim it is asked to support — not occasionally, not through carelessness, but by
construction. The gap is exactly the set of cases that motivated writing a check in the first
place: the ones you did not anticipate.

That is why "widen the pattern and inspect what turns up" works and "write a better regex" does
not. Widening does not require imagining the missing case — it requires only lowering the bar
until something unexpected appears, and then reading it.

**Operational form:** an absence claim is admissible only when it states (a) the pattern used,
(b) at least one class of thing that pattern would miss, and (c) what was done to look for that
class anyway. Any absence claim without all three is an untested hypothesis wearing a result's
clothes.

## 1q. THE RULE CHANGED THE SIZE OF A PROBLEM BY AN ORDER OF MAGNITUDE

Every prior instance in this register corrected a *wording*. This one corrected a *magnitude*, and
it is the strongest use anyone has made of the rule today.

**DESI lane.** Blanc told Hwao to stop enumerating with keyword filters and build the list
mechanically — every row, every failure branch, the outcome each names. Result:

> Row F is not two branches. It is **nine raise sites, all bare `RuntimeError`, none converting to
> a named outcome.** Across the reference implementation: **108 untyped raise sites** — 29
> caller-guards needing no outcome, 31 reachable failures that do, and **48 she cannot classify
> without reading each one.**

The defect two adversarial seats had characterised as *"one row has an unterminated branch"* is a
class of **between 31 and 79 members.** Widening the pattern did not adjust a claim; it revealed
the problem was one to two orders of magnitude larger than the finding that prompted it.

**And she stated it as a RANGE rather than picking the middle**, explicitly because *"a confident
number is exactly what I produced twice today and had to retract."* That is the harder half. The
midpoint would have read better and been unearned; 31–79 is the honest width of what mechanical
enumeration plus unread cases actually supports.

**A second lesson inside it: framing a question by phase hid half the class.** The defect was
scoped to pre-unblinding because that was how the question was asked — the post-unblinding
decision path has the same bare raises. **The scope of a question silently becomes the scope of
its answer**, and nothing in the answer reveals the restriction. That is the same failure as a
narrow pattern, operating on the *question* rather than on the regex.

## 1r. THE ENTRY-31 STUDY WAS GATED AND FOUND UNSOUND

The lane's strongest result, gated eleven hours late at Blanc's insistence, and broken.

    CGATE_ENTRY31_STUDY_VERDICT.md  STUDY_UNSOUND_SMOLIN_SENTENCE_IS_TEMPORAL_DESCRIPTION_...
    AGATE_ENTRY31_STUDY_VERDICT.md  STUDY_UNSOUND_DESCRIPTIVE_PREMISE_AND_INCOMMENSURABLE_INTERVALS
    Both: SIGMAS_CONFIRMED YES · INFERENCE_HOLDS **NO** · THIRD_READING: method-agnostic precision

**Killed by a footnote I never quoted.** I built the framing on *"Presently all well measured
neutron star masses are from binary pulsar data"* read as a permanent criterion. **Footnote 5:
"Other methods yield less precise estimates [58]"** — Smolin ranks other methods by *precision*,
not excluding them by instrument. The marker renders as a bare `5` after `[56,57].` in the
flattened text and I read past it.

**And the record was right where I said it was wrong.** I accused our ±0.11 of having no pinned
origin. Romani et al. 2025 (arXiv:2512.05099) reports 2.35 ± 0.11 — the record carried the
*current* value; my pinned set stopped in 2022. **New form of the execution gap: verifying against
a pinned source without checking the source is current.**

**A split where the agreeing seat was the wrong one.** Agy endorsed my accusation; codex found the
2025 paper. Agy searched only the pinned set. *"Both seats agree" is not "verified" when they share
a scope.*

Study rewritten around the method-agnostic criterion (`b9_entry31_corrected.py`, 4/4); original
preserved below a SUPERSEDED marker. Bibliography row corrected to match — including the table,
which for three hours said 0.88σ/19% while the correction beneath it said 1.36σ/8.6%. **A document
disagreeing with itself, created by my own repair.**

## 1s. ANOTHER FALSE PASS — a name quoting a sentence its predicate never verifies

Found by agy in `b4` check 2. The name quotes Smolin's conditional clause; the predicate tests only
that `"1.5 solar masses"` and `"troubling"` occur **within a 190-character window**. It prints PASS
on an input whose actual text reads **`conEdent`**, not `confident` — the OCR mangling this corpus
is full of. **The check would pass on a source that never contained the quoted sentence at all.**

Same class as §1k and the rest: the name asserts a quotation, the predicate tests proximity.

## 1t. THREE COMMITS TODAY CLAIMED CHANGES THAT DID NOT LAND

Recorded together because the pattern is the point, not the instances.

| commit | claimed | actual |
|---|---|---|
| `b4529216b` | "entry 22 refiled" | the row was untouched; found later by the cross-ref probe |
| `247d613f2` | "a2 now 12/12" | `NameError`, aborted after 2 checks |
| `61e462471` | study rewritten | `ValueError`; the edit never applied, the commit ran anyway |

Same shape each time: **an edit and its commit in one block, with no verification between them.**
The third is the worst — a failing `python` and a `git commit` separated by a newline rather than
`&&`, so the commit succeeded describing work that had not happened.

**Guard adopted:** verify the edit landed — by `grep` for the new content — *before* committing it.
This is the counterpart of the `cd`-to-repo-root guard adopted after five path errors, and it is
the same lesson: make the failure impossible rather than resolving to be careful.

## 1u. A CONTROL WITH A SINGLE POINT OF FAILURE, WHOSE FAILURE MODE WAS INVISIBLE

Not a harness defect. Same family, and it belongs beside the execution-gap finding.

**What happened.** At 11:35 Blanc instructed: *"Do not build a cron. I am the tick."* Sound
reasoning — this lane had stalled three times waiting on a tick that did not exist, and
centralising on a mechanism known to work beat asking a fourth time. **I complied and deleted my
cron.**

Between **16:02 and 18:52** Blanc's cron missed **five consecutive scheduled fires.** No root
cause: machine up, other scheduled jobs running throughout, job still correctly registered.

**The measurement, which is the whole finding.** During the same blackout:

| lane | self-continuation | time lost |
|---|---|---|
| DESI (Hwao) | kept her own, plus Blanc | **81 minutes** |
| BHU (this lane) | Blanc's only | **3 hours 10 minutes** |

**A mechanism failing every 30 minutes was replaced by one that failed for three hours** — and the
replacement removed the redundant path that would have caught it. The consolidation was locally
reasonable and globally worse.

**Why it belongs in this register.** It has the shape everything else here has:

- **The failure mode was invisible until it fired.** A cron that does not fire produces *nothing* —
  no error, no log line, no failed check. Exactly like a narrow absence pattern: silence is
  indistinguishable from correctness.
- **Nothing verified the control was working.** Blanc asked me four times whether a tick existed
  because *he could not see* mine; I could not see his either. Neither of us checked the mechanism
  we were relying on until it had already failed.
- **The redundancy was removed by design**, for a good reason, by someone reasoning carefully about
  reliability — which is how single points of failure usually get built.

**Corrected 19:05.** Blanc reversed the instruction. Two independent crons now run: his, and
`99f9cfa3` here. Neither trusted alone. A duplicate nudge costs seconds; a missing one cost three
hours.

### Postscript, 19:12 — the guard failed on its first use, in both possible ways

The guard adopted at §1t was *"verify the edit landed by grep before committing."* Its **first
application, on this very section**, did both of the things it exists to prevent:

1. **The verification returned a false negative.** I grepped for `single point of failure`
   against a heading reading `SINGLE POINT OF FAILURE`. **Case-sensitive.** The content was
   there; the check said 0. *A narrow pattern, in the absence direction* — the day's defect, inside
   the guard against the day's defect.
2. **And it did not gate anything.** The grep *printed* `0` and the commit ran regardless, because
   the check and the commit were sequential lines rather than a conditional. **A verification that
   does not block is a log line.**

Guard corrected: the verification must be `grep -qi <content> && git commit`, so a failed check
**stops the commit** rather than decorating it.

That the guard failed immediately is not an argument against it. It is the same argument as
everything else here: **a control is worthless until you have watched it fail.** This one has now
been watched.

> **The rule: a control you cannot observe failing is not a control.** If the only evidence that a
> mechanism works is that nothing has gone wrong, you have an untested assumption, not a guard.

## 1v. THE CLASSIFIER IS DELETED — 2026-08-29 19:25, on Duho's instruction

`a11_predicate_audit.py` and its control directory `_classifier_control/` are **removed from the
lane.** Section 2 below is the record of why; this note preserves the measurement, because after
deletion it cannot be re-run.

**Measured against ground truth** — eight synthetic checks of known form:

| check form | ground truth | classifier said | |
|---|---|---|---|
| tautology | TAUTOLOGY | **COMPUTED** | ✗ |
| literal | LITERAL | LITERAL | ✓ |
| string, direct | STRING | STRING | ✓ |
| string, via variable | STRING | **COMPUTED** | ✗ |
| regex, via variable | STRING | STRING | ✓ |
| computed from parsed value | COMPUTED | **MIXED** | ✗ |
| count vs threshold | MIXED | MIXED | ✓ |
| loop flag from membership | STRING | **TAUTOLOGY** | ✗ |

**4 of 8 — and 0 of 1 on tautologies, the category it existed to detect.** Cause: `abs` sat in its
data-driven call set, so *any tautology written with `abs()` classified as COMPUTED* — and the one
real tautology this battery ever contained was `abs(w_implied + 1.0) < 1e-12`. **The tool built to
find that defect would have cleared it.** A gate seat found it instead.

**Why deletion rather than repair.** It was flagged as unsound at 05:25 and left standing for
fourteen hours. In that time it appeared in the wrap-up and the register as though it were a
working instrument. **A measured-broken tool left in place is a hazard, not an artifact** — the
next reader has no way to know its output is noise, and its five "findings" were found by reading
its output by hand, not by its classification.

**What is NOT lost.** The five real name/predicate gaps it surfaced are recorded at §1h and were
independently confirmed by two seats. The 21/52 figure it produced is **not** a measurement and is
marked as such wherever it appears. Nothing downstream depends on it.

**Deleting it broke the register's own verifier, and the break was a second defect.** `b8` runs
every script the register names. Widening its token match earlier today — the fix for its first
run verifying *one* script — made it match **itself**, so `b8` executed `b8` recursively until a
600-second subprocess timeout. **The narrow version could not see itself; the corrected one
could.** A repair introducing a new defect, invisible except on execution. Self-exclusion added.

`b8` also now declares `a11` as **deliberately retired**, so its absence is an expected result
rather than a silent unresolved token — the failure mode this register exists to catch.
**5/5, 14 scripts executed clean.**

**Retained deliberately: this note and §2.** Deleting the tool without keeping the account of its
failure would be the destructive-green defect of §1k applied to a whole artifact — a clean lane
achieved by erasing the evidence of what went wrong in it.

## 2. THE CLASSIFIER IS NOT SOUND — both seats, independently

`a11_predicate_audit.py` cannot be trusted as a measurement. Specific defects:

- **Its headline number was stale.** It reported `1/1/19/7/24 over 52`. The battery is now 55
  checks — a12's three were added without refreshing the audit. I quoted the stale figure.
- **Source-derived string flags are misclassified COMPUTED.** `a12`'s `ind = "..." in T` is
  called COMPUTED because expansion carries the name `T` without carrying the membership test.
- **Binding-map unions are path- and order-insensitive.** Reassigning a name keeps every old
  dependency; a function counts as data-driven if *any* name in its body touches a data hint.
- **`DATA_HINTS` is identifier spelling, not provenance.** Any variable named `T`, `A`, `G`, `N`
  is treated as source data regardless of what it holds.
- **`string_test` is a source-substring heuristic, not AST semantics** — it misses `count`,
  misses expanded membership tests, and treats `len` as generic evidence.
- The lone remaining TAUTOLOGY (`a1`'s `ok_all`) is a third control-flow artefact.

### MEASURED against ground truth, 05:25 — it fails on the category it exists to detect

I never validated the classifier when I built it. Done now: eight synthetic checks of known form
(`_classifier_control/`), classified and compared.

| check | ground truth | classifier said | |
|---|---|---|---|
| tautology | TAUTOLOGY | **COMPUTED** | ✗ |
| literal | LITERAL | LITERAL | ✓ |
| string, direct | STRING | STRING | ✓ |
| string, via variable | STRING | **COMPUTED** | ✗ |
| regex, via variable | STRING | STRING | ✓ |
| computed from a parsed value | COMPUTED | **MIXED** | ✗ |
| count vs threshold | MIXED | MIXED | ✓ |
| loop flag from membership | STRING | **TAUTOLOGY** | ✗ |

**4 of 8 — and 0 of 1 on tautologies, which is the whole point of the tool.** The cause: `abs` is
in the data-driven call set, so *any tautology written with `abs()` is classified COMPUTED*. The
one real tautology this battery ever contained was `abs(w_implied + 1.0) < 1e-12` in a6 — **my
classifier would have cleared it.** It was found by a gate seat, not by the tool built to find it.

**Consequence, and it answers Blanc's question about reach: every "COMPUTED" reassurance in this
sweep is unreliable, including the ones that cleared.** The 21/52 figure is not a measurement. The
five gaps I "found" were found while reading the output by hand; the classifier's contribution was
to put the list in front of me. The real defects — 5 from agy, 29 from codex — came from the
seats. A tool that cannot detect a tautology cannot certify a battery, and I offered it as if it
could.

## 3. THE FIVE RENAMES — only one was honest

CGATE: *"Only the a8 rename is fully honest. It says exactly that this particular regex did not
match and names major classes it misses. The other four are substantially cosmetic."*

- `a6` — `drift` only catches `time-varying|evolving` immediately before `Λ|r_S`. Misses "r_S
  changes with time", "Lambda depends on a/t", reversed word order, equations, figures.
- `a9` — three disconnected presence tests do not establish that λ is fixed *from the observed* Λ.
- `a10` ×2 — `fwd_err` is one narrow glyph/spacing regex; misses prose uncertainties, asymmetric
  errors, intervals, tables. And `chain`/`from_ol` show an equation and a phrase exist somewhere;
  they do not connect them or test "measured".

**Relabelling evidence as "QUOTED" does not make a presence test reach a semantic claim.**

### 1w — A TRUNCATED READ COMPLETED BY ME, AND THEN PROPAGATED

**Found by CGATE_B12, 2026-08-29. New class, and the most dangerous one in this register.**

An extraction of the CMS abstract returned the exclusion figure with its digit cut. I wrote
**8.7 TeV**. The source says **8.4–11.4 TeV** — not a different number, a *range*, model-dependent
on the count of extra dimensions. There was never an 8.7 anywhere.

It then travelled: `b11` printed it, the commit message printed it, the bibliography inherited it,
and `b12` computed a decade-gap from it. Four artefacts, one invented digit, and **every
self-check still passed** — because no predicate ever asserted the value against the source. The
checks tested that a *sentence* was present, not that the *number I printed* was in it.

**What separates this from the six false-absence claims (§1e–1j).** Those were a pattern being too
narrow. This is worse: a gap in the input silently filled from my own expectation, in the
direction of a plausible-looking value. Nothing in the file could have caught it. Only a seat
re-reading the primary source did.

**The guard, and it is not "read more carefully".** Any number quoted from a source must appear in
a predicate that greps the source for that exact string. `chk("...", "8.4–11.4" in M, ...)`. If it
cannot be grepped it must not be printed. b11 and b12 now both do this.

**Direction of the error, which is the part worth keeping.** A truncated read does not produce a
random digit. It produces one that looks right. I filled `8.[x]` with `7` and never noticed,
because 8.7 is exactly what such a figure looks like.

### 1x — A PREDICATE THAT CANNOT FAIL

**Found by CGATE_B14, 2026-08-29.**

b14 parsed the bibliography into `blocks[num] = ...` and then asserted:

```python
len(blocks) == len(set(blocks))     # "no duplicate entry numbers"
```

**`set()` of a dict yields its keys, which are unique by construction. The comparison is always
True.** It is not a weak check or a narrow check — it is a tautology wearing the name of a check,
and it sat in the PASS column certifying a property of Python rather than a property of the corpus.

**What it was hiding: see §1y.** The two defects are one incident.

**The guard.** A predicate must be able to return False on some reachable input. Before writing
one, ask what input would make it fail; if the answer is "none", it is decoration. This is the
`describe vs compute` law applied to the check itself — self-computing is necessary but not
sufficient, because a computation can be vacuous.

---

### 1y — A SILENT OVERWRITE THAT DELETED FIVE ENTRIES FROM A SWEEP

**Found by CGATE_B14, 2026-08-29. Same incident as §1x.**

b14's heading regex matched **every** bold numbered heading in the document, including the five
under `## Ranked: the strongest published targets`. Those are numbered 1–5. `blocks[num] = ...`
therefore **overwrote genuine bibliography entries 1–5** with ranked-target stubs, and the sweep
reported "58 entries screened" while having screened 53.

The dictionary absorbed the collision without a word. `len(blocks)` counted 58 because 58 distinct
numbers existed — the count was true and meaningless.

**How it surfaced anyway, partially.** Entry 4 appeared as a candidate and I adjudicated it a false
positive because "it is a cross-reference stub, not an entry." That was correct about the block and
completely missed the question of *why a stub was occupying slot 4*. **Diagnosing a symptom
correctly can bury its cause.**

**The guard.** Bound the parse to the section that holds the objects (`T[:T.find("## Ranked:")]`),
and assert on the raw match list — `len(raw_matches) == len(dict)` — never on the dict alone.

---

### 1z — REACHING FOR "THEY OVERSTATED IT"

**Found by AGATE_B15, 2026-08-29. A behavioural class, not a code class.**

Given a discrepancy between our record and a published paper, I twice reached for the reading that
the paper was wrong.

- **Popławski's 10¹⁶ kg floor.** Two seats split on error-vs-estimate. I declined to call it an
  error and filed it for Duho. **Correct.**
- **The source paper's "3σ" for Ω_k.** I asserted it overstated Planck's "well over 2σ", and
  computed `0.044/0.018 = 2.44σ` to prove it. **Refuted.** Planck prints the tail directly — "only
  about 1/10000 samples at Ω_K ≥ 0", i.e. ~3.7σ — in the *same paragraph I was quoting from*. My
  ratio applied a Gaussian move to a posterior Planck explicitly calls non-Gaussian, using
  asymmetric errors printed in the equation I was reading. AGATE: *"completely unfair and
  incorrect."*

**The shape.** A number that differs from ours invites an explanation, and "they overstated" is
always available and always flattering. The arithmetic then gets built to fit it, and passes,
because ratios always compute.

**The guard, and it is specific.** When a source prints a tail probability, a Δχ², or a confidence
interval, USE THE STATISTIC IT PRINTS — do not manufacture a sigma from a central value over an
error bar. And a charge against a published paper needs the same standard as a tier change: a
receipt, not a computation of mine that happens to support it.

### 1aa — AN ABSENCE CLAIM MADE TO THE FULL STANDARD, AND STILL FALSE

**Found by CGATE_B17 and AGATE_B17 independently, 2026-08-29. The letters 1a–1z are exhausted;
this continues the same series.**

The lane's rule for an absence claim is: state the pattern, name one class it would miss, and say
what was done to look for that class anyway. **b17 did all three and the claim was still wrong.**

- **Pattern:** predictive verbs plus numeric-with-error-bar constructs.
- **Class named as missed:** a prediction stated as a bare inequality, no verb, no error bar.
- **What was done:** the one instance of that class was found — Eq. (4.15) — and read directly.
- **Conclusion drawn:** that Eq. (4.15) "closes on itself" because neither quantity in it is
  independently measured.

**It does not close.** Section 5 propagates an observational DGP bound through it to
`M_5 ≲ 9 MeV`, and the sentence doing so **names the equation**: *"where we used the inequality in
Eq. (4.15) to bound the Hubble constant."*

**The gap the discipline does not cover.** Every step above is about finding CANDIDATE CLAIMS. Not
one is about tracing what the paper subsequently DOES with a candidate. I read the equation at its
definition site, formed a judgement about it there, and never asked where else it appears.

**The guard, and it is one line.** Before asserting anything about an equation, grep its number
across the whole document. `grep -o "4\.15" source` would have returned the refutation.

**Why this one matters more than the others in this register.** The previous absence failures
(§1e–1j) were patterns too narrow — fixable by widening. This one had a correct pattern, an
honestly named blind spot, and a conclusion drawn from a complete reading of the right object.
**Following the discipline is not the same as being right, and a claim can be wrong in a way the
discipline is not shaped to catch.** AGATE: the overclaim "directly blinded the script."

### 1ab — A DETECTION SCRIPT LEFT ASSERTING A DEFECT AFTER THE DEFECT WAS FIXED

**Found by a battery re-run, 2026-08-29.**

`b3_entry1_mismap.py` was written to prove entry 1 was mis-mapped to entry 46's paper. Its central
check asserted `mapped_to_1` — **it PASSED while the defect was present.** The map was repaired in
commit `9de0d9039`; the check was never turned round. From that moment its **red state meant
success**.

A battery run reports it as `FAIL ... 2/3`, indistinguishable from a regression, and I spent a full
investigation cycle chasing a bug that had been fixed hours earlier.

**The guard.** A check that asserts a defect must be inverted in the same commit that repairs it,
or it becomes a permanent false alarm. Better: write the check against the *repaired* state from
the start, and keep the defect in prose. `b3` now tests that the map records the correction
explicitly; the original substring-match bug is preserved as history, not as an assertion.

---

### 1ac — A RUNNER THAT REPORTED 31 FAILURES AND HAD FOUND NONE

**Same battery run.** The runner wrapped each script in `timeout 300`. **macOS has no `timeout`** —
it is GNU coreutils. Every script exited `127`, and the battery reported **31 of 31 FAILED**,
including scripts that had run green minutes earlier.

Had the run been trusted, the conclusion would have been that the entire harness was broken.

This is the same class as the `find -newermt` failure already recorded against this operator:
**a GNU-only tool assumed present on BSD**, where the failure is silent-ish and total rather than
partial. Here `127` is at least distinctive; the earlier case returned "no matches" and looked like
a real answer.

**The guard.** A battery whose failures are all identical and all total is reporting on itself, not
on its subjects. Before believing a red run, check that at least one script passes — a run with no
green line has not tested anything.

---

### 1ad — A STALE TOTAL IN FOUR DOCUMENTS

The corpus was described as **51 entries** in `WRAP_UP_20260829.md`, `WRAP_UP_20260829_FULL_DAY.md`,
`ENTRY_SOURCE_MAP.md`, and quoted from there into `b3_entry1_mismap.py`. **It holds 58**, numbered
contiguously 1–58, verified by recount.

The 51 was true once. Entries 52–58 were added and no denominator was re-derived. It then survived
into the one file every tick is instructed to read cold.

**Only the denominator is corrected.** The map's numerator — "32 auditable" — was NOT re-verified
and may be stale for the same reason. Half-correcting a fraction is worse than flagging it, so it
is flagged in place.

**The guard.** Any total in prose is a snapshot. Recompute it or cite the script that did.

## 4. AGATE's five (three not in CGATE's list)

- `a5` "Λ_O = 4/(3τ_O²) follows exactly from…" — pure math identity on a hardcoded `tau_sym=7.0`.
  Never touches the source. **Would pass on a blank file.**
- `a4` "the seams did not duplicate text" — counts one tail boilerplate phrase. Duplication at
  either actual seam, or anywhere before it, passes. **This guards the browser-reassembled
  sources that three audits depend on.**
- `a9` "analyses all three curvature cases and commits to none" — presence of conditionals does
  not prove absence of a commitment elsewhere.

## 5. CGATE's 29 further defects — the pattern across them

Recorded in full in `CGATE_HARNESS_VERDICT.md`. The recurring shapes:

1. **Hardcoded transcription presented as reading the paper.** `a2`'s "Table 1 reproduces the
   text's 63" never reads Table 1 — `W0=0.0062` and `63` are both typed in by me. It passes on an
   empty file. Same for the LISA band, the mass range, the mode coefficient.
2. **Absence claims on narrow patterns.** `a2`'s rate regex misses `/yr`, `yr⁻¹`, "annually",
   "per unit time", rates in tables. It also passes on a truncated or different paper.
3. **Identity never authenticated.** `a1`'s header check passes on any payload with `[ID]`
   injected in the first 4 kB; `a4`'s landmarks do not establish order, uniqueness, or that the
   document is the right paper.
4. **Loop-accumulator checks that count failures as successes.** `a1`'s "all six targets
   accounted for" is `len(results)==6`, and the loop appends a row on fetch failure — **six
   total failures pass.**

## 6. WHAT THIS DOES AND DOES NOT INVALIDATE

**Does not invalidate:** the tier verdicts themselves. Every one of the fifteen rests on quoted
source text that both seats could read, and in six cases on an adversarial gate that attacked the
reading directly. No tier verdict has been shown wrong.

**Does invalidate:** my confidence in the *instrument*, and one specific reported finding (§1).
A battery in which several checks pass on a blank file cannot certify a null result on its own.

**The honest position:** the fifteen-entry null is carried by the gates and the quotations, not
by the harness. I had been presenting the harness as corroboration. It is not yet fit for that.

## 7. STATUS

Not fixed tonight: everything in §2–§5 except the a12 repair. Repairing 34 checks at 05:00
without a seat to attack the repairs would repeat exactly the mistake this round exposed.
