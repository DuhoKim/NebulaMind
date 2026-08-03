# P0 Correction Exact-Diff Approval Packet

Status: `PREPARED_ONLY_NOT_EXECUTED__SOURCE_AUTHORITY_REPIN_AND_FRESH_REVIEW_REQUIRED`

Marker: `P0_CORRECTION_PACKET_PREPARED_20260728`

## Scope

This packet prepares, but does not apply, a correction for the served four-page TNG-validation draft. The selected branch retracts the unsupported matched-Te/PP04 consistency claim and aligns the manuscript with the state already present in its Methods, Results, Figure 2, and Discussion:

> On the current unmatched abundance scales, the face-value MZR shortfall is about a factor of two and remains suggestive pending a single-scale re-derivation.

The packet preserves the SFMS result, including the +0.41/+0.49 dex conservative lower bound, the +0.46/+0.83 dex sample-matched widening, the up-to-~1.1 dex envelope, and the +0.13 dex mass-basis robustness claim, with the existing provenance caveat on the exact observed medians.

## Proposed closed-world change set

Existing files that would change only after a later apply gate:

1. `paper-backups/quartet-rewrites-20260723T141609Z/p6_tng-calibration-validation/after.tex`
2. `frontend/src/app/lab/FrontierDrafts.tsx`
3. `frontend/src/app/lab/paperScores.ts`

One new source-level contract test that would be added under the same later gate:

4. `frontend/scripts/test-p0-correction-state.mjs`

No PDF, history JSON, public file, Lab record, database/wiki row, service, runtime, or Git state is changed by this packet.

## Proposed corrections

- Remove the underived −0.40/−0.27/factor-1.5/“consistent once scales are matched” state from abstract and conclusion.
- Remove the unverified `~3×10^4` TNG sample count rather than substituting 23,722 without proving selection identity.
- Make the exact high-z offset medians explicitly provisional because the supplemental citation cannot be verified.
- Replace the cross-wired Lisiecki bibliography row with the missing, role-correct Kennicutt 1998 SFR-calibration reference.
- Narrow the MZR Results, Discussion, Figure 2 caption, and Conclusion to unmatched-scale, suggestive language with no mechanism inference.
- Keep both figure files unchanged: Figure 2 already shows the unmatched factor-of-two state and calibration caveat.
- Remove the dead P0 review metadata; do not fabricate a review artifact.
- Correct all stale P0 merit-note representations: DR, Tori, Kun, and Goru.
- Preserve the human-direction history JSON unchanged as an intended-but-not-landed revision record.

## Custody and source authority

The served PDF and the rich-live backup `after.pdf` are byte-identical: 132,831 bytes, SHA-256 `086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef`.

The adjacent `after.tex` is standalone-compilable and is the only source snapshot corresponding to the served bytes. The older scratch `topic3/tng_draft.tex` is byte-identical to `before.tex` and is stale. Because the serve-matching source lives under `paper-backups/`, a later apply gate must explicitly repin it as the canonical editable source or identify another current generator. This packet must not be applied to the stale scratch source.

## Prepared patch split

- `red_test_only.patch` — adds only the correction-state contract test.
- `green_source_only.patch` — proposes the minimal TeX, board metadata, and merit-note changes.
- `exact_diff.patch` — combined final candidate.

The patches have only been syntax/applicability checked. The RED test, TeX compile, PDF render, TypeScript checks, and build have not been executed because this approval forbids source/test execution.

## Gates still closed

- Source authority repin/apply
- Test execution and TeX compile
- Fresh Lana/Kun/Goru no-self-review
- PDF/public replacement
- Board/public publication
- Service restart
- Git add/commit/push/merge

## Later apply-gate template

`APPROVE APPLY P0 EXACT-DIFF PACKET <manifest-sha256>; REPIN SERVE-MATCHING after.tex AS THE CANDIDATE SOURCE; RUN RED/GREEN + TECTONIC + RENDER REVIEW; NO PUBLICATION, RESTART, OR GIT.`

NO ACTIVE EXECUTION PHRASE
