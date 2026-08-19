#!/usr/bin/env python3
"""nm_septet_cockpit_feed.py — compute the septet block and merge it into the cockpit canonical.

Duho, 2026-08-06: "add the septet monitor on the cockpit?"

Reads live seat state from nm_paper_run_dashboard's collectors (artifacts + processes), writes a
`septet` block into stable-cockpit-canonical.json, and leaves rendering to the guard's documented
unlock -> publish -> lock -> check cycle. It does NOT write the HTML and it does not touch the
lock; that is the guard's job and the single-writer rule is the point of the guard.

The block is deliberately shaped around one question: is a seat idle while a lane owes work? That
pairing is what nothing surfaced on 2026-08-06, when an amendment sat applied-but-unsubmitted for
eleven hours and blocked a measurement sequence.
"""
import json, os, sys

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/tools")
import nm_paper_run_dashboard as dash

CANON = "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/stable-cockpit-canonical.json"
ROLES = {"Hwao": "coordinates; no content work", "Lana": "science pressure",
         "Goru": "mechanical counts", "Kun": "reproducibility / adversarial gate",
         "Tori": "relay, receipts, queue ledger; drives DR",
         "DR": "external evidence (reference only)", "Yui": "video; nothing unpublished"}


def build():
    rows = dash.collect()
    working, interactive = dash.crew_live()
    busy = {c["seat"]: c for c in working}
    blocked_lanes = [r["lane"] for r in rows if r["state"].startswith("BLOCKED")]
    owed = bool(blocked_lanes)

    seats = []
    for name, role in ROLES.items():
        w = busy.get(name)
        if w:
            state, detail = "WORKING", f"{w['elapsed']} elapsed"
        elif name in ("Hwao",):
            state, detail = "COORDINATING", ""
        else:
            state = "IDLE"
            detail = "a lane owes work" if owed else ""
        seats.append({"name": name, "role": role, "state": state,
                      "detail": detail, "owes": (state == "IDLE" and owed)})

    warning = None
    if owed:
        warning = ("BLOCKED lane with idle seats: " + ", ".join(blocked_lanes) +
                   " — this is the shape of the 2026-08-06 eleven-hour stall.")
    elif interactive:
        warning = ("interactive sessions running that are NOT staffed work: " +
                   ", ".join(f"{c['seat']} pid {c['pid']}" for c in interactive))
    return {"seats": seats, "warning": warning,
            "lanes_blocked": blocked_lanes,
            "interactive_not_staffed": [c["seat"] for c in interactive]}


def main():
    canonical = json.load(open(CANON))
    canonical["septet"] = build()
    if os.stat(CANON).st_flags & 0x00000002 if hasattr(os.stat(CANON), "st_flags") else False:
        print("canonical is uchg-locked — unlock via stable_cockpit_guard.py first")
        return 2
    json.dump(canonical, open(CANON, "w"), indent=1)
    b = canonical["septet"]
    print(f"septet block written: {len(b['seats'])} seats, "
          f"{len(b['lanes_blocked'])} blocked lane(s)")
    print(f"  warning: {b['warning'] or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
