# LANA_OVERHAUL — scientific narrative & claim-boundary review

Seat: **Lana** (scientific narrative + claim boundary). Written independently against the rejected
artifact; no other seat's packet was read before this. Stamped **2026-08-08 13:10 KST**.

Inspected directly:
- `integrator/canaries/spin-method-canary-20260808T0648/contact-sheet.jpg` (11 states, the rejected grammar)
- `.../storyboard_spin_method_canary.json` (full narration text of record)
- `lanes/spin/SOURCE_FREEZE.json`, `lanes/spin/STATUS.json` (allowed/forbidden scope, audio-contract change)

---

## Verdict

**The claim boundary held. The narrative did not.** Every sentence in v9 stays inside the allowed
scope — the equation is symbolic, no value, no significance, no dipole/parity/cosmology, no
DESI/Ganalyzer, no black-hole-universe (§ scan below confirms this line by line). So Duho's rejection
is **not** a boundary breach and cannot be fixed by trimming a forbidden clause.

What he rejected is real and it is mine to name: **this is a list of eleven true statements, defensively
framed, in which the one genuinely beautiful idea is buried as item 7 of 11 and given the same weight
as a housekeeping QA check.** Nine iterations polished the list. The list itself is the problem. A
conference audience would not follow a through-line here because there isn't one — there is an ordering.

If this review could have been written about any of the nine prior passes, it would have failed its
charge. So concretely, against the three questions I was handed:

## 1. Does the one-sentence question earn the next 100 seconds? — **The question does; the video squanders it.**

The question is genuinely good: *"is an apparent excess of one spiral handedness a property of the
sky, or of the people who labelled the images?"* That is a crisp, falsifiable, two-world question a
scientist wants answered. It earns the runtime.

But v9 smothers it immediately. **The first two of eleven cards are both disclaimers** — card 1 ends
"The result is deliberately not in this video," card 2 is titled "The result is not yet reportable."
Before the audience has been made to want anything, they are told twice what they will not get. Card
10 returns to the same disclaimer a third time. The **frame of the piece is the withholding**, not
the test. You cannot spend your opening telling people what you're keeping from them and expect them
to lean in.

And the question is never **paid off**. It is asked once at 0:04 and never re-posed. The video ends
on "Method first. The verdict ships only after its review gates close" — a process statement, not a
return to the two-world question. A conference talk that opens on a question must close on that same
question, now armed. This one closes on a workflow policy.

## 2. Does the mirroring argument land as the intellectual core? — **No. It is the core, and it is buried.**

This is the heart of my finding. The mirror argument is the whole reason this method deserves a video:

> A real signal in the sky **must** flip its sign when the images are mirrored — clockwise geometry
> becomes anticlockwise geometry, there is no choice about it. A bias in the *labelling* rides with
> the label, not the pixels, so it **need not** flip. The mirror is therefore a discriminant between
> the two worlds: flips ⇒ the sky; survives ⇒ us.

That is an elegant, self-contained, falsifiable idea. It is the "aha." In v9 it appears as **card 7
of 11** ("Mirroring an image reverses its apparent handedness"), stated once, flatly, then abandoned.
It is handed the same ~12 seconds and the same static heading-plus-paragraph treatment as **card 8**
("The columns were verified before they were trusted") — which is a routine 36-of-36 QA agreement
check. The falsifiability insight and a data-integrity spot-check are presented as peers. They are not
peers. One is the point of the experiment; the other is a chore you'd never mention in a talk.

Because the mirror idea does not **build** — nothing before it sets up the two worlds as a problem,
nothing after it uses it — the audience never feels the turn. There is no moment where the design
"answers" the question. That missing turn is exactly why it reads as a list: a list has no pivot.

## 3. Is the withheld result framed as a result of discipline, or an apology? — **An apology, in the language of a ticketing system.**

v9 explains the withholding in bureaucratic status language: *"required post-run review gates are
still open," "the workflow checklist still marks its evidence, receipt, and referee stages pending,"
"a frozen decision blocks any result render."* That is a status report on an internal process. It
reads as "sorry, we're not cleared yet" — an apology.

The true framing is the opposite and far stronger: **we fixed every cut, threshold, and control
before a single number was computed, precisely so the eventual answer cannot be an artifact of our
own choices — and that same discipline is why we will not leak it early.** Pre-registration is not an
obstacle between the audience and the result; it is the reason the result will be *worth* believing.
Framed that way, withholding becomes the proof of rigor, the most confident thing in the video —
"we tied our own hands on purpose." v9 has this material (card 3, "Every rule was frozen before the
first row was fetched") but spends it as one more item in the list instead of as the spine.

---

## Claim-boundary enforcement — sentence-level scan (the boundary I own)

I scanned every narration body against the forbidden list. **No violation.** Detail so the new build
inherits the same discipline:

| Card | Content | Verdict |
|---|---|---|
| 1 title | two-world question; "result deliberately not in this video" | clean — hypothesis under test, not asserted |
| 2 | reportability disclaimer | clean |
| 3 | pre-registration / freeze-before-fetch | clean |
| 4 | `667,944` rows parsed | clean — sample-funnel count (T1_FUNNEL, allowed scope) |
| 5 figure | 190,225 / 161,172 decisive / 29,053 ties / 51,157 / 30,412 | clean — **sample-funnel counts only, no asymmetry computed**; body correctly says "No asymmetry is computed anywhere in this cut" |
| 6 | `A = (N_CW − N_ACW)/(N_CW + N_ACW)`, "every value is withheld" | clean — **symbolic, no value**; exactly the allowed equation |
| 7 figure | mirror control logic, "must flip … need not" | clean — predeclared control logic, no measured sign |
| 8 | 36/36 column-integrity agreement | clean — T1C alignment check, allowed normal-leg scope |
| 9 | bias controls "designed before the numbers were seen; outcomes not shown" | clean — design only |
| 10 limit | open gates, why verdict absent | clean |
| 11 close | "method first" | clean |

**Two watch-points to carry into the new narrated build** (not violations — risks that appear once
the words are *spoken*):

1. **Sign convention read aloud.** Card 6 says "Positive means more CW labels, negative more ACW."
   On the page this is a neutral definition. Spoken in isolation it can be *heard* as "the answer is
   positive." The new build must keep the convention **symmetric and explicitly undetermined** —
   e.g. "a positive A would mean an excess of clockwise, a negative A the reverse, and we are not
   telling you which" — so the audience hears the withholding, not a leaked direction. **Flag any
   narration line that states the convention without also stating that the value is withheld.**

2. **No numeric drift toward a "result."** The funnel counts (card 4/5) and the 36/36 integrity check
   (card 8) are all method/QA numbers and are in-scope. But they are the *closest* legitimate numbers
   to the forbidden line. If the new build expands, animates, or emphasizes them into anything that
   *feels* like an outcome — a rate, a ratio, a "we found N% …" — it crosses. The only number that
   may carry rhetorical weight is the **sample size**; the asymmetry A stays a symbol with no value,
   its sign and significance absent everywhere including inside any figure, axis, or legend.

I flag no sentence that implies a result direction in v9. The direction-implying risk is entirely a
property of the *new* build's narration and animation, and I've localized it to the two points above.

---

## What the new build's argument must do (spine, not pixels)

Yui owns the representation; I own the through-line those seven §4 elements must serve. The elements
must be arranged as **one detective argument**, not delivered as seven exhibits:

1. **Question / stakes (open on the hook, not the disclaimer).** Spirals come in two handednesses. If
   one is genuinely more common across the sky, that's a fact about the universe. But humans sorted
   these images — so an apparent excess could be a fact about the *sorters*. How do you tell the two
   apart? *No disclaimer yet.* Earn the want first.
2. **Why it's hard.** You cannot settle it by counting — every count is contaminated by the labelling
   process. You need a test that behaves *differently* in the two worlds.
3. **The key idea = the peak (most time, real animation, the emotional center).** Mirror the images. A
   sky signal *must* flip; a labelling habit *need not*. The mirror is the discriminant. This is the
   turn the whole video builds to and pays off from — the mirroring animation (§4.4) is the
   climax shot, not the seventh slide. Mark `CONCEPTUAL — illustration, not data` if generated.
4. **Operationalize the idea.** Now — and only now — the machinery earns its place: the symbolic
   asymmetry A (§4.3, value withheld), computed on a frozen, pre-declared sample (the animated funnel,
   §4.2), with pre-declared bias controls (§4.5) each shown as *"this control catches this specific
   way the labellers could fake a signal."* The controls are motivated by the mirror idea, not listed.
5. **Discipline = why we can trust it and why we withhold it.** Everything above was fixed before any
   number existed (§4.6). State the withholding **once**, as strength: we tied our own hands so the
   answer can't be our artifact; that same rule keeps us from leaking it early.
6. **Boundary + payoff (§4.7).** What is known (the design), what is not reportable (A's value, its
   sign, its significance), the exact next gate (independent post-run verdict review). Then **restate
   the opening question, now armed**: when the gate opens, the mirror test tells us which world we
   live in. Close on the question, not on process.

The single-sentence test for the new candidate: **could a conference attendee, one minute after
watching, tell a colleague *"they built a test where a real sky signal has to flip under mirroring and
a human bias doesn't — and they froze the whole thing before looking, so the answer will actually mean
something"?*** If yes, it has a through-line. If the best they can manage is *"it was about galaxy
spins and they're not ready to say yet,"* it is still the list.

---

## Disposition

- **Rejected artifact:** narrative FAIL (list, not argument; core buried; withholding framed as
  apology). Claim boundary PASS.
- **New candidate:** must be judged on the spine above, not on card polish. I will re-review the new
  candidate's narration against §1–3 and re-run the sentence scan before I concur with any accept.
- No disagreement softened; independent packet preserved as ordered.

---

## AMENDMENT — 2026-08-08 13:12 KST — primary artifact corrected to `spin-method-canary-20260808T0204`

**Provenance correction.** The sections above were written from `spin-method-canary-20260808T0648`.
Per `TORI_USER_WATCHED_ARTIFACT_CORRECTION.md`, the exact file Duho watched and rejected in this
conversation is **`spin-method-canary-20260808T0204`** (SHA-256 `2b1db497…`, 114.0 s, video-only),
which Tori served and hash-verified. 0648 is a later diagnostic iteration, supplemental only. I have
now inspected 0204's contact sheet and storyboard directly. The two share the same 11-card skeleton;
only card 05 differs. **My narrative diagnosis (§Verdict, §1–3) survives unchanged and is if anything
sharper for 0204.** Two corrections and one new boundary flag follow.

### The narrative diagnosis holds — and 0204 is a slightly worse offender

- **Card 05 differs (the one card the correction flagged).** 0204: *"The sample funnel was
  predeclared — each rung only narrows it,"* a monotonic funnel bar chart (`funnel_method.png`). 0648:
  *"Three predeclared readouts of one frozen source,"* parallel readouts. Both are sample-funnel
  counts inside allowed scope; the change does not touch the through-line problem.
- **The buried core is *worse* in 0204.** In 0648 the equation card (06) was later edited to add
  *"mirroring the images should swap the sign of a signal that lives in the sky"* — a sentence that at
  least foreshadows the mirror idea before card 07. **That sentence is absent from 0204.** In the
  watched artifact the equation card says only *"Positive means more CW labels, negative more ACW. Its
  measured value is withheld…"* — so the mirror insight arrives cold at card 07 with nothing setting
  it up. My "core buried as item 7 of 11, no build" finding is therefore *stronger* for the file Duho
  actually saw, not weaker. The list reading stands.
- Front-loaded disclaimers (cards 01/02) and the gate-status "apology" framing of the withholding
  (cards 10) are identical in 0204. §1 and §3 stand verbatim.

### NEW claim-boundary flag — present in 0204, absent in 0648

- **The watched artifact's title card reads "Galaxy spin _parity_ — the method, before the verdict."**
  The 0648 iteration I first reviewed had already changed this to "Galaxy spin _handedness_." The word
  **"parity" is named explicitly on the forbidden-scope list** (order §5, my charge, and
  `SOURCE_FREEZE.forbidden_scope` "cosmological parity violation"). As a bare topic label "spin parity"
  is not itself a cosmological-parity *claim*, so I do not read it as a hard breach of the frozen
  gate — but it sits directly on the boundary, it is the single closest word to the forbidden list in
  the entire watched cut, and **a later iteration of this very lane already replaced it with the safe
  term.** Enforcement call: **the new build must use "handedness" (or "spiral handedness"), never
  "parity," in any audience-facing title, heading, narration, or figure label.** Treat any reappearance
  of "parity" in candidate-facing text as a boundary regression.
- All other 0204 sentences re-scan **clean** against the forbidden list (symbolic equation with no
  value; funnel and 36/36 counts in allowed scope; no significance, dipole, cosmology, GRB/SN Ia/DE/
  quasar/H0, black-hole-universe, or DESI/Ganalyzer). The §-scan table above applies to 0204 with two
  edits: card 06 does **not** contain the "swap the sign" sentence (so watch-point 1 rests entirely on
  the isolated "Positive means more CW" line, which is the more exposed wording of the two), and the
  title carries "parity" as flagged here.

### Unchanged

The spine specification (§"What the new build's argument must do") and the one-sentence acceptance
test are unaffected by the provenance correction and stand as written. No gate reopens; the source
freeze is unchanged.
