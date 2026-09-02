# BS-4 synthetic absolute-sign anchor specification

This is the executable pre-real-image anchor for this Tier-C concordance study.
The celestial winding convention is East-of-North. The constants are exactly
`A_LONGO = +0.0408` in this convention and
`A_LONGO_PUBLISHED_SIGNED = -0.0408` in Longo's published convention.

Procedure (all steps are mandatory and ordered):

1. Verify SHA-256 of `../_successor_build_20260824/ref/successor_ref_v9.py`
   equals `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
2. Verify the sealed renderer configuration, renderer packages/environment,
   and instrument environment against their pins. Feed an asymmetric synthetic
   WCS anchor carrying labelled North and East fiducials through the same
   stitch-neighbours-first, one-bilinear-reprojection renderer used for study
   images. Assert North is up, East is left, the source-to-output Jacobian has
   the required parity, and an intentionally wrong-parity Jacobian returns the
   literal `WRONG-PARITY-REFUSAL`. No real survey pixel is read.
3. In that verified environment run exactly:
   `python3 ../_successor_build_20260824/ref/successor_ref_v9.py --fixtures`.
   Require exit status zero, require exactly one output line beginning
   `BATTERY-SIGN: PASS`, and require the final line `ALL FIXTURES PASS`.
4. The BATTERY-SIGN acceptance criterion is: the deterministic synthetic sky
   injected with amplitude `-0.0408` is never assigned the parent verdict
   `REPRODUCED-LONGO`. Any contrary result, absent line, extra BATTERY-SIGN
   line, nonzero exit, hash mismatch, geometry assertion failure, or refusal
   mismatch is `ABSOLUTE-ANCHOR-FAIL` and no real image may be opened.
5. Seal the synthetic inputs, complete stdout, exit status, renderer config
   digest, renderer/environment record, instrument digest, and PASS in the
   chained journal.

Here BS-4 establishes, before any GZ comparison, that the rendering plus
instrument chain preserves the study's absolute East-of-North sign. It does
not validate GZ1, estimate concordance, or establish handedness truth.
