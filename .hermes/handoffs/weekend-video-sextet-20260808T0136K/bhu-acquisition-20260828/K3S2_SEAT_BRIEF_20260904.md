# K3 step 2 — route-1 seat brief (BLIND DOUBLE)

**Authority:** Duho, "k3s2", relayed by Blanc 2026-09-04 09:57 KST. **Governing document:** `K3S2_EXCHANGE_PREREG_20260904.md`
in this directory — read it first and in full; it binds you, this brief only tells you how to report.

**BLIND.** Do NOT open, list, grep or infer the contents of any file whose name contains `K3S2_claude`, `K3S2_codex`,
`K3S2_RESULT`, `K3S2_ROUTE2`, `K3S2_CHECK`, or `K3S2_RECONCIL`. You may read the prereg, `K3S1_RESULT_20260903.md`,
`K3S1_WHAT_A_CRITIC_GETS_20260904.md`, the step-1 scripts `K3S1_codex_spin.py` and `K3S1_claude_spin.py`, and the source text
`../bhu-reading-20260823/sources/1111.4595v2_poplawski_prd85_clean.txt`.

## What you produce

1. **One executable script** named as the dispatcher tells you (`K3S2_<seat>_exchange.py`), self-contained, runnable with
   `python3 <script>`, using SymPy and/or NumPy only. It must PRINT its own results — a claim that is not printed by the script
   does not exist. Deposit nothing else.
2. **One report** named as the dispatcher tells you (`K3S2_<seat>_RESULT.md`), whose FIRST LINE is a single class token from §4 of
   the prereg and nothing else.

## What the script must do, in this order

1. **Derive the map (prereg §1, O1–O4) yourself.** From `s^i = ½ ψ̄γ^iγ⁵ψ` and `s_ijk = −e_ijkl s^l` (entry 10 Eq. (4), L73–78),
   with the source's projection `s_ijk = s_ij u_k` and `s_ij u^j = 0` (L119–120), compute `½ s_ij s^ij` and `|s⃗|²` and PRINT the
   ratio with its sign. Do not import the step-1 corollary; derive it or contradict it.
2. **Build the state (prereg §2) explicitly**: occupation `n(p,σ,r)` with both particle and antiparticle sectors, `N_f` species
   symbolic, `T` and `μ` independent, and the `p_F`↔`n` relation derived inside the script from the occupation you wrote — never
   quoted.
3. **Evaluate `⟨s_i s^i⟩` at coincident points (prereg §3)**, printing the **direct (Hartree)** and **exchange (Fock)**
   contractions as two separately labelled quantities before any sum. State your normal-ordering / subtraction prescription in the
   script header before the code that uses it, and state the coarse-graining volume `V = ℓ³` in every reported quantity.
4. **Report the leading density power and coefficient** in the thermodynamic limit, in the degenerate (`T→0`) and classical
   (`T→∞`) limits and in the non-relativistic and ultrarelativistic mass regimes.
5. **Print all eight control codes** exactly as named in prereg §6:
   `C1_DIRECT_ZERO`, `C2_POLARIZED_N2_QUARTER`, `C3_CLASSICAL_LINEAR_IN_N`, `C4_EXCHANGE_DELETED`, `C5_UNITS_RESTORED`,
   `C6_MAP_DERIVED`, `C7_ANTIPARTICLE_SECTOR_LIVE`, `C8_NO_PRINTED_COEFF_INPUT`, each as `<CODE>=PASS` or `<CODE>=FAIL`.
   **Before running, write into the script header what you predict C4 will show.** A control that cannot be evaluated is `FAIL`,
   never omitted.
6. **Map back to both printed relations (prereg §5)**: state, for `⅛ n²` (entry 10 L121) and for `¾ n²` (entry 10 L113), whether
   your calculation derives it, contradicts it, or leaves it free. **Neither numeral may enter your computation as an input**;
   C8 asserts this by recomputing with both replaced by free symbols and checking nothing changes.
7. **File exactly one class token** from prereg §4 as the first line of your report.

## Rules

- If the coincident-point limit needs a regularisation the source does not fix, that is the answer: file
  `K3S2_EXCHANGE_PRESCRIPTION_DEPENDENT` and state the residual freedom exactly — which object, which parameter, which range of
  coefficients admissible completions give. **Do not manufacture a coefficient**, and do not pick the completion that reproduces a
  printed number.
- If your own map derivation contradicts step 1's corollary `½ s_ij s^ij = |s⃗|²`, file `K3S2_MAP_CONTRADICTED` and stop there.
- Change no other file in this directory. Move no tier, token, standing or stamp; you have no authority over any of them.
- Every numeral you assert traces to a source line you cite, or to a quantity your own script computed and printed.

SEAT_BRIEF_COMPLETE
