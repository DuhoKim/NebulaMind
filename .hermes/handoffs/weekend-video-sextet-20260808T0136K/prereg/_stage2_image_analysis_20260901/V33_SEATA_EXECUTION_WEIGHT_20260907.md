# SEAT A (V33) — EXECUTION-WEIGHT OBSERVATIONS (draft for the outcome; not a finding against the seat)

Exit artefacts, read BEFORE the report counted (disappearance is not completion):
- stderr 0 bytes (no 'timeout waiting for response'); stdout 5638 bytes; wrapper rc=0, ACCESS PROVEN for f294cb55…; wrapper 17482 exited between 08:27:02 and 08:28:07 KST. This is a NORMALLY COMPLETED seat.
- report sha256 9640093ca7dce9d155505d4e15f9ceca69ab4de1ae45aae7a1fa8426bf4451f1, 4,432 bytes, written 08:18:02 KST. VERDICT: SIGNABLE-AS-PRECOMMITMENT.

Grounding check (read-only, against the pinned candidate): every specific the report names is genuinely in the text — the limit labels L-OFF / L-COV / L-RCPT / L-INH / L-AVAIL, the 7.8 GB and 26 GB figures, rederive_seed's offline default. Nothing in the report is fabricated.

TIMING, which bounds what the report can be evidence OF: dispatch 08:11:31 → report written 08:18:02 = 6 min 31 s. The 32-suite aggregate takes ~15 min under the pinned interpreter (RUN2: 07:40:34 → 07:55:29), of which the 116 controls alone are ~5 min 55 s and the driver suite ~2 min 7 s. Seat A therefore CANNOT have executed the full package before writing, and its §9 is hedged accordingly ('run successfully WHEN the complete sandbox environment ... is supplied'). Its own §4/§5 read the tests rather than reporting their execution.
CONSEQUENCE for the outcome: seat A is a completed seat and its verdict counts as one, but it is a READING-LEVEL review; no execution claim of the package rests on it. The executed evidence is the lane's own retained logs and gate v3.1 over RUN2, and whatever seat B (still running, wrapper 22010, ~16 min elapsed) executes.
