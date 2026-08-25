# GPT56 ADVERSARIAL GATE — successor preregistration draft V2

## Custody pin

Computed SHA-256 for `../PREREG_SUCCESSOR_DRAFT_V2_20260824.md`:

`8362166cc032945792502dde4b2dc472e0c59b434273084c9e9d63b61944fff5`

This equals the brief's required pin. Review proceeded on those bytes.

## Numbered findings

### 1. BLOCKER — the defined estimator is uncorrected for the attenuation that §4 explicitly injects

**Quote.** §3 defines
`Â_c = Σ(s_i − s̄)(c_i − c̄) / Σ(c_i − c̄)²` and says the slope estimates `A` directly. §4 then says the Longo injection is “diluted by” `a = 0.85`. §5 nevertheless compares that same `Â_c` directly with `0.0408`.

**Why this fails.** For a true Longo coefficient `A_true` observed through a symmetric sign classifier with accuracy `a`,
`E[s_obs|c] = (2a−1) A_true c`. The centred slope therefore estimates `(2a−1)A_true`, not `A_true`. At the document's floor, `(2×0.85−1)×0.0408 = 0.02856`. The executable check printed exactly `ATTENUATION a=.85 raw_expected 0.02856 true_A 0.0408`. Thus the document powers on an attenuated signal but judges the uncorrected estimate against the undiluted published amplitude. With enough leverage, a perfectly present Longo signal can satisfy the rejection band merely because the known attenuation was not inverted. The name `Â_c` also collides with V3's attenuation-corrected `Â_c` while V2's formula is only centred, not attenuation-corrected.

**Minimal repair.** Name the raw centred slope `β̂`; define the decision estimand explicitly as `Â = β̂/(2a−1)`; propagate the frozen/hand-checked uncertainty in `a`; and use `Â` consistently in both §5 regions and the detection floor. Alternatively, keep `β̂` raw but transform every target and band into raw-signal units. Do not mix the two conventions.

### 2. BLOCKER — the decision bands and permutation test contain undefined quantities

**Quote.** §5 uses `σ_comb` once and `σ_ours` twice. Neither is defined anywhere in V2. §3 calls “exact permutation” authoritative, while BS-7 uses a finite `n_perm` plus-one Monte Carlo formula. V2 contains no `N_perm` at all.

**Why this fails.** The symbol inventory command returned `V2_OCCURRENCES σ_ours 2`, `σ_comb 1`, and `N_perm 0`. V3's F-4 definitions cannot silently fill the gap: they contain the now-banned full-sphere `3·D̂` normalization, and V2 §8 says F-1 through F-7 are rebuilt. Consequently two implementations can produce different rejection bands while both claiming compliance. “Exact permutation” can mean exhaustive enumeration, whereas BS-7 specifies finite Monte Carlo; no run count, seed schedule, batch rule, injection law, power-trial count, or Monte Carlo pass criterion is frozen. The power probability is therefore not reproducibly receiptable.

**Minimal repair.** Define, in V2, the raw slope permutation standard error and the attenuation-corrected `σ_ours`; define `σ_comb = sqrt(σ_pub² + σ_ours²)` (plus the declared treatment of uncertainty in `a`); state the variance divisor convention; and freeze `N_perm`, seeds, plus-one p-value, the Bernoulli sign-injection law `P(s=+1|c)`, number of power trials, and an acceptance rule that accounts for Monte Carlo error.

### 3. BLOCKER — BS-2/BS-5 and the image campaign form an unfillable temporal cycle

**Quote.** §2 says selection stops at `L_min`, which “BS-5 sets.” The slot register says BS-5 is “open — after BS-2,” while BS-2 must already report the selected brick list and accepted `N`, `Var(cosθ)`, and `L`. §4 further requires BS-5 to use “REAL accepted positions.” §9 says the polar image campaign occurs only after freeze, while the preamble says every binding slot must hold a receipt before the text becomes a preregistration.

**Why this fails.** BS-2 cannot finalize the selected prefix without `L_min`; BS-5 cannot derive `L_min` until after BS-2; and the actual instrument-accepted positions cannot exist until cutouts have been fetched and inference/abstention has run. That campaign is barred until after freeze, but BS-5 is required before the document can become the preregistration. A receipt cannot satisfy all of these statements. The laziest apparent escape—using Cut-6 parent positions as “accepted positions”—reopens the exact footprint loophole because carried instruments abstain and retention can re-tilt the final footprint.

**Minimal repair.** Split the process into (i) a pre-acquisition planning bound with a frozen conservative retention/attenuation model and a deterministic `L_min`, and (ii) a post-inference, pre-sign-unblinding final power gate on the sealed actual acceptance mask. Freeze the second gate's algorithm, inputs, seeds, and failure action before acquisition, but fill its execution receipt only after the mask exists. Rewrite the slot chronology so every prerequisite has an acyclic producer.

### 4. BLOCKER — descending `|cosθ|` is not, in general, a leverage-maximizing selection rule

**Quote.** The design authority requires a subset to “maximise `N * Var(cos theta)`.” V2 instead mandates that bricks be ranked by per-brick `|cosθ|` descending and accepted in that order, with counts second.

**Why this fails.** Variance is centred and therefore depends on the evolving weighted mean. Individual `|c|` is not an additive leverage score. The executable three-brick counterexample with equal counts, `c = [0.99, 0.98, −0.50]`, gives `L = 0.00005` for the first two bricks in descending-`|c|` order, but `L = 1.11005` for `[0.99, −0.50]`: 22,201 times more leverage with the same number of bricks. Counts make the non-additivity stronger. The existing design script itself labels the rule “variance-optimal,” but that is not a theorem. V2 additionally HALTS acquisition using arriving Cut-6 counts although the successor photo-z cut and later instrument retention determine the analysis sample; that can halt on the wrong `N·Var(c)`.

**Minimal repair.** Either choose the full footprint or freeze a deterministic optimizer for weighted marginal increase in `L` using the complete eligible post-photo-z parent inventory, with exact tie-breaking and a proof/test battery including asymmetric footprints and unequal brick counts. Use conservative retention bounds for acquisition and require the final sealed accepted-position gate from Finding 3; never call a Cut-6-only prefix the accepted-sample leverage.

### 5. BLOCKER — `a = 0.85` is assumed but no successor binding slot proves the assumption

**Quote.** §4 takes “labelling floor `a = 0.85` (V3 F-7 minima, carried)” as an input. §8 says only “HC-1H committee and sealed-key protocol” are carried. The seven-slot register has no HC-1H attenuation/validity receipt.

**Why this fails.** V3 did not obtain `a ≥ 0.85` by declaration alone. Its HC-5 required the one-sided lower bound `a_LB = a − 1.645σ_a ≥ 0.85`, per-stratum and synthetic-error gates, and HC-6 re-evaluated power at the hand-checked lower bound before unblinding. V2 carries a new release/footprint and an abstaining instrument but omits those operative validity gates and their receipt. A hostile compliant implementation can set the power input to 0.85 without demonstrating that the successor sample satisfies it. This affects both power and the attenuation correction in Finding 1.

**Minimal repair.** Incorporate the full applicable HC-1H measurement and validity rules, not merely its committee/key mechanics; add a binding successor receipt for `a`, `σ_a`, `a_LB`, strata/count closure, and all integrity triggers; and make both correction and final power consume the conservative receipted lower bound.

### 6. BLOCKER — the fixed axis is not machine-exact, and the named blind-double implementations already use different axes

**Quote.** §1 writes `(l,b)=(52°,68.5°) ≡ (α,δ)=(217°,32°)`. §6 requires the two implementations to agree on the accepted brick set exactly and floating outputs to relative difference at most `1e-9`.

**Why this fails.** The named gpt2 implementation pins `AXIS_RA_DEG = 217.0`, `AXIS_DEC_DEG = 32.0`. Hwao's named selection implementation pins `RA0 = 216.984434295527`, `DEC0 = 32.060611193471`. Those axes are separated by 3.721864 arcmin. Rounded galactic and equatorial coordinates cannot both be treated as an exact identity for brick ranking. Near ordering/tie boundaries, the accepted set can differ, so the current BS-2 exact-set receipt is not fillable under the no-reconciliation rule.

**Minimal repair.** Freeze one authoritative machine-readable unit vector (or one exact coordinate pair plus frame/equinox and conversion implementation), state that the other coordinate pair is display-only, and independently rebuild/regate both calculators against adversarial near-boundary fixtures before accepting a real-catalog comparison.

### 7. MAJOR — BS-7's “behavioural identity” still cannot prove the centred statistic it declares

**Quote.** BS-7 requires the harness to print `{statistic: centred_slope, ...}` and match the greater-tail plus-one p-value on one injected fixture.

**Why this fails.** The statistic identity remains a self-declaration. For fixed positions and a permutation of a fixed sign multiset, an uncentred covariance numerator and the centred numerator differ only by a permutation-invariant additive term; positive rescalings likewise preserve every rank. They therefore produce the same one-sided permutation p-value while reporting a different amplitude and failing monopole projection. BS-7 is a real improvement over merely printing the English sidedness sentence, but it does not behaviorally establish `centred_slope` as claimed.

**Minimal repair.** Have the independent receipt implementation recompute `Â_obs` and every `Â_perm` from the raw fixture arrays using the frozen centred formula, compare the observed value and full fixed-seed permutation vector (or its pinned digest) to the harness, and only then recompute and compare p. Include a nonzero-monopole, asymmetric-footprint fixture.

## Prior eight-finding repair trace

1. agy F1: repaired locally; the slope permutation-variance formula is correct.
2. agy F2: repaired; V3 F-6 regions and strict thresholds are restored.
3. agy F3: the `E[cos²θ]` mismatch is removed and the centred slope is expectation-correct under the stated ideal sign model, but the separate attenuation error in Finding 1 remains.
4. agy F4: repaired; V3 and successor photo-z provenances are separated.
5. agy F5: repaired; power is tied to `p < 0.001`.
6. agy F6: a relative tolerance is now stated, but Finding 6 makes the named comparison presently unfillable.
7. agy F7: partially repaired for greater-tail sidedness, not for the declared centred-statistic identity (Finding 7).
8. agy F8: repaired; the body now points to BS-4.

Thus “all eight findings repaired” overstates F7 and does not cure the newly exposed blockers.

## Attacks that held

- **Custody held.** V2 and V3 recomputed hashes match their stated pins.
- **Centred-slope algebra held under the ideal model.** Exhaustive permutation of `s=[−1,−1,+1,+1]` over an asymmetric footprint `c=[−0.9,−0.2,0.4,0.8]` gave permutation variance `0.8093070308548307`; `Var(s)/((N−1)Var(c))` gave `0.8093070308548306`. With nonzero `c̄=0.025`, `E[s|c]=0.0408c` gave expected slope `0.0408`. The ±1 discreteness is valid because `P(s=+1|c)=(1+Ac)/2`, and the tested maximum `|Ac|=0.03672<1` (globally `|A|=0.0408<1` for `|c|≤1`).
- **Quotation fidelity held for the values specifically attacked.** V3 contains the quoted amplitude and `σ_pub`, both coordinate pairs, `flux_r > 0`, `dered_mag_r < 17.7`, F-5 East-of-North sign, both F-6 thresholds/regions, the `3.09σ_ours` floor, and the `a=0.85` frozen-minimum context. No V3 photo-z cut was attributed in V2.
- **Numeric decision partition held.** With the stated conditions, `p=0.001` and `p=0.05` both classify INCONCLUSIVE; values strictly below/above enter only their respective candidate regions; the reproduced and rejected p-ranges cannot overlap.
- **gpt2 fixture reproducibility held.** Rerunning `python3 ../gpt2/calc_leverage.py` produced a byte-identical fixture table (`cmp` exit 0).

## Evidence ledger

Content read:

- `BRIEF_GATE_SUCCESSOR_V2.md`
- `../PREREG_SUCCESSOR_DRAFT_V2_20260824.md`
- `../PREREG_SUCCESSOR_DRAFT_V1_20260824.md`
- `../../SUCCESSOR_SCOPE_20260821.md`
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `../agy/REVIEW_AGY_20260824.md`
- `../gpt2/BRIEF_GPT2_LEVERAGE_CALC.md`
- `../gpt2/calc_leverage.py`
- `../gpt2/fixture_results.txt`
- `../gpt2/DONE_GPT2.md`
- `../../_successor_instrument_20260823/selection_leverage.py`
- `../../_successor_instrument_20260823/SELECTION_DESIGN_NOTE_20260823.md`
- `../../_successor_instrument_20260823/estimator.py`
- `../../_successor_instrument_20260823/selection_leverage_20260823.txt` (targeted search output)

Commands/checks run:

- `shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V2_20260824.md`
- `shasum -a 256 ../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- Python exhaustive-permutation derivation for §3 expectation/variance, amplitude domain, and attenuation.
- Python coordinate separation and leverage counterexample.
- Python source-symbol/quotation inventory and slot-order line extraction.
- Python mechanical decision-boundary classification at `p=0.001` and `p=0.05`.
- `python3 ../gpt2/calc_leverage.py` followed by `cmp -s` against its archived fixture output.
- Targeted repository searches for V3 quotation literals, all V2 section/slot references, `σ_ours`, `σ_comb`, `N_perm`, acceptance/HC terms, and the named Cut-6 receipt.

No `/Users/duhokim/NebulaMindData/` path was read. No source artifact was edited.

## Testimony

None. The verdict relies on the quoted bytes and executable checks above.

**REFUSED** (blocking findings 1–6: attenuation/estimand mismatch; undefined decision/permutation contract; unfillable gate chronology; non-maximizing selection; unreceipted attenuation floor; non-identical fixed axis).
