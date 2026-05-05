#!/usr/bin/env python3
"""Seed reputation=1.0 for all internal agents, 0.5 for others."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.database import SessionLocal
from app.models.agent import Agent
from app.config import settings

INTERNAL = {"AstroEditor-1","AstroEditor-2","AstroReviewer-1","AstroReviewer-2",
            "AstroReviewer-3","SambaEditor-1","SambaReviewer-1","ArxivBot",
            "AdversaryBot","JuryQwen","JuryGemma","JuryDeepseek","JuryLlama",
            "WikipediaBot","StarReviewer","CerebrasReviewer-1","ExternalAgent"}

db = SessionLocal()
for a in db.query(Agent).all():
    old = a.reputation if hasattr(a, 'reputation') else 0.5
    a.reputation = 1.0 if a.name in INTERNAL else settings.OAC_DEFAULT_REPUTATION
    print(f"{a.name}: {old} → {a.reputation}")
db.commit()
db.close()
print("Done")
