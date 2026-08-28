# REFEREE BRIEF — V28, whole document.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V28_20260827.md`**, sha256
`82cd8ac3690fb87b9cf123719cf29f8af37af70e93652ee7e8a2da2b3ee8b587`. **Verify and state what you
compared.**

## Your V27 findings were about my tooling, and you were right

Both of you found that §10's enforcement claim rested on a checker that could not fail. GPT56 named
all three mechanisms: the current transition skipped entirely; the presence test satisfied by §6.3's
**prose** mention of "the V24→V25 mapping"; the endpoint test ORing digests document-wide so a
predecessor's result digest masked a missing row. **Two table rows were absent and my checker
reported one. V26 was missing one and I had told you it was clean.**

All three are fixed in `tools/prereg_trace.py`:
- the **current transition is checked against the sidecar** that owns it;
- **presence is scoped to the §10 table**, not the document;
- each row must carry **its own result digest**.

**Run it yourself.** Do not accept that from me — that is precisely the mistake that produced this
round.

## What V28 changes

1. **§10's table replaced with the regenerated one** — 26 transitions through `V26 → V27`, each with
   both endpoint digests, computed sections and line counts, §7 row-count changes, and the
   human-supplied findings column.
2. **§10 now states the contract rather than a result**: in-band coverage is the table, scoped to the
   table, stopping at the subject's predecessor; the current transition is mapped and checked in
   `gates/FINDINGS_MAP.md`; **V1→V15 exempt by a named rule in the checker, not by silence.**
3. **No claim that the checker passes.** Asserting a result is what turned my tooling defect into a
   document defect. **If V28 asserts a passing result anywhere, that is a finding.**

## Held from V27 — confirm, do not re-litigate

Stage P `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK` with BS-5p unfillable; the orphan
`VOID-6.1C2-ATTESTATION-FAIL` removed rather than given a fabricated antecedent; catalogue quality in
the closed pre-lock vocabulary; **§2.7 line 378 byte-for-byte unchanged.**

## What to judge

1. **Digest first**, comparison stated.
2. **Run `prereg_trace.py --check` against V28** and report what it returns. The `V27 → V28` sidecar
   mapping was added after the draft was written — check it cites only findings this delta answers.
3. **Does §10 describe the check, or claim it passed?**
4. **Clause 10 both directions; every threshold for value, phase, failure effect; read the
   neighbours.**
5. **Is the regenerated table honest** — do its digests, section lists and counts match the drafts?

## Standing state

**BS-2a DESIGN/UNFILLED. One of fifteen class-P slots filled.** BS-2v UNRESOLVED; findings 1, 2, 2b
and 3 UNRESOLVED; rows C2 and E cannot run; **Stage P superseded pending rerun on the 49,211 mask**;
**BS-6 and the first image byte remain blocked.** No image byte fetched or authorised.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`V28_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.**
