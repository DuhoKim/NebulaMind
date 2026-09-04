# K5 limb A — blind seat brief (the amplitude question, before any acquisition or compute)

**Authority:** Duho, "K3 step 3, K5, K6 in order", relayed 2026-09-04 14:56 KST; "go ahead" 2026-09-04.
**Governing document:** `K5_LISA_FORECAST_PREREG_20260904.md` (frozen V2) — read it in full first; it binds you.

**BLIND.** Do NOT open, list, grep or infer any file whose name contains `K5_limbA`, `K5_LIMBA`, `K5_ROUTE2`,
`K5_RESULT`, `K5_CHECK` or `K5_RECONCIL`. You MAY read the prereg, `PROGRAM_A_FREEDOM_MAP_20260902.md`,
`WARRANT_TABLE_20260903.md`, and the source `../bhu-reading-20260823/sources/2203.13295_clean.txt` ("entry 21").

**DO NOT FETCH ANYTHING.** No network, no LISA sensitivity product, no external data. Limb A is decided before any
acquisition. A seat that fetches fails the run.

## The single question — prereg §1 limb A

**Does entry 21's construction FIX the ringdown strain amplitude, or does a free normalisation survive?**

The prereg's test is mechanical, and it is the whole of your task:

> "To pass limb A, the seat must write down the exact mathematical derivation fixing the amplitude strictly from the
> model's pinned parameters without introducing new free variables; if it cannot, it must conclude the amplitude is
> free."

The pinned parameter set is **`(M, α, distance)`** and nothing else.

## What your script must do

1. **State the chain** from entry 21's model to an observable strain: what quantities must be known, in order, to get
   from the static equilibrium (Eqs. 4–7, **L245**) to a strain `h(t)` at a detector. Print it as an explicit list.
2. **For each link in that chain, state whether entry 21 supplies it**, with a source line if it does. Distinguish
   sharply between three things, and label each link with which it is:
   - **DERIVED** — entry 21 computes it;
   - **DERIVABLE** — not computed there, but fixed in principle by the pinned parameters (say how);
   - **FREE** — requires an input the construction does not contain (say exactly what input).
3. **Attempt the derivation.** Try to express the ringdown strain amplitude in terms of `(M, α, distance)` alone.
   Either complete it — in which case print it and limb A passes — or reach the point where a new independent variable
   must be introduced, **print that variable and what it depends on**, and stop.
4. **Do not conflate two different statements.** "Entry 21 does not compute the excitation factors" (which it says
   outright at **L400**) is NOT the same as "the construction does not fix them". Address them separately and say
   which of the two your conclusion rests on. **This is the specific error the prereg names.**
5. **Consider the standard escape and rule on it:** in general relativity a ringdown amplitude is often set by
   calibrating the radiated-energy fraction against numerical-relativity merger simulations. State whether such a
   calibration exists for *this* model, and whether importing the general-relativity value would be a derivation from
   the construction or an added assumption. Be explicit.
6. **Print the control code** `C5_AMPLITUDE_PROVENANCE=PASS` or `=FAIL`, per the prereg's operational definition, and
   list by name the controls you did NOT run as `NOT RUN`, not as passes. Limb A does not reach C1, C2, C3 or C4.

## Deliverables — exactly two files, nothing else changed

1. `K5_limbA_<seat>.py` — self-contained, runs under `python3`, prints every claim it makes. **Run it.**
2. `K5_LIMBA_<seat>_RESULT.md` — first line exactly one of:
   `LIMBA_AMPLITUDE_FIXED` · `LIMBA_AMPLITUDE_FREE` · `LIMBA_UNDETERMINED`
   and nothing else on that line.

## Rules

- **Do not manufacture an amplitude, an efficiency, or a normalisation.** If one is needed and not supplied, that is
  the finding.
- Every numeral traces to a source line you cite or to something your script printed.
- You have no authority over any tier, warrant token, standing or stamp.

K5_LIMBA_SEAT_BRIEF_COMPLETE
