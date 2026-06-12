import sys
sys.path.append("/Users/duhokim/NebulaMind/NebulaMind/backend")
from app.database import SessionLocal
from app.models.claim import Claim
import requests
import re

ADS_TOKEN = "dEtX4qbYSjfsKzVUWmcOLanb92IBzjfxMYieB85f"

def get_keywords(text):
    # Strip common words, keep nouns / scientific terms
    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
    stop_words = {"this", "that", "with", "from", "were", "have", "been", "only", "about", "above", "below", "between",
                  "which", "what", "where", "when", "into", "onto", "under", "over", "same", "some", "such", "than", "then"}
    keywords = [w for w in words if w not in stop_words]
    return keywords[:3] # Pick top 3 keywords

db = SessionLocal()
# Pick a few highly specific unverified claims
claims_to_mine = [
    {"id": 1939, "text": "Magnetic fields in the circumgalactic medium (CGM) are the primary regulator of gas accretion efficiency onto galaxies"},
    {"id": 1660, "text": "Survival of cold streams against hydrodynamic disruption requires a stream overdensity of at least 10 within 0.1 R_vir"},
    {"id": 1812, "text": "The ram pressure of galaxies traversing cluster cores can reach values of 10^-11 dyn cm^-2"}
]

print("--- TARGETED NASA ADS MINING PREVIEW ---")
for c in claims_to_mine:
    print(f"\nEvaluating Claim #{c['id']}: '{c['text']}'")
    keywords = get_keywords(c['text'])
    print(f"Extracted Keywords: {keywords}")
    
    # Formulate ADS query
    # We require property:refereed
    query_parts = [f'"{kw}"' for kw in keywords]
    q = f"property:refereed AND " + " AND ".join(query_parts)
    print(f"Formulated ADS Query: '{q}'")
    
    # Query ADS
    url = "https://api.adsabs.harvard.edu/v1/search/query"
    params = {
        "q": q,
        "fl": "title,author,pubdate,identifier",
        "rows": 3,
        "sort": "pubdate desc"
    }
    headers = {"Authorization": f"Bearer {ADS_TOKEN}"}
    
    try:
        r = requests.get(url, params=params, headers=headers)
        r.raise_for_status()
        data = r.json()
        docs = data.get("response", {}).get("docs", [])
        
        print(f"Found {len(docs)} matching peer-reviewed papers on ADS:")
        for i, doc in enumerate(docs):
            title = doc.get("title", [""])[0]
            authors = doc.get("author", [])
            bibcode = doc.get("identifier", [""])[0]
            print(f"  [{i+1}] {bibcode} | {authors[0] if authors else 'Anon'} ({doc.get('pubdate', '')[:4]}) | Title: {title[:75]}")
    except Exception as exc:
        print(f"  ADS Query failed: {exc}")

db.close()
