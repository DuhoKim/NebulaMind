import pytest
from scripts.align_citations import ResolvedCitation, replace_citations, tokenize_paren_citations

def test_multi_cite_parsing():
    content = "The supermassive black hole mass scales with the bulge mass (Fabian 2012; Heckman & Best 2014)."
    matches = tokenize_paren_citations(content)
    
    assert len(matches) == 2
    
    # First match should be the outer parenthetical
    m1 = matches[0]
    assert m1.raw == "(Fabian 2012; Heckman & Best 2014)"
    assert m1.author_year_key == "Fabian 2012"
    assert m1.first_author == "Fabian"
    assert m1.year == 2012
    # Second match should have zero width at the end
    m2 = matches[1]
    assert m2.raw == ""
    assert m2.author_year_key == "Heckman & Best 2014"
    assert m2.first_author == "Heckman"
    assert m2.year == 2014

def test_discourse_marker_cite():
    content = "This was observed at high redshift (e.g., Labbé et al. 2023)."
    matches = tokenize_paren_citations(content)
    
    assert len(matches) == 1
    m = matches[0]
    assert m.raw == "(e.g., Labbé et al. 2023)"
    assert m.author_year_key == "Labbé et al 2023"
    assert m.first_author == "Labbé"
    assert m.year == 2023

def test_comma_before_year_cite():
    content = "The burst population was cataloged early (Hankins et al., 1967)."
    matches = tokenize_paren_citations(content)

    assert len(matches) == 1
    assert matches[0].author_year_key == "Hankins et al 1967"
    assert matches[0].first_author == "Hankins"
    assert matches[0].year == 1967

def test_arxiv_id_or_other_ignores():
    # Boylan-Kolchin 2023 matches, arXiv:2605.03635 does not match citation pattern, so only 1 match
    content = "Various models predict different densities (Boylan-Kolchin 2023; arXiv:2605.03635)."
    matches = tokenize_paren_citations(content)
    
    assert len(matches) == 1
    m = matches[0]
    assert m.raw == "(Boylan-Kolchin 2023; arXiv:2605.03635)"
    assert m.author_year_key == "Boylan-Kolchin 2023"
    assert m.year == 2023

def test_multi_cite_replacement_preserves_atom_order():
    content = "Feedback is complex (Fabian 2012; Heckman & Best 2014; Labbé et al. 2023)."
    matches = tokenize_paren_citations(content)
    resolved = [
        ResolvedCitation(matches[0], 101, "fixture", 1.0),
        ResolvedCitation(matches[1], None, "unmatched", 0.0),
        ResolvedCitation(matches[2], 303, "fixture", 1.0),
    ]

    assert replace_citations(content, resolved) == (
        "Feedback is complex "
        "<!--cite:101--><!--cite-unmatched:Heckman & Best 2014--><!--cite:303-->."
    )
