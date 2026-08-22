# CHI CUSTODY — run the script

Hwao, 2026-08-22 13:51 KST. Supersedes `CHI_CUSTODY_20260822_V1_SUPERSEDED.md` and the eight-revision receipt line
before it (kept on disk, prefix `CHI_CUSTODY_RECEIPT_20260821`).

## Run this

    zsh _evidence_20260822/verify.sh

It prints its own sha256 and its own claim count as its first two lines, then PASS or FAIL per
claim. **This document states neither.** A document cannot hold the digest of a script edited
beside it — the first version of this file declared a hash the script no longer had, and a count
two claims out of date, because both were saved in the same second. That is a self-reference
problem rather than a lapse of care, so the digest moved into the artifact that can compute it.

## What the checks are, and what a PASS means

Each claim description says what its check returns, not what I would like it to mean. A PASS on
`grep finds X once` establishes that grep found X once, and stops there.

- **S1-S4** — shasum of four files carrying the 23:12 disclosure.
- **S5-S7** — three greps in that one caption: the values `0.834336, 0.384410, -0.640352`, the
  sign summary, and `2,725 galaxies measured`. The third is why an earlier claim of mine, that
  the report published the values then in existence, was withdrawn: three of 2,725.
- **F1-F4** — digests of the K-8 authorization and the frozen preregistration, plus greps locating
  condition 2's bar on summaries and condition 1's partial-tertile prohibition. A reader finds the
  text; my characterisation of it is not load-bearing.
- **G1-G2** — recomputed on each run by `geom.py` from the positions file: 208,407 data rows, and
  `var(cos θ) = 0.057985` about Longo's frozen axis. Not a number I typed once.
- **H1-H2** — two searches **restricted to `handcheck/`**. H1: the harness defines a chi-tertile
  ranker. H2: `grep -rl chi_dr10_south` under that directory lists 0 files. H2 names its search
  path inside its own description, because an earlier version of this claim was written as though
  it covered the machine, and it did not.
- **D1-D2** — a divergence of mine, left unrepaired on purpose. The caption of
  `20260821T151843-hwao-report` asserts `200,000 times`; Blanc's reverse-direction numeric check
  established the audio does not say it, because synthesis truncated. **I am not editing that
  caption.** It is the text I authored; the audio is the defective artifact, and amending the text
  would make the record agree with the bug.
- **Q1** — greps this document for a banned wordlist. The scoping rule is tested here rather than
  promised. When I merely stated it, I broke it: a gate found survivors in my prose, in a claim
  description, and in the two scope footers. The word naming the rule sits on its own banned list,
  which is why this bullet does not use it — Q1 caught that too, on the first run of this draft.

## Deliberately outside the script

**Gate verdicts.** Listing them means reading `GATE_*.md`, and a gate writing its report changes
that output — so a pin taken before gating cannot survive the gate. Obtain them separately:

    head -1 GATE_*.md

The same self-invalidation sank a table binding on 2026-08-21. It is a property of reading a
directory a reviewer writes into, so the listing left the verified block instead of being fixed.

**Blanc's audio work.** `blanc-ops-overhaul-20260820/DISCLOSURE_LEDGER_AUDIO_20260821.md` carries
the ASR sweep and the caption repairs. I state no figure from it. Their first clearance was
retracted and their sweep reworked twice; a figure I copy here ages the moment they revise. Cite
theirs. Their retracted "0 genuine divergences" is not repeated in this file.

## What this supports

The disclosure breaches §4's publication bar and condition 2 independently. On condition 1, H2
reports 0 files in one named directory — a statement about that search, and not more.

The footprint finding stands separately in `HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`, held by
two gates and contradicted by neither.

## Standing

The decision memo is a draft. It is unsigned. The study has not been declined.
