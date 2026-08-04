import json
import sys
import os
sys.path.append(os.path.abspath("../../../tools"))
from nm_external_data import vizier_tap

def analyze():
    with open('T1_CATALOG_META.json', 'r') as f:
        meta = json.load(f)

    manifest = []
    
    # Process only a few representative tables per survey to avoid spamming VizieR
    # JADES V/159 has photometry. We are looking for Te metallicity catalogs!
    
    # Let's filter for tables that might actually contain metallicity/mass/redshift
    candidate_tables = []
    for m in meta:
        desc = m['description'].lower()
        cols = [c.lower() for c in m['columns']]
        
        # Check if it has something related to mass and redshift and metallicity
        has_z = any('z' in c or 'redshift' in c for c in cols)
        has_m = any('mass' in c or 'mstar' in c or 'm*' in c for c in cols)
        has_z_desc = 'redshift' in desc
        
        candidate_tables.append(m)

    for m in candidate_tables:
        table_id = m['table_name']
        
        # Determine column inventory vs required fields
        cols = m['columns']
        lower_cols = [c.lower() for c in cols]
        
        has_z = any(c in ['z', 'redshift', 'zspec', 'zphot'] for c in lower_cols)
        has_mass = any('mass' in c or 'mstar' in c or 'logm' in c for c in lower_cols)
        has_metal = any('oh' in c or 'metal' in c or '12logoh' in c or 'o_h' in c or 'te' in c for c in lower_cols)
        
        # Count rows using TAP
        try:
            res = vizier_tap(f'SELECT COUNT(*) as cnt FROM "{table_id}"')
            if res and len(res) > 0:
                row_count = int(res[0].get('cnt', 0))
            else:
                row_count = 0
        except Exception as e:
            row_count = f"Error: {e}"
            
        manifest.append({
            "catalog_id": m['catalog_id'],
            "table_id": table_id,
            "availability": "Available" if isinstance(row_count, int) else "Error",
            "columns_vs_required": {
                "has_redshift (z>3 check)": has_z,
                "has_mass (M*)": has_mass,
                "has_metallicity (Te/O/H)": has_metal
            },
            "row_count": row_count,
            "provenance_notes": f"VizieR table {table_id}: {m['description'][:100]}..."
        })

    with open('T1_CATALOG_MANIFEST.json', 'w') as f:
        json.dump(manifest, f, indent=2)

if __name__ == "__main__":
    analyze()
