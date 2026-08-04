import json

def main():
    # 1. Load spans
    spans_by_id = {}
    with open('SPAN_TABLE.jsonl', 'r') as f:
        for line in f:
            if not line.strip(): continue
            span = json.loads(line)
            if 'span_id' in span:
                spans_by_id[span['span_id']] = span

    # 2. Load patch
    patch_rows = []
    with open('STEP4_COMPOSITION_PATCH.jsonl', 'r') as f:
        patch_rows = [json.loads(line) for line in f if line.strip()]

    assertions_patch = {r['entry_id']: r for r in patch_rows if r.get('row_type') == 'assertion'}
    rebinds = [r for r in patch_rows if r.get('row_type') == 'rebind_receipt']
    rebinds_by_id = {r['entry_id']: r for r in rebinds}

    # 3. Load ledger
    with open('C41_LEDGER.jsonl', 'r') as f:
        ledger = [json.loads(line) for line in f if line.strip()]

    assert len(ledger) == 80, f"Expected 80 rows, got {len(ledger)}"

    # Append rebinds to zone adjudication
    with open('STEP4_ZONE_ADJUDICATION.jsonl', 'a') as f:
        for r in rebinds:
            f.write(json.dumps(r) + '\n')

    # 4. Apply patch
    for e in ledger:
        eid = e['entry_id']
        
        # Apply rebind if any
        if eid in rebinds_by_id:
            reb = rebinds_by_id[eid]
            new_span_id = reb['new_span_id']
            if new_span_id not in spans_by_id:
                raise ValueError(f"Span {new_span_id} not found in SPAN_TABLE")
            new_span = spans_by_id[new_span_id]
            e['evidence_spans'][0]['span_id'] = new_span_id
            e['evidence_spans'][0]['quote'] = new_span['quote']
            e['evidence_spans'][0]['rhetorical_zone'] = new_span.get('zone', 'unknown')
            
        # Apply assertion if any
        if eid in assertions_patch:
            a = assertions_patch[eid]
            
            if 'new_assertion' in a: e['assertion'] = a['new_assertion']
            if 'new_modality' in a: e['modality'] = a['new_modality']
            
            if 'new_precision' in a: e['certainty_dimensions']['precision'] = a['new_precision']
            if 'new_model_dependence' in a: e['certainty_dimensions']['model_dependence'] = a['new_model_dependence']
            
            if 'new_rationale' in a: e['evidence_spans'][0]['rationale'] = a['new_rationale']
            if 'new_epistemic_type' in a: e['epistemic_type'] = a['new_epistemic_type']
            if 'new_certainty_level' in a: e['certainty_level'] = a['new_certainty_level']
            if 'new_stance' in a: e['evidence_spans'][0]['stance'] = a['new_stance']
            
            if 'best_span_id' in a: e['evidence_spans'][0]['span_id'] = a['best_span_id']
            if 'best_span_quote' in a: e['evidence_spans'][0]['quote'] = a['best_span_quote']
            
            if 'add_tags' in a:
                for tag in a['add_tags']:
                    if tag not in e.get('tags', []):
                        e.setdefault('tags', []).append(tag)
                        
            # Enforce rule 7 if not explicitly overridden by new_stance
            if 'new_stance' not in a and not a.get('no_claim_recoverable'):
                rz = e['evidence_spans'][0]['rhetorical_zone']
                if rz == 'unknown' and e['epistemic_type'] in ['observational_sample', 'single_case']:
                    e['evidence_spans'][0]['stance'] = 'qualifies'
                elif rz in ['finding', 'interpretation']:
                    e['evidence_spans'][0]['stance'] = 'supports'
                else:
                    e['evidence_spans'][0]['stance'] = 'qualifies'

    assert len(ledger) == 80, f"Expected 80 rows after patch, got {len(ledger)}"

    with open('C41_LEDGER.jsonl', 'w') as f:
        for e in ledger:
            f.write(json.dumps(e) + '\n')
            
    # Update receipt
    with open('STEP4_VALIDATION_RECEIPT.json', 'r') as f:
        receipt = json.load(f)
        
    receipt['entries_count'] = 80
    receipt['version'] = 'V7'
    
    with open('STEP4_VALIDATION_RECEIPT.json', 'w') as f:
        json.dump(receipt, f, indent=2)
            
    print("Patch applied.")

if __name__ == '__main__':
    main()
