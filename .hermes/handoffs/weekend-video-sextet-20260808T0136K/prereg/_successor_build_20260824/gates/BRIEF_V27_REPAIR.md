# REPAIR BRIEF — V27. The language repair held. Three things it was told to do and did not.

Base: `../PREREG_SUCCESSOR_DRAFT_V26_20260827.md`, sha256
`2eec8da41ee69374fcc9c3fca2de150b29c04ca7b921848e908fa97a20bffd52`. **Verify before starting.**
Read `V26_WHOLE_REVIEW_GPT56.md` and `V26_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V27_20260827.md`.** Do not edit V26. **Do not touch V15–V25.**

## What held — the round's central repair succeeded

Both seats confirm independently. CODEX: *"No claim of statistical independence from handedness
survives, and the conditional-independence gap is stated as open rather than replaced by a confident
weaker statistical claim."* GPT56: *"No affirmative independence-from-handedness claim survives."*

**Do not touch §2.7 line 378.** It is the sentence both seats validated.

## Blocker 1 (CRITICAL, both) — the predicate is not in the closed reason list it must belong to

§2.7 declares its pre-lock exclusion reasons **closed and exhaustive**, and catalogue quality is not
among them — so the document operates an exclusion that its own vocabulary does not admit.

**Repair (CODEX's, take it literally):**
- **Add catalogue quality to §2.7's closed pre-lock exclusion vocabulary**, and define in the
  BS-2a/Row-E path its **exact authenticated fields, source digest, one-to-one join keys, verifier,
  and failure effect**.
- **Remove catalogue quality from Row P's P8 decision precedence and from the post-unblinding
  adequacy receipt's fatal `EXCLUDED-BY-*` set** — or carry it there **only as an already-resolved
  pre-lock status that cannot constitute a P8 removal.** Pick one and be explicit.
- **Keep P8 absence, non-finiteness and instrument-confidence separate.** They are different things
  at a different phase.

## Blocker 2 (HIGH, both) — Stage P was told to be marked superseded and was not

§2.6 lines 292–312 and §4 lines 448–450 still present **995/1000** as standing. **It was computed on
65,060 and the analysed population is 49,211.** This was in the V26 brief and did not happen.

**Repair:** mark it **superseded**, and state that **BS-5p cannot be filled until Stage P is rerun on
the actual post-exclusion mask.** Do not soften it to "may need revisiting".

## Blocker 3 (HIGH, CODEX) — reverse `VOID` reachability, and a false closure claim in the preamble

**Repair:** **delete the false preamble closure claim.** Then either **define the exact C2
attestation-failure antecedent and its effect in Row C2**, or **remove the orphan registry ID**. Keep
**reverse reachability explicitly unresolved and BS-6 blocked** until a pinned converter, schema,
registry digest and fixtures establish exact bidirectional closure. An orphan ID in the registry is
worse than an admitted gap, because it reads as coverage.

## Now true, and the document may say so — the findings mapping is enforced

`tools/prereg_trace.py --check` now **returns zero** on V26 under an encoded coverage contract:
in-band coverage stops at the subject's predecessor; the current transition is mapped in the sidecar
`gates/FINDINGS_MAP.md`; V1→V15 are exempt **by a named rule in the checker**, not by silence. A
V25→V26 mapping has been added. Removing any mapping makes the check fire on exactly that transition
— controlled, not assumed.

**§10 may now state that the mapping is enforced**, because it is. Say *how* — the three rules above —
rather than only that it is.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V27_20260827.md`, complete, single write, titled **V27**.

Do not read `/Users/duhokim/NebulaMindData/`. No image byte is authorised.

**Two of these three were in the V26 brief and did not happen. Check each against the document before
you finish, not against your intention to have done it.**
