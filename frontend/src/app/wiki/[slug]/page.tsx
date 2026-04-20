import type { Metadata } from "next";
import WikiPageClient from "./WikiPageClient";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

type Props = {
  params: Promise<{ slug: string }>;
};

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  try {
    const res = await fetch(`${API_BASE}/api/pages/${slug}`, {
      next: { revalidate: 3600 },
    });
    if (!res.ok) throw new Error("not found");
    const page = await res.json();
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
      },
      twitter: {
        card: "summary",
        title: `${page.title} — NebulaMind`,
        description,
      },
      alternates: {
        canonical: `https://nebulamind.net/wiki/${slug}`,
      },
    };
  } catch {
    return {
      title: "Wiki — NebulaMind",
      description: "Explore astronomy topics on NebulaMind.",
    };
  }
}

export default function WikiPageRoute() {
  return <WikiPageClient />;
}
