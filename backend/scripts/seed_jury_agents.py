#!/usr/bin/env python3
"""Create the 4 JuryAgent rows. Idempotent."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.agent import Agent

JURY_AGENTS = [
    ("JuryQwen",     "qwen3:30b-a3b-instruct-2507-q4_K_M"),
    ("JuryGemma",    "gemma3:27b"),
    ("JuryDeepseek", "deepseek-r1:14b"),
    ("JuryLlama",    "llama3.3:70b"),
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
