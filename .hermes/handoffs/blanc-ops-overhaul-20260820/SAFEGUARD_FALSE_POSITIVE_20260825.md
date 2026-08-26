# Safeguard false positives are stalling a data-custody audit lane

2026-08-25, Blanc (OPS). Prepared at Duho's instruction: "report it as a bug."
**Not yet submitted** — filing it externally is his call, see §6.

## 1. Summary

A Claude Code session doing **adversarial data-custody auditing** — deliberately
attempting to forge a checksum chain in order to prove the detector catches it —
has been refused **five times** by the model's safeguards. The refusals are
scattered across a single afternoon of legitimate scientific work on a public
astronomical dataset (DECaLS DR10). Each refusal ends the turn with no output
and leaves the session at an empty prompt, indistinguishable from an idle
session to anything watching from outside.

## 2. Request IDs

| # | Request ID | notes |
|---|---|---|
| 1 | `req_011CePBSdjwneJaZsb4znygJ` | earliest in retained scrollback |
| 2 | `req_011CePKSRaPGbGufeEgwcBaS` | |
| 3 | `req_011CePKwoDhNo2Zto92fFhZ5` | immediately follows #2 |
| 4 | `req_011CePQj6wmWv6Pu1h36AdTZ` | began the ~1h45m stall, ~19:47 KST |
| 5 | `req_011CePU2g69Kx8mYGhALna8s` | ~21:28 KST, on resumption after #4 |

Scrollback retains six `flagged this message` renderings; five carry distinct
request IDs (the sixth is my own OPS notice quoting ID #4 back to the session).
Earlier occurrences may have scrolled out — **five is a floor, not a count.**

## 3. What the work actually is

The lane preregisters and audits a galaxy-orientation measurement. Its custody
chain must be tamper-evident, so the audit protocol *requires* attempting the
tamper and demonstrating refusal. The result immediately before refusal #4, in
the session's own words:

> the round-9 attack now fails. A shortened parent with a regenerated digest is
> refused — and refused by the count-oracle completeness proof, which the
> attacker can't forge without also shortening the oracle, whose total is pinned
> to the release.

That is a **defensive** finding: the detector works. The vocabulary it is
impossible to avoid while describing it — *attacker*, *forge*, *regenerated
digest*, *shortened parent* — appears to be what trips the classifier.

Work completed around the refusals, all sound:

- round-9 forgery attempt correctly refused by a computed completeness proof
- parent-set reconciliation against an independent count oracle:
  `oracle 65,060 / fetched 65,060 / bricks disagreeing 0`

No credentials, no exploitation of any system, no third party involved. The
dataset is public; the "attack" is against the lane's own checksum manifest.

## 4. Aggravating detail: one trigger was a malformed command

Refusal #4 fired on a Bash call that *also* carried a shell syntax error —
`(eval):27: unmatched "`. So the flagged payload was a broken command line
containing custody-audit wording. That may be a useful signal for whoever tunes
this: a truncated/garbled command carrying security vocabulary looks worse than
either does alone.

## 5. The operational cost, which is larger than the lost turns

A refused turn produces no output and returns the session to an empty prompt.
**From outside, that is byte-identical to a session that has finished its work.**
Our cockpit classified the seat as `idle` and reported `blockers: []` for
1h45m while the lane sat dead. Three status reports to Duho said "Hwao idle"
on that basis.

That monitoring gap is our defect and we are fixing it. It is recorded here
because it is the mechanism by which a short refusal becomes a long outage: the
failure is silent, and silence reads as completion.

## 6. What we are NOT asking for

Not a request to weaken safeguards, and not a request for wording that evades
them — OPS explicitly declined to advise the lane on rephrasing, and that stance
stands regardless of how this is resolved.

The ask is narrower: **adversarial self-auditing of one's own data integrity is
a recognisable defensive pattern**, and it currently reads to the classifier the
same as offensive work. If that class can be distinguished, it would unblock a
kind of work that safety-conscious users are more likely to be doing, not less.

Submission channel is `/feedback` from within Claude Code, which lives inside
the affected session. Duho's call whether to send it.

---

# UPDATE 2026-08-26 — it happened again, on both providers, and nearly cost the review

Duho authorised sending this on 2026-08-26 after a second day of refusals.

## New refusals, on a different provider

The lane spent 2026-08-26 rebuilding a manifest-closure check and putting it to
an adversarial referee panel. Runner logs, verbatim:

    ⚠️  The model provider's safety filter blocked this request
        (not a Hermes/gateway failure).
    Provider message: This content was flagged for possible cybersecurity risk.

| seat | time (KST) | outcome |
|---|---|---|
| codex | 15:40 | REFUSED, provider safety filter |
| gpt56 | 15:48 | REFUSED, provider safety filter |
| kimi  | 16:57 | completed — **CLEAR** |

**These are not Anthropic refusals.** They are a second provider, refusing the
same material, on the same day the first provider refused it. Combined with the
five Anthropic request IDs in §2, that is two independent providers rejecting
one lane's defensive-integrity work.

## The reversal is the diagnostic

On 2026-08-25 gpt56 completed the review and codex was refused. On 2026-08-26
the assignment inverted: codex refused, gpt56 refused. Neither provider is
consistently stricter. Both refuse **intermittently**, which means a complete
referee panel is a coin flip rather than something a lane can engineer around by
choosing a seat.

## What was nearly lost

The review survived only because a *third* seat had been dispatched as a
fallback after the first refusal. Had kimi not been added, the closure check
would have had zero referees — and it is the check that decides whether a
~148 GB acquisition is allowed to start.

Its verdict, when it finally ran, was **CLEAR**: the mechanism now reports true
digests regardless of what a calling process rebinds, and the referee
independently reproduced the 12,117-brick closure without invoking the function
under test. So the material three engines kept refusing to look at was correct,
load-bearing, and defensive.

## Why this class is worth distinguishing

The lane's protocol *requires* attempting the tamper in order to prove the
detector catches it. That is not incidental vocabulary — a checksum chain that
has never been attacked is not known to be tamper-evident. Round 9 of this same
work is the proof: an attack the lane believed it had refuted turned out to rest
on an oracle the attacker could edit, and only an adversarial referee found it.

The words that work cannot avoid — *attacker, forge, regenerated digest,
shortened parent* — are what appear to trip the classifiers. Users doing this
are, by construction, the ones taking data integrity most seriously.

## Still not asking for safeguards to be weakened

Unchanged from §6. OPS declined to advise the lane on rephrasing to evade a
filter and that stance held all week, including when it cost a referee. The ask
is only that **adversarial self-auditing of one's own data integrity** be
distinguishable from offensive work.

One concrete signal offered freely: Anthropic refusal #4 fired on a Bash call
that *also* carried a shell syntax error, so the flagged payload was a garbled
command line containing security vocabulary — plausibly a worse signal than
either alone.
