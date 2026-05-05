#!/usr/bin/env python3
"""Patch specific pages that lost hero_facts to < 3 items."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage

PATCHES = {
    "galaxy-clusters": [
        {"label": "Mass Range", "value": "10¹⁴–10¹⁶", "unit": "M☉", "kind": "range", "value_min": 1e14, "value_max": 1e16, "scale": "log"},
        {"label": "Galaxy Count", "value": "10²–10³", "unit": "galaxies", "kind": "range", "value_min": 100, "value_max": 1000, "scale": "log"},
        {"label": "X-ray Temperature", "value": "10⁷–10⁸", "unit": "K", "kind": "range", "value_min": 1e7, "value_max": 1e8, "scale": "log"},
    ],
    "milky-way": [
        {"label": "Diameter", "value": "100,000", "unit": "light-years", "kind": "scalar"},
        {"label": "Age", "value": "~13.6", "unit": "Gyr", "kind": "scalar"},
        {"label": "Star Count", "value": "10¹¹–4×10¹¹", "unit": "stars", "kind": "range", "value_min": 1e11, "value_max": 4e11, "scale": "log"},
    ],
    "neutron-stars": [
        {"label": "Density", "value": "10¹⁴–10¹⁷", "unit": "kg/m³", "kind": "range", "value_min": 1e14, "value_max": 1e17, "scale": "log"},
        {"label": "Mass Range", "value": "1.1–2.3", "unit": "M☉", "kind": "range", "value_min": 1.1, "value_max": 2.3, "scale": "linear"},
        {"label": "Surface Gravity", "value": "~2×10¹¹", "unit": "g⊕", "kind": "scalar"},
    ],
    "quasars": [
        {"label": "First Detection", "value": "1963", "unit": "year", "kind": "date", "year": 1963},
        {"label": "Luminosity Range", "value": "10³⁷–10⁴¹", "unit": "W", "kind": "range", "value_min": 1e37, "value_max": 1e41, "scale": "log"},
        {"label": "Redshift Record", "value": "7.64", "unit": "z", "kind": "scalar"},
    ],
    "tidal-forces": [
        {"label": "Moon-Earth Distance", "value": "384,400", "unit": "km", "kind": "scalar"},
        {"label": "Roche Limit Factor", "value": "~2.44", "unit": "planetary radii", "kind": "scalar"},
        {"label": "Tidal Locking Period", "value": "~27.3", "unit": "days (Moon)", "kind": "scalar"},
    ],
}

db = SessionLocal()
for slug, facts in PATCHES.items():
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if page:
        page.hero_facts = json.dumps(facts)
        print(f"PATCHED {slug}: {len(facts)} facts")
db.commit()
db.close()
print("Done")
