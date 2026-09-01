# R-D human-committee composition and rendering-surface options

Status: options for Duho's ratification. This paper does not authorize an image fetch, inspect image bytes, compute pixel statistics, or read or disclose anything χ-bearing.

## 0. Settled ground — not options

Direction #34 is controlling: **“Both - human + machine committees (Recommended)”**. The design therefore has (i) a machine committee, (ii) a human committee, and (iii) an independent verifier that recomputes the stratum index from Row D receipts and refuses any mismatch. None of those three components is reopened here.

The successor draft freezes the relevant access surfaces:

> **Row G — Hand-check committee:** “views χ-bearing cutouts **of the allocated sample only**, rendered through the sealed interface → each label leaves the member only through that same interface to row H.” Its void conditions include “a member holding any other role; any label, tally, description or impression exported outside the interface; any view outside the allocated sample; any unlogged view.”

> **Row H — Label-ingestion writer:** “receives labels from row G through the interface → writes them, as one label set, into the committee sealed store,” with no outside write path, no intermediate persistence, no field beyond the pinned schema, and no export of the receipt digest.

Thus the hand-check body is a body distinct from the ruled BS-2k reviewer and custody rosters. Those two rosters are each Option A, Duho alone. Row G imposes a different and stricter role rule: a hand-check member may hold **no other role**. On the present text, putting Duho in Row G therefore collides with Duho's already-frozen reviewer/custody roles unless the role separation is explicitly repaired before freeze. Mirroring a roster's headcount does not merge the bodies or waive Row G's prohibition.

The inherited text is also more specific than the word “committee.” The accepted HC-1H record says:

> “HC-1H replaces HC-1…HC-6: **one human checker (Duho), 850 blinded labels** — 500 real, 200 blind synthetic ground-truth injections, 150 mirrored re-presentations.”

It also says the nine strata are machine-committee state × |χ| tertile and that the machine committee is “stratifier / allocator / diagnostic **only, never inside `a`**.” The successor says that V3-pred's “HC-1H measurement and validity rules (committee, sealed keys, HC-5, HC-6) are carried by quotation at freeze.” Consequently, **one checker, Duho, is the currently incorporated rule, not an open headcount choice**. Any multi-person choice below requires an explicit successor revision of that quotation and its estimator/receipt semantics. It cannot be presented as already conforming.

Other frozen rules:

- The object set and complete Row-G traversal — “order, multiplicity, retries and stopping” — are precommitted and χ-blind. The sequence contains interleaved blind synthetics and mirrored re-presentations at randomized later positions; the checker does not choose the next object.
- Exactly `R_max = 2` committed render events occur per allocated object per member. They are contiguous; interruptions consume replays; unused renders are padded per object when the member advances. Row H persists one label set, with no per-object label event in the access chain.
- A view is one display session owned by one render commit. Visibility loss, blanking, occlusion, navigation away, interface clear, or position advance ends it. Dwell and magnification within an uninterrupted session remain the same view. A later display requires the next committed render.
- The 2026-08-30 ruling is verbatim **“abstain.”** A replay-exhausted object receives `ABSTAIN`; the run continues; it is labeled for completeness but contributes no handedness call. This is settled and is not asked again.
- HC-1H's `suspected-identifiable → discard → same-stratum-and-category replacement` escape hatch remains unmodified. It is valid only while identity flagging is not handedness-sensitive. The exemption is bound to the pinned Row-G interface digest; changing what is visible lapses it until the principal re-establishes the finding.
- Geometry is fixed at 128 × 128 pixels and 0.262 arcsec/pixel (33.536 arcsec square). At the smallest allowed `shape_r > 1.5 arcsec`, twice the limiting scale is only about 11.45 pixels. Magnification is therefore an interface necessity, not permission to alter the scientific raster.
- v9 fixes `HC_REAL_LABELS=500`, `N_HC_STRATA=9`, `HC_MIN_PER_CELL=10`, `HC_MIN_PER_STRATUM=30`, and `R_max=2`. Infeasible floors fail rather than shrink.

## 1. Human-committee composition

The workload figures below are per checker because adding checkers does not divide the frozen 500-object calibration stream: each checker who supplies an independent complete label set must see all 500 real allocations. That is **500 real decisions and exactly 1,000 real-object render commits per member**. If the inherited complete 850-presentation HC-1H stream is retained per member, the corresponding upper protocol count is **850 decisions and 1,700 render commits per member**, before replacement presentations. Wall-clock labor is not safely inferable without a ratified dwell/break schedule.

### C1 — Duho alone, literal HC-1H

- Composition: Duho is the sole human checker.
- Work: 500 real decisions / 1,000 real render commits; under the full inherited stream, 850 decisions / 1,700 commits.
- Blinding: Duho must be blind to hypothesis-bearing prompts, object identity beyond the opaque interface token, real/synthetic/repeat category, parity history, stratum, Row-D χ, machine verdict, and all running tallies. Prior knowledge of the broad scientific hypothesis is unavoidable for the principal; operational blindness must therefore be enforced by the surface, not claimed as personal ignorance.
- Conformance: satisfies the literal “one human checker (Duho)” quotation, **but does not presently satisfy Row G's “member holding any other role” prohibition**, because the ruled reviewer and custody rosters also name Duho. A role-conflict repair or waiver would be required; silently treating the bodies as one would not conform.
- Cost: concentrated labor, no independent human replication, and the custody threat model remains single-person.

### C2 — One independent checker, replacing Duho as HC-1H checker — **recommended**

- Composition: one named person who holds no reviewer, custody, machine-committee, Row-D, Row-D2, allocation, ingestion, or verifier role.
- Work: 500 real decisions / 1,000 real render commits; with the full inherited stream, 850 / 1,700.
- Blinding: strongest feasible operational blinding. Recruit and instruct the checker without revealing the directional hypothesis or expected handedness balance; reveal only that the task is morphological handedness classification with blinded controls. The sealed UI hides all forbidden fields.
- Conformance: satisfies Row G's separation rule and keeps one-checker estimator semantics, but changes the quoted identity “Duho.” It therefore needs a narrow successor revision changing checker identity while preserving the one-human architecture, sealed keys, HC-5/HC-6 rules, and receipt bindings.
- Cost: the real recruitment problem is finding a person willing and able to complete 850 blinded presentations (and up to 1,700 committed display sessions) under pauses, replay limits, and no feedback. Training must use non-run, parity-balanced examples and cannot disclose machine results.
- Reason for recommendation: it resolves the otherwise direct Duho role collision with the smallest change to frozen HC-1H semantics and gives materially better hypothesis blindness than the principal checking his own study.

### C3 — Three-person independent committee

- Composition: three named, mutually independent checkers, none holding any other run role.
- Work: **per member** 500 real decisions / 1,000 real commits (or 850 / 1,700 full-stream); aggregate 1,500 real decisions / 3,000 real commits (or 2,550 / 5,100 full-stream).
- Blinding: each member separately blind to the hypothesis direction, identities/categories, strata, χ, machine outputs, other members' labels, and running aggregates. Members must not confer until the sealed label sets are complete.
- Conformance: does **not** satisfy the incorporated one-human quotation without revision. A revision must predeclare whether three complete label sets are combined by majority vote, a latent-error model, or another fixed estimator; how member-specific synthetic error and covariance enter; and whose co-signatures Row H requires. Those are scientific rules, not clerical details.
- Cost: recruiting three people who will each label 500 real objects plus controls is likely the dominant operational risk; labor triples and disagreement adjudication cannot be invented after viewing labels.

### C4 — Five-person independent committee

- Composition: five separated checkers with no other roles.
- Work: **per member** 500 real decisions / 1,000 real commits (or 850 / 1,700); aggregate 2,500 real decisions / 5,000 real commits (or 4,250 / 8,500).
- Blinding and conformance: same requirements and same nonconformance as C3, with a more complex predeclared aggregation/error model.
- Cost: highest recruitment and completion risk. A single incomplete member requires a predeclared consequence; silently reducing committee size after labels exist is forbidden.

**Recommendation: C2**, accompanied by the narrow identity amendment. If the principal refuses any change to “Duho,” C1 is the only literal HC-1H choice, but its collision with Row G must be affirmatively repaired before execution.

## 2. Rendering surface

Every option below preserves parity. No display path may mirror, flip, transpose, rotate by a parity-reversing operation, condition orientation on content, or apply a different transform to different categories. Any permitted transform, parameters, color map, window geometry, and implementation digest must be fixed before image access and applied identically to real, synthetic, and repeat presentations. The underlying 128 × 128 scientific raster is never rewritten.

### R1 — Single-panel integer nearest-neighbour zoom with one frozen global intensity mapping — **recommended**

- Show one centered R-band cutout at a time, enlarged by a fixed integer factor (recommend 8×, yielding 1024 × 1024 screen pixels). Nearest-neighbour replication makes the approximately 11-pixel smallest object visibly about 88 screen pixels across without inventing interpolated structure.
- Use one preregistered, parity-even, object-independent intensity transfer derived from non-χ design information or fixed physical/header units, with fixed clipping endpoints and a fixed grayscale polarity. Do not compute per-object percentiles, histograms, auto-levels, or adaptive contrast from run pixels.
- Do not show maskbits or inverse variance. They are valid scientific companions for input completeness, but a human handedness call does not require their values; overlays may identify real/synthetic construction or quality state and hence threaten the HC-1H identity exemption.
- One object only: no side-by-side original/mirror, prior render, synthetic exemplar, machine view, or comparison object. This prevents a direct parity cue and avoids converting repeat identity into an obvious interface fact.
- Cost: blocky pixels and possibly suboptimal visibility across a broad surface-brightness range. The cost is honest: with no authorized pixel study, an adaptive stretch cannot be justified or frozen from real data.

### R2 — Single-panel nearest-neighbour zoom with a small menu of checker-selected frozen global stretches

- Same geometry, parity discipline, and single-panel rule as R1.
- Permit two or three globally predeclared monotone intensity mappings, available for every object in the same order. Selection occurs within the same uninterrupted render session and does not fetch new bytes.
- Cost: improved visibility without interpolation, but checker choice becomes content-dependent interaction. Although it need not alter parity, the choice/dwell pattern must not be exported, persisted, or used to branch traversal. The interface digest and channel analysis must cover it. More implementation and fixture burden than R1.

### R3 — Single-panel smooth upscaling with one frozen global intensity mapping

- Use a fixed parity-preserving interpolation kernel solely in the display compositor; never feed the upscaled image to Row D or store it as the scientific raster.
- Cost: visually less blocky, but it creates interpolated gradients and can make an 11-pixel object appear more resolved than it is. Kernel behavior at edges and pixel-center alignment must be pinned and parity-tested. It is less audit-transparent than nearest-neighbour and therefore not recommended.

### R4 — Companion toggle (R image plus maskbits/invvar views)

- Permit a fixed-cycle, parity-aligned toggle among R intensity, maskbits, and inverse variance, never side-by-side.
- Cost: companions can help distinguish artifacts, but they add survey-specific identity/quality cues, expand the χ-bearing rendering surface, complicate the suspected-identifiable exemption, and may let checker behavior depend on machine-quality evidence. This option should be rejected unless a separate blind-interface argument establishes necessity.

**Forbidden on every surface:** hypothesis text or expected result; sky coordinates; brickid, objid, catalogue name, file/path/header identifiers, URLs, timestamps, stratum/category labels, real/synthetic/repeat markers, allocation metadata, Row-D χ/sign/amplitude/confidence, machine-committee states or verdicts, other human labels, running counts/tallies/agreement, prior labels, a visible mirror-pair relationship, and any transform that changes parity. The only identity handle should be a non-semantic ephemeral progress token if the pinned schema requires one. No screenshot, clipboard, download, browser cache, accessibility export, compositor restore, or other redisplayable surface may bypass the logged-session rule.

**Recommendation: R1.** It directly addresses the 11-pixel visibility limit, preserves the original samples exactly, minimizes identity channels, and is easiest for an independent parity verifier to reproduce.

## 3. Checker instructions

The wording itself must be pinned as part of the Row-G interface specification. It must not mention the directional hypothesis, χ, machine agreement, strata, expected proportions, or why an item may be repeated.

### I1 — Minimal neutral script — **recommended**

> You will see one centered astronomical image at a time. Classify only the apparent winding direction of the visible spiral pattern on the screen.
>
> Choose **CLOCKWISE** if the arms appear to wind clockwise as they move outward from the center. Choose **COUNTERCLOCKWISE** if they appear to wind counterclockwise as they move outward.
>
> If the image session is interrupted or becomes hidden, do not classify from memory. The interface may provide one logged replay. If the replay allowance is exhausted before you can make a reliable call, choose **ABSTAIN**. ABSTAIN is a complete allowed label; do not guess.
>
> If you believe you recognize the specific object, believe it is a control, or believe you have seen it earlier in this task, choose **SUSPECTED IDENTIFIABLE** before giving a handedness answer. Do not state why. The interface will discard it and, when available, substitute a sealed replacement. Use **SYSTEMATIC IDENTITY EXPOSURE** only if the problem appears systematic rather than item-specific; the interface will stop according to the frozen rule.
>
> Judge each presentation independently. Do not compare it with previous presentations, take notes, capture the screen, discuss an image, infer categories, or try to predict the sequence. Do not report any label, impression, tally, or description outside this interface. Do not use outside catalogues, image search, software, or personal copies.
>
> You may magnify or dwell within the current uninterrupted display session using only the controls provided. Do not rotate, flip, mirror, or otherwise reorient the image. Submit exactly one allowed response when prompted. The interface controls order, replays, breaks, and completion.

Cost: concise and neutral, but orientation terminology must be verified in parity-balanced non-run training so “as they move outward” is understood consistently.

### I2 — Diagram-assisted neutral script

Use I1 plus two parity-balanced synthetic diagrams labeled CLOCKWISE and COUNTERCLOCKWISE, generated and frozen before the run and shown only in a separate training phase that cannot persist beside run images.

Cost: lowers terminology errors, but training assets can prime morphology and create a comparison surface. They must be symmetric in every respect except winding sign, contain no run object, and be unavailable during checking.

### I3 — Text plus required practice gate

Use I1 followed by a fixed parity-balanced synthetic practice set. Require a predeclared accuracy threshold or repeat training before the real sealed traversal begins; practice labels never enter the run's estimator.

Cost: best evidence that instructions are understood, but adds labor and requires a frozen failure/termination rule. Practice cannot be tuned after any real presentation and cannot reveal later injection identities.

**Recommendation: I1**, with a short parity-balanced terminology check only if that check and its consequence are frozen as part of the interface before access.

## 4. What the machine committee is — settled role, remaining design obligations

This section offers no alternative to direction #34. Row D2 requires a **Stratum-index producer** that may read χ through Row B after Row D and before BS-2f, “runs the two committee architectures,” and computes **machine-committee state × χ tertile per object**. It must write a **sealed, pinned, independently verified stratum-index artifact** into the main store via Row B. No stratum output may leave the store or be written after BS-2f. The artifact is capability-limited to Row F's allocation constructor and may never reach `calibration_bins()`; the boundary verifier recomputes position-only calibration boundaries and refuses inequality.

The inherited machine states are `agree-confident`, `disagree`, and `low-confidence`. The machine committee is a stratifier, allocator, and diagnostic only, **never an input to the attenuation estimator `a`**. Direction #34 additionally settles that an independent verifier recomputes the stratum index from Row D receipts and refuses mismatch; producer testimony is not sufficient.

Stage two still must design and pin, without doing so in this paper:

- the identities, exact versions/digests, inputs, and deterministic decision rules of the machine-committee members;
- how their outputs map exactly to the three frozen committee states, including confidence thresholds and all failure/missing-output consequences;
- the χ-tertile construction and tie/degeneracy rules consistent with the frozen nine-stratum allocation;
- canonical artifact and receipt schemas, sealed-store/capability bindings, traversal, and Row-B operations;
- an independently implemented recomputation verifier whose inputs are Row-D receipts, with equality/refusal semantics and adversarial fixtures;
- parity, blindness, completeness, and no-leak fixtures proving that neither committee verdicts nor strata reach the human surface or `calibration_bins()`.

Those are obligations to be filled before execution, not invitations here to select models, thresholds, or committee logic.

SEAT: CODEX
VERSION: COMMITTEE-V1
VERDICT: DRAFTED
COUNT: 4 option sets drafted
