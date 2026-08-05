#!/usr/bin/env python3
"""nm_data_survey.py — what data actually EXISTS for a paper project, before any modelling.

Duho, 2026-08-05: "you should survey the data for each paper project and actually study it".
Every study so far started from published anchors and computed over them; Kun's verdict on the
f_esc sweep names the failure exactly — "a well-measured number about a model of the
literature, not about the sky". This tool inverts the order: for a named physical quantity, it
enumerates what the public archives hold, so a project starts from a data inventory instead of
a literature equation.

Method (generalised from the Shape-1 census, which found 92 of 112 eligible catalogs reachable
ONLY by UCD): two enumeration channels over VizieR's TAP_SCHEMA —
  1. UCD channel: semantic column tags (phys.magAbs, phys.abund.Z, src.redshift, ...), which
     survive arbitrary column naming.
  2. Name channel, case-complete: LIKE is case-sensitive in this service, so each pattern is
     issued in three cases.
Metadata only. No science rows are fetched, nothing is computed, no verdicts are issued — the
output is an availability inventory for a human to choose from.

Output: .hermes/data-surveys/<quantity>.json  (+ a combined index when run with --all)
"""
import json, os, re, sys, time

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/tools")
import nm_external_data as ext

OUT_DIR = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/data-surveys"
os.makedirs(OUT_DIR, exist_ok=True)


def log(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def unq(s):
    return str(s or "").strip().strip('"').strip("'").strip()


# Each entry: the physical quantity a paper project needs, and how to find it in an archive.
QUANTITIES = {
    "uv_luminosity": {
        "why": "bright-end UV LF / cosmic SFRD — Shape-1 gap paper, frontier 41",
        "ucds": ["phys.magAbs", "phys.luminosity.fun"],
        "names": ["MUV", "M1500", "M_UV", "1500Mag"],
    },
    "gas_metallicity": {
        "why": "mass-metallicity relation — anchor-gap census, z7 MZR, z9-10 (rejected)",
        "ucds": ["phys.abund.Z", "phys.abund"],
        "names": ["logOH", "12+log", "OH", "Z_gas"],
    },
    "lyman_continuum": {
        "why": "escape fraction / ionizing budget — reionization papers, frontier 16",
        "ucds": ["phot.flux;em.UV", "phys.absorption"],
        "names": ["fesc", "f_esc", "LyC", "xi_ion", "xion"],
    },
    "stellar_mass": {
        "why": "the mass axis every scaling relation needs",
        "ucds": ["phys.mass"],
        "names": ["logM", "Mstar", "M_star", "logMs"],
    },
    "star_formation": {
        "why": "main sequence, SFRD, quenching",
        "ucds": ["phys.SFR"],
        "names": ["SFR", "logSFR", "sSFR"],
    },
    "redshift_spec": {
        "why": "the axis that makes any of the above an evolution measurement",
        "ucds": ["src.redshift"],
        "names": ["zspec", "zsp", "z_spec"],
    },
}


def tables_by_ucd(ucd):
    q = ("SELECT DISTINCT table_name FROM TAP_SCHEMA.columns "
         f"WHERE ucd LIKE '%{ucd}%'")
    try:
        return {unq(r.get("table_name")) for r in ext.vizier_tap(q)}
    except Exception as e:
        log(f"  ucd {ucd}: FAILED {str(e)[:60]}")
        return set()


def tables_by_name(pat):
    found = set()
    for variant in (pat, pat.lower(), pat.upper()):  # LIKE is case-sensitive here
        q = ("SELECT DISTINCT table_name FROM TAP_SCHEMA.columns "
             f"WHERE column_name LIKE '%{variant}%'")
        try:
            found |= {unq(r.get("table_name")) for r in ext.vizier_tap(q)}
        except Exception as e:
            log(f"  name {variant}: FAILED {str(e)[:60]}")
    return found


def survey(key, spec):
    log(f"=== {key}: {spec['why']}")
    by_ucd, by_name = set(), set()
    per_ucd, per_name = {}, {}
    for u in spec["ucds"]:
        s = tables_by_ucd(u)
        per_ucd[u] = len(s)
        by_ucd |= s
        log(f"  ucd {u}: {len(s)} tables")
    for n in spec["names"]:
        s = tables_by_name(n)
        per_name[n] = len(s)
        by_name |= s
        log(f"  name {n}: {len(s)} tables")
    only_ucd = by_ucd - by_name
    return {
        "quantity": key, "why": spec["why"],
        "tables_total": len(by_ucd | by_name),
        "tables_by_ucd": len(by_ucd), "tables_by_name": len(by_name),
        "tables_reachable_only_by_ucd": len(only_ucd),
        "per_ucd": per_ucd, "per_name": per_name,
        # a sample only — the point is the count, not a curated list
        "sample_ucd_only": sorted(only_ucd)[:25],
        "surveyed_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "method": "VizieR TAP_SCHEMA metadata only; no science rows fetched; no verdicts",
    }


def main():
    keys = sys.argv[1:] or list(QUANTITIES)
    keys = [k for k in keys if k in QUANTITIES]
    index = {}
    for k in keys:
        res = survey(k, QUANTITIES[k])
        json.dump(res, open(os.path.join(OUT_DIR, f"{k}.json"), "w"), indent=1)
        index[k] = {m: res[m] for m in ("why", "tables_total", "tables_by_ucd",
                                        "tables_by_name", "tables_reachable_only_by_ucd")}
        log(f"  -> {res['tables_total']} tables ({res['tables_reachable_only_by_ucd']} UCD-only)")
    json.dump({"surveyed_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "quantities": index},
              open(os.path.join(OUT_DIR, "INDEX.json"), "w"), indent=1)
    log("index written")


if __name__ == "__main__":
    main()
