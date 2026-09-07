# B1 — pre-registration: is the Einstein–Cartan bounce generic, or does it need chosen initial data?
**Tori, 2026-09-07 10:45 KST. DRAFT — declared before any calculation is run. Nothing here is signed, ordered or run.**

## 0. The question, in Duho's words and then in equations
"Can a collapsing black hole turn into an expanding universe under varied conditions, or only with carefully chosen assumptions?"

Formally: in Einstein–Cartan gravity with a spin fluid, does a collapsing anisotropic region bounce for a robust set of initial
data, or only on a measure-small set? This is a question about GENERICITY, not about whether one tuned solution bounces — that is
already published.

## 1. Model, assumptions, published anchors
- **S3** — Popławski, *Phys. Rev. D* **85**, 107502 (2012), APS version verified: the isotropic torsion bounce, cusp condition
  `da/dT = 0`, spin-squared term entering as `n²`.
- **S1** — Popławski, *Gen. Relativ. Gravit.* **53**, 18, publisher full text verified: effective density and pressure
  `ε̃ = ε − α n_f²`, `p̃ = p − α n_f²` (Eq. 1) with `α = κ(ℏc)²/32`; Kantowski–Sachs metric (Eq. 6); field equations (9)–(11);
  the singularity-avoidance condition printed unnumbered in §7, `−κ(ε̃ + 3p̃)/2 > 2σ²`; particle production (33)–(38).
- **S4** — Hehl, von der Heyde, Kerlick & Nester, *Rev. Mod. Phys.* **48**, 393 (1976), APS version verified: the Einstein–Cartan
  formalism and its shear treatment, (5.21) and (5.24).
- **Assumptions declared:** classical Einstein–Cartan with the standard spin-fluid ansatz; ultrarelativistic matter `ε ∝ a⁻⁴`;
  fermion number `n_f ∝ a⁻³` in the absence of production; Bianchi I (flat, anisotropic, homogeneous) — chosen because S1's own
  geometry is Kantowski–Sachs and S1 states it is approximate and proposes, but does not supply, a replacement.

## 2. What our own record forbids me to assume
K3 step 3 (`K3S3_CHECK_SHEET_20260904.md`): at the bounce the four-fermion interaction is a **two-thirds** correction
(`R = |ε̃|/ε = 2/3` at `T_cr`, threshold 0.1, limb A fired); the free-Dirac-gas closure is controlled only below about
`0.32 T_cr`; "at the bounce nobody has a controlled calculation at all", and limb B (Hartree–Fock) was never written.
**Therefore `α` is carried as an INTERVAL, not a number**, and no result may depend on the free-gas value at the bounce. Any
conclusion states which interval it holds on.

## 3. The decisive calculation, and why it is small
In Bianchi I the mean expansion obeys `3H² = κ ε̃ + σ²` with shear `σ² = Σ²/a⁶`. With `ε = ε₀ a⁻⁴` and `n_f = n₀ a⁻³`:

    3H² = κ ε₀ a⁻⁴ + (Σ² − κ α n₀²) a⁻⁶

**Both the shear term and the torsion term scale as `a⁻⁶`.** So, with no production, a bounce (`H = 0` at finite `a`) requires

    κ α n₀² > Σ²   —   a comparison of two CONSTANTS fixed by initial data, which the dynamics never drives either way,

with `a_min² = (κ α n₀² − Σ²)/(κ ε₀)`. If that is right, the bounce in this model is not generic in the ordinary sense: it holds
on the side of a sharp inequality in initial data, and shear does not merely delay it — shear competes with it at every epoch on
equal terms. This is the calculation to do first because it is analytic, it is decidable, and it either exposes the fine-tuning
or refutes my expectation. Particle production is the pivot precisely because it BREAKS this degeneracy: if `n_f` falls slower
than `a⁻³`, the torsion term outruns shear. S1 needs production to dominate shear; S1's `βH⁴` law is phenomenological and, in
S1's own text, not derived microscopically.

## 4. Outcome classes — declared NOW, before any computation
- **B1_DEGENERATE_FINE_TUNED** — the no-production criterion is a constant inequality as above: the bounce requires chosen
  initial data, quantified by the dimensionless ratio `κ α n₀²/Σ²`.
- **B1_GENERIC** — a bounce occurs for an open set of initial data with no inequality on constants, contradicting §3.
- **B1_PRODUCTION_RESCUES** — with S1's production law the bounce set is enlarged from measure-small to open, with the required
  `β` range stated and compared with S1's own values.
- **B1_PRODUCTION_INSUFFICIENT** — production does not enlarge the set over the declared `α` interval and physical `β` range.
- **B1_UNDERDETERMINED** — the system as published does not determine the answer without an input no source supplies; the missing
  input is named. (K3 step 3 makes this a live outcome, not a formality.)
- **B1_ILL_POSED** — the equations as printed do not form a well-posed initial-value problem in the regime where the bounce sits;
  the obstruction is stated. This too is a real result and would be filed as one.

## 5. Controls that must pass before any class is filed
- **C1 recovery:** setting `σ² = 0` and no production must reproduce S3's published isotropic bounce, including the cusp
  condition `da/dT = 0` — a published-value check, not a self-check.
- **C2 formalism:** the Bianchi I Einstein–Cartan equations used must reduce to S4's (5.21)/(5.24) forms in the stated limit.
- **C3 well-posedness BEFORE interpretation:** constraint propagation verified, and the integration's regime of validity stated,
  before any numerical trajectory is read physically.
- **C4 α-interval:** every reported result is reported across the K3S3 interval, never at a single free-gas value at the bounce.
- **C5 independent critique:** the derivation and the code are checked by a seat that did not write them, on a different engine
  from the implementer.

## 6. What would count against my own expectation
If C1 passes and the Bianchi I criterion turns out NOT to be a constant inequality — for instance if the correct shear evolution
in Einstein–Cartan carries a torsion coupling that changes its scaling — then `B1_GENERIC` files and §3 is wrong. I would rather
find that than defend §3.

## 7. Limits, stated now
This addresses the spin-fluid Einstein–Cartan version of the bounce with the assumptions in §1. It does not address every
black-hole-universe model, does not test whether our universe is inside a black hole, and says nothing about the Kantowski–Sachs
case S1 actually solves except by contrast. A negative result would mean: this mechanism, in this class, needs chosen data.

---

## AMENDMENT 1 (2026-09-07 11:50 KST) — which matter row this study is about
Recorded rather than rewritten; §§0–7 above stand as first declared.

1. **GRG 53, 18 uses the spin FLUID row.** Its abstract, read by me at arXiv 2007.11556 (the revised version the publisher entry
   corresponds to): "a relativistic spin fluid as a source", and "torsion may prevent a singularity and replace it with a
   nonsingular bounce if particle production dominates over shear"; its printed $\alpha=\kappa(\hbar c)^2/32$ is the
   Weyssenhoff coefficient, matching the value our ECSK derivation obtained. **B1's genericity question is therefore asked about
   the FLUID row**, which is the correct target: the anisotropic avoidance condition we are testing is that paper's own.
   *Provenance note: the Springer publisher page is behind a cookie handshake I could not pass; the publisher full text was read
   by the source worker, the abstract sentences above are my own read of the arXiv version. Labelled, not blurred.*
2. **K3's two-thirds result belongs to the DIRAC row, not this one.** `K3S3_CHECK_SHEET_20260904.md` computes
   $R=\alpha h_n^2T^2/h_\star$ with $\alpha=(9/16)\kappa$ — the Dirac coefficient of PRD 85, 107502 (corpus entry 10).
   The fluid coefficient is $\kappa/32$ in $\hbar=1$ units, smaller by a factor of 18. **So §2's interval statement above does
   not transfer to the fluid row unchanged**, and the honest position is: the self-consistency ratio for the fluid row at the
   fluid row's OWN turning point has not been computed by anyone here. It is now the first thing B1 computes, and until it is,
   no claim is made about whether the fluid-row closure is controlled at its bounce.
3. **Both rows are carried** wherever the effective pressure enters, per Blanc 11:18.
