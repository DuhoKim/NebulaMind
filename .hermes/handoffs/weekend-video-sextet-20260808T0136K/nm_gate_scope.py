#!/usr/bin/env python3
"""Write a gate-scope sidecar so a spoken claim resolves to SPECIFIC gates.

    nm_gate_scope.py <reading-stem> <phase-label> <gate-file> [gate-file ...]

Why a sidecar and not a deck field: nm_deck_build.py rebuilds the payload from a
fixed key set, so an extra top-level key in an authored deck is dropped. The
sidecar sits beside the audio as <stem>.gates.json, which the claim check can find
deterministically from the reading's own name.

HONESTY RULE, taken from Blanc's reconcile design: a sidecar written at render
time records what the speaker meant. A sidecar written LATER is a reconstruction,
and is marked `reconstructed: true` with a reason. The claim check reports those
as TRUE(reconstructed), never plain TRUE — because backdating a claim about what
was meant is a new assertion, not a repair.
"""
import json, sys, pathlib, subprocess, datetime as dt

AUDIO = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio")
LANE = pathlib.Path(__file__).resolve().parent


def main(argv):
    if len(argv) < 4:
        sys.exit(__doc__)
    stem, phase, gates = argv[1], argv[2], argv[3:]
    mp3 = AUDIO / f"{stem}.mp3"
    if not mp3.exists():
        sys.exit(f"no audio for stem {stem}")

    resolved = []
    for g in gates:
        p = (LANE / g) if not pathlib.Path(g).is_absolute() else pathlib.Path(g)
        if not p.exists():
            sys.exit(f"gate file not found: {g}")
        token = p.open(errors="replace").readline().strip().split()[0]
        resolved.append({"file": p.relative_to(LANE).as_posix(), "token": token,
                         "passing": token.upper().startswith("PASS")})

    # rendered-now vs backfilled: compare audio mtime to now
    age_s = dt.datetime.now().timestamp() - mp3.stat().st_mtime
    reconstructed = age_s > 900          # >15 min after the audio = not authored with it
    doc = {"marker": "NM_GATE_SCOPE_V1", "stem": stem, "phase": phase,
           "gates": resolved,
           "n_gates": len(resolved),
           "n_passing": sum(1 for g in resolved if g["passing"]),
           "reconstructed": reconstructed}
    if reconstructed:
        doc["reconstructed_why"] = (
            f"written {int(age_s//60)} min after the audio; records what the claim referred to, "
            "not what was declared at render time")
    out = AUDIO / f"{stem}.gates.json"
    out.write_text(json.dumps(doc, indent=1) + "\n")
    print(f"  {out.name}: {doc['n_passing']}/{doc['n_gates']} passing, phase={phase}"
          f"{' [RECONSTRUCTED]' if reconstructed else ''}")


if __name__ == "__main__":
    main(sys.argv)
