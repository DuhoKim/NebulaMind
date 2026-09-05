# Limb B

## Completion-free derivation

Using the source-pinned exponential Dymnikova metric, write `x=r/r₀` and `a=r_g/r₀`. C2 rows L01, L06-L08 give

`f(x,a)=g_tt=1-(a/x)[1-exp(-x³/a)]`.

The critical black hole has the printed “double horizon” (L10), so `f=0` and `∂f/∂x=0`. A 50-digit SymPy `nsolve`, protected by a 120 s alarm, returned

`xcrit=1.4957095399086404229377072509146620405789773438627`

`acrit=1.7575890757540665099625263033460434542088104733765`.

Thus, for each fixed `r₀>0`,

`Mcrit(r₀)=(acrit/2)c²r₀/G = 0.878794537877033254981263151673 c²r₀/G`,

and the allowed black-hole mass set is `A(r₀)=[Mcrit(r₀),∞)` (the lower endpoint is the double-horizon solution). Equivalently, with entry 18's printed `r₀²=3c⁴/(8πGε₀)`,

`Mcrit(ε₀)=0.878794537877033... (c²/G) sqrt(3c⁴/(8πGε₀))`.

The source defines but does not fix `ε₀`/`ρ₀` (C2 row L11). Across the completion-free reading's permitted positive density values, `r₀→0+` as `ε₀→∞`, and `Mcrit→0+`. The full allowed set therefore has greatest lower bound zero. Classification: `Z` (permits masses approaching zero), not `P`; it is consistent, so not `I`.

## Finite admissible reading set

| reading | completion | why instantiated/not instantiated | allowed mass set | P/Z/I |
|---|---|---|---|---|
| R0 | none (completion-free) | mandatory base reading | `⋃_{r₀>0}[0.878794537877033...c²r₀/G,∞)=(0,∞)`; infimum 0 | Z |

There are no one-completion readings: Euclidean volume is BOUND by C2 L04; uniform interior is BOUND (and contradicted) by L06; operative order-unity coefficients are BOUND by L01 and L03-L08; the GR exterior is BOUND by L01, L02, and L15. Section 2 permits instantiation only for UNBOUND objects.

Partition: `P=∅`, `Z={R0}`, `I=∅`. Under protocol §4's limb-B table this files class 4, `DYM_NO_POSITIVE_FLOOR`: a positive floor was unreproduced from the stated inputs. The reported family is `M≥Mcrit(r₀)=0.878794537877033...c²r₀/G`, with free `r₀>0` (equivalently free core density).
