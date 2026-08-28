# KUN RECORD GATE

Timestamp: 2026-08-12 KST

Target: `paper/RECORD_SPIN_PROGRAM_20260812.md`

Standard applied: durable internal record, not submission draft.

## Verdict

PASS AS A RECORD, WITH THREE REQUIRED WORDING REPAIRS BEFORE IT BECOMES THE DURABLE COPY.

I found no hidden empirical spin-anisotropy result and no adjudication of Longo, Shamir, or BHU. The record is substantially trustworthy as a future-use map: it captures the closures, the open yield gate, the instrument receipts, and the "do not repeat" lessons. The technical numbers I spot-checked mostly match the receipts.

The required repairs are about operational status, not scientific overclaim. A future reader must not infer that the instrument or preregistration has been cleared for sky use.

## 1. Result Claim Safety

PASS.

The record repeatedly says no result is claimed, no sky run happened, no Longo/Shamir adjudication exists, no BHU claim exists, and nothing is published/submitted/uploaded. The fast-answers table also says the empirical run is blocked at the accepted-yield count and that real catalogue rows require separate authorization.

I do not find a sentence that would have to change when a future measurement lands because it already implies that measurement. The record is about the program state, not the universe.

Required wording repair:

Current fast answer:

> "Can I use the instrument? Yes, with its receipts..."

This is too operationally permissive for a future reader. Replace with:

> "Can I use the instrument? Yes as the frozen synthetic-trained candidate instrument for preregistration work, with its receipts (§2). Do not run it on real galaxy images until the preregistration is frozen and separately authorized; do not retrain or re-calibrate without re-running the receipt suite; do not touch τ after any sky data."

That keeps the useful answer while preserving the no-sky-run boundary.

## 2. Number Spot-Checks

PASS WITH ONE CAVEAT.

Checked against local receipts:

- `96.44%` central retention and `96.15%` one-sided lower 95%: matches `prereg/train_results.json` (`0.964416...`, `0.961528...`) and `prereg/YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md`.
- `τ = 4.4006456017494235`: matches `prereg/train_results.json`.
- production weights hash `83008c1c...49e6d` and canonical hash `1075a4d9...7a589`: match `prereg/train_results.json` and `shasum` for `prereg/weights_frozen.pt`.
- retained production S/N bins and 100% accepted-sign accuracy: match `prereg/train_results.json`.
- interpolating-mirror identity violation `0.058-0.944`: matches Yui spike receipt / runner output.
- deterministic-tracer recalibration on 8,000 nulls: `τ = 5.916292...`, retention `0.13%` central and `0.089%` lower 95%, S/N inversion: matches `prereg/receipt_results.json`.
- V1 power failure: `8.0%` power at `A=0.02`, `N=30,000`, `p<0.001`: matches `spike/GORU_STATS_RECOVERY_TEST_20260812.md`.
- 240-vs-8,000 null calibration lesson: matches Yui spike setup and later production receipt.
- `-99` photo-z sentinel: matches `prereg/TORI_SURVEY_ROUTE_BINDING_20260812.md`.
- Goru yield receipt SHA in the record `df08a525...`: matches local `prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`.

Caveat: the record quotes several long hashes with ellipses. That is fine for prose, but the file index should point to the hash-bearing receipts. It currently does. No blocker.

## 3. Section 6 Lessons

PASS WITH ONE TIGHTENING.

The ten "do not repeat" items are mostly correctly scoped.

Item 4:

> "Human labels, or ML trained on human chirality labels, as the anisotropy instrument..."

This is correct for a result-bearing spin-anisotropy instrument of this kind. It is too broad only if read as banning human labels from calibration, bias-transfer studies, or hand-check attenuation. Repair:

> "Human labels, or ML trained on human chirality labels, as the result-bearing spin-anisotropy instrument. Human labels remain admissible only for blinded attenuation checks or explicit bias-transfer studies."

Item 9:

> "Claiming any spin result says anything about BHU..."

This is correctly scoped by the following phrase: "until the literature changes (a published, calibrated, BHU-specific prediction would be the change)." It matches my BHU closure boundary: no calibrated BHU-specific sky-statistics target exists now; that is not the same as BHU being untestable in principle. No repair required.

Item 5 and the §2 identity paragraph carry the old "training defects cost sensitivity, never validity" language. In §2 it is bounded to the identity, but for safety replace:

> "training defects cost sensitivity, never validity"

with:

> "constant chirality-calibration defects in the wrapped estimator cost sensitivity; validity still depends on the pixel-path, sample-selection, and monopole-gradient controls below."

This prevents a future reader from over-extending the identity to all possible trained-model failures.

## 4. Route Unlock Conditions

PASS.

The route ledger is honest:

- GZ1 unlock condition is the real one: documented frame convention from Galaxy Zoo.
- BHU route correctly says the current closure changes only if the literature supplies a published calibrated BHU-specific prediction.
- Quaia/Mittal-Singal closure is correctly tied to Duho's "move on" plus the methods note's stated reconstruction requirements.
- 4PCF is parked, not falsely closed; it names the four preconditions before revival.
- Longo route is live and blocked at accepted yield, not claimed as a result.

The conditions do not appear written to make closures tidier than they were.

## 5. Seat Attribution

PASS.

The attribution is accurate at record level. It credits Duho for direction, boundaries, and narrowing; names Hwao as coordinator; and records that two of the three §3 failure modes came from re-measuring our own earlier work rather than auditing others. That last point is important and correctly included.

## 6. Remaining VERIFY Items

Safe to rely on now:

- No result exists.
- The BHU route is closed for current sky-statistics work because no calibrated BHU-specific target exists in the cited literature.
- V1 class-floor design died on power/yield.
- V2 Longo-amplitude route is the live design path but is blocked at accepted-yield / freeze.
- Pixel-path parity, resampling mirrors, and thin-null calibration are real failure modes with receipt-backed numbers.
- The production synthetic-trained instrument has receipt-backed synthetic retention and identity tests, but not authorization for real-image use.

Still carries `[VERIFY]` or open status:

- exact receipt line for the raw-vs-dereddened flag;
- GZ1 paired-flip object count before external use;
- Shamir 2012 implied amplitude class;
- trailing-arm universality citation in the filament assessment;
- real DR10.1 accepted-yield counts;
- real-image retention/acceptance and WCS pass rate.

## Plain Verdict For Duho

This is trustworthy as the durable internal record after the three wording repairs above.

It is safe for a future reader to rely on it as a map of what closed, what remains live, why no result exists, and which receipts contain the controlling numbers. It is not safe to treat it as a paper, a frozen preregistration, or permission to run the instrument on real galaxies.

No publication, submission, upload, sky run, video release, or acceptance is authorized by this record.
