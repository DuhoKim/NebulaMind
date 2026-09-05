# R3C2 — the leak floor: Tori's judgement for Duho (asked by Blanc 2026-09-05 18:47 KST; not a ruling)

**Written from six rounds of packet gates (V10–V16), two engines each, with the packet I built. No packet is changed
by this document. The leak-repair loop is stopped on Blanc's instruction; the packet stays at V16 until Duho rules.**

## The shape of the evidence, stated as a fact about readers rather than about the text

Across V11–V16 kimi's packet-only answer was the same every round: *"I can see THAT the lane cares about provenance,
not WHICH provenance result helps it."* codex's answer moved: LEAK=NONE at V13 and V14, then at V15 the same
sentences it had passed twice became "the defensiveness itself leaks", and at V16 "a planned comparison between
reproduction and provenance". The content those verdicts were reading barely changed between V13 and V16; the verdict
changed. **That is the signature of a floor: what is left is at the level of the reader's interpretation, not of the
text.** V15's finding — that stripping a signal created a signal — says the same thing from the other side.
CONSEQUENCE_VISIBLE has been NO on every engine since V12. The leak that remains is content-shaped, not stake-shaped.

## 1. Can a packet instruct a seat to record `rests_on` provenance without revealing that provenance is what the study compares?

**Partly, and the part matters.** Two different things are being conflated in the word "leak":

- **That provenance is of interest cannot be hidden.** A seat asked to classify every input's origin from quotations,
  under a seven-value taxonomy, independently of a second seat, with disagreements carried rather than reconciled, is
  being told by the task itself that provenance is measured with care. No wording removes that; the taxonomy has a
  natural derived-versus-chosen structure and any careful reader sees it. This is the irreducible core.
- **That provenance is compared against reproduction can be hidden.** Nothing in the seat's duties requires knowing
  it. The packet could present origin as one recorded attribute of a ledger record — beside status, units, equation
  number — and say nothing of "two tallies", "rests_on", "what the number rests on", a severity order, or what the
  interpretation reads. `compute` would be a lane-side step after the merge, not a seat command; the seat would run
  `validate` only and report a reproduction verdict plus an origin ledger with no summary field. Such a packet exists;
  it is a redaction of what is already there, not a redesign. It would remove exactly what codex named at V16 and
  kimi's "(a)" at V15. It would not remove "provenance matters", and no packet can.

So: **no packet hides that provenance is of interest; a packet that hides the comparison is describable and cheap.
The floor is "provenance is measured", not "provenance is compared".** Blanc's V13-as-floor reading is right in
substance; the achievable floor is slightly lower than V13 (V13 still carried `rests_on` and the comparison).

## 2. If the seat knows "reproduction and provenance are both measured" but not which answer is wanted and not that any outcome is consequential — is it compromised?

**No, by the mechanism that bias requires and this seat lacks: a target.** Trace the marginal calls a seat makes:

- **Origin of an ambiguous sentence** ("We adopt H₀ = 67.4 from Planck (2018)"): CHOSEN or IMPORTED? The reason-code
  precedence makes it mechanical — a sentence naming an external source is a citation whatever else it says. A seat
  that wanted to tilt this would have to know which of CHOSEN and IMPORTED helps; the packet does not say, and the two
  are adjacent in a severity order the seat cannot see. A tilt without a target is noise, and noise between two
  independent seats shows up as `DISPUTED` rows — visible, carried, never reconciled, and a stop above 10%.
- **Inclusion of a marginal candidate** ("is this numeral the paper's own result?"): a seat could grow or shrink the
  denominator. Growing it adds claims of unknown provenance; shrinking it removes them. Without knowing which direction
  the lane hopes for, neither move serves anything; and the two enumerations must agree at tolerance zero, with the
  full candidate and exclusion ledgers audited against every source.
- **The one pressure kimi found and tested** (V12): a seat nudging marginal claims into the arithmetic group to make
  the census "conclusive". The filing rules are mechanical, precedence-bound, dual-seated and audited; there was no
  filing for that pressure to act on.

**The argument the other way, given its due:** three readers (two seats, one auditor) receive the same framing, so a
shared misreading survives redundancy — kimi's "shared prompt-induced direction". But a direction needs a pole, and
the packet gives none: it does not say that derived-only is good or that chosen is bad, it says only that both are
recorded. What a shared framing can produce without a pole is shared *caution* — more `DISPUTED`, more `UNDECLARED`
where a reader is unsure — and the design reports that as a finding about the corpus rather than hiding it. The
residual that no packet cures is prior exposure from training or an earlier session, which C4 already states; a
knowledgeable reader could guess the lane's pattern from the corpus itself, not from the packet. **On the mechanism,
the seat is not compromised; it is informed about what is measured and uninformed about what is wanted, which is the
state every honest referee is in.**

## 3. Is there a different design that dissolves it — two seats each recording one half?

**Yes, and it is clean; its cost is real but mostly compute.** Split the seats: **A-seats** enumerate candidates,
build the status ledger (PRINTED/STANDARD/ABSENT/BLOCKED), run the arithmetic and file the per-claim reproduction
outcomes, and never see an origin field; **B-seats** receive A's agreed input list and classify origin from the
sources with quotations, and never see a reproduction outcome or an arithmetic attempt. Two A-seats for the dual
enumeration, two B-seats for the dual origin classification; the lane merges by `input_id` and runs `compute`; the
C6 auditor reads both. **What it dissolves:** no seat sees the comparison, and A-seats do not even see that provenance
is measured; B-seats still see that provenance is measured — the irreducible core moves to two seats and stays there.
**What it costs:** four seats instead of two on a corpus of 89 texts and 106,676 non-blank lines (each seat's pass
is the same size; the A/B split does not shrink it), so roughly double the seat-days; a new hand-off surface — B's
input list is downstream of A's, so the `merge` exit-1 machinery moves to the A→B boundary and needs its own rule; a
new C0 and two-seat gate on a V17 that restructures §2, C2, C3, C4 and the packet builder (two packets); and the
"second live copy of a repaired rule" risk that has cost this chain most, multiplied by two packets. Engine cost is
small (a seat run is minutes to hours); the cost is design surface and calendar, after sixteen versions.

## 4. What I would do if it were mine

**Accept the floor, define it, and stop.** Concretely: (i) one final redaction, not a repair round — remove the
comparison from the seat's view (no `rests_on`, no "two tallies", no severity order, no "interpretation reads",
`compute` lane-side), because it is cheap, describable, and removes the last thing either engine has named; (ii)
state in C4, in the master and the packet alike, exactly what the packet reveals — that reproduction is measured and
that provenance is classified with care — and that this is content a seat must have, not consequence; (iii) record
V15's finding as the reason no further stripping is attempted: removing a signal creates a signal, so the record
declares the floor rather than chasing it; (iv) keep the split design (3) in the record as the structural option and
take it only if Duho judges "provenance is measured" to be an unacceptable disclosure — I do not, for the reason in
(2): it has no direction and no consequence, and the design's redundancy turns whatever it induces into visible
disputes rather than silent tilt. The corpus itself will tell any knowledgeable reader more than the packet does, and
that floor is not the packet's to fix.

**I would not rename or reframe anything else in the packet again without a new finding of a new kind.**

R3C2_LEAK_FLOOR_JUDGEMENT_COMPLETE
