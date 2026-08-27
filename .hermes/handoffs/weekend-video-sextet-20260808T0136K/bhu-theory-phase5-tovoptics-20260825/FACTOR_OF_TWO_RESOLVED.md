# The "factor of two" is not a factor — the two nulls belong to two different models
(2026-08-27. Diagnosis by reading platoon/gpt1_blind_p7/p7_blind_dipole.py, after three
numerical hypotheses were eliminated.)

## Three hypotheses, tested and eliminated

1. **Adiabatic exponent.** Theirs is `power = w/(1+w)` (p7_blind_dipole.py:100) — identical to
   mine. Eliminated.
2. **A constant scale factor.** For my null to move to theirs, my epoch-variation term would
   need scaling by 1.466 — not 2, and not any clean convention number. Eliminated.
3. **A sub-term identification.** Freezing opacity and depth-redshift at the centre and letting
   only the source vary gives −0.183 at their root, not the −0.615 cancellation requires.
   Eliminated.

## What the code actually says

**Their P7 does not integrate an exterior profile at all.** It builds the coefficient from
(a) the junction Doppler factor and (b) the shock-side source temperature, integrated
adiabatically **along the crossing epoch** — `d ln T/d η = w/(1+w) · d ln ρ̄/d η`, using the
orbit's ρ̄(η) directly. There is no radial integration, no optical depth, and no depth-redshift
in it.

So the two calculations are **two different physical models**:

| | theirs | mine |
|---|---|---|
| emission from | the shock surface only | the whole exterior column |
| opacity | absent | computed, varies with closure |
| depth redshift | absent | computed from the metric function |
| w enters through | the source's epoch-variation only | opacity, profile, depth-redshift AND source |

Theirs is the **surface-emission (optically thick) limit**. Mine is the **full transfer**.

## The resolution, and why it is not reassuring

Neither is wrong. Each finds the cancellation *of its own model*, and the cancellation is real
in both — which is why the phenomenon survived doubling and should be believed.

But it means **the null's location is model-dependent**, and that is a worse situation than a
convention factor would have been. A convention factor is bookkeeping. A model-dependent null
means the *set of closures that cannot be constrained* moves when the treatment changes, so we
cannot yet say which physical situations escape the test — only that some do.

## What this does and does not change

- **Unchanged:** the headline of the stakes document. The model can produce no signal at all
  without being wrong — established now in two independent treatments, which is stronger
  evidence for the phenomenon than a single one at an agreed location would have been.
- **Unchanged:** that nothing reaches us from beyond the wall, and that the wall's own glow is
  all we could see. Both treatments agree.
- **Changed:** any statement of the form "the exclusion fails at w = X" is not available. I have
  withdrawn the location from the record; only the existence stands.
- **Owed:** a limiting-case check — my full transfer should reduce to their surface model as the
  exterior becomes optically thick. If it does, the two are nested rather than rival and the
  physical null is mine (theirs being its thick limit). If it does not, one of us has an error
  that this whole diagnosis has not reached. **That test is the next thing to run**, and it is
  the kind that either closes the question or reopens it properly.
