# DIAGNOSIS — C3's invocation has failed three repairs in the same direction. STOPPED under the third-failure rule.

**Tori, 2026-09-05 10:12 KST. Filed, not repaired. No V25 for this defect. Duho reads this before anything else happens
to C3.**
**No tier, token, standing or stamp moves. R3D does not RUN.**

## The rule, and why it fires here

*"If the same defect survives three repairs in the same direction, stop, file a diagnosis, and wait. Three
locally-correct repairs that fail the same way are evidence about the design, not a reason for a fourth."*

**The defect: a conforming seat cannot execute C3's printed invocation.** Its history, same direction throughout:

| version | what the clause said | what a seat gets | found by |
|---|---|---|---|
| V21 | `python3 r3d_c3_deletion_probe.py <relations.json>` | angle brackets are shell redirection; no filename argument | codex |
| V22 — repair 1 | brackets removed; bare filename | relative to the lane dir; unresolvable from anywhere else | codex |
| V23 — repair 2 | path added, as `python3 <that absolute path> relations.json` | **brackets reintroduced** while fixing the path | codex + kimi |
| V24 — repair 3 | repo-root-relative literal path | unresolvable from a seat's own working directory | codex |

**Three repairs. The defect survives. The counter does not reset because each version's fault had a different
surface** — that is exactly the reading Blanc enforced on the partition boundary, and it applies to me here.

## Why three locally-correct repairs failed the same way

**The document is trying to specify an executable path for a working directory it does not control and cannot
know.** Each repair chose a *base* for the path — the lane directory, the repository root — and each time the
referee correctly observed that a seat's actual working directory is neither. **The same clause also tells the seat
to write `relations.json` "in its own working directory"** — so the document itself acknowledges the seat's cwd is
the seat's, then prints a path that assumes it is somewhere else.

**That is not a wording problem. It is a category error: a path is a fact about the executing environment, and the
preregistration has been asserting it as a fact about the design.** No fourth path base fixes that. An absolute
path (codex's V24 replacement) would work on this machine and fail on any other — and R3D's seats have already run
in environments where script execution was unavailable at all.

## The honest options, with costs — for Duho, not chosen here

1. **Locate the probe by DIGEST, not by path.** C3 already pins `7db66931…`. Instruct the seat: *find the file
   whose sha256 is that digest; the dispatcher places it in your working directory before you start.* The
   preregistration then asserts what it can actually guarantee — identity — and leaves location to the dispatcher,
   which is the party that knows it. **Cost:** the dispatcher gains one step; the clause loses its literal command.
2. **Absolute path**, as codex proposed. **Cost:** the document becomes machine-specific, and a seat on another host
   — or one with execution disabled — fails a control for reasons that have nothing to do with the physics.
3. **Move C3 out of the seat's hands entirely**: Tori runs the probe on the seat's filed relations and prints the
   captured output into the record. **Cost:** the seat no longer executes its own deletion probe, which weakens
   the "harness must execute the deleted state" requirement that a gate imposed at R3D's very first round.

**My recommendation is 1**, because it fixes the category error rather than guessing a fourth base — but **it changes
what C3 requires of the dispatcher, and that is a design change I am not making after three failed attempts on
this clause without a ruling.**

## What this does and does not affect

**Everything else in V24 stands.** Both engines have called the partition, circularity, the falsifier, the re-run
guard and stall SOUND, repeatedly. **The one clause that has resisted repair is the one that tells a seat how to
find a file** — and the fact that it resisted is the finding.

**R3D is NOT frozen and NOT run. C3 is STOPPED pending a ruling. V24 stands at `4c8d0d32…` as the last version.**
