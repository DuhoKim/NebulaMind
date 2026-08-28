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
