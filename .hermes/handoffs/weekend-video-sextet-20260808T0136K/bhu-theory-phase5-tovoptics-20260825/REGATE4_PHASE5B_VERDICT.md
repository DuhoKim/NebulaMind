HOLD_NULL_EXISTENCE_AND_FLATNESS_UNSUPPORTED

# REGATE4 Phase 5b verdict

## Ruling

Phase 5b does not pass in its reduced form.

The epoch ruling removes not only both quoted null locations but also the claimed model-level existence of a null. The two calculations establish that two added, incompatible thermal closures each happen to generate a cancellation. They do not establish that the pinned geometry generates one. Once the temperature/source field is admitted to be unpinned, its epoch derivative is free data at the crossing; that derivative is one of the two terms whose equality defines the null. An admissible closure with constant surface brightness across the sampled crossing events leaves the positive kinematic coefficient (the reproduced Doppler term is +0.615301) and has no cancellation. Other source gradients can move, create, or remove a root. Thus “a silent configuration exists” is not a prediction of the pinned model.

The safe surviving statement is narrower: this proposed observational test is underdetermined until thermodynamic/radiative closure is added. The existing calculations provide examples of closure-dependent cancellations, not a closure-independent silent configuration.

Claim 5 also fails. The reported 0.11% change is a change in a ratio close to one; the anisotropy is encoded in the small residual `1-R`, not in `R` itself. Re-execution gives `R=0.997726210` at K=0.01 and `R=0.998857603` at K=100. While R changes by only 0.1134%, `1-R` falls from 0.002273790 to 0.001142397, a 49.76% change. Directly projecting the same implementation gives a signed normalized coefficient changing from -0.522912 to +0.043763 over those four decades, including a sign change. It is therefore false that opacity “turns amplitude only” at the precision relevant to the dipole. The blind implementation’s approximately 1.51% coefficient drift over eight decades is not quantitatively explained by that 0.11% headline comparison.

These are binding defects, not nits.

## Claim-by-claim adjudication

### 1. No transmitted background beyond the boundary — CONDITIONAL PASS, scope must be narrowed

For the pinned comoving exterior and a regular finite emitter-frame intensity, the horizon suppression survives the non-radial extension. Near `N-1 -> 0`, finite angular momentum contributes only subleading terms to the null propagation, while the comoving frequency ratio retains the `g ~ sqrt(N-1)` scaling; Liouville then gives bolometric weight `g^4 ~ (N-1)^2 -> 0`. The causal statement that a true event horizon cannot transmit a signal from its forbidden side is not radial-ray-specific.

The receipt does not justify the unrestricted phrase “for a source that is not comoving.” In general `g=(-k.u_rec)/(-k.u_emit)` depends on the emitter four-velocity. A finite-boost, regular source preserves the limiting suppression, but an arbitrary non-comoving source or singular emissivity was neither derived nor bounded. The defensible claim is therefore limited to regular sources with finite local intensity and finite relative boost, plus the causal no-crossing statement for the horizon itself.

### 2. Invariant optical-depth element — PASS in its stated comoving-fluid scope

Starting from the invariant element

`d tau = sigma n_e (-u.k) d lambda`,

with comoving `u^rbar = sqrt(N-1)` and `g_rbar_rbar = -1/(N-1)`, one has

`-u.k = k^rbar/sqrt(N-1)`

up to the orientation sign. Since `d lambda = d rbar/k^rbar`, the trajectory factor cancels:

`d tau = sigma n_e |d rbar|/sqrt(N-1)`.

No radial-null condition was used in that cancellation. Angular components of `k` do not enter because the comoving fluid has no angular component. The result therefore holds for non-radial rays as long as `rbar` is monotone on the segment and the absorber is the pinned comoving fluid. It would not hold unchanged for a non-comoving absorber.

The numerical junction-closure value also reproduced: p1c gave 0.132085 and p6 gave 0.1321.

### 3. `beta_rel = -1/sqrt(N)` — CARRIED PASS

This analytic law was explicitly outside the reopened dispute and no current artifact supplied a contrary result.

### 4. A cancellation exists as a model prediction — FAIL

Both roots are outputs of closures the epoch ruling invalidated for generic w:

- p7/current p6 inherits a blackbody junction anchor `T_s proportional rhobar_s^(1/4)` and an adiabatic depth law;
- the blind p7 seat carries one normalization as `T proportional rhobar^[w/(1+w)]` across distinct crossing events.

Reproducing roots under both assumptions proves robustness only within those two assumed maps. It cannot establish a universal root over the unrestricted set of positive source fields. The cancellation condition is a condition on an unpinned source derivative. A constant-across-epoch surface source is an explicit counterexample: its source-gradient term vanishes and the reproduced kinematic coefficient remains +0.615301 rather than crossing zero.

Therefore the phase may say “the two tested closures each contain a cancellation at different locations.” It may not say “the pinned model contains a silent configuration whose location alone is unknown.” Both existence and location are closure-dependent.

### 5. Flatness-gap closure — FAIL

The amplitude does divide out of a sky-mean-normalized dipole, but the measured shape is not flat at the anisotropy scale. The relevant residual changes by about 50%, and direct projection of the same calculation changes the coefficient by 0.566675 and reverses its sign. The claimed comparison used the percent change of a near-unity ratio, which suppresses the quantity being diagnosed.

The two implementations may still differ because their opacity knobs and thermal closures differ, but `FLATNESS_GAP_CLOSED.md` does not quantitatively close that gap.

## Thermal-closure scope audit

The withdrawal is not fully propagated through the executable/current receipt chain:

- `p6_path_transfer.py:84-91` still states that the source temperature is fixed by A6 w, applies the adiabatic depth exponent, and blackbody-anchors the junction.
- `p7_signed_sweep.py` executes that p6 prefix and therefore inherits the same source construction.
- `p8_thick_limit.py` executes the same prefix and varies opacity around the same invalidated epoch/source construction.
- `FLATNESS_GAP_CLOSED.md:37-44` still describes w as moving “the source law” and calls the two behaviours “the same physics,” despite the epoch ruling removing the source law as a prediction.
- `P6_RECEIPT.md` still contains the withdrawn transmitted-background/dark-sky and exclusion-strength language. The kickoff withdraws it, but the receipt itself is not a clean current statement.

Accordingly, p6/p7/p8 remain useful conditional experiments, not model predictions.

## Reproduction record

Executed in this lane with Python 3.9.6, NumPy 1.26.4, SciPy 1.13.1:

- `python3 p1c_rigorous_sweep.py`: exit 0, 7/7 checks. Reproduced tau(w=0.01)=2.5937, tau(junction)=0.1321, and low-w bracket supremum 20.726. However, the delivered artifact returned `n/a` at w=0.999 even though `P1C_RECEIPT.md` tabulates 0.037 and says every table number is produced by the file. That high-w row is not reproducible from p1c as delivered.
- `python3 p6_path_transfer.py`: exit 0, 5/5 self-checks. Reproduced horizon redshift `Z=5.5769e-06` and tau=0.1321. The w=0.03 centre tau printed `nan` while a dipole was still reported; this weakens the script’s “across every computed opacity” presentation.
- `python3 p7_signed_sweep.py`: exit 0, 4/4 checks. Reproduced the conditional root w=0.0407786 and its narrow interval. This reproduces the implementation, not the pinned model, because the source closure is inherited.
- `python3 p8_thick_limit.py`: exit 1, 1/3 checks. Roots existed only at K=1,10,100; K>=1000 returned `nan`. The script then mislabeled the last finite K=100 root as “K=1e5” in its convergence detail. This agrees with the receipt’s warning that the high-K test is under-resolved; p8 is not a successful thick-limit reproduction.
- Reconstructed the flatness measurement directly from `emergent_K`, the exact off-centre crossing equation at `x/R=1e-3`, and w=0.2456. It reproduces all five printed amplitude/shape rows to the shown precision. Direct coefficient projection refutes the interpretation attached to those rows.

## Failed attacks / surviving points

- I could not break the `k^rbar` cancellation in the optical-depth invariant by adding angular momentum to the photon; comoving flow removes angular contractions, so the cancellation is genuinely non-radial.
- I reproduced the five flatness table rows exactly; the defect is not fabricated data but the interpretation of a near-unity ratio.
- I reproduced both conditional null calculations. The defect is not numerical non-reproducibility of the roots but the unsupported quantifier from “two assumed closures” to “the pinned model.”
- I found no current evidence against the carried analytic `beta_rel` law.

## Required repair for a future PASS

1. Replace claim 4 with a closure-conditional statement, or supply a theorem showing a root for every thermodynamic/radiative closure in a clearly bounded admissible class. The current record supplies an immediate no-root counterexample, so the latter would require changing that class explicitly.
2. Withdraw or redo claim 5 using the normalized dipole coefficient (or `1-R`), not percent drift of R near one.
3. Narrow claim 1 to regular finite-boost sources unless a general emitter-velocity/source bound is derived.
4. Mark p6/p7/p8 outputs explicitly conditional on their thermal closures, and repair the p1c high-w and p8 reporting/reproducibility defects before citing those scripts as clean receipts.

HOLD_NULL_EXISTENCE_AND_FLATNESS_UNSUPPORTED
