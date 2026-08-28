# Clean census run — result, and why it closes the automated route

Tori, 2026-08-29. Run directory contains the five briefs, five JSON outputs, and this note.

## The run was clean

Every defect of the previous attempt was fixed and the fixes worked:

- **No contamination.** The working directory held only the briefs — no `ENTRY_SOURCE_MAP.md`
  (which carries a tier column and had leaked into the last run), no bibliography, no prior
  results. Every batch reported `saw_prior_labels: false`.
- **Machine-readable.** Strict JSON contract. 5/5 files parsed, 24/24 records. The previous run
  cost two rounds of parser artefacts — 10 phantom disagreements from grabbing tier names out of
  discussion prose, and an 89% divergence rate from matching the word "disagree" in a heading.
- **All 24 in one uniform pass**, controls included, rather than two runs stitched together.

## The result

**Controls: 3 of 4.** Entries 6, 31, 51 correct. **Entry 54 wrong** — returned
CALIBRATED-FALSIFIER quoting the abstract bracket, with `diverges: false`, meaning the seat did
not register that the abstract and §VI disagree at all.

Entry 54 has now failed **2 of 3 attempts**. Its one pass was the four-paper protocol test.

**Tier disagreements: 15 of 24**, and directional — 10 are CONSISTENCY-ONLY →
QUALITATIVE-DIRECTIONAL. Two readings compete: our record under-classified, or the seats
over-classify. **Entry 54 discriminates**: it is the case with a known answer, and the seat
over-classified. So the 15 are mostly suspect, not mostly findings.

**Abstract/body divergence: 4 of 24 (17%)** — and this figure is an *undercount*, because entry
54 genuinely diverges and was recorded `false`.

**The observability field did not discriminate.** All six CALIBRATED-FALSIFIER claims returned
`threshold_is_observable: true`, including entry 52, whose threshold is `C > 1.9×10^48` — an
inequality on a model parameter, which is precisely the case the field was added to catch. The
seat asserted observability rather than testing it.

## The negative finding, which is the durable output

**The over-classification bias survives protocol improvement.**

The sequence was: diagnose the mechanism (the error lives between a paper's abstract and its
hedges) → write a protocol that forces an explicit hunt for the hedge → verify it on controls
(4/4) → isolate the working directory → make the output machine-checkable → rerun. **The bias
came back.**

That is a stronger claim than "blind classification fails". It says the failure is not a
prompt-engineering problem. A protocol can make a seat *look* for the qualification, and the seat
will still classify on the headline — and will report `diverges: false` while doing it, so the
instrument does not detect its own failure.

Note also that the protocol's success on the 4-paper test did not replicate at 24 papers. A
control that passes on a small batch is not evidence the method works at scale.

## Consequence

**This method cannot produce the census classification data.** 15 disagreements that cannot be
distinguished from noise is not a dataset. The three entries whose classifications this project
actually trusts — 7, 31, 51 — each cost a full adversarial gate round with two or three seats,
quoted source text, and an explicit attack on the requester's own framing.

So the census is bounded by what can be gated properly, not by what can be classified quickly.
That is a smaller corpus than 24 and needs deciding rather than assuming.

**For the paper**, leg 2 is now: the bias is measurable, reproducible, directional, and resistant
to the obvious fix — with the control design that detects it, and the negative result that
targeting the mechanism did not remove it.
