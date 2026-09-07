# B1 — the pressure-sign question, resolved: NOT a contradiction between papers, a MATTER-MODEL choice
**Tori, 2026-09-07 11:41 KST. This CORRECTS the lane's own earlier framing of 11:00 KST.**

## What I claimed earlier, and why it was wrong
At 11:00 KST I recorded that PRD 85, 107502 (2012) and GRG 53, 18 "carry opposite signs for the torsion correction to pressure"
after converting conventions, and treated that as a discrepancy between two published papers. Two engines agreed with that
reading — Codex's derivation gate (C1=FAIL) and kimi's blind check (SIGN_CHECK=DISCREPANCY). **Both were working from the
EXTRACTED equations. I then read the publisher PDF page myself (p. 107502-2, held locally as
`prd_publisher_verify_20260907/prd_pdf.pdf`), and the paper states BOTH cases in its own prose, one paragraph above Eq. (10).**

## What the published page actually says
Verbatim, p. 107502-2, immediately below Eq. (10):

> "Hehl, von der Heyde, and Kerlick have used the spin-fluid approximation of fermionic matter, $s_{ij}=s_{ij}u_k$ and
> $s_{ij}u^j=0$, to show that the spin-density contribution to $T_{ik}+U_{ik}$ behaves like a stiff matter with
> $\tilde\epsilon=\tilde p=-\frac14\kappa s^2$, where $s^2=\frac12 s_{ik}s^{ik}=\frac18 n^2$ [8,9]."

and, in the column above:

> "In this paper, we use the Dirac form of the spin tensor for fermionic matter, $s_{ijk}=s_{[ijk]}$ … which follows directly
> from the Dirac Lagrangian and is consistent with the cosmological principle."

Then Eq. (10): $\tilde\epsilon=-\tilde p=-\alpha n^2$, $\alpha=\frac{9}{16}\kappa$.

**So the two signs belong to two different spin sources, and the same author states both on the same page:**

| spin source | effective corrections | w | scaling | coefficient |
|---|---|---|---|---|
| Weyssenhoff spin FLUID (Hehl–von der Heyde–Kerlick) | $\tilde\epsilon=\tilde p=-\tfrac14\kappa s^2$ — SAME sign | +1 (stiff) | $a^{-6}$ | $-\kappa n^2/32$ using $s^2=n^2/8$ |
| DIRAC field, fully antisymmetric $s_{ijk}=s_{[ijk]}$ (what PRD uses) | $\tilde\epsilon=-\tilde p=-\alpha n^2$ — OPPOSITE signs | −1 | — | $\alpha=\tfrac{9}{16}\kappa$ |

GRG 53, 18 Eq. (1) uses $\alpha=\kappa(\hbar c)^2/32$ with both corrections negative: that is the FLUID row, not a
contradiction of the PRD paper's Dirac row.

## What our own ECSK derivation established, and what it is worth
The independent derivation from the ECSK action (`ECSK_DERIVATION_20260907.md`, `ecsk_derive.py`, re-run by me) gives, for an
unpolarised spin fluid, $\epsilon_s=p_s=-C\kappa n^2/4$ with $w=+1$, continuity residual exactly 0, and the opposite-pressure
trial leaving a non-zero residual. With the conventional closure $C=\hbar^2/8$ it gives $-\kappa\hbar^2 n^2/32$ — which
**reproduces the published Weyssenhoff value on this page exactly**, and matches GRG's printed $\alpha$. The derivation is
therefore validated against a published result, and it settles the FLUID row. It does not overturn the Dirac row; it was never a
derivation of the Dirac case.

## The question this leaves, which is sharper than the one I asked
The two rows are not interchangeable in the ANISOTROPIC problem, and that is where it bites. GRG's own
singularity-avoidance condition is $-\kappa(\tilde\epsilon+3\tilde p)/2>2\sigma^2$.

- **Fluid row:** $\tilde\epsilon+3\tilde p=(\epsilon+3p)-4\alpha n^2$ — the torsion term enters with weight 4 and the
  condition CAN be met.
- **Dirac row:** $\tilde\epsilon+3\tilde p=(\epsilon-\alpha n^2)+3(p+\alpha n^2)=(\epsilon+3p)+2\alpha n^2>0$ for ordinary
  matter — so $-\kappa(\tilde\epsilon+3\tilde p)/2<0\le 2\sigma^2$ and the condition **cannot be met at all**, at any density,
  with or without shear.

Yet the PRD paper's own isotropic bounce does not depend on that: it comes from $\dot a^2+k=\tfrac13\kappa(\epsilon-\alpha
n^2)a^2$ (Eq. 11), where only the DENSITY correction appears, and the density correction is negative in BOTH rows. **So under the
Dirac spin form the isotropic turning point exists while the anisotropic avoidance criterion is never satisfied.** That is the
live technical question for B1, and it is a question about which spin source the black-hole-universe bounce actually requires —
not about an error by anyone.

## Status
B1's controls stay as filed: C1=FAIL for the cross-model reduction (correctly — it was reducing a FLUID system to a DIRAC
result), C2=NOT_RUN, C3=NOT_RUN, criterion NOT_EVALUATED. The pre-registration's §3 scaling argument was written for the fluid
row and must now be carried for BOTH rows. $\alpha$ remains an interval per K3 step 3 in the fluid row.
