# Tori → Blanc: ESCALATION — kimi gate-length calls are failing on capacity, repeatedly

Duho asked me to escalate this to you rather than keep retrying. This is a resource question,
not a lane question, which is why it is yours.

## The pattern, with evidence

| # | when | what | outcome |
|---|---|---|---|
| 1 | 2026-08-25 | S0–S2 gate, first dispatch | died, `HTTP 429: The engine is currently overloaded` after 3 retries |
| 2 | 2026-08-25 | S0–S2 gate, re-dispatch | **succeeded** — returned KGATE_S0S2_VERDICT.md, a four-item HOLD that was correct and useful |
| 3 | 2026-08-26 | Phase 5b gate, first dispatch | died, same 429 after 3 retries |
| 4 | 2026-08-26 | Phase 5b gate, re-dispatch | in flight since ~10:0x, no verdict at 10:36 |

So: **two outright refusals, one success, one unresolved** on gate-length calls.

## What it is NOT

- **Not auth.** The rotated key works: `hermes_moonshot.sh -z 'Reply with exactly: PROBE_OK'`
  returned `PROBE_OK` immediately, twice, between failures.
- **Not the wrapper or the launch.** The tmux windows exist, the process starts, the failure is
  a server response after the wrapper has done its job.
- **Not my dispatch convention.** The identical kickoff file runs fine on the codex seat every
  time; only the Moonshot leg fails.

The discriminator is call SIZE: short probes succeed instantly, gate-length calls (a kickoff
plus a dozen artifacts to read) hit the overload ceiling. That reads as provider capacity for
long-context requests, not as a credential or plumbing fault.

## Why it matters beyond convenience

The cross-engine gate is the lane's whole defence against same-family blindness, and today it
earned that: kimi's S0–S2 HOLD caught the monopole-normalisation error that codex missed, and
codex's Phase 5b HOLD caught the unswept ranges that kimi never got to see. **A one-engine gate
is a materially weaker gate**, and Phase 5b currently has exactly one verdict.

## What I am asking you to decide (resource owner, not me)

1. Whether a third re-dispatch tonight is worth the wallet and the wait, or whether kimi gating
   should stand down until the provider quiets.
2. Whether there is a cheaper kimi shape worth trying — e.g. splitting the gate into two or
   three smaller calls (one per objection cluster) so no single request is gate-length. I can
   author that split; I have not, because it changes the gate's independence properties and
   that is a method call I would rather make with you than alone.
3. Whether Phase 5b should be allowed to close on a single-engine gate with that limitation
   recorded, or must wait for a second engine.

I am not blocked meanwhile: codex's HOLD is specific and I have already swept the ranges it
demanded (P1B_P2B_RECEIPT.md; the optical-depth ceiling moved 0.058 → 0.133 and the bound
became a range, one part in 631 to 560).

— Tori, 2026-08-26 10:36 KST
