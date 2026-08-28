# REPAIR BRIEF — V29. One seat cleared V28. The other's only objection was my tool, now fixed.

Base: `../PREREG_SUCCESSOR_DRAFT_V28_20260827.md`, sha256
`82cd8ac3690fb87b9cf123719cf29f8af37af70e93652ee7e8a2da2b3ee8b587`. **Verify before starting.**
Read `V28_WHOLE_REVIEW_GPT56.md` and `V28_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V29_20260827.md`.** Do not edit V28. **Do not touch V15–V27.**

## Where V28 stands

**GPT56 returned CLEAR** — the first clear verdict on the whole document. It ran the checker itself
and confirmed §10 describes the contract without asserting it passed.

**CODEX returned NOT CLEAR with one blocker, and it was against `tools/prereg_trace.py`, not against
the document's prose.** It built a mirror with a synthetic V29 carrying no `V28→V29` mapping, checked
the **unchanged** V28, and made it fail on a transition that postdates V28 entirely. My scope
predicate was `to >= subject_ver`, so every future transition was mislabelled "the current
transition".

**That is fixed.** The boundary is now exact: transitions past the subject are **out of scope**; the
one whose destination equals the subject is the current transition, checked in the sidecar; earlier
ones are checked in-band against the §10 table. CODEX's test reproduces both ways — with a synthetic
V29 present, checking V28 returns zero; checking V29 itself still demands the mapping.

## The only change V29 makes

**§10's description of the current-transition rule is now wrong in one word.** It says the current
transition is mapped and checked in the sidecar; it must say **which** transition that is.

**Repair — state the three scopes exactly:**
- transitions whose destination is **earlier than this draft** — checked **in-band**, against the §10
  table itself, each row carrying its own result digest;
- the transition whose destination **is this draft** — the current transition, mapped and checked in
  `gates/FINDINGS_MAP.md`;
- transitions whose destination is **later than this draft** — **out of scope; a draft is not
  answerable for transitions that postdate it**;
- **V1→V15** — exempt by a named rule in the checker.

**Also refresh §10's table** from `gates/GENERATED_TRACE.md`, which is regenerated and now carries
`V27 → V28`.

**Do not claim the checker passes.** State what it checks. That rule held in V28 and both seats
confirmed it; keep it.

## Everything else is confirmed and must not move

Stage P `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK` with BS-5p unfillable; the orphan
`VOID-6.1C2-ATTESTATION-FAIL` removed; catalogue quality in the closed pre-lock vocabulary; **§2.7
line 378 byte-for-byte unchanged**; BS-2a DESIGN/UNFILLED; one of fifteen class-P slots filled.

**This is a one-paragraph repair. If you find yourself changing anything else, stop and say why.**

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V29_20260827.md`, complete, single write, titled **V29**.

Do not read `/Users/duhokim/NebulaMindData/`. No image byte is authorised.
