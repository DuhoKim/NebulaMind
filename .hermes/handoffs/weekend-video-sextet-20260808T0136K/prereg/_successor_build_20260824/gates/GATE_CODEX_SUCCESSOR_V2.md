# CODEX adversarial gate — successor preregistration V2

## Custody pin

Command run before reading the draft:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V2_20260824.md`

Computed:

`8362166cc032945792502dde4b2dc472e0c59b434273084c9e9d63b61944fff5  ../PREREG_SUCCESSOR_DRAFT_V2_20260824.md`

This equals the brief's required pin. I also independently computed the frozen predecessor's SHA-256 as `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, matching V2 line 9.

## Numbered findings

### 1. BLOCKER — the claimed Cut-6 quotation erases a predecessor photo-z cut

**Quote.** V2 lines 25–31 say that Cut-6 is carried from V3, but also say: “V3 contains no photo-z cut; none is attributed to it.”

**Why this fails.** Frozen V3 line 252 defines sample selection by its filled BS-6, and V3 line 456 pins `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`. I recomputed that receipt's hash:

`shasum -a 256 ../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`

Result:

`5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`

That is the receipt pinned by V3. Its lines 28–37 explicitly state that the supporting cuts in the same frozen parent definition include “photo-z join + `0 ≤ z_phot_median < 0.15`”; its lines 49–60 call the referenced chain the frozen Cut-6 definition. V2 cannot both carry that Cut-6 and state that the predecessor has no photo-z cut. This is the quotation-fidelity refusal condition named in the gate brief, and it means AGY F4 was answered textually but not repaired against the actual frozen slot provenance.

**Minimal repair.** Restate the full predecessor Cut-6 predicate set from its hash-pinned BS-6 receipt. Then explicitly identify the predecessor photo-z predicate and say whether the successor carries it, replaces it for a new release, or deliberately removes it. Give each changed predicate a successor provenance and justification; do not describe a predecessor predicate as nonexistent.

### 2. BLOCKER — the statistic estimates the observed-label coefficient, not Longo's latent amplitude, while the decision uncertainties are undefined

**Quote.** V2 lines 52–56 define `Â_c` as the centred slope and say it estimates A directly. Lines 71–74 separately inject `A = 0.0408` “diluted by” labelling floor `a = 0.85`. Lines 81–89 compare the uncorrected `Â_c` with 0.0408 using `σ_ours` and `σ_comb`, but V2 never defines either sigma and never defines an attenuation correction.

**Why this fails.** The direct-slope claim is correct only under the stated model for the labels actually entering the slope, `E[s_obs|c] = A_obs c`. Under the document's own symmetric labelling accuracy `a`, a latent Longo amplitude obeys

`E[s_obs|c] = (2a−1) A_L c`.

At `a = 0.85`, the expected uncorrected slope is `0.7 × 0.0408 = 0.028560`, a bias of `−0.012240` relative to the stated target. My independent calculation printed exactly those values. The old V3 avoided this by defining a corrected amplitude and corrected uncertainty; V2 reuses the symbol `Â_c` and V3's F-6/F-7 decision language after deleting the correction. Because `σ_ours` and `σ_comb` have no V2 definitions, the two numeric decision inequalities and the detection floor cannot be reproduced from this document.

**Minimal repair.** Distinguish the raw centred slope from the target-amplitude estimator. Bind the applicable accepted-sample labelling-accuracy receipt, define (for a symmetric error model) `Â_L = β̂/(2a−1)`, define its permutation variance including the same factor and uncertainty in `a`, and define `σ_ours` and `σ_comb` in the successor notation. Use those definitions consistently in §4, §5, the floor, and BS-5. Alternatively redefine the scientific target as the observed-label coefficient, but then it is not a direct test of Longo's 0.0408 amplitude.

### 3. BLOCKER — `L_min`, BS-2, and BS-5 form an impossible dependency cycle

**Quote.** V2 lines 36–37 require selection to stop at `L_min`, which “BS-5 sets ... from the power gate.” Lines 43–46 require catalog fetching to halt at that same `L_min`. Section 4 requires the power calculation to use the real accepted positions. Yet the slot table says BS-2 produces the accepted set and its leverage, while BS-5 derives `L_min` only “after BS-2” (lines 117–120).

**Why this fails.** The operator needs `L_min` to know when acquisition and acceptance stop; BS-5 cannot derive `L_min` until BS-2 has supplied the accepted set; and BS-2 cannot determine the accepted set until the stop threshold exists. No receipt order can satisfy all three MUSTs. The floor `N_eq ≥ 100,000` does not break the cycle because the text also requires BS-5's power-derived threshold “with margin.”

**Minimal repair.** Before acquisition, freeze a conservative, independently derivable `L_min` (including the margin and the finite-permutation design) and then use final accepted positions for a separate confirmatory power gate. If the intended design is sequential power evaluation instead, specify the exact deterministic sequence, batch boundaries, stopping comparison, maximum acquisition ceiling, and which receipt precedes which; do not label a post-selection quantity as the pre-selection threshold.

### 4. BLOCKER — the named blind-double implementations cannot meet §6's agreement contract

**Quote.** V2 lines 103–109 require Hwao's `_successor_instrument_20260823/` and `gpt2/calc_leverage.py` to agree on the accepted brick set exactly and on `Var(cosθ)`, `L`, and `N_eq` to relative difference at most `1e-9`. Section 4 simultaneously requires variance on “actual accepted positions.”

**Why this fails.** The named implementations do not implement one common contract:

- Hwao's `selection_leverage.py` lines 23–24 use axis `(216.984434295527°, 32.060611193471°)`. GPT2's `calc_leverage.py` lines 8–9 use `(217.0°, 32.0°)`, which is the rounded axis stated in V2.
- Both selection implementations consume count-weighted brick centres, not actual accepted galaxy positions. Hwao's design note lines 28–32 expressly labels this a brick-centre approximation; GPT2's brief lines 18–24 expressly defines positions as brick centres.
- GPT2's only selector is `polar_select(..., q)`, stopping on a fraction of total count (lines 92–109). It has no `L_min` selector, accepts no brick IDs, and returns no accepted brick set. It therefore cannot emit the exact-set receipt §6 requires.

I independently applied the same Cut-6 brick-count inputs and the V2 floor `3L ≥ 100000` under each of the two named axes. The precise-axis run selected 11,534 bricks, `N=34,306`, `Var(c)=0.971663232272068`, `L=33333.878846325577`; the rounded-axis run selected 11,520 bricks, `N=34,293`, `Var(c)=0.972061684582455`, `L=33334.911349386122`. The brick-set symmetric difference was 78; relative differences were `4.099043473333089e-4` for variance and `3.097362551001466e-5` for leverage—many orders above `1e-9`.

**Minimal repair.** Freeze one axis representation (including precision), one per-galaxy versus brick-centre rule, one deterministic brick ranking and tie-break, and one `L_min` crossing rule. Before claiming the pipeline is built, independently implement and hash-pin that exact interface in both programs, including brick-ID output and actual accepted-position statistics, then run a comparator fixture that exercises the crossing boundary and asymmetric footprints.

### 5. BLOCKER — the permutation and power protocols permit vacuous or non-reproducible receipts

**Quote.** V2 line 60 calls “exact permutation” authoritative, while BS-7 line 122 defines a Monte Carlo corrected p-value using an unconstrained `n_perm`. Section 4 fixes neither `n_perm`, the number of injected skies, seed schedule, injection algorithm, nor an uncertainty rule for the claimed probability of at least 0.95.

**Why this fails.** For the required corrected p-value `(1 + #)/(1 + n_perm)`, `n_perm = 999` has minimum p exactly `0.001`, so `p < 0.001` is impossible. This is not hypothetical: Hwao's named validation uses `n_perm=999` and then reports a false-positive test at `p<0.001` (`validate.py` lines 66–71); zero false positives are guaranteed by resolution. My independent p-resolution calculation gave minima `0.001` at 999, `0.000999000999...` at 1000, and `0.0000099999...` at 100,000. At the other extreme, without a fixed number of injected skies or a confidence rule, one successful injected sky can be reported as estimated power 1.0. “Exact permutation” also conflicts with the finite-`n_perm` Monte Carlo formula unless exact enumeration is genuinely intended, which is operationally impossible at the planned N.

**Minimal repair.** Define this as a Monte Carlo permutation test; freeze `n_perm` (the predecessor used 100,000), RNG/seed handling, tie comparison, and valid finite-input checks. Freeze the injection generator including attenuation, the number of power trials, and a pass rule such as a prespecified lower confidence bound at least 0.95. Add non-vacuous resolution tests proving the harness can produce p-values on both sides of 0.001.

### 6. BLOCKER — BS-6 is simultaneously required before preregistration and forbidden until after freeze

**Quote.** V2 lines 3–4 say the draft becomes a preregistration only when every binding slot holds a receipt and Duho signs the freeze. BS-6 is a binding slot, but line 121 marks it “AFTER freeze only,” and the gate plan lines 138–139 places BS-6 only after sign-off, chmod, and git.

**Why this fails.** No state can satisfy both rules: before freeze, the “every binding slot” condition fails because BS-6 must remain open; after freeze, the document has already become frozen without every binding slot having held a receipt. This is an operationally unrealizable slot, which the brief explicitly defines as a finding.

**Minimal repair.** Either move BS-6 before freeze and specify a pre-data transport-plan receipt that can be filled safely, or reclassify BS-6 as a post-freeze execution gate that is explicitly not part of the document-freeze prerequisite. Make the preamble, slot register, and §9 sequence use the same state machine.

## Attacks that did not break

1. **Centred-slope permutation variance.** I exhaustively enumerated all 24 label permutations for `c=[-1.0,-0.2,0.4,0.9]`, `s=[-1,-1,+1,+1]`. The empirical slope variance was `0.664176006642`, exactly matching `Var(s)/((N−1)Var(c)) = 0.664176006642`. V2's repaired §3 formula is correct.
2. **Footprint asymmetry and ±1 discreteness.** Conditional on the stated model `E[s|c]=Ac`, centring makes the slope expectation A for any fixed footprint, including nonzero `c̄`. At `A=0.0408` and `c∈[-1,1]`, the required `P(s=+1|c)=(1+Ac)/2` lies in `[0.4796,0.5204]`; discreteness does not invalidate the model. Finding 2 arises only because V2 separately introduces imperfect labelling without connecting it to that model.
3. **Decision partition.** For valid numeric p-values, strict `p<0.001`, strict `p>0.05`, and “any other” make the boundary values `p=0.001` and `p=0.05` INCONCLUSIVE. The numeric regions are exhaustive and mutually exclusive.
4. **Other V3 values.** The published amplitude, published uncertainty, both axis renderings, F-5 oriented sign, F-6 thresholds, F-7 factor 3.09, `flux_r>0`, and `dered_mag_r<17.7` are present with the values V2 states. Finding 1 is the sole quotation-fidelity break I found.
5. **AGY repair trace.** F1, F2, F3's `E[cos²θ]` mismatch, F5, and F8 are repaired at the textual level. F4 fails against the hash-pinned Cut-6 provenance (Finding 1); F6 names an agreement tolerance but the named implementations cannot satisfy it (Finding 4); F7 is now mathematical rather than a printed sentence but remains vacuous without a permutation resolution (Finding 5).

## Testimony

None. The findings above are grounded in the pinned files, cited line ranges, and the shown read-only commands/calculations.

**REFUSED** — blocking findings 1, 2, 3, 4, 5, and 6.
