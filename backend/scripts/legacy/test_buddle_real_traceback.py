import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim
from app.services.paper_search import PaperRecord
from scripts.targeted_ads_miner import user_prompt, JURY_SYSTEM_PROMPT
import httpx
import asyncio
import traceback

async def test():
    db = SessionLocal()
    claim = db.query(Claim).get(1939)
    record = PaperRecord(
        title="Accretion-driven turbulence in the circumgalactic medium",
        abstract="We present a model for accretion-driven turbulence in the circumgalactic medium...",
        authors=["Author"],
        year=2024,
        arxiv_id="2401.12345"
    )
    prompt = user_prompt(claim, record)
    
    url = "http://192.188.0.4:11435/v1/chat/completions"
    payload = {
        "model": "deepseek-r1:32b",
        "messages": [
            {"role": "system", "content": JURY_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "temperature": 0,
        "options": {"num_ctx": 4096, "temperature": 0},
    }
    
    async with httpx.AsyncClient() as client:
        try:
            print("Sending real prompt to Buddle...")
            res = await client.post(url, json=payload, timeout=180)
            print("Response status:", res.status_code)
            print("Response text:", res.text[:300])
        except Exception as e:
            print("Exception raised:")
            traceback.print_exc()
    db.close()

asyncio.run(test())
