# OPEN QUESTION — two V34 findings I repaired around, not through

**Raised 2026-08-29 06:10 KST by Hwao under self-continuation. Both change what the study claims or
what its frozen inventory contains, so both stop here.**

The absence-clause round found four defects. I fixed three in V35; these two I did not, and the
reason is different for each.

---

## 1. "must be bound before BS-6" has no edge that makes it true (GPT56-V34-1, HIGH)

§1 line 120 says the sensitivity-gradient control's statistic, sample, stratification, uncertainty,
bound, acceptance rule and failure consequence **"must be bound before BS-6."**

**Nothing in the document constructs that precondition.** GPT56 parsed §7 independently: fifteen
class-P rows — BS-1, BS-1b, BS-2a, BS-2k, BS-2v, BS-2c, BS-2o, BS-5p, BS-2s, BS-2m, BS-3, BS-9,
BS-4, BS-7p, BS-8p — and **none is the sensitivity-gradient control.** The rows that block BS-6 are
BS-2a, BS-2k, BS-2v, BS-9, BS-7p; none names the control or a receipt from it. §11 has no producer,
verifier or receipt binding for it either.

> **A future operator can fill every enumerated class-P slot, pass every enumerated gate, and reach
> BS-6 with the control still DESIGN/UNFILLED.** The sentence would be false and nothing in the
> document would notice.

This is the assigned failure shape exactly, and the passing checks make it worse rather than better:
lint and trace *confirm* the closed §7 inventory is 15/8 and contains no control slot.

**Why I stopped.** The smallest repair is to add a named class-P DESIGN slot with a `blocks BS-6`
edge. That **moves the frozen class counts from 15/8 to 16/8** — a change to the document's
normative inventory, emitted by `prereg_counts.py` and gating the lint. Adding a slot is not
specification tidying; it changes what the preregistration commits to.

**Options.** (a) Add the slot, counts move to 16/8, and the control genuinely blocks BS-6. (b) Add
the `blocks BS-6` dependency to an existing row (BS-3 is the natural host) without a new slot —
cheaper, counts unmoved, but it buries the control inside a row whose subject is the instrument
identity. (c) Delete the "must be bound before BS-6" sentence and stop claiming the precondition —
honest, and gives up the protection. **I would take (a); it is the only one where the sentence
becomes true.** But the count change is yours.

---

## 2. `require_authorization()` accepts arbitrary bytes (CODEX-V34-2, HIGH)

§5 lines 511–514 say the guard refuses real data without an authorization file pinned to a SHA-256,
and treats "the authorization does not exist" as a run guard.

**CODEX executed the pinned `successor_ref_v9.py` against `BRIEF_V34_REVIEW.md` — a referee brief —
and `require_authorization(brief_path, brief_hash)` returned successfully.** The runner takes both
`authorization_path` and `authorization_sha256` from its caller and only checks they agree with each
other. There is no authorization schema, signer, study identity, permitted operation, run identity,
or independently frozen expected digest.

So the document can say no authorization exists while the operative guard accepts any existing file.

**Why I stopped.** The repair is a build, not an edit: define a typed authenticated authorization
record with a canonical identity, bind signer/study/operation/schema independently of the caller, and
make the runner read its expectations from frozen configuration. **That means changing
`successor_ref_v9.py`, which is frozen**, and it defines what counts as authorising this study —
which is as close to "what the study claims" as anything in the document.

**Note the guard is not currently load-bearing:** BS-6 and the first image byte are blocked by other
means, so this is not a live path to an unauthorised run. It is a false claim about a guard, not an
open door.

---

## What V35 did fix

- **§1 line 120** — "a biased or broken `w` cannot create one" narrowed to what the identity actually
  enforces. Both seats; the document contradicted itself three sentences later.
- **§6.2 line 592** — the claim that an unlogged archive read breaks the log chain is **deleted**. An
  observational read need not modify any record; detection is no longer claimed, and the burden is
  put where it belongs, on BS-2k demonstrating exclusive mediation.
- **§7 line 698** — my own overclaim in the BS-2a pin. I wrote "all 325 pairwise deletion probes
  caught, strictly." CODEX's 325 was **filter-derived** from control outputs with **six** pairs
  literally source-mutated, and **GPT56 did not run all 325 at round 6.** Now stated at that strength.

V35 = `b80d50afe076fe8d20c9fd1a6e6b5db63779dfc02ee46601667a67227e12fbdd`. Four checkers pass; §1 scope
and §2.7 line 384 still byte- and position-identical to V30; class counts unmoved at 15/8.

---

## VERIFIED CURRENT AGAINST V36 — 2026-08-29 07:25 KST

Written against V34; the draft is now V36 (CLEAR from both seats). Both findings re-checked against
it, because V35 edited the very line finding 1 cites and it matters whether that repair touched it.

**Finding 1 — it did not.** §1 line 120 still ends *"... must be bound before BS-6."* at the same
line number. V35 rewrote the surrounding sentence (the refuted "a biased or broken `w` cannot create
one") and **left this clause untouched**.
- `prereg_counts.py` on V36: **15 class P, 8 class E**, prose matches the table — so option (a)'s
  15/8 → 16/8 is still the real cost.
- `sensitivity-gradient control` occurs **exactly once** in V36: inside the sentence that claims the
  precondition. **No BS- row is that control.** The document's BS- identifiers are BS-1, BS-1b,
  BS-2a, BS-2c, BS-2f, BS-2k, BS-2m, BS-2o, BS-2s, BS-2v, BS-3, BS-4, BS-5f, BS-5p, BS-6, BS-7f,
  BS-7p, BS-8f, BS-8p, BS-9.

**Finding 2 — unchanged.** §5 lines 511–514 are byte- and position-identical in V34 and V36, still
saying the authorization *"does not exist and must not be written yet"*. Its subject
`ref/successor_ref_v9.py` remains frozen at `6a9abbbd…`.

**Both findings hold on the current draft. Nothing in this file is stale.**
