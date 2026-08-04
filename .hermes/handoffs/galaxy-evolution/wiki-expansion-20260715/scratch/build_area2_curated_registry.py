import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
PUBLIC_ADS = AREA / "area2_chemical_evolution_PUBLIC_ADS_IDENTITY_CHECK.json"
OUT = AREA / "area2_chemical_evolution_CURATED_SOURCE_REGISTRY.json"

SOURCES = [
    dict(key="Tinsley1980", authors="Tinsley", year=1980, title="Evolution of the Stars and Gas in Galaxies", doi=None, arxiv="2203.02041", bibcode="1980FCPh....5..287T", role="orientation,established", boundary="Foundational chemical-evolution equations, delayed enrichment, simple-model limits, and the G-dwarf problem; the arXiv item is a later scan."),
    dict(key="Mannucci2010", authors="Mannucci", year=2010, title="A fundamental relation between mass, star formation rate and metallicity in local and high-redshift galaxies", doi="10.1111/j.1365-2966.2010.17291.x", arxiv="1005.0006", bibcode="2010MNRAS.408.2115M", role="established,debate", boundary="Original FMR sample and calibration only; not proof of universal non-evolution or a unique inflow mechanism."),
    dict(key="Lilly2013", authors="Lilly", year=2013, title="Gas regulation of galaxies", doi="10.1088/0004-637X/772/2/119", arxiv="1303.5059", bibcode="2013ApJ...772..119L", role="theory,established,debate", boundary="Analytic gas-regulator framework; equilibrium is an approximation, not a direct measurement of inflow or outflow."),
    dict(key="Kewley2019", authors="Kewley", year=2019, title="Understanding Galaxy Evolution Through Emission Lines", doi="10.1146/annurev-astro-081817-051832", arxiv="1910.09730", bibcode="2019ARA&A..57..511K", role="orientation,caveat", boundary="Review of emission-line diagnostics, ionization and DIG/systematic effects; not one universal abundance calibration."),
    dict(key="MaozBrandt2012", authors="Maoz", year=2012, title="The delay-time distribution of Type Ia supernovae from Sloan II", doi="10.1111/j.1365-2966.2012.21871.x", arxiv="1206.0465", bibcode="2012MNRAS.426.3282M", role="established,measurement", boundary="Sloan-II host reconstruction and its IMF/SFH assumptions; supports a broad approximately t^-1 DTD, not a unique progenitor channel."),
    dict(key="MaozNelemans2014", authors="Maoz", year=2014, title="Observational Clues to the Progenitors of Type Ia Supernovae", doi="10.1146/annurev-astro-082812-141031", arxiv="1312.0628", bibcode="2014ARA&A..52..107M", role="orientation,debate", boundary="Review of Type-Ia progenitors and DTD evidence; progenitor mixture remains unresolved."),
    dict(key="KarakasLattanzio2014", authors="Karakas", year=2014, title="The Dawes Review 2: Nucleosynthesis and Stellar Yields of Low- and Intermediate-Mass Single Stars", doi="10.1017/pasa.2014.21", arxiv="1405.0062", bibcode="2014PASA...31...30K", role="orientation,established,debate", boundary="AGB and low/intermediate-mass single-star yields; contributions depend on initial mass, metallicity, mixing and mass loss."),
    dict(key="Vincenzo2016", authors="Vincenzo", year=2016, title="Nitrogen and oxygen abundances in the Local Universe", doi="10.1093/mnras/stw532", arxiv="1603.00460", bibcode="2016MNRAS.458.3466V", role="established,measurement,debate", boundary="Local N/O-O/H compilation and models; plateau level and transition depend on samples, calibrations and yields."),
    dict(key="Curti2020", authors="Curti", year=2020, title="The mass-metallicity and the fundamental metallicity relation revisited on a fully Te-based abundance scale for galaxies", doi="10.1093/mnras/stz2910", arxiv="1910.00597", bibcode="2020MNRAS.491..944C", role="established,measurement,caveat", boundary="Local stacked direct-method abundance scale and fitted FMR; do not export its zero point or scatter to other diagnostics/redshifts."),
    dict(key="Cameron2023", authors="Cameron", year=2023, title="Nitrogen enhancements 440 Myr after the big bang", doi="10.1093/mnras/stad1579", arxiv="2302.10142", bibcode="2023MNRAS.523.3516C", role="debate,caveat", boundary="GN-z11 case study with competing dense-cluster/TDE/source interpretations; not a clean non-AGN population-wide enrichment measurement."),
    dict(key="Greener2022", authors="Greener", year=2022, title="SDSS-IV MaNGA: the chemical co-evolution of gas and stars in spiral galaxies", doi="10.1093/mnras/stac2355", arxiv="2208.09008", bibcode="2022MNRAS.516.1275G", role="established,caveat", boundary="MaNGA spiral-galaxy gas versus stellar metallicity analysis; retain its sample, spectral-fitting and calibration limits."),
    dict(key="Belfiore2017", authors="Belfiore", year=2017, title="SDSS IV MaNGA - metallicity and nitrogen abundance gradients in local galaxies", doi="10.1093/mnras/stx789", arxiv="1703.03813", bibcode="2017MNRAS.469..151B", role="established,caveat", boundary="Local MaNGA star-forming disks and selected line diagnostics; gas-phase gradients only."),
    dict(key="SellwoodBinney2002", authors="Sellwood", year=2002, title="Radial mixing in galactic discs", doi="10.1046/j.1365-8711.2002.05806.x", arxiv="astro-ph/0203510", bibcode="2002MNRAS.336..785S", role="theory,established", boundary="Dynamical mechanism for stellar radial migration; does not by itself measure a universal migration amplitude or gas gradient."),
    dict(key="Stott2014", authors="Stott", year=2014, title="A relationship between specific star formation rate and metallicity gradient within z approximately 1 galaxies from KMOS-HiZELS", doi="10.1093/mnras/stu1343", arxiv="1407.1047", bibcode="2014MNRAS.443.2695S", role="debate,caveat", boundary="Small z~1 KMOS-HiZELS sample; gradient-sSFR association is not universal and is sensitive to resolution and calibration."),
    dict(key="Cowan1991", authors="Cowan", year=1991, title="The R-process and nucleochronology", doi="10.1016/0370-1573(91)90070-3", arxiv=None, bibcode="1991PhR...208..267C", role="orientation", boundary="Historical r-process review; not evidence that one astrophysical site dominates modern galactic r-process enrichment."),
    dict(key="Nomoto2013", authors="Nomoto", year=2013, title="Nucleosynthesis in Stars and the Chemical Enrichment of Galaxies", doi="10.1146/annurev-astro-082812-140956", arxiv=None, bibcode="2013ARA&A..51..457N", role="orientation,established,debate", boundary="Review of massive-star and supernova yields; yield tables remain model-, mass- and metallicity-dependent."),
    dict(key="MaiolinoMannucci2019", authors="Maiolino", year=2019, title="De re metallica: the cosmic chemical evolution of galaxies", doi="10.1007/s00159-018-0112-2", arxiv="1811.09642", bibcode="2019A&ARv..27....3M", role="orientation", boundary="Broad review used for scope and synthesis, not as sole support for narrow numerical claims."),
    dict(key="Matteucci2021", authors="Matteucci", year=2021, title="Modelling the chemical evolution of the Milky Way", doi="10.1007/s00159-021-00133-8", arxiv="2106.13145", bibcode="2021A&ARv..29....5M", role="orientation,established,debate", boundary="Milky-Way-focused review of infall, abundance ratios and chemical models; avoid universalizing to all galaxy populations."),
    dict(key="Weinberg2017", authors="Weinberg", year=2017, title="Equilibrium and Sudden Events in Chemical Evolution", doi="10.3847/1538-4357/837/2/183", arxiv="1604.07435", bibcode="2017ApJ...837..183W", role="theory,debate", boundary="One-zone analytic solutions under explicit assumptions; useful for causal diagnostics, not direct flow measurements."),
    dict(key="Sanchez2014", authors="Sanchez", year=2014, title="A characteristic oxygen abundance gradient in galaxy disks unveiled with CALIFA", doi="10.1051/0004-6361/201322343", arxiv="1311.7052", bibcode="2014A&A...563A..49S", role="established,measurement,caveat", boundary="Non-interacting CALIFA disks over 0.3-2 effective radii and the adopted abundance diagnostic; not all galaxies or radii."),
    dict(key="Wuyts2016", authors="Wuyts", year=2016, title="The evolution of metallicity and metallicity gradients from z=2.7-0.6 with KMOS3D", doi="10.3847/0004-637X/827/1/74", arxiv="1603.01139", bibcode="2016ApJ...827...74W", role="measurement,debate,caveat", boundary="Seeing-limited KMOS3D sample using NII/Halpha; beam-smearing recovery is geometry-dependent."),
    dict(key="Peeples2014", authors="Peeples", year=2014, title="A Budget and Accounting of Metals at z~0: Results from the COS-Halos Survey", doi="10.1088/0004-637X/786/1/54", arxiv="1310.2253", bibcode="2014ApJ...786...54P", role="established,measurement", boundary="z~0 star-forming systems and COS-Halos accounting assumptions; metal census depends on ionization and unobserved phases."),
    dict(key="Thomas2005", authors="Thomas", year=2005, title="The Epochs of Early-Type Galaxy Formation as a Function of Environment", doi="10.1086/426932", arxiv="astro-ph/0410209", bibcode="2005ApJ...621..673T", role="established,debate", boundary="Integrated stellar populations of local early-type galaxies under population-synthesis and IMF assumptions; alpha/Fe is not a pure clock."),
    dict(key="JohnsonWeinberg2020", authors="Johnson", year=2020, title="The impact of starbursts on element abundance ratios", doi="10.1093/mnras/staa2431", arxiv="1911.02598", bibcode="2020MNRAS.498.1364J", role="theory,debate", boundary="One-zone model predictions for burst signatures; not a direct universal abundance-to-timescale inversion."),
    dict(key="Chiappini1997", authors="Chiappini", year=1997, title="The Chemical Evolution of the Galaxy: The Two-Infall Model", doi="10.1086/303726", arxiv="astro-ph/9609199", bibcode="1997ApJ...477..765C", role="theory,debate", boundary="Milky Way two-infall model; demonstrates one solution family to disk abundance distributions, not unique proof of two discrete infalls."),
    dict(key="Henry2000", authors="Henry", year=2000, title="On the Cosmic Origins of Carbon and Nitrogen", doi="10.1086/309471", arxiv="astro-ph/0004299", bibcode="2000ApJ...541..660H", role="orientation,established,debate", boundary="Chemical-evolution synthesis for C and N production sites; yield assignments are model-dependent and have evolved."),
    dict(key="Sanders2021", authors="Sanders", year=2021, title="The MOSDEF Survey: The Evolution of the Mass-Metallicity Relation from z=0 to z~3.3", doi="10.3847/1538-4357/abf4c1", arxiv="2009.07292", bibcode="2021ApJ...914...19S", role="established,measurement,caveat", boundary="MOSDEF and local comparison with redshift-appropriate calibrations; process framing only here, not a duplicate Area-1 MZR entry."),
    dict(key="PerouxHowk2020", authors="Peroux", year=2020, title="The Cosmic Baryon and Metal Cycles", doi="10.1146/annurev-astro-021820-120014", arxiv="2011.01935", bibcode="2020ARA&A..58..363P", role="orientation,established,debate", boundary="Review of baryon and metal cycling; distinguishes measured reservoirs from model-dependent flow rates."),
    dict(key="KewleyEllison2008", authors="Kewley", year=2008, title="Metallicity Calibrations and the Mass-Metallicity Relation for Star-forming Galaxies", doi="10.1086/587500", arxiv="0801.1849", bibcode="2008ApJ...681.1183K", role="measurement,caveat", boundary="Comparison of local strong-line calibrations; its up-to-0.7 dex spread is not the uncertainty of every individual modern diagnostic."),
]

MANUAL_ADS_PASS = {
    "Curti2020": "Exact public ADS URL returned Curti, 2020, bibcode 2020MNRAS.491..944C.",
    "SellwoodBinney2002": "Exact public ADS URL returned Radial mixing in galactic discs, Sellwood, 2002.",
    "Nomoto2013": "Crossref DOI identity plus independent bibliographic results reconcile to bibcode 2013ARA&A..51..457N.",
    "PerouxHowk2020": "Exact public ADS URL returned The Cosmic Baryon and Metal Cycles, Peroux & Howk, 2020.",
    "KewleyEllison2008": "Exact public SciX/ADS bibcode result returned the matching title and arXiv 0801.1849.",
}


def norm(value):
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower())


def crossref(doi):
    request = urllib.request.Request(
        "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""),
        headers={"User-Agent": "NebulaMind-CHEM-curation/1.0 (mailto:research@example.invalid)"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)["message"]


def arxiv(arxiv_id):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": arxiv_id})
    with urllib.request.urlopen(url, timeout=30) as response:
        root = ET.fromstring(response.read())
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entry = root.find("a:entry", ns)
    if entry is None:
        raise ValueError("arXiv returned no entry")
    return {
        "title": " ".join(entry.findtext("a:title", default="", namespaces=ns).split()),
        "first_author": entry.findtext("a:author/a:name", default="", namespaces=ns),
        "published": entry.findtext("a:published", default="", namespaces=ns)[:4],
        "id": entry.findtext("a:id", default="", namespaces=ns),
    }

public = json.loads(PUBLIC_ADS.read_text())
public_by_key = {row["key"]: row for row in public["rows"]}
rows = []
for source in SOURCES:
    checks = {}
    evidence = {}
    public_row = public_by_key.get(source["key"])
    public_pass = bool(public_row and public_row["status"] == "PASS") or source["key"] in MANUAL_ADS_PASS
    checks["public_ads_identity"] = public_pass
    evidence["public_ads"] = MANUAL_ADS_PASS.get(source["key"], (public_row or {}).get("matching_results", [])[:1])
    if source["doi"]:
        try:
            data = crossref(source["doi"])
            first = ((data.get("author") or [{}])[0].get("family") or "")
            title = (data.get("title") or [""])[0]
            checks["crossref_doi_resolves"] = norm(data.get("DOI", "")) == norm(source["doi"])
            checks["crossref_author"] = norm(source["authors"]) in norm(first) or norm(first) in norm(source["authors"])
            expected_words = [word for word in re.findall(r"[A-Za-z]+", source["title"]) if len(word) >= 6]
            checks["crossref_title"] = sum(norm(word) in norm(title) for word in expected_words) >= max(1, min(3, len(expected_words)))
            evidence["crossref"] = {"doi": data.get("DOI"), "title": title, "first_author": first}
        except Exception as exc:
            checks["crossref_doi_resolves"] = False
            checks["crossref_author"] = False
            checks["crossref_title"] = False
            evidence["crossref_error"] = f"{type(exc).__name__}: {exc}"
    if source["arxiv"]:
        try:
            data = arxiv(source["arxiv"])
            checks["arxiv_resolves"] = norm(source["arxiv"].replace("astro-ph/", "")) in norm(data["id"])
            checks["arxiv_author"] = norm(source["authors"]) in norm(data["first_author"])
            evidence["arxiv"] = data
        except Exception as exc:
            checks["arxiv_resolves"] = False
            checks["arxiv_author"] = False
            evidence["arxiv_error"] = f"{type(exc).__name__}: {exc}"
    status = "PASS" if all(checks.values()) else "FAIL"
    rows.append({"status": status, "source": source, "checks": checks, "evidence": evidence})
    time.sleep(0.15)

summary = {
    "status": "PASS" if all(row["status"] == "PASS" for row in rows) else "HOLD",
    "method": "Composite identity reconciliation using public exact-bibcode ADS/SciX search, Crossref DOI metadata, and arXiv metadata. ADS API tokens were unavailable (HTTP 401), so no ADS API claims are made.",
    "source_count": len(rows),
    "pass_count": sum(row["status"] == "PASS" for row in rows),
    "fail_count": sum(row["status"] == "FAIL" for row in rows),
    "rows": rows,
}
OUT.write_text(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
print(json.dumps({key: summary[key] for key in ("status", "source_count", "pass_count", "fail_count")}, sort_keys=True))
for row in rows:
    if row["status"] == "FAIL":
        print(json.dumps({"key": row["source"]["key"], "checks": row["checks"], "evidence": row["evidence"]}, ensure_ascii=False, sort_keys=True))
raise SystemExit(0 if summary["status"] == "PASS" else 2)
