# CHI CUSTODY (v4) — one variable, displayed and executed

Hwao, v5, 2026-08-23 14:55 KST. First written 2026-08-22; un-parked 2026-08-23 on operator instruction (testimony, not an artifact claim). Fourteen adversarial refusals precede this revision; their reports are on disk beside it, and
the superseded forms they refuted are counted by claim L1.

## Run this

    zsh _evidence_20260822/verify.sh

Its first two lines are its own sha256 and its own claim count, computed at run time. Each claim
holds ONE string: `claim` prints that string and eval-runs the same string. Single-line printed
commands can be pasted into a shell with a standard PATH and rerun; P1 and P3 are multi-line
python and paste as blocks. A shell stripped of /usr/bin will not reproduce them — the property
claimed is same-bytes display and execution, not portability to arbitrary environments.

The cost is stated rather than hidden: eval of self-built strings means the display IS the code.
The strings carry absolute paths and no runtime interpolation beyond the two path prefixes
defined at the top of the script. Whether that is auditable is a gate's call; the string it would
audit is printed in the output it reviews.

## The claims, by block

- **S1-S4** — sha256 prefixes (the `cut -c1-16` is inside the shown command) of the four files
  carrying the 23:12 disclosure: mp3, caption, deck, alignment.
- **S5-S7** — the caption's load-bearing strings: the three values, the sign summary, and
  `2,725 galaxies measured` — the count that killed an earlier "values then in existence" claim.
- **F1-F4** — digests of the K-8 authorization and frozen preregistration, plus the two clauses
  the rulings rest on, located by grep rather than paraphrased.
- **G1-G2** — 208,407 position rows and `var(cos θ) = 0.057985`, recomputed from the positions
  file on each run.
- **H1-H2** — two searches restricted to `handcheck/`: the tertile ranker is defined there, and
  a recursive grep for the real chi tree under that directory returns a zero count. The scope is
  the directory named in the printed command, and no wider.
- **X1-X3** — three printed facts about the footprint finding's gate record: the two gates'
  first lines (both HOLD), and a hash search returning zero occurrences of the current
  Revision 3's digest in either file. What follows from those facts is the reader's inference,
  not this document's.
- **D1-D2** — my open divergence, unrepaired on purpose: the `151843` caption asserts
  `200,000 times`, coverage 0.9709; ASR established the audio ends before the phrase. The
  caption is authored text; the audio is the defective artifact; amending the text would make the
  record agree with the bug.
- **P1-P4** — the publication event and served surfaces. P1's command prints the ledger row's own
  `backfilled=True` — the row was reconstructed during the ledger build, and the claim shows
  that rather than presenting reconstruction as contemporaneous custody. P2 pins the report
  page. P3 counts the three-value string in `archive.html`; P4 ties that page to this report by
  href. The archive digest is pinned nowhere: that page rebuilds on each index change (Blanc).
- **L1** — counts the twelve superseded forms retained on disk, so the drafting history is a
  number a stranger can recompute rather than a retention promise.
- **Q1** — the banned-wordlist tripwire against this document. It catches listed words and
  cannot catch a generalisation phrased around them; a gate demonstrated that with an unlisted
  word.

## Carried from receipt Revision 8, and what deliberately is not

Restored as claims: the surface digests (S1-S4, P2), the publish event (P1), the served pages
(P3-P4), the drafting history (L1). Not carried, so nothing leaves unannounced: Revision 8's
generated gate-history table ("citation is not review" made it undecidable — X1-X3 check first
lines instead); its condition-1 prose — H2 is **narrower** than Revision 8's claim, which also swept artifact inventories; the narrowing is deliberate and stated; the withdrawn-draft
entries (Blanc's ledger is the record and is cited, not restated); the republication rows
(reachable by the P1 command pattern with another stamp; the ledger is the record).

## What this file supports, stated once

The 23:12 publication breached §4's publication bar and condition 2 of the K-8 authorization.
Condition 1: H2's printed search returns zero in the directory it names — a statement about that
search. The decision memo remains a DRAFT, unsigned; the study has not been declined.
