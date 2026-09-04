# R3-C2 — what is in the seat packet, and why each part must be there

**Tori, 2026-09-04 22:10 KST, on Blanc's instruction (22:02), item 2.** kimi V4 finding 6 and codex V4 finding 5.
**No tier, token, standing or stamp moves. Paper HOLD.**

## 1. The leak that was there

C4 claimed pattern blindness while the packet handed the seat **the whole preregistration**, and that document
says in §0 that the lane holds a **shape/magnitude pattern it wrote itself**, that the census may **support, weaken
or break** it, and that **ΛCDM** is the comparison. §10 narrated every gate objection. A seat reading that knows
what the interesting answer looks like before it opens a source.

kimi put it exactly: *the blind denies the pattern's content and the interpretation mapping, not knowledge of its
existence and topic — and as written the packet itself supplies both.*

## 2. What the seat packet now contains, and why each part is necessary

Built by `r3c2_build_seat_packet.py`. Sections **1, 2, 3, 4, 5, 6, 9, 11** survive, minus marked spans.

| kept | why a seat cannot do the work without it |
|---|---|
| **§1 the question + the operational definition of a quantitative claim** | the seat enumerates candidates; without the inclusion/exclusion definition the denominator becomes taste, which is the defect the whole redesign exists to remove |
| **§2 the per-claim method** | the order of operations *is* the task |
| **§3 outcome classes + precedence** | the seat must file exactly one declared outcome; a class it cannot see is a class it cannot file, which recreates the escape hatch |
| **§4 study-level outcomes** | the seat must know which conditions stop the study rather than being decided by it |
| **§5 controls** | each control names a code the seat must print; a control the seat cannot read cannot pass |
| **§6 limb structure** | limb A is enumeration only, and the seat must know not to start arithmetic |
| **§9 inherited discipline** | harness pinning, path lists, the 120-second cap, ACCESS_SHA — all executed by the seat |
| **§11 scope** | states that nothing outward moves; keeps a seat from acting beyond the run |

## 3. What is removed, and what each removal denies the seat

| removed | what it disclosed |
|---|---|
| **§0 whole** | the pattern's topic, its lane authorship, the ΛCDM comparison, and that the tally may break it |
| **§7 whole** | that a sealed comparison against a hypothesis follows the tally |
| **§8 whole** | the ΛCDM discrimination question by name |
| **§10 whole** | nine gate rounds of objections — i.e. every criticism the design has already absorbed, and the pattern behind them |
| **the HELD marker in §3** | that the admissibility rule is disputed and under a ruling; a seat that knows a rule is contested has a reason to read it loosely |
| **the worked example in §3** | it names a corpus entry, its value, and says outright what the census "exists to detect" |
| **§4's "no outcome is a verdict about the pattern"** | that a pattern exists to be a verdict about |
| **C4's rationale** | that a pattern record exists and is being withheld from the reader |
| **three gate-history parentheticals** | which referee found what, and therefore what referees think matters here |
| **the custodian's name in C6** | the custody chain outside the lane |

## 4. Why this is a control and not a promise

The builder does not merely delete. After building, it **asserts that no string on a forbidden list survives
anywhere in the output**, and **exits non-zero without writing the packet** if any does.

**The first run failed on fourteen surviving disclosures** in a packet that had been assembled by hand and would
have gone to a seat — including the orphaned version-table rows, which had been appended below §11 and so escaped
the section drop entirely. That is the case for asserting the redaction rather than reviewing it: the hand-built
packet looked right.

`C4_PACKET_REDACTED=PASS` is therefore an artefact of a script that refuses to produce a leaky packet, not a
declaration by whoever built it.

## 5. What it still does not prove — stated, not implied

- **It does not prove the seat has no prior exposure** from training or an earlier session. Nothing here can, and
  C4 says so in the master rather than implying a stronger blind.
- **It does not restrict reads.** The wrapper's `--add-dir` grants directories; it cannot deny them. Running the
  seat from a directory that contains only the packet is enforceable; a seat that constructs an absolute path to
  the lane anyway is caught, if at all, by the printed path list, which is self-report. **codex's V4 finding 5 —
  that C4 is not mechanical unless the filesystem denies the lane path — is not fully closed**, and is recorded
  here as open rather than argued away.
- **It does not hide that redaction happened.** The packet header says so plainly and tells the seat not to
  reconstruct what is missing. Concealing the redaction would be a worse blind: a seat that notices gaps and
  guesses at them is more dangerous than one told the gaps are deliberate.
