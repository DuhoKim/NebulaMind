import { notFound } from "next/navigation";
import SurveyDetailClient from "./SurveyDetailClient";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

type Props = { params: Promise<{ slug: string }> };

async function surveyExists(slug: string): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE}/api/surveys/${slug}`, { next: { revalidate: 3600 } });
    return res.ok;
  } catch {
    return false;
  }
}

export default async function SurveyDetailPage({ params }: Props) {
  const { slug } = await params;
  if (!(await surveyExists(slug))) notFound();
  return <SurveyDetailClient />;
}
