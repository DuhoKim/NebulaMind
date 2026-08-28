# Resume here — Tori, BHU lane, written 2026-08-28 before a Studio reboot

Read this first. You are me with none of today in memory. Everything below is on disk and
pushed; nothing important lives only in the lost conversation.

**Branch `feat/paper-workflow-v2`, remote tip `ae378af63`, 0 unpushed. All work committed.**

---

## Where you are

Phase 6 (BHU curvature) is **closed, no open items**. A corpus sweep ran after it and is
**complete but its result is mostly negative** — read the next section before acting on it.

Today's chain, newest last:
`85f9d4547` phase 6 opened · `d4d52dbec` C3 χ_* provenance · `c2f87865e` ACT v1 closed ·
`4285826e3` entry 7 audit · `dd35ecc8e` the sweep · `ae378af63` entry 51 + tally note.

---

## THE ONE THING A FRESH CONTEXT WOULD GET WRONG

**The blind re-classification sweep FAILED ITS OWN CONTROL.** Do not treat its output as findings.

Three entries with known gated answers were seeded blind. 6 and 31 passed. **54 FAILED** — the
seat returned CALIBRATED-FALSIFIER quoting the abstract's bracket, which is exactly the error
our record made and two seats corrected that morning. A single-pass blind read reproduces the
overclaim bias, because it is structurally the same method that built the bibliography.

Consequence: the sweep's **six disagreements are all promotions, same direction as the control
failure.** One (entry 51) survived two adversarial gates and is now applied. **The other five —
entries 36, 37, 38, 40, 41 — are UNEXAMINED AND SUSPECT.**

**My recommendation, which I was about to put to Duho when the reboot was called:** record those
five as *blind-flagged, not adjudicated*, and do **not** gate them. They came from the engine
that promoted 5 of 10 (the other promoted 1 of 5 and twice found numbers and declined). Gating
five candidates from an instrument shown to be biased in that exact direction likely costs five
rounds and returns noise. A better-designed sweep can revisit them cheaply now that
`ENTRY_SOURCE_MAP.md` exists. **This is a recommendation, not a decision — Duho had not ruled.**

---

## State of the falsifier tier (this is now written into the bibliography, don't re-derive it)

`bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md`, sha256 `aeee16222e647c2b`.
Pre-edit archived beside it: `_archive_pre_entry51_20260828T1734.md`, sha256 `fbd2a8ab023d9e74`.

Tally **3 CALIBRATED-FALSIFIER / 8 QUALITATIVE-DIRECTIONAL / 3 PROSPECT / 33 CONSISTENCY-ONLY /
4 UNREAD** = 51, verified against the file's own Testability lines.

| entry | standing | fires |
|---|---|---|
| 7 | FIRED | Brown–Bethe instrument chain, **not CNS** (source gives CNS only "serious obstacle") |
| 31 | LIVE, 1.36σ short | CNS at Smolin's 2.5 M☉; 2.35 ± 0.11 observed; drifting **away** as errors tighten |
| 51 | LIVE, unfired | four-dimensional ECKS chain via the LHC route; **not a direct BHU falsifier** |

**3 calibrated, 2 live, but only ONE (entry 31) bears directly on a black-hole-universe theory.**
I mis-stated this tally twice in one day in opposite directions; the standing note in the
bibliography exists to stop that recurring. Do not quote a bare "N live falsifiers".

---

## Things you would not infer

- **I edited the bibliography myself**, on Duho's instruction, because Blanc was writing an
  abstract. It is normally Blanc's single-writer artifact. The rule call separating tier count
  from live count is **mine and no gate settled it** — if Blanc reads it differently it is a
  sentence, not a structure.
- **Fable-to-Fable messages do not round-trip.** Blanc's questions arrive via Duho's
  conversation and replies do not return. **File to disk; do not answer inline.** This cost a
  full day on the model-ID question (now closed: all three coordinators `claude-opus-5[1m]`,
  each self-reported, `042102efa`).
- **The bibliography records DOIs, not arXiv IDs**, so nothing links an entry to its source by
  string search. `ENTRY_SOURCE_MAP.md` is the join, sha-pinned. Keep it or the next sweep
  rebuilds it.
- **The branch is shared with Hwao.** A push sends their commits too, and the tip moves under
  you mid-command. Always `git fetch` *then* count.
- **`s1_falsifier_screen.py` does not work** and says so in its own footer. Segmentation
  collapses on `###` text and OCR mangles `2.5` to `2:5`. Do not resurrect it without fixing
  both.
- Hwao is building a **blind-by-construction** mirror test in the DESI lane (`89021789f`). Their
  blindness is structural where mine relied on a seat not looking something up. Worth comparing
  — I have a concrete failure mode to hand them.

---

## Next action, concretely

Put the five suspect promotions to Duho as a recommendation (record as blind-flagged, don't
gate). If he overrules, gate entries 36/37/38/40/41 two seats each on **different engines**, and
brief them that the proposing engine over-promoted 5 of 10.

Nothing is running. No seats dispatched. Nothing to wait for.
