Paste-ready for `/feedback`. Full evidence: SAFEGUARD_FALSE_POSITIVE_20260825.md

---

Safeguard false positives are blocking adversarial data-integrity auditing.

A Claude Code lane preregisters an astronomy measurement (public DECaLS DR10
data) whose checksum chain must be tamper-evident. The audit protocol requires
attempting to forge the chain in order to prove the detector catches it. That
work has been refused repeatedly.

Anthropic refusals, 2026-08-25 (5 distinct request IDs, a floor not a count —
earlier ones scrolled out):
  req_011CePBSdjwneJaZsb4znygJ
  req_011CePKSRaPGbGufeEgwcBaS
  req_011CePKwoDhNo2Zto92fFhZ5
  req_011CePQj6wmWv6Pu1h36AdTZ   (began a 1h45m dead session)
  req_011CePU2g69Kx8mYGhALna8s

One session hit "Sonnet 5 can't help with this. Start a new session" after a
model switch, so the whole context became unusable and had to be rebuilt.

It is not Anthropic-specific. On 2026-08-26 two other providers refused the same
material ("flagged for possible cybersecurity risk"). On 08-25 one of them
completed the review and the other refused; on 08-26 both refused. Neither is
consistently stricter — refusals are intermittent, so a referee panel becomes a
coin flip.

What was nearly lost: that review gates whether a ~148 GB data acquisition may
start. It survived only because a third reviewer had been dispatched as a
fallback. Its verdict was CLEAR — so the material three engines refused to read
was correct, load-bearing and defensive.

Two things that may help tuning:

1. One refusal fired on a Bash call that ALSO had a shell syntax error, so the
   payload was a garbled command line carrying security vocabulary. That
   combination may look worse than either part alone.

2. A refused turn returns an empty prompt, byte-identical to a finished session.
   Our monitoring reported the seat as "idle" for 1h45m while it was dead. A
   distinguishable signal would prevent a short refusal becoming a long outage.

Not asking for safeguards to be weakened, and not asking how to phrase around
them — we declined to do that even when it cost us a reviewer. The ask is that
adversarial self-auditing of one's OWN data integrity be distinguishable from
offensive security work. The vocabulary is unavoidable (attacker, forge,
regenerated digest), and the users doing it are the ones taking data integrity
most seriously.
