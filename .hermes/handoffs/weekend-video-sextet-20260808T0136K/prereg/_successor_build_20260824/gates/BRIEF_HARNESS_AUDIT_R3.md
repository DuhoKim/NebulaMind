# HARNESS AUDIT R3 — LAST ROUND ON THIS OBJECT. The approach changed, not the patch.

Two rounds have both returned NOT CLEAR on the citation check. **This is the third and final round I
will spend on it.** If it fails again I will stop and write it up as possibly-not-reliably-automatable
rather than attempt a fourth repair — repairing findings one at a time is exactly what the last two
rounds diagnosed.

Reports: `_harness_r1/`, `_harness_r2/`. **Write to `HARNESS_AUDIT_<YOURSEAT>_R3.md`.**

## What you already cleared — do not redo it

The `prereg_trace` refactor is sound (both seats: predicates unchanged, all four refusal branches
identical, three controls invoke `check_trace()`, V34's zero supported by 18 in-band rows, 18
digests, 16/16 mappings). **V34's correction citations are real.** Neither is in dispute.

## The generating defect, named — and the reason this is not another patch

Your two rounds found opposite symptoms in one object. The cause is a single move, which a sister
lane stated as a rule:

> **A narrow pattern is safe for presence, dangerous for absence. Finding a thing with a tight regex
> proves it is there; failing to find it proves nothing.**

Every version enumerated findings by regex and then concluded a citation was **absent** —
manufacturing absence when the grammar was unfamiliar, presence when a numbered non-finding matched.
I wrote a pattern narrower than the data four times last night. **The parser was never the problem;
using pattern-matching to establish a negative was.**

`CITATION_CHECK_SPEC.md` was written *before* the code this time and is a subject of this round.

## What changed

**Three outcomes, not two.** `VERIFIED` / `FABRICATED` / `UNVERIFIABLE`, and **only `FABRICATED` may
be reported as a document defect.** A report is *recognised* only if exactly one grammar declares
findings inside its findings section **and** the numbering is contiguous from 1. A mixed or holed
report is `UNVERIFIABLE`, because there "not declared" cannot be distinguished from "not parsed".
`CODEX-V21 F4` — accepted in R1, wrongly rejected by the R2 rebuild — is now `UNVERIFIABLE`.

**The canary detects its own subject's deletion.** All four probes turn the battery red:

    membership test deleted   -> citation fabricated: SILENT
    parser neutered           -> citation fabricated: SILENT
    unverifiable branch cut   -> citation unverifiable: SILENT
    grammar guard removed     -> citation unverifiable: SILENT

That needed one more fix of the same family, which you should check I have not left elsewhere: the
controls asserted a **category** appeared, not **which outcome**. Since `UNVERIFIABLE` and
`FABRICATED` share the `repair-citations` category, a neutered parser passed *both* citation controls
at once.

**R1 residues you found still live are closed:** `void_registry`'s control label said "row loses
coverage" while testing naming; the orphan scan's `refuse()` arm matched only double-quoted calls.

## Attack

1. **Is `UNVERIFIABLE` an honest third outcome or a way to avoid failing?** It is the load-bearing
   design decision. If it lets a real fabricated citation hide behind "unrecognisable grammar", the
   design is worse than the binary it replaced.
2. **Is the contiguity rule right?** Numbering contiguous from 1 is my proxy for "the grammar was
   parsed completely". Construct a report where it is wrong in either direction.
3. **Do any controls still assert a category rather than an outcome?**
4. **Fifth narrower-than-data instance** — four found so far; hunt the next.
5. **Does the spec match the code?** It is pinned; divergence between them is a finding.

Run every self-test: lint, trace, void_registry, bs2a_quality_gate, gain_gradient_estimator,
verdict_breakpoints. **Do not take my counts from me.**

## Standing

Two decisions parked on the principal — `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md`,
`OPEN_QUESTION_T_COMPLETENESS.md`. Do not re-litigate. Nothing here fills a slot or touches BS-6.
Final line exactly `**CLEAR**` or `**NOT CLEAR**`.

## Subjects

- `tools/prereg_lint.py` — `1b1f84b8537ef5bc11650b76061094056cd85d4c36ff7d4a14a940c1a4a0de9f`
- `../CITATION_CHECK_SPEC.md` — `5db2cf1cc3c2c23ba020ab2d13b87d6a4714ef3842b505de9c2fcb5d41570149`
- `tools/void_registry.py` — `4980701ce8695985d106f840ce8ebe6a9a5d06c15d51f40aff9544bc59046185`
- `../ref/verdict_breakpoints.py` — `bd248c93984ffa2ed39cae16173df7b9535163e02c325109bfbb680bfcf39e56`

**Verify all four and state the comparisons.**
