# CODEX referee report — proposed replacement §6, fifth pass

## Verdict

**NOT CLEAR.** R5 does move the projection writer before the named instrument runner and honestly removes confidence from the pre-lock projection. That is real movement, but it does not make row C2 outcome-free by construction. C2 still exports an actual checksum whose preimage is the galaxy cutout itself; the draft's own scope classifies both that cutout and an opaque digest of it as χ-bearing because the pixels carry the morphology from which handedness is inferred. C2 also promises an execution-completion/non-finite field before row D has executed, so that field is either not the instrument predicate §2.7 needs or must be filled later from the outcome-bearing execution. Nothing enforces “never invokes the classifier” or C2-before-D: the mediator can log a lawful cutout read but cannot see what C2 computes locally, and row D's authorization does not depend on a completed C2 projection receipt. The same capability has therefore been moved earlier and renamed, not removed. Blocking findings: 1–3.

## Numbered findings

### 1. BLOCKING — C2's permitted checksum is itself an outcome-capable channel

**Row / sentence at issue.** Scope lines 29–35 and 52–59; row C2 (line 94); Part 3 C1 (line 198); Part 5 item 1 (line 216).

**Why it fails.** Row C2 reads the cutout and exports its expected/actual checksum. The checksum is indeed of bytes C2 read rather than of a classifier output, but that does not establish the required property: the read bytes are the galaxy image from which handedness is inferred. Changing the image under a handedness-reversing transformation changes the byte digest. The draft itself defines every cutout as χ-bearing (lines 29–35) and “any opaque digest of χ-bearing bytes” as χ-bearing because it is a verification oracle (lines 54–58). Item (v)'s classification of the acceptance projection as non-χ-bearing therefore contradicts the governing default while carrying the actual cutout digest. Moving the digest producer before inference removes knowledge of row D's later result; it does not make the digest incapable of encoding or identifying spin sign.

The other fields do not cure this. A canonical shape derived mechanically from bytes can be technical and sign-insensitive, but “attempt identity” is not given a closed canonical source/serialization that prevents outcome-coded values or lookup against prior knowledge. A checksum is not made harmless by being authentic: authentication preserves the channel exactly.

**Smallest sufficient repair.** Keep all cutout digests inside the sealed store. Pin a pre-inference in-store integrity verifier that recomputes them but exports only narrowly enumerated authenticated predicate bits (for example, parent-attempt present, byte-integrity pass, canonical-shape pass), each bound to an independently fixed parent/attempt manifest. Define the canonical source and serialization of attempt identity. Do not call a bundle containing a cutout digest non-χ-bearing.

### 2. BLOCKING — the pre-inference projection cannot truthfully carry the execution/non-finite predicate it promises

**Row / sentence at issue.** Non-χ-bearing class (line 52); phase line (lines 72–76); rows C2, D and E (lines 94–96); Part 2 item 5 (line 189).

**Why it fails.** C2 must finish before D, yet its output schema includes “execution completion/non-finite status.” If this means C2/cutout execution status, it cannot establish §2.7(2)(c), whether the later instrument output is absent or non-finite. Row E nevertheless reads only the C2 projections and claims to compute the structural §2.7 predicates after inference. If the field instead means row D's instrument completion/finiteness, C2 cannot know it pre-inference; filling or updating it after D reintroduces exactly the outcome-bearing producer/channel R5 says it removed. No later separately pinned, outcome-incapable producer of the instrument predicate is named.

This is not a wording nit. Under the stated order, one of the closed exclusion predicates has no truthful evidence source. Under the only obvious repair—letting D or a post-D process author the field—the original writable status channel returns.

**Smallest sufficient repair.** Split the contracts. Let C2 attest only pre-inference cutout/attempt facts. For instrument presence/finiteness, pin an atomic sealed transaction or independent execution supervisor that registers launches before execution, commits output bytes and terminal state atomically, derives presence/finiteness mechanically inside the sealed boundary, and exports only authenticated predicate proof. Row E must verify that proof rather than trust a D-authored boolean. If that construction cannot be supplied, defer this predicate too and state the resulting cost.

### 3. BLOCKING — “never invokes the classifier” and C2-before-D are promises, not enforced boundaries

**Row / sentence at issue.** Rows B, C2 and D (lines 92, 94–95); clauses 2 and 4 (lines 128–134 and 154); Part 5 item 1 (line 216).

**Why it fails.** BS-2a is said to pin C2's symbol and digest, and executing the classifier is listed as a void condition. Neither makes invocation fail. C2 already has the classifier's necessary raw input—the cutout. Row B can observe and log the permitted cutout read, but it cannot distinguish a checksum computation from a classifier invocation, an equivalent reimplementation, a subprocess, or a local model call over those same bytes. No capability allowlist, hermetic worker profile, import/weights denial, executable call-graph gate, or runtime attestation is specified.

The ordering is likewise descriptive. Row D's authorization is BS-3, BS-9 and the cutout-completion receipt; it does not require a complete authenticated C2 projection set or a C2 phase-completion receipt. The mediator therefore has no named prerequisite whose absence forces a D request to fail. D can run before or concurrently with C2 while satisfying its authorization column. Shared mediation makes touches auditable; it does not, by itself, make the phase separation real.

**Smallest sufficient repair.** Make one authenticated C2 completion artifact over the exact parent/attempt set a hard authorization prerequisite for row D, and require row B to refuse D until that artifact verifies. Pin and gate C2 as a hermetic worker whose permitted inputs, imports, executable/model weights, filesystem, network, subprocess and sealed-store capabilities are allowlisted; externally attest the runtime profile and producer digest. End-to-end fixtures must rerun the real producer under transformed/adversarial cutouts and reject classifier/model access, not hold the projection fixed.

### 4. HIGH — C2 is assigned to a slot that is presently refused and the delivered bytes do not supply a replacement contract

**Row / sentence at issue.** Row C2 and clause 2 (lines 94 and 132–134); Part 2 items 5 and 7 (lines 189–191); brief context naming `BS2A_REVIEW_{GPT56,CODEX,KIMI}.md`.

**Why it fails.** All three BS-2a referee reports end `NOT CLEAR`. They converge that the only frozen confidence quantity is `abs(chi_net)`, that mirror-evenness does not remove amplitude, and that upstream producer-authored evidence can encode outcomes. R5 correctly removes confidence from C2, but it does not provide a fillable replacement BS-2a contract for findings 1–3 above. The current pinned v9 code contains neither `verify_cutout_integrity` nor `recompute_acceptance_ledger`; its `SLOT_SCHEMA` contains no BS-2a or BS-2k. R5 discloses these as future work, so C2 cannot run under the current pin, and the refused BS-2a cannot authorize it by receipt insertion.

**Smallest sufficient repair.** Keep BS-2a refused and BS-6 blocked. Produce a new BS-2a design/code candidate implementing the sealed-digest verifier, split execution attestation, hard C2→D phase receipt, schemas and adversarial fixtures above; gate that candidate before integrating this §6 replacement. Do not cite the refused BS-2a as if it were an available pin.

## Checks that held / failed attacks

1. **Universal access-ban regression attack failed.** The table preamble, clauses 1–2, and row R bind every person and process; the rule bans access, not merely disclosure, and no role-scoped carve-out reappears.
2. **Committee-path regression attack failed.** The BS-8p/allocation → G view → H-only ingestion → in-store label-set receipt → I aggregate path remains authorized, and clause 5 does not void a conforming committee act.
3. **Lock-order regression attack failed.** The named producer chain remains BS-5f → BS-L → unblinding → BS-7f → BS-V; BS-L is class E and does not certify a set containing itself.
4. **Threshold-timing attack held in the text as inherited.** Current V15 §2.7(7) fixes the numeric threshold in BS-3 before any image byte, and R5 moves application—not selection—post-unblinding. R5 does not authorize choosing the threshold after unblinding. This does not make the refused `abs(chi_net)` confidence design valid, and findings 1–4 still block.
5. **§7 count arithmetic held.** Independent lint on current V15 reported 20 rows: 14 class P and 6 class E. Removing class-P BS-L, adding class-P BS-2k, and adding BS-L to class E leaves 14 class P and yields 7 class E. Part 2 correctly says “One of fourteen” and directs replacement of the DESIGN inventory so BS-2a/BS-2k are included and value-only BS-2f is excluded.
6. **BS-2k is not shown impossible merely because it is future work.** Its mediation boundary is stated as a gate condition and inability to enforce it makes the slot unfillable. I found no textual dependency cycle introduced by moving BS-L to class E. Its actual implementation and raw-store exclusivity remain unverified testimony.

## Mechanical and evidence checks

- Recomputed `SECTION6_DRAFT_AGY_R5.md` sha256 as `63782432d816ef74581f5e9d9a181105b9926b7a16bee48acd0288d6593d6654`, matching the brief.
- Read the complete R5 draft, the review brief, current V15 §2.7/§6/§7, all three BS-2a referee reports, and both CODEX/GPT56 R4 reports.
- Ran the current-document linter: exit 0; 20 §7 rows, 14 class P / 6 class E; no current-document inconsistencies. This does not test the unintegrated R5 replacement.
- Inspected current `ref/successor_ref_v9.py`: `SLOT_SCHEMA` has BS-3 `tau` but no BS-2a/BS-2k/BS-L; the file has `run_production_verdict` but no `verify_cutout_integrity`, `recompute_acceptance_ledger`, `verify_lock`, `verify_unblinding_receipt`, or `verify_archive_seal`.
- No data fetch, image read, χ computation, sealed-store operation, archive-content read, credential/key access, or `/Users/duhokim/NebulaMindData/` access occurred. The only file written is this report.

## Testimony

I did not verify any historical or current outcome access, archive seal state, raw-store exclusivity, committee isolation or memory, or the existence/behavior of the proposed mediator, integrity verifier, acceptance ledger, execution supervisor, lock/unblinding/archive verifiers, schemas, receipts, sandbox or integrated fixtures. I did not locate the YUI appendix independently; the line-82 `abs(chi_net)` fact is stated by the supplied brief and independently reported by all three supplied BS-2a reviews, and I use it only as testimony. Assertions about what future implementations could enforce are repair requirements, not claims that those implementations exist.

**NOT CLEAR**