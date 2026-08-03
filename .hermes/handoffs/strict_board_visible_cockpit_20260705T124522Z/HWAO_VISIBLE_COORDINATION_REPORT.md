# HWAO Visible-Coordination Report — strict board-visible cockpit update

Task: `STRICT_BOARD_VISIBLE_COCKPIT_20260705T124522Z` · Coordinator: Hwao/Fable · Mode: all lane work runs **in the visible tmux board panes** (Tori captures pane output as receipts) — no hidden one-shot calls.

## 1. Decision: update the cockpit NOW

The remap milestone is real (packet `…110725Z` executed and verified; consumed phrase retired) and a genuine operator decision is waiting (staged trust recompute, `STAGED_ONLY_AWAITING_EXPLICIT_EXECUTION_APPROVAL`, validation PASS). Under the standing invariant this is exactly when the cockpit must speak and exactly when a phrase belongs above the fold. Lana patches under this direction.

## 2. Lane tasks (run visibly, in this order)

- **Lana** — update canonical JSON and render via the pipeline (canonical → renderer → guard; never hand-edit output HTML). Content per §3. Verify protected anchors (`RICH_BASELINE_STABLE_COCKPIT_V1`, `baseline`, `baseline-steps`, `lane-board`, `safety-ledger`) after render. Post render receipts to the board.
- **Goru** — post-patch mechanical sweep: all public URLs 200 with the new marker; phrase surfaces carry **exactly one** phrase (the staged recompute phrase) and **zero** occurrences of the consumed DB phrase or any retired phrase; queue count 36/36; status JSON consistent with the card; anchors intact.
- **Kun** — boundary check: staged packet's apply/rollback pair present and **unexecuted**, checksums pinned, projections match the packet (7 claims); confirm the Tori-solo scratch path is not referenced or promoted on any public surface (his own standing objection — verify it held).

## 3. Lana may patch directly — YES (content-only, via renderer). Above-the-fold content, verbatim:

- **Marker:** `GALAXY_TRUST_STAGE_DECISION_WAITING_20260705T124522Z`
- **Status line:** *"Evidence re-filing is done and verified in the database (36/36 decisions applied). The article text is unchanged (v1710). ONE decision is waiting for you: a staged trust-label update."*
- **Decision card:**

> **Decision waiting — approve the staged trust recompute?**
> What it does: updates trust labels/scores for **7 claims only** — headline: retired claim **2929 finally drops `consensus` → `unverified`** (its label predates the evidence overhaul and is no longer defensible); the six replacement claims keep their current capped levels (2942 debated · 2943 accepted · 2944 debated · 2945 debated · 2946 reported · 2947 accepted).
> What it does NOT do: no article/prose change, no new claims, no evidence changes, no deploys. Rollback script exists and is pinned.
> To execute, paste exactly: `APPROVE EXECUTE galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z`
> Anything else leaves it staged. Prepared with zero DB writes; recompute executions so far: 0.

## 4. Next-move suggestions to show on the cockpit (each its own gated packet; nothing runs without its exact phrase)

1. **Approve the staged recompute** (above) — recommended first: completes the 2929 story with zero prose impact, rollback ready.
2. **Prose-delta decision after recompute** — judge whether the AGN section wording needs any refresh given the remapped evidence; per Goru's standing block, prose publish stays BLOCKED until an authored+reviewed prose delta exists (likely small or nil; separate packet).
3. **2913/2921 dispositions** — the two held claims still need operator decisions (retire-vs-rewrite; move destination); docs-first, no urgency.
4. **Full-text pinning pass** — upgrade the flagged abstract-only rows (28095, 28141, 28074) and pin 28158's observational X-ray-cavity span, which feeds the standing 2946 observational-heating gap-card ledger work; docs-only.
5. **Semantic-cap commit gate** — if the trust-formula source patch is still uncommitted in the working tree, it remains a one-line operator decision to commit (protects the cap from a stray checkout); git stays locked until that explicit approval.

## 5. Explicit statement

This report and the directed cockpit patch perform: **no DB write, no trust recompute execution, no wiki/prose publish, no git, no restart/deploy, no rollback.** The only mutation authorized here is the Lana-rendered public cockpit content patch.

## 6. Public phrase handling

The consumed DB-remap phrase is dead: must appear **nowhere** (Goru verifies zero occurrences). The staged recompute phrase is the **single** authorized public phrase, displayed on the phrase surfaces with its one-line scope label ("guarded DB trust-label update for 7 claims; nothing else") — a decision is genuinely waiting, so display is correct, not premature. The rollback phrase is **not** displayed (it surfaces only after an execution, per pattern). If the operator pastes anything other than the exact phrase, everything stays staged.

HWAO_VISIBLE_COCKPIT_DIRECTION_20260705T124522Z
