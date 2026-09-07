# B3 — class filed: production DOES rescue the bounce, under a consistent closure
**Tori, 2026-09-07 14:47 KST. Filed by me against `B1_PREREG_BIANCHI_I_BOUNCE_20260907.md`, whose classes were declared before any of this was
computed. Evidence: `B3_RESCUE_20260907.md`, `b3_rescue.py` (re-run by me).**

## 0. My framing error, corrected first
Codex's note of 14:40 KST is right and the error was mine, in the B3 task text and in my own summary: I described the
no-production bounce set as "a codimension-one threshold" that production might turn into "an open region — a difference in
kind". **The no-production bounce set was ALREADY OPEN.** $\kappa\alpha n_0^2>\Sigma^2$ is a strict inequality and so defines an
open region relative to the admissible constraint surface; the EQUALITY is its boundary, and the boundary is codimension one,
not the set. What is true, and what I had stated correctly in the scope qualification before muddling it here, is that the
ratio is conserved without production, so **collapse cannot carry data across the threshold** — a statement about dynamics, not
about the set's dimension. The original task file is preserved unaltered; this is the correction record. The worker did not
inherit the error: it flagged and corrected it independently in its own §1 before computing.

## 1. Class filed: `B1_PRODUCTION_RESCUES` — fluid row, flat Bianchi I, closures (b) and (c), $\Psi=\beta H^4$ with $\beta>0$
**The analytic heart, which is what makes this more than a grid observation.** Under either determined closure, the number
density is no longer diluted as $a^{-3}$, and during contraction ($H<0$)

    d ln(α n²)/d ln a = −6 + 2βH³/n < −6,   while shear remains exactly ∝ a⁻⁶.

So production breaks the shared scaling **in the direction that helps**: the torsion term outruns shear on the way in.
TORSION_SCALING_b=HELPS, TORSION_SCALING_c=HELPS. The report then gives a **finite-bounce proof for every $\alpha>0$ and every
fixed $\beta>0$ in both closures**, not merely a grid: the exponential lower bound on particle number forces a turning point.
The grid (782 bounce / 118 singular / 108 excluded per closure) illustrates it; the counts are explicitly not probabilities, and
I attach no measure claim to them.

**Controls first, as required:** CONSTRAINT_RESIDUAL_b = CONSTRAINT_RESIDUAL_c = 0 exactly; maximum normalised constraint defect
$1.9\times10^{-10}$ over the integrations; singular outcomes are distinguished from integration failures — invalid or
initially-turning data are excluded (X), and the $\beta=0$ singular cases use an exact reduction reaching zero scale factor at
finite proper time with divergent density, not a solver giving up.

## 2. Scope — the part that must travel with the claim
- **Prescription-dependent, and load-bearing.** The proof uses exactly $\Psi=\beta H^4$ with fixed $\beta>0$ extrapolated
  through the whole collapse. An arbitrary non-negative source could create too few particles to help. This is a result about
  the paper's phenomenological production law, not about particle production in general.
- **Closure-dependent.** It holds under the two DETERMINED closures. In GRG's own printed constant-coefficient thermal
  specialisation the system is over-determined and admits only a tuned constant-$H$ steady state with no smooth bouncing
  solution at all (`B1_RESULT_V2` Amendments A and B). The two results do not conflict: **the mechanism works once a consistent
  closure is chosen, and the paper's own printed closure is the part that fails.**
- The two closures agreeing exactly reflects coordinate equivalence, not two independent confirmations.
- Fluid row, flat Bianchi I only. Nothing here is asserted of the Dirac row or of the curved Kantowski–Sachs system.
- Version limits unchanged: equations inspected in arXiv 2007.11556v2; publisher equation identity unestablished; no absence of
  later corrections inferred.
- **This is not a proof of black-hole-universe cosmology and not a disproof of one.** It says the Einstein–Cartan spin-fluid
  bounce mechanism, under this production law and a consistent closure, does turn collapse around for generic admissible data.

## 3. Where this leaves the route
The three results now form one picture. Without production the bounce needs a condition collapse cannot reach. With the paper's
own printed thermal closure nothing smooth bounces at all. With production and a consistent closure, everything admissible
bounces — and it bounces where the spin correction is **at least** the ordinary energy density, with EQUALITY for isotropic
data. The fluid row's own ratio at its own turning point is 1, computed in `C1_REEXAM_20260907.md`; K3 step 3's 2/3 belongs to
the DIRAC row at the Dirac turning point and is not transferred here. On the fluid row's own number, the effective-fluid and
free-gas descriptions are therefore being used exactly where the correction is comparable to the whole ordinary density.
**The mechanism's viability and the regime where its own closure is unverified are the same regime.** That, not a verdict on
the cosmology, is the finding. See `B3_RECONCILIATION_20260907.md` for the corrections behind this paragraph.
