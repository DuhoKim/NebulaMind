#!/usr/bin/env python3
"""Re-ground 171 existing QA pairs using grounded chat pipeline."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.qa import QAQuestion, QAAnswer
from app.services.chat_retrieve import retrieve_grounding
from app.routers.chat import _build_prompt, _call_ollama, _parse_response, SYNTHESIS_SYSTEM

def reground_qa():
    db = SessionLocal()
    try:
        questions = db.query(QAQuestion).all()
        print(f"Regrounding {len(questions)} QA pairs...")
        
        updated = 0
        failed = 0
        
        for i, q in enumerate(questions, 1):
            try:
                grounded = retrieve_grounding(q.question, db, top_k=6)
                if not grounded:
                    print(f"  [{i}/{len(questions)}] SKIP (no grounding): {q.question[:50]}")
                    continue
                
                prompt = _build_prompt(q.question, grounded, [])
                raw = _call_ollama("gemma3:27b", SYNTHESIS_SYSTEM, prompt)
                result = _parse_response(raw, grounded)
                
                # Update the answer
                answer = db.query(QAAnswer).filter(QAAnswer.question_id == q.id).first()
                if answer:
                    answer.body = result["answer"]
                else:
                    db.add(QAAnswer(question_id=q.id, body=result["answer"]))
                
                db.commit()
                strength = result.get("grounding_strength", "?")
                ncit = len(result.get("citations", {}))
                print(f"  [{i}/{len(questions)}] OK ({strength}, {ncit} cit): {q.question[:50]}...")
                updated += 1
                
            except Exception as e:
                print(f"  [{i}/{len(questions)}] ERROR: {e}")
                failed += 1
                db.rollback()
        
        print(f"\nDone: {updated} updated, {failed} failed")
    finally:
        db.close()

if __name__ == "__main__":
    reground_qa()
