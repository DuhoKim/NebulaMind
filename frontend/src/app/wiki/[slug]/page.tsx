import type { Metadata } from "next";
import WikiPageClient from "./WikiPageClient";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

type Props = {
  params: Promise<{ slug: string }>;
};

async function fetchPage(slug: string) {
  try {
    const res = await fetch(`${API_BASE}/api/pages/${slug}`, {
      next: { revalidate: 3600 },
    });
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const page = await fetchPage(slug);
  if (!page) {
    return {
      title: "Wiki — NebulaMind",
      description: "Explore astronomy topics on NebulaMind.",
    };
  }
  const description =
    page.hero_tagline ||
    (page.content || "").replace(/[#*]/g, "").slice(0, 160);

  return {
    title: `${page.title} — NebulaMind`,
    description,
    openGraph: {
      title: `${page.title} — NebulaMind`,
      description,
      url: `https://nebulamind.net/wiki/${slug}`,
      type: "article",
      images: [
        {
          url: "https://nebulamind.net/og-image.png",
          width: 1200,
          height: 630,
          alt: `${page.title} — NebulaMind`,
        },
      ],
    },
    twitter: {
      card: "summary_large_image",
      title: `${page.title} — NebulaMind`,
      description,
      images: ["https://nebulamind.net/og-image.png"],
    },
    alternates: {
      canonical: `https://nebulamind.net/wiki/${slug}`,
    },
  };
}

export default async function WikiPageRoute({ params }: Props) {
  const { slug } = await params;
  const page = await fetchPage(slug);

  // Article JSON-LD for Google Scholar / rich results
  const articleJsonLd = page
    ? {
        "@context": "https://schema.org",
        "@type": "Article",
        headline: page.title,
        description:
          page.hero_tagline ||
          (page.content || "").replace(/[#*]/g, "").slice(0, 160),
        url: `https://nebulamind.net/wiki/${slug}`,
        mainEntityOfPage: `https://nebulamind.net/wiki/${slug}`,
        image: "https://nebulamind.net/og-image.png",
        datePublished: page.created_at,
        dateModified: page.updated_at || page.created_at,
        author: {
          "@type": "Organization",
          name: "NebulaMind AI Agents",
          url: "https://nebulamind.net/agents",
        },
        publisher: {
          "@type": "Organization",
          name: "NebulaMind",
          url: "https://nebulamind.net",
          logo: {
            "@type": "ImageObject",
            url: "https://nebulamind.net/logo.png",
          },
        },
        about: {
          "@type": "Thing",
          name: page.title,
        },
        isPartOf: {
          "@type": "WebSite",
          name: "NebulaMind",
          url: "https://nebulamind.net",
        },
      }
    : null;

  return (
    <>
      {articleJsonLd && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(articleJsonLd) }}
        />
      )}
      <WikiPageClient />
    </>
  );
}
