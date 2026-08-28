# T2b — Calibration-contract SEMANTICS (Shape-2, C41 Track-B)

Lane: `c41-trackb-shape2-mzr-20260804T1452K`
Author: Lana (semantics half, per F6 re-scope: semantics stay Hwao+Lana; conversion-table /
metrology MACHINERY is Goru's T2-machinery deliverable, Kun verifying).
Sources: `MEASUREMENT_DESIGN_V1.md` (v2 revision block; F1/F3/F4 govern this document) and
`KUN_DESIGN_REFUTATION.md` (verdict DESIGN_SOUND_WITH_PATCHES).

**Scope rule for this document.** This file defines terms and decision rules. It contains no
conversion tables, no adopted coefficients, and no numbers of its own. The only magnitudes that
appear are the three discrepancy CLASSES already stated in the design — the ~0.24 dex
Te-vs-strong-line O/H class, the ~0.15 dex per-anchor Te-scale class, and the ~1.4 dex
UV-vs-optical (N/O) channel class — and they appear here as named classes to be instantiated by
the machinery half, never as adopted values. Wherever a rule below needs a number (a conversion,
an uncertainty, a forecast threshold), the rule names the artifact that must supply it.

---

## §1. What constitutes a "declared scale"

**Definition (declared scale).** A metallicity or abundance value is *on a declared scale* if and
only if all four of the following are recorded in the per-sample provenance manifest (T1) or the
machinery tables (T2-machinery) before that value enters any comparison:

1. **Method identity** — the named diagnostic and calibration used to produce the value
   (e.g. "direct-Te via [O III] λ4363", "strong-line calibration X as published by source Y"),
   cited to the source publication, not paraphrased.
2. **Reference frame** — the Te-anchored scale it is expressed on, or the explicit, cited
   conversion by which it is brought onto that scale. The conversion must be an entry in the
   T2-machinery conversion tables; a conversion that exists only in prose is not declared.
3. **Propagated conversion uncertainty** — the conversion's own uncertainty term, carried as a
   separate, identifiable component of the value's error budget (not absorbed into a generic
   "systematic" term).
4. **Channel label** — the abundance channel (§4) and quantity type (O/H vs abundance ratio,
   §4.3) the value belongs to.

**Exclusion rule (by rule, not judgment).** A value failing ANY of the four conditions is
*undeclared-scale* and is excluded from every compared quantity. Exclusion is mechanical: the
test is "are the four fields present and cited?", never "does the value look reasonable?". An
excluded value may still appear in the provenance manifest, flagged `undeclared_scale`, so the
exclusion itself is auditable.

**Testability.** For any row in any compared sample, an auditor (Kun, T4) must be able to point
to: the manifest entry satisfying (1) and (4), the machinery-table entry satisfying (2) and (3).
If any pointer dangles, the row was included in violation of the contract — that is a T4-reportable
defect, not a discretionary call.

## §2. Scale-limited vs detection — the decision rule

Let a claimed offset (deficit, FMR offset) be Δ with total uncertainty budget decomposed, per
§1.3, into a statistical term and the sample's own **scale uncertainty** — the combined declared
conversion + anchor-scale terms applicable to that specific sample (instantiated by
T2-machinery from the 0.24 dex class and the 0.15 dex Te-scale class as applicable; this
document does not fix the combination rule, only requires that it be fixed there, in writing,
before use).

**Rule S (verbatim consequence of the design, made testable).**

- If |Δ| ≤ (that sample's scale uncertainty), the result is reported as **scale-limited**. The
  words "detection", "detected", "measured deficit of" are barred from the reported statement;
  the licensed form is the null template of §6.
- If |Δ| > (that sample's scale uncertainty), the result MAY be reported as a detection, subject
  to the ordinary statistical significance of Δ against its statistical term — the scale floor
  is a necessary gate, not a sufficient one.
- The comparison is made against the scale uncertainty **of the sample that produced Δ**, never
  against a global or best-case scale term. Mixed samples inherit the worst applicable scale
  term of their members unless the machinery tables define a propagated combination.

**No retro-shrinking.** The scale uncertainty used in Rule S is the one frozen in the machinery
tables before the science fetch (F4 discipline). Recomputing a smaller scale term after seeing Δ,
and thereby promoting a scale-limited result to a detection, is a contract violation regardless
of the technical merit of the recomputation. (The reverse — enlarging the term post hoc and
demoting a detection — is permitted, with the change logged.)

**Precedent note.** This rule is the generalization of the crew's z9-10 discipline
("systematic-limited — the formal value is NOT a detection"); the z9-10 anchor set, when reused,
enters already carrying that classification and its published error budget (design F2).

## §3. Te-anchor classes — what qualifies

Every sample member is assigned exactly one of the following classes in the T1 manifest. The
classes are exhaustive and mutually exclusive; class assignment is by measurement content, never
by the value obtained (Step-1 conclusion-blindness).

- **Class A — direct auroral detection.** An auroral line (e.g. [O III] λ4363, O III] λ1666
  serving the Te method, [N II] λ5755-class) detected at the source's stated detection criterion,
  with Te derived and O/H computed by the direct method in the cited source. Class A members are
  *anchors*: they define the Te-anchored scale locally and may enter comparisons without
  conversion (their per-anchor Te-scale term — the 0.15 dex class — still enters the budget
  per §2).
- **Class B — Te-consistent limit.** Auroral line not detected, but the source publishes a
  quantitative limit propagated to a Te or O/H limit by the direct method. Class B members enter
  only quantities defined for censored data; they never anchor a scale and never enter a mean as
  if detected.
- **Class C — strong-line on a declared scale.** No auroral information; value produced by a
  strong-line calibration satisfying all of §1. Class C members enter comparisons ONLY through
  their declared conversion and never serve as anchors.
- **Class X — excluded.** Fails §1 (undeclared scale), or auroral claim not traceable to the
  cited source. Recorded, flagged, not compared.

**Qualification boundary (testable).** "Has an auroral detection" means the DETECTION criterion
is the source's own published one, cited in the manifest. This contract does not set a
signal-to-noise threshold; it requires that whichever threshold is used (a) pre-exists this
study, (b) is cited, and (c) is applied uniformly within a sample. Promoting a Class B member to
Class A on the strength of a re-measurement performed inside this lane is barred — re-measurement
is not in this design's data plan, and such a promotion would make the anchor set
result-contingent.

**Anchor sufficiency is T2a's business, not a class property.** Whether N Class-A anchors in a
bin suffice for a given precision is answered exclusively by the frozen T2a forecast (§6); no
per-bin judgment of "enough anchors" is made anywhere else.

## §4. Channel separation — UV vs optical, and ratios (design F3)

**4.1 Channels are separate declared scales.** UV-line diagnostics (e.g. N IV] λλ1483,1486-class,
O III] λ1666-class, C-line diagnostics) and optical-line diagnostics (e.g. [N II] λ6583-class,
[O III] λ5007/λ4363-class) constitute distinct abundance channels. A declared scale (§1) is
declared *within one channel*; no §1 declaration spans channels implicitly.

**4.2 Cross-channel comparison rule.** UV-derived and optical-derived abundances are never mixed
in one compared quantity unless the comparison carries an **explicitly declared cross-channel
systematic term**: a named, cited, per-channel-pair term entered in the T2-machinery tables
before use. The ~1.4 dex N/O UV-vs-optical class is the design's stated magnitude class for why
this term cannot be assumed negligible; its instantiated value for any given pair is the
machinery's to supply. Absent that term, the comparison simply does not run — the members remain
in their own channels.

**4.3 Ratios are not O/H.** Abundance ratios (N/O, C/O, and kin) are separate quantity types
with their own scales. No O/H-scale conversion is reused for an X/O ratio without a per-channel,
per-ratio validation entry in the machinery tables. A declaration under §1 states which quantity
type it covers; coverage of O/H confers nothing for N/O.

**4.4 Channel-anomaly rule.** If two channels yield abundances for the same objects (or the same
stack) discrepant by more than twice their combined declared uncertainty, the discrepancy is
reported as a **channel anomaly** — a finding in its own right — and is never averaged away or
resolved by preferring one channel post hoc. (This is Kun's F3 clause adopted verbatim in
substance; the factor two is part of the adopted rule, not a new number introduced here.)

## §5. Lensing inheritance — declaration requirements (design F1)

Every sample declares, **per galaxy**, a lensing status:

- **`field`** — not behind a cluster/lens; magnification treated as unity with no lens-model
  dependence.
- **`lensed-with-model`** — magnified, with a published lens model; the magnification μ AND its
  uncertainty (including lens-model-to-lens-model scatter where the source provides it) are
  recorded, and the μ uncertainty is **propagated into the stellar-mass error** used for
  matched-mass binning.
- **`cluster-line-of-sight`** — behind a cluster but without a usable per-object magnification;
  treated as scale-undeclared for mass (excluded from matched-mass comparisons; may appear in
  channel or feasibility statements only, flagged).

**Stratum rule.** `field` and lensed strata are never combined into a single deficit or FMR
statistic. Lensed low-mass bins either (a) stay out of the deficit re-test, or (b) form a
separate, labelled stratum whose result is reported alongside — never averaged with — the field
stratum. Any statement about the lensed stratum carries its magnification-inheritance chain
(which lens models, whose μ, what scatter term) in the same breath.

**Inheritance chain declaration.** For the named 10^5.7 lensing-cluster sample specifically, and
for any lensed sample generally, the T1 manifest records the chain: source survey → lens
model(s) → μ per object → mass correction → mass uncertainty term. If the public table does not
carry per-object μ, the sample's lensed members are `cluster-line-of-sight` by default — the
absence of magnification data is a declaration of exclusion, not an invitation to assume μ≈1.

**Rationale on record.** This is the crew's own demonstrated failure mode (z9-10 study: the
"clean" direct-Te subset was lens-contaminated until re-derived on strictly unlensed field
anchors). The clause exists so that the low-mass regime — exactly where half the faint end of
the named sample is strongly magnified — cannot silently anchor a deficit claim.

## §6. The null statement — template consuming T2a's frozen forecast (design F4)

T2a freezes, BEFORE any science row is fetched: the expected Te-anchored N per matched-mass bin
and the resulting per-bin deficit-precision forecast, defining the null's information content.
This section defines the only licensed form of a null result, and it is deliberately a
fill-in-the-blanks consumer of that frozen artifact — a null that cannot cite the forecast
verbatim is not reportable.

**Template (per bin or per compared quantity):**

> At the pre-committed anchor statistics for this bin (N = ⟨T2a frozen N⟩ Class-A anchors;
> forecast precision ⟨T2a frozen value⟩, frozen in ⟨T2a artifact id/sha⟩ prior to data fetch),
> deficits larger than ⟨T2a frozen exclusion threshold X⟩ are excluded at the declared scale
> floor. The measured offset Δ = ⟨value ± budget⟩ does not exceed this sample's scale
> uncertainty (§2, Rule S); the result is **scale-limited at current anchor statistics**, not a
> detection. This bounds the deficit below ⟨X⟩ on the declared scale and quantifies the
> remaining anchor gap as ⟨anchors needed per the frozen forecast⟩ versus ⟨N obtained⟩.

**Semantic requirements on any instantiation:**

1. Every ⟨⟩ field is filled from the frozen T2a artifact or the measured data — never from a
   post-fetch recomputation of the forecast. If T2a's forecast proves wrong (e.g. real N differs
   from expected N), the null statement reports BOTH the frozen forecast and the realized
   statistics, labelled as such; it does not silently substitute the realized numbers into the
   forecast's role.
2. A null without an exclusion bound ("we saw nothing") is barred. The template's exclusion
   clause is what makes the null an answer to A3's settle-line (it quantifies the anchor gap,
   c41_012) rather than an escape hatch.
3. The null inherits all of §2's vocabulary discipline: "scale-limited", never "no evolution",
   "no deficit", or any phrasing implying a measurement of zero.
4. Direction-blindness: the template is equally the licensed form if Δ points the unexpected
   way; the design's success criterion ("WHATEVER direction it points") applies to nulls too.

## §7. Interface to the machinery half (what this contract requires T2-machinery to supply)

For each rule above, the machinery deliverable (Goru, Kun verifying) must supply — as tables,
with citations and shas, before the science fetch:

- §1.2/§1.3 — the conversion entries: per-sample conversion onto the Te-anchored scale, each
  with its own uncertainty term.
- §2 — the per-sample scale-uncertainty instantiation (from the 0.24 dex class and the 0.15 dex
  Te-scale class) and the written combination rule for mixed samples.
- §4.2/§4.3 — cross-channel systematic terms per channel pair actually used, and per-ratio
  validation entries where any X/O ratio is compared.
- §5 — nothing numeric beyond receiving T1's per-object μ and uncertainty fields; the mass-error
  propagation rule is machinery, its per-galaxy inputs are T1's.
- §6 — nothing; the forecast is T2a's, and this contract only consumes it.

Semantics freeze with this document; the machinery tables may grow entries (new samples, new
channel pairs) but may not alter a definition or decision rule here without a logged revision
gated the same way the design was.

---

LANA_SHAPE2_T2B_COMPLETE_20260804
