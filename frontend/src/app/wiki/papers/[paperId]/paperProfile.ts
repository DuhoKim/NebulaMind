export type PaperProfileStatus = "needs_adjudication" | "needs_source" | "ready_to_review";
export type PaperProfileTone = "support" | "counter" | "neutral";

export interface PaperProfilePaper {
  evidence_id?: number | null;
  arxiv_id?: string | null;
  doi?: string | null;
  url?: string | null;
  title?: string | null;
  authors?: string[] | string | null;
  year?: number | string | null;
  summary?: string | null;
  author_year_key?: string | null;
}

export interface PaperProfileClaimPayload {
  claim_id?: number | null;
  claim_text?: string | null;
  section?: string | null;
  trust_level?: string | null;
  evidence_id?: number | null;
  stance?: string | null;
  status?: string | null;
  tone?: PaperProfileTone | string | null;
  href?: string | null;
  votes_agree?: number | null;
  votes_disagree?: number | null;
}

export interface PaperProfilePagePayload {
  page_id?: number | null;
  slug: string;
  title: string;
  href?: string | null;
  claim_count?: number | null;
  evidence_count?: number | null;
  support_count?: number | null;
  counter_count?: number | null;
  neutral_count?: number | null;
  claims?: PaperProfileClaimPayload[] | null;
}

export interface PaperProfilePayload {
  schema_version: "paper_profile.v1" | string;
  paper_id?: string | null;
  requested_paper_id?: string | null;
  paper?: PaperProfilePaper | null;
  page_count?: number | null;
  claim_count?: number | null;
  evidence_count?: number | null;
  tone_counts?: Record<string, number> | null;
  trust_counts?: Record<string, number> | null;
  vote_counts?: Record<string, number> | null;
  source_gap_count?: number | null;
  triage_status?: PaperProfileStatus | string | null;
  profile_summary?: string | null;
  page_limit?: number | null;
  page_result_count?: number | null;
  pages_truncated?: boolean | null;
  scope?: { label?: string | null; caveat?: string | null } | null;
  directory_href?: string | null;
  pages?: PaperProfilePagePayload[] | null;
}

export interface PaperProfileClaim extends PaperProfileClaimPayload {
  claim_id: number;
  claimText: string;
  tone: PaperProfileTone;
  toneLabel: string;
  trustLabel: string;
  href: string;
  votesAgree: number;
  votesDisagree: number;
  accessibleSummary: string;
}

export interface PaperProfilePage extends PaperProfilePagePayload {
  slug: string;
  title: string;
  href: string;
  claim_count: number;
  evidence_count: number;
  support_count: number;
  counter_count: number;
  neutral_count: number;
  claims: PaperProfileClaim[];
  accessibleSummary: string;
}

export interface PaperProfileDeck {
  hasProfile: boolean;
  paperId: string;
  paperLabel: string;
  title: string;
  summaryText: string;
  externalHref: string | null;
  directoryHref: string;
  status: PaperProfileStatus;
  statusLabel: string;
  pageCount: number;
  claimCount: number;
  evidenceCount: number;
  counterCount: number;
  supportCount: number;
  neutralCount: number;
  sourceGapCount: number;
  voteAgreeCount: number;
  voteDisagreeCount: number;
  summary: string;
  scopeCaveat: string;
  truncationDisclosure: string | null;
  emptyMessage: string;
  pages: PaperProfilePage[];
}

function cleanText(value?: string | number | null): string {
  return String(value ?? "").replace(/\s+/g, " ").trim();
}

function numberValue(value: unknown): number {
  const n = Number(value ?? 0);
  return Number.isFinite(n) ? n : 0;
}

function plural(count: number, singular: string, pluralForm = `${singular}s`): string {
  return `${count.toLocaleString()} ${count === 1 ? singular : pluralForm}`;
}

function firstAuthor(authors?: string[] | string | null): string {
  if (!authors) return "Paper";
  const list = Array.isArray(authors) ? authors : String(authors).split(/[;,]/);
  const first = cleanText(list[0]);
  if (!first) return "Paper";
  const parts = first.split(/\s+/).filter(Boolean);
  return parts[parts.length - 1] || first;
}

function paperLabel(paper?: PaperProfilePaper | null): string {
  const explicit = cleanText(paper?.author_year_key);
  if (explicit) return explicit;
  const title = cleanText(paper?.title);
  const arxivId = cleanText(paper?.arxiv_id);
  const year = cleanText(paper?.year);
  if (year) return `${firstAuthor(paper?.authors)}${year}`;
  return title || arxivId || "Paper profile";
}

function statusLabel(status: PaperProfileStatus): string {
  if (status === "needs_adjudication") return "Needs adjudication";
  if (status === "needs_source") return "Needs source";
  return "Ready to review";
}

function toneLabel(tone: PaperProfileTone): string {
  if (tone === "counter") return "Countering";
  if (tone === "support") return "Supporting";
  return "Neutral";
}

function normalizeTone(input?: string | null): PaperProfileTone {
  const value = cleanText(input).toLowerCase();
  if (/counter|contradict|oppose|against|refut|weak/.test(value)) return "counter";
  if (/support|agree|for|confirm|entail|strengthen/.test(value)) return "support";
  return "neutral";
}

export function encodePaperProfileId(paper?: PaperProfilePaper | null): string {
  const arxivId = cleanText(paper?.arxiv_id).replace(/^arXiv:/i, "");
  if (arxivId) return `arxiv:${arxivId}`;
  const doi = cleanText(paper?.doi);
  if (doi) return `doi:${doi}`;
  const url = cleanText(paper?.url);
  if (url) return `url:${url}`;
  const evidenceId = numberValue(paper?.evidence_id);
  if (evidenceId > 0) return `evidence:${evidenceId}`;
  return "paper:unknown";
}

export function normalizePaperProfileStatus(input: { counterCount?: number; trustCounts?: Record<string, number> | null; hasStableIdentifier?: boolean | null; status?: string | null }): PaperProfileStatus {
  const explicit = cleanText(input.status).toLowerCase();
  if (explicit === "needs_adjudication" || explicit === "needs_source" || explicit === "ready_to_review") return explicit;
  const trustCounts = input.trustCounts || {};
  if (numberValue(input.counterCount) > 0) return "needs_adjudication";
  if (["challenged", "debated", "disputed", "contested"].some((level) => numberValue(trustCounts[level]) > 0)) return "needs_adjudication";
  if (input.hasStableIdentifier === false || numberValue(trustCounts.unverified) > 0) return "needs_source";
  return "ready_to_review";
}

export function buildPaperProfileDeck(payload: PaperProfilePayload | null | undefined): PaperProfileDeck {
  const isKnownSchema = payload?.schema_version === "paper_profile.v1";
  const paper = isKnownSchema ? payload?.paper || {} : {};
  const pagesPayload = isKnownSchema && Array.isArray(payload?.pages) ? payload.pages : [];
  const toneCounts = isKnownSchema ? payload?.tone_counts || {} : {};
  const trustCounts = isKnownSchema ? payload?.trust_counts || {} : {};
  const voteCounts = isKnownSchema ? payload?.vote_counts || {} : {};
  const paperId = cleanText(payload?.paper_id) || encodePaperProfileId(paper);
  const title = cleanText(paper.title) || paperLabel(paper);
  const arxivId = cleanText(paper.arxiv_id);
  const externalHref = cleanText(paper.url) || (arxivId ? `https://arxiv.org/abs/${arxivId}` : null);
  const counterCount = numberValue(toneCounts.counter);
  const supportCount = numberValue(toneCounts.support);
  const neutralCount = numberValue(toneCounts.neutral);
  const status = normalizePaperProfileStatus({
    status: payload?.triage_status,
    counterCount,
    trustCounts,
    hasStableIdentifier: Boolean(arxivId || cleanText(paper.doi) || externalHref),
  });
  const pageCount = numberValue(payload?.page_count || pagesPayload.length);
  const claimCount = numberValue(payload?.claim_count || pagesPayload.reduce((sum, page) => sum + numberValue(page.claim_count), 0));
  const evidenceCount = numberValue(payload?.evidence_count);
  const sourceGapCount = numberValue(payload?.source_gap_count);
  const pages = pagesPayload.map((page) => {
    const pageHref = cleanText(page.href) || `/wiki/${cleanText(page.slug)}`;
    const pageTitle = cleanText(page.title) || cleanText(page.slug) || "Wiki page";
    const claims = (Array.isArray(page.claims) ? page.claims : []).map((claim) => {
      const tone = normalizeTone(claim.tone || claim.stance);
      const trustLabel = cleanText(claim.trust_level) || "unverified";
      const claimText = cleanText(claim.claim_text) || "Untitled claim";
      const claimId = numberValue(claim.claim_id);
      const href = cleanText(claim.href) || `${pageHref}#claim-${claimId}`;
      return {
        ...claim,
        claim_id: claimId,
        claimText,
        tone,
        toneLabel: toneLabel(tone),
        trustLabel,
        href,
        votesAgree: numberValue(claim.votes_agree),
        votesDisagree: numberValue(claim.votes_disagree),
        accessibleSummary: `${pageTitle}: ${toneLabel(tone)} evidence for ${trustLabel} claim. ${claimText}`,
      } satisfies PaperProfileClaim;
    }).sort((a, b) => (a.tone === "counter" ? 0 : 1) - (b.tone === "counter" ? 0 : 1) || b.votesDisagree - a.votesDisagree || a.claim_id - b.claim_id);
    return {
      ...page,
      slug: cleanText(page.slug),
      title: pageTitle,
      href: pageHref,
      claim_count: numberValue(page.claim_count || claims.length),
      evidence_count: numberValue(page.evidence_count),
      support_count: numberValue(page.support_count),
      counter_count: numberValue(page.counter_count),
      neutral_count: numberValue(page.neutral_count),
      claims,
      accessibleSummary: `${pageTitle}: ${numberValue(page.claim_count || claims.length)} claims, ${numberValue(page.counter_count)} countering, ${numberValue(page.evidence_count)} evidence rows.`,
    } satisfies PaperProfilePage;
  }).sort((a, b) => b.counter_count - a.counter_count || b.claim_count - a.claim_count || a.title.localeCompare(b.title));
  const hasProfile = isKnownSchema && pages.length > 0;
  const scopeCaveat = cleanText(payload?.scope?.caveat) || "Across indexed wiki evidence rows; this is not a final verdict. No labels are written.";
  const summary = cleanText(payload?.profile_summary) || `${plural(pageCount, "page")} · ${plural(claimCount, "claim")} · ${counterCount.toLocaleString()} countering`;
  const visiblePageCount = numberValue(payload?.page_result_count || pages.length);
  const truncationDisclosure = payload?.pages_truncated || pageCount > visiblePageCount
    ? `Showing ${visiblePageCount.toLocaleString()} of ${pageCount.toLocaleString()} page footprints for review safety; this is not a final verdict.`
    : null;

  return {
    hasProfile,
    paperId,
    paperLabel: paperLabel(paper),
    title,
    summaryText: cleanText(paper.summary),
    externalHref,
    directoryHref: cleanText(payload?.directory_href) || "/wiki/papers",
    status,
    statusLabel: statusLabel(status),
    pageCount,
    claimCount,
    evidenceCount,
    counterCount,
    supportCount,
    neutralCount,
    sourceGapCount,
    voteAgreeCount: numberValue(voteCounts.agree),
    voteDisagreeCount: numberValue(voteCounts.disagree),
    summary,
    scopeCaveat,
    truncationDisclosure,
    emptyMessage: "No paper profile footprint is available for this paper yet.",
    pages,
  };
}
