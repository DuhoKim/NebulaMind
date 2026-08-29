Q4_IMPL_REFUTED_WARRANT_SCOPE_AND_CELLS

# C-gate verdict — Q4 implementation

I read the current bibliography itself, including its definitions, standing table, all four calibrated entries, and the later status notes, plus the closed question-4 section of `OPEN_QUESTIONS_FOR_DUHO.md`. I am reviewing the implementation, not reopening Duho's choice to use a third axis.

## 1. Tier-definition reading — reasonable, but not proved by the quoted fragment alone

The record's actual definition is:

> Testability classes per brief: **CALIBRATED-FALSIFIER** (number + threshold) / **QUALITATIVE-DIRECTIONAL** / **CONSISTENCY-ONLY** / **PROSPECT** (points at other instruments).

“Number + threshold” is a claim-form criterion. It says nothing about whether the derivation is sound or whether observation has crossed the threshold. The bibliography's established practice reinforces that reading: it retains `CALIBRATED-FALSIFIER` for both LIVE and FIRED entries, and entry 51 retained the class while its derivation was under arithmetic review. Treating tier as shape is therefore the most coherent reading of the existing scheme.

The implementation overstates this slightly when it says Reviewer B's view follows deductively from that one compressed parenthesis. The parenthesis was not a complete semantics for every axis. It strongly supports a shape reading, but the decisive evidence is the definition **plus the record's consistent use**, not the phrase alone. The choice to preserve the tier is nevertheless implemented consistently.

## 2. “Four rows, not 58” — true only under a narrower scope than claimed

The standing table has four calibrated rows, so a column limited to **warrant for calibrated falsifiers** costs four cells today. It does not cost 58, and 58 was never the right denominator in any event: seven entries are support-only and four BHU entries are unread.

But the stated justification—“a warrant only exists where there is a calibrated claim”—is false. Other classes can have disputable derivational warrants:

- a QUALITATIVE-DIRECTIONAL claim can fail to follow in the asserted direction;
- a PROSPECT can fail to connect the theory to the proposed instrument or observable;
- a THEORETICAL-OBSTRUCTION can rest on a disputed no-go derivation; and
- even a CONSISTENCY-ONLY conclusion can be unsupported by its equations, though it has no falsifier warrant in the narrow sense.

Thus the original 58-cell objection was too broad, but the reversal is also too broad. The honest statement is: **this implementation adds four calibrated-falsifier warrant cells; it is not a corpus-wide warrant audit.** If `warrant` is presented as a general third axis for claims, its eventual scope is larger and the maintenance-cost issue returns. The bibliography currently defines it globally as “does the theory actually produce it,” then silently instantiates it only for calibrated claims. That scope must be made explicit.

## 3. Four warrant cells

### Entry 7 — acceptable only as a provenance-limited nonfinding

“Not disputed here” is appropriately cautious. “No published challenge to its derivation is pinned” is also supportable as a statement about the present pinned corpus, not about the literature or the reasoning's soundness. The record has pinned audits that narrow **what fired**—the Brown–Bethe/VM-HLS/kaon-condensation instrument chain, not CNS—but that is scope adjudication, not a positive validation of the derivation.

An adequate text-search pattern would need, at minimum, citations or identifiers for Brown–Lee–Rho 2008 (`PhysRevLett.101.091101`, DOI, title, author combination) together with derivation-critical terms such as kaon condensation, VM/HLS, Brown–Bethe, maximum neutron-star mass, equation of state, challenge, correction, or falsification. It would miss an uncited independent EoS calculation that invalidates the same chain under different terminology; it would also miss criticism locked in an image-only scan. I did not and cannot verify the worldwide absence of a published challenge. The cell must not be promoted to “unchallenged reasoning.”

### Entry 31 — broadly correct, but should retain its bounds

`DISPUTED` is fair. Rothman & Ellis provide a pinned upstream challenge to the local-maximum/selection argument, and Harrison provides a conditional challenge to differential reproduction in a globally recollapsing closed universe. These challenge the warrant by which CNS produces the mass falsifier, not the strange-quark/kaon mass mechanics themselves.

The cell is somewhat compressed. Rothman & Ellis analyze Smolin 1992 and different parameters, not the 2004 strange-quark argument; Harrison's conclusion requires global recollapse to one future singularity. B23 also established that the 2004 falsifier operationalizes a possible directional failure but does not answer the general criticism. `DISPUTED` survives, but it means **weakened/conditional, not severed**. Silk remains unread.

### Entry 51 — refuted as written

The cell says `DOES NOT FOLLOW FROM THE PAPER'S OWN INPUTS`. The gated B13 result was deliberately narrower: none of **six tested routes** reaches 10¹⁶ kg, the paper shows no intermediate derivation, and plausible omitted geometries or suppressed coefficients remain. Both B13 and open question 2 expressly refuse to prove that no route exists or to decide error versus rough estimate.

The cell's explanatory clause mentions the six routes but its categorical heading converts a failure to reproduce into a proof of non-entailment. That contradicts the adopted narrow gate result and prejudges still-open question 2. It should read approximately: **“UNREPRODUCED FROM THE STATED INPUTS — none of six tested routes reaches the printed floor; the paper omits the connecting step; non-exhaustive.”**

### Entry 44 — refuted; it collapses warrant into standing

Under the implementation's own definition—“does the theory actually produce the falsifier?”—entry 44 has a strong, explicit warrant. The Sec. 4 model predicts exact scale invariance, `n_s = 1`. Observation then rejects that prediction at about 8σ. The fact that the prediction fired does not kill its derivation from the model; it kills the tested model's empirical standing.

What lacks warrant is the **replacement**: an uncomputed correction of the size needed to match the observed red tilt. But that repair is not the calibrated claim in the row. The correct separation is:

- tier: calibrated (`n_s = 1`);
- standing: fired;
- warrant: explicit/undisputed for the Sec. 4 model-to-`n_s = 1` derivation;
- surviving repair: uncomputed and presently unwarranted.

“The warrant is what died” therefore defeats the purpose of adding an independent axis.

## 4. Headline — refuted

The sentence

> Only one of this collection's four sharpest claims has reasoning nobody has challenged.

outruns the evidence twice.

First, entry 7 supplies only “no pinned published challenge found,” not the universal claim that nobody has challenged its reasoning. Second, entry 44's calibrated prediction is explicitly derived; what happened is that observation falsified it. On the implemented definition, entry 44 is not a warrant casualty. At most the table supports: **one row has no pinned warrant dispute recorded; two have documented derivational problems or disputes; one has a well-derived prediction that fired, followed by an uncomputed repair.** That is still informative without making an unverified literature-wide absence claim.

## 5. Breakage and consistency

The Markdown table is structurally valid: the header and each of the four data rows have five columns. Adding `warrant` changes no class count, entry number, tier, or cross-reference.

Substantive consistency did break in the ways above: entry 44's cell contradicts the new axis's definition, and entry 51's cell exceeds the adopted B13 scope. The bibliography also contains current internal staleness that the Q4 edit did not repair:

- the standing table calls entry 31 `LIVE, 1.36σ short`, while its later entry says whether it is live is undecided because compact-object identity remains unresolved;
- the later entry still says Ellis 1993 is unread and “two of four” critics were read, despite the completed B22 full read;
- the table's compressed entry-31 warrant does not state Harrison's recollapse bound, although the later note does.

These do not alter class counts, but they prevent the claim that no other passage contradicts or qualifies the new summary. The first is directly within the table's standing field; the second is independently stale bibliography state.

## What I could not verify

I could not verify that no published challenge to entry 7 exists outside the pinned corpus. I could not assess unread/paywalled Silk 1997. I also cannot certify a corpus-wide absence of warrant issues in non-calibrated entries: no such audit was performed, and the four-cell table does not test it.

## Required correction

Keep the third-axis decision, but correct its implementation:

1. Rename/scope it explicitly as **calibrated-falsifier warrant**, unless the other claim classes will also be audited.
2. Narrow entry 51 to an unreproduced, non-exhaustive derivation gap.
3. Mark entry 44's `n_s = 1` warrant as explicit/strong and place the unwarranted status on the proposed repair.
4. Replace the “nobody has challenged” headline with a pinned-record statement.
5. Reconcile entry 31's standing and update the stale Ellis reading count.

The option-3 architecture is sound; the current implementation is not.
