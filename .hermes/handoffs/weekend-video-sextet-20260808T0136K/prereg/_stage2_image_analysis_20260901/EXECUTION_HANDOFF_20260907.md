# EXECUTION HANDOFF — resolved from existing records, no new worker, no anchor (2026-09-07 19:58 KST)

## 1. WHAT EXISTING AUTHORIZATION ALREADY COVERS, AND WHAT IT DOES NOT
Sources, not inference: Duho 2026-09-06 — *"Amend the plan… and make it… run as soon as possible"* (`CODEX_DUHO_CONVERSATION_APPROVAL_RECORD_20260906.md`, Hwao line, concerning the unnecessary 24-hour wait); Duho 2026-09-06 13:00 on the pipeline — *"최대한 빨리 진행해줘"*; Duho 2026-09-07 19:39:06 — *"as your rec"*, adopting the reviewed A1 method.
**COVERED — technical prerequisites inside the adopted method.** The INPUT FREEZE, the anchor, naming a future round, and deriving the split are steps A1 itself specifies; they consume only digests and public randomness. **They publish no protected data, open no images, and read no labels.** Nothing in A1 reserves them for a further user decision, and Duho twice asked for speed. Treating each as a new permission request would be the "generic request to continue" the handoff note forbids.
**NOT COVERED, and not claimed.** Adoption did not perform or waive anything: no anchor exists, no round is designated, no draw has occurred, no protected data has been touched. Protected-data access (tuning render/score, then validation) remains gated on its own terms — see §3.

## 2. COMMIT AND ANCHOR — exact identities, and why C must not be mutated
| item | value |
|---|---|
| commit containing C | `f7486ed56b00d8243a959ee3eff367853910cd9f` |
| C, prepared evidence (NOT an anchor) | `bbc08cd696150f9a077b32a644f0f39b18dc777e8627576c55b6dada8d3269f8` |
| adopted A1 | `6b9ecc79210046fa4c6611953184ece75818214bf4e962e4ac2e308243616e9f` |
**A1 §86 permits two anchor routes**: a public-remote push whose server-side timestamp a third party records, or a provider-timestamped statement. **The second is the better route here, and not for convenience: the anchor must not be under the lane owner's control, and I am the lane owner.** A statement by **Codex — a non-owner — carrying its provider timestamp** binds the three identities above without my being the source of the time. My own push to the public remote is a valid fallback under the first route, but it is my action, and independence is the property the anchor exists to supply.
**How the binding works without mutation.** C's `commit_id` and `external_timestamp` fields stay **UNFILLED**. Filling them would change C's digest and break the very binding being anchored. A **separate anchor record** binds {commit `f7486ed56b00d8243a959ee3eff367853910cd9f`, C `bbc08cd6…`, A1 `6b9ecc79…`} and **quotes the provider timestamp reported by the anchoring party after the event**. It never invents its own timestamp, and it never edits already-anchored content.

## 3. COMPANIONS — what is actually required, and before which action
A1 §123, quoted in substance: V15 remains the signed companion baseline; any V36 identity or pipeline companion relying on this amendment must cite **both** the V15 digest and the adopted FINAL_A1_SHA256 in its own adoption/reference record, naming the clauses relied on; a signed companion is never edited to insert a digest; **"any still-required companion adoption must be completed before its protected action."**
- **Before the anchor, the round, or the selection: NO companion is required.** These consume digests and public randomness only. The generic phrase "companion approval may be required" is not evidence that one is missing, and I am not treating it as such.
- **Before the first PROTECTED-DATA access (tuning render/score): a companion REFERENCE RECORD is required** — the pipeline companion citing V15's digest and the adopted A1 digest with the clauses relied on. The pipeline itself is not unsigned: Duho approved V39 on 2026-09-06 (*"최대한 빨리 진행해줘"*, `CODEX_DUHO_HWAO_V39_PROCEED_20260906.md`) and it was installed. So what remains is a **record to be written, not a decision to be sought** — preparation within existing scope.

## 4. SMALLEST NEXT SEQUENCE, with what already satisfies each step
| # | step | who | already satisfied by |
|---|---|---|---|
| 1 | C committed | done | commit `f7486ed56b00d8243a959ee3eff367853910cd9f`, C verified: 38 input-due digests all present and matching |
| 2 | **anchor**: state {commit, C digest, A1 digest} with a provider timestamp | **Codex (non-owner)** | A1 §86 route two; awaiting Codex's action — **not yet performed** |
| 3 | anchor record binding the three identities, quoting that timestamp | me, after step 2 | template ready; no invented timestamp, C unmutated |
| 4 | name the first drand round scheduled **≥ anchor + 600 s**; authenticate by BLS against the pinned chain with ≥2 hosts agreeing | me | `verify_drand_v2` 4/4; A1's prospectivity rule; **6440756 is excluded — already observed** |
| 5 | derive the split: exactly 400 / 200 / 2,000 from C's inputs and code | me | `select_sample` 16 checks; C's digests; refuses on mismatch or short draw |
| 6 | companion reference record citing V15 + A1 digests | me | required **before** step 7, not before 4–5 |
| 7 | tuning access → render/score/96 configs → winner freeze → single holdout opening | gated | not authorized by this handoff |
**Precise unresolved choice: none requiring Duho.** The only thing standing between here and step 4 is **Codex performing the anchor statement** — a step already inside the method he presented and Duho adopted.
Preserved throughout: drand-only prospectivity, the 600-second minimum measured from a real anchor, exact draw sizes, stage access constraints, and every adopted byte.
