#!/usr/bin/env python3
"""Weekly watch for new neutron-star mass measurements bearing on the BHU live falsifier, entry 31
(Smolin 2004, cosmological natural selection): NO securely measured neutron star above 2.5 Msun.

STEP 2 of Duho's "a -> b -> c" order (2026-09-02). Criteria were pre-registered BEFORE this code in
bhu-acquisition-20260828/NS_MASS_WATCH_PREREG_20260902.md and are restated here so the human reader
tests the right thing:

  FIRE_CANDIDATE  a PEER-REVIEWED mass M +/- sigma with (M - 2.5)/sigma >= 3 from a resolved
                  neutron-star identity (pulsar timing, optical light curve; NOT a gravitational-wave
                  secondary of unresolved nature)  -> two-seat gate + packet to Duho; standing changes
                  only on his stamp.
  RE_GATE         (M - 2.5)/sigma >= 2 in any source; or any peer-reviewed central M > 2.5 at >= 1 sigma;
                  or a GW secondary with resolved NS identity above 2.5  -> human reads, two-seat gate
                  decides whether the ledger changes.
  HINT            posterior P(M > 2.5) >= 5% without RE_GATE  -> log only.
  CLEAR           anything else, including tighter errors on known stars below the bar.

The battery twin already exists: b68_entry31_massbar_tripwire.py recomputes the standing from
entry31_massbar_ledger.json on every battery run and FAILS when a SECURE central mass reaches the bar.
This watch is the human-facing twin (modelled on nm_desi_curvature_watch.py): it finds candidate papers
and flags them; it NEVER interprets a result, never edits the ledger, never changes a standing.

State: seen-ids in ns_mass_watch_state.json beside this script. On new hits: appends rows to
NS_MASS_WATCH_HITS.md and one event to the autopilot feed. Silent when nothing is new (cron etiquette),
but always stamps last_run so a dead watch is detectable. `--seed` marks the current listing as seen
without reporting it (first-run hygiene; the curvature watch's first run dumped 25 stale hits).
Absolute lane paths (register 1av): the cron copy runs from ~/.hermes/scripts/.
"""
import json, re, sys, time, urllib.request, urllib.parse, pathlib

LANE = pathlib.Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K")
STATE = LANE / "ns_mass_watch_state.json"
HITS = LANE / "NS_MASS_WATCH_HITS.md"
FEED = LANE.parent / "galaxy-evolution/mastermind/autopilot-events.jsonl"
BAR = 2.5
Q = ('(abs:"neutron star" OR abs:"pulsar") AND '
     '(abs:"Shapiro delay" OR abs:"most massive" OR abs:"maximum mass" OR abs:"mass measurement" OR '
     'abs:"black widow" OR abs:"redback" OR abs:"mass gap" OR abs:"heaviest")')
CRITERIA = (f"Criteria (prereg 2026-09-02): FIRE_CANDIDATE = peer-reviewed resolved-identity NS with "
            f"(M-{BAR})/sigma >= 3; RE_GATE = (M-{BAR})/sigma >= 2, or peer-reviewed central M > {BAR} at >= 1 sigma, "
            f"or a GW secondary with resolved NS identity above {BAR}; HINT = P(M>{BAR}) >= 5%; else CLEAR. "
            "GW secondaries of unresolved nature do NOT test the bar. A human reads; the ledger changes only "
            "after a two-seat gate; FIRED/LIVE is Duho's stamp.")

def main():
    seed = "--seed" in sys.argv
    state = json.loads(STATE.read_text()) if STATE.exists() else {"seen": []}
    seen = set(state["seen"])
    url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(Q) +
           "&sortBy=submittedDate&sortOrder=descending&max_results=25")
    t = None; err = None
    for attempt in range(3):
        try:
            t = urllib.request.urlopen(urllib.request.Request(
                url, headers={"User-Agent": "NebulaMind-ns-mass-watch/1.0 (mailto:duhokim81@gmail.com)"}),
                timeout=60).read().decode("utf-8", "replace")
            break
        except Exception as e:
            err = e; time.sleep(40 * (attempt + 1))
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if t is None:
        state.update({"last_run": now, "last_error": str(err)[:120]})
        STATE.write_text(json.dumps(state, indent=1)); sys.exit(0)
    new = []
    for e in re.findall(r"<entry>(.*?)</entry>", t, re.S):
        aid = re.sub(r"v\d+$", "", ((re.search(r"<id>(.*?)</id>", e) or [None, ""])[1]).split("/abs/")[-1])
        if not aid or aid in seen:
            continue
        ti = re.sub(r"\s+", " ", (re.search(r"<title>(.*?)</title>", e, re.S) or [None, ""])[1]).strip()
        pub = (re.search(r"<published>(.*?)</published>", e) or [None, ""])[1][:10]
        new.append((aid, pub, ti)); seen.add(aid)
    if new and not seed:
        with HITS.open("a") as fh:
            for aid, pub, ti in new:
                fh.write(f"- {now} · arXiv:{aid} ({pub}) — {ti}\n")
        with FEED.open("a") as fh:
            fh.write(json.dumps({"ts": now, "lane": "bhu", "actor": "tori", "event": "ns_mass_candidate",
                "detail": (f"NS mass watch: {len(new)} new neutron-star mass paper(s) — a HUMAN must read them "
                           f"against entry 31's {BAR} Msun bar. " + CRITERIA + " ") + "; ".join(
                           f"arXiv:{a} {ti[:70]}" for a, _, ti in new[:3])}, ensure_ascii=False) + "\n")
    state.update({"seen": sorted(seen), "last_run": now, "last_error": None,
                  "last_new": 0 if seed else len(new), "seeded": seed or state.get("seeded", False)})
    STATE.write_text(json.dumps(state, indent=1))
    if seed:
        print(f"seeded {len(new)} id(s) as seen; nothing reported"); return
    if new:
        print(f"BHU NS mass watch: {len(new)} new neutron-star mass paper(s) — read against entry 31's {BAR} Msun bar.")
        print("  " + CRITERIA)
        for aid, pub, ti in new[:5]:
            print(f"  arXiv:{aid} ({pub}) {ti[:80]}")

if __name__ == "__main__":
    main()
