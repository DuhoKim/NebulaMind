#!/usr/bin/env python3
"""
Seed local Ollama agents into the agents table. Idempotent.

Blanc  = llama3.3:70b  (Mac Studio) — writer, jury
Mima   = qwen3:30b-a3b-instruct-2507-q4_K_M     (Mac Studio) — writer, reviewer
Tera   = gemma3:27b    (Mac Studio) — commenter, renovator
Nutty  = deepseek-r1:14b (Mac Studio) — reviewer, evidence_linker
Takji  = phi4:14b      (Mac Studio) — commenter, evidence_linker
Buddle = deepseek-r1:32b (Mac Pro)  — synthesis, council
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.agent import Agent

AGENTS = [
    dict(name="Blanc",  model_name="llama3.3:70b",     role="writer",   specialty="astronomy",
         description="Mac Studio T2 — general writing and jury voting"),
    dict(name="Mima",   model_name="qwen3:30b-a3b-instruct-2507-q4_K_M",         role="writer",   specialty="astronomy",
         description="Mac Studio T2 — writing and reviewing"),
    dict(name="Tera",   model_name="gemma3:27b",         role="commenter", specialty="astronomy",
         description="Mac Studio T2 — commentary and renovation synthesis"),
    dict(name="Nutty",  model_name="deepseek-r1:14b",   role="reviewer", specialty="astronomy",
         description="Mac Studio T1 — fast reviewing and evidence linking"),
    dict(name="Takji",  model_name="phi4:14b",           role="commenter", specialty="astronomy",
         description="Mac Studio T1 — fast commentary and evidence linking"),
    dict(name="Buddle", model_name="deepseek-r1:32b",   role="reviewer", specialty="astronomy",
         description="Mac Pro T3 — deep synthesis and council adjudication"),
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
