# Lana — Method1 deepening (v2) review / gap-list acceptance criteria

Parent marker: `AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z`
Seed marker: `DEEPENING_RESOURCE_SEED_20260708T043427Z`
Role/lane: Method1 Lana — prose / no-overclaim / trust-communication review. Read-only + this `.hermes` report only. No candidate edits.
Class: **PROGRESS / PRE-FINALIZATION review artifact.** Written at 2026-07-08T04:37Z; earliest finalization 06:34:40Z is ~2h out → this is a gap-list + acceptance-criteria review, **not** a final no-apply packet.

## State check (mtime/size before judging)
- Deepened v2 dir `…/prose-evidence-trust-deepening-20260708T043427Z/`: **not present yet** (checked 04:37Z). Kun generation still in flight per dispatch.
- Per the task, until v2 exists I review the **first-pass gap list**; the deepened v2 will get its own current-file review when it lands.
- Current best on-disk candidate remains the v1 prose-upgrade (`prose-evidence-trust-upgrade/…20260708T041216Z`), which I rated **PASS (prose/no-overclaim)** in `PROSE_UPGRADE_LANA_M1_CURRENT_REVIEW_20260708T041216Z.md` with residual P2/P3 items. The deepening (v2) exists to close exactly those items.

## Gap list carried into v2 (from my v1 review) → acceptance criteria
The dispatch (`AUTOPILOT_M1_DEEPENING_DISPATCH_20260708T043427Z.md` §11–16) targets the right gaps. Acceptance criteria, with **ground-truth numbers I verified now** from the local bindings/coverage ledger so v2 can be checked exactly:

### G1 — 2929 non-committal caution (my prior Finding-A, P2)
- **Must add** a plain-English caution in the 2929 evidence box (not only in the vocabulary note): its **14 rows carry 0 supporting and 0 refuting stances (all `none`; one 0/1 disagree vote)** and are **context, not direct support**.
- **Must flag low relevance:** **4 of the 14 rows** are "A large, long-lived, slowly-expanding superbubble across the Perseus Arm" — a Milky-Way ISM paper, off-topic to the AGN sign/strength claim. (Verified count = 4/14.)
- **Pass condition:** a reader of the 2929 box cannot mistake "14 evidence" for "14 supporting"; the off-topic/none-stance nature is explicit. The inline chip `[2929 · unverified · 14 evidence]` should be paired with, or reworded toward, "14 associated rows (none-stance)."

### G2 — distinct-paper vs row-count wording (my prior Finding-C, P3)
Verified ground truth (v2 must match, no invention):
| Claim | rows | **distinct papers** |
|---|---:|---:|
| 2931 | 20 | **13** |
| 2929 | 14 | **8** |
| 2946 | 9 | **8** |
| **Total** | **43** | **26 (union)** |
- The dispatch's headline "**43 rows across 26 distinct papers**" is **correct** (26 = distinct union across all three claims). ✅
- **Nuance v2 must not garble:** per-claim distinct sums to 13+8+8 = **29**, larger than the union 26, because **9 papers recur across rows and 3 papers are bound to more than one claim** (e.g. `2403.17145` is a `supports` row under 2946 but a `none` row under 2929; `2604.15438` appears under both 2929 and 2931). So "26 distinct overall; 13/8/8 distinct per claim" is the honest phrasing; do **not** write "26 per claim" or sum per-claim distincts into a bigger headline.
- **Pass condition:** every evidence-count headline (inline chip, box header, coverage summary) is accompanied by, or replaced with, the distinct-paper figure so breadth is not overstated by duplicates.

### G3 — trust-label honesty (focus area)
- **Must preserve** the v1 gains: trust vocabulary stays narrow — `debated`/`unverified`/`reported` copied verbatim from the ledger (scores +0.34 / −0.14 / +0.45), no new trust words, no recompute.
- **Pass condition:** 3/30 bound, no trust label attached to any unbound chip, 0 invented levels/scores. Any deepened narrative must not upgrade a level (e.g. must not let 2946 "reported" drift toward "consensus/established," and must keep 2929 "unverified" honestly weak despite 14 rows).

### G4 — unbound labels (focus area)
- **Must keep** the v1 label fix: 27 unbound chips read `no local evidence / unbound` (never "provenance"), with the explicit "not a trust score, must not be read as high trust" statement.
- **Pass condition:** 27/27 unbound chips carry the non-endorsing label; the trust-inversion defect stays closed.

### G5 — no-overclaim in deepened narrative (focus area — the main new risk in v2)
- The dispatch adds "deepened section/claim narrative and evidence-box explanations." **This is where new overclaim can creep in.** v2 must be re-screened for:
  - legacy overclaims 2298/2299/2924 remaining **absent**;
  - 2946 kept scoped/model-bounded ("reported … model-dependent or simulation-bounded rather than a measured prevalence") — no drift to asserted prevalence;
  - 2929 kept conditional ("sign and strength depend on feedback mode and gas phase; positive feedback can occur locally");
  - no new declarative verbs on unbound chips (they have no evidence shown — deepened prose must not narrate them as settled);
  - hedges preserved on the high-z / JWST mass-budget passages.
- **Pass condition:** deepened prose adds explanation/among-mechanism nuance without converting any hedged claim into a settled one; verb strength still tracks trust level.

## Verdict (this pass): **PENDING v2 — criteria defined, no blocker**
- No FAIL. The v1 candidate is honest and no-overclaim; v2's planned scope matches the outstanding P2/P3 gaps.
- The dispatch's key quantitative claim (26 distinct papers) is **verified accurate**; per-claim distinct = 13/8/8 and 2929 off-topic = 4/14 are the numbers v2 must reproduce.
- When `prose-evidence-trust-deepening-20260708T043427Z/` lands, re-review against G1–G5 on the then-current mtimes/sizes before any finalization (which cannot occur before 06:34:40Z).

## Safety ledger
- Reads: local candidate/ledger + `.hermes` reports only. Writes: this one progress report.
- live-root/NebulaMind-origin-main-live write 0 · mirror 0 · restart/deploy 0 · /api/pages·page_versions·DB/SQL 0 · candidate edits 0 · git 0 · browser 0 · cloud/OAuth/secrets 0 · cron 0.
- No hard gate encountered; nothing prompted. `NO ACTIVE EXECUTION PHRASE`. Final packet intentionally deferred past 06:34:40Z.
