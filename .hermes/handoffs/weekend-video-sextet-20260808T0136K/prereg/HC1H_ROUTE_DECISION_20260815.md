# HC-1H route decision — full 850, no pilot

**Decided:** 2026-08-15 KST by Duho.
**Choice:** the **full HC-1H design (850 labels)**. The optional §2b pilot is **not** taken.

## What this fixes

- 500 real accepted-sample images; 200 blind synthetic ground-truth injections; 150 mirrored
  re-presentations. Sessions capped at 50 images. One checker (Duho).
- Nine strata = machine-committee state x |chi| tertile, Neyman allocation, floor 30 real per stratum.
- `a` is the one-human synthetic-error-corrected estimate: `a_s = (a_hat_s - eps_hat_s)/(1 - 2 eps_hat_s)`,
  global `eps_hat` from the 200 synthetics, sigma_a by the shared-epsilon summed-derivative form.
- HC-5 floors: `a_LB >= 0.85` quality floor and `a_LB >= a_gate(N)`; `a_gate = 0.7905` at N = 130,076.
- HC-7 integrity triggers bind, including clause (v), synthetic/repeat identity exposure.

## What the pilot would have bought, and is now forgone

An intermediate checkpoint after 150 labels returning only PASS-TO-FULL-HC1H or INCONCLUSIVE. Taking
the full route means a harness or image-quality problem surfaces partway through the long commitment
rather than after a short one. The §2b carry-forward and selection-bias exclusion rules are therefore
inoperative — no pilot labels exist to carry forward.

## What this decision does NOT authorise

The hand-check **cannot start**. HC-1H samples from the *accepted* population, which does not yet
exist: no real cutout has been fetched and nothing has been classified. Acquisition and classification
must run first, and that is the **STOP-rule crossing** — still unauthorised.

No real-sky statistic exists anywhere in this program. K-8 remains untripped.
