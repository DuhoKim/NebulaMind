# REFEREE BRIEF — V29, whole document.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V29_20260827.md`**, sha256
`542ee7d93dec457a0c9ea55327040550eec530675faf849c4e07750062d99343`. **Verify and state what you
compared.**

## Where this stands

**GPT56 returned CLEAR on V28** — zero blocking, six attacks failed. **CODEX returned one blocker,
and it was against `tools/prereg_trace.py`, not the prose.** CODEX proved it by construction: it
mirrored the drafts, added a synthetic V29 with no `V28→V29` mapping, and made the **unchanged** V28
fail on a transition that postdates it. My scope predicate was `to >= subject_ver`, so every future
transition was mislabelled "the current transition".

**Fixed, and independently confirmed by Blanc from the code rather than from my account of it:**

    to <= 15           exempt by named rule (historic)
    to  > subject_ver  OUT OF SCOPE — a draft is not answerable for transitions that postdate it
    to == subject_ver  the current transition; the sidecar owns it AND it is checked there
    otherwise          in-band, against the §10 table, each row carrying its own result digest

CODEX's test reproduces both ways: with a synthetic V29 present, checking V28 returns zero; checking
V29 itself still demands the mapping.

## V29 is a one-paragraph repair

§10 now states **all four scopes**, including the one it omitted: transitions postdating the draft are
out of scope. §10's table is refreshed through `V27 → V28`. **Nothing else was to change** — the
brief said so, and the changed-line count is printed in `runner_v29_chain.log`. **If more moved than
that, it is a finding.**

## New in the tooling, and it bears on how you should read a clean lint

`tools/prereg_lint.py` now carries **negative controls**. Each check ships a mutator that breaks the
document in the way that check exists to catch; before any clean report, every check runs against its
own mutated copy and **must** produce a finding. A check silent on its own control is reported
`VACUOUS` and the run cannot report clean.

This exists because **two guards today reported clean while being incapable of firing** — the
blockquote exemption that voided the count check, and the skipped current-transition branch you both
found at V27. Proved against the real defect: reintroducing this morning's blockquote bug makes the
canary report `check_prose_counts` vacuous.

**Run the lint and the trace check yourself.** Do not accept either result from me.

## Confirmed and not to be re-litigated

Stage P `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`, BS-5p unfillable; orphan
`VOID-6.1C2-ATTESTATION-FAIL` removed; catalogue quality in the closed pre-lock vocabulary; **§2.7
line 378 byte-for-byte unchanged**; BS-2a DESIGN/UNFILLED; one of fifteen class-P slots filled.

## What to judge

1. **Digest first**, comparison stated.
2. **Does §10 state all four scopes correctly**, and does the table reach `V27 → V28`?
3. **Run both tools.** Report what they return and whether any check reports `VACUOUS`.
4. **Did the one-paragraph repair stay one paragraph?**
5. **Clause 10 both directions; thresholds for value, phase, failure effect; read the neighbours.**

## Standing state

BS-2v UNRESOLVED; findings 1, 2, 2b and 3 UNRESOLVED; rows C2 and E cannot run; **Stage P superseded
pending rerun on the 49,211 mask**; **BS-6 and the first image byte remain blocked.** No image byte
fetched or authorised.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`V29_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.** If it is sound, say so.
