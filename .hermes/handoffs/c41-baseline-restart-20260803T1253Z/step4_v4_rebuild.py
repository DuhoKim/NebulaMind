import json

def score_span(span):
    quote = span.get('quote', '').lower()
    score = 0
    
    strict_tension = ['rules out', 'cannot explain', 'inconsistent', 'tension', 'disagree', 'challenge']
    contested_dispersion = ['higher', 'lower', 'offset', 'scatter', 'deficit', 'excess', 'discrepancy']
    comparatives = ['more', 'less', 'greater', 'smaller', 'than', 'ratio']
    
    for t in strict_tension:
        if t in quote: score += 50
    for t in contested_dispersion:
        if t in quote: score += 20
    for t in comparatives:
        if t in quote: score += 5
        
    digits = sum(c.isdigit() for c in quote)
    score += digits * 2
    
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
    
def get_certainty(modality):
    if modality == 'mixed_debated': return 'actively_debated'
    if modality == 'in_model_only': return 'contradicted_or_model_dependent'
    if modality in ['may_or_can', 'shows_can_occur', 'reported_only']: return 'emerging_sample_limited'
    return 'emerging_sample_limited' # Ceiling for single source

def format_assertion(quote):
    parts = quote.split('. ')
    assert_text = parts[0]
    if not assert_text.endswith('.'):
        assert_text += '.'
    return assert_text.replace('\n', ' ').strip()

def main():
    with open('STEP2_FULLTEXT_MANIFEST.json', 'r') as f:
        manifest = json.load(f)
        
    ranks = {}
    titles = {}
    for r in manifest['records']:
        key = r['identity']['key']
        ranks[key] = r['identity']['rank']
        titles[key] = r['identity'].get('title', 'Unknown Title')
        
    spans_by_record = {}
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
            if rec_id not in spans_by_record:
                spans_by_record[rec_id] = []
            spans_by_record[rec_id].append(span)
            
    ledger = []
    
    # Load V3 seed entries
    with open('C41_LEDGER.jsonl', 'r') as f:
        for line in f:
            if not line.strip(): continue
            entry = json.loads(line)
            ledger.append(entry)
            
    # Track covered papers
    covered_bibcodes = set()
    for entry in ledger:
        for b in entry.get('source_bibcodes', []):
            covered_bibcodes.add(b)
            
    no_entry_reasons = []
    entry_counter = len(ledger) + 1
    
    for rank_target in range(1, 181):
        rec_id = None
        for k, r in ranks.items():
            if r == rank_target:
                rec_id = k
                break
                
        if not rec_id: continue
        is_priority = rank_target <= 68
        
        bibcode = rec_id.replace('bibcode:', '')
        if bibcode in covered_bibcodes:
            continue
            
        if rec_id not in spans_by_record:
            if is_priority:
                no_entry_reasons.append(f"Rank {rank_target} ({rec_id}): No eligible spans found (only caption/references or no extractions).")
            continue
            
        rec_spans = spans_by_record[rec_id]
        scored_spans = [(score_span(s), s) for s in rec_spans if score_span(s) > 10 and s.get('axis_tags')]
        scored_spans.sort(key=lambda x: -x[0])
        
        if not scored_spans:
            if is_priority:
                no_entry_reasons.append(f"Rank {rank_target} ({rec_id}): Spans present but none met minimum score and axis tag requirements.")
            continue
            
        best_score, best_span = scored_spans[0]
        quote = best_span['quote']
        modality = get_modality(quote)
        certainty = get_certainty(modality)
        axes = best_span.get('axis_tags', [])
        
        rz = best_span.get('zone', 'unknown')
        if rz == 'unknown':
            stance = 'qualifies'
        else:
            stance = 'supports' if rz in ['finding', 'interpretation'] else 'qualifies'
            
        entry = {
            "entry_id": f"c41_{entry_counter:03d}",
            "assertion": format_assertion(quote),
            "modality": modality,
            "scope": {
                "population": "extracted population",
                "sample": "observational sample",
                "redshift": "source-specific",
                "mass": "source-specific",
                "environment": "source-specific",
                "simulation_context": None
            },
            "epistemic_type": "observational_sample",
            "source_access": "full_text",
            "method_or_model": "automated extraction",
            "source_bibcodes": [bibcode],
            "evidence_spans": [{
                "paper_id": bibcode,
                "span_id": best_span['span_id'],
                "quote": quote,
                "location": "C41_STEP3_V3",
                "rhetorical_zone": rz,
                "stance": stance,
                "rationale": "Automated ledger composition based on score.",
                "source_access": "full_text",
                "source_title": titles.get(rec_id, "Unknown Title"),
                "source_year": bibcode[0:4],
                "source_epistemic_type_original": "observational_sample"
            }],
            "certainty_dimensions": {
                "directness": "direct",
                "consistency": "single_source",
                "precision": "qualitative",
                "sample_size": "sample-specific",
                "model_dependence": "none"
            },
            "certainty_level": certainty,
            "links": [],
            "as_of": "2026-08-04",
            "verification_status": "pending",
            "verification_note": "Awaiting human review.",
            "tags": axes
        }
        
        ledger.append(entry)
        entry_counter += 1
        
        if entry_counter > 80:
            break
            
    with open('C41_LEDGER.jsonl', 'w') as f:
        for e in ledger:
            f.write(json.dumps(e) + '\n')
            
    with open('NO_ENTRY_REASONS.json', 'w') as f:
        json.dump(no_entry_reasons, f, indent=2)

if __name__ == '__main__':
    main()
