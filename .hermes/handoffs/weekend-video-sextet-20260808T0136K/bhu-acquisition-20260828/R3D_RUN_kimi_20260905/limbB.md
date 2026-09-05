# LIMB B — R3D kimi seat, 2026-09-05

## 1. The admissible reading set (§2, §4)

The admissible reading set is the completion-free derivation plus at most four one-completion
readings (Euclidean volume / uniform interior / order-unity coefficient set to 1 / GR exterior),
each kind instantiated only where the census leaves its object UNBOUND, each at most once.

Object-by-object check against the census:

| completion kind | its object | BOUND or UNBOUND | binding census row |
|---|---|---|---|
| Euclidean volume | volume-mass conversion for the core | BOUND | L6: entry 19 eq (3) lines 220-230; entry 18 eq (10) lines 129-133 (mass function printed as the density integral) |
| Uniform interior | density profile rho(r) | BOUND | L5: entry 19 lines 252-254; entry 18 eq (8) lines 118-122 (profile printed exactly) |
| Order-unity coefficient set to 1 | coefficients in the core-scale/mass/horizon relations | BOUND | printed exactly: 2 in r_g = 2GM/c^2 (L3), 3 in r0^2 = 3c^4/(8 pi G e0) (L4), 1 in r_*^3 = r0^2 r_g (L2); the criticality coefficient is derived below, not assumed |
| GR exterior | exterior form; identification of M | BOUND | L3 (entry 18 lines 93-96), L7 (entry 18 lines 137-138; entry 19 eq (4) lines 232-240) |

No kind is instantiated. **The admissible reading set is the completion-free derivation alone.**

## 2. The completion-free derivation

Printed inputs (ledger rows): metric g_tt = 1 - R_g(r)/r with R_g(r) = r_g(1 - e^{-r^3/r_*^3})
(L1); r_*^3 = r0^2 r_g (L2); r_g = 2GM/c^2 (L3); r0^2 = 3c^4/(8 pi G e0) (L4);
M >= Mcrit with Mcrit the double-horizon mass (L10); horizons r+, r- (L9).

Derivation (calculus on printed relations only; no added assumption):

1. Horizons are zeros of g_tt(r) = 0, i.e. solutions of R_g(r)/r = 1. Two horizons (or one
   double horizon at criticality) exist iff max over r of [R_g(r)/r] >= 1.
2. With x = r/r_*: R_g(r)/r = (r_g/r_*) (1 - e^{-x^3})/x.
3. max_x [(1 - e^{-x^3})/x]: the derivative vanishes when e^{-x^3}(3x^3 + 1) = 1, i.e.
   e^w = 3w + 1 for w = x^3. The nonzero root (mpmath, mp.dps = 30, 0.05 s — under the 120 s
   symbolic cap; script limbB_criticality.py):
     w* = 1.90381369444038348471014036083, x* = 1.23939045970785719868427916584,
     g_max = 0.686628412234256630275760651836.
4. Criticality: (r_g/r_*) g_max = 1, so r_g = kappa r_* with kappa = 1/g_max =
   1.45639181569263487001561287433.
5. Substituting r_*^3 = r0^2 r_g: r_g = kappa (r0^2 r_g)^{1/3} => r_g^{2/3} = kappa r0^{2/3} =>
     r_g(crit) = kappa^{3/2} r0 = 1.75758907575406650996252630335 r0.
6. With r_g = 2GM/c^2:
     **Mcrit(r0) = kappa^{3/2} c^2 r0 / (2G) = 0.878794537877033254981263151673 * c^2 r0 / G**
   numerically Mcrit(r0) = 1.1833767465690965e27 kg * (r0 / 1 m).
   The black-hole condition is M >= Mcrit(r0), exactly the printed form of entry 19's
   "M >= Mcrit, where Mcrit corresponds to the double horizon" (L10) — here with the closed
   coefficient the sources do not print.

Consistency: no two printed relations used above contradict one another; the reading is
consistent (allowed mass set non-empty for every r0 > 0).

## 3. The allowed mass set of the completion-free reading

The printed relations leave the core scale r0 — equivalently the limiting density e0/rho0
through r0^2 = 3c^4/(8 pi G e0) (L4) — UNBOUND as a value: no manifest relation fixes it or
bounds it away from zero. It is a free parameter of the construction ranging over (0, inf).

Allowed mass set over the model family:

  { M : exists r0 > 0 with M >= kappa^{3/2} c^2 r0 / (2G) } = (0, inf)

Greatest lower bound = 0 (take r0 -> 0 with M = Mcrit(r0) -> 0; every element of the set is
strictly positive, and values arbitrarily close to zero are admitted). The reading therefore
**permits masses approaching zero** — it lies in **Z**.

For any FIXED r0 the reading yields a strictly positive lower bound Mcrit(r0) — but r0 is not
fixed by any printed relation, so the reading as a whole yields no positive floor.

## 4. Partition and classification (§4)

- P = {} (no admissible reading yields a positive floor)
- Z = { completion-free derivation }
- I = {} (no inconsistent reading)

P is empty and Z is non-empty -> **class 4: DYM_NO_POSITIVE_FLOOR** —
"a positive floor was unreproduced from the stated inputs".

Family to report (§4 class 4: "Report the family"):

  Mcrit(r0) = kappa^{3/2} c^2 r0 / (2G), kappa = [max_x (1 - e^{-x^3})/x]^{-1} = 1.4563918156926349
  i.e. Mcrit(r0) = 0.8787945378770333 * c^2 r0 / G
                 = 1.1833767465690965e27 kg * (r0 / 1 m),

the family of critical masses indexed by the free core scale r0 in (0, inf). The infimum over
the family is 0; there is no positive minimum black-hole mass.

## 5. Control dispositions on this class (reached directly)

- C3_DELETION_PROBE=NOT_RUN — §4 class 4 clause: "Record C3_DELETION_PROBE=NOT_RUN on this
  class WHEN THE RUN REACHES IT DIRECTLY: no positive floor survives, so the deletion probe has
  no candidate to test". The probe is never engaged; _c3_relations.json is not written; the
  probe script is never opened.
- C4_GR_BENCHMARK: reached and carried out (C4_benchmark.md).
- C6_BREAKER_TEST=NOT_RUN — §5 C6 clause: C6 applies on every positive-floor outcome
  (classes 1 and 2); on DYM_NO_POSITIVE_FLOOR no positive floor was produced, so C6 was never
  engaged.
- C0, C1, C2, C5, C5b: reached, actual results recorded in the report.
