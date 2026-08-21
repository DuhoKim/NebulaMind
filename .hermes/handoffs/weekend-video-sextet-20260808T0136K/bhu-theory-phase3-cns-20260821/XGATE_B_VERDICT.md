PASS_P3B

# Cross-engine Gate B verdict — Track B

## Independent verdict

PASS. The reversal is substantively sound and is not an attempt to erase an inconvenient valid result. BLR's helium-red-giant deposit is not an uncosted evolutionary channel: in the modern DNS sequence reviewed by Tauris it falls within post-CE neutron-star/helium-star accretion, especially Case BB Roche-lobe overflow. Tauris's source-level ceiling is <0.02 M⊙, which is far below BLR's 0.1–0.2 M⊙ proviso.

Two qualifications are required. First, 0.0134 M⊙ is the auditor's arithmetic subtotal, not Tauris's stated all-phase ceiling; the source's own generous total is <0.02 M⊙. Second, Tauris supplies a modern formation-model bound and population argument, not a direct measurement of how much J1913+1102 accreted, so the SETTLED sentence "was 0.1–0.2 M⊙ actually deposited? NO" is too categorical. Neither qualification rescues the 5.1σ interpretation or breaks the reversal because the current finding records the <0.02 M⊙ correction and preserves the genuinely valid discovery that BLR did quantify the caveat.

## 1. The 4% derivation — verified

BLR says, without an intervening auditor step:

> "Helium burning takes up 10% of the star lifetime ... To go from lifetimes to masses one must divide by about 2.5, so the two giant progenitors must be within 4% of each other in mass." (`sources/blr_physrept_clean.txt:1119-1123`)

Thus the 10%, divisor 2.5, and resulting 4% are all the source's. The arithmetic 0.10/2.5 = 0.04 reran exactly in R2 and in an independent calculation.

The explanatory scaling in `TRACK_B_INTERIM_FINDING.md:16`, "τ ∝ M/L and L ∝ M³·⁵, so τ ∝ M⁻²·⁵," is not present in BLR Sec. 3.2. It is auditor-supplied reconstruction. It is physically consistent as the usual local main-sequence approximation: available fuel scales approximately with M, luminosity as M^3.5, so lifetime scales as M^-2.5 and |dτ/τ| ≈ 2.5|dM/M|. It should not be attributed to BLR. The later gate note correctly labels this at `TRACK_B_INTERIM_FINDING.md:151-152`.

## 2. The proviso quote — verified

BLR states:

> "During the helium burning red giant, ∼0.1 to 0.2 M⊙ can be deposited on the first born neutron star by the helium star companion, and the first born neutron star should be that much more massive than the other, in addition to the possible ∼4% difference in mass..." (`sources/blr_physrept_clean.txt:1139-1144`)

The interim quotation at `TRACK_B_INTERIM_FINDING.md:26-28` is accurate, including "in addition to." The scope is not generic: BLR introduces it for "the lower mass neutron stars in the double pulsars J0737−3039 and J1756−2251" (`sources/blr_physrept_clean.txt:1133-1136`). BLR later says that the 0.1–0.2 M⊙ value came from a hypercritical-accretion calculation during the He-red-giant phase (`sources/blr_physrept_clean.txt:1190-1197`).

## 3. The J1913+1102 channel and mass direction — verified

Ferdman groups J1913+1102 with precisely the two BLR examples:

> "PSR J1913+1102 is part of a population of several very close DNS binary systems ... (e.g. PSRs J0737−3039A/B and J1756−2251). These imply an evolutionary path in which the second-formed NS was born as a result of an envelope-stripped helium star progenitor..." (`sources/ferdman2020_clean.txt:83`)

Ferdman also identifies the observed pulsar as the first-formed NS and says it "was subsequently recycled by accretion of matter from the progenitor to the second NS" (`sources/ferdman2020_clean.txt:74-75`). The masses are 1.62 ± 0.03 M⊙ for that pulsar and 1.27 ± 0.03 M⊙ for the companion (`sources/ferdman2020_clean.txt:79-80`). Therefore the first-born NS is the heavier component, exactly the direction BLR's deposit predicts. R3 reproduces this direction check.

Ferdman's single sentence does not itself say "helium red giant" or quantify Case BB accretion. It establishes the stripped-He-star channel and mass ordering; the phase identification comes from Tauris's explicit DNS evolution sequence below.

## 4. The crux: the phase mapping survives adversarial attack

BLR's proviso has three defining elements: the second progenitor has reached a helium-burning red-giant stage, the donor is a helium-star companion, and matter reaches the already formed first NS (`sources/blr_physrept_clean.txt:1133-1144`).

Tauris lays out the matching sequence. After the hydrogen-rich common envelope is ejected, "it consists of a NS orbiting a helium star"; depending on separation and helium-star mass, "an additional phase of mass transfer ... Case BB RLO" occurs and recycles the NS (`sources/tauris2017_clean.txt:249-261`). Tauris defines Case BB more tightly as "mass transfer via Roche-lobe overflow from a naked helium star in the post-HMXB/post-CE system" (`sources/tauris2017_clean.txt:329-332`). That is the relevant modern name for the transfer geometry BLR calls the He-red-giant deposit.

The accretion inventory is expressly intended to be complete for the first-born NS in DNS formation: Tauris says it identified "five consecutive phases of evolution where the first-born NS in a DNS system will potentially accrete material," including CE, helium-star wind, and Case BB RLO (`sources/tauris2017_clean.txt:1322-1346`). It then states that the donor/progenitor of the second NS supplies potential accretion material to the first NS "in all above-mentioned phases" (`sources/tauris2017_clean.txt:1493-1495`) and sums those stages to <0.02 M⊙ (`sources/tauris2017_clean.txt:1511-1515`).

Therefore the reversal does not silently substitute an unrelated channel. BLR's He-star-to-first-NS transfer is covered, principally by Tauris's Case BB treatment, with CE and helium-star wind making the source-generous total broader still. No named BLR transfer geometry remains outside Tauris's five-stage inventory.

The real disagreement is accretion physics, not channel identity. BLR invokes hypercritical accretion (`sources/blr_physrept_clean.txt:1191-1197`). Tauris reviews the hypercritical-CE proposal (`sources/tauris2017_clean.txt:1403-1424`), adopts a much smaller CE allowance, and models Case BB around Eddington-limited accretion while allowing factors 2–3 above it (`sources/tauris2017_clean.txt:1450-1476`). This supports "modern DNS literature contradicts/supersedes BLR's magnitude," but not the stronger claim that J1913+1102's individual accreted mass was directly observed.

## 5. Tauris figures and the receipt ceiling — verified with a material label correction

### Source figures

- Common envelope: Tauris does adopt 0.01 M⊙, not merely mention it: "we take ΔM_NS = 0.01 M⊙ as a reasonable estimate for the upper limit" (`sources/tauris2017_clean.txt:1434-1435`). The same sentence retains uncertainty: further accretion cannot be fully ruled out.
- The 0.1 M⊙ number is MacLeod & Ramirez-Ruiz's upper limit. Tauris reports that their approximations "likely lead their calculations ... to be an overestimate" (`sources/tauris2017_clean.txt:1421-1424`). Tauris then gives the stated population argument: four DNS recycled components are below 1.38 M⊙, and accreting about 0.1 M⊙ would require birth masses below 1.28 M⊙, "unexpected ... in so many systems" (`sources/tauris2017_clean.txt:1426-1433`).
- Helium-star wind: "ΔM_NS < 4×10^-4 M⊙" over the wind-accretion phase of NS–helium-star binaries (`sources/tauris2017_clean.txt:1445-1448`).
- Baseline Case BB: 5×10^-5–3×10^-3 M⊙ for DNS-forming binaries (`sources/tauris2017_clean.txt:1461-1465`). Tauris also allows up to (6–9)×10^-3 M⊙ in a few cases (`sources/tauris2017_clean.txt:1471-1476`).
- Tauris's own all-stage conclusion is <0.02 M⊙ (`sources/tauris2017_clean.txt:1511-1515`; also the abstract at `:64-66`).

### What 0.0134 M⊙ is and is not

0.0134 M⊙ is correctly computed as 0.01 + 0.0004 + 0.003. It is nevertheless auditor-constructed; Tauris does not print that sum. It is not "every phase at maximum": it omits the earlier HMXB-wind contribution of a few ×10^-3 M⊙ (`sources/tauris2017_clean.txt:1392-1393`), the exceptional 0.006–0.009 M⊙ Case BB range, and the very small shell-impact term. R4's printed label "TOTAL (all phases, each at max)" is therefore false as a source description even though its arithmetic is correct.

The current finding recognizes this at `TRACK_B_INTERIM_FINDING.md:149-150` and adopts the source's approximately 0.02 M⊙ generous ceiling. The reversal should rest on Tauris's <0.02 M⊙, not on calling 0.0134 M⊙ an all-phase maximum. With 0.02 M⊙, BLR's 0.1–0.2 M⊙ is larger by about 5–10×; "several-to-tenfold" is more exact than an unqualified "order of magnitude."

## 6. Receipt reruns and independent arithmetic

All four receipts were run with `python3`; all exited 0:

- `receipts/r1_entropy.py`: 1.0494×10^77 k_B, 0.05% from the printed coefficient; `R1 PASS`.
- `receipts/r2_four_percent.py`: 4.0%; its 0, 0.1, and 0.2 M⊙ rows reproduce 22.8σ, 13.9σ, and 5.1σ using the script's 2026-update masses.
- `receipts/r3_channel_settled.py`: Ferdman rows reproduce 7.1σ bare and 2.3σ with a 0.2 M⊙ deposit; the mass-direction check matches.
- `receipts/r4_accreted_mass.py`: arithmetic sum 0.0134 M⊙ and the script's 21.6σ row reproduce, subject to the ceiling-label defect above.

Independent Python arithmetic reproduced 0.10/2.5 = 0.04 and 0.01 + 0.0004 + 0.003 = 0.0134. Using the in-scope Ferdman masses, the independently computed excesses are 7.05σ bare, 6.74σ with 0.0134 M⊙, 6.58σ with Tauris's 0.02 M⊙ ceiling, and 2.34σ if BLR's full 0.2 M⊙ were retained.

UNVERIFIED-AT-GATE: the exact 5.1σ, 21.6σ, and 21.0σ margins depend on the tighter 2026 A&A masses, which were not one of the three primary sources named for this gate. The current finding itself discloses this at `TRACK_B_INTERIM_FINDING.md:153-158`. The reversal's direction is verified from Ferdman; those exact headline margins are not independently source-gated here.

## 7. Over-correction check — no over-retraction

The original track made one durable correction: the He-red-giant caveat is quantified in BLR's companion Phys. Rept. paper, contrary to the adjudication's treatment of it as unquantified. That remains true from `sources/blr_physrept_clean.txt:1133-1144` regardless of whether BLR's magnitude survives modern modelling.

The SETTLED text explicitly keeps this point: "the caveat is quantified" and the verdict survives because the modern DNS literature contradicts the size, not because the caveat lacks a number (`TRACK_B_INTERIM_FINDING.md:122-127`). The later gate record again says the quantification survives (`TRACK_B_INTERIM_FINDING.md:139-145`). Only the conditional choice to use 0.2 M⊙ as the present-day ceiling is withdrawn. That is the correct boundary; the author did not discard the valid result.

## 8. Overclaim sweep — clean

A targeted search of `TRACK_B_INTERIM_FINDING.md` returned zero CNS-level verdicts and zero BHU-wide generalizations. The finding stays on the DNS mass-asymmetry limb and the accretion-margin question. The prohibited BHU-wide formulation is absent. This is consistent with the Phase 3 boundary at `PHASE3_BRIEF.md:61-68`.

## Bottom line

The decisive mapping is justified by the primary sources. The reversal should be expressed as a model-and-literature adjudication using Tauris's <0.02 M⊙ all-stage ceiling, not as a direct measurement of J1913+1102 and not as a 0.0134 M⊙ source-printed maximum. With those already substantially acknowledged qualifications, the reversal stands, the valuable caveat-quantification correction remains, and no HOLD condition is met.

— Cross-engine reviewer: OpenAI GPT-5.6 Sol (Codex runtime), 2026-08-21 19:22 KST. Independent adversarial reading; findings only; no network.
