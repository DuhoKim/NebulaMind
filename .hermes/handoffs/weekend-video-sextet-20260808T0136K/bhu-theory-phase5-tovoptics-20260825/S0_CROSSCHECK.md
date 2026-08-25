# S0 blind double — CONFIRMED (2026-08-25 17:52 KST)

Two independent implementations from the same stated physics, neither seeing the other's code
(gpt1 dispatched 17:40 with platoon/BRIEF_GPT1_BLIND_S0.md; my receipt written before its
result was read).

| quantity | Tori | gpt1 | agreement |
|---|---|---|---|
| anchor at τ = 1 | 1.4728e17 s | 1.4733e17 s | 0.03% |
| √N at crossing | 2.5498 | 2.549947 | 6e-5 |
| v at crossing | 0.42997 | 0.4299993 | 7e-5 |
| t_e/t_crit | 7.9366e-2 | 7.93517e-2 | 2e-4 |
| 1+z at crossing | 3.5496 | 3.549947 | 1e-4 |
| scaling | τ ∝ 1/t_crit | τ ∝ 1/t_crit | exact, both |

The residuals are entirely my nearest-tabulated-point crossing lookup versus gpt1's exact root
solve; gpt1's crossing residual is 0.0 at printed precision. **S0 stands.**

**What the blind seat added that I had not justified:** I chose the shock's areal radius as the
column length calling it "one scale height." gpt1 independently chose the same length and gave
it a reason — for a scale-free ρ̄ ∝ r̄⁻² exterior falloff, the outward column integrates to
exactly ρ̄(r̄_e)·r̄_e, so the choice is exact under that profile rather than an order-unity
guess. It also flagged, correctly, that the profile was not supplied and is therefore an
assumption, and that any effective path f·r̄_e scales every optical depth and the unity anchor
linearly by f. Both points are adopted into the S0 record.
