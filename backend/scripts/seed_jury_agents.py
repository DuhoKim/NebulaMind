#!/usr/bin/env python3
"""Create the 4 JuryAgent rows. Idempotent."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.agent import Agent

JURY_AGENTS = [
    ("JuryQwen36",   "qwen3.6:35b-a3b-nvfp4"),
    ("JuryGptOss20", "gpt-oss:20b"),
    ("JuryAtom",     "vanta-research/atom-astronomy-7b"),
    ("JuryGeminiFlash", "gemini-2.5-flash"),
]

db = SessionLocal()
for name, model in JURY_AGENTS:
    if not db.query(Agent).filter(Agent.name == name).first():
        db.add(Agent(name=name, role="jury", model_name=model, specialty="jury"))
        print(f"Created: {name}")
    else:
        print(f"Exists:  {name}")
db.commit()
db.close()
