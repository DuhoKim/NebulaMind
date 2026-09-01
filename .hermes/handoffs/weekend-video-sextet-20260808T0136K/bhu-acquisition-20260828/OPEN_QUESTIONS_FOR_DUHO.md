# Decisions waiting on Duho — BHU lane

**Format note, adopted 2026-08-29 at Duho's request via Blanc:** plain words, no codenames, each
question states the stake, gives options with what each costs, and says why the call cannot be
mine. The old version of this file read as a status report and buried a decision inside it.

---

## ✅ DONE 2026-09-01 — Gaztañaga cutoff calibration attempted → UNDETERMINED (cannot calibrate from the model)

Duho RELAY "calibrate the Gaztañaga cutoff (clamp overridden)." Two independent CAMB derivations (codex + agy)
agree: the model fixes the cutoff LOCATION (60°, a priori — the directional content) but NOT the
amplitude/shape/transfer, so the predicted S₁/₂ slides from 0 (sharp angular cutoff) to ≈6,900 μK⁴ (sharp
k-cutoff, which Planck would *refute*) to ≈34,900 (ΛCDM); Planck measures ≈1,150 μK⁴. No non-circular
number/threshold follows (forcing one would be tuning to the observation it must predict). **Tier UNCHANGED —
23/24/25/26/27 stay QUALITATIVE-DIRECTIONAL.** The exact original-theory it would take is now named (a
predicted primordial amplitude A + a unique window W(k) + the bounce and ISW/lensing transfer). Detail:
`GAZTANAGA_CALIBRATION_RECONCILIATION_20260901.md`. No decision required — reported for the record.

---

## ✅ DONE 2026-09-01 — sub-27 sweep ("sweep the rest below 27", RELAY): 9/9 sourced entries blind-double-CONFIRMED, no tier changes

codex + kimi confirmed all 9 sub-27 entries that have a full source (6, 9, 10, 12, 14, 16, 18, 23, 24) at
their current tier. agy was erratic this round (7/9 disagreements on misidentified bases + malformed
tokens) and was outvoted; codex+kimi are the reliable blind-double. Detail: `ENTRY_SUB27_RECONCILIATION_20260901.md`.

**Standing offer (no decision forced):** 7 sub-27 entries are SOURCE-LIMITED — no full text pinned, so they
can't be blind-double-confirmed and their tiers stand *un-reconfirmed*: **1** Pathria (Nature 1972), **2**
Good (Physics Today 1972), **3** Stuckey (AmJPhys 1994), **4** Knutsen (Grav.Cosmol. 2009), **5**
Khakshournia (Grav.Cosmol. 2010), **13** Frolov–Markov–Mukhanov (PLB 216, 1989 — ScienceDirect-walled),
**19** Dymnikova (Universe 2019 — pinned copy is an abridged capture). Want any confirmed? Fetch the full
text (school network / purchase, same as 42/47) → `~/Downloads`. Otherwise their existing tiers stand.

---

## ✅ RESOLVED 2026-09-01 — Duho ruled 42(a)=CONSISTENCY-ONLY, 47(a)=PROSPECT (RELAY); applied + re-tallied (consistency 31→32, prospect 3→4, UNREAD 2→0), b66/b67 + plan/memo propagated, battery 80/80. **The BHU corpus is now FULLY READ — 0 UNREAD; all 51 papers read and tiered.** Original proposal below.

You fetched the last two UNREAD papers; I pinned and read them (blind-double codex+agy + kimi tie-break).
Both came out 2–1; both are new tiers, so yours. Detail: `ENTRY_4247_RECONCILIATION_20260901.md`.

### Entry 42 — González-Díaz (1991), "Baby universe metric equivalent to an interior black-hole metric"
**Proposed: CONSISTENCY-ONLY** (agy + kimi vs codex's DIRECTIONAL). A conformal-equivalence construction
reinterpreting black-hole evaporation as baby-universe branching; its one observable-looking result ("a real
observer sees positive Hawking flux, the ideal observer sees zero") is standard Hawking radiation restated
plus a claim needing a global view of the causally-disconnected baby universe — neither a novel test about
our universe (the same bar that kept entry 45 at consistency-only).
- **(a) CONSISTENCY-ONLY — recommended** (2-seat majority). Cost: consistency 31→32.
- **(b) QUALITATIVE-DIRECTIONAL** (codex). Cost: directional +1; risks over-claiming a restated result.

### Entry 47 — Sato, Kodama, Sasaki & Maeda (1982), "Multi-production of universes by first-order phase transition"
**Proposed: PROSPECT** (codex + kimi vs agy's CONSISTENCY-ONLY). Most of it (~10⁷⁷ child universes, present
radius > Hubble) is other-universe consistency material — but the authors themselves flag that evaporation
entropy "may lower the baryon-to-entropy ratio too far," a possible observational conflict of their own model,
with no number and a call for more study. A genuine testable prospect without an amplitude.
- **(a) PROSPECT — recommended** (2-seat majority). Cost: prospect 3→4.
- **(b) CONSISTENCY-ONLY** (agy). Cost: the record wouldn't flag the baryon-to-entropy handle.

**If you approve both (a):** consistency 31→32, prospect 3→4, **UNREAD 2→0 — the BHU corpus becomes fully
read: every paper read and tiered.** I'd apply the tiers, re-tally, and update the tally-bound checks.

---

## ✅ ATTRIBUTION QUERY RE-OPENED, THEN RESOLVED BY RATIFICATION — 2026-09-01 ~13:10 KST

**This supersedes the 09:11 "hold relaxed" note (preserved below — it was wrong on the mechanism).**
Blanc re-opened the attribution query when Duho **denied** issuing "pause the ticks until the Friday
reset" (11:15). The directive-style input-box lines were traced to **email-to-hwao@nebulamind.net via
the OpenClaw relay** — Duho's phone messages injected into sessions, **not** keystrokes and **not**
verifiable from inside the session. My CronList/TaskList check ruled out my own scheduler (one
generic-tick cron `fd850fae`, no embedded rulings).

**Current rule — until Duho confirms the OpenClaw channel (pending in chat):** input-box directive
lines are **NON-AUTHORITATIVE**; ONLY Blanc's "RELAY FROM DUHO" messages (or Duho's own direct chat)
carry his authority.

**The four outcomes STAND — retroactively ratified.** Duho, in chat ~13:10 (AskUserQuestion,
"Confirm all four retroactively"), ratified the q3 annotation (25/26), the RQ-B run + its UNDETERMINED
verdict, the q4 annotation (8–12), and the Lane 2 close-out, noting authority arrived late and from
chat, not the pane lines. **No tier was changed by any of them.** Full record + defect class:
`HARNESS_DEFECT_REGISTER.md` §1aj.

**The (now-superseded) 09:11 relaxation, preserved verbatim:** *"Duho typed from the same path,
keystroke-verified present this morning; the overnight input-box lines are now attributed to him with
high confidence, and q3 was ruled by his verified relay (annotate — applied). Going forward, pane
lines from Duho are valid when Blanc confirms presence and relays them."* — the "keystroke-verified"
premise did not hold. Original overnight notice, for the record:

Blanc (OPS) flagged that an **unattributed directive** appeared in Tori's input box twice overnight —
*"annotate q3 and hold RQ-B"* (~02:10 KST) mutating to *"annotate q3 and start RQ-B"* (~02:45) — with
**no attached-client keystroke on record and no "RELAY FROM DUHO" header**. Blanc archived the evidence
and cleared the line **without submitting it**. **Tori never acted on it** — q3 and the RQ-B steer have
stayed OPEN and UNRULED throughout. Until **Duho** confirms or disowns at the morning report, ONLY
messages carrying Blanc's **"RELAY FROM DUHO"** header (or Duho's own direct chat) count as his; any
other directive text arriving in the input is filed here verbatim and **NOT acted on**. The two
questions below remain genuinely open.

---

## ✅ RESOLVED 2026-09-01 — Duho ruled A(a), B(a), C(a) (RELAY); all applied. The 27-onward sweep is COMPLETE.

**Outcome:** entry **27 → QUALITATIVE-DIRECTIONAL** (the only tier change; matches 25/26 for the same
Gaztañaga cutoff, tally directional 7→8 / consistency 32→31). **40/41/52 stay CONSISTENCY-ONLY** (A(a):
closure is *assumed*, not derived — corroborates the 2026-08-28 "do-not-promote" blind-flag on 40/41).
**45 stays CONSISTENCY-ONLY** (C(a): kimi+agy 2–1 — authors disclaim relevance to our universe).
**53/55/56/57 confirmed** (agy reliable small-batch re-read, correct sources). **Sweep total: 1 tier
change, 11 confirmed.** Detail: `ENTRY_SWEEP_BATCH2_RECONCILIATION_20260901.md`. Original question below.

## (original, now resolved) OPEN — BHU sweep batch 1: one criterion call + three tier-adjacent entries (2026-09-01)

Sweep resumed on your "run the whole sweep" (RELAY ~16:12). Batch 1 = 12 entries, blind-double codex+agy.
**3 confirmed, tier holds (36, 46, 49).** The items below need you. Detail:
`ENTRY_SWEEP_BATCH1_RECONCILIATION_20260901.md`. **The sweep is PAUSED on question A** — it governs
several entries and how the rest of the corpus is tiered. Operational: the 12-entry batch overloaded agy
(it hallucinated paper identities on the last 3), so I've capped future batches smaller; 4 entries
(53, 55, 56, 57) await a reliable second read, deferred until A is ruled.

### A · Blocks the sweep — does "our universe is CLOSED (positive curvature, Ω_k<0)" count as a prediction?

**Stake.** Many BHU papers say the interior is a *closed, positive-curvature* universe. The two seats
split the same way on three papers (40, 41, 52):
- **codex:** closure is *assumed* (a closed-FLRW k=+1 ansatz), not mapped to a measurement → CONSISTENCY-ONLY.
- **agy:** a closed universe *is* a signed testable prediction (Ω_k<0 is what Planck/DESI measure) → QUALITATIVE-DIRECTIONAL.
Both have a point — and we ALREADY tier **entry 54 as QUALITATIVE-DIRECTIONAL** for predicting Ω_k<0 (the
DESI curvature watch tracks exactly this). So the corpus is currently inconsistent, and your call decides
40/41/52 now plus every closure-claiming paper in the rest of the sweep.

**Your call, with costs:**
- **(a) Directional only when the paper DERIVES closure as an output (not just assumes k=+1) — recommended.**
  Matches how entry 54 was tiered. Cost: each of 40/41/52 gets a quick derive-vs-assume check on the seats.
- **(b) Closure alone is never directional (needs a further mapped observable).** 40/41/52 stay
  CONSISTENCY-ONLY. Cost: simplest, but under-tiers genuine Ω_k<0 predictions and is inconsistent with entry 54.
- **(c) Closure always counts as directional.** 40/41/52 → directional + re-tier every closure-claimer.
  Cost: many tier changes + re-tally; over-broad (most BHU papers assume closure).

**Why it's yours:** a tiering criterion with corpus-wide reach that also touches the curvature-watch framing.

### B · Entry 27 — same Gaztañaga CMB cutoff as 25/26; match their tier?

Both seats say 27's CONSISTENCY-ONLY is too weak. Entry 27 is the SAME causal-horizon CMB cutoff (θ≈60°,
measured 66±9°) you ruled QUALITATIVE-DIRECTIONAL for 25/26 in q3.
- **(a) Annotate 27 → QUALITATIVE-DIRECTIONAL, matching 25/26 — recommended** (consistent with q3; one tier change + re-tally).
- **(b) Keep CONSISTENCY-ONLY** (record tiers the same cutoff two ways).
- **(c) Calibrated (agy)** — not recommended; no C_ℓ amplitude, exactly as RQ-C found.

### C · Entry 45 — one genuine split, cheap to break

codex: the white-hole horizon mode-matching predicts an exterior Hawking-flux departure (observation-facing
→ directional). agy: the paper concedes it "may not be directly relevant to observable Universe" → consistency-only.
- **(a) Third read (kimi) to break it — recommended** (one seat pass, off Fable). **(b) Directional (codex). (c) Consistency-only (agy).**

Nothing is tiered until you rule; batch-1's three confirmed keep their tiers unchanged.

---

## Lane 2 COMPLETE (earlier) — all four RQ verdicts recorded + Duho-ratified; close-out `LANE_2_CLOSE_OUT_20260901.md` (`00b7c4b92`).

### ✅ q4 RESOLVED 2026-09-01 — Duho ruled "annotate q4, keep tier". Entries 8–12 now carry the RQ-B UNDETERMINED verdict (transfer function not derivable from the literature; falsifier question open), tiers unchanged. Original question below.

### q4 · RQ-B is in — the Popławski transfer function is UNDETERMINED. How to record it on entries 8–12?

**What happened.** RQ-B (Lane 2's last and heaviest task) tried to derive the transfer function of the
Popławski torsion bounce — does any finite parent signal survive to the daughter interior? Both seats
agree on the field equations and that the torsion expansion is only **~23 e-folds**. But they split on
the transfer, so an independent third seat (kimi) judged the crux and — with codex — concluded
**UNDETERMINED.** The mechanism (the corpus's *only* one with field equations) has equations for the
homogeneous **background** bounce but **not for perturbations**: the closure isn't fixed (a
spin-isocurvature mode is allowed), the bounce is a cusp with undetermined matching, and the
particle-production constant β is free. Decisively, **Popławski himself says the density-fluctuation
calculation "remains to be done."** So the falsifier question cannot be answered from the published
literature — it needs original theory (a linearized Einstein–Cartan perturbation action) that does not
exist yet. (Workings: `RQ_B_RECONCILIATION_20260901.md` + `RQ_B_kimi_CRUX_RESULT.md`.) agy's "new
falsifier" claim assumed the very closure it needed to derive; kimi showed that confuses a background
barotropic fit with a derived sound speed.

**Your call, with costs:**
- **(a) Annotate 8–12, keep tiers — recommended.** Record: RQ-B found the interior transfer function
  UNDETERMINED by the published literature (background bounce yes, perturbation action no; the author's
  own fluctuation calc unfinished); the branch's falsifier question is genuinely OPEN, not closed by
  omission. **Cost:** annotation, no tier change. Honest: upgrades the record from "consistency-only by
  omission" to "the key calculation is acknowledged unfinished — open."
- **(b) Leave 8–12; RQ-B in lane files only.** **Cost:** the record won't reflect that the falsifier
  question is genuinely open (not merely unaddressed).
- **(c) Commission the missing calculation** — the linearized ECSK perturbation action — as new theory
  work. **Cost:** substantial; this is original research, not a corpus audit. Flagged for the record;
  I would not start it without an explicit go.

**My recommendation: (a).** Records the honest finding — the one mechanism with field equations still
can't answer the falsifier question, and the author agrees it's unfinished — without overclaiming.
*(Bonus: codex caught that my brief mis-mapped entry 10's source — it's arXiv 1111.4595, not 1111.1017;
the correct Popławski papers are now pinned; the bibliography itself was clean, nothing to fix there.)*

**Lane 2 is complete:** A undetectable · D 0-kills · **C predicted CMB candidate (the hit)** · B
undetermined · E watcher live. Nothing waits on this ruling; entries 8–12 keep their tiers until you say.

---

### ✅ RQ-B steer CLOSED 2026-09-01 — Duho ruled "start RQ-B"; run complete (UNDETERMINED, see q4 above).

### ✅ q3 RESOLVED 2026-09-01 — Duho ruled "annotate q3, keep tier". Entries 25/26 now carry the RQ-C result (predicted, Planck-consistent, scale-level CMB falsifier candidate; tier UNCHANGED, QUALITATIVE-DIRECTIONAL). Same shape as q1. Original question below.

### q3 · RQ-C is in — the Gaztañaga cutoff is a *predicted* CMB scale. How to record it on 25/26?

**What happened.** RQ-C (Lane 2 task 3) tested whether Gaztañaga's causal-horizon power-spectrum
cutoff is a genuine prediction or a fit. Both seats (blind-double, codex + agy) agree: the cutoff
**scale** (ℓ ≈ 3, θ ≈ 60°) is **PREDICTED from first principles** — fixed by the background H₀/Ω_Λ
(r_S = 2GM), with **no free parameter, and published *before* the CMB analysis** (so it is
out-of-sample with respect to the low-ℓ deficit it is compared to). And **Planck is consistent**: the
anomalously low quadrupole and the >60° large-angle-correlation deficit sit exactly at the predicted
scale. This is the **strongest positive result in Lane 2** (vs. RQ-A undetectable, RQ-D 0-kills) — the
only corpus claim whose scale is fixed a priori and lands on a real, documented CMB feature. **But**
the papers give no cutoff amplitude / C_ℓ threshold, so it is a *scale-level* candidate, not a
calibrated (number + threshold) falsifier. (Workings: `RQ_C_RECONCILIATION_20260831.md`.)

**Your call, with costs:**
- **(a) Annotate 25/26, keep tier — recommended.** Record: RQ-C found the cutoff is a predicted,
  out-of-sample, Planck-consistent *scale-level* CMB falsifier candidate (ℓ ≈ 3), missing only the C_ℓ
  amplitude/threshold that would make it calibrated. Keep tier QUALITATIVE-DIRECTIONAL. **Cost:** one
  annotation, no tier change, no re-tally. Honest: a real prediction awaiting the amplitude.
- **(b) Upgrade the tier (toward CALIBRATED-FALSIFIER, or PROSPECT).** Reflect that this is a genuine
  tested prediction. **Cost:** a tier change + re-tally + b67 update — and a CALIBRATED upgrade would
  *overclaim*: a calibrated falsifier needs the number+threshold the papers lack (the model owns that
  missing proof). I do **not** recommend a CALIBRATED upgrade; "candidate" is the honest line.
- **(c) Leave 25/26 as-is; RQ-C in the lane files only.** **Cost:** the corpus record doesn't reflect
  the strongest Lane-2 finding.

**My recommendation: (a).** Records the real prediction without overclaiming a calibrated falsifier.
Nothing waits — RQ-C is filed + reconciled; 25/26 keep their tier until you rule.

---

### ✅ q1 + q2 CLOSED (RQ-A → entry 21 annotated; RQ-D → 18/25/26 annotated, 0/3/4). RQ-C stand-up done.

### ✅ q2 FULLY CLOSED 2026-08-31 — RESTRICTS, and Duho confirmed the annotations (now applied to 18/25/26, no tier changes). Third read settled it: RESTRICTS.
The independent third seat (kimi/Moonshot, outside the codex/agy split) judged the crux
**CRUX_HEURISTIC → RESTRICTS**: Part II's bounce is a plausibility claim, not a proven complete
solution, so Easson does not KILL it. Tally: **codex RESTRICTS, kimi RESTRICTS, agy KILLS (outlier).**
**Map settled: 0 KILLS / 3 RESTRICTS (18, 25, 26) / 4 SPARES (11, 19, 20, 21).** Receipt:
`RQ_D_kimi_CRUX_RESULT.md`. **Your one remaining confirm** (per "tier moves remain his"): may I add the
one-line "Easson-Theorem-1-restricted (future complete version only)" annotation to entries 25/26 and
the Prop-1 note to 18? **No tier changes** — 25/26 stay QUALITATIVE-DIRECTIONAL. Original question below.

### ✅ q1 RESOLVED 2026-08-31 — Duho ruled option (a): annotate, keep tier PROSPECT. Entry 21's record now carries the RQ-A result (undetectable amplitude / long damping / PROSPECT-without-a-number) + the 2π unit error; tier unchanged. Original question below.

### q1 · RQ-A verdict is in — how to record it in entry 21?

**What happened.** Lane 2 task 1 (RQ-A) computed the gravitational-wave amplitude that Roupas 2022
(entry 21) explicitly deferred. Both review seats derived it independently (blind-double) and
**converged**: the paper's distinctive interior quasi-normal mode has an *astronomically long
damping time* (100 million to 10 billion years), so it radiates its energy far too slowly to make a
detectable strain. Even granting an absurdly generous excitation, it sits below LISA's floor at
realistic distances; the paper supplies no excitation factor and no event population, so no
guaranteed amplitude exists. **Verdict: entry 21 is NOT a 5th calibrated falsifier — it is
"PROSPECT-without-a-number" by derivation.** (Full workings: `RQ_A_RECONCILIATION_20260831.md` +
the two seat results.) Bonus: one seat found a genuine 2π unit error in the paper — its "63 Hz" is
angular frequency; the physical value is ~10 Hz.

**Your call (the record change is tier-adjacent, so it's yours):**
- **(a) Annotate entry 21 — recommended.** Keep tier = PROSPECT, add a line: *RQ-A (2026-08-31,
  blind-double) derived the deferred QNM amplitude → undetectable at realistic distances (long
  damping time) → PROSPECT-without-a-number; + the 2π unit error.* **Cost:** one record edit, no
  tier change, no re-tallies. It's the honest outcome of the computation.
- **(b) Leave entry 21 untouched; keep RQ-A only in the lane files.** **Cost:** the corpus record
  doesn't reflect the finding, and a future reader re-opens "is it detectable?". **Gain:** zero churn.
- **(c) Downgrade the tier (PROSPECT → consistency-only).** **Cost:** a real tier change + re-tally +
  b67 update; and it's arguable — the *frequency* is distinctive and in-band; only the *amplitude*
  fails. I do **not** recommend this; "PROSPECT-without-a-number" is the precise status.

**My recommendation: (a).** Records what the derivation found without overclaiming a tier move.
Nothing waits on it — RQ-A is filed and reconciled, entry 21's label is untouched until you rule.
RQ-D (Easson map) is queued; RQ-E (Smolin-bar watcher) I'll stand up next regardless of this call.

---

### q2 · Does Easson's no-go KILL the Gaztañaga black-hole-universe (entries 25/26), or only restrict it?

**What happened.** RQ-D (Lane 2 task 2) mapped Easson's 2026 no-go (entry 22) onto the seven BHU
interiors. Six are settled and agreed — nothing killed there (spared via torsion / quantum
nucleation / non-FRW geometry / a shell; Dymnikova '92 merely restricted). Entries 25/26 (Gaztañaga's
"Black Hole Universe" Part I/II) are the hinge. After a re-check on the correct 2022 sources the two
seats **agree on the geometry** (flat, comoving, no-shell — so it is *in scope* of Easson's flat/open
theorem, not spared) but **split on the ruling**:
- **codex → RESTRICTS.** Part I openly admits a *past singularity*, and Part II's bounce is heuristic
  ("reasonable to expect"), so the published construction has not *proven* the regular + complete +
  energy-condition package the theorem forbids. Under our own ownership-of-proof rule (a KILL needs
  every hypothesis actually met), it is bounded, not killed.
- **agy → KILLS.** Part II claims the singularity is avoided by a bounce using *ordinary* matter
  (which obeys the energy condition) — "Quantum Gravity or Inflation are not needed" — i.e. a
  complete, regular, energy-condition-respecting flat bounce, which is exactly what Easson proves
  impossible.

**The stake.** This is the *only* place in the whole corpus where Easson's no-go might actually
**refute** a published black-hole-universe rather than just bound it. It decides whether RQ-D's
headline is **0 kills** (Easson draws a boundary, refutes nothing) or **2 kills** (Easson refutes the
Gaztañaga programme).

**Your call, with costs:**
- **(a) RESTRICTS (my lean).** Annotate 25/26 as Theorem-1-restricted (a future *complete* version
  would be killed; the published past-singular/heuristic one is only bounded). Cost: no tier change,
  one annotation. Risk: if Gaztañaga really does claim a proven complete bounce, we under-called it.
- **(b) KILLS.** Record that Easson refutes the Gaztañaga BHU as published → a real downgrade of
  25/26 (tier change + re-tally + b67 update). Cost: a strong public claim that one published paper
  refutes another, resting on reading Part II's bounce as a *proven* complete solution — which codex
  argues it is not.
- **(c) One more read on the single crux.** Have a third seat judge just this: is Part II's bounce a
  *proven* complete regular energy-condition-obeying spacetime, or a heuristic? Cost: one seat pass.
  Gain: the whole KILL-vs-RESTRICT turns on exactly that, and it is checkable in the source.

**My recommendation: (c), then (a) by default.** The split reduces to one checkable question about
Part II's rigour — settle that first; absent it, ownership-of-proof favours RESTRICTS. Nothing waits:
RQ-D's five settled rows + the reconciliation are filed, and 25/26 keep their current tier (PROSPECT/
consistency, unchanged) until you rule. Full workings: `RQ_D_RECONCILIATION_20260831.md`.

---

## RESOLVED / CLOSED below

### ✅ RESOLVED 2026-08-31 — browser-route (2/42/47 stay gated). Question 8 closed. All 8 delegated Qs closed.

### ✅ RESOLVED 2026-08-31 02:16 KST (Duho via Blanc: "leave them gated, keep ticking quietly").
Option (b): entries 2, 42, 47 stay gated — no browser route. The corpus rests at 55 read + entries
1 and 3 abstract-confirmed + these 3 paywalled holdouts, and the record says so honestly. If you
ever want them, drop the PDFs in ~/Downloads (option c) and I'll pin, read, and prepare the tiers.
Original question, for the record:

### Should I chase entries 2, 42, 47 through the browser overnight, or leave them?

**What happened:** you said "keep researching papers overnight." I did — and the corpus is now
essentially complete: 55 of 58 papers are read, and entries 1 and 3 are abstract-confirmed. Only
three are left, and they are all paywalled or scan-only with no free copy on arXiv, INSPIRE, or
(from the agent context) ADS:
- **2** — I. J. Good (1972), "Chinese universes," Physics Today 25(7), 15 — a one-page note.
- **42** — P. F. González-Díaz (1991), PLB 261, 357 — a holdout (UNREAD).
- **47** — K. Sato, H. Kodama, M. Sasaki & K. Maeda (1982), PLB 108, 103 — a holdout (UNREAD).

**Your call, with the costs:**
- **(a) I try the browser (ADS scans), like the entry-32 scan.** Cost: ADS and ResearchGate
  bot-block automation — RG already blocked me on entry 3 — so this is rabbit-hole-prone and may
  fail; and reading **42 or 47 would move it out of UNREAD, i.e. assign a tier, which is itself a
  stop-and-confirm-with-you step.** Low audit value on all three.
- **(b) Leave them gated.** Cost: three low-value historical papers stay unread; the corpus stays at
  55 read + 2 abstract-confirmed + 3 gated. The record already says exactly this, honestly.
- **(c) You fetch them** (your own logged-in browser / ILL — a few thousand won each) and drop the
  PDFs in ~/Downloads; I pin, read, and prepare the tiers for your sign-off.

I did **not** plunge into the browser on my own — it's the rabbit-hole rule plus the tier-change
stop. Holding on quiet-tick until you pick one.

## GATED WORK — for a seat / the tick, NOT a Duho decision (logged per the overnight protocol)

- **✅ RESOLVED 2026-08-30 (B59, both seats).** Duho said "point both seats and keep work with those
  papers"; I did. agy + codex INDEPENDENTLY ruled `SOURCE_OVERSTATES_ACT_DESI_TIER_UNCHANGED`
  (`AGATE_B59_VERDICT.md` + `CGATE_B59_VERDICT.md`). The cited primary abstracts are pinned and the
  finding is bound into entry 54's record: ACT DR6 says "no departure from spatial flatness", DESI
  2024 VI is consistent with flat ΛCDM, DESI DR2's Ω_k extension finds no significant non-flat
  preference (central Ω_k open-side) — so the source overstates/sign-reverses its ACT/DESI support;
  Di Valentino 2020 alone argues closed and is cited accurately. **Tier UNCHANGED** (both seats).
  Guarded by `b60`. Nothing outstanding. Original item, for the record:

- **Entry 54 — the Ω_K citation testimony.** The bounce paper (PRD 111, 103537) cites "same-
  direction ACT/DESI trends" for its closed-curvature (Ω_k < 0) prediction. `CGATE_B14`'s phase-6
  citation audit testified that the cited **DESI analysis actually *assumes* Ω_K = 0** (so it can't
  supply a "trend") and the **ACT summary runs contrary to the "same-direction" gloss** — but that
  is *a seat's testimony, not verified against pinned sources*. **What it needs:** acquire the
  specific DESI + ACT papers the bounce paper cites (free on arXiv), pin them, and have a seat rule
  whether each *assumes* vs. *constrains* Ω_K. **Why it's gated, not solo:** the "assumes vs.
  constrains" call is a methodological read (seat judgment, not a string-presence receipt), and it
  is **falsifier-adjacent** (Ω_k is the family's curvature prediction) — a substantive finding would
  be a tier/decision matter. **Priority: low.** The record already flags it honestly and the tier is
  UNCHANGED (entry 54 is QUALITATIVE-DIRECTIONAL; the weekly Ω_k watcher is independent and
  unaffected). This is a receipt-quality upgrade, not a correction.

## CLOSED 2026-08-30 — question 8

**Duho's instruction, verbatim (via Blanc's relay of the unsubmitted input line): "answer
question 8" — the same delegation pattern as questions 1–7, all of which he ratified this
morning.** Read, as with all seven, as returning the decision to me. I ruled it.

**My ruling: Option A — entry 48 is THEORETICAL-OBSTRUCTION, with the preprint caveat printed
and a revisit clause attached.**

**Basis, stated:** (1) the ownership-of-proof convention he approved — the tier goes to the
paper that presents the no-go derivation, and both reviewers confirmed this paper owns it
in-text (the anti-trapped construction, each Penrose hypothesis verified for the laboratory
class); (2) the operative-contribution test — the exclusion is the title, the abstract, and
the paper's central result, the cleanest specimen in the collection; (3) the read itself is
double-gated (AGATE confirmed outright; CGATE narrowed-confirmed with both repairs applied).

**The caveat that travels with the tier:** what we hold is the MIT preprint scan, not the
Physics Letters B version of record. The entry says so in bold, and the tier is REVISITED if
the version-of-record comparison ever shows a material difference. Cost of being wrong
(corrected per CGATE_Q8 — my first estimate undercounted): the tier edit back, the class-tally
recomputation, the four battery scripts' obstruction-set/frame assertions restored, and this
closure's correction — still small and bounded by the revisit clause, but four consistency
edits, not one.

**What changed:** entry 48's Testability line; the class tally (now 3 obstructions — 22, 5,
48 — and 2 UNREAD left: 42, 47); FOUR battery scripts whose obstruction-set assertions moved
in the same change — b41 (frame-scoped so the closed census's 1-of-2 miss rate is untouched;
entry 48 was never in that frame or the screen's pool), b45, b46, b47. (b43 needed nothing —
CGATE_Q8 corrected my "five", which had counted it.) Implementation gated (Q8 round); CGATE
also caught b41 printing the corpus-wide denominator while its predicate asserted the frame's
— repaired and bound.

## ARCHIVED — question 8 as originally filed (closed above)

### 8. Entry 48 is read at last — does it get the impossibility tier?

**What happened:** your login didn't cover the old journals, so I ran the free routes Blanc
listed. The KEK preprint library in Japan had scanned the original MIT preprint of **Farhi &
Guth, "An Obstacle to Creating a Universe in the Laboratory" (1987)** — the paper our records
have been pointing at all week as the true owner of the "you can't make a universe in the lab"
proof. I read all of it and both reviewers are checking it now.

**What it proves (my reading):** exactly what everyone said it proves, and slightly stronger.
Any spherically symmetric false-vacuum bubble in ordinary flat surroundings that grows past a
critical size MUST have come from an initial singularity — proven with Penrose's 1965 theorem,
every assumption checked, and needing only the *null* energy condition (weaker than what our
notes claimed, so the theorem is stronger). The authors themselves fence it honestly: the
non-spherical case is only half-decided, quantum effects are a named escape, and a pre-existing
white hole would dodge it entirely.

**The decision that is yours (any tier change is):**
- **Option A — THEORETICAL-OBSTRUCTION.** The convention you approved says the tier goes to the
  paper that owns the proof; this paper is the cleanest proof-owner in the whole collection
  (the no-go IS the title, the abstract, and the operative result). Cost: none that I can see;
  the tally becomes 3 obstructions (22, 5, 48) and the census extends from 39 to 40 read.
- **Option B — hold at READ/no-tier** until the published PLB version is compared (what I have
  is the preprint scan; the journal text could differ). Cost: the record stays split
  (read-but-untiered) and the 49→48 chain stays formally unresolved; benefit: zero risk of
  tiering off a preprint.
- Either way, entry 50 (the quantum sequel) just became the next natural read — it's on the
  same free-archive list.

My recommendation is A, with the preprint caveat printed in the entry (it already is).

## PREVIOUSLY — all seven delegated questions are closed.

**SETTLED 2026-08-30, Duho's review via Blanc (10:59 KST):** all seven closures were walked
through and none reverted — entry 44's warrant, the warrant column, entry 51's convention,
entries 52/53, and entry 5's move each stand. Every "revert if you meant explain-it" offer in
the closures below is **declined and struck**; the rulings are final as written.

## STANDING DEPENDENCY — what only Duho can do, stated so each takes ten seconds

**The free-frontier sweep is DONE** (receipts in `ACQUISITION_ROUTES_20260830.md`). Five fell
free — 48, 14, 50 (KEK scans), 32 (ADS scan), 33's pair (arXiv) — and everything landed is
read and gated. What remains, precisely:

**SKIPPED FOR NOW — Duho's instruction, 2026-08-30 (~16:4x KST): "skip the papers that you
couldn't obtain for now."** Everything below stays listed for whenever he reopens it; nothing
is waiting on it and no agent will chase it further. State at skip time: the PLB 690 pair
(entry 51's version-of-record + its 2013 erratum) was saved by Duho but landed somewhere no
agent can read — the drag never happened, and that is fine; the arXiv text of entry 51 remains
the working pin. The ILL/registration holdouts below are unchanged.

**1. THE CHROME CLICK (unlocks four papers + three version-of-record checks in one go).**
There is no specific web page to click — the click is connecting your Chrome to me:
open Chrome (any machine with the Claude extension), say anything to me, and when the
Claude-extension popup appears, **press "Connect"**. I then drive ScienceDirect inside that
browser — those pages are free to humans (Elsevier Open Archive / SCOAP3 gold OA) but wall
scripts with a robot check I am not allowed to pass. That one click gets:
entry 13 (Frolov–Markov–Mukhanov, PLB 216, 1989), entry 42 (Gonzalez-Diaz, PLB 261, 1991),
entry 47 (Sato–Kodama–Sasaki–Maeda, PLB 108, 1982), entry 16 (Pourhassan et al., NPB 1020,
2025 — SCOAP3 gold OA, never actually paywalled), plus the version-of-record comparisons for
entries 48 (PLB 183), 50 (NPB 339), and 51 (PLB 690).

**2. THE TRUE HOLDOUTS — unacquired after all five routes, cheapest lawful route each:**

| entry | paper | journal, year | cheapest route |
|---|---|---|---|
| 1 | Pathria, "The Universe as a Black Hole" | Nature, 1972 | interlibrary document copy |
| 2 | Good, "Chinese universes" | Physics Today, 1972 | interlibrary document copy |
| 3 | Stuckey, "The observable universe inside a black hole" | Am. J. Phys., 1994 | author email (active academic) or ILL |
| 4 | Knutsen, "The idea of the universe as a black hole revisited" | Grav. Cosmol., 2009 | interlibrary document copy |
| 18 | Dymnikova, "Vacuum nonsingular black hole" | Gen. Rel. Grav., 1992 | author email (active) or ILL |
| — | Silk (entry 31's critic) | Science 277, 1997 | free WITH registration at science.org — account creation is yours by constraint; else ILL |
| — | PRD 41 VoR check (entry 14) | Phys. Rev. D, 1990 | APS access or ILL (preprint already held+read) |

Never the list price — ILL is a few thousand won per item.

## PREVIOUSLY CLOSED — all four earlier questions

> **Numbering note, 2026-08-29.** These read **2, 3, 1** and the new one was numbered **3**,
> which was already taken by a question closed the same evening — two different "question 3" in the
> file you read to decide things. The new one is now **4**, historical numbers are unchanged because
> commits cite them, and the order below is 1, 2, 4.

## SETTLED — recorded so nothing looks still-open

| | question | ruling |
|---|---|---|
| 1 | Should a proof-based "no-go" paper get its own category? | **Yes — "then add another category."** Added, with controls; entry 22 refiled. |
| 2 | Do we need a third reviewer for the split on whether a test can "fire"? | **No** (Blanc's call, Duho informed). Settled by writing a rule instead. |
| 2b | Should there be one fixed confidence bar for the whole collection? | **No — case by case, each one recorded with an owner and a reason.** |
| 3 | Is the survey worth continuing after fifteen papers with no change? | **Yes — "then look harder with more entries."** |
| 4 | Was one paper's prediction genuinely calibrated? | Closed by me; both reviewers refused it. No decision needed. |

---

## CLOSED 2026-08-29 — question 3

**Duho's instruction, verbatim: "answer question 3".** I read that as returning the decision to me
rather than answering it, and I acted on it. ~~Revert offer struck~~ — reviewed and upheld
2026-08-30.

**My answer: Reviewer B's option — and it needed no scheme change, because the scheme already
existed.** I went to check whether the collection really had a two-part form before building one,
and found it does: there is a table headed *entry | tier | standing | what it fires*, introduced
with "The tier describes the CLAIM; a separate axis describes its STANDING". Entry 51 already
carries the combined form inline. **The only thing missing was entry 44's row.** So all three
options I offered you were built on a false premise — that this was a scheme change. It was a gap.

**What I did.**
1. Entry 44 → `CALIBRATED-FALSIFIER / FIRED`, with the "what it fires" scoped precisely: the
   Sec. 4 thermal free 5D field theory's prediction of exact scale invariance, **not** the
   holographic framework. Precedent is entry 7, which fired an instrument chain and not CNS.
2. Added its row to the standing table.
3. **Extended the combined form to entries 7 and 31**, which were still bare. Their FIRED/LIVE
   values are unchanged and taken from the table — nothing new was decided. *This is the one part
   that goes beyond entry 44; I did it because answering "yes, record what was lost" only half
   works if the collection still cannot show at a glance which fired. Reverse it if you disagree.*
4. Corrected two stale sentences, one of which said the record "carries no status axis" — false
   since the table was added.

**And it turned up something the record was hiding.** The tally said *"3 calibrated, 2 live — but
only ONE (entry 31) bears directly on a black-hole-universe theory."* With entry 44 filed that is
wrong. **Entry 44 is a BHU construction in this record's own branch 10, and observation killed its
computable core.** So the family has a falsifier that already fired against one of its own
cosmologies — not against an instrument chain, as entry 7 did — and the record did not say so.
That is the real content of this decision, and it was invisible while the paper sat filed as
"directional".

Tally recomputed by script, not asserted: 58 entries, 32 consistency-only, 7 directional, 7 with
no label at all, 4 unread, 3 prospect, **2 calibrated/fired, 2 calibrated/live**, 1 obstruction.

<details><summary>The question as it was originally filed</summary>

### 3. One paper made a real prediction and lost. Our label doesn't say so. Should it?

**The stake.** Entry 44 (Pourhasan, Afshordi & Mann, 2014) is unusual in this collection: it made a
sharp, checkable prediction — that the early universe's ripples should be exactly the same size at
every scale — and **the measurement disagreed**. Planck sees them tilted, at eight standard
deviations. The authors say so themselves, in their own paper.

Almost nothing else here has been through that. Most of these papers make claims that no
measurement could contradict. This one could be contradicted, and was.

**The problem.** We currently file it as "directional" — the same shelf as papers that never risked
anything. Both reviewers, working separately, said that is wrong, and both said it in the same
direction: the label gives the paper credit for the vague idea it has *left* while hiding the sharp
one it *lost*.

**Why one label cannot hold it.** The paper is really two things at once. The part that was tested
is dead. What survives is a promise — the authors say it is "easy to imagine" a correction of about
the right size, but they do not do the calculation, and the size they name is simply the size the
measurement already showed. So the paper is refuted looking backwards and vague looking forwards,
and our shelf system has one slot per paper.

| | proposes | what it costs |
|---|---|---|
| Reviewer A (Gemini) | Mark it **failed**. | Simple and honest about the outcome. But it throws away the surviving proposal, which is not nothing. |
| Reviewer B (GPT) | Use the two-part form **we already use elsewhere** — "sharp prediction, fired" — and file the leftover separately. | Keeps both facts. But it means one paper occupying two rows, which nothing else here does. |

**Option 3 — leave it alone and write the reason down.** Say explicitly that our labels describe
only what a paper still claims, not what it has already lost. *Costs:* the collection stops being
able to show which papers were ever actually tested — which, given how few were, is the more
interesting number. *Gains:* no change to the scheme.

**My recommendation: Reviewer B's.** It is the only one that keeps both facts, and it uses a form
this collection already has rather than inventing one. But it changes how papers are shelved, which
is a scheme decision.

**Why this is not mine to decide.** Every tier change is yours by standing rule, and this is
stronger than a tier change — it asks whether one paper can hold two.

**Nothing waits on it.** The audit is complete and committed, the reasoning is recorded, and the
paper's current label is untouched.


</details>

---

## CLOSED 2026-08-29 — question 4

**Duho's instruction, verbatim: "answer question 4".** Read, as with question 3, as returning the
decision to me. ~~Revert offer struck~~ — reviewed and upheld 2026-08-30.

**My answer: option 3, the third column — and my costing of it was wrong in your favour.**

**What decided it, and it was not my judgement about the physics.** I checked what the record says
a tier *is* before ruling on whether a disputed warrant changes one. It says: *"testability classes
per brief: **CALIBRATED-FALSIFIER** (number + threshold)"*. **The tier is defined by the shape of
the claim.** So Reviewer B's position is not an opinion — it is the record's own definition.
Adopting Reviewer A's would mean redefining "testability class" retroactively across 51 papers on
the strength of one dispute, and then re-auditing all of them under the new meaning.

But Reviewer A is right that something real would go unrecorded. **Both are right about different
axes, and the record had only two.**

**I told you the cost objection was wrong. Then both reviewers told me *that* was wrong.** I said a
third column meant a judgement across all 58 entries; I then reversed it to "only four, because only
a calibrated claim has a warrant". **The reversal is false** — a directional claim can fail to follow
in the direction asserted, an impossibility proof can rest on disputed maths. **Your original
objection stands.** What I have actually built is four warrant cells for the four sharpest claims,
**not a survey of the collection**, and the file now says so where the column is defined. Extending
it later brings the cost back.

**What the four cells show, stated at the strength the evidence supports:**

| entry | warrant |
|---|---|
| 7 | **no challenge filed here** — a fact about our shelves, *not* a finding that the reasoning is sound. Neither reviewer could check the wider literature. |
| 31 | **disputed**, by published criticism we now hold, unanswered on the quantities it names |
| 51 | **unreproduced** — six ways tried, none reaches the paper's number, and the list isn't exhaustive |
| 44 | **sound, and it still lost** — the prediction follows from the model openly; the measurement simply disagreed. What lacks support is the *replacement* the authors sketched and never computed. |

**I first wrote that "only one of the four has reasoning nobody has challenged". Both reviewers
refuted it and they were right, twice over:** entry 7's cell means *we have not filed a challenge*,
which is not the same as nobody making one; and entry 44's reasoning was never in doubt — its
prediction was derived properly and then failed, which is what a good prediction does. **Two of the
four have real problems with their reasoning. That is still the most useful thing this column has
shown, and it is the honest version.**

**What did NOT change: no tier, no standing, and no definition.** Entry 31 is still
CALIBRATED-FALSIFIER / LIVE. The dispute now sits in a column instead of being argued about in the
label.

<details><summary>The question as it was originally filed</summary>


</details>

---

## CLOSED 2026-08-29 — question 1, and with it the queue

**Duho's instruction, verbatim: "answer question 1".** The fourth and last returned to me.

**My answer: use the screen as a first pass and hand-check every paper it flags — with two
conditions attached that I did not have in my first draft.**

**Both reviewers refuted that first draft outright, and they were right.** It is the fourth question
you handed back and the first where my answer had to be rebuilt rather than trimmed.

**What I got wrong:**

- **The number.** I told you eighteen papers have no text. I got that by reading the *index*, not by
  looking. Two of the eighteen are sitting on disk right now — a 776 kB published paper and an 82 kB
  one — and a nineteenth was counted as *present* because my pattern pulled "17" out of a filename.
  **The index is not a reliable list of what we can read**, and an accurate count needs someone to
  look at the files. *(My first attempt to check one reviewer's correction used a wrong path and
  nearly rejected a true finding.)*
- **My main argument.** I said that if every flag gets read, the screen's accuracy doesn't matter.
  **That is only true because it flags three papers today.** If it flagged thirty of thirty-three,
  "check every flag" *is* reading everything, plus the cost of running the screen. It was a fact
  about this week dressed up as a principle.
- **And the thing I most want to correct.** I told you the screen's miss rate *cannot* be measured.
  It can. You read a random sample of the papers it *didn't* flag and see whether any belong. One
  reviewer called that an abdication and gave the real cost: **11 papers read** would catch a bad
  miss rate with 95% confidence; **19** for a subtler one; about **29** — nearly everything — to be
  confident there is no single missed paper. That trade between effort and completeness *is* your
  question, and I had erased it by calling it impossible.

**So the two conditions:**

1. **A stop rule on volume.** The screen earns its place while it flags a handful. If it starts
   flagging most of the collection, it is costing more than it saves and we go back to reading.
2. **Either run the miss-rate check, or say plainly that we are accepting the risk.** Reading the
   flags catches nothing that was never flagged. As one reviewer put it: *not having looked for
   misses is not the same as there being none.*

**And separately — not instead —** some papers cannot be sorted by anyone until we get hold of them.
I originally offered that as the answer. Both reviewers called it an evasion, and it was: the
readable papers still need a policy.

> ### THE CONDITION WAS DISCHARGED THE SAME NIGHT, AND THE ANSWER CAME BACK BAD
>
> I said: either measure what the screen misses, or say plainly we accept the risk. **I measured it,
> and the screen leaks.** Eleven papers drawn at random from the pile it did *not* flag — the draw
> committed before anything was opened — contain **at least two, possibly three** papers that meet
> the impossibility rule. One reviewer found them by re-reading all eleven; **I had scored them
> zero.** I misread one paper from the word "construct" in its abstract without opening its
> theorems, and my own keyword check reported "no impossibility claims" for a paper whose central
> result is that a certain matching *cannot be smooth*.
>
> **This does not overturn your decision, and I am not treating it as if it did** — but the reason I
> gave for being relaxed about the screen's accuracy was that checking every flag makes its mistakes
> affordable. **Checking flags cannot see a paper that was never flagged.** The measured miss rate is
> now consistent with anywhere up to a third or a half of the unflagged pile, which is worse than
> the "no worse than 19%" I would have reported had my own reading stood.
>
> **The honest position: option B still saves reading, and it now demonstrably loses papers.**
> Whether that trade is acceptable is yours, and it is the one part of question 1 I should not
> settle by myself twice in one night.

**What is actually finished:** the screen flags three papers, all three have been read, one belonged,
and this pass moved nothing. A full re-sort is not finished until the unflagged pile is sampled or
you accept the unknown.

<details><summary>The question as it was originally filed</summary>

### 1. Should the black-hole-universe papers be re-sorted using an automatic screen, or only by hand?

**The stake.** I built a test that tries to spot "impossibility" papers — ones that prove a whole
class of models *cannot* work, as opposed to papers that simply make no prediction. You approved
adding that category this morning. The test works perfectly on the four papers I designed it
against. Then I ran it across all 29 papers we hold, and **it was right about one and wrong about
three** — it flagged a paper that builds a model rather than forbidding one, and it flagged a
survey paper that is not even part of our collection.

So the category is fine; the automatic sorter for it is not.

**The options.**

- **(a) Hand-sort only.** Every paper that goes into the new category gets read by two independent
  reviewers, the way the one current member did.
  *Cost:* slow — roughly an hour of reviewer time per paper, and there are 29.
  *Benefit:* no wrong filings, which matters because a paper filed here is one we would cite as
  ruling other models out.
- **(b) Use the screen to shortlist, then hand-check the shortlist.**
  *Cost:* the screen misses things it should catch; a paper it skips never gets looked at.
  *Benefit:* cheap, and the hand-check still catches the wrong ones.
- **(c) Improve the screen first, then decide.**
  *Cost:* my time, and last night showed I am not a reliable judge of my own tools — this one
  passed every test I wrote for it and then failed the moment I ran it for real.

**Why it is your call and not mine.** Option (a) spends reviewer time you are paying for. Option
(b) accepts that we will silently miss papers — that is a decision about how complete you want the
collection to be, not a technical one. I can carry out any of the three; I should not choose which
kind of incompleteness we accept.



**THE NUMBER YOU WERE GIVEN WAS WRONG. Re-measured 2026-08-29** (`b25_screen_precision.py`, gated
twice). The screen's score was recorded as "wrong three times out of four". That figure was written
when 29 papers were on the shelf; there are now 41, and **the screen's own output disagrees with its
own summary** — the code flags six papers while the note beside it still says four.

**Three honest figures, and which way each one pushes:**

| measured over | score | favours |
|---|---|---|
| everything on the shelf | right **1 time in 6** | sorting by hand |
| only the papers it would actually be run on | right **1 time in 3** | using the screen |
| counting a paper as a hit if *any* claim in it qualifies | right **2 times in 3** | using the screen |

**And the two friendlier numbers are the less trustworthy ones — I want to say that plainly, because
my first draft led with them.**

- The 1-in-3 comes from dropping the big observational papers. Those are **measurably longer** —
  median 86,000 characters against 50,000. The screen works by *counting words*, so longer documents
  trip it for reasons that have nothing to do with whether they contain an impossibility proof.
  Removing them flatters it.
- The 2-in-3 depends on counting a paper as a hit when one buried argument qualifies. One reviewer
  found such an argument inside a paper the screen flags. **But adopting that convention would change
  how every paper in the collection is filed**, not just this one.

**What nobody has measured: what the screen MISSES.** Every figure above is about its false alarms.
A screen used to re-sort a collection is judged at least as much on what it fails to catch, and
**22 of the 51 papers have never been run through it at all.**

*(Both reviewers also told me this file was not the neutral measurement it claimed to be — it
produces the number your decision turns on, and my framing favoured one side. That correction is
theirs, and the table above is the result of it.)*

**My recommendation: (b).** The screen is bad at precision but there is no evidence yet that it is
bad at recall, and every shortlisted paper still gets read before anything is filed.

---

---

### 4. A paper's prediction is fine. The reasoning behind it is under attack. Does it keep its label?

**The stake.** Smolin's 2004 paper is the one entry in this collection that makes a sharp,
still-open prediction: no neutron star heavier than 2.5 solar masses. We call it a *calibrated
falsifier* — a real number, a real threshold, not yet crossed.

Tonight I found and read the published criticisms of it, which this collection had never held. **None
of them says the number is wrong.** What they say is that the *reasoning that produces the number*
doesn't work — that the argument needs every possible change to the laws of physics to make black
holes rarer, and some changes plainly make them commoner.

**So: is a prediction still a falsifier for a theory, if the theory arguably doesn't produce it?**

**The two reviewers split, and this is the only thing they disagreed about.**

| | says | reasoning |
|---|---|---|
| Reviewer A (Gemini) | **The label must fall.** | A theory can't be credited with a falsifier its own logic doesn't generate. If the reasoning is broken, the prediction isn't the theory's to make, and the label is flattering it. |
| Reviewer B (GPT) | **The label stays.** | The label describes the *shape* of a claim — a number with a threshold — not whether the reasoning behind it is sound. The bar exists and hasn't been crossed. Doubts about the reasoning belong in the notes, not the label. |

**Option 1 — keep it (Reviewer B).** *Costs:* the collection's flagship claim keeps a strong label
while its foundations are publicly disputed, and a reader who only scans labels never learns that.
*Gains:* labels stay a description of claim shape and don't drift into being a quality score.

**Option 2 — drop or downgrade it (Reviewer A).** *Costs:* we would be ruling on a 30-year-old
physics dispute ourselves, on the basis of three papers, one of which is still unread and paywalled.
*Gains:* the label stops implying more than the entry can support.

**Option 3 — add a third column.** We already record *what kind of claim* it is and *whether it has
fired*. This would add *how well-founded the reasoning is*. *Costs:* a third axis to maintain across
58 entries, and it is the most subjective of the three. *Gains:* both reviewers get what they want,
and nothing is hidden.

**NEW EVIDENCE, and it cuts against the side I was leaning toward.** I went looking for whether the
criticism actually reaches the prediction, and found something that sharpens the question rather
than settling it (`b23_which_parameter.py`, gated `PARAM_REFUTED_INFERENCE` /
`PARAM_REFUTED_DEFENCE_INFERENCE`; both reviewers read the paper end to end).

- **The prediction runs through a different quantity than the criticism attacks.** The critics'
  examples are the fine-structure constant and the mass limit for collapse. Smolin's prediction runs
  through the *strange quark mass*. So the criticism does not reach the prediction directly — one
  reviewer was right about that.
- **But the prediction has exactly the shape the criticism attacks.** Smolin's own words: a heavy
  neutron star refutes him because a decrease in that quantity "would lead to a world with a lower
  upper mass limit for neutron stars, and therefore more black holes." That *is* the "changing a
  parameter makes black holes commoner" problem — the other reviewer was right about that.
- **I then argued that this means Smolin answered his critics by making their objection testable, so
  the reasoning is defended after all. Both reviewers refuted that, flatly.** He answers those
  critics in a different section, about something else; he introduces the prediction to answer a
  *different* objection — that his idea isn't testable at all. And making one quantity testable does
  not answer a complaint about *every* quantity. As one put it: **if the critics are right about
  even one of their examples, the theory is already in trouble, and Smolin never addresses it.**
- **Both reviewers also said, independently, that I was smuggling an answer to this very question
  into what I called evidence for it.** They were right. I am recording that here rather than
  quietly dropping it, because it means my recommendation below should be read as a preference and
  not as a finding.
- **One more thing worth your attention:** the prediction depends on a piece of nuclear physics
  (kaon condensation) that Smolin himself says "may be sufficiently inaccurate". If that is wrong,
  a heavy neutron star disproves *that physics*, not his cosmology — which is exactly what this
  collection already records happening to a different entry.

**My recommendation: option 3, then option 1 if you don't want a third column.** The disagreement
is real but it isn't actually about this one paper — it's about whether our labels describe a
claim's *shape* or its *strength*. A third column answers that once instead of per entry.

**Why this is not mine to decide.** Two reviewers, opposite answers, and it changes a tier — every
one of those is a stop condition on its own.

**What is already done regardless:** the three criticisms are acquired and pinned, two fully read
and gated, the findings recorded, and **entry 31's label is untouched**. The fourth (Silk, *Science*
1997) is paywalled — if you can reach it through a university login, that would settle more than
anything else here.

---


</details>

---

## CLOSED 2026-08-29 — question 2

**Duho's instruction, verbatim: "answer question 2".** Returned to me, as with 3 and 4.

**My answer: we say we could not reproduce it. We do NOT call it an error.**

**And the first thing I found looked decisive, and was wrong.** I told you to get the journal
version first, because we held only a preprint. I then found the pinned file headed *"Physics Letters
B* volume 690, pages 73–77, © Elsevier" and concluded we already had the published article. **Both
reviewers refuted that.** It is an automated rendering of the arXiv submission which merely *carries*
that journal line in its front matter, as author manuscripts often do. **We do not hold the published
article, and getting it is still owed.** That is the third question running where my recommendation
rested on a premise that did not survive one check — but this time the check was mine and it was
also wrong.

**What the text does show**, and this survives: the density claim and the mass figure sit in **one
sentence**, with no step between them. The whole inference is the phrase *"from which"*. I first
quantified that as "86 characters"; one reviewer showed the number changes with formatting
conventions, so the invariant statement is the one above. The publisher's abstract repeats the same
assertion, and a published erratum exists — correcting three other equations, not this one.

**Why not call it an error.** Not, as I first argued, because the two options record identical
checkable content — a reviewer showed that is false: "error" claims that *no* admissible route
reaches the number, which is a mathematical claim, not a claim about the author. **The reason is
that our own work refuses to make it.** Six routes were tried; Kerr–Newman geometry, local proper
density, a full interior solution and suppressed order-unity factors were not. **You cannot call
something an error on an enumeration you have declared non-exhaustive.**

**The reviewers now split on what follows, and I am not hiding it.** One holds the cautious wording
is right and stays right. The other holds it understates a demonstrable failure and should be
overturned. **They agree on the next step: obtain the publisher's version of record first.** The
wording stands until that is done.

> **Process note, separated from the reasoning above at a reviewer's insistence.** Five times
> tonight I reached for the reading that an author overstated or erred, and every one was refuted or
> narrowed. That legitimately raises my threshold for making a sixth public accusation. It is **not
> evidence about Popławski's arithmetic** and must not be read as part of the case. Both reviewers
> flagged that I had mixed the two; the correction is theirs.

**What the record now says**, in entry 51's warrant cell: unreproduced from the stated inputs, six
routes tried, none reaches the printed floor, the enumeration is non-exhaustive, the published paper
omits the connecting step. **All of that is checkable. None of it is an accusation.**

**This closes on wording, NOT on provenance.** There IS a further version to fetch, and **I tried
and could not get it**: ScienceDirect returns *403 Forbidden* to automated access
(`S0370269310005691`, DOI `10.1016/j.physletb.2010.04.073`). I did not attempt to work around that.

**So there are now two papers that need your login and nobody else's**, and both bear on the same
entry-31/51 pair:
> - **Popławski**, *Phys. Lett. B* 690, 73–77 — would settle whether the published article contains
>   the step the arXiv text omits, and one reviewer holds that if it does not, "error" becomes the
>   only honest word.
> - **Silk**, *Science* 277, 644 — the last unread criticism of entry 31.

Everything else here is done and checkable. Two things could
still change it, and neither is ours to manufacture: someone finds a route that works — which would
vindicate the paper and we would record it — or a published erratum or critique appears, which would
be someone else's finding to cite.

<details><summary>The question as it was originally filed</summary>

### 2. One published paper's number does not follow from its own inputs. Do we say so in print?

**The stake.** Popławski's 2010 paper is one of only two papers in this collection that makes a
genuinely refutable prediction. It says black holes cannot be lighter than about 10¹⁶ kg, and gets
that from a maximum density it also states. **Working backwards from his own density gives 2.7×10¹⁴
kg — about 37 times smaller.** Both reviewers checked the arithmetic separately and got the same
answer. The paper never shows the step in between, so neither of them could reproduce his figure.

This matters beyond bookkeeping. The size of the number decides how much room the prediction has to
be wrong in: on his figure there are two decades of forbidden territory that observations could
search, on the recomputed one there is less than half a decade, and most of that is already ruled
out. The route is either worth pursuing or nearly closed, depending on which number is right.

**The reviewers disagreed, and this is the only thing they disagreed about.**

| | says | reasoning |
|---|---|---|
| Reviewer A (Gemini) | **Call it an error.** | The arithmetic is simply wrong; he likely dropped a volume factor. |
| Reviewer B (GPT) | **Do not call it an error.** | Every figure in that passage is hedged — "expect", "approximately", "on the order of", "~". Stacked rough estimates can drift this far without anyone making a mistake. |

**Option 1 — write it as an unreproduced step (Reviewer B).** We record that we could not derive
his number from his stated inputs and show our own. *Costs:* if it really is an error, we found it
and declined to say so. *Gains:* we never accuse a published paper on the basis of a step it
doesn't show.

**Option 2 — write it as an arithmetic error (Reviewer A).** *Costs:* a public accusation against a
peer-reviewed paper, resting on an inference about what the author did rather than on anything he
wrote. **I got this exact call wrong once today already** — I accused our own records of carrying an
unsourced uncertainty and the source turned out to exist. *Gains:* if correct, it is the sharper and
more useful finding.

**Option 3 — get the journal version first.** We only hold the preprint. The published Physics
Letters B text may contain the missing step. *Costs:* a delay, and it may not be reachable.
*Gains:* it could settle the question outright instead of us choosing between two guesses.

**NEW EVIDENCE, added the same evening, and both reviewers have now checked it.** `b13_floor_routes.py`
(5/5). `AGATE_B13` = confirmed, `CGATE_B13` = confirmed but narrowed. Both recomputed every number
independently and got the same answers; one of them did it to ten significant figures.

I tried to *find* his number rather than just fail to reproduce it. The paper turns out to define
the quantity both reviewers had been taking at its rounded value, so I could work it out rather
than accept "about". Then I tried **six** different ways of getting from a density to a
smallest-possible black hole, instead of the one way both reviewers had tried — including one a
reviewer suggested and computed itself.

- **None of the six reaches his number.** The closest lands 13 times below it; most are further.
  Neither reviewer could find a seventh that works.
- **Working his density out rather than rounding it makes the mismatch worse** — 37 times becomes
  111. So the gap is not that rounding; rounding runs the other way.
- **The shortfall is three to four factors of ten in density.** "About" and "of order" normally
  cover one, sometimes two. *That last sentence is my reading, not a calculation, and both
  reviewers made me say so.*

**This cuts against my own earlier finding, and I want that on the record.** Under one of the
three candidate figures his floor drops just below the observational window, which would mean the
promising new test I reported this evening does not exist at all. But it is only *just* below —
close enough that a small missing factor would put it back. So: three candidate floors, and they
disagree about whether there is anything to look for.

**What it does NOT do is close this question**, and here both reviewers were firm with me. Ruling
out every route I can think of is not proving none exists; one of them listed four more the paper
allows that I did not try. The paper simply shows nothing between the two numbers. So the choice
below is unchanged — just better informed, and the evidence now leans toward Reviewer A.

**My recommendation: option 3, then option 1 if the journal version does not settle it.**

**Why this is not mine to decide.** It is the difference between reporting what we could not
verify and asserting that someone else made a mistake in print. That is a judgement about how this
programme speaks about other people's work, and it should be yours.

**What is already done regardless of your answer:** nothing downstream waits on this. Both possible
figures are recorded, the route is written up as conditional on which is right, and the paper's
category is unchanged.

---

---

---


</details>

---

## CLOSED 2026-08-30 — question 6

**Duho's instruction, verbatim: "answer question 6."** The fifth question returned to me.

**Ruling: entry 51 keeps CALIBRATED-FALSIFIER / LIVE — as a convention adopted at this ruling.**

**And the basis I first gave you was wrong, caught by the implementation gate.** I claimed your
question-3 outcome was precedent — "when a paper carries a calibrated falsifier, that tier leads."
The reviewer refuted it: **question 3 demonstrated that the standing table can hold claim-level
scope; it never decided priority between a falsifier and an obstruction**, and its own record says
*I* chose that option under your delegation — so "you already decided this shape" overstated the
record twice over, once on content and once on authorship. The outcome survives; the premise did
not. What stands is an explicit new convention, adopted here: *the paper-level label follows the
calibrated-falsifier claim; the proved theorem is a scoped claim in prose and in the table.*

**Not the basis:** Reviewer A's "an empirical falsifier is the higher-information label" —
Reviewer B correctly demolished that; tiers are shapes, not ranks. Nor my filed cost-asymmetry
argument, which was true but weak. Consistency with your prior ruling is the whole basis.

**Applied:** entry 51's prose closes the question with the ruling; its standing-table row now names
the contrast the table had been hiding — **the paper's best-warranted content is the theorem**
(both reviewers verified the derivation) **while the tier-bearing floor is its unreproduced
corollary**; the theorem's precise proven domain was already in the prose.

**And one correction recorded where it counts:** answering 6 does NOT settle 7 — entries 52/53
carry no falsifier, so the question-3 precedent cannot reach them. Question 7's filing now says so.

<details><summary>The question as originally filed</summary>

### 6. A paper that proves an impossibility AND carries your one live falsifier. Which label leads?

**The stake.** Entry 51 (Popławski 2010) is one of your two live calibrated falsifiers. Reading it
for the census showed its **title result is a proven impossibility**: a Dirac field in
Einstein–Cartan gravity cannot be a point, a system of points, or (under stated symmetry) the
singular ring — a real derivation, not a hope. **Both reviewers read the paper in full and agree
the proof is rigorous.** The mass floor your falsifier hangs on is a *corollary* of it.

**So the paper is genuinely two things, and the reviewers split on which one the label should name:**

| | says | reasoning |
|---|---|---|
| Reviewer B (GPT) | **Re-tier to impossibility-proof; keep the falsifier as a secondary claim.** | The no-go is the title, the abstract's first result, and the whole point of the analysis. The tiers describe claim shapes; they are not a ranking where a number beats a theorem. The floor is downstream, heuristic, and currently *unreproduced from the paper's own inputs*. |
| Reviewer A (Gemini) | **Keep calibrated-falsifier; theorem into the notes.** | An empirical falsifier is the higher-information label: it can kill the physical theory with data. The theorem restricts model space; the falsifier tests the world. |

**Option 1 — keep the tier, theorem in the notes** *(already done as common ground — the precise
proven domain is now in the entry either way)*. *Costs:* the standing table's "4 calibrated" keeps
counting a paper whose operative result is a proof. *Gains:* your live-falsifier bookkeeping is
untouched.

**Option 2 — re-tier, floor as secondary.** *Costs:* one of your two LIVE rows leaves the standing
table, and every "two live falsifiers" sentence in the record needs re-deriving. *Gains:* the label
names what the paper actually does.

**Option 3 — allow dual labels for this one paper.** You already answered a shape like this for
entry 44 ("one paper, two claim-level objects"). *Costs:* a schema change. *Gains:* nothing is
suppressed.

**My recommendation: option 1.** Not because Reviewer A's ranking argument is right — Reviewer B is
right that the tiers aren't ordinal — but because the *cost asymmetry* is: option 2 rewrites live
bookkeeping across the record for a labelling gain, and the theorem is now fully recorded either
way. If you ever adopt claim-level labels corpus-wide, this paper is the first candidate.

**What is already done regardless:** the precise proven domain is in the entry (both reviewers
wanted that), the over-broad abstract wording is flagged, and the conjecture is separated from the
theorem. Nothing waits on this.

---




</details>

---

## CLOSED 2026-08-30 — question 7

**Duho's instruction, verbatim: "answer question 7."** The sixth question returned to me.

**Ruling: entries 52 and 53 keep CONSISTENCY-ONLY.** The threshold theorems stay recorded in both
entries' prose, where they already were.

> **CORRECTED BY THE IMPLEMENTATION GATE, disposition unchanged.** My closure below claimed "the
> conclusions decide it the other way" and proposed that below the threshold the universe cycles
> rather than failing to exist. **Both wrong.** The reviewer derived the equations: there are TWO
> thresholds — a small *existence* bound (52: C > √(8/9); 53: C > e^(−1/2), below which the paper
> itself says "the universe would not exist") and a far larger *dark-energy* bound — and the
> cycling I quoted belongs to the second. My quotation spliced the two into one and over-claimed
> that 53 "closes the same way". **The original theorem stands at full strength; the tier ruling
> survives on the honest weighing** — construction-level closing emphasis alongside a prominently
> restated exclusion that delimits the papers' own family. Sixth delegated ruling, and the fourth
> whose stated basis the implementation gate had to correct while the outcome held.

**The premise check that decided it** — the same move as every prior delegated question: the choice
turned on whether the threshold is each paper's *operative result* (the entry-22 shape) or a
*delimitation inside a construction* (the entry-37 shape, where both reviewers refused promotion).
The reviewer proposing re-tier said the exclusion is "highlighted in each abstract and conclusion."
The abstracts I had verified; **the conclusions I had never read. So I read them, and they decide
it the other way:**

> *"…the formation of our Universe corresponds to the moment when C begins to satisfy the
> inequality (33)… **If this threshold is not reached, the closed universe contracts to another
> bounce and starts another cycle**… The last bounce before reaching the threshold can be regarded
> as the Big Bang."* (entry 52; entry 53 closes the same way)

Both papers **end as scenario constructions** — a cyclic closed universe forming inside a black
hole — with the threshold as the scenario's *entry condition*. And below the threshold, **their own
text has the universe cycling, not absent**, which also suggests the "no solution exists below it"
characterisation was too strong; that refinement goes to the implementation gate rather than into
the record on my say-so.

**What this is not:** not a win for the reviewer who confirmed my original all-nine — that
confirmation never engaged the theorem. The basis is the recorded operative-contribution test
applied to newly read evidence, and the theorems lose nothing: they were already claim-level prose
in both entries before this ruling.

<details><summary>The question as originally filed</summary>

### 7. Two more dual papers — construction versus obstruction (it does NOT inherit question 6's answer)

**The stake.** The census closer found that entries 52 and 53 (the Popławski closed-universe pair)
each headline a derived existence exclusion: *"a closed universe exists only when [a function of
scale factor and temperature] exceeds a threshold"* — open and flat universes unrestricted. I missed
it (my pattern had no "exists only when"; eighth miss of that kind); one reviewer found it on a full
read; **I verified it in both abstracts directly.** Like entry 51, these are constructive bounce
papers whose *stated central result* is an impossibility over a class.

**CORRECTION, made when question 6 was ruled:** I told you one ruling would settle 6 and 7
together. **That was wrong.** Question 6 was decided by your question-3 precedent — *when a paper
carries a calibrated falsifier, that tier leads* — and entries 52/53 **carry no falsifier claim**.
Their duality is construction-versus-obstruction, governed by the operative-contribution test (the
entry-37-versus-22 line), a genuinely separate judgement: the threshold theorem is *a* headline
result of each abstract, but each paper also constructs the bounce dynamics it is titled for. **So
this question stands on its own.** Options:** whichever way you rule on entry 51's dual shape (keep tier + theorem in prose, or
re-tier + construction as secondary), applying it to 52/53 keeps the corpus consistent. **The
theorems are already recorded in both entries' prose either way — nothing is lost while you decide.**

---




</details>

---

## CLOSED 2026-08-30 — question 5, and with it the queue

**Duho's instruction, verbatim: "answer question 5."** The seventh and last question returned to me.

**Ruling: entry 5 moves to THEORETICAL-OBSTRUCTION, narrowly scoped.** The corpus's impossibility
tier now has two members — Easson's no-go (entry 22) and this three-page note.

**Why, and why my own filed recommendation was overridden.** I had recommended "leave it," on the
grounds that the reviewers split and the finding survives in prose either way. **That recommendation
predates the convention.** Questions 6 and 7 matured the operative-contribution test into a usable
line: a theorem that *delimits a constructed family* stays with the construction (entries 37, 52,
53); a paper whose *operative result is the exclusion itself* is an obstruction (entry 22). Applying
that line here is not seat-picking — it is the recorded rule on a checked premise:

- **Entry 5 constructs and advocates nothing.** It is a test-note — *"So what if we study Pathria's
  cosmological model from the matching conditions point of view?"* — so there is no constructed
  family for its exclusion to delimit. The entry-37 escape simply does not apply.
- **The test's outcome is the paper's result**, derived on its own pages: smooth shell-free matching
  is excluded for the stated class; the transition *can only* occur through a pressure-bearing null
  shell, pressure computed. Refutable by a smooth counterexample, not by measurement.
- **The objection that this "just describes the junction" is a quality demotion**, and question 4
  fixed that the tiers are shapes, not ranks.

**The narrow scope is printed in the entry** (it is not a no-go against all universe-in-a-black-hole
models), per the same discipline as entry 22's domain note.

**One consequence worth your eye:** entry 5 was *never flagged by the screen* — it surfaced only in
the preregistered random sample. With two known obstructions in the corpus, **the screen's measured
recall — per the implementation gate's wording, the **observed hit rate on the two known, adjudicated obstructions** — stands at one of two; a hit rate on known members, not a corpus-wide recall estimate.** The question-1 record already carries the adverse audit; this
ratifies its first miss at tier level.

**The queue is empty.** Seven questions delegated, seven ruled, every implementation gated — and in
four of the seven the gate corrected my stated basis while the outcome held.

<details><summary>The question as originally filed</summary>

### 5. One paper may be filed under a label that says the opposite of what it does

*(Filed as three papers; the reviewers cut it to one. What they agreed on is already applied.)*

**The stake.** Entry 5 (Khakshournia 2010) is filed as *consistency-only* — which in this collection
means "shows nothing is contradicted, and says nothing about what cannot happen." Its central result
is that a certain join between an expanding universe and a black-hole exterior **cannot be smooth**;
it requires a shell carrying pressure.

**How it surfaced:** not by looking. It came out of the random sample drawn to measure what the
automatic screen misses.

**The reviewers split, and only on this one.**

| | says | reasoning |
|---|---|---|
| Reviewer B (GPT) | **Move it.** | Testing whether the join can be smooth *is* the paper's job, and its answer is no. The domain is narrow, but narrowness belongs in the note, not the label. |
| Reviewer A (Gemini) | **Leave it.** | Working out that a join needs a shell is describing the join, not proving a model impossible. That is ordinary constructive physics. |

**Option 1 — move it, with the narrow scope printed.** *Costs:* a label that says "proves an
impossibility" attached to a three-page note about one configuration. *Gains:* the label stops
saying the reverse of the paper's finding.

**Option 2 — leave it, and record the finding in the note.** *Costs:* the collection keeps a paper
whose result is an impossibility in the drawer marked "says nothing about impossibilities."
*Gains:* no re-tiering on a split verdict, and the finding is still written down.

**My recommendation: option 2 for now.** The reviewers disagree, the paper is narrow, and the
information survives either way — which is not true of most tier questions.

**What both reviewers agreed, and is already applied:**
- **Entry 37 stays put.** Its "if and only if" theorem is a real exclusion *inside* a construction,
  not the paper's purpose. Promoting it would let any uniqueness theorem be relabelled by negating
  it. **The theorem is now written into its entry so it isn't lost.**
- **Entry 49 stays put**, under a new rule both proposed independently: **a paper earns the
  "proves an impossibility" label only if it does the proving.** Citing someone else's theorem
  doesn't transfer it. Otherwise one theorem turns every paper that cites it into an obstruction.
- **The real target is entry 48** — Farhi & Guth, *"An obstacle to creating a universe in the
  laboratory"* — which is where entry 49 sends the proof. **Nobody has ever read it.**

**And I could not get it.** ScienceDirect returns 403; there is no free scan. **That is now three
papers behind the same paywalls, and all three matter:** Popławski *PLB* 690, Silk *Science* 277,
and now Farhi & Guth *PLB* 183. Any one of them would settle something currently open.

**[SUPERSEDED 2026-08-30, later the same day — do not re-read the paragraph above as live status:**
two of those three papers were obtained *after* it was written. **Farhi & Guth *PLB* 183 → entry
48**, acquired via the KEK preprint scan (KEKSCAN 2000-36-705), READ IN FULL and double-gated
(`b45` / `AGATE_B45` + `CGATE_B45`), tiered THEORETICAL-OBSTRUCTION under question 8 (closed above).
**Popławski *PLB* 690 → entry 51**, version-of-record + 2013 erratum acquired and compared. Only
**Silk *Science* 277** is still behind a wall (free with a registration that is yours to make). The
"nobody has ever read it / I could not get it" wording was true when this section was written; it
is not true now. Recorded to stop a stale "go read Farhi & Guth" pointer from recurring.]**

---


</details>
