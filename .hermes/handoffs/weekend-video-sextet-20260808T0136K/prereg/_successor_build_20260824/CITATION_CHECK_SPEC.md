# What the citation check is FOR, and what would make it right in both directions

Written 2026-08-29 05:20 KST before touching the code, because two adversarial rounds have both
returned NOT CLEAR on this one object. That is a signal I have been repairing findings one at a time
rather than the defect generating them.

## The generating defect, named

Tori's lane hit this independently and stated it as a rule:

> **A narrow pattern is safe for presence, dangerous for absence. Finding a thing with a tight regex
> proves it is there; failing to find it proves nothing.**

Every version of this check has used a pattern in the **absence** direction. It enumerates findings
by regex and then concludes a cited finding is *absent*. When the regex misses a grammar, absence is
manufactured. When the regex over-matches, presence is manufactured. Both of my failures are the
same move in opposite directions:

| version | direction | failure |
|---|---|---|
| original | absence of a *report* | a citation to a nonexistent finding passed if any report existed |
| strengthened | absence of a *heading* | real `### F3` findings read as missing |
| rebuilt | both | numbered non-findings accepted; mixed-grammar reports mis-enumerated |

**Four times tonight I have written a pattern narrower than the data and treated the data as wrong.**
The parser is not the problem. Using pattern-matching to establish a negative is the problem.

## What the check is FOR

The document's most dangerous sentence is one announcing a repair, because a reader stops checking
there. The check exists so that **`V## CORRECTION (SEAT-Vn Fk)` cannot cite a finding nobody made.**
It is a guard against a fabricated or drifted citation, not a general markdown parser.

## What must be true for it to be right

**Soundness (no false accept).** If the cited finding is not declared in that seat's report for that
version, the check must say so. A numbered item that is not a finding must not satisfy the citation.

**Completeness (no false reject).** If the report declares that finding in any grammar it actually
uses — including a report mixing grammars — the check must accept it.

**These cannot both be guaranteed by regex over arbitrary markdown**, and pretending otherwise is
what produced two NOT CLEARs. Which numbered things are findings is a judgement the report's author
made and did not machine-encode.

## Therefore: three outcomes, not two

The check must stop forcing a binary. Absence-by-pattern-miss and absence-in-fact are different
claims and must be reported differently.

1. **VERIFIED** — the report's findings section is recognisable *and internally consistent*, and the
   cited number is among the declared findings.
2. **FABRICATED** — the report's findings section is recognisable and consistent, and the cited
   number is **not** among them. This is the only case that may be reported as a document defect.
3. **UNVERIFIABLE** — the report's grammar is not confidently recognisable, or mixes forms
   inconsistently. **Reported as unverifiable, never as clean and never as fabricated.**

Outcome 3 is the direct application of Tori's rule: when the pattern fails, say the pattern failed.
Do not convert a parse miss into a claim about the document.

## What the canary must do

Both seats noted the existing canary only exercises **report absence**, so it cannot detect either
current defect. A control that cannot detect its own subject's deletion is not a control.

The battery must fail if any of these is deleted or inverted:

- **the membership test** — cite a number absent from a well-parsed report → must be FABRICATED;
- **the parser itself** — if enumeration returns everything or nothing, the membership control breaks;
- **the over-permissive guard** — a numbered non-finding under a findings heading → must NOT verify;
- **the under-narrow guard** — a real finding in each grammar, and in a mixed-grammar report → must
  VERIFY;
- **the unverifiable path** — an unrecognisable report → must be UNVERIFIABLE, not clean.

Each control asserts its own **outcome**, not merely that some message appeared.

## What I am not claiming

This does not make the check a general finding-extractor. It makes its *failure mode* honest: it can
still fail to recognise a grammar, and when it does it will say so instead of manufacturing a verdict
in either direction.
