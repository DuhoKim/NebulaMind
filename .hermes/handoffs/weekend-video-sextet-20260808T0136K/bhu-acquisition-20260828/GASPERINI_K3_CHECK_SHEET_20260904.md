# Gasperini 1986 against K3 — one-page check sheet (Tori, 2026-09-04 00:25 KST)

**Question:** Does Gasperini derive `σ² = ⅛ℏ²⟨n²⟩` for an unpolarized spin-½ fluid, or does he adopt a closure?
**Closed class:** **CONVENTION CONFIRMED** (Tori + independent agy seat, 2/2).
**Scope:** record/warrant repair on rows 9, 10, 11 only; no tier, standing, stamp or K3-step-2 authority.

## Inputs and receipts

| test | source receipt | what is fixed |
|---|---|---|
| spin-fluid tensor | Gasperini source L75–80 | `S_{αβ}` is fluid spin density; canonical spin tensor is built with `u` |
| spatial/Frenkel condition | L90–103 | `S_{αβ}u^β=0`; in the comoving frame the spin tensor is spatial |
| macroscopic average | L98–119 | suitable space-time average; random spins have zero mean but generally nonzero mean square |
| scalar definition | L117–121, Eq. (8) | `⟨S_{αβ}⟩=0`; `σ²=½⟨S_{αβ}S^{αβ}⟩` |
| fermion premise | L130–139 | unpolarized liquid, constituent spin `ℏ/2`; `p=kρ` adopted as in Ref. 8 |
| closure line | L139–149, Eq. (15) | “We have then” `σ²=½⟨S²⟩=ℏ²⟨n²⟩/8`; subsequent averaging law cites Ref. 8 |
| dispersion gloss | L149–156 | for `⟨S⟩=0`, `⟨S²⟩` is the spin-density dispersion squared |
| full-text completion | L229–260 | references/final page contain no later derivation |

## Coefficient audit

`σ² = ½⟨S²⟩` fixes the first factor `½`. Factoring Gasperini's printed final equality leaves `⟨S²⟩=ℏ²⟨n²⟩/4`; constituent spin `ℏ/2` makes that factor suggestive, but the paper does not separately state a local rule `|S|=ℏn/2`. Multiplication after the unstated constitutive step gives `½ × ¼ = ⅛`.

What is **not** derived is the load-bearing identification `⟨S²⟩ = ℏ²⟨n²⟩/4` for randomly oriented microscopic spins. No particle sum, cross-term rule, correlation model, density matrix, coarse-graining volume or combinatorial trace appears. Thus the arithmetic after the prescription is fixed; the prescription and n² scaling are not.

## Closed-class tests

| declared class | result | reason |
|---|---|---|
| DERIVED | no | no microscopic average fixes the cross terms or n² law |
| CONVENTION CONFIRMED | **yes** | same scalar is defined, then the n² identification is stated as “We have then” |
| DIFFERENT OBJECT | no | convective condition reduces Gasperini’s scalar to K3’s spatial `½s_{ij}s^{ij}` |
| INCONCLUSIVE | no | the full text is explicit enough to distinguish definition from missing derivation |

## Citation and record bounds

Ref. 5 supports the nonzero spin-squared average; Ref. 6 supports the variational formalism/convective condition; Ref. 8 is attached to the equation of state and subsequent averaging law. Do not infer what the still-unread Nurgaliev & Ponomariev paper proves. Gasperini’s result confirms, rather than narrows, K3 step 1. Entry 10’s ¾-versus-⅛ factor-six conflict remains. Nurgaliev stays a non-blocking acquisition note. **K3 step 2 has since been ordered (2026-09-04 09:57 KST) and completed** — see `K3S2_RESULT_20260904.md` and `K3S2_CHECK_SHEET_20260904.md`; it does not change anything on this sheet.

GASPERINI_K3_CHECK_SHEET_COMPLETE
