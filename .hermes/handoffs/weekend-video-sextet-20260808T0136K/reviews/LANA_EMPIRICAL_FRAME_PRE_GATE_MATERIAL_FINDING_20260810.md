# LANA — material pre-gate finding on the empirical frame test (raise before the gate, as the grant invited)

Under `SOURCE_FREEZE_AMENDMENT_A2_EMPIRICAL_FRAME_GRANTED_20260810T2115K` (grant `ebd0ef76…`). Filed
**2026-08-10 20:45 KST**, **before** binding any pre-registration and **before any computation**. The grant
explicitly asked: *"If you believe existing t2_mirror_bias output has ALREADY effectively revealed the
sign, say so now."* I do. Here it is.

## The finding
The empirical sign test's discriminant is **(a) effectively already revealed** and **(b) structurally
confounded** — so the test as designed cannot be run blind and is very likely INCONCLUSIVE, and this is
foreseeable now, not after a run.

This rests **only on what is already on the record** — the aggregate mirror-vs-normal statistic that
`t2_mirror_bias.py` / `T2_MIRROR_BIAS.json` already computed and that `KUN_FRAME_REVIEW.md` already
re-derived, which I read while writing the provenance finding. **I did not re-open that output, run the
correlation, or take any "look for a hint."**

### (a) Blindness is compromised
The already-known aggregate statistic **reverses between the unmirrored (normal) leg and the mirrored leg.**
A per-object correlation and an aggregate reversal are the same phenomenon at two scales: an aggregate
reversal is the population manifestation of a **negative** per-object relationship, whereas a **positive**
per-object correlation — the FRAME_DEMIRRORED prediction — would produce **no** reversal. So the already-seen
reversal telegraphs the direction the per-object test would point. Everyone who has read Kun's frame review
holds that prior. The "decide before seeing" pre-registration — the part I called the whole integrity of
the test — is undermined at its root, because the sign is pre-seen through a sibling statistic.

### (b) The revealed sign is degenerate with the confound
An aggregate handedness reversal under mirroring is **precisely the signature classifier bias produces** —
that is Land et al. (2008)'s entire result. So FRAME_AS_SEEN and the classifier bias predict the **same**
direction. The sign the test would report cannot, by itself, tell frame from bias. My pre-registered
rule-3 bias-confound control therefore does not face a hypothetical it might catch; it faces a **known,
structural** degeneracy. The honest pre-registered outcome of the bare sign test is **INCONCLUSIVE**, and I
can state that before any number is computed.

## Why I am not binding the sign test as-is
Binding a pre-registration for a discriminant that is both pre-seen and structurally confounded would be
procedure without integrity — it would produce a confounded "answer" dressed in a gate. The pre-registration
I designed exists to stop exactly that. So I am **not** handing Kun the bare sign test to gate.

## Two honest paths
- **(A) Redesign the discriminant to break the degeneracy.** The sign is too weak. A stronger test asks,
  object by object, **which unmirrored fraction `pcS1` tracks — the unmirrored clockwise or the unmirrored
  anticlockwise** — because a frame convention is a near-deterministic relabelling (`pcS1` should nearly
  equal one of the two unmirrored fractions), while bias is a soft additive offset. That identity test can
  cleanly detect the **as-seen** case (`pcS1` tracks the unmirrored *anticlockwise* fraction); it still
  cannot cleanly separate **de-mirrored** from **bias** (both track the unmirrored *clockwise* fraction). So
  even redesigned, one branch stays confounded. If Duho wants to invest, this identity discriminant — with
  its own pre-registered near-identity threshold, the rule-3 bias control, and the size/representativeness
  gates — is the **only** version worth binding, and I would design and hand *that* to Kun. Never the bare
  sign test.
- **(B) Accept Path C (terminal), on the strongest record yet.** Both routes are now documented as unable to
  resolve the frame: the documentary route exhausted across three surfaces (`LANA_SPIN_FRAME_PROVENANCE_
  FINDING` Rev 2), and the empirical sign test structurally confounded by the bias under study. Per the
  grant, this **inconclusive/unresolvable outcome is a successful execution of the amendment**, returns the
  lane to Path C, and is reported as plainly as any other result — not a failure.

## My recommendation
**Lean (B).** The confound is structural, not a threshold I can tune, and the identity redesign rescues only
one of the two branches — a partial instrument for a question that may still land unresolved. Path C now has
the fullest possible justification on record: we tried the documentary route to exhaustion and identified,
before spending it, that the empirical route cannot cleanly answer either. That is the honest terminal
state. If Duho would rather spend the effort for the chance that the as-seen branch resolves cleanly, path
(A)'s identity test is the responsible way to do it, and I will bind and gate it — blind to any number,
with the same pre-registration discipline — before it runs.

## Integrity and scope statement
No correlation computed; no trial, no sanity check, no fresh look at `T2_MIRROR_BIAS.json`. This finding uses
only the already-on-record aggregate reversal from Kun's review, cited to assess test blindness — it asserts
no asymmetry, direction, sign, or parity about the sky, and the aggregate statistic remains the fenced,
withheld result whose sign-meaning is exactly what is unverified. Nothing is unblocked:
`STATUS_RESULT_MISMATCH`, `WORKFLOW_STATUS_NOT_RELEASE_READY`, and `LATER_FREEZE_EXCLUDES_NEW_POINTERS`
stand; `BLOCK_SUBSTANTIVE_RESULT_RENDER` survives; `video_reportable_now` stays false. Handed to Duho (decide
A or B) and Kun (who gates whichever test, blind, before any number) — I bind nothing runnable until that
decision.