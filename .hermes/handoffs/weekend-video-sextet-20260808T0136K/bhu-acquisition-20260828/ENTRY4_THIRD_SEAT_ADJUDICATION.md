DOMAIN_NARROWER

# Entry 4 — Knutsen (2009), Grav. Cosmol. 15, 273 — THIRD-SEAT ADJUDICATION of the codex / claude-seat split

Seat: third seat (Fable 5.1, fresh context). Stamped: 2026-09-02 21:16 KST (`date`).
Read, in order: `ENTRY4_AUDIT_BRIEF_20260902.md`, `ENTRY4_codex_DEEP_RESULT.md` (AUDIT_HOLDS_THEORETICAL_OBSTRUCTION),
`ENTRY4_claude_DEEP_RESULT.md` (AUDIT_DOMAIN_NARROWER), then the pinned source
`../bhu-reading-20260823/sources/knutsen_2009_gravcosmol15_273_clean.txt` (1,191 lines; junction section lines
516–1090, conclusion 1140–1145, plus lines 9–15, 82–98, 159–169, 176–231, 245–289, 405–426, 491–514 for the
metrics, the Friedmann equation, the mass formula and the light-cone argument). Line receipts refer to that file;
OCR scatters equation fragments, so each receipt also names the equation number. No other file touched.

**The split in one line.** Both seats agree the matching (eqs. 17–43) is correctly derived here and yields dust +
the mass formula for every r_b. They part at §5: codex accepts Knutsen's reading of eq. 44 ("static sphere merged
with its horizon", lines 1084–1088); claude-seat says that reading divides eq. 36 by Ṫ under an assumption (eq. 24,
T timelike) that the resulting configuration violates, and that the true r_b = 1 solution is the zero-Killing-energy
expanding–recollapsing dust hemisphere. The three mandated sanity checks below decide it.

---

## Sanity check 1 — eq. 34 combined with eq. 36 at r_b = 1, by hand

**Notation** (lines 43–66, eq. 1; lines 245–282, eq. 7; lines 806–815, eq. 31; line 549, eq. 20): interior k = 1 FLRW
`ds² = −c²dt² + a²[dr²/(1−r²) + r²dΩ²]`; exterior Kottler `ds² = −Bc²dT² + B⁻¹dR² + R²dΩ²`,
`B ≡ 1 − 2m/R − ΛR²/3`; boundary `r = r_b` ↔ `R = R_b(T)`; `A ≡ a r_b`; dot = d/dt (interior proper time).

**Eq. 22–23 (lines 603–642).** `A = R_b` and `Ṫ ≡ dT/dt = [B − (1/c²)B⁻¹(dR_b/dT)²]^{−1/2}`.
Since `dR_b/dT = Ȧ/Ṫ`, squaring gives the unmultiplied form   `Ṫ²B − Ȧ²/(c²B) = 1`   (★).
Multiplying (★) by `c²B`:  `c²B(BṪ² − 1) = Ȧ²`, i.e. **eq. 34** `c²B = Ȧ²/(BṪ² − 1)` (lines 862–872) — re-derived ✓.
Note (★) → eq. 34 is a multiplication by B; the step is reversible only where B ≠ 0.

**Eq. 36 (lines 910–922).** From `K⁻_θθ = r√(1−r²)·a` (eq. 29, lines 788–793; check: g^{rr} = (1−r²)/a²,
Γ^r_θθ = −r(1−r²), n⁻_r = a/√(1−r²) ⇒ K⁻_θθ = a r√(1−r²) ✓) and `K⁺_θθ = ṪRB` (eq. 30, lines 802–804; check:
Γ^R_θθ = −RB, n⁺_R = Ṫ ⇒ ṪRB ✓), with R = a r_b:  **`ṪB = √(1 − r_b²)`** ✓. Physically this is the conserved Killing
energy of the boundary worldline, `E = B dT/dτ = √(1 − r_b²)` — the Oppenheimer–Snyder relation E = cos χ_b.

**Combination for general r_b.** Square eq. 36: `B²Ṫ² = 1 − r_b²` ⇒ `BṪ² = (1 − r_b²)/B`. Insert in eq. 34:
`c²B = Ȧ²B / [(1 − r_b²) − B]` ⇒ `c²B[(1 − r_b²) − B] = Ȧ²B` ⇒ (for B ≠ 0)
   **`Ȧ²/c² = (1 − r_b²) − B(A) = 2m/A + ΛA²/3 − r_b²`.**
With `A = a r_b` this is `ȧ²/c² = 2m/(a³r_b³)·a² + Λa²/3 − 1`, which is the Friedmann eq. 5 (lines 159–169:
`ȧ²/c² = Λa²/3 + C/a − 1`) iff `2m = C r_b³`, i.e. `m = (4πG/3c²)ρa³r_b³` = eq. 13 (lines 415–422) = eq. 43
(lines 1025–1050) ✓. So eqs. 34+36 are consistent with the Friedmann interior for every r_b, and I confirm both
seats: dust and the mass formula are derived, not cited.

**At r_b = 1.** Eq. 36 becomes `ṪB = 0`. The multiplied identity becomes `c²B·(−B) = Ȧ²B`, i.e.
   **`B · (Ȧ² + c²B) = 0`**  — two branches:

- **Branch (i): B = 0.** Then eq. 34 reads `0 = Ȧ²/(0·Ṫ² − 1) = −Ȧ²` ⇒ `Ȧ = 0`. So B = 0 AND Ȧ = 0 together:
  `R_b = R_s = const` on the horizon. This is Knutsen's "static sphere merged with its horizon" (line 1084–1087),
  obtained by dividing `ṪB = 0` by Ṫ (finite, non-zero — the eq. 24 assumption). But go back to the unmultiplied
  (★): with B = 0 and Ȧ = 0 it reads `0 − 0/0 = 1` — undefined, not satisfied. Branch (i) is a solution only of the
  B-multiplied equations, not of eq. 23 itself. (Also eq. 40, `R̈ = −c²D`, `D = m/R² − ΛR/3`, lines 924–934,
  950–964: a static boundary needs D = 0, i.e. `m/R² = ΛR/3`, impossible for Λ ≤ 0 and for Λ > 0 only at the
  extremal 9Λm² = 1 Nariai point — for Schwarzschild proper, "static" contradicts Knutsen's own eq. 40 outright.)
- **Branch (ii): B(A) = −Ȧ²/c² ≤ 0.** Then B < 0 wherever Ȧ ≠ 0, and eq. 36 `ṪB = 0` forces **Ṫ = 0**: the boundary
  runs along T = const. Inside the horizon (B < 0) T is spacelike, so T = const is a timelike curve; its induced
  line element is `dR²/B = −dR²/|B|`, and `c²dt² = dR²/|B|` gives `Ṙ² = −c²B` — the same relation, self-consistent ✓.
  This is the radial geodesic of zero Killing energy (E = BṪ = 0). Angular matching: `K⁺_θθ = ṪRB = 0 = K⁻_θθ` at
  r = 1 (the equator of the 3-sphere) ✓. K_tt matching: `K⁻_tt = 0` (eq. 32, dust worldlines are geodesics) demands
  the boundary be an exterior geodesic, which is exactly eq. 40; and differentiating `Ȧ² = c²(2m/A + ΛA²/3 − 1)` gives
  `Ä = −c²(m/A² − ΛA/3) = −c²D` ✓. Full junction satisfied. Motion: expands from A = 0, reaches `Ȧ = 0` at the root of
  B, i.e. **A_max = R_s** (Pathria's a_max = R_s, lines 218–220), where `Ä = −c²D < 0` because `D = −B'(R_s)/2 < 0`
  is exactly the sign condition of eq. 10 (lines 193–208) — a maximum — then recollapses. B ≤ 0 throughout, B = 0
  only at the instant of maximum expansion.

**What the equations imply at r_b = 1:** NOT "Ṫ = 0 and B = 0 both". They imply `ṪB = 0` with the two branches
above. The branch that satisfies the unmultiplied first-fundamental-form condition is (ii): **Ṫ = 0, B(A) = −Ȧ²/c²,
a non-static zero-Killing-energy Oppenheimer–Snyder dust ball (the χ_b = π/2 hemisphere), expanding to A_max = R_s
and recollapsing, surface on or inside the horizon at all times.** The static branch (i) is spurious (next check).

## Sanity check 2 — does the static-at-horizon surface satisfy Knutsen's eqs. 19 and 24?

- **Eq. 19 (lines 534–539):** Σ must carry the induced metric `ds²_Σ = −c²dt² + A²dΩ²` — a timelike hypersurface
  with proper time t. Restrict the exterior metric (eq. 7) to `R = R_s = const`, `B(R_s) = 0`: `ds² = −0·c²dT² + 0 +
  R_s²dΩ² = R_s²dΩ²`. Degenerate: the surface is the null horizon itself, has no `−c²dt²` term for any choice of
  T(t), and cannot equal eq. 19. **Fails eq. 19.**
- **Eq. 23–24 (lines 610–689):** `dT/dt = [B − (1/c²)B⁻¹(dR_b/dT)²]^{−1/2}` with the bracket assumed `> 0` "so that T
  is a timelike coordinate". At B = 0, dR_b/dT = 0 the bracket is `0 − 0/0`: undefined, not > 0; approaching along
  static spheres R_0 → R_s⁺ the bracket → 0⁺ and Ṫ → ∞. **Fails eq. 24** (and its gloss: on the horizon T is null,
  not timelike).
- **Eq. 40 (lines 950–964):** `R̈ = −c²D`; static ⇒ D = 0 ⇒ `m/R² = ΛR/3`. For Λ = 0 (Schwarzschild) or Λ < 0 no
  solution with m > 0. **Fails eq. 40 for the very case (Λ = 0) Pathria's a_max = R_s = 2m is usually read in.**

So the configuration Knutsen names in lines 1084–1087 is not a solution of the junction conditions he wrote down. It
is the r_b → 1⁻ limit of static spheres (eq. 36 with Ṙ = 0 gives `r_b² = 1 − B(R_0)`, so r_b → 1 as R_0 → R_s), but
at r_b = 1 exactly that limit is a null surface, and static spheres at any r_b < 1 only exist at D = 0 anyway.

## Sanity check 3 — what Knutsen's own words claim, and whether the algebra supports them

- **Lines 1084–1088 (verbatim):** "Hence, this choice of boundary value for the comoving radial coordinate just means
  that the fluid sphere is static, and the surface of the fluid sphere merges with its event horizon. Thus this
  particular model cannot describe our expanding universe." Preceded by the only displayed algebra of §5, eq. 44
  (lines 1067–1082): "it is now seen from Eqs. (29) and (30) that Pathria's choice r_b = 1 yields
  `1 − 2m/R_b(T) − ΛR_b²(T)/3 = 0`" — i.e. eq. 36 with the right side zero, divided by Ṫ.
- **Lines 1140–1145 (verbatim):** "Our final conclusion is that Pathria's interpretation of some mathematical
  similarities certainly served as an inspiration for a guesswork that is much too drastic. A declaration is no
  explanation. A closer look shows that the model just represents careless notation and confused concepts."
  Also the abstract, lines 14–15: "our expanding universe cannot be inside the event horizon of the vacuum metric."
- **Support.** The algebra supports **"at/inside the horizon"** only: eqs. 34+36 at r_b = 1 give `B(A) = −Ȧ²/c² ≤ 0`,
  so the surface is never in the B > 0 exterior region and touches the horizon exactly at maximum expansion. It does
  **not** support "static" (branch (i) fails eqs. 19, 24 and — for Λ ≤ 0 — 40), and therefore does not support
  "cannot describe our expanding universe" by that route. The paper's other route, the light-cone argument at lines
  498–504 ("all light cones … point inward. Hence, a particle at the surface has no choice but to move inward"), is
  stated before any matching and is true only in the future-trapped (collapse) phase; the expansion phase of branch
  (ii) lives in the past-trapped region, which the static (T, R) chart does not cover — which is exactly why the
  paper sees only a "static" degenerate limit. Lines 1140–1145 and the abstract are conclusions in words, not
  derived. One caution on claude-seat's wording: "never visible from outside" over-reaches — light leaving the
  surface during the expansion (white-hole) phase does reach the static exterior, as with any white-hole emission;
  what is derived is only that the surface itself never enters the exterior static region.

---

## Ruling: **DOMAIN_NARROWER**

Codex is right that the exclusion is the operative result, that dust and the mass formula are derived here, and
that shells / other r_b / non-FLRW interiors are untouched. Codex is wrong to accept "R_b(T) fixed at a root ⇒
static": that step is the division of `ṪB = 0` by Ṫ, valid only under eq. 24, and the surface it produces violates
eq. 24 and eq. 19 (check 2). Codex's own "coordinate subtlety" paragraph (its §2) already concedes the honest
content — "the assumed smooth timelike expanding boundary cannot persist at r_b = 1" *in the T-timelike region* —
which is the narrower statement, not the stamped one. Claude-seat's algebra is confirmed line by line (check 1) with
the one over-reach on visibility noted in check 3.

**Replacement wording for the stamped domain (exact):**

> "FLRW perfect-fluid interior matched smoothly to a Λ-vacuum (Kottler) exterior forces dust and m = (4πG/3c²)ρa³r_b³
> for every r_b (eqs. 36, 40–43, lines 910–1050); at Pathria's r_b = 1 the matching forces ṪB = 0, i.e.
> B(A) = −Ȧ²/c² ≤ 0: the surface is never in the exterior static region (B > 0) and touches the horizon only at
> maximum expansion A_max = R_s. No smooth matching exists with the surface in the T-timelike exterior assumed at
> eq. 24 (lines 652–689). The paper's further claims — 'the fluid sphere is static … merges with its event horizon
> … cannot describe our expanding universe' (lines 1084–1088) — are stated in words from a division by Ṫ; the
> static surface is null and satisfies neither eq. 19 nor eq. 24 (nor eq. 40 for Λ ≤ 0), while the equations'
> actual r_b = 1 solution is the non-static zero-Killing-energy Oppenheimer–Snyder dust hemisphere (expanding to
> A_max = R_s, recollapsing). NOT derived: 'static', 'cannot be expanding'. Shell-bearing junctions and other
> boundary choices not excluded."

Tier not changed here (boundary). Note for Duho's packet: the surviving derived content does not obstruct "the
universe is inside a black hole" — it *realises* it (Pathria's a_max = R_s is the r_b = 1 junction condition, eqs.
13/43, lines 424–426, 1022–1024); what it obstructs is Knutsen's static-sphere reading and any picture in which the
r_b = 1 surface sits in the static exterior. Whether that still merits THEORETICAL-OBSTRUCTION is tier-adjacent.

**Plain language.** Knutsen glues half of a closed dust universe onto empty outside space and does the gluing
correctly: the matter must be pressureless and its mass comes out to the usual formula — both seats and I agree.
At the special boundary Pathria used, his equation says only that a certain product is zero. He cancels one factor
and concludes the ball is frozen on its own horizon and so can't be an expanding universe. But that frozen surface
is a light-speed surface, and his own earlier equations (a time-like surface with a proper time, eq. 19; his
time-coordinate assumption, eq. 24; and for ordinary Schwarzschild his acceleration equation, eq. 40) forbid it.
Keeping the other factor instead gives a perfectly good solution that his coordinates simply cannot show: the ball
expands, reaches its largest size exactly at the Schwarzschild radius, and falls back, its edge always on or inside
the horizon. That is Pathria's picture, explained rather than refuted. So what Knutsen actually proves is smaller
than the stamp says: such a universe's edge can never be out in the static exterior — it cannot be "static on the
horizon" and it cannot be watched sitting outside its horizon — and the stamped "forces a static sphere … cannot
describe our expanding universe" clause must go.
