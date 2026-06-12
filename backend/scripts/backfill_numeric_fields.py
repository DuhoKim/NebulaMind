#!/usr/bin/env python3
"""
Backfill wavelength_center_um, z_max, dr_year, data_volume_tb
for all surveys from existing text fields.

Run from backend dir with venv active:
  python3 scripts/backfill_numeric_fields.py
"""

import re
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from sqlalchemy import text


# ---------------------------------------------------------------------------
# Parsers — same logic as SurveyExplorer.tsx (Python port)
# ---------------------------------------------------------------------------

def parse_wavelength_um(wr: str):
    if not wr:
        return None

    def avg(a, b): return (a + b) / 2
    def geomean(a, b): return (a * b) ** 0.5

    # TeV (gamma)
    m = re.search(r'([\d.]+)\s*MeV\s*[–\-]\s*([\d.]+)\s*TeV', wr, re.I)
    if m: return 1.23984e-6 / geomean(float(m.group(1)), float(m.group(2)) * 1e6)
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*TeV', wr, re.I)
    if m: return 1.23984e-12 / geomean(float(m.group(1)), float(m.group(2)))
    m = re.search(r'([\d.]+)\s*TeV', wr, re.I)
    if m: return 1.23984e-12 / float(m.group(1))

    # GeV
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*GeV', wr, re.I)
    if m: return 1.23984e-9 / geomean(float(m.group(1)), float(m.group(2)))
    m = re.search(r'([\d.]+)\s*GeV', wr, re.I)
    if m: return 1.23984e-9 / float(m.group(1))

    # MeV
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*MeV', wr, re.I)
    if m: return 1.23984e-6 / geomean(float(m.group(1)), float(m.group(2)))
    m = re.search(r'([\d.]+)\s*MeV', wr, re.I)
    if m: return 1.23984e-6 / float(m.group(1))

    # keV (X-ray)
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*keV', wr, re.I)
    if m: return 1.23984e-3 / avg(float(m.group(1)), float(m.group(2)))
    m = re.search(r'([\d.]+)\s*keV', wr, re.I)
    if m: return 1.23984e-3 / float(m.group(1))

    # μm
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*μm', wr)
    if m: return avg(float(m.group(1)), float(m.group(2)))
    m = re.search(r'([\d.]+)\s*μm', wr)
    if m: return float(m.group(1))

    # nm → ÷1000
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*nm', wr, re.I)
    if m: return avg(float(m.group(1)), float(m.group(2))) / 1000
    m = re.search(r'([\d.]+)\s*nm', wr, re.I)
    if m: return float(m.group(1)) / 1000

    # mm → ×1000
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*mm', wr, re.I)
    if m: return avg(float(m.group(1)), float(m.group(2))) * 1000
    m = re.search(r'([\d.]+)\s*mm', wr, re.I)
    if m: return float(m.group(1)) * 1000

    # GHz → 3e5 / f
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*GHz', wr, re.I)
    if m: return 3e5 / avg(float(m.group(1)), float(m.group(2)))
    m = re.search(r'([\d.]+)\s*GHz', wr, re.I)
    if m: return 3e5 / float(m.group(1))

    # MHz → 3e8 / f
    m = re.search(r'([\d.]+)\s*[–\-]\s*([\d.]+)\s*MHz', wr, re.I)
    if m: return 3e8 / avg(float(m.group(1)), float(m.group(2)))
    m = re.search(r'([\d.]+)\s*MHz', wr, re.I)
    if m: return 3e8 / float(m.group(1))

    return None


def parse_z_max(rr: str):
    if not rr:
        return None
    z_candidates = []
    # ranges: "z ≈ 0–0.1", "z = 0–5+", "z = 0.01–6.5" — capture the hi end
    for m in re.finditer(r'z\s*[≈=~]\s*[\d.]+\s*[–\-]\s*([\d.]+)\+?', rr):
        z_candidates.append(float(m.group(1)))
    # single values: "z up to X", "z = X", "z ~ X", "z < X"
    for m in re.finditer(r'z\s*(?:up to|=|~|≈|<)\s*([\d.]+)', rr, re.I):
        z_candidates.append(float(m.group(1)))
    if z_candidates:
        return max(z_candidates)
    return None


def parse_dr_year(dr: str):
    if not dr:
        return None
    if re.search(r'no data|not yet|planned|tbd', dr, re.I):
        return None
    m = re.search(r'\b(19|20)\d{2}\b', dr)
    return int(m.group(0)) if m else None


def parse_data_volume_tb(dv: str):
    if not dv:
        return None
    m = re.search(r'~?([\d.]+)\s*EB', dv, re.I)
    if m: return float(m.group(1)) * 1e6
    m = re.search(r'~?([\d.]+)\s*PB', dv, re.I)
    if m: return float(m.group(1)) * 1000
    m = re.search(r'~?([\d.]+)\s*TB', dv, re.I)
    if m: return float(m.group(1))
    m = re.search(r'~?([\d.]+)\s*GB', dv, re.I)
    if m: return float(m.group(1)) / 1000
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    db = SessionLocal()
    try:
        rows = db.execute(text(
            "SELECT id, wavelength_range, redshift_range, "
            "current_data_release, data_volume FROM surveys ORDER BY id"
        )).fetchall()

        counts = {
            "wavelength_center_um": 0,
            "z_max": 0,
            "dr_year": 0,
            "data_volume_tb": 0,
        }
        failed_wavelength = []

        for row in rows:
            sid = row.id
            updates = {}

            wl = parse_wavelength_um(row.wavelength_range or "")
            if wl is not None:
                updates["wavelength_center_um"] = wl
                counts["wavelength_center_um"] += 1
            else:
                failed_wavelength.append(f"id={sid} wr={row.wavelength_range!r}")

            z = parse_z_max(row.redshift_range)
            if z is not None:
                updates["z_max"] = z
                counts["z_max"] += 1

            y = parse_dr_year(row.current_data_release)
            if y is not None:
                updates["dr_year"] = y
                counts["dr_year"] += 1

            tb = parse_data_volume_tb(row.data_volume)
            if tb is not None:
                updates["data_volume_tb"] = tb
                counts["data_volume_tb"] += 1

            if updates:
                set_clause = ", ".join(f"{k} = :{k}" for k in updates)
                updates["sid"] = sid
                db.execute(
                    text(f"UPDATE surveys SET {set_clause} WHERE id = :sid"),
                    updates,
                )

        db.commit()
        total = len(rows)
        print(f"Backfill complete — {total} surveys processed")
        print()
        for field, n in counts.items():
            pct = 100 * n / total
            print(f"  {field:<24} {n:>3}/{total}  ({pct:.0f}%)")
        if failed_wavelength:
            print(f"\nWavelength parse failures ({len(failed_wavelength)}):")
            for f in failed_wavelength:
                print(f"  {f}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
