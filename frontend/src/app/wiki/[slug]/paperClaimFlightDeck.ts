export interface PaperClaimCitationLike {
  evidence_id?: number | string | null;
  author_year_key?: string | null;
  title?: string | null;
  authors?: string[] | string | null;
  year?: number | string | null;
  doi?: string | null;
  arxiv_id?: string | null;
  url?: string | null;
  summary?: string | null;
  abstract?: string | null;
  journal_ref?: string | null;
}

export interface PaperClaimLike {
  id?: number | string | null;
  text?: string | null;
  trust_level?: string | null;
  evidence_count?: number | null;
  con_count?: number | null;
  section?: string | null;
}

export interface PaperClaimEdge {
  evidenceId: number;
  claimId: number;
}

export interface PaperClaimLink {
  claimId: number;
  claimText: string;
  trustLevel: string;
  sectionLabel: string;
  href: string;
  counterPressure: boolean;
}

export interface PaperClaimFlightDeckItem {
  evidenceId: number;
  paperLabel: string;
  title: string;
  byline: string;
  locator: string;
  summary: string;
  externalHref: string | null;
  sourceIndexHref: string | null;
  claimCount: number;
  counterPressureClaims: number;
  rankScore: number;
  rankLabel: string;
  claimLinks: PaperClaimLink[];
}

export interface PaperClaimFlightDeck {
  totalPapers: number;
  linkedPapers: number;
  unmappedPapers: number;
  linkedClaims: number;
  hasFlightDeck: boolean;
  headline: string;
  summary: string;
  items: PaperClaimFlightDeckItem[];
}

function cleanText(value?: string | number | null): string {
  return String(value ?? "").replace(/\s+/g, " ").trim();
}

function parseIds(raw: string): number[] {
  return String(raw || "")
    .split(",")
    .map((part) => Number(part.trim()))
    .filter((value) => Number.isFinite(value) && value > 0)
    .map((value) => Math.floor(value));
}

function pluralCount(count: number, singular: string, plural = `${singular}s`): string {
  return `${count.toLocaleString()} ${count === 1 ? singular : plural}`;
}

function splitAuthors(authors?: string[] | string | null): string[] {
  if (!authors) return [];
  const raw = Array.isArray(authors) ? authors : [authors];
  if (raw.length === 1 && typeof raw[0] === "string") {
    const value = raw[0];
    if (value.includes(";")) return value.split(";").map((s) => s.trim()).filter(Boolean);
    if (value.includes(",")) return value.split(",").map((s) => s.trim()).filter(Boolean);
  }
  return raw.map((item) => String(item).trim()).filter(Boolean);
}

function formatAuthors(authors?: string[] | string | null): string {
  const list = splitAuthors(authors);
  if (list.length === 0) return "Source metadata pending";
  if (list[0]?.toLowerCase().includes("collaboration")) return list[0];
  if (list.length <= 2) return list.join(", ");
  return `${list.slice(0, 2).join(", ")} et al.`;
}

function formatByline(citation: PaperClaimCitationLike): string {
  const parts = [formatAuthors(citation.authors)];
  const year = cleanText(citation.year);
  if (year) parts.push(year);
  const journal = cleanText(citation.journal_ref);
  if (journal) parts.push(journal);
  return parts.filter(Boolean).join(" · ") || "Source metadata pending";
}

function formatLocator(citation: PaperClaimCitationLike): string {
  const parts: string[] = [];
  const arxiv = cleanText(citation.arxiv_id);
  if (arxiv) parts.push(`arXiv:${arxiv}`);
  const doi = cleanText(citation.doi);
  if (doi) parts.push(`DOI:${doi}`);
  if (parts.length > 0) return parts.join(" · ");
  return cleanText(citation.url) ? "External source link available" : "External source link unavailable";
}

function formatSummary(citation: PaperClaimCitationLike): string {
  const value = cleanText(citation.summary || citation.abstract);
  if (!value) return "No abstract or summary has been published for this source yet.";
  return value.length > 190 ? `${value.slice(0, 189)}…` : value;
}

function citationId(citation: PaperClaimCitationLike): number | null {
  const value = Number(citation.evidence_id);
  return Number.isFinite(value) && value > 0 ? Math.floor(value) : null;
}

function sectionLabel(section: any): string {
  const label = cleanText(section?.title ?? section?.heading ?? section?.name ?? section?.section);
  return label || "Claim layer";
}

function claimIdNumber(raw: PaperClaimLike["id"]): number | null {
  const value = Number(raw);
  return Number.isFinite(value) && value > 0 ? Math.floor(value) : null;
}

function flattenClaims(pageClaims: any): Array<PaperClaimLike & { sectionLabel: string }> {
  const output: Array<PaperClaimLike & { sectionLabel: string }> = [];
  const seen = new Set<number>();
  const pushClaim = (claim: PaperClaimLike, label: string) => {
    const id = claimIdNumber(claim?.id);
    if (id == null || seen.has(id)) return;
    seen.add(id);
    output.push({ ...claim, sectionLabel: label });
  };

  if (Array.isArray(pageClaims)) {
    for (const claim of pageClaims) pushClaim(claim, "Claim layer");
  }

  for (const section of pageClaims?.sections ?? []) {
    const label = sectionLabel(section);
    for (const claim of section?.claims ?? []) pushClaim(claim, label);
  }

  return output;
}

function normalizeRenderedClaimIds(renderedClaimIds?: Iterable<number | string> | null): Set<number> | null {
  if (!renderedClaimIds) return null;
  const ids = new Set<number>();
  for (const raw of renderedClaimIds) {
    const id = Number(raw);
    if (Number.isFinite(id) && id > 0) ids.add(Math.floor(id));
  }
  return ids.size > 0 ? ids : null;
}

function claimHasCounterPressure(claim: PaperClaimLike): boolean {
  const counterCount = Number(claim.con_count || 0);
  if (Number.isFinite(counterCount) && counterCount > 0) return true;
  const trust = cleanText(claim.trust_level).toLowerCase();
  return trust === "challenged" || trust === "debated";
}

function claimText(claim: PaperClaimLike, fallbackId: number): string {
  return cleanText(claim.text) || `Claim ${fallbackId}`;
}

function pageSlugHref(pageSlug?: string | null): string | null {
  const slug = cleanText(pageSlug).replace(/^\/+|\/+$/g, "");
  return slug ? `/wiki/${encodeURIComponent(slug)}/sources` : null;
}

export function extractPaperClaimEdges(content?: string | null): PaperClaimEdge[] {
  const source = String(content || "");
  const edges: PaperClaimEdge[] = [];
  const seen = new Set<string>();
  const claimBlock = /<!--\s*claim:([\d,\s]+?)\s*-->([\s\S]*?)<!--\s*\/claim:([\d,\s]+?)\s*-->/g;
  let claimMatch: RegExpExecArray | null;

  while ((claimMatch = claimBlock.exec(source))) {
    const openClaimIds = parseIds(claimMatch[1]);
    const closeClaimIds = parseIds(claimMatch[3]);
    if (openClaimIds.join(",") !== closeClaimIds.join(",")) continue;
    const body = claimMatch[2] || "";
    const citePattern = /<!--\s*cite:([\d,\s]+?)\s*-->/g;
    let citeMatch: RegExpExecArray | null;
    while ((citeMatch = citePattern.exec(body))) {
      const evidenceIds = parseIds(citeMatch[1]);
      for (const evidenceId of evidenceIds) {
        for (const claimId of openClaimIds) {
          const key = `${evidenceId}:${claimId}`;
          if (seen.has(key)) continue;
          seen.add(key);
          edges.push({ evidenceId, claimId });
        }
      }
    }
  }

  return edges;
}

export function buildPaperClaimFlightDeck(
  content: string | null | undefined,
  citations: PaperClaimCitationLike[] | null | undefined,
  pageClaims: any,
  renderedClaimIds?: Iterable<number | string> | null,
  pageSlug?: string | null,
): PaperClaimFlightDeck {
  const citationList = Array.isArray(citations) ? citations : [];
  const rendered = normalizeRenderedClaimIds(renderedClaimIds);
  const claimMap = new Map<number, PaperClaimLike & { sectionLabel: string }>();
  for (const claim of flattenClaims(pageClaims)) {
    const id = claimIdNumber(claim.id);
    if (id == null) continue;
    if (rendered && !rendered.has(id)) continue;
    claimMap.set(id, claim);
  }

  const edgesByEvidence = new Map<number, Set<number>>();
  for (const edge of extractPaperClaimEdges(content)) {
    if (!claimMap.has(edge.claimId)) continue;
    if (!edgesByEvidence.has(edge.evidenceId)) edgesByEvidence.set(edge.evidenceId, new Set<number>());
    edgesByEvidence.get(edge.evidenceId)?.add(edge.claimId);
  }

  const sourceIndexHref = pageSlugHref(pageSlug);
  const linkedClaimIds = new Set<number>();
  const items: PaperClaimFlightDeckItem[] = [];

  for (const citation of citationList) {
    const evidenceId = citationId(citation);
    if (evidenceId == null) continue;
    const claimIds = [...(edgesByEvidence.get(evidenceId) ?? new Set<number>())]
      .filter((claimId) => claimMap.has(claimId))
      .sort((a, b) => a - b);
    if (claimIds.length === 0) continue;

    const claimLinks = claimIds.map((claimId) => {
      const claim = claimMap.get(claimId)!;
      linkedClaimIds.add(claimId);
      return {
        claimId,
        claimText: claimText(claim, claimId),
        trustLevel: cleanText(claim.trust_level).toLowerCase() || "unverified",
        sectionLabel: claim.sectionLabel,
        href: `#claim-${claimId}`,
        counterPressure: claimHasCounterPressure(claim),
      } satisfies PaperClaimLink;
    });
    const counterPressureClaims = claimLinks.filter((link) => link.counterPressure).length;
    const claimCount = claimLinks.length;
    const year = Number(citation.year);
    const rankScore = counterPressureClaims * 1000 + claimCount * 100 + (Number.isFinite(year) ? year / 10000 : 0);

    items.push({
      evidenceId,
      paperLabel: cleanText(citation.author_year_key) || `Evidence #${evidenceId}`,
      title: cleanText(citation.title) || "Untitled paper source",
      byline: formatByline(citation),
      locator: formatLocator(citation),
      summary: formatSummary(citation),
      externalHref: cleanText(citation.url) || null,
      sourceIndexHref,
      claimCount,
      counterPressureClaims,
      rankScore,
      rankLabel: `${pluralCount(claimCount, "claim link")} · ${counterPressureClaims.toLocaleString()} with counter pressure`,
      claimLinks,
    });
  }

  items.sort((a, b) =>
    b.counterPressureClaims - a.counterPressureClaims ||
    b.claimCount - a.claimCount ||
    b.rankScore - a.rankScore ||
    a.evidenceId - b.evidenceId,
  );

  const linkedPapers = items.length;
  const linkedClaims = linkedClaimIds.size;
  const unmappedPapers = Math.max(0, citationList.length - linkedPapers);
  return {
    totalPapers: citationList.length,
    linkedPapers,
    unmappedPapers,
    linkedClaims,
    hasFlightDeck: linkedPapers > 0,
    headline: linkedPapers > 0
      ? `${pluralCount(linkedPapers, "paper")} linked to ${pluralCount(linkedClaims, "visible claim")}`
      : "No paper-to-claim links mapped yet",
    summary: linkedPapers > 0
      ? "Paper-to-claim navigation ranked by linked visible claims and counter-pressure; this is not a final verdict about which claim is correct."
      : "Claim-scoped paper links will appear here once citations are mapped to visible claims.",
    items,
  };
}
