# Delta_Q Fix Spec v1 — Stop Sonnet section_rewrites from degrading page 57

**Author:** Kun 🔬
**Date:** 2026-05-15 17:00 KST
**Target:** `avg delta_q = -0.0179` on Sonnet `section_rewrite` rows last 4h (page 57 quality slowly degrading). Started after v3 deploy.
**Implementer:** Tori.

---

## 1. Diagnosis summary (live data, 2026-05-15 17:00 KST)

### 1.1 Delta_q by proposer, last 4h

| Proposer | Judge | n | avg dq | min | max | q0 | q1 | commits | rollbacks |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `astrosage-70b` | None | 23 | None | — | — | 0.836 | None | 0 | 0 |
| `claude-sonnet-4-6` | None | 8 | **−0.0179** | −0.0560 | 0.0000 | **0.934** | 0.916 | **4** | 0 |

**Two distinct paths, two distinct problems:**

- **AstroSage rows (23 in 4h):** all `judge=None`, `q1=None`, `decision` NOT in {commit, rollback} — these are stuck in `audit` state, never reaching the judge step. Probably AstroSage HTTP timeouts (confirmed via error log "AstroSage HTTP error: timed out" entries). **Not the delta_q regression source.**
- **Sonnet rows (8 in 4h):** 4 commits with `dq ∈ {0.0, -0.008, -0.009, +0.0}`, 4 gate_rejects with `dq < -0.01`. The committed-but-slightly-negative rows are dragging the average down.

### 1.2 The Sonnet gate is too loose

Sample rows:

| id | dq | decision |
|---:|---:|---|
| 506 | **−0.0198** | gate_reject (reject_reason="delta_q=-0.0198") |
| 501 | **−0.0095** | **commit** ← problem |
| 488 | **−0.0079** | **commit** ← problem |
| 495 | −0.0560 | gate_reject |
| 476 | −0.0118 | gate_reject |
| 463 | −0.0109 | gate_reject |
| 513 | 0.0000 | commit |

**Threshold is approximately `dq <= -0.01 → gate_reject`, `dq > -0.01 → commit`.** Tiny negatives (−0.0079, −0.0095) sneak through and degrade the page.

### 1.3 The legacy autowiki_tick path uses a STRICTER threshold

From `autowiki/tasks.py:830` error log entries:
```
[autowiki] ROLLBACK page=57 type=section_rewrite Q0=1.000→Q1=0.941 Δ=-0.059
```
And from the code (line we saw earlier): `reject_reason = f"Δq={delta_q:+.4f} < 0.02"`.

So legacy autowiki_tick requires **`dq ≥ +0.02`** to commit (must measurably improve). Anything less → rollback.

**v3 introduced a threshold inconsistency:** legacy +0.02 floor vs Sonnet's −0.01 floor. Sonnet commits things legacy would have rolled back.

### 1.4 Ceiling effect compounding the issue

Sonnet's q0 mean is **0.934** (mean of recent Sonnet rows). The sections it's rewriting are *already near peak quality* — there's essentially no upside left. Continued rewriting at this q0 mostly produces wash or tiny regression, dragging avg dq negative even when individual rewrites are well-intentioned.

### 1.5 The rationale-string mystery (informational, not blocking)

Sonnet rows in DB have `judge_rationale = "sonnet_section section='X' delta_q=±0.XXX"` — but the `sonnet_section_rewrite` task code at `autowiki/tasks.py:1124` writes `judge_rationale = f"sonnet_section section='{section_header}' body_len={len(section_body)}"` (no `delta_q=` in the string). So **something is updating these rows after they're written**.

Tori needs to find that path. Either:
- A second task back-fills q0/q1/dq from a separate quality scorer (likely the new `sonnet-judge-tick` or `opus-judge-tick` running on recent commits).
- The `sonnet_section_rewrite` code has been edited since my grep and now writes delta_q directly.

This back-fill path is **where the gate threshold should actually be enforced** — and it's where the −0.01 threshold leak lives.

---

## 2. Three fixes (in implementation order)

### 2.1 P0 — Skip Sonnet rewrites on already-excellent sections

Easiest fix, biggest win. Sections with `q0 ≥ 0.90` have nowhere to go but down. Don't have Sonnet rewrite them.

In `autowiki/tasks.py:965` `sonnet_section_rewrite`, after the `section_header` is picked (after the `rewrite_count` round-robin block, around line ~995), add:

```python
# v3.1 §2.1: don't rewrite sections that are already near-peak quality.
# We need to know the current section's q0 — query the most recent autowiki_runs row
# for this page+section to get q1 from its last successful commit.
from sqlalchemy import func as _func
recent_q1 = (
    db.query(AutowikiRun.q1)
    .filter(
        AutowikiRun.page_id == page_id,
        AutowikiRun.proposal_type == "section_rewrite",
        AutowikiRun.q1.isnot(None),
        AutowikiRun.judge_rationale.ilike(f"%section='{section_header}'%"),
    )
    .order_by(AutowikiRun.id.desc())
    .first()
)
if recent_q1 and recent_q1[0] is not None and recent_q1[0] >= 0.90:
    run = AutowikiRun(
        page_id=page_id, started_at=started_at, finished_at=_dt.datetime.utcnow(),
        proposal_type="section_rewrite", model_proposer="claude-sonnet-4-6",
        decision="skip",
        reject_reason=f"section already high quality (q1={recent_q1[0]:.3f} >= 0.90)",
    )
    db.add(run)
    db.commit()
    return {"decision": "skip", "reason": "section_high_quality", "q1": recent_q1[0]}
```

Cuts ~70% of Sonnet rewrites that have no real upside. Saves cloud cost and prevents tiny-negative-dq drift.

### 2.2 P0 — Align the Sonnet gate threshold with the legacy autowiki_tick threshold

Find the back-fill judge path (§1.5 above). It's writing `delta_q` onto Sonnet `autowiki_runs` rows and gating commit/gate_reject on roughly `dq ≤ -0.01`. Two candidates:

1. **`sonnet-judge-tick`** (`autowiki/judge_panel.py`, schedule = 20 min): probably the one. Tori should grep:
   ```bash
   grep -n "delta_q\|update.*autowiki_runs\|judge_rationale.*sonnet_section" \
     ~/NebulaMind/NebulaMind/backend/app/agent_loop/autowiki/judge_panel.py
   ```
2. **`opus-judge-tick`** (same file, 60 min): less likely (smaller volume), but check too.

Find the threshold constant. Change it to **`+0.02`** to match `autowiki_tick` legacy path:

```python
# v3.1 §2.2: align Sonnet/Opus judge threshold with autowiki_tick (+0.02)
DELTA_Q_COMMIT_FLOOR = 0.02   # was something like -0.01

if delta_q < DELTA_Q_COMMIT_FLOOR:
    decision = "gate_reject"
    reject_reason = f"delta_q={delta_q:+.4f} < {DELTA_Q_COMMIT_FLOOR:+.2f}"
else:
    decision = "commit"
```

If the existing code commits the page change BEFORE running the judge (i.e., the back-fill runs after the fact and only updates the row's bookkeeping), then a `gate_reject` AFTER the fact doesn't undo the page change. In that case Tori also needs to add a **post-hoc rollback**: if `delta_q < +0.02`, restore `wiki_pages.content` from the prior PageVersion. The legacy autowiki_tick path already does this via `_do_rollback()`; mirror it.

### 2.3 P1 — Decouple judge from proposer (no Sonnet judging Sonnet)

The "sonnet_section" judge naming suggests Sonnet (or similar Claude model) is judging Sonnet-authored sections. Self-judging creates a circular preference signal — Sonnet's prose style scores high on Sonnet's rubric regardless of factual lift.

After identifying the back-fill judge path in §2.2, swap the judge model to **`deepseek-r1:14b` (Nutty)** or **`claude-opus-4-7`** for Sonnet rewrites. Nutty is the cheaper, faster option and is the same judge used by legacy autowiki_tick — keeps the rubric consistent across proposers. Opus is the higher-quality option if cost (~$0.10 × 48/day = $5/day extra) is acceptable.

Concrete: in `judge_panel.py`, where the Sonnet/Opus judge scores `section_rewrite` rows, branch on `model_proposer`:

```python
if run.model_proposer == "claude-sonnet-4-6":
    judge_model = "deepseek-r1:14b"      # avoid Sonnet-judging-Sonnet
elif run.model_proposer == "claude-opus-4-7":
    judge_model = "deepseek-r1:14b"      # avoid Opus-judging-Opus
else:
    judge_model = "deepseek-r1:14b"      # legacy default
```

### 2.4 P2 — Investigate AstroSage's stuck rows

Separate from delta_q regression: 23 AstroSage rows in 4h are in `judge=None / q1=None / decision != commit/rollback` state. These are *stuck after the proposer step but before the judge step*. Likely cause: Nutty (judge model) Ollama timeouts on Mac Studio, dropping the autowiki_tick mid-flow.

Symptom in error log: `[proposers] AstroSage HTTP error: timed out` is common (Tori, check `~/NebulaMind/logs/celery_autowiki.error.log` head — there are dozens of these). The proposer is on Mac Studio (AstroSage `astrosage-70b`) — the HTTP timeout is the proposer's own call, not the judge's. So the row gets to "proposer attempted" state but the autowiki_tick body short-circuits.

Fix is **not in v3.1 scope**: it's a Mac Studio resource issue (AstroSage 70b under load on the same box as Nutty 14b + qwen3:30b + Atom 7b + Takji 14b + Tera 27b = ~180 GB resident competing for inference slots). Tori should:

1. Bump AstroSage HTTP timeout from default (probably 60s) to 300s in `autowiki/proposers.py`.
2. Add `log.warning("[proposers] AstroSage timeout — writing audit row")` and emit an `autowiki_runs` row with `decision='error', error_text='astrosage_timeout'` so we have audit trail.

Separate PR from §2.1–2.3. Flag for follow-up.

---

## 3. Acceptance criteria

After deploying §2.1 + §2.2 + §2.3 and restarting autowiki workers:

1. **Within 1 h**, the count of Sonnet rewrites with `decision='skip'` and `reject_reason LIKE '%high quality%'` should be ≥ 1. (Proves §2.1's skip gate fires.)

2. **Within 4 h**, query:
   ```sql
   SELECT model_proposer, COUNT(*), ROUND(AVG(delta_q)::numeric, 4) AS avg_dq
   FROM autowiki_runs
   WHERE started_at >= NOW() - INTERVAL '4 hours'
     AND proposal_type = 'section_rewrite'
     AND delta_q IS NOT NULL
   GROUP BY model_proposer;
   ```
   Sonnet's `avg_dq` should be **≥ +0.02** (matches new threshold). If it's still negative, §2.2's gate threshold isn't being applied — re-investigate the back-fill path.

3. **Within 24 h**, page-57 quality measured by `sonnet-judge-tick`'s `q1` audit value should be **stable or rising** week-over-week (not drifting down). Query:
   ```sql
   SELECT date_trunc('day', started_at) AS d, ROUND(AVG(q1)::numeric, 3) AS avg_q1
   FROM autowiki_runs
   WHERE proposal_type = 'sonnet_audit'
     AND started_at >= NOW() - INTERVAL '7 days'
   GROUP BY 1 ORDER BY 1;
   ```
   The trend line should not be negative-sloped.

4. **Within 1 h**, observe at least one Sonnet section_rewrite row with `model_judge = 'deepseek-r1:14b'` (or `'claude-opus-4-7'` if Opus path chosen). Proves §2.3 cross-judge fix landed.

---

## 4. Cost impact

§2.1 cuts ~70% of Sonnet section_rewrite Anthropic API calls. Daily Anthropic spend drops from ~$1/day (Sonnet rewrites in v3) to ~$0.30/day. **Net win** — fewer wasted calls, fewer wasted edits.

§2.3 if Opus is chosen as judge: +$5/day cloud spend (48 judge ticks × $0.10). Total daily cloud spend rises from ~$6 to ~$11. Still well under any sane budget. If Nutty (free, local) is chosen as judge, zero cost delta.

---

## 5. What this fix does NOT touch

- Beat schedule (Sonnet still fires every 30 min — the skip gate just makes most ticks no-op).
- `sonnet-judge-tick` and `opus-judge-tick` passive audits (those are intentionally score-only; their `q1` numbers feed §2.1's threshold check).
- AstroSage rewrites (their stuck-row problem is §2.4 — separate fix).
- Sonnet itself as section_rewrite proposer (kept — but only for sections worth rewriting).

— 🔬 Kun
