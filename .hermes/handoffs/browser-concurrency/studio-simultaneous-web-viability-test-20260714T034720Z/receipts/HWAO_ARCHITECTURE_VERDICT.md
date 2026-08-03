# HWAO_ARCHITECTURE_VERDICT — mechanical A-vs-B verdict (sandbox evidence only)

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z` · Captain: Hwao. Scope: **mechanical, sandbox-only** — no live-account viability is claimed here. Evidence: broker probe (Tailscale + fresh Thunderbolt), SM-1 ×3, XM-1 pass1r1, Yui non-interference countersign, 42/42 local tests + node/ws checks.

## Evidence of record
- **Architecture A (single machine, Studio):** SM-1 passes 1–3 **PASS, 3/3 reproducible** — byte-identical normalized sha256 `91d32b39…7f7c16` across all three; 24/24/29 in-flight DOM/CDP overlap pairs; every op broker-checked; clean teardown; sockets removed.
- **Architecture B (Studio Flow + Mac Pro DR):** XM-1 **pass1r1 PASS — 1/1 mechanically proven, NOT yet 3-run reproducible.** Real sandbox Chrome on each host, writerA `host_id=studio` + writerB `host_id=macpro` leased from the one Studio broker authority; 22 in-flight overlap pairs; cross-host freeze denied both hosts; partition (dropped `ssh -L`) failed closed; remote controller stopped clean (exit 0). Prerequisite fresh `thunderbolt-pass1r1` broker probe PASS (transport round-trip + live-lease partition fail-closed + authority-reports-non-live).
- **Transport (B):** direct **Thunderbolt** link (169.254.100.0/24), **~0.5 ms, 0% loss**, StrictHostKeyChecking pinned by HostKeyAlias; **no Tailscale fallback — link failure is a STOP** (Tailscale recovery-only, never dialed by the canary).
- **Governance during the run:** the duplicate Hwao invocation of pass1r1 was **REFUSED before execution** by the nonempty-passdir guard (exit 5) — completed evidence preserved, no second run touched anything.
- **Held-gate integrity:** no account, quota, or sign-in/CAPTCHA surface was involved, and **the harness did not address the default Chrome profile or the user Flow window** (it targets only non-default sandbox profiles + exact CDP target ids, DOM/CDP only — a statement of what the code does, not an observational sweep of those apps). **These canaries used zero cua/AX/pointer/keyboard** (writers are DOM/CDP only). Non-interference is supported by a Hwao read-only synthesis from receipts/process-state (`receipts/HWAO_READONLY_NONINTERFERENCE_SYNTHESIS_pass1r1.md`) — **not an independent Yui observation.**

## Mechanical verdict
Both architectures are **mechanically viable** for the target pattern: parallel browser writes on the DOM/CDP path across separate non-default profiles, every action gated by a single fail-closed broker authority, with cross-host freeze and partition proven fail-closed.

- **A is simpler and fully reproducible (3/3), with no network dependency** and no cross-host transport to maintain. Scope note (applies to both A and B): the parallelism proven here is **DOM/CDP-only, and these canaries used zero cua/AX/pointer/keyboard**; any *future* cua/AX/pointer/keyboard automation would require per-host serialization under that host's desktop-control lease (only one such writer at a time per machine) and is not part of what was demonstrated.
- **B removes cross-side desktop contention structurally** (separate per-host desktops), and isolates crash/update/bridge-loss blast radius — at the cost of a cross-host broker transport, `ssh -L` CDP forwarding, a remote controller, and a **new network-partition failure mode** (demonstrated fail-closed). B is proven once (1/1), **not yet 3/3**.

Per the evaluation decision rule (*prefer the simpler architecture unless its safety or reproducibility is materially worse*): **A is the recommended default** — simpler, no network dependency, and 3/3 reproducible. **B is a validated upgrade path** to adopt only if stronger fault isolation (independent desktops / crash-update / bridge-loss domains) is later required, and only after it reaches the same 3/3 reproducibility bar (XM-1 passes 2–3, currently held).

Neither architecture changes the **account plane**, which is identical for both (one Google account): account-wide quota (VERIFIED), same-account concurrent-submission support (UNKNOWN), and Flow/Gemini challenge scope (UNKNOWN). Those are not resolvable by any machine boundary and are out of scope for this sandbox test.

## Separately gated next steps (none authorized here)
1. **XM-1 passes 2–3 (held):** finish B's 3/3 reproducibility set (sandbox, no account) — needs your go; not run under the pass1r1-only scope.
2. **Phase IV live overlap canary (held, requires fresh explicit user approval):** the only step that can establish real same-account Flow + Deep Research active-job overlap — one minimal Flow job + one minimal Deep Research job, submissions serialized under the account-submission lease, challenge freeze armed, fixed small quota budget, capture-and-stop. **No live-account viability may be claimed from these sandbox tests alone.**
3. All original held gates remain: no credentials/cookies/secrets, no sign-in/prompt/CAPTCHA handling, no submissions, no quota spend, no DB/deploy/git/publication/billing/cron, no cua-driver install on the Pro.

HWAO_ARCHITECTURE_VERDICT_20260714T034720Z
