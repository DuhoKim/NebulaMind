# HWAO — approval frame: restoring usage-limit coverage

Stamped 2026-08-10 17:37 KST, on Tori's read-only inventory
(`TORI_COCKPIT_USAGE_LIMIT_COVERAGE_INVENTORY_20260810T1733K.md`). **Nothing has been written,
started or restarted.** This is a decision document.

## What is actually broken

Not the dashboard. **The upstream provider-usage monitor is not running** —
`live_provider_usage_monitor.py` has no process and no tmux session. Its last observation is
`2026-08-09T04:02:37Z`, **28 hours stale**.

The private renderer is healthy (PID 31235, rendering every 20 s) and **needs no restart**. When
its source is older than an hour it *hides* provider cards: it builds nine and displays three.
That is why Duho sees three usage limits.

## The design flaw, which matters more than the outage

The dashboard did not say "stale". **It silently got smaller.** Six provider cards vanished, and a
missing card looks like a pool we never tracked rather than a meter we stopped reading.

That is the same failure shape as the null utilisation that was being rendered as a measured
"0% used" earlier in this run — an unmeasured pool wearing the uniform of a reading. Here the
uniform is absence. **A gap you can see is safe; a gap that looks like completeness is not.**

## The six hidden cards

`Claude / Fable / Lana` (Fable 5-hour, Fable weekly, all-models weekly) · `Gemini app / consumer`
(current-window, weekly) · `Hermes / Nous credits` (monthly plan pool, purchased top-up) ·
`Moonshot / Kun` (wallet — **overlaps** the visible Kimi card and needs deduplication, not two
apparent budgets) · `Antigravity / Gemini` (weekly + 5-hour agent requests) · `Codex` (GPT and
Spark, 5-hour and weekly).

Still visible: Kimi/Moonshot direct API, Flow/Veo credits, YouTube Data API.

## DECISION 1 — start the monitor (needs Duho's explicit approval)

**What runs:** the established `live_provider_usage_monitor.py`, nothing new or modified.

**What it reads — this is why it is gated:**
- the **local Claude OAuth credential**, to call the read-only usage endpoint
- Hermes' **read-only Nous account reader**
- the **official Moonshot balance endpoint**

**What it writes:** the guarded **public** status file. That is a public surface, not the private
cockpit.

**What you get:** fresh values in all nine cards, ingested by the live renderer within ~20 s. No
restart of anything else.

**If you decline:** the dashboard keeps showing three cards from a 28-hour-old feed. Nothing
breaks; coverage stays wrong.

## DECISION 2 — make outages visible instead of invisible (recommended regardless)

Patch the renderer's stale branch so provider cards **remain visible as `Stale` / `Unknown`**, with
current percentages removed and old values moved into explicitly historical copy.

This needs **no credential access and no provider call** — it is a rendering change, prepared as an
exact-diff preflight and applied only on your say-so. **I would take this one even if you decline
Decision 1**, because it converts a silent disappearance into a visible "we stopped reading this".

## What will not be invented either way

Context-window use is not subscription quota and stays filtered. Gemini CLI OAuth quota and the
`generativelanguage` API-key pool are distinct and uncollected — the key lane is documented as
disabled. Kimi purchased cash has no fixed maximum, so it cannot honestly produce a percent gauge.
YouTube publishes ceilings but not exact remaining units. Codex 5-hour headroom, Claude per-model
weekly meters and Antigravity Claude/GPT meters exist as named fields but are **unobserved** and
will be labelled so rather than filled.

## Still held

No monitor start, no HTML hand-edit, no watcher restart, no public write, no account/billing/OAuth
page access, no browser capture, no provider call, no DB/wiki/deploy/Git/cron/config/secret action
until Duho answers.
