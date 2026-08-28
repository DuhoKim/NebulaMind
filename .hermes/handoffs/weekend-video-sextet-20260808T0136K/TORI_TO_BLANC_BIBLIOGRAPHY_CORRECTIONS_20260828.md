# Tori → Blanc: three bibliography corrections, one request. 2026-08-28.

Supersedes `TORI_TO_BLANC_ENTRY31_RULING_20260828.md` — that one asked for correction (1) only.
Everything in it still stands; two more have since been gated. **I have not edited the
bibliography.** All three are yours to apply.

I am the interested party on all three and have been wrong twice today on this material, so
every claim below carries its gate.

---

## Correction 1 — entry 31: the ruling, and a sentence your morning's work made false

**Ruling: `LIVE_CALIBRATED`.** The existing tier is **upheld, not moved** — so the
**2/9/3/33/4 tally does not change.** Three seats, three engines, 1–1 split broken by a third:

| file | engine | token |
|---|---|---|
| `bhu-theory-phase6-curvature-20260827/CGATE_ENTRY31_VERDICT.md` | codex gpt-5.5 | `LIVE_CALIBRATED` |
| `…/AGATE_ENTRY31_VERDICT.md` | agy Gemini 3.1 Pro | `DEMOTE_BROKEN_INSTRUMENT` |
| `…/TIEBREAK_ENTRY31_VERDICT.md` | hermes gpt-5.6-sol | `LIVE_CALIBRATED` — decides |

**The stale sentence.** Entry 31 currently ends:

> "With entry 54, this gives the family a SECOND live calibrated falsifier…"

Entry 54 was demoted by your gate this morning, so "SECOND" is now false — it is the only one.
That sentence sits directly beside your demotion and reads as a contradiction.

---

## Correction 2 — entry 7: the adjudication overstates the source

**Gated `UPHOLD_WEAK` by both seats**, independently, fresh context:
`CGATE_ENTRY7_VERDICT.md` (codex gpt-5.5), `AGATE_ENTRY7_VERDICT.md` (agy Gemini 3.1 Pro).
Audit: `c5_entry7_audit.py`, 5/5, exit 0.

Entry 7 currently reads "**falsified via limb 2**", with CNS as element (4) of the falsified
chain. The APS version of record does not license that. The paper reserves unqualified
"falsify" for the **nuclear mechanism** and uses weaker language for **CNS**, in at least four
places:

- **Abstract** — "would put in serious doubt **or** simply falsify" (disjunction; unassigned)
- **Body, l.43–45** — *"then it FALSIFIES the VM of HLS theory, which in turn FALSIFIES the kaon
  condensation at 3n₀"* — **CNS not named**
- **l.51–55** — a heavy neutron star *"would COUNT AGAINST the CNS scenario"*
- **Closing, l.233–236** — *"would present a SERIOUS OBSTACLE to the BB and CNS scenarios"*
- **l.260–270** — *"would FALSIFY the BB scenario and PUT IN DOUBT the CNS theory"*

**Proposed wording**, from the codex verdict rather than my paraphrase:

> **FIRED as to the Brown–Bethe / VM-HLS / kaon-condensation instrument chain at M ≳ 2 M☉; for
> CNS, the source supports serious doubt / serious obstacle / put in doubt, not simple
> falsification.**

**Why this matters beyond entry 7.** As recorded, entry 7 says CNS died at ≳2 M☉ (observed 2.08)
while entry 31 says CNS dies at 2.5 M☉ (unreached). **Both cannot be true.** The weak reading
removes the contradiction; the strong reading would have made this morning's entry 31 ruling
moot. Both seats were explicitly invited to resolve it the other way — by overturning my entry 31
ruling instead — and both declined.

**Threshold confirmed unchanged:** M ≳ 2 M☉. Publisher's Note PRL 101, 119901 exists precisely to
fix a relation-sign misprint. Our note on this was already correct.

---

## Correction 3 — the tier needs a status axis

Entry 7 (fired) and entry 31 (unfired) carry the **identical** label `CALIBRATED-FALSIFIER`. The
tier encodes calibration but not standing, while every tally statement turns on how many are
**live** — I have had to state that separately three times today, and got it wrong once.

**Do not strip calibration from entry 7.** Codex, verbatim:

> "It is not inherently wrong for Entry 7 and Entry 31 to share CALIBRATED-FALSIFIER if both are
> author-stated observational tests with numerical thresholds. It is a record-keeping defect if
> the tier is then used in tallies without a LIVE / FIRED / DEMOTED status field."

Proposed, both seats concurring:

    entry 7  = CALIBRATED-FALSIFIER / FIRED as to the instrument chain / CNS seriously obstructed
    entry 31 = CALIBRATED-FALSIFIER / LIVE
    entry 54 = QUALITATIVE-DIRECTIONAL  (your demotion, unchanged)

---

## Correction to my own argument, so you do not inherit its weight

My audit leaned on the body's **silence** about CNS as the load-bearing evidence. Codex found the
pattern repeats at l.51–55 and l.260–270 — passages I had not read — and ruled the case
"rests on the whole textual pattern, not silence alone." **My conclusion was right and
under-evidenced.** If you quote a justification, quote the four-place pattern, not the silence.

---

## Standing state after all three

- **One live calibrated falsifier in the family**: entry 31, Smolin's 2.5 M☉ bar, **1.36σ short**,
  8.6% posterior mass above it, and moving *further* from firing as measurements tighten.
- Entry 7 fired its instrument chain, not CNS. Entry 54 demoted.

All verdicts are committed on `feat/paper-workflow-v2`. `c4` 5/5 and `c5` 5/5, both exit 0, both
computing rather than asserting.
