PASS_P3C

# Cross-engine Gate C verdict — Track C

Verdict: PASS. I reached this independently from the named source files and reran the executable receipt. Track C’s narrow result survives: Smolin’s preprint supplies a local-black-hole-maximum argument and a 2.5 M_sun clean-refutation bound; it does not originate Brown–Lee–Rho’s 4% double-neutron-star limb or independently derive Brown–Bethe’s numerical 1.5 M_sun ceiling. The result remains context-grade because the decisive Smolin text is an unpublished preprint.

## 1. Central claim — PASS, with a wording caveat

Smolin defines the governing condition as a local maximum, not as a free-standing neutron-star-mass postulate. In `sources/smolin_ns_clean.txt:96-99`:

> “If p is changed from the present value in any direction in P the first significant changes in B(p) encountered must be to decrease B(p).”

Section 2 then supplies the parameter diagnostic. It says that below the critical strange-quark mass the upper mass is “low, approximately 1.5 M_sun,” while above it conventional equations of state put the limit “almost certainly above 2” (`sources/smolin_ns_clean.txt:188-193`). A sufficiently massive neutron star would establish the high-mu side (`:194-200`). The quoted sentence does perform the claimed logical work (`:201-204`):

> “this would refute S because it would then be the case that a decrease of mu would lead to a world with a lower upper mass limit for neutron stars, and therefor more black holes.”

That is a local-gradient contradiction: the proposed decrease raises black-hole production when S requires the first significant change in every direction to lower it.

The strongest fair counter-reading is real. Because Smolin says a pulsar above 2.5 M_sun would refute S in both the abstract and conclusion, S plus the Bethe–Brown mapping does make a one-sided observational prediction: no such heavy pulsar. In that operational sense Smolin does effectively predict a low-enough maximum mass, even though the numerical 1.5 M_sun value is imported from Bethe–Brown rather than derived by CNS. Track C now acknowledges exactly this at `TRACK_C_AUDIT.md:29-31`:

> “calling it ‘never a prediction’ overshoots — a falsifiable upper bound is a one-sided prediction in the Popperian sense”

and narrows the surviving claim to:

> “CNS does not predict the specific number ≈1.5 M_sun; that is Brown–Bethe’s.”

Therefore the document’s “diagnostic” language is acceptable only with its own explicit qualification; read literally as “not predictive in any sense,” it would be too strong. The qualification is present in the gated artifact, so this is not a HOLD.

## 2. The 2.5 versus 2.0 claim — PASS

The 2.5 M_sun clean-refutation wording occurs in both required locations.

Abstract, `sources/smolin_ns_clean.txt:21-29`:

> “The first, the observation of a pulsar with mass greater than 2.5 M_sun, would cleanly refute the theory.”

Section 5, `sources/smolin_ns_clean.txt:404-407`:

> “the discovery of a pulsar with mass above 2.5 M_sun would refute S.”

The weaker form is also present in Section 2, `sources/smolin_ns_clean.txt:197-200`:

> “Sufficiently high is certainly 2.5 M_sun, although if one is completely confident of Bethe and Brown’s upper limit of 1.5 solar masses, any value higher than this would be troubling.”

Track C does not suppress that qualification. It quotes it at `TRACK_C_AUDIT.md:43-45`, and the receipt docstring repeats it at `receipts/r5_smolin_threshold.py:4-8`. Brown–Lee–Rho’s separate published wording is also explicit in `sources/blr_clean.txt:44-46`: their CNS-attributed quotation uses a mass “appreciably” above the Brown–Bethe maximum, while their HLS/kaon falsifier uses approximately 2 M_sun.

Independent rerun:

`python3 receipts/r5_smolin_threshold.py` exited 0 and printed:

> `PSR J0740+6620  2.080+/-0.070  -6.0s` versus 2.5
>
> `PSR J1614-2230  1.928+/-0.017  -33.6s` versus 2.5
>
> `PSR J0952-0607  2.350+/-0.170  -0.9s` versus 2.5, excluded class

The receipt’s statement that the heaviest qualifying object is 6.0 sigma below 2.5 reproduces exactly. Track C’s comparison is transparent about provenance: 2.5 comes from the context-grade Smolin preprint; 2.0 comes from published Brown–Lee–Rho and the lane preregistration.

## 3. Negative search — PASS; independently robust to synonyms

A case-insensitive line scan and a second whole-text scan with whitespace normalized both returned zero for:

- `4%`, `four percent`, `four per cent`, and `0.04`;
- `asymmetr`, `double neutron`, and `double-neutron`;
- `mass ratio`, `unequal`, `binary pulsar masses`, `difference in mass`, and `different from each other`;
- `two neutron stars`, `both neutron stars`, `companion mass`, and `double pulsar`.

The two apparent near-hits do not hide the claimed test:

- `binary pulsar` occurs once at `sources/smolin_ns_clean.txt:206-208`: “all well measured neutron star masses are from binary pulsar data and are all below 1.5 M_sun.” This concerns the provenance of individual mass measurements, not within-binary asymmetry.
- Normalized `mass difference` occurs once through the Section 2 footnote at `:225-227`, referring to the “proton-neutron mass difference,” not two stellar masses.

Regex probes for mass within 80 characters of ratio/difference/unequal/asymmetry found only that proton–neutron footnote; a probe for pair/double/both language near “neutron star” found zero.

By contrast Brown–Lee–Rho state the 4% condition explicitly in `sources/blr_clean.txt:45`:

> “Find a well measured double neutron star binary in which the two neutron stars are more than 4% different from each other … Then the BB theory will be falsified.”

The negative is genuine: this is not a test proposed in Smolin’s preprint. One wording caution remains: `TRACK_C_AUDIT.md:66` says flatly that it “is not a CNS falsifier.” Read broadly, Brown–Lee–Rho did place it in a chain that included CNS. Track C’s Section 4 supplies the needed precision by preserving the “chain as [Brown–Lee–Rho] state it” verdict and attributing the second test to Brown–Lee–Rho. The defensible finding is that it is not Smolin’s test.

## 4. Overreach on our own record — PASS; no strawman

The C08 adjudication does not say the 4% limb is one of Smolin’s own tests. It says at `../bhu-mass-adjudication-20260817/C08_MASS_ADJUDICATION_20260817.md:122-124`:

> “the mass evidence FALSIFIES the chain as the source states it, via the source’s own second falsifier limb”

where that source is Brown–Lee–Rho. Its per-link discussion nevertheless does make the claim Track C is correcting. At `:137-142` it says:

> “CNS’s flagship falsifiable prediction … is gone. CNS as a hypothesis is not thereby refuted; it can retreat from the Brown–Bethe EOS route, at the price of no longer being tested by this channel.”

The actual lane-2 page also contains the language, so Track C is not knocking down an invented record. `/Users/duhokim/HermesOps/cockpit/bhu-lane2-status.html:24` says:

> “Settled: the chain fails by its author’s own second test”

and line 28 says:

> “Smolin’s hypothesis is not refuted either — it loses its flagship falsifiable prediction and can leave this route, at the price of no longer being tested by this channel.”

The page identifies Brown–Lee–Rho as the authors of the two-limb chain at lines 26-27, so “author’s own second test” is not misattribution to Smolin. But its separate “flagship” sentence is exactly the substantive sentence Track C disputes. Track C also says the C08 per-link verdict survives (`TRACK_C_AUDIT.md:68-75`). This is sharpening a real statement, not reversing C08 or constructing a strawman.

## 5. Source-status discipline — PASS

The source-class limitation is prominent before, during, and after the substantive argument:

- Headline, `TRACK_C_AUDIT.md:8-11`: the answer is “established from a preprint,” is “context-grade rather than a verdict on the published record,” and concerns the specific 1.5 M_sun claim.
- Section 1 entry, `:15-16`: “source status flagged hard in §5 below.”
- Section 5 lead, `:86-91`: “This finding rests on a preprint” and the conclusion is “context-grade, not base-layer,” which “must not be presented as a verdict on the published record.”
- Acquisition boundary, `:93-102`: both published Smolin sources are listed as unobtained, and B-18 remains “UNVERIFIED-AT-GATE rather than resolved.”
- Receipt, `receipts/r5_smolin_threshold.py:4`: the source is labeled “preprint; context-only under the published-base-layer rule.”

This is sufficiently prominent. No conclusion silently promotes the preprint to the peer-reviewed base layer. The assertive conclusions in Sections 1-4 are claims about what this preprint says and are globally and locally downgraded; the base-layer row is expressly left unresolved.

UNVERIFIED-AT-GATE: I did not independently refresh the current INSPIRE record because the order forbids network access. The unpublished/context-only source classification is a binding premise of this gate and is stated consistently throughout the artifact; this limitation does not prevent checking whether Track C honors that class.

## 6. Overclaim sweep — PASS

Track C does not generalize from CNS to black-hole-universe cosmology. Its sole lexical encounter with the prohibited general claim is inside an explicit rejection at `TRACK_C_AUDIT.md:110` (“would be false and is not said”), followed by “this concerns CNS, one branch of 28 papers.” The Phase 3 boundary says the same at `PHASE3_BRIEF.md:61-63`.

No `vindicat*` or `support*` wording appears in Track C. Its positive-status formulation is limited to non-refutation by this mass threshold: `TRACK_C_AUDIT.md:76-77` says, “On Smolin’s own stated criterion — a pulsar above 2.5 M_sun — CNS has not been refuted,” immediately backed by the 6-sigma shortfall. That is not evidence for CNS and is not presented as such.

## Independent gate conclusion

All six checks pass. The central semantic caveat is real but already repaired inside Track C: mass is diagnostic of the local parameter gradient and also a one-sided prediction once Smolin’s auxiliary Bethe–Brown assumptions are accepted. The defensible lane correction is narrower than “CNS predicts no mass bound”: Smolin does not derive the approximately 1.5 M_sun number, and the 4% double-neutron-star limb is Brown–Lee–Rho’s test, not Smolin’s. Track C keeps that conclusion context-grade and does not overturn the published C08 chain verdict.

— Cross-engine reviewer: Hermes Agent, OpenAI gpt-5.6-sol via openai-codex, 2026-08-21 KST
