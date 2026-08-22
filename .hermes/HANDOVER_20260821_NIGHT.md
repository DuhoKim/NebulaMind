# Handover — night of 2026-08-21 (written 00:12 KST on the 22nd)

## The headline is scientific, and it is not good news for this run

Two independent findings, both established from **positions and frozen text alone** — no chi value
was ever read, and every gate certified that boundary:

1. **BS-1's footprint-variance PASS was measured on the wrong population.** It swept 832,393
   dered Cut-6 objects across the full BRICKID keyspace; the sample being measured is 208,407
   Cut-5 rows from BRICKID 1..121000. `var(cos θ)` is **0.0580** against a required 0.15.
2. **The frozen power gate cannot see the footprint.** HC-6 evaluates `sim_power.py`'s
   uniform-sphere logic at exactly two inputs, `A_eff` and `N`, neither of them geometric. It
   would PASS on a sample with 5.75× less leverage than it assumes. Because `SSE(S) ≤ SSE(P)`,
   **36,253 full-sphere-equivalent galaxies bounds every possible accepted subset**, and at perfect
   labelling the noncentrality bound is 4.4888 where 0.95 power needs 4.7351.

**No accepted subset of this parent reaches the preregistered power at Longo's amplitude.** The
cause is structural: the harvest stopped on *"contiguous BRICKIDs until 200,000 galaxies"*, and
Legacy brick IDs run south-to-north, so a contiguous prefix **is** a polar cap. The figure of merit
is `N · Var(cos θ)`; the rule maximised N and destroyed the other factor.

This survived **ten adversarial gates on two engines** and was never contradicted.

## Where the decision stands

`DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md` is at **Revision 6, DRAFT, unsigned, NOT in force.**
It claims no preregistered outcome — it records that the investigator declines to proceed, which
lies outside the preregistration. Committing it (Blanc, `acad6b05`) did not make it effective.
**The study has not been declined. That is Duho's signature.**

Successor design: `SUCCESSOR_SCOPE_20260821.md`. Same N drawn from the full footprint is worth
**7.7× the leverage**; the full keyspace clears the requirement at 9% acceptance. Recommend DR11
once photo-z lands, fallback to DR10.1-full on **2026-09-05**.

## The custody record: ten refusals, one repeated mistake

Every gate refuted the *record*, never the science. The defects converge on one shape: **I assert
coverage the artifact does not have.** "Complete ledger", "no code path", "cited by no gate",
"exact input set", "three times before review", "committed as witness" — six versions of one error.
The last one covered 13 of 72 actual inputs.

**Approved approach for tomorrow (Duho, 2026-08-22):** stop writing a receipt that describes its own
completeness. Publish the evidence — the generator, its raw output, the gate reports, Blanc's audio
ledger — and let the receipt make only claims a reader can check in one command. **No universal
quantifiers.** Every defect tonight lived inside a word like *every*, *exact*, *no*, or *all*.

## What was actually disclosed, and it is a real breach

One report, six sha-pinned surfaces, published 52 minutes after the K-8 authorization:
`0.834336, 0.384410, -0.640352` — three of 2,725 values then existing, plus a sign summary.
Breaches **§4's outright publication bar** and **condition 2**. Condition 1 (partial tertiles) shows
no breach within the authorized evidence boundary. Blanc's `DISCLOSURE_LEDGER_AUDIO_20260821.md` is
the authoritative ledger.

Found only because a gate **transcribed the audio**: `nm_caption_norm` summed digit-words after
"point" (`8+3+4+3+3+6 = 27`), so every text surface said numbers that never existed. Nine captions
were corrupted; repairing them **increased** text exposure, which is Duho's to ratify.

## Running unattended, all guarded

| | |
|---|---|
| transfer | PAUSED_WINDOW, 15,914 / 60,308 (26.4%), 191 GB, 0 quarantined |
| cutter | 49,927 tensors |
| chi | 49,927 measured, fully drained |

**The window is America/Los_Angeles, not KST** — NERSC's off-peak. Resumes **12:00 KST today**,
then runs **~60 hours unbroken** to Tuesday 00:00 KST. Completion ~Wednesday evening at 540/hr.

## Open

- Duho's signature on the decline, and ratification of the caption-repair exposure increase.
- Task 26: Dustin's r-band checksum list, offered and accepted, not yet delivered.
- Task 27: the verdict estimator **does not exist** — spec only. No forward claim is made about it.
- Blanc: three caption/audio divergences reported, including a TTS truncation where the audio is
  shorter than the caption. Two of the nine "repaired" captions still carry connector-split numbers.
