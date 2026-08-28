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

**Consequence: the 21/52 figure I reported is not a measurement.** It should be read as "a rough
triage that found five real gaps", nothing more.

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
