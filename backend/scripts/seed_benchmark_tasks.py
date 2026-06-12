#!/usr/bin/env python3
"""Seed benchmark_tasks from high-quality wiki claims."""
import sys, os, hashlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.benchmark import BenchmarkTask

# 20 hand-crafted Q&A tasks based on consensus/accepted claims
TASKS = [
    {
        "q": "What is the approximate surface temperature of the cosmic microwave background radiation today?",
        "a": "2.725 K", "cat": "cosmology", "diff": "intermediate",
        "choices": ["2.725 K", "3.5 K", "1.9 K", "4.2 K"],
    },
    {
        "q": "What is the Chandrasekhar limit — the maximum mass of a white dwarf star?",
        "a": "1.44 solar masses", "cat": "stellar", "diff": "intermediate",
        "choices": ["1.44 solar masses", "2.5 solar masses", "0.8 solar masses", "3.0 solar masses"],
    },
    {
        "q": "What is the mean distance from Earth to the Moon?",
        "a": "384,400 km", "cat": "solarsystem", "diff": "beginner",
        "choices": ["384,400 km", "250,000 km", "450,000 km", "510,000 km"],
    },
    {
        "q": "What is the approximate current value of the Hubble constant (early-universe measurement)?",
        "a": "67.4 km/s/Mpc", "cat": "cosmology", "diff": "advanced",
        "choices": ["67.4 km/s/Mpc", "73.0 km/s/Mpc", "55.0 km/s/Mpc", "80.0 km/s/Mpc"],
    },
    {
        "q": "What minimum stellar mass is required to produce a core-collapse supernova?",
        "a": "8 solar masses", "cat": "stellar", "diff": "intermediate",
        "choices": ["8 solar masses", "4 solar masses", "12 solar masses", "20 solar masses"],
    },
    {
        "q": "What is the Schwarzschild radius of a 1 solar-mass black hole?",
        "a": "2.95 km", "cat": "blackhole", "diff": "advanced",
        "choices": ["2.95 km", "5.0 km", "1.5 km", "10.0 km"],
    },
    {
        "q": "What fraction of the universe's total energy density does dark energy constitute?",
        "a": "~68%", "cat": "cosmology", "diff": "intermediate",
        "choices": ["~68%", "~27%", "~5%", "~45%"],
    },
    {
        "q": "What is the sound horizon scale used in baryon acoustic oscillations?",
        "a": "~147 Mpc", "cat": "cosmology", "diff": "advanced",
        "choices": ["~147 Mpc", "~50 Mpc", "~300 Mpc", "~90 Mpc"],
    },
    {
        "q": "What is the typical rotation speed of a millisecond pulsar?",
        "a": "Hundreds of Hz (up to ~700 Hz)", "cat": "highenergy", "diff": "advanced",
        "choices": ["Hundreds of Hz (up to ~700 Hz)", "1-10 Hz", "1000-5000 Hz", "0.1-1 Hz"],
    },
    {
        "q": "What is the Roche limit factor for a rigid body?",
        "a": "2.44 planetary radii", "cat": "solarsystem", "diff": "advanced",
        "choices": ["2.44 planetary radii", "1.5 planetary radii", "3.0 planetary radii", "5.0 planetary radii"],
    },
    {
        "q": "At what redshift did cosmic reionization end?",
        "a": "~z = 5.5", "cat": "cosmology", "diff": "advanced",
        "choices": ["~z = 5.5", "~z = 10", "~z = 2", "~z = 20"],
    },
    {
        "q": "What is the approximate age of the universe according to Planck 2018?",
        "a": "13.787 Gyr", "cat": "cosmology", "diff": "intermediate",
        "choices": ["13.787 Gyr", "12.5 Gyr", "15.0 Gyr", "11.0 Gyr"],
    },
    {
        "q": "What are the inner and outer edges of the main asteroid belt?",
        "a": "2.1–3.3 AU", "cat": "solarsystem", "diff": "intermediate",
        "choices": ["2.1–3.3 AU", "1.5–2.5 AU", "3.0–5.0 AU", "4.0–6.0 AU"],
    },
    {
        "q": "What is the typical surface temperature range for O-type stars?",
        "a": "30,000–52,000 K", "cat": "stellar", "diff": "intermediate",
        "choices": ["30,000–52,000 K", "5,000–7,000 K", "10,000–15,000 K", "60,000–80,000 K"],
    },
    {
        "q": "What telescope first imaged the shadow of the supermassive black hole Sgr A*?",
        "a": "Event Horizon Telescope (EHT)", "cat": "blackhole", "diff": "beginner",
        "choices": ["Event Horizon Telescope (EHT)", "Hubble Space Telescope", "James Webb Space Telescope", "Chandra X-ray Observatory"],
    },
    {
        "q": "What is the typical energy release of a core-collapse supernova in ergs?",
        "a": "~10^51 erg", "cat": "highenergy", "diff": "intermediate",
        "choices": ["~10^51 erg", "~10^44 erg", "~10^58 erg", "~10^40 erg"],
    },
    {
        "q": "What is the mean diameter of Ceres, the largest asteroid?",
        "a": "~939 km", "cat": "solarsystem", "diff": "intermediate",
        "choices": ["~939 km", "~500 km", "~1500 km", "~200 km"],
    },
    {
        "q": "Which galaxy is the Milky Way predicted to merge with in ~4.5 billion years?",
        "a": "Andromeda (M31)", "cat": "galaxy", "diff": "beginner",
        "choices": ["Andromeda (M31)", "Triangulum (M33)", "Large Magellanic Cloud", "Centaurus A"],
    },
    {
        "q": "What is the typical duration of a short gamma-ray burst?",
        "a": "Less than 2 seconds", "cat": "highenergy", "diff": "intermediate",
        "choices": ["Less than 2 seconds", "10–100 seconds", "1–10 minutes", "More than 1 hour"],
    },
    {
        "q": "What was the first gravitational wave event detected by LIGO, and what did it result from?",
        "a": "GW150914, merger of two black holes", "cat": "blackhole", "diff": "beginner",
        "choices": ["GW150914, merger of two black holes", "GW170817, neutron star merger", "GW190521, intermediate mass black hole", "GW150914, neutron star collapse"],
    },
]


def hash_answer(answer: str) -> str:
    return hashlib.sha256(answer.lower().strip().encode()).hexdigest()[:32]


db = SessionLocal()
existing = db.query(BenchmarkTask).count()
if existing > 0:
    print(f"Already have {existing} tasks, skipping seed")
    db.close()
    exit(0)

added = 0
for t in TASKS:
    task = BenchmarkTask(
        question=t["q"],
        correct_answer=hash_answer(t["a"]),  # store hashed
        category=t["cat"],
        difficulty=t["diff"],
        answer_choices=t["choices"] if t.get("choices") else None,  # pass list directly for JSON column
        active=True,
    )
    db.add(task)
    added += 1

db.commit()
db.close()
print(f"Seeded {added} benchmark tasks")
