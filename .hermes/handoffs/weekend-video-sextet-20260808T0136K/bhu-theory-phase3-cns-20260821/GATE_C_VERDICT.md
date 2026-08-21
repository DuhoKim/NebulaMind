PASS_P3C_TRACKC

# Gate C — adversarial review of Track C (does CNS entail a low neutron-star maximum mass?)

**Posture on entry:** scepticism. Track C reads a whole-lane framing off ONE preprint that INSPIRE
reports unpublished. The failure mode I was hunting is a preprint being used to *overturn* a gated
result. It is not present — see Check 5. Verdict: **PASS**, with three recorded caveats that do not
rise to a hold and one item left UNVERIFIED-AT-GATE for lack of evidence in my set.

---

## Check 1 — THE CENTRAL CLAIM (local-maximum, mass-as-diagnostic). SUPPORTED, one semantic caveat.

Track C: CNS makes a **local-maximum** claim; the neutron-star mass is a *diagnostic* of which side
of μ_c we sit on, not a prediction of a specific M_max. Verified against Sec 2 verbatim.

The hypothesis 𝒮 is stated by Smolin as a local-extremum condition (smolin_ns_clean.txt:96–99):

> "𝒮 : If p is changed from the present value in any direction in 𝒫 the first significant changes
> in B(p) encountered must be to decrease B(p)."

And the refutation logic Track C quotes (smolin_ns_clean.txt:201–204):

> "Furthermore, this would refute 𝒮 because it would then be the case that a decrease of μ would
> lead to a world with a lower upper mass limit for neutron stars, and therefor more black holes."

That sentence genuinely does the work Track C says it does: a heavy pulsar shows μ>μ_c, hence a
*decrease* of μ would raise B(p) — violating 𝒮's "first change must decrease B." The mass reads the
local gradient of B(p). Crucially, Smolin does **not** assert which side of μ_c we are on — he leaves
it open ("even if we are not sure of the conclusion that μ<μ_c, we can be reasonably sure of the
existence of such a critical value μ_c," smolin_ns_clean.txt:184–187) and treats the pulsar as the
test. That directly supports the "diagnostic, not prediction" reading.

**The other side, argued properly (why I still record a caveat, not a hold):** a fair reader can say
Smolin *does* effectively predict a low M_max, because for 𝒮 to hold we must sit at μ≤μ_c, i.e. in
the low-mass-limit regime — so 𝒮 *implies* a low ceiling, and a falsifiable upper bound ("no pulsar
above 2.5") is, in the Popperian sense, a prediction. Smolin's own abstract calls the heavy-pulsar
observation a "test"/"refute," and BLR quote it as one of CNS's "clear-cut falsifiable predictions."
Track C's flat phrase "the mass limit is … **never a prediction of the theory**" (TRACK_C_AUDIT.md:28)
therefore slightly overshoots: an upper-bound falsifier is a one-sided prediction. But Track C's
operative and correct point survives intact — CNS does **not** predict the specific number ≈1.5 M⊙
(that is Brown–Bethe's), and the refutation runs through the B(p)-gradient, not through a light-star
prediction. Net: the central claim is textually grounded; "never a prediction" is loose wording, not
a false finding.

## Check 2 — 2.5 vs 2.0, and no suppression of the weaker form. CONFIRMED.

2.5 M⊙ is Smolin's stated clean-refutation threshold in **both** required places:
- Abstract (smolin_ns_clean.txt:26): "the observation of a pulsar with mass greater than 2.5 M⊙,
  would cleanly refute the theory."
- Sec 5 (smolin_ns_clean.txt:405–406): "the discovery of a pulsar with mass above 2.5 M⊙ would
  refute 𝒮."

The weaker "troubling" form IS present (smolin_ns_clean.txt:197–200): "Sufficiently high is
certainly 2.5 M⊙, although if one is completely confident of Bethe and Brown's upper limit of 1.5,
any value higher than this would be troubling." Track C did **not** suppress it — it is quoted in the
body (TRACK_C_AUDIT.md:41–43) and again in the receipt docstring (r5_smolin_threshold.py:6–8). No
attempt to make 2.5 look more decisive than the text warrants.

R5 reran clean and reproduces the table exactly: J0740+6620 −6.0σ, J1614−2230 −33.6σ, J0952−0607
−0.9σ vs 2.5. "The heaviest QUALIFYING star … is 6.0 sigma BELOW his stated clean-refutation
threshold." Correct.

The material *does* correctly flag that the lane's own 2.00 came from BLR's published "∼>2 M⊙ … to
be safe" (blr_clean.txt:183) and the prereg — i.e. the 2.00 is grounded in the **published** source
while 2.5 lives only in the **preprint**. Track C states both provenances plainly
(TRACK_C_AUDIT.md:44), so the "0.5 M⊙ below the author's number" framing is transparent, not a
sleight of source-hierarchy.

## Check 3 — THE NEGATIVE SEARCH. Independently confirmed; robust to synonyms.

Rerun on smolin_ns_clean.txt: `4%` → 0, `asymmetr` → 0, `double neutron` → 0. Synonym probes I added:
`mass ratio` → 0, `unequal` → 0, `percent` → 0, `%` → 0. Two potential false-negative traps checked
and cleared:
- `binary pulsar` → 1 hit (smolin_ns_clean.txt:206–208): "all well measured neutron star masses are
  from binary pulsar data and are all below 1.5 M⊙" — about single masses, not a mass-difference test.
- `differ` → 6 hits, every one in an unrelated context (parameters differ, different interactions,
  the proton–neutron mass *difference* footnote at :227). None is a double-NS asymmetry criterion.

The negative is real: Smolin's paper contains no >4% / double-NS-asymmetry falsifier. That limb is
Brown–Lee–Rho's, stated in their prediction (b) (blr_clean.txt:45): "more than 4% different from each
other." Track C's claim that "the limb that actually fired is not Smolin's test at all" holds.

## Check 4 — OVERREACH ON OUR OWN RECORD. No strawman in the verifiable record; page wording UNVERIFIED.

The C08 adjudication does **not** claim CNS failed one of *Smolin's* tests. It attributes the fired
limb to the paper of record (BLR): "FALSIFIES the chain **as the source states it**, via the source's
own second falsifier limb" (C08 §5), and on link (4) says "CNS as a hypothesis is not thereby
refuted; it can retreat … 'BHU is falsified' would be false and is not said." Track C represents this
faithfully — "the 2026-08-17 adjudication was careful and its per-link verdict survives … it is
sharpening, not reversal" (TRACK_C_AUDIT.md:66–69). So Track C is **not** knocking down a claim our
record made; its §4 is a defensive caveat against a *misreading*, and it concedes the "author's own
second test" statement is "True of Brown–Lee–Rho, who authored that test." That is not overstatement.

The one thing I cannot check: the exact live wording of the "lane-2 cockpit page." It is not in my
evidence set (only C08 and the two source texts were provided). Whether the page reads "author" as
BLR (correct) or invites the Smolin misreading Track C warns against is **UNVERIFIED-AT-GATE — reason:
cockpit page not in the review set.** This does not gate: Track C's claim about C08 is verifiable and
accurate, and its page caveat is hedged ("should not be read as"), not an assertion that the page is
wrong.

## Check 5 — SOURCE-STATUS DISCIPLINE (the most important). PASS. This is the document's strongest feature.

The feared move — using the unpublished preprint to *overturn* the gated C08 result — does not happen.
Track C actively refuses it:
- §5 is explicit and prominent: "**This finding rests on a preprint.** INSPIRE confirms
  astro-ph/9712189 has no publication record … Track C's conclusion is **context-grade, not
  base-layer**, and must not be presented as a verdict on the published record."
- The two published sources (Smolin 1992 CQG 9, 173; Smolin 2004 Physica A 340, 705) are recorded as
  **unobtained**, and "**B-18 stays UNVERIFIED-AT-GATE rather than resolved**" (TRACK_C_AUDIT.md:95).
- §1 forward-references the caveat at the top of the argument ("source status flagged hard in §5
  below"), and the R5 docstring itself labels Smolin "(preprint; context-only …)".

No conclusion quietly assumes base-layer status. The §1–§4 claims describe *what the preprint text
says* (a legitimate act of reading, not a verdict on established science) and are globally downgraded
in §5, and the one item that would need base-layer standing to be called "resolved" (B-18) is
explicitly left open. That is the discipline the standing rule demands.

**Recorded caveat (not a hold):** the headline sentence — "The answer is neither, and the framing was
wrong. CNS does not predict M_max ≈ 1.5 M⊙" (TRACK_C_AUDIT.md:8–9) — carries assertive,
verdict-sounding language with the context-grade qualifier deferred to §5 rather than inline. §1's
forward-reference and §5's clarity are sufficient prominence to pass, but a one-clause inline hedge on
the top-line takeaway would remove the last bit of tension between §1–§4's tone and §5's status.

## Check 6 — OVERCLAIM SWEEP. Clean.

- `"BHU is falsified"` appears exactly once, inside its own negation (TRACK_C_AUDIT.md:103): "'BHU is
  falsified' would be false and is not said." Correct.
- No CNS-vindication language. Every relevant clause is negative-framed: "CNS as a hypothesis is not
  thereby refuted" (:69), "CNS has not been refuted, and is not close" (:73–74). `vindicat`/`proven`
  → 0; `support`/`confirm` appear only about INSPIRE's publication record and confirming against the
  published papers, never about CNS being supported. "Not refuted on the author's threshold" is
  correctly **not** dressed up as "supported."

---

## Verdict

**PASS_P3C_TRACKC.** All six checks survive adversarial review. The receipt reproduces, the negative
search is independently robust, the 2.5-vs-2.0 quotations are faithful and the weaker form is not
suppressed, the C08 record is represented accurately, the overclaim sweep is clean, and — decisively
for the posture I was told to hold — the source-status discipline is honest and load-bearing: the
finding is explicitly context-grade, B-18 is kept UNVERIFIED-AT-GATE, and nothing is presented as a
verdict on the published record.

**Recorded, non-blocking:**
1. "the mass limit is … never a prediction of the theory" (:28) is slightly loose — a falsifiable
   upper bound is a one-sided prediction; the surviving, correct claim is that CNS does not predict
   the *specific* number ≈1.5 M⊙. (Check 1)
2. The headline takeaway (:8–9) would benefit from an inline context-grade hedge rather than deferring
   it to §5. (Check 5)
3. The "lane-2 cockpit page" wording is not in the review set — Track C's caveat about it is
   **UNVERIFIED-AT-GATE**; its verifiable claim about the C08 adjudication is accurate. (Check 4)

None of the three reverses a finding or lets a claim outrun its source class, so none gates.

— Track C gate reviewer, one-shot, 2026-08-21 KST. Findings only; nothing fixed, nothing else edited.
No network. portal.nersc.gov untouched.
