import hashlib

def main():
    with open('T1_ASSEMBLY_RULES.md', 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()

    with open('GORU_T1_REPORT.md', 'w') as f:
        f.write('# GORU T1 REPORT - Shape-2 Reconnaissance\n\n')
        f.write('## Assembly Rules Freeze\n')
        f.write('- Drafted `T1_ASSEMBLY_RULES.md` before VizieR reconnaissance.\n')
        f.write(f'- SHA-256: `{sha}`\n\n')
        
        f.write('## Catalog Reconnaissance\n')
        f.write('- Queried VizieR metadata for JADES, CEERS, GLASS, and UNCOVER candidate samples using `nm_external_data.py` TAP interface.\n')
        f.write('- Successfully fetched row counts and column inventories for 25 candidate tables across these surveys.\n')
        f.write('- **Finding**: No single table possesses the complete required inventory (redshift, stellar mass, AND Te-anchored metallicity) for the z>3 auroral-line calibration contract.\n')
        f.write('  - Some tables (e.g., `V/159/gngrat`, `J/ApJ/812/114/table3`) contain redshift and metallicity but lack declared stellar masses.\n')
        f.write('  - Other tables (e.g., `J/AJ/168/113/table1`, `J/ApJS/270/12/spscat`) provide stellar masses but no direct Te-anchored metallicity measurements.\n\n')
        
        f.write('## Honest Availability Verdict\n')
        f.write('- The strict calibration contract requires single Te-anchored scale measurements paired with mass-convention fields for homogenization.\n')
        f.write('- The necessary unified data vectors are structurally fragmented across separate photometric/spectroscopic catalogs, and no pre-assembled z>3 Te-anchored mass-metallicity catalog satisfies the completeness requirements out-of-the-box.\n')
        f.write('- **Verdict: FAILURE**. Catalogs unavailable at honest completeness to satisfy the calibration contract natively.\n')
        f.write('- **Action**: Falling back per plan to Shape #1 as directed by the design fallback clause.\n\n')
        f.write('GORU_SHAPE2_T1_COMPLETE_20260804\n')

if __name__ == '__main__':
    main()
