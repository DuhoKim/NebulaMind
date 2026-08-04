import sys
import json
from astroquery.vizier import Vizier

def main():
    Vizier.ROW_LIMIT = 50
    catalogs = [
        'V/159',
        'J/ApJ/946/L16', 'J/ApJ/960/104', 'J/ApJS/278/33', 'J/A+A/691/A59', 'J/A+A/708/A235', 'J/AJ/168/113',
        'J/ApJ/811/29', 'J/ApJ/812/114', 'J/ApJ/831/182',
        'J/ApJS/270/7', 'J/ApJS/270/12'
    ]
    
    manifest = []
    for cat_id in catalogs:
        try:
            res = Vizier.get_catalogs(cat_id)
            for t in res:
                table_name = t.meta.get('name', 'unknown')
                description = t.meta.get('description', '')
                cols = t.colnames
                count = len(t) # Astroquery might only return up to ROW_LIMIT, but it's enough to check columns.
                manifest.append({
                    "catalog_id": cat_id,
                    "table_name": table_name,
                    "description": description,
                    "columns": cols
                })
        except Exception as e:
            print(f"Error on {cat_id}: {e}")

    with open('T1_CATALOG_META.json', 'w') as f:
        json.dump(manifest, f, indent=2)

if __name__ == "__main__":
    main()
