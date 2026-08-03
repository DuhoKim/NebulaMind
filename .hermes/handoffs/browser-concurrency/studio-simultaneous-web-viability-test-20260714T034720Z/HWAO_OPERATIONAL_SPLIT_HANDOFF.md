# HWAO_OPERATIONAL_SPLIT_HANDOFF — split architecture operating mode

> **CURRENT STATUS: ACTIVE STOP / FROZEN (2026-07-14).** A Flow go-live attempt on the Studio hit a Google account challenge (Korean-locale "Action required" toolbar label) on Yui's READ-ONLY capture; Yui froze BOTH sides pre-submit — zero submit, zero lease, zero quota. Yui's **live broker authority (PID 72222, tmux `architecture-b-live-broker`) is RUNNING and FROZEN and must stay so — do NOT kill, do NOT unfreeze.** Ledger: epoch16 go-live ack -> epoch17 emergency_stop -> epoch18 pre-submit STOP. Receipt `receipts/YUI_FLOW_GOLIVE_PRE_SUBMIT_STOP.md`. **Only Duho may authorize a broker reset after manual inspection of the account challenge.** This banner supersedes the "no browser/job launched" phrasing below: the split went live (read-only Flow capture + running frozen broker), while the submission/quota/account gates held.

Decision of record: `USER_ARCHITECTURE_DECISION_DR_PRO_FLOW_STUDIO.md` (sha256 `5d0109e6…87bda`), ledger epoch 14. Architecture **B (two machines)** is adopted as the operating mode: **Deep Research runs on the Mac Pro; Duho works Flow separately on the Mac Studio with Yui.**

## Roles
- **Hwao** — sole coordinator/captain; runtime calls, adjudication, ledger authority. Coordination is **ledger-mediated**; Hwao does not drive browsers.
- **Tori** — Deep-Research-side **correspondent / receipt verifier on the Mac Pro** (relay, record, verify, report). DR is pure DOM/CDP (cua-driver absent on the Pro).
- **Yui** — Flow-side **correspondent on the Mac Studio**, alongside Duho's own Flow work. (Flow is cua-bound; its blast radius is physically isolated on the Studio.)
- (Standing role memory further designates Yui/Tori as lane operators under broker leases with agy drivers; this handoff uses the correspondent/verifier framing per the decision receipt.)

## Transport
- **Direct Thunderbolt is primary** (link-local 169.254.100.0/24, ~0.5 ms, 0% loss), StrictHostKeyChecking pinned by HostKeyAlias.
- **Tailscale is recovery-only** — never dialed during normal operation; a Thunderbolt link failure is a STOP, not an auto-failover.

## Broker & source of truth
- **One Studio broker authority** owns all agent-controlled shared resources: target leases (host-aware), the machine-wide/per-host desktop-control, clipboard, and focus leases, and the **global account-submission lease**. No lane acts without a live lease; fail-closed on lease/identity loss (never a frontmost fallback).
- One append-only, hash-chained **run ledger** is the single source of truth; correspondents write observations, never re-scope lanes; disagreements are STOP-class to Hwao. Anyone may declare emergency STOP; the broker freezes; only Duho gates resume.

## Reproducibility status
- **XM-1 passes 2–3 are NO LONGER a prerequisite** for operating the split, per this decision. They remain **HELD** and available if a full 3/3 reproducibility record for Architecture B is wanted later. B is mechanically proven 1/1 (`receipts/HWAO_ARCHITECTURE_VERDICT.md`).

## Held gates (shared single Google account — unchanged, binding)
The two sides share one Google account: **account-wide credit/quota, and a challenge/CAPTCHA freezes BOTH sides; same-account concurrent-submission support is UNKNOWN.** Therefore, still gated: any live Flow or Deep Research submission, any quota/credit spend, sign-in/security/CAPTCHA handling, and simultaneous LIVE runs. A simultaneous-live posture requires one of: **separate Google accounts** (hosts already measured distinct public egress, which helps the automation-flag risk), **the gated Phase-IV live-overlap test**, or **time-separated runs** — each a fresh explicit Duho gate.

## Operating boundaries (updated for ACTIVE STOP / FROZEN)
- **While FROZEN:** the broker (PID 72222) stays running/frozen; **no unfreeze, no kill, no DR/Flow launch, no lease, no submission, no account/quota/sign-in/challenge handling.** Only Duho, after manual inspection of the account challenge, may authorize a broker reset.
- The account challenge itself is Duho's to resolve manually; Hwao/agents do not click, navigate, or handle it.
- No cua-driver install on the Pro (DR stays DOM/CDP-only). Coordination is via the shared ledger and receipts only; no direct hermes↔agy peer control.
- The challenge freeze fired correctly as a STOP condition. Other STOP conditions (two-sided simultaneous submit attempt, lease/fencing anomaly, orphaned process, Thunderbolt link failure) likewise escalate to Hwao immediately; resume is Duho-gated.

HWAO_OPERATIONAL_SPLIT_HANDOFF_20260714T034720Z
