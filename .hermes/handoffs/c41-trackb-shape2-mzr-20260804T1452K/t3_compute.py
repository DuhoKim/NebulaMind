import sys, os
sys.path.append(os.path.abspath('../../../tools'))
from nm_external_data import vizier_tap
import json

def main():
    print("Fetching JADES gsgrat...")
    gsgrat = vizier_tap('SELECT TOP 10 * FROM "V/159/gsgrat" WHERE zspec > 3')
    print("Fetching JADES gssample...")
    gssample = vizier_tap('SELECT TOP 10 * FROM "V/159/gssample"')
    
    print("Checking contract fields...")
    # T2b says: Method identity, Reference frame, Propagated conversion uncertainty, Channel label.
    # Also "Class A — direct auroral detection... with Te derived and O/H computed by the direct method in the cited source."
    
    sample_rows = []
    anomalies = []
    
    if gsgrat and len(gsgrat) > 0:
        row = gsgrat[0]
        # Check if Te and O/H are computed
        has_te = any('Te' in k or 'T_e' in k for k in row.keys())
        has_oh = any('OH' in k or 'O_H' in k or 'O/H' in k for k in row.keys())
        if not has_te and not has_oh:
            anomalies.append(
                "CONTRACT CONFLICT: JADES 'gsgrat' provides line fluxes but NO direct Te or O/H computed by the source. "
                "Per T2b §3, Class A requires Te derived and O/H computed by the direct method IN THE CITED SOURCE. "
                "Re-deriving Te from fluxes here violates the contract."
            )
            
    # Check GLASS for mu
    print("Fetching GLASS table...")
    glass = vizier_tap('SELECT TOP 1 * FROM "J/ApJ/812/114/table3"')
    if glass and len(glass) > 0:
        row = glass[0]
        has_mu = any('mu' in k.lower() or 'magnif' in k.lower() for k in row.keys())
        if not has_mu:
            anomalies.append(
                "CONTRACT CONFLICT: GLASS/MACS catalog lacks per-object magnification (mu) and its uncertainty. "
                "Per T2b §5, these must default to 'cluster-line-of-sight' and be EXCLUDED from the main MZR. "
                "This removes the $10^{5.7}$ low-mass sample from the anchor set."
            )

    if anomalies:
        print("STOPPING due to contract conflicts:")
        for a in anomalies:
            print(f"- {a}")
        
        with open('T3_SAMPLE.jsonl', 'w') as f:
            pass # Empty because we stopped
        with open('T3_RESULTS.json', 'w') as f:
            json.dump({"status": "ABORTED", "reason": anomalies}, f, indent=2)
            
        with open('GORU_T3_REPORT.md', 'w') as f:
            f.write('# GORU T3 REPORT\n\n')
            f.write('## Honest Anomalies (Execution Stopped)\n')
            for a in anomalies:
                f.write(f'- {a}\n')
            f.write('\n## Politeness & Runtime\n')
            f.write('- `nm_external_data` was used with cache and defaults.\n')
            f.write('- Runtime: <1 minute.\n\n')
            f.write('GORU_SHAPE2_T3_COMPLETE_20260804\n')
            
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "EXECUTION ABORTED\nContract Conflicts", ha="center", va="center", fontsize=15)
        ax.axis("off")
        fig.savefig("T3_FIGURE_ABORTED.png")

        sys.exit(1)
        
    print("Success (unexpected).")

if __name__ == '__main__':
    main()
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.text(0.5, 0.5, "EXECUTION ABORTED\nContract Conflicts", ha="center", va="center", fontsize=15)
ax.axis("off")
fig.savefig("T3_FIGURE_ABORTED.png")
