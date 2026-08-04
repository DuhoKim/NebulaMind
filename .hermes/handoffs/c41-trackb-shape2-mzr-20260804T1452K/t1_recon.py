import sys
import json
import os
sys.path.append(os.path.abspath("../../../tools"))
from nm_external_data import vizier_tap

def main():
    manifest = []
    
    # 1. Search for JWST metallicity / auroral / JADES / CEERS / GLASS / UNCOVER catalogs
    query = """
    SELECT TOP 50 m.obs_id, m.cat_name, m.title
    FROM "METAcat" m
    WHERE m.title LIKE '%JWST%' 
       OR m.title LIKE '%JADES%' 
       OR m.title LIKE '%CEERS%' 
       OR m.title LIKE '%auroral%'
       OR m.title LIKE '%metallicity%'
       OR m.title LIKE '%UNCOVER%'
    """
    try:
        results = vizier_tap(query)
    except Exception as e:
        results = []
        print(f"Error querying METAcat: {e}")

    with open('_tmp_vizier_meta.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
