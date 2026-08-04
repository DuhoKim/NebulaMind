import json

def score_span_v6(span):
    quote = span.get('quote', '').lower()
    score = 0
    
    strict_tension = ['rules out', 'cannot explain', 'inconsistent', 'tension', 'disagree', 'challenge']
    for t in strict_tension:
        if t in quote: score += 50
        
    if span.get('zone') == 'finding':
        score += 30
    if span.get('zone') == 'interpretation':
        score += 20
        
    text = span.get('quote', '').strip()
    if not text:
        return -1000
    digits = sum(c.isdigit() for c in text)
    if len(text) > 0 and (digits / len(text) > 0.1):
        score -= 100
    if '|' in text:
        score -= 50 * text.count('|')
        
    axes = span.get('axis_tags', [])
    if axes:
        score += 10
        
    return score

def get_modality(quote):
    quote = quote.lower()
    if any(w in quote for w in ['may', 'might', 'could', 'can']):
        return 'may_or_can'
    if any(w in quote for w in ['tension', 'inconsistent', 'disagree', 'debate']):
        return 'mixed_debated'
    if any(w in quote for w in ['probably', 'commonly', 'often', 'usually']):
        return 'commonly_probably'
    if 'model' in quote or 'simulat' in quote:
        return 'in_model_only'
    if 'show' in quote or 'reveal' in quote:
        return 'shows_can_occur'
    return 'is_are_does'

def clean_assertion(quote):
    text = quote.replace('\n', ' ').strip()
    tokens = text.split()
    if not tokens: return None
    
    digits = sum(c.isdigit() for c in text)
    # Stricter table detection
    if len(text) > 0 and (digits / len(text) > 0.15) and ('|' in text or '  ' in text or '=' in text or '+' in text or '-' in text):
        return None 
    if text.count('|') > 2:
        return None
        
    # Check if it has actual alphabetical words
    words = [t for t in tokens if t.isalpha()]
    if len(words) < 5:
        return None
        
    parts = text.split('. ')
    assert_text = parts[0].strip()
    if len(assert_text) < 40 and len(parts) > 1:
        assert_text += '. ' + parts[1].strip()
        
    if assert_text.startswith('We find that '):
        assert_text = assert_text[13].upper() + assert_text[14:]
    elif assert_text.startswith('We show that '):
        assert_text = assert_text[13].upper() + assert_text[14:]
        
    if not assert_text.endswith('.'):
        assert_text += '.'
        
    return assert_text

def main():
    spans_by_bibcode = {}
    with open('SPAN_TABLE.jsonl', 'r') as f:
        for line in f:
            if not line.strip(): continue
            span = json.loads(line)
            if 'span_id' not in span or span.get('type') == 'no_span_record':
                continue
            zone = span.get('zone', 'unknown')
            if zone in ['caption', 'references']:
                continue
            rec_id = span['record_identity']
            bibcode = rec_id.replace('bibcode:', '')
            if bibcode not in spans_by_bibcode:
                spans_by_bibcode[bibcode] = []
            spans_by_bibcode[bibcode].append(span)

    with open('C41_LEDGER.jsonl', 'r') as f:
        ledger = [json.loads(line) for line in f if line.strip()]

    patch = []
    for i, e in enumerate(ledger):
        bibcode = e['source_bibcodes'][0]
        
        # PRESERVE THE V3 SEED COMPLETELY
        if i < 6:
            patch.append({
                "entry_id": e['entry_id'],
                "new_assertion": e['assertion'],
                "modality": e['modality'],
                "span_id": e['evidence_spans'][0]['span_id'],
                "quote": e['evidence_spans'][0]['quote'],
                "zone": e['evidence_spans'][0]['rhetorical_zone'],
                "links": []
            })
            continue

        spans = spans_by_bibcode.get(bibcode, [])
        if not spans:
            patch.append({
                "entry_id": e['entry_id'],
                "no_claim_recoverable": True,
                "evidence_quote": "No spans available."
            })
            continue
            
        spans.sort(key=lambda x: -score_span_v6(x))
        
        best_span = None
        assertion = None
        for s in spans:
            a = clean_assertion(s['quote'])
            if a:
                best_span = s
                assertion = a
                break
                
        if not best_span or not assertion:
            patch.append({
                "entry_id": e['entry_id'],
                "no_claim_recoverable": True,
                "evidence_quote": spans[0]['quote']
            })
        else:
            patch.append({
                "entry_id": e['entry_id'],
                "new_assertion": assertion,
                "modality": get_modality(best_span['quote']),
                "span_id": best_span['span_id'],
                "quote": best_span['quote'],
                "zone": best_span.get('zone', 'unknown'),
                "links": []
            })
            
    for i in range(len(patch) - 1):
        if patch[i].get('no_claim_recoverable'): continue
        for j in range(i+1, min(i+4, len(patch))):
            if patch[j].get('no_claim_recoverable'): continue
            axes_i = set(ledger[i]['tags'])
            axes_j = set(ledger[j]['tags'])
            intersection = axes_i.intersection(axes_j)
            if intersection and any(a in ['formation_efficiency', 'chemical_enrichment', 'ionizing_output'] for a in intersection):
                patch[i]['links'].append({
                    "type": "same_axis",
                    "entry_id": patch[j]['entry_id'],
                    "description": "Shares the same major axis tag."
                })

    with open('STEP4_QUALITY_PATCH.jsonl', 'w') as f:
        for p in patch:
            f.write(json.dumps(p) + '\n')
            
    # Count no_claim
    unrec = sum(1 for p in patch if p.get('no_claim_recoverable'))
    print(f"Generated {len(patch)} patch rows. {unrec} no_claim_recoverable.")

if __name__ == '__main__':
    main()
