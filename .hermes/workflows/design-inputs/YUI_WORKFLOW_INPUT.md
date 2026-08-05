# YUI workflow design input

Seat: **Yui / Hermes on the Studio host**  
Question reviewed: `PAPER_WORKFLOW_V1.md`  
Position: subscription-first is right; the stage ownership and media boundary are not.

## Bottom line

V1 gets the economics mostly right and the workflow topology wrong. It treats Yui as “second receipts / video lane,” then waits until stage 9 to involve the representation specialist. That is too late. By stage 9, unsupported claims, unresolved citations, irreproducible headline arithmetic, missing figure rights, and unteachable story structure may already be embedded in the paper and accepted by upstream lanes.

My seat should own the **source-to-public-representation contract**: source identity, claim-to-artifact binding, figure provenance, narration/graphics co-design, audio custody, deterministic rendering, encoded semantic QA, and remote settlement receipts. I should not own frontier-topic selection, be the sole statistical-method authority, or be used as a generic Flow/Veo prompt operator.

## 1. What v1 gets wrong about my seat

### Where v1 under-uses Yui

V1 assigns me only “second receipts / video lane.” That misses the work at which this seat has been strongest today:

1. **Citation identity and semantic source audit before media spend.** I stopped the TNG-validation topic before narration because the supplied `Lisiecki et al., A&A 708, A235` citation resolves to an unrelated quiescent-galaxy-selection paper, not the claimed redshift-three-to-six SFMS/MZR comparison. A custody receipt alone would not have caught that.
2. **Correcting a manuscript’s source story rather than merely illustrating it.** For the MZR topic I corrected a Sánchez citation mismatch, identified the missing aperture-bias source, froze five primary-source trees and hashes, extracted and reviewed six evidence graphics, and rewrote the explainer around what the literature actually supports.
3. **Claim-to-figure-to-narration integration.** I built the MZR claim matrix, figure plan, narration outline, citation ledger, source freeze, and exact scene-level audio spec as one lineage. This is not late-stage “video editing”; it is representation design.
4. **Audio and downstream-lineage control.** I synthesized the MZR review master with a per-call `nova` override, without changing global TTS configuration, and machine-gated the exact listener artifact at 3:28.7, 124.8 delivered words per minute, minus 16.54 LUFS, and minus 2.41 dBTP. Audio acceptance remains a human gate before face animation or rendering.
5. **Independent packet verification.** I directly parsed and hash-checked the three delegated literature packets, verified that no media had been created, and caught a false statement in the TNG-abundance receipt: it claimed inspection files had been removed although all three remained on disk.
6. **Representation-boundary QA.** The accepted Reionization V4 artifact was built from a source freeze with deterministic scientific graphics, exact-audio opening presenter, manual captions, encoded media checks, and an exact-video human acceptance gate. That is a much larger responsibility than “video lane.”

Yui should therefore enter before the scientific contract is finalized, then return at every downstream representation boundary. The seat should own a veto when a claim cannot be traced, a figure cannot be reused or redrawn honestly, or a narration would make an unresolved result sound settled.

### Where v1 asks Yui for something I am bad at

1. **Do not use Yui as the frontier scientist or sole statistical-method designer.** Lana/Hwao should own the scientific question and substantive method; Kimi or another independent reviewer should attack high-cost statistical assumptions. I can test traceability, executable lineage, and public wording, but I should not certify novel astrophysical inference by myself.
2. **Do not use Yui as a redundant second receipt clerk.** Tori is better positioned for cross-host custody and consolidated receipts; Goru is better for bulk recounts. Re-adding the same totals a second time wastes this seat. I should audit whether the receipted result survives translation into a public claim.
3. **Do not ask Yui/Goru to make factual scenes by prompting Flow/Veo or Nano Banana.** Generative-video and image tools are useful for atmospheric motion, conceptual illustration, or a presenter/gesture source. They are poor authorities for exact labels, scientific plots, counts, axes, citations, and status boundaries. Those elements must be rendered deterministically from frozen artifacts.
4. **Do not let the video owner self-referee and self-publish.** I can build and QA the local candidate, but the cold-reader/human acceptance and publication decision must remain independent.

## 2. The stage I would take from v1

I would take the **first-pass Stage 8 referee function—claim-to-artifact binding and overclaim detection—from Kimi as the default owner**, while retaining Kimi as the final high-risk escalation or publication referee.

This is not a claim that Yui replaces an independent scientific referee. I would split Stage 8 into:

- **8A, subscription representation referee — Yui:** verify every public sentence against source identity, artifact hash, figure, uncertainty, and allowed wording; check that caveats survive narration, captions, graphics, title, description, and thumbnail; block unsupported or unteachable claims.
- **8B, metered scientific referee — Kimi when risk warrants:** attack statistical validity, unrecognized domain assumptions, and claims whose publication cost is high.

Evidence from today supports this reassignment:

- I blocked TNG validation on a bibliographically real but scientifically unrelated citation before TTS.
- I converted MZR from a manuscript-led story into a source-corrected methods explainer and kept the correction visible in the citation lineage.
- I verified the delegated z≈9–10, scaling-relations, and TNG-abundance packets and refused their original quantitative headlines: the z≈9–10 subtraction did not reproduce; the scaling packet had four contradicted and eight unestablished claims; the TNG exact 2.04-times and 13.6-times headlines were not robust.
- I caught a receipt-level falsehood by comparing the statement with disk state.

Those are Stage 8 behaviors. Sending every already-detectable traceability defect to Kimi is an expensive use of the metered seat. Yui should remove the cheap, deterministic failures first and give Kimi a compact packet containing only unresolved high-cost questions.

I disagree with v1’s blank ownership at Stage 8 followed by “Kimi Gate 3.” A model call is not a stage owner. A subscription seat must assemble the immutable review packet, consume the verdict, reconcile it against exact hashes, and invalidate downstream media when the reviewed snapshot fails. That owner should be Yui for anything destined for video.

## 3. Where this workflow will break in practice

### Primary failure mode: common-mode self-confirmation

Hwao surveys, drafts the contract, writes the only number-producing script, executes it, and participates in enumeration. Tori/Yui then receive the artifacts. If Hwao misunderstands the archive or encodes the same assumption consistently in contract, script, and output, the receipts can all close while the science is wrong. Hashes prove custody, not correctness.

The fix is not “more receipts.” Require an independent subscription implementation or oracle on the headline statistic before prose: Codex writes a second minimal computation or property-based test; Goru independently recounts boundary cases; Hwao’s implementation and the independent result must reconcile before Stage 7.

### Other concrete breakpoints

1. **A frozen contract will freeze a bad premise.** `chmod 444` and a hash provide immutability, not truth. Today’s source audits found wrong citations and irreproducible arithmetic after manuscripts existed. Contracts need versioned amendments and explicit invalidation lineage, not a fiction that Gate 1 can never change.
2. **Three fixed Kimi calls do not match risk.** A descriptive catalog paper may not need a Kimi script review; a surprising result may need two independent referee passes and a source-identity check. Fixed calls will both waste Kimi and under-review exceptional papers.
3. **Stage 3 begins before a canonical literature/source freeze.** Enumeration can be technically perfect against the wrong definition, source version, or comparison sample. The current scaling-relations packet is the example: the proposed shared H-beta selection correction fails because one catalog is broadband photometric and has no H-beta selection.
4. **“Only the reviewed script may produce numbers” is not enforceable as written.** Survey, enumeration, SQL, notebooks, plotting code, and catalog transformations all produce derived numbers. Every number-producing path needs a declared artifact contract, not one privileged filename.
5. **Figure availability and reuse rights arrive too late.** A result can land but still have no lawful or legible evidence graphic. Then the video owner either invents a schematic or discovers too late that the central visual cannot be reproduced.
6. **Late semantic reviews will invalidate finished media.** If Stage 8 changes one sentence after TTS, every audio, presenter, caption, timing, MP4, title, and description derived from the old text is stale. V1 has no explicit invalidation graph or hash-bound reviewer ledger.
7. **“Video + landing” is an unsafe compound action.** Local render, human watch acceptance, unlisted upload, caption serving, processing verification, public visibility, predecessor unlisting, Lab mapping, deployment, and Git are distinct non-atomic mutations. One failure can leave a partial public swap.
8. **The workflow has no comprehension failure state.** A scientifically correct script can still fail as an explainer. Today’s video standard requires a human listening gate and a paper-naive reviewer who can state what was measured, why it was difficult, what the evidence shows, and what is not claimed.

## 4. The stage missing entirely

Add **Stage 1.5: evidence, source-identity, and representation freeze** before the scientific contract.

Owners: Yui for integration, Goru for bulk source/caption/catalog inventory, Lana for domain meaning, Codex for machine-checkable predicates, Tori for custody. No Kimi by default; escalate only unresolved high-cost rows.

Required outputs per paper:

- canonical manuscript/PDF and catalog hashes;
- bibliography identity resolution by title, authors, year, journal, DOI/arXiv, and topic;
- claim matrix with allowed wording, uncertainty, and forbidden implication;
- exact source table/figure/page for every headline claim;
- final-publisher-versus-preprint reconciliation;
- figure availability, licensing, crop/redraw/conceptual decision, and legibility plan;
- a reproducibility classification for each headline number: independently reproduced, internally sourced, partially reproduced, contradicted, or blocked;
- a “video-reportable now?” verdict distinct from “paper exists” or “study landed.”

This stage would have prevented all four blockers found today from leaking downstream: the unrelated TNG-validation citation, the invalid shared H-beta selection correction, the non-reproducing z≈9–10 subtraction, and the unsupported exact TNG abundance ratios.

## 5. If one Kimi gate must be cut

Cut **Kimi Gate 1: contract freeze** as a mandatory per-paper call.

Keep Kimi at pre-execution script review and final high-risk referee. Those are closest to irreversible compute and public claims, and today’s evidence shows Kimi is especially valuable at fail-open code paths, tie handling, contaminating fields, and overclaim boundaries.

If one subscription seat must own the replacement, choose **Codex** because it is currently unassigned and is a genuinely separate implementation/review surface from Hwao’s authoring lane.

Replacement procedure:

1. Hwao drafts a versioned contract after Stage 1.5.
2. Codex converts every clause into executable invariants, adversarial fixtures, terminal states, and explicit fail-open/fail-closed expectations.
3. Goru enumerates boundary cases and confirms that the named fields/tables actually exist at the required scale.
4. Lana attacks the scientific framing and alternative hypotheses.
5. Yui attacks claim reportability, figure lineage, uncertainty wording, and downstream invalidation rules.
6. Tori seals the reviewed contract, review packets, hashes, and unresolved-item ledger.
7. Any unresolved high-cost clause escalates to Kimi; the default Kimi call is removed, not forbidden.

What we lose:

- Kimi’s independent semantic lens before implementation. Today it caught a mirror-bias clause that licensed publication of a known systematic and an unpinned appendix that allowed recall-set drift. A subscription panel can still share a common premise and miss exactly that class of loophole.
- A single decisive adversarial verdict. Multi-seat subscription review costs coordination time and can produce ambiguous ownership.
- Some efficiency: Kimi may find one deep flaw faster than five subscription seats produce a checklist.

The loss is real. I would accept it only because contract defects remain cheap to amend before execution, while script defects and final-publication overclaims are the two places where a miss is most expensive. The replacement must be adversarial and test-producing; a prose “looks good” review is not an adequate substitute.

## Stage 9: is it buildable with the tooling we have?

**The desired video outcome is buildable with the tooling we have. Stage 9 as written is not buildable as one stage, and the three named generic scripts are not sufficient.**

### What the named tools actually do

- `HermesOps/scripts/assemble_video.py` is a useful clip normalizer/concatenator. It deliberately strips source audio during normalization (`assemble_video.py:86-100`) and then adds only music or silence (`assemble_video.py:159-185`). It has no source-frozen narration timeline, evidence-plot states, manual captions, presenter lineage, claim checks, or semantic QA.
- `HermesOps/scripts/generate_long_video.py` is not a production-safe Flow/Veo pipeline. It contains thirteen hard-coded generic cosmic prompts (`generate_long_video.py:37-50`), closes Chrome windows and drives the foreground UI (`generate_long_video.py:74-103`), uses fragile DOM/download discovery (`generate_long_video.py:127-153`), and ends with raw stream-copy concatenation (`generate_long_video.py:167-174`). It has no account/channel pin, immutable prompt manifest, generation receipt, identity continuity, source grounding, stop conditions, or durable checkpointing.
- `HermesOps/scripts/upload_to_youtube.py` is hard-coded to one old file and defaults that example to `public` (`upload_to_youtube.py:88-96`). It does not pin the NebulaMind channel identity, default to unlisted review, upload manual captions, verify processing/embeddability/privacy, settle a replacement, preserve rollback margin, or write a remote receipt.
- Flow/Veo can provide short atmospheric or conceptual motion and possibly presenter/gesture source material. It must not generate factual text, axes, values, citations, or evidence geometry.
- Nano Banana Pro can help with conceptual illustrations, identity/reference assets, or visual ideation. It is not the authoritative renderer for legible exact on-screen text or quantitative plots. Exact labels and charts should be rendered locally with Pillow/Matplotlib/ffmpeg from frozen data.

### Evidence that the broader stack is sufficient

Today’s accepted Reionization V4 builder demonstrates the viable stack: source freeze and citation ledger; Pillow/Matplotlib deterministic graphics; managed TTS; exact-audio opening presenter through SadTalker; ffmpeg compositing at 1920 by 1080 and 60 fps; manual SRT; encoded-frame, audio, caption, presenter, and semantic QA; then exact-video human acceptance. The MZR audio-first lane demonstrates the same lineage before rendering.

So the tools are sufficient if we use the custom literature-V4 pipeline as the production core and treat `assemble_video.py`, Flow/Veo, and Nano Banana as subordinate asset tools—not as the truth-bearing renderer.

### What Stage 9 gets wrong about video production

1. It starts too late. Story, evidence selection, figure rights, and graphics/narration timing must be co-designed during Stage 1.5 and Stage 8A, not after the paper “lands.”
2. It treats “script from the paper” as sufficient. The video script must come from the source/claim ledger and referee reconciliation. Today several manuscripts contained wrong or unsupported source claims.
3. It has no audio gate. The exact normalized WAV must be listened to and approved before face animation, captions, or full render.
4. It has no comprehension gate. A paper-naive reviewer must demonstrate understanding before expensive media work.
5. It has no sentence-aligned storyboard. Scientific graphics need timed reveals, highlights, plot states, and caveats; a sequence of attractive clips behind paragraphs is not an explainer.
6. It does not distinguish evidence graphics from conceptual/generated illustration. Every non-data diagram must be labeled; generated footage cannot stand in for evidence.
7. It does not freeze presenter motion class or identity. Opening-only face animation, scene-level poses, and continuous full-body gestures require different tools and QA.
8. It does not specify exact encoded QA: complete axes/legends, plot legibility, caption equality, audio correlation, presenter finite window, full decode, hashes, and representative/full-resolution frame review.
9. It combines local artifact and remote release. “Unlisted by default” is necessary but insufficient; upload, captions, processing, watch approval, public visibility, predecessor unlisting, website mapping, deployment, and Git must remain separate gates.
10. “A video is only made for a study that landed” is too rigid. Publication should wait for a landed/accepted study, but a local evidence/storyboard or audio canary can be a valuable pre-landing falsification tool. It exposed manuscript defects today. The artifact must be labeled diagnostic and kept local.

### Replace Stage 9 with explicit sub-stages

- **9A — media eligibility and source freeze:** authoritative human disposition, claim ledger, figure rights, graphics plan.
- **9B — narration plus sentence/action storyboard:** Yui owns; every substantive sentence has a source and timed visual action.
- **9C — exact WAV listening gate:** machine QA plus Duho’s explicit naturalness/clarity verdict.
- **9D — paper-naive comprehension gate:** independent reviewer; no answer key in the packet.
- **9E — no-face motion-graphics canary:** evidence plot readability and timing before presenter cost.
- **9F — presenter bookend/full candidate:** exact approved audio drives presenter, audible mix, and captions.
- **9G — encoded semantic/media QA:** hashes, ffprobe, full decode, captions, loudness, plot legibility, frame/state and presenter-window checks.
- **9H — exact-video human watch acceptance.**
- **9I — unlisted upload plus manual captions:** pin NebulaMind channel; verify processing, privacy, captions, embeddability, and remote hash/metadata receipt where possible.
- **9J — public settlement:** explicit approval; make replacement public, verify, then unlist exact predecessor. Delete nothing.
- **9K — website/Lab mapping and deploy:** separate approval and separate Git/runtime gates.

Yui should own 9A through 9I locally and operationally, but must not self-approve 9C, 9D, 9H, 9J, or 9K.

## Recommended role correction in one sentence

Use flat-rate seats to produce multiple independent, hash-bound artifacts; use Yui to stop bad science from crossing the source-to-public-representation boundary; use Kimi only on the compact unresolved questions where a wrong contract, execution, or public claim would be expensive.

WORKFLOW_INPUT_COMPLETE
