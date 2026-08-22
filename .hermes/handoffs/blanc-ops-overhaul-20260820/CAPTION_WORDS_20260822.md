# Corrupted words: the check the numeric sweeps could not run

2026-08-22. Follows [CAPTION_CORRUPTION_20260821.md](CAPTION_CORRUPTION_20260821.md),
which repaired corrupted *numbers*. Tori's observation closing that thread —
*"a check that compares quantities cannot see a corrupted word"* — is now
measured rather than argued, and acted on.

## The population

152 of 219 captions in the archive are machine transcriptions backfilled by
local `faster_whisper base.en`, each stamped *"the original written text was not
saved"*. That model's error profile is systematic, not incidental: it wrote
`longdo` for **Longo** — the physicist whose dipole is the entire subject of the
spin-parity study — `dipol` for dipole, `amisotropy` for anisotropy, `cayon`
for kaon, and `preferred access` for **preferred axis**, in the clause used as
evidence about a spin-parity claim.

**29 captions carried a confirmed non-word garble.** None changed any count, so
every numeric sweep passed them.

## Repairs, in three instruments

**1. whisper-1 re-transcription (Tori) — the four physics captions.** Her runs
and my independent ones agree 95–99%. Fixed: dipole, anisotropy, kaon,
resampling. **Not fixed: the names.** whisper-1 still wrote `longdo`, `kuhn's`,
and `Torii` for Tori. Both models garble proper nouns; whisper-1 is better at
domain vocabulary, not at people. `nm_retranscribe.py` (HermesOps/scripts) is
the tool for the remaining 148 backfills — dry-run by default, and it
deliberately does not publish or append ledger events, so a re-transcription
cannot quietly become a publication.

**2. Name glossary, three rounds — 34 garbled names, ~50 captions, 57
substitutions in round three alone.** Kun appeared as `Koon` ×22, `Koon's`,
`Kuhn's`, `Coons`; Goru as `Gauru`, `Goro`, `Gorou`, `Gora`, `Gorus`, `GoRoo`,
`Gorra's`, `Guru's`, `Goracek's`; plus `Longdo's`, `Tories`, `land's`, `Mital`,
`Shmir`. Method: non-word forms replaced wherever they appear; real-word forms
**only** in captions whose sentence was read and confirmed to refer to the
person. Round three exists because round two surfaced 22 more `Koon`s than the
approval covered — held for Duho's explicit go-ahead rather than rolled into an
approval that didn't cover it.

One judgement call, recorded not silent: `Goracek's structure` parallels
`Gauru Czech structure`, so the audio almost certainly said *"Goru checks
structure"* — but rewriting a possessive into a verb phrase exceeds a name
pass. It became `Goru's`, keeping the syntax; the ledger event explains the
residual oddness for anyone citing that line.

**3. Left alone, on purpose — then resolved without guessing.** `cardi` and
`shorty` were left visible because their intended words could not be identified
from phonetics. Within the hour of this file being committed, Tori identified
both **from the source documents the readings narrate**: `cardi` → *party*
(`LANA_SPIN_ANISOTROPY_ENTRY_ASSESSMENT_20260811.md` line ~206, near-verbatim),
and `F shorty` → **Afshordi** (`GORU_BHU_INDEPENDENT_LITERATURE_VERDICT` line
11 — af-SHOR-di, the Pourhasan–Afshordi–Mann white-hole big bang, whose
signature prediction is exactly the low-multipole suppression the sentence
discusses). The same sentences yielded `Gia, zoo and pen` → **Jia, Zhu & Pen**,
`anti-satripy` → anisotropy, `free access` → free-axis, `multipulse` →
multipole. Both source lines re-verified before applying; ledger event 66.

**The method point outranks the fixes:** *"the original written text was not
saved"* is only half-true for narration-type readings — the narrated document
survives, and it is authored text. Source-anchored repair beats any glossary:
it surfaced an author trio (*Jia, Zhu & Pen*) that no name list carried.
Candidates are found by matching a backfilled caption's date and distinctive
phrases against `reviews/` and handoff documents.
Hwao's `20260821T151843` caption (asserts "200,000 times" with no audio behind
it) stays unrepaired by his own ruling: the caption is authored text, the audio
is the defective artifact. And `tori-fresh-verdict` was repaired by **Tori**,
not me — her whisper-1 replacement, my ledger event, after I wrongly told her
the item was open on her side when it was open on mine.

## Round four: the source-anchored pass, generalised

Tori's method scaled. A 5-word-shingle matcher found **27 of 145 backfilled
captions narrate documents that still exist** in the sextet handoff tree;
sentence-aligning each caption against its source surfaced word divergences,
classified rather than bulk-applied: narration paraphrase and hyphenation style
skipped — the caption follows the *audio*, not the document's orthography —
genuine garbles applied after corpus-wide context reads. **79 substitutions
across 40 captions** (ledger event 67, backups `.pre-glossary4`).

What it caught that nothing else could:

- **Duho's own name as `do host`** ("2 clear-eyed caveats do host should grant
  this knowing").
- **`UE`/`U.E.` is Yui, ×17** — her estimator work was unsearchable under her
  name. Also `Kimmy` → Kimi.
- **Bare `Coon` ×31, `Gore` ×12, `Tory` ×17** — earlier rounds missed these
  because residual scans checked *known forms*, not phonetic neighbours. A
  check that confirms clean on what it looked for, beside a larger population
  of the same defect, is the night's recurring failure shape one more time.
- **`parody` → parity ×6** — "4-point parity", "parity custody proof",
  "preserves parity". A physics term, invisible to every name list.
- **The real-word class, now confirmed reachable:** `defensively frozen` →
  *defensibly* frozen; `Kimi purchased cache` → *cash*. Both change meaning;
  both passed every previous check; both caught only because the authored
  source says otherwise. This partially discharges the floor caveat below —
  for narration-type readings only.
- Plus `premordum` → premortem, `shamere` → Shamir, `reprejection` →
  reprojection, `post-hock` → post-hoc, `trace's` → tracer's.

Still unidentified, no guess recorded: `Baidam` (rowcount) and `Knight's
decider` (overnight-converged) — no source match. Zero suspicious merges from
the aggressive short patterns (`ue`), verified after applying.

## Custody

Every original in `_caption_backup_20260822/` (`.pre-whisper1`,
`.pre-glossary` through `.pre-glossary4`, `.pre-source-anchored`). Seven ledger
events — two `caption_corrected`, four `caption_glossary_pass`, one for Tori's
replacement — ledger at 67, each carrying full change lists and authority. Pages rebuilt;
zero garbled forms remain in any caption or on any served page. The archive now
says Goru ×57 and Kun ×115 where mangled forms used to sit — a search for a
crew name or for Longo now finds the reports that discuss them.

## The floor, stated plainly

These counts are floors. The method catches only garbles recognisable as
non-words; a real-word substitution (`promise` for premise, `dense` for sense,
`deadline` for headline — all present in the candidate list) is invisible to
it, and to every other method we have short of a human reading each caption
against its audio. The glossary captions are **rule-edited, not re-verified
against audio**: the audio still says the garbled sound; the text now says the
name the speaker meant. Each ledger event says exactly that.

## Detector failures, kept beside the findings

- My scan flagged Tori's 14:22 report for `brownly`/`cayon`/`rose-owned` — a
  **mention**, not a use; she quotes each garble and corrects it in the same
  sentence. My detector has no mention/use distinction; her gate-claim checker
  already does (its 82-item mention-only category).
- My "pages don't carry the fix" alarm was my own grep failing on HTML-escaped
  apostrophes (`Longo&#x27;s`). The pages were right.
