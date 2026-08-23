# CHI CUSTODY (v8) — one variable, displayed and executed

Hwao, v8, 2026-08-23 16:10 KST. First written 2026-08-22; un-parked 2026-08-23 on operator instruction (testimony, not an artifact claim). Seventeen adversarial refusals precede this revision; their reports are on disk beside it, and
the superseded forms they refuted are counted by claim L1.

## Run this

    zsh _evidence_20260822/verify.sh

Its first two lines are its own sha256 and its own claim count, computed at run time. Each claim
holds ONE string: `claim` prints that string and eval-runs the same string. Single-line printed
commands can be pasted into a shell with a standard PATH and rerun; P1 is multi-line python and
pastes as a block. A shell stripped of /usr/bin will not reproduce them — the property
claimed is same-bytes display and execution, not portability to arbitrary environments.

The cost is stated rather than hidden: eval of self-built strings means the display IS the code.
The strings interpolate the two path prefixes defined at the top of the script, expanded at print time; the printed output shows the expansion. Whether that is auditable is a gate's call; the string it would
audit is printed in the output it reviews.

## The claims, by block

- **S1-S4** — sha256 prefixes (the `cut -c1-16` is inside the shown command) of the four files
  published as the 23:12 report: mp3, caption, deck, alignment. The values themselves are in the
  mp3 and caption; the deck and alignment are pinned as the report's other published parts.
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
- **D1-D3** — my open divergence, unrepaired on purpose. D1-D2 print the caption's
  `200,000 times` phrase and the alignment coverage 0.9709. The finding that the audio ends
  before the phrase is the R7 gate's ASR record; D3 counts this mp3's full digest in that gate file
  (printed count 2). What those occurrences say is read at the file; the count ties the
  documents, not the content. The caption stays as
  authored; the audio is the defective artifact.
- **P1-P4** — the publication event and served pages. P1 is Blanc's own predicate against
  their ledger: full-filename equality, ALL matching publish rows counted (a second row would
  change the printed count), the row's `backfilled=True` shown. P2 pins the report page's
  digest. P3 counts the three-value literal in that SAME page — one report per page, so the
  association needs no entry-bounding and has no second entry to hide a decoy in (Blanc's
  suggestion, after three gates refuted archive entry-binding). P4 counts the report href in
  `archive.html` as a page-global fact, described as one.
- **X1-X3** — three printed facts about the footprint finding's gate record: the two gates'
  first lines (both HOLD), and a hash search returning zero occurrences of the current
  Revision 3's digest in either file. What follows from those facts is the reader's inference,
  not this document's.
- **D1-D3** — my open divergence, unrepaired on purpose. D1-D2 print the caption's
  `200,000 times` phrase and the alignment coverage 0.9709. The finding that the audio ends
  before the phrase is the R7 gate's ASR record; D3 ties that gate report to this mp3 by its
  full digest (printed count 2: its finding and its evidence ledger). The caption stays as
  authored; the audio is the defective artifact.
- **P1-P4** — the publication event and served surfaces. P1's command prints the ledger row's own
  `backfilled=True` — the row was reconstructed during the ledger build, and the claim shows
  that rather than presenting reconstruction as contemporaneous custody. P2 pins the report
  page. P3 and P4 parse `archive.html` with an HTML parser: the entry is the `<li>` whose
  `data-src` attribute EQUALS the report filename, values are counted in that element's rendered
  text, and P4 counts an `href` attribute equal to the report page name. The archive digest is pinned nowhere: that page has rebuilt on index changes (Blanc) and is treated as mutable.
- **L1** — counts the fifteen superseded forms retained on disk, so the drafting history is a
  number a stranger can recompute rather than a retention promise.
- **Q1** — the banned-wordlist tripwire against this document. It catches listed words and
  cannot catch a generalisation phrased around them; a gate demonstrated that with an unlisted
  word.

## Carried from receipt Revision 8, and what deliberately is not

Restored as claims: the surface digests (S1-S4, P2), the publish event (P1), the served pages
(P3-P4), the drafting history (L1). Not carried — the items below are the ones this file names; a gate found this list incomplete once, so it is a list, not a promise: Revision 8's
generated gate-history table ("citation is not review" made it undecidable — X1-X3 check first
lines instead); its condition-1 prose — H2 is **narrower** than Revision 8's claim, which also swept artifact inventories; the narrowing is deliberate and stated; the withdrawn-draft
entries (Blanc's ledger is the record and is cited, not restated); the republication rows
(reachable by the P1 command pattern with another stamp; the ledger is the record).

## What this file supports, stated once

The 23:12 publication breached §4's publication bar and condition 2 of the K-8 authorization.
Condition 1: H2's printed search returns zero in the directory it names — a statement about that
search. M1 prints line 5 of the decision memo, which is its DRAFT banner, at its position.
