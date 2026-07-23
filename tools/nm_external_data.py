#!/usr/bin/env python3
"""nm_external_data.py — robust external-data-pull capability for the Lab.

Reaches data beyond the existing SDSS-single-table / TNG-integrated envelope that
lab_runner_worker is limited to. That envelope is exactly the z~0 low-hanging fruit
that keeps getting rejected; the genuinely novel frontiers (Gaia DR3 kinematics,
APOGEE value-added distances / galactocentric radius, JWST/COSMOS census catalogs,
r-process abundance compilations) live in VizieR or need resilient fetching.

Two sources:
  • VizieR (CDS) via raw-HTTP TAP/ADQL — the primary unlock. Works reliably where the
    SkyServer value-added-catalog queries (e.g. astroNN) return 503 / time out.
  • SkyServer (SDSS DR18) wrapped with retry+backoff+cache — the existing single-table
    pulls flake intermittently (503/read-timeout); this makes them survivable.

Every fetch returns a list-of-dict rows (CSV parsed) and is disk-cached by query hash
(set NM_EXT_CACHE to relocate; delete the dir to force refresh). Helpers convert rows
to numpy arrays and do IN-PROCESS id joins — the coordinate joins on SkyServer time
out, so pull each table separately and join here on a shared string key.

Usage:
    from nm_external_data import vizier_tap, skyserver_sql, to_arrays, id_join
    gaia = vizier_tap('SELECT TOP 100 Source, Plx, pmRA, pmDE FROM "I/355/gaiadr3"')
    # APOGEE distances (galactocentric radius) — the axis SkyServer couldn't reach:
    # sh = vizier_tap('SELECT APOGEE_ID, GALR FROM "<starhorse-catalog-id>" WHERE ...')

CLI smoke test:  python3 tools/nm_external_data.py
"""
from __future__ import annotations
import csv
import hashlib
import os
import time
import warnings

import requests

warnings.filterwarnings("ignore")

VIZIER_TAP = os.environ.get("NM_VIZIER_TAP", "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync")
SKYSERVER = os.environ.get("NM_SKYSERVER", "https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch")
CACHE_DIR = os.environ.get("NM_EXT_CACHE", os.path.expanduser("~/.cache/nm_external"))


def _key(*parts) -> str:
    return hashlib.sha256("||".join(map(str, parts)).encode()).hexdigest()[:20]


def _cache_read(key):
    p = os.path.join(CACHE_DIR, key + ".csv")
    if os.path.exists(p):
        with open(p) as f:
            return f.read()
    return None


def _cache_write(key, text):
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(os.path.join(CACHE_DIR, key + ".csv"), "w") as f:
        f.write(text)


def _parse_csv(text, comment="#"):
    # SkyServer prepends a '#Table1' line; VizieR CSV is clean. Strip comment/blank lines.
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.startswith(comment)]
    if not lines:
        return []
    return [dict(r) for r in csv.DictReader(lines)]


def _resilient(method, url, *, params=None, data=None, timeout=90, retries=4,
               backoff=3.0, retry_on=(500, 502, 503, 504)):
    """One HTTP call with retry+backoff on transient 5xx / timeouts / conn errors."""
    last = None
    for i in range(retries):
        try:
            r = requests.request(method, url, params=params, data=data, timeout=timeout)
            if r.status_code in retry_on:
                last = f"http {r.status_code}"
                time.sleep(backoff * (i + 1))
                continue
            r.raise_for_status()
            return r.text
        except requests.exceptions.RequestException as e:
            last = type(e).__name__
            time.sleep(backoff * (i + 1))
    raise RuntimeError(f"request failed after {retries} tries ({url.split('/')[2]}): {last}")


def vizier_tap(adql, *, timeout=120, retries=4, cache=True):
    """Query VizieR via raw-HTTP TAP (ADQL). Returns list-of-dict rows.

    Catalog ids are VizieR table names in double quotes, e.g. "I/355/gaiadr3".
    """
    key = _key("viz", adql)
    if cache and (c := _cache_read(key)) is not None:
        return _parse_csv(c)
    text = _resilient(
        "POST", VIZIER_TAP,
        data={"request": "doQuery", "lang": "ADQL", "format": "csv", "query": adql},
        timeout=timeout, retries=retries,
    )
    if cache:
        _cache_write(key, text)
    return _parse_csv(text)


def skyserver_sql(sql, *, timeout=90, retries=5, cache=True):
    """Query SDSS DR18 SkyServer resiliently (retry on the intermittent 503/timeouts)."""
    key = _key("sdss", sql)
    if cache and (c := _cache_read(key)) is not None:
        return _parse_csv(c)
    text = _resilient("GET", SKYSERVER, params={"cmd": sql, "format": "csv"},
                      timeout=timeout, retries=retries)
    if cache:
        _cache_write(key, text)
    return _parse_csv(text)


def vizier_query(catalog, columns=None, *, row_limit=50000, constraints=None, table=None):
    """Pull a VizieR catalog via astroquery — robust table-name resolution (raw TAP
    needs the exact table id, which is hard to guess; this resolves by catalog id).

    catalog     VizieR catalog id, e.g. 'J/A+A/673/A155' (APOGEE DR17 StarHorse) or
                'I/355/gaiadr3'.
    columns     list of columns, or None for the catalog default; ['**'] for all.
    constraints astroquery column_filters, e.g. {'Dist50': '<15', 'logg50': '<3.5'}.
    table       when a catalog has several tables, pick the one whose name contains
                this substring (e.g. 'apogee17').
    Returns list-of-dict rows with string values (masked cells -> None), matching the
    TAP path so downstream helpers (to_arrays / id_join) work identically.
    """
    from astroquery.vizier import Vizier
    v = Vizier(columns=columns or ["**"], row_limit=row_limit, column_filters=constraints or {})
    res = v.get_catalogs(catalog)
    if len(res) == 0:
        return []
    t = res[0]
    if table is not None:
        for cand in res:
            if table in (cand.meta.get("name") or ""):
                t = cand
                break
    out = []
    for i in range(len(t)):
        row = {}
        for c in t.colnames:
            val = t[c][i]
            row[c] = None if (val is None or str(val) in ("--", "")) else str(val)
        out.append(row)
    return out


def to_arrays(rows, cols, dtype=float):
    """Columns of dict-rows -> {col: np.array}. Non-parseable cells become NaN (float)."""
    import numpy as np
    out = {}
    for c in cols:
        vals = []
        for r in rows:
            v = r.get(c, "")
            try:
                vals.append(dtype(v))
            except (ValueError, TypeError):
                vals.append(np.nan if dtype is float else None)
        out[c] = np.array(vals)
    return out


def id_join(a_rows, b_rows, key, bcols=None):
    """In-process inner join of two row-lists on a shared string key (SkyServer joins
    time out, so pull tables separately and join here). b's columns fill without
    overwriting a's; restrict b to `bcols` if given."""
    idx = {r[key]: r for r in b_rows if r.get(key)}
    out = []
    for r in a_rows:
        b = idx.get(r.get(key))
        if b is None:
            continue
        merged = dict(r)
        for k, v in b.items():
            if bcols is None or k in bcols:
                merged.setdefault(k, v)
        out.append(merged)
    return out


if __name__ == "__main__":
    print("nm_external_data smoke test")
    g = vizier_tap('SELECT TOP 5 Source, RA_ICRS, DE_ICRS, Plx FROM "I/355/gaiadr3"', cache=False)
    print(f"  VizieR Gaia DR3: {len(g)} rows; sample={g[0] if g else None}")
    a = to_arrays(g, ["Plx"])
    print(f"  to_arrays Plx: {a['Plx']}")
