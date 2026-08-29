# BHU lane — full-day wrap-up, 2026-08-28 21:00 → 2026-08-29 22:15 KST

**Read cold, this file first.** It supersedes `WRAP_UP_20260829.md`, which covers only the
overnight half and knows nothing after 08:30. Two artifacts stand behind it and both are written
to need no recollection: **`ENTRY31_STUDY.md`** (the result) and **`HARNESS_DEFECT_REGISTER.md`**
(what went wrong and what guards it).

---

## The day in three parts

**Overnight (21:00–11:35): a corpus sweep that changed nothing, and that is the result.**
Fifteen entries examined — twelve hand-picked, three drawn at random as a selection-bias control
seeded from a git sha fixed before the draw. Six went through adversarial gates. **Not one tier
changed.** Two promotion candidates were proposed and both were refused by both seats.

The sweep was specifically hunting the *opposite* error — an entry tiered too weak, concealing a
number and threshold. Six such candidates across three author lines and three frameworks. In every
case the number turned out to be **borrowed from the data it was checked against, placed beyond
observability, or carrying a free parameter.** The hypothesis was **tested and refuted**, not left
unfound.

**Daytime (11:35–19:45): Duho redirected the lane to entry 31**, on the grounds that a sixteenth
consistency-only audit cannot compete with a real prediction being decided by data. The study was
gated, found unsound, and rewritten — see below.

**Evening (19:45–21:35): entry 51, a corpus-wide sweep it triggered, entry 44, and then the case
*against* entry 31.** Duho closed open question 3 by returning it to me: entry 44 is now
`CALIBRATED-FALSIFIER / FIRED`, and filing it revealed that the record's claim that "only ONE
[entry] bears directly on a black-hole-universe theory" was wrong — **the family has already had
one of its own cosmologies falsified.** A source-level sweep (`b18`) then found no *second*
self-admitted firing among the 27 pinned corpus papers, but turned up that entry 31's own source
names four published criticisms the record had never carried. Three acquired as free ADS scans;
two read (`b20`, `b21`), both gated. **Rothman & Ellis does confront Smolin with COBE data** — a
claim I had withdrawn wrongly and then re-established. **Harrison is a rival theory** whose
objection is topological and bounded to recollapsing cosmologies. A cross-entry tension I proposed
between entries 31 and 54 was **refuted by both seats and withdrawn**.

**Where entry 31 stands after all of it — read this before re-deriving anything.** The published
criticisms attack the *reasoning*, not the number. The prediction runs through the **strange quark
mass** (not the collapse mass limit the critics attack), and Smolin's own words make it a
local-maximum argument of exactly the form they object to. **I then argued that this means Smolin
answered them by making their objection testable — BOTH SEATS REFUTED THAT AND IT IS WITHDRAWN**
(`b23`, `PARAM_REFUTED_INFERENCE` / `PARAM_REFUTED_DEFENCE_INFERENCE`): he answers those critics
elsewhere, introduces the falsifier against a *different* objection, and making one parameter
testable cannot answer a complaint quantified over all of them. **Do not re-derive it.** Both seats
also said I was smuggling a verdict on open question 4 into what I called evidence for it — which
is recorded in the question itself, so my recommendation there reads as a preference, not a finding.

**Questions 3 and 4 were both closed by Duho returning them to me.** Entry 44 is
`CALIBRATED-FALSIFIER / FIRED`; the standing table gained a **warrant** column — scoped to the four
calibrated falsifiers only, **not** a corpus-wide audit, and my "it only costs four rows"
justification was itself refuted (a directional claim or a no-go can have a disputed warrant too;
Duho's original cost objection stands). Two of the four have real derivational problems: entry 31
disputed by criticism we now hold, entry 51 unreproduced from its own inputs. Entry 44's reasoning
is **sound** — it made a proper prediction and the measurement disagreed.

**Entry 22 (the one no-go) now states its domain**, which it never did. And I was unfair to it:
I counted eleven "conditions" that were eleven *phrases* for about eight hypotheses, and called a
theorem's stated hypotheses a limitation. Both seats refuted that. **A flagged follow-up — that this
record's matching series escapes the no-go via Israel junction conditions — is FALSE and withdrawn**;
Israel formalism does not imply a shell, and the pinned series says it has no surface term. Entry 31 is *not* the
corpus's only live calibrated falsifier — **entry 51 is the other**, and its measurement side was
found to be an uncited sentence. Fixing that turned up a second defect of the same class, and
sweeping for it turned up two more. Detail in the section below; six sources pinned, four new
harness defect classes, one new decision for Duho, **no tier changed**.

---

## What the entry-31 work concluded — after being gated and found unsound

Smolin (2004) predicts a sufficiently heavy neutron star refutes cosmological natural selection.
**His bar is graded: 2.5 M☉ for certain refutation, 1.5 M☉ for "troubling"** if one credits
Bethe–Brown.

**My first study claimed the falsifier's status turns on which instrument you accept.
Both gate seats returned `STUDY_UNSOUND`, and they were right.** It died on a footnote I never
quoted — footnote 5: *"Other methods yield less precise estimates [58]"* — which ranks other
methods **by precision**, not excluding them by instrument.

**The corrected finding:**

| estimate | value | method | vs the 2.5 M☉ bar |
|---|---|---|---|
| PSR J0740+6620 | 2.08 ± 0.07 | radio timing (Fonseca 2021) | 6.00σ |
| PSR J0952−0607 | **2.35 ± 0.11** | optical (Romani **2025**) | **1.36σ — 8.6% above** |
| GW190814 secondary | 2.50–2.67 (90%) | gravitational waves (Abbott 2020) | conditional |

**What is undecided is the OBJECT, not the instrument.** These are three estimates of one quantity
with different systematics, all evidence. **Duho's keep-both ruling survives; the reasoning I gave
him for it did not.**

**The durable statement, which survives whichever measurement anyone prefers:**
> **Is any object above 2.5 M☉ securely a neutron star? Today none is.**

And an arithmetic result that inverts the original intuition: **tightening cannot fire this
falsifier — only kill it.** At a central value of 2.35, every gain in precision drives the bar
further away. Firing requires the *central value* to move.

**Also true and previously untracked: the 1.5 M☉ bar was passed years ago**, by every measurement
here. Smolin's own 2004 premise — that all well-measured masses lie below 1.5 — is now false.

---

## Scheme changes made today (all on Duho's rulings)

1. **New tier `THEORETICAL-OBSTRUCTION`** for proof-based no-gos; entry 22 refiled into it. Its
   membership criterion passes four controls and **fails at corpus scale (~1-in-4 precision)** —
   recorded, and it must not be used to propose candidates.
2. **Falsifier-threshold rule**: falsifiability is a property of the theory's content, not the
   author's candour; but firing requires a threshold, and **if the author supplied none, we supply
   it and own it.**
3. **Bars are set case by case**, each with an owner and a justification. "No bar chosen" is retired.

---

## The evening: entry 51 and what the sweep found

**Entry 51 (Popławski 2010) is the corpus's second live CALIBRATED-FALSIFIER**, and the wrap-up
above understated that by calling entry 31 the only one. Its status — "CMS reports no evidence for
microscopic black holes as of 2025-12" — carried **no citation of any kind**. Now receipted to two
CMS searches (`2604.10732`, `2511.10662`).

**A proposed better test route, gated and narrowed.** Popławski's floor is a bound on *density*
(the LHC is his illustration, not his scope), so primordial black holes are in scope and the floor
lands inside the open PBH dark-matter window. Both seats narrowed this to a **conditional**
astrophysical route: the derivation covers fermionic matter only, the window is caveated, and no
present detection protocol is pinned. `b12` (8/8), `b13` (5/5), four gate verdicts.

**Six routes to Popławski's floor, none of which reaches it.** `b13` computes the Cartan radius
from the paper's own eq. (33); the shortfall is 3.1–4.1 decades in density and *refining his inputs
makes it worse*. Both seats reproduced every number; neither found a seventh route. **This is
open question 2 and it is Duho's** — whether to call it an error or an unreproduced step.

**The sweep (`b14`, 4/4).** Because *both* live falsifiers rested on uncited experiment claims, all
58 entries were swept for that shape. **No fabricated result was found anywhere.** Three
candidates: entry 39 a false positive (the Planck *unit*, not the satellite), entry 44 real and its
">5σ" claim **true and understated** (Planck: 8σ, 9σ with BAO), entry 54 real — the record carried
one side of a live dispute and now carries Planck's own resolution (adding lensing returns Ω_K to
−0.0106 ± 0.0065, flat within 2σ).

---

## What a cold reader should distrust

**The check batteries are working notes, not verification.** Two seats declared the harness
`UNSOUND` at 04:21; every repair since was mine. `b8_verify_register.py` (5/5, 14 scripts) checks
the register against the filesystem, but cannot check prose — and most of the register is prose.

**Every tier conclusion rests on quoted source text and on gates, never on the harness.**

**Eight defect classes were added this evening and most are about checks that passed.**
§1w a number I invented to fill a truncated read, which spread to four artifacts while every
self-check passed; §1x a predicate that *could not fail* (`len(d)==len(set(d))` on a dict);
§1y the silent overwrite §1x was hiding, which had a sweep reporting 58 entries screened having
screened 53; §1z reaching for "they overstated it" against a published paper and building a naive
Gaussian ratio to support it — **refuted by a seat**, and the charge is withdrawn;
§1aa an absence claim made to this lane's *full* standard that was **still false**, because every
step of that standard is about finding candidate claims and none is about tracing what a paper
later does with one; §1ab a detection script left asserting a defect after the defect was fixed,
so its **red state meant success**; §1ac a battery runner that reported 31 of 31 failed and had
found nothing (`timeout` is GNU; macOS has none); §1ad the stale 51 in four documents.

**Entry 44 audited and gated (`b17`, 6/6).** No concealed calibrated falsifier — Eq. (4.14)'s
four-significant-figure `T_b/M_5 = 0.17139 ± 0.00077` is a *fitted normalisation*, the seventh
borrowed number the sweep has found and the first to four figures. The paper's testable core,
exact scale-invariance, **was tested and lost** at 8σ. One of my claims was refuted outright and
is withdrawn in the file. **Battery re-run after all repairs: 31/31 green.**

**A CORRECTION TO THIS FILE, AND THEN A CORRECTION TO THE CORRECTION.** This said "36 of 51
entries"; I declared the 51 stale, "fixed" it to 58 in three documents, and **was wrong**. There
are 58 numbered entries and **51 BHU papers** — the difference is 7 support-role entries (29, 30,
32, 33, 34, 35, 58), and the bibliography defines the term at its own lines 19 and 24. Both numbers
are correct for different things; all my "corrections" are reverted. Use **51** for papers and
**58** for entries, and say which.

The register's §1h table says, per entry, what each conclusion rested on **before** and **now**.
Nine re-derived, one named limit, none unknown.

---

## Methodological findings worth carrying to other lanes

- **The execution gap** (`FINDING_THE_EXECUTION_GAP.md`) — claims made without executing the thing
  that would falsify them. Eight instances, two lanes, four artifact types.
- **Absence claims**: six were tested today; three false, three true. *Nothing but widening the
  pattern and inspecting the hits separates them.* An absence claim must state its pattern, one
  class it would miss, and what was done to look for that class anyway.
- **Destructive-green controls** (§1k) — a check whose green state is reachable by deleting the
  record it audits. First instance either lane produced.
- **A control you cannot observe failing is not a control** (§1u) — a cron blackout cost this lane
  3h10m; the lane that kept a redundant path lost 81 minutes.

---

## Open

**One decision for Duho** (`OPEN_QUESTIONS_FOR_DUHO.md`): whether the new tier's members are
hand-sorted, screened-then-checked, or the screen improved first. **Recommendation: screen then
hand-check** — the screen is imprecise but there is no evidence it is bad at recall, and nothing
is filed without a read.

**A SECOND decision for Duho**, filed this evening: whether to say in print that Popławski's
10¹⁶ kg does not follow from his own inputs, or only that we could not reproduce it. Both seats
agree on the arithmetic and disagree on that. **Recommendation: get the journal version first** —
we hold only the preprint and it never shows the step.

**Not blocked, not done:** **51 BHU papers** across **58 numbered entries**, of which the large
majority remain unaudited; the sweep is parked by redirect, not by obstacle. **Entry 44 is the standing next
target** — it surfaced this evening as a real sweep candidate and exactly one sentence of it has
ever been read. The highest-value real-world item is not ours to do — an independent mass for a black
widow by a non-optical method would settle far more than another audit.
