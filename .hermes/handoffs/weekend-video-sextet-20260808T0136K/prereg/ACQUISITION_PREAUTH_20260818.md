# Acquisition pre-authorization — the STOP-rule crossing, conditionally granted

**Duho, 2026-08-18 20:38–20:45 KST, verbatim: "pre-authorize the acquisition, run it after the
cross-check passes"**

Given in the Hwao session immediately after `PILOT_DECISION_20260818.md`. This is the explicit
human authorization the lane has required since 2026-08-14 for fetching real survey imaging
("Authorise the acquisition run — still the STOP-rule crossing").

## Conditions — both must hold before the first image byte moves

1. **Checksum harvest complete**: all 60,308 working-set `.sha256sum` receipts present
   (`state COMPLETE`, no `BLOCK_EVENT.json`), receipts.jsonl parse-clean.
2. **Known-issues cross-check PASSES**: the DR10 known-issues / DR10.1-replacement information is
   checked against the harvested digests per the route-decision memo's cross-check; a pass means
   no silent pre-replacement-bytes hazard in the working set. If it fails or is ambiguous:
   STOP and report to Duho — the pre-authorization does not cover an unresolved cross-check.

## What is authorized once the conditions hold

Execution of the image acquisition **exactly under the frozen successor route binding**:
`TORI_ROUTE_BINDING_SUCCESSOR_20260817.md`, SHA-256
`1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b`, mode 444, gated
`PASS_SUCCESSOR_ROUTE_BINDING` (`KUN_SUCCESSOR_BINDING_REGATE_20260817.md`), frozen by Duho
2026-08-17 14:21 KST. Route B, public HTTPS, DR10 South `image-r` coadd bricks for the 60,308-brick
working set (~0.7 TB), each file verified against its harvested per-brick digest before acceptance.

## What this pre-authorization does NOT waive

- **Lane gating.** The acquisition build is MockTransport-only by certified design
  (`PASS_ACQUISITION_BUILD_ONLY_GATE`). Building/altering a real transport (including removing the
  `BUILD_ONLY_STOP` guard) is itself gated: Tori builds, **Kun gates the transport against the
  frozen binding before the first image byte**. The pre-authorization covers running the gated
  result, not skipping the gate.
- **The binding's own rules**: windows, pacing, receipts, and the standing prohibitions
  (no recursion, no wildcards, no mirroring/crawling, no range requests, no cutout-service calls,
  no unmanifested URLs). A block event or any digest mismatch stops the run and goes to Duho.
- **Anything beyond acquisition**: cutout production and the §2b pilot follow their own recorded
  steps (`PILOT_DECISION_20260818.md`); nothing here authorizes analysis of sky statistics.

## Sequencing (projected)

Harvest completion projected 2026-08-20 ~14:00 KST (40,436/60,308 at 20:38 KST, window closes
24:00 KST tonight, resumes 12:00 KST Wednesday). Then: cross-check → transport build + Kun gate →
paced transfer under the binding (multi-window; the binding's pacing governs the calendar) →
per-file digest verification receipts → report to Duho at completion or on any stop condition.

— recorded by Hwao; the authorization and its verbatim wording are Duho's. K-8 remains untripped
until the conditions hold and the gated transport runs.
