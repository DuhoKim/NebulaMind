# BHU closed-routes register

Tori, 2026-08-27. Opened so that routes this programme has already closed are not silently
reopened by a later session — mine or anyone's.

**Rule for this file.** An entry may be added only with (a) the receipt that closed it and
(b) the *scope the gate actually allowed*, which is often narrower than the prose I first
wrote. Nothing enters here from memory. If a route is held rather than closed, it says HELD
and does not belong in the CLOSED section.

---

## CLOSED

### C1 — Expansion-rate anisotropy (Phase 4, Track A)

**Status: CLOSED, in the gate's scope — not in the blanket form I first stated.**

The interior of the matched solution is **exact FRW**, not approximately FRW
(`bhu-theory-phase4-anisotropy-20260823/A2_RECEIPT.md:9`). Any photon path lying wholly inside
that region is a path in exact FRW, so the redshift–distance relation carries no directional
information (`A3_RECEIPT.md:13`). Directional expansion-rate measurements therefore cannot
detect the boundary, at any precision and from any off-centre position.

**Scope correction, and it is mine to carry.** `GATE_TRACKA_VERDICT.md:28-30` narrowed this:
the limb is *"null only for wholly interior signals, not identically null for the observable
named in the brief."* It holds for comoving sources whose **complete** light paths remain
inside exact FRW. My stakes document says the test is "dead, permanently" without that
qualifier. **The qualifier is the gate's, and it governs.** Anyone quoting C1 must quote the
restriction with it.

### C2 — Hawking radiation / horizon thermodynamics

**Status: CLOSED AS A SOURCE-PINNED ROUTE — scope tightened 2026-08-27 by
`CGATE_REGATE5_CONFIRM_VERDICT.md` (CLEARED_HAWKING_DEMOTION).**

**What is closed.** The Smoller–Temple artifacts audited in this lane **do not themselves define
a Hawking observable.** Importing `T_H = ħc³/8πGMk_B` reports a property of an added model, not
a source-pinned BHU prediction. Nothing in these papers supplies the horizon thermodynamics the
formula presumes.

**What is NOT closed, and must not be read into this entry.** This is **not** a proof that no
conceivable added horizon-thermodynamics model could ever produce an observable. Someone who
supplies the missing exterior thermodynamics as a defended physical model in its own right is
not refuted by C2 — they are outside its scope. In the confirm seat's words: Hawking is closed
*"only as a source-pinned route supplied by these artifacts, not as an exclusion of all
conceivable added thermodynamic models."*

Four reasons below, **ordered by strength and numbered to match the bottom line of
`P9_HAWKING_RECEIPT.md`**. Reason 1 is load-bearing, reason 2 the strongest self-contained one,
and reason 4 is demoted to supporting (see the boxed withdrawal under it). The gate that demoted
reason 4 explicitly affirmed the rest: *"the stronger objections in p9 still stand … That does
not reopen Hawking radiation as a usable route."*

> **RENUMBERED 2026-08-27.** This list previously ran in discovery order, which put the
> distinctiveness argument at position 1 and the source argument at position 4 — the exact
> reverse of the receipt, so "C2 reason 1" and "P9 reason 1" named opposite things.
> Positions 2 and 3 are unchanged. Any earlier citation resolves as:
>
> | old | new | reason |
> |---|---|---|
> | C2 reason 1 | **reason 4** | not distinctive (factor of two) |
> | C2 reason 4 | **reason 1** | not defined for this model |

Note on reasons 2 and 3: they are amplitude/structural facts about the *naive Schwarzschild*
calculation. They bound what THAT calculation could ever deliver; they are not independent
bounds on an arbitrary added thermodynamic model either. Reason 1 is the one that is genuinely
about the source.

Receipt: `P9_HAWKING_RECEIPT.md`; computation `p9_hawking.py`, 16/16 self-checks, exit 0.
Run at both H₀ = 67.36 and 73.04 km/s/Mpc; every conclusion holds at both.

1. **Not defined for this model, from the source text.** Smoller–Temple mention Hawking twice,
   both in the reference list (`math-ph_0302036_clean.txt`, `grep -i hawking` → 2 hits, lines
   3152 and 3168; the 1997 paper → 0 hits). Their horizon is a **White Hole event horizon of
   an ambient Schwarzschild metric**, and the entropy condition fixes the time orientation *to
   the case Hawking's derivation excludes*: "the FRW metric expanding outward behind a shock
   wave emanating from a White Hole is entropy satisfying, while its time reversal ... is
   entropy violating." They also take T₀ as an **assignable constant** of the solution, so the
   background temperature is an input and cannot be an output.
2. **Not resolvable in principle.** Wien peak `λ = 2.183884e+27 m` against `R_H = 1.373312e+26
   m` → **λ_peak / R_H = 15.9023**. Not one mode fits inside the observable universe. The ratio
   is *identical* at both H₀ values (both quantities scale as 1/H₀), so it is immune to the
   Hubble tension.
3. **Not detectable.** `u_Hawking / u_CMB = 5.617799e-122`; evaporation `1.451605e+125` Hubble
   times. For the CMB to *be* Hawking radiation the source would need `4.501595e+22 kg`
   (0.6131 lunar masses) with `r_s = 66.86 μm`.
4. **Not distinctive — SUPPORTING ONLY. Demoted 2026-08-27 by REGATE5.**
   `T_Hawking(M_H) = 1.326889e-30 K`; the Gibbons–Hawking temperature ΛCDM already predicts for
   its own de Sitter horizon is `ħH₀/2πk_B = 2.653778e-30 K`; the ratio is
   **2.000000000000 — exactly two**. Against the asymptotic rate `H_Λ = H₀√Ω_Λ` it is 1.654932.

   > **This entry originally read "Not discriminating — the decisive one" and asserted that a
   > horizon-temperature measurement of unlimited precision could not separate BHU from standard
   > cosmology. That is WITHDRAWN.** `CGATE_REGATE5_PHASE5B_VERDICT.md`
   > (HOLD_HAWKING_DEGENERACY_OVERCLAIM) ruled, correctly, that a factor of two is not a
   > degeneracy: an ideal thermometer distinguishes 1.3269e-30 K from 2.6538e-30 K. The claim
   > that it "generalises to any black-hole cosmology at the Hubble scale" is withdrawn with it.

   What survives: both figures sit at the same `ħH/k_B` scale, so a horizon temperature of that
   order is **not by itself evidence for BHU**. A distinctiveness point, not a
   no-discrimination point. It supports the closure; it does not carry it.

**Why C2 matters beyond itself — stated as a diagnosis, not a theorem.** Writing
`T_H = ħc³/8πGMk_B` for this model presumes a vacuum Killing horizon with an asymptotic region.
The audited version has a **TOV fluid exterior** with `p = σρ`. Quoting a Hawking temperature
therefore means adding thermodynamics the papers do not contain and reporting a property of
what was added — **structurally the same error REGATE4 failed on the same day**
(`REGATE4_DISPOSITION.md`). The optical route (H1) and the thermodynamic route close on the
same absence in the same source.

> **Scope limit on that observation, imposed by the confirm seat and kept deliberately:**
> *"The tidy statement that the Hawking and optical routes close on the same missing exterior
> physics should not be promoted into a theorem, but as a diagnosis of this lane's source gap
> it is fair."*
>
> I had described it to Duho as "a coherent finding rather than two coincidences," which leans
> toward the theorem side. It is a diagnosis of **these papers**, and it should be quoted that
> way. A neat unifying story is exactly the shape of the overclaim that produced
> HOLD_HAWKING_DEGENERACY_OVERCLAIM in the first place.

---

### C3 — Tolman–Ehrenfest as the missing caloric equation of state

**Status: CLOSED 2026-08-28. Refuted by two independent gates, on the geometry.**

Phase 5b closed because Smoller–Temple supply a mechanical equation of state `p(ρ)` and never a
caloric one, so every computed signature was a property of an added closure. REGATE4 sharpened
it: varying the crossing epoch sweeps a *spacelike* family of fluid elements, so a per-worldline
adiabatic law cannot relate them. What is missing is the exterior's **spatial** temperature
profile.

**The proposal (mine, `p12_tolman.py`):** the ST exterior is a static TOV solution, so
Tolman–Ehrenfest `T·√(−g_tt) = const` should fix that profile as `T(r) = T_j / Z(r)`, with `Z`
already integrated by p6 from the model's own field equations and no free parameter.

**Why it fails.** Tolman–Ehrenfest requires a **timelike Killing vector**. p6/p12 integrate from
the junction to `N = 1 + ε`, so the entire domain has `N > 1`, hence `A < 0`. The pinned source
states the causal character for exactly this case — the metric is called TOV because its
components depend only on `r̄`, *"but now r̄ is timelike"*, and in the shock-matching section that
`x⁰ = r̄` is timelike and `x¹ = t̄` is spacelike because `N > 1`.

So `∂_t̄`, the only candidate, is **spacelike throughout the integrated region**. The timelike
direction is `∂_r̄`, but every metric function depends on `r̄`, so it is not a Killing direction.
In the gate's words: *"This is not a static exterior in the Tolman–Ehrenfest sense; it is a
time-dependent interior solution written with the timelike coordinate r̄."*

**The instructive part.** `B` really is the metric coefficient and the exponent really is the
familiar inverse square root — *"but it is being applied to the wrong causal object."* The
arithmetic was correct and meaningless, which is why `p12_tolman.py` runs 4/4: its checks test
determinacy and difference, never applicability. **A green self-check is not a licence.**

**Verdicts:** `CGATE_P12_VERDICT.md` (SUPPLY_INVALID_ATTACK1_NO_TIMELIKE_KILLING, codex gpt-5.5)
and `AGATE_P12_VERDICT.md` (SUPPLY_INVALID_ATTACK1_TBAR_SPACELIKE, agy) — independent, same
reason, both from the primary source rather than the requester's framing.

**Note against myself.** The fact that killed this is the one phase 5 established three separate
times: inside the horizon `r̄` plays the role of time. It killed the expansion-anisotropy route
(C1), it *gave* us the optical-depth cancellation (claim 2), and it has now killed my own
proposed fix. I proposed, computed and reported P12 before noticing that — and caught it only
while writing the brief designed to attack it. **Ask the causal-character question first.**

**What stays open:** the successor question is unchanged. A caloric equation of state must still
come from somewhere, and it is not this.

---

## HELD (not closed — do not file these as settled either way)

### H1 — Boundary glow / optical transfer across the shock

**Status: HOLD**, `REGATE4_PHASE5B_VERDICT.md` → `HOLD_NULL_EXISTENCE_AND_FLATNESS_UNSUPPORTED`.
Blocked on the same missing exterior thermodynamics as C2. Reopening requires *added* physics
defended as a physical model in its own right — see the four required repairs in that verdict.

---

## WITHDRAWN — must not be re-cited as results

Per `REGATE4_DISPOSITION.md` (2026-08-27 16:02):

- **Null existence as a model property.** Permitted: "the two tested closures each contain a
  cancellation, at different locations." Not permitted: "the pinned model contains a silent
  configuration." Both existence and location are closure-dependent.
- **Null location**, both values, mine and the blind seat's.
- **Flatness-gap closure.** `FLATNESS_GAP_CLOSED.md` does not close the gap; the relevant
  residual moves ~50% and direct projection changes the coefficient by 0.566675 **and reverses
  its sign**.

---

## NOT A BHU ROUTE — recorded to prevent a conflation

**The Longo-amplitude successor preregistration is not a BHU test and must not be cited as
one.** `prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V15_20260827.md:95` (sha256
`efb27c619c063f8f…`) states in its own claim boundary:

> "This tests that published amplitude at that published axis. It does not test A ≈ 0.02,
> Shamir, **BHU**, or whether the sky is isotropic."

That document is a fixed-axis reproduction test of a published galaxy-handedness amplitude.
Galaxy spin parity is a *separate* line of interest with its own history (declined by Duho's
signature, 2026-08-25). C2 belongs in this register, **not** in that preregistration: its §1
already excludes BHU by name, so the prereg needs no amendment to keep the Hawking route
closed, and adding BHU material to it would contradict its own stated boundary.

---

*Register opened 2026-08-27 17:17 KST. Entries: C1, C2 closed; H1 held; three findings
withdrawn.*
