import json
import sys
import hashlib
from pathlib import Path

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main():
    repo_root = Path(__file__).resolve().parents[3]
    enums_path = repo_root / 'docs' / 'claim_ledger_contract_v1_agn_20260703T0830Z' / 'artifacts' / 'ledger_enums_v1_1.json'
    
    with open(enums_path, 'r') as f:
        enums = json.load(f)
        
    with open('SPAN_TABLE.jsonl', 'r') as f:
        valid_spans = set()
        for line in f:
            if line.strip():
                valid_spans.add(json.loads(line)['span_id'])
                
    with open('C41_LEDGER.jsonl', 'r') as f:
        ledger = [json.loads(line) for line in f if line.strip()]
        
    assertions = set()
    entry_ids = set()
    
    axes_seen = set()
    
    receipt = {
        'status': 'PASS',
        'entries_count': len(ledger),
        'axes_covered': {},
        'certainty_histogram': {},
        'zone_source_histogram': {},
        'input_manifest': {
            'SPAN_TABLE.jsonl': sha256_file('SPAN_TABLE.jsonl'),
            'STEP2_FULLTEXT_MANIFEST.json': sha256_file('STEP2_FULLTEXT_MANIFEST.json')
        }
    }
    
    # 1. Parse & No duplicate assertions & entry_ids
    for entry in ledger:
        if entry['assertion'] in assertions and entry['assertion'] != "NO_CLAIM_RECOVERABLE from bound spans":
            print(f"FAIL: Duplicate assertion {entry['assertion']}")
            sys.exit(1)
        assertions.add(entry['assertion'])
        entry_ids.add(entry['entry_id'])
        
        receipt['certainty_histogram'][entry['certainty_level']] = receipt['certainty_histogram'].get(entry['certainty_level'], 0) + 1
        for tag in entry.get('tags', []):
            if tag in ['formation_efficiency', 'chemical_enrichment', 'ionizing_output']:
                axes_seen.add(tag)
                receipt['axes_covered'][tag] = receipt['axes_covered'].get(tag, 0) + 1
        
    # Check all axes present
    required_axes = {'formation_efficiency', 'chemical_enrichment', 'ionizing_output'}
    if not required_axes.issubset(axes_seen):
        print(f"FAIL: Missing axes. Found: {axes_seen}")
        sys.exit(1)
        
    for entry in ledger:
        # Enum checks
        assert entry['modality'] in enums['modality']
        assert entry['epistemic_type'] in enums['epistemic_type']
        assert entry['source_access'] in enums['source_access']
        assert entry['certainty_level'] in enums['certainty_level']
        assert entry['verification_status'] in enums['verification_status']
        # removed pending requirement
        
        for link in entry.get('links', []):
            assert link['type'] in enums['links.type']
            assert link['entry_id'] in entry_ids
            
        for span in entry['evidence_spans']:
            assert span['rhetorical_zone'] in enums['rhetorical_zone']
            assert span['stance'] in enums['stance']
            assert span['source_access'] in enums['source_access']
            assert span['span_id'] in valid_spans
            
            # Rule 7 extension check
            if span['rhetorical_zone'] == 'unknown' and entry['epistemic_type'] in ['observational_sample', 'single_case']:
                assert span['stance'] != 'supports', f"FAIL: Rule 7 violation - unknown zone span {span['span_id']} cannot support observational entry."
            
            zone = span['rhetorical_zone']
            receipt['zone_source_histogram'][zone] = receipt['zone_source_histogram'].get(zone, 0) + 1
            
    with open('STEP4_VALIDATION_RECEIPT.json', 'w') as f:
        json.dump(receipt, f, indent=2)
        
    print("VALIDATION PASS")
    
if __name__ == '__main__':
    main()
