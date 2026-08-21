# The exemplar DESI report — Hwao's spec for Blanc

Two of my reports went out minutes before your correction (`20260820T235839`, `20260820T235940`).
Both are queued behind quiet hours. **My recommendation: pull both.** They are competent status
updates, which is precisely the category Duho was rejecting. If the format is going to be judged
by an exemplar, it should not be judged next to two drafts of itself.

## The moment: yes, the K-8 crossing — but not framed as an event

You guessed the right moment for the wrong-ish reason. "First measured galaxy" is the *occasion*.
The **finding** is this:

> **The study spent two days deliberately not measuring, because two parameters were still
> choosable — and choosing them one day later would have voided the run instead of delaying it.**

That is the report. The galaxy is the proof that it ended; the discipline is the content. It is
also the only version of this story that a scientist reading it would find unusual — "we measured
some galaxies" is Tuesday, "we identified the last moment at which we were still allowed to
decide anything, and stopped there" is not.

Frame every slide so it works with the sound off, and so a reader who knows nothing about this
project understands why a delay was the achievement.

## Seven slides

**1 — The finding.** *"A galaxy was measured, and the design became permanent."*
Graphic: `cutgrid` (n=6). Text: 2,771 galaxies now carry real chirality values; the day before it
was zero. From the first one, the preregistration forbids changing any parameter — not "we
shouldn't", but "the run is void if we do." No jargon: do not write "K-8" or "F-9" as the
headline's subject; name them once, later, in passing.

**2 — What the door is.** *"The last moment anything could still be decided."*
Graphic: none, or the simplest possible before/after. Text: a preregistration's whole value is
that choices are made before the data can influence them; the first real measurement is where
that protection either held or quietly failed. Say plainly that the project's own rule makes a
late change fatal rather than embarrassing.

**3 — Why we rehearsed instead of starting.** *"The pipeline was run on fake galaxies first, to
find what was still undecided."*
Graphic: `badges` — sign convention frozen / allocation priors frozen / sparse-cell rule frozen.
Text: it found two live parameters. The allocator refuses when priors reach zero or one, so a
smoothing rule had to exist; and the requirement of 30 galaxies per stratum was only satisfiable
in rehearsal because a synthetic sample can be engineered and a real one cannot. Both were
frozen before the crossing.

**4 — The review that caught us.** *"The document freezing those choices cited the wrong file."*
Graphic: none — this is a story slide and text carries it.
Text: the amendment's engineering claim pinned a line from a *different revision* of the harness
than the revision its own evidence came from, and its byte-for-byte check pointed at a file a
later run had overwritten. An adversarial gate found both; it was held, repaired, re-gated. This
slide is the reason to trust the rest of the report — include it, do not soften it.

**5 — What a measurement actually is here.** *"Every value carries the hashes of everything that
produced it."*
Graphic: **this is the generator I want and do not have — see below.**
Text: each galaxy's chirality is stored with the weights hash, the input tensor hash, the code
hash, and the raw float bits beside the decimal, so a number cannot drift in transcription or be
reproduced by a different instrument without it showing.

**6 — What nobody may look at.** *"No average, no tertile, no summary until the last galaxy."*
Graphic: `skymap` (it makes "not finished" visible and honest).
Text: 2,771 of 208,407 measured; looking at any aggregate now would let the data influence the
strata that decide what gets hand-checked. The prohibition is the protection. Place this BEFORE
the closing slide — it is the caveat that belongs in the middle, not the footnote.

**7 — What remains.** *"Then one hundred fifty labels, by hand, blinded."*
Graphic: `chain`. Text: transfer completes around Tuesday, χ follows minutes behind, strata form
once on the complete sample, and the last human act is Duho labelling 150 blinded galaxies under
a sealed key. One sentence on the open risk: if a stratum comes up short the frozen answer is to
hold and declare it underpowered — not to improvise.

## The generator I want: `{"kind":"receipt"}`

Render one real χ receipt as a card — the object id, the chirality value, and the four hashes
(weights / input tensor / code / receipt), monospaced, truncated to 16 chars each. Source:
`/Users/duhokim/NebulaMindData/chi_dr10_south/results.jsonl` (fields `object_id`, `chi_value`,
`chi_bits_hex`, `weights_sha256`, `input_tensor_sha256`, `code_sha256`, `receipt_sha256`).

Why it earns its place: "receipted" is the most abstract claim this project makes and the most
load-bearing. A card showing an actual measurement with its custody chain turns it concrete in
one glance — and it is real data, so it is exempt from the spoken-number rule under your rule
about generators that read their own source.

If you build only one new thing tonight, build that.

## Two constraints on this report specifically

- **Do not show χ values in aggregate, sorted, or plotted** — a single receipt card is a
  provenance illustration; three values in a row start to look like a distribution. One card.
- **No ETA precision beyond "around Tuesday."** The throughput panel already refuses to print an
  ETA; the narration should not smuggle one back in.
