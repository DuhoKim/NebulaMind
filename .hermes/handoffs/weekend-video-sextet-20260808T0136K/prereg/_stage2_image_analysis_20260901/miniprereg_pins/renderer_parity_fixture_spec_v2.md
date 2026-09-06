<!-- renderer_parity_fixture_spec_v2 (Tier-C V37 draft): identical to its V35 §2.11 predecessor except that the pinned renderer is now renderer_v4. -->
# Renderer parity and configuration fixture specification (V20)

This replaces the BS-4 synthetic absolute-sign anchor specification, which is
retained unchanged at `bs4_sign_anchor_spec.md` as a superseded artefact.

## What was withdrawn, and why

The superseded specification asserted that the fixture established an ABSOLUTE
sign before any real image was opened. It did not and could not: step 3 of that
specification ran `successor_ref_v9.py --fixtures`, and §9.1a of this
preregistration states that `successor_ref_v9.py` is NOT the instrument of this
study and is not one of its inputs. The check therefore exercised a reference
implementation's sign convention, not the CE-ResNet's. Two independent referee
seats, on different engines and in different rounds, read the resulting
combination -- an anchor named "absolute" that the instrument never reaches,
an orientation-agnostic §9B gate, and §10.10's mapping flip -- as machinery
written to rescue a backwards instrument.

The premise of that reading was correct even though its conclusion was not:
§14.2 and §10.13 disclaim absolute handedness outright, so a global sign flip is
by construction outside what this study claims to detect. The defect was not
that the study was rescued; it was that the document asserted an absolute
guarantee its own estimand disowns. Duho ruled on 2026-09-05 that the
absolute-anchor language be withdrawn rather than the instrument check added.

## What survives, and why it earns its place

Two of the three parts of the superseded procedure test properties this study
genuinely relies on, and neither is duplicated elsewhere:

- The synthetic North/East fiducial test is an END-TO-END check that the pinned
  renderer preserves orientation and parity. §8.7's `WRONG-PARITY-REFUSAL` is an
  analytic test of the Jacobian only; it cannot catch an array flip introduced
  after the WCS step. This fixture can.
- The configuration test asserts that the pinned `render_config_v2.json` matches
  the frozen §8 constants, which §8.13 requires.

The third part -- the reference-implementation fixture battery, including
`BATTERY-SIGN` -- is retired. It tested a script this study does not use.

## Procedure (mandatory and ordered)

1. Verify the instrument identity and environment against their pins. This
   fixture does not invoke the instrument; it verifies that the identity the
   run will use is the frozen one before recording a receipt about it.
2. Verify that `miniprereg_pins/render_config_v2.json` equals the frozen §8
   constants exactly, including `neighbour_policy = single-brick-containment`
   and `interpolation = bilinear-image-nearest-integer-planes`. A mismatch is
   `DATA-INTEGRITY-FAIL`.
3. Feed an asymmetric synthetic WCS carrying labelled North and East fiducials
   through the pinned single-brick renderer `study_renderer/renderer_v4.py`.
   Assert North is up and East is left. Feed a deliberately wrong-parity
   Jacobian and require the literal `WRONG-PARITY-REFUSAL`. A failure of either
   assertion is `WRONG-PARITY-REFUSAL`. No real survey pixel is read.
4. Seal the synthetic inputs, the geometry result, the renderer configuration
   digest, the renderer and instrument environment records, the instrument
   digest, and PASS in the chained journal. The receipt carries
   `establishes_absolute_sign: false` as an explicit field, so that no later
   reader can recover the withdrawn claim from the journal.

## What this fixture does NOT establish

It does not establish absolute handedness. It does not exercise the CE-ResNet.
It does not validate GZ1. A global sign flip in the instrument would pass this
fixture, and that is a disclosed and accepted property of a study whose estimand
is relative concordance (§1.1a, §14.2).
