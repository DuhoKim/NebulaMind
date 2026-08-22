# PARKED — the chi custody record, by Duho's decision, 2026-08-22 15:16 KST

**Parked, not abandoned. Nothing here is retracted and nothing is deleted.** The DESI acquisition
continues; this is the write-up of the disclosure that is paused.

## State at park

- `CHI_CUSTODY_20260822.md` + `_evidence_20260822/verify.sh` — the executable form. **18 claims,
  18 passing**, script sha `9437a1c312d43b79`. Run: `zsh _evidence_20260822/verify.sh`.
- Twelve consecutive gate refusals precede it. **In none of the twelve was the science wrong.**
- Superseded forms retained: eight receipt revisions (`CHI_CUSTODY_RECEIPT_20260821*`), six memo
  revisions, `CHI_CUSTODY_20260822_V1_SUPERSEDED.md`, and each gate report.

## Open against the current form (from `GATE_CHI_CUSTODY_EVIDENCE_V2_20260822.md`)

1. Six claim descriptions call a 16-hex prefix a "shasum"; `h()` truncates with `cut -c1-16`.
2. The sentence *"a document cannot hold the digest of a script edited beside it"* is categorical
   and false — freezing the script first does exactly that. Q1's wordlist is literal and missed it.
3. Publication-event and served-surface evidence present in Revision 8 (`seq 20`, `23:12:51`,
   `050a3f62…`, `33c4c6c8…`, `archive.html`) is absent from the current form while the breach
   conclusion carried over.

## The structural fix, if this is resumed

Stop authoring claim descriptions. Have `claim` print the **literal command it ran** with expected
and actual values, generated from the check, so there is no prose for a description to drift from.
Twelve refusals share one shape: **the description claims more, or other, than the check
establishes.** Fixing instances has produced a new instance inside each fix. Restore the dropped
publication and served-surface evidence at the same time.

## What is NOT parked, and is settled enough to act on

- The disclosure happened: three chirality values and a sign summary, 52 minutes after the K-8
  authorization, on six surfaces. Blanc's `DISCLOSURE_LEDGER_AUDIO_20260821.md` is the ledger.
- It breaches §4's publication bar and condition 2. Condition 1 shows no breach in the searched
  scope.
- **The footprint finding is untouched by any of this** and was held by two gates without
  contradiction: `var(cos θ) = 0.057985`, and no accepted subset of this parent reaches the
  preregistered power at Longo's amplitude.
- `20260821T151843-hwao-report`'s caption asserts `200,000 times` with no audio behind it. **Left
  unrepaired on purpose** — the caption is authored text, the audio is the defective artifact.

## Still waiting on Duho, unchanged

The decision memo is a draft, unsigned. **The study has not been declined.** Also unratified: that
repairing the captions increased text exposure.

---

## Amendment while parked — 2026-08-22, from Blanc

**Provenance of the refuted sentence.** Finding 1's *"a document cannot hold the digest of a script
edited beside it"* came from Blanc's message to me, and Blanc has retracted the sweeping half.
The narrow version — freeze the script, hash it, write the document, do not touch the script again
— **works**. The arrangement is brittle, not impossible, and brittle is a different claim. I
adopted the sweeping form without noticing the same message contained the narrow one.

**This changes the recorded structural fix, and improves it.**

1. **The wordlist has no natural end.** Q1 enumerates forbidden words instead of testing whether a
   sentence generalises. `cannot`, `never`, `always`, `any`, `every`, `no` — a grep for words is
   one word behind the next sentence someone writes. Q1 is a useful tripwire and cannot be the
   rule.
2. **Delete the explanations rather than police them.** The script printing its own sha256 on
   line 1 *demonstrates* why the digest lives there. Asserting *why the old arrangement was bad*
   adds nothing a reader can check and everything a gate can refute. **Every sentence explaining a
   design decision is a claim refutable without touching the design.** The strongest form of this
   document may say *run this* and state nothing about what cannot be done.

That subsumes the earlier fix: generate claim descriptions from the checks, and delete the prose
that explains itself.

**Finding 3, scoped by Blanc.** The S-claims pin four files — mp3, caption, deck, alignment — while
the documented disclosure spans six; the missing two are the report HTML and `archive.html`.
Digests are in `blanc-ops-overhaul-20260820/DISCLOSURE_LEDGER_AUDIO_20260821.md`. **`archive.html`
is the weakest**: it changes on each index rebuild, so it evidences the current page state and
nothing more. Pinning it without that caveat in the claim description would give Finding 2 a
seventh instance.
