import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim
from app.services.paper_search import PaperRecord
from scripts.targeted_ads_miner import _call_juror, jury_models
import asyncio

async def test():
    db = SessionLocal()
    claim = db.query(Claim).get(1654)
    record = PaperRecord(
        title="Accretion-driven turbulence in the circumgalactic medium",
        abstract="We present a model for accretion-driven turbulence in the circumgalactic medium...",
        authors=["Author"],
        year=2024,
        arxiv_id="2401.12345"
    )
    
    models = jury_models()
    # Correct the model name for Atom-7B just in case:
    for m in models:
        if m["label"] == "Atom-7B":
            m["model"] = "vanta-research/atom-astronomy-7b:latest"
            
    from scripts.targeted_ads_miner import user_prompt
    prompt = user_prompt(claim, record)
    
    import httpx
    async with httpx.AsyncClient() as client:
        for m in models:
            print(f"Testing {m['label']} on {m['base_url']}...")
            try:
                res = await _call_juror(client, m, prompt)
                if res:
                    print(f"  {m['label']} SUCCESS! Response length: {len(res['raw'])}")
                    print(f"  RAW RESP: {res['raw']!r}")
                    from scripts.targeted_ads_miner import parse_juror
                    parsed = parse_juror(m['label'], res['raw'], record.abstract)
                    print(f"  PARSED RESULT: {parsed}")
                else:
                    print(f"  {m['label']} FAILED! returned None")
            except Exception as e:
                print(f"  {m['label']} RAISED EXCEPTION: {e}")
                import traceback
                traceback.print_exc()
    db.close()

asyncio.run(test())
