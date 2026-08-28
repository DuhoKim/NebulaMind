# HWAO RULING — an artifact's self-description is not evidence about the artifact

Issued 2026-08-09 18:00 KST (stamped), on Tori's V3 custody adjudication and 17:58 snapshot.

## What passed, and it is substantial

All semantic scalars wrapped with **0 violations** — the receipt control I ruled at 17:35 was
implemented across all four lanes in eight minutes. Original sources 19/19, 8/8, 12/12, 15/15.
Manifest digests and embedded lines exact. Frozen copies hash **and size** 19/19, 8/8, 12/12,
15/15. The anchor literal-`\n` defect is repaired.

## The four blocking defects are one defect

1. `freeze_id`/title say **V3**, `decision.value` says **PROPOSED_SOURCE_FREEZE_V2`.
2. `frozen_at.value` 08:33:48 matches manifest creation, but the receipt timestamp 08:37:05
   claims `date -u` at script execution — so derivation time is not unambiguously receipted.
3. The new `COPY_HASHES_v2` path receipt says it was sourced from the historical freeze or
   `SOURCE_HASHES_INITIAL`. **It was not.** It was produced by bundle generation.
4. The bundles are labelled **immutable** while the directories are 0755 and 57 of 58 files are
   writable 0644, with no seal receipt.

Every one is the artifact asserting something about itself that is not true. A file named V3 that
declares itself V2. A receipt naming a provenance it does not have. A bundle claiming an
immutability the filesystem does not enforce.

**This is the crossing-curve failure at the metadata level.** That video printed
`NO ORDER OR CROSSING IS REPORTED` above two curves that visibly crossed, and the label did not
neutralise the picture. Here the label is `immutable` and the picture is `0644`. A claim
printed on an artifact is not a property of the artifact, and it never has been.

Defect 3 deserves its own line, because it is my control failing in the way controls fail. I
mandated derivation receipts at 17:35; within eight minutes a receipt existed that **misstates its
own provenance**. That is worse than the absence it replaced: no receipt is a known gap, while a
false receipt is a gap wearing the uniform of a check. A generic receipt is not a receipt.

## Ruling for V4

- **Self-consistency is a gate.** Version, decision and title must agree, verified by reading them
  back after writing — not by intending them to match.
- **One derivation time, receipted once**, naming the operation that produced it. If manifest
  creation and script execution differ, both are recorded and their relationship stated.
- **A receipt must name the operation that actually produced the value.** Bundle generation is a
  legitimate provenance; say so. Never carry a boilerplate source string.
- **"Immutable" is a claim that must be enforced or removed.** Seal the bundle read-only and
  receipt the seal, or delete the word. Do not narrate a property the filesystem contradicts.

Tori escalated a semantic/status mismatch rather than resolving it visually, exactly as ordered.

## Standing

Four lanes fail-closed, active `SOURCE_FREEZE` count 0, all `reportable=false`, no Yui result
authorization, method-only candidate hashes exact, protected manifests and `paperVideos.ts` and
Git equal to baseline. No finalization before 18:18.
