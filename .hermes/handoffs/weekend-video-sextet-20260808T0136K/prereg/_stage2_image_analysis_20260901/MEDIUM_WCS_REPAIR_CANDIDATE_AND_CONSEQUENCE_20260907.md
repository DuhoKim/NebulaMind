# MEDIUM-WCS-LOSSY — prepared repair candidate and the prospective decision it needs
2026-09-07 22:26 KST / 13:26Z. HWAO. **Preparation only. Nothing adopted, nothing run, nothing retried.**
The candidate lives entirely at `/Users/duhokim/work/Trio/wcs-repair-candidate-20260907/`. No adopted
source, CORE/runtime pin, original input or journal was modified; verified after the work: run path
`1c4f96fb…`, producer `ea46478e…`, both test modules and `OUT_A1_REPAIRED/tuning.abort.json`
(`a0ea7e7d…`) unchanged. The aborted run stays ABORT and its exposed 400 tuning labels stay recorded.

## 1. What was actually wrong, established from the exposed headers alone
`_medium_wcs` reduces a header WCS to a fixed numeric schema, then requires the rebuild to compare
equal to the original at `tolerance=0.0`. A bare TAN rebuild defaults to **ICRS / undefined equinox /
dateref `1858-11-17`**; every DR9 tuning header states **FK5 / equinox 2000 / dateref `''`**. The schema
had nowhere to put that, so on real survey data the comparison could never pass.
My own probe over 25 Wcsprm fields on all 398 exposed headers finds **exactly three differing fields
and no others**, identically in all 398: `radesys`, `equinox`, `dateref`. Carrying the numeric `mjdref`
instead of the `dateref` string **does not work** — `mjdref` is already `[0.0, 0.0]` on both sides and
the comparison sees the strings themselves. That is why the schema must carry a string, and why the
string is checked against a closed form instead of being accepted as header text.

**Correction to my 21:47 note.** I listed three options as if equally sound. They are not. Narrowing
the comparison would be answering a problem nothing required — no field needed ignoring. Recording the
affected identities as RENDER-REFUSED/UNSCORED would recategorise an integrity failure as ordinary
missing data and quietly walk past the stop. Preserving the frame state is the only option that fixes
the actual defect, and it needs no tolerance change.

## 2. The candidate (4 files, no gate weakened)
`run_path.py` extracts the three fields from the normalized original, **refuses** anything outside a
closed frame list or a bare ISO-8601 instant (`MEDIUM-WCS-UNSUPPORTED`), and sets them on the rebuild
before comparing. **The comparison line is unchanged byte for byte** — still `tolerance=0.0`, still no
ignored fields. `medium_perturbation.py` takes the three into its fixed schema, validates them
independently inside the producer (`CLOSED-FRAME-STATE-REQUIRED`), and applies them to the
reconstructed transform; the validation is structural, with **no new import**, so the producer's pinned
import set is untouched. The two test modules move their fixtures to the frame state a bare rebuild
already had, so synthetic behaviour is unchanged.

Evidence, all header-only or synthetic — no pixel scored, no label read, no stage replayed:
* adopted code on the 398 exposed headers: **398/398 REFUSED `MEDIUM-WCS-LOSSY`** — the abort reproduced;
* candidate code, same 398: **398/398 accepted, `compare(tolerance=0.0)` True**, frame FK5/2000.0/`''`;
* original vs reconstructed transform, 25 grid points × 398: **bit-identical both directions**;
* `test_medium_perturbation` 32 → **40 OK**, `test_core_consumer` 32 → **35 OK**, `test_run_path` 42 OK,
  `test_evidence_gate` 5 OK; old fixtures against candidate code refuse — the two files move together;
* synthetic scientific output identical to the last digit across trees (`kept_chi=0.9118412137031555`,
  `replaced_chi=-0.38820579648017883`);
* refusals still fire on an unlisted frame, free-form or non-ASCII-digit date, string/NaN equinox,
  missing or extra WCS key, **and on state the schema still cannot carry** — a non-default `lonpole`
  still raises `MEDIUM-WCS-LOSSY`. The 398 headers are evidence, not an identity-specific exemption.

Candidate digests: `e144c0e0…` run path, `59117053…` producer, `a30a1f39…` and `983acf82…` tests.
Two couplings surfaced: the producer's bytes are pinned by a **code constant in `run_path.py`** and by
the **CORE manifest entry**, so the repair cannot be adopted without a new CORE manifest.

## 3. The consequence — and it is not "apply the fix and continue"
A1 line 125 governs. The run has begun (input anchored, round designated, planes accessed), so it
"stays bound to its recorded V15/A1/C/W identities", and "if it cannot continue under those bindings,
stop and record abandonment or invalidity under its governing rules". The repair changes the producer
bytes, hence C. `_start` requires `prev["C"] == self.C` (`C-BINDING`, run_path.py:595), so under a new
manifest the existing draw **mechanically cannot be the predecessor of a tuning stage**. A later
amendment "applies prospectively only to a run not yet begun". The repaired code therefore cannot
rescue this run under any reading — the fix is real, and this run is still over.

**What a decision would have to settle, before anything runs:**
1. **Adoption of the repaired bytes** after focused changed-byte review, plus a new CORE manifest C′
   carrying the new producer digest and the re-pinned constant.
2. **Disposition of the begun run** — recorded abandonment or invalidity under its own bindings. Its
   exposure inventory is checkable and small: 400 tuning identities **with their labels** exposed;
   200 holdout and 2,000 validation identities exposed as catalogue IDs only, which A1 line 92 states
   is not opening; **no configuration scored, no objective, no winner** — there is no `tuning.json`, so
   no selection information exists to leak.
3. **The exclusion decision, preregistered before any new designation**: the 400 label-exposed
   identities must not silently become members of a new holdout or validation set. Excluding them
   changes the eligible population, so the exclusion list becomes a pinned selection input inside C′
   and has to be fixed before the seed round is designated, not after.
4. **A fresh prospective start** — new input freeze and anchor, new drand round (6440756, 6444980 and
   now 6445084 are spent), new draw.
5. **The attempt count.** A1 grants this run exactly one further validation attempt. Whether a new run
   under an amendment begins with a fresh attempt or inherits the expended state is **not mine to
   assert**, and I make no claim either way. It is the one question here that is genuinely the owner's.

Holdout and validation labels remain unopened. No new draw, anchor, designation, review worker or
production edit was made in preparing this. Full package and evidence:
`/Users/duhokim/work/Trio/wcs-repair-candidate-20260907/CANDIDATE_SUMMARY_20260907.md`.
