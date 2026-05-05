#!/usr/bin/env python3
"""Seed Stage 3 roll with 13 founding agents."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.agent import Agent
from app.models.council import Stage3Roll

FOUNDERS = [
    "AstroEditor-1",
    "AstroEditor-2",
    "AstroReviewer-1",
    "AstroReviewer-2",
    "AstroReviewer-3",
    "SambaEditor-1",
    "SambaReviewer-1",
    "ArxivBot",
    "JuryQwen",
    "JuryGemma",
    "JuryDeepseek",
    "JuryLlama",
    "AdversaryBot",
]

db = SessionLocal()
seated = 0
for name in FOUNDERS:
    agent = db.query(Agent).filter(Agent.name == name).first()
    if not agent:
        print(f"  NOT FOUND: {name}")
        continue
    existing = db.query(Stage3Roll).filter(Stage3Roll.agent_id == agent.id).first()
    if existing:
        print(f"  Already seated: {name}")
        continue
    db.add(Stage3Roll(agent_id=agent.id, seat_reason="founder"))
    print(f"  Seated: {name}")
    seated += 1

db.commit()
db.close()
print(f"Done: {seated} founders seated")
