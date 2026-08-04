import json

def main():
    with open('C41_LEDGER.jsonl', 'r') as f:
        ledger = [json.loads(line) for line in f if line.strip()]
        
    assert len(ledger) == 80, f"Expected 80 entries before patch, got {len(ledger)}"
    
    with open('STEP4_QUALITY_PATCH.jsonl', 'r') as f:
        patch = [json.loads(line) for line in f if line.strip()]
        
    assert len(patch) == 80, f"Expected 80 patch rows, got {len(patch)}"
    
    patch_by_id = {p['entry_id']: p for p in patch}
    
    for e in ledger:
        p = patch_by_id.get(e['entry_id'])
        assert p, f"Missing patch row for {e['entry_id']}"
        
        if p.get('no_claim_recoverable'):
            e['assertion'] = "NO_CLAIM_RECOVERABLE from bound spans"
            e['certainty_level'] = "no_info"
            # Update the evidence span to the verbatim quoted one
            e['evidence_spans'][0]['quote'] = p['evidence_quote']
            e['evidence_spans'][0]['rationale'] = "Span could not support an atomic assertion."
            e['modality'] = "is_are_does"
        else:
            e['assertion'] = p['new_assertion']
            e['modality'] = p['modality']
            e['evidence_spans'][0]['span_id'] = p['span_id']
            e['evidence_spans'][0]['quote'] = p['quote']
            e['evidence_spans'][0]['rhetorical_zone'] = p['zone']
            e['evidence_spans'][0]['rationale'] = "Indicates that " + p['new_assertion'].lower()[:60] + "..."
            e['links'] = p['links']
            
            # Stance logic
            rz = p['zone']
            e['evidence_spans'][0]['stance'] = 'supports' if rz in ['finding', 'interpretation'] else 'qualifies'
            
    assert len(ledger) == 80, f"Expected 80 entries after patch, got {len(ledger)}"
    
    with open('C41_LEDGER.jsonl', 'w') as f:
        for e in ledger:
            f.write(json.dumps(e) + '\n')
            
    # Update receipt
    with open('STEP4_VALIDATION_RECEIPT.json', 'r') as f:
        receipt = json.load(f)
        
    receipt['entries_count'] = 80
    receipt['version'] = 'V6'
    
    with open('STEP4_VALIDATION_RECEIPT.json', 'w') as f:
        json.dump(receipt, f, indent=2)
        
    print("Patch applied successfully. Ledger remains at 80 entries.")

if __name__ == '__main__':
    main()
