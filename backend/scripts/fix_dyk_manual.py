#!/usr/bin/env python3
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.page import WikiPage

MANUAL = {
    "milky-way": [
        "The Milky Way rotates at roughly 828,000 km/h at the Sun's location, yet takes ~225 Myr to complete one orbit around the galactic center.",
        "Sagittarius A*, the Milky Way's central black hole, has a mass of ~4.1×10⁶ M☉ and fits within an orbit smaller than our solar system.",
        "The Milky Way's stellar disk spans ~100,000 light-years, but its dark matter halo extends out to ~300,000 light-years.",
    ],
    "neutron-stars": [
        "A neutron star packs 1.4 solar masses into a sphere ~20 km across, giving it an average density of ~10¹⁴ g/cm³ — comparable to an atomic nucleus.",
        "The fastest-spinning pulsar, PSR J1748-2446ad, rotates 716 times per second, with its equator moving at ~24% of the speed of light.",
        "Neutron stars have surface gravity ~2×10¹¹ times Earth's — a 70 kg person would weigh roughly 1.4×10¹³ kg on the surface.",
    ],
    "quasars": [
        "The most luminous quasar, J0529-4351, outshines 500 trillion suns and is powered by a black hole accreting ~370 M☉ per year.",
        "Quasars were first identified in 1963 by Maarten Schmidt, who found 3C 273 was redshifted by z=0.158, placing it 2.4 Gly away.",
        "Some quasars vary in brightness over just a few days, implying their energy-producing region is smaller than our solar system.",
    ],
    "supernovae": [
        "A Type Ia supernova releases ~1–2×10⁴⁴ joules of energy in seconds — more than the Sun will emit across its entire ~10 Gyr lifetime.",
        "SN 1987A, just 168,000 light-years away, was visible to the naked eye and confirmed neutrino bursts from a collapsing stellar core.",
        "Each supernova seeds ~0.1–1 M☉ of newly synthesized heavy elements into surrounding space, making supernovae the primary source of elements heavier than iron.",
    ],
}

db = SessionLocal()
for slug, facts in MANUAL.items():
    page = db.query(WikiPage).filter(WikiPage.slug == slug).first()
    if page:
        page.did_you_know = json.dumps(facts)
        print(f"FIXED {slug}: {facts[0][:80]}")
db.commit()
db.close()
print("Done")
