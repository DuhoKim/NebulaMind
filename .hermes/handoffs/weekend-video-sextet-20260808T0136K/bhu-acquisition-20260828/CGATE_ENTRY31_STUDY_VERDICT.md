STUDY_UNSOUND_SMOLIN_SENTENCE_IS_TEMPORAL_DESCRIPTION_NOT_PERMANENT_INSTRUMENT_CRITERION
SIGMAS_CONFIRMED:   YES
INFERENCE_HOLDS:    NO
THIRD_READING:      method-agnostic precision with secure neutron-star identification

# Dispositive defect

The headline does not survive the source. Smolin does **not** define binary-pulsar data as a
permanent admissibility criterion. After deriving the proposed falsifier, he writes:

> “Presently all well measured neutron star masses are from binary pulsar data and are all below
> 1.5 M_sun. But an observation of a heavy neutron star may be made at any time.”

“Presently” makes the sentence a report about the evidence available in 2004. The footnote attached
to it is more decisive:

> “Other methods yield less precise estimates [58].”

That footnote acknowledges other methods and ranks them by precision; it does not exclude them by
instrument. Reference 58 is the dynamical mass of the neutron star in Cyg X-2. The operative
criterion supported by the passage is therefore method-agnostic: is the object securely a neutron
star, is its mass sufficiently high, and is the estimate sufficiently precise? On that reading,
J0740 and J0952 are not alternative “branches” from which one must choose. They are two estimates
with different likelihoods and systematics. Duho's instruction to keep both is consistent with this
reading; the study's claim that “the instrument decides it” is not.

This invalidates the headline and its downstream claims that the corpus has four mutually competing
“readings,” that radio timing has special textual standing, and that choosing an instrument decides
whether the falsifier is live. Measurement quality and object classification matter; Smolin does not
legislate an instrument whitelist.

# Independent arithmetic and source values

Smolin's proposed certain bar is correctly read. His paper says:

> “Sufficiently high is certainly 2.5 M_sun,”

with the separate conditional statement that a value above 1.5 M_sun would be “troubling” if one is
completely confident in the Bethe--Brown limit.

The pinned Fonseca paper reports J0740 as

> “m_p = 2.08 +0.07/-0.07 M_sun (68.3% credibility)”

from relativistic Shapiro time delay. Independently computing against 2.5 gives
`z = (2.50 - 2.08)/0.07 = 6.0000` and, under the study's Gaussian approximation,
`P(M > 2.5) = 9.8659e-10`.

The pinned Romani paper reports J0952 as

> “M_NS = 2.35 +/- 0.17 M_sun,”

not +/-0.11. Independently, `z = (2.50 - 2.35)/0.17 = 0.88235` and the Gaussian
one-sided probability is `0.188793` (18.88%). Thus the requested 6.0 and 0.88 sigma
figures are confirmed, conditional on approximating the reported uncertainties as Gaussian.

The +/-0.11 value has no origin in the pinned 2022 paper set, but it is not an unexplained value in
the literature as of this audit. Romani et al., *PSR J0952-0607: Tightening a Record-High Neutron
Star Mass* (arXiv:2512.05099, submitted 2025-12-04), reports `2.35 +/- 0.11 M_sun`. It gives
`z = 1.36364` and `P(M > 2.5) = 0.086341` under the same approximation. Therefore the study is right
about what the pinned 2022 source says, but its rhetoric that +/-0.11 “belongs to none” of the
measurements is obsolete and materially misleading.

# Drift audit

The two radio numbers are correctly quoted: Cromartie 2020 gives `2.14 +0.10/-0.09`, and Fonseca
2021 gives `2.08 +/-0.07`. Symmetrizing the first uncertainty to 0.095 reproduces the script:

* old tail: `z = 3.78947`, `P = 7.54834e-5`;
* new tail: `z = 6.00000`, `P = 9.86588e-10`;
* ratio: `76,509.6`.

The number is reproducible, but “drift” and “two epochs” overstate what it establishes. Fonseca says
it combines about 1.5 years of additional high-cadence data **with previous measurements** and
“confirms and improves upon previous estimates.” These are nested, partially overlapping analyses
of one constant mass, not independent epoch measurements or evidence of physical/temporal drift.
The defensible statement is that the posterior was revised downward and tightened.

The black-widow claim is false as a current literature claim. The 2025 follow-up revises the same
J0952 result from `2.35 +/-0.17` to `2.35 +/-0.11`; the corresponding Gaussian mass above 2.5 falls
from 18.88% to 8.63%, a factor of about 2.19. It was not a **prior** measurement available to the
2022 paper, but it is a measurement history available on the audit date. The b5 absence regex could
never establish the claimed corpus-wide or literature-wide absence.

# Gravitational-wave leg

The pinned numbers are transcribed correctly. The GW190814 discovery paper gives a secondary mass
of `2.50-2.67 M_sun` at 90% credibility and says it is

> “either the lightest black hole or the heaviest neutron star ever discovered in a double
> compact-object system.”

Hence the reported **90% interval** is wholly at or above 2.5, but “FIRES” remains conditional on
the secondary being a neutron star and does not mean the full posterior is above the bar.

The GW170817/GW190814 tension paper says GW170817 suggests `M_TOV <=~2.3 M_sun`, while GW190814
requires `M_TOV >=~2.5 M_sun` if its secondary was a non- or slowly rotating neutron star. It reports
`M_TOV = 2.210 +0.116/-0.123 M_sun` at 2 sigma, i.e. `[2.087, 2.326]`; 2.5 is above that interval.

The table nevertheless compares unlike summaries: a 90% credible interval for an individual
compact object's mass against a stated 2-sigma confidence range for a model-derived nonrotating
maximum mass. The qualitative tension is real and is stated by the paper, but the rows are neither
commensurate confidence statements nor two direct “measurements of the maximum neutron-star mass.”
GW190814 supplies a conditional lower bound on M_TOV only after a neutron-star and spin assumption.

# Third reading

A third reading is already implied by Smolin's footnote: accept any method that yields a sufficiently
precise mass for an object securely classified as a neutron star. Modern examples can include optical
dynamical modelling, X-ray pulse-profile modelling, and gravitational-wave inference, with their
method-specific systematics carried rather than turned into mutually exclusive branches. This reading
produces neither “radio wins” nor “optical wins”: all likelihoods remain evidence, and GW190814 remains
conditional because identity, not instrument, is unresolved.

# Script reproduction and name/predicate audit

All scripts reproduced their advertised totals: b4 `6/6` (the prompt's `7/7` is stale), b5 `2/2`,
and b6 `4/4`. PASS is not probative because these names exceed their predicates:

1. **b4 “Smolin names BINARY PULSAR DATA as what counts as well-measured”**: the predicate only
   finds the sentence. It does not test the permanent-criterion interpretation, and the surrounding
   text and footnote contradict that interpretation.
2. **b4 “both masses read from their own pinned papers”**: each fallback is disconnected presence
   of two number strings; it does not bind a value to an uncertainty, object, method, or confidence.
3. **b4 “instrument choice changes this ... opposite conclusions”**: the arithmetic uses hard-coded
   masses and errors and does not test that an instrument must be chosen or that Smolin requires one.
4. **b4 “the 0.11 has no pinned origin”** appears only in detail and is never tested by any predicate.
5. **b5 “drift claim is TRUE”**: the predicate tests two hard-coded Gaussian tails plus a weak source
   hit. It does not test independence, temporal drift, or commensurability of the analyses.
6. **b5 “one measurement and no history”**: the predicate counts only three narrowly phrased regex
   forms inside one paper. It neither counts measurements nor searches references/literature. It is
   false on the audit date while reporting PASS.
7. **b6 “entire 90% credible interval ... at or above”**: the predicate only finds the range string;
   “90%,” association with the secondary, and interval semantics are not tested.
8. **b6 “declines to classify”**: an `either ... or` substring supports ambiguity but does not by
   itself test a deliberate refusal or the asserted consequence for Smolin's bar.
9. **b6 “if and only if”**: the predicate checks disconnected occurrences of `requiring` and
   `if the secondary was a`; it does not establish **only if**, and the quoted source says “if,” not
   “if and only if.” Rotation supplies an expressly discussed alternative.
10. **b6 “paper's own 2-sigma interval”**: source detection falls back to disconnected number
    presence, while the interval and comparison are computed from hard-coded constants.

The decisive false pass is b5's black-widow-history check. The decisive study failure, however, is
prior to all arithmetic: the permanent-instrument criterion is not in Smolin's argument.
