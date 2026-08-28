# LANA — step 3: scope of a PROVENANCE FEASIBILITY GATE

Per `HWAO_RESEARCH_PLAN_20260810T1715K.md` step 3 (started only after Part B filed). Filed
**2026-08-10 17:20 KST**. This scopes what the gate *checks*; it is a specification, not an implementation.

## What it is, and the one-line value
A **pre-commitment, fail-closed check**: before a study commits to a question that depends on archival
fields, verify **from primary documentation** that every field the *result* depends on has a documented,
unambiguous meaning — and, where the result's interpretation turns on a convention, that the **convention
itself is documented verbatim, not merely implied by a procedure.** Spin spent a week and died because no
one had written down how a stored column was oriented; this gate would have surfaced that on day one and
killed the question in a day, not a week.

## The four checks, per depended-on field
For each field the intended result *depends on* (not every field in the table — the ones whose values or
signs enter the claim):
1. **Definition exists.** The field has a meaning stated in a primary source (ReadMe / data-release paper /
   database schema), quotable verbatim. *No verbatim definition → FLAG.*
2. **Definition is unambiguous for this use.** The name/UCD does not collide across meanings for the
   intended interpretation (e.g. a column "Z" that could be redshift, a spatial height, or a stellar metal
   fraction). *Ambiguous for the use → FLAG.*
3. **Interpretation-critical convention is documented — verbatim, and as a convention, not a procedure.**
   Where the result depends on a sign, frame, orientation, scale, zero-point, or unit, that convention must
   be stated verbatim. **A documented procedure is not a documented convention** (this is the spin lesson):
   "images were shown mirrored" is a procedure; "a stored clockwise is recorded de-mirrored to sky" is the
   convention, and only the latter passes. *Convention only proceduralised, or absent → FAIL.*
4. **Pinned, not recalled.** Each definition and convention is quoted verbatim from the primary source and
   the source is receipt-pinned (URL/hash). *Paraphrase from memory is inadmissible* (the A2 lesson: a
   directional claim written from recollection inverted a lane). *Not verbatim/pinned → FLAG.*

## Pass / fail semantics (fail-closed)
- **PASS** — every depended-on field clears all four checks: the question is provenance-feasible as posed.
- **FAIL** — any interpretation-critical convention (check 3) is undocumented: the question **cannot be
  posed to yield an interpretable result** and must be either (a) restricted to a claim that does not depend
  on the missing convention, (b) deferred until the documentation is found in a primary source, or (c)
  dropped. Fail-closed is the default and a legitimate outcome — exactly as with spin.
- **FLAG** — a definition/disambiguation/pinning gap that is not yet interpretation-critical: recorded and
  resolved before commitment, not silently carried.

## The artifact it produces — a provenance ledger
One row per depended-on field:
`field · intended use · primary source (pinned) · verbatim definition · interpretation-critical
convention(s) · convention documented? (verbatim quote / FLAG / FAIL)`
A question is committed only when the ledger is complete and carries **no FAIL**. The ledger is the receipt
that the check was actually run against primary sources, not intended to have been.

## When it runs, and cost
At **question-commitment time, before any measurement** — a precondition, not a post-hoc review. Cost is a
day of documentary reading per question (read the primaries, quote each field's meaning + convention,
pin the sources, flag gaps). That is the whole point: a day of documentary verification up front against a
week of measurement that dies on an undocumented field at the end.

## Grounded in this week's failure modes (the four checks each catch one)
- **spin** — undocumented *recording convention* of the mirrored-direction fields; procedure was documented,
  convention was not. → **Check 3** catches it (procedure ≠ convention). Cost of missing it: a week.
- **mzr-census** — metadata *symbol collision* ("Z" meaning redshift vs height vs model metal fraction). →
  **Check 2** catches it.
- **mzr-anchor** — metallicity *calibration scale / zero-point* not comparable across methods (~0.7 dex,
  Kewley & Ellison 2008); a "metallicity" value has no single documented scale. → **Check 3** (scale is an
  interpretation-critical convention) catches it.
- **A2 (2026-08-06)** — a directional literature claim written *from memory* and later inverted by the
  primary source. → **Check 4** (verbatim, pinned) catches it.

## Relationship to A3.9
A3.9 was the expensive, after-the-fact version of this check — it invoked the verbatim-establishment
standard only once a lane was already built and its result already in doubt. This gate moves the same
standard **up front**: the same bar ("a verbatim statement of the convention, not a procedure, not an
inference"), applied at commitment, where it is cheap. A3.9 rescued nothing about spin's week; the gate
would have spent a day instead.

---
Scope note: this is a specification of what the gate checks and when. It opens no science, asserts no
result, and is method/process only.