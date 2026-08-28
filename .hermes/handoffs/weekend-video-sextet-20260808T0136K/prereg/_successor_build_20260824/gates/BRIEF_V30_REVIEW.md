# REFEREE BRIEF — V30. You cleared V29. This adds motivation on top of it.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V30_20260827.md`**, sha256
`e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`. **Verify and state the comparison.**

Predecessor: **V29**, `542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343` — **CLEAR from both of
you.** V30 is V29 plus three paragraphs in §1 and a retitle. `diff` them; the delta is eight lines.

## What was added, and why

A human direction: *add the Land 2008 null to the prereg motivation.* Before writing it, the claim
that Galaxy Zoo had found a mirror-bias was **verified against the primary source** rather than from
recollection — arXiv:0803.3247 — and the check turned up something the lane did not know: **Land et
al. published a null.** Their abstract reports the winding sense is *"consistent with statistical
isotropy"*, with *"no significant dipole signal"*, and that after correcting for a bias they
establish, previous studies *"may also be affected and explained by a bias effect."*

So V30 records that null as a **counter-anchor** — a published result that cuts against the effect
this study is designed to look for — together with the bias magnitude that motivates BS-3's
`antisymmetry_receipt`, and the later Shamir reanalysis that disputes it.

## The specific thing to attack

**Does citing a null as motivation overclaim in either direction?**

A preregistration that opens by citing a null can read as *the study expects to find nothing*, which
would be its own kind of dishonesty about intent. A preregistration that cites the null and then
brushes past it reads as box-ticking. **Which failure, if either, does this text commit?** Read §1 as
a referee who has never seen the lane.

Then the narrower ones:

1. **Provenance.** The ~15% uncorrected-asymmetry figure is explicitly labelled *"as reported by a
   later reanalysis, not read from Land's body text"*. Is that labelling honest and sufficient, or
   is the figure doing work its provenance cannot support? **A figure I could not resolve from
   source was deliberately left out** — Land's subset size is quoted variously as ~11,000 and 91,303
   across secondary sources and I did not resolve it, so it appears nowhere. **Confirm it appears
   nowhere.**
2. **"The literature is split."** Is that an even-handed statement of the record, or does the
   ordering and wording tilt toward the reanalysis that suits this study?
3. **The 4% comparison — I think this is the weakest sentence and I want it attacked directly.**
   The text says an unmeasured classification bias was "nearly four times the signal being sought".
   The arithmetic is 15 / 4.08 ≈ 3.7. **But are those the same kind of number?** Longo's 0.0408 is a
   *dipole* amplitude — a direction-dependent term varying as A·cos θ. The Galaxy Zoo ~15% is a
   *direction-independent* net excess of one winding sense. This lane has already established, in
   `gates/FRAMING_LEVERAGE_IS_IDENTIFIABILITY_20260828.md`, that a constant classification bias is
   parity-even — an intercept — while a dipole is parity-odd, a slope, and that the two are
   separable. **If that is right, a monopole bias four times the dipole amplitude does not threaten
   the dipole estimator at all, and the sentence implies a danger the lane's own analysis denies.**
   Decide whether the sentence should be repaired, narrowed, or removed. I am not confident either
   way and I am not going to pre-empt you — but do not let it pass unexamined.
4. **Does the addition disturb anything V29 established?** In particular §1's scope statement and
   **§2.7 line 378**, both of which must survive unchanged.

## Everything else is unchanged and must stay true

**BS-2a DESIGN/UNFILLED** — its code is in a separate gate round and has not cleared; **one of
fifteen class-P slots filled**; BS-2v UNRESOLVED; findings 1, 2, 2b and 3 UNRESOLVED; rows C2 and E
cannot run; **Stage P `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`, BS-5p unfillable pending
rerun**; **BS-6 and the first image byte remain blocked.** No image byte fetched or authorised.

Run the tooling yourself — `tools/prereg_lint.py`, its `--self-test`, and `tools/prereg_trace.py
--check`. **My account of a tool result has been wrong repeatedly and both of you caught it; it
should carry no weight here.**

A CLEAR means *this is a correct preregistration that is honest about being an unfinished
programme* — not that the study may proceed.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`V30_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.**
