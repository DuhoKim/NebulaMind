#!/usr/bin/env python3
"""
Seed local Ollama agents into the agents table. Idempotent.

Blanc  = llama3.3:70b  (Mac Studio) — non-astronomy prose
Mima   = qwen3.6:35b-a3b (Mac Studio) — jury juror, scoring
Tera   = qwen3.6:27b   (Mac Studio) — general mid, vision
Nutty  = gpt-oss:20b   (Mac Studio) — fast reviewer, JSON
Buddle = gpt-oss:120b  (Mac Studio) — heavy general synthesis
Vera   = astrosage-70b (Mac Studio) — astronomy drafting
Pico   = vanta-research/atom-astronomy-7b (Mac Studio) — fast astro screen
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.agent import Agent

AGENTS = [
    dict(name="Blanc",  model_name="llama3.3:70b",     role="writer",   specialty="astronomy",
         description="Mac Studio — non-astronomy prose"),
    dict(name="Mima",   model_name="qwen3.6:35b-a3b", role="reviewer", specialty="astronomy",
         description="Mac Studio — jury juror #1 and general scoring"),
    dict(name="Tera",   model_name="qwen3.6:27b", role="commenter", specialty="astronomy",
         description="Mac Studio — general mid model with vision"),
    dict(name="Nutty",  model_name="gpt-oss:20b", role="reviewer", specialty="astronomy",
         description="Mac Studio — jury juror #2, fast reasoning and JSON"),
    dict(name="Buddle", model_name="gpt-oss:120b", role="reviewer", specialty="astronomy",
         description="Mac Studio — heavy general reasoning and synthesis backup"),
    dict(name="Vera", model_name="astrosage-70b", role="writer", specialty="astronomy",
         description="Mac Studio — astronomy drafting and synthesis"),
    dict(name="Pico", model_name="vanta-research/atom-astronomy-7b", role="reviewer", specialty="astronomy",
         description="Mac Studio — fast astronomy screen and jury juror #3"),
]

db = SessionLocal()
for a in AGENTS:
    existing = db.query(Agent).filter(Agent.name == a["name"]).first()
    if existing:
        # Update model_name and description in case they changed
        existing.model_name = a["model_name"]
        existing.role = a["role"]
        existing.specialty = a["specialty"]
        existing.description = a["description"]
        print(f"Updated: {a['name']}")
    else:
        db.add(Agent(**a))
        print(f"Created: {a['name']}")
db.commit()
db.close()
print("Done.")
